"""
118_drawdown_recovery_asymmetry — Base Features 001-075
Domain: asymmetry between down-legs and up-legs within the price path —
        magnitude/speed/duration of down-moves vs up-moves, ratchet behaviour
        (fast falls vs slow grinds), gain/loss ratio of the path, up-day vs
        down-day average size asymmetry, downside vs upside participation,
        asymmetry of the cumulative path around the drawdown.
        NOT the statistical skew of the return distribution — this is about
        the geometry of falls vs rises in the path.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _up_ret(close: pd.Series) -> pd.Series:
    """Daily return clipped to positive (up-day moves only)."""
    return close.pct_change(1).clip(lower=0.0)


def _dn_ret(close: pd.Series) -> pd.Series:
    """Absolute daily return clipped to positive when negative (down-day magnitudes)."""
    return (-close.pct_change(1)).clip(lower=0.0)


def _rolling_nanmean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean that drops NaNs before averaging (min_periods = w//2)."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Average up-day vs down-day return magnitude ---

def dra_001_avg_up_ret_21d(close: pd.Series) -> pd.Series:
    """Mean up-day return over trailing 21 days (average positive return size)."""
    up = _up_ret(close)
    up_pos = up.where(up > 0)
    return _rolling_nanmean(up_pos, _TD_MON)


def dra_002_avg_dn_ret_21d(close: pd.Series) -> pd.Series:
    """Mean down-day absolute return over trailing 21 days."""
    dn = _dn_ret(close)
    dn_pos = dn.where(dn > 0)
    return _rolling_nanmean(dn_pos, _TD_MON)


def dra_003_up_dn_avg_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day return to average down-day return (21 days).
    Values < 1 indicate down-moves are larger on average (bearish asymmetry)."""
    avg_up = dra_001_avg_up_ret_21d(close)
    avg_dn = dra_002_avg_dn_ret_21d(close)
    return _safe_div(avg_up, avg_dn.replace(0, np.nan))


def dra_004_avg_up_ret_63d(close: pd.Series) -> pd.Series:
    """Mean up-day return over trailing 63 days."""
    up = _up_ret(close)
    up_pos = up.where(up > 0)
    return _rolling_nanmean(up_pos, _TD_QTR)


def dra_005_avg_dn_ret_63d(close: pd.Series) -> pd.Series:
    """Mean down-day absolute return over trailing 63 days."""
    dn = _dn_ret(close)
    dn_pos = dn.where(dn > 0)
    return _rolling_nanmean(dn_pos, _TD_QTR)


def dra_006_up_dn_avg_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day return to average down-day return (63 days)."""
    avg_up = dra_004_avg_up_ret_63d(close)
    avg_dn = dra_005_avg_dn_ret_63d(close)
    return _safe_div(avg_up, avg_dn.replace(0, np.nan))


def dra_007_avg_up_ret_252d(close: pd.Series) -> pd.Series:
    """Mean up-day return over trailing 252 days."""
    up = _up_ret(close)
    up_pos = up.where(up > 0)
    return _rolling_nanmean(up_pos, _TD_YEAR)


def dra_008_avg_dn_ret_252d(close: pd.Series) -> pd.Series:
    """Mean down-day absolute return over trailing 252 days."""
    dn = _dn_ret(close)
    dn_pos = dn.where(dn > 0)
    return _rolling_nanmean(dn_pos, _TD_YEAR)


def dra_009_up_dn_avg_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day return to average down-day return (252 days)."""
    avg_up = dra_007_avg_up_ret_252d(close)
    avg_dn = dra_008_avg_dn_ret_252d(close)
    return _safe_div(avg_up, avg_dn.replace(0, np.nan))


def dra_010_avg_up_dn_diff_21d(close: pd.Series) -> pd.Series:
    """Difference (avg_up - avg_dn) over 21 days. Negative = larger down-moves."""
    avg_up = dra_001_avg_up_ret_21d(close)
    avg_dn = dra_002_avg_dn_ret_21d(close)
    return avg_up - avg_dn


