"""
68_asset_quality — Base Features 076-150
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Asset-base speed and acceleration of contraction ---

def aqy_076_assets_qoq_change_rolling_mean_4q(assets: pd.Series) -> pd.Series:
    """Rolling 4-quarter mean of the QoQ asset change (trend in contraction rate)."""
    qoq = assets - assets.shift(_TD_QTR)
    return _rolling_mean(qoq, _TD_YEAR)


def aqy_077_assets_qoq_change_rolling_mean_8q(assets: pd.Series) -> pd.Series:
    """Rolling 8-quarter mean of the QoQ asset change."""
    qoq = assets - assets.shift(_TD_QTR)
    return _rolling_mean(qoq, _TD_2Y)


def aqy_078_assets_range_position_8q(assets: pd.Series) -> pd.Series:
    """
    Position of total assets within its trailing 8-quarter [min, max] range:
    (assets - min) / (max - min).  0.0 = at 8-quarter low (maximum contraction stress).
    """
    lo = _rolling_min(assets, _TD_2Y)
    hi = _rolling_max(assets, _TD_2Y)
    return _safe_div(assets - lo, hi - lo)


def aqy_079_assets_qoq_pct_rolling_mean_4q(assets: pd.Series) -> pd.Series:
    """Rolling 4-quarter mean of QoQ percent asset change."""
    prior = assets.shift(_TD_QTR)
    qoq_pct = _safe_div_abs(assets - prior, prior)
    return _rolling_mean(qoq_pct, _TD_YEAR)


def aqy_080_assets_zscore_4q(assets: pd.Series) -> pd.Series:
    """Z-score of total assets in trailing 4-quarter (252-day) window."""
    return _zscore_rolling(assets, _TD_YEAR)


def aqy_081_assets_zscore_8q(assets: pd.Series) -> pd.Series:
    """Z-score of total assets in trailing 8-quarter (504-day) window."""
    return _zscore_rolling(assets, _TD_2Y)


def aqy_082_assets_zscore_12q(assets: pd.Series) -> pd.Series:
    """Z-score of total assets in trailing 12-quarter (756-day) window."""
    return _zscore_rolling(assets, _TD_3Y)


def aqy_083_assets_expanding_zscore(assets: pd.Series) -> pd.Series:
    """Expanding z-score of total assets (how extreme vs entire history)."""
    m  = assets.expanding(min_periods=2).mean()
    sd = assets.expanding(min_periods=2).std()
    return _safe_div(assets - m, sd)


def aqy_084_assets_pct_rank_4q(assets: pd.Series) -> pd.Series:
    """Percentile rank of total assets within trailing 4-quarter window."""
    return _rolling_rank_pct(assets, _TD_YEAR)


def aqy_085_assets_pct_rank_8q(assets: pd.Series) -> pd.Series:
    """Percentile rank of total assets within trailing 8-quarter window."""
    return _rolling_rank_pct(assets, _TD_2Y)


def aqy_086_assets_pct_rank_12q(assets: pd.Series) -> pd.Series:
    """Percentile rank of total assets within trailing 12-quarter window."""
    return _rolling_rank_pct(assets, _TD_3Y)


def aqy_087_assets_expanding_pct_rank(assets: pd.Series) -> pd.Series:
    """Expanding percentile rank of total assets (all-history rank)."""
    return assets.expanding(min_periods=2).rank(pct=True)


def aqy_088_assets_ewm_deviation(assets: pd.Series) -> pd.Series:
    """Total assets minus its 4-quarter EWM (span=252); captures asset momentum shift."""
    ewm = _ewm_mean(assets, _TD_YEAR)
    return assets - ewm


def aqy_089_assetsnc_pct_drawdown_from_4q_peak(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets percent drawdown from 4-quarter peak."""
    peak = _rolling_max(assetsnc, _TD_YEAR)
    return _safe_div_abs(assetsnc - peak, peak)


def aqy_090_assetsnc_pct_drawdown_from_expanding_peak(assetsnc: pd.Series) -> pd.Series:
    """Non-current assets percent drawdown from all-history expanding peak."""
    peak = assetsnc.expanding(min_periods=1).max()
    return _safe_div_abs(assetsnc - peak, peak)


# --- Group G (091-105): Receivables and current-asset quality ---

