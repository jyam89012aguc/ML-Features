"""
68_asset_quality — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative asset-quality features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
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
_TD_QTR   = 63
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


# ── 2nd-derivative helpers (self-contained recomputes) ───────────────────────

def _assets_qoq(assets: pd.Series) -> pd.Series:
    return assets - assets.shift(_TD_QTR)


def _assets_qoq_accel(assets: pd.Series) -> pd.Series:
    """2nd-order: QoQ change in the QoQ asset change."""
    base = _assets_qoq(assets)
    return base - base.shift(_TD_QTR)


def _assets_pct_drawdown_4q(assets: pd.Series) -> pd.Series:
    peak = _rolling_max(assets, _TD_YEAR)
    return _safe_div_abs(assets - peak, peak)


def _assets_drawdown_4q_qoq_diff(assets: pd.Series) -> pd.Series:
    """2nd: QoQ diff of level drawdown from 4Q peak."""
    peak = _rolling_max(assets, _TD_YEAR)
    base = assets - peak
    return base - base.shift(_TD_QTR)


def _assets_zscore_4q(assets: pd.Series) -> pd.Series:
    m  = _rolling_mean(assets, _TD_YEAR)
    sd = _rolling_std(assets, _TD_YEAR)
    return _safe_div(assets - m, sd)


def _assets_zscore_4q_qoq_diff(assets: pd.Series) -> pd.Series:
    """2nd: QoQ diff of 4Q z-score."""
    base = _assets_zscore_4q(assets)
    return base - base.shift(_TD_QTR)


def _intangibles_qoq(intangibles: pd.Series) -> pd.Series:
    return intangibles - intangibles.shift(_TD_QTR)


def _intangibles_qoq_qoq_diff(intangibles: pd.Series) -> pd.Series:
    """2nd: QoQ change in the QoQ intangibles change."""
    base = _intangibles_qoq(intangibles)
    return base - base.shift(_TD_QTR)


def _intangibles_to_assets_qoq_diff(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd: QoQ diff of intangibles-to-assets ratio."""
    ratio = _safe_div(intangibles, assets)
    return ratio - ratio.shift(_TD_QTR)


def _ppnenet_qoq(ppnenet: pd.Series) -> pd.Series:
    return ppnenet - ppnenet.shift(_TD_QTR)


def _ppnenet_qoq_qoq_diff(ppnenet: pd.Series) -> pd.Series:
    """2nd: QoQ change in the QoQ PP&E change."""
    base = _ppnenet_qoq(ppnenet)
    return base - base.shift(_TD_QTR)


