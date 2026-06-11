"""
45_panic_bar_signatures — 3rd Derivatives (Features pbs_drv3_001-025)
Domain: rate of change of 2nd-derivative panic-bar features — acceleration of panic morphology
Includes marubozu and climax bar third-order signals.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def pbs_drv3_001_range_ratio_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of range/21d-avg ratio (acceleration of wide-bar velocity)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    vel = rr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_002_range_ratio_21d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of range/avg ratio (jerk in monthly change)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    vel21 = rr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_drv3_003_range_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of range z-score (acceleration of range extremity)."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    z = _safe_div(rng - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_004_lower_tail_ratio_range_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of lower-tail-to-range fraction (jerk in wick velocity)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_005_panic_bar_fraction_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day panic bar fraction."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq = _rolling_sum(flag, _TD_MON) / _TD_MON
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_006_exhaustion_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of exhaustion bar score (acceleration of exhaustion)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    score = rr * lt_frac
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_007_panic_composite_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of composite panic score (acceleration of panic intensity)."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_008_clv_21d_avg_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day average CLV (jerk in close-location trend)."""
    clv = _close_loc(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_MON)
    vel = avg_clv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_009_panic_composite_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of composite panic score."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_drv3_010_lower_tail_ratio_range_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of lower-tail fraction."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_drv3_011_range_ratio_21d_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of range/avg ratio (acceleration of range trend)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    slp = _linslope(rr, _TD_MON)
    return slp.diff(_TD_WEEK)


def pbs_drv3_012_exhaustion_score_slope_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of exhaustion score (rate of slope change)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    score = rr * lt_frac
    slp = _linslope(score, _TD_QTR)
    return slp.diff(_TD_WEEK)


def pbs_drv3_013_panic_bar_fraction_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day panic bar fraction."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    vel21 = freq.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_drv3_014_range_times_vol_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of range*volume z-score."""
    rng = _bar_range(high, low)
    rv = rng * volume
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    z = _safe_div(rv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_015_lower_tail_sum_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day sum of lower tails (jerk in wick accumulation)."""
    lt = _lower_tail(open, close, low)
    lt_sum = _rolling_sum(lt, _TD_MON)
    vel = lt_sum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_016_panic_composite_slope_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of panic composite over 63 days."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    slp = _linslope(score, _TD_QTR)
    return slp.diff(_TD_WEEK)


def pbs_drv3_017_clv_21d_avg_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of CLV 21d average."""
    clv = _close_loc(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_MON)
    vel21 = avg_clv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_drv3_018_wide_range_count_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day wide-range bar count."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_019_bearish_marubozu_count_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bearish marubozu count (jerk in full-conviction selling).
    Third-order: detects abrupt onset/cessation of marubozu-type capitulation clusters."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((body_frac >= 0.80) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_020_panic_intensity_5d_diff_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of panic intensity score."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    intensity = rng_z + lt_frac + bear
    vel = intensity.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pbs_drv3_021_selling_climax_count_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day selling climax count (jerk in climax-bar frequency).
    Third-order: detects abrupt spikes in climax bar clusters — sudden phase transitions."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_022_climax_intensity_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of climax intensity score (acceleration of range+vol extremity).
    Third-order: abrupt change in the velocity of combined panic energy."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_drv3_023_climax_intensity_slope_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of climax intensity over 63 days (acceleration of trend in climax energy)."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    slp = _linslope(intensity, _TD_QTR)
    return slp.diff(_TD_WEEK)


def pbs_drv3_024_lower_tail_21d_avg_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of 21-day avg lower tail."""
    lt = _lower_tail(open, close, low)
    avg_lt = _rolling_mean(lt, _TD_MON)
    vel = avg_lt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pbs_drv3_025_panic_composite_5d_diff_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of composite panic score."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    vel = score.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_REGISTRY_3RD_DERIVATIVES = {
    "pbs_drv3_001_range_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_001_range_ratio_21d_5d_diff_5d_diff},
    "pbs_drv3_002_range_ratio_21d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_002_range_ratio_21d_21d_diff_5d_diff},
    "pbs_drv3_003_range_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_003_range_zscore_252d_5d_diff_5d_diff},
    "pbs_drv3_004_lower_tail_ratio_range_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_004_lower_tail_ratio_range_5d_diff_5d_diff},
    "pbs_drv3_005_panic_bar_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_005_panic_bar_fraction_21d_5d_diff_5d_diff},
    "pbs_drv3_006_exhaustion_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_006_exhaustion_score_5d_diff_5d_diff},
    "pbs_drv3_007_panic_composite_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_007_panic_composite_5d_diff_5d_diff},
    "pbs_drv3_008_clv_21d_avg_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_008_clv_21d_avg_5d_diff_5d_diff},
    "pbs_drv3_009_panic_composite_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_009_panic_composite_21d_diff_5d_diff},
    "pbs_drv3_010_lower_tail_ratio_range_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_010_lower_tail_ratio_range_21d_diff_5d_diff},
    "pbs_drv3_011_range_ratio_21d_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_011_range_ratio_21d_slope_5d_diff},
    "pbs_drv3_012_exhaustion_score_slope_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_012_exhaustion_score_slope_63d_5d_diff},
    "pbs_drv3_013_panic_bar_fraction_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_013_panic_bar_fraction_63d_21d_diff_5d_diff},
    "pbs_drv3_014_range_times_vol_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": pbs_drv3_014_range_times_vol_zscore_5d_diff_5d_diff},
    "pbs_drv3_015_lower_tail_sum_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_015_lower_tail_sum_21d_5d_diff_5d_diff},
    "pbs_drv3_016_panic_composite_slope_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_016_panic_composite_slope_63d_5d_diff},
    "pbs_drv3_017_clv_21d_avg_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_017_clv_21d_avg_21d_diff_5d_diff},
    "pbs_drv3_018_wide_range_count_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": pbs_drv3_018_wide_range_count_21d_5d_diff_5d_diff},
    "pbs_drv3_019_bearish_marubozu_count_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_019_bearish_marubozu_count_21d_5d_diff_5d_diff},
    "pbs_drv3_020_panic_intensity_5d_diff_slope_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_020_panic_intensity_5d_diff_slope_21d},
    "pbs_drv3_021_selling_climax_count_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv3_021_selling_climax_count_21d_5d_diff_5d_diff},
    "pbs_drv3_022_climax_intensity_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv3_022_climax_intensity_score_5d_diff_5d_diff},
    "pbs_drv3_023_climax_intensity_slope_63d_5d_diff": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_drv3_023_climax_intensity_slope_63d_5d_diff},
    "pbs_drv3_024_lower_tail_21d_avg_5d_diff_slope": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_024_lower_tail_21d_avg_5d_diff_slope},
    "pbs_drv3_025_panic_composite_5d_diff_slope_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_drv3_025_panic_composite_5d_diff_slope_21d},
}
