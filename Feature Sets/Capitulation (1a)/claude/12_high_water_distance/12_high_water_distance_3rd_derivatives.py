"""
12_high_water_distance — 3rd Derivatives (Features drv3_001-025)
Domain: rate-of-change of 2nd-derivative HWM features — acceleration of the velocity
        of high-water-mark distance changes. Each feature applies another .diff(n),
        slope, or pct-change to a 2nd-derivative concept.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _expanding_hwm(s: pd.Series) -> pd.Series:
    """Expanding (all-time) high-water mark."""
    return s.expanding(min_periods=1).max()


def _days_since_expanding_max(s: pd.Series) -> pd.Series:
    """Number of bars elapsed since the expanding-window maximum was last set."""
    hwm = _expanding_hwm(s)
    at_peak = (s >= hwm).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _days_since_rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars elapsed since the rolling-w maximum was last set."""
    roll_max = _rolling_max(s, w)
    at_peak = (s >= roll_max).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        xm = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - xm)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def hwd_drv3_001_log_dist_ath_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-dist-ATH) — acceleration of worsening velocity."""
    ld  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    v   = ld.diff(5)
    return v.diff(5)


def hwd_drv3_002_log_dist_ath_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of log-dist-ATH) — short-term accel of monthly velocity."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    v  = ld.diff(_TD_MON)
    return v.diff(5)


def hwd_drv3_003_pct_below_ath_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of pct-below-ATH) — second-order price-vs-HWM change."""
    pct = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    v   = pct.diff(5)
    return v.diff(5)


def hwd_drv3_004_regain_multiple_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of ATH regain multiple) — acceleration of gap widening."""
    rm = _safe_div(_expanding_hwm(close), close)
    v  = rm.diff(5)
    return v.diff(5)


def hwd_drv3_005_days_since_ath_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of days-since-ATH) — time accumulation acceleration."""
    d = _days_since_expanding_max(close)
    v = d.diff(5)
    return v.diff(5)


def hwd_drv3_006_log_dist_1y_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-dist from 1-year HWM)."""
    ld = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    v  = ld.diff(5)
    return v.diff(5)


def hwd_drv3_007_staleness_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of staleness score) — acceleration of staleness growth."""
    ld    = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    dlog  = np.log1p(_days_since_expanding_max(close).fillna(0))
    stale = ld * dlog
    v     = stale.diff(5)
    return v.diff(5)


def hwd_drv3_008_frac_252d_below_ath_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d fraction-below-ATH)."""
    hwm   = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    frac  = _rolling_mean(below, _TD_YEAR)
    v     = frac.diff(5)
    return v.diff(5)


def hwd_drv3_009_composite_multiscale_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite multi-scale HWM distance)."""
    dath = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    d1y  = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    d2y  = _log_safe(_rolling_max(close, 504)) - _log_safe(close)
    d5y  = _log_safe(_rolling_max(close, 1260)) - _log_safe(close)
    comp = 0.4 * dath + 0.3 * d1y + 0.2 * d2y + 0.1 * d5y
    v    = comp.diff(5)
    return v.diff(5)


def hwd_drv3_010_log_dist_ath_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day OLS slope of log-dist-ATH)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    sl = _linslope(ld, _TD_MON)
    v  = sl.diff(5)
    return v.diff(5)


def hwd_drv3_011_log_dist_ath_ewm21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day EMA of log-dist-ATH)."""
    ld  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ema = _ewm_mean(ld, _TD_MON)
    v   = ema.diff(5)
    return v.diff(5)


def hwd_drv3_012_log_dist_ath_vol_adj_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-adjusted log-dist-ATH)."""
    ld  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    va  = _safe_div(ld, vol)
    v   = va.diff(5)
    return v.diff(5)


def hwd_drv3_013_regain_multiple_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of regain multiple)."""
    rm = _safe_div(_expanding_hwm(close), close)
    sl = _linslope(rm, _TD_MON)
    v  = sl.diff(5)
    return v.diff(5)


def hwd_drv3_014_log_dist_ath_pct_chg_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day pct-change in log-dist-from-ATH (3rd-order rate)."""
    ld     = (_log_safe(_expanding_hwm(close)) - _log_safe(close)).clip(lower=_EPS)
    pct_chg = _safe_div(ld - ld.shift(_TD_MON), ld.shift(_TD_MON).abs().replace(0, np.nan))
    return pct_chg.diff(5)


