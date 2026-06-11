"""
68_asset_quality — Extended Features 001-075
Domain: asset-base contraction / asset-quality erosion — additional variants:
        contraction streaks, range positions, slopes, writedown depth/clusters,
        reinvestment-gap dynamics, soft-vs-hard mix shifts, severity composites
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Total assets — additional windows and angles ---

def aqy_ext_001_assets_qoq_change(assets: pd.Series) -> pd.Series:
    """Total assets absolute QoQ change (63-day lag)."""
    return assets - assets.shift(_TD_QTR)


def aqy_ext_002_assets_5y_change(assets: pd.Series) -> pd.Series:
    """Total assets change over 5 years (1260-day lag)."""
    return assets - assets.shift(_TD_5Y)


def aqy_ext_003_assets_5y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 5-year percent change; denominator is abs(prior)."""
    prior = assets.shift(_TD_5Y)
    return _safe_div_abs(assets - prior, prior)


def aqy_ext_004_assets_drawdown_from_5y_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its rolling 20-quarter (1260-day) peak."""
    return assets - _rolling_max(assets, _TD_5Y)


def aqy_ext_005_assets_pct_drawdown_from_5y_peak(assets: pd.Series) -> pd.Series:
    """Total assets percent drawdown from its 20-quarter peak."""
    peak = _rolling_max(assets, _TD_5Y)
    return _safe_div_abs(assets - peak, peak)


def aqy_ext_006_assets_range_position_4q(assets: pd.Series) -> pd.Series:
    """Position of total assets within trailing 4-quarter [min,max] range."""
    return _range_position(assets, _TD_YEAR)


def aqy_ext_007_assets_range_position_12q(assets: pd.Series) -> pd.Series:
    """Position of total assets within trailing 12-quarter [min,max] range."""
    return _range_position(assets, _TD_3Y)


def aqy_ext_008_assets_4q_slope(assets: pd.Series) -> pd.Series:
    """OLS slope of total assets over trailing 4-quarter window."""
    return _rolling_slope(assets, _TD_YEAR)


def aqy_ext_009_assets_8q_slope(assets: pd.Series) -> pd.Series:
    """OLS slope of total assets over trailing 8-quarter window."""
    return _rolling_slope(assets, _TD_2Y)


def aqy_ext_010_assets_qoq_decel(assets: pd.Series) -> pd.Series:
    """Acceleration: QoQ asset change minus the prior-quarter QoQ change."""
    dq = assets - assets.shift(_TD_QTR)
    return dq - dq.shift(_TD_QTR)


def aqy_ext_011_assets_contraction_streak(assets: pd.Series) -> pd.Series:
    """Consecutive-day streak of total assets contracting QoQ."""
    return _consec_streak(assets < assets.shift(_TD_QTR))


def aqy_ext_012_assets_contraction_count_12q(assets: pd.Series) -> pd.Series:
    """Count of days in trailing 12 quarters where total assets contracted QoQ."""
    flag = (assets < assets.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_3Y)


# --- Group B (013-024): Intangibles writedown depth and clusters ---

def aqy_ext_013_intangibles_writedown_depth(intangibles: pd.Series) -> pd.Series:
    """Depth of QoQ intangibles drop below zero (magnitude of writedown, 0 if rising)."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    return (-pct).clip(lower=0.0)


def aqy_ext_014_intangibles_large_writedown_count_8q(intangibles: pd.Series) -> pd.Series:
    """Count of days in trailing 8 quarters where intangibles fell >25% QoQ."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    return _rolling_sum((pct < -0.25).astype(float), _TD_2Y)


def aqy_ext_015_intangibles_severe_writedown_flag(intangibles: pd.Series) -> pd.Series:
    """Binary: 1 if intangibles dropped more than 40% QoQ (massive impairment)."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    return (pct < -0.40).astype(float)


def aqy_ext_016_intangibles_contraction_streak(intangibles: pd.Series) -> pd.Series:
    """Consecutive-day streak of intangibles contracting QoQ."""
    return _consec_streak(intangibles < intangibles.shift(_TD_QTR))


def aqy_ext_017_intangibles_3y_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles 3-year percent change; denominator is abs(prior)."""
    prior = intangibles.shift(_TD_3Y)
    return _safe_div_abs(intangibles - prior, prior)


def aqy_ext_018_intangibles_drawdown_from_12q_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles level drawdown from its 12-quarter rolling peak."""
    return intangibles - _rolling_max(intangibles, _TD_3Y)


