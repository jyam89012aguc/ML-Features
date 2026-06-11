"""
12_high_water_distance — 2nd Derivatives (Features drv2_001-025)
Domain: rate-of-change / velocity of base high-water-mark distance features.
        Each feature computes .diff(n), slope, or pct-change of a base HWM concept.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def hwd_drv2_001_log_dist_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first difference of log-distance from ATH (velocity of HWM distress)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return ld.diff(5)


def hwd_drv2_002_log_dist_ath_21d_diff(close: pd.Series) -> pd.Series:
    """21-day first difference of log-distance from ATH (monthly worsening pace)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return ld.diff(_TD_MON)


def hwd_drv2_003_pct_below_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of pct-below-ATH (velocity of price-vs-HWM deterioration)."""
    pct = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return pct.diff(5)


def hwd_drv2_004_regain_multiple_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ATH regain multiple (how fast recovery gap is growing)."""
    rm = _safe_div(_expanding_hwm(close), close)
    return rm.diff(5)


def hwd_drv2_005_days_since_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-ATH (normally +5 unless new ATH is set)."""
    d = _days_since_expanding_max(close)
    return d.diff(5)


def hwd_drv2_006_log_dist_1y_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-distance from 1-year HWM."""
    ld = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    return ld.diff(5)


def hwd_drv2_007_log_dist_2y_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of log-distance from 2-year HWM."""
    ld = _log_safe(_rolling_max(close, 504)) - _log_safe(close)
    return ld.diff(_TD_MON)


def hwd_drv2_008_frac_history_below_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of fraction-of-history-below-ATH (pace of time accumulation below)."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    frac = below.expanding(min_periods=1).mean()
    return frac.diff(5)


def hwd_drv2_009_frac_252d_below_ath_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day fraction-below-ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    frac = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5)


def hwd_drv2_010_staleness_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of staleness score (log_dist_ATH * log(days_since_ATH+1))."""
    ld   = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    dlog = np.log1p(_days_since_expanding_max(close).fillna(0))
    stale = ld * dlog
    return stale.diff(5)


def hwd_drv2_011_regain_multiple_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of ATH regain multiple (monthly pace of recovery gap widening)."""
    rm = _safe_div(_expanding_hwm(close), close)
    return rm.diff(_TD_MON)


def hwd_drv2_012_log_dist_ath_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of log-dist-from-ATH (acceleration of trend)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    sl = _linslope(ld, _TD_MON)
    return sl.diff(5)


def hwd_drv2_013_log_dist_ath_ewm21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day EMA of log-distance from ATH."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ema = _ewm_mean(ld, _TD_MON)
    return ema.diff(5)


def hwd_drv2_014_log_dist_ath_vol_adj_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of volatility-adjusted log-distance from ATH."""
    ld  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    va  = _safe_div(ld, vol)
    return va.diff(5)


def hwd_drv2_015_pct_below_1y_hwm_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day slope of pct-below-1y-HWM (2nd-order slope change)."""
    pct = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    sl  = _linslope(pct, _TD_MON)
    return sl.diff(5)


def hwd_drv2_016_composite_multiscale_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite multi-scale HWM distance (0.4 ATH+0.3 1y+0.2 2y+0.1 5y)."""
    dath = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    d1y  = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    d2y  = _log_safe(_rolling_max(close, 504)) - _log_safe(close)
    d5y  = _log_safe(_rolling_max(close, 1260)) - _log_safe(close)
    comp = 0.4 * dath + 0.3 * d1y + 0.2 * d2y + 0.1 * d5y
    return comp.diff(5)


def hwd_drv2_017_new_hwm_count_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of new-ATH count in trailing 252d (pace of new-high formation)."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    cnt = _rolling_sum(at_peak, _TD_YEAR)
    return cnt.diff(5)


def hwd_drv2_018_frac_252d_at_new_hwm_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of fraction-of-252d-at-new-ATH (pace of new-high frequency change)."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    frac = _rolling_mean(at_peak, _TD_YEAR)
    return frac.diff(5)


def hwd_drv2_019_log_dist_ath_pct_chg_21d(close: pd.Series) -> pd.Series:
    """21-day percent change in log-dist-from-ATH (relative worsening rate)."""
    ld = (_log_safe(_expanding_hwm(close)) - _log_safe(close)).clip(lower=_EPS)
    return _safe_div(ld - ld.shift(_TD_MON), ld.shift(_TD_MON).abs().replace(0, np.nan))


def hwd_drv2_020_regain_multiple_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of ATH regain multiple."""
    rm = _safe_div(_expanding_hwm(close), close)
    sl = _linslope(rm, _TD_MON)
    return sl.diff(5)


def hwd_drv2_021_vol_wtd_log_dist_ath_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted log-distance from ATH (252d window)."""
    ld    = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    v_n   = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    vwld  = _rolling_mean(ld * v_n, _TD_YEAR)
    return vwld.diff(5)


