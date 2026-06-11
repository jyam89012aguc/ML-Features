"""
67_working_capital_drain — Extended Features 001-075
Domain: working-capital depletion — additional variants: quick-ratio dynamics,
        CCC longer windows and slopes, receivables/inventory build streaks,
        depletion-speed accelerations, range positions, multi-metric composites
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_DAYS_Q   = 91.25
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    flag = cond.fillna(False).astype(int)
    arr = flag.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=cond.index)


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over a trailing window of width w."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = np.nanmean(arr)
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within trailing [min,max] range; 0=window low."""
    lo = _rolling_min(s, w)
    hi = _rolling_max(s, w)
    return _safe_div(s - lo, hi - lo)


def _ccc(receivables, inventory, payables, revenue, cor):
    """Cash conversion cycle (DSO + DIO - DPO) helper."""
    dr = (revenue / _DAYS_Q).abs().replace(0, np.nan)
    dc = (cor / _DAYS_Q).abs().replace(0, np.nan)
    return _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Working capital — additional windows and angles ---

def wcd_ext_001_wc_5y_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital absolute change over 5 years (1260-day lag)."""
    return workingcapital - workingcapital.shift(_TD_5Y)


def wcd_ext_002_wc_3y_pct(workingcapital: pd.Series) -> pd.Series:
    """Working capital 3-year percent change; denominator is abs(prior)."""
    prior = workingcapital.shift(_TD_3Y)
    return _safe_div_abs(workingcapital - prior, prior)


def wcd_ext_003_wc_drawdown_from_5y_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its rolling 20-quarter (1260-day) peak."""
    return workingcapital - _rolling_max(workingcapital, _TD_5Y)


def wcd_ext_004_wc_pct_drawdown_from_12q_peak(workingcapital: pd.Series) -> pd.Series:
    """Percent drawdown of working capital from its 12-quarter peak."""
    peak = _rolling_max(workingcapital, _TD_3Y)
    return _safe_div_abs(workingcapital - peak, peak)


def wcd_ext_005_wc_range_position_4q(workingcapital: pd.Series) -> pd.Series:
    """Position of working capital within trailing 4-quarter [min,max] range."""
    return _range_position(workingcapital, _TD_YEAR)


def wcd_ext_006_wc_range_position_12q(workingcapital: pd.Series) -> pd.Series:
    """Position of working capital within trailing 12-quarter [min,max] range."""
    return _range_position(workingcapital, _TD_3Y)


def wcd_ext_007_wc_4q_slope(workingcapital: pd.Series) -> pd.Series:
    """OLS slope of working capital over trailing 4-quarter window."""
    return _rolling_slope(workingcapital, _TD_YEAR)


def wcd_ext_008_wc_8q_slope(workingcapital: pd.Series) -> pd.Series:
    """OLS slope of working capital over trailing 8-quarter window."""
    return _rolling_slope(workingcapital, _TD_2Y)


def wcd_ext_009_wc_qoq_decel(workingcapital: pd.Series) -> pd.Series:
    """Acceleration: QoQ WC change minus the prior-quarter QoQ change."""
    dq = workingcapital - workingcapital.shift(_TD_QTR)
    return dq - dq.shift(_TD_QTR)


def wcd_ext_010_wc_at_8q_low_flag(workingcapital: pd.Series) -> pd.Series:
    """Binary: 1 if working capital is at or below its trailing 8-quarter minimum."""
    return (workingcapital <= _rolling_min(workingcapital, _TD_2Y)).astype(float)


def wcd_ext_011_wc_at_expanding_low_flag(workingcapital: pd.Series) -> pd.Series:
    """Binary: 1 if working capital is at its all-history expanding minimum."""
    return (workingcapital <= workingcapital.expanding(min_periods=1).min()).astype(float)


