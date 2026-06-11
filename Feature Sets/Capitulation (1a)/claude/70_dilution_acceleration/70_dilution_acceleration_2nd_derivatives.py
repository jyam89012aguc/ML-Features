"""
70_dilution_acceleration — 2nd-Derivative Features 001-025
Domain: rate of change of base dilution-acceleration features
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
# These inline the relevant base computations so this file needs no cross-import.

def _sharesbas_qoq_pct(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(_TD_QTR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def _sharesbas_yoy_pct(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(_TD_YEAR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def _sharesbas_qoq_change(sharesbas: pd.Series) -> pd.Series:
    return sharesbas - sharesbas.shift(_TD_QTR)


def _sharesbas_yoy_change(sharesbas: pd.Series) -> pd.Series:
    return sharesbas - sharesbas.shift(_TD_YEAR)


def _shareswadil_qoq_pct(shareswadil: pd.Series) -> pd.Series:
    prior = shareswadil.shift(_TD_QTR)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def _diluted_basic_gap(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return shareswadil - shareswa


def _diluted_basic_gap_pct(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    gap = shareswadil - shareswa
    return _safe_div(gap, shareswa.replace(0, np.nan))


def _ncfcommon_4q_sum(ncfcommon: pd.Series) -> pd.Series:
    return ncfcommon.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


def _sbcomp_to_equity(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    return _safe_div(sbcomp, equity.abs().replace(0, np.nan))


def _sharesbas_zscore_4q(sharesbas: pd.Series) -> pd.Series:
    m  = _rolling_mean(sharesbas, _TD_YEAR)
    sd = _rolling_std(sharesbas, _TD_YEAR)
    return _safe_div(sharesbas - m, sd)


def _sharesbas_cumulative_3y(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(3 * _TD_YEAR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def _issuance_flag_4q_sum(ncfcommon: pd.Series) -> pd.Series:
    flag = (ncfcommon > 0).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


def _equity_per_share(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(equity, sharesbas.replace(0, np.nan))


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def dla_drv2_001_sharesbas_qoq_pct_qoq_diff(sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the QoQ share growth rate (acceleration of QoQ dilution rate)."""
    base = _sharesbas_qoq_pct(sharesbas)
    return base - base.shift(_TD_QTR)


