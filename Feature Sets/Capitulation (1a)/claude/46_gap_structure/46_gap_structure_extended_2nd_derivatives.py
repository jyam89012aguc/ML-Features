"""
46_gap_structure — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended-base gap-structure features (ext_001-075) — velocity of
        per-type z-scores, fill dynamics, vol profiles, gap-fill overhang, cumulative return
        contributions, direction persistence, dispersion, range-ratio, tail distribution,
        run statistics, frequency acceleration, and composite distress scores.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight gap as fraction of prior close."""
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(lower=0)


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(upper=0).abs()


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


# ── Gap-type classification helpers (self-contained) ─────────────────────────

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True,
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _exhaustion_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                               low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    maturity = _trend_maturity(close, _TD_QTR)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & late_downtrend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                              low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & (rng_pos <= 0.1) & (vol_r > 1.2)).astype(float)


def _runaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                      low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    mid_trend = (maturity > 0.3) & (maturity < 0.72)
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & mid_trend & inside_range & (vol_r > 0.8)).astype(float)


def _exhaustion_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                         low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    late_uptrend = (trend_dir > 0) & (maturity > 0.75)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    late_trend = late_uptrend | late_downtrend
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & late_trend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                        low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    outside_range = (rng_pos <= 0.1) | (rng_pos >= 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & outside_range & (vol_r > 1.2)).astype(float)


def _common_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                     low: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    return ((ag > _EPS) & (ag < 0.005) & inside_range).astype(float)


def _prior_day_range_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    pc = close.shift(1).abs().clip(lower=_EPS)
    return _safe_div(high.shift(1) - low.shift(1), pc)


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

# --- extdrv2_001-005: Velocity of per-type magnitude z-scores (ext_001-005) ---