def wcd_ext_012_wc_pct_rank_5y(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of working capital within trailing 20-quarter window."""
    return _rolling_rank_pct(workingcapital, _TD_5Y)


# --- Group B (013-024): Current / quick ratio dynamics ---

def wcd_ext_013_current_ratio_qoq_change(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in current ratio (assetsc / liabilitiesc)."""
    ratio = _safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def wcd_ext_014_current_ratio_below_1_flag(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current ratio < 1.0 (current liabilities exceed current assets)."""
    return (_safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan)) < 1.0).astype(float)


def wcd_ext_015_current_ratio_below_1_streak(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Consecutive-day streak of current ratio below 1.0."""
    return _consec_streak(_safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan)) < 1.0)


def wcd_ext_016_current_ratio_zscore_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan)), _TD_YEAR)


def wcd_ext_017_quick_ratio(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio: (assetsc - inventory) / liabilitiesc."""
    return _safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan))


def wcd_ext_018_quick_ratio_qoq_change(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in quick ratio."""
    ratio = _safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def wcd_ext_019_quick_ratio_yoy_change(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in quick ratio."""
    ratio = _safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_ext_020_quick_ratio_below_1_flag(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if quick ratio < 1.0 (illiquid current position)."""
    return (_safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan)) < 1.0).astype(float)


def wcd_ext_021_quick_ratio_zscore_4q(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of quick ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan)), _TD_YEAR)


def wcd_ext_022_cash_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio: cashnequiv / liabilitiesc (strictest liquidity measure)."""
    return _safe_div(cashnequiv, liabilitiesc.abs().replace(0, np.nan))


def wcd_ext_023_cash_ratio_below_quarter_flag(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if cash ratio < 0.25 (cash covers less than a quarter of current liabilities)."""
    return (_safe_div(cashnequiv, liabilitiesc.abs().replace(0, np.nan)) < 0.25).astype(float)