def dla_drv2_002_sharesbas_yoy_pct_qoq_diff(sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the YoY share growth rate (how fast the annual dilution rate is shifting)."""
    base = _sharesbas_yoy_pct(sharesbas)
    return base - base.shift(_TD_QTR)


def dla_drv2_003_sharesbas_qoq_change_yoy_diff(sharesbas: pd.Series) -> pd.Series:
    """YoY change in the QoQ share-count change (annual shift in quarterly issuance pace)."""
    base = _sharesbas_qoq_change(sharesbas)
    return base - base.shift(_TD_YEAR)


def dla_drv2_004_sharesbas_yoy_change_yoy_diff(sharesbas: pd.Series) -> pd.Series:
    """YoY change in the YoY share-count change (2nd-order annual dilution)."""
    base = _sharesbas_yoy_change(sharesbas)
    return base - base.shift(_TD_YEAR)


def dla_drv2_005_shareswadil_qoq_pct_qoq_diff(shareswadil: pd.Series) -> pd.Series:
    """QoQ change in the QoQ diluted-share growth rate."""
    base = _shareswadil_qoq_pct(shareswadil)
    return base - base.shift(_TD_QTR)


def dla_drv2_006_diluted_basic_gap_qoq_pct_diff(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """QoQ change in the diluted-vs-basic gap percent (acceleration of overhang rate)."""
    base = _diluted_basic_gap_pct(shareswadil, shareswa)
    return base - base.shift(_TD_QTR)


def dla_drv2_007_diluted_basic_gap_yoy_diff(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY change in the diluted-vs-basic absolute gap."""
    base = _diluted_basic_gap(shareswadil, shareswa)
    return base - base.shift(_TD_YEAR)


def dla_drv2_008_ncfcommon_4q_sum_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """QoQ change in the TTM equity issuance sum (acceleration of issuance pace)."""
    base = _ncfcommon_4q_sum(ncfcommon)
    return base - base.shift(_TD_QTR)


def dla_drv2_009_ncfcommon_4q_sum_yoy_diff(ncfcommon: pd.Series) -> pd.Series:
    """YoY change in the TTM equity issuance sum."""
    base = _ncfcommon_4q_sum(ncfcommon)
    return base - base.shift(_TD_YEAR)


def dla_drv2_010_sbcomp_to_equity_qoq_diff(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in the SBC-to-equity ratio (acceleration of SBC dilution burden)."""
    base = _sbcomp_to_equity(sbcomp, equity)
    return base - base.shift(_TD_QTR)


def dla_drv2_011_sbcomp_to_equity_yoy_diff(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the SBC-to-equity ratio."""
    base = _sbcomp_to_equity(sbcomp, equity)
    return base - base.shift(_TD_YEAR)


def dla_drv2_012_sharesbas_zscore_4q_qoq_diff(sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of basic shares."""
    base = _sharesbas_zscore_4q(sharesbas)
    return base - base.shift(_TD_QTR)


def dla_drv2_013_sharesbas_zscore_4q_yoy_diff(sharesbas: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of basic shares."""
    base = _sharesbas_zscore_4q(sharesbas)
    return base - base.shift(_TD_YEAR)


def dla_drv2_014_sharesbas_cumulative_3y_qoq_diff(sharesbas: pd.Series) -> pd.Series:
    """QoQ change in the 3-year cumulative dilution percent."""
    base = _sharesbas_cumulative_3y(sharesbas)
    return base - base.shift(_TD_QTR)


def dla_drv2_015_issuance_flag_4q_sum_qoq_diff(ncfcommon: pd.Series) -> pd.Series:
    """QoQ change in the rolling count of issuance quarters (acceleration of issuance frequency)."""
    base = _issuance_flag_4q_sum(ncfcommon)
    return base - base.shift(_TD_QTR)


def dla_drv2_016_equity_per_share_qoq_slope(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ equity-per-share change series.
    Captures the trend in per-share book-value dilution pace.
    """
    bvps = _equity_per_share(equity, sharesbas)
    base = bvps - bvps.shift(_TD_QTR)

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


def dla_drv2_017_sharesbas_qoq_pct_yoy_diff(sharesbas: pd.Series) -> pd.Series:
    """YoY change in the QoQ share growth rate (annual shift in quarterly dilution velocity)."""
    base = _sharesbas_qoq_pct(sharesbas)
    return base - base.shift(_TD_YEAR)


def dla_drv2_018_shareswadil_yoy_pct_qoq_diff(shareswadil: pd.Series) -> pd.Series:
    """QoQ change in the YoY diluted-share growth rate."""
    prior = shareswadil.shift(_TD_YEAR)
    base  = _safe_div(shareswadil - prior, prior.replace(0, np.nan))
    return base - base.shift(_TD_QTR)


def dla_drv2_019_ncfcommon_qoq_pct_diff(ncfcommon: pd.Series) -> pd.Series:
    """QoQ percent change in the QoQ ncfcommon change (2nd-order issuance momentum)."""
    base = ncfcommon - ncfcommon.shift(_TD_QTR)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def dla_drv2_020_diluted_basic_gap_pct_yoy_diff(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY change in the diluted-vs-basic gap percent (annual overhang acceleration)."""
    base = _diluted_basic_gap_pct(shareswadil, shareswa)
    return base - base.shift(_TD_YEAR)


def dla_drv2_021_sharesbas_qoq_pct_ewm_diff(sharesbas: pd.Series) -> pd.Series:
    """
    QoQ share growth pct minus its own 4-quarter EWM (span=252).
    Is this quarter's issuance rate above the smoothed trend of the QoQ rate?
    """
    base = _sharesbas_qoq_pct(sharesbas)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def dla_drv2_022_ncfcommon_4q_sum_pct_chg_qoq(ncfcommon: pd.Series) -> pd.Series:
    """QoQ percent change in the TTM issuance sum."""
    base  = _ncfcommon_4q_sum(ncfcommon)
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def dla_drv2_023_sbcomp_qoq_pct_diff(sbcomp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ SBC percent change (SBC momentum acceleration)."""
    prior = sbcomp.shift(_TD_QTR)
    base  = _safe_div_abs(sbcomp - prior, prior)
    return base - base.shift(_TD_QTR)


def dla_drv2_024_sharesbas_qoq_pct_zscore_qoq_diff(sharesbas: pd.Series) -> pd.Series:
    """
    QoQ change in the z-score of the QoQ share growth rate.
    Captures how extreme current-quarter dilution is becoming relative to the rolling window.
    """
    pct = _sharesbas_qoq_pct(sharesbas)
    m   = _rolling_mean(pct, _TD_YEAR)
    sd  = _rolling_std(pct, _TD_YEAR)
    base = _safe_div(pct - m, sd)
    return base - base.shift(_TD_QTR)


def dla_drv2_025_dilution_severity_qoq_accel(sharesbas: pd.Series, shareswadil: pd.Series,
                                              ncfcommon: pd.Series, sbcomp: pd.Series,
                                              equity: pd.Series) -> pd.Series:
    """
    QoQ change in a composite dilution severity score:
    equal-weight z-scores of (sharesbas QoQ pct, diluted-vs-basic gap pct,
    ncfcommon level, SBC-to-equity ratio) within 4-quarter window.
    The diff of the composite measures the acceleration of multi-factor dilution pressure.
    """
    bas_pct = _sharesbas_qoq_pct(sharesbas)
    gap_pct = _safe_div(shareswadil - sharesbas, sharesbas.replace(0, np.nan))
    sbc_eq  = _sbcomp_to_equity(sbcomp, equity)

    def _z(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    composite = (_z(bas_pct) + _z(gap_pct) + _z(ncfcommon) + _z(sbc_eq)) / 4.0
    return composite - composite.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

DILUTION_ACCELERATION_REGISTRY_2ND_DERIVATIVES = {
    "dla_drv2_001_sharesbas_qoq_pct_qoq_diff":         {"inputs": ["sharesbas"],                                          "func": dla_drv2_001_sharesbas_qoq_pct_qoq_diff},
    "dla_drv2_002_sharesbas_yoy_pct_qoq_diff":         {"inputs": ["sharesbas"],                                          "func": dla_drv2_002_sharesbas_yoy_pct_qoq_diff},
    "dla_drv2_003_sharesbas_qoq_change_yoy_diff":      {"inputs": ["sharesbas"],                                          "func": dla_drv2_003_sharesbas_qoq_change_yoy_diff},
    "dla_drv2_004_sharesbas_yoy_change_yoy_diff":      {"inputs": ["sharesbas"],                                          "func": dla_drv2_004_sharesbas_yoy_change_yoy_diff},
    "dla_drv2_005_shareswadil_qoq_pct_qoq_diff":       {"inputs": ["shareswadil"],                                        "func": dla_drv2_005_shareswadil_qoq_pct_qoq_diff},
    "dla_drv2_006_diluted_basic_gap_qoq_pct_diff":     {"inputs": ["shareswadil", "shareswa"],                            "func": dla_drv2_006_diluted_basic_gap_qoq_pct_diff},
    "dla_drv2_007_diluted_basic_gap_yoy_diff":         {"inputs": ["shareswadil", "shareswa"],                            "func": dla_drv2_007_diluted_basic_gap_yoy_diff},
    "dla_drv2_008_ncfcommon_4q_sum_qoq_diff":          {"inputs": ["ncfcommon"],                                          "func": dla_drv2_008_ncfcommon_4q_sum_qoq_diff},
    "dla_drv2_009_ncfcommon_4q_sum_yoy_diff":          {"inputs": ["ncfcommon"],                                          "func": dla_drv2_009_ncfcommon_4q_sum_yoy_diff},
    "dla_drv2_010_sbcomp_to_equity_qoq_diff":          {"inputs": ["sbcomp", "equity"],                                   "func": dla_drv2_010_sbcomp_to_equity_qoq_diff},
    "dla_drv2_011_sbcomp_to_equity_yoy_diff":          {"inputs": ["sbcomp", "equity"],                                   "func": dla_drv2_011_sbcomp_to_equity_yoy_diff},
    "dla_drv2_012_sharesbas_zscore_4q_qoq_diff":       {"inputs": ["sharesbas"],                                          "func": dla_drv2_012_sharesbas_zscore_4q_qoq_diff},
    "dla_drv2_013_sharesbas_zscore_4q_yoy_diff":       {"inputs": ["sharesbas"],                                          "func": dla_drv2_013_sharesbas_zscore_4q_yoy_diff},
    "dla_drv2_014_sharesbas_cumulative_3y_qoq_diff":   {"inputs": ["sharesbas"],                                          "func": dla_drv2_014_sharesbas_cumulative_3y_qoq_diff},
    "dla_drv2_015_issuance_flag_4q_sum_qoq_diff":      {"inputs": ["ncfcommon"],                                          "func": dla_drv2_015_issuance_flag_4q_sum_qoq_diff},
    "dla_drv2_016_equity_per_share_qoq_slope":         {"inputs": ["equity", "sharesbas"],                                "func": dla_drv2_016_equity_per_share_qoq_slope},
    "dla_drv2_017_sharesbas_qoq_pct_yoy_diff":         {"inputs": ["sharesbas"],                                          "func": dla_drv2_017_sharesbas_qoq_pct_yoy_diff},
    "dla_drv2_018_shareswadil_yoy_pct_qoq_diff":       {"inputs": ["shareswadil"],                                        "func": dla_drv2_018_shareswadil_yoy_pct_qoq_diff},
    "dla_drv2_019_ncfcommon_qoq_pct_diff":             {"inputs": ["ncfcommon"],                                          "func": dla_drv2_019_ncfcommon_qoq_pct_diff},
    "dla_drv2_020_diluted_basic_gap_pct_yoy_diff":     {"inputs": ["shareswadil", "shareswa"],                            "func": dla_drv2_020_diluted_basic_gap_pct_yoy_diff},
    "dla_drv2_021_sharesbas_qoq_pct_ewm_diff":         {"inputs": ["sharesbas"],                                          "func": dla_drv2_021_sharesbas_qoq_pct_ewm_diff},
    "dla_drv2_022_ncfcommon_4q_sum_pct_chg_qoq":       {"inputs": ["ncfcommon"],                                          "func": dla_drv2_022_ncfcommon_4q_sum_pct_chg_qoq},
    "dla_drv2_023_sbcomp_qoq_pct_diff":                {"inputs": ["sbcomp"],                                             "func": dla_drv2_023_sbcomp_qoq_pct_diff},
    "dla_drv2_024_sharesbas_qoq_pct_zscore_qoq_diff":  {"inputs": ["sharesbas"],                                          "func": dla_drv2_024_sharesbas_qoq_pct_zscore_qoq_diff},
    "dla_drv2_025_dilution_severity_qoq_accel":        {"inputs": ["sharesbas", "shareswadil", "ncfcommon", "sbcomp", "equity"], "func": dla_drv2_025_dilution_severity_qoq_accel},
}
