"""amihud_roll_kyle_liquidity d2 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Pastor-Stambaugh / LOT / FHT / Effective-Tick (Holden) / Abdi-Ranaldi / Hou-Mendel /
Glosten-Harris / Madhavan-Richardson-Roomans / Hasbrouck info-share / Liu LM /
Pollet / liquidity resilience / commonality / multi-measure composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _pastor_stambaugh_gamma(close, volume, n, min_periods=None):
    """Pastor-Stambaugh (2003) reversal coefficient: r_t+1 = a + b*r_t + gamma * sign(r_t) * dollar-vol_t.
    Per-window OLS, last-bar gamma. Returns rolling series (NaN at warmup)."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    r = _safe_log(close).diff()
    dv = (close * volume).fillna(0)
    sv = np.sign(r) * dv
    def _f_idx(idx_window):
        # rolling.apply gives a numpy array; we need the indices to align r and sv
        # We do per-window via rolling.cov / rolling.var instead. Implemented below directly.
        return np.nan
    # Direct PIT-clean implementation: rolling OLS of r_now on r_lag1 and sv_lag1
    r_lag = r.shift(1)
    sv_lag = sv.shift(1)
    # Use a simple per-window OLS via rolling.apply on a concatenated DataFrame
    df = pd.concat([r.rename('y'), r_lag.rename('x1'), sv_lag.rename('x2')], axis=1)
    out = pd.Series(np.nan, index=close.index)
    arr_y = df['y'].values; arr_x1 = df['x1'].values; arr_x2 = df['x2'].values
    N = len(close)
    for i in range(N):
        if i < min_periods - 1:
            continue
        start = max(0, i - n + 1)
        y_w = arr_y[start:i+1]; x1_w = arr_x1[start:i+1]; x2_w = arr_x2[start:i+1]
        mask = ~np.isnan(y_w) & ~np.isnan(x1_w) & ~np.isnan(x2_w)
        if mask.sum() < min_periods:
            continue
        y = y_w[mask]; x1 = x1_w[mask]; x2 = x2_w[mask]
        X = np.column_stack([np.ones(y.size), x1, x2])
        try:
            beta, *_ = np.linalg.lstsq(X, y, rcond=None)
            out.iloc[i] = float(beta[2])
        except Exception:
            continue
    return out


def _lot_zero_return_frac(close, n, min_periods=None, tol=1e-6):
    """Lesmond-Ogden-Trzcinka zero-return frequency."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    r = _safe_log(close).diff()
    zero = (r.abs() < tol).astype(float).where(r.notna(), np.nan)
    return zero.rolling(n, min_periods=min_periods).mean()


def _effective_tick_proxy(close, n, min_periods=None):
    """Holden (2009) Effective Tick: fraction of closes ending at coarser tick clusters.
    Proxy: weighted sum of cluster shares. Coarse cluster = closing price at multiples
    of $0.25 / $0.10 / $0.05 / $0.01 — heavier clusters imply larger effective spread."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    # Project to cents
    cents = (close * 100.0).round().astype(float)
    # Tick weights: $0.25 -> 0.20, $0.10 -> 0.10, $0.05 -> 0.05, $0.01 -> 0.01
    in_25 = ((cents % 25) == 0).astype(float)
    in_10 = (((cents % 10) == 0) & ((cents % 25) != 0)).astype(float)
    in_05 = (((cents % 5) == 0) & ((cents % 10) != 0) & ((cents % 25) != 0)).astype(float)
    in_01 = (((cents % 5) != 0)).astype(float)
    weighted = (in_25 * 0.20 + in_10 * 0.10 + in_05 * 0.05 + in_01 * 0.01)
    return weighted.rolling(n, min_periods=min_periods).mean()


