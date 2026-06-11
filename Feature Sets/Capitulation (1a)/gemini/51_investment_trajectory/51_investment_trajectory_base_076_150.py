"""
51_investment_trajectory — Base Features 076-150
Domain: investment_trajectory
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def invt_076_asset_growth_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_076_asset_growth_lvl_5d"""
    base = assets.pct_change(252)
    return _rolling_mean(base, 5)

def invt_077_asset_growth_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_077_asset_growth_zscore_5d"""
    base = assets.pct_change(252)
    return _zscore_rolling(base, 5)

def invt_078_asset_growth_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_078_asset_growth_rank_5d"""
    base = assets.pct_change(252)
    return _rank_pct(base, 5)

def invt_079_asset_growth_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_079_asset_growth_lvl_21d"""
    base = assets.pct_change(252)
    return _rolling_mean(base, 21)

def invt_080_asset_growth_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_080_asset_growth_zscore_21d"""
    base = assets.pct_change(252)
    return _zscore_rolling(base, 21)

def invt_081_asset_growth_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_081_asset_growth_rank_21d"""
    base = assets.pct_change(252)
    return _rank_pct(base, 21)

def invt_082_asset_growth_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_082_asset_growth_lvl_63d"""
    base = assets.pct_change(252)
    return _rolling_mean(base, 63)

def invt_083_asset_growth_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_083_asset_growth_zscore_63d"""
    base = assets.pct_change(252)
    return _zscore_rolling(base, 63)

def invt_084_asset_growth_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_084_asset_growth_rank_63d"""
    base = assets.pct_change(252)
    return _rank_pct(base, 63)

def invt_085_asset_growth_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_085_asset_growth_lvl_126d"""
    base = assets.pct_change(252)
    return _rolling_mean(base, 126)

def invt_086_asset_growth_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_086_asset_growth_zscore_126d"""
    base = assets.pct_change(252)
    return _zscore_rolling(base, 126)

def invt_087_asset_growth_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_087_asset_growth_rank_126d"""
    base = assets.pct_change(252)
    return _rank_pct(base, 126)

def invt_088_asset_growth_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_088_asset_growth_lvl_252d"""
    base = assets.pct_change(252)
    return _rolling_mean(base, 252)

def invt_089_asset_growth_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_089_asset_growth_zscore_252d"""
    base = assets.pct_change(252)
    return _zscore_rolling(base, 252)

def invt_090_asset_growth_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_090_asset_growth_rank_252d"""
    base = assets.pct_change(252)
    return _rank_pct(base, 252)

def invt_091_reinvestment_rate_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_091_reinvestment_rate_lvl_5d"""
    base = _safe_div(capex.abs(), ocf)
    return _rolling_mean(base, 5)

def invt_092_reinvestment_rate_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_092_reinvestment_rate_zscore_5d"""
    base = _safe_div(capex.abs(), ocf)
    return _zscore_rolling(base, 5)

def invt_093_reinvestment_rate_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_093_reinvestment_rate_rank_5d"""
    base = _safe_div(capex.abs(), ocf)
    return _rank_pct(base, 5)

def invt_094_reinvestment_rate_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_094_reinvestment_rate_lvl_21d"""
    base = _safe_div(capex.abs(), ocf)
    return _rolling_mean(base, 21)

def invt_095_reinvestment_rate_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_095_reinvestment_rate_zscore_21d"""
    base = _safe_div(capex.abs(), ocf)
    return _zscore_rolling(base, 21)

def invt_096_reinvestment_rate_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_096_reinvestment_rate_rank_21d"""
    base = _safe_div(capex.abs(), ocf)
    return _rank_pct(base, 21)

def invt_097_reinvestment_rate_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_097_reinvestment_rate_lvl_63d"""
    base = _safe_div(capex.abs(), ocf)
    return _rolling_mean(base, 63)

def invt_098_reinvestment_rate_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_098_reinvestment_rate_zscore_63d"""
    base = _safe_div(capex.abs(), ocf)
    return _zscore_rolling(base, 63)

def invt_099_reinvestment_rate_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_099_reinvestment_rate_rank_63d"""
    base = _safe_div(capex.abs(), ocf)
    return _rank_pct(base, 63)

def invt_100_reinvestment_rate_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_100_reinvestment_rate_lvl_126d"""
    base = _safe_div(capex.abs(), ocf)
    return _rolling_mean(base, 126)

