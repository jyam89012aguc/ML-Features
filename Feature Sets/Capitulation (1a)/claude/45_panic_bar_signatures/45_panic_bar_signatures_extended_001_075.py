"""
45_panic_bar_signatures — Extended Features 001-075
Domain: wide-range / long-tail bar patterns at the low — deeper panic-bar coverage
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Net-new extensions: deeper marubozu/climax thresholds, volume-confirmed variants,
spike/pin-bar/shooting-star asymmetry, gap-and-wide-range, range-vs-volume z-score
products, multi-bar panic sequences, bar-body location, effort-vs-result exhaustion,
volume-spike bars, widest-bar-in-window recency, intraday-reversal magnitude,
RoC and acceleration of panic frequency/intensity.
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Deeper marubozu thresholds & volume-confirmed variants ---

def pbs_ext_001_bearish_marubozu_flag_70pct(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: body/range >= 70% AND close < open (moderate bearish marubozu threshold,
    lower than existing 80/90% variants)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((frac >= 0.70) & (close < open)).astype(float)


def pbs_ext_002_bearish_marubozu_flag_95pct(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: body/range >= 95% AND close < open (near-perfect bearish marubozu, strictest
    threshold — essentially zero wicks, maximum selling conviction)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((frac >= 0.95) & (close < open)).astype(float)


def pbs_ext_003_bearish_marubozu_3x_vol_confirmed(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: bearish marubozu (body>80% range) AND volume > 3x 21-day median.
    Stricter volume confirmation than existing 2x variant (pbs_095)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    return ((frac >= 0.80) & (close < open) & (volume > 3.0 * med_vol)).astype(float)


def pbs_ext_004_bearish_marubozu_wide_3x_vol_confirmed(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: bearish marubozu (body>80%) AND range > 2x avg AND volume > 2x median.
    Triple-confirmation: full-body, wide range, extreme volume."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    return ((frac >= 0.80) & (close < open) & (rng > 2.0 * avg)
            & (volume > 2.0 * med_vol)).astype(float)


def pbs_ext_005_bearish_marubozu_near_52wk_low_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: bearish marubozu (body>80%) AND close within 5% of 252-day closing low.
    Marks full-conviction selling near annual lows — deeper than pbs_064 which uses 21d."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    roll_min = close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    near_low = (close - roll_min) / roll_min.clip(lower=_EPS) < 0.05
    return ((frac >= 0.80) & (close < open) & near_low).astype(float)


def pbs_ext_006_bearish_marubozu_streak(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of consecutive bearish marubozu bars (body>80%, close<open) ending today
    (running streak length; resets to 0 on any non-marubozu day)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((frac >= 0.80) & (close < open)).astype(float).fillna(0.0)
    streak = flag.copy()
    for i in range(1, len(flag)):
        if flag.iloc[i] == 1.0:
            streak.iloc[i] = streak.iloc[i - 1] + 1.0
        else:
            streak.iloc[i] = 0.0
    return streak


def pbs_ext_007_bullish_marubozu_flag_70pct(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: body/range >= 70% AND close > open (moderate bullish marubozu — lower
    threshold than existing 80/90% variants, captures post-panic recovery bars)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((frac >= 0.70) & (close > open)).astype(float)


def pbs_ext_008_bearish_marubozu_count_5d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of bearish marubozu bars (body>80%, close<open) in trailing 5 days.
    Short window not present in existing 21/63/252 counts."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((frac >= 0.80) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def pbs_ext_009_marubozu_degree_ewm_5d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """5-day EWM of body/range ratio (smooth short-term marubozu degree trend).
    Captures trend in bar conviction morphology, distinct from raw ratio."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    return _ewm_mean(frac, _TD_WEEK)


