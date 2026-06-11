"""
87_insider_timing — Base Features 076-150 (extended to 200)
Domain: insider activity timing vs price drawdown depth
Asset class: US equities | SF2 insider series + daily close price
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
Inputs are:
  (1) daily close price (standard daily closing price)
  (2) daily event-aggregated Sharadar SF2 insider transaction series, one row
      per (ticker, date).  These series are EVENT-DRIVEN: they are mostly ZERO
      on non-filing dates and must NOT be forward-filled.  They are aggregated
      with trailing rolling SUMS over various windows.

Available field names (lowercase):
  close, insider_buy_count, insider_sell_count, insider_buy_shares,
  insider_sell_shares, insider_buy_value, insider_sell_value,
  insider_buyers, insider_sellers, officer_buy_value, ceo_buy_value,
  cfo_buy_value, insider_shares_held

Primary fields for this folder:
  close, insider_buy_count, insider_buy_value, insider_buyers,
  insider_sell_value, officer_buy_value

All feature functions look strictly backward: drawdown uses trailing
rolling/expanding max of close only.  No negative shifts, no forward peaks.
Every function must return a same-length pandas Series with no exception even
when all insider series inputs are zero.

Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_HALF  = 126
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _drawdown_from_expanding_high(close: pd.Series) -> pd.Series:
    """Price drawdown from expanding (all-history) high; always <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _drawdown_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    """Price drawdown from rolling w-day high; always <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Insider shares vs drawdown depth ---

def itm_076_buy_shares_21d(insider_buy_shares: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider buy shares."""
    return _rolling_sum(insider_buy_shares, _TD_MON)


def itm_077_buy_shares_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider buy shares."""
    return _rolling_sum(insider_buy_shares, _TD_QTR)


def itm_078_buy_shares_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider buy shares."""
    return _rolling_sum(insider_buy_shares, _TD_YEAR)


def itm_079_buy_shares_x_ath_dd_63d(
    close: pd.Series, insider_buy_shares: pd.Series
) -> pd.Series:
    """63d buy shares (log1p) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    sh63    = _rolling_sum(insider_buy_shares, _TD_QTR)
    log_sh  = np.log1p(sh63.clip(lower=0))
    return log_sh * dd_mag


def itm_080_buy_shares_x_1y_dd_63d(
    close: pd.Series, insider_buy_shares: pd.Series
) -> pd.Series:
    """63d buy shares (log1p) times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    sh63   = _rolling_sum(insider_buy_shares, _TD_QTR)
    log_sh = np.log1p(sh63.clip(lower=0))
    return log_sh * dd_mag


def itm_081_sell_shares_63d(insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider sell shares."""
    return _rolling_sum(insider_sell_shares, _TD_QTR)


def itm_082_net_shares_63d(
    insider_buy_shares: pd.Series, insider_sell_shares: pd.Series
) -> pd.Series:
    """63-day net insider share flow (buy minus sell)."""
    return _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)


def itm_083_buy_shares_fraction_held_63d(
    insider_buy_shares: pd.Series, insider_shares_held: pd.Series
) -> pd.Series:
    """63d buy shares as fraction of trailing insider shares held."""
    sh63   = _rolling_sum(insider_buy_shares, _TD_QTR)
    held63 = _rolling_mean(insider_shares_held, _TD_QTR)
    return _safe_div(sh63, held63)


def itm_084_buy_shares_fraction_held_252d(
    insider_buy_shares: pd.Series, insider_shares_held: pd.Series
) -> pd.Series:
    """252d buy shares as fraction of trailing insider shares held."""
    sh252  = _rolling_sum(insider_buy_shares, _TD_YEAR)
    held252 = _rolling_mean(insider_shares_held, _TD_YEAR)
    return _safe_div(sh252, held252)


def itm_085_buy_avg_price_63d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Implied average insider buy price over 63 days (total value / total shares)."""
    val63 = _rolling_sum(insider_buy_value, _TD_QTR)
    sh63  = _rolling_sum(insider_buy_shares, _TD_QTR)
    return _safe_div(val63, sh63)


def itm_086_buy_avg_price_vs_current_close_63d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Ratio of current close to implied 63d insider avg buy price.
    < 1 means stock is now below where insiders last bought."""
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    sh63    = _rolling_sum(insider_buy_shares, _TD_QTR)
    avg_px  = _safe_div(val63, sh63)
    return _safe_div(close, avg_px)


def itm_087_buy_avg_price_vs_1y_high_63d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Implied 63d avg insider buy price as fraction of 1-year high.
    Low = insiders paid near the bottom."""
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    sh63    = _rolling_sum(insider_buy_shares, _TD_QTR)
    avg_px  = _safe_div(val63, sh63)
    hi_1y   = _rolling_max(close, _TD_YEAR)
    return _safe_div(avg_px, hi_1y)


def itm_088_buy_avg_price_vs_ath_63d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Implied 63d avg insider buy price as fraction of ATH."""
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    sh63    = _rolling_sum(insider_buy_shares, _TD_QTR)
    avg_px  = _safe_div(val63, sh63)
    ath     = close.expanding(min_periods=1).max()
    return _safe_div(avg_px, ath)


def itm_089_sell_shares_x_ath_dd_63d(
    close: pd.Series, insider_sell_shares: pd.Series
) -> pd.Series:
    """63d sell shares (log1p) times ATH drawdown magnitude (selling into decline)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ss63    = _rolling_sum(insider_sell_shares, _TD_QTR)
    log_ss  = np.log1p(ss63.clip(lower=0))
    return log_ss * dd_mag


def itm_090_net_shares_x_ath_dd_63d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_sell_shares: pd.Series
) -> pd.Series:
    """63d net shares (buy-sell) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    net_sh  = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return net_sh * dd_mag


# --- Group G (091-105): CEO/CFO specific timing features ---

def itm_091_ceo_buy_value_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day sum of CEO insider buy value."""
    return _rolling_sum(ceo_buy_value, _TD_QTR)


