"""
68_asset_quality — 2nd-Derivative Features 001-025
Domain: rate of change of base asset-quality features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 2nd-derivative series are sparse/stepwise on a daily index because the
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


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# Inline base concepts so this file needs no cross-file imports.

def _assets_qoq(assets: pd.Series) -> pd.Series:
    return assets - assets.shift(_TD_QTR)


def _assets_yoy(assets: pd.Series) -> pd.Series:
    return assets - assets.shift(_TD_YEAR)


def _assets_qoq_pct(assets: pd.Series) -> pd.Series:
    prior = assets.shift(_TD_QTR)
    return _safe_div_abs(assets - prior, prior)


def _assets_pct_drawdown_4q(assets: pd.Series) -> pd.Series:
    peak = _rolling_max(assets, _TD_YEAR)
    return _safe_div_abs(assets - peak, peak)


def _assets_zscore_4q(assets: pd.Series) -> pd.Series:
    m  = _rolling_mean(assets, _TD_YEAR)
    sd = _rolling_std(assets, _TD_YEAR)
    return _safe_div(assets - m, sd)


def _intangibles_qoq(intangibles: pd.Series) -> pd.Series:
    return intangibles - intangibles.shift(_TD_QTR)


def _intangibles_to_assets(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(intangibles, assets)


def _ppnenet_qoq(ppnenet: pd.Series) -> pd.Series:
    return ppnenet - ppnenet.shift(_TD_QTR)


def _ppnenet_pct_drawdown_4q(ppnenet: pd.Series) -> pd.Series:
    peak = _rolling_max(ppnenet, _TD_YEAR)
    return _safe_div_abs(ppnenet - peak, peak)


def _tangibles_to_assets(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(tangibles, assets)


def _depamor_to_ppnenet(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    return _safe_div(depamor, ppnenet)


def _capex_to_depamor(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    return _safe_div(capex.abs(), depamor.abs())


def _asset_turnover(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(revenue.abs(), assets)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def aqy_drv2_001_assets_qoq_change_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the QoQ asset change (acceleration of asset contraction)."""
    base = _assets_qoq(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_002_assets_yoy_change_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the YoY asset change (how fast YoY trend is shifting)."""
    base = _assets_yoy(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_003_assets_qoq_pct_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of total assets."""
    base = _assets_qoq_pct(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_004_assets_pct_drawdown_4q_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the 4Q-peak percent drawdown of total assets."""
    base = _assets_pct_drawdown_4q(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_005_assets_zscore_4q_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of total assets."""
    base = _assets_zscore_4q(assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_006_assets_zscore_4q_yoy_diff(assets: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of total assets."""
    base = _assets_zscore_4q(assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_007_intangibles_qoq_change_qoq_diff(intangibles: pd.Series) -> pd.Series:
    """QoQ change in the QoQ intangibles change (writedown acceleration)."""
    base = _intangibles_qoq(intangibles)
    return base - base.shift(_TD_QTR)


def aqy_drv2_008_intangibles_to_assets_qoq_diff(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in intangibles-to-assets ratio (2nd-order soft-asset mix drift)."""
    base = _intangibles_to_assets(intangibles, assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_009_intangibles_to_assets_yoy_diff(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in intangibles-to-assets ratio."""
    base = _intangibles_to_assets(intangibles, assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_010_ppnenet_qoq_change_qoq_diff(ppnenet: pd.Series) -> pd.Series:
    """QoQ change in the QoQ PP&E change (acceleration of PP&E contraction)."""
    base = _ppnenet_qoq(ppnenet)
    return base - base.shift(_TD_QTR)


def aqy_drv2_011_ppnenet_pct_drawdown_4q_qoq_diff(ppnenet: pd.Series) -> pd.Series:
    """QoQ change in the 4Q-peak percent drawdown of PP&E."""
    base = _ppnenet_pct_drawdown_4q(ppnenet)
    return base - base.shift(_TD_QTR)


def aqy_drv2_012_tangibles_to_assets_qoq_diff(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in tangibles-to-assets ratio (2nd-order hard-asset mix drift)."""
    base = _tangibles_to_assets(tangibles, assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_013_tangibles_to_assets_yoy_diff(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in tangibles-to-assets ratio."""
    base = _tangibles_to_assets(tangibles, assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_014_depamor_to_ppnenet_qoq_diff(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """QoQ change in depamor/ppnenet ratio (aging rate of asset base accelerating)."""
    base = _depamor_to_ppnenet(depamor, ppnenet)
    return base - base.shift(_TD_QTR)


def aqy_drv2_015_depamor_to_ppnenet_yoy_diff(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """YoY change in depamor/ppnenet ratio."""
    base = _depamor_to_ppnenet(depamor, ppnenet)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_016_capex_to_depamor_qoq_diff(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """QoQ change in capex/depamor ratio (underinvestment acceleration)."""
    base = _capex_to_depamor(capex, depamor)
    return base - base.shift(_TD_QTR)


def aqy_drv2_017_asset_turnover_qoq_diff(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in asset turnover (how fast utilization is declining)."""
    base = _asset_turnover(revenue, assets)
    return base - base.shift(_TD_QTR)


def aqy_drv2_018_asset_turnover_yoy_diff(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in asset turnover."""
    base = _asset_turnover(revenue, assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_019_assets_qoq_slope_of_qoq(assets: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ asset change series.
    Captures the trend in QoQ momentum of asset contraction.
    """
    base = _assets_qoq(assets)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def aqy_drv2_020_assets_qoq_pct_yoy_diff(assets: pd.Series) -> pd.Series:
    """YoY change in the QoQ percent change of assets (2nd-order YoY)."""
    base = _assets_qoq_pct(assets)
    return base - base.shift(_TD_YEAR)


def aqy_drv2_021_intangibles_qoq_pct_qoq_diff(intangibles: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of intangibles."""
    prior = intangibles.shift(_TD_QTR)
    base = _safe_div_abs(intangibles - prior, prior)
    return base - base.shift(_TD_QTR)


def aqy_drv2_022_assets_drawdown_4q_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the assets level drawdown from 4Q peak."""
    peak = _rolling_max(assets, _TD_YEAR)
    base = assets - peak
    return base - base.shift(_TD_QTR)


def aqy_drv2_023_ppnenet_qoq_ewm_diff(ppnenet: pd.Series) -> pd.Series:
    """
    Current QoQ PP&E change minus its 4-quarter EWM (span=252).
    Measures whether current PP&E contraction is worse than its recent trend.
    """
    base = _ppnenet_qoq(ppnenet)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def aqy_drv2_024_assets_contraction_acceleration(assets: pd.Series) -> pd.Series:
    """
    Change in the total-asset drawdown from its expanding peak (2nd order):
    QoQ diff of (assets - expanding_max(assets)).
    Captures whether the gap to the historic peak is widening.
    """
    peak = assets.expanding(min_periods=1).max()
    base = assets - peak
    return base - base.shift(_TD_QTR)


def aqy_drv2_025_multi_asset_erosion_qoq_diff(
    assets: pd.Series,
    tangibles: pd.Series,
    ppnenet: pd.Series,
    intangibles: pd.Series,
) -> pd.Series:
    """
    QoQ change in the multi-asset erosion composite:
    (z_assets + z_tangibles + z_ppnenet - z_intangible_share) / 4, diffed QoQ.
    """
    def _zscore(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    intsh = _safe_div(intangibles, assets)
    composite = (_zscore(assets) + _zscore(tangibles) + _zscore(ppnenet) - _zscore(intsh)) / 4.0
    return composite - composite.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

ASSET_QUALITY_REGISTRY_2ND_DERIVATIVES = {
    "aqy_drv2_001_assets_qoq_change_qoq_diff":          {"inputs": ["assets"],                                        "func": aqy_drv2_001_assets_qoq_change_qoq_diff},
    "aqy_drv2_002_assets_yoy_change_qoq_diff":          {"inputs": ["assets"],                                        "func": aqy_drv2_002_assets_yoy_change_qoq_diff},
    "aqy_drv2_003_assets_qoq_pct_qoq_diff":             {"inputs": ["assets"],                                        "func": aqy_drv2_003_assets_qoq_pct_qoq_diff},
    "aqy_drv2_004_assets_pct_drawdown_4q_qoq_diff":     {"inputs": ["assets"],                                        "func": aqy_drv2_004_assets_pct_drawdown_4q_qoq_diff},
    "aqy_drv2_005_assets_zscore_4q_qoq_diff":           {"inputs": ["assets"],                                        "func": aqy_drv2_005_assets_zscore_4q_qoq_diff},
    "aqy_drv2_006_assets_zscore_4q_yoy_diff":           {"inputs": ["assets"],                                        "func": aqy_drv2_006_assets_zscore_4q_yoy_diff},
    "aqy_drv2_007_intangibles_qoq_change_qoq_diff":     {"inputs": ["intangibles"],                                   "func": aqy_drv2_007_intangibles_qoq_change_qoq_diff},
    "aqy_drv2_008_intangibles_to_assets_qoq_diff":      {"inputs": ["intangibles", "assets"],                         "func": aqy_drv2_008_intangibles_to_assets_qoq_diff},
    "aqy_drv2_009_intangibles_to_assets_yoy_diff":      {"inputs": ["intangibles", "assets"],                         "func": aqy_drv2_009_intangibles_to_assets_yoy_diff},
    "aqy_drv2_010_ppnenet_qoq_change_qoq_diff":         {"inputs": ["ppnenet"],                                       "func": aqy_drv2_010_ppnenet_qoq_change_qoq_diff},
    "aqy_drv2_011_ppnenet_pct_drawdown_4q_qoq_diff":    {"inputs": ["ppnenet"],                                       "func": aqy_drv2_011_ppnenet_pct_drawdown_4q_qoq_diff},
    "aqy_drv2_012_tangibles_to_assets_qoq_diff":        {"inputs": ["tangibles", "assets"],                           "func": aqy_drv2_012_tangibles_to_assets_qoq_diff},
    "aqy_drv2_013_tangibles_to_assets_yoy_diff":        {"inputs": ["tangibles", "assets"],                           "func": aqy_drv2_013_tangibles_to_assets_yoy_diff},
    "aqy_drv2_014_depamor_to_ppnenet_qoq_diff":         {"inputs": ["depamor", "ppnenet"],                            "func": aqy_drv2_014_depamor_to_ppnenet_qoq_diff},
    "aqy_drv2_015_depamor_to_ppnenet_yoy_diff":         {"inputs": ["depamor", "ppnenet"],                            "func": aqy_drv2_015_depamor_to_ppnenet_yoy_diff},
    "aqy_drv2_016_capex_to_depamor_qoq_diff":           {"inputs": ["capex", "depamor"],                              "func": aqy_drv2_016_capex_to_depamor_qoq_diff},
    "aqy_drv2_017_asset_turnover_qoq_diff":             {"inputs": ["revenue", "assets"],                             "func": aqy_drv2_017_asset_turnover_qoq_diff},
    "aqy_drv2_018_asset_turnover_yoy_diff":             {"inputs": ["revenue", "assets"],                             "func": aqy_drv2_018_asset_turnover_yoy_diff},
    "aqy_drv2_019_assets_qoq_slope_of_qoq":             {"inputs": ["assets"],                                        "func": aqy_drv2_019_assets_qoq_slope_of_qoq},
    "aqy_drv2_020_assets_qoq_pct_yoy_diff":             {"inputs": ["assets"],                                        "func": aqy_drv2_020_assets_qoq_pct_yoy_diff},
    "aqy_drv2_021_intangibles_qoq_pct_qoq_diff":        {"inputs": ["intangibles"],                                   "func": aqy_drv2_021_intangibles_qoq_pct_qoq_diff},
    "aqy_drv2_022_assets_drawdown_4q_qoq_diff":         {"inputs": ["assets"],                                        "func": aqy_drv2_022_assets_drawdown_4q_qoq_diff},
    "aqy_drv2_023_ppnenet_qoq_ewm_diff":                {"inputs": ["ppnenet"],                                       "func": aqy_drv2_023_ppnenet_qoq_ewm_diff},
    "aqy_drv2_024_assets_contraction_acceleration":     {"inputs": ["assets"],                                        "func": aqy_drv2_024_assets_contraction_acceleration},
    "aqy_drv2_025_multi_asset_erosion_qoq_diff":        {"inputs": ["assets", "tangibles", "ppnenet", "intangibles"], "func": aqy_drv2_025_multi_asset_erosion_qoq_diff},
}