def invt_101_reinvestment_rate_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_101_reinvestment_rate_zscore_126d"""
    base = _safe_div(capex.abs(), ocf)
    return _zscore_rolling(base, 126)

def invt_102_reinvestment_rate_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_102_reinvestment_rate_rank_126d"""
    base = _safe_div(capex.abs(), ocf)
    return _rank_pct(base, 126)

def invt_103_reinvestment_rate_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_103_reinvestment_rate_lvl_252d"""
    base = _safe_div(capex.abs(), ocf)
    return _rolling_mean(base, 252)

def invt_104_reinvestment_rate_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_104_reinvestment_rate_zscore_252d"""
    base = _safe_div(capex.abs(), ocf)
    return _zscore_rolling(base, 252)

def invt_105_reinvestment_rate_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_105_reinvestment_rate_rank_252d"""
    base = _safe_div(capex.abs(), ocf)
    return _rank_pct(base, 252)

def invt_106_net_investment_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_106_net_investment_lvl_5d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rolling_mean(base, 5)

def invt_107_net_investment_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_107_net_investment_zscore_5d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _zscore_rolling(base, 5)

def invt_108_net_investment_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_108_net_investment_rank_5d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rank_pct(base, 5)

def invt_109_net_investment_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_109_net_investment_lvl_21d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rolling_mean(base, 21)

def invt_110_net_investment_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_110_net_investment_zscore_21d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _zscore_rolling(base, 21)

def invt_111_net_investment_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_111_net_investment_rank_21d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rank_pct(base, 21)

def invt_112_net_investment_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_112_net_investment_lvl_63d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rolling_mean(base, 63)

def invt_113_net_investment_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_113_net_investment_zscore_63d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _zscore_rolling(base, 63)

def invt_114_net_investment_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_114_net_investment_rank_63d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rank_pct(base, 63)

def invt_115_net_investment_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_115_net_investment_lvl_126d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rolling_mean(base, 126)

def invt_116_net_investment_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_116_net_investment_zscore_126d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _zscore_rolling(base, 126)

def invt_117_net_investment_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_117_net_investment_rank_126d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rank_pct(base, 126)

def invt_118_net_investment_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_118_net_investment_lvl_252d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rolling_mean(base, 252)

def invt_119_net_investment_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_119_net_investment_zscore_252d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _zscore_rolling(base, 252)

def invt_120_net_investment_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_120_net_investment_rank_252d"""
    base = _safe_div(capex.abs() - depamor.fillna(0), assets)
    return _rank_pct(base, 252)

def invt_121_acq_ratio_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_121_acq_ratio_lvl_5d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rolling_mean(base, 5)

def invt_122_acq_ratio_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_122_acq_ratio_zscore_5d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _zscore_rolling(base, 5)

def invt_123_acq_ratio_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_123_acq_ratio_rank_5d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rank_pct(base, 5)

def invt_124_acq_ratio_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_124_acq_ratio_lvl_21d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rolling_mean(base, 21)

def invt_125_acq_ratio_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_125_acq_ratio_zscore_21d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _zscore_rolling(base, 21)

def invt_126_acq_ratio_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_126_acq_ratio_rank_21d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rank_pct(base, 21)

def invt_127_acq_ratio_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_127_acq_ratio_lvl_63d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rolling_mean(base, 63)

def invt_128_acq_ratio_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_128_acq_ratio_zscore_63d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _zscore_rolling(base, 63)

def invt_129_acq_ratio_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_129_acq_ratio_rank_63d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rank_pct(base, 63)

def invt_130_acq_ratio_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_130_acq_ratio_lvl_126d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rolling_mean(base, 126)

def invt_131_acq_ratio_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_131_acq_ratio_zscore_126d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _zscore_rolling(base, 126)

def invt_132_acq_ratio_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_132_acq_ratio_rank_126d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rank_pct(base, 126)

def invt_133_acq_ratio_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_133_acq_ratio_lvl_252d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rolling_mean(base, 252)

def invt_134_acq_ratio_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_134_acq_ratio_zscore_252d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _zscore_rolling(base, 252)

