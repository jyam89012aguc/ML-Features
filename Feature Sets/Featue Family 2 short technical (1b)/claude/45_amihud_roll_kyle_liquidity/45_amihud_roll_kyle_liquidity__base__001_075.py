"""amihud_roll_kyle_liquidity base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each
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


def f45_arkl_001_amihud_illiq_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 5, min_periods=2)
    return out


def f45_arkl_002_amihud_illiq_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 21, min_periods=7)
    return out


def f45_arkl_003_amihud_illiq_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 63, min_periods=21)
    return out


def f45_arkl_004_amihud_illiq_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 252, min_periods=84)
    return out


def f45_arkl_005_amihud_illiq_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _amihud(close, volume, 504, min_periods=168)
    return out


def f45_arkl_006_amihud_zscore_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = _rolling_zscore(il, 252, min_periods=84)
    return out


def f45_arkl_007_amihud_robust_z_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = _rolling_robust_z(il, 252, min_periods=84)
    return out


def f45_arkl_008_amihud_pct_rank_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = _rolling_pct_rank(il, 252, min_periods=84)
    return out


def f45_arkl_009_amihud_log_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = _safe_log(il + 1e-15)
    return out


def f45_arkl_010_amihud_slope_21d_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    il = _amihud(close, volume, 63, min_periods=21)
    out = il - il.shift(21)
    return out


def f45_arkl_011_amihud_ratio_21d_over_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(_amihud(close, volume, 21, min_periods=7), _amihud(close, volume, 252, min_periods=84))
    return out


def f45_arkl_012_amihud_upside_only_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rp = r.where(r > 0, 0.0)
    dv = (close * volume).replace(0, np.nan)
    u = _safe_div(rp, dv)
    out = u.rolling(63, min_periods=21).mean()
    return out


def f45_arkl_013_amihud_downside_only_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rn = (-r).where(r < 0, 0.0)
    dv = (close * volume).replace(0, np.nan)
    d = _safe_div(rn, dv)
    out = d.rolling(63, min_periods=21).mean()
    return out


def f45_arkl_014_amihud_downside_minus_upside_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rp = r.where(r > 0, 0.0); rn = (-r).where(r < 0, 0.0)
    dv = (close * volume).replace(0, np.nan)
    out = (_safe_div(rn, dv).rolling(63, min_periods=21).mean() - _safe_div(rp, dv).rolling(63, min_periods=21).mean())
    return out


def f45_arkl_015_amihud_sq_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r2 = (_safe_log(close).diff() ** 2)
    dv = (close * volume).replace(0, np.nan)
    out = _safe_div(r2, dv).rolling(63, min_periods=21).mean()
    return out


def f45_arkl_016_roll_spread_21d(close: pd.Series) -> pd.Series:
    out = _roll_spread(close, 21, min_periods=7)
    return out


def f45_arkl_017_roll_spread_63d(close: pd.Series) -> pd.Series:
    out = _roll_spread(close, 63, min_periods=21)
    return out


def f45_arkl_018_roll_spread_252d(close: pd.Series) -> pd.Series:
    out = _roll_spread(close, 252, min_periods=84)
    return out


def f45_arkl_019_roll_spread_504d(close: pd.Series) -> pd.Series:
    out = _roll_spread(close, 504, min_periods=168)
    return out


def f45_arkl_020_roll_spread_norm_close_63d(close: pd.Series) -> pd.Series:
    out = _safe_div(_roll_spread(close, 63, min_periods=21), close)
    return out


def f45_arkl_021_roll_spread_log_63d(close: pd.Series) -> pd.Series:
    out = _safe_log(_roll_spread(close, 63, min_periods=21) + 1e-12)
    return out


def f45_arkl_022_roll_cov_dp_lag1_63d(close: pd.Series) -> pd.Series:
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
    out = dp.rolling(63, min_periods=21).apply(_f, raw=True)
    return out


def f45_arkl_023_roll_cov_negative_fraction_63d_in_252d(close: pd.Series) -> pd.Series:
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
    neg = (c < 0).astype(float).where(c.notna(), np.nan)
    out = neg.rolling(252, min_periods=84).mean()
    return out


def f45_arkl_024_roll_spread_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    out = _rolling_pct_rank(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    return out


def f45_arkl_025_roll_spread_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    out = _rolling_zscore(_roll_spread(close, 63, min_periods=21), 252, min_periods=84)
    return out


def f45_arkl_026_roll_spread_ratio_21d_over_252d(close: pd.Series) -> pd.Series:
    out = _safe_div(_roll_spread(close, 21, min_periods=7), _roll_spread(close, 252, min_periods=84))
    return out


def f45_arkl_027_roll_spread_slope_21d_63d(close: pd.Series) -> pd.Series:
    s = _roll_spread(close, 63, min_periods=21)
    out = s - s.shift(21)
    return out


def f45_arkl_028_roll_half_spread_pct_63d(close: pd.Series) -> pd.Series:
    out = 0.5 * _safe_div(_roll_spread(close, 63, min_periods=21), close)
    return out


def f45_arkl_029_roll_spread_logclose_63d(close: pd.Series) -> pd.Series:
    out = _roll_spread(_safe_log(close), 63, min_periods=21)
    return out


def f45_arkl_030_roll_spread_1d_avg_21d(close: pd.Series) -> pd.Series:
    dp = close.diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 3:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        a = v[1:]; b = v[:-1]
        c = float(np.mean((a - a.mean()) * (b - b.mean())))
        if c >= 0:
            return np.nan
        return 2.0 * np.sqrt(-c)
    # 3-bar minimum and 21-bar rolling avg
    spr3 = dp.rolling(3, min_periods=3).apply(_f, raw=True)
    out = spr3.rolling(21, min_periods=7).mean()
    return out


def f45_arkl_031_kyle_lambda_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _kyle_lambda(close, volume, 21, min_periods=7)
    return out


def f45_arkl_032_kyle_lambda_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _kyle_lambda(close, volume, 63, min_periods=21)
    return out


def f45_arkl_033_kyle_lambda_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _kyle_lambda(close, volume, 252, min_periods=84)
    return out


def f45_arkl_034_kyle_lambda_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _kyle_lambda(close, volume, 504, min_periods=168)
    return out


def f45_arkl_035_kyle_lambda_zscore_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _rolling_zscore(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    return out


def f45_arkl_036_kyle_lambda_pct_rank_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    return out


def f45_arkl_037_kyle_lambda_ratio_21d_over_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_div(_kyle_lambda(close, volume, 21, min_periods=7), _kyle_lambda(close, volume, 252, min_periods=84))
    return out


def f45_arkl_038_kyle_lambda_upside_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rp = r.where(r > 0, 0.0)
    dv = (close * volume).clip(lower=1.0)
    out = _safe_div(rp, np.sqrt(dv)).rolling(63, min_periods=21).mean()
    return out


def f45_arkl_039_kyle_lambda_downside_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rn = (-r).where(r < 0, 0.0)
    dv = (close * volume).clip(lower=1.0)
    out = _safe_div(rn, np.sqrt(dv)).rolling(63, min_periods=21).mean()
    return out


def f45_arkl_040_kyle_lambda_down_minus_up_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rp = r.where(r > 0, 0.0); rn = (-r).where(r < 0, 0.0)
    dv = (close * volume).clip(lower=1.0)
    out = (_safe_div(rn, np.sqrt(dv)).rolling(63, min_periods=21).mean() - _safe_div(rp, np.sqrt(dv)).rolling(63, min_periods=21).mean())
    return out


def f45_arkl_041_kyle_lambda_log_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_log(_kyle_lambda(close, volume, 63, min_periods=21) + 1e-15)
    return out


def f45_arkl_042_kyle_lambda_slope_21d_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _kyle_lambda(close, volume, 63, min_periods=21)
    out = k - k.shift(21)
    return out


def f45_arkl_043_kyle_x_amihud_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _kyle_lambda(close, volume, 63, min_periods=21) * _amihud(close, volume, 63, min_periods=21)
    return out


def f45_arkl_044_kyle_lambda_top_quintile_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rk = _rolling_pct_rank(_kyle_lambda(close, volume, 63, min_periods=21), 252, min_periods=84)
    out = (rk > 0.8).astype(float).where(rk.notna(), np.nan)
    return out


def f45_arkl_045_kyle_lambda_std_63d_over_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _kyle_lambda(close, volume, 63, min_periods=21)
    out = k.rolling(63, min_periods=21).std()
    return out


def f45_arkl_046_corwin_schultz_spread_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _corwin_schultz(high, low, 21, min_periods=7)
    return out


def f45_arkl_047_corwin_schultz_spread_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _corwin_schultz(high, low, 63, min_periods=21)
    return out


def f45_arkl_048_corwin_schultz_spread_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _corwin_schultz(high, low, 252, min_periods=84)
    return out


def f45_arkl_049_cs_spread_norm_close_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(_corwin_schultz(high, low, 63, min_periods=21), close)
    return out


def f45_arkl_050_cs_spread_zscore_63d_in_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _rolling_zscore(_corwin_schultz(high, low, 63, min_periods=21), 252, min_periods=84)
    return out


def f45_arkl_051_hl_range_pct_close_1d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(high - low, close)
    return out


def f45_arkl_052_hl_range_pct_close_21d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close)
    out = rp.rolling(21, min_periods=7).mean()
    return out


def f45_arkl_053_hl_range_pct_close_63d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close)
    out = rp.rolling(63, min_periods=21).mean()
    return out


def f45_arkl_054_hl_range_pct_zscore_63d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close).rolling(63, min_periods=21).mean()
    out = _rolling_zscore(rp, 252, min_periods=84)
    return out


def f45_arkl_055_eff_half_spread_proxy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = (_safe_div(high - low, 2.0 * close)).rolling(21, min_periods=7).mean()
    return out


def f45_arkl_056_eff_half_spread_proxy_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = (_safe_div(high - low, 2.0 * close)).rolling(63, min_periods=21).mean()
    return out


def f45_arkl_057_hl_range_pct_rank_63d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close).rolling(63, min_periods=21).mean()
    out = _rolling_pct_rank(rp, 252, min_periods=84)
    return out


def f45_arkl_058_cs_over_roll_spread_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cs = _corwin_schultz(high, low, 63, min_periods=21)
    rl = _roll_spread(close, 63, min_periods=21)
    out = _safe_div(cs, rl)
    return out


def f45_arkl_059_cs_minus_amihud_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cs_z = _rolling_zscore(_corwin_schultz(high, low, 63, min_periods=21), 252, min_periods=84)
    am_z = _rolling_zscore(_amihud(close, volume, 63, min_periods=21), 252, min_periods=84)
    out = cs_z - am_z
    return out


def f45_arkl_060_zero_change_bars_density_63d(close: pd.Series) -> pd.Series:
    no_change = (close.diff().abs() < 1e-10).astype(float).where(close.notna() & close.shift(1).notna(), np.nan)
    out = no_change.rolling(63, min_periods=21).mean()
    return out


def f45_arkl_061_vpin_proxy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = _safe_div(sv.rolling(21, min_periods=7).sum().abs(), volume.rolling(21, min_periods=7).sum())
    return out


def f45_arkl_062_vpin_proxy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    return out


def f45_arkl_063_vpin_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = _safe_div(sv.rolling(252, min_periods=84).sum().abs(), volume.rolling(252, min_periods=84).sum())
    return out


def f45_arkl_064_vpin_zscore_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    out = _rolling_zscore(v, 252, min_periods=84)
    return out


def f45_arkl_065_vpin_pct_rank_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    out = _rolling_pct_rank(v, 252, min_periods=84)
    return out


def f45_arkl_066_vpin_slope_21d_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    out = v - v.shift(21)
    return out


def f45_arkl_067_buy_over_sell_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    buy = (volume * (sgn > 0)).rolling(21, min_periods=7).sum()
    sell = (volume * (sgn < 0)).rolling(21, min_periods=7).sum()
    out = _safe_div(buy, sell.replace(0, np.nan))
    return out


def f45_arkl_068_buy_over_sell_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    buy = (volume * (sgn > 0)).rolling(63, min_periods=21).sum()
    sell = (volume * (sgn < 0)).rolling(63, min_periods=21).sum()
    out = _safe_div(buy, sell.replace(0, np.nan))
    return out


def f45_arkl_069_signed_vol_cum_drift_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = sv.rolling(21, min_periods=7).sum()
    return out


def f45_arkl_070_signed_vol_drift_norm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = _safe_div(sv.rolling(63, min_periods=21).sum(), volume.rolling(63, min_periods=21).sum())
    return out


def f45_arkl_071_vpin_top_decile_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    rk = _rolling_pct_rank(v, 252, min_periods=84)
    out = (rk > 0.9).astype(float).where(rk.notna(), np.nan)
    return out


def f45_arkl_072_vpin_21d_minus_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v21 = _safe_div(sv.rolling(21, min_periods=7).sum().abs(), volume.rolling(21, min_periods=7).sum())
    v63 = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    out = v21 - v63
    return out


def f45_arkl_073_directional_vpin_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    out = _safe_div(sv.rolling(21, min_periods=7).sum(), volume.rolling(21, min_periods=7).sum())
    return out


def f45_arkl_074_vpin_above_05_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    hi = (v > 0.5).astype(int).where(v.notna(), 0)
    block = (hi != hi.shift(1)).fillna(False).cumsum()
    st = hi.groupby(block).cumcount().astype(float)
    out = (st * (hi > 0)).where(v.notna(), np.nan)
    return out


def f45_arkl_075_vpin_x_amihud_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    sv = sgn * volume
    v = _safe_div(sv.rolling(63, min_periods=21).sum().abs(), volume.rolling(63, min_periods=21).sum())
    out = v * _amihud(close, volume, 63, min_periods=21)
    return out


# ============================================================
#                         REGISTRY 001_075 (base)
# ============================================================

AMIHUD_ROLL_KYLE_LIQUIDITY_BASE_REGISTRY_001_075 = {
    "f45_arkl_001_amihud_illiq_5d": {"inputs": ["close", "volume"], "func": f45_arkl_001_amihud_illiq_5d},
    "f45_arkl_002_amihud_illiq_21d": {"inputs": ["close", "volume"], "func": f45_arkl_002_amihud_illiq_21d},
    "f45_arkl_003_amihud_illiq_63d": {"inputs": ["close", "volume"], "func": f45_arkl_003_amihud_illiq_63d},
    "f45_arkl_004_amihud_illiq_252d": {"inputs": ["close", "volume"], "func": f45_arkl_004_amihud_illiq_252d},
    "f45_arkl_005_amihud_illiq_504d": {"inputs": ["close", "volume"], "func": f45_arkl_005_amihud_illiq_504d},
    "f45_arkl_006_amihud_zscore_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_006_amihud_zscore_63d_in_252d},
    "f45_arkl_007_amihud_robust_z_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_007_amihud_robust_z_63d_in_252d},
    "f45_arkl_008_amihud_pct_rank_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_008_amihud_pct_rank_63d_in_252d},
    "f45_arkl_009_amihud_log_63d": {"inputs": ["close", "volume"], "func": f45_arkl_009_amihud_log_63d},
    "f45_arkl_010_amihud_slope_21d_63d": {"inputs": ["close", "volume"], "func": f45_arkl_010_amihud_slope_21d_63d},
    "f45_arkl_011_amihud_ratio_21d_over_252d": {"inputs": ["close", "volume"], "func": f45_arkl_011_amihud_ratio_21d_over_252d},
    "f45_arkl_012_amihud_upside_only_63d": {"inputs": ["close", "volume"], "func": f45_arkl_012_amihud_upside_only_63d},
    "f45_arkl_013_amihud_downside_only_63d": {"inputs": ["close", "volume"], "func": f45_arkl_013_amihud_downside_only_63d},
    "f45_arkl_014_amihud_downside_minus_upside_63d": {"inputs": ["close", "volume"], "func": f45_arkl_014_amihud_downside_minus_upside_63d},
    "f45_arkl_015_amihud_sq_return_63d": {"inputs": ["close", "volume"], "func": f45_arkl_015_amihud_sq_return_63d},
    "f45_arkl_016_roll_spread_21d": {"inputs": ["close"], "func": f45_arkl_016_roll_spread_21d},
    "f45_arkl_017_roll_spread_63d": {"inputs": ["close"], "func": f45_arkl_017_roll_spread_63d},
    "f45_arkl_018_roll_spread_252d": {"inputs": ["close"], "func": f45_arkl_018_roll_spread_252d},
    "f45_arkl_019_roll_spread_504d": {"inputs": ["close"], "func": f45_arkl_019_roll_spread_504d},
    "f45_arkl_020_roll_spread_norm_close_63d": {"inputs": ["close"], "func": f45_arkl_020_roll_spread_norm_close_63d},
    "f45_arkl_021_roll_spread_log_63d": {"inputs": ["close"], "func": f45_arkl_021_roll_spread_log_63d},
    "f45_arkl_022_roll_cov_dp_lag1_63d": {"inputs": ["close"], "func": f45_arkl_022_roll_cov_dp_lag1_63d},
    "f45_arkl_023_roll_cov_negative_fraction_63d_in_252d": {"inputs": ["close"], "func": f45_arkl_023_roll_cov_negative_fraction_63d_in_252d},
    "f45_arkl_024_roll_spread_pct_rank_63d_in_252d": {"inputs": ["close"], "func": f45_arkl_024_roll_spread_pct_rank_63d_in_252d},
    "f45_arkl_025_roll_spread_zscore_63d_in_252d": {"inputs": ["close"], "func": f45_arkl_025_roll_spread_zscore_63d_in_252d},
    "f45_arkl_026_roll_spread_ratio_21d_over_252d": {"inputs": ["close"], "func": f45_arkl_026_roll_spread_ratio_21d_over_252d},
    "f45_arkl_027_roll_spread_slope_21d_63d": {"inputs": ["close"], "func": f45_arkl_027_roll_spread_slope_21d_63d},
    "f45_arkl_028_roll_half_spread_pct_63d": {"inputs": ["close"], "func": f45_arkl_028_roll_half_spread_pct_63d},
    "f45_arkl_029_roll_spread_logclose_63d": {"inputs": ["close"], "func": f45_arkl_029_roll_spread_logclose_63d},
    "f45_arkl_030_roll_spread_1d_avg_21d": {"inputs": ["close"], "func": f45_arkl_030_roll_spread_1d_avg_21d},
    "f45_arkl_031_kyle_lambda_21d": {"inputs": ["close", "volume"], "func": f45_arkl_031_kyle_lambda_21d},
    "f45_arkl_032_kyle_lambda_63d": {"inputs": ["close", "volume"], "func": f45_arkl_032_kyle_lambda_63d},
    "f45_arkl_033_kyle_lambda_252d": {"inputs": ["close", "volume"], "func": f45_arkl_033_kyle_lambda_252d},
    "f45_arkl_034_kyle_lambda_504d": {"inputs": ["close", "volume"], "func": f45_arkl_034_kyle_lambda_504d},
    "f45_arkl_035_kyle_lambda_zscore_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_035_kyle_lambda_zscore_63d_in_252d},
    "f45_arkl_036_kyle_lambda_pct_rank_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_036_kyle_lambda_pct_rank_63d_in_252d},
    "f45_arkl_037_kyle_lambda_ratio_21d_over_252d": {"inputs": ["close", "volume"], "func": f45_arkl_037_kyle_lambda_ratio_21d_over_252d},
    "f45_arkl_038_kyle_lambda_upside_63d": {"inputs": ["close", "volume"], "func": f45_arkl_038_kyle_lambda_upside_63d},
    "f45_arkl_039_kyle_lambda_downside_63d": {"inputs": ["close", "volume"], "func": f45_arkl_039_kyle_lambda_downside_63d},
    "f45_arkl_040_kyle_lambda_down_minus_up_63d": {"inputs": ["close", "volume"], "func": f45_arkl_040_kyle_lambda_down_minus_up_63d},
    "f45_arkl_041_kyle_lambda_log_63d": {"inputs": ["close", "volume"], "func": f45_arkl_041_kyle_lambda_log_63d},
    "f45_arkl_042_kyle_lambda_slope_21d_63d": {"inputs": ["close", "volume"], "func": f45_arkl_042_kyle_lambda_slope_21d_63d},
    "f45_arkl_043_kyle_x_amihud_composite_63d": {"inputs": ["close", "volume"], "func": f45_arkl_043_kyle_x_amihud_composite_63d},
    "f45_arkl_044_kyle_lambda_top_quintile_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_044_kyle_lambda_top_quintile_63d_in_252d},
    "f45_arkl_045_kyle_lambda_std_63d_over_63d": {"inputs": ["close", "volume"], "func": f45_arkl_045_kyle_lambda_std_63d_over_63d},
    "f45_arkl_046_corwin_schultz_spread_21d": {"inputs": ["high", "low"], "func": f45_arkl_046_corwin_schultz_spread_21d},
    "f45_arkl_047_corwin_schultz_spread_63d": {"inputs": ["high", "low"], "func": f45_arkl_047_corwin_schultz_spread_63d},
    "f45_arkl_048_corwin_schultz_spread_252d": {"inputs": ["high", "low"], "func": f45_arkl_048_corwin_schultz_spread_252d},
    "f45_arkl_049_cs_spread_norm_close_63d": {"inputs": ["high", "low", "close"], "func": f45_arkl_049_cs_spread_norm_close_63d},
    "f45_arkl_050_cs_spread_zscore_63d_in_252d": {"inputs": ["high", "low"], "func": f45_arkl_050_cs_spread_zscore_63d_in_252d},
    "f45_arkl_051_hl_range_pct_close_1d": {"inputs": ["high", "low", "close"], "func": f45_arkl_051_hl_range_pct_close_1d},
    "f45_arkl_052_hl_range_pct_close_21d_mean": {"inputs": ["high", "low", "close"], "func": f45_arkl_052_hl_range_pct_close_21d_mean},
    "f45_arkl_053_hl_range_pct_close_63d_mean": {"inputs": ["high", "low", "close"], "func": f45_arkl_053_hl_range_pct_close_63d_mean},
    "f45_arkl_054_hl_range_pct_zscore_63d_in_252d": {"inputs": ["high", "low", "close"], "func": f45_arkl_054_hl_range_pct_zscore_63d_in_252d},
    "f45_arkl_055_eff_half_spread_proxy_21d": {"inputs": ["high", "low", "close"], "func": f45_arkl_055_eff_half_spread_proxy_21d},
    "f45_arkl_056_eff_half_spread_proxy_63d": {"inputs": ["high", "low", "close"], "func": f45_arkl_056_eff_half_spread_proxy_63d},
    "f45_arkl_057_hl_range_pct_rank_63d_in_252d": {"inputs": ["high", "low", "close"], "func": f45_arkl_057_hl_range_pct_rank_63d_in_252d},
    "f45_arkl_058_cs_over_roll_spread_63d": {"inputs": ["high", "low", "close"], "func": f45_arkl_058_cs_over_roll_spread_63d},
    "f45_arkl_059_cs_minus_amihud_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": f45_arkl_059_cs_minus_amihud_zscore_63d},
    "f45_arkl_060_zero_change_bars_density_63d": {"inputs": ["close"], "func": f45_arkl_060_zero_change_bars_density_63d},
    "f45_arkl_061_vpin_proxy_21d": {"inputs": ["close", "volume"], "func": f45_arkl_061_vpin_proxy_21d},
    "f45_arkl_062_vpin_proxy_63d": {"inputs": ["close", "volume"], "func": f45_arkl_062_vpin_proxy_63d},
    "f45_arkl_063_vpin_proxy_252d": {"inputs": ["close", "volume"], "func": f45_arkl_063_vpin_proxy_252d},
    "f45_arkl_064_vpin_zscore_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_064_vpin_zscore_63d_in_252d},
    "f45_arkl_065_vpin_pct_rank_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_065_vpin_pct_rank_63d_in_252d},
    "f45_arkl_066_vpin_slope_21d_63d": {"inputs": ["close", "volume"], "func": f45_arkl_066_vpin_slope_21d_63d},
    "f45_arkl_067_buy_over_sell_vol_ratio_21d": {"inputs": ["close", "volume"], "func": f45_arkl_067_buy_over_sell_vol_ratio_21d},
    "f45_arkl_068_buy_over_sell_vol_ratio_63d": {"inputs": ["close", "volume"], "func": f45_arkl_068_buy_over_sell_vol_ratio_63d},
    "f45_arkl_069_signed_vol_cum_drift_21d": {"inputs": ["close", "volume"], "func": f45_arkl_069_signed_vol_cum_drift_21d},
    "f45_arkl_070_signed_vol_drift_norm_63d": {"inputs": ["close", "volume"], "func": f45_arkl_070_signed_vol_drift_norm_63d},
    "f45_arkl_071_vpin_top_decile_63d_in_252d": {"inputs": ["close", "volume"], "func": f45_arkl_071_vpin_top_decile_63d_in_252d},
    "f45_arkl_072_vpin_21d_minus_63d": {"inputs": ["close", "volume"], "func": f45_arkl_072_vpin_21d_minus_63d},
    "f45_arkl_073_directional_vpin_21d": {"inputs": ["close", "volume"], "func": f45_arkl_073_directional_vpin_21d},
    "f45_arkl_074_vpin_above_05_streak_63d": {"inputs": ["close", "volume"], "func": f45_arkl_074_vpin_above_05_streak_63d},
    "f45_arkl_075_vpin_x_amihud_composite_63d": {"inputs": ["close", "volume"], "func": f45_arkl_075_vpin_x_amihud_composite_63d},
}