# --- Group B (011-020): Up-day vs down-day count asymmetry ---

def dra_011_up_day_count_21d(close: pd.Series) -> pd.Series:
    """Count of up-days (close > prev close) in trailing 21 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret > 0).astype(float), _TD_MON)


def dra_012_dn_day_count_21d(close: pd.Series) -> pd.Series:
    """Count of down-days (close < prev close) in trailing 21 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret < 0).astype(float), _TD_MON)


def dra_013_up_dn_count_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of up-day count to down-day count over 21 days."""
    return _safe_div(dra_011_up_day_count_21d(close), dra_012_dn_day_count_21d(close))


def dra_014_up_day_count_63d(close: pd.Series) -> pd.Series:
    """Count of up-days in trailing 63 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret > 0).astype(float), _TD_QTR)


def dra_015_dn_day_count_63d(close: pd.Series) -> pd.Series:
    """Count of down-days in trailing 63 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret < 0).astype(float), _TD_QTR)


def dra_016_up_dn_count_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of up-day count to down-day count over 63 days."""
    return _safe_div(dra_014_up_day_count_63d(close), dra_015_dn_day_count_63d(close))


def dra_017_up_day_count_252d(close: pd.Series) -> pd.Series:
    """Count of up-days in trailing 252 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret > 0).astype(float), _TD_YEAR)


def dra_018_dn_day_count_252d(close: pd.Series) -> pd.Series:
    """Count of down-days in trailing 252 days."""
    ret = close.pct_change(1)
    return _rolling_sum((ret < 0).astype(float), _TD_YEAR)


def dra_019_up_dn_count_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of up-day count to down-day count over 252 days."""
    return _safe_div(dra_017_up_day_count_252d(close), dra_018_dn_day_count_252d(close))


def dra_020_dn_dominance_21d(close: pd.Series) -> pd.Series:
    """Fraction of total days that were down-days over 21 days (0.5 = neutral)."""
    ret = close.pct_change(1)
    dn = _rolling_sum((ret < 0).astype(float), _TD_MON)
    total = _rolling_sum((~ret.isna()).astype(float), _TD_MON)
    return _safe_div(dn, total)


# --- Group C (021-030): Sum of up vs down returns (path gain/loss) ---

def dra_021_sum_up_ret_21d(close: pd.Series) -> pd.Series:
    """Sum of all positive daily returns over trailing 21 days (total upside captured)."""
    return _rolling_sum(_up_ret(close), _TD_MON)


def dra_022_sum_dn_ret_21d(close: pd.Series) -> pd.Series:
    """Sum of all negative daily return magnitudes over trailing 21 days."""
    return _rolling_sum(_dn_ret(close), _TD_MON)


def dra_023_gain_loss_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of total up-return sum to total down-return sum over 21 days.
    < 1 means path lost more than it gained (ratchet down behavior)."""
    return _safe_div(dra_021_sum_up_ret_21d(close), dra_022_sum_dn_ret_21d(close))


def dra_024_sum_up_ret_63d(close: pd.Series) -> pd.Series:
    """Sum of positive daily returns over trailing 63 days."""
    return _rolling_sum(_up_ret(close), _TD_QTR)


def dra_025_sum_dn_ret_63d(close: pd.Series) -> pd.Series:
    """Sum of negative daily return magnitudes over trailing 63 days."""
    return _rolling_sum(_dn_ret(close), _TD_QTR)


def dra_026_gain_loss_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of total up-return to total down-return magnitudes over 63 days."""
    return _safe_div(dra_024_sum_up_ret_63d(close), dra_025_sum_dn_ret_63d(close))


def dra_027_sum_up_ret_252d(close: pd.Series) -> pd.Series:
    """Sum of positive daily returns over trailing 252 days."""
    return _rolling_sum(_up_ret(close), _TD_YEAR)


