"""
78_marketcap_destruction — Base Features 001-075 (registry extended to 100)
Domain: market-capitalization destruction — magnitude and speed of market-cap decline
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
  NO raw price/volume or quarterly SF1 fundamental inputs.
All features are strictly backward-looking; no forward information is used.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

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


def _pct_change1(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Feature Functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Marketcap drawdown from trailing peaks, various windows ---

def mcd_001_mc_dd_from_21d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 21-day rolling peak (1-month drawdown fraction)."""
    pk = _rolling_max(marketcap, _TD_MON)
    return _safe_div(marketcap - pk, pk)


def mcd_002_mc_dd_from_63d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 63-day rolling peak (1-quarter drawdown fraction)."""
    pk = _rolling_max(marketcap, _TD_QTR)
    return _safe_div(marketcap - pk, pk)


def mcd_003_mc_dd_from_126d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 126-day rolling peak (half-year drawdown fraction)."""
    pk = _rolling_max(marketcap, _TD_HALF)
    return _safe_div(marketcap - pk, pk)


def mcd_004_mc_dd_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 252-day rolling peak (1-year drawdown fraction)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    return _safe_div(marketcap - pk, pk)


def mcd_005_mc_dd_from_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 504-day rolling peak (2-year drawdown fraction)."""
    pk = _rolling_max(marketcap, 504)
    return _safe_div(marketcap - pk, pk)


def mcd_006_mc_dd_from_756d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 756-day rolling peak (3-year drawdown fraction)."""
    pk = _rolling_max(marketcap, 756)
    return _safe_div(marketcap - pk, pk)


def mcd_007_mc_dd_from_1260d_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs 1260-day rolling peak (5-year drawdown fraction)."""
    pk = _rolling_max(marketcap, 1260)
    return _safe_div(marketcap - pk, pk)


def mcd_008_mc_dd_from_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Marketcap vs all-time expanding peak (all-time drawdown fraction)."""
    pk = marketcap.expanding(min_periods=1).max()
    return _safe_div(marketcap - pk, pk)


def mcd_009_mc_log_dd_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 252-day peak."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_010_mc_log_dd_from_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from all-time peak."""
    pk = marketcap.expanding(min_periods=1).max()
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_011_mc_log_dd_from_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 504-day peak."""
    pk = _rolling_max(marketcap, 504)
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_012_mc_log_dd_from_756d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 756-day peak."""
    pk = _rolling_max(marketcap, 756)
    return _log_safe(marketcap) - _log_safe(pk)


# --- Group B (013-022): Dollar / absolute value destroyed ---

def mcd_013_mc_dollar_loss_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Dollar value destroyed vs 252-day peak marketcap (raw $M difference)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    return marketcap - pk


def mcd_014_mc_dollar_loss_from_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Dollar value destroyed vs all-time peak marketcap."""
    pk = marketcap.expanding(min_periods=1).max()
    return marketcap - pk


def mcd_015_mc_dollar_loss_from_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Dollar value destroyed vs 504-day peak marketcap."""
    pk = _rolling_max(marketcap, 504)
    return marketcap - pk


def mcd_016_mc_log_dollar_loss_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Log of absolute dollar loss from 252-day peak (sign-preserving log magnitude)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    loss = pk - marketcap
    return _log_safe(loss.clip(lower=_EPS))


def mcd_017_mc_log_dollar_loss_from_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Log of absolute dollar loss from all-time peak."""
    pk = marketcap.expanding(min_periods=1).max()
    loss = pk - marketcap
    return _log_safe(loss.clip(lower=_EPS))


def mcd_018_mc_fraction_peak_remaining(marketcap: pd.Series) -> pd.Series:
    """Fraction of all-time peak marketcap still remaining (1 = at peak, <1 = destroyed)."""
    pk = marketcap.expanding(min_periods=1).max()
    return _safe_div(marketcap, pk)


def mcd_019_mc_fraction_252d_peak_remaining(marketcap: pd.Series) -> pd.Series:
    """Fraction of 252-day peak marketcap still remaining."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    return _safe_div(marketcap, pk)


def mcd_020_ev_dd_from_252d_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value vs 252-day rolling peak (EV destruction fraction)."""
    pk = _rolling_max(ev, _TD_YEAR)
    return _safe_div(ev - pk, pk)


def mcd_021_ev_dd_from_all_time_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value vs all-time expanding peak (all-time EV destruction)."""
    pk = ev.expanding(min_periods=1).max()
    return _safe_div(ev - pk, pk)


def mcd_022_ev_dollar_loss_from_252d_peak(ev: pd.Series) -> pd.Series:
    """Absolute EV destroyed vs 252-day peak (raw $M EV loss)."""
    pk = _rolling_max(ev, _TD_YEAR)
    return ev - pk


# --- Group C (023-033): Velocity — N-day speed of marketcap decline ---

