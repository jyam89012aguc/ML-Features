"""
45_panic_bar_signatures — 2nd Derivatives (Features pbs_drv2_001-025)
Domain: rate of change of base panic-bar signature features — velocity of panic morphology
Includes marubozu and climax bar derivative signals.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _bar_range(high: pd.Series, low: pd.Series) -> pd.Series:
    return high - low


def _lower_tail(open: pd.Series, close: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([open, close], axis=1).min(axis=1) - low


def _body(open: pd.Series, close: pd.Series) -> pd.Series:
    return (close - open).abs()


def _avg_range(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_bar_range(high, low), w)


def _close_loc(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rng = _bar_range(high, low)
    return _safe_div(close - low, rng)


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

def pbs_drv2_001_range_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of range/21d-avg-range ratio (velocity of wide-bar intensity)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return rr.diff(_TD_WEEK)


def pbs_drv2_002_range_ratio_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of range/21d-avg-range ratio (monthly velocity)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return rr.diff(_TD_MON)


def pbs_drv2_003_range_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of range z-score (acceleration of range extremity)."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    z = _safe_div(rng - m, s)
    return z.diff(_TD_WEEK)


def pbs_drv2_004_lower_tail_ratio_range_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of lower-tail-to-range fraction."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    return frac.diff(_TD_WEEK)


def pbs_drv2_005_lower_tail_ratio_range_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of lower-tail-to-range fraction."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    return frac.diff(_TD_MON)


def pbs_drv2_006_panic_bar_fraction_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day panic bar fraction."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq = _rolling_sum(flag, _TD_MON) / _TD_MON
    return freq.diff(_TD_WEEK)


def pbs_drv2_007_panic_bar_fraction_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day panic bar fraction."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    return freq.diff(_TD_MON)


def pbs_drv2_008_exhaustion_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of exhaustion bar score (range_ratio * lower_tail_frac)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    score = rr * lt_frac
    return score.diff(_TD_WEEK)


def pbs_drv2_009_exhaustion_score_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of exhaustion bar score."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    score = rr * lt_frac
    return score.diff(_TD_MON)


def pbs_drv2_010_panic_composite_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of composite panic score (range_zscore * clv_inv * bear)."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    return score.diff(_TD_WEEK)


def pbs_drv2_011_panic_composite_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of composite panic score."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    return score.diff(_TD_MON)


def pbs_drv2_012_range_ratio_21d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of range/21d-avg ratio over trailing 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return _linslope(rr, _TD_MON)


def pbs_drv2_013_lower_tail_21d_avg_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling average lower tail (velocity of wick growth)."""
    lt = _lower_tail(open, close, low)
    avg_lt = _rolling_mean(lt, _TD_MON)
    return avg_lt.diff(_TD_WEEK)


def pbs_drv2_014_clv_21d_avg_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day average close location value."""
    clv = _close_loc(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_MON)
    return avg_clv.diff(_TD_WEEK)


def pbs_drv2_015_clv_21d_avg_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day average close location value."""
    clv = _close_loc(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_MON)
    return avg_clv.diff(_TD_MON)


def pbs_drv2_016_wide_range_bar_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of wide-range bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def pbs_drv2_017_exhaustion_bar_count_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day exhaustion bar count."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    flag = ((rng > 2.0 * avg) & (lt_frac > 0.40)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def pbs_drv2_018_range_times_vol_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of range*volume z-score."""
    rng = _bar_range(high, low)
    rv = rng * volume
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    z = _safe_div(rv - m, s)
    return z.diff(_TD_WEEK)


