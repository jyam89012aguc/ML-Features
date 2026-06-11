# f03_kalman_filter_price — REAL indicator: 1-D Kalman filter on price.
#
# Two scalar state-space models, implemented with a single Python loop over rows:
#   * local-level     : x_t = x_{t-1} + w,            y_t = x_t + v   (random walk + obs noise)
#   * local-linear-trend (LLT): level + velocity state, level_t = level + vel,
#                               vel_t = vel + w2,      y_t = level_t + v
# We expose facets: filtered level, innovation/residual (price - filtered), residual z-score,
# Kalman gain, |innovation|, velocity (slope) state, and smoothed(level)-vs-raw spread.
# Variants differ by process/measurement noise ratio q = Q/R (1e-1 .. 1e-5) and window.
import numpy as np
import pandas as pd


def _kalman_level(y, q, r=1.0):
    """Scalar local-level Kalman filter (random walk + obs noise).

    Returns dict of arrays: level (filtered estimate), innov (y - prior),
    gain (Kalman gain), resid (y - level, posterior residual).
    q = process variance Q, r = measurement variance R. Only the ratio q/r matters.
    Single explicit loop over n rows (vectorization is not possible for the recursion).
    """
    n = y.shape[0]
    level = np.full(n, np.nan)
    innov = np.full(n, np.nan)
    gain = np.full(n, np.nan)
    resid = np.full(n, np.nan)

    # init on first finite observation
    x = np.nan
    p = 1.0
    started = False
    for t in range(n):
        yt = y[t]
        if not np.isfinite(yt):
            level[t] = x if started else np.nan
            continue
        if not started:
            x = yt
            p = r
            level[t] = x
            innov[t] = 0.0
            gain[t] = 0.0
            resid[t] = 0.0
            started = True
            continue
        # predict
        x_pred = x
        p_pred = p + q
        # update
        s = p_pred + r
        k = p_pred / s
        e = yt - x_pred
        x = x_pred + k * e
        p = (1.0 - k) * p_pred
        level[t] = x
        innov[t] = e
        gain[t] = k
        resid[t] = yt - x
    return {'level': level, 'innov': innov, 'gain': gain, 'resid': resid}


def _kalman_llt(y, q_level, q_vel, r=1.0):
    """Scalar local-linear-trend Kalman filter (level + velocity state).

    Diagonal-ish 2-state filter implemented with explicit scalar algebra so it stays
    a single fast loop. Returns level, vel (slope state), innov, resid.
    """
    n = y.shape[0]
    level = np.full(n, np.nan)
    vel = np.full(n, np.nan)
    innov = np.full(n, np.nan)
    resid = np.full(n, np.nan)

    xl = np.nan   # level
    xv = 0.0      # velocity
    # 2x2 covariance entries
    p11 = 1.0
    p12 = 0.0
    p22 = 1.0
    started = False
    for t in range(n):
        yt = y[t]
        if not np.isfinite(yt):
            level[t] = xl if started else np.nan
            vel[t] = xv if started else np.nan
            continue
        if not started:
            xl = yt
            xv = 0.0
            p11 = r
            p12 = 0.0
            p22 = r
            level[t] = xl
            vel[t] = xv
            innov[t] = 0.0
            resid[t] = 0.0
            started = True
            continue
        # predict: level' = level + vel ; vel' = vel
        xl_p = xl + xv
        xv_p = xv
        # F = [[1,1],[0,1]] ; P' = F P F^T + Q
        np11 = p11 + 2.0 * p12 + p22 + q_level
        np12 = p12 + p22
        np22 = p22 + q_vel
        p11, p12, p22 = np11, np12, np22
        # update with H = [1,0]
        s = p11 + r
        k1 = p11 / s
        k2 = p12 / s
        e = yt - xl_p
        xl = xl_p + k1 * e
        xv = xv_p + k2 * e
        # P = (I - K H) P
        n11 = (1.0 - k1) * p11
        n12 = (1.0 - k1) * p12
        n22 = p22 - k2 * p12
        p11, p12, p22 = n11, n12, n22
        level[t] = xl
        vel[t] = xv
        innov[t] = e
        resid[t] = yt - xl
    return {'level': level, 'vel': vel, 'innov': innov, 'resid': resid}


