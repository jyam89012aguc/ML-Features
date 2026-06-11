"""
41_range_compression — Extended 2nd Derivatives (Features rcp_extdrv2_001-025)
Domain: rate of change of extended base range-compression concepts — velocity of
        compression on new windows, EWM ATR change, NR10/NR14 streak growth,
        percentile rank velocity, log-range velocity, Donchian contraction speed,
        transition counter rates, volume-weighted range velocity.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rcp_extdrv2_001_tr_ratio_10d_mean_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR/10d_mean_TR ratio (velocity of ultra-short compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, 10))
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_002_tr_ratio_126d_mean_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR/126d_mean_TR ratio (velocity of half-year compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_HALF))
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_003_atr10_vs_atr63_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR10/ATR63 ratio (2-week vs quarterly compression velocity)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_004_atr126_vs_atr252_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of ATR126/ATR252 ratio (monthly change in half-year compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_HALF), _rolling_mean(tr, _TD_YEAR))
    return ratio.diff(_TD_MON)


def rcp_extdrv2_005_tr_ewm_ratio_span21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR/EWM21 ratio (EWM-smoothed compression velocity)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _ewm_mean(tr, _TD_MON))
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_006_nr10_count_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of NR10 count in trailing 63 days (NR10 accumulation velocity)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    nr10 = (rng < prev_max).astype(float)
    count63 = nr10.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return count63.diff(_TD_WEEK)


def rcp_extdrv2_007_consec_nr10_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive NR10 streak (NR10 streak growth rate)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    streak = _consec_streak(rng < prev_max)
    return streak.diff(_TD_WEEK)


def rcp_extdrv2_008_hl_pct_rank_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of HL percentile rank within 63-day distribution."""
    rng = high - low
    rank = rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def rcp_extdrv2_009_hl_pct_rank_126d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of HL percentile rank within 126-day distribution."""
    rng = high - low
    rank = rng.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)
    return rank.diff(_TD_MON)


def rcp_extdrv2_010_tr_zscore_126d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR z-score relative to 126-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_HALF)
    s = _rolling_std(tr, _TD_HALF)
    z = _safe_div(tr - m, s)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_011_log_tr_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of log(TR) z-score within 252-day distribution."""
    log_tr = _log_safe(_tr(close, high, low))
    mu = _rolling_mean(log_tr, _TD_YEAR)
    sigma = _rolling_std(log_tr, _TD_YEAR)
    z = _safe_div(log_tr - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_012_donchian_10d_vs_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 10d/63d Donchian channel width ratio (short-term Donchian compression velocity)."""
    w10 = _rolling_max(high, 10) - _rolling_min(low, 10)
    w63 = _rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)
    ratio = _safe_div(w10, w63)
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_013_donchian_21d_pct_rank_252d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d Donchian width percentile rank within 252-day distribution."""
    w21 = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    rank = w21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def rcp_extdrv2_014_ewm_bb_width_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM BB width span21 / span63 ratio."""
    mu21 = _ewm_mean(close, _TD_MON)
    sd21 = _ewm_std(close, _TD_MON)
    bw21 = _safe_div(2.0 * sd21, mu21)
    mu63 = _ewm_mean(close, _TD_QTR)
    sd63 = _ewm_std(close, _TD_QTR)
    bw63 = _safe_div(2.0 * sd63, mu63)
    ratio = _safe_div(bw21, bw63)
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_015_expand_to_compress_count_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of expand-to-compress transition count in trailing 63 days."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    was_above = tr.shift(1) >= mean21.shift(1)
    now_below = tr < mean21
    transition = (was_above & now_below).astype(float)
    count63 = _rolling_sum(transition, _TD_QTR)
    return count63.diff(_TD_WEEK)


def rcp_extdrv2_016_bb_width_63d_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day BB width z-score within 252-day distribution."""
    m = _rolling_mean(close, _TD_QTR)
    s = _rolling_std(close, _TD_QTR)
    bw = _safe_div(2.0 * s, m)
    mu = _rolling_mean(bw, _TD_YEAR)
    sigma = _rolling_std(bw, _TD_YEAR)
    z = _safe_div(bw - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_017_tr_ewm_zscore_span63_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of EWM z-score of TR (span 63) — EWM compression extremity velocity."""
    tr = _tr(close, high, low)
    mu = _ewm_mean(tr, _TD_QTR)
    sigma = _ewm_std(tr, _TD_QTR)
    z = _safe_div(tr - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_018_vol_compression_5d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5d/63d volume ratio (volume drying-up velocity)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_019_vol_weighted_tr_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted TR ratio vs VW ATR21 (VW compression velocity)."""
    tr = _tr(close, high, low)
    vwtr = _safe_div(_rolling_sum(tr * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    ratio = _safe_div(tr, vwtr)
    return ratio.diff(_TD_WEEK)


def rcp_extdrv2_020_atr10_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR10 z-score within 252-day ATR10 distribution."""
    tr = _tr(close, high, low)
    atr10 = _rolling_mean(tr, 10)
    mu = _rolling_mean(atr10, _TD_YEAR)
    sigma = _rolling_std(atr10, _TD_YEAR)
    z = _safe_div(atr10 - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_021_log_hl_zscore_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of log(H-L) z-score within 63-day distribution."""
    log_rng = _log_safe(high - low)
    mu = _rolling_mean(log_rng, _TD_QTR)
    sigma = _rolling_std(log_rng, _TD_QTR)
    z = _safe_div(log_rng - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_extdrv2_022_nr14_fraction_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of NR14 fraction in trailing 63 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(13, min_periods=6).max()
    nr14 = (rng < prev_max).astype(float)
    frac63 = nr14.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return frac63.diff(_TD_WEEK)


def rcp_extdrv2_023_multi_window_compression_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of multi-window compression score (avg of TR/10d,21d,63d,252d means)."""
    tr = _tr(close, high, low)
    r10 = _safe_div(tr, _rolling_mean(tr, 10))
    r21 = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    r63 = _safe_div(tr, _rolling_mean(tr, _TD_QTR))
    r252 = _safe_div(tr, _rolling_mean(tr, _TD_YEAR))
    score = (r10 + r21 + r63 + r252) / 4.0
    return score.diff(_TD_WEEK)


def rcp_extdrv2_024_squeeze_intensity_63d_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of squeeze intensity score over trailing 21 days."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    squeeze_frac = _rolling_mean(squeeze, _TD_QTR)
    atr_rank = atr21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    intensity = squeeze_frac * (1.0 - atr_rank.fillna(0.5))
    return _linslope(intensity, _TD_MON)


def rcp_extdrv2_025_capitulation_coil_index_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of capitulation coil index (ATR_ratio * vol_drying * nr7_flag)."""
    tr = _tr(close, high, low)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    vol_ratio = (1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))).clip(lower=0, upper=1)
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7_flag = (rng < prev_max).astype(float)
    index = atr_ratio * vol_ratio * nr7_flag
    return index.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "rcp_extdrv2_001_tr_ratio_10d_mean_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_001_tr_ratio_10d_mean_5d_diff},
    "rcp_extdrv2_002_tr_ratio_126d_mean_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_002_tr_ratio_126d_mean_5d_diff},
    "rcp_extdrv2_003_atr10_vs_atr63_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_003_atr10_vs_atr63_5d_diff},
    "rcp_extdrv2_004_atr126_vs_atr252_21d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_004_atr126_vs_atr252_21d_diff},
    "rcp_extdrv2_005_tr_ewm_ratio_span21_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_005_tr_ewm_ratio_span21_5d_diff},
    "rcp_extdrv2_006_nr10_count_63d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_006_nr10_count_63d_5d_diff},
    "rcp_extdrv2_007_consec_nr10_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_007_consec_nr10_5d_diff},
    "rcp_extdrv2_008_hl_pct_rank_63d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_008_hl_pct_rank_63d_5d_diff},
    "rcp_extdrv2_009_hl_pct_rank_126d_21d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_009_hl_pct_rank_126d_21d_diff},
    "rcp_extdrv2_010_tr_zscore_126d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_010_tr_zscore_126d_5d_diff},
    "rcp_extdrv2_011_log_tr_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_011_log_tr_zscore_252d_5d_diff},
    "rcp_extdrv2_012_donchian_10d_vs_63d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_012_donchian_10d_vs_63d_5d_diff},
    "rcp_extdrv2_013_donchian_21d_pct_rank_252d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_013_donchian_21d_pct_rank_252d_5d_diff},
    "rcp_extdrv2_014_ewm_bb_width_ratio_5d_diff": {"inputs": ["close"], "func": rcp_extdrv2_014_ewm_bb_width_ratio_5d_diff},
    "rcp_extdrv2_015_expand_to_compress_count_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_015_expand_to_compress_count_63d_5d_diff},
    "rcp_extdrv2_016_bb_width_63d_zscore_252d_5d_diff": {"inputs": ["close"], "func": rcp_extdrv2_016_bb_width_63d_zscore_252d_5d_diff},
    "rcp_extdrv2_017_tr_ewm_zscore_span63_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_017_tr_ewm_zscore_span63_5d_diff},
    "rcp_extdrv2_018_vol_compression_5d_vs_63d_5d_diff": {"inputs": ["volume"], "func": rcp_extdrv2_018_vol_compression_5d_vs_63d_5d_diff},
    "rcp_extdrv2_019_vol_weighted_tr_ratio_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_extdrv2_019_vol_weighted_tr_ratio_21d_5d_diff},
    "rcp_extdrv2_020_atr10_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_020_atr10_zscore_252d_5d_diff},
    "rcp_extdrv2_021_log_hl_zscore_63d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_021_log_hl_zscore_63d_5d_diff},
    "rcp_extdrv2_022_nr14_fraction_63d_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv2_022_nr14_fraction_63d_5d_diff},
    "rcp_extdrv2_023_multi_window_compression_score_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_023_multi_window_compression_score_5d_diff},
    "rcp_extdrv2_024_squeeze_intensity_63d_slope": {"inputs": ["close", "high", "low"], "func": rcp_extdrv2_024_squeeze_intensity_63d_slope},
    "rcp_extdrv2_025_capitulation_coil_index_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_extdrv2_025_capitulation_coil_index_5d_diff},
}