def _abdi_ranaldi_spread(high, low, close, n, min_periods=None):
    """Abdi-Ranaldi (2017) 2-day high-low spread estimator.
    sigma_hat^2 = (4/n) * sum_t [(ln(H_t) - ln(C_t)) * (ln(C_t) - ln(L_t))]
    where H_t, L_t are 2-day high/low and C_t is midpoint of log-H and log-L on day t."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    lh = _safe_log(high); ll = _safe_log(low); lc = _safe_log(close)
    h2 = pd.concat([lh, lh.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([ll, ll.shift(1)], axis=1).min(axis=1)
    eta = (lh + ll) / 2.0
    term = (eta - lc) ** 2
    sigma_sq = 4.0 * term.rolling(n, min_periods=min_periods).mean()
    return 2.0 * sigma_sq.clip(lower=0).pow(0.5)


def _liu_lm(close, volume, n_days, min_periods=None):
    """Liu (2006) LM measure: (zero-return-day-count + 1/(n-day turnover)) * 21 / (n-month average turnover).
    Standardized for cross-stock comparison."""
    if min_periods is None:
        min_periods = max(n_days // 3, 2)
    r = _safe_log(close).diff()
    z = (r.abs() < 1e-6).astype(float).where(r.notna(), np.nan)
    z_count = z.rolling(n_days, min_periods=min_periods).sum()
    turn = volume.rolling(n_days, min_periods=min_periods).sum()
    # 1/turn for tiebreak; normalize by (1 + 21*n_days)
    adj = z_count + _safe_div(1.0 / 21.0, turn.replace(0, np.nan))
    return adj * 21.0


def f45_arkl_151_pastor_stambaugh_gamma_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _pastor_stambaugh_gamma(close, volume, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_152_pastor_stambaugh_gamma_504d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _pastor_stambaugh_gamma(close, volume, 504, min_periods=168)
    return out.diff().diff()


def f45_arkl_153_ps_gamma_pct_rank_252d_in_504d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 252, min_periods=84)
    out = _rolling_pct_rank(g, 504, min_periods=168)
    return out.diff().diff()


def f45_arkl_154_lot_zero_return_freq_252d_d2(close: pd.Series) -> pd.Series:
    out = _lot_zero_return_frac(close, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_155_lot_zero_return_and_vol_freq_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = (((r.abs() < 1e-6) & (volume <= 0)).astype(float)).where(r.notna() & volume.notna(), np.nan)
    out = z.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f45_arkl_156_fht_simplified_lot_252d_d2(close: pd.Series) -> pd.Series:
    zr = _lot_zero_return_frac(close, 252, min_periods=84)
    sigma = _safe_log(close).diff().rolling(252, min_periods=84).std()
    # Phi_inv((1+zr)/2) via piecewise linear approx (close enough for ranking)
    from math import sqrt
    v = zr.clip(0.001, 0.999)
    zfunc = pd.Series(np.where(v < 0.5, -1.0, 1.0) * np.sqrt(-2.0 * np.log(1.0 - (2.0 * np.abs(v - 0.5)).clip(0.001, 0.999))), index=zr.index)
    out = 2.0 * sigma * zfunc.abs()
    return out.diff().diff()


def f45_arkl_157_liu_lm12_standardized_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _liu_lm(close, volume, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_158_liu_lm3_standardized_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _liu_lm(close, volume, 63, min_periods=21)
    return out.diff().diff()


def f45_arkl_159_liu_lm1_standardized_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _liu_lm(close, volume, 21, min_periods=7)
    return out.diff().diff()


def f45_arkl_160_consec_zero_return_streak_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = (r.abs() < 1e-6).astype(int).where(r.notna(), 0)
    block = (z != z.shift(1)).fillna(False).cumsum()
    st = z.groupby(block).cumcount().astype(float)
    out = (st * (z > 0)).where(r.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_161_three_plus_zero_return_streak_indicator_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = (r.abs() < 1e-6).astype(int).where(r.notna(), 0)
    block = (z != z.shift(1)).fillna(False).cumsum()
    st = z.groupby(block).cumcount().astype(float)
    out = ((st * (z > 0)) >= 3).astype(float).where(r.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_162_ps_gamma_sign_flip_event_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 252, min_periods=84)
    sg = np.sign(g)
    out = (sg != sg.shift(21)).astype(float).where(sg.notna() & sg.shift(21).notna(), np.nan)
    return out.diff().diff()


def f45_arkl_163_abs_ps_gamma_zscore_252d_in_504d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 252, min_periods=84).abs()
    out = _rolling_zscore(g, 504, min_periods=168)
    return out.diff().diff()


def f45_arkl_164_ps_gamma_slope_63d_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 252, min_periods=84)
    out = g - g.shift(63)
    return out.diff().diff()


def f45_arkl_165_lot_21d_zero_freq_above_2x_252d_median_d2(close: pd.Series) -> pd.Series:
    z21 = _lot_zero_return_frac(close, 21, min_periods=7)
    z252_med = z21.rolling(252, min_periods=84).median()
    out = (z21 > 2.0 * z252_med).astype(float).where(z252_med.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_166_effective_tick_proxy_holden_63d_d2(close: pd.Series) -> pd.Series:
    out = _effective_tick_proxy(close, 63, min_periods=21)
    return out.diff().diff()


def f45_arkl_167_effective_tick_proxy_holden_252d_d2(close: pd.Series) -> pd.Series:
    out = _effective_tick_proxy(close, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_168_abdi_ranaldi_2d_hl_spread_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    return out.diff().diff()


def f45_arkl_169_abdi_ranaldi_2d_hl_spread_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _abdi_ranaldi_spread(high, low, close, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_170_close_at_whole_dollar_freq_63d_d2(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(float)
    at_whole = ((cents % 100) == 0).astype(float).where(close.notna(), np.nan)
    out = at_whole.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f45_arkl_171_close_last_cent_digit_entropy_63d_d2(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(int).astype(float)
    dig = cents % 10
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        h, _ = np.histogram(v, bins=10, range=(-0.5, 9.5))
        if h.sum() == 0:
            return np.nan
        p = h / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = dig.rolling(63, min_periods=21).apply(_ent, raw=True)
    return out.diff().diff()


def f45_arkl_172_hasbrouck_gibbs_proxy_63d_d2(close: pd.Series) -> pd.Series:
    dp = close.diff()
    same_sign = (np.sign(dp) == np.sign(dp.shift(1))).astype(float)
    # Spread proxy: average |dp| weighted by sign-flip probability
    est = dp.abs() * (1.0 - same_sign)
    out = est.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f45_arkl_173_choe_hasbrouck_spread_63d_d2(close: pd.Series) -> pd.Series:
    dp = close.diff()
    flipped = (np.sign(dp) != np.sign(dp.shift(1))).astype(float)
    spr_on_flip = dp.abs().where(flipped > 0.5, np.nan)
    out = spr_on_flip.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f45_arkl_174_glosten_harris_adverse_sel_proxy_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dp = close.diff()
    sv_sign = np.sign(dp.shift(-0)) * volume
    # Permanent (info) impact: cov(Δp, signed-vol). Transitory: residual.
    dp_lag1 = dp.shift(1)
    perm = dp.rolling(63, min_periods=21).cov(np.sign(dp) * volume)
    var_dp = dp.rolling(63, min_periods=21).var()
    out = _safe_div(perm, var_dp)
    return out.diff().diff()


def f45_arkl_175_mrr_order_flow_impact_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dp = close.diff()
    svol = np.sign(dp) * volume
    impact = dp.rolling(63, min_periods=21).corr(svol) * dp.rolling(63, min_periods=21).std() / svol.rolling(63, min_periods=21).std().replace(0, np.nan)
    out = impact
    return out.diff().diff()


def f45_arkl_176_abdi_ranaldi_spread_over_rv_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    rv = _safe_log(close).diff().rolling(63, min_periods=21).std()
    out = _safe_div(spr, rv)
    return out.diff().diff()


def f45_arkl_177_abdi_ranaldi_spread_over_atr21_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    atr = _atr(high, low, close, n=21)
    out = _safe_div(spr * close, atr)
    return out.diff().diff()


def f45_arkl_178_abdi_ranaldi_5d_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _abdi_ranaldi_spread(high, low, close, 5, min_periods=3)
    return out.diff().diff()


def f45_arkl_179_abdi_ranaldi_spread_accel_21_21_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    out = (spr - spr.shift(21)) - (spr.shift(21) - spr.shift(42))
    return out.diff().diff()


def f45_arkl_180_abdi_ranaldi_spread_pct_rank_63d_in_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    out = _rolling_pct_rank(spr, 252, min_periods=84)
    return out.diff().diff()


def f45_arkl_181_permanent_impact_signed_vol_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dp = close.diff()
    sv = np.sign(dp) * volume
    # 21d-ahead price change vs today's signed volume
    fut_dp = _safe_log(close).diff(21).shift(21)
    # rolling correlation: 63d window
    c = sv.rolling(63, min_periods=21).corr(fut_dp.shift(21))
    out = c
    return out.diff().diff()


def f45_arkl_182_transitory_impact_signed_vol_corr_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dp = close.diff()
    sv = np.sign(dp) * volume
    out = dp.rolling(63, min_periods=21).corr(sv)
    return out.diff().diff()


def f45_arkl_183_info_share_proxy_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dp = close.diff()
    sv = np.sign(dp) * volume
    # fit dp_t = a + b*sv_t  --> permanent = b*sv_t variance share
    b = dp.rolling(63, min_periods=21).cov(sv) / sv.rolling(63, min_periods=21).var().replace(0, np.nan)
    perm = (b * sv) ** 2
    tot = dp.rolling(63, min_periods=21).var()
    out = _safe_div(perm.rolling(63, min_periods=21).mean(), tot)
    return out.diff().diff()


def f45_arkl_184_spread_half_life_proxy_63d_d2(close: pd.Series) -> pd.Series:
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        rho = float((vc[1:] * vc[:-1]).sum() / den)
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(2) / np.log(rho))
    out = dp.abs().rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f45_arkl_185_spread_autocorr_lag5_63d_d2(close: pd.Series) -> pd.Series:
    dp = close.diff().abs()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 6:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        return float((vc[5:] * vc[:-5]).sum() / den)
    out = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f45_arkl_186_current_wide_spread_streak_63d_252d_med_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    med = spr.rolling(252, min_periods=84).median()
    wd = (spr > med).astype(int).where(med.notna(), 0)
    block = (wd != wd.shift(1)).fillna(False).cumsum()
    st = wd.groupby(block).cumcount().astype(float)
    out = (st * (wd > 0)).where(med.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_187_abdi_ranaldi_spread_3sigma_overshoot_63d_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    m = spr.rolling(252, min_periods=84).mean()
    sd = spr.rolling(252, min_periods=84).std()
    out = (spr > m + 3.0 * sd).astype(float).where(sd.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_188_hl_over_roll_spread_proxy_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = _safe_div(high - low, close).rolling(63, min_periods=21).mean()
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    rol = _safe_div(dp.rolling(63, min_periods=21).apply(_f, raw=True), close)
    out = _safe_div(hl, rol)
    return out.diff().diff()


def f45_arkl_189_spread_volume_corr_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 21, min_periods=7)
    out = spr.rolling(63, min_periods=21).corr(volume)
    return out.diff().diff()


def f45_arkl_190_ch_over_roll_spread_ratio_63d_d2(close: pd.Series) -> pd.Series:
    dp = close.diff()
    flipped = (np.sign(dp) != np.sign(dp.shift(1))).astype(float)
    ch = dp.abs().where(flipped > 0.5, np.nan).rolling(63, min_periods=21).mean()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    rol = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    out = _safe_div(ch, rol)
    return out.diff().diff()


def f45_arkl_191_wide_spread_low_vol_joint_stress_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    spr_med = spr.rolling(252, min_periods=84).median()
    vol_med = volume.rolling(252, min_periods=84).median()
    out = ((spr > spr_med) & (volume < vol_med)).astype(float).where(spr_med.notna() & vol_med.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_192_spread_accel_zscore_21d_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 21, min_periods=7)
    ch = spr - spr.shift(21)
    sd = spr.rolling(63, min_periods=21).std()
    out = _safe_div(ch, sd)
    return out.diff().diff()


def f45_arkl_193_spread_pct_distance_to_extreme_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    p95 = spr.rolling(252, min_periods=84).quantile(0.95)
    m = spr.rolling(252, min_periods=84).mean()
    out = _safe_div(spr - m, p95 - m)
    return out.diff().diff()


def f45_arkl_194_spread_regime_entropy_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 63, min_periods=21)
    med = spr.rolling(252, min_periods=84).median()
    state = np.where(spr < 0.5 * med, 0, np.where(spr > 2.0 * med, 2, 1))
    ss = pd.Series(state, index=spr.index).where(med.notna(), np.nan)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        p = np.array([(v == k).sum() / v.size for k in (0, 1, 2)])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = ss.rolling(252, min_periods=84).apply(_ent, raw=True)
    return out.diff().diff()


def f45_arkl_195_spread_vol_21d_over_252d_median_spread_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 21, min_periods=7)
    sd = spr.rolling(21, min_periods=7).std()
    med = spr.rolling(252, min_periods=84).median()
    out = _safe_div(sd, med)
    return out.diff().diff()


def f45_arkl_196_liu_lm12_zscore_252d_in_504d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    lm = _liu_lm(close, volume, 252, min_periods=84)
    out = _rolling_zscore(lm, 504, min_periods=168)
    return out.diff().diff()


def f45_arkl_197_liu_lm3_over_lm12_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(_liu_lm(close, volume, 63, min_periods=21), _liu_lm(close, volume, 252, min_periods=84))
    return out.diff().diff()


def f45_arkl_198_amihud_turnover_adjusted_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(63, min_periods=21).mean()
    # relative turnover
    m_vol = volume.rolling(252, min_periods=84).mean()
    rel_t = _safe_div(volume, m_vol).rolling(63, min_periods=21).mean()
    out = _safe_div(il, rel_t)
    return out.diff().diff()


def f45_arkl_199_pollet_rv_over_vol_of_vol_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(21, min_periods=7).std()
    vov = volume.rolling(21, min_periods=7).std() / volume.rolling(21, min_periods=7).mean().replace(0, np.nan)
    out = _safe_div(rv, vov).rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f45_arkl_200_amihud_half_life_proxy_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(21, min_periods=7).mean()
    def _hl(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        rho = float((vc[1:] * vc[:-1]).sum() / den)
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(2) / np.log(rho))
    out = il.rolling(252, min_periods=84).apply(_hl, raw=True)
    return out.diff().diff()


def f45_arkl_201_amihud_autocorr_lag5_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(21, min_periods=7).mean()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 6:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        return float((vc[5:] * vc[:-5]).sum() / den)
    out = il.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f45_arkl_202_amihud_vol_corr_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(21, min_periods=7).std()
    ra = r.abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(ra, dv).rolling(21, min_periods=7).mean()
    out = il.rolling(252, min_periods=84).corr(rv)
    return out.diff().diff()


def f45_arkl_203_amihud_return_corr_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ra = r.abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(ra, dv).rolling(21, min_periods=7).mean()
    out = il.rolling(252, min_periods=84).corr(r)
    return out.diff().diff()


def f45_arkl_204_amihud_rank_std_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(63, min_periods=21).mean()
    rk = _rolling_pct_rank(il, 252, min_periods=84)
    out = rk.rolling(252, min_periods=84).std()
    return out.diff().diff()


def f45_arkl_205_amihud_mean_reversion_speed_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(21, min_periods=7).mean()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        rho = float((vc[1:] * vc[:-1]).sum() / den)
        if abs(rho) <= 0 or abs(rho) >= 1:
            return np.nan
        return float(-np.log(abs(rho)))
    out = il.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f45_arkl_206_amihud_surge_recovery_bars_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv).rolling(21, min_periods=7).mean()
    def _f(w):
        if w.size < 30 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk >= w.size - 5:
            return np.nan
        peak_v = w[pk]
        if not np.isfinite(peak_v):
            return np.nan
        half = peak_v * 0.5
        for j in range(pk + 1, w.size):
            if not np.isnan(w[j]) and w[j] <= half:
                return float(j - pk)
        return float(w.size - pk)
    out = il.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f45_arkl_207_dollar_vol_mean_revert_halflife_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _safe_log(close * volume)
    def _hl(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        rho = float((vc[1:] * vc[:-1]).sum() / den)
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(2) / np.log(rho))
    out = dv.rolling(252, min_periods=84).apply(_hl, raw=True)
    return out.diff().diff()


def f45_arkl_208_trade_intensity_volume_over_1260d_mean_d2(volume: pd.Series) -> pd.Series:
    m = volume.rolling(1260, min_periods=252).mean()
    out = _safe_div(volume, m)
    return out.diff().diff()


def f45_arkl_209_pollet_rv_over_vol_z_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(21, min_periods=7).std()
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21).abs()
    out = _safe_div(rv, vz)
    return out.diff().diff()


def f45_arkl_210_vol_volatility_corr_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    rv = _safe_log(close).diff().rolling(21, min_periods=7).std()
    out = volume.rolling(63, min_periods=21).corr(rv)
    return out.diff().diff()


def f45_arkl_211_four_metric_illiq_rank_composite_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    dp = close.diff()
    def _r(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    rl = _rolling_pct_rank(dp.rolling(63, min_periods=21).apply(_r, raw=True), 252, min_periods=84)
    kr = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), np.sqrt((close * volume).clip(lower=1.0))).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    spr = _rolling_pct_rank(_abdi_ranaldi_spread(high, low, close, 63, min_periods=21), 252, min_periods=84)
    out = (ar + rl + kr + spr) / 4.0
    return out.diff().diff()


def f45_arkl_212_four_metric_rank_spread_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    dp = close.diff()
    def _r(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    rl = _rolling_pct_rank(dp.rolling(63, min_periods=21).apply(_r, raw=True), 252, min_periods=84)
    kr = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), np.sqrt((close * volume).clip(lower=1.0))).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    spr = _rolling_pct_rank(_abdi_ranaldi_spread(high, low, close, 63, min_periods=21), 252, min_periods=84)
    stk = pd.concat([ar.rename(0), rl.rename(1), kr.rename(2), spr.rename(3)], axis=1)
    out = stk.max(axis=1) - stk.min(axis=1)
    return out.diff().diff()


def f45_arkl_213_lot_zero_freq_at_high_composite_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    z = _lot_zero_return_frac(close, 21, min_periods=7)
    med = z.rolling(252, min_periods=84).median()
    surge = (z > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (surge * at_high).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_214_abs_ps_gamma_high_at_252d_high_composite_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 63, min_periods=21).abs()
    med = g.rolling(252, min_periods=84).median()
    high_g = (g > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (high_g * at_high).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_215_eff_tick_rising_at_high_composite_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    et = _effective_tick_proxy(close, 63, min_periods=21)
    etch = et - et.shift(63)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((etch > 0).astype(float) * at_high).where(et.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_216_three_plus_zero_days_in_21d_at_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = (r.abs() < 1e-6).astype(float).where(r.notna(), np.nan)
    c = z.rolling(21, min_periods=7).sum()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((c >= 3).astype(float) * at_high).where(c.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_217_illiq_composite_accel_at_high_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    acc = ar - ar.shift(21)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (acc * at_high).where(ar.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_218_dv_decline_amihud_surge_at_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _safe_log(close * volume)
    dv_z = _rolling_zscore(dv, 252, min_periods=84)
    decline = (dv_z < -1.0).astype(float)
    il = _safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(21, min_periods=7).mean()
    med = il.rolling(252, min_periods=84).median()
    surge = (il > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (decline * surge * at_high).where(med.notna() & rmax.notna() & dv_z.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_219_lot_top10_at_high_composite_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    z = _lot_zero_return_frac(close, 21, min_periods=7)
    rk = _rolling_pct_rank(z, 252, min_periods=84)
    top = (rk > 0.9).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (top * at_high).where(rk.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_220_ps_amihud_joint_top_quintile_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    g = _pastor_stambaugh_gamma(close, volume, 63, min_periods=21).abs()
    g_rk = _rolling_pct_rank(g, 252, min_periods=84)
    il = _safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    il_rk = _rolling_pct_rank(il, 252, min_periods=84)
    out = ((g_rk > 0.8) & (il_rk > 0.8)).astype(float).where(g_rk.notna() & il_rk.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_221_spread_compress_then_blowout_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spr = _abdi_ranaldi_spread(high, low, close, 21, min_periods=7)
    med = spr.rolling(252, min_periods=84).median()
    prior_low = (spr.shift(5).rolling(21, min_periods=7).max() < 0.7 * med).astype(float)
    now_high = (spr > 1.5 * med).astype(float)
    out = (prior_low * now_high).where(med.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_222_illiq_composite_slope_accel_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84)
    out = (ar - ar.shift(21)) - (ar.shift(21) - ar.shift(42))
    return out.diff().diff()


def f45_arkl_223_return_on_lagged_amihud_beta_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    il = _safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(21, min_periods=7).mean()
    out = _safe_div(r.rolling(252, min_periods=84).cov(il.shift(1)), il.shift(1).rolling(252, min_periods=84).var().replace(0, np.nan))
    return out.diff().diff()


def f45_arkl_224_multi_stress_with_price_decline_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = (_rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84) > 0.9).astype(float)
    spr = (_rolling_pct_rank(_abdi_ranaldi_spread(high, low, close, 63, min_periods=21), 252, min_periods=84) > 0.9).astype(float)
    z = (_rolling_pct_rank(_lot_zero_return_frac(close, 21, min_periods=7), 252, min_periods=84) > 0.9).astype(float)
    ret21 = _safe_log(close).diff(21)
    decl = (ret21 < 0).astype(float)
    out = ((ar + spr + z) * decl).where(ret21.notna(), np.nan)
    return out.diff().diff()


def f45_arkl_225_comp_ultimate_liq_trap_at_high_5plus_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = (_rolling_pct_rank(_safe_div(_safe_log(close).diff().abs(), (close * volume).replace(0, np.nan)).rolling(63, min_periods=21).mean(), 252, min_periods=84) > 0.8).astype(float)
    spr = (_rolling_pct_rank(_abdi_ranaldi_spread(high, low, close, 63, min_periods=21), 252, min_periods=84) > 0.8).astype(float)
    z = (_rolling_pct_rank(_lot_zero_return_frac(close, 21, min_periods=7), 252, min_periods=84) > 0.8).astype(float)
    lm = (_rolling_pct_rank(_liu_lm(close, volume, 63, min_periods=21), 252, min_periods=84) > 0.8).astype(float)
    ps = (_rolling_pct_rank(_pastor_stambaugh_gamma(close, volume, 63, min_periods=21).abs(), 252, min_periods=84) > 0.8).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    tot = (ar + spr + z + lm + ps)
    out = (tot * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


# ============================================================
#                         REGISTRY 151_225 (d2)
# ============================================================

AMIHUD_ROLL_KYLE_LIQUIDITY_D2_REGISTRY_151_225 = {
    "f45_arkl_151_pastor_stambaugh_gamma_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_151_pastor_stambaugh_gamma_252d_d2},
    "f45_arkl_152_pastor_stambaugh_gamma_504d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_152_pastor_stambaugh_gamma_504d_d2},
    "f45_arkl_153_ps_gamma_pct_rank_252d_in_504d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_153_ps_gamma_pct_rank_252d_in_504d_d2},
    "f45_arkl_154_lot_zero_return_freq_252d_d2": {"inputs": ["close"], "func": f45_arkl_154_lot_zero_return_freq_252d_d2},
    "f45_arkl_155_lot_zero_return_and_vol_freq_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_155_lot_zero_return_and_vol_freq_252d_d2},
    "f45_arkl_156_fht_simplified_lot_252d_d2": {"inputs": ["close"], "func": f45_arkl_156_fht_simplified_lot_252d_d2},
    "f45_arkl_157_liu_lm12_standardized_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_157_liu_lm12_standardized_252d_d2},
    "f45_arkl_158_liu_lm3_standardized_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_158_liu_lm3_standardized_63d_d2},
    "f45_arkl_159_liu_lm1_standardized_21d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_159_liu_lm1_standardized_21d_d2},
    "f45_arkl_160_consec_zero_return_streak_d2": {"inputs": ["close"], "func": f45_arkl_160_consec_zero_return_streak_d2},
    "f45_arkl_161_three_plus_zero_return_streak_indicator_d2": {"inputs": ["close"], "func": f45_arkl_161_three_plus_zero_return_streak_indicator_d2},
    "f45_arkl_162_ps_gamma_sign_flip_event_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_162_ps_gamma_sign_flip_event_252d_d2},
    "f45_arkl_163_abs_ps_gamma_zscore_252d_in_504d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_163_abs_ps_gamma_zscore_252d_in_504d_d2},
    "f45_arkl_164_ps_gamma_slope_63d_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_164_ps_gamma_slope_63d_252d_d2},
    "f45_arkl_165_lot_21d_zero_freq_above_2x_252d_median_d2": {"inputs": ["close"], "func": f45_arkl_165_lot_21d_zero_freq_above_2x_252d_median_d2},
    "f45_arkl_166_effective_tick_proxy_holden_63d_d2": {"inputs": ["close"], "func": f45_arkl_166_effective_tick_proxy_holden_63d_d2},
    "f45_arkl_167_effective_tick_proxy_holden_252d_d2": {"inputs": ["close"], "func": f45_arkl_167_effective_tick_proxy_holden_252d_d2},
    "f45_arkl_168_abdi_ranaldi_2d_hl_spread_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_168_abdi_ranaldi_2d_hl_spread_63d_d2},
    "f45_arkl_169_abdi_ranaldi_2d_hl_spread_252d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_169_abdi_ranaldi_2d_hl_spread_252d_d2},
    "f45_arkl_170_close_at_whole_dollar_freq_63d_d2": {"inputs": ["close"], "func": f45_arkl_170_close_at_whole_dollar_freq_63d_d2},
    "f45_arkl_171_close_last_cent_digit_entropy_63d_d2": {"inputs": ["close"], "func": f45_arkl_171_close_last_cent_digit_entropy_63d_d2},
    "f45_arkl_172_hasbrouck_gibbs_proxy_63d_d2": {"inputs": ["close"], "func": f45_arkl_172_hasbrouck_gibbs_proxy_63d_d2},
    "f45_arkl_173_choe_hasbrouck_spread_63d_d2": {"inputs": ["close"], "func": f45_arkl_173_choe_hasbrouck_spread_63d_d2},
    "f45_arkl_174_glosten_harris_adverse_sel_proxy_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_174_glosten_harris_adverse_sel_proxy_63d_d2},
    "f45_arkl_175_mrr_order_flow_impact_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_175_mrr_order_flow_impact_63d_d2},
    "f45_arkl_176_abdi_ranaldi_spread_over_rv_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_176_abdi_ranaldi_spread_over_rv_63d_d2},
    "f45_arkl_177_abdi_ranaldi_spread_over_atr21_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_177_abdi_ranaldi_spread_over_atr21_63d_d2},
    "f45_arkl_178_abdi_ranaldi_5d_spread_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_178_abdi_ranaldi_5d_spread_d2},
    "f45_arkl_179_abdi_ranaldi_spread_accel_21_21_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_179_abdi_ranaldi_spread_accel_21_21_63d_d2},
    "f45_arkl_180_abdi_ranaldi_spread_pct_rank_63d_in_252d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_180_abdi_ranaldi_spread_pct_rank_63d_in_252d_d2},
    "f45_arkl_181_permanent_impact_signed_vol_21d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_181_permanent_impact_signed_vol_21d_d2},
    "f45_arkl_182_transitory_impact_signed_vol_corr_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_182_transitory_impact_signed_vol_corr_63d_d2},
    "f45_arkl_183_info_share_proxy_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_183_info_share_proxy_63d_d2},
    "f45_arkl_184_spread_half_life_proxy_63d_d2": {"inputs": ["close"], "func": f45_arkl_184_spread_half_life_proxy_63d_d2},
    "f45_arkl_185_spread_autocorr_lag5_63d_d2": {"inputs": ["close"], "func": f45_arkl_185_spread_autocorr_lag5_63d_d2},
    "f45_arkl_186_current_wide_spread_streak_63d_252d_med_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_186_current_wide_spread_streak_63d_252d_med_d2},
    "f45_arkl_187_abdi_ranaldi_spread_3sigma_overshoot_63d_252d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_187_abdi_ranaldi_spread_3sigma_overshoot_63d_252d_d2},
    "f45_arkl_188_hl_over_roll_spread_proxy_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_188_hl_over_roll_spread_proxy_63d_d2},
    "f45_arkl_189_spread_volume_corr_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_189_spread_volume_corr_63d_d2},
    "f45_arkl_190_ch_over_roll_spread_ratio_63d_d2": {"inputs": ["close"], "func": f45_arkl_190_ch_over_roll_spread_ratio_63d_d2},
    "f45_arkl_191_wide_spread_low_vol_joint_stress_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_191_wide_spread_low_vol_joint_stress_63d_d2},
    "f45_arkl_192_spread_accel_zscore_21d_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_192_spread_accel_zscore_21d_63d_d2},
    "f45_arkl_193_spread_pct_distance_to_extreme_252d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_193_spread_pct_distance_to_extreme_252d_d2},
    "f45_arkl_194_spread_regime_entropy_252d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_194_spread_regime_entropy_252d_d2},
    "f45_arkl_195_spread_vol_21d_over_252d_median_spread_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_195_spread_vol_21d_over_252d_median_spread_d2},
    "f45_arkl_196_liu_lm12_zscore_252d_in_504d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_196_liu_lm12_zscore_252d_in_504d_d2},
    "f45_arkl_197_liu_lm3_over_lm12_d2": {"inputs": ["close", "volume"], "func": f45_arkl_197_liu_lm3_over_lm12_d2},
    "f45_arkl_198_amihud_turnover_adjusted_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_198_amihud_turnover_adjusted_63d_d2},
    "f45_arkl_199_pollet_rv_over_vol_of_vol_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_199_pollet_rv_over_vol_of_vol_63d_d2},
    "f45_arkl_200_amihud_half_life_proxy_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_200_amihud_half_life_proxy_252d_d2},
    "f45_arkl_201_amihud_autocorr_lag5_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_201_amihud_autocorr_lag5_252d_d2},
    "f45_arkl_202_amihud_vol_corr_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_202_amihud_vol_corr_252d_d2},
    "f45_arkl_203_amihud_return_corr_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_203_amihud_return_corr_252d_d2},
    "f45_arkl_204_amihud_rank_std_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_204_amihud_rank_std_252d_d2},
    "f45_arkl_205_amihud_mean_reversion_speed_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_205_amihud_mean_reversion_speed_252d_d2},
    "f45_arkl_206_amihud_surge_recovery_bars_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_206_amihud_surge_recovery_bars_252d_d2},
    "f45_arkl_207_dollar_vol_mean_revert_halflife_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_207_dollar_vol_mean_revert_halflife_252d_d2},
    "f45_arkl_208_trade_intensity_volume_over_1260d_mean_d2": {"inputs": ["volume"], "func": f45_arkl_208_trade_intensity_volume_over_1260d_mean_d2},
    "f45_arkl_209_pollet_rv_over_vol_z_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_209_pollet_rv_over_vol_z_63d_d2},
    "f45_arkl_210_vol_volatility_corr_63d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_210_vol_volatility_corr_63d_d2},
    "f45_arkl_211_four_metric_illiq_rank_composite_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_211_four_metric_illiq_rank_composite_252d_d2},
    "f45_arkl_212_four_metric_rank_spread_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_212_four_metric_rank_spread_252d_d2},
    "f45_arkl_213_lot_zero_freq_at_high_composite_d2": {"inputs": ["high", "close"], "func": f45_arkl_213_lot_zero_freq_at_high_composite_d2},
    "f45_arkl_214_abs_ps_gamma_high_at_252d_high_composite_d2": {"inputs": ["high", "close", "volume"], "func": f45_arkl_214_abs_ps_gamma_high_at_252d_high_composite_d2},
    "f45_arkl_215_eff_tick_rising_at_high_composite_d2": {"inputs": ["high", "close"], "func": f45_arkl_215_eff_tick_rising_at_high_composite_d2},
    "f45_arkl_216_three_plus_zero_days_in_21d_at_high_d2": {"inputs": ["high", "close"], "func": f45_arkl_216_three_plus_zero_days_in_21d_at_high_d2},
    "f45_arkl_217_illiq_composite_accel_at_high_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_217_illiq_composite_accel_at_high_252d_d2},
    "f45_arkl_218_dv_decline_amihud_surge_at_high_d2": {"inputs": ["high", "close", "volume"], "func": f45_arkl_218_dv_decline_amihud_surge_at_high_d2},
    "f45_arkl_219_lot_top10_at_high_composite_d2": {"inputs": ["high", "close"], "func": f45_arkl_219_lot_top10_at_high_composite_d2},
    "f45_arkl_220_ps_amihud_joint_top_quintile_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_220_ps_amihud_joint_top_quintile_252d_d2},
    "f45_arkl_221_spread_compress_then_blowout_63d_d2": {"inputs": ["high", "low", "close"], "func": f45_arkl_221_spread_compress_then_blowout_63d_d2},
    "f45_arkl_222_illiq_composite_slope_accel_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_222_illiq_composite_slope_accel_252d_d2},
    "f45_arkl_223_return_on_lagged_amihud_beta_252d_d2": {"inputs": ["close", "volume"], "func": f45_arkl_223_return_on_lagged_amihud_beta_252d_d2},
    "f45_arkl_224_multi_stress_with_price_decline_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_224_multi_stress_with_price_decline_21d_d2},
    "f45_arkl_225_comp_ultimate_liq_trap_at_high_5plus_d2": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_225_comp_ultimate_liq_trap_at_high_5plus_d2},
}