def aqy_091_receivables_qoq_change(receivables: pd.Series) -> pd.Series:
    """Receivables QoQ absolute change."""
    return receivables - receivables.shift(_TD_QTR)


def aqy_092_receivables_yoy_change(receivables: pd.Series) -> pd.Series:
    """Receivables YoY absolute change."""
    return receivables - receivables.shift(_TD_YEAR)


def aqy_093_receivables_to_assets_ratio(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Receivables as fraction of total assets."""
    return _safe_div(receivables, assets)


def aqy_094_receivables_to_assets_qoq_change(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in receivables-to-assets ratio."""
    ratio = _safe_div(receivables, assets)
    return ratio - ratio.shift(_TD_QTR)


def aqy_095_receivables_drawdown_from_4q_peak(receivables: pd.Series) -> pd.Series:
    """Receivables level drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(receivables, _TD_YEAR)
    return receivables - peak


def aqy_096_receivables_zscore_4q(receivables: pd.Series) -> pd.Series:
    """Z-score of receivables in trailing 4-quarter window."""
    return _zscore_rolling(receivables, _TD_YEAR)


def aqy_097_assetsc_to_assets_ratio(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current assets as fraction of total assets (liquidity mix)."""
    return _safe_div(assetsc, assets)


def aqy_098_assetsc_to_assets_qoq_change(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in current-assets-to-assets ratio."""
    ratio = _safe_div(assetsc, assets)
    return ratio - ratio.shift(_TD_QTR)


def aqy_099_inventory_yoy_change(inventory: pd.Series) -> pd.Series:
    """Inventory YoY absolute change."""
    return inventory - inventory.shift(_TD_YEAR)


def aqy_100_inventory_drawdown_from_4q_peak(inventory: pd.Series) -> pd.Series:
    """Inventory level drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(inventory, _TD_YEAR)
    return inventory - peak


def aqy_101_inventory_pct_drawdown_from_4q_peak(inventory: pd.Series) -> pd.Series:
    """Inventory percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(inventory, _TD_YEAR)
    return _safe_div_abs(inventory - peak, peak)


def aqy_102_inventory_zscore_4q(inventory: pd.Series) -> pd.Series:
    """Z-score of inventory in trailing 4-quarter window."""
    return _zscore_rolling(inventory, _TD_YEAR)


def aqy_103_inventory_large_drop_count_4q(inventory: pd.Series) -> pd.Series:
    """Count of trailing 4Q periods where inventory fell more than 15% QoQ."""
    pct = _safe_div_abs(inventory - inventory.shift(_TD_QTR), inventory.shift(_TD_QTR))
    flag = (pct < -0.15).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_104_cashnequiv_to_assets_ratio(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Cash & equivalents as fraction of total assets (liquid asset quality)."""
    return _safe_div(cashnequiv, assets)


def aqy_105_cashnequiv_to_assets_qoq_change(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in cash-to-assets ratio (declining = cash burning)."""
    ratio = _safe_div(cashnequiv, assets)
    return ratio - ratio.shift(_TD_QTR)


# --- Group H (106-120): Investment portfolio and capex contraction ---

def aqy_106_investmentsnc_pct_drawdown_from_4q_peak(investmentsnc: pd.Series) -> pd.Series:
    """Non-current investments percent drawdown from 4-quarter rolling peak."""
    peak = _rolling_max(investmentsnc, _TD_YEAR)
    return _safe_div_abs(investmentsnc - peak, peak)


def aqy_107_investmentsnc_zscore_4q(investmentsnc: pd.Series) -> pd.Series:
    """Z-score of non-current investments in trailing 4-quarter window."""
    return _zscore_rolling(investmentsnc, _TD_YEAR)


def aqy_108_investmentsnc_contracting_flag(investmentsnc: pd.Series) -> pd.Series:
    """Binary: 1 if non-current investments are below their prior-quarter level."""
    return (investmentsnc < investmentsnc.shift(_TD_QTR)).astype(float)


def aqy_109_investmentsc_qoq_change(investmentsc: pd.Series) -> pd.Series:
    """Current investments QoQ absolute change."""
    return investmentsc - investmentsc.shift(_TD_QTR)


def aqy_110_investmentsc_to_assets_ratio(investmentsc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current investments as fraction of total assets."""
    return _safe_div(investmentsc, assets)


def aqy_111_capex_qoq_change(capex: pd.Series) -> pd.Series:
    """Capital expenditures QoQ absolute change (capex may be negative in SF1)."""
    return capex - capex.shift(_TD_QTR)


def aqy_112_capex_yoy_change(capex: pd.Series) -> pd.Series:
    """Capital expenditures YoY absolute change."""
    return capex - capex.shift(_TD_YEAR)


def aqy_113_capex_to_assets_ratio(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """Capex intensity relative to total assets."""
    return _safe_div(capex.abs(), assets)


def aqy_114_capex_drawdown_from_4q_peak(capex: pd.Series) -> pd.Series:
    """Capex (absolute value) drawdown from 4-quarter rolling peak."""
    cap_abs = capex.abs()
    peak = _rolling_max(cap_abs, _TD_YEAR)
    return cap_abs - peak


def aqy_115_capex_pct_drawdown_from_4q_peak(capex: pd.Series) -> pd.Series:
    """Capex (absolute) percent drawdown from 4-quarter rolling peak."""
    cap_abs = capex.abs()
    peak = _rolling_max(cap_abs, _TD_YEAR)
    return _safe_div_abs(cap_abs - peak, peak)


def aqy_116_capex_zscore_4q(capex: pd.Series) -> pd.Series:
    """Z-score of capex (absolute value) in trailing 4-quarter window."""
    return _zscore_rolling(capex.abs(), _TD_YEAR)


def aqy_117_capex_contracting_flag(capex: pd.Series) -> pd.Series:
    """Binary: 1 if |capex| is lower than prior quarter (capex cutback)."""
    cap_abs = capex.abs()
    return (cap_abs < cap_abs.shift(_TD_QTR)).astype(float)


def aqy_118_capex_contraction_count_4q(capex: pd.Series) -> pd.Series:
    """Count of trailing 4Q where |capex| declined QoQ."""
    cap_abs = capex.abs()
    flag = (cap_abs < cap_abs.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_119_capex_to_revenue_ratio(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Capex intensity as fraction of revenue; declining = underinvestment."""
    return _safe_div(capex.abs(), revenue.abs())


def aqy_120_depamor_qoq_change(depamor: pd.Series) -> pd.Series:
    """D&A QoQ absolute change."""
    return depamor - depamor.shift(_TD_QTR)


# --- Group I (121-135): Multi-period asset erosion and ranking ---

def aqy_121_assets_worst_4q_low(assets: pd.Series) -> pd.Series:
    """Lowest total-assets level in trailing 4-quarter (252-day) window."""
    return _rolling_min(assets, _TD_YEAR)


def aqy_122_assets_worst_8q_low(assets: pd.Series) -> pd.Series:
    """Lowest total-assets level in trailing 8-quarter (504-day) window."""
    return _rolling_min(assets, _TD_2Y)


def aqy_123_assets_at_expanding_low_flag(assets: pd.Series) -> pd.Series:
    """Binary: 1 if current total assets equals the all-history expanding minimum."""
    expanding_min = assets.expanding(min_periods=1).min()
    return (assets <= expanding_min).astype(float)


def aqy_124_intangibles_contraction_count_4q(intangibles: pd.Series) -> pd.Series:
    """Count of trailing 4Q where intangibles declined QoQ."""
    flag = (intangibles < intangibles.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_125_intangibles_contraction_count_8q(intangibles: pd.Series) -> pd.Series:
    """Count of trailing 8Q where intangibles declined QoQ."""
    flag = (intangibles < intangibles.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def aqy_126_ppnenet_contraction_count_4q(ppnenet: pd.Series) -> pd.Series:
    """Count of trailing 4Q where PP&E declined QoQ."""
    flag = (ppnenet < ppnenet.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_127_ppnenet_zscore_4q(ppnenet: pd.Series) -> pd.Series:
    """Z-score of net PP&E in trailing 4-quarter window."""
    return _zscore_rolling(ppnenet, _TD_YEAR)


def aqy_128_ppnenet_zscore_8q(ppnenet: pd.Series) -> pd.Series:
    """Z-score of net PP&E in trailing 8-quarter window."""
    return _zscore_rolling(ppnenet, _TD_2Y)


def aqy_129_tangibles_zscore_4q(tangibles: pd.Series) -> pd.Series:
    """Z-score of tangible assets in trailing 4-quarter window."""
    return _zscore_rolling(tangibles, _TD_YEAR)


def aqy_130_tangibles_qoq_change(tangibles: pd.Series) -> pd.Series:
    """Tangible assets QoQ absolute change."""
    return tangibles - tangibles.shift(_TD_QTR)


def aqy_131_tangibles_yoy_change(tangibles: pd.Series) -> pd.Series:
    """Tangible assets YoY absolute change."""
    return tangibles - tangibles.shift(_TD_YEAR)


def aqy_132_tangibles_qoq_pct(tangibles: pd.Series) -> pd.Series:
    """Tangible assets QoQ percent change."""
    prior = tangibles.shift(_TD_QTR)
    return _safe_div_abs(tangibles - prior, prior)


def aqy_133_tangibles_yoy_pct(tangibles: pd.Series) -> pd.Series:
    """Tangible assets YoY percent change."""
    prior = tangibles.shift(_TD_YEAR)
    return _safe_div_abs(tangibles - prior, prior)


def aqy_134_tangibles_contraction_count_4q(tangibles: pd.Series) -> pd.Series:
    """Count of trailing 4Q where tangibles declined QoQ."""
    flag = (tangibles < tangibles.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def aqy_135_tangibles_2y_pct(tangibles: pd.Series) -> pd.Series:
    """Tangible assets 2-year percent change."""
    prior = tangibles.shift(_TD_2Y)
    return _safe_div_abs(tangibles - prior, prior)


# --- Group J (136-150): Cross-asset ratios, composites, and advanced signals ---

def aqy_136_intangibles_plus_goodwill_share(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles share of total assets; tracks soft-asset mix over time (zscore 4Q)."""
    ratio = _safe_div(intangibles, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def aqy_137_hard_asset_share_zscore_4q(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of tangibles-to-assets ratio in trailing 4-quarter window."""
    ratio = _safe_div(tangibles, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def aqy_138_hard_asset_share_pct_rank_4q(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of tangibles-to-assets in trailing 4-quarter window."""
    ratio = _safe_div(tangibles, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def aqy_139_depamor_to_revenue_ratio(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """D&A as fraction of revenue; rising indicates asset-burden relative to revenue."""
    return _safe_div(depamor, revenue.abs())


def aqy_140_depamor_to_revenue_qoq_change(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in D&A-to-revenue ratio."""
    ratio = _safe_div(depamor, revenue.abs())
    return ratio - ratio.shift(_TD_QTR)


def aqy_141_capex_minus_depamor_gap(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Capex minus D&A (net investment); negative = maintenance underspend."""
    return capex.abs() - depamor.abs()


def aqy_142_capex_minus_depamor_to_assets(capex: pd.Series, depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """Net investment (capex - depamor) as fraction of total assets."""
    net_inv = capex.abs() - depamor.abs()
    return _safe_div(net_inv, assets)


def aqy_143_asset_turnover_proxy(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Revenue divided by total assets (asset-utilization proxy)."""
    return _safe_div(revenue.abs(), assets)


def aqy_144_asset_turnover_pct_rank_8q(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Percentile rank of asset turnover (revenue/assets) within the trailing 8-quarter
    (504-day) window.  Low rank = asset utilization near its weakest level over 2 years.
    """
    ratio = _safe_div(revenue.abs(), assets)
    return _rolling_rank_pct(ratio, _TD_2Y)


def aqy_145_asset_turnover_zscore_4q(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of asset turnover in trailing 4-quarter window."""
    ratio = _safe_div(revenue.abs(), assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def aqy_146_asset_turnover_drawdown_from_4q_peak(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Asset turnover level drawdown from its 4-quarter rolling peak."""
    ratio = _safe_div(revenue.abs(), assets)
    peak = _rolling_max(ratio, _TD_YEAR)
    return ratio - peak


def aqy_147_assets_vs_4q_avg(assets: pd.Series) -> pd.Series:
    """Total assets minus trailing 4-quarter mean."""
    return assets - _rolling_mean(assets, _TD_YEAR)


def aqy_148_assets_vs_8q_avg(assets: pd.Series) -> pd.Series:
    """Total assets minus trailing 8-quarter mean."""
    return assets - _rolling_mean(assets, _TD_2Y)


def aqy_149_multi_asset_erosion_composite(
    assets: pd.Series,
    tangibles: pd.Series,
    ppnenet: pd.Series,
    intangibles: pd.Series,
) -> pd.Series:
    """
    Multi-asset erosion composite: z-score of (assets contraction + tangibles
    contraction + PP&E contraction - intangibles share) all in 4Q window.
    Combines four asset-quality dimensions into one severity signal.
    """
    z_a   = _zscore_rolling(assets,     _TD_YEAR)
    z_t   = _zscore_rolling(tangibles,  _TD_YEAR)
    z_p   = _zscore_rolling(ppnenet,    _TD_YEAR)
    intsh = _safe_div(intangibles, assets)
    z_i   = _zscore_rolling(intsh,      _TD_YEAR)
    return (z_a + z_t + z_p - z_i) / 4.0


def aqy_150_asset_quality_expanding_pct_rank(assets: pd.Series) -> pd.Series:
    """Expanding percentile rank of total assets (all-history rank; low = historic low)."""
    return assets.expanding(min_periods=2).rank(pct=True)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

ASSET_QUALITY_REGISTRY_076_150 = {
    "aqy_076_assets_qoq_change_rolling_mean_4q":         {"inputs": ["assets"],                                          "func": aqy_076_assets_qoq_change_rolling_mean_4q},
    "aqy_077_assets_qoq_change_rolling_mean_8q":         {"inputs": ["assets"],                                          "func": aqy_077_assets_qoq_change_rolling_mean_8q},
    "aqy_078_assets_range_position_8q":                  {"inputs": ["assets"],                                          "func": aqy_078_assets_range_position_8q},
    "aqy_079_assets_qoq_pct_rolling_mean_4q":            {"inputs": ["assets"],                                          "func": aqy_079_assets_qoq_pct_rolling_mean_4q},
    "aqy_080_assets_zscore_4q":                          {"inputs": ["assets"],                                          "func": aqy_080_assets_zscore_4q},
    "aqy_081_assets_zscore_8q":                          {"inputs": ["assets"],                                          "func": aqy_081_assets_zscore_8q},
    "aqy_082_assets_zscore_12q":                         {"inputs": ["assets"],                                          "func": aqy_082_assets_zscore_12q},
    "aqy_083_assets_expanding_zscore":                   {"inputs": ["assets"],                                          "func": aqy_083_assets_expanding_zscore},
    "aqy_084_assets_pct_rank_4q":                        {"inputs": ["assets"],                                          "func": aqy_084_assets_pct_rank_4q},
    "aqy_085_assets_pct_rank_8q":                        {"inputs": ["assets"],                                          "func": aqy_085_assets_pct_rank_8q},
    "aqy_086_assets_pct_rank_12q":                       {"inputs": ["assets"],                                          "func": aqy_086_assets_pct_rank_12q},
    "aqy_087_assets_expanding_pct_rank":                 {"inputs": ["assets"],                                          "func": aqy_087_assets_expanding_pct_rank},
    "aqy_088_assets_ewm_deviation":                      {"inputs": ["assets"],                                          "func": aqy_088_assets_ewm_deviation},
    "aqy_089_assetsnc_pct_drawdown_from_4q_peak":        {"inputs": ["assetsnc"],                                        "func": aqy_089_assetsnc_pct_drawdown_from_4q_peak},
    "aqy_090_assetsnc_pct_drawdown_from_expanding_peak": {"inputs": ["assetsnc"],                                        "func": aqy_090_assetsnc_pct_drawdown_from_expanding_peak},
    "aqy_091_receivables_qoq_change":                    {"inputs": ["receivables"],                                     "func": aqy_091_receivables_qoq_change},
    "aqy_092_receivables_yoy_change":                    {"inputs": ["receivables"],                                     "func": aqy_092_receivables_yoy_change},
    "aqy_093_receivables_to_assets_ratio":               {"inputs": ["receivables", "assets"],                           "func": aqy_093_receivables_to_assets_ratio},
    "aqy_094_receivables_to_assets_qoq_change":          {"inputs": ["receivables", "assets"],                           "func": aqy_094_receivables_to_assets_qoq_change},
    "aqy_095_receivables_drawdown_from_4q_peak":         {"inputs": ["receivables"],                                     "func": aqy_095_receivables_drawdown_from_4q_peak},
    "aqy_096_receivables_zscore_4q":                     {"inputs": ["receivables"],                                     "func": aqy_096_receivables_zscore_4q},
    "aqy_097_assetsc_to_assets_ratio":                   {"inputs": ["assetsc", "assets"],                               "func": aqy_097_assetsc_to_assets_ratio},
    "aqy_098_assetsc_to_assets_qoq_change":              {"inputs": ["assetsc", "assets"],                               "func": aqy_098_assetsc_to_assets_qoq_change},
    "aqy_099_inventory_yoy_change":                      {"inputs": ["inventory"],                                       "func": aqy_099_inventory_yoy_change},
    "aqy_100_inventory_drawdown_from_4q_peak":           {"inputs": ["inventory"],                                       "func": aqy_100_inventory_drawdown_from_4q_peak},
    "aqy_101_inventory_pct_drawdown_from_4q_peak":       {"inputs": ["inventory"],                                       "func": aqy_101_inventory_pct_drawdown_from_4q_peak},
    "aqy_102_inventory_zscore_4q":                       {"inputs": ["inventory"],                                       "func": aqy_102_inventory_zscore_4q},
    "aqy_103_inventory_large_drop_count_4q":             {"inputs": ["inventory"],                                       "func": aqy_103_inventory_large_drop_count_4q},
    "aqy_104_cashnequiv_to_assets_ratio":                {"inputs": ["cashnequiv", "assets"],                            "func": aqy_104_cashnequiv_to_assets_ratio},
    "aqy_105_cashnequiv_to_assets_qoq_change":           {"inputs": ["cashnequiv", "assets"],                            "func": aqy_105_cashnequiv_to_assets_qoq_change},
    "aqy_106_investmentsnc_pct_drawdown_from_4q_peak":   {"inputs": ["investmentsnc"],                                   "func": aqy_106_investmentsnc_pct_drawdown_from_4q_peak},
    "aqy_107_investmentsnc_zscore_4q":                   {"inputs": ["investmentsnc"],                                   "func": aqy_107_investmentsnc_zscore_4q},
    "aqy_108_investmentsnc_contracting_flag":            {"inputs": ["investmentsnc"],                                   "func": aqy_108_investmentsnc_contracting_flag},
    "aqy_109_investmentsc_qoq_change":                   {"inputs": ["investmentsc"],                                    "func": aqy_109_investmentsc_qoq_change},
    "aqy_110_investmentsc_to_assets_ratio":              {"inputs": ["investmentsc", "assets"],                          "func": aqy_110_investmentsc_to_assets_ratio},
    "aqy_111_capex_qoq_change":                          {"inputs": ["capex"],                                           "func": aqy_111_capex_qoq_change},
    "aqy_112_capex_yoy_change":                          {"inputs": ["capex"],                                           "func": aqy_112_capex_yoy_change},
    "aqy_113_capex_to_assets_ratio":                     {"inputs": ["capex", "assets"],                                 "func": aqy_113_capex_to_assets_ratio},
    "aqy_114_capex_drawdown_from_4q_peak":               {"inputs": ["capex"],                                           "func": aqy_114_capex_drawdown_from_4q_peak},
    "aqy_115_capex_pct_drawdown_from_4q_peak":           {"inputs": ["capex"],                                           "func": aqy_115_capex_pct_drawdown_from_4q_peak},
    "aqy_116_capex_zscore_4q":                           {"inputs": ["capex"],                                           "func": aqy_116_capex_zscore_4q},
    "aqy_117_capex_contracting_flag":                    {"inputs": ["capex"],                                           "func": aqy_117_capex_contracting_flag},
    "aqy_118_capex_contraction_count_4q":                {"inputs": ["capex"],                                           "func": aqy_118_capex_contraction_count_4q},
    "aqy_119_capex_to_revenue_ratio":                    {"inputs": ["capex", "revenue"],                                "func": aqy_119_capex_to_revenue_ratio},
    "aqy_120_depamor_qoq_change":                        {"inputs": ["depamor"],                                         "func": aqy_120_depamor_qoq_change},
    "aqy_121_assets_worst_4q_low":                       {"inputs": ["assets"],                                          "func": aqy_121_assets_worst_4q_low},
    "aqy_122_assets_worst_8q_low":                       {"inputs": ["assets"],                                          "func": aqy_122_assets_worst_8q_low},
    "aqy_123_assets_at_expanding_low_flag":              {"inputs": ["assets"],                                          "func": aqy_123_assets_at_expanding_low_flag},
    "aqy_124_intangibles_contraction_count_4q":          {"inputs": ["intangibles"],                                     "func": aqy_124_intangibles_contraction_count_4q},
    "aqy_125_intangibles_contraction_count_8q":          {"inputs": ["intangibles"],                                     "func": aqy_125_intangibles_contraction_count_8q},
    "aqy_126_ppnenet_contraction_count_4q":              {"inputs": ["ppnenet"],                                         "func": aqy_126_ppnenet_contraction_count_4q},
    "aqy_127_ppnenet_zscore_4q":                         {"inputs": ["ppnenet"],                                         "func": aqy_127_ppnenet_zscore_4q},
    "aqy_128_ppnenet_zscore_8q":                         {"inputs": ["ppnenet"],                                         "func": aqy_128_ppnenet_zscore_8q},
    "aqy_129_tangibles_zscore_4q":                       {"inputs": ["tangibles"],                                       "func": aqy_129_tangibles_zscore_4q},
    "aqy_130_tangibles_qoq_change":                      {"inputs": ["tangibles"],                                       "func": aqy_130_tangibles_qoq_change},
    "aqy_131_tangibles_yoy_change":                      {"inputs": ["tangibles"],                                       "func": aqy_131_tangibles_yoy_change},
    "aqy_132_tangibles_qoq_pct":                         {"inputs": ["tangibles"],                                       "func": aqy_132_tangibles_qoq_pct},
    "aqy_133_tangibles_yoy_pct":                         {"inputs": ["tangibles"],                                       "func": aqy_133_tangibles_yoy_pct},
    "aqy_134_tangibles_contraction_count_4q":            {"inputs": ["tangibles"],                                       "func": aqy_134_tangibles_contraction_count_4q},
    "aqy_135_tangibles_2y_pct":                          {"inputs": ["tangibles"],                                       "func": aqy_135_tangibles_2y_pct},
    "aqy_136_intangibles_plus_goodwill_share":           {"inputs": ["intangibles", "assets"],                           "func": aqy_136_intangibles_plus_goodwill_share},
    "aqy_137_hard_asset_share_zscore_4q":                {"inputs": ["tangibles", "assets"],                             "func": aqy_137_hard_asset_share_zscore_4q},
    "aqy_138_hard_asset_share_pct_rank_4q":              {"inputs": ["tangibles", "assets"],                             "func": aqy_138_hard_asset_share_pct_rank_4q},
    "aqy_139_depamor_to_revenue_ratio":                  {"inputs": ["depamor", "revenue"],                              "func": aqy_139_depamor_to_revenue_ratio},
    "aqy_140_depamor_to_revenue_qoq_change":             {"inputs": ["depamor", "revenue"],                              "func": aqy_140_depamor_to_revenue_qoq_change},
    "aqy_141_capex_minus_depamor_gap":                   {"inputs": ["capex", "depamor"],                                "func": aqy_141_capex_minus_depamor_gap},
    "aqy_142_capex_minus_depamor_to_assets":             {"inputs": ["capex", "depamor", "assets"],                      "func": aqy_142_capex_minus_depamor_to_assets},
    "aqy_143_asset_turnover_proxy":                      {"inputs": ["revenue", "assets"],                               "func": aqy_143_asset_turnover_proxy},
    "aqy_144_asset_turnover_pct_rank_8q":                {"inputs": ["revenue", "assets"],                               "func": aqy_144_asset_turnover_pct_rank_8q},
    "aqy_145_asset_turnover_zscore_4q":                  {"inputs": ["revenue", "assets"],                               "func": aqy_145_asset_turnover_zscore_4q},
    "aqy_146_asset_turnover_drawdown_from_4q_peak":      {"inputs": ["revenue", "assets"],                               "func": aqy_146_asset_turnover_drawdown_from_4q_peak},
    "aqy_147_assets_vs_4q_avg":                          {"inputs": ["assets"],                                          "func": aqy_147_assets_vs_4q_avg},
    "aqy_148_assets_vs_8q_avg":                          {"inputs": ["assets"],                                          "func": aqy_148_assets_vs_8q_avg},
    "aqy_149_multi_asset_erosion_composite":             {"inputs": ["assets", "tangibles", "ppnenet", "intangibles"],   "func": aqy_149_multi_asset_erosion_composite},
    "aqy_150_asset_quality_expanding_pct_rank":          {"inputs": ["assets"],                                          "func": aqy_150_asset_quality_expanding_pct_rank},
}