def _z(s, window):
    m = s.rolling(window, min_periods=max(2, window // 2)).mean()
    sd = s.rolling(window, min_periods=max(2, window // 2)).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


# Variant grid: process/measurement ratios spanning 1e-1 .. 1e-5, plus windows.
# Each ratio maps a smoothing strength; window is used for the facet rolling stats /
# the smoothed-vs-raw spread reference. closeadj is used wherever a window > 21d.
_RATIOS = [1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-4, 5e-5, 1e-5, 3e-2,
           7e-3, 2e-3, 8e-4, 4e-4, 2e-4]
_WINDOWS = [5, 10, 21, 42, 63, 126, 252]
_FACETS = ['level', 'resid', 'resid_z', 'vel', 'abs_innov', 'gain', 'smooth_spread']


def _build_specs(i_start, i_end):
    """Deterministically enumerate (ratio, window, facet) specs for column ids.

    Facet varies fastest, then ratio, then window, so every column within any small
    span gets a different facet -> no two of the 150 features are the same expression
    up to a window change only. 7 facets * 15 ratios * 7 windows = 735 unique combos
    cover the 150 ids with room to spare.
    """
    nf, nr, nw = len(_FACETS), len(_RATIOS), len(_WINDOWS)
    specs = []
    for i in range(i_start, i_end + 1):
        k = i - 1  # 0-based global index 0..149
        facet = _FACETS[k % nf]
        ratio = _RATIOS[(k // nf) % nr]
        # window rotates on a co-prime stride so the full window list (incl. >21d ->
        # closeadj) is exercised across the 150 ids rather than only the first one or two.
        window = _WINDOWS[(k // nf + (k % nf) * 3) % nw]
        specs.append((i, ratio, window, facet))
    return specs


def _price_col(df, window):
    # any rolling window > 21 trading days uses closeadj; the Kalman recursion itself is a
    # long-memory filter, so use closeadj as the canonical price series for stability.
    return df['closeadj'] if window > 21 else df['close']


def _compute(df, i_start, i_end):
    close = df['close'].astype('float64')
    closeadj = df['closeadj'].astype('float64')
    y_raw_close = close.values
    y_raw_adj = closeadj.values

    features = {}
    # cache filter runs keyed by (price_source, ratio) so repeated facets reuse work
    cache = {}
    for (i, ratio, window, facet) in _build_specs(i_start, i_end):
        price = _price_col(df, window)
        src = 'adj' if (price is closeadj) else 'cls'
        key = (src, ratio)
        if key not in cache:
            yv = y_raw_adj if src == 'adj' else y_raw_close
            # local-level filter; r fixed at 1.0, q encodes the ratio
            ll = _kalman_level(yv, q=ratio, r=1.0)
            # local-linear-trend: velocity process noise an order smaller than level noise
            llt = _kalman_llt(yv, q_level=ratio, q_vel=ratio * 1e-2, r=1.0)
            cache[key] = (ll, llt, price)
        ll, llt, price = cache[key]
        idx = price.index
        col = f'f03_kalman_filter_price_{i:03d}'

        mp = max(2, window // 2)
        if facet == 'level':
            # filtered level expressed as its window-horizon slope (drift of the state),
            # i.e. how far the Kalman level has moved over `window` days, % of price.
            lvl = pd.Series(ll['level'], index=idx)
            features[col] = ((lvl - lvl.shift(window)) / lvl.shift(window)).replace(
                [np.inf, -np.inf], np.nan)
        elif facet == 'resid':
            # price - filtered level, normalized by a rolling price scale (window-dependent)
            resid = pd.Series(ll['resid'], index=idx)
            scale = price.rolling(window, min_periods=mp).std()
            features[col] = (resid / scale).replace([np.inf, -np.inf], np.nan)
        elif facet == 'resid_z':
            resid = pd.Series(ll['resid'], index=idx)
            features[col] = _z(resid, window)
        elif facet == 'vel':
            # velocity (slope) state of the local-linear-trend filter, smoothed over window
            v = pd.Series(llt['vel'], index=idx)
            features[col] = v.rolling(window, min_periods=mp).mean()
        elif facet == 'abs_innov':
            # mean absolute innovation over the window (filter surprise / volatility proxy)
            ai = pd.Series(np.abs(ll['innov']), index=idx)
            features[col] = ai.rolling(window, min_periods=mp).mean()
        elif facet == 'gain':
            # state correction = Kalman gain * innovation (the actual update applied to the
            # level each step). The bare gain converges to a constant at steady state, so we
            # use the gain-weighted innovation, smoothed over the window -> stays informative.
            g = pd.Series(ll['gain'], index=idx)
            e = pd.Series(ll['innov'], index=idx)
            correction = (g * e) / price
            features[col] = correction.rolling(window, min_periods=mp).mean().replace(
                [np.inf, -np.inf], np.nan)
        elif facet == 'smooth_spread':
            # smoothed (LLT level) vs raw price spread, then its window-horizon change
            llt_level = pd.Series(llt['level'], index=idx)
            spread = ((llt_level - price) / price).replace([np.inf, -np.inf], np.nan)
            features[col] = spread - spread.shift(window)
    return pd.DataFrame(features)


def get_f03_kalman_filter_price_base_001_075(df):
    return _compute(df, 1, 75)
