"""
65_leverage_stress — 3rd-Derivative Features 001-025
Domain: rate-of-change of 2nd-derivative leverage-stress features
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
    """
    Element-wise division; replaces zero denominator with NaN.
    Negative denominators (e.g. negative equity) are preserved as-is.
    """
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


# ── 2nd-derivative helpers (self-contained) ──────────────────────────────────
# Each helper returns the 2nd-derivative concept that the 3rd-derivative
# feature will differentiate further.

def _d2_de_qoq(debt, equity):
    """D/E QoQ change acceleration (2nd diff QoQ)."""
    ratio = _safe_div(debt, equity)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_da_qoq(debt, assets):
    """D/A QoQ change acceleration."""
    ratio = _safe_div(debt, assets)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_nd_qoq(debt, cashnequiv):
    """Net-debt QoQ change acceleration."""
    nd = debt - cashnequiv
    d1 = nd - nd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_la_qoq(liabilities, assets):
    """L/A QoQ change acceleration."""
    ratio = _safe_div(liabilities, assets)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_nde_qoq(debt, cashnequiv, equity):
    """Net-D/equity QoQ change acceleration."""
    ratio = _safe_div(debt - cashnequiv, equity)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_ndebitda_qoq(debt, cashnequiv, ebitda):
    """Net-D/EBITDA QoQ change acceleration."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_de_zscore_qoq(debt, equity):
    """QoQ diff of D/E z-score (4q window)."""
    ratio = _safe_div(debt, equity)
    m     = _rolling_mean(ratio, _TD_YEAR)
    sd    = _rolling_std(ratio, _TD_YEAR)
    z     = _safe_div(ratio - m, sd)
    return z - z.shift(_TD_QTR)


def _d2_equity_erosion(equity):
    """QoQ change in QoQ equity change."""
    d1 = equity - equity.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_fin_lev_qoq(assets, equity):
    """Financial leverage QoQ change acceleration."""
    ratio = _safe_div(assets, equity)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _d2_de_yoy_qoq(debt, equity):
    """QoQ diff of the YoY D/E change."""
    ratio = _safe_div(debt, equity)
    yoy   = ratio - ratio.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def lvs_drv3_001_de_qoq_accel_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the D/E QoQ acceleration (3rd diff over QoQ steps)."""
    base = _d2_de_qoq(debt, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_002_da_qoq_accel_qoq_diff(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the D/A QoQ acceleration."""
    base = _d2_da_qoq(debt, assets)
    return base - base.shift(_TD_QTR)