def wcd_ext_024_current_ratio_drawdown_from_8q_peak(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio drawdown from its 8-quarter rolling peak."""
    ratio = _safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan))
    return ratio - _rolling_max(ratio, _TD_2Y)


# --- Group C (025-038): Cash-conversion-cycle — longer windows and slopes ---

def wcd_ext_025_ccc_8q_slope(receivables: pd.Series, inventory: pd.Series,
                             payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """OLS slope of CCC over trailing 8-quarter window."""
    return _rolling_slope(_ccc(receivables, inventory, payables, revenue, cor), _TD_2Y)


def wcd_ext_026_ccc_zscore_8q(receivables: pd.Series, inventory: pd.Series,
                              payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Z-score of CCC within trailing 8-quarter window."""
    return _zscore_rolling(_ccc(receivables, inventory, payables, revenue, cor), _TD_2Y)


def wcd_ext_027_ccc_pct_rank_8q(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Percentile rank of CCC within trailing 8-quarter window (high = worst stretch)."""
    return _rolling_rank_pct(_ccc(receivables, inventory, payables, revenue, cor), _TD_2Y)


def wcd_ext_028_ccc_drawup_from_4q_low(receivables: pd.Series, inventory: pd.Series,
                                       payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """CCC minus its trailing 4-quarter rolling minimum (worsening from best level)."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    return ccc - _rolling_min(ccc, _TD_YEAR)


def wcd_ext_029_ccc_range_position_8q(receivables: pd.Series, inventory: pd.Series,
                                      payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Position of CCC within trailing 8-quarter [min,max] range."""
    return _range_position(_ccc(receivables, inventory, payables, revenue, cor), _TD_2Y)


def wcd_ext_030_ccc_rising_streak(receivables: pd.Series, inventory: pd.Series,
                                  payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Consecutive-day streak of CCC rising QoQ (lengthening conversion cycle)."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    return _consec_streak(ccc > ccc.shift(_TD_QTR))


def wcd_ext_031_ccc_vs_8q_avg(receivables: pd.Series, inventory: pd.Series,
                              payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """CCC minus its trailing 8-quarter mean."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    return ccc - _rolling_mean(ccc, _TD_2Y)


def wcd_ext_032_dso_8q_slope(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of DSO over trailing 8-quarter window."""
    dso = _safe_div(receivables, (revenue / _DAYS_Q).abs().replace(0, np.nan))
    return _rolling_slope(dso, _TD_2Y)


def wcd_ext_033_dso_pct_rank_8q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of DSO within trailing 8-quarter window."""
    dso = _safe_div(receivables, (revenue / _DAYS_Q).abs().replace(0, np.nan))
    return _rolling_rank_pct(dso, _TD_2Y)


def wcd_ext_034_dso_rising_streak(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Consecutive-day streak of DSO rising QoQ (collection deterioration)."""
    dso = _safe_div(receivables, (revenue / _DAYS_Q).abs().replace(0, np.nan))
    return _consec_streak(dso > dso.shift(_TD_QTR))


def wcd_ext_035_dio_8q_slope(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """OLS slope of DIO over trailing 8-quarter window."""
    dio = _safe_div(inventory, (cor / _DAYS_Q).abs().replace(0, np.nan))
    return _rolling_slope(dio, _TD_2Y)


def wcd_ext_036_dio_zscore_4q(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Z-score of DIO within trailing 4-quarter window."""
    dio = _safe_div(inventory, (cor / _DAYS_Q).abs().replace(0, np.nan))
    return _zscore_rolling(dio, _TD_YEAR)


def wcd_ext_037_dio_rising_streak(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Consecutive-day streak of DIO rising QoQ (inventory build-up)."""
    dio = _safe_div(inventory, (cor / _DAYS_Q).abs().replace(0, np.nan))
    return _consec_streak(dio > dio.shift(_TD_QTR))


def wcd_ext_038_dpo_zscore_4q(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """Z-score of DPO within trailing 4-quarter window (payables stretching)."""
    dpo = _safe_div(payables, (cor / _DAYS_Q).abs().replace(0, np.nan))
    return _zscore_rolling(dpo, _TD_YEAR)


# --- Group D (039-050): Receivables / inventory build dynamics ---

def wcd_ext_039_receivables_yoy_change(receivables: pd.Series) -> pd.Series:
    """Receivables absolute YoY change."""
    return receivables - receivables.shift(_TD_YEAR)


def wcd_ext_040_receivables_to_revenue_zscore_4q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of receivables-to-revenue ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(receivables, revenue.abs().replace(0, np.nan)), _TD_YEAR)


def wcd_ext_041_receivables_to_revenue_pct_rank_8q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of receivables-to-revenue ratio within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(receivables, revenue.abs().replace(0, np.nan)), _TD_2Y)


def wcd_ext_042_receivables_rising_streak(receivables: pd.Series) -> pd.Series:
    """Consecutive-day streak of receivables rising QoQ."""
    return _consec_streak(receivables > receivables.shift(_TD_QTR))


def wcd_ext_043_receivables_drawup_from_4q_low(receivables: pd.Series) -> pd.Series:
    """Receivables minus their trailing 4-quarter rolling minimum (build from trough)."""
    return receivables - _rolling_min(receivables, _TD_YEAR)


def wcd_ext_044_inventory_to_revenue_zscore_4q(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of inventory-to-revenue ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(inventory, revenue.abs().replace(0, np.nan)), _TD_YEAR)


def wcd_ext_045_inventory_to_revenue_pct_rank_8q(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of inventory-to-revenue ratio within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(inventory, revenue.abs().replace(0, np.nan)), _TD_2Y)


def wcd_ext_046_inventory_rising_streak(inventory: pd.Series) -> pd.Series:
    """Consecutive-day streak of inventory rising QoQ."""
    return _consec_streak(inventory > inventory.shift(_TD_QTR))


def wcd_ext_047_inventory_yoy_change(inventory: pd.Series) -> pd.Series:
    """Inventory absolute YoY change."""
    return inventory - inventory.shift(_TD_YEAR)


def wcd_ext_048_receivables_plus_inventory_yoy_change(receivables: pd.Series, inventory: pd.Series) -> pd.Series:
    """YoY change in (receivables + inventory) — combined illiquid-WC build."""
    combined = receivables + inventory
    return combined - combined.shift(_TD_YEAR)


def wcd_ext_049_receivables_growth_vs_revenue_growth(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY receivables growth minus YoY revenue growth (positive = receivables outpacing sales)."""
    dr = _safe_div_abs(receivables - receivables.shift(_TD_YEAR), receivables.shift(_TD_YEAR))
    dv = _safe_div_abs(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR))
    return dr - dv


def wcd_ext_050_inventory_growth_vs_revenue_growth(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY inventory growth minus YoY revenue growth (positive = inventory overhang building)."""
    di = _safe_div_abs(inventory - inventory.shift(_TD_YEAR), inventory.shift(_TD_YEAR))
    dv = _safe_div_abs(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR))
    return di - dv


# --- Group E (051-062): Cash depletion and current-liability pressure ---

def wcd_ext_051_cash_3y_change(cashnequiv: pd.Series) -> pd.Series:
    """Cash & equivalents absolute change over 3 years (756-day lag)."""
    return cashnequiv - cashnequiv.shift(_TD_3Y)


def wcd_ext_052_cash_range_position_8q(cashnequiv: pd.Series) -> pd.Series:
    """Position of cash within trailing 8-quarter [min,max] range (0 = cash low)."""
    return _range_position(cashnequiv, _TD_2Y)


def wcd_ext_053_cash_8q_slope(cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of cash & equivalents over trailing 8-quarter window."""
    return _rolling_slope(cashnequiv, _TD_2Y)


def wcd_ext_054_cash_declining_streak(cashnequiv: pd.Series) -> pd.Series:
    """Consecutive-day streak of cash declining QoQ (sustained cash burn)."""
    return _consec_streak(cashnequiv < cashnequiv.shift(_TD_QTR))


def wcd_ext_055_cash_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash within trailing 8-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_2Y)


def wcd_ext_056_cash_at_8q_low_flag(cashnequiv: pd.Series) -> pd.Series:
    """Binary: 1 if cash is at or below its trailing 8-quarter minimum."""
    return (cashnequiv <= _rolling_min(cashnequiv, _TD_2Y)).astype(float)


def wcd_ext_057_liabilitiesc_rising_streak(liabilitiesc: pd.Series) -> pd.Series:
    """Consecutive-day streak of current liabilities rising QoQ."""
    return _consec_streak(liabilitiesc > liabilitiesc.shift(_TD_QTR))


def wcd_ext_058_liabilitiesc_zscore_4q(liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current liabilities within trailing 4-quarter window."""
    return _zscore_rolling(liabilitiesc, _TD_YEAR)


def wcd_ext_059_liabilitiesc_drawup_from_4q_low(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities minus their trailing 4-quarter rolling minimum."""
    return liabilitiesc - _rolling_min(liabilitiesc, _TD_YEAR)


def wcd_ext_060_debtc_to_assetsc(debtc: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Short-term debt as fraction of current assets — near-term maturity coverage stress."""
    return _safe_div(debtc, assetsc.abs().replace(0, np.nan))


def wcd_ext_061_debtc_yoy_change(debtc: pd.Series) -> pd.Series:
    """Short-term debt absolute YoY change (rising = refinancing pressure)."""
    return debtc - debtc.shift(_TD_YEAR)


def wcd_ext_062_cash_minus_debtc(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """Cash minus short-term debt — net liquid position against near-term maturities."""
    return cashnequiv - debtc


# --- Group F (063-075): NCFO interaction, depletion speed, composites ---

def wcd_ext_063_ncfo_zscore_4q(ncfo: pd.Series) -> pd.Series:
    """Z-score of operating cash flow within trailing 4-quarter window."""
    return _zscore_rolling(ncfo, _TD_YEAR)


def wcd_ext_064_ncfo_declining_streak(ncfo: pd.Series) -> pd.Series:
    """Consecutive-day streak of operating cash flow declining QoQ."""
    return _consec_streak(ncfo < ncfo.shift(_TD_QTR))


def wcd_ext_065_ncfo_negative_streak(ncfo: pd.Series) -> pd.Series:
    """Consecutive-day streak of negative operating cash flow."""
    return _consec_streak(ncfo < 0)


def wcd_ext_066_ncfo_to_wc_yoy_change(ncfo: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """YoY change in ncfo-to-working-capital ratio."""
    ratio = _safe_div(ncfo, workingcapital.replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_ext_067_wc_drain_12q_cumulative(workingcapital: pd.Series) -> pd.Series:
    """Cumulative QoQ WC change over trailing 12 quarters (chronic-drain measure)."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _rolling_sum(dw, _TD_3Y)


def wcd_ext_068_wc_decline_speed_accel(workingcapital: pd.Series) -> pd.Series:
    """WC decline-speed acceleration: 4-quarter avg QoQ change minus the 8-quarter avg."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _rolling_mean(dw, _TD_YEAR) - _rolling_mean(dw, _TD_2Y)


def wcd_ext_069_wc_decline_fraction_8q(workingcapital: pd.Series) -> pd.Series:
    """Fraction of trailing 8 quarters where WC declined QoQ."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _rolling_mean((dw < 0).astype(float), _TD_2Y)


def wcd_ext_070_wc_volatility_ratio_4q_8q(workingcapital: pd.Series) -> pd.Series:
    """Ratio of 4-quarter to 8-quarter rolling std of WC (rising = recent instability)."""
    return _safe_div(_rolling_std(workingcapital, _TD_YEAR), _rolling_std(workingcapital, _TD_2Y))


def wcd_ext_071_noncash_wc_zscore_4q(assetsc: pd.Series, cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of non-cash working capital within trailing 4-quarter window."""
    nwc = (assetsc - cashnequiv) - liabilitiesc
    return _zscore_rolling(nwc, _TD_YEAR)


def wcd_ext_072_noncash_wc_drawdown_from_8q_peak(assetsc: pd.Series, cashnequiv: pd.Series,
                                                 liabilitiesc: pd.Series) -> pd.Series:
    """Non-cash working capital drawdown from its 8-quarter rolling peak."""
    nwc = (assetsc - cashnequiv) - liabilitiesc
    return nwc - _rolling_max(nwc, _TD_2Y)


def wcd_ext_073_wc_negative_streak(workingcapital: pd.Series) -> pd.Series:
    """Consecutive-day streak of negative working capital."""
    return _consec_streak(workingcapital < 0)


def wcd_ext_074_liquidity_severity_composite(assetsc: pd.Series, inventory: pd.Series,
                                             liabilitiesc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Liquidity severity composite: equally weighted mean of 4-quarter z-scores of
    current ratio, quick ratio and cash ratio. Lower = more distressed liquidity."""
    cur = _safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan))
    qck = _safe_div(assetsc - inventory, liabilitiesc.abs().replace(0, np.nan))
    csh = _safe_div(cashnequiv, liabilitiesc.abs().replace(0, np.nan))
    return (_zscore_rolling(cur, _TD_YEAR)
            + _zscore_rolling(qck, _TD_YEAR)
            + _zscore_rolling(csh, _TD_YEAR)) / 3.0


def wcd_ext_075_wc_capitulation_composite(workingcapital: pd.Series, cashnequiv: pd.Series,
                                          receivables: pd.Series, inventory: pd.Series,
                                          revenue: pd.Series) -> pd.Series:
    """Capitulation WC composite: averages normalized distress signals — inverse WC
    8-quarter range position, inverse cash 8-quarter range position, receivables-to-
    revenue rank, inventory-to-revenue rank. Higher = more extreme WC drain."""
    wc_pos = _range_position(workingcapital, _TD_2Y).fillna(0.5)
    cash_pos = _range_position(cashnequiv, _TD_2Y).fillna(0.5)
    rec_rank = _rolling_rank_pct(_safe_div(receivables, revenue.abs().replace(0, np.nan)), _TD_2Y).fillna(0.5)
    inv_rank = _rolling_rank_pct(_safe_div(inventory, revenue.abs().replace(0, np.nan)), _TD_2Y).fillna(0.5)
    return ((1.0 - wc_pos) + (1.0 - cash_pos) + rec_rank + inv_rank) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

WORKING_CAPITAL_DRAIN_EXTENDED_REGISTRY_001_075 = {
    "wcd_ext_001_wc_5y_change":                       {"inputs": ["workingcapital"],                                              "func": wcd_ext_001_wc_5y_change},
    "wcd_ext_002_wc_3y_pct":                          {"inputs": ["workingcapital"],                                              "func": wcd_ext_002_wc_3y_pct},
    "wcd_ext_003_wc_drawdown_from_5y_peak":           {"inputs": ["workingcapital"],                                              "func": wcd_ext_003_wc_drawdown_from_5y_peak},
    "wcd_ext_004_wc_pct_drawdown_from_12q_peak":      {"inputs": ["workingcapital"],                                              "func": wcd_ext_004_wc_pct_drawdown_from_12q_peak},
    "wcd_ext_005_wc_range_position_4q":               {"inputs": ["workingcapital"],                                              "func": wcd_ext_005_wc_range_position_4q},
    "wcd_ext_006_wc_range_position_12q":              {"inputs": ["workingcapital"],                                              "func": wcd_ext_006_wc_range_position_12q},
    "wcd_ext_007_wc_4q_slope":                        {"inputs": ["workingcapital"],                                              "func": wcd_ext_007_wc_4q_slope},
    "wcd_ext_008_wc_8q_slope":                        {"inputs": ["workingcapital"],                                              "func": wcd_ext_008_wc_8q_slope},
    "wcd_ext_009_wc_qoq_decel":                       {"inputs": ["workingcapital"],                                              "func": wcd_ext_009_wc_qoq_decel},
    "wcd_ext_010_wc_at_8q_low_flag":                  {"inputs": ["workingcapital"],                                              "func": wcd_ext_010_wc_at_8q_low_flag},
    "wcd_ext_011_wc_at_expanding_low_flag":           {"inputs": ["workingcapital"],                                              "func": wcd_ext_011_wc_at_expanding_low_flag},
    "wcd_ext_012_wc_pct_rank_5y":                     {"inputs": ["workingcapital"],                                              "func": wcd_ext_012_wc_pct_rank_5y},
    "wcd_ext_013_current_ratio_qoq_change":           {"inputs": ["assetsc", "liabilitiesc"],                                     "func": wcd_ext_013_current_ratio_qoq_change},
    "wcd_ext_014_current_ratio_below_1_flag":         {"inputs": ["assetsc", "liabilitiesc"],                                     "func": wcd_ext_014_current_ratio_below_1_flag},
    "wcd_ext_015_current_ratio_below_1_streak":       {"inputs": ["assetsc", "liabilitiesc"],                                     "func": wcd_ext_015_current_ratio_below_1_streak},
    "wcd_ext_016_current_ratio_zscore_4q":            {"inputs": ["assetsc", "liabilitiesc"],                                     "func": wcd_ext_016_current_ratio_zscore_4q},
    "wcd_ext_017_quick_ratio":                        {"inputs": ["assetsc", "inventory", "liabilitiesc"],                        "func": wcd_ext_017_quick_ratio},
    "wcd_ext_018_quick_ratio_qoq_change":             {"inputs": ["assetsc", "inventory", "liabilitiesc"],                        "func": wcd_ext_018_quick_ratio_qoq_change},
    "wcd_ext_019_quick_ratio_yoy_change":             {"inputs": ["assetsc", "inventory", "liabilitiesc"],                        "func": wcd_ext_019_quick_ratio_yoy_change},
    "wcd_ext_020_quick_ratio_below_1_flag":           {"inputs": ["assetsc", "inventory", "liabilitiesc"],                        "func": wcd_ext_020_quick_ratio_below_1_flag},
    "wcd_ext_021_quick_ratio_zscore_4q":              {"inputs": ["assetsc", "inventory", "liabilitiesc"],                        "func": wcd_ext_021_quick_ratio_zscore_4q},
    "wcd_ext_022_cash_ratio":                         {"inputs": ["cashnequiv", "liabilitiesc"],                                  "func": wcd_ext_022_cash_ratio},
    "wcd_ext_023_cash_ratio_below_quarter_flag":      {"inputs": ["cashnequiv", "liabilitiesc"],                                  "func": wcd_ext_023_cash_ratio_below_quarter_flag},
    "wcd_ext_024_current_ratio_drawdown_from_8q_peak": {"inputs": ["assetsc", "liabilitiesc"],                                    "func": wcd_ext_024_current_ratio_drawdown_from_8q_peak},
    "wcd_ext_025_ccc_8q_slope":                       {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_025_ccc_8q_slope},
    "wcd_ext_026_ccc_zscore_8q":                      {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_026_ccc_zscore_8q},
    "wcd_ext_027_ccc_pct_rank_8q":                    {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_027_ccc_pct_rank_8q},
    "wcd_ext_028_ccc_drawup_from_4q_low":             {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_028_ccc_drawup_from_4q_low},
    "wcd_ext_029_ccc_range_position_8q":              {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_029_ccc_range_position_8q},
    "wcd_ext_030_ccc_rising_streak":                  {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_030_ccc_rising_streak},
    "wcd_ext_031_ccc_vs_8q_avg":                      {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],      "func": wcd_ext_031_ccc_vs_8q_avg},
    "wcd_ext_032_dso_8q_slope":                       {"inputs": ["receivables", "revenue"],                                      "func": wcd_ext_032_dso_8q_slope},
    "wcd_ext_033_dso_pct_rank_8q":                    {"inputs": ["receivables", "revenue"],                                      "func": wcd_ext_033_dso_pct_rank_8q},
    "wcd_ext_034_dso_rising_streak":                  {"inputs": ["receivables", "revenue"],                                      "func": wcd_ext_034_dso_rising_streak},
    "wcd_ext_035_dio_8q_slope":                       {"inputs": ["inventory", "cor"],                                            "func": wcd_ext_035_dio_8q_slope},
    "wcd_ext_036_dio_zscore_4q":                      {"inputs": ["inventory", "cor"],                                            "func": wcd_ext_036_dio_zscore_4q},
    "wcd_ext_037_dio_rising_streak":                  {"inputs": ["inventory", "cor"],                                            "func": wcd_ext_037_dio_rising_streak},
    "wcd_ext_038_dpo_zscore_4q":                      {"inputs": ["payables", "cor"],                                             "func": wcd_ext_038_dpo_zscore_4q},
    "wcd_ext_039_receivables_yoy_change":             {"inputs": ["receivables"],                                                 "func": wcd_ext_039_receivables_yoy_change},
    "wcd_ext_040_receivables_to_revenue_zscore_4q":   {"inputs": ["receivables", "revenue"],                                      "func": wcd_ext_040_receivables_to_revenue_zscore_4q},
    "wcd_ext_041_receivables_to_revenue_pct_rank_8q": {"inputs": ["receivables", "revenue"],                                      "func": wcd_ext_041_receivables_to_revenue_pct_rank_8q},
    "wcd_ext_042_receivables_rising_streak":          {"inputs": ["receivables"],                                                 "func": wcd_ext_042_receivables_rising_streak},
    "wcd_ext_043_receivables_drawup_from_4q_low":     {"inputs": ["receivables"],                                                 "func": wcd_ext_043_receivables_drawup_from_4q_low},
    "wcd_ext_044_inventory_to_revenue_zscore_4q":     {"inputs": ["inventory", "revenue"],                                        "func": wcd_ext_044_inventory_to_revenue_zscore_4q},
    "wcd_ext_045_inventory_to_revenue_pct_rank_8q":   {"inputs": ["inventory", "revenue"],                                        "func": wcd_ext_045_inventory_to_revenue_pct_rank_8q},
    "wcd_ext_046_inventory_rising_streak":            {"inputs": ["inventory"],                                                   "func": wcd_ext_046_inventory_rising_streak},
    "wcd_ext_047_inventory_yoy_change":               {"inputs": ["inventory"],                                                   "func": wcd_ext_047_inventory_yoy_change},
    "wcd_ext_048_receivables_plus_inventory_yoy_change": {"inputs": ["receivables", "inventory"],                                 "func": wcd_ext_048_receivables_plus_inventory_yoy_change},
    "wcd_ext_049_receivables_growth_vs_revenue_growth": {"inputs": ["receivables", "revenue"],                                    "func": wcd_ext_049_receivables_growth_vs_revenue_growth},
    "wcd_ext_050_inventory_growth_vs_revenue_growth": {"inputs": ["inventory", "revenue"],                                        "func": wcd_ext_050_inventory_growth_vs_revenue_growth},
    "wcd_ext_051_cash_3y_change":                     {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_051_cash_3y_change},
    "wcd_ext_052_cash_range_position_8q":             {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_052_cash_range_position_8q},
    "wcd_ext_053_cash_8q_slope":                      {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_053_cash_8q_slope},
    "wcd_ext_054_cash_declining_streak":              {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_054_cash_declining_streak},
    "wcd_ext_055_cash_pct_rank_8q":                   {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_055_cash_pct_rank_8q},
    "wcd_ext_056_cash_at_8q_low_flag":                {"inputs": ["cashnequiv"],                                                  "func": wcd_ext_056_cash_at_8q_low_flag},
    "wcd_ext_057_liabilitiesc_rising_streak":         {"inputs": ["liabilitiesc"],                                                "func": wcd_ext_057_liabilitiesc_rising_streak},
    "wcd_ext_058_liabilitiesc_zscore_4q":             {"inputs": ["liabilitiesc"],                                                "func": wcd_ext_058_liabilitiesc_zscore_4q},
    "wcd_ext_059_liabilitiesc_drawup_from_4q_low":    {"inputs": ["liabilitiesc"],                                                "func": wcd_ext_059_liabilitiesc_drawup_from_4q_low},
    "wcd_ext_060_debtc_to_assetsc":                   {"inputs": ["debtc", "assetsc"],                                            "func": wcd_ext_060_debtc_to_assetsc},
    "wcd_ext_061_debtc_yoy_change":                   {"inputs": ["debtc"],                                                       "func": wcd_ext_061_debtc_yoy_change},
    "wcd_ext_062_cash_minus_debtc":                   {"inputs": ["cashnequiv", "debtc"],                                         "func": wcd_ext_062_cash_minus_debtc},
    "wcd_ext_063_ncfo_zscore_4q":                     {"inputs": ["ncfo"],                                                        "func": wcd_ext_063_ncfo_zscore_4q},
    "wcd_ext_064_ncfo_declining_streak":              {"inputs": ["ncfo"],                                                        "func": wcd_ext_064_ncfo_declining_streak},
    "wcd_ext_065_ncfo_negative_streak":               {"inputs": ["ncfo"],                                                        "func": wcd_ext_065_ncfo_negative_streak},
    "wcd_ext_066_ncfo_to_wc_yoy_change":              {"inputs": ["ncfo", "workingcapital"],                                      "func": wcd_ext_066_ncfo_to_wc_yoy_change},
    "wcd_ext_067_wc_drain_12q_cumulative":            {"inputs": ["workingcapital"],                                              "func": wcd_ext_067_wc_drain_12q_cumulative},
    "wcd_ext_068_wc_decline_speed_accel":             {"inputs": ["workingcapital"],                                              "func": wcd_ext_068_wc_decline_speed_accel},
    "wcd_ext_069_wc_decline_fraction_8q":             {"inputs": ["workingcapital"],                                              "func": wcd_ext_069_wc_decline_fraction_8q},
    "wcd_ext_070_wc_volatility_ratio_4q_8q":          {"inputs": ["workingcapital"],                                              "func": wcd_ext_070_wc_volatility_ratio_4q_8q},
    "wcd_ext_071_noncash_wc_zscore_4q":               {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                       "func": wcd_ext_071_noncash_wc_zscore_4q},
    "wcd_ext_072_noncash_wc_drawdown_from_8q_peak":   {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                       "func": wcd_ext_072_noncash_wc_drawdown_from_8q_peak},
    "wcd_ext_073_wc_negative_streak":                 {"inputs": ["workingcapital"],                                              "func": wcd_ext_073_wc_negative_streak},
    "wcd_ext_074_liquidity_severity_composite":       {"inputs": ["assetsc", "inventory", "liabilitiesc", "cashnequiv"],          "func": wcd_ext_074_liquidity_severity_composite},
    "wcd_ext_075_wc_capitulation_composite":          {"inputs": ["workingcapital", "cashnequiv", "receivables", "inventory", "revenue"], "func": wcd_ext_075_wc_capitulation_composite},
}