def itm_092_cfo_buy_value_63d(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day sum of CFO insider buy value."""
    return _rolling_sum(cfo_buy_value, _TD_QTR)


def itm_093_ceo_buy_value_x_ath_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d CEO buy value (log1p) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    cv63    = _rolling_sum(ceo_buy_value, _TD_QTR)
    log_v   = np.log1p(cv63.clip(lower=0))
    return log_v * dd_mag


def itm_094_cfo_buy_value_x_ath_dd_63d(
    close: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """63d CFO buy value (log1p) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    cv63    = _rolling_sum(cfo_buy_value, _TD_QTR)
    log_v   = np.log1p(cv63.clip(lower=0))
    return log_v * dd_mag


def itm_095_ceo_buy_in_50pct_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d CEO buy value while stock is >=50% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    cv_deep = ceo_buy_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(cv_deep, _TD_QTR)


def itm_096_cfo_buy_in_50pct_dd_63d(
    close: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """63d CFO buy value while stock is >=50% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    cv_deep = cfo_buy_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(cv_deep, _TD_QTR)


def itm_097_ceo_buy_fraction_of_total_63d(
    insider_buy_value: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """CEO buy value as fraction of total insider buy value (63d)."""
    tot63 = _rolling_sum(insider_buy_value, _TD_QTR)
    ceo63 = _rolling_sum(ceo_buy_value, _TD_QTR)
    return _safe_div(ceo63, tot63)


def itm_098_cfo_buy_fraction_of_total_63d(
    insider_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """CFO buy value as fraction of total insider buy value (63d)."""
    tot63 = _rolling_sum(insider_buy_value, _TD_QTR)
    cfo63 = _rolling_sum(cfo_buy_value, _TD_QTR)
    return _safe_div(cfo63, tot63)


def itm_099_ceo_cfo_combined_buy_63d(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """63-day sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)


def itm_100_ceo_cfo_buy_x_ath_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """63d combined CEO+CFO buy value (log1p) times ATH drawdown magnitude."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    combined = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    log_v    = np.log1p(combined.clip(lower=0))
    return log_v * dd_mag


def itm_101_officer_buy_value_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of officer-level insider buy value."""
    return _rolling_sum(officer_buy_value, _TD_YEAR)


def itm_102_officer_buy_x_ath_dd_252d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """252d officer buy value (log1p) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov252   = _rolling_sum(officer_buy_value, _TD_YEAR)
    log_v   = np.log1p(ov252.clip(lower=0))
    return log_v * dd_mag


def itm_103_officer_buy_in_70pct_dd_63d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63d officer buy value while stock is >=70% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    ov_deep = officer_buy_value.where(dd <= -0.70, other=0.0)
    return _rolling_sum(ov_deep, _TD_QTR)


def itm_104_ceo_buy_in_70pct_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d CEO buy value while stock is >=70% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    cv_deep = ceo_buy_value.where(dd <= -0.70, other=0.0)
    return _rolling_sum(cv_deep, _TD_QTR)


def itm_105_senior_officer_timing_composite_63d(
    close: pd.Series, officer_buy_value: pd.Series,
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """Composite: log(officer63d) + log(ceo63d) + log(cfo63d) * ATH DD magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov63    = np.log1p(_rolling_sum(officer_buy_value, _TD_QTR).clip(lower=0))
    ceo63   = np.log1p(_rolling_sum(ceo_buy_value, _TD_QTR).clip(lower=0))
    cfo63   = np.log1p(_rolling_sum(cfo_buy_value, _TD_QTR).clip(lower=0))
    return (ov63 + ceo63 + cfo63) * dd_mag


# --- Group H (106-120): Drawdown acceleration and insider response ---

def itm_106_dd_acceleration_21d(close: pd.Series) -> pd.Series:
    """Second difference of 1-year drawdown over 21-day steps: measures acceleration."""
    dd = _drawdown_from_rolling_high(close, _TD_YEAR)
    d1 = dd - dd.shift(_TD_MON)
    d2 = d1 - d1.shift(_TD_MON)
    return d2


def itm_107_dd_acceleration_63d(close: pd.Series) -> pd.Series:
    """Second difference of 1-year drawdown over 63-day steps."""
    dd = _drawdown_from_rolling_high(close, _TD_YEAR)
    d1 = dd - dd.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2


def itm_108_buy_count_during_dd_acceleration(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d insider buy count on days where drawdown is accelerating (worsening)."""
    dd   = _drawdown_from_rolling_high(close, _TD_YEAR)
    accel = (dd < dd.shift(1)).astype(float)
    return _rolling_sum(insider_buy_count * accel, _TD_MON)


def itm_109_buy_value_during_dd_acceleration_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d insider buy value on days where drawdown is worsening day-over-day."""
    dd    = _drawdown_from_rolling_high(close, _TD_YEAR)
    accel = (dd < dd.shift(1)).astype(float)
    return _rolling_sum(insider_buy_value * accel, _TD_QTR)


def itm_110_dd_rate_of_change_21d(close: pd.Series) -> pd.Series:
    """21-day change in ATH drawdown (how fast the drawdown is deepening)."""
    dd = _drawdown_from_expanding_high(close)
    return dd - dd.shift(_TD_MON)


def itm_111_buy_count_x_dd_rate_21d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d insider buy count times absolute 21d drawdown rate of change."""
    roc    = (dd := _drawdown_from_expanding_high(close)) - dd.shift(_TD_MON)
    buy21  = _rolling_sum(insider_buy_count, _TD_MON)
    return buy21 * roc.abs()


def itm_112_dd_velocity_63d(close: pd.Series) -> pd.Series:
    """63-day change in ATH drawdown depth."""
    dd = _drawdown_from_expanding_high(close)
    return dd - dd.shift(_TD_QTR)


def itm_113_buy_count_x_dd_velocity_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63d buy count times absolute 63d ATH drawdown velocity."""
    dd   = _drawdown_from_expanding_high(close)
    vel  = (dd - dd.shift(_TD_QTR)).abs()
    buy63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return buy63 * vel


def itm_114_dd_new_low_streak(close: pd.Series) -> pd.Series:
    """Consecutive trading days where each day set a new 252d low (streak length)."""
    low252    = _rolling_min(close, _TD_YEAR)
    new_low   = (close == low252).astype(int)
    arr       = new_low.values.copy()
    streak    = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=close.index)


def itm_115_buy_during_new_low_streak_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63d insider buy count on days within an active 252d new-low streak."""
    low252  = _rolling_min(close, _TD_YEAR)
    new_low = (close == low252).astype(float)
    return _rolling_sum(insider_buy_count * new_low, _TD_QTR)


def itm_116_buy_value_during_new_low_streak_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d insider buy value on days that set a new 252d low."""
    low252  = _rolling_min(close, _TD_YEAR)
    new_low = (close == low252).astype(float)
    return _rolling_sum(insider_buy_value * new_low, _TD_QTR)


def itm_117_dd_depth_percentile_1y(close: pd.Series) -> pd.Series:
    """Percentile rank of current ATH drawdown within trailing 252-day window."""
    dd = _drawdown_from_expanding_high(close)
    return _rolling_rank_pct(dd, _TD_YEAR)


def itm_118_dd_depth_percentile_3y(close: pd.Series) -> pd.Series:
    """Percentile rank of current ATH drawdown within trailing 756-day window."""
    dd = _drawdown_from_expanding_high(close)
    return _rolling_rank_pct(dd, _TD_3Y)


def itm_119_buy_count_x_dd_percentile_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63d buy count times ATH drawdown 252d percentile (inverted so deep=high)."""
    dd     = _drawdown_from_expanding_high(close)
    pct    = 1.0 - _rolling_rank_pct(dd, _TD_YEAR).fillna(0.5)
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    return buy63 * pct


def itm_120_buy_value_x_dd_percentile_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log1p) times ATH drawdown 252d severity percentile (inverted)."""
    dd      = _drawdown_from_expanding_high(close)
    pct     = 1.0 - _rolling_rank_pct(dd, _TD_YEAR).fillna(0.5)
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_v   = np.log1p(buy_val.clip(lower=0))
    return log_v * pct


# --- Group I (121-135): Multi-window buy accumulation and net sentiment ---

def itm_121_buy_count_5d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 5-day (1-week) sum of insider buy count."""
    return _rolling_sum(insider_buy_count, _TD_WEEK)


def itm_122_buy_value_5d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 5-day (1-week) sum of insider buy value."""
    return _rolling_sum(insider_buy_value, _TD_WEEK)


def itm_123_buy_count_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 126-day (half-year) sum of insider buy count."""
    return _rolling_sum(insider_buy_count, _TD_HALF)


def itm_124_buy_value_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 126-day sum of insider buy value."""
    return _rolling_sum(insider_buy_value, _TD_HALF)


def itm_125_buy_count_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 504-day (2-year) sum of insider buy count."""
    return _rolling_sum(insider_buy_count, _TD_2Y)


def itm_126_buy_value_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 504-day sum of insider buy value."""
    return _rolling_sum(insider_buy_value, _TD_2Y)


def itm_127_buy_count_ratio_21d_to_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21d to 252d buy count (recent vs long-term pace)."""
    buy21  = _rolling_sum(insider_buy_count, _TD_MON)
    buy252 = _rolling_sum(insider_buy_count, _TD_YEAR)
    return _safe_div(buy21 * (_TD_YEAR / _TD_MON), buy252)


def itm_128_buy_value_ratio_21d_to_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of annualized 21d buy value pace to 252d buy value."""
    val21  = _rolling_sum(insider_buy_value, _TD_MON)
    val252 = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(val21 * (_TD_YEAR / _TD_MON), val252)


def itm_129_buy_count_ratio_63d_to_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of annualized 63d buy count pace to 504d buy count."""
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    buy504 = _rolling_sum(insider_buy_count, _TD_2Y)
    return _safe_div(buy63 * (_TD_2Y / _TD_QTR), buy504)


def itm_130_buy_value_ewm_63(insider_buy_value: pd.Series) -> pd.Series:
    """Exponentially weighted mean of insider buy value with span=63."""
    return _ewm_mean(insider_buy_value, _TD_QTR)


def itm_131_buy_count_ewm_63(insider_buy_count: pd.Series) -> pd.Series:
    """Exponentially weighted mean of insider buy count with span=63."""
    return _ewm_mean(insider_buy_count, _TD_QTR)


def itm_132_buyers_21d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 21-day sum of unique insider buyer count."""
    return _rolling_sum(insider_buyers, _TD_MON)


def itm_133_buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 63-day sum of unique insider buyer count."""
    return _rolling_sum(insider_buyers, _TD_MON)


def itm_134_buyers_252d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 252-day sum of unique insider buyer count."""
    return _rolling_sum(insider_buyers, _TD_YEAR)


def itm_135_buy_to_sell_count_ratio_63d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """63d insider buy count divided by sell count."""
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    sell63 = _rolling_sum(insider_sell_count, _TD_QTR)
    return _safe_div(buy63, sell63)


# --- Group J (136-150): Composite, cross-signal, and advanced timing features ---

def itm_136_buy_value_x_ath_dd_x_1y_dd_product_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log1p) times ATH DD magnitude times 1y DD magnitude (triple product)."""
    ath_dd = _drawdown_from_expanding_high(close).abs()
    d1y    = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    buy_v  = _rolling_sum(insider_buy_value, _TD_QTR)
    log_v  = np.log1p(buy_v.clip(lower=0))
    return log_v * ath_dd * d1y


def itm_137_buy_value_x_log_ath_dd_x_officers_63d(
    close: pd.Series, insider_buy_value: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """Composite: 63d total buy (log1p) * log(1+ATH DD) * officer fraction."""
    ath_dd   = _drawdown_from_expanding_high(close).abs()
    log_dd   = np.log1p(ath_dd)
    tot63    = _rolling_sum(insider_buy_value, _TD_QTR)
    off63    = _rolling_sum(officer_buy_value, _TD_QTR)
    off_frac = _safe_div(off63, tot63.replace(0, np.nan)).fillna(0.0)
    log_v    = np.log1p(tot63.clip(lower=0))
    return log_v * log_dd * (1.0 + off_frac)


def itm_138_buy_intensity_vs_prior_year_pace_63d(
    insider_buy_count: pd.Series
) -> pd.Series:
    """Current 63d buy count minus trailing 252d mean of 63d rolling buy count."""
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    avg63  = _rolling_mean(buy63, _TD_YEAR)
    return buy63 - avg63


def itm_139_buy_value_intensity_vs_prior_year_pace_63d(
    insider_buy_value: pd.Series
) -> pd.Series:
    """Current 63d buy value minus trailing 252d mean of 63d rolling buy value."""
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    avg63  = _rolling_mean(val63, _TD_YEAR)
    return val63 - avg63


def itm_140_buy_count_z_x_ath_dd_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Z-score of 63d buy count (252d window) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    z      = _zscore_rolling(buy63, _TD_YEAR)
    return z * dd_mag


def itm_141_buy_value_z_x_ath_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Z-score of 63d buy value (252d window) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    z       = _zscore_rolling(val63, _TD_YEAR)
    return z * dd_mag


def itm_142_buy_value_pct_rank_x_ath_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Percentile rank of 63d buy value (252d window) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    pct     = _rolling_rank_pct(val63, _TD_YEAR).fillna(0.0)
    return pct * dd_mag


def itm_143_net_buy_value_x_ath_dd_252d(
    close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """252d net buy value times ATH drawdown magnitude."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    net252   = _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)
    return net252 * dd_mag


