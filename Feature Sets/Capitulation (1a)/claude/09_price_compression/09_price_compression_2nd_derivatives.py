"""
09_price_compression — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base price-compression features
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes .diff(n), slope, or pct-change of a base-compression concept.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def pcmp_drv2_001_bbw_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first diff of 21-day BB width — speed of BB squeeze."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return bbw.diff(_TD_WEEK)


def pcmp_drv2_002_bbw_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day BB width — monthly change in squeeze level."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return bbw.diff(_TD_MON)


def pcmp_drv2_003_tr_ratio_21_vs_252_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day/252-day ATR ratio — acceleration of TR compression."""
    tr     = _true_range(close, high, low)
    ratio  = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def pcmp_drv2_004_hl_range_ratio_21_vs_252_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day vs 252-day HL/close ratio."""
    hl_frac  = (high - low) / close.replace(0, np.nan)
    ratio    = _safe_div(_rolling_mean(hl_frac, _TD_MON), _rolling_mean(hl_frac, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def pcmp_drv2_005_log_range_ratio_21_vs_252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d log-range ratio — acceleration of log-channel compression."""
    lr21  = _log_safe(_rolling_max(close, _TD_MON))  - _log_safe(_rolling_min(close, _TD_MON))
    lr252 = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    ratio = _safe_div(lr21, lr252)
    return ratio.diff(_TD_WEEK)


def pcmp_drv2_006_vol_ratio_21_vs_252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d realized-vol ratio."""
    lr   = _log_safe(close).diff(1)
    v21  = lr.rolling(_TD_MON,  min_periods=max(2, _TD_MON  // 2)).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    ratio = _safe_div(v21, v252)
    return ratio.diff(_TD_WEEK)


def pcmp_drv2_007_channel_width_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day channel width (max-min)/min."""
    cw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    return cw.diff(_TD_WEEK)


def pcmp_drv2_008_inside_bar_frac_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day inside-bar fraction — acceleration of coiling."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    frac   = _rolling_mean(inside, _TD_MON)
    return frac.diff(_TD_WEEK)