def hwd_drv3_015_new_hwm_count_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of new-ATH count in 252d window)."""
    hwm     = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    cnt     = _rolling_sum(at_peak, _TD_YEAR)
    v       = cnt.diff(5)
    return v.diff(5)


def hwd_drv3_016_frac_history_below_ath_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of expanding fraction-below-ATH)."""
    hwm   = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    frac  = below.expanding(min_periods=1).mean()
    v     = frac.diff(5)
    return v.diff(5)


def hwd_drv3_017_log_dist_ath_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d z-score of log-dist-ATH)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    zs = _zscore_rolling(ld, _TD_YEAR)
    v  = zs.diff(5)
    return v.diff(5)


def hwd_drv3_018_days_since_ath_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d z-score of days-since-ATH)."""
    d  = _days_since_expanding_max(close)
    zs = _zscore_rolling(d, _TD_YEAR)
    v  = zs.diff(5)
    return v.diff(5)


def hwd_drv3_019_dist_x_staleness_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of (log_dist_ATH * log_days_since_ATH)."""
    ld    = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    dlog  = np.log1p(_days_since_expanding_max(close).fillna(0))
    stale = ld * dlog
    sl    = _linslope(stale, _TD_MON)
    return sl.diff(5)


def hwd_drv3_020_composite_distress_index_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite distress index)."""
    ld_ath  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ld_1y   = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    d_log   = np.log1p(_days_since_expanding_max(close).fillna(0))
    lr      = _log_safe(_safe_div(_expanding_hwm(close), close))
    d_zs    = _zscore_rolling(d_log, _TD_YEAR)
    ld_zs   = _zscore_rolling(ld_ath, _TD_YEAR)
    ld1y_zs = _zscore_rolling(ld_1y, _TD_YEAR)
    lr_zs   = _zscore_rolling(lr, _TD_YEAR)
    comp    = 0.35 * ld_zs + 0.25 * ld1y_zs + 0.25 * d_zs + 0.15 * lr_zs
    v       = comp.diff(5)
    return v.diff(5)


def hwd_drv3_021_vol_wtd_log_dist_ath_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-weighted log-dist-ATH)."""
    ld   = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    v_n  = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    vwld = _rolling_mean(ld * v_n, _TD_YEAR)
    vel  = vwld.diff(5)
    return vel.diff(5)


def hwd_drv3_022_log_dist_ath_ewm21_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day slope of (21-day EMA of log-dist-ATH)."""
    ld  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ema = _ewm_mean(ld, _TD_MON)
    sl  = _linslope(ema, _TD_MON)
    return sl.diff(5)


def hwd_drv3_023_pct_below_1y_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of pct-below-1y-HWM)."""
    pct = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    sl  = _linslope(pct, _TD_MON)
    v   = sl.diff(5)
    return v.diff(5)


