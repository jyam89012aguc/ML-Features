"""
84_insider_buy_size — Base Features 076-200
Domain: dollar magnitude of insider purchases (buy size / dollar scale)
Asset class: US equities | Sharadar SF2 insider transactions (daily aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
aggregated from Sharadar SF2 insider transaction filings to one row per
(ticker, date).  These are EVENT-DRIVEN series: most days are ZERO; positive
values appear only on filing days.  Do NOT forward-fill these series.
Aggregate over trailing windows using rolling SUMS.  Functions look strictly
backward using .shift(positive), .rolling(), or .expanding().
Trading-day cadence: 1 week = 5, 1 month = 21, 1 quarter = 63, 1 year = 252.

Canonical input fields (lowercase):
    insider_buy_value, insider_buy_shares, insider_buy_count,
    officer_buy_value, ceo_buy_value, cfo_buy_value, tenpct_buy_value,
    director_buy_value, insider_sell_value, insider_shares_held
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_W5   = 5
_W21  = 21
_W63  = 63
_W126 = 126
_W252 = 252
_W504 = 504
_EPS  = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Momentum / acceleration of buy-value windows ---

def ibs_076_buy_value_21d_vs_prior_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Change in 21-day buy value sum vs the prior 21-day period (21-day diff)."""
    curr = _rolling_sum(insider_buy_value, _W21)
    return curr - curr.shift(_W21)


def ibs_077_buy_value_63d_vs_prior_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Change in 63-day buy value sum vs the prior 63-day period."""
    curr = _rolling_sum(insider_buy_value, _W63)
    return curr - curr.shift(_W63)


def ibs_078_buy_value_21d_pct_chg_vs_prior_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 21-day buy value sum vs the prior 21-day period."""
    curr  = _rolling_sum(insider_buy_value, _W21)
    prior = curr.shift(_W21)
    return _safe_div(curr - prior, prior)


def ibs_079_buy_value_63d_pct_chg_vs_prior_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day buy value sum vs the prior 63-day period."""
    curr  = _rolling_sum(insider_buy_value, _W63)
    prior = curr.shift(_W63)
    return _safe_div(curr - prior, prior)


def ibs_080_buy_value_252d_vs_prior_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Change in 252-day buy value sum vs the prior 252-day period."""
    curr = _rolling_sum(insider_buy_value, _W252)
    return curr - curr.shift(_W252)


def ibs_081_buy_value_21d_vs_63d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 21-day buy value to 63-day buy value (short vs medium momentum)."""
    short = _rolling_sum(insider_buy_value, _W21)
    med   = _rolling_sum(insider_buy_value, _W63)
    return _safe_div(short, med)


def ibs_082_buy_value_63d_vs_252d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 63-day buy value to 252-day buy value (medium vs long momentum)."""
    med  = _rolling_sum(insider_buy_value, _W63)
    lng  = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(med, lng)


def ibs_083_buy_value_21d_ewm_span63(insider_buy_value: pd.Series) -> pd.Series:
    """EWM (span=63) of daily insider buy value — smoothed short-term signal."""
    return _ewm_mean(insider_buy_value, _W63)


def ibs_084_buy_value_21d_ewm_span252(insider_buy_value: pd.Series) -> pd.Series:
    """EWM (span=252) of daily insider buy value — smoothed long-term signal."""
    return _ewm_mean(insider_buy_value, _W252)


def ibs_085_buy_value_ewm_crossover(insider_buy_value: pd.Series) -> pd.Series:
    """Short EWM (span=21) minus long EWM (span=252) of daily buy value (momentum crossover)."""
    short = _ewm_mean(insider_buy_value, _W21)
    lng   = _ewm_mean(insider_buy_value, _W252)
    return short - lng


def ibs_086_officer_buy_value_21d_vs_prior_21d(officer_buy_value: pd.Series) -> pd.Series:
    """Change in 21-day officer buy value vs prior 21-day period."""
    curr = _rolling_sum(officer_buy_value, _W21)
    return curr - curr.shift(_W21)


def ibs_087_ceo_buy_value_63d_vs_prior_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """Change in 63-day CEO buy value vs prior 63-day period."""
    curr = _rolling_sum(ceo_buy_value, _W63)
    return curr - curr.shift(_W63)


def ibs_088_buy_shares_21d_vs_prior_21d(insider_buy_shares: pd.Series) -> pd.Series:
    """Change in 21-day buy shares vs prior 21-day period."""
    curr = _rolling_sum(insider_buy_shares, _W21)
    return curr - curr.shift(_W21)


def ibs_089_buy_shares_63d_pct_chg_vs_prior(insider_buy_shares: pd.Series) -> pd.Series:
    """Percent change in 63-day buy shares vs prior 63-day period."""
    curr  = _rolling_sum(insider_buy_shares, _W63)
    prior = curr.shift(_W63)
    return _safe_div(curr - prior, prior)


def ibs_090_buy_value_acceleration_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Second-difference of 21-day buy value (acceleration of rolling buy momentum)."""
    curr = _rolling_sum(insider_buy_value, _W21)
    d1   = curr - curr.shift(_W21)
    return d1 - d1.shift(_W21)


# --- Group G (091-105): Big-buy thresholds and distribution features ---

def ibs_091_big_buy_flag_1m_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 21-day buy value exceeds $1 million."""
    return (_rolling_sum(insider_buy_value, _W21) > 1_000_000).astype(float)