def dra_028_sum_dn_ret_252d(close: pd.Series) -> pd.Series:
    """Sum of negative daily return magnitudes over trailing 252 days."""
    return _rolling_sum(_dn_ret(close), _TD_YEAR)


def dra_029_gain_loss_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of total up-return to total down-return magnitudes over 252 days."""
    return _safe_div(dra_027_sum_up_ret_252d(close), dra_028_sum_dn_ret_252d(close))


def dra_030_net_path_balance_21d(close: pd.Series) -> pd.Series:
    """Net path: sum_up - sum_dn over 21 days. Negative = cumulative path lost more."""
    return dra_021_sum_up_ret_21d(close) - dra_022_sum_dn_ret_21d(close)


# --- Group D (031-040): Speed/duration of largest leg asymmetry ---

def dra_031_max_single_up_ret_21d(close: pd.Series) -> pd.Series:
    """Maximum single-day up-return over trailing 21 days."""
    return _rolling_max(_up_ret(close), _TD_MON)


def dra_032_max_single_dn_ret_21d(close: pd.Series) -> pd.Series:
    """Maximum single-day down-return magnitude over trailing 21 days."""
    return _rolling_max(_dn_ret(close), _TD_MON)


def dra_033_max_up_vs_dn_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of max single up-day to max single down-day over 21 days."""
    return _safe_div(dra_031_max_single_up_ret_21d(close), dra_032_max_single_dn_ret_21d(close))


def dra_034_max_single_up_ret_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day up-return over trailing 63 days."""
    return _rolling_max(_up_ret(close), _TD_QTR)


def dra_035_max_single_dn_ret_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day down-return magnitude over trailing 63 days."""
    return _rolling_max(_dn_ret(close), _TD_QTR)


def dra_036_max_up_vs_dn_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of max single up-day to max single down-day over 63 days."""
    return _safe_div(dra_034_max_single_up_ret_63d(close), dra_035_max_single_dn_ret_63d(close))


def dra_037_max_single_up_ret_252d(close: pd.Series) -> pd.Series:
    """Maximum single-day up-return over trailing 252 days."""
    return _rolling_max(_up_ret(close), _TD_YEAR)


def dra_038_max_single_dn_ret_252d(close: pd.Series) -> pd.Series:
    """Maximum single-day down-return magnitude over trailing 252 days."""
    return _rolling_max(_dn_ret(close), _TD_YEAR)


def dra_039_max_up_vs_dn_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of max single up-day to max single down-day over 252 days."""
    return _safe_div(dra_037_max_single_up_ret_252d(close), dra_038_max_single_dn_ret_252d(close))


def dra_040_dn_excess_over_up_max_21d(close: pd.Series) -> pd.Series:
    """Max down-day minus max up-day over 21 days. Positive = bigger drops than rises."""
    return dra_032_max_single_dn_ret_21d(close) - dra_031_max_single_up_ret_21d(close)


# --- Group E (041-050): Ratchet / consecutive streak asymmetry ---

def dra_041_max_consec_dn_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak within trailing 21 days."""
    ret = close.pct_change(1)
    dn_streak = _consec_streak(ret < 0)
    return dn_streak.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()


def dra_042_max_consec_up_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day streak within trailing 21 days."""
    ret = close.pct_change(1)
    up_streak = _consec_streak(ret > 0)
    return up_streak.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()


def dra_043_consec_streak_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of max dn-streak to max up-streak over 21 days.
    > 1 = sustained falls longer than rises (ratchet down behavior)."""
    return _safe_div(dra_041_max_consec_dn_streak_21d(close),
                     dra_042_max_consec_up_streak_21d(close))


def dra_044_max_consec_dn_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak within trailing 63 days."""
    ret = close.pct_change(1)
    dn_streak = _consec_streak(ret < 0)
    return dn_streak.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()


