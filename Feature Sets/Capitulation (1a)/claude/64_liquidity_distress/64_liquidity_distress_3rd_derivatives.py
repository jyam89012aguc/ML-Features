"""
64_liquidity_distress — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative liquidity-distress features — diffs/slopes/
        pct-changes of acceleration series for current ratio, quick ratio, cash ratio,
        z-score trajectories, NCA dynamics, and composite signals.
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


# ── Base and 2nd-derivative helpers (self-contained recomputes) ───────────────

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


def _qr_qoq(assetsc: pd.Series, inventory: pd.Series,
             liabilitiesc: pd.Series) -> pd.Series:
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_QTR)


def _car_qoq(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_QTR)


def _cr_qoq_accel(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in CR QoQ change."""
    d1 = _cr_qoq(assetsc, liabilitiesc)
    return d1 - d1.shift(_TD_QTR)


def _qr_qoq_accel(assetsc: pd.Series, inventory: pd.Series,
                   liabilitiesc: pd.Series) -> pd.Series:
    d1 = _qr_qoq(assetsc, inventory, liabilitiesc)
    return d1 - d1.shift(_TD_QTR)


def _car_qoq_accel(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    d1 = _car_qoq(cashnequiv, liabilitiesc)
    return d1 - d1.shift(_TD_QTR)


def _cr_zscore_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr = _current_ratio(assetsc, liabilitiesc)
    m  = _rolling_mean(cr, _TD_YEAR)
    sd = _rolling_std(cr, _TD_YEAR)
    return _safe_div(cr - m, sd)


def _cr_zscore_qoq_diff(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in CR z-score."""
    z = _cr_zscore_4q(assetsc, liabilitiesc)
    return z - z.shift(_TD_QTR)


def _cr_drawdown_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_YEAR)
    return cr - peak


def _cr_drawdown_qoq_diff(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in CR drawdown."""
    d = _cr_drawdown_4q(assetsc, liabilitiesc)
    return d - d.shift(_TD_QTR)


def _nca(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return assetsc - liabilitiesc


def _nca_qoq(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    n = _nca(assetsc, liabilitiesc)
    return n - n.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def lqd_drv3_001_cr_qoq_accel_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the CR acceleration (2nd deriv) — 3rd order CR derivative."""
    base = _cr_qoq_accel(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_002_qr_qoq_accel_qoq_diff(assetsc: pd.Series, inventory: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QR acceleration (2nd deriv) — 3rd order QR derivative."""
    base = _qr_qoq_accel(assetsc, inventory, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_003_car_qoq_accel_qoq_diff(cashnequiv: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the cash-ratio acceleration — 3rd order cash-ratio derivative."""
    base = _car_qoq_accel(cashnequiv, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_004_cr_zscore_qoq_diff_qoq(assetsc: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of CR z-score (3rd order z-score dynamics)."""
    base = _cr_zscore_qoq_diff(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_005_cr_drawdown_qoq_diff_qoq(assetsc: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the CR-drawdown 2nd derivative — jerk of drawdown acceleration."""
    base = _cr_drawdown_qoq_diff(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_006_nca_qoq_accel(assetsc: pd.Series,
                                 liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ NCA change — NCA 2nd difference."""
    base = _nca_qoq(assetsc, liabilitiesc)
    return base - base.shift(_TD_QTR)


def lqd_drv3_007_cr_qoq_accel_yoy_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the CR QoQ-change acceleration (2nd deriv)."""
    base = _cr_qoq_accel(assetsc, liabilitiesc)
    return base - base.shift(_TD_YEAR)


def lqd_drv3_008_cr_qoq_slope_qoq_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling 4-quarter OLS slope of the CR QoQ change series.
    (slope of slope = curvature of CR QoQ trend.)
    """
    base_d1 = _cr_qoq(assetsc, liabilitiesc)

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

    slope_series = base_d1.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _slope, raw=True
    )
    return slope_series - slope_series.shift(_TD_QTR)


def lqd_drv3_009_cashnequiv_burn_accel(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the QoQ cash-burn acceleration (3rd order cash derivative)."""
    d1   = cashnequiv - cashnequiv.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def lqd_drv3_010_liabilitiesc_growth_jerk(liabilitiesc: pd.Series) -> pd.Series:
    """3rd difference of current liabilities over QoQ steps (jerk of liability growth)."""
    d1 = liabilitiesc - liabilitiesc.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def lqd_drv3_011_cr_qoq_accel_ewm_diff(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """
    CR-QoQ acceleration minus its EWM (span=252):
    measures whether the current acceleration is worse than its recent average.
    """
    accel = _cr_qoq_accel(assetsc, liabilitiesc)
    ewm   = accel.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return accel - ewm


def lqd_drv3_012_qr_qoq_accel_yoy_diff(assetsc: pd.Series, inventory: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the QR QoQ acceleration."""
    base = _qr_qoq_accel(assetsc, inventory, liabilitiesc)
    return base - base.shift(_TD_YEAR)


def lqd_drv3_013_car_qoq_accel_yoy_diff(cashnequiv: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in the cash-ratio QoQ acceleration."""
    base = _car_qoq_accel(cashnequiv, liabilitiesc)
    return base - base.shift(_TD_YEAR)


def lqd_drv3_014_cr_zscore_4q_accel(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """2nd QoQ difference of the 4-quarter z-score of current ratio."""
    z  = _cr_zscore_4q(assetsc, liabilitiesc)
    d1 = z - z.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_015_nca_drawdown_accel(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the NCA drawdown 2nd-deriv (NCA drawdown jerk)."""
    nca  = _nca(assetsc, liabilitiesc)
    peak = _rolling_max(nca, _TD_YEAR)
    dd   = nca - peak
    d1   = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_016_cr_qoq_accel_zscore_4q(assetsc: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """Z-score (within 4-quarter window) of the CR QoQ acceleration series."""
    accel = _cr_qoq_accel(assetsc, liabilitiesc)
    m     = _rolling_mean(accel, _TD_YEAR)
    sd    = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def lqd_drv3_017_qr_qoq_accel_zscore_4q(assetsc: pd.Series, inventory: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """Z-score (within 4-quarter window) of the QR QoQ acceleration series."""
    accel = _qr_qoq_accel(assetsc, inventory, liabilitiesc)
    m     = _rolling_mean(accel, _TD_YEAR)
    sd    = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def lqd_drv3_018_car_qoq_accel_zscore_4q(cashnequiv: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """Z-score (within 4-quarter window) of the cash-ratio QoQ acceleration series."""
    accel = _car_qoq_accel(cashnequiv, liabilitiesc)
    m     = _rolling_mean(accel, _TD_YEAR)
    sd    = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, sd)


def lqd_drv3_019_cr_qoq_diff_pct_of_level(assetsc: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """
    3rd-order measure: acceleration of CR QoQ change relative to the current CR level.
    = (CR_QoQ_accel) / |CR|, i.e., normalised jerk.
    """
    accel = _cr_qoq_accel(assetsc, liabilitiesc)
    cr    = _current_ratio(assetsc, liabilitiesc)
    return _safe_div_abs(accel, cr)


def lqd_drv3_020_cashnequiv_drawdown_accel(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the cash-drawdown-from-4q-peak 2nd deriv (drawdown jerk)."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    dd   = cashnequiv - peak
    d1   = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_021_cr_drawdown_pct_accel(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """2nd QoQ difference of the percent drawdown of current ratio from 4q peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_YEAR)
    pdd  = _safe_div_abs(cr - peak, peak)
    d1   = pdd - pdd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_022_cr_vs_4q_avg_accel(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """2nd QoQ difference of (current ratio - trailing 4q mean) — mean-deviation jerk."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    dev = cr - _rolling_mean(cr, _TD_YEAR)
    d1  = dev - dev.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_023_composite_3ratio_accel(assetsc: pd.Series, inventory: pd.Series,
                                         cashnequiv: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """
    2nd QoQ difference of the 3-ratio composite distress z-score — composite jerk.
    """
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    z1 = _safe_div(cr  - _rolling_mean(cr,  _TD_YEAR), _rolling_std(cr,  _TD_YEAR))
    z2 = _safe_div(qr  - _rolling_mean(qr,  _TD_YEAR), _rolling_std(qr,  _TD_YEAR))
    z3 = _safe_div(car - _rolling_mean(car, _TD_YEAR), _rolling_std(car, _TD_YEAR))
    comp = (z1 + z2 + z3) / 3.0
    d1   = comp - comp.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lqd_drv3_024_cr_qoq_accel_slope_4q(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the CR QoQ acceleration series.
    Captures the trend in CR second-derivative momentum.
    """
    accel = _cr_qoq_accel(assetsc, liabilitiesc)

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

    return accel.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _slope, raw=True
    )


def lqd_drv3_025_nca_qoq_accel_zscore_4q(assetsc: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """Z-score (4-quarter window) of the NCA QoQ acceleration (2nd difference of NCA)."""
    n   = _nca(assetsc, liabilitiesc)
    d1  = n - n.shift(_TD_QTR)
    d2  = d1 - d1.shift(_TD_QTR)
    m   = _rolling_mean(d2, _TD_YEAR)
    sd  = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

LIQUIDITY_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "lqd_drv3_001_cr_qoq_accel_qoq_diff":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_001_cr_qoq_accel_qoq_diff},
    "lqd_drv3_002_qr_qoq_accel_qoq_diff":        {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv3_002_qr_qoq_accel_qoq_diff},
    "lqd_drv3_003_car_qoq_accel_qoq_diff":       {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv3_003_car_qoq_accel_qoq_diff},
    "lqd_drv3_004_cr_zscore_qoq_diff_qoq":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_004_cr_zscore_qoq_diff_qoq},
    "lqd_drv3_005_cr_drawdown_qoq_diff_qoq":     {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_005_cr_drawdown_qoq_diff_qoq},
    "lqd_drv3_006_nca_qoq_accel":                {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_006_nca_qoq_accel},
    "lqd_drv3_007_cr_qoq_accel_yoy_diff":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_007_cr_qoq_accel_yoy_diff},
    "lqd_drv3_008_cr_qoq_slope_qoq_diff":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_008_cr_qoq_slope_qoq_diff},
    "lqd_drv3_009_cashnequiv_burn_accel":         {"inputs": ["cashnequiv"],                                           "func": lqd_drv3_009_cashnequiv_burn_accel},
    "lqd_drv3_010_liabilitiesc_growth_jerk":      {"inputs": ["liabilitiesc"],                                         "func": lqd_drv3_010_liabilitiesc_growth_jerk},
    "lqd_drv3_011_cr_qoq_accel_ewm_diff":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_011_cr_qoq_accel_ewm_diff},
    "lqd_drv3_012_qr_qoq_accel_yoy_diff":        {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv3_012_qr_qoq_accel_yoy_diff},
    "lqd_drv3_013_car_qoq_accel_yoy_diff":       {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv3_013_car_qoq_accel_yoy_diff},
    "lqd_drv3_014_cr_zscore_4q_accel":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_014_cr_zscore_4q_accel},
    "lqd_drv3_015_nca_drawdown_accel":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_015_nca_drawdown_accel},
    "lqd_drv3_016_cr_qoq_accel_zscore_4q":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_016_cr_qoq_accel_zscore_4q},
    "lqd_drv3_017_qr_qoq_accel_zscore_4q":       {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_drv3_017_qr_qoq_accel_zscore_4q},
    "lqd_drv3_018_car_qoq_accel_zscore_4q":      {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_drv3_018_car_qoq_accel_zscore_4q},
    "lqd_drv3_019_cr_qoq_diff_pct_of_level":     {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_019_cr_qoq_diff_pct_of_level},
    "lqd_drv3_020_cashnequiv_drawdown_accel":     {"inputs": ["cashnequiv"],                                           "func": lqd_drv3_020_cashnequiv_drawdown_accel},
    "lqd_drv3_021_cr_drawdown_pct_accel":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_021_cr_drawdown_pct_accel},
    "lqd_drv3_022_cr_vs_4q_avg_accel":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_022_cr_vs_4q_avg_accel},
    "lqd_drv3_023_composite_3ratio_accel":        {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_drv3_023_composite_3ratio_accel},
    "lqd_drv3_024_cr_qoq_accel_slope_4q":        {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_024_cr_qoq_accel_slope_4q},
    "lqd_drv3_025_nca_qoq_accel_zscore_4q":      {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_drv3_025_nca_qoq_accel_zscore_4q},
}
