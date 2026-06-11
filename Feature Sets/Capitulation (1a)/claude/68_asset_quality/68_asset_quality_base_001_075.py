"""
68_asset_quality — Base Features 001-075
Domain: asset-base contraction, asset-quality erosion, writedown signatures
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Total assets QoQ / YoY contraction levels ---

def aqy_001_assets_level(assets: pd.Series) -> pd.Series:
    """Total assets level (Sharadar SF1 field). Provides the raw asset-base
    magnitude for scaling and ranking — distinct from any rate-of-change feature."""
    return assets.copy()


def aqy_002_assets_yoy_change(assets: pd.Series) -> pd.Series:
    """Total assets YoY absolute change (252-day lag)."""
    return assets - assets.shift(_TD_YEAR)


def aqy_003_assets_qoq_pct(assets: pd.Series) -> pd.Series:
    """Total assets QoQ percent change; denominator is abs(prior)."""
    prior = assets.shift(_TD_QTR)
    return _safe_div_abs(assets - prior, prior)


def aqy_004_assets_yoy_pct(assets: pd.Series) -> pd.Series:
    """Total assets YoY percent change; denominator is abs(prior)."""
    prior = assets.shift(_TD_YEAR)
    return _safe_div_abs(assets - prior, prior)


def aqy_005_assets_2y_change(assets: pd.Series) -> pd.Series:
    """Total assets change over 2 years (504-day lag)."""
    return assets - assets.shift(_TD_2Y)


def aqy_006_assets_3y_change(assets: pd.Series) -> pd.Series:
    """Total assets change over 3 years (756-day lag)."""
    return assets - assets.shift(_TD_3Y)


def aqy_007_assets_2y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 2-year percent change."""
    prior = assets.shift(_TD_2Y)
    return _safe_div_abs(assets - prior, prior)


def aqy_008_assets_3y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 3-year percent change."""
    prior = assets.shift(_TD_3Y)
    return _safe_div_abs(assets - prior, prior)


def aqy_009_assetsnc_qoq_change(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets QoQ absolute change."""
    return assetsnc - assetsnc.shift(_TD_QTR)


