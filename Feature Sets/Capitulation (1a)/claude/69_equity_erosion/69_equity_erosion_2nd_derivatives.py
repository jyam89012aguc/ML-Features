"""
69_equity_erosion — 2nd-Derivative Features 001-025
Domain: rate of change / acceleration of base equity-erosion features
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


# ── Base concept helpers (self-contained — no cross-file imports) ─────────────

def _equity_qoq(equity: pd.Series) -> pd.Series:
    return equity - equity.shift(_TD_QTR)


def _equity_yoy(equity: pd.Series) -> pd.Series:
    return equity - equity.shift(_TD_YEAR)


def _equity_qoq_pct(equity: pd.Series) -> pd.Series:
    prior = equity.shift(_TD_QTR)
    return _safe_div_abs(equity - prior, prior)


def _equity_yoy_pct(equity: pd.Series) -> pd.Series:
    prior = equity.shift(_TD_YEAR)
    return _safe_div_abs(equity - prior, prior)


def _retearn_qoq(retearn: pd.Series) -> pd.Series:
    return retearn - retearn.shift(_TD_QTR)


def _retearn_yoy(retearn: pd.Series) -> pd.Series:
    return retearn - retearn.shift(_TD_YEAR)


def _retearn_qoq_pct(retearn: pd.Series) -> pd.Series:
    prior = retearn.shift(_TD_QTR)
    return _safe_div_abs(retearn - prior, prior)


def _equity_drawdown_1y(equity: pd.Series) -> pd.Series:
    return equity - _rolling_max(equity, _TD_YEAR)


def _equity_drawdown_2y(equity: pd.Series) -> pd.Series:
    return equity - _rolling_max(equity, _TD_2Y)


def _equity_drawdown_expanding(equity: pd.Series) -> pd.Series:
    peak = equity.expanding(min_periods=1).max()
    return equity - peak


def _retearn_drawdown_expanding(retearn: pd.Series) -> pd.Series:
    peak = retearn.expanding(min_periods=1).max()
    return retearn - peak


def _equity_zscore_4q(equity: pd.Series) -> pd.Series:
    m  = _rolling_mean(equity, _TD_YEAR)
    sd = _rolling_std(equity, _TD_YEAR)
    return _safe_div(equity - m, sd)


def _retearn_zscore_4q(retearn: pd.Series) -> pd.Series:
    m  = _rolling_mean(retearn, _TD_YEAR)
    sd = _rolling_std(retearn, _TD_YEAR)
    return _safe_div(retearn - m, sd)


def _equity_to_assets(equity: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(equity, assets)


def _bvps(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(equity, sharesbas)


def _tangible_equity(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    return equity - intangibles


def _netinc_ttm(netinc: pd.Series) -> pd.Series:
    return netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def eqe_drv2_001_equity_qoq_change_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ equity change (acceleration of equity erosion)."""
    base = _equity_qoq(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_002_equity_yoy_change_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the YoY equity change (how fast the YoY trend is worsening)."""
    base = _equity_yoy(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_003_equity_qoq_pct_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent equity change."""
    base = _equity_qoq_pct(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_004_equity_yoy_pct_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent equity change."""
    base = _equity_yoy_pct(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_005_retearn_qoq_change_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the QoQ retained-earnings change (acceleration of deficit accumulation)."""
    base = _retearn_qoq(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv2_006_retearn_yoy_change_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the YoY retained-earnings change."""
    base = _retearn_yoy(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv2_007_retearn_qoq_pct_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent retained-earnings change."""
    base = _retearn_qoq_pct(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv2_008_equity_drawdown_1y_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the 1-year equity peak drawdown (drawdown accelerating = worsening)."""
    base = _equity_drawdown_1y(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_009_equity_drawdown_2y_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the 2-year equity peak drawdown."""
    base = _equity_drawdown_2y(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_010_equity_drawdown_expanding_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the expanding-peak equity drawdown."""
    base = _equity_drawdown_expanding(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_011_equity_drawdown_expanding_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the expanding-peak equity drawdown."""
    base = _equity_drawdown_expanding(equity)
    return base - base.shift(_TD_YEAR)


def eqe_drv2_012_retearn_drawdown_expanding_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the expanding-peak retained-earnings drawdown."""
    base = _retearn_drawdown_expanding(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv2_013_equity_zscore_4q_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of total equity."""
    base = _equity_zscore_4q(equity)
    return base - base.shift(_TD_QTR)


def eqe_drv2_014_equity_zscore_4q_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of total equity."""
    base = _equity_zscore_4q(equity)
    return base - base.shift(_TD_YEAR)


def eqe_drv2_015_retearn_zscore_4q_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of retained earnings."""
    base = _retearn_zscore_4q(retearn)
    return base - base.shift(_TD_QTR)


def eqe_drv2_016_equity_to_assets_qoq_chg_qoq_diff(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the QoQ equity/assets ratio change (leverage worsening rate)."""
    ratio = _equity_to_assets(equity, assets)
    base  = ratio - ratio.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def eqe_drv2_017_bvps_qoq_change_qoq_diff(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the QoQ BVPS change (book-value-per-share erosion acceleration)."""
    bvps = _bvps(equity, sharesbas)
    base = bvps - bvps.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def eqe_drv2_018_bvps_yoy_pct_qoq_diff(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent BVPS change."""
    bvps  = _bvps(equity, sharesbas)
    prior = bvps.shift(_TD_YEAR)
    base  = _safe_div_abs(bvps - prior, prior)
    return base - base.shift(_TD_QTR)


def eqe_drv2_019_tangible_equity_yoy_qoq_diff(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """QoQ change in the YoY tangible equity change."""
    tbe  = _tangible_equity(equity, intangibles)
    base = tbe - tbe.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def eqe_drv2_020_netinc_ttm_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the TTM net income sum (worsening earnings stream into equity)."""
    base = _netinc_ttm(netinc)
    return base - base.shift(_TD_QTR)


def eqe_drv2_021_equity_yoy_pct_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the YoY percent equity change (2nd-order YoY erosion)."""
    base = _equity_yoy_pct(equity)
    return base - base.shift(_TD_YEAR)


def eqe_drv2_022_equity_drawdown_pct_1y_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in equity drawdown from 1-year peak as percent of abs(peak)."""
    peak = _rolling_max(equity, _TD_YEAR)
    base = _safe_div_abs(equity - peak, peak)
    return base - base.shift(_TD_QTR)


def eqe_drv2_023_retearn_yoy_pct_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent retained-earnings change."""
    prior = retearn.shift(_TD_YEAR)
    base  = _safe_div_abs(retearn - prior, prior)
    return base - base.shift(_TD_QTR)


def eqe_drv2_024_equity_qoq_ewm_diff(equity: pd.Series) -> pd.Series:
    """
    Current QoQ equity change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ erosion is worse than its recent trend.
    """
    base = _equity_qoq(equity)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def eqe_drv2_025_equity_erosion_composite_qoq_diff(equity: pd.Series, retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """
    QoQ change in a composite equity-erosion z-score:
    average of equity z-score, retearn z-score, equity/assets z-score — then differenced QoQ.
    """
    z_eq = _equity_zscore_4q(equity)
    z_re = _retearn_zscore_4q(retearn)
    ea   = _equity_to_assets(equity, assets)
    z_ea = _safe_div(ea - _rolling_mean(ea, _TD_YEAR), _rolling_std(ea, _TD_YEAR))
    base = (z_eq + z_re + z_ea) / 3.0
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

EQUITY_EROSION_REGISTRY_2ND_DERIVATIVES = {
    "eqe_drv2_001_equity_qoq_change_qoq_diff":           {"inputs": ["equity"],                    "func": eqe_drv2_001_equity_qoq_change_qoq_diff},
    "eqe_drv2_002_equity_yoy_change_qoq_diff":           {"inputs": ["equity"],                    "func": eqe_drv2_002_equity_yoy_change_qoq_diff},
    "eqe_drv2_003_equity_qoq_pct_qoq_diff":              {"inputs": ["equity"],                    "func": eqe_drv2_003_equity_qoq_pct_qoq_diff},
    "eqe_drv2_004_equity_yoy_pct_qoq_diff":              {"inputs": ["equity"],                    "func": eqe_drv2_004_equity_yoy_pct_qoq_diff},
    "eqe_drv2_005_retearn_qoq_change_qoq_diff":          {"inputs": ["retearn"],                   "func": eqe_drv2_005_retearn_qoq_change_qoq_diff},
    "eqe_drv2_006_retearn_yoy_change_qoq_diff":          {"inputs": ["retearn"],                   "func": eqe_drv2_006_retearn_yoy_change_qoq_diff},
    "eqe_drv2_007_retearn_qoq_pct_qoq_diff":             {"inputs": ["retearn"],                   "func": eqe_drv2_007_retearn_qoq_pct_qoq_diff},
    "eqe_drv2_008_equity_drawdown_1y_qoq_diff":          {"inputs": ["equity"],                    "func": eqe_drv2_008_equity_drawdown_1y_qoq_diff},
    "eqe_drv2_009_equity_drawdown_2y_qoq_diff":          {"inputs": ["equity"],                    "func": eqe_drv2_009_equity_drawdown_2y_qoq_diff},
    "eqe_drv2_010_equity_drawdown_expanding_qoq_diff":   {"inputs": ["equity"],                    "func": eqe_drv2_010_equity_drawdown_expanding_qoq_diff},
    "eqe_drv2_011_equity_drawdown_expanding_yoy_diff":   {"inputs": ["equity"],                    "func": eqe_drv2_011_equity_drawdown_expanding_yoy_diff},
    "eqe_drv2_012_retearn_drawdown_expanding_qoq_diff":  {"inputs": ["retearn"],                   "func": eqe_drv2_012_retearn_drawdown_expanding_qoq_diff},
    "eqe_drv2_013_equity_zscore_4q_qoq_diff":            {"inputs": ["equity"],                    "func": eqe_drv2_013_equity_zscore_4q_qoq_diff},
    "eqe_drv2_014_equity_zscore_4q_yoy_diff":            {"inputs": ["equity"],                    "func": eqe_drv2_014_equity_zscore_4q_yoy_diff},
    "eqe_drv2_015_retearn_zscore_4q_qoq_diff":           {"inputs": ["retearn"],                   "func": eqe_drv2_015_retearn_zscore_4q_qoq_diff},
    "eqe_drv2_016_equity_to_assets_qoq_chg_qoq_diff":   {"inputs": ["equity", "assets"],          "func": eqe_drv2_016_equity_to_assets_qoq_chg_qoq_diff},
    "eqe_drv2_017_bvps_qoq_change_qoq_diff":             {"inputs": ["equity", "sharesbas"],       "func": eqe_drv2_017_bvps_qoq_change_qoq_diff},
    "eqe_drv2_018_bvps_yoy_pct_qoq_diff":                {"inputs": ["equity", "sharesbas"],       "func": eqe_drv2_018_bvps_yoy_pct_qoq_diff},
    "eqe_drv2_019_tangible_equity_yoy_qoq_diff":         {"inputs": ["equity", "intangibles"],     "func": eqe_drv2_019_tangible_equity_yoy_qoq_diff},
    "eqe_drv2_020_netinc_ttm_qoq_diff":                  {"inputs": ["netinc"],                    "func": eqe_drv2_020_netinc_ttm_qoq_diff},
    "eqe_drv2_021_equity_yoy_pct_yoy_diff":              {"inputs": ["equity"],                    "func": eqe_drv2_021_equity_yoy_pct_yoy_diff},
    "eqe_drv2_022_equity_drawdown_pct_1y_qoq_diff":      {"inputs": ["equity"],                    "func": eqe_drv2_022_equity_drawdown_pct_1y_qoq_diff},
    "eqe_drv2_023_retearn_yoy_pct_qoq_diff":             {"inputs": ["retearn"],                   "func": eqe_drv2_023_retearn_yoy_pct_qoq_diff},
    "eqe_drv2_024_equity_qoq_ewm_diff":                  {"inputs": ["equity"],                    "func": eqe_drv2_024_equity_qoq_ewm_diff},
    "eqe_drv2_025_equity_erosion_composite_qoq_diff":    {"inputs": ["equity", "retearn", "assets"], "func": eqe_drv2_025_equity_erosion_composite_qoq_diff},
}