def aqy_ext_019_intangibles_range_position_8q(intangibles: pd.Series) -> pd.Series:
    """Position of intangibles within trailing 8-quarter [min,max] range."""
    return _range_position(intangibles, _TD_2Y)


def aqy_ext_020_intangibles_8q_slope(intangibles: pd.Series) -> pd.Series:
    """OLS slope of intangibles over trailing 8-quarter window."""
    return _rolling_slope(intangibles, _TD_2Y)


def aqy_ext_021_intangibles_to_assets_qoq_change(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in intangibles-to-assets ratio (falling = writedown shrinking soft assets)."""
    ratio = _safe_div(intangibles, assets)
    return ratio - ratio.shift(_TD_QTR)


def aqy_ext_022_intangibles_to_assets_pct_rank_8q(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of intangibles-to-assets ratio within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(intangibles, assets), _TD_2Y)


def aqy_ext_023_intangibles_zscore_8q(intangibles: pd.Series) -> pd.Series:
    """Z-score of intangibles within trailing 8-quarter window."""
    return _zscore_rolling(intangibles, _TD_2Y)


def aqy_ext_024_intangibles_at_8q_low_flag(intangibles: pd.Series) -> pd.Series:
    """Binary: 1 if intangibles are at or below their trailing 8-quarter minimum."""
    return (intangibles <= _rolling_min(intangibles, _TD_2Y)).astype(float)


# --- Group C (025-036): PP&E and tangible-asset contraction dynamics ---

def aqy_ext_025_ppnenet_drawdown_from_12q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E level drawdown from its 12-quarter rolling peak."""
    return ppnenet - _rolling_max(ppnenet, _TD_3Y)


def aqy_ext_026_ppnenet_pct_drawdown_from_8q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E percent drawdown from its 8-quarter rolling peak."""
    peak = _rolling_max(ppnenet, _TD_2Y)
    return _safe_div_abs(ppnenet - peak, peak)


def aqy_ext_027_ppnenet_range_position_8q(ppnenet: pd.Series) -> pd.Series:
    """Position of net PP&E within trailing 8-quarter [min,max] range."""
    return _range_position(ppnenet, _TD_2Y)


def aqy_ext_028_ppnenet_8q_slope(ppnenet: pd.Series) -> pd.Series:
    """OLS slope of net PP&E over trailing 8-quarter window."""
    return _rolling_slope(ppnenet, _TD_2Y)


def aqy_ext_029_ppnenet_2y_pct(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E 2-year percent change; denominator is abs(prior)."""
    prior = ppnenet.shift(_TD_2Y)
    return _safe_div_abs(ppnenet - prior, prior)


def aqy_ext_030_ppnenet_contraction_count_8q(ppnenet: pd.Series) -> pd.Series:
    """Count of days in trailing 8 quarters where net PP&E contracted QoQ."""
    flag = (ppnenet < ppnenet.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def aqy_ext_031_ppnenet_to_assets_yoy_change(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in PP&E-to-assets ratio (falling = hard-asset base eroding)."""
    ratio = _safe_div(ppnenet, assets)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_032_ppnenet_to_assets_zscore_4q(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of PP&E-to-assets ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(ppnenet, assets), _TD_YEAR)


def aqy_ext_033_tangibles_drawdown_from_12q_peak(tangibles: pd.Series) -> pd.Series:
    """Tangible assets level drawdown from its 12-quarter rolling peak."""
    return tangibles - _rolling_max(tangibles, _TD_3Y)


def aqy_ext_034_tangibles_range_position_8q(tangibles: pd.Series) -> pd.Series:
    """Position of tangible assets within trailing 8-quarter [min,max] range."""
    return _range_position(tangibles, _TD_2Y)


def aqy_ext_035_tangibles_8q_slope(tangibles: pd.Series) -> pd.Series:
    """OLS slope of tangible assets over trailing 8-quarter window."""
    return _rolling_slope(tangibles, _TD_2Y)


def aqy_ext_036_tangibles_contraction_streak(tangibles: pd.Series) -> pd.Series:
    """Consecutive-day streak of tangible assets contracting QoQ."""
    return _consec_streak(tangibles < tangibles.shift(_TD_QTR))


# --- Group D (037-048): Reinvestment gap and depreciation burden ---

def aqy_ext_037_capex_to_depamor_below_1_flag(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Binary: 1 if capex/depamor < 1.0 (reinvestment below depreciation)."""
    return (_safe_div(capex.abs(), depamor.abs()) < 1.0).astype(float)


def aqy_ext_038_capex_to_depamor_below_1_streak(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Consecutive-day streak of capex/depamor below 1.0 (chronic underinvestment)."""
    return _consec_streak(_safe_div(capex.abs(), depamor.abs()) < 1.0)


def aqy_ext_039_capex_to_depamor_zscore_4q(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Z-score of capex/depamor ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(capex.abs(), depamor.abs()), _TD_YEAR)


def aqy_ext_040_capex_to_depamor_yoy_change(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """YoY change in capex/depamor reinvestment-coverage ratio."""
    ratio = _safe_div(capex.abs(), depamor.abs())
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_041_capex_minus_depamor_yoy_change(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """YoY change in the net-investment gap (|capex| - |depamor|)."""
    gap = capex.abs() - depamor.abs()
    return gap - gap.shift(_TD_YEAR)


def aqy_ext_042_capex_3y_pct(capex: pd.Series) -> pd.Series:
    """Capex (absolute) 3-year percent change; denominator is abs(prior)."""
    cap = capex.abs()
    prior = cap.shift(_TD_3Y)
    return _safe_div_abs(cap - prior, prior)


def aqy_ext_043_capex_8q_slope(capex: pd.Series) -> pd.Series:
    """OLS slope of |capex| over trailing 8-quarter window."""
    return _rolling_slope(capex.abs(), _TD_2Y)


def aqy_ext_044_capex_contraction_streak(capex: pd.Series) -> pd.Series:
    """Consecutive-day streak of |capex| declining QoQ (sustained capex cutback)."""
    cap = capex.abs()
    return _consec_streak(cap < cap.shift(_TD_QTR))


def aqy_ext_045_capex_to_assets_yoy_change(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in capex-to-assets intensity ratio."""
    ratio = _safe_div(capex.abs(), assets)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_046_depamor_to_assets_yoy_change(depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in D&A-to-assets ratio (rising = asset base aging faster)."""
    ratio = _safe_div(depamor, assets)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_047_depamor_to_ppnenet_yoy_change(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """YoY change in D&A-to-PP&E ratio (rising = aging hard-asset base)."""
    ratio = _safe_div(depamor, ppnenet)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_048_depamor_to_ppnenet_pct_rank_8q(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """Percentile rank of D&A-to-PP&E ratio within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(depamor, ppnenet), _TD_2Y)


# --- Group E (049-060): Current-asset / receivables / inventory quality ---

def aqy_ext_049_assetsc_range_position_8q(assetsc: pd.Series) -> pd.Series:
    """Position of current assets within trailing 8-quarter [min,max] range."""
    return _range_position(assetsc, _TD_2Y)


def aqy_ext_050_assetsc_contraction_streak(assetsc: pd.Series) -> pd.Series:
    """Consecutive-day streak of current assets contracting QoQ."""
    return _consec_streak(assetsc < assetsc.shift(_TD_QTR))


def aqy_ext_051_assetsc_zscore_4q(assetsc: pd.Series) -> pd.Series:
    """Z-score of current assets within trailing 4-quarter window."""
    return _zscore_rolling(assetsc, _TD_YEAR)


def aqy_ext_052_assetsc_to_assets_zscore_4q(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of current-assets-to-total-assets ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(assetsc, assets), _TD_YEAR)


def aqy_ext_053_receivables_to_assets_zscore_4q(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of receivables-to-assets ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(receivables, assets), _TD_YEAR)


def aqy_ext_054_receivables_to_assets_pct_rank_8q(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of receivables-to-assets ratio within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(receivables, assets), _TD_2Y)


def aqy_ext_055_receivables_8q_slope(receivables: pd.Series) -> pd.Series:
    """OLS slope of receivables over trailing 8-quarter window."""
    return _rolling_slope(receivables, _TD_2Y)


def aqy_ext_056_inventory_to_assets_yoy_change(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in inventory-to-assets ratio (rising = inventory overhang building)."""
    ratio = _safe_div(inventory, assets)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_057_inventory_writedown_depth(inventory: pd.Series) -> pd.Series:
    """Depth of QoQ inventory drop below zero (magnitude of writedown, 0 if rising)."""
    pct = _safe_div_abs(inventory - inventory.shift(_TD_QTR), inventory.shift(_TD_QTR))
    return (-pct).clip(lower=0.0)


def aqy_ext_058_inventory_8q_slope(inventory: pd.Series) -> pd.Series:
    """OLS slope of inventory over trailing 8-quarter window."""
    return _rolling_slope(inventory, _TD_2Y)


def aqy_ext_059_cashnequiv_to_assets_zscore_4q(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of cash-to-assets ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(cashnequiv, assets), _TD_YEAR)


def aqy_ext_060_cashnequiv_to_assets_yoy_change(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in cash-to-assets ratio (falling = liquid-asset quality eroding)."""
    ratio = _safe_div(cashnequiv, assets)
    return ratio - ratio.shift(_TD_YEAR)


# --- Group F (061-068): Investments, asset turnover, soft/hard mix ---

def aqy_ext_061_investmentsnc_yoy_pct(investmentsnc: pd.Series) -> pd.Series:
    """Non-current investments YoY percent change; denominator is abs(prior)."""
    prior = investmentsnc.shift(_TD_YEAR)
    return _safe_div_abs(investmentsnc - prior, prior)


def aqy_ext_062_investmentsnc_drawdown_from_8q_peak(investmentsnc: pd.Series) -> pd.Series:
    """Non-current investments level drawdown from its 8-quarter rolling peak."""
    return investmentsnc - _rolling_max(investmentsnc, _TD_2Y)


def aqy_ext_063_investmentsnc_contraction_streak(investmentsnc: pd.Series) -> pd.Series:
    """Consecutive-day streak of non-current investments contracting QoQ."""
    return _consec_streak(investmentsnc < investmentsnc.shift(_TD_QTR))


def aqy_ext_064_asset_turnover_yoy_change(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in asset turnover (revenue/assets) — falling = utilization eroding."""
    ratio = _safe_div(revenue.abs(), assets)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_065_asset_turnover_8q_slope(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """OLS slope of asset turnover over trailing 8-quarter window."""
    return _rolling_slope(_safe_div(revenue.abs(), assets), _TD_2Y)


def aqy_ext_066_asset_turnover_range_position_8q(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Position of asset turnover within trailing 8-quarter [min,max] range."""
    return _range_position(_safe_div(revenue.abs(), assets), _TD_2Y)


def aqy_ext_067_hard_vs_soft_ratio_yoy_change(tangibles: pd.Series, intangibles: pd.Series) -> pd.Series:
    """YoY change in tangible-to-intangible (hard/soft) asset ratio."""
    ratio = _safe_div(tangibles, intangibles)
    return ratio - ratio.shift(_TD_YEAR)


def aqy_ext_068_hard_vs_soft_ratio_zscore_4q(tangibles: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Z-score of hard-to-soft asset ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(tangibles, intangibles), _TD_YEAR)


# --- Group G (069-075): Multi-asset confluence and severity composites ---

def aqy_ext_069_asset_contraction_breadth(assets: pd.Series, tangibles: pd.Series,
                                          ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Count of asset categories (assets, tangibles, PP&E, intangibles) contracting QoQ."""
    flags = [
        (assets < assets.shift(_TD_QTR)).astype(float),
        (tangibles < tangibles.shift(_TD_QTR)).astype(float),
        (ppnenet < ppnenet.shift(_TD_QTR)).astype(float),
        (intangibles < intangibles.shift(_TD_QTR)).astype(float),
    ]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def aqy_ext_070_all_assets_contracting_flag(assets: pd.Series, tangibles: pd.Series,
                                            ppnenet: pd.Series) -> pd.Series:
    """Binary: 1 when total assets, tangibles AND net PP&E are ALL contracting QoQ."""
    return ((assets < assets.shift(_TD_QTR))
            & (tangibles < tangibles.shift(_TD_QTR))
            & (ppnenet < ppnenet.shift(_TD_QTR))).astype(float)


def aqy_ext_071_asset_zscore_min_4q(assets: pd.Series, tangibles: pd.Series,
                                    ppnenet: pd.Series) -> pd.Series:
    """Minimum (worst) of the 4-quarter z-scores of assets, tangibles and net PP&E."""
    z_a = _zscore_rolling(assets, _TD_YEAR)
    z_t = _zscore_rolling(tangibles, _TD_YEAR)
    z_p = _zscore_rolling(ppnenet, _TD_YEAR)
    return pd.concat([z_a, z_t, z_p], axis=1).min(axis=1)


def aqy_ext_072_writedown_breadth_4q(intangibles: pd.Series, inventory: pd.Series,
                                     ppnenet: pd.Series) -> pd.Series:
    """Count of asset classes (intangibles, inventory, PP&E) with a >15% QoQ drop
    in the trailing 4-quarter window — breadth of writedown activity."""
    def _wd(s):
        pct = _safe_div_abs(s - s.shift(_TD_QTR), s.shift(_TD_QTR))
        return _rolling_sum((pct < -0.15).astype(float), _TD_YEAR)
    return ((_wd(intangibles) > 0).astype(float)
            + (_wd(inventory) > 0).astype(float)
            + (_wd(ppnenet) > 0).astype(float))


def aqy_ext_073_asset_erosion_composite_8q(assets: pd.Series, tangibles: pd.Series,
                                           ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Composite asset erosion: equally weighted 8-quarter z-scores of assets,
    tangibles, PP&E minus intangibles share. Lower = broader asset-quality erosion."""
    z_a = _zscore_rolling(assets, _TD_2Y)
    z_t = _zscore_rolling(tangibles, _TD_2Y)
    z_p = _zscore_rolling(ppnenet, _TD_2Y)
    z_i = _zscore_rolling(_safe_div(intangibles, assets), _TD_2Y)
    return (z_a + z_t + z_p - z_i) / 4.0


def aqy_ext_074_asset_erosion_yoy_composite(assets: pd.Series, tangibles: pd.Series,
                                            ppnenet: pd.Series) -> pd.Series:
    """Composite YoY erosion: equally weighted mean of YoY percent changes in
    assets, tangibles and net PP&E. More negative = broader contraction."""
    d_a = _safe_div_abs(assets - assets.shift(_TD_YEAR), assets.shift(_TD_YEAR))
    d_t = _safe_div_abs(tangibles - tangibles.shift(_TD_YEAR), tangibles.shift(_TD_YEAR))
    d_p = _safe_div_abs(ppnenet - ppnenet.shift(_TD_YEAR), ppnenet.shift(_TD_YEAR))
    return (d_a + d_t + d_p) / 3.0


def aqy_ext_075_asset_quality_capitulation_composite(assets: pd.Series, tangibles: pd.Series,
                                                     ppnenet: pd.Series, intangibles: pd.Series,
                                                     revenue: pd.Series) -> pd.Series:
    """Capitulation asset-quality composite: averages normalized distress signals —
    inverse assets 8-quarter range position, inverse PP&E 8-quarter range position,
    intangibles-to-assets rank, and inverse asset-turnover rank. Higher = more
    extreme asset-quality erosion."""
    a_pos = _range_position(assets, _TD_2Y).fillna(0.5)
    p_pos = _range_position(ppnenet, _TD_2Y).fillna(0.5)
    int_rank = _rolling_rank_pct(_safe_div(intangibles, assets), _TD_2Y).fillna(0.5)
    turn_rank = _rolling_rank_pct(_safe_div(revenue.abs(), assets), _TD_2Y).fillna(0.5)
    return ((1.0 - a_pos) + (1.0 - p_pos) + int_rank + (1.0 - turn_rank)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

ASSET_QUALITY_EXTENDED_REGISTRY_001_075 = {
    "aqy_ext_001_assets_qoq_change":                  {"inputs": ["assets"],                                          "func": aqy_ext_001_assets_qoq_change},
    "aqy_ext_002_assets_5y_change":                   {"inputs": ["assets"],                                          "func": aqy_ext_002_assets_5y_change},
    "aqy_ext_003_assets_5y_pct":                      {"inputs": ["assets"],                                          "func": aqy_ext_003_assets_5y_pct},
    "aqy_ext_004_assets_drawdown_from_5y_peak":       {"inputs": ["assets"],                                          "func": aqy_ext_004_assets_drawdown_from_5y_peak},
    "aqy_ext_005_assets_pct_drawdown_from_5y_peak":   {"inputs": ["assets"],                                          "func": aqy_ext_005_assets_pct_drawdown_from_5y_peak},
    "aqy_ext_006_assets_range_position_4q":           {"inputs": ["assets"],                                          "func": aqy_ext_006_assets_range_position_4q},
    "aqy_ext_007_assets_range_position_12q":          {"inputs": ["assets"],                                          "func": aqy_ext_007_assets_range_position_12q},
    "aqy_ext_008_assets_4q_slope":                    {"inputs": ["assets"],                                          "func": aqy_ext_008_assets_4q_slope},
    "aqy_ext_009_assets_8q_slope":                    {"inputs": ["assets"],                                          "func": aqy_ext_009_assets_8q_slope},
    "aqy_ext_010_assets_qoq_decel":                   {"inputs": ["assets"],                                          "func": aqy_ext_010_assets_qoq_decel},
    "aqy_ext_011_assets_contraction_streak":          {"inputs": ["assets"],                                          "func": aqy_ext_011_assets_contraction_streak},
    "aqy_ext_012_assets_contraction_count_12q":       {"inputs": ["assets"],                                          "func": aqy_ext_012_assets_contraction_count_12q},
    "aqy_ext_013_intangibles_writedown_depth":        {"inputs": ["intangibles"],                                     "func": aqy_ext_013_intangibles_writedown_depth},
    "aqy_ext_014_intangibles_large_writedown_count_8q": {"inputs": ["intangibles"],                                   "func": aqy_ext_014_intangibles_large_writedown_count_8q},
    "aqy_ext_015_intangibles_severe_writedown_flag":  {"inputs": ["intangibles"],                                     "func": aqy_ext_015_intangibles_severe_writedown_flag},
    "aqy_ext_016_intangibles_contraction_streak":     {"inputs": ["intangibles"],                                     "func": aqy_ext_016_intangibles_contraction_streak},
    "aqy_ext_017_intangibles_3y_pct":                 {"inputs": ["intangibles"],                                     "func": aqy_ext_017_intangibles_3y_pct},
    "aqy_ext_018_intangibles_drawdown_from_12q_peak": {"inputs": ["intangibles"],                                     "func": aqy_ext_018_intangibles_drawdown_from_12q_peak},
    "aqy_ext_019_intangibles_range_position_8q":      {"inputs": ["intangibles"],                                     "func": aqy_ext_019_intangibles_range_position_8q},
    "aqy_ext_020_intangibles_8q_slope":               {"inputs": ["intangibles"],                                     "func": aqy_ext_020_intangibles_8q_slope},
    "aqy_ext_021_intangibles_to_assets_qoq_change":   {"inputs": ["intangibles", "assets"],                           "func": aqy_ext_021_intangibles_to_assets_qoq_change},
    "aqy_ext_022_intangibles_to_assets_pct_rank_8q":  {"inputs": ["intangibles", "assets"],                           "func": aqy_ext_022_intangibles_to_assets_pct_rank_8q},
    "aqy_ext_023_intangibles_zscore_8q":              {"inputs": ["intangibles"],                                     "func": aqy_ext_023_intangibles_zscore_8q},
    "aqy_ext_024_intangibles_at_8q_low_flag":         {"inputs": ["intangibles"],                                     "func": aqy_ext_024_intangibles_at_8q_low_flag},
    "aqy_ext_025_ppnenet_drawdown_from_12q_peak":     {"inputs": ["ppnenet"],                                         "func": aqy_ext_025_ppnenet_drawdown_from_12q_peak},
    "aqy_ext_026_ppnenet_pct_drawdown_from_8q_peak":  {"inputs": ["ppnenet"],                                         "func": aqy_ext_026_ppnenet_pct_drawdown_from_8q_peak},
    "aqy_ext_027_ppnenet_range_position_8q":          {"inputs": ["ppnenet"],                                         "func": aqy_ext_027_ppnenet_range_position_8q},
    "aqy_ext_028_ppnenet_8q_slope":                   {"inputs": ["ppnenet"],                                         "func": aqy_ext_028_ppnenet_8q_slope},
    "aqy_ext_029_ppnenet_2y_pct":                     {"inputs": ["ppnenet"],                                         "func": aqy_ext_029_ppnenet_2y_pct},
    "aqy_ext_030_ppnenet_contraction_count_8q":       {"inputs": ["ppnenet"],                                         "func": aqy_ext_030_ppnenet_contraction_count_8q},
    "aqy_ext_031_ppnenet_to_assets_yoy_change":       {"inputs": ["ppnenet", "assets"],                               "func": aqy_ext_031_ppnenet_to_assets_yoy_change},
    "aqy_ext_032_ppnenet_to_assets_zscore_4q":        {"inputs": ["ppnenet", "assets"],                               "func": aqy_ext_032_ppnenet_to_assets_zscore_4q},
    "aqy_ext_033_tangibles_drawdown_from_12q_peak":   {"inputs": ["tangibles"],                                       "func": aqy_ext_033_tangibles_drawdown_from_12q_peak},
    "aqy_ext_034_tangibles_range_position_8q":        {"inputs": ["tangibles"],                                       "func": aqy_ext_034_tangibles_range_position_8q},
    "aqy_ext_035_tangibles_8q_slope":                 {"inputs": ["tangibles"],                                       "func": aqy_ext_035_tangibles_8q_slope},
    "aqy_ext_036_tangibles_contraction_streak":       {"inputs": ["tangibles"],                                       "func": aqy_ext_036_tangibles_contraction_streak},
    "aqy_ext_037_capex_to_depamor_below_1_flag":      {"inputs": ["capex", "depamor"],                                "func": aqy_ext_037_capex_to_depamor_below_1_flag},
    "aqy_ext_038_capex_to_depamor_below_1_streak":    {"inputs": ["capex", "depamor"],                                "func": aqy_ext_038_capex_to_depamor_below_1_streak},
    "aqy_ext_039_capex_to_depamor_zscore_4q":         {"inputs": ["capex", "depamor"],                                "func": aqy_ext_039_capex_to_depamor_zscore_4q},
    "aqy_ext_040_capex_to_depamor_yoy_change":        {"inputs": ["capex", "depamor"],                                "func": aqy_ext_040_capex_to_depamor_yoy_change},
    "aqy_ext_041_capex_minus_depamor_yoy_change":     {"inputs": ["capex", "depamor"],                                "func": aqy_ext_041_capex_minus_depamor_yoy_change},
    "aqy_ext_042_capex_3y_pct":                       {"inputs": ["capex"],                                           "func": aqy_ext_042_capex_3y_pct},
    "aqy_ext_043_capex_8q_slope":                     {"inputs": ["capex"],                                           "func": aqy_ext_043_capex_8q_slope},
    "aqy_ext_044_capex_contraction_streak":           {"inputs": ["capex"],                                           "func": aqy_ext_044_capex_contraction_streak},
    "aqy_ext_045_capex_to_assets_yoy_change":         {"inputs": ["capex", "assets"],                                 "func": aqy_ext_045_capex_to_assets_yoy_change},
    "aqy_ext_046_depamor_to_assets_yoy_change":       {"inputs": ["depamor", "assets"],                               "func": aqy_ext_046_depamor_to_assets_yoy_change},
    "aqy_ext_047_depamor_to_ppnenet_yoy_change":      {"inputs": ["depamor", "ppnenet"],                              "func": aqy_ext_047_depamor_to_ppnenet_yoy_change},
    "aqy_ext_048_depamor_to_ppnenet_pct_rank_8q":     {"inputs": ["depamor", "ppnenet"],                              "func": aqy_ext_048_depamor_to_ppnenet_pct_rank_8q},
    "aqy_ext_049_assetsc_range_position_8q":          {"inputs": ["assetsc"],                                         "func": aqy_ext_049_assetsc_range_position_8q},
    "aqy_ext_050_assetsc_contraction_streak":         {"inputs": ["assetsc"],                                         "func": aqy_ext_050_assetsc_contraction_streak},
    "aqy_ext_051_assetsc_zscore_4q":                  {"inputs": ["assetsc"],                                         "func": aqy_ext_051_assetsc_zscore_4q},
    "aqy_ext_052_assetsc_to_assets_zscore_4q":        {"inputs": ["assetsc", "assets"],                               "func": aqy_ext_052_assetsc_to_assets_zscore_4q},
    "aqy_ext_053_receivables_to_assets_zscore_4q":    {"inputs": ["receivables", "assets"],                           "func": aqy_ext_053_receivables_to_assets_zscore_4q},
    "aqy_ext_054_receivables_to_assets_pct_rank_8q":  {"inputs": ["receivables", "assets"],                           "func": aqy_ext_054_receivables_to_assets_pct_rank_8q},
    "aqy_ext_055_receivables_8q_slope":               {"inputs": ["receivables"],                                     "func": aqy_ext_055_receivables_8q_slope},
    "aqy_ext_056_inventory_to_assets_yoy_change":     {"inputs": ["inventory", "assets"],                             "func": aqy_ext_056_inventory_to_assets_yoy_change},
    "aqy_ext_057_inventory_writedown_depth":          {"inputs": ["inventory"],                                       "func": aqy_ext_057_inventory_writedown_depth},
    "aqy_ext_058_inventory_8q_slope":                 {"inputs": ["inventory"],                                       "func": aqy_ext_058_inventory_8q_slope},
    "aqy_ext_059_cashnequiv_to_assets_zscore_4q":     {"inputs": ["cashnequiv", "assets"],                            "func": aqy_ext_059_cashnequiv_to_assets_zscore_4q},
    "aqy_ext_060_cashnequiv_to_assets_yoy_change":    {"inputs": ["cashnequiv", "assets"],                            "func": aqy_ext_060_cashnequiv_to_assets_yoy_change},
    "aqy_ext_061_investmentsnc_yoy_pct":              {"inputs": ["investmentsnc"],                                   "func": aqy_ext_061_investmentsnc_yoy_pct},
    "aqy_ext_062_investmentsnc_drawdown_from_8q_peak": {"inputs": ["investmentsnc"],                                  "func": aqy_ext_062_investmentsnc_drawdown_from_8q_peak},
    "aqy_ext_063_investmentsnc_contraction_streak":   {"inputs": ["investmentsnc"],                                   "func": aqy_ext_063_investmentsnc_contraction_streak},
    "aqy_ext_064_asset_turnover_yoy_change":          {"inputs": ["revenue", "assets"],                               "func": aqy_ext_064_asset_turnover_yoy_change},
    "aqy_ext_065_asset_turnover_8q_slope":            {"inputs": ["revenue", "assets"],                               "func": aqy_ext_065_asset_turnover_8q_slope},
    "aqy_ext_066_asset_turnover_range_position_8q":   {"inputs": ["revenue", "assets"],                               "func": aqy_ext_066_asset_turnover_range_position_8q},
    "aqy_ext_067_hard_vs_soft_ratio_yoy_change":      {"inputs": ["tangibles", "intangibles"],                        "func": aqy_ext_067_hard_vs_soft_ratio_yoy_change},
    "aqy_ext_068_hard_vs_soft_ratio_zscore_4q":       {"inputs": ["tangibles", "intangibles"],                        "func": aqy_ext_068_hard_vs_soft_ratio_zscore_4q},
    "aqy_ext_069_asset_contraction_breadth":          {"inputs": ["assets", "tangibles", "ppnenet", "intangibles"],   "func": aqy_ext_069_asset_contraction_breadth},
    "aqy_ext_070_all_assets_contracting_flag":        {"inputs": ["assets", "tangibles", "ppnenet"],                  "func": aqy_ext_070_all_assets_contracting_flag},
    "aqy_ext_071_asset_zscore_min_4q":                {"inputs": ["assets", "tangibles", "ppnenet"],                  "func": aqy_ext_071_asset_zscore_min_4q},
    "aqy_ext_072_writedown_breadth_4q":               {"inputs": ["intangibles", "inventory", "ppnenet"],             "func": aqy_ext_072_writedown_breadth_4q},
    "aqy_ext_073_asset_erosion_composite_8q":         {"inputs": ["assets", "tangibles", "ppnenet", "intangibles"],   "func": aqy_ext_073_asset_erosion_composite_8q},
    "aqy_ext_074_asset_erosion_yoy_composite":        {"inputs": ["assets", "tangibles", "ppnenet"],                  "func": aqy_ext_074_asset_erosion_yoy_composite},
    "aqy_ext_075_asset_quality_capitulation_composite": {"inputs": ["assets", "tangibles", "ppnenet", "intangibles", "revenue"], "func": aqy_ext_075_asset_quality_capitulation_composite},
}