def pcmp_drv2_009_contracting_bar_frac_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day contracting-range-bar fraction."""
    hl   = high - low
    cont = (hl < hl.shift(1)).astype(float)
    frac = _rolling_mean(cont, _TD_MON)
    return frac.diff(_TD_WEEK)


def pcmp_drv2_010_bbw_ratio_21_vs_252_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d/252d BB-width ratio."""
    bbw21  = _safe_div(4.0 * _rolling_std(close, _TD_MON),  _rolling_mean(close, _TD_MON))
    bbw252 = _safe_div(4.0 * _rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    ratio  = _safe_div(bbw21, bbw252)
    return ratio.diff(_TD_MON)


def pcmp_drv2_011_bbw_21d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day BB width over trailing 21 days (trend of squeeze)."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _linslope(bbw, _TD_MON)


def pcmp_drv2_012_tr_ratio_21_252_21d_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21d/252d ATR ratio over trailing 21 days."""
    tr    = _true_range(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return _linslope(ratio, _TD_MON)


def pcmp_drv2_013_vol_ratio_5d_vs_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/252d realized-vol ratio — acceleration of short-term compression."""
    lr  = _log_safe(close).diff(1)
    v5  = lr.rolling(_TD_WEEK, min_periods=2).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    return _safe_div(v5, v252).diff(_TD_WEEK)


def pcmp_drv2_014_bbw_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day BB width percentile rank."""
    bbw  = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    rank = _rolling_rank_pct(bbw, _TD_YEAR)
    return rank.diff(_TD_WEEK)


def pcmp_drv2_015_tr_pct_rank_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR percentile rank within 252-day window."""
    tr   = _true_range(close, high, low)
    rank = _rolling_rank_pct(tr, _TD_YEAR)
    return rank.diff(_TD_WEEK)


def pcmp_drv2_016_hl_range_quantile_rank_252d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of HL range percentile rank within 252-day window."""
    hl   = high - low
    rank = _rolling_rank_pct(hl, _TD_YEAR)
    return rank.diff(_TD_WEEK)


def pcmp_drv2_017_squeeze_duration_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of BB-vs-Keltner squeeze fraction (21d window)."""
    bb_sd = _rolling_std(close, _TD_MON)
    bb_w  = 4.0 * bb_sd
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    in_sq = (bb_w < kc_w).astype(float)
    frac  = _rolling_mean(in_sq, _TD_MON)
    return frac.diff(_TD_WEEK)


def pcmp_drv2_018_channel_compression_21_252_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21d/252d HL-band compression ratio."""
    band21  = _rolling_max(high, _TD_MON)  - _rolling_min(low, _TD_MON)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    ratio   = _safe_div(band21, band252)
    return ratio.diff(_TD_MON)


def pcmp_drv2_019_log_range_21d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day log-channel-width over trailing 21 days."""
    lr21 = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    return _linslope(lr21, _TD_MON)


def pcmp_drv2_020_vol_ratio_21_63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/63d realized-vol ratio."""
    lr  = _log_safe(close).diff(1)
    v21 = lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    v63 = lr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    return _safe_div(v21, v63).diff(_TD_WEEK)


def pcmp_drv2_021_contracting_tr_frac_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63-day contracting-TR fraction."""
    tr   = _true_range(close, high, low)
    cont = (tr < tr.shift(1)).astype(float)
    frac = _rolling_mean(cont, _TD_QTR)
    return frac.diff(_TD_WEEK)


def pcmp_drv2_022_bbw_21d_pct_change_5d(close: pd.Series) -> pd.Series:
    """5-day percent change in 21-day BB width (relative speed of squeeze)."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _safe_div(bbw - bbw.shift(_TD_WEEK), bbw.shift(_TD_WEEK).abs().clip(lower=_EPS))


def pcmp_drv2_023_tr_mean_21d_pct_change_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day percent change in 21-day mean TR."""
    atr = _rolling_mean(_true_range(close, high, low), _TD_MON)
    return _safe_div(atr - atr.shift(_TD_WEEK), atr.shift(_TD_WEEK).abs().clip(lower=_EPS))


def pcmp_drv2_024_hl_band_zscore_252d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day HL band z-score within 252-day window."""
    band  = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    zscore = _zscore_rolling(band, _TD_YEAR)
    return zscore.diff(_TD_WEEK)


def pcmp_drv2_025_grand_composite_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the grand compression composite (BB+TR+logrange+channel, 252d ranks)."""
    bbw21  = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    bbw_r  = _rolling_rank_pct(bbw21, _TD_YEAR)
    tr     = _true_range(close, high, low)
    tr_r   = _rolling_rank_pct(tr, _TD_YEAR)
    lr21   = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    lr_r   = _rolling_rank_pct(lr21, _TD_YEAR)
    cw21   = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                       _rolling_min(close, _TD_MON))
    cw_r   = _rolling_rank_pct(cw21, _TD_YEAR)
    comp   = (bbw_r + tr_r + lr_r + cw_r) / 4.0
    return comp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    "pcmp_drv2_001_bbw_21d_5d_diff":                   {"inputs": ["close"], "func": pcmp_drv2_001_bbw_21d_5d_diff},
    "pcmp_drv2_002_bbw_21d_21d_diff":                  {"inputs": ["close"], "func": pcmp_drv2_002_bbw_21d_21d_diff},
    "pcmp_drv2_003_tr_ratio_21_vs_252_5d_diff":        {"inputs": ["close", "high", "low"], "func": pcmp_drv2_003_tr_ratio_21_vs_252_5d_diff},
    "pcmp_drv2_004_hl_range_ratio_21_vs_252_5d_diff":  {"inputs": ["close", "high", "low"], "func": pcmp_drv2_004_hl_range_ratio_21_vs_252_5d_diff},
    "pcmp_drv2_005_log_range_ratio_21_vs_252_5d_diff": {"inputs": ["close"], "func": pcmp_drv2_005_log_range_ratio_21_vs_252_5d_diff},
    "pcmp_drv2_006_vol_ratio_21_vs_252_5d_diff":       {"inputs": ["close"], "func": pcmp_drv2_006_vol_ratio_21_vs_252_5d_diff},
    "pcmp_drv2_007_channel_width_21d_5d_diff":         {"inputs": ["close"], "func": pcmp_drv2_007_channel_width_21d_5d_diff},
    "pcmp_drv2_008_inside_bar_frac_21d_5d_diff":       {"inputs": ["high", "low"], "func": pcmp_drv2_008_inside_bar_frac_21d_5d_diff},
    "pcmp_drv2_009_contracting_bar_frac_21d_5d_diff":  {"inputs": ["high", "low"], "func": pcmp_drv2_009_contracting_bar_frac_21d_5d_diff},
    "pcmp_drv2_010_bbw_ratio_21_vs_252_21d_diff":      {"inputs": ["close"], "func": pcmp_drv2_010_bbw_ratio_21_vs_252_21d_diff},
    "pcmp_drv2_011_bbw_21d_21d_slope":                 {"inputs": ["close"], "func": pcmp_drv2_011_bbw_21d_21d_slope},
    "pcmp_drv2_012_tr_ratio_21_252_21d_slope":         {"inputs": ["close", "high", "low"], "func": pcmp_drv2_012_tr_ratio_21_252_21d_slope},
    "pcmp_drv2_013_vol_ratio_5d_vs_252d_5d_diff":      {"inputs": ["close"], "func": pcmp_drv2_013_vol_ratio_5d_vs_252d_5d_diff},
    "pcmp_drv2_014_bbw_pct_rank_252d_5d_diff":         {"inputs": ["close"], "func": pcmp_drv2_014_bbw_pct_rank_252d_5d_diff},
    "pcmp_drv2_015_tr_pct_rank_252d_5d_diff":          {"inputs": ["close", "high", "low"], "func": pcmp_drv2_015_tr_pct_rank_252d_5d_diff},
    "pcmp_drv2_016_hl_range_quantile_rank_252d_5d_diff": {"inputs": ["high", "low"], "func": pcmp_drv2_016_hl_range_quantile_rank_252d_5d_diff},
    "pcmp_drv2_017_squeeze_duration_21d_5d_diff":      {"inputs": ["close", "high", "low"], "func": pcmp_drv2_017_squeeze_duration_21d_5d_diff},
    "pcmp_drv2_018_channel_compression_21_252_21d_diff": {"inputs": ["high", "low"], "func": pcmp_drv2_018_channel_compression_21_252_21d_diff},
    "pcmp_drv2_019_log_range_21d_21d_slope":           {"inputs": ["close"], "func": pcmp_drv2_019_log_range_21d_21d_slope},
    "pcmp_drv2_020_vol_ratio_21_63_5d_diff":           {"inputs": ["close"], "func": pcmp_drv2_020_vol_ratio_21_63_5d_diff},
    "pcmp_drv2_021_contracting_tr_frac_63d_5d_diff":   {"inputs": ["close", "high", "low"], "func": pcmp_drv2_021_contracting_tr_frac_63d_5d_diff},
    "pcmp_drv2_022_bbw_21d_pct_change_5d":             {"inputs": ["close"], "func": pcmp_drv2_022_bbw_21d_pct_change_5d},
    "pcmp_drv2_023_tr_mean_21d_pct_change_5d":         {"inputs": ["close", "high", "low"], "func": pcmp_drv2_023_tr_mean_21d_pct_change_5d},
    "pcmp_drv2_024_hl_band_zscore_252d_5d_diff":       {"inputs": ["high", "low"], "func": pcmp_drv2_024_hl_band_zscore_252d_5d_diff},
    "pcmp_drv2_025_grand_composite_5d_diff":           {"inputs": ["close", "high", "low"], "func": pcmp_drv2_025_grand_composite_5d_diff},
}
