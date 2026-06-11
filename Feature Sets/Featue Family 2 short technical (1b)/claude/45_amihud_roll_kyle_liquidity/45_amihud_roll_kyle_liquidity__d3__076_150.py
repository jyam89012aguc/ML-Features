"""amihud_roll_kyle_liquidity d3 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d3__001_075.py. Each
feature encodes a different concept in the liquidity theme:
Amihud illiquidity / Roll spread / Kyle's lambda / Corwin-Schultz / VPIN /
liquidity ratio / regime indicators / multi-horizon disagreement / deterioration composites.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _rolling_robust_z(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median()
    return _safe_div(s - med, 1.4826 * mad)


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


def _amihud(close, volume, n, min_periods=None):
    """Amihud illiquidity = mean(|r| / $-volume) over n days."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    il = _safe_div(r, dv)
    return il.rolling(n, min_periods=min_periods).mean()


def _roll_spread(close, n, min_periods=None):
    """Roll spread = 2 * sqrt(-cov(dp_t, dp_lag1)) when cov is negative, else NaN.
    Defined on price-changes."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    return dp.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _kyle_lambda(close, volume, n, min_periods=None):
    """Kyle's lambda proxy = |return| / sqrt(dollar-volume) averaged over n days."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    r = _safe_log(close).diff().abs()
    dv = (close * volume).clip(lower=1.0)
    k = _safe_div(r, np.sqrt(dv))
    return k.rolling(n, min_periods=min_periods).mean()


