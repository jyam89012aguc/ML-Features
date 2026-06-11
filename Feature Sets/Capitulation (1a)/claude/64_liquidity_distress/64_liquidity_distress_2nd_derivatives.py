"""
64_liquidity_distress — 2nd-Derivative Features 001-025
Domain: rate of change of base liquidity-distress features — QoQ/YoY diffs,
        slopes, and percent changes of current ratio, quick ratio, cash ratio,
        drawdown series, z-scores, and composite signals.
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
# These inline relevant base computations so this file needs no cross-import.

def _current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(assetsc, liabilitiesc)


def _quick_ratio(assetsc: pd.Series, inventory: pd.Series,
                 liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(assetsc - inventory, liabilitiesc)


def _cash_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(cashnequiv, liabilitiesc)


def _cr_qoq(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_QTR)


def _cr_yoy(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_YEAR)


def _qr_qoq(assetsc: pd.Series, inventory: pd.Series,
             liabilitiesc: pd.Series) -> pd.Series:
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_QTR)


def _car_qoq(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_QTR)


def _cr_drawdown_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_YEAR)
    return cr - peak


def _cr_zscore_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _current_ratio(assetsc, liabilitiesc)
    m  = _rolling_mean(cr, _TD_YEAR)
    sd = _rolling_std(cr, _TD_YEAR)
    return _safe_div(cr - m, sd)


def _qr_zscore_4q(assetsc: pd.Series, inventory: pd.Series,
                  liabilitiesc: pd.Series) -> pd.Series:
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    m  = _rolling_mean(qr, _TD_YEAR)
    sd = _rolling_std(qr, _TD_YEAR)
    return _safe_div(qr - m, sd)


def _car_zscore_4q(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    m  = _rolling_mean(cr, _TD_YEAR)
    sd = _rolling_std(cr, _TD_YEAR)
    return _safe_div(cr - m, sd)


def _nca(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return assetsc - liabilitiesc


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def lqd_drv2_001_cr_qoq_change_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ current-ratio change (acceleration of CR decline)."""
    base = _cr_qoq(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_002_cr_yoy_change_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the YoY current-ratio change (how fast the YoY trend shifts)."""
    base = _cr_yoy(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_003_cr_qoq_pct_qoq_diff(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of current ratio."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    prior = cr.shift(_TD_QTR)
    base  = _safe_div_abs(cr - prior, prior)
    return base - base.shift(_TD_QTR)


def lqd_drv2_004_qr_qoq_change_qoq_diff(assetsc: pd.Series, inventory: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ quick-ratio change (acceleration of QR decline)."""
    base = _qr_qoq(assetsc, inventory, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_005_car_qoq_change_qoq_diff(cashnequiv: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ cash-ratio change (acceleration of cash-ratio decline)."""
    base = _car_qoq(cashnequiv, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_006_cr_zscore_4q_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of current ratio."""
    base = _cr_zscore_4q(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_007_cr_zscore_4q_yoy_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of current ratio."""
    base = _cr_zscore_4q(assetsc, liabilitiesc)
    return base - base.shift(_TD_YEAR)


def lqd_drv2_008_qr_zscore_4q_qoq_diff(assetsc: pd.Series, inventory: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of quick ratio."""
    base = _qr_zscore_4q(assetsc, inventory, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_009_car_zscore_4q_qoq_diff(cashnequiv: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of cash ratio."""
    base = _car_zscore_4q(cashnequiv, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_010_cr_drawdown_4q_qoq_diff(assetsc: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter-peak drawdown of current ratio."""
    base = _cr_drawdown_4q(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv2_011_cr_drawdown_4q_yoy_diff(assetsc: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter-peak drawdown of current ratio."""
    base = _cr_drawdown_4q(assetsc, liabilitiesc)
    return base - base.shift(_TD_YEAR)


def lqd_drv2_012_nca_qoq_diff(assetsc: pd.Series,
                                liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in net current assets (working capital)."""
    nca = _nca(assetsc, liabilitiesc)
    return nca - nca.shift(_TD_QTR)


def lqd_drv2_013_nca_yoy_diff(assetsc: pd.Series,
                                liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in net current assets."""
    nca = _nca(assetsc, liabilitiesc)
    return nca - nca.shift(_TD_YEAR)


def lqd_drv2_014_cashnequiv_qoq_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the QoQ cash change (cash-burn acceleration)."""
    base = cashnequiv - cashnequiv.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lqd_drv2_015_cr_qoq_slope_4q(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ current-ratio change series.
    Captures trend in QoQ current ratio momentum.
    """
    base = _cr_qoq(assetsc, liabilitiesc)

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


def lqd_drv2_016_cr_yoy_pct_yoy_diff(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the YoY percent-change of current ratio (2nd-order YoY)."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    prior = cr.shift(_TD_YEAR)
    base  = _safe_div_abs(cr - prior, prior)
    return base - base.shift(_TD_YEAR)


def lqd_drv2_017_qr_qoq_pct_chg(assetsc: pd.Series, inventory: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in the QoQ quick-ratio change series."""
    base = _qr_qoq(assetsc, inventory, liabilitiesc)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def lqd_drv2_018_cr_drawdown_pct_qoq_diff(assetsc: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the percent drawdown of current ratio from 4-quarter peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_YEAR)
    base = _safe_div_abs(cr - peak, peak)
    return base - base.shift(_TD_QTR)


def lqd_drv2_019_car_qoq_pct_chg(cashnequiv: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in the QoQ cash-ratio change series."""
    base = _car_qoq(cashnequiv, liabilitiesc)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def lqd_drv2_020_nca_drawdown_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the NCA drawdown from its 4-quarter peak."""
    nca  = _nca(assetsc, liabilitiesc)
    peak = _rolling_max(nca, _TD_YEAR)
    base = nca - peak
    return base - base.shift(_TD_QTR)


def lqd_drv2_021_cr_zscore_8q_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the 8-quarter z-score of current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    m  = _rolling_mean(cr, _TD_2Y)
    sd = _rolling_std(cr, _TD_2Y)
    base = _safe_div(cr - m, sd)
    return base - base.shift(_TD_QTR)


def lqd_drv2_022_cr_qoq_ewm_diff(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """
    Current QoQ current-ratio change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ decline is worse than recent trend.
    """
    base = _cr_qoq(assetsc, liabilitiesc)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def lqd_drv2_023_liabilitiesc_growth_acceleration(liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ current-liabilities growth rate (liability-growth acceleration)."""
    base = liabilitiesc - liabilitiesc.shift(_TD_QTR)
    return base - base.shift(_TD_QTR)


def lqd_drv2_024_cashnequiv_drawdown_qoq_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the cash-drawdown-from-4q-peak series."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    base = cashnequiv - peak
    return base - base.shift(_TD_QTR)


def lqd_drv2_025_composite_3ratio_zscore_qoq_diff(assetsc: pd.Series,
                                                    inventory: pd.Series,
                                                    cashnequiv: pd.Series,
                                                    liabilitiesc: pd.Series) -> pd.Series:
    """
    QoQ change in the 3-ratio composite distress z-score
    (equally weighted z-scores of current ratio, quick ratio, cash ratio).
    """
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    z_cr  = _safe_div(cr  - _rolling_mean(cr,  _TD_YEAR), _rolling_std(cr,  _TD_YEAR))
    z_qr  = _safe_div(qr  - _rolling_mean(qr,  _TD_YEAR), _rolling_std(qr,  _TD_YEAR))
    z_car = _safe_div(car - _rolling_mean(car, _TD_YEAR), _rolling_std(car, _TD_YEAR))
    composite = (z_cr + z_qr + z_car) / 3.0
    return composite - composite.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

LIQUIDITY_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "lqd_drv2_001_cr_qoq_change_qoq_diff":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_001_cr_qoq_change_qoq_diff},
    "lqd_drv2_002_cr_yoy_change_qoq_diff":          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_002_cr_yoy_change_qoq_diff},
    "lqd_drv2_003_cr_qoq_pct_qoq_diff":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_003_cr_qoq_pct_qoq_diff},
    "lqd_drv2_004_qr_qoq_change_qoq_diff":          {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv2_004_qr_qoq_change_qoq_diff},
    "lqd_drv2_005_car_qoq_change_qoq_diff":         {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv2_005_car_qoq_change_qoq_diff},
    "lqd_drv2_006_cr_zscore_4q_qoq_diff":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_006_cr_zscore_4q_qoq_diff},
    "lqd_drv2_007_cr_zscore_4q_yoy_diff":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_007_cr_zscore_4q_yoy_diff},
    "lqd_drv2_008_qr_zscore_4q_qoq_diff":           {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv2_008_qr_zscore_4q_qoq_diff},
    "lqd_drv2_009_car_zscore_4q_qoq_diff":          {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv2_009_car_zscore_4q_qoq_diff},
    "lqd_drv2_010_cr_drawdown_4q_qoq_diff":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_010_cr_drawdown_4q_qoq_diff},
    "lqd_drv2_011_cr_drawdown_4q_yoy_diff":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_011_cr_drawdown_4q_yoy_diff},
    "lqd_drv2_012_nca_qoq_diff":                    {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_012_nca_qoq_diff},
    "lqd_drv2_013_nca_yoy_diff":                    {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_013_nca_yoy_diff},
    "lqd_drv2_014_cashnequiv_qoq_diff_qoq":         {"inputs": ["cashnequiv"],                                           "func": lqd_drv2_014_cashnequiv_qoq_diff_qoq},
    "lqd_drv2_015_cr_qoq_slope_4q":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_015_cr_qoq_slope_4q},
    "lqd_drv2_016_cr_yoy_pct_yoy_diff":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_016_cr_yoy_pct_yoy_diff},
    "lqd_drv2_017_qr_qoq_pct_chg":                  {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv2_017_qr_qoq_pct_chg},
    "lqd_drv2_018_cr_drawdown_pct_qoq_diff":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_018_cr_drawdown_pct_qoq_diff},
    "lqd_drv2_019_car_qoq_pct_chg":                 {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv2_019_car_qoq_pct_chg},
    "lqd_drv2_020_nca_drawdown_qoq_diff":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_020_nca_drawdown_qoq_diff},
    "lqd_drv2_021_cr_zscore_8q_qoq_diff":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_021_cr_zscore_8q_qoq_diff},
    "lqd_drv2_022_cr_qoq_ewm_diff":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv2_022_cr_qoq_ewm_diff},
    "lqd_drv2_023_liabilitiesc_growth_acceleration": {"inputs": ["liabilitiesc"],                                        "func": lqd_drv2_023_liabilitiesc_growth_acceleration},
    "lqd_drv2_024_cashnequiv_drawdown_qoq_diff":    {"inputs": ["cashnequiv"],                                           "func": lqd_drv2_024_cashnequiv_drawdown_qoq_diff},
    "lqd_drv2_025_composite_3ratio_zscore_qoq_diff": {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],  "func": lqd_drv2_025_composite_3ratio_zscore_qoq_diff},
}