def hwd_drv2_022_days_since_ath_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of days-since-ATH."""
    d  = _days_since_expanding_max(close)
    zs = _zscore_rolling(d, _TD_YEAR)
    return zs.diff(5)


def hwd_drv2_023_dist_x_staleness_slope_21d(close: pd.Series) -> pd.Series:
    """21-day OLS slope of the staleness composite (log_dist * log_days_since_ATH)."""
    ld   = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    dlog = np.log1p(_days_since_expanding_max(close).fillna(0))
    stale = ld * dlog
    return _linslope(stale, _TD_MON)


def hwd_drv2_024_log_dist_ath_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of log-dist-from-ATH."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    zs = _zscore_rolling(ld, _TD_YEAR)
    return zs.diff(5)


def hwd_drv2_025_composite_distress_index_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite HWM distress index (weighted z-scores)."""
    ld_ath  = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ld_1y   = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    d_log   = np.log1p(_days_since_expanding_max(close).fillna(0))
    lr      = _log_safe(_safe_div(_expanding_hwm(close), close))
    d_zs    = _zscore_rolling(d_log, _TD_YEAR)
    ld_zs   = _zscore_rolling(ld_ath, _TD_YEAR)
    ld1y_zs = _zscore_rolling(ld_1y, _TD_YEAR)
    lr_zs   = _zscore_rolling(lr, _TD_YEAR)
    comp    = 0.35 * ld_zs + 0.25 * ld1y_zs + 0.25 * d_zs + 0.15 * lr_zs
    return comp.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

HIGH_WATER_DISTANCE_REGISTRY_2ND_DERIVATIVES = {
    "hwd_drv2_001_log_dist_ath_5d_diff":              {"inputs": ["close"], "func": hwd_drv2_001_log_dist_ath_5d_diff},
    "hwd_drv2_002_log_dist_ath_21d_diff":             {"inputs": ["close"], "func": hwd_drv2_002_log_dist_ath_21d_diff},
    "hwd_drv2_003_pct_below_ath_5d_diff":             {"inputs": ["close"], "func": hwd_drv2_003_pct_below_ath_5d_diff},
    "hwd_drv2_004_regain_multiple_5d_diff":           {"inputs": ["close"], "func": hwd_drv2_004_regain_multiple_5d_diff},
    "hwd_drv2_005_days_since_ath_5d_diff":            {"inputs": ["close"], "func": hwd_drv2_005_days_since_ath_5d_diff},
    "hwd_drv2_006_log_dist_1y_5d_diff":               {"inputs": ["close"], "func": hwd_drv2_006_log_dist_1y_5d_diff},
    "hwd_drv2_007_log_dist_2y_21d_diff":              {"inputs": ["close"], "func": hwd_drv2_007_log_dist_2y_21d_diff},
    "hwd_drv2_008_frac_history_below_ath_5d_diff":    {"inputs": ["close"], "func": hwd_drv2_008_frac_history_below_ath_5d_diff},
    "hwd_drv2_009_frac_252d_below_ath_5d_diff":       {"inputs": ["close"], "func": hwd_drv2_009_frac_252d_below_ath_5d_diff},
    "hwd_drv2_010_staleness_score_5d_diff":           {"inputs": ["close"], "func": hwd_drv2_010_staleness_score_5d_diff},
    "hwd_drv2_011_regain_multiple_21d_diff":          {"inputs": ["close"], "func": hwd_drv2_011_regain_multiple_21d_diff},
    "hwd_drv2_012_log_dist_ath_slope_21d_5d_diff":    {"inputs": ["close"], "func": hwd_drv2_012_log_dist_ath_slope_21d_5d_diff},
    "hwd_drv2_013_log_dist_ath_ewm21_5d_diff":        {"inputs": ["close"], "func": hwd_drv2_013_log_dist_ath_ewm21_5d_diff},
    "hwd_drv2_014_log_dist_ath_vol_adj_5d_diff":      {"inputs": ["close"], "func": hwd_drv2_014_log_dist_ath_vol_adj_5d_diff},
    "hwd_drv2_015_pct_below_1y_hwm_slope_21d_5d_diff":{"inputs": ["close"], "func": hwd_drv2_015_pct_below_1y_hwm_slope_21d_5d_diff},
    "hwd_drv2_016_composite_multiscale_5d_diff":      {"inputs": ["close"], "func": hwd_drv2_016_composite_multiscale_5d_diff},
    "hwd_drv2_017_new_hwm_count_252d_5d_diff":        {"inputs": ["close"], "func": hwd_drv2_017_new_hwm_count_252d_5d_diff},
    "hwd_drv2_018_frac_252d_at_new_hwm_5d_diff":      {"inputs": ["close"], "func": hwd_drv2_018_frac_252d_at_new_hwm_5d_diff},
    "hwd_drv2_019_log_dist_ath_pct_chg_21d":          {"inputs": ["close"], "func": hwd_drv2_019_log_dist_ath_pct_chg_21d},
    "hwd_drv2_020_regain_multiple_slope_21d_5d_diff":  {"inputs": ["close"], "func": hwd_drv2_020_regain_multiple_slope_21d_5d_diff},
    "hwd_drv2_021_vol_wtd_log_dist_ath_5d_diff":      {"inputs": ["close", "volume"], "func": hwd_drv2_021_vol_wtd_log_dist_ath_5d_diff},
    "hwd_drv2_022_days_since_ath_zscore_5d_diff":     {"inputs": ["close"], "func": hwd_drv2_022_days_since_ath_zscore_5d_diff},
    "hwd_drv2_023_dist_x_staleness_slope_21d":        {"inputs": ["close"], "func": hwd_drv2_023_dist_x_staleness_slope_21d},
    "hwd_drv2_024_log_dist_ath_zscore_252d_5d_diff":  {"inputs": ["close"], "func": hwd_drv2_024_log_dist_ath_zscore_252d_5d_diff},
    "hwd_drv2_025_composite_distress_index_5d_diff":  {"inputs": ["close"], "func": hwd_drv2_025_composite_distress_index_5d_diff},
}