def mcd_023_mc_5d_pct_change(marketcap: pd.Series) -> pd.Series:
    """5-day percent change in marketcap (1-week destruction velocity)."""
    return marketcap.pct_change(5)


def mcd_024_mc_21d_pct_change(marketcap: pd.Series) -> pd.Series:
    """21-day percent change in marketcap (1-month destruction velocity)."""
    return marketcap.pct_change(_TD_MON)


def mcd_025_mc_63d_pct_change(marketcap: pd.Series) -> pd.Series:
    """63-day percent change in marketcap (1-quarter destruction velocity)."""
    return marketcap.pct_change(_TD_QTR)


def mcd_026_mc_126d_pct_change(marketcap: pd.Series) -> pd.Series:
    """126-day percent change in marketcap (half-year destruction velocity)."""
    return marketcap.pct_change(_TD_HALF)


def mcd_027_mc_252d_pct_change(marketcap: pd.Series) -> pd.Series:
    """252-day percent change in marketcap (1-year total destruction)."""
    return marketcap.pct_change(_TD_YEAR)


def mcd_028_mc_5d_log_change(marketcap: pd.Series) -> pd.Series:
    """5-day log change in marketcap (log-velocity of destruction)."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(5))


def mcd_029_mc_21d_log_change(marketcap: pd.Series) -> pd.Series:
    """21-day log change in marketcap."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_MON))


def mcd_030_mc_63d_log_change(marketcap: pd.Series) -> pd.Series:
    """63-day log change in marketcap."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_QTR))


def mcd_031_mc_252d_log_change(marketcap: pd.Series) -> pd.Series:
    """252-day log change in marketcap."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_YEAR))


def mcd_032_ev_21d_pct_change(ev: pd.Series) -> pd.Series:
    """21-day percent change in enterprise value (EV destruction velocity)."""
    return ev.pct_change(_TD_MON)


def mcd_033_ev_63d_pct_change(ev: pd.Series) -> pd.Series:
    """63-day percent change in enterprise value."""
    return ev.pct_change(_TD_QTR)


# --- Group D (034-044): Fastest N-day / N-quarter marketcap drop (min over window) ---

def mcd_034_mc_worst_5d_drop_in_63d(marketcap: pd.Series) -> pd.Series:
    """Worst single 5-day pct drop in marketcap within trailing 63-day window."""
    chg = marketcap.pct_change(5)
    return chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()


def mcd_035_mc_worst_21d_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Worst single 21-day pct drop in marketcap within trailing 252-day window."""
    chg = marketcap.pct_change(_TD_MON)
    return chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def mcd_036_mc_worst_63d_drop_in_504d(marketcap: pd.Series) -> pd.Series:
    """Worst single 63-day pct drop in marketcap within trailing 504-day window."""
    chg = marketcap.pct_change(_TD_QTR)
    return chg.rolling(504, min_periods=252).min()


def mcd_037_mc_worst_1d_drop_in_21d(marketcap: pd.Series) -> pd.Series:
    """Worst single daily pct drop in marketcap within trailing 21-day window."""
    chg = marketcap.pct_change(1)
    return chg.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()


def mcd_038_mc_worst_1d_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Worst single daily pct drop in marketcap within trailing 252-day window."""
    chg = marketcap.pct_change(1)
    return chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def mcd_039_mc_worst_5d_drop_expanding(marketcap: pd.Series) -> pd.Series:
    """All-time worst single 5-day pct drop in marketcap (expanding window)."""
    chg = marketcap.pct_change(5)
    return chg.expanding(min_periods=5).min()


def mcd_040_mc_avg_1d_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Average of daily negative pct changes in marketcap over 252-day window."""
    chg = marketcap.pct_change(1)
    neg = chg.where(chg < 0, other=0.0)
    return _rolling_mean(neg, _TD_YEAR)


def mcd_041_mc_sum_neg_1d_in_63d(marketcap: pd.Series) -> pd.Series:
    """Sum of daily negative pct changes in marketcap over 63-day window (total damage)."""
    chg = marketcap.pct_change(1)
    neg = chg.where(chg < 0, other=0.0)
    return _rolling_sum(neg, _TD_QTR)


def mcd_042_ev_worst_21d_drop_in_252d(ev: pd.Series) -> pd.Series:
    """Worst single 21-day pct drop in EV within trailing 252-day window."""
    chg = ev.pct_change(_TD_MON)
    return chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def mcd_043_mc_worst_21d_log_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Worst single 21-day log-drop in marketcap within trailing 252-day window."""
    chg = _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_MON))
    return chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def mcd_044_mc_worst_63d_log_drop_expanding(marketcap: pd.Series) -> pd.Series:
    """All-time worst single 63-day log-drop in marketcap (expanding window)."""
    chg = _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_QTR))
    return chg.expanding(min_periods=_TD_QTR).min()


# --- Group E (045-055): Consecutive periods of marketcap decline ---

