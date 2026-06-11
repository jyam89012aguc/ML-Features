"""
78_marketcap_destruction — Extended Features 001-075
Domain: market-capitalization destruction — additional drawdown depth/duration variants,
        rebound-from-trough metrics, acceleration-free velocity composites, EV-destruction
        angles, persistence/streak counts, and cross-window compression ratios.
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield.
        These are native daily-frequency series — no quarterly forward-fill alignment needed.
All features are strictly backward-looking; no forward information is used.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_EPS     = 1e-9

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Additional drawdown windows and quantile-depth variants ---

def mcd_ext_001_mc_dd_from_42d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 42-day rolling peak (two-month drawdown fraction)."""
    pk = _rolling_max(marketcap, 42)
    return _safe_div(marketcap - pk, pk)


def mcd_ext_002_mc_dd_from_189d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 189-day rolling peak (three-quarter drawdown fraction)."""
    pk = _rolling_max(marketcap, 189)
    return _safe_div(marketcap - pk, pk)


def mcd_ext_003_mc_dd_from_378d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 378-day rolling peak (1.5-year drawdown fraction)."""
    pk = _rolling_max(marketcap, 378)
    return _safe_div(marketcap - pk, pk)


def mcd_ext_004_mc_dd_from_1008d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 1008-day rolling peak (4-year drawdown fraction)."""
    pk = _rolling_max(marketcap, 1008)
    return _safe_div(marketcap - pk, pk)


def mcd_ext_005_mc_dd_from_10d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 10-day rolling peak (bi-weekly drawdown fraction)."""
    pk = _rolling_max(marketcap, 10)
    return _safe_div(marketcap - pk, pk)


def mcd_ext_006_mc_dd_vs_252d_median(marketcap: pd.Series) -> pd.Series:
    """Marketcap fractional deviation below its 252-day rolling median."""
    med = _rolling_median(marketcap, _TD_YEAR)
    return _safe_div(marketcap - med, med)