def dra_045_max_consec_up_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day streak within trailing 63 days."""
    ret = close.pct_change(1)
    up_streak = _consec_streak(ret > 0)
    return up_streak.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()


def dra_046_consec_streak_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of max dn-streak to max up-streak over 63 days."""
    return _safe_div(dra_044_max_consec_dn_streak_63d(close),
                     dra_045_max_consec_up_streak_63d(close))


def dra_047_current_dn_streak(close: pd.Series) -> pd.Series:
    """Current consecutive down-day streak (number of days closing lower)."""
    return _consec_streak(close.pct_change(1) < 0).astype(float)


def dra_048_current_up_streak(close: pd.Series) -> pd.Series:
    """Current consecutive up-day streak (number of days closing higher)."""
    return _consec_streak(close.pct_change(1) > 0).astype(float)


def dra_049_streak_balance_21d(close: pd.Series) -> pd.Series:
    """Max dn-streak minus max up-streak over 21 days. Positive = falls persist longer."""
    return dra_041_max_consec_dn_streak_21d(close) - dra_042_max_consec_up_streak_21d(close)


def dra_050_dn_streak_dominance_252d(close: pd.Series) -> pd.Series:
    """Max dn-streak minus max up-streak over 252 days (long-run ratchet signature)."""
    ret = close.pct_change(1)
    dn_streak = _consec_streak(ret < 0)
    up_streak = _consec_streak(ret > 0)
    max_dn = dn_streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    max_up = up_streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return max_dn - max_up


# --- Group F (051-060): Downside vs upside participation rates ---

def dra_051_dn_participation_rate_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day return variance explained by down-days.
    Computed as sum_dn^2 / (sum_dn^2 + sum_up^2) where each is rolling sum of squared daily rets."""
    ret = close.pct_change(1)
    up_sq = (ret.clip(lower=0.0) ** 2)
    dn_sq = ((-ret).clip(lower=0.0) ** 2)
    sum_up_sq = _rolling_sum(up_sq, _TD_MON)
    sum_dn_sq = _rolling_sum(dn_sq, _TD_MON)
    total = sum_up_sq + sum_dn_sq
    return _safe_div(sum_dn_sq, total.replace(0, np.nan))


def dra_052_dn_participation_rate_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day return variance explained by down-days."""
    ret = close.pct_change(1)
    up_sq = (ret.clip(lower=0.0) ** 2)
    dn_sq = ((-ret).clip(lower=0.0) ** 2)
    sum_up_sq = _rolling_sum(up_sq, _TD_QTR)
    sum_dn_sq = _rolling_sum(dn_sq, _TD_QTR)
    total = sum_up_sq + sum_dn_sq
    return _safe_div(sum_dn_sq, total.replace(0, np.nan))


def dra_053_dn_participation_rate_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day return variance explained by down-days."""
    ret = close.pct_change(1)
    up_sq = (ret.clip(lower=0.0) ** 2)
    dn_sq = ((-ret).clip(lower=0.0) ** 2)
    sum_up_sq = _rolling_sum(up_sq, _TD_YEAR)
    sum_dn_sq = _rolling_sum(dn_sq, _TD_YEAR)
    total = sum_up_sq + sum_dn_sq
    return _safe_div(sum_dn_sq, total.replace(0, np.nan))


def dra_054_upside_vol_21d(close: pd.Series) -> pd.Series:
    """Upside semi-deviation over 21 days (std of positive returns)."""
    ret = close.pct_change(1)
    up = ret.clip(lower=0.0)
    return up.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()


def dra_055_downside_vol_21d(close: pd.Series) -> pd.Series:
    """Downside semi-deviation over 21 days (std of negative return magnitudes)."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    return dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()