def mcd_045_mc_consec_down_days(marketcap: pd.Series) -> pd.Series:
    """Current streak of consecutive days with marketcap decline."""
    down = (marketcap.diff(1) < 0).astype(int)
    streak = down.copy().astype(float)
    for i in range(1, len(streak)):
        if down.iloc[i] == 1:
            streak.iloc[i] = streak.iloc[i - 1] + 1
        else:
            streak.iloc[i] = 0.0
    return streak


def mcd_046_mc_consec_down_weeks(marketcap: pd.Series) -> pd.Series:
    """Current streak of consecutive 5-day periods with negative 5-day change."""
    down = (marketcap.pct_change(5) < 0).astype(int)
    streak = down.copy().astype(float)
    for i in range(1, len(streak)):
        if down.iloc[i] == 1:
            streak.iloc[i] = streak.iloc[i - 1] + 1
        else:
            streak.iloc[i] = 0.0
    return streak


def mcd_047_mc_down_days_fraction_21d(marketcap: pd.Series) -> pd.Series:
    """Fraction of days in last 21d where marketcap declined from prior day."""
    down = (marketcap.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_MON)


def mcd_048_mc_down_days_fraction_63d(marketcap: pd.Series) -> pd.Series:
    """Fraction of days in last 63d where marketcap declined from prior day."""
    down = (marketcap.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_QTR)


def mcd_049_mc_down_days_fraction_252d(marketcap: pd.Series) -> pd.Series:
    """Fraction of days in last 252d where marketcap declined from prior day."""
    down = (marketcap.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_YEAR)


def mcd_050_ev_down_days_fraction_63d(ev: pd.Series) -> pd.Series:
    """Fraction of days in last 63d where EV declined from prior day."""
    down = (ev.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_QTR)


def mcd_051_mc_down_weeks_fraction_252d(marketcap: pd.Series) -> pd.Series:
    """Fraction of 5-day windows in last 252d showing negative 5-day change."""
    down = (marketcap.pct_change(5) < 0).astype(float)
    return _rolling_mean(down, _TD_YEAR)


def mcd_052_mc_max_consec_down_in_252d(marketcap: pd.Series) -> pd.Series:
    """Maximum consecutive-down-days streak seen in the trailing 252-day window."""
    down = (marketcap.diff(1) < 0).astype(float)
    def _max_streak(x):
        cur = best = 0
        for v in x:
            if v == 1:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return down.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_streak, raw=True)


def mcd_053_mc_max_consec_down_in_63d(marketcap: pd.Series) -> pd.Series:
    """Maximum consecutive-down-days streak seen in the trailing 63-day window."""
    down = (marketcap.diff(1) < 0).astype(float)
    def _max_streak_q(x):
        cur = best = 0
        for v in x:
            if v == 1:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return down.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_streak_q, raw=True)


def mcd_054_mc_down_qtrs_fraction_504d(marketcap: pd.Series) -> pd.Series:
    """Fraction of 63-day windows in last 504d showing negative 63-day change."""
    down = (marketcap.pct_change(_TD_QTR) < 0).astype(float)
    return _rolling_mean(down, 504)


def mcd_055_ev_down_days_fraction_252d(ev: pd.Series) -> pd.Series:
    """Fraction of days in last 252d where EV declined from prior day."""
    down = (ev.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_YEAR)


# --- Group F (056-065): Marketcap at multi-year lows / low-range metrics ---

def mcd_056_mc_pct_above_252d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 252-day marketcap low (distance from trough)."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return _safe_div(marketcap - lo, lo)


def mcd_057_mc_pct_above_504d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 504-day marketcap low."""
    lo = _rolling_min(marketcap, 504)
    return _safe_div(marketcap - lo, lo)


def mcd_058_mc_pct_above_1260d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 1260-day (5-year) marketcap low."""
    lo = _rolling_min(marketcap, 1260)
    return _safe_div(marketcap - lo, lo)


def mcd_059_mc_pct_above_all_time_low(marketcap: pd.Series) -> pd.Series:
    """Percent above all-time expanding marketcap low."""
    lo = marketcap.expanding(min_periods=1).min()
    return _safe_div(marketcap - lo, lo)


def mcd_060_mc_position_in_252d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 252-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(marketcap, _TD_YEAR)
    lo = _rolling_min(marketcap, _TD_YEAR)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_061_mc_position_in_504d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 504-day high-low range."""
    hi = _rolling_max(marketcap, 504)
    lo = _rolling_min(marketcap, 504)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_062_mc_position_in_1260d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 1260-day high-low range."""
    hi = _rolling_max(marketcap, 1260)
    lo = _rolling_min(marketcap, 1260)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_063_mc_log_spread_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Log distance from current marketcap to 252-day peak (always positive)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    return _log_safe(pk) - _log_safe(marketcap)


def mcd_064_mc_log_spread_from_all_time_peak(marketcap: pd.Series) -> pd.Series:
    """Log distance from current marketcap to all-time peak."""
    pk = marketcap.expanding(min_periods=1).max()
    return _log_safe(pk) - _log_safe(marketcap)


