"""
09_price_compression — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative compression features (acceleration of acceleration)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes .diff(n), slope, or pct-change of a 2nd-derivative concept.
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
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _true_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(arr):
        n = len(arr)
        if n < max(2, w // 2):
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── Helper: compute 2nd-derivative intermediates ──────────────────────────────

def _bbw_diff_5d(close: pd.Series) -> pd.Series:
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return bbw.diff(_TD_WEEK)


def _tr_ratio_21_252_diff_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    tr    = _true_range(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def _log_range_ratio_diff_5d(close: pd.Series) -> pd.Series:
    lr21  = _log_safe(_rolling_max(close, _TD_MON))  - _log_safe(_rolling_min(close, _TD_MON))
    lr252 = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    return _safe_div(lr21, lr252).diff(_TD_WEEK)


def _vol_ratio_21_252_diff_5d(close: pd.Series) -> pd.Series:
    lr   = _log_safe(close).diff(1)
    v21  = lr.rolling(_TD_MON,  min_periods=max(2, _TD_MON  // 2)).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    return _safe_div(v21, v252).diff(_TD_WEEK)


def _inside_bar_frac_diff_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return _rolling_mean(inside, _TD_MON).diff(_TD_WEEK)


def _grand_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    bbw_r = _rolling_rank_pct(bbw21, _TD_YEAR)
    tr    = _true_range(close, high, low)
    tr_r  = _rolling_rank_pct(tr, _TD_YEAR)
    lr21  = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    lr_r  = _rolling_rank_pct(lr21, _TD_YEAR)
    cw21  = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                      _rolling_min(close, _TD_MON))
    cw_r  = _rolling_rank_pct(cw21, _TD_YEAR)
    return (bbw_r + tr_r + lr_r + cw_r) / 4.0


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def pcmp_drv3_001_bbw_diff5d_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d-BB-width) — jerk of BB-width change."""
    return _bbw_diff_5d(close).diff(_TD_WEEK)


def pcmp_drv3_002_bbw_diff5d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of 21d-BB-width) over trailing 21 days."""
    return _linslope(_bbw_diff_5d(close), _TD_MON)


def pcmp_drv3_003_tr_ratio_diff5d_further_diff5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of TR-ratio 21d/252d) — jerk of TR-compression."""
    return _tr_ratio_21_252_diff_5d(close, high, low).diff(_TD_WEEK)


def pcmp_drv3_004_tr_ratio_diff5d_21d_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of TR-ratio 21d/252d) over trailing 21 days."""
    return _linslope(_tr_ratio_21_252_diff_5d(close, high, low), _TD_MON)


def pcmp_drv3_005_log_range_ratio_diff5d_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-range-ratio 21d/252d)."""
    return _log_range_ratio_diff_5d(close).diff(_TD_WEEK)


def pcmp_drv3_006_log_range_ratio_diff5d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of log-range-ratio 21d/252d) over 21 days."""
    return _linslope(_log_range_ratio_diff_5d(close), _TD_MON)


def pcmp_drv3_007_vol_ratio_diff5d_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-ratio 21d/252d) — jerk of vol-compression."""
    return _vol_ratio_21_252_diff_5d(close).diff(_TD_WEEK)


def pcmp_drv3_008_vol_ratio_diff5d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of vol-ratio 21d/252d) over 21 days."""
    return _linslope(_vol_ratio_21_252_diff_5d(close), _TD_MON)


def pcmp_drv3_009_inside_bar_diff5d_further_diff5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of inside-bar fraction) — jerk of coiling signal."""
    return _inside_bar_frac_diff_5d(high, low).diff(_TD_WEEK)


