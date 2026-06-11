"""
45_panic_bar_signatures — Extended 3rd Derivatives (Features pbs_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative features — acceleration of the
        velocity of deeper panic morphology (second diff / slope-of-slope / diff-of-slope).
        Source concepts: extended base 001-075 via their extended 2nd derivatives.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Net-new: third-order signals applied to extended-base concepts; not duplicates of
pbs_drv3_001-025 which are third derivatives of the non-extended base.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _bar_range(high: pd.Series, low: pd.Series) -> pd.Series:
    return high - low


def _lower_tail(open_: pd.Series, close: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([open_, close], axis=1).min(axis=1) - low


def _upper_tail(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    return high - pd.concat([open_, close], axis=1).max(axis=1)


def _body(open_: pd.Series, close: pd.Series) -> pd.Series:
    return (close - open_).abs()


def _avg_range(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_bar_range(high, low), w)


def _close_loc(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close location value in [0,1]: 0=at low, 1=at high."""
    rng = _bar_range(high, low)
    return _safe_div(close - low, rng)


def _body_midpoint_loc(open_: pd.Series, close: pd.Series,
                       high: pd.Series, low: pd.Series) -> pd.Series:
    """Body midpoint location within bar range: 0=bottom, 1=top."""
    body_mid = (open_ + close) / 2.0
    rng = _bar_range(high, low)
    return _safe_div(body_mid - low, rng)


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


# ── Extended 3rd-Derivative Feature Functions ────────────────────────────────
# Each = diff/slope applied to an extended-2nd-derivative concept.

# --- Group A (001-005): Marubozu vol-score third-order ---

