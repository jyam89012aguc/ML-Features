"""
41_range_compression — Extended 3rd Derivatives (Features rcp_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative range-compression concepts —
        acceleration of ultra-short ATR velocity, jerk in NR10/NR14 accumulation,
        curvature of log-range z-score, Donchian contraction jerk, EWM BB width
        acceleration, volume-drying jerk, and multi-signal composite acceleration.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def rcp_extdrv3_001_tr_ratio_10d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR/10d_mean ratio (jerk in ultra-short compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, 10))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_002_atr10_vs_atr63_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR10/ATR63 ratio (jerk in 2-week vs quarterly compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_003_tr_ratio_126d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR/126d_mean ratio (jerk in half-year compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_HALF))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_004_tr_ewm_ratio_span21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR/EWM21 ratio (EWM compression acceleration)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _ewm_mean(tr, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_005_nr10_count_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of NR10 count in trailing 63d (acceleration of NR10 clustering)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    nr10 = (rng < prev_max).astype(float)
    count63 = nr10.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vel = count63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_006_hl_pct_rank_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of HL percentile rank in 63-day window (rank compression jerk)."""
    rng = high - low
    rank = rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_007_log_tr_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of log(TR) z-score within 252-day distribution (log-range extremity jerk)."""
    log_tr = _log_safe(_tr(close, high, low))
    mu = _rolling_mean(log_tr, _TD_YEAR)
    sigma = _rolling_std(log_tr, _TD_YEAR)
    z = _safe_div(log_tr - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_008_donchian_10d_vs_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 10d/63d Donchian ratio (Donchian contraction jerk)."""
    w10 = _rolling_max(high, 10) - _rolling_min(low, 10)
    w63 = _rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)
    ratio = _safe_div(w10, w63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_009_ewm_bb_width_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM BB width span21/span63 ratio (EWM squeeze jerk)."""
    mu21 = _ewm_mean(close, _TD_MON)
    sd21 = _ewm_std(close, _TD_MON)
    bw21 = _safe_div(2.0 * sd21, mu21)
    mu63 = _ewm_mean(close, _TD_QTR)
    sd63 = _ewm_std(close, _TD_QTR)
    bw63 = _safe_div(2.0 * sd63, mu63)
    ratio = _safe_div(bw21, bw63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_010_vol_compression_5d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/63d volume ratio (volume drying-up jerk)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_011_tr_zscore_126d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR z-score relative to 126-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_HALF)
    s = _rolling_std(tr, _TD_HALF)
    z = _safe_div(tr - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_012_atr10_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR10 z-score within 252-day distribution."""
    tr = _tr(close, high, low)
    atr10 = _rolling_mean(tr, 10)
    mu = _rolling_mean(atr10, _TD_YEAR)
    sigma = _rolling_std(atr10, _TD_YEAR)
    z = _safe_div(atr10 - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_013_donchian_21d_rank_252d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d Donchian width percentile rank (Donchian rank jerk)."""
    w21 = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    rank = w21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_014_multi_window_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-window compression score (acceleration)."""
    tr = _tr(close, high, low)
    r10 = _safe_div(tr, _rolling_mean(tr, 10))
    r21 = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    r63 = _safe_div(tr, _rolling_mean(tr, _TD_QTR))
    r252 = _safe_div(tr, _rolling_mean(tr, _TD_YEAR))
    score = (r10 + r21 + r63 + r252) / 4.0
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_015_log_hl_zscore_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of log(H-L) z-score within 63-day distribution."""
    log_rng = _log_safe(high - low)
    mu = _rolling_mean(log_rng, _TD_QTR)
    sigma = _rolling_std(log_rng, _TD_QTR)
    z = _safe_div(log_rng - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_016_nr14_fraction_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of NR14 fraction in trailing 63 days (NR14 clustering jerk)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(13, min_periods=6).max()
    nr14 = (rng < prev_max).astype(float)
    frac63 = nr14.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel = frac63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_017_expand_compress_count_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of expand-to-compress transition count (transition jerk)."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    was_above = tr.shift(1) >= mean21.shift(1)
    now_below = tr < mean21
    transition = (was_above & now_below).astype(float)
    count63 = _rolling_sum(transition, _TD_QTR)
    vel = count63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_018_atr126_vs_atr252_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in ATR126/ATR252 ratio (half-year compression jerk)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_HALF), _rolling_mean(tr, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rcp_extdrv3_019_bb_width_63d_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day BB width z-score (quarterly squeeze extremity jerk)."""
    m = _rolling_mean(close, _TD_QTR)
    s = _rolling_std(close, _TD_QTR)
    bw = _safe_div(2.0 * s, m)
    mu = _rolling_mean(bw, _TD_YEAR)
    sigma = _rolling_std(bw, _TD_YEAR)
    z = _safe_div(bw - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_020_tr_ewm_zscore_span63_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM z-score of TR (span 63) — EWM compression jerk."""
    tr = _tr(close, high, low)
    mu = _ewm_mean(tr, _TD_QTR)
    sigma = _ewm_std(tr, _TD_QTR)
    z = _safe_div(tr - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_021_consec_nr10_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive NR10 streak (streak acceleration)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    streak = _consec_streak(rng < prev_max)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_022_squeeze_intensity_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of squeeze intensity (slope-of-slope curvature)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    squeeze_frac = _rolling_mean(squeeze, _TD_QTR)
    atr_rank = atr21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    intensity = squeeze_frac * (1.0 - atr_rank.fillna(0.5))
    slope = _linslope(intensity, _TD_MON)
    return slope.diff(_TD_WEEK)


def rcp_extdrv3_023_vol_weighted_tr_ratio_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VW TR ratio vs VW ATR21 (volume-weighted compression jerk)."""
    tr = _tr(close, high, low)
    vwtr = _safe_div(_rolling_sum(tr * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    ratio = _safe_div(tr, vwtr)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_extdrv3_024_atr10_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of ATR10 over trailing 21 days (ATR10 slope curvature)."""
    tr = _tr(close, high, low)
    atr10 = _rolling_mean(tr, 10)
    slope = _linslope(atr10, _TD_MON)
    return slope.diff(_TD_WEEK)


def rcp_extdrv3_025_capitulation_coil_index_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of capitulation coil index (ATR_ratio * vol_drying * nr7_flag jerk)."""
    tr = _tr(close, high, low)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    vol_ratio = (1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))).clip(lower=0, upper=1)
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7_flag = (rng < prev_max).astype(float)
    index = atr_ratio * vol_ratio * nr7_flag
    vel = index.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rcp_extdrv3_001_tr_ratio_10d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_001_tr_ratio_10d_5d_diff_5d_diff},
    "rcp_extdrv3_002_atr10_vs_atr63_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_002_atr10_vs_atr63_5d_diff_5d_diff},
    "rcp_extdrv3_003_tr_ratio_126d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_003_tr_ratio_126d_5d_diff_5d_diff},
    "rcp_extdrv3_004_tr_ewm_ratio_span21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_004_tr_ewm_ratio_span21_5d_diff_5d_diff},
    "rcp_extdrv3_005_nr10_count_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_005_nr10_count_63d_5d_diff_5d_diff},
    "rcp_extdrv3_006_hl_pct_rank_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_006_hl_pct_rank_63d_5d_diff_5d_diff},
    "rcp_extdrv3_007_log_tr_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_007_log_tr_zscore_252d_5d_diff_5d_diff},
    "rcp_extdrv3_008_donchian_10d_vs_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_008_donchian_10d_vs_63d_5d_diff_5d_diff},
    "rcp_extdrv3_009_ewm_bb_width_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": rcp_extdrv3_009_ewm_bb_width_ratio_5d_diff_5d_diff},
    "rcp_extdrv3_010_vol_compression_5d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": rcp_extdrv3_010_vol_compression_5d_vs_63d_5d_diff_5d_diff},
    "rcp_extdrv3_011_tr_zscore_126d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_011_tr_zscore_126d_5d_diff_5d_diff},
    "rcp_extdrv3_012_atr10_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_012_atr10_zscore_252d_5d_diff_5d_diff},
    "rcp_extdrv3_013_donchian_21d_rank_252d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_013_donchian_21d_rank_252d_5d_diff_5d_diff},
    "rcp_extdrv3_014_multi_window_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_014_multi_window_score_5d_diff_5d_diff},
    "rcp_extdrv3_015_log_hl_zscore_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_015_log_hl_zscore_63d_5d_diff_5d_diff},
    "rcp_extdrv3_016_nr14_fraction_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_016_nr14_fraction_63d_5d_diff_5d_diff},
    "rcp_extdrv3_017_expand_compress_count_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_017_expand_compress_count_63d_5d_diff_5d_diff},
    "rcp_extdrv3_018_atr126_vs_atr252_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_018_atr126_vs_atr252_21d_diff_5d_diff},
    "rcp_extdrv3_019_bb_width_63d_zscore_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": rcp_extdrv3_019_bb_width_63d_zscore_252d_5d_diff_5d_diff},
    "rcp_extdrv3_020_tr_ewm_zscore_span63_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_020_tr_ewm_zscore_span63_5d_diff_5d_diff},
    "rcp_extdrv3_021_consec_nr10_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_extdrv3_021_consec_nr10_5d_diff_5d_diff},
    "rcp_extdrv3_022_squeeze_intensity_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_022_squeeze_intensity_slope_5d_diff},
    "rcp_extdrv3_023_vol_weighted_tr_ratio_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_extdrv3_023_vol_weighted_tr_ratio_5d_diff_5d_diff},
    "rcp_extdrv3_024_atr10_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_extdrv3_024_atr10_slope_5d_diff},
    "rcp_extdrv3_025_capitulation_coil_index_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_extdrv3_025_capitulation_coil_index_5d_diff_5d_diff},
}