def dra_056_vol_asymmetry_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 21 days. > 1 = more volatile falls."""
    return _safe_div(dra_055_downside_vol_21d(close), dra_054_upside_vol_21d(close))


def dra_057_upside_vol_63d(close: pd.Series) -> pd.Series:
    """Upside semi-deviation over 63 days."""
    ret = close.pct_change(1)
    up = ret.clip(lower=0.0)
    return up.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()


def dra_058_downside_vol_63d(close: pd.Series) -> pd.Series:
    """Downside semi-deviation over 63 days."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    return dn.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()


def dra_059_vol_asymmetry_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 63 days."""
    return _safe_div(dra_058_downside_vol_63d(close), dra_057_upside_vol_63d(close))


def dra_060_vol_asymmetry_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 252 days."""
    ret = close.pct_change(1)
    up_vol = ret.clip(lower=0.0).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    return _safe_div(dn_vol, up_vol)


# --- Group G (061-075): Drawdown leg geometry — cumulative path asymmetry ---

def dra_061_sum_dn_over_sum_up_21d(close: pd.Series) -> pd.Series:
    """Sum of down-return magnitudes divided by sum of up-returns over 21 days.
    > 1 means the path gave back more than it gained in the window."""
    return _safe_div(dra_022_sum_dn_ret_21d(close), dra_021_sum_up_ret_21d(close))


def dra_062_sum_dn_over_sum_up_63d(close: pd.Series) -> pd.Series:
    """Sum of down-return magnitudes divided by sum of up-returns over 63 days."""
    return _safe_div(dra_025_sum_dn_ret_63d(close), dra_024_sum_up_ret_63d(close))


def dra_063_sum_dn_over_sum_up_252d(close: pd.Series) -> pd.Series:
    """Sum of down-return magnitudes divided by sum of up-returns over 252 days."""
    return _safe_div(dra_028_sum_dn_ret_252d(close), dra_027_sum_up_ret_252d(close))


def dra_064_path_net_cumret_21d(close: pd.Series) -> pd.Series:
    """Net cumulative return of the path over 21 days (close/close[21] - 1)."""
    return close.pct_change(_TD_MON)


def dra_065_path_net_cumret_63d(close: pd.Series) -> pd.Series:
    """Net cumulative return of the path over 63 days."""
    return close.pct_change(_TD_QTR)


def dra_066_path_net_cumret_252d(close: pd.Series) -> pd.Series:
    """Net cumulative return of the path over 252 days."""
    return close.pct_change(_TD_YEAR)


def dra_067_gross_dn_path_21d(close: pd.Series) -> pd.Series:
    """Gross downside of the path over 21 days: sum of all down daily magnitudes."""
    return dra_022_sum_dn_ret_21d(close)


def dra_068_gross_dn_vs_net_21d(close: pd.Series) -> pd.Series:
    """Gross downside minus abs(net return) over 21 days.
    Positive = the path was more volatile than its net move (lots of churn)."""
    net = dra_064_path_net_cumret_21d(close).abs()
    gross_dn = dra_022_sum_dn_ret_21d(close)
    return gross_dn - net


def dra_069_gross_dn_vs_net_63d(close: pd.Series) -> pd.Series:
    """Gross downside minus abs(net return) over 63 days."""
    net = dra_065_path_net_cumret_63d(close).abs()
    gross_dn = dra_025_sum_dn_ret_63d(close)
    return gross_dn - net


def dra_070_dn_ret_concentration_21d(close: pd.Series) -> pd.Series:
    """Concentration of down-day returns: max_dn / sum_dn over 21 days.
    High = one big plunge dominates the down-path (panic-bar signature)."""
    max_dn = dra_032_max_single_dn_ret_21d(close)
    sum_dn = dra_022_sum_dn_ret_21d(close)
    return _safe_div(max_dn, sum_dn.replace(0, np.nan))