def mcd_065_ev_position_in_252d_range(ev: pd.Series) -> pd.Series:
    """Position of EV within 252-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(ev, _TD_YEAR)
    lo = _rolling_min(ev, _TD_YEAR)
    return _safe_div(ev - lo, hi - lo)


# --- Group G (066-075): Marketcap vs trailing averages / compression metrics ---

def mcd_066_mc_vs_sma21(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 21-day trailing average (pct)."""
    ma = _rolling_mean(marketcap, _TD_MON)
    return _safe_div(marketcap - ma, ma)


def mcd_067_mc_vs_sma63(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 63-day trailing average (pct)."""
    ma = _rolling_mean(marketcap, _TD_QTR)
    return _safe_div(marketcap - ma, ma)


def mcd_068_mc_vs_sma252(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 252-day trailing average (pct)."""
    ma = _rolling_mean(marketcap, _TD_YEAR)
    return _safe_div(marketcap - ma, ma)


def mcd_069_mc_vs_ema21(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 21-day EMA (pct)."""
    ma = _ewm_mean(marketcap, _TD_MON)
    return _safe_div(marketcap - ma, ma)


def mcd_070_mc_vs_ema63(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 63-day EMA (pct)."""
    ma = _ewm_mean(marketcap, _TD_QTR)
    return _safe_div(marketcap - ma, ma)


def mcd_071_mc_vs_ema252(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 252-day EMA (pct)."""
    ma = _ewm_mean(marketcap, _TD_YEAR)
    return _safe_div(marketcap - ma, ma)


def mcd_072_mc_zscore_252d(marketcap: pd.Series) -> pd.Series:
    """Z-score of marketcap relative to trailing 252-day distribution."""
    return _zscore_rolling(marketcap, _TD_YEAR)


def mcd_073_mc_zscore_504d(marketcap: pd.Series) -> pd.Series:
    """Z-score of marketcap relative to trailing 504-day distribution."""
    return _zscore_rolling(marketcap, 504)


def mcd_074_mc_pct_rank_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of current marketcap within trailing 252-day window."""
    return _rolling_rank_pct(marketcap, _TD_YEAR)


def mcd_075_mc_pct_rank_1260d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of current marketcap within trailing 1260-day window."""
    return _rolling_rank_pct(marketcap, 1260)


# --- Group H2 (151-160): EWM and median-based marketcap destruction extensions ---

def mcd_151_mc_vs_ema126(marketcap: pd.Series) -> pd.Series:
    """Marketcap deviation from its 126-day EMA (pct)."""
    ma = _ewm_mean(marketcap, _TD_HALF)
    return _safe_div(marketcap - ma, ma)


def mcd_152_mc_zscore_126d(marketcap: pd.Series) -> pd.Series:
    """Z-score of marketcap relative to trailing 126-day distribution."""
    return _zscore_rolling(marketcap, _TD_HALF)


def mcd_153_mc_pct_rank_504d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of current marketcap within trailing 504-day window."""
    return _rolling_rank_pct(marketcap, 504)


def mcd_154_mc_vs_126d_median(marketcap: pd.Series) -> pd.Series:
    """Percent deviation of marketcap from its 126-day rolling median."""
    med = _rolling_median(marketcap, _TD_HALF)
    return _safe_div(marketcap - med, med)


def mcd_155_mc_log_dd_from_126d_peak(marketcap: pd.Series) -> pd.Series:
    """Log-space marketcap drawdown from 126-day peak."""
    pk = _rolling_max(marketcap, _TD_HALF)
    return _log_safe(marketcap) - _log_safe(pk)


def mcd_156_mc_dd_from_63d_peak_vol_adj(marketcap: pd.Series) -> pd.Series:
    """63-day mc drawdown divided by 63-day rolling std of daily pct changes."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), _TD_QTR)
    return _safe_div(dd, vol)


def mcd_157_mc_log_spread_from_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Log distance from current marketcap to 504-day peak (always non-negative)."""
    pk = _rolling_max(marketcap, 504)
    return _log_safe(pk) - _log_safe(marketcap)


def mcd_158_mc_sma21_vs_sma63(marketcap: pd.Series) -> pd.Series:
    """21-day SMA minus 63-day SMA, normalized by 63-day SMA (short-term vs medium momentum)."""
    s21 = _rolling_mean(marketcap, _TD_MON)
    s63 = _rolling_mean(marketcap, _TD_QTR)
    return _safe_div(s21 - s63, s63)


def mcd_159_mc_sma63_vs_sma252(marketcap: pd.Series) -> pd.Series:
    """63-day SMA minus 252-day SMA, normalized by 252-day SMA (medium vs annual momentum)."""
    s63  = _rolling_mean(marketcap, _TD_QTR)
    s252 = _rolling_mean(marketcap, _TD_YEAR)
    return _safe_div(s63 - s252, s252)


def mcd_160_mc_ema21_vs_ema126(marketcap: pd.Series) -> pd.Series:
    """21-day EMA minus 126-day EMA, normalized by 126-day EMA."""
    e21  = _ewm_mean(marketcap, _TD_MON)
    e126 = _ewm_mean(marketcap, _TD_HALF)
    return _safe_div(e21 - e126, e126)


# --- Group I2 (161-170): Velocity and persistence extensions ---

def mcd_161_mc_63d_log_change(marketcap: pd.Series) -> pd.Series:
    """63-day log change in marketcap (quarterly log-velocity)."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_QTR))


def mcd_162_mc_126d_log_change(marketcap: pd.Series) -> pd.Series:
    """126-day log change in marketcap (half-year log-velocity)."""
    return _log_safe(marketcap) - _log_safe(marketcap.shift(_TD_HALF))


def mcd_163_mc_down_days_fraction_126d(marketcap: pd.Series) -> pd.Series:
    """Fraction of days in last 126d where marketcap declined from prior day."""
    down = (marketcap.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_HALF)


def mcd_164_mc_sum_neg_1d_in_252d(marketcap: pd.Series) -> pd.Series:
    """Sum of daily negative pct changes in marketcap over 252-day window."""
    chg = marketcap.pct_change(1)
    neg = chg.where(chg < 0, other=0.0)
    return _rolling_sum(neg, _TD_YEAR)


def mcd_165_mc_worst_5d_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Worst single 5-day pct drop in marketcap within trailing 252-day window."""
    chg = marketcap.pct_change(5)
    return chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def mcd_166_mc_worst_1d_drop_in_126d(marketcap: pd.Series) -> pd.Series:
    """Worst single daily pct drop in marketcap within trailing 126-day window."""
    chg = marketcap.pct_change(1)
    return chg.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()


def mcd_167_mc_avg_5d_drop_in_252d(marketcap: pd.Series) -> pd.Series:
    """Average of 5-day negative pct changes in marketcap over 252-day window."""
    chg = marketcap.pct_change(5)
    neg = chg.where(chg < 0, other=0.0)
    return _rolling_mean(neg, _TD_YEAR)


def mcd_168_mc_down_qtrs_fraction_252d(marketcap: pd.Series) -> pd.Series:
    """Fraction of 63-day windows in last 252d showing negative 63-day change."""
    down = (marketcap.pct_change(_TD_QTR) < 0).astype(float)
    return _rolling_mean(down, _TD_YEAR)


def mcd_169_ev_126d_pct_change(ev: pd.Series) -> pd.Series:
    """126-day percent change in enterprise value (half-year EV destruction velocity)."""
    return ev.pct_change(_TD_HALF)


def mcd_170_ev_252d_pct_change(ev: pd.Series) -> pd.Series:
    """252-day percent change in enterprise value (annual EV destruction velocity)."""
    return ev.pct_change(_TD_YEAR)


# --- Group J2 (171-175): Absolute level and cross-field extensions ---

def mcd_171_mc_pct_above_126d_low(marketcap: pd.Series) -> pd.Series:
    """Percent above 126-day marketcap low (distance from half-year trough)."""
    lo = _rolling_min(marketcap, _TD_HALF)
    return _safe_div(marketcap - lo, lo)


def mcd_172_mc_position_in_126d_range(marketcap: pd.Series) -> pd.Series:
    """Position of marketcap within 126-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(marketcap, _TD_HALF)
    lo = _rolling_min(marketcap, _TD_HALF)
    return _safe_div(marketcap - lo, hi - lo)


def mcd_173_ev_position_in_504d_range(ev: pd.Series) -> pd.Series:
    """Position of EV within 504-day high-low range (0=low, 1=high)."""
    hi = _rolling_max(ev, 504)
    lo = _rolling_min(ev, 504)
    return _safe_div(ev - lo, hi - lo)


def mcd_174_mc_ev_ratio_zscore_504d(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Z-score of MC/EV ratio over trailing 504-day window."""
    ratio = _safe_div(marketcap, ev)
    return _zscore_rolling(ratio, 504)


def mcd_175_mc_log_level_vs_126d_avg(marketcap: pd.Series) -> pd.Series:
    """Log marketcap minus log of 126-day avg marketcap (half-year compression measure)."""
    return _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, _TD_HALF))


# ── Registry ───────────────────────────────────────────────────────────────────

MARKETCAP_DESTRUCTION_REGISTRY_001_075 = {
    "mcd_001_mc_dd_from_21d_peak":             {"inputs": ["marketcap"], "func": mcd_001_mc_dd_from_21d_peak},
    "mcd_002_mc_dd_from_63d_peak":             {"inputs": ["marketcap"], "func": mcd_002_mc_dd_from_63d_peak},
    "mcd_003_mc_dd_from_126d_peak":            {"inputs": ["marketcap"], "func": mcd_003_mc_dd_from_126d_peak},
    "mcd_004_mc_dd_from_252d_peak":            {"inputs": ["marketcap"], "func": mcd_004_mc_dd_from_252d_peak},
    "mcd_005_mc_dd_from_504d_peak":            {"inputs": ["marketcap"], "func": mcd_005_mc_dd_from_504d_peak},
    "mcd_006_mc_dd_from_756d_peak":            {"inputs": ["marketcap"], "func": mcd_006_mc_dd_from_756d_peak},
    "mcd_007_mc_dd_from_1260d_peak":           {"inputs": ["marketcap"], "func": mcd_007_mc_dd_from_1260d_peak},
    "mcd_008_mc_dd_from_all_time_peak":        {"inputs": ["marketcap"], "func": mcd_008_mc_dd_from_all_time_peak},
    "mcd_009_mc_log_dd_from_252d_peak":        {"inputs": ["marketcap"], "func": mcd_009_mc_log_dd_from_252d_peak},
    "mcd_010_mc_log_dd_from_all_time_peak":    {"inputs": ["marketcap"], "func": mcd_010_mc_log_dd_from_all_time_peak},
    "mcd_011_mc_log_dd_from_504d_peak":        {"inputs": ["marketcap"], "func": mcd_011_mc_log_dd_from_504d_peak},
    "mcd_012_mc_log_dd_from_756d_peak":        {"inputs": ["marketcap"], "func": mcd_012_mc_log_dd_from_756d_peak},
    "mcd_013_mc_dollar_loss_from_252d_peak":   {"inputs": ["marketcap"], "func": mcd_013_mc_dollar_loss_from_252d_peak},
    "mcd_014_mc_dollar_loss_from_all_time_peak": {"inputs": ["marketcap"], "func": mcd_014_mc_dollar_loss_from_all_time_peak},
    "mcd_015_mc_dollar_loss_from_504d_peak":   {"inputs": ["marketcap"], "func": mcd_015_mc_dollar_loss_from_504d_peak},
    "mcd_016_mc_log_dollar_loss_from_252d_peak": {"inputs": ["marketcap"], "func": mcd_016_mc_log_dollar_loss_from_252d_peak},
    "mcd_017_mc_log_dollar_loss_from_all_time_peak": {"inputs": ["marketcap"], "func": mcd_017_mc_log_dollar_loss_from_all_time_peak},
    "mcd_018_mc_fraction_peak_remaining":      {"inputs": ["marketcap"], "func": mcd_018_mc_fraction_peak_remaining},
    "mcd_019_mc_fraction_252d_peak_remaining": {"inputs": ["marketcap"], "func": mcd_019_mc_fraction_252d_peak_remaining},
    "mcd_020_ev_dd_from_252d_peak":            {"inputs": ["ev"],        "func": mcd_020_ev_dd_from_252d_peak},
    "mcd_021_ev_dd_from_all_time_peak":        {"inputs": ["ev"],        "func": mcd_021_ev_dd_from_all_time_peak},
    "mcd_022_ev_dollar_loss_from_252d_peak":   {"inputs": ["ev"],        "func": mcd_022_ev_dollar_loss_from_252d_peak},
    "mcd_023_mc_5d_pct_change":                {"inputs": ["marketcap"], "func": mcd_023_mc_5d_pct_change},
    "mcd_024_mc_21d_pct_change":               {"inputs": ["marketcap"], "func": mcd_024_mc_21d_pct_change},
    "mcd_025_mc_63d_pct_change":               {"inputs": ["marketcap"], "func": mcd_025_mc_63d_pct_change},
    "mcd_026_mc_126d_pct_change":              {"inputs": ["marketcap"], "func": mcd_026_mc_126d_pct_change},
    "mcd_027_mc_252d_pct_change":              {"inputs": ["marketcap"], "func": mcd_027_mc_252d_pct_change},
    "mcd_028_mc_5d_log_change":                {"inputs": ["marketcap"], "func": mcd_028_mc_5d_log_change},
    "mcd_029_mc_21d_log_change":               {"inputs": ["marketcap"], "func": mcd_029_mc_21d_log_change},
    "mcd_030_mc_63d_log_change":               {"inputs": ["marketcap"], "func": mcd_030_mc_63d_log_change},
    "mcd_031_mc_252d_log_change":              {"inputs": ["marketcap"], "func": mcd_031_mc_252d_log_change},
    "mcd_032_ev_21d_pct_change":               {"inputs": ["ev"],        "func": mcd_032_ev_21d_pct_change},
    "mcd_033_ev_63d_pct_change":               {"inputs": ["ev"],        "func": mcd_033_ev_63d_pct_change},
    "mcd_034_mc_worst_5d_drop_in_63d":         {"inputs": ["marketcap"], "func": mcd_034_mc_worst_5d_drop_in_63d},
    "mcd_035_mc_worst_21d_drop_in_252d":       {"inputs": ["marketcap"], "func": mcd_035_mc_worst_21d_drop_in_252d},
    "mcd_036_mc_worst_63d_drop_in_504d":       {"inputs": ["marketcap"], "func": mcd_036_mc_worst_63d_drop_in_504d},
    "mcd_037_mc_worst_1d_drop_in_21d":         {"inputs": ["marketcap"], "func": mcd_037_mc_worst_1d_drop_in_21d},
    "mcd_038_mc_worst_1d_drop_in_252d":        {"inputs": ["marketcap"], "func": mcd_038_mc_worst_1d_drop_in_252d},
    "mcd_039_mc_worst_5d_drop_expanding":      {"inputs": ["marketcap"], "func": mcd_039_mc_worst_5d_drop_expanding},
    "mcd_040_mc_avg_1d_drop_in_252d":          {"inputs": ["marketcap"], "func": mcd_040_mc_avg_1d_drop_in_252d},
    "mcd_041_mc_sum_neg_1d_in_63d":            {"inputs": ["marketcap"], "func": mcd_041_mc_sum_neg_1d_in_63d},
    "mcd_042_ev_worst_21d_drop_in_252d":       {"inputs": ["ev"],        "func": mcd_042_ev_worst_21d_drop_in_252d},
    "mcd_043_mc_worst_21d_log_drop_in_252d":   {"inputs": ["marketcap"], "func": mcd_043_mc_worst_21d_log_drop_in_252d},
    "mcd_044_mc_worst_63d_log_drop_expanding": {"inputs": ["marketcap"], "func": mcd_044_mc_worst_63d_log_drop_expanding},
    "mcd_045_mc_consec_down_days":             {"inputs": ["marketcap"], "func": mcd_045_mc_consec_down_days},
    "mcd_046_mc_consec_down_weeks":            {"inputs": ["marketcap"], "func": mcd_046_mc_consec_down_weeks},
    "mcd_047_mc_down_days_fraction_21d":       {"inputs": ["marketcap"], "func": mcd_047_mc_down_days_fraction_21d},
    "mcd_048_mc_down_days_fraction_63d":       {"inputs": ["marketcap"], "func": mcd_048_mc_down_days_fraction_63d},
    "mcd_049_mc_down_days_fraction_252d":      {"inputs": ["marketcap"], "func": mcd_049_mc_down_days_fraction_252d},
    "mcd_050_ev_down_days_fraction_63d":       {"inputs": ["ev"],        "func": mcd_050_ev_down_days_fraction_63d},
    "mcd_051_mc_down_weeks_fraction_252d":     {"inputs": ["marketcap"], "func": mcd_051_mc_down_weeks_fraction_252d},
    "mcd_052_mc_max_consec_down_in_252d":      {"inputs": ["marketcap"], "func": mcd_052_mc_max_consec_down_in_252d},
    "mcd_053_mc_max_consec_down_in_63d":       {"inputs": ["marketcap"], "func": mcd_053_mc_max_consec_down_in_63d},
    "mcd_054_mc_down_qtrs_fraction_504d":      {"inputs": ["marketcap"], "func": mcd_054_mc_down_qtrs_fraction_504d},
    "mcd_055_ev_down_days_fraction_252d":      {"inputs": ["ev"],        "func": mcd_055_ev_down_days_fraction_252d},
    "mcd_056_mc_pct_above_252d_low":           {"inputs": ["marketcap"], "func": mcd_056_mc_pct_above_252d_low},
    "mcd_057_mc_pct_above_504d_low":           {"inputs": ["marketcap"], "func": mcd_057_mc_pct_above_504d_low},
    "mcd_058_mc_pct_above_1260d_low":          {"inputs": ["marketcap"], "func": mcd_058_mc_pct_above_1260d_low},
    "mcd_059_mc_pct_above_all_time_low":       {"inputs": ["marketcap"], "func": mcd_059_mc_pct_above_all_time_low},
    "mcd_060_mc_position_in_252d_range":       {"inputs": ["marketcap"], "func": mcd_060_mc_position_in_252d_range},
    "mcd_061_mc_position_in_504d_range":       {"inputs": ["marketcap"], "func": mcd_061_mc_position_in_504d_range},
    "mcd_062_mc_position_in_1260d_range":      {"inputs": ["marketcap"], "func": mcd_062_mc_position_in_1260d_range},
    "mcd_063_mc_log_spread_from_252d_peak":    {"inputs": ["marketcap"], "func": mcd_063_mc_log_spread_from_252d_peak},
    "mcd_064_mc_log_spread_from_all_time_peak": {"inputs": ["marketcap"], "func": mcd_064_mc_log_spread_from_all_time_peak},
    "mcd_065_ev_position_in_252d_range":       {"inputs": ["ev"],        "func": mcd_065_ev_position_in_252d_range},
    "mcd_066_mc_vs_sma21":                     {"inputs": ["marketcap"], "func": mcd_066_mc_vs_sma21},
    "mcd_067_mc_vs_sma63":                     {"inputs": ["marketcap"], "func": mcd_067_mc_vs_sma63},
    "mcd_068_mc_vs_sma252":                    {"inputs": ["marketcap"], "func": mcd_068_mc_vs_sma252},
    "mcd_069_mc_vs_ema21":                     {"inputs": ["marketcap"], "func": mcd_069_mc_vs_ema21},
    "mcd_070_mc_vs_ema63":                     {"inputs": ["marketcap"], "func": mcd_070_mc_vs_ema63},
    "mcd_071_mc_vs_ema252":                    {"inputs": ["marketcap"], "func": mcd_071_mc_vs_ema252},
    "mcd_072_mc_zscore_252d":                  {"inputs": ["marketcap"], "func": mcd_072_mc_zscore_252d},
    "mcd_073_mc_zscore_504d":                  {"inputs": ["marketcap"], "func": mcd_073_mc_zscore_504d},
    "mcd_074_mc_pct_rank_252d":                {"inputs": ["marketcap"], "func": mcd_074_mc_pct_rank_252d},
    "mcd_075_mc_pct_rank_1260d":               {"inputs": ["marketcap"], "func": mcd_075_mc_pct_rank_1260d},
    "mcd_151_mc_vs_ema126":                    {"inputs": ["marketcap"], "func": mcd_151_mc_vs_ema126},
    "mcd_152_mc_zscore_126d":                  {"inputs": ["marketcap"], "func": mcd_152_mc_zscore_126d},
    "mcd_153_mc_pct_rank_504d":                {"inputs": ["marketcap"], "func": mcd_153_mc_pct_rank_504d},
    "mcd_154_mc_vs_126d_median":               {"inputs": ["marketcap"], "func": mcd_154_mc_vs_126d_median},
    "mcd_155_mc_log_dd_from_126d_peak":        {"inputs": ["marketcap"], "func": mcd_155_mc_log_dd_from_126d_peak},
    "mcd_156_mc_dd_from_63d_peak_vol_adj":     {"inputs": ["marketcap"], "func": mcd_156_mc_dd_from_63d_peak_vol_adj},
    "mcd_157_mc_log_spread_from_504d_peak":    {"inputs": ["marketcap"], "func": mcd_157_mc_log_spread_from_504d_peak},
    "mcd_158_mc_sma21_vs_sma63":               {"inputs": ["marketcap"], "func": mcd_158_mc_sma21_vs_sma63},
    "mcd_159_mc_sma63_vs_sma252":              {"inputs": ["marketcap"], "func": mcd_159_mc_sma63_vs_sma252},
    "mcd_160_mc_ema21_vs_ema126":              {"inputs": ["marketcap"], "func": mcd_160_mc_ema21_vs_ema126},
    "mcd_161_mc_63d_log_change":               {"inputs": ["marketcap"], "func": mcd_161_mc_63d_log_change},
    "mcd_162_mc_126d_log_change":              {"inputs": ["marketcap"], "func": mcd_162_mc_126d_log_change},
    "mcd_163_mc_down_days_fraction_126d":      {"inputs": ["marketcap"], "func": mcd_163_mc_down_days_fraction_126d},
    "mcd_164_mc_sum_neg_1d_in_252d":           {"inputs": ["marketcap"], "func": mcd_164_mc_sum_neg_1d_in_252d},
    "mcd_165_mc_worst_5d_drop_in_252d":        {"inputs": ["marketcap"], "func": mcd_165_mc_worst_5d_drop_in_252d},
    "mcd_166_mc_worst_1d_drop_in_126d":        {"inputs": ["marketcap"], "func": mcd_166_mc_worst_1d_drop_in_126d},
    "mcd_167_mc_avg_5d_drop_in_252d":          {"inputs": ["marketcap"], "func": mcd_167_mc_avg_5d_drop_in_252d},
    "mcd_168_mc_down_qtrs_fraction_252d":      {"inputs": ["marketcap"], "func": mcd_168_mc_down_qtrs_fraction_252d},
    "mcd_169_ev_126d_pct_change":              {"inputs": ["ev"],        "func": mcd_169_ev_126d_pct_change},
    "mcd_170_ev_252d_pct_change":              {"inputs": ["ev"],        "func": mcd_170_ev_252d_pct_change},
    "mcd_171_mc_pct_above_126d_low":           {"inputs": ["marketcap"], "func": mcd_171_mc_pct_above_126d_low},
    "mcd_172_mc_position_in_126d_range":       {"inputs": ["marketcap"], "func": mcd_172_mc_position_in_126d_range},
    "mcd_173_ev_position_in_504d_range":       {"inputs": ["ev"],        "func": mcd_173_ev_position_in_504d_range},
    "mcd_174_mc_ev_ratio_zscore_504d":         {"inputs": ["marketcap", "ev"], "func": mcd_174_mc_ev_ratio_zscore_504d},
    "mcd_175_mc_log_level_vs_126d_avg":        {"inputs": ["marketcap"], "func": mcd_175_mc_log_level_vs_126d_avg},
}