def mcd_ext_007_mc_dd_from_q90_252d(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation below the 252-day 90th-percentile level (robust peak proxy)."""
    q = marketcap.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _safe_div(marketcap - q, q)


def mcd_ext_008_mc_dd_from_q90_504d(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation below the 504-day 90th-percentile level."""
    q = marketcap.rolling(_TD_2Y, min_periods=_TD_HALF).quantile(0.90)
    return _safe_div(marketcap - q, q)


def mcd_ext_009_mc_log_dd_from_42d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 42-day peak."""
    pk = _rolling_max(marketcap, 42)
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_ext_010_mc_log_dd_from_1260d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 1260-day (5-year) peak."""
    pk = _rolling_max(marketcap, _TD_5Y)
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_ext_011_mc_dd_squared_252d(marketcap: pd.Series) -> pd.Series:
    """Squared 252-day drawdown magnitude (convex emphasis on deep destruction)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(pk - marketcap, pk)
    return dd.clip(lower=0.0) ** 2


def mcd_ext_012_mc_dd_252d_severe_flag(marketcap: pd.Series) -> pd.Series:
    """Binary flag: marketcap is more than 50% below its 252-day peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return (dd < -0.50).astype(float)


# --- Group B (013-024): Drawdown duration, time-in-drawdown, time-since-peak ---

def mcd_ext_013_days_since_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Days elapsed since marketcap last equalled its 252-day rolling peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    at_peak = (marketcap >= pk - _EPS)
    idx = pd.Series(np.arange(len(marketcap), dtype=float), index=marketcap.index)
    last = idx.where(at_peak).ffill()
    return idx - last


def mcd_ext_014_days_since_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Days elapsed since marketcap last equalled its 504-day rolling peak."""
    pk = _rolling_max(marketcap, _TD_2Y)
    at_peak = (marketcap >= pk - _EPS)
    idx = pd.Series(np.arange(len(marketcap), dtype=float), index=marketcap.index)
    last = idx.where(at_peak).ffill()
    return idx - last


def mcd_ext_015_days_since_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Days elapsed since marketcap last equalled its expanding all-time peak."""
    pk = marketcap.expanding(min_periods=1).max()
    at_peak = (marketcap >= pk - _EPS)
    idx = pd.Series(np.arange(len(marketcap), dtype=float), index=marketcap.index)
    last = idx.where(at_peak).ffill()
    return idx - last


def mcd_ext_016_days_since_252d_trough(marketcap: pd.Series) -> pd.Series:
    """Days elapsed since marketcap last equalled its 252-day rolling trough."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    at_low = (marketcap <= lo + _EPS)
    idx = pd.Series(np.arange(len(marketcap), dtype=float), index=marketcap.index)
    last = idx.where(at_low).ffill()
    return idx - last


def mcd_ext_017_time_in_dd_fraction_252d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 252 days marketcap sat below its expanding peak (in drawdown)."""
    pk = marketcap.expanding(min_periods=1).max()
    in_dd = (marketcap < pk - _EPS).astype(float)
    return _rolling_mean(in_dd, _TD_YEAR)


def mcd_ext_018_time_in_dd_fraction_63d(marketcap: pd.Series) -> pd.Series:
    """Fraction of last 63 days marketcap sat below its expanding peak."""
    pk = marketcap.expanding(min_periods=1).max()
    in_dd = (marketcap < pk - _EPS).astype(float)
    return _rolling_mean(in_dd, _TD_QTR)


def mcd_ext_019_consec_days_below_sma63(marketcap: pd.Series) -> pd.Series:
    """Consecutive days marketcap has closed below its 63-day SMA."""
    ma = _rolling_mean(marketcap, _TD_QTR)
    return _consec_streak(marketcap < ma)


def mcd_ext_020_consec_days_below_sma252(marketcap: pd.Series) -> pd.Series:
    """Consecutive days marketcap has closed below its 252-day SMA."""
    ma = _rolling_mean(marketcap, _TD_YEAR)
    return _consec_streak(marketcap < ma)


def mcd_ext_021_consec_days_in_dd_over_20pct(marketcap: pd.Series) -> pd.Series:
    """Consecutive days marketcap stayed more than 20% below its 252-day peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _consec_streak(dd < -0.20)


def mcd_ext_022_max_consec_below_sma63_in_252d(marketcap: pd.Series) -> pd.Series:
    """Longest run of consecutive days below the 63-day SMA within the trailing year."""
    ma = _rolling_mean(marketcap, _TD_QTR)
    streak = _consec_streak(marketcap < ma)
    return _rolling_max(streak, _TD_YEAR)


def mcd_ext_023_days_since_dd_under_10pct(marketcap: pd.Series) -> pd.Series:
    """Days since marketcap was last within 10% of its 252-day peak (health recency)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    healthy = (dd > -0.10)
    idx = pd.Series(np.arange(len(marketcap), dtype=float), index=marketcap.index)
    last = idx.where(healthy).ffill()
    return idx - last


def mcd_ext_024_dd_252d_duration_weighted(marketcap: pd.Series) -> pd.Series:
    """Current 252-day drawdown depth scaled by fraction of last 63d spent in drawdown."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    in_dd = (marketcap < pk - _EPS).astype(float)
    return dd * _rolling_mean(in_dd, _TD_QTR)


# --- Group C (025-036): Rebound-from-trough and trough-proximity metrics ---

def mcd_ext_025_mc_pct_above_42d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 42-day marketcap low (two-month trough distance)."""
    lo = _rolling_min(marketcap, 42)
    return _safe_div(marketcap - lo, lo)


def mcd_ext_026_mc_pct_above_756d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 756-day (3-year) marketcap low."""
    lo = _rolling_min(marketcap, _TD_3Y)
    return _safe_div(marketcap - lo, lo)


def mcd_ext_027_mc_log_above_252d_low(marketcap: pd.Series) -> pd.Series:
    """Log distance of marketcap above its 252-day rolling trough."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return _log_safe(marketcap) - _log_safe(lo)


def mcd_ext_028_mc_at_252d_low_flag(marketcap: pd.Series) -> pd.Series:
    """Binary flag: marketcap equals its trailing 252-day low (fresh annual low)."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return (marketcap <= lo + _EPS).astype(float)


def mcd_ext_029_mc_at_all_time_low_flag(marketcap: pd.Series) -> pd.Series:
    """Binary flag: marketcap equals its expanding all-time low."""
    lo = marketcap.expanding(min_periods=1).min()
    return (marketcap <= lo + _EPS).astype(float)


def mcd_ext_030_mc_new_252d_low_count_63d(marketcap: pd.Series) -> pd.Series:
    """Count of fresh 252-day lows printed within the trailing 63 days."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    fresh = (marketcap <= lo + _EPS).astype(float)
    return _rolling_sum(fresh, _TD_QTR)


def mcd_ext_031_mc_new_252d_low_count_21d(marketcap: pd.Series) -> pd.Series:
    """Count of fresh 252-day lows printed within the trailing 21 days."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    fresh = (marketcap <= lo + _EPS).astype(float)
    return _rolling_sum(fresh, _TD_MON)


def mcd_ext_032_mc_rebound_from_63d_low(marketcap: pd.Series) -> pd.Series:
    """Marketcap rebound: percent gain over the trailing 63-day rolling low."""
    lo = _rolling_min(marketcap, _TD_QTR)
    return _safe_div(marketcap - lo, lo)


def mcd_ext_033_mc_position_in_63d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 63-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(marketcap, _TD_QTR)
    lo = _rolling_min(marketcap, _TD_QTR)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_ext_034_mc_position_in_756d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 756-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(marketcap, _TD_3Y)
    lo = _rolling_min(marketcap, _TD_3Y)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_ext_035_mc_position_in_all_time_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within expanding all-time high-low range."""
    hi = marketcap.expanding(min_periods=1).max()
    lo = marketcap.expanding(min_periods=1).min()
    return _safe_div(marketcap - lo, hi - lo)


def mcd_ext_036_mc_near_252d_low_flag(marketcap: pd.Series) -> pd.Series:
    """Binary flag: marketcap within 5% of its trailing 252-day low."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return (_safe_div(marketcap - lo, lo) < 0.05).astype(float)


# --- Group D (037-048): Velocity variants — additional horizons and smoothing ---

def mcd_ext_037_mc_10d_pct_change(marketcap: pd.Series) -> pd.Series:
    """10-day percent change in marketcap (bi-weekly destruction velocity)."""
    return marketcap.pct_change(10)


def mcd_ext_038_mc_42d_pct_change(marketcap: pd.Series) -> pd.Series:
    """42-day percent change in marketcap (two-month destruction velocity)."""
    return marketcap.pct_change(42)


def mcd_ext_039_mc_189d_pct_change(marketcap: pd.Series) -> pd.Series:
    """189-day percent change in marketcap (three-quarter destruction velocity)."""
    return marketcap.pct_change(189)


def mcd_ext_040_mc_504d_pct_change(marketcap: pd.Series) -> pd.Series:
    """504-day percent change in marketcap (two-year total destruction)."""
    return marketcap.pct_change(_TD_2Y)


def mcd_ext_041_mc_42d_log_change(marketcap: pd.Series) -> pd.Series:
    """42-day log change in marketcap (two-month log-velocity)."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(42))


def mcd_ext_042_mc_504d_log_change(marketcap: pd.Series) -> pd.Series:
    """504-day log change in marketcap (two-year log-velocity)."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_2Y))


def mcd_ext_043_mc_smoothed_21d_velocity(marketcap: pd.Series) -> pd.Series:
    """5-day-EWM-smoothed 21-day percent change in marketcap (de-noised velocity)."""
    return _ewm_mean(marketcap.pct_change(_TD_MON), _TD_WEEK)


def mcd_ext_044_mc_velocity_zscore_252d(marketcap: pd.Series) -> pd.Series:
    """Z-score of 21-day marketcap pct change over its trailing 252-day distribution."""
    return _zscore_rolling(marketcap.pct_change(_TD_MON), _TD_YEAR)


def mcd_ext_045_mc_63d_change_pct_rank_504d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of 63-day marketcap pct change within trailing 504-day window."""
    return _rolling_rank_pct(marketcap.pct_change(_TD_QTR), _TD_2Y)


def mcd_ext_046_mc_drop_speed_ratio(marketcap: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day pct change (recent vs annual pace of destruction)."""
    return _safe_div(marketcap.pct_change(_TD_MON), marketcap.pct_change(_TD_YEAR))


def mcd_ext_047_mc_neg_velocity_streak(marketcap: pd.Series) -> pd.Series:
    """Consecutive days the 21-day marketcap pct change has stayed negative."""
    return _consec_streak(marketcap.pct_change(_TD_MON) < 0)


def mcd_ext_048_mc_velocity_below_neg10pct_flag(marketcap: pd.Series) -> pd.Series:
    """Binary flag: 21-day marketcap pct change below -10% (acute monthly destruction)."""
    return (marketcap.pct_change(_TD_MON) < -0.10).astype(float)


# --- Group E (049-058): Worst-drop and damage-accumulation variants ---

def mcd_ext_049_mc_worst_10d_drop_in_126d(marketcap: pd.Series) -> pd.Series:
    """Worst single 10-day pct drop in marketcap within trailing 126-day window."""
    return marketcap.pct_change(10).rolling(_TD_HALF, min_periods=_TD_QTR).min()


def mcd_ext_050_mc_worst_42d_drop_in_504d(marketcap: pd.Series) -> pd.Series:
    """Worst single 42-day pct drop in marketcap within trailing 504-day window."""
    return marketcap.pct_change(42).rolling(_TD_2Y, min_periods=_TD_HALF).min()


def mcd_ext_051_mc_worst_5d_drop_in_21d(marketcap: pd.Series) -> pd.Series:
    """Worst single 5-day pct drop in marketcap within trailing 21-day window."""
    return marketcap.pct_change(5).rolling(_TD_MON, min_periods=10).min()


def mcd_ext_052_mc_worst_1d_drop_expanding(marketcap: pd.Series) -> pd.Series:
    """All-time worst single daily pct drop in marketcap (expanding window)."""
    return marketcap.pct_change(1).expanding(min_periods=5).min()


def mcd_ext_053_mc_sum_neg_1d_in_21d(marketcap: pd.Series) -> pd.Series:
    """Sum of daily negative pct changes in marketcap over 21-day window."""
    chg = marketcap.pct_change(1)
    return _rolling_sum(chg.where(chg < 0, 0.0), _TD_MON)


def mcd_ext_054_mc_sum_neg_1d_in_126d(marketcap: pd.Series) -> pd.Series:
    """Sum of daily negative pct changes in marketcap over 126-day window."""
    chg = marketcap.pct_change(1)
    return _rolling_sum(chg.where(chg < 0, 0.0), _TD_HALF)


def mcd_ext_055_mc_count_big_down_days_63d(marketcap: pd.Series) -> pd.Series:
    """Count of days in last 63d with marketcap daily drop worse than -3%."""
    chg = marketcap.pct_change(1)
    return _rolling_sum((chg < -0.03).astype(float), _TD_QTR)


def mcd_ext_056_mc_count_big_down_days_252d(marketcap: pd.Series) -> pd.Series:
    """Count of days in last 252d with marketcap daily drop worse than -5%."""
    chg = marketcap.pct_change(1)
    return _rolling_sum((chg < -0.05).astype(float), _TD_YEAR)


def mcd_ext_057_mc_downside_capture_63d(marketcap: pd.Series) -> pd.Series:
    """Ratio of summed negative daily moves to summed absolute daily moves over 63d."""
    chg = marketcap.pct_change(1)
    neg = _rolling_sum(chg.where(chg < 0, 0.0).abs(), _TD_QTR)
    tot = _rolling_sum(chg.abs(), _TD_QTR)
    return _safe_div(neg, tot)


def mcd_ext_058_mc_avg_abs_drop_63d(marketcap: pd.Series) -> pd.Series:
    """Average magnitude of negative daily pct changes in marketcap over 63d."""
    chg = marketcap.pct_change(1)
    neg = chg.where(chg < 0)
    return neg.abs().rolling(_TD_QTR, min_periods=_TD_MON).mean()


# --- Group F (059-066): Distributional and volatility-of-destruction variants ---

def mcd_ext_059_mc_return_vol_63d(marketcap: pd.Series) -> pd.Series:
    """63-day rolling std of daily marketcap pct changes (destruction volatility)."""
    return _rolling_std(marketcap.pct_change(1), _TD_QTR)


def mcd_ext_060_mc_return_vol_252d(marketcap: pd.Series) -> pd.Series:
    """252-day rolling std of daily marketcap pct changes (annual destruction volatility)."""
    return _rolling_std(marketcap.pct_change(1), _TD_YEAR)


def mcd_ext_061_mc_return_skew_252d(marketcap: pd.Series) -> pd.Series:
    """252-day rolling skewness of daily marketcap pct changes (crash asymmetry)."""
    return marketcap.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def mcd_ext_062_mc_return_downside_vol_126d(marketcap: pd.Series) -> pd.Series:
    """126-day rolling std of only the negative daily marketcap pct changes."""
    chg = marketcap.pct_change(1)
    return chg.where(chg < 0).rolling(_TD_HALF, min_periods=_TD_MON).std()


def mcd_ext_063_mc_dd_252d_vol_scaled(marketcap: pd.Series) -> pd.Series:
    """252-day drawdown depth divided by 63-day return volatility (vol-adjusted distress)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), _TD_QTR)
    return _safe_div(dd, vol)


