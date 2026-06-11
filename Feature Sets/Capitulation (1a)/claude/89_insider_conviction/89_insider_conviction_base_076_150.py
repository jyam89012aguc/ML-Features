"""
89_insider_conviction — Base Features 076-200
Domain: insider conviction — purchase size relative to existing insider stake
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records to one row per (ticker, date).

FLOW series (insider_buy_count, insider_sell_count, insider_buy_shares,
insider_sell_shares, insider_buy_value, insider_sell_value, insider_buyers,
insider_sellers, officer_buy_count, officer_buy_value, officer_sell_value,
director_buy_count, director_buy_value, director_sell_value, ceo_buy_value,
cfo_buy_value, tenpct_buy_count, tenpct_buy_value):
  EVENT-DRIVEN — most days are ZERO. Not forward-filled. Aggregate with
  trailing rolling SUMS over windows like 5/21/63/126/252 trading days.

STOCK series (insider_shares_held):
  CUMULATIVE total shares held by insiders following all transactions known
  as of each date. Persists/steps; treat as a LEVEL series. May be read
  directly or smoothed; do NOT sum it.

Trading-day calendar: 252/yr, 126/half-yr, 63/qtr, 21/mo, 5/wk.
All feature functions look strictly backward.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_2Y    = 504
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; returns NaN wherever denominator is zero or NaN.
    Deliberately returns NaN (not zero) when the prior stake is zero — a buy
    when there are zero prior shares is undefined in conviction-ratio terms."""
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

# --- Group G (076-090): Conviction ratio vs rolling baseline ---

def icn_076_buy_ratio_vs_1y_avg(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy conviction ratio minus its 1-year rolling mean.
    Captures whether current conviction is elevated vs. historical norm."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def icn_077_buy_ratio_vs_2y_avg(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy conviction ratio minus its 2-year rolling mean."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_2Y)


def icn_078_buy_ratio_vs_median_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy conviction ratio minus its 1-year rolling median."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return ratio - _rolling_median(ratio, _TD_YEAR)