def itm_144_buy_value_consistency_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of days in 63d window with nonzero insider buy value."""
    nonzero = (insider_buy_value > 0).astype(float)
    return _rolling_mean(nonzero, _TD_QTR)


def itm_145_buy_value_consistency_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of days in 252d window with nonzero insider buy value."""
    nonzero = (insider_buy_value > 0).astype(float)
    return _rolling_mean(nonzero, _TD_YEAR)


def itm_146_buy_event_density_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per trading day over 63 days."""
    return _rolling_mean(insider_buy_count, _TD_QTR)


def itm_147_buy_event_density_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per trading day over 252 days."""
    return _rolling_mean(insider_buy_count, _TD_YEAR)


def itm_148_dd_below_50pct_duration_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where ATH drawdown was >= 50%."""
    dd     = _drawdown_from_expanding_high(close)
    deep   = (dd <= -0.50).astype(float)
    return _rolling_mean(deep, _TD_YEAR)


def itm_149_dd_below_70pct_duration_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where ATH drawdown was >= 70%."""
    dd   = _drawdown_from_expanding_high(close)
    deep = (dd <= -0.70).astype(float)
    return _rolling_mean(deep, _TD_YEAR)


def itm_150_grand_composite_timing_score(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, officer_buy_value: pd.Series,
    insider_buyers: pd.Series
) -> pd.Series:
    """Grand composite: equal-weight z-scores of four deep-dd buy signals
    (value x ATH-dd, count x ATH-dd, officer x ATH-dd, buyers x ATH-dd)
    normalized over 252d window."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = np.log1p(_rolling_sum(officer_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s4 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    z1 = _zscore_rolling(s1, _TD_YEAR)
    z2 = _zscore_rolling(s2, _TD_YEAR)
    z3 = _zscore_rolling(s3, _TD_YEAR)
    z4 = _zscore_rolling(s4, _TD_YEAR)
    return (z1 + z2 + z3 + z4) / 4.0


# ── Feature functions 176-200 ─────────────────────────────────────────────────

# --- Group K (176-190): Shares-held ratios, sell intensity, and cross-window composites ---

def itm_176_shares_held_mean_252d(insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 252-day mean of insider shares held."""
    return _rolling_mean(insider_shares_held, _TD_YEAR)