def ibs_092_big_buy_flag_1m_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 63-day buy value exceeds $1 million."""
    return (_rolling_sum(insider_buy_value, _W63) > 1_000_000).astype(float)


def ibs_093_big_buy_flag_5m_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 252-day buy value exceeds $5 million."""
    return (_rolling_sum(insider_buy_value, _W252) > 5_000_000).astype(float)


def ibs_094_officer_big_buy_flag_500k_63d(officer_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 63-day officer buy value exceeds $500k."""
    return (_rolling_sum(officer_buy_value, _W63) > 500_000).astype(float)


def ibs_095_ceo_big_buy_flag_500k_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 63-day CEO buy value exceeds $500k."""
    return (_rolling_sum(ceo_buy_value, _W63) > 500_000).astype(float)


def ibs_096_buy_value_above_252d_median_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 21-day buy value exceeds 252-day rolling median of daily values."""
    short  = _rolling_sum(insider_buy_value, _W21)
    med    = _rolling_median(insider_buy_value, _W252)
    return (short > med).astype(float)


def ibs_097_buy_value_above_252d_mean_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: today's buy value exceeds trailing 252-day mean daily buy value."""
    mean_val = _rolling_mean(insider_buy_value, _W252)
    return (insider_buy_value > mean_val).astype(float)


def ibs_098_peak_buy_value_21d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + peak daily buy value in trailing 21-day window)."""
    return np.log1p(_rolling_max(insider_buy_value, _W21).clip(lower=0))


def ibs_099_peak_buy_value_63d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + peak daily buy value in trailing 63-day window)."""
    return np.log1p(_rolling_max(insider_buy_value, _W63).clip(lower=0))


def ibs_100_peak_buy_value_252d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + peak daily buy value in trailing 252-day window)."""
    return np.log1p(_rolling_max(insider_buy_value, _W252).clip(lower=0))


def ibs_101_buy_value_std_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Standard deviation of daily buy value over trailing 63-day window (variability)."""
    return _rolling_std(insider_buy_value, _W63)


def ibs_102_buy_value_std_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Standard deviation of daily buy value over trailing 252-day window."""
    return _rolling_std(insider_buy_value, _W252)


def ibs_103_buy_value_cv_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy value over trailing 252-day window."""
    return _safe_div(_rolling_std(insider_buy_value, _W252),
                     _rolling_mean(insider_buy_value, _W252))


def ibs_104_buy_value_median_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Median daily buy value over trailing 63-day window."""
    return _rolling_median(insider_buy_value, _W63)


def ibs_105_buy_value_median_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Median daily buy value over trailing 252-day window."""
    return _rolling_median(insider_buy_value, _W252)


# --- Group H (106-120): Cross-role buy size comparisons ---

