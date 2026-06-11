"""
45_panic_bar_signatures — Extended 2nd Derivatives (Features pbs_extdrv2_001-025)
Domain: rate of change of extended panic-bar signature features (extended base 001-075)
        — velocity of deeper panic morphology (marubozu, climax, spike/pin-bar,
          gap-and-wide-range, multi-bar sequence, body-location, effort-vs-result,
          volume-spike, intraday-reversal, panic RoC).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Net-new: derivatives sourced exclusively from extended-base-001-075 concepts;
not duplicates of pbs_drv2_001-025 which derive from the non-extended base.
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


# ── Extended 2nd-Derivative Feature Functions ────────────────────────────────

# --- Group A (001-005): Extended marubozu / vol-score derivatives ---

def pbs_extdrv2_001_bearish_marubozu_vol_score_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of the marubozu vol score (body_range_ratio * vol_zscore_21d on bear bars).
    Velocity of conviction-weighted selling morphology — from ext_010."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    score = frac.fillna(0.0) * vol_z * bear
    return score.diff(_TD_WEEK)


def pbs_extdrv2_002_bearish_marubozu_vol_score_21d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of the marubozu vol score — monthly velocity of ext_010."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    score = frac.fillna(0.0) * vol_z * bear
    return score.diff(_TD_MON)


def pbs_extdrv2_003_marubozu_degree_ewm5_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of the 5-day EWM of body/range ratio — acceleration of marubozu trend (ext_009)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    ewm_frac = _ewm_mean(frac, _TD_WEEK)
    return ewm_frac.diff(_TD_WEEK)


def pbs_extdrv2_004_bearish_marubozu_count_5d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 5-day bearish marubozu count — velocity of ultra-short-term conviction surge (ext_008)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((frac >= 0.80) & (close < open)).astype(float)
    cnt = _rolling_sum(flag, _TD_WEEK)
    return cnt.diff(_TD_WEEK)


def pbs_extdrv2_005_marubozu_degree_ewm5_slope_21d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """OLS slope over 21 days of 5-day EWM body/range ratio — sustained trend in ext_009."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    ewm_frac = _ewm_mean(frac, _TD_WEEK)
    return _linslope(ewm_frac, _TD_MON)


# --- Group B (006-010): Extended climax-bar derivatives ---

def pbs_extdrv2_006_climax_intensity_bear_only_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of bear-only climax intensity (range_z * vol_z * bear) — velocity of ext_016."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    bear = (close < open).astype(float)
    score = rng_z * vol_z * bear
    return score.diff(_TD_WEEK)


def pbs_extdrv2_007_climax_intensity_zscore_252d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 252d z-scored climax intensity — velocity of normalised ext_017."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    mi = _rolling_mean(intensity, _TD_YEAR)
    si = _rolling_std(intensity, _TD_YEAR)
    iz = _safe_div(intensity - mi, si)
    return iz.diff(_TD_WEEK)


def pbs_extdrv2_008_climax_recency_decay_5d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 5-day EWM of selling climax flag — velocity of short recency decay (ext_018)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    decay = _ewm_mean(flag, _TD_WEEK)
    return decay.diff(_TD_WEEK)


def pbs_extdrv2_009_climax_recency_decay_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM of selling climax flag — velocity of medium recency decay (ext_019)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    decay = _ewm_mean(flag, _TD_MON)
    return decay.diff(_TD_WEEK)


def pbs_extdrv2_010_range_vol_zscore_product_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of range-z * vol-z product (dual-normalised panic energy velocity) — ext_020."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng)
    m_vol = _rolling_mean(volume, _TD_QTR)
    s_vol = _rolling_std(volume, _TD_QTR)
    vol_z = _safe_div(volume - m_vol, s_vol)
    product = rng_z * vol_z
    return product.diff(_TD_WEEK)


# --- Group C (011-013): Pin-bar / tail asymmetry derivatives ---

def pbs_extdrv2_011_hammer_vs_shooting_star_asymmetry_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of (lower_tail_frac - upper_tail_frac) — velocity of intraday directional rejection asymmetry (ext_023)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    asym = lt_f - ut_f
    return asym.diff(_TD_WEEK)