def mcd_ext_064_mc_velocity_vol_scaled_63d(marketcap: pd.Series) -> pd.Series:
    """63-day marketcap pct change divided by 63-day return volatility."""
    vol = _rolling_std(marketcap.pct_change(1), _TD_QTR)
    return _safe_div(marketcap.pct_change(_TD_QTR), vol)


def mcd_ext_065_mc_vol_regime_ratio(marketcap: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day return volatility (volatility-spike regime)."""
    v_short = _rolling_std(marketcap.pct_change(1), _TD_MON)
    v_long  = _rolling_std(marketcap.pct_change(1), _TD_YEAR)
    return _safe_div(v_short, v_long)


def mcd_ext_066_mc_return_q05_252d(marketcap: pd.Series) -> pd.Series:
    """252-day 5th-percentile of daily marketcap pct changes (left-tail crash depth)."""
    return marketcap.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


# --- Group G (067-075): EV-destruction angles, cross-field and composites ---

def mcd_ext_067_ev_dd_from_504d_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value vs 504-day rolling peak (two-year EV destruction fraction)."""
    pk = _rolling_max(ev, _TD_2Y)
    return _safe_div(ev - pk, pk)


def mcd_ext_068_ev_log_dd_from_252d_peak(ev: pd.Series) -> pd.Series:
    """Log-space EV drawdown from its 252-day peak."""
    pk = _rolling_max(ev, _TD_YEAR)
    return _log_safe(ev) - _log_safe(pk)


def mcd_ext_069_ev_zscore_252d(ev: pd.Series) -> pd.Series:
    """Z-score of enterprise value relative to trailing 252-day distribution."""
    return _zscore_rolling(ev, _TD_YEAR)


def mcd_ext_070_ev_pct_rank_504d(ev: pd.Series) -> pd.Series:
    """Percentile rank of enterprise value within trailing 504-day window."""
    return _rolling_rank_pct(ev, _TD_2Y)


def mcd_ext_071_ev_consec_down_days(ev: pd.Series) -> pd.Series:
    """Consecutive days with enterprise value declining from the prior day."""
    return _consec_streak(ev.diff(1) < 0)


def mcd_ext_072_mc_minus_ev_dd_252d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Marketcap 252-day drawdown minus EV 252-day drawdown (equity-vs-enterprise gap)."""
    mc_pk = _rolling_max(marketcap, _TD_YEAR)
    ev_pk = _rolling_max(ev, _TD_YEAR)
    return _safe_div(marketcap - mc_pk, mc_pk) - _safe_div(ev - ev_pk, ev_pk)


def mcd_ext_073_mc_ev_destruction_ratio_252d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Ratio of marketcap 252-day pct change to EV 252-day pct change."""
    return _safe_div(marketcap.pct_change(_TD_YEAR), ev.pct_change(_TD_YEAR))


def mcd_ext_074_mc_destruction_breadth_score(marketcap: pd.Series) -> pd.Series:
    """Count (0-4) of marketcap drawdowns from 21/63/126/252-day peaks each beyond -20%."""
    flags = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR):
        pk = _rolling_max(marketcap, w)
        flags.append((_safe_div(marketcap - pk, pk) < -0.20).astype(float))
    total = flags[0]
    for f in flags[1:]:
        total = total + f
    return total