def ibs_106_officer_vs_director_buy_value_63d(officer_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Officer 63-day buy value minus director 63-day buy value (role magnitude gap)."""
    return _rolling_sum(officer_buy_value, _W63) - _rolling_sum(director_buy_value, _W63)


def ibs_107_officer_vs_director_buy_ratio_63d(officer_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Ratio of officer 63-day buy value to director 63-day buy value."""
    return _safe_div(_rolling_sum(officer_buy_value, _W63),
                     _rolling_sum(director_buy_value, _W63))


def ibs_108_ceo_vs_officer_buy_ratio_252d(ceo_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Ratio of CEO 252-day buy value to officer 252-day buy value."""
    return _safe_div(_rolling_sum(ceo_buy_value, _W252),
                     _rolling_sum(officer_buy_value, _W252))


def ibs_109_tenpct_vs_officer_buy_ratio_252d(tenpct_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Ratio of 10%+ holder 252-day buy value to officer 252-day buy value."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _W252),
                     _rolling_sum(officer_buy_value, _W252))


def ibs_110_cfo_vs_ceo_buy_ratio_252d(cfo_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """Ratio of CFO 252-day buy value to CEO 252-day buy value."""
    return _safe_div(_rolling_sum(cfo_buy_value, _W252),
                     _rolling_sum(ceo_buy_value, _W252))


def ibs_111_officer_plus_director_buy_value_63d(officer_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Combined officer + director buy value over 63-day window."""
    return _rolling_sum(officer_buy_value + director_buy_value, _W63)


def ibs_112_officer_plus_director_buy_value_252d(officer_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Combined officer + director buy value over 252-day window."""
    return _rolling_sum(officer_buy_value + director_buy_value, _W252)


def ibs_113_director_frac_of_total_buy_value_63d(director_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Director buy value as fraction of total insider buy value over 63-day window."""
    return _safe_div(_rolling_sum(director_buy_value, _W63),
                     _rolling_sum(insider_buy_value, _W63))


def ibs_114_tenpct_frac_of_total_buy_value_63d(tenpct_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """10%+ holder buy value as fraction of total insider buy value over 63-day window."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _W63),
                     _rolling_sum(insider_buy_value, _W63))


def ibs_115_cfo_frac_of_total_buy_value_63d(cfo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CFO buy value as fraction of total insider buy value over 63-day window."""
    return _safe_div(_rolling_sum(cfo_buy_value, _W63),
                     _rolling_sum(insider_buy_value, _W63))


def ibs_116_officer_buy_value_zscore_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily officer buy value within trailing 252-day window."""
    return _zscore_rolling(officer_buy_value, _W252)


def ibs_117_ceo_buy_value_zscore_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily CEO buy value within trailing 252-day window."""
    return _zscore_rolling(ceo_buy_value, _W252)


def ibs_118_director_buy_value_zscore_252d(director_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily director buy value within trailing 252-day window."""
    return _zscore_rolling(director_buy_value, _W252)


def ibs_119_tenpct_buy_value_zscore_252d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily 10%+ holder buy value within trailing 252-day window."""
    return _zscore_rolling(tenpct_buy_value, _W252)


def ibs_120_all_exec_buy_value_252d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO + officer buy value over 252-day window (executive buy total)."""
    combined = ceo_buy_value + cfo_buy_value + officer_buy_value
    return _rolling_sum(combined, _W252)


# --- Group I (121-135): Buy value drawdown from peak and recovery features ---

def ibs_121_buy_value_63d_drawdown_from_252d_peak(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy sum minus its 252-day rolling peak (distance from high)."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W252)
    return val - peak


def ibs_122_buy_value_63d_drawdown_from_504d_peak(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy sum minus its 504-day rolling peak."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W504)
    return val - peak


def ibs_123_buy_value_252d_drawdown_from_expanding_peak(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 252-day buy sum minus its expanding all-time peak."""
    val  = _rolling_sum(insider_buy_value, _W252)
    peak = val.expanding(min_periods=1).max()
    return val - peak


def ibs_124_buy_value_63d_above_expanding_mean_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 63-day buy sum is above its expanding historical mean."""
    val  = _rolling_sum(insider_buy_value, _W63)
    mean = val.expanding(min_periods=1).mean()
    return (val > mean).astype(float)


def ibs_125_buy_value_252d_above_expanding_mean_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 252-day buy sum is above its expanding historical mean."""
    val  = _rolling_sum(insider_buy_value, _W252)
    mean = val.expanding(min_periods=1).mean()
    return (val > mean).astype(float)


def ibs_126_buy_value_63d_new_high_count_252d(insider_buy_value: pd.Series) -> pd.Series:
    """
    Count of days within trailing 252-day window where 63-day buy sum
    equalled its own 252-day rolling maximum on that day (new-high frequency).
    Uses a scalar rolling apply; safe on all-zero inputs.
    """
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W252)
    is_high = (val >= peak - _EPS).astype(float)
    return _rolling_sum(is_high, _W252)


def ibs_127_buy_value_21d_pct_of_252d_sum(insider_buy_value: pd.Series) -> pd.Series:
    """21-day buy value as fraction of 252-day buy value (recency concentration)."""
    short = _rolling_sum(insider_buy_value, _W21)
    lng   = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(short, lng)


def ibs_128_buy_value_63d_pct_of_252d_sum(insider_buy_value: pd.Series) -> pd.Series:
    """63-day buy value as fraction of 252-day buy value."""
    med = _rolling_sum(insider_buy_value, _W63)
    lng = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(med, lng)


def ibs_129_officer_buy_value_126d(officer_buy_value: pd.Series) -> pd.Series:
    """Total officer buy value over trailing 126-day window."""
    return _rolling_sum(officer_buy_value, _W126)


def ibs_130_director_buy_value_126d(director_buy_value: pd.Series) -> pd.Series:
    """Total director buy value over trailing 126-day window."""
    return _rolling_sum(director_buy_value, _W126)


def ibs_131_tenpct_buy_value_126d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Total 10%+ holder buy value over trailing 126-day window."""
    return _rolling_sum(tenpct_buy_value, _W126)


def ibs_132_buy_shares_21d_log(insider_buy_shares: pd.Series) -> pd.Series:
    """Log(1 + trailing 21-day buy shares sum) — compresses distribution."""
    val = _rolling_sum(insider_buy_shares, _W21)
    return np.log1p(val.clip(lower=0))


def ibs_133_buy_shares_252d_log(insider_buy_shares: pd.Series) -> pd.Series:
    """Log(1 + trailing 252-day buy shares sum) — compresses distribution."""
    val = _rolling_sum(insider_buy_shares, _W252)
    return np.log1p(val.clip(lower=0))


def ibs_134_buy_value_per_buy_count_ratio_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    Ratio of avg buy size (63d) to 252-day mean avg buy size
    (how large is today's average transaction vs baseline).
    """
    avg_63  = _safe_div(_rolling_sum(insider_buy_value, _W63),
                        _rolling_sum(insider_buy_count, _W63))
    avg_252 = _safe_div(_rolling_sum(insider_buy_value, _W252),
                        _rolling_sum(insider_buy_count, _W252))
    return _safe_div(avg_63, avg_252)


def ibs_135_buy_value_nonzero_day_fraction_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252-day window with any insider buy activity."""
    active = (insider_buy_value > 0).astype(float)
    return _rolling_mean(active, _W252)


# --- Group J (136-150): Composite magnitude indices and final features ---

def ibs_136_buy_value_nonzero_day_fraction_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63-day window with any insider buy activity."""
    active = (insider_buy_value > 0).astype(float)
    return _rolling_mean(active, _W63)


def ibs_137_avg_buy_value_on_active_days_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Mean buy value on days where buy value > 0, trailing 63-day window."""
    active = insider_buy_value.where(insider_buy_value > 0)
    return _rolling_mean(active, _W63)


def ibs_138_avg_buy_value_on_active_days_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Mean buy value on days where buy value > 0, trailing 252-day window."""
    active = insider_buy_value.where(insider_buy_value > 0)
    return _rolling_mean(active, _W252)


def ibs_139_peak_buy_value_to_mean_ratio_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Peak 63-day buy sum divided by mean 63-day buy sum in 252-day window (lumpiness)."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W252)
    mean = _rolling_mean(val, _W252)
    return _safe_div(peak, mean)


def ibs_140_buy_value_63d_vs_sell_value_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day buy value divided by 252-day sell value (near-term buying vs long-term selling)."""
    buys  = _rolling_sum(insider_buy_value, _W63)
    sells = _rolling_sum(insider_sell_value, _W252)
    return _safe_div(buys, sells)


def ibs_141_net_buy_value_252d_log(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Log(1 + max(0, net_buy_252d)) — log of positive net buy value over 252 days."""
    buys  = _rolling_sum(insider_buy_value, _W252)
    sells = _rolling_sum(insider_sell_value, _W252)
    net   = (buys - sells).clip(lower=0)
    return np.log1p(net)


def ibs_142_buy_value_21d_expanding_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 21-day buy value sum (all-history)."""
    val = _rolling_sum(insider_buy_value, _W21)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_143_officer_buy_value_252d_expanding_zscore(officer_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 252-day officer buy value sum."""
    val = _rolling_sum(officer_buy_value, _W252)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_144_ceo_buy_value_252d_expanding_zscore(ceo_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 252-day CEO buy value sum."""
    val = _rolling_sum(ceo_buy_value, _W252)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_145_buy_value_slope_252d(insider_buy_value: pd.Series) -> pd.Series:
    """
    OLS slope of the 63-day rolling buy value series over a 252-day window.
    Positive = increasing buy magnitude trend; negative = declining.
    """
    val = _rolling_sum(insider_buy_value, _W63)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return val.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibs_146_buy_value_63d_vs_own_ewm_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """63-day buy value divided by its EWM (span=252) — buy intensity vs trend."""
    val = _rolling_sum(insider_buy_value, _W63)
    ewm = _ewm_mean(val, _W252)
    return _safe_div(val, ewm)


def ibs_147_buy_shares_nonzero_fraction_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63-day window with any insider share purchases."""
    active = (insider_buy_shares > 0).astype(float)
    return _rolling_mean(active, _W63)


def ibs_148_total_exec_buy_value_63d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO + officer buy value over 63-day window (executive concentration)."""
    combined = ceo_buy_value + cfo_buy_value + officer_buy_value
    return _rolling_sum(combined, _W63)


def ibs_149_buy_value_252d_above_1m_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 252-day buy value exceeds $1 million."""
    return (_rolling_sum(insider_buy_value, _W252) > 1_000_000).astype(float)


def ibs_150_buy_magnitude_composite(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series, tenpct_buy_value: pd.Series) -> pd.Series:
    """
    Composite buy-magnitude score: equally weighted average of four 252-day z-scores
    (total, officer, CEO, 10%+ holder buy values) — broad measure of buy-size intensity.
    """
    def _zs(s):
        return _zscore_rolling(_rolling_sum(s, _W252), _W252)

    z_total = _zs(insider_buy_value)
    z_off   = _zs(officer_buy_value)
    z_ceo   = _zs(ceo_buy_value)
    z_ten   = _zs(tenpct_buy_value)
    return (z_total + z_off + z_ceo + z_ten) / 4.0


# --- Group K new (176-200): Additional cross-window, z-score, and composite features ---

def ibs_176_buy_value_126d_pct_rank_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of trailing 126-day buy sum within a 504-day window."""
    val = _rolling_sum(insider_buy_value, _W126)
    return _rolling_rank_pct(val, _W504)


def ibs_177_buy_value_21d_vs_126d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 21-day buy sum to 126-day buy sum (short vs half-year concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W21),
                     _rolling_sum(insider_buy_value, _W126))


def ibs_178_officer_buy_value_zscore_504d(officer_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily officer buy value within trailing 504-day window."""
    return _zscore_rolling(officer_buy_value, _W504)


def ibs_179_ceo_buy_value_zscore_504d(ceo_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily CEO buy value within trailing 504-day window."""
    return _zscore_rolling(ceo_buy_value, _W504)


def ibs_180_director_buy_value_zscore_504d(director_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily director buy value within trailing 504-day window."""
    return _zscore_rolling(director_buy_value, _W504)


def ibs_181_buy_value_nonzero_day_fraction_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of days in trailing 126-day window with any insider buy activity."""
    return _rolling_mean((insider_buy_value > 0).astype(float), _W126)


def ibs_182_avg_buy_value_on_active_days_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Mean buy value on days where buy value > 0, trailing 126-day window."""
    active = insider_buy_value.where(insider_buy_value > 0)
    return _rolling_mean(active, _W126)


def ibs_183_buy_value_std_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Standard deviation of daily buy value over trailing 126-day window."""
    return _rolling_std(insider_buy_value, _W126)


def ibs_184_buy_value_cv_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy value over trailing 504-day window."""
    return _safe_div(_rolling_std(insider_buy_value, _W504),
                     _rolling_mean(insider_buy_value, _W504))


def ibs_185_buy_value_median_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Median daily buy value over trailing 126-day window."""
    return _rolling_median(insider_buy_value, _W126)


def ibs_186_peak_buy_value_504d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + peak daily buy value in trailing 504-day window)."""
    return np.log1p(_rolling_max(insider_buy_value, _W504).clip(lower=0))


def ibs_187_buy_value_126d_vs_own_ewm_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """126-day buy sum divided by its EWM (span=504) — buy intensity vs long-run trend."""
    val = _rolling_sum(insider_buy_value, _W126)
    ewm = _ewm_mean(val, _W504)
    return _safe_div(val, ewm)


def ibs_188_buy_value_504d_expanding_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 504-day buy value sum (all-history)."""
    val = _rolling_sum(insider_buy_value, _W504)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_189_officer_buy_value_126d_expanding_zscore(officer_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 126-day officer buy value sum."""
    val = _rolling_sum(officer_buy_value, _W126)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_190_net_buy_value_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider buy value (buys minus sells) over 504-day window."""
    return _rolling_sum(insider_buy_value, _W504) - _rolling_sum(insider_sell_value, _W504)


def ibs_191_buy_to_sell_value_ratio_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of total buy value to total sell value over 504-day window."""
    return _safe_div(_rolling_sum(insider_buy_value, _W504),
                     _rolling_sum(insider_sell_value, _W504))


def ibs_192_ceo_plus_cfo_buy_value_126d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO buy dollar value over trailing 126-day window."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _W126)


def ibs_193_officer_plus_director_buy_value_126d(officer_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Combined officer + director buy value over 126-day window."""
    return _rolling_sum(officer_buy_value + director_buy_value, _W126)


def ibs_194_tenpct_vs_director_buy_ratio_252d(tenpct_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Ratio of 10%+ holder 252-day buy value to director 252-day buy value."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _W252),
                     _rolling_sum(director_buy_value, _W252))


def ibs_195_buy_value_252d_slope_504d(insider_buy_value: pd.Series) -> pd.Series:
    """
    OLS slope of the 63-day rolling buy value series over a 504-day window.
    Longer-horizon trend in quarterly buy activity.
    """
    val = _rolling_sum(insider_buy_value, _W63)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return val.rolling(_W504, min_periods=max(2, _W504 // 4)).apply(_slope, raw=True)


def ibs_196_buy_value_5d_pct_of_252d_sum(insider_buy_value: pd.Series) -> pd.Series:
    """5-day buy value as fraction of 252-day buy value (ultra-near-term concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W5),
                     _rolling_sum(insider_buy_value, _W252))


def ibs_197_buy_shares_nonzero_fraction_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252-day window with any insider share purchases."""
    return _rolling_mean((insider_buy_shares > 0).astype(float), _W252)


def ibs_198_ceo_buy_value_126d_expanding_zscore(ceo_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 126-day CEO buy value sum."""
    val = _rolling_sum(ceo_buy_value, _W126)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_199_all_exec_buy_value_126d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO + officer buy value over 126-day window."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _W126)


def ibs_200_buy_magnitude_composite_504d(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series, tenpct_buy_value: pd.Series) -> pd.Series:
    """Composite buy-magnitude score: equally weighted average of four 504-day z-scores (total, officer, CEO, 10%+ holder)."""
    def _zs(s):
        return _zscore_rolling(_rolling_sum(s, _W504), _W504)
    return (_zs(insider_buy_value) + _zs(officer_buy_value) + _zs(ceo_buy_value) + _zs(tenpct_buy_value)) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_BUY_SIZE_REGISTRY_076_150 = {
    "ibs_076_buy_value_21d_vs_prior_21d":              {"inputs": ["insider_buy_value"],                                                       "func": ibs_076_buy_value_21d_vs_prior_21d},
    "ibs_077_buy_value_63d_vs_prior_63d":              {"inputs": ["insider_buy_value"],                                                       "func": ibs_077_buy_value_63d_vs_prior_63d},
    "ibs_078_buy_value_21d_pct_chg_vs_prior_21d":      {"inputs": ["insider_buy_value"],                                                       "func": ibs_078_buy_value_21d_pct_chg_vs_prior_21d},
    "ibs_079_buy_value_63d_pct_chg_vs_prior_63d":      {"inputs": ["insider_buy_value"],                                                       "func": ibs_079_buy_value_63d_pct_chg_vs_prior_63d},
    "ibs_080_buy_value_252d_vs_prior_252d":            {"inputs": ["insider_buy_value"],                                                       "func": ibs_080_buy_value_252d_vs_prior_252d},
    "ibs_081_buy_value_21d_vs_63d_ratio":              {"inputs": ["insider_buy_value"],                                                       "func": ibs_081_buy_value_21d_vs_63d_ratio},
    "ibs_082_buy_value_63d_vs_252d_ratio":             {"inputs": ["insider_buy_value"],                                                       "func": ibs_082_buy_value_63d_vs_252d_ratio},
    "ibs_083_buy_value_21d_ewm_span63":                {"inputs": ["insider_buy_value"],                                                       "func": ibs_083_buy_value_21d_ewm_span63},
    "ibs_084_buy_value_21d_ewm_span252":               {"inputs": ["insider_buy_value"],                                                       "func": ibs_084_buy_value_21d_ewm_span252},
    "ibs_085_buy_value_ewm_crossover":                 {"inputs": ["insider_buy_value"],                                                       "func": ibs_085_buy_value_ewm_crossover},
    "ibs_086_officer_buy_value_21d_vs_prior_21d":      {"inputs": ["officer_buy_value"],                                                       "func": ibs_086_officer_buy_value_21d_vs_prior_21d},
    "ibs_087_ceo_buy_value_63d_vs_prior_63d":          {"inputs": ["ceo_buy_value"],                                                           "func": ibs_087_ceo_buy_value_63d_vs_prior_63d},
    "ibs_088_buy_shares_21d_vs_prior_21d":             {"inputs": ["insider_buy_shares"],                                                      "func": ibs_088_buy_shares_21d_vs_prior_21d},
    "ibs_089_buy_shares_63d_pct_chg_vs_prior":         {"inputs": ["insider_buy_shares"],                                                      "func": ibs_089_buy_shares_63d_pct_chg_vs_prior},
    "ibs_090_buy_value_acceleration_21d":              {"inputs": ["insider_buy_value"],                                                       "func": ibs_090_buy_value_acceleration_21d},
    "ibs_091_big_buy_flag_1m_21d":                     {"inputs": ["insider_buy_value"],                                                       "func": ibs_091_big_buy_flag_1m_21d},
    "ibs_092_big_buy_flag_1m_63d":                     {"inputs": ["insider_buy_value"],                                                       "func": ibs_092_big_buy_flag_1m_63d},
    "ibs_093_big_buy_flag_5m_252d":                    {"inputs": ["insider_buy_value"],                                                       "func": ibs_093_big_buy_flag_5m_252d},
    "ibs_094_officer_big_buy_flag_500k_63d":           {"inputs": ["officer_buy_value"],                                                       "func": ibs_094_officer_big_buy_flag_500k_63d},
    "ibs_095_ceo_big_buy_flag_500k_63d":               {"inputs": ["ceo_buy_value"],                                                           "func": ibs_095_ceo_big_buy_flag_500k_63d},
    "ibs_096_buy_value_above_252d_median_flag":        {"inputs": ["insider_buy_value"],                                                       "func": ibs_096_buy_value_above_252d_median_flag},
    "ibs_097_buy_value_above_252d_mean_flag":          {"inputs": ["insider_buy_value"],                                                       "func": ibs_097_buy_value_above_252d_mean_flag},
    "ibs_098_peak_buy_value_21d_log":                  {"inputs": ["insider_buy_value"],                                                       "func": ibs_098_peak_buy_value_21d_log},
    "ibs_099_peak_buy_value_63d_log":                  {"inputs": ["insider_buy_value"],                                                       "func": ibs_099_peak_buy_value_63d_log},
    "ibs_100_peak_buy_value_252d_log":                 {"inputs": ["insider_buy_value"],                                                       "func": ibs_100_peak_buy_value_252d_log},
    "ibs_101_buy_value_std_63d":                       {"inputs": ["insider_buy_value"],                                                       "func": ibs_101_buy_value_std_63d},
    "ibs_102_buy_value_std_252d":                      {"inputs": ["insider_buy_value"],                                                       "func": ibs_102_buy_value_std_252d},
    "ibs_103_buy_value_cv_252d":                       {"inputs": ["insider_buy_value"],                                                       "func": ibs_103_buy_value_cv_252d},
    "ibs_104_buy_value_median_63d":                    {"inputs": ["insider_buy_value"],                                                       "func": ibs_104_buy_value_median_63d},
    "ibs_105_buy_value_median_252d":                   {"inputs": ["insider_buy_value"],                                                       "func": ibs_105_buy_value_median_252d},
    "ibs_106_officer_vs_director_buy_value_63d":       {"inputs": ["officer_buy_value", "director_buy_value"],                                 "func": ibs_106_officer_vs_director_buy_value_63d},
    "ibs_107_officer_vs_director_buy_ratio_63d":       {"inputs": ["officer_buy_value", "director_buy_value"],                                 "func": ibs_107_officer_vs_director_buy_ratio_63d},
    "ibs_108_ceo_vs_officer_buy_ratio_252d":           {"inputs": ["ceo_buy_value", "officer_buy_value"],                                      "func": ibs_108_ceo_vs_officer_buy_ratio_252d},
    "ibs_109_tenpct_vs_officer_buy_ratio_252d":        {"inputs": ["tenpct_buy_value", "officer_buy_value"],                                   "func": ibs_109_tenpct_vs_officer_buy_ratio_252d},
    "ibs_110_cfo_vs_ceo_buy_ratio_252d":               {"inputs": ["cfo_buy_value", "ceo_buy_value"],                                          "func": ibs_110_cfo_vs_ceo_buy_ratio_252d},
    "ibs_111_officer_plus_director_buy_value_63d":     {"inputs": ["officer_buy_value", "director_buy_value"],                                 "func": ibs_111_officer_plus_director_buy_value_63d},
    "ibs_112_officer_plus_director_buy_value_252d":    {"inputs": ["officer_buy_value", "director_buy_value"],                                 "func": ibs_112_officer_plus_director_buy_value_252d},
    "ibs_113_director_frac_of_total_buy_value_63d":    {"inputs": ["director_buy_value", "insider_buy_value"],                                 "func": ibs_113_director_frac_of_total_buy_value_63d},
    "ibs_114_tenpct_frac_of_total_buy_value_63d":      {"inputs": ["tenpct_buy_value", "insider_buy_value"],                                   "func": ibs_114_tenpct_frac_of_total_buy_value_63d},
    "ibs_115_cfo_frac_of_total_buy_value_63d":         {"inputs": ["cfo_buy_value", "insider_buy_value"],                                      "func": ibs_115_cfo_frac_of_total_buy_value_63d},
    "ibs_116_officer_buy_value_zscore_252d":           {"inputs": ["officer_buy_value"],                                                       "func": ibs_116_officer_buy_value_zscore_252d},
    "ibs_117_ceo_buy_value_zscore_252d":               {"inputs": ["ceo_buy_value"],                                                           "func": ibs_117_ceo_buy_value_zscore_252d},
    "ibs_118_director_buy_value_zscore_252d":          {"inputs": ["director_buy_value"],                                                      "func": ibs_118_director_buy_value_zscore_252d},
    "ibs_119_tenpct_buy_value_zscore_252d":            {"inputs": ["tenpct_buy_value"],                                                        "func": ibs_119_tenpct_buy_value_zscore_252d},
    "ibs_120_all_exec_buy_value_252d":                 {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"],                     "func": ibs_120_all_exec_buy_value_252d},
    "ibs_121_buy_value_63d_drawdown_from_252d_peak":   {"inputs": ["insider_buy_value"],                                                       "func": ibs_121_buy_value_63d_drawdown_from_252d_peak},
    "ibs_122_buy_value_63d_drawdown_from_504d_peak":   {"inputs": ["insider_buy_value"],                                                       "func": ibs_122_buy_value_63d_drawdown_from_504d_peak},
    "ibs_123_buy_value_252d_drawdown_from_expanding_peak": {"inputs": ["insider_buy_value"],                                                   "func": ibs_123_buy_value_252d_drawdown_from_expanding_peak},
    "ibs_124_buy_value_63d_above_expanding_mean_flag": {"inputs": ["insider_buy_value"],                                                       "func": ibs_124_buy_value_63d_above_expanding_mean_flag},
    "ibs_125_buy_value_252d_above_expanding_mean_flag":{"inputs": ["insider_buy_value"],                                                       "func": ibs_125_buy_value_252d_above_expanding_mean_flag},
    "ibs_126_buy_value_63d_new_high_count_252d":       {"inputs": ["insider_buy_value"],                                                       "func": ibs_126_buy_value_63d_new_high_count_252d},
    "ibs_127_buy_value_21d_pct_of_252d_sum":           {"inputs": ["insider_buy_value"],                                                       "func": ibs_127_buy_value_21d_pct_of_252d_sum},
    "ibs_128_buy_value_63d_pct_of_252d_sum":           {"inputs": ["insider_buy_value"],                                                       "func": ibs_128_buy_value_63d_pct_of_252d_sum},
    "ibs_129_officer_buy_value_126d":                  {"inputs": ["officer_buy_value"],                                                       "func": ibs_129_officer_buy_value_126d},
    "ibs_130_director_buy_value_126d":                 {"inputs": ["director_buy_value"],                                                      "func": ibs_130_director_buy_value_126d},
    "ibs_131_tenpct_buy_value_126d":                   {"inputs": ["tenpct_buy_value"],                                                        "func": ibs_131_tenpct_buy_value_126d},
    "ibs_132_buy_shares_21d_log":                      {"inputs": ["insider_buy_shares"],                                                      "func": ibs_132_buy_shares_21d_log},
    "ibs_133_buy_shares_252d_log":                     {"inputs": ["insider_buy_shares"],                                                      "func": ibs_133_buy_shares_252d_log},
    "ibs_134_buy_value_per_buy_count_ratio_63d":       {"inputs": ["insider_buy_value", "insider_buy_count"],                                  "func": ibs_134_buy_value_per_buy_count_ratio_63d},
    "ibs_135_buy_value_nonzero_day_fraction_252d":     {"inputs": ["insider_buy_value"],                                                       "func": ibs_135_buy_value_nonzero_day_fraction_252d},
    "ibs_136_buy_value_nonzero_day_fraction_63d":      {"inputs": ["insider_buy_value"],                                                       "func": ibs_136_buy_value_nonzero_day_fraction_63d},
    "ibs_137_avg_buy_value_on_active_days_63d":        {"inputs": ["insider_buy_value"],                                                       "func": ibs_137_avg_buy_value_on_active_days_63d},
    "ibs_138_avg_buy_value_on_active_days_252d":       {"inputs": ["insider_buy_value"],                                                       "func": ibs_138_avg_buy_value_on_active_days_252d},
    "ibs_139_peak_buy_value_to_mean_ratio_252d":       {"inputs": ["insider_buy_value"],                                                       "func": ibs_139_peak_buy_value_to_mean_ratio_252d},
    "ibs_140_buy_value_63d_vs_sell_value_252d":        {"inputs": ["insider_buy_value", "insider_sell_value"],                                 "func": ibs_140_buy_value_63d_vs_sell_value_252d},
    "ibs_141_net_buy_value_252d_log":                  {"inputs": ["insider_buy_value", "insider_sell_value"],                                 "func": ibs_141_net_buy_value_252d_log},
    "ibs_142_buy_value_21d_expanding_zscore":          {"inputs": ["insider_buy_value"],                                                       "func": ibs_142_buy_value_21d_expanding_zscore},
    "ibs_143_officer_buy_value_252d_expanding_zscore": {"inputs": ["officer_buy_value"],                                                       "func": ibs_143_officer_buy_value_252d_expanding_zscore},
    "ibs_144_ceo_buy_value_252d_expanding_zscore":     {"inputs": ["ceo_buy_value"],                                                           "func": ibs_144_ceo_buy_value_252d_expanding_zscore},
    "ibs_145_buy_value_slope_252d":                    {"inputs": ["insider_buy_value"],                                                       "func": ibs_145_buy_value_slope_252d},
    "ibs_146_buy_value_63d_vs_own_ewm_ratio":          {"inputs": ["insider_buy_value"],                                                       "func": ibs_146_buy_value_63d_vs_own_ewm_ratio},
    "ibs_147_buy_shares_nonzero_fraction_63d":         {"inputs": ["insider_buy_shares"],                                                      "func": ibs_147_buy_shares_nonzero_fraction_63d},
    "ibs_148_total_exec_buy_value_63d":                {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"],                     "func": ibs_148_total_exec_buy_value_63d},
    "ibs_149_buy_value_252d_above_1m_flag":            {"inputs": ["insider_buy_value"],                                                       "func": ibs_149_buy_value_252d_above_1m_flag},
    "ibs_150_buy_magnitude_composite":                 {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value", "tenpct_buy_value"], "func": ibs_150_buy_magnitude_composite},
    "ibs_176_buy_value_126d_pct_rank_504d":            {"inputs": ["insider_buy_value"],                                                              "func": ibs_176_buy_value_126d_pct_rank_504d},
    "ibs_177_buy_value_21d_vs_126d_ratio":             {"inputs": ["insider_buy_value"],                                                              "func": ibs_177_buy_value_21d_vs_126d_ratio},
    "ibs_178_officer_buy_value_zscore_504d":           {"inputs": ["officer_buy_value"],                                                              "func": ibs_178_officer_buy_value_zscore_504d},
    "ibs_179_ceo_buy_value_zscore_504d":               {"inputs": ["ceo_buy_value"],                                                                  "func": ibs_179_ceo_buy_value_zscore_504d},
    "ibs_180_director_buy_value_zscore_504d":          {"inputs": ["director_buy_value"],                                                             "func": ibs_180_director_buy_value_zscore_504d},
    "ibs_181_buy_value_nonzero_day_fraction_126d":     {"inputs": ["insider_buy_value"],                                                              "func": ibs_181_buy_value_nonzero_day_fraction_126d},
    "ibs_182_avg_buy_value_on_active_days_126d":       {"inputs": ["insider_buy_value"],                                                              "func": ibs_182_avg_buy_value_on_active_days_126d},
    "ibs_183_buy_value_std_126d":                      {"inputs": ["insider_buy_value"],                                                              "func": ibs_183_buy_value_std_126d},
    "ibs_184_buy_value_cv_504d":                       {"inputs": ["insider_buy_value"],                                                              "func": ibs_184_buy_value_cv_504d},
    "ibs_185_buy_value_median_126d":                   {"inputs": ["insider_buy_value"],                                                              "func": ibs_185_buy_value_median_126d},
    "ibs_186_peak_buy_value_504d_log":                 {"inputs": ["insider_buy_value"],                                                              "func": ibs_186_peak_buy_value_504d_log},
    "ibs_187_buy_value_126d_vs_own_ewm_ratio":         {"inputs": ["insider_buy_value"],                                                              "func": ibs_187_buy_value_126d_vs_own_ewm_ratio},
    "ibs_188_buy_value_504d_expanding_zscore":         {"inputs": ["insider_buy_value"],                                                              "func": ibs_188_buy_value_504d_expanding_zscore},
    "ibs_189_officer_buy_value_126d_expanding_zscore": {"inputs": ["officer_buy_value"],                                                              "func": ibs_189_officer_buy_value_126d_expanding_zscore},
    "ibs_190_net_buy_value_504d":                      {"inputs": ["insider_buy_value", "insider_sell_value"],                                        "func": ibs_190_net_buy_value_504d},
    "ibs_191_buy_to_sell_value_ratio_504d":            {"inputs": ["insider_buy_value", "insider_sell_value"],                                        "func": ibs_191_buy_to_sell_value_ratio_504d},
    "ibs_192_ceo_plus_cfo_buy_value_126d":             {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                                 "func": ibs_192_ceo_plus_cfo_buy_value_126d},
    "ibs_193_officer_plus_director_buy_value_126d":    {"inputs": ["officer_buy_value", "director_buy_value"],                                        "func": ibs_193_officer_plus_director_buy_value_126d},
    "ibs_194_tenpct_vs_director_buy_ratio_252d":       {"inputs": ["tenpct_buy_value", "director_buy_value"],                                         "func": ibs_194_tenpct_vs_director_buy_ratio_252d},
    "ibs_195_buy_value_252d_slope_504d":               {"inputs": ["insider_buy_value"],                                                              "func": ibs_195_buy_value_252d_slope_504d},
    "ibs_196_buy_value_5d_pct_of_252d_sum":            {"inputs": ["insider_buy_value"],                                                              "func": ibs_196_buy_value_5d_pct_of_252d_sum},
    "ibs_197_buy_shares_nonzero_fraction_252d":        {"inputs": ["insider_buy_shares"],                                                             "func": ibs_197_buy_shares_nonzero_fraction_252d},
    "ibs_198_ceo_buy_value_126d_expanding_zscore":     {"inputs": ["ceo_buy_value"],                                                                  "func": ibs_198_ceo_buy_value_126d_expanding_zscore},
    "ibs_199_all_exec_buy_value_126d":                 {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"],                            "func": ibs_199_all_exec_buy_value_126d},
    "ibs_200_buy_magnitude_composite_504d":            {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value", "tenpct_buy_value"],    "func": ibs_200_buy_magnitude_composite_504d},
}
