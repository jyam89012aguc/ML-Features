"""
65_leverage_stress — 2nd-Derivative Features 001-025
Domain: rate of change of base leverage-stress features
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _de_ratio(debt, equity):
    return _safe_div(debt, equity)


def _da_ratio(debt, assets):
    return _safe_div(debt, assets)


def _la_ratio(liabilities, assets):
    return _safe_div(liabilities, assets)


def _net_debt(debt, cashnequiv):
    return debt - cashnequiv


def _nd_equity(debt, cashnequiv, equity):
    return _safe_div(debt - cashnequiv, equity)


def _nd_ebitda(debt, cashnequiv, ebitda):
    return _safe_div(debt - cashnequiv, ebitda)


def _fin_lev(assets, equity):
    return _safe_div(assets, equity)


def _st_mix(debtc, debt):
    return _safe_div(debtc, debt)


def _de_zscore_4q(debt, equity):
    ratio = _de_ratio(debt, equity)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, sd)


def _da_zscore_4q(debt, assets):
    ratio = _da_ratio(debt, assets)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, sd)


def _nd_drawup_4q_min(debt, cashnequiv):
    nd = _net_debt(debt, cashnequiv)
    return nd - _rolling_min(nd, _TD_YEAR)


def _leverage_drawup_4q_min(debt, equity):
    ratio = _de_ratio(debt, equity)
    return ratio - _rolling_min(ratio, _TD_YEAR)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def lvs_drv2_001_de_ratio_qoq_diff_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ D/E change (acceleration of leverage buildup QoQ)."""
    base = _de_ratio(debt, equity) - _de_ratio(debt, equity).shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_002_de_ratio_yoy_diff_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the YoY D/E change (how fast the YoY leverage trend is shifting)."""
    base = _de_ratio(debt, equity) - _de_ratio(debt, equity).shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_003_da_ratio_qoq_diff_qoq(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the QoQ D/A change."""
    base = _da_ratio(debt, assets) - _da_ratio(debt, assets).shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_004_la_ratio_qoq_diff_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the QoQ L/A change."""
    base = _la_ratio(liabilities, assets) - _la_ratio(liabilities, assets).shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_005_net_debt_qoq_diff_qoq(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the QoQ net-debt change (net-debt acceleration)."""
    nd   = _net_debt(debt, cashnequiv)
    base = nd - nd.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_006_nd_equity_qoq_diff_qoq(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ net-D/equity change."""
    base = _nd_equity(debt, cashnequiv, equity)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_007_nd_ebitda_qoq_diff_qoq(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in the QoQ net-D/EBITDA change."""
    base = _nd_ebitda(debt, cashnequiv, ebitda)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_008_de_zscore_4q_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of D/E ratio."""
    base = _de_zscore_4q(debt, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv2_009_de_zscore_4q_yoy_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of D/E ratio."""
    base = _de_zscore_4q(debt, equity)
    return base - base.shift(_TD_YEAR)


def lvs_drv2_010_da_zscore_4q_qoq_diff(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of D/A ratio."""
    base = _da_zscore_4q(debt, assets)
    return base - base.shift(_TD_QTR)


def lvs_drv2_011_leverage_drawup_4q_min_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the D/E drawup from 4-quarter minimum."""
    base = _leverage_drawup_4q_min(debt, equity)
    return base - base.shift(_TD_QTR)


def lvs_drv2_012_nd_drawup_4q_min_qoq_diff(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in net-debt drawup from its 4-quarter minimum."""
    base = _nd_drawup_4q_min(debt, cashnequiv)
    return base - base.shift(_TD_QTR)


def lvs_drv2_013_st_mix_qoq_diff_qoq(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in the QoQ short-term-debt-mix change."""
    base = _st_mix(debtc, debt)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_014_fin_lev_qoq_diff_qoq(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ financial-leverage-multiplier change."""
    base = _fin_lev(assets, equity)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_015_de_ratio_pct_chg_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ percent change in the D/E ratio itself."""
    ratio = _de_ratio(debt, equity)
    prior = ratio.shift(_TD_QTR)
    return _safe_div_abs(ratio - prior, prior)


def lvs_drv2_016_de_ratio_yoy_pct_chg(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY percent change in D/E ratio."""
    ratio = _de_ratio(debt, equity)
    prior = ratio.shift(_TD_YEAR)
    return _safe_div_abs(ratio - prior, prior)


def lvs_drv2_017_de_ratio_slope_of_qoq_trend(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ D/E-change series.
    Captures trend in leverage-buildup momentum.
    """
    base = _de_ratio(debt, equity) - _de_ratio(debt, equity).shift(_TD_QTR)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def lvs_drv2_018_net_debt_yoy_diff_yoy(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the YoY net-debt change (2nd-order YoY net-debt acceleration)."""
    nd   = _net_debt(debt, cashnequiv)
    base = nd - nd.shift(_TD_YEAR)
    return base - base.shift(_TD_YEAR)


def lvs_drv2_019_equity_qoq_diff_qoq(equity: pd.Series) -> pd.Series:
    """QoQ change in the QoQ equity change (equity erosion acceleration)."""
    d1 = equity - equity.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_020_debt_to_ebitda_qoq_diff_qoq(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in the QoQ D/EBITDA change."""
    base = _safe_div(debt, ebitda)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_021_la_ratio_yoy_diff_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the YoY L/A change."""
    base = _la_ratio(liabilities, assets) - _la_ratio(liabilities, assets).shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def lvs_drv2_022_de_ratio_ewm_diff_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    QoQ change in (D/E minus its 4-quarter EWM).
    Measures whether leverage deviation from trend is accelerating.
    """
    ratio = _de_ratio(debt, equity)
    ewm   = ratio.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base  = ratio - ewm
    return base - base.shift(_TD_QTR)


def lvs_drv2_023_nd_ebitda_yoy_diff_qoq(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in the YoY net-D/EBITDA change."""
    base = _nd_ebitda(debt, cashnequiv, ebitda)
    d1   = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def lvs_drv2_024_de_ratio_drawup_pct_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    QoQ change in (D/E pct deviation above its 4-quarter mean).
    """
    ratio = _de_ratio(debt, equity)
    avg   = _rolling_mean(ratio, _TD_YEAR)
    base  = _safe_div_abs(ratio - avg, avg)
    return base - base.shift(_TD_QTR)


def lvs_drv2_025_leverage_composite_zscore_qoq_diff(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    QoQ change in the composite leverage z-score
    (average of z-scores of D/E, D/A, D/EBITDA within 4-quarter window).
    """
    z_de  = _de_zscore_4q(debt, equity)
    z_da  = _da_zscore_4q(debt, assets)
    de_eb = _safe_div(debt, ebitda)
    m3    = _rolling_mean(de_eb, _TD_YEAR)
    sd3   = _rolling_std(de_eb, _TD_YEAR)
    z_deb = _safe_div(de_eb - m3, sd3)
    comp  = (z_de + z_da + z_deb) / 3.0
    return comp - comp.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

LEVERAGE_STRESS_REGISTRY_2ND_DERIVATIVES = {
    "lvs_drv2_001_de_ratio_qoq_diff_qoq":           {"inputs": ["debt", "equity"],                        "func": lvs_drv2_001_de_ratio_qoq_diff_qoq},
    "lvs_drv2_002_de_ratio_yoy_diff_qoq":           {"inputs": ["debt", "equity"],                        "func": lvs_drv2_002_de_ratio_yoy_diff_qoq},
    "lvs_drv2_003_da_ratio_qoq_diff_qoq":           {"inputs": ["debt", "assets"],                        "func": lvs_drv2_003_da_ratio_qoq_diff_qoq},
    "lvs_drv2_004_la_ratio_qoq_diff_qoq":           {"inputs": ["liabilities", "assets"],                 "func": lvs_drv2_004_la_ratio_qoq_diff_qoq},
    "lvs_drv2_005_net_debt_qoq_diff_qoq":           {"inputs": ["debt", "cashnequiv"],                    "func": lvs_drv2_005_net_debt_qoq_diff_qoq},
    "lvs_drv2_006_nd_equity_qoq_diff_qoq":          {"inputs": ["debt", "cashnequiv", "equity"],          "func": lvs_drv2_006_nd_equity_qoq_diff_qoq},
    "lvs_drv2_007_nd_ebitda_qoq_diff_qoq":          {"inputs": ["debt", "cashnequiv", "ebitda"],          "func": lvs_drv2_007_nd_ebitda_qoq_diff_qoq},
    "lvs_drv2_008_de_zscore_4q_qoq_diff":           {"inputs": ["debt", "equity"],                        "func": lvs_drv2_008_de_zscore_4q_qoq_diff},
    "lvs_drv2_009_de_zscore_4q_yoy_diff":           {"inputs": ["debt", "equity"],                        "func": lvs_drv2_009_de_zscore_4q_yoy_diff},
    "lvs_drv2_010_da_zscore_4q_qoq_diff":           {"inputs": ["debt", "assets"],                        "func": lvs_drv2_010_da_zscore_4q_qoq_diff},
    "lvs_drv2_011_leverage_drawup_4q_min_qoq_diff": {"inputs": ["debt", "equity"],                        "func": lvs_drv2_011_leverage_drawup_4q_min_qoq_diff},
    "lvs_drv2_012_nd_drawup_4q_min_qoq_diff":       {"inputs": ["debt", "cashnequiv"],                    "func": lvs_drv2_012_nd_drawup_4q_min_qoq_diff},
    "lvs_drv2_013_st_mix_qoq_diff_qoq":             {"inputs": ["debtc", "debt"],                         "func": lvs_drv2_013_st_mix_qoq_diff_qoq},
    "lvs_drv2_014_fin_lev_qoq_diff_qoq":            {"inputs": ["assets", "equity"],                      "func": lvs_drv2_014_fin_lev_qoq_diff_qoq},
    "lvs_drv2_015_de_ratio_pct_chg_qoq":            {"inputs": ["debt", "equity"],                        "func": lvs_drv2_015_de_ratio_pct_chg_qoq},
    "lvs_drv2_016_de_ratio_yoy_pct_chg":            {"inputs": ["debt", "equity"],                        "func": lvs_drv2_016_de_ratio_yoy_pct_chg},
    "lvs_drv2_017_de_ratio_slope_of_qoq_trend":     {"inputs": ["debt", "equity"],                        "func": lvs_drv2_017_de_ratio_slope_of_qoq_trend},
    "lvs_drv2_018_net_debt_yoy_diff_yoy":           {"inputs": ["debt", "cashnequiv"],                    "func": lvs_drv2_018_net_debt_yoy_diff_yoy},
    "lvs_drv2_019_equity_qoq_diff_qoq":             {"inputs": ["equity"],                                "func": lvs_drv2_019_equity_qoq_diff_qoq},
    "lvs_drv2_020_debt_to_ebitda_qoq_diff_qoq":     {"inputs": ["debt", "ebitda"],                        "func": lvs_drv2_020_debt_to_ebitda_qoq_diff_qoq},
    "lvs_drv2_021_la_ratio_yoy_diff_qoq":           {"inputs": ["liabilities", "assets"],                 "func": lvs_drv2_021_la_ratio_yoy_diff_qoq},
    "lvs_drv2_022_de_ratio_ewm_diff_qoq":           {"inputs": ["debt", "equity"],                        "func": lvs_drv2_022_de_ratio_ewm_diff_qoq},
    "lvs_drv2_023_nd_ebitda_yoy_diff_qoq":          {"inputs": ["debt", "cashnequiv", "ebitda"],          "func": lvs_drv2_023_nd_ebitda_yoy_diff_qoq},
    "lvs_drv2_024_de_ratio_drawup_pct_qoq_diff":    {"inputs": ["debt", "equity"],                        "func": lvs_drv2_024_de_ratio_drawup_pct_qoq_diff},
    "lvs_drv2_025_leverage_composite_zscore_qoq_diff": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": lvs_drv2_025_leverage_composite_zscore_qoq_diff},
}