def mcd_ext_075_mc_capitulation_composite(marketcap: pd.Series) -> pd.Series:
    """Composite distress: 252d drawdown depth + (1 - 252d pct-rank) + |252d z-score|/3 clipped."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    depth = _safe_div(pk - marketcap, pk).clip(lower=0.0)
    rank = _rolling_rank_pct(marketcap, _TD_YEAR)
    z = _zscore_rolling(marketcap, _TD_YEAR).abs().clip(upper=3.0) / 3.0
    return depth + (1.0 - rank.fillna(0.5)) + z


# ── Registry ───────────────────────────────────────────────────────────────────

MARKETCAP_DESTRUCTION_EXTENDED_REGISTRY_001_075 = {
    "mcd_ext_001_mc_dd_from_42d_peak":          {"inputs": ["marketcap"], "func": mcd_ext_001_mc_dd_from_42d_peak},
    "mcd_ext_002_mc_dd_from_189d_peak":         {"inputs": ["marketcap"], "func": mcd_ext_002_mc_dd_from_189d_peak},
    "mcd_ext_003_mc_dd_from_378d_peak":         {"inputs": ["marketcap"], "func": mcd_ext_003_mc_dd_from_378d_peak},
    "mcd_ext_004_mc_dd_from_1008d_peak":        {"inputs": ["marketcap"], "func": mcd_ext_004_mc_dd_from_1008d_peak},
    "mcd_ext_005_mc_dd_from_10d_peak":          {"inputs": ["marketcap"], "func": mcd_ext_005_mc_dd_from_10d_peak},
    "mcd_ext_006_mc_dd_vs_252d_median":         {"inputs": ["marketcap"], "func": mcd_ext_006_mc_dd_vs_252d_median},
    "mcd_ext_007_mc_dd_from_q90_252d":          {"inputs": ["marketcap"], "func": mcd_ext_007_mc_dd_from_q90_252d},
    "mcd_ext_008_mc_dd_from_q90_504d":          {"inputs": ["marketcap"], "func": mcd_ext_008_mc_dd_from_q90_504d},
    "mcd_ext_009_mc_log_dd_from_42d_peak":      {"inputs": ["marketcap"], "func": mcd_ext_009_mc_log_dd_from_42d_peak},
    "mcd_ext_010_mc_log_dd_from_1260d_peak":    {"inputs": ["marketcap"], "func": mcd_ext_010_mc_log_dd_from_1260d_peak},
    "mcd_ext_011_mc_dd_squared_252d":           {"inputs": ["marketcap"], "func": mcd_ext_011_mc_dd_squared_252d},
    "mcd_ext_012_mc_dd_252d_severe_flag":       {"inputs": ["marketcap"], "func": mcd_ext_012_mc_dd_252d_severe_flag},
    "mcd_ext_013_days_since_252d_peak":         {"inputs": ["marketcap"], "func": mcd_ext_013_days_since_252d_peak},
    "mcd_ext_014_days_since_504d_peak":         {"inputs": ["marketcap"], "func": mcd_ext_014_days_since_504d_peak},
    "mcd_ext_015_days_since_all_time_peak":     {"inputs": ["marketcap"], "func": mcd_ext_015_days_since_all_time_peak},
    "mcd_ext_016_days_since_252d_trough":       {"inputs": ["marketcap"], "func": mcd_ext_016_days_since_252d_trough},
    "mcd_ext_017_time_in_dd_fraction_252d":     {"inputs": ["marketcap"], "func": mcd_ext_017_time_in_dd_fraction_252d},
    "mcd_ext_018_time_in_dd_fraction_63d":      {"inputs": ["marketcap"], "func": mcd_ext_018_time_in_dd_fraction_63d},
    "mcd_ext_019_consec_days_below_sma63":      {"inputs": ["marketcap"], "func": mcd_ext_019_consec_days_below_sma63},
    "mcd_ext_020_consec_days_below_sma252":     {"inputs": ["marketcap"], "func": mcd_ext_020_consec_days_below_sma252},
    "mcd_ext_021_consec_days_in_dd_over_20pct": {"inputs": ["marketcap"], "func": mcd_ext_021_consec_days_in_dd_over_20pct},
    "mcd_ext_022_max_consec_below_sma63_in_252d": {"inputs": ["marketcap"], "func": mcd_ext_022_max_consec_below_sma63_in_252d},
    "mcd_ext_023_days_since_dd_under_10pct":    {"inputs": ["marketcap"], "func": mcd_ext_023_days_since_dd_under_10pct},
    "mcd_ext_024_dd_252d_duration_weighted":    {"inputs": ["marketcap"], "func": mcd_ext_024_dd_252d_duration_weighted},
    "mcd_ext_025_mc_pct_above_42d_low":         {"inputs": ["marketcap"], "func": mcd_ext_025_mc_pct_above_42d_low},
    "mcd_ext_026_mc_pct_above_756d_low":        {"inputs": ["marketcap"], "func": mcd_ext_026_mc_pct_above_756d_low},
    "mcd_ext_027_mc_log_above_252d_low":        {"inputs": ["marketcap"], "func": mcd_ext_027_mc_log_above_252d_low},
    "mcd_ext_028_mc_at_252d_low_flag":          {"inputs": ["marketcap"], "func": mcd_ext_028_mc_at_252d_low_flag},
    "mcd_ext_029_mc_at_all_time_low_flag":      {"inputs": ["marketcap"], "func": mcd_ext_029_mc_at_all_time_low_flag},
    "mcd_ext_030_mc_new_252d_low_count_63d":    {"inputs": ["marketcap"], "func": mcd_ext_030_mc_new_252d_low_count_63d},
    "mcd_ext_031_mc_new_252d_low_count_21d":    {"inputs": ["marketcap"], "func": mcd_ext_031_mc_new_252d_low_count_21d},
    "mcd_ext_032_mc_rebound_from_63d_low":      {"inputs": ["marketcap"], "func": mcd_ext_032_mc_rebound_from_63d_low},
    "mcd_ext_033_mc_position_in_63d_range":     {"inputs": ["marketcap"], "func": mcd_ext_033_mc_position_in_63d_range},
    "mcd_ext_034_mc_position_in_756d_range":    {"inputs": ["marketcap"], "func": mcd_ext_034_mc_position_in_756d_range},
    "mcd_ext_035_mc_position_in_all_time_range": {"inputs": ["marketcap"], "func": mcd_ext_035_mc_position_in_all_time_range},
    "mcd_ext_036_mc_near_252d_low_flag":        {"inputs": ["marketcap"], "func": mcd_ext_036_mc_near_252d_low_flag},
    "mcd_ext_037_mc_10d_pct_change":            {"inputs": ["marketcap"], "func": mcd_ext_037_mc_10d_pct_change},
    "mcd_ext_038_mc_42d_pct_change":            {"inputs": ["marketcap"], "func": mcd_ext_038_mc_42d_pct_change},
    "mcd_ext_039_mc_189d_pct_change":           {"inputs": ["marketcap"], "func": mcd_ext_039_mc_189d_pct_change},
    "mcd_ext_040_mc_504d_pct_change":           {"inputs": ["marketcap"], "func": mcd_ext_040_mc_504d_pct_change},
    "mcd_ext_041_mc_42d_log_change":            {"inputs": ["marketcap"], "func": mcd_ext_041_mc_42d_log_change},
    "mcd_ext_042_mc_504d_log_change":           {"inputs": ["marketcap"], "func": mcd_ext_042_mc_504d_log_change},
    "mcd_ext_043_mc_smoothed_21d_velocity":     {"inputs": ["marketcap"], "func": mcd_ext_043_mc_smoothed_21d_velocity},
    "mcd_ext_044_mc_velocity_zscore_252d":      {"inputs": ["marketcap"], "func": mcd_ext_044_mc_velocity_zscore_252d},
    "mcd_ext_045_mc_63d_change_pct_rank_504d":  {"inputs": ["marketcap"], "func": mcd_ext_045_mc_63d_change_pct_rank_504d},
    "mcd_ext_046_mc_drop_speed_ratio":          {"inputs": ["marketcap"], "func": mcd_ext_046_mc_drop_speed_ratio},
    "mcd_ext_047_mc_neg_velocity_streak":       {"inputs": ["marketcap"], "func": mcd_ext_047_mc_neg_velocity_streak},
    "mcd_ext_048_mc_velocity_below_neg10pct_flag": {"inputs": ["marketcap"], "func": mcd_ext_048_mc_velocity_below_neg10pct_flag},
    "mcd_ext_049_mc_worst_10d_drop_in_126d":    {"inputs": ["marketcap"], "func": mcd_ext_049_mc_worst_10d_drop_in_126d},
    "mcd_ext_050_mc_worst_42d_drop_in_504d":    {"inputs": ["marketcap"], "func": mcd_ext_050_mc_worst_42d_drop_in_504d},
    "mcd_ext_051_mc_worst_5d_drop_in_21d":      {"inputs": ["marketcap"], "func": mcd_ext_051_mc_worst_5d_drop_in_21d},
    "mcd_ext_052_mc_worst_1d_drop_expanding":   {"inputs": ["marketcap"], "func": mcd_ext_052_mc_worst_1d_drop_expanding},
    "mcd_ext_053_mc_sum_neg_1d_in_21d":         {"inputs": ["marketcap"], "func": mcd_ext_053_mc_sum_neg_1d_in_21d},
    "mcd_ext_054_mc_sum_neg_1d_in_126d":        {"inputs": ["marketcap"], "func": mcd_ext_054_mc_sum_neg_1d_in_126d},
    "mcd_ext_055_mc_count_big_down_days_63d":   {"inputs": ["marketcap"], "func": mcd_ext_055_mc_count_big_down_days_63d},
    "mcd_ext_056_mc_count_big_down_days_252d":  {"inputs": ["marketcap"], "func": mcd_ext_056_mc_count_big_down_days_252d},
    "mcd_ext_057_mc_downside_capture_63d":      {"inputs": ["marketcap"], "func": mcd_ext_057_mc_downside_capture_63d},
    "mcd_ext_058_mc_avg_abs_drop_63d":          {"inputs": ["marketcap"], "func": mcd_ext_058_mc_avg_abs_drop_63d},
    "mcd_ext_059_mc_return_vol_63d":            {"inputs": ["marketcap"], "func": mcd_ext_059_mc_return_vol_63d},
    "mcd_ext_060_mc_return_vol_252d":           {"inputs": ["marketcap"], "func": mcd_ext_060_mc_return_vol_252d},
    "mcd_ext_061_mc_return_skew_252d":          {"inputs": ["marketcap"], "func": mcd_ext_061_mc_return_skew_252d},
    "mcd_ext_062_mc_return_downside_vol_126d":  {"inputs": ["marketcap"], "func": mcd_ext_062_mc_return_downside_vol_126d},
    "mcd_ext_063_mc_dd_252d_vol_scaled":        {"inputs": ["marketcap"], "func": mcd_ext_063_mc_dd_252d_vol_scaled},
    "mcd_ext_064_mc_velocity_vol_scaled_63d":   {"inputs": ["marketcap"], "func": mcd_ext_064_mc_velocity_vol_scaled_63d},
    "mcd_ext_065_mc_vol_regime_ratio":          {"inputs": ["marketcap"], "func": mcd_ext_065_mc_vol_regime_ratio},
    "mcd_ext_066_mc_return_q05_252d":           {"inputs": ["marketcap"], "func": mcd_ext_066_mc_return_q05_252d},
    "mcd_ext_067_ev_dd_from_504d_peak":         {"inputs": ["ev"],        "func": mcd_ext_067_ev_dd_from_504d_peak},
    "mcd_ext_068_ev_log_dd_from_252d_peak":     {"inputs": ["ev"],        "func": mcd_ext_068_ev_log_dd_from_252d_peak},
    "mcd_ext_069_ev_zscore_252d":               {"inputs": ["ev"],        "func": mcd_ext_069_ev_zscore_252d},
    "mcd_ext_070_ev_pct_rank_504d":             {"inputs": ["ev"],        "func": mcd_ext_070_ev_pct_rank_504d},
    "mcd_ext_071_ev_consec_down_days":          {"inputs": ["ev"],        "func": mcd_ext_071_ev_consec_down_days},
    "mcd_ext_072_mc_minus_ev_dd_252d":          {"inputs": ["marketcap", "ev"], "func": mcd_ext_072_mc_minus_ev_dd_252d},
    "mcd_ext_073_mc_ev_destruction_ratio_252d": {"inputs": ["marketcap", "ev"], "func": mcd_ext_073_mc_ev_destruction_ratio_252d},
    "mcd_ext_074_mc_destruction_breadth_score": {"inputs": ["marketcap"], "func": mcd_ext_074_mc_destruction_breadth_score},
    "mcd_ext_075_mc_capitulation_composite":    {"inputs": ["marketcap"], "func": mcd_ext_075_mc_capitulation_composite},
}