def pcmp_drv3_010_inside_bar_diff5d_21d_slope(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of inside-bar fraction) over 21 days."""
    return _linslope(_inside_bar_frac_diff_5d(high, low), _TD_MON)


def pcmp_drv3_011_grand_composite_diff5d_further_diff5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of grand compression composite)."""
    comp = _grand_composite(close, high, low)
    return comp.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_012_grand_composite_diff5d_21d_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of grand composite) over trailing 21 days."""
    comp = _grand_composite(close, high, low)
    return _linslope(comp.diff(_TD_WEEK), _TD_MON)


def pcmp_drv3_013_bbw_21d_diff_21d_pct_chg_5d(close: pd.Series) -> pd.Series:
    """5-day pct-change of (21-day diff of 21d-BB-width) — relative speed of monthly squeeze."""
    bbw  = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    d21  = bbw.diff(_TD_MON)
    return _safe_div(d21 - d21.shift(_TD_WEEK), d21.shift(_TD_WEEK).abs().clip(lower=_EPS))


def pcmp_drv3_014_tr_ratio_21_252_diff21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of TR-ratio 21d/252d)."""
    tr    = _true_range(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return ratio.diff(_TD_MON).diff(_TD_WEEK)


def pcmp_drv3_015_bbw_pct_rank_diff5d_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d-BB-width percentile rank within 252d)."""
    bbw  = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    rank = _rolling_rank_pct(bbw, _TD_YEAR)
    return rank.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_016_tr_pct_rank_diff5d_further_diff5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of TR percentile rank within 252d)."""
    tr   = _true_range(close, high, low)
    rank = _rolling_rank_pct(tr, _TD_YEAR)
    return rank.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_017_hl_band_zscore_diff5d_further_diff5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of HL-band 252d z-score)."""
    band   = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    zscore = _zscore_rolling(band, _TD_YEAR)
    return zscore.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_018_hl_band_zscore_diff5d_21d_slope(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of (5-day diff of HL-band 252d z-score) over trailing 21 days."""
    band   = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    zscore = _zscore_rolling(band, _TD_YEAR)
    return _linslope(zscore.diff(_TD_WEEK), _TD_MON)


def pcmp_drv3_019_log_range_21d_slope_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (OLS slope of 21d log-range over 21-day window)."""
    lr21  = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    slope = _linslope(lr21, _TD_MON)
    return slope.diff(_TD_WEEK)


def pcmp_drv3_020_vol_ratio_21_63_diff5d_further_diff5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-ratio 21d/63d)."""
    lr  = _log_safe(close).diff(1)
    v21 = lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    v63 = lr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    ratio = _safe_div(v21, v63)
    return ratio.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_021_squeeze_duration_diff5d_further_diff5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of squeeze-duration fraction)."""
    bb_sd = _rolling_std(close, _TD_MON)
    bb_w  = 4.0 * bb_sd
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    in_sq = (bb_w < kc_w).astype(float)
    frac  = _rolling_mean(in_sq, _TD_MON)
    return frac.diff(_TD_WEEK).diff(_TD_WEEK)


def pcmp_drv3_022_channel_comp_21_252_diff21_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 21d/252d HL-band compression ratio)."""
    band21  = _rolling_max(high, _TD_MON)  - _rolling_min(low, _TD_MON)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    ratio   = _safe_div(band21, band252)
    return ratio.diff(_TD_MON).diff(_TD_WEEK)


def pcmp_drv3_023_bbw_diff5d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of (5-day diff of 21d-BB-width) within trailing 63-day window."""
    d = _bbw_diff_5d(close)
    return _zscore_rolling(d, _TD_QTR)


def pcmp_drv3_024_tr_ratio_diff5d_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (5-day diff of TR-ratio 21d/252d) within trailing 63-day window."""
    d = _tr_ratio_21_252_diff_5d(close, high, low)
    return _zscore_rolling(d, _TD_QTR)