def pbs_extdrv2_012_hammer_vs_shooting_star_asymmetry_21d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day diff of lower-tail vs upper-tail asymmetry — monthly velocity of ext_023."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    asym = lt_f - ut_f
    return asym.diff(_TD_MON)


def pbs_extdrv2_013_lower_tail_count_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 21-day count of strong-lower-tail bars — velocity of pin-bar frequency (ext_028)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    flag = (lt_f > 0.50).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


# --- Group D (014-016): Gap-down and sequence derivatives ---

def pbs_extdrv2_014_gap_down_magnitude_pct_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of gap-down magnitude pct — velocity of downward opening dislocations (ext_031)."""
    prior_close = close.shift(1)
    gap = (prior_close - open) / prior_close.clip(lower=_EPS)
    gap_mag = gap.clip(lower=0.0)
    return gap_mag.diff(_TD_WEEK)


def pbs_extdrv2_015_gap_down_count_21d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 21-day gap-down count — velocity of gap-down frequency (ext_037)."""
    prior_close = close.shift(1)
    gap_down = (open < prior_close).astype(float)
    cnt = _rolling_sum(gap_down, _TD_MON)
    return cnt.diff(_TD_WEEK)


def pbs_extdrv2_016_gap_down_total_loss_pct_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of total session loss pct from prior close — velocity of ext_040 (gap+close decline)."""
    prior_close = close.shift(1)
    loss = ((prior_close - close) / prior_close.clip(lower=_EPS)).clip(lower=0.0)
    return loss.diff(_TD_WEEK)


# --- Group E (017-019): Body-location derivatives ---

def pbs_extdrv2_017_body_midpoint_loc_21d_avg_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 21-day rolling mean body midpoint location — velocity of downward body drift (ext_057)."""
    bml = _body_midpoint_loc(open, close, high, low)
    avg_bml = _rolling_mean(bml, _TD_MON)
    return avg_bml.diff(_TD_WEEK)


def pbs_extdrv2_018_body_midpoint_loc_21d_avg_21d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day diff of 21-day rolling mean body midpoint location — monthly velocity of ext_057."""
    bml = _body_midpoint_loc(open, close, high, low)
    avg_bml = _rolling_mean(bml, _TD_MON)
    return avg_bml.diff(_TD_MON)


def pbs_extdrv2_019_body_midpoint_loc_slope_21d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """OLS slope over 21 days of body midpoint location — sustained trend toward session-low body positioning (ext_051)."""
    bml = _body_midpoint_loc(open, close, high, low)
    return _linslope(bml, _TD_MON)


# --- Group F (020-022): Effort-vs-result derivatives ---

def pbs_extdrv2_020_effort_vs_result_ratio_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of effort-vs-result ratio (vol_z / body_range_frac) — velocity of absorption pressure (ext_059)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS)).clip(lower=_EPS)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    evr = _safe_div(vol_z, bd_f)
    return evr.diff(_TD_WEEK)


def pbs_extdrv2_021_effort_vs_result_ratio_21d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of effort-vs-result ratio — monthly velocity of absorption pressure (ext_059)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS)).clip(lower=_EPS)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    evr = _safe_div(vol_z, bd_f)
    return evr.diff(_TD_MON)


def pbs_extdrv2_022_effort_vs_result_count_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day count of effort-vs-result bars — velocity of exhaustion bar frequency (ext_062)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((volume > 2.0 * med_vol) & (bd_f < 0.20)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


# --- Group G (023-025): Volume-spike and panic-RoC derivatives ---

def pbs_extdrv2_023_volume_spike_count_21d_5d_diff(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day volume spike count (>3x 21d median) — velocity of extreme-vol surge frequency (ext_069)."""
    med_vol = _rolling_median(volume, _TD_MON)
    flag = (volume > 3.0 * med_vol).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def pbs_extdrv2_024_panic_freq_roc_21d_63d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of the 21d/63d panic frequency ratio — velocity of the frequency acceleration metric (ext_073)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq21 = _rolling_sum(flag, _TD_MON) / _TD_MON
    freq63 = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    roc = _safe_div(freq21, freq63.clip(lower=_EPS))
    return roc.diff(_TD_WEEK)