def lvs_drv3_003_nd_qoq_accel_qoq_diff(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the net-debt QoQ acceleration."""
    base = _d2_nd_qoq(debt, cashnequiv)
    return base - base.shift(_TD_QTR)


def lvs_drv3_004_la_qoq_accel_qoq_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the L/A QoQ acceleration."""
    base = _d2_la_qoq(liabilities, assets)
    return base - base.shift(_TD_QTR)


def lvs_drv3_005_nde_qoq_accel_qoq_diff(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the net-D/equity QoQ acceleration."""
    base = _d2_nde_qoq(debt, cashnequiv, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_006_ndebitda_qoq_accel_qoq_diff(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in the net-D/EBITDA QoQ acceleration."""
    base = _d2_ndebitda_qoq(debt, cashnequiv, ebitda)
    return base - base.shift(_TD_QTR)


def lvs_drv3_007_de_zscore_accel_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff-of-D/E-zscore (3rd-order z-score momentum)."""
    base = _d2_de_zscore_qoq(debt, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_008_equity_erosion_accel_qoq(equity: pd.Series) -> pd.Series:
    """QoQ change in equity QoQ-change acceleration (3rd diff equity)."""
    base = _d2_equity_erosion(equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_009_fin_lev_accel_qoq_diff(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in financial-leverage QoQ acceleration."""
    base = _d2_fin_lev_qoq(assets, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_010_de_yoy_accel_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in QoQ-diff-of-YoY-D/E (3rd-order YoY derivative)."""
    base = _d2_de_yoy_qoq(debt, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv3_011_de_qoq_accel_yoy_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in D/E QoQ acceleration."""
    base = _d2_de_qoq(debt, equity)
    return base - base.shift(_TD_YEAR)


def lvs_drv3_012_nd_qoq_accel_yoy_diff(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in net-debt QoQ acceleration."""
    base = _d2_nd_qoq(debt, cashnequiv)
    return base - base.shift(_TD_YEAR)


def lvs_drv3_013_de_accel_pct_chg_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ percent change in D/E QoQ acceleration series."""
    base  = _d2_de_qoq(debt, equity)
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def lvs_drv3_014_nd_accel_pct_chg_qoq(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ percent change in net-debt QoQ acceleration."""
    base  = _d2_nd_qoq(debt, cashnequiv)
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def lvs_drv3_015_de_accel_ewm_deviation(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E acceleration minus its 4-quarter EWM (capturing unusual jerk)."""
    base = _d2_de_qoq(debt, equity)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def lvs_drv3_016_nd_accel_ewm_deviation(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net-debt acceleration minus its 4-quarter EWM."""
    base = _d2_nd_qoq(debt, cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def lvs_drv3_017_de_zscore_accel_rolling_mean_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter mean of the D/E z-score QoQ acceleration."""
    base = _d2_de_zscore_qoq(debt, equity)
    return _rolling_mean(base, _TD_YEAR)


def lvs_drv3_018_composite_accel_score(debt: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """
    Average QoQ change across three 2nd-derivative series:
    D/E acceleration, D/A acceleration, financial-leverage acceleration.
    """
    a1 = _d2_de_qoq(debt, equity)
    a2 = _d2_da_qoq(debt, assets)
    a3 = _d2_fin_lev_qoq(assets, equity)
    d1 = a1 - a1.shift(_TD_QTR)
    d2 = a2 - a2.shift(_TD_QTR)
    d3 = a3 - a3.shift(_TD_QTR)
    return (d1 + d2 + d3) / 3.0


def lvs_drv3_019_de_accel_zscore_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of D/E QoQ-acceleration within trailing 4-quarter window."""
    base = _d2_de_qoq(debt, equity)
    m    = _rolling_mean(base, _TD_YEAR)
    sd   = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def lvs_drv3_020_nd_accel_zscore_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of net-debt QoQ-acceleration within trailing 4-quarter window."""
    base = _d2_nd_qoq(debt, cashnequiv)
    m    = _rolling_mean(base, _TD_YEAR)
    sd   = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def lvs_drv3_021_de_3rd_diff_above_zero_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if 3rd derivative of D/E (QoQ accel delta) is positive — worsening jerk."""
    base  = _d2_de_qoq(debt, equity)
    third = base - base.shift(_TD_QTR)
    return (third > 0).astype(float)


def lvs_drv3_022_nd_3rd_diff_above_zero_flag(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """1 if 3rd derivative of net-debt (QoQ accel delta) is positive."""
    base  = _d2_nd_qoq(debt, cashnequiv)
    third = base - base.shift(_TD_QTR)
    return (third > 0).astype(float)


def lvs_drv3_023_de_accel_worst_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter maximum (worst/highest) D/E QoQ acceleration."""
    base = _d2_de_qoq(debt, equity)
    return _rolling_max(base, _TD_YEAR)


def lvs_drv3_024_nd_accel_worst_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Rolling 4-quarter maximum (worst) net-debt QoQ acceleration."""
    base = _d2_nd_qoq(debt, cashnequiv)
    return _rolling_max(base, _TD_YEAR)


def lvs_drv3_025_leverage_jerk_composite(debt: pd.Series, equity: pd.Series, assets: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative leverage-jerk score:
    equally-weighted average of QoQ-accel-deltas for D/E, D/A, net-D/equity,
    and net-D/EBITDA — measures simultaneous deterioration of all leverage
    dimensions at the 3rd-order level.
    """
    a1 = _d2_de_qoq(debt, equity)
    a2 = _d2_da_qoq(debt, assets)
    a3 = _d2_nde_qoq(debt, cashnequiv, equity)
    a4 = _d2_ndebitda_qoq(debt, cashnequiv, ebitda)
    d1 = a1 - a1.shift(_TD_QTR)
    d2 = a2 - a2.shift(_TD_QTR)
    d3 = a3 - a3.shift(_TD_QTR)
    d4 = a4 - a4.shift(_TD_QTR)
    return (d1 + d2 + d3 + d4) / 4.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

LEVERAGE_STRESS_REGISTRY_3RD_DERIVATIVES = {
    "lvs_drv3_001_de_qoq_accel_qoq_diff":           {"inputs": ["debt", "equity"],                          "func": lvs_drv3_001_de_qoq_accel_qoq_diff},
    "lvs_drv3_002_da_qoq_accel_qoq_diff":           {"inputs": ["debt", "assets"],                          "func": lvs_drv3_002_da_qoq_accel_qoq_diff},
    "lvs_drv3_003_nd_qoq_accel_qoq_diff":           {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_003_nd_qoq_accel_qoq_diff},
    "lvs_drv3_004_la_qoq_accel_qoq_diff":           {"inputs": ["liabilities", "assets"],                   "func": lvs_drv3_004_la_qoq_accel_qoq_diff},
    "lvs_drv3_005_nde_qoq_accel_qoq_diff":          {"inputs": ["debt", "cashnequiv", "equity"],            "func": lvs_drv3_005_nde_qoq_accel_qoq_diff},
    "lvs_drv3_006_ndebitda_qoq_accel_qoq_diff":     {"inputs": ["debt", "cashnequiv", "ebitda"],            "func": lvs_drv3_006_ndebitda_qoq_accel_qoq_diff},
    "lvs_drv3_007_de_zscore_accel_qoq_diff":        {"inputs": ["debt", "equity"],                          "func": lvs_drv3_007_de_zscore_accel_qoq_diff},
    "lvs_drv3_008_equity_erosion_accel_qoq":        {"inputs": ["equity"],                                  "func": lvs_drv3_008_equity_erosion_accel_qoq},
    "lvs_drv3_009_fin_lev_accel_qoq_diff":          {"inputs": ["assets", "equity"],                        "func": lvs_drv3_009_fin_lev_accel_qoq_diff},
    "lvs_drv3_010_de_yoy_accel_qoq_diff":           {"inputs": ["debt", "equity"],                          "func": lvs_drv3_010_de_yoy_accel_qoq_diff},
    "lvs_drv3_011_de_qoq_accel_yoy_diff":           {"inputs": ["debt", "equity"],                          "func": lvs_drv3_011_de_qoq_accel_yoy_diff},
    "lvs_drv3_012_nd_qoq_accel_yoy_diff":           {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_012_nd_qoq_accel_yoy_diff},
    "lvs_drv3_013_de_accel_pct_chg_qoq":            {"inputs": ["debt", "equity"],                          "func": lvs_drv3_013_de_accel_pct_chg_qoq},
    "lvs_drv3_014_nd_accel_pct_chg_qoq":            {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_014_nd_accel_pct_chg_qoq},
    "lvs_drv3_015_de_accel_ewm_deviation":          {"inputs": ["debt", "equity"],                          "func": lvs_drv3_015_de_accel_ewm_deviation},
    "lvs_drv3_016_nd_accel_ewm_deviation":          {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_016_nd_accel_ewm_deviation},
    "lvs_drv3_017_de_zscore_accel_rolling_mean_4q": {"inputs": ["debt", "equity"],                          "func": lvs_drv3_017_de_zscore_accel_rolling_mean_4q},
    "lvs_drv3_018_composite_accel_score":           {"inputs": ["debt", "equity", "assets"],                "func": lvs_drv3_018_composite_accel_score},
    "lvs_drv3_019_de_accel_zscore_4q":              {"inputs": ["debt", "equity"],                          "func": lvs_drv3_019_de_accel_zscore_4q},
    "lvs_drv3_020_nd_accel_zscore_4q":              {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_020_nd_accel_zscore_4q},
    "lvs_drv3_021_de_3rd_diff_above_zero_flag":     {"inputs": ["debt", "equity"],                          "func": lvs_drv3_021_de_3rd_diff_above_zero_flag},
    "lvs_drv3_022_nd_3rd_diff_above_zero_flag":     {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_022_nd_3rd_diff_above_zero_flag},
    "lvs_drv3_023_de_accel_worst_4q":               {"inputs": ["debt", "equity"],                          "func": lvs_drv3_023_de_accel_worst_4q},
    "lvs_drv3_024_nd_accel_worst_4q":               {"inputs": ["debt", "cashnequiv"],                      "func": lvs_drv3_024_nd_accel_worst_4q},
    "lvs_drv3_025_leverage_jerk_composite":         {"inputs": ["debt", "equity", "assets", "cashnequiv", "ebitda"], "func": lvs_drv3_025_leverage_jerk_composite},
}
