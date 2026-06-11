"""
76_balance_sheet_decay — 2nd-Derivative Features 001-075
Domain: rate of change of base balance-sheet decay features
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline base computations so this file needs no cross-file imports.

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
    nav  = _nav(assets, liabilities)
    return nav - _rolling_max(nav, _TD_YEAR)


def _retearn_drawdown_4q(retearn: pd.Series) -> pd.Series:
    return retearn - _rolling_max(retearn, _TD_YEAR)


def _liab_to_assets(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(liabilities, assets)


def _debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(debt, equity.abs().replace(0, np.nan))


# ── 2nd-derivative feature functions 001-025 ─────────────────────────────────

def bsd_drv2_001_equity_yoy_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the YoY equity change (acceleration of equity trend)."""
    base = _equity_yoy(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv2_002_equity_yoy_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the YoY equity change (second-order YoY equity trend)."""
    base = _equity_yoy(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_003_assets_yoy_qoq_diff(assets: pd.Series) -> pd.Series:
    """QoQ change in the YoY assets change."""
    base = _assets_yoy(assets)
    return base - base.shift(_TD_QTR)


def bsd_drv2_004_nav_yoy_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in the YoY net-asset-value change."""
    base = _nav_yoy(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv2_005_nav_yoy_yoy_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """YoY change in the YoY NAV change (persistent multi-year erosion signal)."""
    base = _nav_yoy(assets, liabilities)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_006_retearn_yoy_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the YoY retained-earnings change."""
    base = _retearn_yoy(retearn)
    return base - base.shift(_TD_QTR)


def bsd_drv2_007_debt_yoy_qoq_diff(debt: pd.Series) -> pd.Series:
    """QoQ change in the YoY debt change (acceleration of debt accumulation)."""
    base = _debt_yoy(debt)
    return base - base.shift(_TD_QTR)


def bsd_drv2_008_liab_yoy_qoq_diff(liabilities: pd.Series) -> pd.Series:
    """QoQ change in the YoY liabilities change."""
    base = _liab_yoy(liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv2_009_bs_health_4q_qoq_diff(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the 4-line 4Q BS health index (health deterioration speed)."""
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv2_010_bs_health_4q_yoy_diff(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the 4-line 4Q BS health index."""
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_011_equity_drawdown_4q_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the equity 4Q-peak drawdown."""
    base = _equity_drawdown_4q(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv2_012_equity_drawdown_4q_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the equity 4Q-peak drawdown."""
    base = _equity_drawdown_4q(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_013_nav_drawdown_4q_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in the NAV 4Q-peak drawdown."""
    base = _nav_drawdown_4q(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv2_014_retearn_drawdown_4q_qoq_diff(retearn: pd.Series) -> pd.Series:
    """QoQ change in the retained-earnings 4Q-peak drawdown."""
    base = _retearn_drawdown_4q(retearn)
    return base - base.shift(_TD_QTR)


def bsd_drv2_015_liab_to_assets_qoq_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the liabilities-to-assets ratio."""
    base = _liab_to_assets(liabilities, assets)
    return base - base.shift(_TD_QTR)


def bsd_drv2_016_liab_to_assets_yoy_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in the liabilities-to-assets ratio."""
    base = _liab_to_assets(liabilities, assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_017_debt_to_equity_qoq_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the debt-to-equity ratio."""
    base = _debt_to_equity(debt, equity)
    return base - base.shift(_TD_QTR)


def bsd_drv2_018_equity_qoq_pct_chg_of_qoq(equity: pd.Series) -> pd.Series:
    """Percent change in the QoQ equity change (how much faster the QoQ decline is)."""
    base = _equity_qoq(equity)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def bsd_drv2_019_equity_yoy_slope_4q(equity: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the YoY equity-change series.
    Captures the trend in YoY equity momentum.
    """
    base = _equity_yoy(equity)

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


def bsd_drv2_020_nav_yoy_slope_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the YoY NAV-change series.
    """
    base = _nav_yoy(assets, liabilities)

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


def bsd_drv2_021_retearn_yoy_yoy_diff(retearn: pd.Series) -> pd.Series:
    """YoY change in the YoY retained-earnings change (second-order retained-earnings trend)."""
    base = _retearn_yoy(retearn)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_022_debt_yoy_yoy_diff(debt: pd.Series) -> pd.Series:
    """YoY change in the YoY debt change (persistent debt-growth acceleration)."""
    base = _debt_yoy(debt)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_023_equity_qoq_ewm_diff(equity: pd.Series) -> pd.Series:
    """
    QoQ equity change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ equity change is worse than its recent trend.
    """
    base = _equity_qoq(equity)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_024_bs_health_ewm_diff(assets: pd.Series, liabilities: pd.Series,
                                     equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    4-line BS health index minus its own 4-quarter EWM.
    Captures whether balance-sheet health is deteriorating faster than its trend.
    """
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_025_nav_cumulative_decay_accel(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """
    Change in the NAV drawdown from its expanding peak (2nd order):
    QoQ diff of (NAV - expanding_max(NAV)).
    Captures accelerating value destruction vs all-time peak.
    """
    nav  = _nav(assets, liabilities)
    peak = nav.expanding(min_periods=1).max()
    base = nav - peak
    return base - base.shift(_TD_QTR)


# ── Additional base helpers for features 026-075 ─────────────────────────────

def _invcap_yoy(invcap: pd.Series) -> pd.Series:
    return invcap - invcap.shift(_TD_YEAR)


def _cashnequiv_yoy(cashnequiv: pd.Series) -> pd.Series:
    return cashnequiv - cashnequiv.shift(_TD_YEAR)


def _workingcapital_yoy(workingcapital: pd.Series) -> pd.Series:
    return workingcapital - workingcapital.shift(_TD_YEAR)


def _assets_qoq(assets: pd.Series) -> pd.Series:
    return assets - assets.shift(_TD_QTR)


def _debt_qoq(debt: pd.Series) -> pd.Series:
    return debt - debt.shift(_TD_QTR)


def _retearn_qoq(retearn: pd.Series) -> pd.Series:
    return retearn - retearn.shift(_TD_QTR)


def _liab_qoq(liabilities: pd.Series) -> pd.Series:
    return liabilities - liabilities.shift(_TD_QTR)


def _invcap_qoq(invcap: pd.Series) -> pd.Series:
    return invcap - invcap.shift(_TD_QTR)


def _cashnequiv_qoq(cashnequiv: pd.Series) -> pd.Series:
    return cashnequiv - cashnequiv.shift(_TD_QTR)


def _workingcapital_qoq(workingcapital: pd.Series) -> pd.Series:
    return workingcapital - workingcapital.shift(_TD_QTR)


def _equity_drawdown_8q(equity: pd.Series) -> pd.Series:
    return equity - _rolling_max(equity, _TD_2Y)


def _nav_drawdown_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    nav = _nav(assets, liabilities)
    return nav - _rolling_max(nav, _TD_2Y)


def _cashnequiv_drawdown_4q(cashnequiv: pd.Series) -> pd.Series:
    return cashnequiv - _rolling_max(cashnequiv, _TD_YEAR)


def _debt_to_assets(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(debt, assets)


def _liab_to_equity(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(liabilities, equity.abs().replace(0, np.nan))


def _bs_health_8q(assets: pd.Series, liabilities: pd.Series,
                   equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    def _z(s):
        m  = _rolling_mean(s, _TD_2Y)
        sd = _rolling_std(s, _TD_2Y)
        return _safe_div(s - m, sd)
    return (_z(assets) + _z(-liabilities) + _z(equity) + _z(cashnequiv)) / 4.0


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def bsd_drv2_026_invcap_yoy_qoq_diff(invcap: pd.Series) -> pd.Series:
    """QoQ change in the YoY invested-capital change."""
    base = _invcap_yoy(invcap)
    return base - base.shift(_TD_QTR)


def bsd_drv2_027_cashnequiv_yoy_qoq_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the YoY cash-and-equivalents change."""
    base = _cashnequiv_yoy(cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv2_028_workingcapital_yoy_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the YoY working-capital change."""
    base = _workingcapital_yoy(workingcapital)
    return base - base.shift(_TD_QTR)


def bsd_drv2_029_assets_qoq_yoy_diff(assets: pd.Series) -> pd.Series:
    """YoY change in the QoQ assets change (cross-window 2nd derivative)."""
    base = _assets_qoq(assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_030_debt_qoq_yoy_diff(debt: pd.Series) -> pd.Series:
    """YoY change in the QoQ debt change."""
    base = _debt_qoq(debt)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_031_retearn_qoq_yoy_diff(retearn: pd.Series) -> pd.Series:
    """YoY change in the QoQ retained-earnings change."""
    base = _retearn_qoq(retearn)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_032_liab_qoq_yoy_diff(liabilities: pd.Series) -> pd.Series:
    """YoY change in the QoQ liabilities change."""
    base = _liab_qoq(liabilities)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_033_invcap_yoy_yoy_diff(invcap: pd.Series) -> pd.Series:
    """YoY change in the YoY invested-capital change (second-order YoY)."""
    base = _invcap_yoy(invcap)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_034_cashnequiv_yoy_yoy_diff(cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the YoY cash change (second-order YoY cash trend)."""
    base = _cashnequiv_yoy(cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_035_workingcapital_yoy_yoy_diff(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the YoY working-capital change."""
    base = _workingcapital_yoy(workingcapital)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_036_equity_drawdown_8q_qoq_diff(equity: pd.Series) -> pd.Series:
    """QoQ change in the equity 8Q-peak drawdown."""
    base = _equity_drawdown_8q(equity)
    return base - base.shift(_TD_QTR)


def bsd_drv2_037_nav_drawdown_8q_qoq_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """QoQ change in the NAV 8Q-peak drawdown."""
    base = _nav_drawdown_8q(assets, liabilities)
    return base - base.shift(_TD_QTR)


def bsd_drv2_038_cashnequiv_drawdown_4q_qoq_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the cash 4Q-peak drawdown."""
    base = _cashnequiv_drawdown_4q(cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv2_039_debt_to_assets_qoq_diff(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the debt-to-assets ratio."""
    base = _debt_to_assets(debt, assets)
    return base - base.shift(_TD_QTR)


def bsd_drv2_040_debt_to_assets_yoy_diff(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in the debt-to-assets ratio."""
    base = _debt_to_assets(debt, assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_041_liab_to_equity_qoq_diff(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the liabilities-to-equity ratio."""
    base = _liab_to_equity(liabilities, equity)
    return base - base.shift(_TD_QTR)


def bsd_drv2_042_liab_to_equity_yoy_diff(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the liabilities-to-equity ratio."""
    base = _liab_to_equity(liabilities, equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_043_bs_health_8q_qoq_diff(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the 4-line 8Q BS health index."""
    base = _bs_health_8q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_QTR)


def bsd_drv2_044_bs_health_8q_yoy_diff(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the 4-line 8Q BS health index."""
    base = _bs_health_8q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_045_equity_yoy_slope_8q(equity: pd.Series) -> pd.Series:
    """Rolling 8-quarter OLS slope of the YoY equity-change series."""
    base = _equity_yoy(equity)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def bsd_drv2_046_nav_yoy_slope_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 8-quarter OLS slope of the YoY NAV-change series."""
    base = _nav_yoy(assets, liabilities)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(_slope, raw=True)


def bsd_drv2_047_debt_yoy_slope_4q(debt: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the YoY debt-change series."""
    base = _debt_yoy(debt)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv2_048_liab_yoy_slope_4q(liabilities: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the YoY liabilities-change series."""
    base = _liab_yoy(liabilities)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv2_049_retearn_yoy_slope_4q(retearn: pd.Series) -> pd.Series:
    """Rolling 4-quarter OLS slope of the YoY retained-earnings-change series."""
    base = _retearn_yoy(retearn)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0.0 else ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def bsd_drv2_050_equity_qoq_ewm_diff_8q(equity: pd.Series) -> pd.Series:
    """QoQ equity change minus its own 8-quarter EWM (span=504)."""
    base = _equity_qoq(equity)
    ewm  = base.ewm(span=_TD_2Y, min_periods=max(1, _TD_2Y // 4)).mean()
    return base - ewm


def bsd_drv2_051_debt_qoq_ewm_diff(debt: pd.Series) -> pd.Series:
    """QoQ debt change minus its own 4-quarter EWM — debt acceleration vs trend."""
    base = _debt_qoq(debt)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_052_liab_yoy_ewm_diff(liabilities: pd.Series) -> pd.Series:
    """YoY liabilities change minus its own 4-quarter EWM."""
    base = _liab_yoy(liabilities)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_053_cashnequiv_yoy_ewm_diff(cashnequiv: pd.Series) -> pd.Series:
    """YoY cash change minus its own 4-quarter EWM."""
    base = _cashnequiv_yoy(cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_054_retearn_yoy_ewm_diff(retearn: pd.Series) -> pd.Series:
    """YoY retained-earnings change minus its own 4-quarter EWM."""
    base = _retearn_yoy(retearn)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_055_liab_to_assets_zscore_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in the 4Q z-score of the liabilities-to-assets ratio."""
    ratio = _safe_div(liabilities, assets)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    base = _safe_div(ratio - m, sd)
    return base - base.shift(_TD_QTR)


def bsd_drv2_056_debt_to_equity_yoy_diff(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the debt-to-equity ratio."""
    base = _debt_to_equity(debt, equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_057_nav_cumulative_decay_accel_yoy(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """YoY diff of (NAV - expanding_max(NAV)): persistent expanding-peak drawdown worsening."""
    nav  = _nav(assets, liabilities)
    peak = nav.expanding(min_periods=1).max()
    base = nav - peak
    return base - base.shift(_TD_YEAR)


def bsd_drv2_058_equity_drawdown_4q_2q_diff(equity: pd.Series) -> pd.Series:
    """2Q (126-day) change in the equity 4Q-peak drawdown."""
    base = _equity_drawdown_4q(equity)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_059_nav_drawdown_4q_2q_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """2Q change in the NAV 4Q-peak drawdown."""
    base = _nav_drawdown_4q(assets, liabilities)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_060_retearn_drawdown_4q_yoy_diff(retearn: pd.Series) -> pd.Series:
    """YoY change in the retained-earnings 4Q-peak drawdown."""
    base = _retearn_drawdown_4q(retearn)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_061_bs_health_4q_2q_diff(assets: pd.Series, liabilities: pd.Series,
                                        equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """2Q change in the 4-line 4Q BS health index."""
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_062_equity_yoy_2q_diff(equity: pd.Series) -> pd.Series:
    """2Q change in the YoY equity change."""
    base = _equity_yoy(equity)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_063_assets_yoy_yoy_diff(assets: pd.Series) -> pd.Series:
    """YoY change in the YoY assets change (second-order YoY assets trend)."""
    base = _assets_yoy(assets)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_064_nav_yoy_2q_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """2Q change in the YoY NAV change."""
    base = _nav_yoy(assets, liabilities)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_065_debt_yoy_2q_diff(debt: pd.Series) -> pd.Series:
    """2Q change in the YoY debt change."""
    base = _debt_yoy(debt)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_066_liab_yoy_yoy_diff(liabilities: pd.Series) -> pd.Series:
    """YoY change in the YoY liabilities change (second-order YoY liabilities trend)."""
    base = _liab_yoy(liabilities)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_067_invcap_yoy_2q_diff(invcap: pd.Series) -> pd.Series:
    """2Q change in the YoY invested-capital change."""
    base = _invcap_yoy(invcap)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_068_cashnequiv_drawdown_4q_yoy_diff(cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the cash 4Q-peak drawdown."""
    base = _cashnequiv_drawdown_4q(cashnequiv)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_069_retearn_qoq_ewm_diff(retearn: pd.Series) -> pd.Series:
    """QoQ retained-earnings change minus its own 4-quarter EWM."""
    base = _retearn_qoq(retearn)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_070_invcap_qoq_ewm_diff(invcap: pd.Series) -> pd.Series:
    """QoQ invested-capital change minus its own 4-quarter EWM."""
    base = _invcap_qoq(invcap)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_071_bs_health_8q_ewm_diff(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """8Q BS health index minus its own 4-quarter EWM."""
    base = _bs_health_8q(assets, liabilities, equity, cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def bsd_drv2_072_equity_drawdown_8q_yoy_diff(equity: pd.Series) -> pd.Series:
    """YoY change in the equity 8Q-peak drawdown."""
    base = _equity_drawdown_8q(equity)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_073_nav_drawdown_8q_yoy_diff(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """YoY change in the NAV 8Q-peak drawdown."""
    base = _nav_drawdown_8q(assets, liabilities)
    return base - base.shift(_TD_YEAR)


def bsd_drv2_074_liab_to_assets_2q_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """2Q change in the liabilities-to-assets ratio."""
    base = _liab_to_assets(liabilities, assets)
    return base - base.shift(2 * _TD_QTR)


def bsd_drv2_075_bs_health_4q_ewm_zscore(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    4-line 4Q BS health index minus its EWM, normalized by rolling std.
    Captures standardized acceleration of balance-sheet health deterioration.
    """
    base = _bs_health_4q(assets, liabilities, equity, cashnequiv)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    diff = base - ewm
    sd   = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff, sd)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

BALANCE_SHEET_DECAY_REGISTRY_2ND_DERIVATIVES = {
    "bsd_drv2_001_equity_yoy_qoq_diff":       {"inputs": ["equity"],                                              "func": bsd_drv2_001_equity_yoy_qoq_diff},
    "bsd_drv2_002_equity_yoy_yoy_diff":       {"inputs": ["equity"],                                              "func": bsd_drv2_002_equity_yoy_yoy_diff},
    "bsd_drv2_003_assets_yoy_qoq_diff":       {"inputs": ["assets"],                                              "func": bsd_drv2_003_assets_yoy_qoq_diff},
    "bsd_drv2_004_nav_yoy_qoq_diff":          {"inputs": ["assets", "liabilities"],                               "func": bsd_drv2_004_nav_yoy_qoq_diff},
    "bsd_drv2_005_nav_yoy_yoy_diff":          {"inputs": ["assets", "liabilities"],                               "func": bsd_drv2_005_nav_yoy_yoy_diff},
    "bsd_drv2_006_retearn_yoy_qoq_diff":      {"inputs": ["retearn"],                                             "func": bsd_drv2_006_retearn_yoy_qoq_diff},
    "bsd_drv2_007_debt_yoy_qoq_diff":         {"inputs": ["debt"],                                                "func": bsd_drv2_007_debt_yoy_qoq_diff},
    "bsd_drv2_008_liab_yoy_qoq_diff":         {"inputs": ["liabilities"],                                         "func": bsd_drv2_008_liab_yoy_qoq_diff},
    "bsd_drv2_009_bs_health_4q_qoq_diff":     {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv2_009_bs_health_4q_qoq_diff},
    "bsd_drv2_010_bs_health_4q_yoy_diff":     {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv2_010_bs_health_4q_yoy_diff},
    "bsd_drv2_011_equity_drawdown_4q_qoq_diff":{"inputs": ["equity"],                                             "func": bsd_drv2_011_equity_drawdown_4q_qoq_diff},
    "bsd_drv2_012_equity_drawdown_4q_yoy_diff":{"inputs": ["equity"],                                             "func": bsd_drv2_012_equity_drawdown_4q_yoy_diff},
    "bsd_drv2_013_nav_drawdown_4q_qoq_diff":  {"inputs": ["assets", "liabilities"],                               "func": bsd_drv2_013_nav_drawdown_4q_qoq_diff},
    "bsd_drv2_014_retearn_drawdown_4q_qoq_diff":{"inputs": ["retearn"],                                           "func": bsd_drv2_014_retearn_drawdown_4q_qoq_diff},
    "bsd_drv2_015_liab_to_assets_qoq_diff":   {"inputs": ["liabilities", "assets"],                               "func": bsd_drv2_015_liab_to_assets_qoq_diff},
    "bsd_drv2_016_liab_to_assets_yoy_diff":   {"inputs": ["liabilities", "assets"],                               "func": bsd_drv2_016_liab_to_assets_yoy_diff},
    "bsd_drv2_017_debt_to_equity_qoq_diff":   {"inputs": ["debt", "equity"],                                      "func": bsd_drv2_017_debt_to_equity_qoq_diff},
    "bsd_drv2_018_equity_qoq_pct_chg_of_qoq": {"inputs": ["equity"],                                             "func": bsd_drv2_018_equity_qoq_pct_chg_of_qoq},
    "bsd_drv2_019_equity_yoy_slope_4q":       {"inputs": ["equity"],                                              "func": bsd_drv2_019_equity_yoy_slope_4q},
    "bsd_drv2_020_nav_yoy_slope_4q":          {"inputs": ["assets", "liabilities"],                               "func": bsd_drv2_020_nav_yoy_slope_4q},
    "bsd_drv2_021_retearn_yoy_yoy_diff":      {"inputs": ["retearn"],                                             "func": bsd_drv2_021_retearn_yoy_yoy_diff},
    "bsd_drv2_022_debt_yoy_yoy_diff":         {"inputs": ["debt"],                                                "func": bsd_drv2_022_debt_yoy_yoy_diff},
    "bsd_drv2_023_equity_qoq_ewm_diff":       {"inputs": ["equity"],                                              "func": bsd_drv2_023_equity_qoq_ewm_diff},
    "bsd_drv2_024_bs_health_ewm_diff":        {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],       "func": bsd_drv2_024_bs_health_ewm_diff},
    "bsd_drv2_025_nav_cumulative_decay_accel": {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_025_nav_cumulative_decay_accel},
    "bsd_drv2_026_invcap_yoy_qoq_diff":        {"inputs": ["invcap"],                                             "func": bsd_drv2_026_invcap_yoy_qoq_diff},
    "bsd_drv2_027_cashnequiv_yoy_qoq_diff":    {"inputs": ["cashnequiv"],                                         "func": bsd_drv2_027_cashnequiv_yoy_qoq_diff},
    "bsd_drv2_028_workingcapital_yoy_qoq_diff":{"inputs": ["workingcapital"],                                     "func": bsd_drv2_028_workingcapital_yoy_qoq_diff},
    "bsd_drv2_029_assets_qoq_yoy_diff":        {"inputs": ["assets"],                                             "func": bsd_drv2_029_assets_qoq_yoy_diff},
    "bsd_drv2_030_debt_qoq_yoy_diff":          {"inputs": ["debt"],                                               "func": bsd_drv2_030_debt_qoq_yoy_diff},
    "bsd_drv2_031_retearn_qoq_yoy_diff":       {"inputs": ["retearn"],                                            "func": bsd_drv2_031_retearn_qoq_yoy_diff},
    "bsd_drv2_032_liab_qoq_yoy_diff":          {"inputs": ["liabilities"],                                        "func": bsd_drv2_032_liab_qoq_yoy_diff},
    "bsd_drv2_033_invcap_yoy_yoy_diff":        {"inputs": ["invcap"],                                             "func": bsd_drv2_033_invcap_yoy_yoy_diff},
    "bsd_drv2_034_cashnequiv_yoy_yoy_diff":    {"inputs": ["cashnequiv"],                                         "func": bsd_drv2_034_cashnequiv_yoy_yoy_diff},
    "bsd_drv2_035_workingcapital_yoy_yoy_diff":{"inputs": ["workingcapital"],                                     "func": bsd_drv2_035_workingcapital_yoy_yoy_diff},
    "bsd_drv2_036_equity_drawdown_8q_qoq_diff":{"inputs": ["equity"],                                             "func": bsd_drv2_036_equity_drawdown_8q_qoq_diff},
    "bsd_drv2_037_nav_drawdown_8q_qoq_diff":   {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_037_nav_drawdown_8q_qoq_diff},
    "bsd_drv2_038_cashnequiv_drawdown_4q_qoq_diff":{"inputs": ["cashnequiv"],                                     "func": bsd_drv2_038_cashnequiv_drawdown_4q_qoq_diff},
    "bsd_drv2_039_debt_to_assets_qoq_diff":    {"inputs": ["debt", "assets"],                                     "func": bsd_drv2_039_debt_to_assets_qoq_diff},
    "bsd_drv2_040_debt_to_assets_yoy_diff":    {"inputs": ["debt", "assets"],                                     "func": bsd_drv2_040_debt_to_assets_yoy_diff},
    "bsd_drv2_041_liab_to_equity_qoq_diff":    {"inputs": ["liabilities", "equity"],                              "func": bsd_drv2_041_liab_to_equity_qoq_diff},
    "bsd_drv2_042_liab_to_equity_yoy_diff":    {"inputs": ["liabilities", "equity"],                              "func": bsd_drv2_042_liab_to_equity_yoy_diff},
    "bsd_drv2_043_bs_health_8q_qoq_diff":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],     "func": bsd_drv2_043_bs_health_8q_qoq_diff},
    "bsd_drv2_044_bs_health_8q_yoy_diff":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],     "func": bsd_drv2_044_bs_health_8q_yoy_diff},
    "bsd_drv2_045_equity_yoy_slope_8q":        {"inputs": ["equity"],                                             "func": bsd_drv2_045_equity_yoy_slope_8q},
    "bsd_drv2_046_nav_yoy_slope_8q":           {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_046_nav_yoy_slope_8q},
    "bsd_drv2_047_debt_yoy_slope_4q":          {"inputs": ["debt"],                                               "func": bsd_drv2_047_debt_yoy_slope_4q},
    "bsd_drv2_048_liab_yoy_slope_4q":          {"inputs": ["liabilities"],                                        "func": bsd_drv2_048_liab_yoy_slope_4q},
    "bsd_drv2_049_retearn_yoy_slope_4q":       {"inputs": ["retearn"],                                            "func": bsd_drv2_049_retearn_yoy_slope_4q},
    "bsd_drv2_050_equity_qoq_ewm_diff_8q":     {"inputs": ["equity"],                                             "func": bsd_drv2_050_equity_qoq_ewm_diff_8q},
    "bsd_drv2_051_debt_qoq_ewm_diff":          {"inputs": ["debt"],                                               "func": bsd_drv2_051_debt_qoq_ewm_diff},
    "bsd_drv2_052_liab_yoy_ewm_diff":          {"inputs": ["liabilities"],                                        "func": bsd_drv2_052_liab_yoy_ewm_diff},
    "bsd_drv2_053_cashnequiv_yoy_ewm_diff":    {"inputs": ["cashnequiv"],                                         "func": bsd_drv2_053_cashnequiv_yoy_ewm_diff},
    "bsd_drv2_054_retearn_yoy_ewm_diff":       {"inputs": ["retearn"],                                            "func": bsd_drv2_054_retearn_yoy_ewm_diff},
    "bsd_drv2_055_liab_to_assets_zscore_qoq":  {"inputs": ["liabilities", "assets"],                              "func": bsd_drv2_055_liab_to_assets_zscore_qoq},
    "bsd_drv2_056_debt_to_equity_yoy_diff":    {"inputs": ["debt", "equity"],                                     "func": bsd_drv2_056_debt_to_equity_yoy_diff},
    "bsd_drv2_057_nav_cumulative_decay_accel_yoy":{"inputs": ["assets", "liabilities"],                           "func": bsd_drv2_057_nav_cumulative_decay_accel_yoy},
    "bsd_drv2_058_equity_drawdown_4q_2q_diff": {"inputs": ["equity"],                                             "func": bsd_drv2_058_equity_drawdown_4q_2q_diff},
    "bsd_drv2_059_nav_drawdown_4q_2q_diff":    {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_059_nav_drawdown_4q_2q_diff},
    "bsd_drv2_060_retearn_drawdown_4q_yoy_diff":{"inputs": ["retearn"],                                           "func": bsd_drv2_060_retearn_drawdown_4q_yoy_diff},
    "bsd_drv2_061_bs_health_4q_2q_diff":       {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],     "func": bsd_drv2_061_bs_health_4q_2q_diff},
    "bsd_drv2_062_equity_yoy_2q_diff":         {"inputs": ["equity"],                                             "func": bsd_drv2_062_equity_yoy_2q_diff},
    "bsd_drv2_063_assets_yoy_yoy_diff":        {"inputs": ["assets"],                                             "func": bsd_drv2_063_assets_yoy_yoy_diff},
    "bsd_drv2_064_nav_yoy_2q_diff":            {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_064_nav_yoy_2q_diff},
    "bsd_drv2_065_debt_yoy_2q_diff":           {"inputs": ["debt"],                                               "func": bsd_drv2_065_debt_yoy_2q_diff},
    "bsd_drv2_066_liab_yoy_yoy_diff":          {"inputs": ["liabilities"],                                        "func": bsd_drv2_066_liab_yoy_yoy_diff},
    "bsd_drv2_067_invcap_yoy_2q_diff":         {"inputs": ["invcap"],                                             "func": bsd_drv2_067_invcap_yoy_2q_diff},
    "bsd_drv2_068_cashnequiv_drawdown_4q_yoy_diff":{"inputs": ["cashnequiv"],                                     "func": bsd_drv2_068_cashnequiv_drawdown_4q_yoy_diff},
    "bsd_drv2_069_retearn_qoq_ewm_diff":       {"inputs": ["retearn"],                                            "func": bsd_drv2_069_retearn_qoq_ewm_diff},
    "bsd_drv2_070_invcap_qoq_ewm_diff":        {"inputs": ["invcap"],                                             "func": bsd_drv2_070_invcap_qoq_ewm_diff},
    "bsd_drv2_071_bs_health_8q_ewm_diff":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],     "func": bsd_drv2_071_bs_health_8q_ewm_diff},
    "bsd_drv2_072_equity_drawdown_8q_yoy_diff":{"inputs": ["equity"],                                             "func": bsd_drv2_072_equity_drawdown_8q_yoy_diff},
    "bsd_drv2_073_nav_drawdown_8q_yoy_diff":   {"inputs": ["assets", "liabilities"],                              "func": bsd_drv2_073_nav_drawdown_8q_yoy_diff},
    "bsd_drv2_074_liab_to_assets_2q_diff":     {"inputs": ["liabilities", "assets"],                              "func": bsd_drv2_074_liab_to_assets_2q_diff},
    "bsd_drv2_075_bs_health_4q_ewm_zscore":    {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],     "func": bsd_drv2_075_bs_health_4q_ewm_zscore},
}