def hwd_drv3_024_log_dist_ath_5d_diff_zscore_252d(close: pd.Series) -> pd.Series:
    """252-day z-score of (5-day diff of log-dist-ATH) — normalized velocity extremity."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    v  = ld.diff(5)
    return _zscore_rolling(v, _TD_YEAR)


def hwd_drv3_025_regain_multiple_5d_diff_zscore_252d(close: pd.Series) -> pd.Series:
    """252-day z-score of (5-day diff of ATH regain multiple) — normalized gap velocity."""
    rm = _safe_div(_expanding_hwm(close), close)
    v  = rm.diff(5)
    return _zscore_rolling(v, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

HIGH_WATER_DISTANCE_REGISTRY_3RD_DERIVATIVES = {
    "hwd_drv3_001_log_dist_ath_5d_diff_5d_diff":              {"inputs": ["close"],          "func": hwd_drv3_001_log_dist_ath_5d_diff_5d_diff},
    "hwd_drv3_002_log_dist_ath_21d_diff_5d_diff":             {"inputs": ["close"],          "func": hwd_drv3_002_log_dist_ath_21d_diff_5d_diff},
    "hwd_drv3_003_pct_below_ath_5d_diff_5d_diff":             {"inputs": ["close"],          "func": hwd_drv3_003_pct_below_ath_5d_diff_5d_diff},
    "hwd_drv3_004_regain_multiple_5d_diff_5d_diff":           {"inputs": ["close"],          "func": hwd_drv3_004_regain_multiple_5d_diff_5d_diff},
    "hwd_drv3_005_days_since_ath_5d_diff_5d_diff":            {"inputs": ["close"],          "func": hwd_drv3_005_days_since_ath_5d_diff_5d_diff},
    "hwd_drv3_006_log_dist_1y_5d_diff_5d_diff":               {"inputs": ["close"],          "func": hwd_drv3_006_log_dist_1y_5d_diff_5d_diff},
    "hwd_drv3_007_staleness_score_5d_diff_5d_diff":           {"inputs": ["close"],          "func": hwd_drv3_007_staleness_score_5d_diff_5d_diff},
    "hwd_drv3_008_frac_252d_below_ath_5d_diff_5d_diff":       {"inputs": ["close"],          "func": hwd_drv3_008_frac_252d_below_ath_5d_diff_5d_diff},
    "hwd_drv3_009_composite_multiscale_5d_diff_5d_diff":      {"inputs": ["close"],          "func": hwd_drv3_009_composite_multiscale_5d_diff_5d_diff},
    "hwd_drv3_010_log_dist_ath_slope_21d_5d_diff_5d_diff":    {"inputs": ["close"],          "func": hwd_drv3_010_log_dist_ath_slope_21d_5d_diff_5d_diff},
    "hwd_drv3_011_log_dist_ath_ewm21_5d_diff_5d_diff":        {"inputs": ["close"],          "func": hwd_drv3_011_log_dist_ath_ewm21_5d_diff_5d_diff},
    "hwd_drv3_012_log_dist_ath_vol_adj_5d_diff_5d_diff":      {"inputs": ["close"],          "func": hwd_drv3_012_log_dist_ath_vol_adj_5d_diff_5d_diff},
    "hwd_drv3_013_regain_multiple_slope_21d_5d_diff_5d_diff": {"inputs": ["close"],          "func": hwd_drv3_013_regain_multiple_slope_21d_5d_diff_5d_diff},
    "hwd_drv3_014_log_dist_ath_pct_chg_21d_5d_diff":          {"inputs": ["close"],          "func": hwd_drv3_014_log_dist_ath_pct_chg_21d_5d_diff},
    "hwd_drv3_015_new_hwm_count_252d_5d_diff_5d_diff":        {"inputs": ["close"],          "func": hwd_drv3_015_new_hwm_count_252d_5d_diff_5d_diff},
    "hwd_drv3_016_frac_history_below_ath_5d_diff_5d_diff":    {"inputs": ["close"],          "func": hwd_drv3_016_frac_history_below_ath_5d_diff_5d_diff},
    "hwd_drv3_017_log_dist_ath_zscore_252d_5d_diff_5d_diff":  {"inputs": ["close"],          "func": hwd_drv3_017_log_dist_ath_zscore_252d_5d_diff_5d_diff},
    "hwd_drv3_018_days_since_ath_zscore_5d_diff_5d_diff":     {"inputs": ["close"],          "func": hwd_drv3_018_days_since_ath_zscore_5d_diff_5d_diff},
    "hwd_drv3_019_dist_x_staleness_slope_21d_5d_diff":        {"inputs": ["close"],          "func": hwd_drv3_019_dist_x_staleness_slope_21d_5d_diff},
    "hwd_drv3_020_composite_distress_index_5d_diff_5d_diff":  {"inputs": ["close"],          "func": hwd_drv3_020_composite_distress_index_5d_diff_5d_diff},
    "hwd_drv3_021_vol_wtd_log_dist_ath_5d_diff_5d_diff":      {"inputs": ["close", "volume"],"func": hwd_drv3_021_vol_wtd_log_dist_ath_5d_diff_5d_diff},
    "hwd_drv3_022_log_dist_ath_ewm21_slope_21d_5d_diff":      {"inputs": ["close"],          "func": hwd_drv3_022_log_dist_ath_ewm21_slope_21d_5d_diff},
    "hwd_drv3_023_pct_below_1y_slope_21d_5d_diff_5d_diff":    {"inputs": ["close"],          "func": hwd_drv3_023_pct_below_1y_slope_21d_5d_diff_5d_diff},
    "hwd_drv3_024_log_dist_ath_5d_diff_zscore_252d":           {"inputs": ["close"],          "func": hwd_drv3_024_log_dist_ath_5d_diff_zscore_252d},
    "hwd_drv3_025_regain_multiple_5d_diff_zscore_252d":        {"inputs": ["close"],          "func": hwd_drv3_025_regain_multiple_5d_diff_zscore_252d},
}