def pbs_ext_010_bearish_marubozu_vol_score(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Continuous score: body_range_ratio * volume_zscore_21d on bear bars, else 0.
    Combines conviction morphology with volume intensity."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    bear = (close < open).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    return frac.fillna(0.0) * vol_z * bear


# --- Group B (011-020): Climax-bar deeper variants ---

def pbs_ext_011_selling_climax_3x_range_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: range > 3x 21-day avg AND volume > 2x median AND close < open.
    Extreme version of selling climax — range threshold upgraded from 2x to 3x."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    return ((rng > 3.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)


def pbs_ext_012_selling_climax_3x_vol_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: range > 2x avg AND volume > 3x median AND close < open.
    Volume threshold upgraded to 3x — captures ultra-high-volume panic bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    return ((rng > 2.0 * avg) & (volume > 3.0 * med_vol) & (close < open)).astype(float)


def pbs_ext_013_climax_bar_near_low_vol_confirmed(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: selling climax (range>2x, vol>2x median, close<open) AND close within
    bottom 10% of range. Combines extreme selling with session-low close and volume."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    clv = _close_loc(close, high, low)
    return ((rng > 2.0 * avg) & (volume > 2.0 * med_vol)
            & (close < open) & (clv <= 0.10)).astype(float)


def pbs_ext_014_climax_count_5d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Count of selling climax bars in trailing 5 days (ultra-short window).
    Complements existing 21/63/252 counts with a week-scale view."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def pbs_ext_015_climax_vol_fraction_63d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fraction of 63-day total volume occurring on selling climax bars.
    Distinct from existing pbs_098 which uses panic bars and 21d window."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    is_climax = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    climax_vol = _rolling_sum(volume * is_climax, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(climax_vol, total_vol)


def pbs_ext_016_climax_intensity_score_bear_only(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Climax intensity (range_z * vol_z) restricted to bear bars (close < open).
    Unlike pbs_070 which is unsigned, this is zeroed on bull bars."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    bear = (close < open).astype(float)
    return rng_z * vol_z * bear


def pbs_ext_017_climax_intensity_zscore_252d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of climax intensity (range_z * vol_z) vs 252-day distribution.
    Normalises the intensity score to historical context."""
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
    return _safe_div(intensity - mi, si)


def pbs_ext_018_selling_climax_recency_decay_5d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day EWM of selling climax flag (short recency decay of climax events).
    Distinct from pbs_078/pbs_080 which decay panic/exhaustion bars not climax."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    return _ewm_mean(flag, _TD_WEEK)


def pbs_ext_019_selling_climax_recency_decay_21d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day EWM of selling climax flag (medium recency decay)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    return _ewm_mean(flag, _TD_MON)


def pbs_ext_020_range_vol_zscore_product(
    close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Product of range z-score (252d) and volume z-score (63d) — dual-normalized
    panic energy proxy. Distinct from pbs_070 which clips at 0 and uses 21d vol window."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng)
    m_vol = _rolling_mean(volume, _TD_QTR)
    s_vol = _rolling_std(volume, _TD_QTR)
    vol_z = _safe_div(volume - m_vol, s_vol)
    return rng_z * vol_z


# --- Group C (021-030): Spike-bar / pin-bar / shooting-star vs hammer asymmetry ---

def pbs_ext_021_pin_bar_hammer_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: lower tail > 67% of range AND upper tail < 15% of range AND body < 20% of range.
    Strict pin-bar hammer: dominant lower wick, tiny upper wick, small body."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    body = _body(open, close)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    return ((lt_f > 0.67) & (ut_f < 0.15) & (bd_f < 0.20)).astype(float)


def pbs_ext_022_shooting_star_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: upper tail > 67% of range AND lower tail < 15% of range AND body < 20% of range.
    Shooting star (bearish intraday rejection at high) — asymmetric to pin-bar hammer."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    body = _body(open, close)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    return ((ut_f > 0.67) & (lt_f < 0.15) & (bd_f < 0.20)).astype(float)


def pbs_ext_023_hammer_vs_shooting_star_asymmetry(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Lower tail fraction minus upper tail fraction: positive = hammer bias,
    negative = shooting star bias. Measures intraday directional rejection asymmetry."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    return lt_f - ut_f


def pbs_ext_024_pin_bar_hammer_wide_range_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: pin-bar hammer morphology AND range > 2x 21-day avg.
    Wide-range pin bar at panic lows — distinct from pbs_022 (uses lt>50%, no ut constraint)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    body = _body(open, close)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    pin = (lt_f > 0.67) & (ut_f < 0.15) & (bd_f < 0.20)
    return (pin & (rng > 2.0 * avg)).astype(float)


def pbs_ext_025_pin_bar_vol_confirmed_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: pin-bar hammer AND volume > 2x 21-day median (volume-confirmed capitulation pin)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    body = _body(open, close)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    ut_f = _safe_div(ut, rng.clip(lower=_EPS))
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    pin = (lt_f > 0.67) & (ut_f < 0.15) & (bd_f < 0.20)
    med_vol = _rolling_median(volume, _TD_MON)
    return (pin & (volume > 2.0 * med_vol)).astype(float)


def pbs_ext_026_lower_tail_gt3x_body_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: lower tail > 3x body size (extreme pin-bar/spike rejection).
    Stricter than existing pbs_028 which uses 2x body threshold."""
    lt = _lower_tail(open, close, low)
    body = _body(open, close).clip(lower=_EPS)
    return (lt > 3.0 * body).astype(float)


def pbs_ext_027_upper_tail_gt3x_body_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: upper tail > 3x body size (shooting-star/supply spike bar).
    Captures extreme upper-wick rejection — no equivalent in existing features."""
    ut = _upper_tail(open, close, high)
    body = _body(open, close).clip(lower=_EPS)
    return (ut > 3.0 * body).astype(float)


def pbs_ext_028_lower_tail_count_21d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of strong lower-tail bars (lt > 50% range) in trailing 21 days.
    Distinct from exhaustion bar count — no range-width requirement."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    flag = (lt_f > 0.50).astype(float)
    return _rolling_sum(flag, _TD_MON)


def pbs_ext_029_lower_tail_pct_rank_63d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Percentile rank of lower-tail/range fraction in trailing 63-day distribution.
    Complements pbs_024 (252d) and pbs_025 (63d raw) with the 63d pct rank."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    return lt_f.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def pbs_ext_030_lower_tail_zscore_63d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Z-score of lower tail length vs 63-day distribution.
    Complements pbs_023 (252d) with a shorter reference window."""
    lt = _lower_tail(open, close, low)
    m = _rolling_mean(lt, _TD_QTR)
    s = _rolling_std(lt, _TD_QTR)
    return _safe_div(lt - m, s)


# --- Group D (031-040): Gap-and-wide-range panic bars ---

def pbs_ext_031_gap_down_magnitude_pct(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Gap-down magnitude: (prior_close - open) / prior_close, clipped at 0.
    Measures size of opening gap below prior close (0 if gap up or flat)."""
    prior_close = close.shift(1)
    gap = (prior_close - open) / prior_close.clip(lower=_EPS)
    return gap.clip(lower=0.0)


def pbs_ext_032_gap_down_wide_range_score(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Continuous score: gap_down_magnitude_pct * range_ratio_21d.
    Products gap severity with bar width — captures panic gap-open days."""
    gap = pbs_ext_031_gap_down_magnitude_pct(close, open)
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return gap * rr.fillna(0.0)


def pbs_ext_033_gap_down_3pct_wide_range_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: gap-down > 3% AND range > 2x 21-day avg.
    Captures large-gap panic openings — distinct from pbs_037 which has no gap-size floor."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    gap = pbs_ext_031_gap_down_magnitude_pct(close, open)
    return ((gap > 0.03) & (rng > 2.0 * avg)).astype(float)


def pbs_ext_034_gap_down_close_below_gap_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: gap-down AND close below open (no intraday recovery; gap filled down).
    Bears won the session after a bad opening — full continuation panic."""
    prior_close = close.shift(1)
    gap_down = open < prior_close
    return (gap_down & (close < open)).astype(float)


def pbs_ext_035_gap_fill_pct_on_gap_day(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """On gap-down days: fraction of gap filled by close = (close - open) / (prior_close - open).
    0 = close at open (zero fill), 1 = close at prior close (full gap fill).
    Measures intraday recovery after panic gap open."""
    prior_close = close.shift(1)
    gap = (prior_close - open).clip(lower=_EPS)
    fill = (close - open) / gap
    gap_down = open < prior_close
    return fill.where(gap_down, np.nan)


def pbs_ext_036_gap_down_vol_spike_flag(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: gap-down open AND volume > 2x 21-day median (panic gap with volume confirmation)."""
    prior_close = close.shift(1)
    gap_down = open < prior_close
    med_vol = _rolling_median(volume, _TD_MON)
    return (gap_down & (volume > 2.0 * med_vol)).astype(float)


def pbs_ext_037_gap_down_count_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of gap-down open days in trailing 21 days (frequency of downward gaps)."""
    prior_close = close.shift(1)
    gap_down = (open < prior_close).astype(float)
    return _rolling_sum(gap_down, _TD_MON)


def pbs_ext_038_gap_down_count_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of gap-down open days in trailing 63 days."""
    prior_close = close.shift(1)
    gap_down = (open < prior_close).astype(float)
    return _rolling_sum(gap_down, _TD_QTR)


def pbs_ext_039_gap_down_marubozu_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: gap-down open AND bearish marubozu (body>80%, close<open).
    Combines opening gap dislocation with full-conviction close — extreme panic day."""
    prior_close = close.shift(1)
    gap_down = open < prior_close
    body = _body(open, close)
    rng = _bar_range(high, low)
    frac = _safe_div(body, rng.clip(lower=_EPS))
    return (gap_down & (frac >= 0.80) & (close < open)).astype(float)


def pbs_ext_040_gap_down_total_loss_pct(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Total session loss from prior close: (prior_close - close) / prior_close.
    Captures combined gap + close decline; positive = session net loss vs prior close."""
    prior_close = close.shift(1)
    return ((prior_close - close) / prior_close.clip(lower=_EPS)).clip(lower=0.0)


# --- Group E (041-050): Multi-bar panic sequences ---

def pbs_ext_041_consec_wide_down_bars_2(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: 2 consecutive wide-range bear bars (range > 2x avg, close < open)
    ending today (t-1 and t both qualify). Multi-bar panic sequence."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = ((rng > 2.0 * avg) & (close < open)).astype(float)
    return ((flag == 1.0) & (flag.shift(1) == 1.0)).astype(float)


def pbs_ext_042_consec_wide_down_bars_3(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: 3 consecutive wide-range bear bars ending today. Extreme panic sequence."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = ((rng > 2.0 * avg) & (close < open)).astype(float)
    return ((flag == 1.0) & (flag.shift(1) == 1.0) & (flag.shift(2) == 1.0)).astype(float)


def pbs_ext_043_panic_then_reversal_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: yesterday was a wide-range bear bar AND today close > yesterday close.
    Classic panic-bar-then-reversal pair — a potential capitulation bottom signal."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    was_panic = ((rng.shift(1) > 2.0 * avg.shift(1)) & (close.shift(1) < open.shift(1)))
    reversal = close > close.shift(1)
    return (was_panic & reversal).astype(float)


def pbs_ext_044_panic_reversal_magnitude(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """On panic-then-reversal days: magnitude of reversal = (close - prior_close) / prior_close.
    Captures the strength of the recovery after a panic bar."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    was_panic = ((rng.shift(1) > 2.0 * avg.shift(1)) & (close.shift(1) < open.shift(1)))
    mag = (close - close.shift(1)) / close.shift(1).clip(lower=_EPS)
    return mag.where(was_panic, np.nan)


def pbs_ext_045_climax_then_up_bar_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: yesterday was a selling climax AND today close > open (bullish follow-through).
    Climax-reversal sequence — two-bar capitulation + recovery pattern."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    was_climax = ((rng.shift(1) > 2.0 * avg.shift(1))
                  & (volume.shift(1) > 2.0 * med_vol.shift(1))
                  & (close.shift(1) < open.shift(1)))
    return (was_climax & (close > open)).astype(float)


def pbs_ext_046_panic_bar_streak_count(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Running streak of consecutive panic bars (>2x avg range, close<open, clv<0.25)
    ending today; resets to 0 on any non-panic day."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float).fillna(0.0)
    streak = flag.copy()
    for i in range(1, len(flag)):
        if flag.iloc[i] == 1.0:
            streak.iloc[i] = streak.iloc[i - 1] + 1.0
        else:
            streak.iloc[i] = 0.0
    return streak


def pbs_ext_047_consec_down_close_bars_count(
    close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of consecutive sessions closing below prior close ending today
    (running down-close streak). Captures persistent selling momentum."""
    is_down = (close < close.shift(1)).astype(float).fillna(0.0)
    streak = is_down.copy()
    for i in range(1, len(is_down)):
        if is_down.iloc[i] == 1.0:
            streak.iloc[i] = streak.iloc[i - 1] + 1.0
        else:
            streak.iloc[i] = 0.0
    return streak


def pbs_ext_048_two_bar_range_expansion(
    close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Two-bar combined range ratio: (today_high - min(today_low, prior_low)) /
    avg_range_21d. Measures the breadth of panic over two bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    two_bar_high = high  # today's high
    two_bar_low = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    two_bar_rng = two_bar_high - two_bar_low
    return _safe_div(two_bar_rng, avg)


def pbs_ext_049_panic_bar_followed_by_hammer_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: yesterday was a panic bar AND today is a hammer (lt > 50% range).
    Hammer after panic bar — demand re-emerging at panic lows."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    was_panic = ((rng.shift(1) > 2.0 * avg.shift(1))
                 & (close.shift(1) < open.shift(1))
                 & (clv.shift(1) <= 0.25))
    lt = _lower_tail(open, close, low)
    lt_f = _safe_div(lt, rng.clip(lower=_EPS))
    is_hammer = lt_f > 0.50
    return (was_panic & is_hammer).astype(float)


def pbs_ext_050_wide_down_bar_count_10d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Count of wide-range bear bars (range>2x avg, close<open) in trailing 10 days.
    Mid-window between existing 5d (none) and 21d counts."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = ((rng > 2.0 * avg) & (close < open)).astype(float)
    return _rolling_sum(flag, 10)


# --- Group F (051-058): Bar-body location features ---

def pbs_ext_051_body_midpoint_location(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Body midpoint as fraction of bar range (0=bottom, 1=top of range).
    Low value = body buried at the low — distinct from CLV which uses close only."""
    return _body_midpoint_loc(open, close, high, low)


def pbs_ext_052_body_midpoint_near_low_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: body midpoint in bottom 30% of range (body buried near session low)."""
    bml = _body_midpoint_loc(open, close, high, low)
    return (bml <= 0.30).astype(float)


def pbs_ext_053_open_location_value(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Open price location within bar range: (open - low) / (high - low).
    Captures where the bar opened relative to its full range."""
    rng = _bar_range(high, low)
    return _safe_div(open - low, rng)


def pbs_ext_054_open_near_high_close_near_low_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: open in top 30% of range AND close in bottom 30% of range.
    Full-session sell-off: opened strong, closed weak — bears dominated entire day."""
    rng = _bar_range(high, low)
    olv = _safe_div(open - low, rng)
    clv = _close_loc(close, high, low)
    return ((olv >= 0.70) & (clv <= 0.30)).astype(float)


def pbs_ext_055_body_vs_lower_tail_location(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Body-bottom location (min(open,close) - low) / range: how far the body sits above the low.
    Low value = body hugging session low, distinct from lower_tail_ratio."""
    rng = _bar_range(high, low)
    body_bottom = pd.concat([open, close], axis=1).min(axis=1)
    return _safe_div(body_bottom - low, rng.clip(lower=_EPS))


def pbs_ext_056_body_near_low_wide_range_flag(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Flag: body bottom in lowest 20% of range AND range > 2x 21-day avg.
    Wide-range bar with body anchored to the low — panic pressure with little intraday bounce."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    body_bottom = pd.concat([open, close], axis=1).min(axis=1)
    body_bottom_loc = _safe_div(body_bottom - low, rng.clip(lower=_EPS))
    return ((body_bottom_loc <= 0.20) & (rng > 2.0 * avg)).astype(float)


def pbs_ext_057_body_midpoint_loc_21d_avg(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day rolling mean of body midpoint location.
    Persistent low values signal sustained downward body positioning."""
    bml = _body_midpoint_loc(open, close, high, low)
    return _rolling_mean(bml, _TD_MON)


def pbs_ext_058_body_midpoint_loc_pct_rank_252d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Percentile rank of body midpoint location in 252-day distribution.
    Low rank = body historically low within range — extreme downside positioning."""
    bml = _body_midpoint_loc(open, close, high, low)
    return bml.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (059-065): Effort-vs-result exhaustion (large volume + small body) ---

def pbs_ext_059_effort_vs_result_ratio(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Volume z-score divided by body/range ratio: high value = large effort (volume)
    for small result (body) — exhaustion / absorption signal."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS)).clip(lower=_EPS)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    return _safe_div(vol_z, bd_f)


def pbs_ext_060_effort_vs_result_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: volume > 2x 21d median AND body < 20% of range (high effort, low result).
    Exhaustion absorption bar: sellers trying but price not moving — supply being absorbed."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    return ((volume > 2.0 * med_vol) & (bd_f < 0.20)).astype(float)


def pbs_ext_061_effort_vs_result_bear_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: effort_vs_result conditions AND close < open (bearish effort absorption).
    Bears pushing with high volume but limited price gain downward."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    bd_f = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    return ((volume > 2.0 * med_vol) & (bd_f < 0.20) & (close < open)).astype(float)


def pbs_ext_062_effort_vs_result_count_21d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Count of effort-vs-result exhaustion bars (vol>2x median, body<20% range) in 21 days."""
    flag = pbs_ext_060_effort_vs_result_flag(close, high, low, open, volume)
    return _rolling_sum(flag, _TD_MON)


def pbs_ext_063_effort_vs_result_score_zscore_252d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of the effort-vs-result ratio in 252-day distribution."""
    evr = pbs_ext_059_effort_vs_result_ratio(close, high, low, open, volume)
    m = _rolling_mean(evr, _TD_YEAR)
    s = _rolling_std(evr, _TD_YEAR)
    return _safe_div(evr - m, s)


def pbs_ext_064_vol_over_body_zscore_252d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of volume / body_size ratio in 252-day distribution.
    Alternative effort-vs-result normalisation using raw body size as denominator."""
    body = _body(open, close).clip(lower=_EPS)
    vb = _safe_div(volume, body)
    m = _rolling_mean(vb, _TD_YEAR)
    s = _rolling_std(vb, _TD_YEAR)
    return _safe_div(vb - m, s)


def pbs_ext_065_effort_vs_result_pct_rank_252d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Percentile rank of effort-vs-result ratio in 252-day distribution."""
    evr = pbs_ext_059_effort_vs_result_ratio(close, high, low, open, volume)
    return evr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (066-070): Widest-bar-in-window and volume-spike bars ---

def pbs_ext_066_is_widest_bar_21d(
    close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: today's bar range equals the 21-day rolling maximum range.
    Marks the single widest bar in the trailing month."""
    rng = _bar_range(high, low)
    roll_max = _rolling_max(rng, _TD_MON)
    return (rng >= roll_max).astype(float)


def pbs_ext_067_is_widest_bar_63d(
    close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: today's bar range equals the 63-day rolling maximum range."""
    rng = _bar_range(high, low)
    roll_max = _rolling_max(rng, _TD_QTR)
    return (rng >= roll_max).astype(float)


def pbs_ext_068_volume_spike_flag_3x_median(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: volume > 3x 21-day median (extreme volume spike regardless of range).
    Pure volume-surge signal — no range condition, distinct from all existing features."""
    med_vol = _rolling_median(volume, _TD_MON)
    return (volume > 3.0 * med_vol).astype(float)


def pbs_ext_069_volume_spike_count_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Count of volume spike bars (>3x 21d median) in trailing 21 days."""
    flag = pbs_ext_068_volume_spike_flag_3x_median(close, volume)
    return _rolling_sum(flag, _TD_MON)


def pbs_ext_070_volume_spike_bear_bar_flag(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Flag: volume > 3x 21-day median AND close < open (extreme-volume bear bar).
    Pure volume-spike on a down day — not gated by range width."""
    med_vol = _rolling_median(volume, _TD_MON)
    return ((volume > 3.0 * med_vol) & (close < open)).astype(float)


# --- Group I (071-075): Intraday-reversal magnitude & RoC of panic intensity ---

def pbs_ext_071_intraday_reversal_from_low(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Intraday reversal magnitude from session low: (close - low) / avg_range_21d.
    On panic bars (range>2x avg), measures how far price rallied from session low.
    Absolute value normalized by average range."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    reversal = close - low
    norm = _safe_div(reversal, avg)
    return norm.where(rng > 2.0 * avg, np.nan)


def pbs_ext_072_intraday_reversal_from_low_pct_rank_252d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Percentile rank of intraday reversal from low (on panic bars) in 252-day distribution."""
    rev = pbs_ext_071_intraday_reversal_from_low(close, high, low, open)
    return rev.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_ext_073_panic_freq_roc_21d_to_63d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Rate of change: 21-day panic bar frequency divided by 63-day panic bar frequency.
    >1 = recent acceleration; <1 = recent deceleration in panic frequency."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq21 = _rolling_sum(flag, _TD_MON) / _TD_MON
    freq63 = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    return _safe_div(freq21, freq63.clip(lower=_EPS))


def pbs_ext_074_panic_intensity_roc_5d_to_21d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series
) -> pd.Series:
    """Rate of change: 5-day avg composite panic score vs 21-day avg composite score.
    >1 = short-term escalation relative to medium-term baseline."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    score = rng_z * (1.0 - clv.fillna(0.5)) * bear
    avg5 = _rolling_mean(score, _TD_WEEK)
    avg21 = _rolling_mean(score, _TD_MON)
    return _safe_div(avg5, avg21.clip(lower=_EPS))


def pbs_ext_075_climax_intensity_roc_5d_to_21d(
    close: pd.Series, high: pd.Series, low: pd.Series,
    open: pd.Series, volume: pd.Series
) -> pd.Series:
    """Rate of change: 5-day avg climax intensity vs 21-day avg climax intensity.
    >1 = short-term escalation in combined range+volume panic energy."""
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
    return _safe_div(avg5, avg21.clip(lower=_EPS))


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_EXTENDED_REGISTRY_001_075 = {
    "pbs_ext_001_bearish_marubozu_flag_70pct": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_001_bearish_marubozu_flag_70pct},
    "pbs_ext_002_bearish_marubozu_flag_95pct": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_002_bearish_marubozu_flag_95pct},
    "pbs_ext_003_bearish_marubozu_3x_vol_confirmed": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_003_bearish_marubozu_3x_vol_confirmed},
    "pbs_ext_004_bearish_marubozu_wide_3x_vol_confirmed": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_004_bearish_marubozu_wide_3x_vol_confirmed},
    "pbs_ext_005_bearish_marubozu_near_52wk_low_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_005_bearish_marubozu_near_52wk_low_flag},
    "pbs_ext_006_bearish_marubozu_streak": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_006_bearish_marubozu_streak},
    "pbs_ext_007_bullish_marubozu_flag_70pct": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_007_bullish_marubozu_flag_70pct},
    "pbs_ext_008_bearish_marubozu_count_5d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_008_bearish_marubozu_count_5d},
    "pbs_ext_009_marubozu_degree_ewm_5d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_009_marubozu_degree_ewm_5d},
    "pbs_ext_010_bearish_marubozu_vol_score": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_010_bearish_marubozu_vol_score},
    "pbs_ext_011_selling_climax_3x_range_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_011_selling_climax_3x_range_flag},
    "pbs_ext_012_selling_climax_3x_vol_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_012_selling_climax_3x_vol_flag},
    "pbs_ext_013_climax_bar_near_low_vol_confirmed": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_013_climax_bar_near_low_vol_confirmed},
    "pbs_ext_014_climax_count_5d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_014_climax_count_5d},
    "pbs_ext_015_climax_vol_fraction_63d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_015_climax_vol_fraction_63d},
    "pbs_ext_016_climax_intensity_score_bear_only": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_016_climax_intensity_score_bear_only},
    "pbs_ext_017_climax_intensity_zscore_252d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_017_climax_intensity_zscore_252d},
    "pbs_ext_018_selling_climax_recency_decay_5d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_018_selling_climax_recency_decay_5d},
    "pbs_ext_019_selling_climax_recency_decay_21d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_019_selling_climax_recency_decay_21d},
    "pbs_ext_020_range_vol_zscore_product": {
        "inputs": ["close", "high", "low", "volume"], "func": pbs_ext_020_range_vol_zscore_product},
    "pbs_ext_021_pin_bar_hammer_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_021_pin_bar_hammer_flag},
    "pbs_ext_022_shooting_star_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_022_shooting_star_flag},
    "pbs_ext_023_hammer_vs_shooting_star_asymmetry": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_023_hammer_vs_shooting_star_asymmetry},
    "pbs_ext_024_pin_bar_hammer_wide_range_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_024_pin_bar_hammer_wide_range_flag},
    "pbs_ext_025_pin_bar_vol_confirmed_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_025_pin_bar_vol_confirmed_flag},
    "pbs_ext_026_lower_tail_gt3x_body_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_026_lower_tail_gt3x_body_flag},
    "pbs_ext_027_upper_tail_gt3x_body_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_027_upper_tail_gt3x_body_flag},
    "pbs_ext_028_lower_tail_count_21d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_028_lower_tail_count_21d},
    "pbs_ext_029_lower_tail_pct_rank_63d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_029_lower_tail_pct_rank_63d},
    "pbs_ext_030_lower_tail_zscore_63d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_030_lower_tail_zscore_63d},
    "pbs_ext_031_gap_down_magnitude_pct": {
        "inputs": ["close", "open"], "func": pbs_ext_031_gap_down_magnitude_pct},
    "pbs_ext_032_gap_down_wide_range_score": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_032_gap_down_wide_range_score},
    "pbs_ext_033_gap_down_3pct_wide_range_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_033_gap_down_3pct_wide_range_flag},
    "pbs_ext_034_gap_down_close_below_gap_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_034_gap_down_close_below_gap_flag},
    "pbs_ext_035_gap_fill_pct_on_gap_day": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_035_gap_fill_pct_on_gap_day},
    "pbs_ext_036_gap_down_vol_spike_flag": {
        "inputs": ["close", "open", "volume"], "func": pbs_ext_036_gap_down_vol_spike_flag},
    "pbs_ext_037_gap_down_count_21d": {
        "inputs": ["close", "open"], "func": pbs_ext_037_gap_down_count_21d},
    "pbs_ext_038_gap_down_count_63d": {
        "inputs": ["close", "open"], "func": pbs_ext_038_gap_down_count_63d},
    "pbs_ext_039_gap_down_marubozu_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_039_gap_down_marubozu_flag},
    "pbs_ext_040_gap_down_total_loss_pct": {
        "inputs": ["close", "open"], "func": pbs_ext_040_gap_down_total_loss_pct},
    "pbs_ext_041_consec_wide_down_bars_2": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_041_consec_wide_down_bars_2},
    "pbs_ext_042_consec_wide_down_bars_3": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_042_consec_wide_down_bars_3},
    "pbs_ext_043_panic_then_reversal_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_043_panic_then_reversal_flag},
    "pbs_ext_044_panic_reversal_magnitude": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_044_panic_reversal_magnitude},
    "pbs_ext_045_climax_then_up_bar_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_045_climax_then_up_bar_flag},
    "pbs_ext_046_panic_bar_streak_count": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_046_panic_bar_streak_count},
    "pbs_ext_047_consec_down_close_bars_count": {
        "inputs": ["close", "high", "low"], "func": pbs_ext_047_consec_down_close_bars_count},
    "pbs_ext_048_two_bar_range_expansion": {
        "inputs": ["close", "high", "low"], "func": pbs_ext_048_two_bar_range_expansion},
    "pbs_ext_049_panic_bar_followed_by_hammer_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_049_panic_bar_followed_by_hammer_flag},
    "pbs_ext_050_wide_down_bar_count_10d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_050_wide_down_bar_count_10d},
    "pbs_ext_051_body_midpoint_location": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_051_body_midpoint_location},
    "pbs_ext_052_body_midpoint_near_low_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_052_body_midpoint_near_low_flag},
    "pbs_ext_053_open_location_value": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_053_open_location_value},
    "pbs_ext_054_open_near_high_close_near_low_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_054_open_near_high_close_near_low_flag},
    "pbs_ext_055_body_vs_lower_tail_location": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_055_body_vs_lower_tail_location},
    "pbs_ext_056_body_near_low_wide_range_flag": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_056_body_near_low_wide_range_flag},
    "pbs_ext_057_body_midpoint_loc_21d_avg": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_057_body_midpoint_loc_21d_avg},
    "pbs_ext_058_body_midpoint_loc_pct_rank_252d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_058_body_midpoint_loc_pct_rank_252d},
    "pbs_ext_059_effort_vs_result_ratio": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_059_effort_vs_result_ratio},
    "pbs_ext_060_effort_vs_result_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_060_effort_vs_result_flag},
    "pbs_ext_061_effort_vs_result_bear_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_061_effort_vs_result_bear_flag},
    "pbs_ext_062_effort_vs_result_count_21d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_062_effort_vs_result_count_21d},
    "pbs_ext_063_effort_vs_result_score_zscore_252d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_063_effort_vs_result_score_zscore_252d},
    "pbs_ext_064_vol_over_body_zscore_252d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_064_vol_over_body_zscore_252d},
    "pbs_ext_065_effort_vs_result_pct_rank_252d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_065_effort_vs_result_pct_rank_252d},
    "pbs_ext_066_is_widest_bar_21d": {
        "inputs": ["close", "high", "low"], "func": pbs_ext_066_is_widest_bar_21d},
    "pbs_ext_067_is_widest_bar_63d": {
        "inputs": ["close", "high", "low"], "func": pbs_ext_067_is_widest_bar_63d},
    "pbs_ext_068_volume_spike_flag_3x_median": {
        "inputs": ["close", "volume"], "func": pbs_ext_068_volume_spike_flag_3x_median},
    "pbs_ext_069_volume_spike_count_21d": {
        "inputs": ["close", "volume"], "func": pbs_ext_069_volume_spike_count_21d},
    "pbs_ext_070_volume_spike_bear_bar_flag": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_070_volume_spike_bear_bar_flag},
    "pbs_ext_071_intraday_reversal_from_low": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_071_intraday_reversal_from_low},
    "pbs_ext_072_intraday_reversal_from_low_pct_rank_252d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_072_intraday_reversal_from_low_pct_rank_252d},
    "pbs_ext_073_panic_freq_roc_21d_to_63d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_073_panic_freq_roc_21d_to_63d},
    "pbs_ext_074_panic_intensity_roc_5d_to_21d": {
        "inputs": ["close", "high", "low", "open"], "func": pbs_ext_074_panic_intensity_roc_5d_to_21d},
    "pbs_ext_075_climax_intensity_roc_5d_to_21d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": pbs_ext_075_climax_intensity_roc_5d_to_21d},
}