def icn_079_buy_ratio_at_1y_max_flag(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if current monthly conviction ratio equals its 1-year rolling maximum."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    max_1y = _rolling_max(ratio, _TD_YEAR)
    return (ratio >= max_1y - _EPS).astype(float)


def icn_080_buy_ratio_drawdown_from_1y_peak(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Conviction ratio drawdown from its 1-year peak."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    max_1y = _rolling_max(ratio, _TD_YEAR)
    return ratio - max_1y


def icn_081_buy_value_ratio_vs_1y_avg(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy value / held ratio minus its 1-year rolling mean."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _TD_MO), insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def icn_082_net_conviction_ratio_vs_1y_avg(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly net-buy conviction ratio minus its 1-year rolling mean."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def icn_083_held_pct_growth_vs_1y_avg(insider_shares_held: pd.Series) -> pd.Series:
    """Monthly held growth % minus its 1-year rolling mean of monthly growth %."""
    pct = _safe_div(insider_shares_held - insider_shares_held.shift(_TD_MO), insider_shares_held.shift(_TD_MO))
    return pct - _rolling_mean(pct, _TD_YEAR)


def icn_084_conviction_ratio_ewm_vs_mean(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=63) of monthly conviction ratio minus rolling 1-year mean of ratio.
    Smoothed current conviction vs. long-run average."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    ewm = _ewm_mean(ratio, _TD_QTR)
    avg = _rolling_mean(ratio, _TD_YEAR)
    return ewm - avg


def icn_085_officer_conviction_vs_avg(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly officer conviction ratio minus its 1-year rolling mean."""
    ratio = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def icn_086_director_conviction_ratio_1y_zscore(director_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly director conviction ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(director_buy_value, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


def icn_087_ceo_conviction_ratio_1y_zscore(ceo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly CEO conviction ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(ceo_buy_value, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


def icn_088_held_growth_pct_rank_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of quarterly held_shares growth within trailing 1-year window."""
    growth = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    return _rolling_rank_pct(growth, _TD_YEAR)


def icn_089_net_conviction_pct_rank_1y(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of monthly net-buy conviction ratio within trailing 1-year window."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def icn_090_conviction_ratio_expanding_pct_rank(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Expanding percentile rank of monthly conviction ratio — all-history standing."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return ratio.expanding(min_periods=2).rank(pct=True)


# --- Group H (091-105): Proportional commitment and sell-adjusted conviction ---

def icn_091_buy_vs_sell_conviction_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy conviction ratio divided by sell conviction ratio.
    Values > 1 mean buying represents a larger fraction of held than selling does."""
    buy_ratio  = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    sell_ratio = _safe_div(_rolling_sum(insider_sell_shares, _TD_QTR), insider_shares_held)
    return _safe_div(buy_ratio, sell_ratio)


def icn_092_proportional_commitment_mo(insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """(buy_value - sell_value) / held shares — net dollar commitment per held share (monthly)."""
    net = _rolling_sum(insider_buy_value, _TD_MO) - _rolling_sum(insider_sell_value, _TD_MO)
    return _safe_div(net, insider_shares_held)


def icn_093_proportional_commitment_qtr(insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """(buy_value - sell_value) / held shares — net dollar commitment per held share (quarterly)."""
    net = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def icn_094_sell_conviction_ratio_mo(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly sell_shares / insider_shares_held — sell conviction (stake reduction rate)."""
    sells = _rolling_sum(insider_sell_shares, _TD_MO)
    return _safe_div(sells, insider_shares_held)


def icn_095_sell_conviction_ratio_qtr(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly sell_shares / insider_shares_held."""
    sells = _rolling_sum(insider_sell_shares, _TD_QTR)
    return _safe_div(sells, insider_shares_held)


def icn_096_buy_minus_sell_conviction_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly (buy_conviction_ratio - sell_conviction_ratio).
    Cleanly separates the two directions normalized by the same stake denominator."""
    buy_r  = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    sell_r = _safe_div(_rolling_sum(insider_sell_shares, _TD_MO), insider_shares_held)
    return buy_r - sell_r


def icn_097_buy_minus_sell_conviction_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly (buy_conviction_ratio - sell_conviction_ratio)."""
    buy_r  = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    sell_r = _safe_div(_rolling_sum(insider_sell_shares, _TD_QTR), insider_shares_held)
    return buy_r - sell_r


def icn_098_held_dilution_adjusted_buy_ratio_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Dilution-adjusted buy ratio: buy_conviction / (1 + sell_conviction), monthly.
    Penalizes simultaneous selling."""
    buy_r  = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    sell_r = _safe_div(_rolling_sum(insider_sell_shares, _TD_MO), insider_shares_held).fillna(0)
    return _safe_div(buy_r, 1.0 + sell_r)


def icn_099_tenpct_holder_net_conviction_qtr(tenpct_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """10%-holder quarterly buy conviction ratio — large-blockholder conviction."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), insider_shares_held)


def icn_100_officer_net_conviction_qtr(officer_buy_value: pd.Series, officer_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Officer net (buy - sell) conviction: (officer_buy_value - officer_sell_value) / held, quarterly."""
    net = _rolling_sum(officer_buy_value, _TD_QTR) - _rolling_sum(officer_sell_value, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def icn_101_director_net_conviction_qtr(director_buy_value: pd.Series, director_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Director net (buy - sell) conviction per held share, quarterly."""
    net = _rolling_sum(director_buy_value, _TD_QTR) - _rolling_sum(director_sell_value, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def icn_102_pure_buy_days_fraction_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of days in the past month with buying but no selling.
    Pure-buy days signal conviction uncompromised by concurrent distribution."""
    has_buy  = (insider_buy_shares > 0).astype(float)
    has_sell = (insider_sell_shares > 0).astype(float)
    pure_buy = has_buy * (1 - has_sell)
    return _rolling_mean(pure_buy, _TD_MO)


def icn_103_pure_buy_days_fraction_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of days in the past quarter with buying but no selling."""
    has_buy  = (insider_buy_shares > 0).astype(float)
    has_sell = (insider_sell_shares > 0).astype(float)
    pure_buy = has_buy * (1 - has_sell)
    return _rolling_mean(pure_buy, _TD_QTR)


def icn_104_buy_event_held_ratio_max_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 21-day max of the daily buy_shares / held ratio.
    Captures peak single-day conviction events."""
    daily_ratio = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_max(daily_ratio, _TD_MO)


def icn_105_buy_event_held_ratio_max_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 63-day max of the daily buy_shares / held ratio."""
    daily_ratio = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_max(daily_ratio, _TD_QTR)


# --- Group I (106-120): Window comparisons and conviction momentum ---

def icn_106_conviction_ratio_wk_vs_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Weekly buy conviction ratio minus quarterly buy conviction ratio.
    Positive = very recent buying intensity above quarterly rate."""
    r_wk  = _safe_div(_rolling_sum(insider_buy_shares, _TD_WK), insider_shares_held)
    r_qtr = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return r_wk - r_qtr


def icn_107_conviction_ratio_mo_vs_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly conviction ratio minus half-year conviction ratio."""
    r_mo  = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    r_hy  = _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)
    return r_mo - r_hy


def icn_108_conviction_ratio_qtr_vs_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly conviction ratio minus 2-year conviction ratio."""
    r_qtr = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    r_2y  = _safe_div(_rolling_sum(insider_buy_shares, _TD_2Y), insider_shares_held)
    return r_qtr - r_2y


def icn_109_held_shares_trend_slope_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """OLS slope of insider_shares_held over trailing 63 days (trend rate of accumulation)."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return insider_shares_held.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def icn_110_held_shares_trend_slope_1y(insider_shares_held: pd.Series) -> pd.Series:
    """OLS slope of insider_shares_held over trailing 252 days."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return insider_shares_held.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def icn_111_buy_conviction_slope_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """OLS slope of monthly conviction ratio over trailing 252 days (conviction trend)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def icn_112_conviction_acceleration_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Second difference of monthly conviction ratio at monthly lag (acceleration of conviction)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    d1 = ratio - ratio.shift(_TD_MO)
    return d1 - d1.shift(_TD_MO)


def icn_113_conviction_acceleration_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Second difference of quarterly conviction ratio at quarterly lag."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icn_114_conviction_ewm_acceleration(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=63) of conviction ratio — short-vs-long EWM crossover."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    short_ewm = _ewm_mean(ratio, _TD_MO)
    long_ewm  = _ewm_mean(ratio, _TD_QTR)
    return short_ewm - long_ewm


def icn_115_conviction_level_change_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Change in quarterly conviction ratio vs. its value one quarter ago."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return ratio - ratio.shift(_TD_QTR)


def icn_116_conviction_level_change_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Change in quarterly conviction ratio vs. its value one year ago."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return ratio - ratio.shift(_TD_YEAR)


def icn_117_held_growth_exceeds_buy_shares_flag(insider_shares_held: pd.Series, insider_buy_shares: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly held_shares growth exceeds quarterly buy_shares.
    Detects apparent non-purchase inflows (stock awards, grants, etc.)."""
    growth = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    buys = _rolling_sum(insider_buy_shares, _TD_QTR)
    return (growth > buys + _EPS).astype(float)


def icn_118_conviction_ratio_halfyr_zscore_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of half-year conviction ratio within trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)
    return _zscore_rolling(ratio, _TD_2Y)


def icn_119_officer_conviction_pct_rank_1y(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of monthly officer conviction ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def icn_120_net_conviction_zscore_1y(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly net-buy conviction ratio within trailing 1-year window."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


# --- Group J (121-135): Held-share level patterns and divergence signals ---

def icn_121_held_shares_above_expanding_mean(insider_shares_held: pd.Series) -> pd.Series:
    """1 if insider_shares_held is above its expanding mean (all-time rising flag)."""
    exp_mean = insider_shares_held.expanding(min_periods=1).mean()
    return (insider_shares_held > exp_mean).astype(float)


def icn_122_held_shares_rolling_min_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 1-year minimum of insider_shares_held (lowest insider ownership in 1 year)."""
    return _rolling_min(insider_shares_held, _TD_YEAR)


def icn_123_held_shares_rolling_max_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 1-year maximum of insider_shares_held."""
    return _rolling_max(insider_shares_held, _TD_YEAR)


def icn_124_held_shares_range_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Range (max - min) of insider_shares_held over the trailing 1 year."""
    return _rolling_max(insider_shares_held, _TD_YEAR) - _rolling_min(insider_shares_held, _TD_YEAR)


def icn_125_held_shares_position_in_1y_range(insider_shares_held: pd.Series) -> pd.Series:
    """Position of insider_shares_held within its 1-year range (0=at min, 1=at max)."""
    lo = _rolling_min(insider_shares_held, _TD_YEAR)
    hi = _rolling_max(insider_shares_held, _TD_YEAR)
    return _safe_div(insider_shares_held - lo, hi - lo)


def icn_126_held_shares_zscore_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of insider_shares_held within trailing 1-year window."""
    return _zscore_rolling(insider_shares_held, _TD_YEAR)


def icn_127_held_shares_zscore_2y(insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of insider_shares_held within trailing 2-year window."""
    return _zscore_rolling(insider_shares_held, _TD_2Y)


def icn_128_held_shares_expanding_zscore(insider_shares_held: pd.Series) -> pd.Series:
    """Expanding z-score of insider_shares_held (all-history)."""
    m  = insider_shares_held.expanding(min_periods=2).mean()
    sd = insider_shares_held.expanding(min_periods=2).std()
    return _safe_div(insider_shares_held - m, sd)


def icn_129_held_shares_ewm_deviation_mo(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held minus its EWM(span=21) — deviation from short-term trend."""
    return insider_shares_held - _ewm_mean(insider_shares_held, _TD_MO)


def icn_130_held_shares_ewm_deviation_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held minus its EWM(span=63) — deviation from quarterly trend."""
    return insider_shares_held - _ewm_mean(insider_shares_held, _TD_QTR)


def icn_131_buy_shares_to_held_level_daily(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Daily (raw, not rolled) buy_shares / insider_shares_held.
    Non-zero only on transaction days; captures the instantaneous stake impact of each buy."""
    return _safe_div(insider_buy_shares, insider_shares_held)


def icn_132_sell_shares_to_held_level_daily(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Daily (raw) sell_shares / insider_shares_held — instantaneous stake reduction per event."""
    return _safe_div(insider_sell_shares, insider_shares_held)


def icn_133_net_flow_to_held_daily(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Daily net (buy - sell) / insider_shares_held — instantaneous net conviction."""
    return _safe_div(insider_buy_shares - insider_sell_shares, insider_shares_held)


def icn_134_buy_event_magnitude_sum_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Sum of daily buy_shares/held over 1 year (cumulative conviction flow).
    Aggregates the stake-fraction impact of every buy over the year."""
    daily = _safe_div(insider_buy_shares, insider_shares_held).fillna(0)
    return _rolling_sum(daily, _TD_YEAR)


def icn_135_buy_event_magnitude_sum_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Sum of daily buy_shares/held over 1 quarter."""
    daily = _safe_div(insider_buy_shares, insider_shares_held).fillna(0)
    return _rolling_sum(daily, _TD_QTR)


# --- Group K (136-150): Composite, multi-signal, and advanced conviction ---

def icn_136_ceo_flag_x_stake_growth(ceo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """CEO monthly conviction ratio multiplied by quarterly held_shares growth indicator.
    Joint signal: CEO buying when total stake is growing."""
    ceo_r  = _safe_div(_rolling_sum(ceo_buy_value, _TD_MO), insider_shares_held)
    held_g = (insider_shares_held - insider_shares_held.shift(_TD_QTR) > 0).astype(float)
    return ceo_r * held_g


def icn_137_multibuyer_conviction_score_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Multi-buyer conviction score: conviction_ratio * buyers * (1 + count/buyers).
    Rewards broad participation AND frequency."""
    ratio  = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    buyers = _rolling_sum(insider_buyers, _TD_QTR)
    cnt    = _rolling_sum(insider_buy_count, _TD_QTR)
    freq   = _safe_div(cnt, buyers.replace(0, np.nan)).fillna(0)
    return ratio * buyers * (1.0 + freq)


def icn_138_conviction_above_threshold_days_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Count of days in past 252 where daily buy_shares/held > 1% of held.
    Measures how often insiders make individually meaningful purchases."""
    daily = _safe_div(insider_buy_shares, insider_shares_held).fillna(0)
    above = (daily > 0.01).astype(float)
    return _rolling_sum(above, _TD_YEAR)


def icn_139_conviction_above_threshold_days_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Count of days in past 63 where daily buy_shares/held > 1% of held."""
    daily = _safe_div(insider_buy_shares, insider_shares_held).fillna(0)
    above = (daily > 0.01).astype(float)
    return _rolling_sum(above, _TD_QTR)


def icn_140_held_growth_vs_buy_ratio(insider_shares_held: pd.Series, insider_buy_shares: pd.Series) -> pd.Series:
    """Ratio of quarterly held_shares growth to quarterly buy_shares.
    Values close to 1 indicate all stake growth is from open-market purchases."""
    growth = (insider_shares_held - insider_shares_held.shift(_TD_QTR)).clip(lower=0)
    buys   = _rolling_sum(insider_buy_shares, _TD_QTR)
    return _safe_div(growth, buys)


def icn_141_conviction_regime_flag(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Regime flag: 1 when quarterly conviction ratio is above its 2-year 75th percentile."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    p75   = ratio.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).quantile(0.75)
    return (ratio > p75).astype(float)


def icn_142_low_conviction_regime_flag(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Regime flag: 1 when quarterly conviction ratio is below its 2-year 25th percentile."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    p25   = ratio.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).quantile(0.25)
    return (ratio < p25).astype(float)


def icn_143_sell_stake_erosion_flag(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly sell_shares >= 5% of insider_shares_held (significant liquidation)."""
    ratio = _safe_div(_rolling_sum(insider_sell_shares, _TD_QTR), insider_shares_held)
    return (ratio >= 0.05).astype(float)


def icn_144_buy_overwhelms_sell_flag(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_conviction >= 2x quarterly sell_conviction."""
    buy_r  = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    sell_r = _safe_div(_rolling_sum(insider_sell_shares, _TD_QTR), insider_shares_held).fillna(0)
    return (buy_r >= 2.0 * sell_r + _EPS).astype(float)


def icn_145_tenpct_buy_count_conviction_qtr(tenpct_buy_count: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """10%-holder buy count per 1M held shares (quarterly) — blockholder buy frequency conviction."""
    cnt = _rolling_sum(tenpct_buy_count, _TD_QTR)
    return _safe_div(cnt, insider_shares_held / 1e6)


def icn_146_insider_count_weighted_conviction_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Conviction ratio weighted by (buy_count / distinct_buyers): rewards repeat buyers."""
    ratio   = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    cnt     = _rolling_sum(insider_buy_count, _TD_QTR)
    buyers  = _rolling_sum(insider_buyers, _TD_QTR).replace(0, np.nan)
    repeats = cnt / buyers
    return ratio * repeats.fillna(1.0)


def icn_147_conviction_surprise_vs_1y_ewm(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Conviction surprise: monthly ratio minus EWM(span=252) of monthly ratio.
    Captures a sudden spike in conviction above the long-run exponential trend."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    ewm   = _ewm_mean(ratio, _TD_YEAR)
    return ratio - ewm


def icn_148_conviction_ratio_2y_zscore(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of quarterly conviction ratio within trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return _zscore_rolling(ratio, _TD_2Y)


def icn_149_held_shares_recovery_from_min(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held divided by its 1-year rolling minimum.
    Values > 1 indicate accumulation above the recent trough."""
    min_1y = _rolling_min(insider_shares_held, _TD_YEAR)
    return _safe_div(insider_shares_held, min_1y)


def icn_150_grand_conviction_composite(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series, officer_buy_value: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Grand conviction composite: equally weighted average of five z-scored signals.
    1) quarterly buy/held ratio, 2) held shares growth, 3) buy count, 4) officer buy/held,
    5) net (buy-sell)/held. Undefined inputs yield NaN that are excluded from the average."""
    z1 = _zscore_rolling(_safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held), _TD_YEAR)
    z2 = _zscore_rolling(insider_shares_held - insider_shares_held.shift(_TD_QTR), _TD_YEAR)
    z3 = _zscore_rolling(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)
    z4 = _zscore_rolling(_safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    z5 = _zscore_rolling(_safe_div(net, insider_shares_held), _TD_YEAR)
    n_valid = (z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
               + z4.notna().astype(float) + z5.notna().astype(float))
    total = z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0)
    return _safe_div(total, n_valid)


# --- Group L (151-175 in 076-150 file, numbered 176-200 globally): New features ---

def icn_176_buy_conviction_halfyr_zscore_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of half-year (126d) buy conviction ratio within trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)
    return _zscore_rolling(ratio, _TD_2Y)


def icn_177_held_shares_median_deviation_1y(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held minus its 1-year rolling median — deviation from median ownership."""
    return insider_shares_held - _rolling_median(insider_shares_held, _TD_YEAR)


def icn_178_buy_conviction_ewm_span126(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=126) of monthly buy conviction ratio — half-year smoothed conviction level."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return _ewm_mean(ratio, _TD_HALF)


def icn_179_sell_conviction_ewm_mo(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=21) of monthly sell conviction ratio (sell_shares/held)."""
    ratio = _safe_div(_rolling_sum(insider_sell_shares, _TD_MO), insider_shares_held)
    return _ewm_mean(ratio, _TD_MO)


def icn_180_net_conviction_ewm_1y(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=252) of monthly net conviction ratio — long-run smoothed net conviction."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return _ewm_mean(ratio, _TD_YEAR)


def icn_181_held_shares_2y_pct_rank(insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of insider_shares_held within trailing 2-year window."""
    return _rolling_rank_pct(insider_shares_held, _TD_2Y)


def icn_182_buy_conviction_ratio_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year (126-day) rolling buy conviction ratio (buy_shares/held)."""
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)


def icn_183_sell_conviction_ratio_halfyr(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year (126-day) rolling sell conviction ratio (sell_shares/held)."""
    return _safe_div(_rolling_sum(insider_sell_shares, _TD_HALF), insider_shares_held)


def icn_184_net_conviction_ratio_halfyr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year net conviction ratio: (buy - sell) / held over 126 days."""
    net = _rolling_sum(insider_buy_shares, _TD_HALF) - _rolling_sum(insider_sell_shares, _TD_HALF)
    return _safe_div(net, insider_shares_held)


def icn_185_buy_conviction_ratio_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """2-year (504-day) rolling buy conviction ratio."""
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_2Y), insider_shares_held)


def icn_186_held_shares_below_1y_min_flag(insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if insider_shares_held is at or below its 1-year rolling minimum (capitulation low)."""
    min_1y = _rolling_min(insider_shares_held, _TD_YEAR)
    return (insider_shares_held <= min_1y + _EPS).astype(float)


def icn_187_held_shares_near_2y_peak_flag(insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if insider_shares_held is within 5% of its 2-year rolling maximum."""
    max_2y = _rolling_max(insider_shares_held, _TD_2Y)
    return (insider_shares_held >= 0.95 * max_2y).astype(float)


def icn_188_buy_shares_wk_vs_mo_ratio(insider_buy_shares: pd.Series) -> pd.Series:
    """Weekly buy_shares sum divided by monthly buy_shares sum — very-recent vs. 1-month pace."""
    wk = _rolling_sum(insider_buy_shares, _TD_WK)
    mo = _rolling_sum(insider_buy_shares, _TD_MO)
    return _safe_div(wk, mo)


def icn_189_sell_shares_wk_vs_mo_ratio(insider_sell_shares: pd.Series) -> pd.Series:
    """Weekly sell_shares sum divided by monthly sell_shares sum."""
    wk = _rolling_sum(insider_sell_shares, _TD_WK)
    mo = _rolling_sum(insider_sell_shares, _TD_MO)
    return _safe_div(wk, mo)


def icn_190_buy_value_halfyr_zscore_2y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of half-year buy value / held within trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _TD_HALF), insider_shares_held)
    return _zscore_rolling(ratio, _TD_2Y)


def icn_191_held_shares_pct_growth_halfyr(insider_shares_held: pd.Series) -> pd.Series:
    """Percent growth in insider_shares_held over 126 days."""
    prior = insider_shares_held.shift(_TD_HALF)
    return _safe_div(insider_shares_held - prior, prior)


def icn_192_held_shares_pct_growth_2y(insider_shares_held: pd.Series) -> pd.Series:
    """Percent growth in insider_shares_held over 504 days (2 years)."""
    prior = insider_shares_held.shift(_TD_2Y)
    return _safe_div(insider_shares_held - prior, prior)


def icn_193_conviction_buy_value_rank_2y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of monthly buy value conviction ratio (buy_value/held) in trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _TD_MO), insider_shares_held)
    return _rolling_rank_pct(ratio, _TD_2Y)


def icn_194_officer_net_conviction_halfyr(officer_buy_value: pd.Series, officer_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year net (officer_buy_value - officer_sell_value) / insider_shares_held."""
    net = _rolling_sum(officer_buy_value, _TD_HALF) - _rolling_sum(officer_sell_value, _TD_HALF)
    return _safe_div(net, insider_shares_held)


def icn_195_director_net_conviction_halfyr(director_buy_value: pd.Series, director_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year net (director_buy_value - director_sell_value) / insider_shares_held."""
    net = _rolling_sum(director_buy_value, _TD_HALF) - _rolling_sum(director_sell_value, _TD_HALF)
    return _safe_div(net, insider_shares_held)


def icn_196_buy_conviction_vs_halfyr_avg(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly conviction ratio minus its half-year rolling mean — conviction above recent norm."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return ratio - _rolling_mean(ratio, _TD_HALF)


def icn_197_sell_conviction_zscore_1y(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly sell conviction ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(insider_sell_shares, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


def icn_198_net_conviction_expanding_rank(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Expanding percentile rank of monthly net conviction ratio — all-history standing."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return ratio.expanding(min_periods=2).rank(pct=True)


def icn_199_held_shares_1y_low_recovery_pct(insider_shares_held: pd.Series) -> pd.Series:
    """Percent recovery of insider_shares_held from its 1-year low: (held - min_1y) / min_1y."""
    min_1y = _rolling_min(insider_shares_held, _TD_YEAR)
    return _safe_div(insider_shares_held - min_1y, min_1y)


def icn_200_senior_exec_conviction_composite(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Composite senior-exec conviction: z-score average of CEO, CFO, and officer conviction ratios.
    Rewards broad senior participation in buying relative to existing stake."""
    z1 = _zscore_rolling(_safe_div(_rolling_sum(ceo_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(_rolling_sum(cfo_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    n_valid = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
    total = z1.fillna(0) + z2.fillna(0) + z3.fillna(0)
    return _safe_div(total, n_valid)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_CONVICTION_REGISTRY_076_150 = {
    "icn_076_buy_ratio_vs_1y_avg":                    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_076_buy_ratio_vs_1y_avg},
    "icn_077_buy_ratio_vs_2y_avg":                    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_077_buy_ratio_vs_2y_avg},
    "icn_078_buy_ratio_vs_median_1y":                 {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_078_buy_ratio_vs_median_1y},
    "icn_079_buy_ratio_at_1y_max_flag":               {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_079_buy_ratio_at_1y_max_flag},
    "icn_080_buy_ratio_drawdown_from_1y_peak":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_080_buy_ratio_drawdown_from_1y_peak},
    "icn_081_buy_value_ratio_vs_1y_avg":              {"inputs": ["insider_buy_value", "insider_shares_held"],                                                               "func": icn_081_buy_value_ratio_vs_1y_avg},
    "icn_082_net_conviction_ratio_vs_1y_avg":         {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_082_net_conviction_ratio_vs_1y_avg},
    "icn_083_held_pct_growth_vs_1y_avg":              {"inputs": ["insider_shares_held"],                                                                                    "func": icn_083_held_pct_growth_vs_1y_avg},
    "icn_084_conviction_ratio_ewm_vs_mean":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_084_conviction_ratio_ewm_vs_mean},
    "icn_085_officer_conviction_vs_avg":              {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_085_officer_conviction_vs_avg},
    "icn_086_director_conviction_ratio_1y_zscore":    {"inputs": ["director_buy_value", "insider_shares_held"],                                                              "func": icn_086_director_conviction_ratio_1y_zscore},
    "icn_087_ceo_conviction_ratio_1y_zscore":         {"inputs": ["ceo_buy_value", "insider_shares_held"],                                                                   "func": icn_087_ceo_conviction_ratio_1y_zscore},
    "icn_088_held_growth_pct_rank_1y":                {"inputs": ["insider_shares_held"],                                                                                    "func": icn_088_held_growth_pct_rank_1y},
    "icn_089_net_conviction_pct_rank_1y":             {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_089_net_conviction_pct_rank_1y},
    "icn_090_conviction_ratio_expanding_pct_rank":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_090_conviction_ratio_expanding_pct_rank},
    "icn_091_buy_vs_sell_conviction_qtr":             {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_091_buy_vs_sell_conviction_qtr},
    "icn_092_proportional_commitment_mo":             {"inputs": ["insider_buy_value", "insider_sell_value", "insider_shares_held"],                                         "func": icn_092_proportional_commitment_mo},
    "icn_093_proportional_commitment_qtr":            {"inputs": ["insider_buy_value", "insider_sell_value", "insider_shares_held"],                                         "func": icn_093_proportional_commitment_qtr},
    "icn_094_sell_conviction_ratio_mo":               {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_094_sell_conviction_ratio_mo},
    "icn_095_sell_conviction_ratio_qtr":              {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_095_sell_conviction_ratio_qtr},
    "icn_096_buy_minus_sell_conviction_mo":           {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_096_buy_minus_sell_conviction_mo},
    "icn_097_buy_minus_sell_conviction_qtr":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_097_buy_minus_sell_conviction_qtr},
    "icn_098_held_dilution_adjusted_buy_ratio_mo":    {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_098_held_dilution_adjusted_buy_ratio_mo},
    "icn_099_tenpct_holder_net_conviction_qtr":       {"inputs": ["tenpct_buy_value", "insider_shares_held"],                                                                "func": icn_099_tenpct_holder_net_conviction_qtr},
    "icn_100_officer_net_conviction_qtr":             {"inputs": ["officer_buy_value", "officer_sell_value", "insider_shares_held"],                                         "func": icn_100_officer_net_conviction_qtr},
    "icn_101_director_net_conviction_qtr":            {"inputs": ["director_buy_value", "director_sell_value", "insider_shares_held"],                                       "func": icn_101_director_net_conviction_qtr},
    "icn_102_pure_buy_days_fraction_mo":              {"inputs": ["insider_buy_shares", "insider_sell_shares"],                                                              "func": icn_102_pure_buy_days_fraction_mo},
    "icn_103_pure_buy_days_fraction_qtr":             {"inputs": ["insider_buy_shares", "insider_sell_shares"],                                                              "func": icn_103_pure_buy_days_fraction_qtr},
    "icn_104_buy_event_held_ratio_max_mo":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_104_buy_event_held_ratio_max_mo},
    "icn_105_buy_event_held_ratio_max_qtr":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_105_buy_event_held_ratio_max_qtr},
    "icn_106_conviction_ratio_wk_vs_qtr":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_106_conviction_ratio_wk_vs_qtr},
    "icn_107_conviction_ratio_mo_vs_halfyr":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_107_conviction_ratio_mo_vs_halfyr},
    "icn_108_conviction_ratio_qtr_vs_2y":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_108_conviction_ratio_qtr_vs_2y},
    "icn_109_held_shares_trend_slope_qtr":            {"inputs": ["insider_shares_held"],                                                                                    "func": icn_109_held_shares_trend_slope_qtr},
    "icn_110_held_shares_trend_slope_1y":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_110_held_shares_trend_slope_1y},
    "icn_111_buy_conviction_slope_1y":                {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_111_buy_conviction_slope_1y},
    "icn_112_conviction_acceleration_mo":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_112_conviction_acceleration_mo},
    "icn_113_conviction_acceleration_qtr":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_113_conviction_acceleration_qtr},
    "icn_114_conviction_ewm_acceleration":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_114_conviction_ewm_acceleration},
    "icn_115_conviction_level_change_qtr":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_115_conviction_level_change_qtr},
    "icn_116_conviction_level_change_1y":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_116_conviction_level_change_1y},
    "icn_117_held_growth_exceeds_buy_shares_flag":    {"inputs": ["insider_shares_held", "insider_buy_shares"],                                                              "func": icn_117_held_growth_exceeds_buy_shares_flag},
    "icn_118_conviction_ratio_halfyr_zscore_2y":      {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_118_conviction_ratio_halfyr_zscore_2y},
    "icn_119_officer_conviction_pct_rank_1y":         {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_119_officer_conviction_pct_rank_1y},
    "icn_120_net_conviction_zscore_1y":               {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_120_net_conviction_zscore_1y},
    "icn_121_held_shares_above_expanding_mean":       {"inputs": ["insider_shares_held"],                                                                                    "func": icn_121_held_shares_above_expanding_mean},
    "icn_122_held_shares_rolling_min_1y":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_122_held_shares_rolling_min_1y},
    "icn_123_held_shares_rolling_max_1y":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_123_held_shares_rolling_max_1y},
    "icn_124_held_shares_range_1y":                   {"inputs": ["insider_shares_held"],                                                                                    "func": icn_124_held_shares_range_1y},
    "icn_125_held_shares_position_in_1y_range":       {"inputs": ["insider_shares_held"],                                                                                    "func": icn_125_held_shares_position_in_1y_range},
    "icn_126_held_shares_zscore_1y":                  {"inputs": ["insider_shares_held"],                                                                                    "func": icn_126_held_shares_zscore_1y},
    "icn_127_held_shares_zscore_2y":                  {"inputs": ["insider_shares_held"],                                                                                    "func": icn_127_held_shares_zscore_2y},
    "icn_128_held_shares_expanding_zscore":           {"inputs": ["insider_shares_held"],                                                                                    "func": icn_128_held_shares_expanding_zscore},
    "icn_129_held_shares_ewm_deviation_mo":           {"inputs": ["insider_shares_held"],                                                                                    "func": icn_129_held_shares_ewm_deviation_mo},
    "icn_130_held_shares_ewm_deviation_qtr":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_130_held_shares_ewm_deviation_qtr},
    "icn_131_buy_shares_to_held_level_daily":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_131_buy_shares_to_held_level_daily},
    "icn_132_sell_shares_to_held_level_daily":        {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_132_sell_shares_to_held_level_daily},
    "icn_133_net_flow_to_held_daily":                 {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_133_net_flow_to_held_daily},
    "icn_134_buy_event_magnitude_sum_1y":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_134_buy_event_magnitude_sum_1y},
    "icn_135_buy_event_magnitude_sum_qtr":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_135_buy_event_magnitude_sum_qtr},
    "icn_136_ceo_flag_x_stake_growth":                {"inputs": ["ceo_buy_value", "insider_shares_held"],                                                                   "func": icn_136_ceo_flag_x_stake_growth},
    "icn_137_multibuyer_conviction_score_qtr":        {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers", "insider_buy_count"],                       "func": icn_137_multibuyer_conviction_score_qtr},
    "icn_138_conviction_above_threshold_days_1y":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_138_conviction_above_threshold_days_1y},
    "icn_139_conviction_above_threshold_days_qtr":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_139_conviction_above_threshold_days_qtr},
    "icn_140_held_growth_vs_buy_ratio":               {"inputs": ["insider_shares_held", "insider_buy_shares"],                                                              "func": icn_140_held_growth_vs_buy_ratio},
    "icn_141_conviction_regime_flag":                 {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_141_conviction_regime_flag},
    "icn_142_low_conviction_regime_flag":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_142_low_conviction_regime_flag},
    "icn_143_sell_stake_erosion_flag":                {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_143_sell_stake_erosion_flag},
    "icn_144_buy_overwhelms_sell_flag":               {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_144_buy_overwhelms_sell_flag},
    "icn_145_tenpct_buy_count_conviction_qtr":        {"inputs": ["tenpct_buy_count", "insider_shares_held"],                                                                "func": icn_145_tenpct_buy_count_conviction_qtr},
    "icn_146_insider_count_weighted_conviction_qtr":  {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count", "insider_buyers"],                       "func": icn_146_insider_count_weighted_conviction_qtr},
    "icn_147_conviction_surprise_vs_1y_ewm":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_147_conviction_surprise_vs_1y_ewm},
    "icn_148_conviction_ratio_2y_zscore":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_148_conviction_ratio_2y_zscore},
    "icn_149_held_shares_recovery_from_min":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_149_held_shares_recovery_from_min},
    "icn_150_grand_conviction_composite":             {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count", "officer_buy_value", "insider_sell_shares"], "func": icn_150_grand_conviction_composite},
    "icn_176_buy_conviction_halfyr_zscore_2y":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_176_buy_conviction_halfyr_zscore_2y},
    "icn_177_held_shares_median_deviation_1y":        {"inputs": ["insider_shares_held"],                                                                                    "func": icn_177_held_shares_median_deviation_1y},
    "icn_178_buy_conviction_ewm_span126":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_178_buy_conviction_ewm_span126},
    "icn_179_sell_conviction_ewm_mo":                 {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_179_sell_conviction_ewm_mo},
    "icn_180_net_conviction_ewm_1y":                  {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_180_net_conviction_ewm_1y},
    "icn_181_held_shares_2y_pct_rank":                {"inputs": ["insider_shares_held"],                                                                                    "func": icn_181_held_shares_2y_pct_rank},
    "icn_182_buy_conviction_ratio_halfyr":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_182_buy_conviction_ratio_halfyr},
    "icn_183_sell_conviction_ratio_halfyr":           {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_183_sell_conviction_ratio_halfyr},
    "icn_184_net_conviction_ratio_halfyr":            {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_184_net_conviction_ratio_halfyr},
    "icn_185_buy_conviction_ratio_2y":               {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_185_buy_conviction_ratio_2y},
    "icn_186_held_shares_below_1y_min_flag":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_186_held_shares_below_1y_min_flag},
    "icn_187_held_shares_near_2y_peak_flag":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_187_held_shares_near_2y_peak_flag},
    "icn_188_buy_shares_wk_vs_mo_ratio":              {"inputs": ["insider_buy_shares"],                                                                                     "func": icn_188_buy_shares_wk_vs_mo_ratio},
    "icn_189_sell_shares_wk_vs_mo_ratio":             {"inputs": ["insider_sell_shares"],                                                                                    "func": icn_189_sell_shares_wk_vs_mo_ratio},
    "icn_190_buy_value_halfyr_zscore_2y":             {"inputs": ["insider_buy_value", "insider_shares_held"],                                                              "func": icn_190_buy_value_halfyr_zscore_2y},
    "icn_191_held_shares_pct_growth_halfyr":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_191_held_shares_pct_growth_halfyr},
    "icn_192_held_shares_pct_growth_2y":              {"inputs": ["insider_shares_held"],                                                                                    "func": icn_192_held_shares_pct_growth_2y},
    "icn_193_conviction_buy_value_rank_2y":           {"inputs": ["insider_buy_value", "insider_shares_held"],                                                              "func": icn_193_conviction_buy_value_rank_2y},
    "icn_194_officer_net_conviction_halfyr":          {"inputs": ["officer_buy_value", "officer_sell_value", "insider_shares_held"],                                         "func": icn_194_officer_net_conviction_halfyr},
    "icn_195_director_net_conviction_halfyr":         {"inputs": ["director_buy_value", "director_sell_value", "insider_shares_held"],                                       "func": icn_195_director_net_conviction_halfyr},
    "icn_196_buy_conviction_vs_halfyr_avg":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_196_buy_conviction_vs_halfyr_avg},
    "icn_197_sell_conviction_zscore_1y":              {"inputs": ["insider_sell_shares", "insider_shares_held"],                                                             "func": icn_197_sell_conviction_zscore_1y},
    "icn_198_net_conviction_expanding_rank":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_198_net_conviction_expanding_rank},
    "icn_199_held_shares_1y_low_recovery_pct":        {"inputs": ["insider_shares_held"],                                                                                    "func": icn_199_held_shares_1y_low_recovery_pct},
    "icn_200_senior_exec_conviction_composite":       {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "insider_shares_held"],                             "func": icn_200_senior_exec_conviction_composite},
}
