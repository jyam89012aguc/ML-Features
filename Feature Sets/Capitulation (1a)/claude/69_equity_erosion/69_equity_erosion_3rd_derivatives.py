"""
69_equity_erosion — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative equity-erosion features
(acceleration-of-acceleration, jerk in book value erosion)
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
    """Element-wise division; replaces zero denominators with NaN.
    Negative denominators are preserved — negative equity is meaningful distress."""
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


# ── 2nd-derivative helpers (self-contained — no cross-file imports) ───────────

def _d2_equity_qoq_accel(equity: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ equity change."""
    d1 = equity - equity.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_equity_yoy_qoq_diff(equity: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY equity change."""
    d1 = equity - equity.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def _d2_retearn_qoq_accel(retearn: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ retained-earnings change."""
    d1 = retearn - retearn.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_retearn_yoy_qoq_diff(retearn: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY retained-earnings change."""
    d1 = retearn - retearn.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def _d2_equity_drawdown_1y_qoq(equity: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in equity 1-year drawdown."""
    dd = equity - _rolling_max(equity, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


def _d2_equity_drawdown_exp_qoq(equity: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in equity expanding-peak drawdown."""
    peak = equity.expanding(min_periods=1).max()
    dd = equity - peak
    return dd - dd.shift(_TD_QTR)


def _d2_retearn_drawdown_exp_qoq(retearn: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in retained-earnings expanding drawdown."""
    peak = retearn.expanding(min_periods=1).max()
    dd = retearn - peak
    return dd - dd.shift(_TD_QTR)


def _d2_equity_zscore_qoq(equity: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in 4Q equity z-score."""
    m  = _rolling_mean(equity, _TD_YEAR)
    sd = _rolling_std(equity, _TD_YEAR)
    z  = _safe_div(equity - m, sd)
    return z - z.shift(_TD_QTR)


def _d2_retearn_zscore_qoq(retearn: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in 4Q retearn z-score."""
    m  = _rolling_mean(retearn, _TD_YEAR)
    sd = _rolling_std(retearn, _TD_YEAR)
    z  = _safe_div(retearn - m, sd)
    return z - z.shift(_TD_QTR)


def _d2_bvps_qoq_accel(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ BVPS change."""
    bvps = _safe_div(equity, sharesbas)
    d1   = bvps - bvps.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_netinc_ttm_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in TTM net income."""
    ttm = netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return (ttm - ttm.shift(_TD_QTR)) - (ttm.shift(_TD_QTR) - ttm.shift(_TD_2Q))


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def eqe_drv3_001_equity_qoq_accel_qoq_diff(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the QoQ equity-change acceleration."""
    base = _d2_equity_qoq_accel(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv3_002_equity_yoy_qoq_diff_qoq_diff(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative (QoQ of YoY equity change)."""
    base = _d2_equity_yoy_qoq_diff(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv3_003_retearn_qoq_accel_qoq_diff(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the QoQ retained-earnings-change acceleration."""
    base = _d2_retearn_qoq_accel(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv3_004_retearn_yoy_qoq_diff_qoq_diff(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative (QoQ of YoY retearn change)."""
    base = _d2_retearn_yoy_qoq_diff(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv3_005_equity_drawdown_1y_qoq_diff_qoq_diff(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative equity 1-year drawdown."""
    base = _d2_equity_drawdown_1y_qoq(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv3_006_equity_drawdown_exp_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the QoQ-of-QoQ expanding-peak equity drawdown."""
    base = _d2_equity_drawdown_exp_qoq(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv3_007_retearn_drawdown_exp_3rd_deriv(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative retearn expanding drawdown."""
    base = _d2_retearn_drawdown_exp_qoq(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv3_008_equity_zscore_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative equity z-score."""
    base = _d2_equity_zscore_qoq(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv3_009_retearn_zscore_3rd_deriv(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative retearn z-score."""
    base = _d2_retearn_zscore_qoq(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv3_010_bvps_qoq_accel_qoq_diff(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative BVPS QoQ acceleration."""
    base = _d2_bvps_qoq_accel(equity, sharesbas)
    return base - base.shift(_TD_QTR)


def eqe_drv3_011_netinc_ttm_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative TTM net income."""
    base = _d2_netinc_ttm_qoq(netinc)
    return base - base.shift(_TD_QTR)


def eqe_drv3_012_equity_qoq_accel_slope_1y(equity: pd.Series) -> pd.Series:
    """
    Rolling 1-year OLS slope of the equity QoQ acceleration series
    (3rd-order: trend in the rate of change of the rate of equity erosion).
    """
    base = _d2_equity_qoq_accel(equity)
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
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def eqe_drv3_013_retearn_qoq_accel_slope_1y(retearn: pd.Series) -> pd.Series:
    """Rolling 1-year OLS slope of the retearn QoQ acceleration series."""
    base = _d2_retearn_qoq_accel(retearn)
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
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def eqe_drv3_014_equity_qoq_pct_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative equity QoQ pct-change acceleration."""
    prior = equity.shift(_TD_QTR)
    pct   = _safe_div_abs(equity - prior, prior)
    d2    = pct - pct.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_015_retearn_yoy_pct_3rd_deriv(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative retearn YoY pct-change."""
    prior = retearn.shift(_TD_YEAR)
    pct   = _safe_div_abs(retearn - prior, prior)
    d2    = pct - pct.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_016_equity_drawdown_pct_1y_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative equity drawdown pct from 1y peak."""
    peak = _rolling_max(equity, _TD_YEAR)
    pct  = _safe_div_abs(equity - peak, peak)
    d2   = pct - pct.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_017_equity_to_assets_3rd_deriv(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative equity/assets QoQ change."""
    ratio = _safe_div(equity, assets)
    d1    = ratio - ratio.shift(_TD_QTR)
    d2    = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_018_tangible_equity_3rd_deriv(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative tangible equity YoY change."""
    tbe  = equity - intangibles
    d1   = tbe - tbe.shift(_TD_YEAR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_019_bvps_yoy_pct_3rd_deriv(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative BVPS YoY pct change."""
    bvps  = _safe_div(equity, sharesbas)
    prior = bvps.shift(_TD_YEAR)
    pct   = _safe_div_abs(bvps - prior, prior)
    d2    = pct - pct.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_020_equity_zscore_yoy_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative (YoY of equity z-score)."""
    m  = _rolling_mean(equity, _TD_YEAR)
    sd = _rolling_std(equity, _TD_YEAR)
    z  = _safe_div(equity - m, sd)
    d1 = z - z.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_021_retearn_zscore_yoy_3rd_deriv(retearn: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative (YoY of retearn z-score)."""
    m  = _rolling_mean(retearn, _TD_YEAR)
    sd = _rolling_std(retearn, _TD_YEAR)
    z  = _safe_div(retearn - m, sd)
    d1 = z - z.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_022_equity_ewm_diff_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-derivative of (equity QoQ vs. its EWM)."""
    d1  = equity - equity.shift(_TD_QTR)
    ewm = d1.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base = d1 - ewm
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_023_equity_drawdown_exp_yoy_3rd_deriv(equity: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change of the 2nd-derivative (YoY of expanding drawdown)."""
    peak = equity.expanding(min_periods=1).max()
    dd   = equity - peak
    d1   = dd - dd.shift(_TD_YEAR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_024_retearn_deficit_expansion_3rd_deriv(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """
    3rd derivative: QoQ change in the 2nd-derivative of the retearn/|equity| ratio.
    Captures jerk in the accumulated-deficit-to-equity dynamic.
    """
    ratio = _safe_div(retearn, equity.abs().replace(0, np.nan))
    d1    = ratio - ratio.shift(_TD_QTR)
    d2    = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def eqe_drv3_025_composite_3rd_deriv(equity: pd.Series, retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """
    3rd derivative of composite equity-erosion z-score:
    average of equity z-score, retearn z-score, equity/assets z-score — triple-differenced QoQ.
    Captures the curvature of curvature in multi-dimensional book-value distress.
    """
    z_eq = _safe_div(equity  - _rolling_mean(equity, _TD_YEAR),  _rolling_std(equity, _TD_YEAR))
    z_re = _safe_div(retearn - _rolling_mean(retearn, _TD_YEAR), _rolling_std(retearn, _TD_YEAR))
    ea   = _safe_div(equity, assets)
    z_ea = _safe_div(ea - _rolling_mean(ea, _TD_YEAR), _rolling_std(ea, _TD_YEAR))
    comp = (z_eq + z_re + z_ea) / 3.0
    d1   = comp - comp.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

EQUITY_EROSION_REGISTRY_3RD_DERIVATIVES = {
    "eqe_drv3_001_equity_qoq_accel_qoq_diff":           {"inputs": ["equity"],                      "func": eqe_drv3_001_equity_qoq_accel_qoq_diff},
    "eqe_drv3_002_equity_yoy_qoq_diff_qoq_diff":        {"inputs": ["equity"],                      "func": eqe_drv3_002_equity_yoy_qoq_diff_qoq_diff},
    "eqe_drv3_003_retearn_qoq_accel_qoq_diff":          {"inputs": ["retearn"],                     "func": eqe_drv3_003_retearn_qoq_accel_qoq_diff},
    "eqe_drv3_004_retearn_yoy_qoq_diff_qoq_diff":       {"inputs": ["retearn"],                     "func": eqe_drv3_004_retearn_yoy_qoq_diff_qoq_diff},
    "eqe_drv3_005_equity_drawdown_1y_qoq_diff_qoq_diff":{"inputs": ["equity"],                      "func": eqe_drv3_005_equity_drawdown_1y_qoq_diff_qoq_diff},
    "eqe_drv3_006_equity_drawdown_exp_3rd_deriv":        {"inputs": ["equity"],                      "func": eqe_drv3_006_equity_drawdown_exp_3rd_deriv},
    "eqe_drv3_007_retearn_drawdown_exp_3rd_deriv":       {"inputs": ["retearn"],                     "func": eqe_drv3_007_retearn_drawdown_exp_3rd_deriv},
    "eqe_drv3_008_equity_zscore_3rd_deriv":              {"inputs": ["equity"],                      "func": eqe_drv3_008_equity_zscore_3rd_deriv},
    "eqe_drv3_009_retearn_zscore_3rd_deriv":             {"inputs": ["retearn"],                     "func": eqe_drv3_009_retearn_zscore_3rd_deriv},
    "eqe_drv3_010_bvps_qoq_accel_qoq_diff":             {"inputs": ["equity", "sharesbas"],         "func": eqe_drv3_010_bvps_qoq_accel_qoq_diff},
    "eqe_drv3_011_netinc_ttm_3rd_deriv":                 {"inputs": ["netinc"],                      "func": eqe_drv3_011_netinc_ttm_3rd_deriv},
    "eqe_drv3_012_equity_qoq_accel_slope_1y":            {"inputs": ["equity"],                      "func": eqe_drv3_012_equity_qoq_accel_slope_1y},
    "eqe_drv3_013_retearn_qoq_accel_slope_1y":           {"inputs": ["retearn"],                     "func": eqe_drv3_013_retearn_qoq_accel_slope_1y},
    "eqe_drv3_014_equity_qoq_pct_3rd_deriv":             {"inputs": ["equity"],                      "func": eqe_drv3_014_equity_qoq_pct_3rd_deriv},
    "eqe_drv3_015_retearn_yoy_pct_3rd_deriv":            {"inputs": ["retearn"],                     "func": eqe_drv3_015_retearn_yoy_pct_3rd_deriv},
    "eqe_drv3_016_equity_drawdown_pct_1y_3rd_deriv":     {"inputs": ["equity"],                      "func": eqe_drv3_016_equity_drawdown_pct_1y_3rd_deriv},
    "eqe_drv3_017_equity_to_assets_3rd_deriv":           {"inputs": ["equity", "assets"],            "func": eqe_drv3_017_equity_to_assets_3rd_deriv},
    "eqe_drv3_018_tangible_equity_3rd_deriv":            {"inputs": ["equity", "intangibles"],       "func": eqe_drv3_018_tangible_equity_3rd_deriv},
    "eqe_drv3_019_bvps_yoy_pct_3rd_deriv":               {"inputs": ["equity", "sharesbas"],         "func": eqe_drv3_019_bvps_yoy_pct_3rd_deriv},
    "eqe_drv3_020_equity_zscore_yoy_3rd_deriv":          {"inputs": ["equity"],                      "func": eqe_drv3_020_equity_zscore_yoy_3rd_deriv},
    "eqe_drv3_021_retearn_zscore_yoy_3rd_deriv":         {"inputs": ["retearn"],                     "func": eqe_drv3_021_retearn_zscore_yoy_3rd_deriv},
    "eqe_drv3_022_equity_ewm_diff_3rd_deriv":            {"inputs": ["equity"],                      "func": eqe_drv3_022_equity_ewm_diff_3rd_deriv},
    "eqe_drv3_023_equity_drawdown_exp_yoy_3rd_deriv":    {"inputs": ["equity"],                      "func": eqe_drv3_023_equity_drawdown_exp_yoy_3rd_deriv},
    "eqe_drv3_024_retearn_deficit_expansion_3rd_deriv":  {"inputs": ["retearn", "equity"],           "func": eqe_drv3_024_retearn_deficit_expansion_3rd_deriv},
    "eqe_drv3_025_composite_3rd_deriv":                  {"inputs": ["equity", "retearn", "assets"], "func": eqe_drv3_025_composite_3rd_deriv},
}
