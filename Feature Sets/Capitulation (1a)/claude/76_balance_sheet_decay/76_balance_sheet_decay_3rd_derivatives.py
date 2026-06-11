"""
76_balance_sheet_decay — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative balance-sheet decay features
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
    this helper is for documentation and optional manual use.
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


# ── 2nd-derivative base helpers (self-contained) ─────────────────────────────

def _equity_yoy(equity: pd.Series) -> pd.Series:
    return equity - equity.shift(_TD_YEAR)


def _equity_qoq(equity: pd.Series) -> pd.Series:
    return equity - equity.shift(_TD_QTR)


def _assets_yoy(assets: pd.Series) -> pd.Series:
    return assets - assets.shift(_TD_YEAR)


def _nav(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    return assets - liabilities


def _nav_yoy(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    nav = _nav(assets, liabilities)
    return nav - nav.shift(_TD_YEAR)


def _retearn_yoy(retearn: pd.Series) -> pd.Series:
    return retearn - retearn.shift(_TD_YEAR)


def _debt_yoy(debt: pd.Series) -> pd.Series:
    return debt - debt.shift(_TD_YEAR)


def _liab_yoy(liabilities: pd.Series) -> pd.Series:
    return liabilities - liabilities.shift(_TD_YEAR)


def _bs_health_4q(assets: pd.Series, liabilities: pd.Series,
                   equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    def _z(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)
    return (_z(assets) + _z(-liabilities) + _z(equity) + _z(cashnequiv)) / 4.0


def _equity_drawdown_4q(equity: pd.Series) -> pd.Series:
    return equity - _rolling_max(equity, _TD_YEAR)


def _nav_drawdown_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    nav = _nav(assets, liabilities)
    return nav - _rolling_max(nav, _TD_YEAR)


def _liab_to_assets(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(liabilities, assets)


def _debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(debt, equity.abs().replace(0, np.nan))


# ── 2nd-derivative intermediate computations ─────────────────────────────────

def _drv2_equity_yoy_qoq(equity: pd.Series) -> pd.Series:
    base = _equity_yoy(equity)
    return base - base.shift(_TD_QTR)


def _drv2_nav_yoy_qoq(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    base = _nav_yoy(assets, liabilities)
    return base - base.shift(_TD_QTR)


def _drv2_retearn_yoy_qoq(retearn: pd.Series) -> pd.Series:
    base = _retearn_yoy(retearn)
    return base - base.shift(_TD_QTR)


def _drv2_debt_yoy_qoq(debt: pd.Series) -> pd.Series:
    base = _debt_yoy(debt)
    return base - base.shift(_TD_QTR)


def _drv2_liab_yoy_qoq(liabilities: pd.Series) -> pd.Series:
    base = _liab_yoy(liabilities)
    return base - base.shift(_TD_QTR)


def _drv2_bs_health_qoq(assets: pd.Series, liabilities: pd.Series,
                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_QTR)


def _drv2_equity_drawdown_qoq(equity: pd.Series) -> pd.Series:
    base = _equity_drawdown_4q(equity)
    return base - base.shift(_TD_QTR)


def _drv2_nav_drawdown_qoq(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    base = _nav_drawdown_4q(assets, liabilities)
    return base - base.shift(_TD_QTR)


def _drv2_liab_to_assets_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    base = _liab_to_assets(liabilities, assets)
    return base - base.shift(_TD_QTR)


def _drv2_debt_to_equity_qoq(debt: pd.Series, equity: pd.Series) -> pd.Series:
    base = _debt_to_equity(debt, equity)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions 001-025 ─────────────────────────────────

def bsd_drv3_001_equity_yoy_qoq_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY equity): 3rd-order equity derivative."""
    base = _drv2_equity_yoy_qoq(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_002_equity_yoy_qoq_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY equity): cross-window 3rd derivative."""
    base = _drv2_equity_yoy_qoq(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_003_nav_yoy_qoq_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY NAV): 3rd-order NAV derivative."""
    base = _drv2_nav_yoy_qoq(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv3_004_retearn_yoy_qoq_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY retained earnings): 3rd-order derivative."""
    base = _drv2_retearn_yoy_qoq(retearn)
    return base - base.shift(_TD_QTR)


def bsd_drv3_005_debt_yoy_qoq_qoq_diff(debt: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY debt): 3rd-order debt derivative."""
    base = _drv2_debt_yoy_qoq(debt)
    return base - base.shift(_TD_QTR)