def _corwin_schultz(high, low, n, min_periods=None):
    """Corwin-Schultz spread estimator. Returns the 2-day-bar version averaged over n days."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    lh = _safe_log(high)
    ll = _safe_log(low)
    # one-day beta proxy: ratio sum of (log(H/L))^2 over 2 bars
    g1 = (lh - ll) ** 2
    beta = g1 + g1.shift(1)
    # gamma: log of high-of-2-bar / low-of-2-bar squared
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (_safe_log(h2) - _safe_log(l2)) ** 2
    denom = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / denom - np.sqrt(_safe_div(gamma, denom))
    spr = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spr.clip(lower=0).rolling(n, min_periods=min_periods).mean()


def f45_arkl_076_dollar_vol_per_abs_return_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = close * volume
    out = _safe_div(dv, r.replace(0, np.nan)).rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f45_arkl_077_dollar_vol_per_abs_return_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = close * volume
    out = _safe_div(dv, r.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f45_arkl_078_vol_over_hl_range_21d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(volume, (high - low).replace(0, np.nan)).rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f45_arkl_079_vol_over_hl_range_63d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(volume, (high - low).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f45_arkl_080_relative_turnover_63d_d3(volume: pd.Series) -> pd.Series:
    m = volume.rolling(252, min_periods=84).mean()
    out = _safe_div(volume, m).rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f45_arkl_081_turnover_pct_rank_63d_in_252d_d3(volume: pd.Series) -> pd.Series:
    m = volume.rolling(252, min_periods=84).mean()
    rt = _safe_div(volume, m).rolling(63, min_periods=21).mean()
    out = _rolling_pct_rank(rt, 252, min_periods=84)
    return out.diff().diff().diff()


def f45_arkl_082_vol_over_hl_range_zscore_63d_in_252d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    ll = _safe_div(volume, (high - low).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    out = _rolling_zscore(ll, 252, min_periods=84)
    return out.diff().diff().diff()


def f45_arkl_083_inv_amihud_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = 1.0 / _amihud(close, volume, 63, min_periods=21).replace(0, np.nan)
    return out.diff().diff().diff()


def f45_arkl_084_inv_roll_spread_63d_d3(close: pd.Series) -> pd.Series:
    out = 1.0 / _roll_spread(close, 63, min_periods=21).replace(0, np.nan)
    return out.diff().diff().diff()


def f45_arkl_085_amihud_over_hh_liq_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    hh = _safe_div(volume, (high - low).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    out = _safe_div(il, hh)
    return out.diff().diff().diff()


def f45_arkl_086_zero_vol_day_count_63d_d3(volume: pd.Series) -> pd.Series:
    zv = (volume <= 0).astype(float).where(volume.notna(), np.nan)
    out = zv.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f45_arkl_087_zero_vol_day_count_252d_d3(volume: pd.Series) -> pd.Series:
    zv = (volume <= 0).astype(float).where(volume.notna(), np.nan)
    out = zv.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f45_arkl_088_mean_log_dollar_vol_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    out = _safe_log(dv).rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f45_arkl_089_log_dollar_vol_zscore_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _safe_log(close * volume)
    out = _rolling_zscore(dv.rolling(63, min_periods=21).mean(), 252, min_periods=84)
    return out.diff().diff().diff()


def f45_arkl_090_inv_dollar_vol_zscore_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).replace(0, np.nan)
    inv = 1.0 / dv
    out = _rolling_zscore(inv.rolling(63, min_periods=21).mean(), 252, min_periods=84)
    return out.diff().diff().diff()


def f45_arkl_091_autocorr_dp_lag1_63d_d3(close: pd.Series) -> pd.Series:
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean()
        vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    out = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff().diff()


def f45_arkl_092_autocorr_logret_lag1_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean()
        vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f45_arkl_093_neg_autocorr_indicator_63d_d3(close: pd.Series) -> pd.Series:
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
        return float((vc[1:] * vc[:-1]).sum() / den)
    ac = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    out = (ac < 0).astype(float).where(ac.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_094_abs_neg_autocorr_dp_63d_d3(close: pd.Series) -> pd.Series:
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
        return float((vc[1:] * vc[:-1]).sum() / den)
    ac = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    out = ac.abs().where(ac < 0, np.nan)
    return out.diff().diff().diff()


def f45_arkl_095_roll_measure_lag3_cov_63d_d3(close: pd.Series) -> pd.Series:
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 6:
            return np.nan
        a = v[3:]; b = v[:-3]
        return float(np.mean((a - a.mean()) * (b - b.mean())))
    out = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff().diff()


def f45_arkl_096_alternating_sign_run_density_63d_d3(close: pd.Series) -> pd.Series:
    sg = np.sign(close.diff())
    flip = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = flip.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f45_arkl_097_sign_flip_density_dp_21d_d3(close: pd.Series) -> pd.Series:
    sg = np.sign(close.diff())
    flip = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = flip.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f45_arkl_098_sign_flip_density_dp_252d_d3(close: pd.Series) -> pd.Series:
    sg = np.sign(close.diff())
    flip = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = flip.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f45_arkl_099_close_to_open_var_share_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    ovn = _safe_log(open) - _safe_log(close.shift(1))
    day = _safe_log(close) - _safe_log(open)
    v_ovn = ovn.rolling(63, min_periods=21).var()
    v_day = day.rolling(63, min_periods=21).var()
    out = _safe_div(v_ovn, v_ovn + v_day)
    return out.diff().diff().diff()


def f45_arkl_100_roll_cov_up_minus_down_days_63d_d3(close: pd.Series) -> pd.Series:
    dp = close.diff()
    sgn = np.sign(dp)
    up = dp.where(sgn > 0, np.nan)
    dn = dp.where(sgn < 0, np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        return float(np.mean((a - a.mean()) * (b - b.mean())))
    c_up = up.rolling(63, min_periods=21).apply(_f, raw=True)
    c_dn = dn.rolling(63, min_periods=21).apply(_f, raw=True)
    out = c_up - c_dn
    return out.diff().diff().diff()


def f45_arkl_101_var_dp_63d_over_var_dp_252d_d3(close: pd.Series) -> pd.Series:
    dp = close.diff()
    out = _safe_div(dp.rolling(63, min_periods=21).var(), dp.rolling(252, min_periods=84).var())
    return out.diff().diff().diff()


def f45_arkl_102_roll_spread_change_63d_63d_d3(close: pd.Series) -> pd.Series:
    s = _roll_spread(close, 63, min_periods=21)
    out = s - s.shift(63)
    return out.diff().diff().diff()


def f45_arkl_103_amihud_accel_21_21_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = (il - il.shift(21)) - (il.shift(21) - il.shift(42))
    return out.diff().diff().diff()


def f45_arkl_104_amihud_std_63d_over_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    out = il.rolling(63, min_periods=21).std()
    return out.diff().diff().diff()


def f45_arkl_105_roll_cov_var_63d_over_252d_d3(close: pd.Series) -> pd.Series:
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        return float(np.mean((a - a.mean()) * (b - b.mean())))
    c = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    out = c.rolling(252, min_periods=84).var()
    return out.diff().diff().diff()


def f45_arkl_106_amihud_above_2x_median_indicator_63d_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    med = il.rolling(252, min_periods=84).median()
    out = (il > 2.0 * med).astype(float).where(med.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_107_dryup_5bar_below_half_median_indicator_d3(volume: pd.Series) -> pd.Series:
    med = volume.rolling(252, min_periods=84).median()
    low = (volume < 0.5 * med).astype(float).where(med.notna(), np.nan)
    out = (low.rolling(5, min_periods=5).min() > 0.5).astype(float).where(med.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_108_current_amihud_above_252d_median_streak_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    med = il.rolling(252, min_periods=84).median()
    above = (il > med).astype(int).where(med.notna(), 0)
    block = (above != above.shift(1)).fillna(False).cumsum()
    st = above.groupby(block).cumcount().astype(float)
    out = (st * (above > 0)).where(med.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_109_frac_amihud_above_median_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    med = il.rolling(252, min_periods=84).median()
    above = (il > med).astype(float).where(med.notna(), np.nan)
    out = above.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f45_arkl_110_amihud_regime_cross_2x_event_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    med = il.rolling(252, min_periods=84).median()
    above = (il > 2.0 * med).astype(float).where(med.notna(), np.nan)
    ev = ((above.shift(1) < 0.5) & (above > 0.5)).astype(float).where(med.notna() & med.shift(1).notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f45_arkl_111_roll_spread_above_1pct_close_indicator_63d_d3(close: pd.Series) -> pd.Series:
    s = _roll_spread(close, 63, min_periods=21)
    out = (s > 0.01 * close).astype(float).where(s.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_112_roll_spread_regime_transition_count_252d_d3(close: pd.Series) -> pd.Series:
    s = _roll_spread(close, 63, min_periods=21)
    med = s.rolling(252, min_periods=84).median()
    above = (s > 2.0 * med).astype(float).where(med.notna(), np.nan)
    ev = ((above.shift(1) < 0.5) & (above > 0.5)).astype(float).where(med.notna() & med.shift(1).notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f45_arkl_113_multi_illiq_rank_composite_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    out = (ar + rr + kr) / 3.0
    return out.diff().diff().diff()


def f45_arkl_114_high_illiq_composite_above_80_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    out = (c > 0.8).astype(float).where(c.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_115_illiq_composite_slope_21d_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    out = c - c.shift(21)
    return out.diff().diff().diff()


def f45_arkl_116_amihud_up_minus_down_days_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rp = r.where(r > 0, 0.0); rn = (-r).where(r < 0, 0.0)
    dv = (close * volume).replace(0, np.nan)
    out = (_safe_div(rn.abs(), dv).rolling(63, min_periods=21).mean() - _safe_div(rp.abs(), dv).rolling(63, min_periods=21).mean())
    return out.diff().diff().diff()


def f45_arkl_117_amihud_3x_median_events_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    med = il.rolling(252, min_periods=84).median()
    ev = (il > 3.0 * med).astype(float).where(med.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f45_arkl_118_bars_since_amihud_3x_median_event_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    med = il.rolling(252, min_periods=84).median()
    ev = (il > 3.0 * med) & med.notna()
    arr = ev.fillna(False).astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=il.index)
    return out.diff().diff().diff()


def f45_arkl_119_amihud_event_mean_gap_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    med = il.rolling(252, min_periods=84).median()
    ev = (il > 3.0 * med).astype(float).where(med.notna(), np.nan)
    cnt = ev.rolling(252, min_periods=84).sum()
    out = 252.0 / cnt.replace(0, np.nan)
    return out.diff().diff().diff()


def f45_arkl_120_triple_stress_regime_indicator_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    vr = _rolling_pct_rank(v, 252, min_periods=84)
    out = ((ar > 0.8) & (rr > 0.8) & (vr > 0.8)).astype(float).where(ar.notna() & rr.notna() & vr.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_121_amihud_21d_vs_252d_zscore_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    z21 = _rolling_zscore(_amihud(close, volume, 21, min_periods=7), 504, min_periods=168)
    z252 = _rolling_zscore(_amihud(close, volume, 252, min_periods=84), 504, min_periods=168)
    out = z21 - z252
    return out.diff().diff().diff()


def f45_arkl_122_amihud_rank_diff_21_vs_252_in_504d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r21 = _rolling_pct_rank(_amihud(close, volume, 21, min_periods=7), 504, min_periods=168)
    r252 = _rolling_pct_rank(_amihud(close, volume, 252, min_periods=84), 504, min_periods=168)
    out = r21 - r252
    return out.diff().diff().diff()


def f45_arkl_123_roll_spread_21_vs_252_zscore_diff_d3(close: pd.Series) -> pd.Series:
    z21 = _rolling_zscore(_roll_spread(close, 21, min_periods=7), 504, min_periods=168)
    z252 = _rolling_zscore(_roll_spread(close, 252, min_periods=84), 504, min_periods=168)
    out = z21 - z252
    return out.diff().diff().diff()


def f45_arkl_124_kyle_21_vs_252_zscore_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    z21 = _rolling_zscore(_kyle_lambda(close, volume, 21, min_periods=7), 504, min_periods=168)
    z252 = _rolling_zscore(_kyle_lambda(close, volume, 252, min_periods=84), 504, min_periods=168)
    out = z21 - z252
    return out.diff().diff().diff()


def f45_arkl_125_arkl_unanimous_high_indicator_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    out = ((ar > 0.5) & (rr > 0.5) & (kr > 0.5)).astype(float).where(ar.notna() & rr.notna() & kr.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_126_amihud_minus_cs_rank_diff_63d_in_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    cs = _rolling_pct_rank(_corwin_schultz(high, low, 63, min_periods=21), 252, min_periods=84)
    out = ar - cs
    return out.diff().diff().diff()


def f45_arkl_127_amihud_ratio_5d_over_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(_amihud(close, volume, 5, min_periods=2), _amihud(close, volume, 63, min_periods=21))
    return out.diff().diff().diff()


def f45_arkl_128_amihud_3horizon_sign_entropy_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    z21 = np.sign(_rolling_zscore(_amihud(close, volume, 21, min_periods=7), 252, min_periods=84))
    z63 = np.sign(_rolling_zscore(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84))
    z252 = np.sign(_rolling_zscore(_amihud(close, volume, 252, min_periods=84), 252, min_periods=84))
    st = pd.concat([z21.rename(0), z63.rename(1), z252.rename(2)], axis=1)
    def _e(row):
        a = row.dropna().values
        if a.size < 2:
            return np.nan
        pp = (a > 0).sum() / a.size
        pn = (a < 0).sum() / a.size
        pz = (a == 0).sum() / a.size
        p = np.array([pp, pn, pz])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = st.apply(_e, axis=1)
    return out.diff().diff().diff()


def f45_arkl_129_arkl_metric_agreement_frac_63d_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = np.sign(_rolling_zscore(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84))
    rr = np.sign(_rolling_zscore(_roll_spread(close, 63, min_periods=21), 252, min_periods=84))
    kr = np.sign(_rolling_zscore(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84))
    agree = ((ar == rr).astype(float) + (rr == kr).astype(float) + (ar == kr).astype(float)) / 3.0
    out = agree.where(ar.notna() & rr.notna() & kr.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_130_amihud_252d_minus_5d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 252, min_periods=84) - _amihud(close, volume, 5, min_periods=2)
    return out.diff().diff().diff()


def f45_arkl_131_amihud_z_spread_3horizons_in_504d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    z21 = _rolling_zscore(_amihud(close, volume, 21, min_periods=7), 504, min_periods=168)
    z63 = _rolling_zscore(_amihud(close, volume, 63, min_periods=21), 504, min_periods=168)
    z252 = _rolling_zscore(_amihud(close, volume, 252, min_periods=84), 504, min_periods=168)
    st = pd.concat([z21.rename(0), z63.rename(1), z252.rename(2)], axis=1)
    out = st.max(axis=1) - st.min(axis=1)
    return out.diff().diff().diff()


def f45_arkl_132_roll_spread_21_over_252_d3(close: pd.Series) -> pd.Series:
    out = _safe_div(_roll_spread(close, 21, min_periods=7), _roll_spread(close, 252, min_periods=84))
    return out.diff().diff().diff()


def f45_arkl_133_amihud_roll_corr_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    rl = _roll_spread(close, 21, min_periods=7)
    out = il.rolling(252, min_periods=84).corr(rl)
    return out.diff().diff().diff()


def f45_arkl_134_amihud_kyle_corr_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    kl = _kyle_lambda(close, volume, 21, min_periods=7)
    out = il.rolling(252, min_periods=84).corr(kl)
    return out.diff().diff().diff()


def f45_arkl_135_roll_kyle_corr_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    rl = _roll_spread(close, 21, min_periods=7)
    kl = _kyle_lambda(close, volume, 21, min_periods=7)
    out = rl.rolling(252, min_periods=84).corr(kl)
    return out.diff().diff().diff()


def f45_arkl_136_illiq_composite_rising_30pct_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    out = (c - c.shift(21) > 0.3).astype(float).where(c.notna() & c.shift(21).notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_137_dryup_at_252d_high_indicator_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= rmax - 0.05 * rmax).astype(float)
    med = volume.rolling(252, min_periods=84).median()
    low_v = (volume < 0.5 * med).astype(float)
    out = (at_high * low_v).where(rmax.notna() & med.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_138_amihud_surge_at_high_composite_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 21, min_periods=7)
    med = il.rolling(252, min_periods=84).median()
    surge = (il > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (surge * at_high).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_139_roll_spread_doubled_at_high_composite_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    s = _roll_spread(close, 63, min_periods=21)
    med = s.rolling(252, min_periods=84).median()
    dou = (s > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (dou * at_high).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_140_kyle_lambda_surge_at_high_composite_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _kyle_lambda(close, volume, 63, min_periods=21)
    med = k.rolling(252, min_periods=84).median()
    surge = (k > 2.0 * med).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (surge * at_high).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_141_vpin_05_at_252d_high_composite_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((v > 0.5).astype(float) * at_high).where(v.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_142_illiq_accel_at_high_composite_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    acc = c - c.shift(21)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (acc * at_high).where(c.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_143_illiq_top10_with_price_decline_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    high_il = (c > 0.9).astype(float)
    ret21 = _safe_log(close).diff(21)
    out = (high_il * (ret21 < 0).astype(float)).where(c.notna() & ret21.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_144_dollar_vol_collapse_at_high_composite_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _safe_log(close * volume).rolling(21, min_periods=7).mean()
    z = _rolling_zscore(dv, 252, min_periods=84)
    coll = (z < -2.0).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (coll * at_high).where(z.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_145_neg_autocorr_at_high_composite_d3(high: pd.Series, close: pd.Series) -> pd.Series:
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
        return float((vc[1:] * vc[:-1]).sum() / den)
    ac = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    neg = (ac < -0.1).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (neg * at_high).where(ac.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_146_zero_vol_count_3plus_at_high_21d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    zv = (volume <= 0).astype(float)
    cnt = zv.rolling(21, min_periods=7).sum()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((cnt >= 3).astype(float) * at_high).where(cnt.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_147_cs_up_amihud_down_at_high_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cs = _corwin_schultz(high, low, 63, min_periods=21)
    il = _amihud(close, volume, 63, min_periods=21)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    disag = (((cs - cs.shift(21)) > 0).astype(float) * ((il - il.shift(21)) < 0).astype(float))
    out = (disag * at_high).where(cs.notna() & il.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_148_stress_metric_count_top_decile_63d_in_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = (_rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84) > 0.9).astype(float)
    rr = (_rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84) > 0.9).astype(float)
    kr = (_rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84) > 0.9).astype(float)
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    vr = (_rolling_pct_rank(v, 252, min_periods=84) > 0.9).astype(float)
    out = ar + rr + kr + vr
    return out.diff().diff().diff()


def f45_arkl_149_sustained_illiq_21bar_above_07_composite_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    c = (ar + rr + kr) / 3.0
    out = (c.rolling(21, min_periods=10).min() > 0.7).astype(float).where(c.notna(), np.nan)
    return out.diff().diff().diff()


def f45_arkl_150_comp_ultimate_illiq_trap_at_high_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ar = _rolling_pct_rank(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    rr = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    kr = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    sgn = np.sign(close.diff()); sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    vr = _rolling_pct_rank(v, 252, min_periods=84)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((ar > 0.8).astype(float) + (rr > 0.8).astype(float) + (kr > 0.8).astype(float) + (vr > 0.8).astype(float) + at_high).where(ar.notna() & rr.notna() & kr.notna() & vr.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d3)
# ============================================================

AMIHUD_ROLL_KYLE_LIQUIDITY_D3_REGISTRY_076_150 = {
    "f45_arkl_076_dollar_vol_per_abs_return_21d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_076_dollar_vol_per_abs_return_21d_d3},
    "f45_arkl_077_dollar_vol_per_abs_return_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_077_dollar_vol_per_abs_return_63d_d3},
    "f45_arkl_078_vol_over_hl_range_21d_d3": {"inputs": ["high", "low", "volume"], "func": f45_arkl_078_vol_over_hl_range_21d_d3},
    "f45_arkl_079_vol_over_hl_range_63d_d3": {"inputs": ["high", "low", "volume"], "func": f45_arkl_079_vol_over_hl_range_63d_d3},
    "f45_arkl_080_relative_turnover_63d_d3": {"inputs": ["volume"], "func": f45_arkl_080_relative_turnover_63d_d3},
    "f45_arkl_081_turnover_pct_rank_63d_in_252d_d3": {"inputs": ["volume"], "func": f45_arkl_081_turnover_pct_rank_63d_in_252d_d3},
    "f45_arkl_082_vol_over_hl_range_zscore_63d_in_252d_d3": {"inputs": ["high", "low", "volume"], "func": f45_arkl_082_vol_over_hl_range_zscore_63d_in_252d_d3},
    "f45_arkl_083_inv_amihud_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_083_inv_amihud_63d_d3},
    "f45_arkl_084_inv_roll_spread_63d_d3": {"inputs": ["close"], "func": f45_arkl_084_inv_roll_spread_63d_d3},
    "f45_arkl_085_amihud_over_hh_liq_63d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_085_amihud_over_hh_liq_63d_d3},
    "f45_arkl_086_zero_vol_day_count_63d_d3": {"inputs": ["volume"], "func": f45_arkl_086_zero_vol_day_count_63d_d3},
    "f45_arkl_087_zero_vol_day_count_252d_d3": {"inputs": ["volume"], "func": f45_arkl_087_zero_vol_day_count_252d_d3},
    "f45_arkl_088_mean_log_dollar_vol_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_088_mean_log_dollar_vol_63d_d3},
    "f45_arkl_089_log_dollar_vol_zscore_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_089_log_dollar_vol_zscore_63d_in_252d_d3},
    "f45_arkl_090_inv_dollar_vol_zscore_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_090_inv_dollar_vol_zscore_63d_in_252d_d3},
    "f45_arkl_091_autocorr_dp_lag1_63d_d3": {"inputs": ["close"], "func": f45_arkl_091_autocorr_dp_lag1_63d_d3},
    "f45_arkl_092_autocorr_logret_lag1_252d_d3": {"inputs": ["close"], "func": f45_arkl_092_autocorr_logret_lag1_252d_d3},
    "f45_arkl_093_neg_autocorr_indicator_63d_d3": {"inputs": ["close"], "func": f45_arkl_093_neg_autocorr_indicator_63d_d3},
    "f45_arkl_094_abs_neg_autocorr_dp_63d_d3": {"inputs": ["close"], "func": f45_arkl_094_abs_neg_autocorr_dp_63d_d3},
    "f45_arkl_095_roll_measure_lag3_cov_63d_d3": {"inputs": ["close"], "func": f45_arkl_095_roll_measure_lag3_cov_63d_d3},
    "f45_arkl_096_alternating_sign_run_density_63d_d3": {"inputs": ["close"], "func": f45_arkl_096_alternating_sign_run_density_63d_d3},
    "f45_arkl_097_sign_flip_density_dp_21d_d3": {"inputs": ["close"], "func": f45_arkl_097_sign_flip_density_dp_21d_d3},
    "f45_arkl_098_sign_flip_density_dp_252d_d3": {"inputs": ["close"], "func": f45_arkl_098_sign_flip_density_dp_252d_d3},
    "f45_arkl_099_close_to_open_var_share_63d_d3": {"inputs": ["open", "close"], "func": f45_arkl_099_close_to_open_var_share_63d_d3},
    "f45_arkl_100_roll_cov_up_minus_down_days_63d_d3": {"inputs": ["close"], "func": f45_arkl_100_roll_cov_up_minus_down_days_63d_d3},
    "f45_arkl_101_var_dp_63d_over_var_dp_252d_d3": {"inputs": ["close"], "func": f45_arkl_101_var_dp_63d_over_var_dp_252d_d3},
    "f45_arkl_102_roll_spread_change_63d_63d_d3": {"inputs": ["close"], "func": f45_arkl_102_roll_spread_change_63d_63d_d3},
    "f45_arkl_103_amihud_accel_21_21_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_103_amihud_accel_21_21_63d_d3},
    "f45_arkl_104_amihud_std_63d_over_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_104_amihud_std_63d_over_63d_d3},
    "f45_arkl_105_roll_cov_var_63d_over_252d_d3": {"inputs": ["close"], "func": f45_arkl_105_roll_cov_var_63d_over_252d_d3},
    "f45_arkl_106_amihud_above_2x_median_indicator_63d_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_106_amihud_above_2x_median_indicator_63d_252d_d3},
    "f45_arkl_107_dryup_5bar_below_half_median_indicator_d3": {"inputs": ["volume"], "func": f45_arkl_107_dryup_5bar_below_half_median_indicator_d3},
    "f45_arkl_108_current_amihud_above_252d_median_streak_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_108_current_amihud_above_252d_median_streak_63d_d3},
    "f45_arkl_109_frac_amihud_above_median_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_109_frac_amihud_above_median_252d_d3},
    "f45_arkl_110_amihud_regime_cross_2x_event_count_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_110_amihud_regime_cross_2x_event_count_252d_d3},
    "f45_arkl_111_roll_spread_above_1pct_close_indicator_63d_d3": {"inputs": ["close"], "func": f45_arkl_111_roll_spread_above_1pct_close_indicator_63d_d3},
    "f45_arkl_112_roll_spread_regime_transition_count_252d_d3": {"inputs": ["close"], "func": f45_arkl_112_roll_spread_regime_transition_count_252d_d3},
    "f45_arkl_113_multi_illiq_rank_composite_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_113_multi_illiq_rank_composite_63d_in_252d_d3},
    "f45_arkl_114_high_illiq_composite_above_80_indicator_d3": {"inputs": ["close", "volume"], "func": f45_arkl_114_high_illiq_composite_above_80_indicator_d3},
    "f45_arkl_115_illiq_composite_slope_21d_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_115_illiq_composite_slope_21d_63d_d3},
    "f45_arkl_116_amihud_up_minus_down_days_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_116_amihud_up_minus_down_days_63d_d3},
    "f45_arkl_117_amihud_3x_median_events_count_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_117_amihud_3x_median_events_count_252d_d3},
    "f45_arkl_118_bars_since_amihud_3x_median_event_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_118_bars_since_amihud_3x_median_event_252d_d3},
    "f45_arkl_119_amihud_event_mean_gap_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_119_amihud_event_mean_gap_252d_d3},
    "f45_arkl_120_triple_stress_regime_indicator_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_120_triple_stress_regime_indicator_63d_in_252d_d3},
    "f45_arkl_121_amihud_21d_vs_252d_zscore_diff_d3": {"inputs": ["close", "volume"], "func": f45_arkl_121_amihud_21d_vs_252d_zscore_diff_d3},
    "f45_arkl_122_amihud_rank_diff_21_vs_252_in_504d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_122_amihud_rank_diff_21_vs_252_in_504d_d3},
    "f45_arkl_123_roll_spread_21_vs_252_zscore_diff_d3": {"inputs": ["close"], "func": f45_arkl_123_roll_spread_21_vs_252_zscore_diff_d3},
    "f45_arkl_124_kyle_21_vs_252_zscore_diff_d3": {"inputs": ["close", "volume"], "func": f45_arkl_124_kyle_21_vs_252_zscore_diff_d3},
    "f45_arkl_125_arkl_unanimous_high_indicator_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_125_arkl_unanimous_high_indicator_63d_in_252d_d3},
    "f45_arkl_126_amihud_minus_cs_rank_diff_63d_in_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_126_amihud_minus_cs_rank_diff_63d_in_252d_d3},
    "f45_arkl_127_amihud_ratio_5d_over_63d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_127_amihud_ratio_5d_over_63d_d3},
    "f45_arkl_128_amihud_3horizon_sign_entropy_d3": {"inputs": ["close", "volume"], "func": f45_arkl_128_amihud_3horizon_sign_entropy_d3},
    "f45_arkl_129_arkl_metric_agreement_frac_63d_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_129_arkl_metric_agreement_frac_63d_252d_d3},
    "f45_arkl_130_amihud_252d_minus_5d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_130_amihud_252d_minus_5d_d3},
    "f45_arkl_131_amihud_z_spread_3horizons_in_504d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_131_amihud_z_spread_3horizons_in_504d_d3},
    "f45_arkl_132_roll_spread_21_over_252_d3": {"inputs": ["close"], "func": f45_arkl_132_roll_spread_21_over_252_d3},
    "f45_arkl_133_amihud_roll_corr_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_133_amihud_roll_corr_252d_d3},
    "f45_arkl_134_amihud_kyle_corr_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_134_amihud_kyle_corr_252d_d3},
    "f45_arkl_135_roll_kyle_corr_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_135_roll_kyle_corr_252d_d3},
    "f45_arkl_136_illiq_composite_rising_30pct_21d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_136_illiq_composite_rising_30pct_21d_d3},
    "f45_arkl_137_dryup_at_252d_high_indicator_d3": {"inputs": ["high", "volume"], "func": f45_arkl_137_dryup_at_252d_high_indicator_d3},
    "f45_arkl_138_amihud_surge_at_high_composite_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_138_amihud_surge_at_high_composite_d3},
    "f45_arkl_139_roll_spread_doubled_at_high_composite_d3": {"inputs": ["high", "close"], "func": f45_arkl_139_roll_spread_doubled_at_high_composite_d3},
    "f45_arkl_140_kyle_lambda_surge_at_high_composite_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_140_kyle_lambda_surge_at_high_composite_d3},
    "f45_arkl_141_vpin_05_at_252d_high_composite_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_141_vpin_05_at_252d_high_composite_d3},
    "f45_arkl_142_illiq_accel_at_high_composite_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_142_illiq_accel_at_high_composite_d3},
    "f45_arkl_143_illiq_top10_with_price_decline_21d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_143_illiq_top10_with_price_decline_21d_d3},
    "f45_arkl_144_dollar_vol_collapse_at_high_composite_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_144_dollar_vol_collapse_at_high_composite_d3},
    "f45_arkl_145_neg_autocorr_at_high_composite_d3": {"inputs": ["high", "close"], "func": f45_arkl_145_neg_autocorr_at_high_composite_d3},
    "f45_arkl_146_zero_vol_count_3plus_at_high_21d_d3": {"inputs": ["high", "volume"], "func": f45_arkl_146_zero_vol_count_3plus_at_high_21d_d3},
    "f45_arkl_147_cs_up_amihud_down_at_high_d3": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_147_cs_up_amihud_down_at_high_d3},
    "f45_arkl_148_stress_metric_count_top_decile_63d_in_252d_d3": {"inputs": ["close", "volume"], "func": f45_arkl_148_stress_metric_count_top_decile_63d_in_252d_d3},
    "f45_arkl_149_sustained_illiq_21bar_above_07_composite_d3": {"inputs": ["close", "volume"], "func": f45_arkl_149_sustained_illiq_21bar_above_07_composite_d3},
    "f45_arkl_150_comp_ultimate_illiq_trap_at_high_d3": {"inputs": ["high", "close", "volume"], "func": f45_arkl_150_comp_ultimate_illiq_trap_at_high_d3},
}