def pcmp_drv3_025_grand_composite_diff5d_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (5-day diff of grand composite) within trailing 63-day window."""
    d = _grand_composite(close, high, low).diff(_TD_WEEK)
    return _zscore_rolling(d, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    "pcmp_drv3_001_bbw_diff5d_further_diff5d":             {"inputs": ["close"], "func": pcmp_drv3_001_bbw_diff5d_further_diff5d},
    "pcmp_drv3_002_bbw_diff5d_21d_slope":                  {"inputs": ["close"], "func": pcmp_drv3_002_bbw_diff5d_21d_slope},
    "pcmp_drv3_003_tr_ratio_diff5d_further_diff5d":        {"inputs": ["close", "high", "low"], "func": pcmp_drv3_003_tr_ratio_diff5d_further_diff5d},
    "pcmp_drv3_004_tr_ratio_diff5d_21d_slope":             {"inputs": ["close", "high", "low"], "func": pcmp_drv3_004_tr_ratio_diff5d_21d_slope},
    "pcmp_drv3_005_log_range_ratio_diff5d_further_diff5d": {"inputs": ["close"], "func": pcmp_drv3_005_log_range_ratio_diff5d_further_diff5d},
    "pcmp_drv3_006_log_range_ratio_diff5d_21d_slope":      {"inputs": ["close"], "func": pcmp_drv3_006_log_range_ratio_diff5d_21d_slope},
    "pcmp_drv3_007_vol_ratio_diff5d_further_diff5d":       {"inputs": ["close"], "func": pcmp_drv3_007_vol_ratio_diff5d_further_diff5d},
    "pcmp_drv3_008_vol_ratio_diff5d_21d_slope":            {"inputs": ["close"], "func": pcmp_drv3_008_vol_ratio_diff5d_21d_slope},
    "pcmp_drv3_009_inside_bar_diff5d_further_diff5d":      {"inputs": ["high", "low"], "func": pcmp_drv3_009_inside_bar_diff5d_further_diff5d},
    "pcmp_drv3_010_inside_bar_diff5d_21d_slope":           {"inputs": ["high", "low"], "func": pcmp_drv3_010_inside_bar_diff5d_21d_slope},
    "pcmp_drv3_011_grand_composite_diff5d_further_diff5d": {"inputs": ["close", "high", "low"], "func": pcmp_drv3_011_grand_composite_diff5d_further_diff5d},
    "pcmp_drv3_012_grand_composite_diff5d_21d_slope":      {"inputs": ["close", "high", "low"], "func": pcmp_drv3_012_grand_composite_diff5d_21d_slope},
    "pcmp_drv3_013_bbw_21d_diff_21d_pct_chg_5d":          {"inputs": ["close"], "func": pcmp_drv3_013_bbw_21d_diff_21d_pct_chg_5d},
    "pcmp_drv3_014_tr_ratio_21_252_diff21_5d_diff":        {"inputs": ["close", "high", "low"], "func": pcmp_drv3_014_tr_ratio_21_252_diff21_5d_diff},
    "pcmp_drv3_015_bbw_pct_rank_diff5d_further_diff5d":    {"inputs": ["close"], "func": pcmp_drv3_015_bbw_pct_rank_diff5d_further_diff5d},
    "pcmp_drv3_016_tr_pct_rank_diff5d_further_diff5d":     {"inputs": ["close", "high", "low"], "func": pcmp_drv3_016_tr_pct_rank_diff5d_further_diff5d},
    "pcmp_drv3_017_hl_band_zscore_diff5d_further_diff5d":  {"inputs": ["high", "low"], "func": pcmp_drv3_017_hl_band_zscore_diff5d_further_diff5d},
    "pcmp_drv3_018_hl_band_zscore_diff5d_21d_slope":       {"inputs": ["high", "low"], "func": pcmp_drv3_018_hl_band_zscore_diff5d_21d_slope},
    "pcmp_drv3_019_log_range_21d_slope_further_diff5d":    {"inputs": ["close"], "func": pcmp_drv3_019_log_range_21d_slope_further_diff5d},
    "pcmp_drv3_020_vol_ratio_21_63_diff5d_further_diff5d": {"inputs": ["close"], "func": pcmp_drv3_020_vol_ratio_21_63_diff5d_further_diff5d},
    "pcmp_drv3_021_squeeze_duration_diff5d_further_diff5d": {"inputs": ["close", "high", "low"], "func": pcmp_drv3_021_squeeze_duration_diff5d_further_diff5d},
    "pcmp_drv3_022_channel_comp_21_252_diff21_5d_diff":    {"inputs": ["high", "low"], "func": pcmp_drv3_022_channel_comp_21_252_diff21_5d_diff},
    "pcmp_drv3_023_bbw_diff5d_zscore_63d":                 {"inputs": ["close"], "func": pcmp_drv3_023_bbw_diff5d_zscore_63d},
    "pcmp_drv3_024_tr_ratio_diff5d_zscore_63d":            {"inputs": ["close", "high", "low"], "func": pcmp_drv3_024_tr_ratio_diff5d_zscore_63d},
    "pcmp_drv3_025_grand_composite_diff5d_zscore_63d":     {"inputs": ["close", "high", "low"], "func": pcmp_drv3_025_grand_composite_diff5d_zscore_63d},
}