def bsd_drv3_006_liab_yoy_qoq_qoq_diff(liabilities: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY liabilities): 3rd-order derivative."""
    base = _drv2_liab_yoy_qoq(liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv3_007_bs_health_qoq_qoq_diff(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in BS health index): health acceleration's rate of change."""
    base = _drv2_bs_health_qoq(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv3_008_bs_health_qoq_yoy_diff(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in BS health index)."""
    base = _drv2_bs_health_qoq(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_009_equity_drawdown_qoq_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in equity 4Q-peak drawdown): 3rd-order drawdown."""
    base = _drv2_equity_drawdown_qoq(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_010_nav_drawdown_qoq_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in NAV 4Q-peak drawdown): 3rd-order NAV drawdown."""
    base = _drv2_nav_drawdown_qoq(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv3_011_liab_to_assets_qoq_qoq_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in liabilities/assets ratio): 3rd-order leverage."""
    base = _drv2_liab_to_assets_qoq(liabilities, assets)
    return base - base.shift(_TD_QTR)


def bsd_drv3_012_debt_to_equity_qoq_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in debt/equity ratio): 3rd-order D/E ratio."""
    base = _drv2_debt_to_equity_qoq(debt, equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_013_equity_yoy_qoq_ewm_diff(equity: pd.Series) -> pd.Series:
    """
    2nd-derivative equity signal minus its EWM:
    (QoQ change in YoY equity change) minus own EWM (span=252).
    Captures whether 2nd-derivative deterioration is worsening vs its own trend.
    """
    base = _drv2_equity_yoy_qoq(equity)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_014_nav_yoy_qoq_ewm_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """
    (QoQ change in YoY NAV change) minus its own EWM (span=252).
    """
    base = _drv2_nav_yoy_qoq(assets, liabilities)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_015_bs_health_qoq_ewm_diff(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    (QoQ change in BS health index) minus its own EWM (span=252).
    3rd-order: are health worsening steps themselves accelerating beyond trend?
    """
    base = _drv2_bs_health_qoq(assets, liabilities, equity, cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_016_equity_yoy_qoq_slope_4q(equity: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the 2nd-derivative equity series
    (QoQ change in YoY equity change).
    """
    base = _drv2_equity_yoy_qoq(equity)

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
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv3_017_nav_yoy_qoq_slope_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the 2nd-derivative NAV series."""
    base = _drv2_nav_yoy_qoq(assets, liabilities)

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
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv3_018_equity_qoq_3rd_diff(equity: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of equity: d3/dq3 via QoQ steps."""
    d1 = equity - equity.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3


def bsd_drv3_019_assets_qoq_3rd_diff(assets: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of total assets."""
    d1 = assets - assets.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3


def bsd_drv3_020_nav_qoq_3rd_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of net asset value."""
    nav = _nav(assets, liabilities)
    d1  = nav - nav.shift(_TD_QTR)
    d2  = d1 - d1.shift(_TD_QTR)
    d3  = d2 - d2.shift(_TD_QTR)
    return d3


def bsd_drv3_021_debt_qoq_3rd_diff(debt: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of total debt."""
    d1 = debt - debt.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3


def bsd_drv3_022_retearn_qoq_3rd_diff(retearn: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of retained earnings."""
    d1 = retearn - retearn.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3


def bsd_drv3_023_bs_health_yoy_qoq_diff(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    QoQ change in (YoY change in BS health index):
    Cross-window 3rd-derivative of BS health.
    """
    health = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    yoy    = health - health.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_QTR)


def bsd_drv3_024_equity_drawdown_qoq_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in equity 4Q-peak drawdown): mixed-window 3rd derivative."""
    base = _drv2_equity_drawdown_qoq(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_025_bs_decay_3rd_order_composite(assets: pd.Series, liabilities: pd.Series,
                                               equity: pd.Series, cashnequiv: pd.Series,
                                               retearn: pd.Series) -> pd.Series:
    """
    3rd-order composite: average of 3rd finite differences of equity, NAV, and retearn,
    each normalized by their own 4-quarter rolling std.
    Captures the curvature of multi-line balance-sheet deterioration.
    """
    def _normed_3rd(s):
        d1 = s - s.shift(_TD_QTR)
        d2 = d1 - d1.shift(_TD_QTR)
        d3 = d2 - d2.shift(_TD_QTR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(d3, sd)

    nav = assets - liabilities
    n_eq  = _normed_3rd(equity)
    n_nav = _normed_3rd(nav)
    n_re  = _normed_3rd(retearn)
    return (n_eq + n_nav + n_re) / 3.0


# ── Additional 2nd-derivative helpers for 3rd-derivative features 026-075 ────

def _drv2_equity_yoy_yoy(equity: pd.Series) -> pd.Series:
    base = _equity_yoy(equity)
    return base - base.shift(_TD_YEAR)


def _drv2_assets_yoy_qoq(assets: pd.Series) -> pd.Series:
    base = _assets_yoy(assets)
    return base - base.shift(_TD_QTR)


def _drv2_debt_yoy_qoq2(debt: pd.Series) -> pd.Series:
    base = _debt_yoy(debt)
    return base - base.shift(_TD_QTR)


def _drv2_liab_yoy_qoq2(liabilities: pd.Series) -> pd.Series:
    base = _liab_yoy(liabilities)
    return base - base.shift(_TD_QTR)


def _drv2_retearn_yoy_qoq2(retearn: pd.Series) -> pd.Series:
    base = _retearn_yoy(retearn)
    return base - base.shift(_TD_QTR)


def _drv2_cashnequiv_yoy_qoq(cashnequiv: pd.Series) -> pd.Series:
    base = cashnequiv - cashnequiv.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_invcap_yoy_qoq(invcap: pd.Series) -> pd.Series:
    base = invcap - invcap.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_workingcapital_yoy_qoq(workingcapital: pd.Series) -> pd.Series:
    base = workingcapital - workingcapital.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def _drv2_equity_drawdown_8q_qoq(equity: pd.Series) -> pd.Series:
    dd = equity - equity.rolling(_TD_2Y, min_periods=max(1, _TD_2Y // 4)).max()
    return dd - dd.shift(_TD_QTR)


def _drv2_nav_drawdown_8q_qoq(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    nav = _nav(assets, liabilities)
    dd  = nav - nav.rolling(_TD_2Y, min_periods=max(1, _TD_2Y // 4)).max()
    return dd - dd.shift(_TD_QTR)


def _drv2_debt_to_assets_qoq(debt: pd.Series, assets: pd.Series) -> pd.Series:
    ratio = _safe_div(debt, assets)
    return ratio - ratio.shift(_TD_QTR)


def _drv2_liab_to_equity_qoq(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    ratio = _safe_div(liabilities, equity.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def _drv2_bs_health_8q_qoq(assets: pd.Series, liabilities: pd.Series,
                             equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    def _z8(s):
        m  = _rolling_mean(s, _TD_2Y)
        sd = _rolling_std(s, _TD_2Y)
        return _safe_div(s - m, sd)
    h = (_z8(assets) + _z8(-liabilities) + _z8(equity) + _z8(cashnequiv)) / 4.0
    return h - h.shift(_TD_QTR)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def bsd_drv3_026_equity_yoy_yoy_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in (YoY change in YoY equity): 3rd-order cross-window derivative."""
    base = _drv2_equity_yoy_yoy(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_027_equity_yoy_yoy_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in (YoY change in YoY equity): pure 3rd-order YoY derivative."""
    base = _drv2_equity_yoy_yoy(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_028_assets_yoy_qoq_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY assets): 3rd-order assets derivative."""
    base = _drv2_assets_yoy_qoq(assets)
    return base - base.shift(_TD_QTR)


def bsd_drv3_029_assets_yoy_qoq_yoy_diff(assets: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY assets): mixed-window 3rd derivative."""
    base = _drv2_assets_yoy_qoq(assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_030_debt_yoy_qoq_yoy_diff(debt: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY debt): cross-window 3rd derivative."""
    base = _drv2_debt_yoy_qoq2(debt)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_031_liab_yoy_qoq_yoy_diff(liabilities: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY liabilities): 3rd-order derivative."""
    base = _drv2_liab_yoy_qoq2(liabilities)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_032_retearn_yoy_qoq_yoy_diff(retearn: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY retained earnings): 3rd-order derivative."""
    base = _drv2_retearn_yoy_qoq2(retearn)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_033_cashnequiv_yoy_qoq_qoq_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY cash): 3rd-order cash derivative."""
    base = _drv2_cashnequiv_yoy_qoq(cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv3_034_cashnequiv_yoy_qoq_yoy_diff(cashnequiv: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in YoY cash): mixed-window 3rd-order derivative."""
    base = _drv2_cashnequiv_yoy_qoq(cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_035_invcap_yoy_qoq_qoq_diff(invcap: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY invested capital): 3rd-order derivative."""
    base = _drv2_invcap_yoy_qoq(invcap)
    return base - base.shift(_TD_QTR)


def bsd_drv3_036_workingcapital_yoy_qoq_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in YoY working capital): 3rd-order derivative."""
    base = _drv2_workingcapital_yoy_qoq(workingcapital)
    return base - base.shift(_TD_QTR)


def bsd_drv3_037_equity_drawdown_8q_qoq_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in equity 8Q-peak drawdown): 3rd-order."""
    base = _drv2_equity_drawdown_8q_qoq(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_038_nav_drawdown_8q_qoq_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in NAV 8Q-peak drawdown): 3rd-order."""
    base = _drv2_nav_drawdown_8q_qoq(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv3_039_debt_to_assets_qoq_qoq_diff(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in debt/assets ratio): 3rd-order leverage."""
    base = _drv2_debt_to_assets_qoq(debt, assets)
    return base - base.shift(_TD_QTR)


def bsd_drv3_040_liab_to_equity_qoq_qoq_diff(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in liab/equity ratio): 3rd-order derivative."""
    base = _drv2_liab_to_equity_qoq(liabilities, equity)
    return base - base.shift(_TD_QTR)


def bsd_drv3_041_bs_health_8q_qoq_qoq_diff(assets: pd.Series, liabilities: pd.Series,
                                             equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in (QoQ change in 8Q BS health index): 3rd-order health acceleration."""
    base = _drv2_bs_health_8q_qoq(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv3_042_bs_health_8q_qoq_yoy_diff(assets: pd.Series, liabilities: pd.Series,
                                             equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in 8Q BS health index): cross-window 3rd order."""
    base = _drv2_bs_health_8q_qoq(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_043_equity_qoq_3rd_diff_ewm(equity: pd.Series) -> pd.Series:
    """Pure 3rd QoQ diff of equity minus its own EWM (span=252)."""
    d1 = equity - equity.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    ewm = d3.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d3 - ewm


def bsd_drv3_044_assets_qoq_3rd_diff_ewm(assets: pd.Series) -> pd.Series:
    """Pure 3rd QoQ diff of assets minus its own EWM (span=252)."""
    d1 = assets - assets.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    ewm = d3.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d3 - ewm


def bsd_drv3_045_nav_qoq_3rd_diff_ewm(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Pure 3rd QoQ diff of NAV minus its own EWM."""
    nav = _nav(assets, liabilities)
    d1 = nav - nav.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    ewm = d3.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d3 - ewm


def bsd_drv3_046_debt_qoq_3rd_diff_ewm(debt: pd.Series) -> pd.Series:
    """Pure 3rd QoQ diff of debt minus its own EWM."""
    d1 = debt - debt.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    ewm = d3.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d3 - ewm


def bsd_drv3_047_retearn_qoq_3rd_diff_ewm(retearn: pd.Series) -> pd.Series:
    """Pure 3rd QoQ diff of retained earnings minus its own EWM."""
    d1 = retearn - retearn.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    ewm = d3.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d3 - ewm


def bsd_drv3_048_equity_yoy_qoq_slope_8q(equity: pd.Series) -> pd.Series:
    """Rolling 8-quarter OLS slope of the 2nd-derivative equity series."""
    base = _drv2_equity_yoy_qoq(equity)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def bsd_drv3_049_nav_yoy_qoq_slope_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 8-quarter OLS slope of the 2nd-derivative NAV series."""
    base = _drv2_nav_yoy_qoq(assets, liabilities)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def bsd_drv3_050_bs_health_qoq_slope_4q(assets: pd.Series, liabilities: pd.Series,
                                          equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the 2nd-derivative BS health QoQ series."""
    base = _drv2_bs_health_qoq(assets, liabilities, equity, cashnequiv)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv3_051_debt_yoy_qoq_ewm_diff(debt: pd.Series) -> pd.Series:
    """(QoQ change in YoY debt change) minus its own EWM: 3rd-order debt acceleration vs trend."""
    base = _drv2_debt_yoy_qoq2(debt)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_052_liab_yoy_qoq_ewm_diff(liabilities: pd.Series) -> pd.Series:
    """(QoQ change in YoY liabilities change) minus its own EWM."""
    base = _drv2_liab_yoy_qoq2(liabilities)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_053_retearn_yoy_qoq_ewm_diff(retearn: pd.Series) -> pd.Series:
    """(QoQ change in YoY retained-earnings change) minus its own EWM."""
    base = _drv2_retearn_yoy_qoq2(retearn)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_054_cashnequiv_yoy_qoq_ewm_diff(cashnequiv: pd.Series) -> pd.Series:
    """(QoQ change in YoY cash change) minus its own EWM."""
    base = _drv2_cashnequiv_yoy_qoq(cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_055_invcap_yoy_qoq_ewm_diff(invcap: pd.Series) -> pd.Series:
    """(QoQ change in YoY invested-capital change) minus its own EWM."""
    base = _drv2_invcap_yoy_qoq(invcap)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_056_equity_drawdown_qoq_slope_4q(equity: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the 2nd-derivative equity drawdown QoQ series."""
    base = _drv2_equity_drawdown_qoq(equity)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv3_057_nav_drawdown_qoq_slope_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the 2nd-derivative NAV drawdown QoQ series."""
    base = _drv2_nav_drawdown_qoq(assets, liabilities)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv3_058_liab_to_assets_qoq_yoy_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in liab/assets ratio): cross-window 3rd order."""
    base = _drv2_liab_to_assets_qoq(liabilities, assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_059_debt_to_equity_qoq_yoy_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in (QoQ change in debt/equity ratio): cross-window 3rd order."""
    base = _drv2_debt_to_equity_qoq(debt, equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv3_060_equity_liabilities_ratio(equity: pd.Series) -> pd.Series:
    """Pure 3rd QoQ finite diff of equity, normalized by trailing 4Q std — curvature signal."""
    d1 = equity - equity.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    d3 = d2 - d2.shift(_TD_QTR)
    sd = _rolling_std(equity, _TD_YEAR)
    return _safe_div(d3, sd)


def bsd_drv3_061_liab_qoq_3rd_diff(liabilities: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of total liabilities via QoQ steps."""
    d1 = liabilities - liabilities.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def bsd_drv3_062_cashnequiv_qoq_3rd_diff(cashnequiv: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of cash and equivalents via QoQ steps."""
    d1 = cashnequiv - cashnequiv.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def bsd_drv3_063_invcap_qoq_3rd_diff(invcap: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of invested capital via QoQ steps."""
    d1 = invcap - invcap.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def bsd_drv3_064_workingcapital_qoq_3rd_diff(workingcapital: pd.Series) -> pd.Series:
    """Pure 3rd finite difference of working capital via QoQ steps."""
    d1 = workingcapital - workingcapital.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def bsd_drv3_065_bs_decay_3rd_order_5line(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series,
                                           debt: pd.Series) -> pd.Series:
    """
    3rd-order composite: normalized 3rd finite differences of 5 lines
    (equity, NAV, cash, negative-debt, assets), averaged.
    """
    def _nd3(s):
        d1 = s - s.shift(_TD_QTR)
        d2 = d1 - d1.shift(_TD_QTR)
        d3 = d2 - d2.shift(_TD_QTR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(d3, sd)

    nav = assets - liabilities
    return (_nd3(equity) + _nd3(nav) + _nd3(cashnequiv) + _nd3(-debt) + _nd3(assets)) / 5.0


def bsd_drv3_066_equity_yoy_qoq_zscore_4q(equity: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative equity signal (QoQ of YoY) within a 4Q window."""
    base = _drv2_equity_yoy_qoq(equity)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_067_nav_yoy_qoq_zscore_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative NAV signal (QoQ of YoY) within a 4Q window."""
    base = _drv2_nav_yoy_qoq(assets, liabilities)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_068_debt_yoy_qoq_zscore_4q(debt: pd.Series) -> pd.Series:
    """Z-score of (QoQ of YoY debt change) within a 4Q window."""
    base = _drv2_debt_yoy_qoq2(debt)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_069_liab_yoy_qoq_zscore_4q(liabilities: pd.Series) -> pd.Series:
    """Z-score of (QoQ of YoY liabilities change) within a 4Q window."""
    base = _drv2_liab_yoy_qoq2(liabilities)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_070_bs_health_qoq_zscore_4q(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of (QoQ change in BS health index) within a 4Q window."""
    base = _drv2_bs_health_qoq(assets, liabilities, equity, cashnequiv)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_071_retearn_yoy_qoq_zscore_4q(retearn: pd.Series) -> pd.Series:
    """Z-score of (QoQ of YoY retained-earnings change) within a 4Q window."""
    base = _drv2_retearn_yoy_qoq2(retearn)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_072_cashnequiv_yoy_qoq_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of (QoQ of YoY cash change) within a 4Q window."""
    base = _drv2_cashnequiv_yoy_qoq(cashnequiv)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def bsd_drv3_073_bs_decay_3rd_6line_normalized(assets: pd.Series, liabilities: pd.Series,
                                                equity: pd.Series, cashnequiv: pd.Series,
                                                retearn: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Normalized 3rd-order composite: z-scores of 2nd-derivative signals for
    equity, NAV, cash, retearn, negative-debt, assets; average of 6.
    """
    nav = assets - liabilities

    def _drv2_qoq(s):
        b = s - s.shift(_TD_YEAR)
        return b - b.shift(_TD_QTR)

    def _zscore2(s):
        base = _drv2_qoq(s)
        m  = _rolling_mean(base, _TD_YEAR)
        sd = _rolling_std(base, _TD_YEAR)
        return _safe_div(base - m, sd)

    return (_zscore2(equity) + _zscore2(nav) + _zscore2(cashnequiv) +
            _zscore2(retearn) + _zscore2(-debt) + _zscore2(assets)) / 6.0


def bsd_drv3_074_equity_drawdown_8q_qoq_ewm_diff(equity: pd.Series) -> pd.Series:
    """(QoQ change in 8Q-peak equity drawdown) minus its own EWM."""
    base = _drv2_equity_drawdown_8q_qoq(equity)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv3_075_bs_decay_curvature_4q_composite(assets: pd.Series, liabilities: pd.Series,
                                                   equity: pd.Series, cashnequiv: pd.Series,
                                                   retearn: pd.Series) -> pd.Series:
    """
    4Q composite curvature of balance-sheet decay: OLS slope of the 2nd-derivative
    (QoQ of YoY) series for equity, NAV, cash, retearn over trailing 4Q, averaged.
    Negative = accelerating deterioration whose rate is itself worsening.
    """
    nav = assets - liabilities

    def _drv2_qoq_series(s):
        b = s - s.shift(_TD_YEAR)
        return b - b.shift(_TD_QTR)

    def _slope4q(s):
        def _slope(arr):
            n = len(arr)
            if n < 2:
                return np.nan
            x = np.arange(n, dtype=float)
            xm = x.mean(); ym = arr.mean()
            denom = ((x - xm) ** 2).sum()
            return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom
        return s.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)

    return (_slope4q(_drv2_qoq_series(equity)) +
            _slope4q(_drv2_qoq_series(nav)) +
            _slope4q(_drv2_qoq_series(cashnequiv)) +
            _slope4q(_drv2_qoq_series(retearn))) / 4.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

BALANCE_SHEET_DECAY_REGISTRY_3RD_DERIVATIVES = {
    "bsd_drv3_001_equity_yoy_qoq_qoq_diff":   {"inputs": ["equity"],                                              "func": bsd_drv3_001_equity_yoy_qoq_qoq_diff},
    "bsd_drv3_002_equity_yoy_qoq_yoy_diff":   {"inputs": ["equity"],                                              "func": bsd_drv3_002_equity_yoy_qoq_yoy_diff},
    "bsd_drv3_003_nav_yoy_qoq_qoq_diff":      {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_003_nav_yoy_qoq_qoq_diff},
    "bsd_drv3_004_retearn_yoy_qoq_qoq_diff":  {"inputs": ["retearn"],                                             "func": bsd_drv3_004_retearn_yoy_qoq_qoq_diff},
    "bsd_drv3_005_debt_yoy_qoq_qoq_diff":     {"inputs": ["debt"],                                                "func": bsd_drv3_005_debt_yoy_qoq_qoq_diff},
    "bsd_drv3_006_liab_yoy_qoq_qoq_diff":     {"inputs": ["liabilities"],                                         "func": bsd_drv3_006_liab_yoy_qoq_qoq_diff},
    "bsd_drv3_007_bs_health_qoq_qoq_diff":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv3_007_bs_health_qoq_qoq_diff},
    "bsd_drv3_008_bs_health_qoq_yoy_diff":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv3_008_bs_health_qoq_yoy_diff},
    "bsd_drv3_009_equity_drawdown_qoq_qoq_diff":{"inputs": ["equity"],                                            "func": bsd_drv3_009_equity_drawdown_qoq_qoq_diff},
    "bsd_drv3_010_nav_drawdown_qoq_qoq_diff": {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_010_nav_drawdown_qoq_qoq_diff},
    "bsd_drv3_011_liab_to_assets_qoq_qoq_diff":{"inputs": ["liabilities", "assets"],                              "func": bsd_drv3_011_liab_to_assets_qoq_qoq_diff},
    "bsd_drv3_012_debt_to_equity_qoq_qoq_diff":{"inputs": ["debt", "equity"],                                     "func": bsd_drv3_012_debt_to_equity_qoq_qoq_diff},
    "bsd_drv3_013_equity_yoy_qoq_ewm_diff":   {"inputs": ["equity"],                                              "func": bsd_drv3_013_equity_yoy_qoq_ewm_diff},
    "bsd_drv3_014_nav_yoy_qoq_ewm_diff":      {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_014_nav_yoy_qoq_ewm_diff},
    "bsd_drv3_015_bs_health_qoq_ewm_diff":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv3_015_bs_health_qoq_ewm_diff},
    "bsd_drv3_016_equity_yoy_qoq_slope_4q":   {"inputs": ["equity"],                                              "func": bsd_drv3_016_equity_yoy_qoq_slope_4q},
    "bsd_drv3_017_nav_yoy_qoq_slope_4q":      {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_017_nav_yoy_qoq_slope_4q},
    "bsd_drv3_018_equity_qoq_3rd_diff":       {"inputs": ["equity"],                                              "func": bsd_drv3_018_equity_qoq_3rd_diff},
    "bsd_drv3_019_assets_qoq_3rd_diff":       {"inputs": ["assets"],                                              "func": bsd_drv3_019_assets_qoq_3rd_diff},
    "bsd_drv3_020_nav_qoq_3rd_diff":          {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_020_nav_qoq_3rd_diff},
    "bsd_drv3_021_debt_qoq_3rd_diff":         {"inputs": ["debt"],                                                "func": bsd_drv3_021_debt_qoq_3rd_diff},
    "bsd_drv3_022_retearn_qoq_3rd_diff":      {"inputs": ["retearn"],                                             "func": bsd_drv3_022_retearn_qoq_3rd_diff},
    "bsd_drv3_023_bs_health_yoy_qoq_diff":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv3_023_bs_health_yoy_qoq_diff},
    "bsd_drv3_024_equity_drawdown_qoq_yoy_diff":{"inputs": ["equity"],                                            "func": bsd_drv3_024_equity_drawdown_qoq_yoy_diff},
    "bsd_drv3_025_bs_decay_3rd_order_composite":{"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn"], "func": bsd_drv3_025_bs_decay_3rd_order_composite},
    "bsd_drv3_026_equity_yoy_yoy_qoq_diff":     {"inputs": ["equity"],                                              "func": bsd_drv3_026_equity_yoy_yoy_qoq_diff},
    "bsd_drv3_027_equity_yoy_yoy_yoy_diff":     {"inputs": ["equity"],                                              "func": bsd_drv3_027_equity_yoy_yoy_yoy_diff},
    "bsd_drv3_028_assets_yoy_qoq_qoq_diff":     {"inputs": ["assets"],                                              "func": bsd_drv3_028_assets_yoy_qoq_qoq_diff},
    "bsd_drv3_029_assets_yoy_qoq_yoy_diff":     {"inputs": ["assets"],                                              "func": bsd_drv3_029_assets_yoy_qoq_yoy_diff},
    "bsd_drv3_030_debt_yoy_qoq_yoy_diff":       {"inputs": ["debt"],                                                "func": bsd_drv3_030_debt_yoy_qoq_yoy_diff},
    "bsd_drv3_031_liab_yoy_qoq_yoy_diff":       {"inputs": ["liabilities"],                                         "func": bsd_drv3_031_liab_yoy_qoq_yoy_diff},
    "bsd_drv3_032_retearn_yoy_qoq_yoy_diff":    {"inputs": ["retearn"],                                             "func": bsd_drv3_032_retearn_yoy_qoq_yoy_diff},
    "bsd_drv3_033_cashnequiv_yoy_qoq_qoq_diff": {"inputs": ["cashnequiv"],                                          "func": bsd_drv3_033_cashnequiv_yoy_qoq_qoq_diff},
    "bsd_drv3_034_cashnequiv_yoy_qoq_yoy_diff": {"inputs": ["cashnequiv"],                                          "func": bsd_drv3_034_cashnequiv_yoy_qoq_yoy_diff},
    "bsd_drv3_035_invcap_yoy_qoq_qoq_diff":     {"inputs": ["invcap"],                                              "func": bsd_drv3_035_invcap_yoy_qoq_qoq_diff},
    "bsd_drv3_036_workingcapital_yoy_qoq_qoq_diff":{"inputs": ["workingcapital"],                                   "func": bsd_drv3_036_workingcapital_yoy_qoq_qoq_diff},
    "bsd_drv3_037_equity_drawdown_8q_qoq_qoq_diff":{"inputs": ["equity"],                                           "func": bsd_drv3_037_equity_drawdown_8q_qoq_qoq_diff},
    "bsd_drv3_038_nav_drawdown_8q_qoq_qoq_diff":{"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_038_nav_drawdown_8q_qoq_qoq_diff},
    "bsd_drv3_039_debt_to_assets_qoq_qoq_diff": {"inputs": ["debt", "assets"],                                      "func": bsd_drv3_039_debt_to_assets_qoq_qoq_diff},
    "bsd_drv3_040_liab_to_equity_qoq_qoq_diff": {"inputs": ["liabilities", "equity"],                               "func": bsd_drv3_040_liab_to_equity_qoq_qoq_diff},
    "bsd_drv3_041_bs_health_8q_qoq_qoq_diff":   {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],      "func": bsd_drv3_041_bs_health_8q_qoq_qoq_diff},
    "bsd_drv3_042_bs_health_8q_qoq_yoy_diff":   {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],      "func": bsd_drv3_042_bs_health_8q_qoq_yoy_diff},
    "bsd_drv3_043_equity_qoq_3rd_diff_ewm":     {"inputs": ["equity"],                                              "func": bsd_drv3_043_equity_qoq_3rd_diff_ewm},
    "bsd_drv3_044_assets_qoq_3rd_diff_ewm":     {"inputs": ["assets"],                                              "func": bsd_drv3_044_assets_qoq_3rd_diff_ewm},
    "bsd_drv3_045_nav_qoq_3rd_diff_ewm":        {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_045_nav_qoq_3rd_diff_ewm},
    "bsd_drv3_046_debt_qoq_3rd_diff_ewm":       {"inputs": ["debt"],                                                "func": bsd_drv3_046_debt_qoq_3rd_diff_ewm},
    "bsd_drv3_047_retearn_qoq_3rd_diff_ewm":    {"inputs": ["retearn"],                                             "func": bsd_drv3_047_retearn_qoq_3rd_diff_ewm},
    "bsd_drv3_048_equity_yoy_qoq_slope_8q":     {"inputs": ["equity"],                                              "func": bsd_drv3_048_equity_yoy_qoq_slope_8q},
    "bsd_drv3_049_nav_yoy_qoq_slope_8q":        {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_049_nav_yoy_qoq_slope_8q},
    "bsd_drv3_050_bs_health_qoq_slope_4q":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],      "func": bsd_drv3_050_bs_health_qoq_slope_4q},
    "bsd_drv3_051_debt_yoy_qoq_ewm_diff":       {"inputs": ["debt"],                                                "func": bsd_drv3_051_debt_yoy_qoq_ewm_diff},
    "bsd_drv3_052_liab_yoy_qoq_ewm_diff":       {"inputs": ["liabilities"],                                         "func": bsd_drv3_052_liab_yoy_qoq_ewm_diff},
    "bsd_drv3_053_retearn_yoy_qoq_ewm_diff":    {"inputs": ["retearn"],                                             "func": bsd_drv3_053_retearn_yoy_qoq_ewm_diff},
    "bsd_drv3_054_cashnequiv_yoy_qoq_ewm_diff": {"inputs": ["cashnequiv"],                                          "func": bsd_drv3_054_cashnequiv_yoy_qoq_ewm_diff},
    "bsd_drv3_055_invcap_yoy_qoq_ewm_diff":     {"inputs": ["invcap"],                                              "func": bsd_drv3_055_invcap_yoy_qoq_ewm_diff},
    "bsd_drv3_056_equity_drawdown_qoq_slope_4q":{"inputs": ["equity"],                                              "func": bsd_drv3_056_equity_drawdown_qoq_slope_4q},
    "bsd_drv3_057_nav_drawdown_qoq_slope_4q":   {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_057_nav_drawdown_qoq_slope_4q},
    "bsd_drv3_058_liab_to_assets_qoq_yoy_diff": {"inputs": ["liabilities", "assets"],                               "func": bsd_drv3_058_liab_to_assets_qoq_yoy_diff},
    "bsd_drv3_059_debt_to_equity_qoq_yoy_diff": {"inputs": ["debt", "equity"],                                      "func": bsd_drv3_059_debt_to_equity_qoq_yoy_diff},
    "bsd_drv3_060_equity_liabilities_ratio":    {"inputs": ["equity"],                                              "func": bsd_drv3_060_equity_liabilities_ratio},
    "bsd_drv3_061_liab_qoq_3rd_diff":           {"inputs": ["liabilities"],                                         "func": bsd_drv3_061_liab_qoq_3rd_diff},
    "bsd_drv3_062_cashnequiv_qoq_3rd_diff":     {"inputs": ["cashnequiv"],                                          "func": bsd_drv3_062_cashnequiv_qoq_3rd_diff},
    "bsd_drv3_063_invcap_qoq_3rd_diff":         {"inputs": ["invcap"],                                              "func": bsd_drv3_063_invcap_qoq_3rd_diff},
    "bsd_drv3_064_workingcapital_qoq_3rd_diff": {"inputs": ["workingcapital"],                                      "func": bsd_drv3_064_workingcapital_qoq_3rd_diff},
    "bsd_drv3_065_bs_decay_3rd_order_5line":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "debt"], "func": bsd_drv3_065_bs_decay_3rd_order_5line},
    "bsd_drv3_066_equity_yoy_qoq_zscore_4q":    {"inputs": ["equity"],                                              "func": bsd_drv3_066_equity_yoy_qoq_zscore_4q},
    "bsd_drv3_067_nav_yoy_qoq_zscore_4q":       {"inputs": ["assets", "liabilities"],                               "func": bsd_drv3_067_nav_yoy_qoq_zscore_4q},
    "bsd_drv3_068_debt_yoy_qoq_zscore_4q":      {"inputs": ["debt"],                                                "func": bsd_drv3_068_debt_yoy_qoq_zscore_4q},
    "bsd_drv3_069_liab_yoy_qoq_zscore_4q":      {"inputs": ["liabilities"],                                         "func": bsd_drv3_069_liab_yoy_qoq_zscore_4q},
    "bsd_drv3_070_bs_health_qoq_zscore_4q":     {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],      "func": bsd_drv3_070_bs_health_qoq_zscore_4q},
    "bsd_drv3_071_retearn_yoy_qoq_zscore_4q":   {"inputs": ["retearn"],                                             "func": bsd_drv3_071_retearn_yoy_qoq_zscore_4q},
    "bsd_drv3_072_cashnequiv_yoy_qoq_zscore_4q":{"inputs": ["cashnequiv"],                                          "func": bsd_drv3_072_cashnequiv_yoy_qoq_zscore_4q},
    "bsd_drv3_073_bs_decay_3rd_6line_normalized":{"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "debt"], "func": bsd_drv3_073_bs_decay_3rd_6line_normalized},
    "bsd_drv3_074_equity_drawdown_8q_qoq_ewm_diff":{"inputs": ["equity"],                                           "func": bsd_drv3_074_equity_drawdown_8q_qoq_ewm_diff},
    "bsd_drv3_075_bs_decay_curvature_4q_composite":{"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn"], "func": bsd_drv3_075_bs_decay_curvature_4q_composite},
}