def aqy_010_assetsnc_yoy_change(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets YoY absolute change."""
    return assetsnc - assetsnc.shift(_TD_YEAR)


def aqy_011_assetsnc_qoq_pct(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets QoQ percent change."""
    prior = assetsnc.shift(_TD_QTR)
    return _safe_div_abs(assetsnc - prior, prior)


def aqy_012_assetsc_qoq_change(assetsc: pd.Series) -> pd.Series:
    """Current assets QoQ absolute change."""
    return assetsc - assetsc.shift(_TD_QTR)


def aqy_013_assetsc_yoy_change(assetsc: pd.Series) -> pd.Series:
    """Current assets YoY absolute change."""
    return assetsc - assetsc.shift(_TD_YEAR)


def aqy_014_assetsc_qoq_pct(assetsc: pd.Series) -> pd.Series:
    """Current assets QoQ percent change."""
    prior = assetsc.shift(_TD_QTR)
    return _safe_div_abs(assetsc - prior, prior)


def aqy_015_assets_contracting_flag(assets: pd.Series) -> pd.Series:
    """Binary: 1 if total assets are below their prior-quarter level."""
    return (assets < assets.shift(_TD_QTR)).astype(float)


# --- Group B (016-030): Asset drawdown from trailing peaks ---

def aqy_016_assets_drawdown_from_4q_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its 4-quarter (252-day) rolling peak (level drawdown)."""
    peak = _rolling_max(assets, _TD_YEAR)
    return assets - peak


def aqy_017_assets_drawdown_from_8q_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its 8-quarter (504-day) rolling peak."""
    peak = _rolling_max(assets, _TD_2Y)
    return assets - peak


def aqy_018_assets_drawdown_from_12q_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its 12-quarter (756-day) rolling peak."""
    peak = _rolling_max(assets, _TD_3Y)
    return assets - peak


def aqy_019_assets_pct_drawdown_from_4q_peak(assets: pd.Series) -> pd.Series:
    """Total assets percent drawdown from 4-quarter peak."""
    peak = _rolling_max(assets, _TD_YEAR)
    return _safe_div_abs(assets - peak, peak)


def aqy_020_assets_pct_drawdown_from_8q_peak(assets: pd.Series) -> pd.Series:
    """Total assets percent drawdown from 8-quarter peak."""
    peak = _rolling_max(assets, _TD_2Y)
    return _safe_div_abs(assets - peak, peak)


def aqy_021_assets_pct_drawdown_from_12q_peak(assets: pd.Series) -> pd.Series:
    """Total assets percent drawdown from 12-quarter peak."""
    peak = _rolling_max(assets, _TD_3Y)
    return _safe_div_abs(assets - peak, peak)


def aqy_022_assets_drawdown_from_expanding_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its all-history expanding maximum."""
    peak = assets.expanding(min_periods=1).max()
    return assets - peak


def aqy_023_assets_pct_drawdown_from_expanding_peak(assets: pd.Series) -> pd.Series:
    """Total assets percent drawdown from all-history expanding peak."""
    peak = assets.expanding(min_periods=1).max()
    return _safe_div_abs(assets - peak, peak)


def aqy_024_assetsnc_drawdown_from_4q_peak(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets level drawdown from 4-quarter peak."""
    peak = _rolling_max(assetsnc, _TD_YEAR)
    return assetsnc - peak


def aqy_025_tangibles_drawdown_from_4q_peak(tangibles: pd.Series) -> pd.Series:
    """Tangible assets level drawdown from 4-quarter peak."""
    peak = _rolling_max(tangibles, _TD_YEAR)
    return tangibles - peak


def aqy_026_tangibles_drawdown_from_8q_peak(tangibles: pd.Series) -> pd.Series:
    """Tangible assets level drawdown from 8-quarter peak."""
    peak = _rolling_max(tangibles, _TD_2Y)
    return tangibles - peak


def aqy_027_tangibles_pct_drawdown_from_4q_peak(tangibles: pd.Series) -> pd.Series:
    """Tangible assets percent drawdown from 4-quarter peak."""
    peak = _rolling_max(tangibles, _TD_YEAR)
    return _safe_div_abs(tangibles - peak, peak)


def aqy_028_ppnenet_drawdown_from_4q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E level drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(ppnenet, _TD_YEAR)
    return ppnenet - peak


def aqy_029_ppnenet_drawdown_from_8q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E level drawdown from 8-quarter rolling peak."""
    peak = _rolling_max(ppnenet, _TD_2Y)
    return ppnenet - peak


def aqy_030_ppnenet_pct_drawdown_from_4q_peak(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(ppnenet, _TD_YEAR)
    return _safe_div_abs(ppnenet - peak, peak)


# --- Group C (031-045): Intangibles / goodwill writedown signatures ---

def aqy_031_intangibles_qoq_change(intangibles: pd.Series) -> pd.Series:
    """Intangibles QoQ absolute change; large negative = goodwill/intangible writedown."""
    return intangibles - intangibles.shift(_TD_QTR)


def aqy_032_intangibles_yoy_change(intangibles: pd.Series) -> pd.Series:
    """Intangibles YoY absolute change."""
    return intangibles - intangibles.shift(_TD_YEAR)


def aqy_033_intangibles_qoq_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles QoQ percent change; large negative = writedown event."""
    prior = intangibles.shift(_TD_QTR)
    return _safe_div_abs(intangibles - prior, prior)


def aqy_034_intangibles_yoy_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles YoY percent change."""
    prior = intangibles.shift(_TD_YEAR)
    return _safe_div_abs(intangibles - prior, prior)


def aqy_035_intangibles_to_assets_ratio(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles as a fraction of total assets (soft-asset intensity)."""
    return _safe_div(intangibles, assets)


def aqy_036_intangibles_to_assets_zscore_4q(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Z-score of the intangibles-to-assets ratio within a trailing 4-quarter (252-day) window.
    High positive z-score = soft-asset intensity near its worst (most elevated) recent level.
    """
    ratio = _safe_div(intangibles, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def aqy_037_intangibles_drawdown_from_4q_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles level drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(intangibles, _TD_YEAR)
    return intangibles - peak


def aqy_038_intangibles_drawdown_from_8q_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles level drawdown from 8-quarter rolling peak."""
    peak = _rolling_max(intangibles, _TD_2Y)
    return intangibles - peak


def aqy_039_intangibles_writedown_flag(intangibles: pd.Series) -> pd.Series:
    """1 if intangibles dropped more than 10% QoQ (writedown signal)."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    return (pct < -0.10).astype(float)


def aqy_040_intangibles_large_writedown_flag(intangibles: pd.Series) -> pd.Series:
    """1 if intangibles dropped more than 25% QoQ (severe writedown signal)."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    return (pct < -0.25).astype(float)


def aqy_041_intangibles_writedown_count_4q(intangibles: pd.Series) -> pd.Series:
    """Count of quarters in trailing 4Q where intangibles fell >10% QoQ."""
    pct = _safe_div_abs(intangibles - intangibles.shift(_TD_QTR), intangibles.shift(_TD_QTR))
    flag = (pct < -0.10).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_042_intangibles_vs_4q_avg(intangibles: pd.Series) -> pd.Series:
    """Intangibles minus its trailing 4-quarter mean (level deviation)."""
    return intangibles - _rolling_mean(intangibles, _TD_YEAR)


def aqy_043_intangibles_zscore_4q(intangibles: pd.Series) -> pd.Series:
    """Z-score of intangibles in trailing 4-quarter (252-day) window."""
    return _zscore_rolling(intangibles, _TD_YEAR)


def aqy_044_intangibles_2y_pct(intangibles: pd.Series) -> pd.Series:
    """Intangibles 2-year percent change."""
    prior = intangibles.shift(_TD_2Y)
    return _safe_div_abs(intangibles - prior, prior)


def aqy_045_intangibles_pct_drawdown_from_expanding_peak(intangibles: pd.Series) -> pd.Series:
    """Intangibles percent drawdown from all-history expanding peak."""
    peak = intangibles.expanding(min_periods=1).max()
    return _safe_div_abs(intangibles - peak, peak)


# --- Group D (046-060): PP&E contraction and depamor burden ---

def aqy_046_ppnenet_qoq_change(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E QoQ absolute change."""
    return ppnenet - ppnenet.shift(_TD_QTR)


def aqy_047_ppnenet_yoy_change(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E YoY absolute change."""
    return ppnenet - ppnenet.shift(_TD_YEAR)


def aqy_048_ppnenet_qoq_pct(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E QoQ percent change."""
    prior = ppnenet.shift(_TD_QTR)
    return _safe_div_abs(ppnenet - prior, prior)


def aqy_049_ppnenet_yoy_pct(ppnenet: pd.Series) -> pd.Series:
    """Net PP&E YoY percent change."""
    prior = ppnenet.shift(_TD_YEAR)
    return _safe_div_abs(ppnenet - prior, prior)


def aqy_050_ppnenet_to_assets_ratio(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Net PP&E as fraction of total assets (hard-asset intensity)."""
    return _safe_div(ppnenet, assets)


def aqy_051_ppnenet_to_assets_qoq_change(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in PP&E-to-assets ratio (falling = hard-asset base eroding)."""
    ratio = _safe_div(ppnenet, assets)
    return ratio - ratio.shift(_TD_QTR)


def aqy_052_depamor_to_ppnenet_ratio(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """Depreciation & amortization relative to net PP&E; rising = aging asset base."""
    return _safe_div(depamor, ppnenet)


def aqy_053_depamor_to_ppnenet_zscore_4q(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """
    Z-score of the depamor/ppnenet ratio within a trailing 4-quarter (252-day) window.
    High positive z-score = D&A burden on net PP&E is near its worst recent level
    (aging asset base relative to carrying value).
    """
    ratio = _safe_div(depamor, ppnenet)
    return _zscore_rolling(ratio, _TD_YEAR)


def aqy_054_depamor_to_assets_ratio(depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """Depreciation & amortization as fraction of total assets."""
    return _safe_div(depamor, assets)


def aqy_055_capex_to_depamor_ratio(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Capital expenditures relative to D&A; <1 = insufficient reinvestment."""
    return _safe_div(capex.abs(), depamor.abs())


def aqy_056_capex_to_depamor_pct_rank_8q(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """
    Percentile rank of the capex/depamor ratio within a trailing 8-quarter (504-day) window.
    Low rank = reinvestment coverage near its weakest level over 2 years (underinvestment stress).
    """
    ratio = _safe_div(capex.abs(), depamor.abs())
    return _rolling_rank_pct(ratio, _TD_2Y)


def aqy_057_ppnenet_contracting_flag(ppnenet: pd.Series) -> pd.Series:
    """Binary: 1 if net PP&E is below its prior-quarter level."""
    return (ppnenet < ppnenet.shift(_TD_QTR)).astype(float)


def aqy_058_ppnenet_consecutive_contraction_streak(ppnenet: pd.Series) -> pd.Series:
    """
    Current consecutive-quarter PP&E contraction streak (in daily observations).
    Resets to 0 on any quarter where PP&E did not decline.
    """
    contracting = (ppnenet < ppnenet.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(contracting), dtype=float)
    arr = contracting.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ppnenet.index)


def aqy_059_depamor_yoy_change(depamor: pd.Series) -> pd.Series:
    """Depreciation & amortization YoY absolute change (rising = asset base aging)."""
    return depamor - depamor.shift(_TD_YEAR)


def aqy_060_depamor_zscore_4q(depamor: pd.Series) -> pd.Series:
    """Z-score of D&A within trailing 4-quarter window."""
    return _zscore_rolling(depamor, _TD_YEAR)


# --- Group E (061-075): Asset composition, inventory, investments, and composites ---

def aqy_061_tangibles_to_assets_ratio(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Tangible assets as fraction of total assets (hard-asset share)."""
    return _safe_div(tangibles, assets)


def aqy_062_tangibles_to_assets_pct_rank_4q(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Percentile rank of the tangibles-to-assets ratio within a trailing 4-quarter (252-day)
    window.  Low rank = hard-asset share near its weakest recent level.
    """
    ratio = _safe_div(tangibles, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def aqy_063_tangibles_to_assets_pct_rank_8q(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Percentile rank of the tangibles-to-assets ratio within a trailing 8-quarter (504-day)
    window.  Low rank = hard-asset share near its weakest level over 2 years.
    """
    ratio = _safe_div(tangibles, assets)
    return _rolling_rank_pct(ratio, _TD_2Y)


def aqy_064_inventory_qoq_change(inventory: pd.Series) -> pd.Series:
    """Inventory QoQ absolute change; large drops may signal writedowns."""
    return inventory - inventory.shift(_TD_QTR)


def aqy_065_inventory_qoq_pct(inventory: pd.Series) -> pd.Series:
    """Inventory QoQ percent change."""
    prior = inventory.shift(_TD_QTR)
    return _safe_div_abs(inventory - prior, prior)


def aqy_066_inventory_to_assets_ratio(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """Inventory as fraction of total assets."""
    return _safe_div(inventory, assets)


def aqy_067_inventory_writedown_flag(inventory: pd.Series) -> pd.Series:
    """1 if inventory dropped more than 15% QoQ (potential writedown)."""
    pct = _safe_div_abs(inventory - inventory.shift(_TD_QTR), inventory.shift(_TD_QTR))
    return (pct < -0.15).astype(float)


def aqy_068_investmentsnc_qoq_change(investmentsnc: pd.Series) -> pd.Series:
    """Non-current investments QoQ absolute change."""
    return investmentsnc - investmentsnc.shift(_TD_QTR)


def aqy_069_investmentsnc_yoy_change(investmentsnc: pd.Series) -> pd.Series:
    """Non-current investments YoY absolute change."""
    return investmentsnc - investmentsnc.shift(_TD_YEAR)


def aqy_070_investmentsnc_to_assets_ratio(investmentsnc: pd.Series, assets: pd.Series) -> pd.Series:
    """Non-current investments as fraction of total assets."""
    return _safe_div(investmentsnc, assets)


def aqy_071_assets_consecutive_contraction_quarters(assets: pd.Series) -> pd.Series:
    """
    Current consecutive-quarter total-asset contraction streak (daily count).
    Resets to 0 on any quarter where assets did not decline.
    """
    contracting = (assets < assets.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(contracting), dtype=float)
    arr = contracting.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assets.index)


def aqy_072_assets_contraction_count_4q(assets: pd.Series) -> pd.Series:
    """Number of trailing 4Q periods where assets contracted QoQ."""
    flag = (assets < assets.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_073_assets_contraction_count_8q(assets: pd.Series) -> pd.Series:
    """Number of trailing 8Q periods where assets contracted QoQ."""
    flag = (assets < assets.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def aqy_074_asset_quality_composite_zscore(
    assets: pd.Series,
    intangibles: pd.Series,
    ppnenet: pd.Series,
) -> pd.Series:
    """
    Composite asset-quality erosion score: equally weighted sum of z-scores
    of (assets, -intangibles_share, ppnenet) in a 4-quarter rolling window.
    Negative values indicate deteriorating asset quality.
    """
    z_assets = _zscore_rolling(assets, _TD_YEAR)
    intang_share = _safe_div(intangibles, assets)
    z_intang  = _zscore_rolling(intang_share, _TD_YEAR)
    z_ppne    = _zscore_rolling(ppnenet, _TD_YEAR)
    return (z_assets - z_intang + z_ppne) / 3.0


def aqy_075_hard_vs_soft_asset_ratio(
    tangibles: pd.Series,
    intangibles: pd.Series,
) -> pd.Series:
    """
    Ratio of tangible (hard) to intangible (soft) assets.
    Declining ratio indicates increasing reliance on soft assets.
    """
    return _safe_div(tangibles, intangibles)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

ASSET_QUALITY_REGISTRY_001_075 = {
    "aqy_001_assets_level":                              {"inputs": ["assets"],                              "func": aqy_001_assets_level},
    "aqy_002_assets_yoy_change":                         {"inputs": ["assets"],                              "func": aqy_002_assets_yoy_change},
    "aqy_003_assets_qoq_pct":                            {"inputs": ["assets"],                              "func": aqy_003_assets_qoq_pct},
    "aqy_004_assets_yoy_pct":                            {"inputs": ["assets"],                              "func": aqy_004_assets_yoy_pct},
    "aqy_005_assets_2y_change":                          {"inputs": ["assets"],                              "func": aqy_005_assets_2y_change},
    "aqy_006_assets_3y_change":                          {"inputs": ["assets"],                              "func": aqy_006_assets_3y_change},
    "aqy_007_assets_2y_pct":                             {"inputs": ["assets"],                              "func": aqy_007_assets_2y_pct},
    "aqy_008_assets_3y_pct":                             {"inputs": ["assets"],                              "func": aqy_008_assets_3y_pct},
    "aqy_009_assetsnc_qoq_change":                       {"inputs": ["assetsnc"],                           "func": aqy_009_assetsnc_qoq_change},
    "aqy_010_assetsnc_yoy_change":                       {"inputs": ["assetsnc"],                           "func": aqy_010_assetsnc_yoy_change},
    "aqy_011_assetsnc_qoq_pct":                          {"inputs": ["assetsnc"],                           "func": aqy_011_assetsnc_qoq_pct},
    "aqy_012_assetsc_qoq_change":                        {"inputs": ["assetsc"],                            "func": aqy_012_assetsc_qoq_change},
    "aqy_013_assetsc_yoy_change":                        {"inputs": ["assetsc"],                            "func": aqy_013_assetsc_yoy_change},
    "aqy_014_assetsc_qoq_pct":                           {"inputs": ["assetsc"],                            "func": aqy_014_assetsc_qoq_pct},
    "aqy_015_assets_contracting_flag":                   {"inputs": ["assets"],                              "func": aqy_015_assets_contracting_flag},
    "aqy_016_assets_drawdown_from_4q_peak":              {"inputs": ["assets"],                              "func": aqy_016_assets_drawdown_from_4q_peak},
    "aqy_017_assets_drawdown_from_8q_peak":              {"inputs": ["assets"],                              "func": aqy_017_assets_drawdown_from_8q_peak},
    "aqy_018_assets_drawdown_from_12q_peak":             {"inputs": ["assets"],                              "func": aqy_018_assets_drawdown_from_12q_peak},
    "aqy_019_assets_pct_drawdown_from_4q_peak":          {"inputs": ["assets"],                              "func": aqy_019_assets_pct_drawdown_from_4q_peak},
    "aqy_020_assets_pct_drawdown_from_8q_peak":          {"inputs": ["assets"],                              "func": aqy_020_assets_pct_drawdown_from_8q_peak},
    "aqy_021_assets_pct_drawdown_from_12q_peak":         {"inputs": ["assets"],                              "func": aqy_021_assets_pct_drawdown_from_12q_peak},
    "aqy_022_assets_drawdown_from_expanding_peak":       {"inputs": ["assets"],                              "func": aqy_022_assets_drawdown_from_expanding_peak},
    "aqy_023_assets_pct_drawdown_from_expanding_peak":   {"inputs": ["assets"],                              "func": aqy_023_assets_pct_drawdown_from_expanding_peak},
    "aqy_024_assetsnc_drawdown_from_4q_peak":            {"inputs": ["assetsnc"],                           "func": aqy_024_assetsnc_drawdown_from_4q_peak},
    "aqy_025_tangibles_drawdown_from_4q_peak":           {"inputs": ["tangibles"],                          "func": aqy_025_tangibles_drawdown_from_4q_peak},
    "aqy_026_tangibles_drawdown_from_8q_peak":           {"inputs": ["tangibles"],                          "func": aqy_026_tangibles_drawdown_from_8q_peak},
    "aqy_027_tangibles_pct_drawdown_from_4q_peak":       {"inputs": ["tangibles"],                          "func": aqy_027_tangibles_pct_drawdown_from_4q_peak},
    "aqy_028_ppnenet_drawdown_from_4q_peak":             {"inputs": ["ppnenet"],                            "func": aqy_028_ppnenet_drawdown_from_4q_peak},
    "aqy_029_ppnenet_drawdown_from_8q_peak":             {"inputs": ["ppnenet"],                            "func": aqy_029_ppnenet_drawdown_from_8q_peak},
    "aqy_030_ppnenet_pct_drawdown_from_4q_peak":         {"inputs": ["ppnenet"],                            "func": aqy_030_ppnenet_pct_drawdown_from_4q_peak},
    "aqy_031_intangibles_qoq_change":                    {"inputs": ["intangibles"],                        "func": aqy_031_intangibles_qoq_change},
    "aqy_032_intangibles_yoy_change":                    {"inputs": ["intangibles"],                        "func": aqy_032_intangibles_yoy_change},
    "aqy_033_intangibles_qoq_pct":                       {"inputs": ["intangibles"],                        "func": aqy_033_intangibles_qoq_pct},
    "aqy_034_intangibles_yoy_pct":                       {"inputs": ["intangibles"],                        "func": aqy_034_intangibles_yoy_pct},
    "aqy_035_intangibles_to_assets_ratio":               {"inputs": ["intangibles", "assets"],              "func": aqy_035_intangibles_to_assets_ratio},
    "aqy_036_intangibles_to_assets_zscore_4q":           {"inputs": ["intangibles", "assets"],              "func": aqy_036_intangibles_to_assets_zscore_4q},
    "aqy_037_intangibles_drawdown_from_4q_peak":         {"inputs": ["intangibles"],                        "func": aqy_037_intangibles_drawdown_from_4q_peak},
    "aqy_038_intangibles_drawdown_from_8q_peak":         {"inputs": ["intangibles"],                        "func": aqy_038_intangibles_drawdown_from_8q_peak},
    "aqy_039_intangibles_writedown_flag":                {"inputs": ["intangibles"],                        "func": aqy_039_intangibles_writedown_flag},
    "aqy_040_intangibles_large_writedown_flag":          {"inputs": ["intangibles"],                        "func": aqy_040_intangibles_large_writedown_flag},
    "aqy_041_intangibles_writedown_count_4q":            {"inputs": ["intangibles"],                        "func": aqy_041_intangibles_writedown_count_4q},
    "aqy_042_intangibles_vs_4q_avg":                     {"inputs": ["intangibles"],                        "func": aqy_042_intangibles_vs_4q_avg},
    "aqy_043_intangibles_zscore_4q":                     {"inputs": ["intangibles"],                        "func": aqy_043_intangibles_zscore_4q},
    "aqy_044_intangibles_2y_pct":                        {"inputs": ["intangibles"],                        "func": aqy_044_intangibles_2y_pct},
    "aqy_045_intangibles_pct_drawdown_from_expanding_peak": {"inputs": ["intangibles"],                     "func": aqy_045_intangibles_pct_drawdown_from_expanding_peak},
    "aqy_046_ppnenet_qoq_change":                        {"inputs": ["ppnenet"],                            "func": aqy_046_ppnenet_qoq_change},
    "aqy_047_ppnenet_yoy_change":                        {"inputs": ["ppnenet"],                            "func": aqy_047_ppnenet_yoy_change},
    "aqy_048_ppnenet_qoq_pct":                           {"inputs": ["ppnenet"],                            "func": aqy_048_ppnenet_qoq_pct},
    "aqy_049_ppnenet_yoy_pct":                           {"inputs": ["ppnenet"],                            "func": aqy_049_ppnenet_yoy_pct},
    "aqy_050_ppnenet_to_assets_ratio":                   {"inputs": ["ppnenet", "assets"],                  "func": aqy_050_ppnenet_to_assets_ratio},
    "aqy_051_ppnenet_to_assets_qoq_change":              {"inputs": ["ppnenet", "assets"],                  "func": aqy_051_ppnenet_to_assets_qoq_change},
    "aqy_052_depamor_to_ppnenet_ratio":                  {"inputs": ["depamor", "ppnenet"],                 "func": aqy_052_depamor_to_ppnenet_ratio},
    "aqy_053_depamor_to_ppnenet_zscore_4q":              {"inputs": ["depamor", "ppnenet"],                 "func": aqy_053_depamor_to_ppnenet_zscore_4q},
    "aqy_054_depamor_to_assets_ratio":                   {"inputs": ["depamor", "assets"],                  "func": aqy_054_depamor_to_assets_ratio},
    "aqy_055_capex_to_depamor_ratio":                    {"inputs": ["capex", "depamor"],                   "func": aqy_055_capex_to_depamor_ratio},
    "aqy_056_capex_to_depamor_pct_rank_8q":              {"inputs": ["capex", "depamor"],                   "func": aqy_056_capex_to_depamor_pct_rank_8q},
    "aqy_057_ppnenet_contracting_flag":                  {"inputs": ["ppnenet"],                            "func": aqy_057_ppnenet_contracting_flag},
    "aqy_058_ppnenet_consecutive_contraction_streak":    {"inputs": ["ppnenet"],                            "func": aqy_058_ppnenet_consecutive_contraction_streak},
    "aqy_059_depamor_yoy_change":                        {"inputs": ["depamor"],                            "func": aqy_059_depamor_yoy_change},
    "aqy_060_depamor_zscore_4q":                         {"inputs": ["depamor"],                            "func": aqy_060_depamor_zscore_4q},
    "aqy_061_tangibles_to_assets_ratio":                 {"inputs": ["tangibles", "assets"],                "func": aqy_061_tangibles_to_assets_ratio},
    "aqy_062_tangibles_to_assets_pct_rank_4q":           {"inputs": ["tangibles", "assets"],                "func": aqy_062_tangibles_to_assets_pct_rank_4q},
    "aqy_063_tangibles_to_assets_pct_rank_8q":           {"inputs": ["tangibles", "assets"],                "func": aqy_063_tangibles_to_assets_pct_rank_8q},
    "aqy_064_inventory_qoq_change":                      {"inputs": ["inventory"],                          "func": aqy_064_inventory_qoq_change},
    "aqy_065_inventory_qoq_pct":                         {"inputs": ["inventory"],                          "func": aqy_065_inventory_qoq_pct},
    "aqy_066_inventory_to_assets_ratio":                 {"inputs": ["inventory", "assets"],                "func": aqy_066_inventory_to_assets_ratio},
    "aqy_067_inventory_writedown_flag":                  {"inputs": ["inventory"],                          "func": aqy_067_inventory_writedown_flag},
    "aqy_068_investmentsnc_qoq_change":                  {"inputs": ["investmentsnc"],                      "func": aqy_068_investmentsnc_qoq_change},
    "aqy_069_investmentsnc_yoy_change":                  {"inputs": ["investmentsnc"],                      "func": aqy_069_investmentsnc_yoy_change},
    "aqy_070_investmentsnc_to_assets_ratio":             {"inputs": ["investmentsnc", "assets"],            "func": aqy_070_investmentsnc_to_assets_ratio},
    "aqy_071_assets_consecutive_contraction_quarters":   {"inputs": ["assets"],                             "func": aqy_071_assets_consecutive_contraction_quarters},
    "aqy_072_assets_contraction_count_4q":               {"inputs": ["assets"],                             "func": aqy_072_assets_contraction_count_4q},
    "aqy_073_assets_contraction_count_8q":               {"inputs": ["assets"],                             "func": aqy_073_assets_contraction_count_8q},
    "aqy_074_asset_quality_composite_zscore":            {"inputs": ["assets", "intangibles", "ppnenet"],   "func": aqy_074_asset_quality_composite_zscore},
    "aqy_075_hard_vs_soft_asset_ratio":                  {"inputs": ["tangibles", "intangibles"],           "func": aqy_075_hard_vs_soft_asset_ratio},
}