def _tangibles_to_assets_qoq_diff(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd: QoQ diff of tangibles-to-assets ratio."""
    ratio = _safe_div(tangibles, assets)
    return ratio - ratio.shift(_TD_QTR)


def _depamor_to_ppnenet_qoq_diff(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """2nd: QoQ diff of depamor/ppnenet ratio."""
    ratio = _safe_div(depamor, ppnenet)
    return ratio - ratio.shift(_TD_QTR)


def _asset_turnover_qoq_diff(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd: QoQ diff of asset turnover."""
    ratio = _safe_div(revenue.abs(), assets)
    return ratio - ratio.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def aqy_drv3_001_assets_qoq_accel_qoq_diff(assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of the QoQ acceleration of total assets (jerk of asset contraction)."""
    base = _assets_qoq_accel(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv3_002_assets_pct_drawdown_4q_qoq_accel(assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of pct drawdown from 4Q peak)."""
    d1 = _assets_pct_drawdown_4q(assets)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def aqy_drv3_003_assets_zscore_4q_qoq_accel(assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of 4Q z-score of assets)."""
    d1 = _assets_zscore_4q_qoq_diff(assets)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_004_assets_drawdown_4q_qoq_accel(assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of level drawdown from 4Q peak)."""
    d1 = _assets_drawdown_4q_qoq_diff(assets)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_005_intangibles_qoq_accel_qoq_diff(intangibles: pd.Series) -> pd.Series:
    """3rd: QoQ diff of the QoQ acceleration of intangibles."""
    base = _intangibles_qoq_qoq_diff(intangibles)
    return base - base.shift(_TD_QTR)


def aqy_drv3_006_intangibles_to_assets_qoq_accel(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of intangibles-to-assets ratio)."""
    d1 = _intangibles_to_assets_qoq_diff(intangibles, assets)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_007_ppnenet_qoq_accel_qoq_diff(ppnenet: pd.Series) -> pd.Series:
    """3rd: QoQ diff of the QoQ acceleration of PP&E contraction."""
    base = _ppnenet_qoq_qoq_diff(ppnenet)
    return base - base.shift(_TD_QTR)


def aqy_drv3_008_tangibles_to_assets_qoq_accel(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of tangibles-to-assets ratio)."""
    d1 = _tangibles_to_assets_qoq_diff(tangibles, assets)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_009_depamor_to_ppnenet_qoq_accel(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of depamor/ppnenet ratio)."""
    d1 = _depamor_to_ppnenet_qoq_diff(depamor, ppnenet)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_010_asset_turnover_qoq_accel(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of asset turnover)."""
    d1 = _asset_turnover_qoq_diff(revenue, assets)
    return d1 - d1.shift(_TD_QTR)


def aqy_drv3_011_assets_qoq_accel_yoy_diff(assets: pd.Series) -> pd.Series:
    """3rd: YoY change in the QoQ acceleration of total assets."""
    base = _assets_qoq_accel(assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv3_012_intangibles_qoq_accel_yoy_diff(intangibles: pd.Series) -> pd.Series:
    """3rd: YoY change in the QoQ acceleration of intangibles contraction."""
    base = _intangibles_qoq_qoq_diff(intangibles)
    return base - base.shift(_TD_YEAR)


def aqy_drv3_013_ppnenet_qoq_accel_yoy_diff(ppnenet: pd.Series) -> pd.Series:
    """3rd: YoY change in the QoQ acceleration of PP&E contraction."""
    base = _ppnenet_qoq_qoq_diff(ppnenet)
    return base - base.shift(_TD_YEAR)


def aqy_drv3_014_assets_zscore_4q_qoq_accel_ewm(assets: pd.Series) -> pd.Series:
    """
    3rd: Current QoQ diff of 4Q z-score minus its 4Q EWM.
    Captures whether the rate of z-score deterioration is worse than recent average.
    """
    d1 = _assets_zscore_4q_qoq_diff(assets)
    ewm = d1.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d1 - ewm


def aqy_drv3_015_tangibles_to_assets_qoq_accel_yoy_diff(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd: YoY change in the QoQ diff of tangibles-to-assets ratio."""
    d1 = _tangibles_to_assets_qoq_diff(tangibles, assets)
    return d1 - d1.shift(_TD_YEAR)


def aqy_drv3_016_assets_qoq_pct_3rd_diff(assets: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of QoQ pct change of assets)."""
    prior = assets.shift(_TD_QTR)
    pct = _safe_div_abs(assets - prior, prior)
    d2 = (pct - pct.shift(_TD_QTR))
    return d2 - d2.shift(_TD_QTR)


def aqy_drv3_017_intangibles_share_qoq_accel_4q_mean(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """
    3rd: Rolling 4Q mean of the QoQ diff of (QoQ diff of intangibles-to-assets).
    Smoothed third-order signal of soft-asset mix drift.
    """
    d1 = _intangibles_to_assets_qoq_diff(intangibles, assets)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()


def aqy_drv3_018_ppnenet_drawdown_4q_qoq_accel(ppnenet: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of PP&E pct drawdown from 4Q peak)."""
    peak = _rolling_max(ppnenet, _TD_YEAR)
    pct_dd = _safe_div_abs(ppnenet - peak, peak)
    d2 = pct_dd - pct_dd.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def aqy_drv3_019_depamor_to_ppnenet_qoq_accel_ewm(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """
    3rd: QoQ diff of depamor/ppnenet ratio vs its 4Q EWM.
    Captures whether the aging-rate acceleration is worsening.
    """
    d1 = _depamor_to_ppnenet_qoq_diff(depamor, ppnenet)
    ewm = d1.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d1 - ewm


def aqy_drv3_020_asset_turnover_qoq_accel_4q_mean(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """
    3rd: Rolling 4Q mean of the QoQ diff of (QoQ diff of asset turnover).
    Smoothed third-order signal of asset-utilization deterioration.
    """
    d1 = _asset_turnover_qoq_diff(revenue, assets)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()


def aqy_drv3_021_assets_qoq_accel_zscore_4q(assets: pd.Series) -> pd.Series:
    """3rd: Z-score (4Q window) of the QoQ acceleration of total assets."""
    accel = _assets_qoq_accel(assets)
    m  = _rolling_mean(accel, _TD_YEAR)
    sd = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def aqy_drv3_022_intangibles_qoq_accel_zscore_4q(intangibles: pd.Series) -> pd.Series:
    """3rd: Z-score (4Q window) of the QoQ acceleration of intangibles."""
    accel = _intangibles_qoq_qoq_diff(intangibles)
    m  = _rolling_mean(accel, _TD_YEAR)
    sd = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def aqy_drv3_023_ppnenet_qoq_accel_zscore_4q(ppnenet: pd.Series) -> pd.Series:
    """3rd: Z-score (4Q window) of the QoQ acceleration of PP&E contraction."""
    accel = _ppnenet_qoq_qoq_diff(ppnenet)
    m  = _rolling_mean(accel, _TD_YEAR)
    sd = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def aqy_drv3_024_capex_to_depamor_qoq_accel(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """3rd: QoQ diff of (QoQ diff of capex/depamor ratio) — underinvestment jerk."""
    ratio = _safe_div(capex.abs(), depamor.abs())
    d2 = (ratio - ratio.shift(_TD_QTR))
    return d2 - d2.shift(_TD_QTR)


def aqy_drv3_025_multi_asset_erosion_qoq_accel(
    assets: pd.Series,
    tangibles: pd.Series,
    ppnenet: pd.Series,
    intangibles: pd.Series,
) -> pd.Series:
    """
    3rd: QoQ diff of (QoQ diff of multi-asset erosion composite).
    Composite = (z_assets + z_tangibles + z_ppnenet - z_intangible_share) / 4.
    This third derivative captures the jerk of the overall asset erosion signal.
    """
    def _zscore(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    intsh = _safe_div(intangibles, assets)
    composite = (_zscore(assets) + _zscore(tangibles) + _zscore(ppnenet) - _zscore(intsh)) / 4.0
    d2 = composite - composite.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

ASSET_QUALITY_REGISTRY_3RD_DERIVATIVES = {
    "aqy_drv3_001_assets_qoq_accel_qoq_diff":           {"inputs": ["assets"],                                        "func": aqy_drv3_001_assets_qoq_accel_qoq_diff},
    "aqy_drv3_002_assets_pct_drawdown_4q_qoq_accel":    {"inputs": ["assets"],                                        "func": aqy_drv3_002_assets_pct_drawdown_4q_qoq_accel},
    "aqy_drv3_003_assets_zscore_4q_qoq_accel":          {"inputs": ["assets"],                                        "func": aqy_drv3_003_assets_zscore_4q_qoq_accel},
    "aqy_drv3_004_assets_drawdown_4q_qoq_accel":        {"inputs": ["assets"],                                        "func": aqy_drv3_004_assets_drawdown_4q_qoq_accel},
    "aqy_drv3_005_intangibles_qoq_accel_qoq_diff":      {"inputs": ["intangibles"],                                   "func": aqy_drv3_005_intangibles_qoq_accel_qoq_diff},
    "aqy_drv3_006_intangibles_to_assets_qoq_accel":     {"inputs": ["intangibles", "assets"],                         "func": aqy_drv3_006_intangibles_to_assets_qoq_accel},
    "aqy_drv3_007_ppnenet_qoq_accel_qoq_diff":          {"inputs": ["ppnenet"],                                       "func": aqy_drv3_007_ppnenet_qoq_accel_qoq_diff},
    "aqy_drv3_008_tangibles_to_assets_qoq_accel":       {"inputs": ["tangibles", "assets"],                           "func": aqy_drv3_008_tangibles_to_assets_qoq_accel},
    "aqy_drv3_009_depamor_to_ppnenet_qoq_accel":        {"inputs": ["depamor", "ppnenet"],                            "func": aqy_drv3_009_depamor_to_ppnenet_qoq_accel},
    "aqy_drv3_010_asset_turnover_qoq_accel":            {"inputs": ["revenue", "assets"],                             "func": aqy_drv3_010_asset_turnover_qoq_accel},
    "aqy_drv3_011_assets_qoq_accel_yoy_diff":           {"inputs": ["assets"],                                        "func": aqy_drv3_011_assets_qoq_accel_yoy_diff},
    "aqy_drv3_012_intangibles_qoq_accel_yoy_diff":      {"inputs": ["intangibles"],                                   "func": aqy_drv3_012_intangibles_qoq_accel_yoy_diff},
    "aqy_drv3_013_ppnenet_qoq_accel_yoy_diff":          {"inputs": ["ppnenet"],                                       "func": aqy_drv3_013_ppnenet_qoq_accel_yoy_diff},
    "aqy_drv3_014_assets_zscore_4q_qoq_accel_ewm":      {"inputs": ["assets"],                                        "func": aqy_drv3_014_assets_zscore_4q_qoq_accel_ewm},
    "aqy_drv3_015_tangibles_to_assets_qoq_accel_yoy_diff": {"inputs": ["tangibles", "assets"],                        "func": aqy_drv3_015_tangibles_to_assets_qoq_accel_yoy_diff},
    "aqy_drv3_016_assets_qoq_pct_3rd_diff":             {"inputs": ["assets"],                                        "func": aqy_drv3_016_assets_qoq_pct_3rd_diff},
    "aqy_drv3_017_intangibles_share_qoq_accel_4q_mean": {"inputs": ["intangibles", "assets"],                         "func": aqy_drv3_017_intangibles_share_qoq_accel_4q_mean},
    "aqy_drv3_018_ppnenet_drawdown_4q_qoq_accel":       {"inputs": ["ppnenet"],                                       "func": aqy_drv3_018_ppnenet_drawdown_4q_qoq_accel},
    "aqy_drv3_019_depamor_to_ppnenet_qoq_accel_ewm":    {"inputs": ["depamor", "ppnenet"],                            "func": aqy_drv3_019_depamor_to_ppnenet_qoq_accel_ewm},
    "aqy_drv3_020_asset_turnover_qoq_accel_4q_mean":    {"inputs": ["revenue", "assets"],                             "func": aqy_drv3_020_asset_turnover_qoq_accel_4q_mean},
    "aqy_drv3_021_assets_qoq_accel_zscore_4q":          {"inputs": ["assets"],                                        "func": aqy_drv3_021_assets_qoq_accel_zscore_4q},
    "aqy_drv3_022_intangibles_qoq_accel_zscore_4q":     {"inputs": ["intangibles"],                                   "func": aqy_drv3_022_intangibles_qoq_accel_zscore_4q},
    "aqy_drv3_023_ppnenet_qoq_accel_zscore_4q":         {"inputs": ["ppnenet"],                                       "func": aqy_drv3_023_ppnenet_qoq_accel_zscore_4q},
    "aqy_drv3_024_capex_to_depamor_qoq_accel":          {"inputs": ["capex", "depamor"],                              "func": aqy_drv3_024_capex_to_depamor_qoq_accel},
    "aqy_drv3_025_multi_asset_erosion_qoq_accel":       {"inputs": ["assets", "tangibles", "ppnenet", "intangibles"], "func": aqy_drv3_025_multi_asset_erosion_qoq_accel},
}