def dra_071_dn_ret_concentration_63d(close: pd.Series) -> pd.Series:
    """Concentration of down-day returns: max_dn / sum_dn over 63 days."""
    max_dn = dra_035_max_single_dn_ret_63d(close)
    sum_dn = dra_025_sum_dn_ret_63d(close)
    return _safe_div(max_dn, sum_dn.replace(0, np.nan))


def dra_072_up_ret_concentration_21d(close: pd.Series) -> pd.Series:
    """Concentration of up-day returns: max_up / sum_up over 21 days."""
    max_up = dra_031_max_single_up_ret_21d(close)
    sum_up = dra_021_sum_up_ret_21d(close)
    return _safe_div(max_up, sum_up.replace(0, np.nan))


def dra_073_dn_up_concentration_diff_21d(close: pd.Series) -> pd.Series:
    """Dn concentration minus up concentration over 21 days.
    Positive = down-moves more spike-like vs distributed up-moves."""
    return dra_070_dn_ret_concentration_21d(close) - dra_072_up_ret_concentration_21d(close)


def dra_074_path_efficiency_dn_21d(close: pd.Series) -> pd.Series:
    """Down-path efficiency: net_dn_move / gross_dn over 21 days.
    High = falling efficiently (few recoveries); low = falling with churn."""
    net = close.pct_change(_TD_MON)
    dn_net = (-net).clip(lower=0.0)
    gross_dn = dra_022_sum_dn_ret_21d(close)
    return _safe_div(dn_net, gross_dn.replace(0, np.nan))