def gap_extdrv2_001_exhaustion_down_mag_zscore_252d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 252d exhaustion-down magnitude z-score (velocity of capitulation extremity)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    z = _safe_div(mag_on_type - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def gap_extdrv2_002_breakaway_down_mag_zscore_252d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 252d breakaway-down magnitude z-score (velocity of breakaway extremity)."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    z = _safe_div(mag_on_type - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def gap_extdrv2_003_exhaustion_down_mag_zscore_63d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 63d exhaustion-down magnitude z-score (monthly velocity of z-score regime)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_QTR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_QTR, min_periods=2).std()
    z = _safe_div(mag_on_type - m, s.clip(lower=_EPS))
    return z.diff(_TD_MON)


def gap_extdrv2_004_common_gap_mag_zscore_252d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 252d common-gap magnitude z-score (velocity of common-gap extremity)."""
    flag = _common_gap_flag(close, open, high, low)
    ag = _gap_pct(close, open).abs()
    mag_on_type = ag.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    z = _safe_div(mag_on_type - m, s.clip(lower=_EPS))
    return z.diff(_TD_MON)


def gap_extdrv2_005_runaway_down_mag_zscore_252d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 252d runaway-down magnitude z-score."""
    run_flag = _runaway_gap_flag(close, open, high, low, volume)
    g = _gap_pct(close, open)
    dg = _gap_down(close, open)
    combined = (run_flag > 0) & (g < 0)
    mag_on_type = dg.where(combined, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    z = _safe_div(mag_on_type - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


# --- extdrv2_006-009: Velocity of per-type volume z-scores (ext_011-015) ---

def gap_extdrv2_006_exhaustion_down_vol_zscore_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 63d exhaustion-down volume z-score (velocity of capitulation vol extremity)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    vol_on_type = volume.where(flag > 0, np.nan)
    m = vol_on_type.rolling(_TD_QTR, min_periods=1).mean()
    s = vol_on_type.rolling(_TD_QTR, min_periods=2).std()
    z = _safe_div(volume.where(flag > 0, np.nan) - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def gap_extdrv2_007_exhaustion_down_vol_avg_252d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 252d exhaustion-down avg vol-ratio (velocity of long-run vol profile)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    avg = vol_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    return avg.diff(_TD_MON)


def gap_extdrv2_008_breakaway_down_vol_avg_252d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 252d breakaway-down avg vol-ratio."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    avg = vol_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    return avg.diff(_TD_MON)


def gap_extdrv2_009_runaway_vol_avg_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 63d runaway-gap avg vol-ratio (velocity of runaway vol premium)."""
    flag = _runaway_gap_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    avg = vol_on_type.rolling(_TD_QTR, min_periods=1).mean()
    return avg.diff(_TD_WEEK)


# --- extdrv2_010-012: Velocity of gap-fill dynamics (ext_021-022) ---

def gap_extdrv2_010_partial_fill_fraction_21d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day rolling partial gap-fill fraction (velocity of intraday fill rate)."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    dn_gap = gap_price < 0
    up_gap = gap_price > 0
    dn_frac = _safe_div((high - open).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    up_frac = _safe_div((open - low).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    partial = pd.Series(np.nan, index=close.index)
    partial = partial.where(~dn_gap, dn_frac)
    partial = partial.where(~up_gap, up_frac)
    fill_21 = partial.rolling(_TD_MON, min_periods=1).mean()
    return fill_21.diff(_TD_WEEK)


def gap_extdrv2_011_partial_fill_fraction_5d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 5-day rolling partial gap-fill fraction (monthly shift in intraday fill)."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    dn_gap = gap_price < 0
    up_gap = gap_price > 0
    dn_frac = _safe_div((high - open).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    up_frac = _safe_div((open - low).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    partial = pd.Series(np.nan, index=close.index)
    partial = partial.where(~dn_gap, dn_frac)
    partial = partial.where(~up_gap, up_frac)
    fill_5 = partial.rolling(_TD_WEEK, min_periods=1).mean()
    return fill_5.diff(_TD_MON)


def gap_extdrv2_012_unfilled_down_gap_count_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of unfilled-down-gap count in trailing 63d (velocity of overhead gap supply)."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    w = _TD_QTR
    total_unfilled = pd.Series(0.0, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        dg_k = (gap_price.shift(k) < 0)
        rh_k = high.rolling(k, min_periods=1).max()
        filled_k = dg_k & (rh_k >= pc_k)
        unfilled_k = (dg_k & ~filled_k).astype(float)
        total_unfilled = total_unfilled + unfilled_k
    return total_unfilled.diff(_TD_WEEK)


# --- extdrv2_013-015: Velocity of cumulative gap return contributions (ext_028-034) ---

def gap_extdrv2_013_gap_cumret_vs_total_126d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 126d gap-return share of total return (velocity of overnight return dominance)."""
    gap_sum = _rolling_sum(_gap_pct(close, open), _TD_HALF)
    total_sum = _rolling_sum(close.pct_change(1), _TD_HALF)
    ratio = _safe_div(gap_sum, total_sum.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def gap_extdrv2_014_gap_adjusted_return_21d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 21-day intraday-only return component (total minus overnight gap sum)."""
    total_ret = _rolling_sum(close.pct_change(1), _TD_MON)
    gap_ret = _rolling_sum(_gap_pct(close, open), _TD_MON)
    intra = total_ret - gap_ret
    return intra.diff(_TD_WEEK)


def gap_extdrv2_015_gap_net_contribution_126d_21d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day diff of 126d net gap contribution (up_sum-dn_sum)/abs_ret (shift in net overnight bias)."""
    up_sum = _rolling_sum(_gap_up(close, open), _TD_HALF)
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_HALF)
    tot_abs = _rolling_sum(close.pct_change(1).abs(), _TD_HALF).clip(lower=_EPS)
    net_share = _safe_div(up_sum - dn_sum, tot_abs)
    return net_share.diff(_TD_MON)


# --- extdrv2_016-018: Velocity of gap dispersion features (ext_042-047) ---

def gap_extdrv2_016_gap_iqr_63d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 63d gap IQR (velocity of gap dispersion widening/narrowing)."""
    g = _gap_pct(close, open)
    q75 = g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    return iqr.diff(_TD_WEEK)


def gap_extdrv2_017_gap_down_dispersion_ratio_63d_21d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day diff of 63d down/up gap dispersion ratio (velocity of downside skew in gap vol)."""
    dg = _gap_down(close, open)
    ug = _gap_up(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    ug_nan = ug.where(ug > 0, np.nan)
    std_dn = dg_nan.rolling(_TD_QTR, min_periods=2).std()
    std_up = ug_nan.rolling(_TD_QTR, min_periods=2).std()
    ratio = _safe_div(std_dn, std_up.clip(lower=_EPS))
    return ratio.diff(_TD_MON)


def gap_extdrv2_018_gap_std_short_vs_long_ratio_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 5d/63d gap std ratio (velocity of very short vs medium regime shift signal)."""
    ag = _gap_pct(close, open)
    s5 = _rolling_std(ag, _TD_WEEK)
    s63 = _rolling_std(ag, _TD_QTR)
    ratio = _safe_div(s5, s63.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


# --- extdrv2_019-020: Velocity of gap vs prior-range features (ext_048-053) ---

def gap_extdrv2_019_gap_vs_prior_range_ratio_21d_avg_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21d avg abs-gap/prior-range ratio (velocity of gap size relative to prior range)."""
    ag = _gap_pct(close, open).abs()
    pc = close.shift(1).abs().clip(lower=_EPS)
    prior_range = _safe_div(high.shift(1) - low.shift(1), pc).clip(lower=_EPS)
    ratio = _safe_div(ag, prior_range)
    avg21 = _rolling_mean(ratio, _TD_MON)
    return avg21.diff(_TD_WEEK)


def gap_extdrv2_020_gap_exceeds_prior_range_freq_63d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63d frequency of gaps exceeding prior H-L range (velocity of extreme-gap frequency)."""
    ag = _gap_pct(close, open).abs()
    pc = close.shift(1).abs().clip(lower=_EPS)
    prior_range = _safe_div(high.shift(1) - low.shift(1), pc).clip(lower=_EPS)
    ratio = _safe_div(ag, prior_range)
    freq = _rolling_count_true(ratio > 1.0, _TD_QTR) / _TD_QTR
    return freq.diff(_TD_MON)


# --- extdrv2_021-022: Velocity of overnight return tail features (ext_056-060) ---

def gap_extdrv2_021_overnight_ret_left_tail_mass_63d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 63d left-tail probability mass (<-2% gaps) — velocity of fat-tail buildup."""
    g = _gap_pct(close, open)
    left_mass = _rolling_count_true(g < -0.02, _TD_QTR) / _TD_QTR
    return left_mass.diff(_TD_WEEK)


def gap_extdrv2_022_overnight_ret_tail_asymmetry_63d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day diff of 63d tail asymmetry (left minus right tail mass) — velocity of tail imbalance."""
    g = _gap_pct(close, open)
    left_mass = _rolling_count_true(g < -0.02, _TD_QTR) / _TD_QTR
    right_mass = _rolling_count_true(g > 0.02, _TD_QTR) / _TD_QTR
    asym = left_mass - right_mass
    return asym.diff(_TD_WEEK)


# --- extdrv2_023-025: Velocity of composite distress and cluster features (ext_073-075) ---

def gap_extdrv2_023_gap_type_down_distress_score_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 63d weighted down-gap distress score (exh=3, breakaway=2, runaway=1)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    run_flag = _runaway_gap_flag(close, open, high, low, volume)
    g = _gap_pct(close, open)
    run_dn = ((run_flag > 0) & (g < 0)).astype(float)
    score = 3.0 * ex_dn + 2.0 * ba_dn + 1.0 * run_dn
    score_63 = _rolling_sum(score, _TD_QTR)
    return score_63.diff(_TD_WEEK)


def gap_extdrv2_024_exhaustion_down_count_126d_21d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 126d exhaustion-down gap count (velocity of half-year capitulation accumulation)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_HALF)
    return cnt.diff(_TD_MON)


def gap_extdrv2_025_gap_type_cluster_freq_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 63d gap-type cluster frequency (exh+breakaway within 5d) — velocity of clustering."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    ex_in_5d = _rolling_sum(ex_dn, _TD_WEEK) > 0
    ba_in_5d = _rolling_sum(ba_dn, _TD_WEEK) > 0
    cluster = (ex_in_5d & ba_in_5d).astype(float)
    freq = _rolling_count_true(cluster > 0, _TD_QTR) / _TD_QTR
    return freq.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "gap_extdrv2_001_exhaustion_down_mag_zscore_252d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_001_exhaustion_down_mag_zscore_252d_5d_diff,
    },
    "gap_extdrv2_002_breakaway_down_mag_zscore_252d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_002_breakaway_down_mag_zscore_252d_5d_diff,
    },
    "gap_extdrv2_003_exhaustion_down_mag_zscore_63d_21d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_003_exhaustion_down_mag_zscore_63d_21d_diff,
    },
    "gap_extdrv2_004_common_gap_mag_zscore_252d_21d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_004_common_gap_mag_zscore_252d_21d_diff,
    },
    "gap_extdrv2_005_runaway_down_mag_zscore_252d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_005_runaway_down_mag_zscore_252d_5d_diff,
    },
    "gap_extdrv2_006_exhaustion_down_vol_zscore_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_006_exhaustion_down_vol_zscore_63d_5d_diff,
    },
    "gap_extdrv2_007_exhaustion_down_vol_avg_252d_21d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_007_exhaustion_down_vol_avg_252d_21d_diff,
    },
    "gap_extdrv2_008_breakaway_down_vol_avg_252d_21d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_008_breakaway_down_vol_avg_252d_21d_diff,
    },
    "gap_extdrv2_009_runaway_vol_avg_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_009_runaway_vol_avg_63d_5d_diff,
    },
    "gap_extdrv2_010_partial_fill_fraction_21d_5d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_010_partial_fill_fraction_21d_5d_diff,
    },
    "gap_extdrv2_011_partial_fill_fraction_5d_21d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_011_partial_fill_fraction_5d_21d_diff,
    },
    "gap_extdrv2_012_unfilled_down_gap_count_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_012_unfilled_down_gap_count_63d_5d_diff,
    },
    "gap_extdrv2_013_gap_cumret_vs_total_126d_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_013_gap_cumret_vs_total_126d_5d_diff,
    },
    "gap_extdrv2_014_gap_adjusted_return_21d_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_014_gap_adjusted_return_21d_5d_diff,
    },
    "gap_extdrv2_015_gap_net_contribution_126d_21d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_015_gap_net_contribution_126d_21d_diff,
    },
    "gap_extdrv2_016_gap_iqr_63d_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_016_gap_iqr_63d_5d_diff,
    },
    "gap_extdrv2_017_gap_down_dispersion_ratio_63d_21d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_017_gap_down_dispersion_ratio_63d_21d_diff,
    },
    "gap_extdrv2_018_gap_std_short_vs_long_ratio_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_018_gap_std_short_vs_long_ratio_5d_diff,
    },
    "gap_extdrv2_019_gap_vs_prior_range_ratio_21d_avg_5d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_019_gap_vs_prior_range_ratio_21d_avg_5d_diff,
    },
    "gap_extdrv2_020_gap_exceeds_prior_range_freq_63d_21d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gap_extdrv2_020_gap_exceeds_prior_range_freq_63d_21d_diff,
    },
    "gap_extdrv2_021_overnight_ret_left_tail_mass_63d_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_021_overnight_ret_left_tail_mass_63d_5d_diff,
    },
    "gap_extdrv2_022_overnight_ret_tail_asymmetry_63d_5d_diff": {
        "inputs": ["close", "open"],
        "func": gap_extdrv2_022_overnight_ret_tail_asymmetry_63d_5d_diff,
    },
    "gap_extdrv2_023_gap_type_down_distress_score_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_023_gap_type_down_distress_score_63d_5d_diff,
    },
    "gap_extdrv2_024_exhaustion_down_count_126d_21d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_024_exhaustion_down_count_126d_21d_diff,
    },
    "gap_extdrv2_025_gap_type_cluster_freq_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low", "volume"],
        "func": gap_extdrv2_025_gap_type_cluster_freq_63d_5d_diff,
    },
}