def invt_135_acq_ratio_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_135_acq_ratio_rank_252d"""
    base = _safe_div(ncfi.abs() - capex.abs(), assets).clip(lower=0)
    return _rank_pct(base, 252)

def invt_136_inv_stability_lvl_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_136_inv_stability_lvl_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rolling_mean(base, 5)

def invt_137_inv_stability_zscore_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_137_inv_stability_zscore_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _zscore_rolling(base, 5)

def invt_138_inv_stability_rank_5d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_138_inv_stability_rank_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rank_pct(base, 5)

def invt_139_inv_stability_lvl_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_139_inv_stability_lvl_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rolling_mean(base, 21)

def invt_140_inv_stability_zscore_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_140_inv_stability_zscore_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _zscore_rolling(base, 21)

def invt_141_inv_stability_rank_21d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_141_inv_stability_rank_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rank_pct(base, 21)

def invt_142_inv_stability_lvl_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_142_inv_stability_lvl_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rolling_mean(base, 63)

def invt_143_inv_stability_zscore_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_143_inv_stability_zscore_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _zscore_rolling(base, 63)

def invt_144_inv_stability_rank_63d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_144_inv_stability_rank_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rank_pct(base, 63)

def invt_145_inv_stability_lvl_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_145_inv_stability_lvl_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rolling_mean(base, 126)

def invt_146_inv_stability_zscore_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_146_inv_stability_zscore_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _zscore_rolling(base, 126)

def invt_147_inv_stability_rank_126d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_147_inv_stability_rank_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rank_pct(base, 126)

def invt_148_inv_stability_lvl_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_148_inv_stability_lvl_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rolling_mean(base, 252)

def invt_149_inv_stability_zscore_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_149_inv_stability_zscore_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _zscore_rolling(base, 252)

def invt_150_inv_stability_rank_252d(capex: pd.Series, ncfi: pd.Series, rnd: pd.Series, assets: pd.Series, revenue: pd.Series, ocf: pd.Series, depamor: pd.Series) -> pd.Series:
    """invt_150_inv_stability_rank_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(capex.abs().fillna(0) + rnd.fillna(0), 252) / _rolling_mean(capex.abs().fillna(0) + rnd.fillna(0), 252).replace(0, _EPS))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V51_REGISTRY_2 = {
    "invt_076_asset_growth_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_076_asset_growth_lvl_5d},
    "invt_077_asset_growth_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_077_asset_growth_zscore_5d},
    "invt_078_asset_growth_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_078_asset_growth_rank_5d},
    "invt_079_asset_growth_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_079_asset_growth_lvl_21d},
    "invt_080_asset_growth_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_080_asset_growth_zscore_21d},
    "invt_081_asset_growth_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_081_asset_growth_rank_21d},
    "invt_082_asset_growth_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_082_asset_growth_lvl_63d},
    "invt_083_asset_growth_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_083_asset_growth_zscore_63d},
    "invt_084_asset_growth_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_084_asset_growth_rank_63d},
    "invt_085_asset_growth_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_085_asset_growth_lvl_126d},
    "invt_086_asset_growth_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_086_asset_growth_zscore_126d},
    "invt_087_asset_growth_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_087_asset_growth_rank_126d},
    "invt_088_asset_growth_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_088_asset_growth_lvl_252d},
    "invt_089_asset_growth_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_089_asset_growth_zscore_252d},
    "invt_090_asset_growth_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_090_asset_growth_rank_252d},
    "invt_091_reinvestment_rate_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_091_reinvestment_rate_lvl_5d},
    "invt_092_reinvestment_rate_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_092_reinvestment_rate_zscore_5d},
    "invt_093_reinvestment_rate_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_093_reinvestment_rate_rank_5d},
    "invt_094_reinvestment_rate_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_094_reinvestment_rate_lvl_21d},
    "invt_095_reinvestment_rate_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_095_reinvestment_rate_zscore_21d},
    "invt_096_reinvestment_rate_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_096_reinvestment_rate_rank_21d},
    "invt_097_reinvestment_rate_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_097_reinvestment_rate_lvl_63d},
    "invt_098_reinvestment_rate_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_098_reinvestment_rate_zscore_63d},
    "invt_099_reinvestment_rate_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_099_reinvestment_rate_rank_63d},
    "invt_100_reinvestment_rate_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_100_reinvestment_rate_lvl_126d},
    "invt_101_reinvestment_rate_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_101_reinvestment_rate_zscore_126d},
    "invt_102_reinvestment_rate_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_102_reinvestment_rate_rank_126d},
    "invt_103_reinvestment_rate_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_103_reinvestment_rate_lvl_252d},
    "invt_104_reinvestment_rate_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_104_reinvestment_rate_zscore_252d},
    "invt_105_reinvestment_rate_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_105_reinvestment_rate_rank_252d},
    "invt_106_net_investment_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_106_net_investment_lvl_5d},
    "invt_107_net_investment_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_107_net_investment_zscore_5d},
    "invt_108_net_investment_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_108_net_investment_rank_5d},
    "invt_109_net_investment_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_109_net_investment_lvl_21d},
    "invt_110_net_investment_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_110_net_investment_zscore_21d},
    "invt_111_net_investment_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_111_net_investment_rank_21d},
    "invt_112_net_investment_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_112_net_investment_lvl_63d},
    "invt_113_net_investment_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_113_net_investment_zscore_63d},
    "invt_114_net_investment_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_114_net_investment_rank_63d},
    "invt_115_net_investment_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_115_net_investment_lvl_126d},
    "invt_116_net_investment_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_116_net_investment_zscore_126d},
    "invt_117_net_investment_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_117_net_investment_rank_126d},
    "invt_118_net_investment_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_118_net_investment_lvl_252d},
    "invt_119_net_investment_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_119_net_investment_zscore_252d},
    "invt_120_net_investment_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_120_net_investment_rank_252d},
    "invt_121_acq_ratio_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_121_acq_ratio_lvl_5d},
    "invt_122_acq_ratio_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_122_acq_ratio_zscore_5d},
    "invt_123_acq_ratio_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_123_acq_ratio_rank_5d},
    "invt_124_acq_ratio_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_124_acq_ratio_lvl_21d},
    "invt_125_acq_ratio_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_125_acq_ratio_zscore_21d},
    "invt_126_acq_ratio_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_126_acq_ratio_rank_21d},
    "invt_127_acq_ratio_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_127_acq_ratio_lvl_63d},
    "invt_128_acq_ratio_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_128_acq_ratio_zscore_63d},
    "invt_129_acq_ratio_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_129_acq_ratio_rank_63d},
    "invt_130_acq_ratio_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_130_acq_ratio_lvl_126d},
    "invt_131_acq_ratio_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_131_acq_ratio_zscore_126d},
    "invt_132_acq_ratio_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_132_acq_ratio_rank_126d},
    "invt_133_acq_ratio_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_133_acq_ratio_lvl_252d},
    "invt_134_acq_ratio_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_134_acq_ratio_zscore_252d},
    "invt_135_acq_ratio_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_135_acq_ratio_rank_252d},
    "invt_136_inv_stability_lvl_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_136_inv_stability_lvl_5d},
    "invt_137_inv_stability_zscore_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_137_inv_stability_zscore_5d},
    "invt_138_inv_stability_rank_5d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_138_inv_stability_rank_5d},
    "invt_139_inv_stability_lvl_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_139_inv_stability_lvl_21d},
    "invt_140_inv_stability_zscore_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_140_inv_stability_zscore_21d},
    "invt_141_inv_stability_rank_21d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_141_inv_stability_rank_21d},
    "invt_142_inv_stability_lvl_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_142_inv_stability_lvl_63d},
    "invt_143_inv_stability_zscore_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_143_inv_stability_zscore_63d},
    "invt_144_inv_stability_rank_63d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_144_inv_stability_rank_63d},
    "invt_145_inv_stability_lvl_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_145_inv_stability_lvl_126d},
    "invt_146_inv_stability_zscore_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_146_inv_stability_zscore_126d},
    "invt_147_inv_stability_rank_126d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_147_inv_stability_rank_126d},
    "invt_148_inv_stability_lvl_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_148_inv_stability_lvl_252d},
    "invt_149_inv_stability_zscore_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_149_inv_stability_zscore_252d},
    "invt_150_inv_stability_rank_252d": {"inputs": ["capex", "ncfi", "rnd", "assets", "revenue", "ocf", "depamor"], "func": invt_150_inv_stability_rank_252d},
}