def pbs_extdrv2_025_climax_intensity_roc_5d_21d_5d_diff(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of the 5d/21d climax intensity RoC — velocity of the escalation ratio (ext_075)."""
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
    return roc.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "pbs_extdrv2_001_bearish_marubozu_vol_score_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_001_bearish_marubozu_vol_score_5d_diff},
    "pbs_extdrv2_002_bearish_marubozu_vol_score_21d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_002_bearish_marubozu_vol_score_21d_diff},
    "pbs_extdrv2_003_marubozu_degree_ewm5_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_003_marubozu_degree_ewm5_5d_diff},
    "pbs_extdrv2_004_bearish_marubozu_count_5d_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_004_bearish_marubozu_count_5d_5d_diff},
    "pbs_extdrv2_005_marubozu_degree_ewm5_slope_21d": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_005_marubozu_degree_ewm5_slope_21d},
    "pbs_extdrv2_006_climax_intensity_bear_only_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_006_climax_intensity_bear_only_5d_diff},
    "pbs_extdrv2_007_climax_intensity_zscore_252d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_007_climax_intensity_zscore_252d_5d_diff},
    "pbs_extdrv2_008_climax_recency_decay_5d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_008_climax_recency_decay_5d_5d_diff},
    "pbs_extdrv2_009_climax_recency_decay_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_009_climax_recency_decay_21d_5d_diff},
    "pbs_extdrv2_010_range_vol_zscore_product_5d_diff": {
        "inputs": ["close", "high", "low", "volume"],
        "func": pbs_extdrv2_010_range_vol_zscore_product_5d_diff},
    "pbs_extdrv2_011_hammer_vs_shooting_star_asymmetry_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_011_hammer_vs_shooting_star_asymmetry_5d_diff},
    "pbs_extdrv2_012_hammer_vs_shooting_star_asymmetry_21d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_012_hammer_vs_shooting_star_asymmetry_21d_diff},
    "pbs_extdrv2_013_lower_tail_count_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_013_lower_tail_count_21d_5d_diff},
    "pbs_extdrv2_014_gap_down_magnitude_pct_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv2_014_gap_down_magnitude_pct_5d_diff},
    "pbs_extdrv2_015_gap_down_count_21d_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv2_015_gap_down_count_21d_5d_diff},
    "pbs_extdrv2_016_gap_down_total_loss_pct_5d_diff": {
        "inputs": ["close", "open"],
        "func": pbs_extdrv2_016_gap_down_total_loss_pct_5d_diff},
    "pbs_extdrv2_017_body_midpoint_loc_21d_avg_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_017_body_midpoint_loc_21d_avg_5d_diff},
    "pbs_extdrv2_018_body_midpoint_loc_21d_avg_21d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_018_body_midpoint_loc_21d_avg_21d_diff},
    "pbs_extdrv2_019_body_midpoint_loc_slope_21d": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_019_body_midpoint_loc_slope_21d},
    "pbs_extdrv2_020_effort_vs_result_ratio_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_020_effort_vs_result_ratio_5d_diff},
    "pbs_extdrv2_021_effort_vs_result_ratio_21d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_021_effort_vs_result_ratio_21d_diff},
    "pbs_extdrv2_022_effort_vs_result_count_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_022_effort_vs_result_count_21d_5d_diff},
    "pbs_extdrv2_023_volume_spike_count_21d_5d_diff": {
        "inputs": ["close", "volume"],
        "func": pbs_extdrv2_023_volume_spike_count_21d_5d_diff},
    "pbs_extdrv2_024_panic_freq_roc_21d_63d_5d_diff": {
        "inputs": ["close", "high", "low", "open"],
        "func": pbs_extdrv2_024_panic_freq_roc_21d_63d_5d_diff},
    "pbs_extdrv2_025_climax_intensity_roc_5d_21d_5d_diff": {
        "inputs": ["close", "high", "low", "open", "volume"],
        "func": pbs_extdrv2_025_climax_intensity_roc_5d_21d_5d_diff},
}