def pbs_extdrv3_001_bearish_marubozu_vol_score_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of marubozu vol score — acceleration of conviction-weighted selling velocity (ext_010 → extdrv2_001)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    score = frac.fillna(0.0) * vol_z * bear
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_002_bearish_marubozu_vol_score_21d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of the 21-day velocity of marubozu vol score — jerk in monthly conviction selling (ext_010 → extdrv2_002)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    score = frac.fillna(0.0) * vol_z * bear
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_extdrv3_003_marubozu_degree_ewm5_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of 5d EWM body/range ratio — acceleration of short-term marubozu trend (ext_009 → extdrv2_003)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    ewm_frac = _ewm_mean(frac, _TD_WEEK)
    vel = ewm_frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_004_marubozu_degree_ewm5_slope_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 5d EWM body/range ratio — rate of slope change in conviction morphology (ext_009 → extdrv2_005)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    ewm_frac = _ewm_mean(frac, _TD_WEEK)
    slp = _linslope(ewm_frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def pbs_extdrv3_005_bearish_marubozu_count_5d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of 5-day marubozu count — jerk in ultra-short-term conviction surge (ext_008 → extdrv2_004)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((frac >= 0.80) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_WEEK)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group B (006-010): Climax-bar third-order ---

def pbs_extdrv3_006_climax_intensity_bear_only_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of bear-only climax intensity — acceleration of bear-climax velocity (ext_016 → extdrv2_006)."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    bear = (close < open).astype(float)
    score = rng_z * vol_z * bear
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_007_climax_intensity_bear_only_slope_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of bear-only climax intensity — rate of slope change in bear climax trend (ext_016)."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    bear = (close < open).astype(float)
    score = rng_z * vol_z * bear
    slp = _linslope(score, _TD_MON)
    return slp.diff(_TD_WEEK)


def pbs_extdrv3_008_climax_recency_decay_5d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 5d EWM climax flag — acceleration of short recency decay velocity (ext_018 → extdrv2_008)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    decay = _ewm_mean(flag, _TD_WEEK)
    vel = decay.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_009_climax_recency_decay_21d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21d EWM climax flag — acceleration of medium recency decay velocity (ext_019 → extdrv2_009)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    decay = _ewm_mean(flag, _TD_MON)
    vel = decay.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_010_range_vol_zscore_product_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of range-z * vol-z product — acceleration of dual-normalised panic energy (ext_020 → extdrv2_010)."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng)
    m_vol = _rolling_mean(volume, _TD_QTR)
    s_vol = _rolling_std(volume, _TD_QTR)
    vol_z = _safe_div(volume - m_vol, s_vol)
    product = rng_z * vol_z
    vel = product.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group C (011-013): Pin-bar / tail asymmetry third-order ---

def pbs_extdrv3_011_hammer_vs_shooting_star_asymmetry_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of tail asymmetry — acceleration of intraday directional rejection shift (ext_023 → extdrv2_011)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    asym = lt_f - ut_f
    vel = asym.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_012_hammer_vs_shooting_star_asymmetry_21d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 21-day velocity of tail asymmetry — jerk in monthly directional wick shift (ext_023 → extdrv2_012)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    asym = lt_f - ut_f
    vel21 = asym.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_extdrv3_013_lower_tail_count_21d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day strong-lower-tail count — jerk in pin-bar frequency (ext_028 → extdrv2_013)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    flag = (lt_f > 0.50).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group D (014-016): Gap-down third-order ---

def pbs_extdrv3_014_gap_down_magnitude_pct_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of gap-down magnitude pct — acceleration of opening dislocation velocity (ext_031 → extdrv2_014)."""
    prior_close = close.shift(1)
    gap = (prior_close - open) / prior_close.clip(lower=_EPS)
    gap_mag = gap.clip(lower=0.0)
    vel = gap_mag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_015_gap_down_count_21d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day gap-down count — jerk in gap-down frequency (ext_037 → extdrv2_015)."""
    prior_close = close.shift(1)
    gap_down = (open < prior_close).astype(float)
    cnt = _rolling_sum(gap_down, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_016_gap_down_total_loss_pct_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of total session loss pct from prior close — acceleration of gap+decline pressure (ext_040 → extdrv2_016)."""
    prior_close = close.shift(1)
    loss = ((prior_close - close) / prior_close.clip(lower=_EPS)).clip(lower=0.0)
    vel = loss.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group E (017-019): Body-location third-order ---

def pbs_extdrv3_017_body_midpoint_loc_21d_avg_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21d avg body midpoint location — acceleration of downward body drift (ext_057 → extdrv2_017)."""
    bml = _body_midpoint_loc(open, close, high, low)
    avg_bml = _rolling_mean(bml, _TD_MON)
    vel = avg_bml.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_018_body_midpoint_loc_21d_avg_21d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of the 21-day velocity of 21d avg body midpoint location — jerk in monthly body drift (ext_057 → extdrv2_018)."""
    bml = _body_midpoint_loc(open, close, high, low)
    avg_bml = _rolling_mean(bml, _TD_MON)
    vel21 = avg_bml.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_extdrv3_019_body_midpoint_loc_slope_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of body midpoint location — rate of slope change in session-low body positioning (ext_051 → extdrv2_019)."""
    bml = _body_midpoint_loc(open, close, high, low)
    slp = _linslope(bml, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- Group F (020-022): Effort-vs-result third-order ---

def pbs_extdrv3_020_effort_vs_result_ratio_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of effort-vs-result ratio — acceleration of absorption pressure velocity (ext_059 → extdrv2_020)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS)).clip(lower=_EPS)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    evr = _safe_div(vol_z, bd_f)
    vel = evr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_021_effort_vs_result_ratio_21d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of the 21-day velocity of effort-vs-result ratio — jerk in monthly absorption pressure (ext_059 → extdrv2_021)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS)).clip(lower=_EPS)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    evr = _safe_div(vol_z, bd_f)
    vel21 = evr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pbs_extdrv3_022_effort_vs_result_count_21d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21d exhaustion bar count — jerk in exhaustion bar frequency (ext_062 → extdrv2_022)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((volume > 2.0 * med_vol) & (bd_f < 0.20)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group G (023-025): Volume-spike and panic-RoC third-order ---

def pbs_extdrv3_023_volume_spike_count_21d_5d_diff_5d_diff(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day volume spike count — jerk in extreme-volume surge frequency (ext_069 → extdrv2_023)."""
    med_vol = _rolling_median(volume, _TD_MON)
    flag = (volume > 3.0 * med_vol).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_024_panic_freq_roc_21d_63d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Second 5-day diff of the 21d/63d panic frequency ratio — acceleration of frequency acceleration (ext_073 → extdrv2_024)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq21 = _rolling_sum(flag, _TD_MON) / _TD_MON
    freq63 = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    roc = _safe_div(freq21, freq63.clip(lower=_EPS))
    vel = roc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pbs_extdrv3_025_climax_intensity_roc_5d_21d_5d_diff_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of the 5d/21d climax intensity RoC — acceleration of climax escalation ratio velocity (ext_075 → extdrv2_025)."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    avg5 = _rolling_mean(intensity, _TD_WEEK)
    avg21 = _rolling_mean(intensity, _TD_MON)
    roc = _safe_div(avg5, avg21.clip(lower=_EPS))
    vel = roc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "pbs_extdrv3_001_bearish_marubozu_vol_score_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_001_bearish_marubozu_vol_score_5d_diff_5d_diff},
    "pbs_extdrv3_002_bearish_marubozu_vol_score_21d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_002_bearish_marubozu_vol_score_21d_diff_5d_diff},
    "pbs_extdrv3_003_marubozu_degree_ewm5_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_003_marubozu_degree_ewm5_5d_diff_5d_diff},
    "pbs_extdrv3_004_marubozu_degree_ewm5_slope_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_004_marubozu_degree_ewm5_slope_21d_5d_diff},
    "pbs_extdrv3_005_bearish_marubozu_count_5d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_005_bearish_marubozu_count_5d_5d_diff_5d_diff},
    "pbs_extdrv3_006_climax_intensity_bear_only_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_006_climax_intensity_bear_only_5d_diff_5d_diff},
    "pbs_extdrv3_007_climax_intensity_bear_only_slope_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_007_climax_intensity_bear_only_slope_21d_5d_diff},
    "pbs_extdrv3_008_climax_recency_decay_5d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_008_climax_recency_decay_5d_5d_diff_5d_diff},
    "pbs_extdrv3_009_climax_recency_decay_21d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_009_climax_recency_decay_21d_5d_diff_5d_diff},
    "pbs_extdrv3_010_range_vol_zscore_product_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "volume"],
        "func": pbs_extdrv3_010_range_vol_zscore_product_5d_diff_5d_diff},
    "pbs_extdrv3_011_hammer_vs_shooting_star_asymmetry_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_011_hammer_vs_shooting_star_asymmetry_5d_diff_5d_diff},
    "pbs_extdrv3_012_hammer_vs_shooting_star_asymmetry_21d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_012_hammer_vs_shooting_star_asymmetry_21d_diff_5d_diff},
    "pbs_extdrv3_013_lower_tail_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_013_lower_tail_count_21d_5d_diff_5d_diff},
    "pbs_extdrv3_014_gap_down_magnitude_pct_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv3_014_gap_down_magnitude_pct_5d_diff_5d_diff},
    "pbs_extdrv3_015_gap_down_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv3_015_gap_down_count_21d_5d_diff_5d_diff},
    "pbs_extdrv3_016_gap_down_total_loss_pct_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv3_016_gap_down_total_loss_pct_5d_diff_5d_diff},
    "pbs_extdrv3_017_body_midpoint_loc_21d_avg_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_017_body_midpoint_loc_21d_avg_5d_diff_5d_diff},
    "pbs_extdrv3_018_body_midpoint_loc_21d_avg_21d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_018_body_midpoint_loc_21d_avg_21d_diff_5d_diff},
    "pbs_extdrv3_019_body_midpoint_loc_slope_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_019_body_midpoint_loc_slope_21d_5d_diff},
    "pbs_extdrv3_020_effort_vs_result_ratio_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_020_effort_vs_result_ratio_5d_diff_5d_diff},
    "pbs_extdrv3_021_effort_vs_result_ratio_21d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_021_effort_vs_result_ratio_21d_diff_5d_diff},
    "pbs_extdrv3_022_effort_vs_result_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_022_effort_vs_result_count_21d_5d_diff_5d_diff},
    "pbs_extdrv3_023_volume_spike_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "volume"],
        "func": pbs_extdrv3_023_volume_spike_count_21d_5d_diff_5d_diff},
    "pbs_extdrv3_024_panic_freq_roc_21d_63d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv3_024_panic_freq_roc_21d_63d_5d_diff_5d_diff},
    "pbs_extdrv3_025_climax_intensity_roc_5d_21d_5d_diff_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv3_025_climax_intensity_roc_5d_21d_5d_diff_5d_diff},
}
