# Real indicator: volume-weighted rate of change / momentum (features 076..150)
# Core: ROC(n) = closeadj.pct_change(n), weighted by relative volume (volume / SMA_volume).
# Windows > 21d use 'closeadj' for returns; raw 'volume' for weights; closeadj*volume = dollar-volume.
import numpy as np
import pandas as pd

WINDOWS = [5, 10, 21, 63, 126, 252]


def _ret_col(window):
    return 'close' if window <= 21 else 'closeadj'


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(price, n):
    return price.pct_change(n).replace([np.inf, -np.inf], np.nan)


def _relvol(volume, window):
    sv = volume.rolling(window).mean()
    return (volume / sv).replace([np.inf, -np.inf], np.nan)


def _vw_roc(df, n):
    price = df[_ret_col(n)]
    rv = _relvol(df['volume'], n)
    return (_roc(price, n) * rv).replace([np.inf, -np.inf], np.nan)


def _vw_momentum(df, n):
    price = df[_ret_col(n)]
    ret = price.pct_change().replace([np.inf, -np.inf], np.nan)
    rv = _relvol(df['volume'], n)
    return (ret * rv).rolling(n).sum()


def _dollar_vw_roc(df, n):
    price = df[_ret_col(n)]
    dv = df['closeadj'] * df['volume']
    sdv = dv.rolling(n).mean()
    rel = (dv / sdv).replace([np.inf, -np.inf], np.nan)
    return (_roc(price, n) * rel).replace([np.inf, -np.inf], np.nan)


def get_f27_volume_weighted_roc_base_076_150(df):
    features = {}
    f = {}

    for w in WINDOWS:
        ret_d = df[_ret_col(w)].pct_change().replace([np.inf, -np.inf], np.nan)
        rv = _relvol(df['volume'], w)
        vwroc = _vw_roc(df, w)
        roc = _roc(df[_ret_col(w)], w)

        # 1. EMA-smoothed vw-ROC (alternative smoothing facet)
        f[('vwroc_ema', w)] = vwroc.ewm(span=w, min_periods=w).mean()
        # 2. vw-momentum z-score
        f[('vwmom_z', w)] = _z(_vw_momentum(df, w), max(w, 21))
        # 3. dollar-vw-ROC z-score
        f[('dvroc_z', w)] = _z(_dollar_vw_roc(df, w), max(w, 21))
        # 4. relative-volume-confirmed ROC z-score (gated confirmation)
        conf = np.where(rv > 1.0, 1.0, 0.25)
        rvc = (roc * pd.Series(conf, index=roc.index)).replace([np.inf, -np.inf], np.nan)
        f[('rvconf_z', w)] = _z(rvc, max(w, 21))
        # 5. vw-ROC vs plain ROC ratio (divergence ratio)
        f[('vw_ratio', w)] = (vwroc / roc).replace([np.inf, -np.inf], np.nan).clip(-10, 10)
        # 6. vw-ROC regime/threshold distance from zero in std units
        f[('vwroc_regime', w)] = (vwroc / vwroc.rolling(max(w, 21)).std()).replace([np.inf, -np.inf], np.nan)
        # 7. volume-confirmed breakout strength (low-side, support test)
        price = df[_ret_col(w)]
        ll = price.rolling(w).min()
        bd = ((ll.shift(1) - price) / ll.shift(1)).replace([np.inf, -np.inf], np.nan)
        f[('vw_breakdn', w)] = (vwroc * (1 + bd.clip(lower=0))).replace([np.inf, -np.inf], np.nan)
        # 8. vw-momentum slope/delta
        f[('vwmom_d', w)] = _vw_momentum(df, w).diff(max(1, w // 3))
        # 9. interaction: vw-ROC * relative-volume (volume-confirmed acceleration)
        f[('vwroc_x_rv', w)] = (vwroc * rv).replace([np.inf, -np.inf], np.nan)
        # 10. dollar-vw-ROC vs plain ROC divergence
        f[('dv_div', w)] = (_dollar_vw_roc(df, w) - roc).replace([np.inf, -np.inf], np.nan)
        # 11. sign-streak of vw-momentum
        sign = np.sign(_vw_momentum(df, w))
        grp = (sign != sign.shift()).cumsum()
        f[('vwmom_streak', w)] = (sign * sign.groupby(grp).cumcount().add(1))
        # 12. vw-ROC percentile rank of momentum (long-window rank)
        f[('vwroc_rank2', w)] = vwroc.rolling(max(2 * w, 42)).rank(pct=True)

    # cross-window short-vs-long facets (distinct from file 1)
    spreads = {}
    pairs = [(5, 21), (10, 63), (21, 126)]
    for (s, l) in pairs:
        # ratio facet
        spreads[('ratio', s, l)] = (_vw_roc(df, s) / _vw_roc(df, l)).replace([np.inf, -np.inf], np.nan).clip(-10, 10)
        # momentum spread facet
        spreads[('mom', s, l)] = (_vw_momentum(df, s) - _vw_momentum(df, l)).replace([np.inf, -np.inf], np.nan)

    facet_order = ['vwroc_ema', 'vwmom_z', 'dvroc_z', 'rvconf_z', 'vw_ratio',
                   'vwroc_regime', 'vw_breakdn', 'vwmom_d', 'vwroc_x_rv', 'dv_div',
                   'vwmom_streak', 'vwroc_rank2']
    ordered = []
    for fac in facet_order:
        for w in WINDOWS:
            ordered.append(f[(fac, w)])
    # 12 * 6 = 72
    for (s, l) in pairs:
        ordered.append(spreads[('ratio', s, l)])
        ordered.append(spreads[('mom', s, l)])
    # +6 = 78 available, take first 75

    for k in range(75):
        features[f'f27_volume_weighted_roc_{76 + k:03d}'] = ordered[k]

    return pd.DataFrame(features)