def pbs_drv2_019_panic_vol_fraction_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of fraction of volume occurring on panic bars in 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    panic_vol = _rolling_sum(volume * is_panic, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    frac = _safe_div(panic_vol, total_vol)
    return frac.diff(_TD_WEEK)


def pbs_drv2_020_bearish_marubozu_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of bearish marubozu bars (body>80% range, close<open).
    Captures acceleration in full-conviction panic selling morphology."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((body_frac >= 0.80) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def pbs_drv2_021_body_range_ratio_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of body/range ratio (shift toward marubozu vs wick-dominant morphology)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    br = _safe_div(body, rng.clip(lower=_EPS))
    return br.diff(_TD_MON)


def pbs_drv2_022_selling_climax_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day selling climax bar count (wide bear + vol>2x median).
    Detects acceleration in climax-bar frequency — a key capitulation signal."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def pbs_drv2_023_climax_intensity_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of climax intensity score (range_zscore * vol_zscore).
    Velocity of combined range+volume extremity — rising = escalating climax pressure."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    return intensity.diff(_TD_WEEK)


def pbs_drv2_024_climax_intensity_score_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of climax intensity score (range_zscore * vol_zscore).
    Monthly velocity of combined panic energy — rising = sustained climax environment."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    return intensity.diff(_TD_MON)


def pbs_drv2_025_panic_intensity_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of panic intensity score (range_zscore + lt_frac + bear)."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    intensity = rng_z + lt_frac + bear
    return intensity.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_REGISTRY_2ND_DERIVATIVES = {
    "pbs_drv2_001_range_ratio_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_001_range_ratio_21d_5d_diff},
    "pbs_drv2_002_range_ratio_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_002_range_ratio_21d_21d_diff},
    "pbs_drv2_003_range_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_003_range_zscore_252d_5d_diff},
    "pbs_drv2_004_lower_tail_ratio_range_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_004_lower_tail_ratio_range_5d_diff},
    "pbs_drv2_005_lower_tail_ratio_range_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_005_lower_tail_ratio_range_21d_diff},
    "pbs_drv2_006_panic_bar_fraction_21d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_006_panic_bar_fraction_21d_5d_diff},
    "pbs_drv2_007_panic_bar_fraction_63d_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_007_panic_bar_fraction_63d_21d_diff},
    "pbs_drv2_008_exhaustion_score_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_008_exhaustion_score_5d_diff},
    "pbs_drv2_009_exhaustion_score_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_009_exhaustion_score_21d_diff},
    "pbs_drv2_010_panic_composite_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_010_panic_composite_5d_diff},
    "pbs_drv2_011_panic_composite_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_011_panic_composite_21d_diff},
    "pbs_drv2_012_range_ratio_21d_slope_21d": {"inputs": ["close", "high", "low"], "func": pbs_drv2_012_range_ratio_21d_slope_21d},
    "pbs_drv2_013_lower_tail_21d_avg_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_013_lower_tail_21d_avg_5d_diff},
    "pbs_drv2_014_clv_21d_avg_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_014_clv_21d_avg_5d_diff},
    "pbs_drv2_015_clv_21d_avg_21d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_015_clv_21d_avg_21d_diff},
    "pbs_drv2_016_wide_range_bar_count_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv2_016_wide_range_bar_count_21d_5d_diff},
    "pbs_drv2_017_exhaustion_bar_count_63d_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_017_exhaustion_bar_count_63d_21d_diff},
    "pbs_drv2_018_range_times_vol_zscore_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": pbs_drv2_018_range_times_vol_zscore_5d_diff},
    "pbs_drv2_019_panic_vol_fraction_21d_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv2_019_panic_vol_fraction_21d_5d_diff},
    "pbs_drv2_020_bearish_marubozu_count_21d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_020_bearish_marubozu_count_21d_5d_diff},
    "pbs_drv2_021_body_range_ratio_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_021_body_range_ratio_21d_diff},
    "pbs_drv2_022_selling_climax_count_21d_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv2_022_selling_climax_count_21d_5d_diff},
    "pbs_drv2_023_climax_intensity_score_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv2_023_climax_intensity_score_5d_diff},
    "pbs_drv2_024_climax_intensity_score_21d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv2_024_climax_intensity_score_21d_diff},
    "pbs_drv2_025_panic_intensity_score_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv2_025_panic_intensity_score_5d_diff},
}