def dra_075_path_efficiency_dn_63d(close: pd.Series) -> pd.Series:
    """Down-path efficiency: net_dn_move / gross_dn over 63 days."""
    net = close.pct_change(_TD_QTR)
    dn_net = (-net).clip(lower=0.0)
    gross_dn = dra_025_sum_dn_ret_63d(close)
    return _safe_div(dn_net, gross_dn.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_RECOVERY_ASYMMETRY_REGISTRY_001_075 = {
    "dra_001_avg_up_ret_21d": {"inputs": ["close"], "func": dra_001_avg_up_ret_21d},
    "dra_002_avg_dn_ret_21d": {"inputs": ["close"], "func": dra_002_avg_dn_ret_21d},
    "dra_003_up_dn_avg_ratio_21d": {"inputs": ["close"], "func": dra_003_up_dn_avg_ratio_21d},
    "dra_004_avg_up_ret_63d": {"inputs": ["close"], "func": dra_004_avg_up_ret_63d},
    "dra_005_avg_dn_ret_63d": {"inputs": ["close"], "func": dra_005_avg_dn_ret_63d},
    "dra_006_up_dn_avg_ratio_63d": {"inputs": ["close"], "func": dra_006_up_dn_avg_ratio_63d},
    "dra_007_avg_up_ret_252d": {"inputs": ["close"], "func": dra_007_avg_up_ret_252d},
    "dra_008_avg_dn_ret_252d": {"inputs": ["close"], "func": dra_008_avg_dn_ret_252d},
    "dra_009_up_dn_avg_ratio_252d": {"inputs": ["close"], "func": dra_009_up_dn_avg_ratio_252d},
    "dra_010_avg_up_dn_diff_21d": {"inputs": ["close"], "func": dra_010_avg_up_dn_diff_21d},
    "dra_011_up_day_count_21d": {"inputs": ["close"], "func": dra_011_up_day_count_21d},
    "dra_012_dn_day_count_21d": {"inputs": ["close"], "func": dra_012_dn_day_count_21d},
    "dra_013_up_dn_count_ratio_21d": {"inputs": ["close"], "func": dra_013_up_dn_count_ratio_21d},
    "dra_014_up_day_count_63d": {"inputs": ["close"], "func": dra_014_up_day_count_63d},
    "dra_015_dn_day_count_63d": {"inputs": ["close"], "func": dra_015_dn_day_count_63d},
    "dra_016_up_dn_count_ratio_63d": {"inputs": ["close"], "func": dra_016_up_dn_count_ratio_63d},
    "dra_017_up_day_count_252d": {"inputs": ["close"], "func": dra_017_up_day_count_252d},
    "dra_018_dn_day_count_252d": {"inputs": ["close"], "func": dra_018_dn_day_count_252d},
    "dra_019_up_dn_count_ratio_252d": {"inputs": ["close"], "func": dra_019_up_dn_count_ratio_252d},
    "dra_020_dn_dominance_21d": {"inputs": ["close"], "func": dra_020_dn_dominance_21d},
    "dra_021_sum_up_ret_21d": {"inputs": ["close"], "func": dra_021_sum_up_ret_21d},
    "dra_022_sum_dn_ret_21d": {"inputs": ["close"], "func": dra_022_sum_dn_ret_21d},
    "dra_023_gain_loss_ratio_21d": {"inputs": ["close"], "func": dra_023_gain_loss_ratio_21d},
    "dra_024_sum_up_ret_63d": {"inputs": ["close"], "func": dra_024_sum_up_ret_63d},
    "dra_025_sum_dn_ret_63d": {"inputs": ["close"], "func": dra_025_sum_dn_ret_63d},
    "dra_026_gain_loss_ratio_63d": {"inputs": ["close"], "func": dra_026_gain_loss_ratio_63d},
    "dra_027_sum_up_ret_252d": {"inputs": ["close"], "func": dra_027_sum_up_ret_252d},
    "dra_028_sum_dn_ret_252d": {"inputs": ["close"], "func": dra_028_sum_dn_ret_252d},
    "dra_029_gain_loss_ratio_252d": {"inputs": ["close"], "func": dra_029_gain_loss_ratio_252d},
    "dra_030_net_path_balance_21d": {"inputs": ["close"], "func": dra_030_net_path_balance_21d},
    "dra_031_max_single_up_ret_21d": {"inputs": ["close"], "func": dra_031_max_single_up_ret_21d},
    "dra_032_max_single_dn_ret_21d": {"inputs": ["close"], "func": dra_032_max_single_dn_ret_21d},
    "dra_033_max_up_vs_dn_ratio_21d": {"inputs": ["close"], "func": dra_033_max_up_vs_dn_ratio_21d},
    "dra_034_max_single_up_ret_63d": {"inputs": ["close"], "func": dra_034_max_single_up_ret_63d},
    "dra_035_max_single_dn_ret_63d": {"inputs": ["close"], "func": dra_035_max_single_dn_ret_63d},
    "dra_036_max_up_vs_dn_ratio_63d": {"inputs": ["close"], "func": dra_036_max_up_vs_dn_ratio_63d},
    "dra_037_max_single_up_ret_252d": {"inputs": ["close"], "func": dra_037_max_single_up_ret_252d},
    "dra_038_max_single_dn_ret_252d": {"inputs": ["close"], "func": dra_038_max_single_dn_ret_252d},
    "dra_039_max_up_vs_dn_ratio_252d": {"inputs": ["close"], "func": dra_039_max_up_vs_dn_ratio_252d},
    "dra_040_dn_excess_over_up_max_21d": {"inputs": ["close"], "func": dra_040_dn_excess_over_up_max_21d},
    "dra_041_max_consec_dn_streak_21d": {"inputs": ["close"], "func": dra_041_max_consec_dn_streak_21d},
    "dra_042_max_consec_up_streak_21d": {"inputs": ["close"], "func": dra_042_max_consec_up_streak_21d},
    "dra_043_consec_streak_ratio_21d": {"inputs": ["close"], "func": dra_043_consec_streak_ratio_21d},
    "dra_044_max_consec_dn_streak_63d": {"inputs": ["close"], "func": dra_044_max_consec_dn_streak_63d},
    "dra_045_max_consec_up_streak_63d": {"inputs": ["close"], "func": dra_045_max_consec_up_streak_63d},
    "dra_046_consec_streak_ratio_63d": {"inputs": ["close"], "func": dra_046_consec_streak_ratio_63d},
    "dra_047_current_dn_streak": {"inputs": ["close"], "func": dra_047_current_dn_streak},
    "dra_048_current_up_streak": {"inputs": ["close"], "func": dra_048_current_up_streak},
    "dra_049_streak_balance_21d": {"inputs": ["close"], "func": dra_049_streak_balance_21d},
    "dra_050_dn_streak_dominance_252d": {"inputs": ["close"], "func": dra_050_dn_streak_dominance_252d},
    "dra_051_dn_participation_rate_21d": {"inputs": ["close"], "func": dra_051_dn_participation_rate_21d},
    "dra_052_dn_participation_rate_63d": {"inputs": ["close"], "func": dra_052_dn_participation_rate_63d},
    "dra_053_dn_participation_rate_252d": {"inputs": ["close"], "func": dra_053_dn_participation_rate_252d},
    "dra_054_upside_vol_21d": {"inputs": ["close"], "func": dra_054_upside_vol_21d},
    "dra_055_downside_vol_21d": {"inputs": ["close"], "func": dra_055_downside_vol_21d},
    "dra_056_vol_asymmetry_ratio_21d": {"inputs": ["close"], "func": dra_056_vol_asymmetry_ratio_21d},
    "dra_057_upside_vol_63d": {"inputs": ["close"], "func": dra_057_upside_vol_63d},
    "dra_058_downside_vol_63d": {"inputs": ["close"], "func": dra_058_downside_vol_63d},
    "dra_059_vol_asymmetry_ratio_63d": {"inputs": ["close"], "func": dra_059_vol_asymmetry_ratio_63d},
    "dra_060_vol_asymmetry_ratio_252d": {"inputs": ["close"], "func": dra_060_vol_asymmetry_ratio_252d},
    "dra_061_sum_dn_over_sum_up_21d": {"inputs": ["close"], "func": dra_061_sum_dn_over_sum_up_21d},
    "dra_062_sum_dn_over_sum_up_63d": {"inputs": ["close"], "func": dra_062_sum_dn_over_sum_up_63d},
    "dra_063_sum_dn_over_sum_up_252d": {"inputs": ["close"], "func": dra_063_sum_dn_over_sum_up_252d},
    "dra_064_path_net_cumret_21d": {"inputs": ["close"], "func": dra_064_path_net_cumret_21d},
    "dra_065_path_net_cumret_63d": {"inputs": ["close"], "func": dra_065_path_net_cumret_63d},
    "dra_066_path_net_cumret_252d": {"inputs": ["close"], "func": dra_066_path_net_cumret_252d},
    "dra_067_gross_dn_path_21d": {"inputs": ["close"], "func": dra_067_gross_dn_path_21d},
    "dra_068_gross_dn_vs_net_21d": {"inputs": ["close"], "func": dra_068_gross_dn_vs_net_21d},
    "dra_069_gross_dn_vs_net_63d": {"inputs": ["close"], "func": dra_069_gross_dn_vs_net_63d},
    "dra_070_dn_ret_concentration_21d": {"inputs": ["close"], "func": dra_070_dn_ret_concentration_21d},
    "dra_071_dn_ret_concentration_63d": {"inputs": ["close"], "func": dra_071_dn_ret_concentration_63d},
    "dra_072_up_ret_concentration_21d": {"inputs": ["close"], "func": dra_072_up_ret_concentration_21d},
    "dra_073_dn_up_concentration_diff_21d": {"inputs": ["close"], "func": dra_073_dn_up_concentration_diff_21d},
    "dra_074_path_efficiency_dn_21d": {"inputs": ["close"], "func": dra_074_path_efficiency_dn_21d},
    "dra_075_path_efficiency_dn_63d": {"inputs": ["close"], "func": dra_075_path_efficiency_dn_63d},
}