def itm_177_shares_held_pct_rank_252d(insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of insider shares held within trailing 252-day window."""
    return _rolling_rank_pct(insider_shares_held, _TD_YEAR)


def itm_178_sell_shares_x_ath_dd_252d(
    close: pd.Series, insider_sell_shares: pd.Series
) -> pd.Series:
    """252d sell shares (log1p) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ss252  = _rolling_sum(insider_sell_shares, _TD_YEAR)
    return np.log1p(ss252.clip(lower=0)) * dd_mag


def itm_179_net_shares_x_ath_dd_252d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_sell_shares: pd.Series
) -> pd.Series:
    """252d net shares (buy-sell) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    net252 = _rolling_sum(insider_buy_shares, _TD_YEAR) - _rolling_sum(insider_sell_shares, _TD_YEAR)
    return net252 * dd_mag


def itm_180_buy_shares_x_2y_dd_63d(
    close: pd.Series, insider_buy_shares: pd.Series
) -> pd.Series:
    """63d buy shares (log1p) times 2-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    sh63   = _rolling_sum(insider_buy_shares, _TD_QTR)
    return np.log1p(sh63.clip(lower=0)) * dd_mag


def itm_181_buy_avg_price_vs_ath_252d(
    close: pd.Series, insider_buy_shares: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Implied 252d avg insider buy price as fraction of ATH."""
    val252  = _rolling_sum(insider_buy_value, _TD_YEAR)
    sh252   = _rolling_sum(insider_buy_shares, _TD_YEAR)
    avg_px  = _safe_div(val252, sh252)
    ath     = close.expanding(min_periods=1).max()
    return _safe_div(avg_px, ath)


def itm_182_sell_count_x_ath_dd_63d(
    close: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """63d sell count times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    sc63    = _rolling_sum(insider_sell_count, _TD_QTR)
    return sc63 * dd_mag


def itm_183_ceo_buy_value_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of CEO insider buy value."""
    return _rolling_sum(ceo_buy_value, _TD_YEAR)


def itm_184_cfo_buy_value_252d(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of CFO insider buy value."""
    return _rolling_sum(cfo_buy_value, _TD_YEAR)


def itm_185_ceo_buy_x_1y_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d CEO buy value (log1p) times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    cv63   = _rolling_sum(ceo_buy_value, _TD_QTR)
    return np.log1p(cv63.clip(lower=0)) * dd_mag


def itm_186_cfo_buy_x_1y_dd_63d(
    close: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """63d CFO buy value (log1p) times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    cv63   = _rolling_sum(cfo_buy_value, _TD_QTR)
    return np.log1p(cv63.clip(lower=0)) * dd_mag


def itm_187_ceo_buy_in_90pct_dd_63d(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d CEO buy value while stock is >=90% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    cv_deep = ceo_buy_value.where(dd <= -0.90, other=0.0)
    return _rolling_sum(cv_deep, _TD_QTR)


def itm_188_officer_buy_in_90pct_dd_252d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """252d officer buy value while stock is >=90% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    ov_deep = officer_buy_value.where(dd <= -0.90, other=0.0)
    return _rolling_sum(ov_deep, _TD_YEAR)


def itm_189_buy_shares_fraction_held_126d(
    insider_buy_shares: pd.Series, insider_shares_held: pd.Series
) -> pd.Series:
    """126d buy shares as fraction of 126d mean insider shares held."""
    sh126   = _rolling_sum(insider_buy_shares, _TD_HALF)
    held126 = _rolling_mean(insider_shares_held, _TD_HALF)
    return _safe_div(sh126, held126)


def itm_190_ceo_cfo_combined_buy_252d(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """252-day sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)


# --- Group L (191-200): Dd-duration, sell-buy dynamics, and composites ---

def itm_191_dd_below_90pct_duration_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where ATH drawdown was >= 90%."""
    dd   = _drawdown_from_expanding_high(close)
    deep = (dd <= -0.90).astype(float)
    return _rolling_mean(deep, _TD_YEAR)


def itm_192_buy_count_in_deep_dd_fraction_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Fraction of 252d insider buy days that occurred >=50% below ATH."""
    dd       = _drawdown_from_expanding_high(close)
    deep_buy = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    all_buy  = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(deep_buy, _TD_YEAR), _rolling_sum(all_buy, _TD_YEAR))


def itm_193_sell_value_zscore_252d(insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily insider sell value within trailing 252-day window."""
    return _zscore_rolling(insider_sell_value, _TD_YEAR)


def itm_194_sell_count_x_1y_dd_63d(
    close: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """63d sell count times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    sc63   = _rolling_sum(insider_sell_count, _TD_QTR)
    return sc63 * dd_mag


def itm_195_net_buy_value_126d(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """126-day net insider buy value (buy minus sell)."""
    return _rolling_sum(insider_buy_value, _TD_HALF) - _rolling_sum(insider_sell_value, _TD_HALF)


def itm_196_buy_value_vs_sell_value_ratio_252d(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """252d insider buy value divided by sell value."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_YEAR), _rolling_sum(insider_sell_value, _TD_YEAR))


def itm_197_dd_below_50pct_buy_density_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Average daily buy count on days where ATH DD >= 50%, over 252d window."""
    dd      = _drawdown_from_expanding_high(close)
    deep    = (dd <= -0.50).astype(float)
    buy_cnt = insider_buy_count * deep
    n_deep  = _rolling_sum(deep, _TD_YEAR).replace(0, np.nan)
    return _safe_div(_rolling_sum(buy_cnt, _TD_YEAR), n_deep)


def itm_198_senior_buy_vs_total_fraction_252d(
    insider_buy_value: pd.Series, officer_buy_value: pd.Series,
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series
) -> pd.Series:
    """(Officer+CEO+CFO) 252d buy value fraction of total 252d insider buy value."""
    senior = _rolling_sum(officer_buy_value + ceo_buy_value + cfo_buy_value, _TD_YEAR)
    total  = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(senior, total)


def itm_199_buy_value_x_dd_duration_score(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log1p) times fraction of 252d days in ATH DD >= 50%
    (persistence-weighted conviction)."""
    dd      = _drawdown_from_expanding_high(close)
    dur_frac = _rolling_mean((dd <= -0.50).astype(float), _TD_YEAR)
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    return np.log1p(buy_val.clip(lower=0)) * dur_frac


def itm_200_ultimate_timing_composite(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, officer_buy_value: pd.Series,
    insider_buyers: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """Ultimate composite: z-scores of five deep-dd buy signals including CEO,
    all normalized over 252d window — equal-weight average."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = np.log1p(_rolling_sum(officer_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s4 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    s5 = np.log1p(_rolling_sum(ceo_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    scores = [_zscore_rolling(s, _TD_YEAR) for s in (s1, s2, s3, s4, s5)]
    return sum(scores) / 5.0


# ── Registry 076-150 ─────────────────────────────────────────────────────────

INSIDER_TIMING_REGISTRY_076_150 = {
    "itm_076_buy_shares_21d":                              {"inputs": ["insider_buy_shares"],                                                   "func": itm_076_buy_shares_21d},
    "itm_077_buy_shares_63d":                              {"inputs": ["insider_buy_shares"],                                                   "func": itm_077_buy_shares_63d},
    "itm_078_buy_shares_252d":                             {"inputs": ["insider_buy_shares"],                                                   "func": itm_078_buy_shares_252d},
    "itm_079_buy_shares_x_ath_dd_63d":                    {"inputs": ["close", "insider_buy_shares"],                                          "func": itm_079_buy_shares_x_ath_dd_63d},
    "itm_080_buy_shares_x_1y_dd_63d":                     {"inputs": ["close", "insider_buy_shares"],                                          "func": itm_080_buy_shares_x_1y_dd_63d},
    "itm_081_sell_shares_63d":                             {"inputs": ["insider_sell_shares"],                                                  "func": itm_081_sell_shares_63d},
    "itm_082_net_shares_63d":                              {"inputs": ["insider_buy_shares", "insider_sell_shares"],                            "func": itm_082_net_shares_63d},
    "itm_083_buy_shares_fraction_held_63d":               {"inputs": ["insider_buy_shares", "insider_shares_held"],                            "func": itm_083_buy_shares_fraction_held_63d},
    "itm_084_buy_shares_fraction_held_252d":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                            "func": itm_084_buy_shares_fraction_held_252d},
    "itm_085_buy_avg_price_63d":                           {"inputs": ["close", "insider_buy_shares", "insider_buy_value"],                     "func": itm_085_buy_avg_price_63d},
    "itm_086_buy_avg_price_vs_current_close_63d":         {"inputs": ["close", "insider_buy_shares", "insider_buy_value"],                     "func": itm_086_buy_avg_price_vs_current_close_63d},
    "itm_087_buy_avg_price_vs_1y_high_63d":               {"inputs": ["close", "insider_buy_shares", "insider_buy_value"],                     "func": itm_087_buy_avg_price_vs_1y_high_63d},
    "itm_088_buy_avg_price_vs_ath_63d":                   {"inputs": ["close", "insider_buy_shares", "insider_buy_value"],                     "func": itm_088_buy_avg_price_vs_ath_63d},
    "itm_089_sell_shares_x_ath_dd_63d":                   {"inputs": ["close", "insider_sell_shares"],                                         "func": itm_089_sell_shares_x_ath_dd_63d},
    "itm_090_net_shares_x_ath_dd_63d":                    {"inputs": ["close", "insider_buy_shares", "insider_sell_shares"],                   "func": itm_090_net_shares_x_ath_dd_63d},
    "itm_091_ceo_buy_value_63d":                           {"inputs": ["ceo_buy_value"],                                                        "func": itm_091_ceo_buy_value_63d},
    "itm_092_cfo_buy_value_63d":                           {"inputs": ["cfo_buy_value"],                                                        "func": itm_092_cfo_buy_value_63d},
    "itm_093_ceo_buy_value_x_ath_dd_63d":                 {"inputs": ["close", "ceo_buy_value"],                                               "func": itm_093_ceo_buy_value_x_ath_dd_63d},
    "itm_094_cfo_buy_value_x_ath_dd_63d":                 {"inputs": ["close", "cfo_buy_value"],                                               "func": itm_094_cfo_buy_value_x_ath_dd_63d},
    "itm_095_ceo_buy_in_50pct_dd_63d":                    {"inputs": ["close", "ceo_buy_value"],                                               "func": itm_095_ceo_buy_in_50pct_dd_63d},
    "itm_096_cfo_buy_in_50pct_dd_63d":                    {"inputs": ["close", "cfo_buy_value"],                                               "func": itm_096_cfo_buy_in_50pct_dd_63d},
    "itm_097_ceo_buy_fraction_of_total_63d":              {"inputs": ["insider_buy_value", "ceo_buy_value"],                                   "func": itm_097_ceo_buy_fraction_of_total_63d},
    "itm_098_cfo_buy_fraction_of_total_63d":              {"inputs": ["insider_buy_value", "cfo_buy_value"],                                   "func": itm_098_cfo_buy_fraction_of_total_63d},
    "itm_099_ceo_cfo_combined_buy_63d":                   {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                       "func": itm_099_ceo_cfo_combined_buy_63d},
    "itm_100_ceo_cfo_buy_x_ath_dd_63d":                   {"inputs": ["close", "ceo_buy_value", "cfo_buy_value"],                              "func": itm_100_ceo_cfo_buy_x_ath_dd_63d},
    "itm_101_officer_buy_value_252d":                     {"inputs": ["officer_buy_value"],                                                    "func": itm_101_officer_buy_value_252d},
    "itm_102_officer_buy_x_ath_dd_252d":                  {"inputs": ["close", "officer_buy_value"],                                           "func": itm_102_officer_buy_x_ath_dd_252d},
    "itm_103_officer_buy_in_70pct_dd_63d":                {"inputs": ["close", "officer_buy_value"],                                           "func": itm_103_officer_buy_in_70pct_dd_63d},
    "itm_104_ceo_buy_in_70pct_dd_63d":                    {"inputs": ["close", "ceo_buy_value"],                                               "func": itm_104_ceo_buy_in_70pct_dd_63d},
    "itm_105_senior_officer_timing_composite_63d":        {"inputs": ["close", "officer_buy_value", "ceo_buy_value", "cfo_buy_value"],         "func": itm_105_senior_officer_timing_composite_63d},
    "itm_106_dd_acceleration_21d":                        {"inputs": ["close"],                                                                "func": itm_106_dd_acceleration_21d},
    "itm_107_dd_acceleration_63d":                        {"inputs": ["close"],                                                                "func": itm_107_dd_acceleration_63d},
    "itm_108_buy_count_during_dd_acceleration":           {"inputs": ["close", "insider_buy_count"],                                           "func": itm_108_buy_count_during_dd_acceleration},
    "itm_109_buy_value_during_dd_acceleration_63d":       {"inputs": ["close", "insider_buy_value"],                                           "func": itm_109_buy_value_during_dd_acceleration_63d},
    "itm_110_dd_rate_of_change_21d":                      {"inputs": ["close"],                                                                "func": itm_110_dd_rate_of_change_21d},
    "itm_111_buy_count_x_dd_rate_21d":                    {"inputs": ["close", "insider_buy_count"],                                           "func": itm_111_buy_count_x_dd_rate_21d},
    "itm_112_dd_velocity_63d":                            {"inputs": ["close"],                                                                "func": itm_112_dd_velocity_63d},
    "itm_113_buy_count_x_dd_velocity_63d":                {"inputs": ["close", "insider_buy_count"],                                           "func": itm_113_buy_count_x_dd_velocity_63d},
    "itm_114_dd_new_low_streak":                          {"inputs": ["close"],                                                                "func": itm_114_dd_new_low_streak},
    "itm_115_buy_during_new_low_streak_63d":              {"inputs": ["close", "insider_buy_count"],                                           "func": itm_115_buy_during_new_low_streak_63d},
    "itm_116_buy_value_during_new_low_streak_63d":        {"inputs": ["close", "insider_buy_value"],                                           "func": itm_116_buy_value_during_new_low_streak_63d},
    "itm_117_dd_depth_percentile_1y":                     {"inputs": ["close"],                                                                "func": itm_117_dd_depth_percentile_1y},
    "itm_118_dd_depth_percentile_3y":                     {"inputs": ["close"],                                                                "func": itm_118_dd_depth_percentile_3y},
    "itm_119_buy_count_x_dd_percentile_63d":              {"inputs": ["close", "insider_buy_count"],                                           "func": itm_119_buy_count_x_dd_percentile_63d},
    "itm_120_buy_value_x_dd_percentile_63d":              {"inputs": ["close", "insider_buy_value"],                                           "func": itm_120_buy_value_x_dd_percentile_63d},
    "itm_121_buy_count_5d":                               {"inputs": ["insider_buy_count"],                                                    "func": itm_121_buy_count_5d},
    "itm_122_buy_value_5d":                               {"inputs": ["insider_buy_value"],                                                    "func": itm_122_buy_value_5d},
    "itm_123_buy_count_126d":                             {"inputs": ["insider_buy_count"],                                                    "func": itm_123_buy_count_126d},
    "itm_124_buy_value_126d":                             {"inputs": ["insider_buy_value"],                                                    "func": itm_124_buy_value_126d},
    "itm_125_buy_count_504d":                             {"inputs": ["insider_buy_count"],                                                    "func": itm_125_buy_count_504d},
    "itm_126_buy_value_504d":                             {"inputs": ["insider_buy_value"],                                                    "func": itm_126_buy_value_504d},
    "itm_127_buy_count_ratio_21d_to_252d":                {"inputs": ["insider_buy_count"],                                                    "func": itm_127_buy_count_ratio_21d_to_252d},
    "itm_128_buy_value_ratio_21d_to_252d":                {"inputs": ["insider_buy_value"],                                                    "func": itm_128_buy_value_ratio_21d_to_252d},
    "itm_129_buy_count_ratio_63d_to_504d":                {"inputs": ["insider_buy_count"],                                                    "func": itm_129_buy_count_ratio_63d_to_504d},
    "itm_130_buy_value_ewm_63":                           {"inputs": ["insider_buy_value"],                                                    "func": itm_130_buy_value_ewm_63},
    "itm_131_buy_count_ewm_63":                           {"inputs": ["insider_buy_count"],                                                    "func": itm_131_buy_count_ewm_63},
    "itm_132_buyers_21d":                                 {"inputs": ["insider_buyers"],                                                       "func": itm_132_buyers_21d},
    "itm_133_buyers_63d":                                 {"inputs": ["insider_buyers"],                                                       "func": itm_133_buyers_63d},
    "itm_134_buyers_252d":                                {"inputs": ["insider_buyers"],                                                       "func": itm_134_buyers_252d},
    "itm_135_buy_to_sell_count_ratio_63d":                {"inputs": ["insider_buy_count", "insider_sell_count"],                              "func": itm_135_buy_to_sell_count_ratio_63d},
    "itm_136_buy_value_x_ath_dd_x_1y_dd_product_63d":    {"inputs": ["close", "insider_buy_value"],                                           "func": itm_136_buy_value_x_ath_dd_x_1y_dd_product_63d},
    "itm_137_buy_value_x_log_ath_dd_x_officers_63d":     {"inputs": ["close", "insider_buy_value", "officer_buy_value"],                      "func": itm_137_buy_value_x_log_ath_dd_x_officers_63d},
    "itm_138_buy_intensity_vs_prior_year_pace_63d":       {"inputs": ["insider_buy_count"],                                                    "func": itm_138_buy_intensity_vs_prior_year_pace_63d},
    "itm_139_buy_value_intensity_vs_prior_year_pace_63d": {"inputs": ["insider_buy_value"],                                                    "func": itm_139_buy_value_intensity_vs_prior_year_pace_63d},
    "itm_140_buy_count_z_x_ath_dd_63d":                   {"inputs": ["close", "insider_buy_count"],                                           "func": itm_140_buy_count_z_x_ath_dd_63d},
    "itm_141_buy_value_z_x_ath_dd_63d":                   {"inputs": ["close", "insider_buy_value"],                                           "func": itm_141_buy_value_z_x_ath_dd_63d},
    "itm_142_buy_value_pct_rank_x_ath_dd_63d":            {"inputs": ["close", "insider_buy_value"],                                           "func": itm_142_buy_value_pct_rank_x_ath_dd_63d},
    "itm_143_net_buy_value_x_ath_dd_252d":                {"inputs": ["close", "insider_buy_value", "insider_sell_value"],                     "func": itm_143_net_buy_value_x_ath_dd_252d},
    "itm_144_buy_value_consistency_63d":                  {"inputs": ["insider_buy_value"],                                                    "func": itm_144_buy_value_consistency_63d},
    "itm_145_buy_value_consistency_252d":                 {"inputs": ["insider_buy_value"],                                                    "func": itm_145_buy_value_consistency_252d},
    "itm_146_buy_event_density_63d":                      {"inputs": ["insider_buy_count"],                                                    "func": itm_146_buy_event_density_63d},
    "itm_147_buy_event_density_252d":                     {"inputs": ["insider_buy_count"],                                                    "func": itm_147_buy_event_density_252d},
    "itm_148_dd_below_50pct_duration_252d":               {"inputs": ["close"],                                                                "func": itm_148_dd_below_50pct_duration_252d},
    "itm_149_dd_below_70pct_duration_252d":               {"inputs": ["close"],                                                                "func": itm_149_dd_below_70pct_duration_252d},
    "itm_150_grand_composite_timing_score":               {"inputs": ["close", "insider_buy_value", "insider_buy_count", "officer_buy_value", "insider_buyers"], "func": itm_150_grand_composite_timing_score},
    "itm_176_shares_held_mean_252d":                     {"inputs": ["insider_shares_held"],                                                            "func": itm_176_shares_held_mean_252d},
    "itm_177_shares_held_pct_rank_252d":                 {"inputs": ["insider_shares_held"],                                                            "func": itm_177_shares_held_pct_rank_252d},
    "itm_178_sell_shares_x_ath_dd_252d":                 {"inputs": ["close", "insider_sell_shares"],                                                   "func": itm_178_sell_shares_x_ath_dd_252d},
    "itm_179_net_shares_x_ath_dd_252d":                  {"inputs": ["close", "insider_buy_shares", "insider_sell_shares"],                             "func": itm_179_net_shares_x_ath_dd_252d},
    "itm_180_buy_shares_x_2y_dd_63d":                    {"inputs": ["close", "insider_buy_shares"],                                                    "func": itm_180_buy_shares_x_2y_dd_63d},
    "itm_181_buy_avg_price_vs_ath_252d":                 {"inputs": ["close", "insider_buy_shares", "insider_buy_value"],                               "func": itm_181_buy_avg_price_vs_ath_252d},
    "itm_182_sell_count_x_ath_dd_63d":                   {"inputs": ["close", "insider_sell_count"],                                                    "func": itm_182_sell_count_x_ath_dd_63d},
    "itm_183_ceo_buy_value_252d":                        {"inputs": ["ceo_buy_value"],                                                                  "func": itm_183_ceo_buy_value_252d},
    "itm_184_cfo_buy_value_252d":                        {"inputs": ["cfo_buy_value"],                                                                  "func": itm_184_cfo_buy_value_252d},
    "itm_185_ceo_buy_x_1y_dd_63d":                       {"inputs": ["close", "ceo_buy_value"],                                                         "func": itm_185_ceo_buy_x_1y_dd_63d},
    "itm_186_cfo_buy_x_1y_dd_63d":                       {"inputs": ["close", "cfo_buy_value"],                                                         "func": itm_186_cfo_buy_x_1y_dd_63d},
    "itm_187_ceo_buy_in_90pct_dd_63d":                   {"inputs": ["close", "ceo_buy_value"],                                                         "func": itm_187_ceo_buy_in_90pct_dd_63d},
    "itm_188_officer_buy_in_90pct_dd_252d":              {"inputs": ["close", "officer_buy_value"],                                                     "func": itm_188_officer_buy_in_90pct_dd_252d},
    "itm_189_buy_shares_fraction_held_126d":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                      "func": itm_189_buy_shares_fraction_held_126d},
    "itm_190_ceo_cfo_combined_buy_252d":                 {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                                 "func": itm_190_ceo_cfo_combined_buy_252d},
    "itm_191_dd_below_90pct_duration_252d":              {"inputs": ["close"],                                                                          "func": itm_191_dd_below_90pct_duration_252d},
    "itm_192_buy_count_in_deep_dd_fraction_252d":        {"inputs": ["close", "insider_buy_count"],                                                     "func": itm_192_buy_count_in_deep_dd_fraction_252d},
    "itm_193_sell_value_zscore_252d":                    {"inputs": ["insider_sell_value"],                                                             "func": itm_193_sell_value_zscore_252d},
    "itm_194_sell_count_x_1y_dd_63d":                    {"inputs": ["close", "insider_sell_count"],                                                    "func": itm_194_sell_count_x_1y_dd_63d},
    "itm_195_net_buy_value_126d":                         {"inputs": ["insider_buy_value", "insider_sell_value"],                                        "func": itm_195_net_buy_value_126d},
    "itm_196_buy_value_vs_sell_value_ratio_252d":        {"inputs": ["insider_buy_value", "insider_sell_value"],                                        "func": itm_196_buy_value_vs_sell_value_ratio_252d},
    "itm_197_dd_below_50pct_buy_density_252d":           {"inputs": ["close", "insider_buy_count"],                                                     "func": itm_197_dd_below_50pct_buy_density_252d},
    "itm_198_senior_buy_vs_total_fraction_252d":         {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value", "cfo_buy_value"],       "func": itm_198_senior_buy_vs_total_fraction_252d},
    "itm_199_buy_value_x_dd_duration_score":             {"inputs": ["close", "insider_buy_value"],                                                     "func": itm_199_buy_value_x_dd_duration_score},
    "itm_200_ultimate_timing_composite":                 {"inputs": ["close", "insider_buy_value", "insider_buy_count", "officer_buy_value", "insider_buyers", "ceo_buy_value"], "func": itm_200_ultimate_timing_composite},
}
