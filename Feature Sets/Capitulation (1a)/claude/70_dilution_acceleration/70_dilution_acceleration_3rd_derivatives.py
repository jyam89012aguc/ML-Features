"""
70_dilution_acceleration — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative dilution-acceleration features
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

def _sharesbas_qoq_pct(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(_TD_QTR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def _sharesbas_qoq_change(sharesbas: pd.Series) -> pd.Series:
    return sharesbas - sharesbas.shift(_TD_QTR)


def _sharesbas_yoy_pct(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(_TD_YEAR)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def _shareswadil_qoq_pct(shareswadil: pd.Series) -> pd.Series:
    prior = shareswadil.shift(_TD_QTR)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


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


# 2nd-derivative helpers (QoQ diff of base)

def _drv2_sharesbas_qoq_pct_qoq(sharesbas: pd.Series) -> pd.Series:
    base = _sharesbas_qoq_pct(sharesbas)
    return base - base.shift(_TD_QTR)


def _drv2_sharesbas_yoy_pct_qoq(sharesbas: pd.Series) -> pd.Series:
    base = _sharesbas_yoy_pct(sharesbas)
    return base - base.shift(_TD_QTR)


def _drv2_ncfcommon_4q_sum_qoq(ncfcommon: pd.Series) -> pd.Series:
    base = _ncfcommon_4q_sum(ncfcommon)
    return base - base.shift(_TD_QTR)


def _drv2_sbcomp_to_equity_qoq(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    base = _sbcomp_to_equity(sbcomp, equity)
    return base - base.shift(_TD_QTR)


def _drv2_diluted_basic_gap_pct_qoq(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    base = _diluted_basic_gap_pct(shareswadil, shareswa)
    return base - base.shift(_TD_QTR)


def _drv2_shareswadil_qoq_pct_qoq(shareswadil: pd.Series) -> pd.Series:
    base = _shareswadil_qoq_pct(shareswadil)
    return base - base.shift(_TD_QTR)


def _drv2_sharesbas_zscore_4q_qoq(sharesbas: pd.Series) -> pd.Series:
    base = _sharesbas_zscore_4q(sharesbas)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def dla_drv3_001_sharesbas_qoq_pct_3rd_diff(sharesbas: pd.Series) -> pd.Series:
    """3rd QoQ difference of the share growth rate (jerk of dilution rate)."""
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_002_sharesbas_yoy_pct_3rd_diff(sharesbas: pd.Series) -> pd.Series:
    """3rd QoQ difference of the YoY share growth rate."""
    d2 = _drv2_sharesbas_yoy_pct_qoq(sharesbas)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_003_shareswadil_qoq_pct_3rd_diff(shareswadil: pd.Series) -> pd.Series:
    """3rd QoQ difference of the diluted-share QoQ growth rate."""
    d2 = _drv2_shareswadil_qoq_pct_qoq(shareswadil)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_004_diluted_basic_gap_pct_3rd_diff(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """3rd QoQ difference of the diluted-vs-basic gap percent."""
    d2 = _drv2_diluted_basic_gap_pct_qoq(shareswadil, shareswa)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_005_ncfcommon_4q_sum_3rd_diff(ncfcommon: pd.Series) -> pd.Series:
    """3rd QoQ difference of the TTM equity issuance sum."""
    d2 = _drv2_ncfcommon_4q_sum_qoq(ncfcommon)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_006_sbcomp_to_equity_3rd_diff(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """3rd QoQ difference of the SBC-to-equity ratio."""
    d2 = _drv2_sbcomp_to_equity_qoq(sbcomp, equity)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_007_sharesbas_zscore_4q_3rd_diff(sharesbas: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 4-quarter z-score of basic shares."""
    d2 = _drv2_sharesbas_zscore_4q_qoq(sharesbas)
    return d2 - d2.shift(_TD_QTR)


def dla_drv3_008_sharesbas_qoq_pct_3rd_yoy(sharesbas: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative (QoQ accel of QoQ share growth rate)."""
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    return d2 - d2.shift(_TD_YEAR)


def dla_drv3_009_ncfcommon_4q_sum_3rd_yoy(ncfcommon: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative of the TTM issuance sum."""
    d2 = _drv2_ncfcommon_4q_sum_qoq(ncfcommon)
    return d2 - d2.shift(_TD_YEAR)


def dla_drv3_010_sbcomp_to_equity_3rd_yoy(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative of the SBC-to-equity ratio."""
    d2 = _drv2_sbcomp_to_equity_qoq(sbcomp, equity)
    return d2 - d2.shift(_TD_YEAR)


def dla_drv3_011_sharesbas_qoq_pct_ewm_3rd(sharesbas: pd.Series) -> pd.Series:
    """
    QoQ change in (2nd-derivative QoQ share growth rate minus its EWM).
    3rd-order momentum deviation of dilution rate.
    """
    d2  = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base = d2 - ewm
    return base - base.shift(_TD_QTR)


def dla_drv3_012_diluted_basic_gap_3rd_yoy(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative of the diluted-vs-basic gap percent."""
    d2 = _drv2_diluted_basic_gap_pct_qoq(shareswadil, shareswa)
    return d2 - d2.shift(_TD_YEAR)


def dla_drv3_013_sharesbas_qoq_accel_slope(sharesbas: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the 2nd-derivative share-growth series.
    Captures the trend in acceleration — is the jerk positive (worsening pace)?
    """
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)

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

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def dla_drv3_014_ncfcommon_accel_slope(ncfcommon: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the 2nd-derivative TTM issuance series.
    """
    d2 = _drv2_ncfcommon_4q_sum_qoq(ncfcommon)

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

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def dla_drv3_015_sharesbas_qoq_pct_d2_zscore(sharesbas: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative QoQ share growth rate within trailing 4-quarter window."""
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def dla_drv3_016_ncfcommon_d2_zscore_4q(ncfcommon: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative TTM issuance sum within trailing 4-quarter window."""
    d2 = _drv2_ncfcommon_4q_sum_qoq(ncfcommon)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def dla_drv3_017_sbcomp_to_equity_d2_zscore(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative SBC-to-equity ratio within trailing 4-quarter window."""
    d2 = _drv2_sbcomp_to_equity_qoq(sbcomp, equity)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def dla_drv3_018_shareswadil_d2_zscore_4q(shareswadil: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative diluted-share QoQ growth rate within 4-quarter window."""
    d2 = _drv2_shareswadil_qoq_pct_qoq(shareswadil)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def dla_drv3_019_sharesbas_qoq_pct_d2_pct_rank(sharesbas: pd.Series) -> pd.Series:
    """Percentile rank of the 2nd-derivative QoQ share growth rate within 4-quarter window."""
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def dla_drv3_020_diluted_basic_gap_d2_zscore(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative diluted-vs-basic gap percent within 4-quarter window."""
    d2 = _drv2_diluted_basic_gap_pct_qoq(shareswadil, shareswa)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def dla_drv3_021_sharesbas_d2_expanding_zscore(sharesbas: pd.Series) -> pd.Series:
    """Expanding z-score of the 2nd-derivative QoQ share growth rate (all-history extremity)."""
    d2 = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    m  = d2.expanding(min_periods=2).mean()
    sd = d2.expanding(min_periods=2).std()
    return _safe_div(d2 - m, sd)


def dla_drv3_022_ncfcommon_d2_expanding_zscore(ncfcommon: pd.Series) -> pd.Series:
    """Expanding z-score of the 2nd-derivative TTM issuance sum (all-history extremity)."""
    d2 = _drv2_ncfcommon_4q_sum_qoq(ncfcommon)
    m  = d2.expanding(min_periods=2).mean()
    sd = d2.expanding(min_periods=2).std()
    return _safe_div(d2 - m, sd)


def dla_drv3_023_sharesbas_qoq_pct_d2_ewm_dev(sharesbas: pd.Series) -> pd.Series:
    """
    2nd-derivative QoQ share growth rate minus its own EWM (span=252).
    Measures whether the acceleration of dilution is itself accelerating above trend.
    """
    d2  = _drv2_sharesbas_qoq_pct_qoq(sharesbas)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def dla_drv3_024_sbcomp_to_equity_d2_pct_rank(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of the 2nd-derivative SBC-to-equity ratio within 4-quarter window."""
    d2 = _drv2_sbcomp_to_equity_qoq(sbcomp, equity)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def dla_drv3_025_dilution_jerk_composite(sharesbas: pd.Series, shareswadil: pd.Series,
                                         ncfcommon: pd.Series, sbcomp: pd.Series,
                                         equity: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative dilution jerk score (equal-weight z-scores):
    - 3rd diff of QoQ sharesbas growth rate
    - 3rd diff of diluted-vs-basic gap pct
    - 3rd diff of TTM ncfcommon
    - 3rd diff of SBC-to-equity
    All within 4-quarter trailing window.  Positive = dilution pressure is
    accelerating in its own acceleration (convex distress trajectory).
    """
    d3_bas = (_drv2_sharesbas_qoq_pct_qoq(sharesbas) - _drv2_sharesbas_qoq_pct_qoq(sharesbas).shift(_TD_QTR))
    d3_gap = (_drv2_diluted_basic_gap_pct_qoq(shareswadil, sharesbas) -
              _drv2_diluted_basic_gap_pct_qoq(shareswadil, sharesbas).shift(_TD_QTR))
    ncf4q  = _ncfcommon_4q_sum(ncfcommon)
    d2_ncf = ncf4q - ncf4q.shift(_TD_QTR)
    d3_ncf = d2_ncf - d2_ncf.shift(_TD_QTR)
    d3_sbc = (_drv2_sbcomp_to_equity_qoq(sbcomp, equity) -
              _drv2_sbcomp_to_equity_qoq(sbcomp, equity).shift(_TD_QTR))

    def _z(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    return (_z(d3_bas) + _z(d3_gap) + _z(d3_ncf) + _z(d3_sbc)) / 4.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

DILUTION_ACCELERATION_REGISTRY_3RD_DERIVATIVES = {
    "dla_drv3_001_sharesbas_qoq_pct_3rd_diff":       {"inputs": ["sharesbas"],                                               "func": dla_drv3_001_sharesbas_qoq_pct_3rd_diff},
    "dla_drv3_002_sharesbas_yoy_pct_3rd_diff":       {"inputs": ["sharesbas"],                                               "func": dla_drv3_002_sharesbas_yoy_pct_3rd_diff},
    "dla_drv3_003_shareswadil_qoq_pct_3rd_diff":     {"inputs": ["shareswadil"],                                             "func": dla_drv3_003_shareswadil_qoq_pct_3rd_diff},
    "dla_drv3_004_diluted_basic_gap_pct_3rd_diff":   {"inputs": ["shareswadil", "shareswa"],                                 "func": dla_drv3_004_diluted_basic_gap_pct_3rd_diff},
    "dla_drv3_005_ncfcommon_4q_sum_3rd_diff":        {"inputs": ["ncfcommon"],                                               "func": dla_drv3_005_ncfcommon_4q_sum_3rd_diff},
    "dla_drv3_006_sbcomp_to_equity_3rd_diff":        {"inputs": ["sbcomp", "equity"],                                        "func": dla_drv3_006_sbcomp_to_equity_3rd_diff},
    "dla_drv3_007_sharesbas_zscore_4q_3rd_diff":     {"inputs": ["sharesbas"],                                               "func": dla_drv3_007_sharesbas_zscore_4q_3rd_diff},
    "dla_drv3_008_sharesbas_qoq_pct_3rd_yoy":        {"inputs": ["sharesbas"],                                               "func": dla_drv3_008_sharesbas_qoq_pct_3rd_yoy},
    "dla_drv3_009_ncfcommon_4q_sum_3rd_yoy":         {"inputs": ["ncfcommon"],                                               "func": dla_drv3_009_ncfcommon_4q_sum_3rd_yoy},
    "dla_drv3_010_sbcomp_to_equity_3rd_yoy":         {"inputs": ["sbcomp", "equity"],                                        "func": dla_drv3_010_sbcomp_to_equity_3rd_yoy},
    "dla_drv3_011_sharesbas_qoq_pct_ewm_3rd":        {"inputs": ["sharesbas"],                                               "func": dla_drv3_011_sharesbas_qoq_pct_ewm_3rd},
    "dla_drv3_012_diluted_basic_gap_3rd_yoy":        {"inputs": ["shareswadil", "shareswa"],                                 "func": dla_drv3_012_diluted_basic_gap_3rd_yoy},
    "dla_drv3_013_sharesbas_qoq_accel_slope":        {"inputs": ["sharesbas"],                                               "func": dla_drv3_013_sharesbas_qoq_accel_slope},
    "dla_drv3_014_ncfcommon_accel_slope":            {"inputs": ["ncfcommon"],                                               "func": dla_drv3_014_ncfcommon_accel_slope},
    "dla_drv3_015_sharesbas_qoq_pct_d2_zscore":      {"inputs": ["sharesbas"],                                               "func": dla_drv3_015_sharesbas_qoq_pct_d2_zscore},
    "dla_drv3_016_ncfcommon_d2_zscore_4q":           {"inputs": ["ncfcommon"],                                               "func": dla_drv3_016_ncfcommon_d2_zscore_4q},
    "dla_drv3_017_sbcomp_to_equity_d2_zscore":       {"inputs": ["sbcomp", "equity"],                                        "func": dla_drv3_017_sbcomp_to_equity_d2_zscore},
    "dla_drv3_018_shareswadil_d2_zscore_4q":         {"inputs": ["shareswadil"],                                             "func": dla_drv3_018_shareswadil_d2_zscore_4q},
    "dla_drv3_019_sharesbas_qoq_pct_d2_pct_rank":    {"inputs": ["sharesbas"],                                               "func": dla_drv3_019_sharesbas_qoq_pct_d2_pct_rank},
    "dla_drv3_020_diluted_basic_gap_d2_zscore":      {"inputs": ["shareswadil", "shareswa"],                                 "func": dla_drv3_020_diluted_basic_gap_d2_zscore},
    "dla_drv3_021_sharesbas_d2_expanding_zscore":    {"inputs": ["sharesbas"],                                               "func": dla_drv3_021_sharesbas_d2_expanding_zscore},
    "dla_drv3_022_ncfcommon_d2_expanding_zscore":    {"inputs": ["ncfcommon"],                                               "func": dla_drv3_022_ncfcommon_d2_expanding_zscore},
    "dla_drv3_023_sharesbas_qoq_pct_d2_ewm_dev":     {"inputs": ["sharesbas"],                                               "func": dla_drv3_023_sharesbas_qoq_pct_d2_ewm_dev},
    "dla_drv3_024_sbcomp_to_equity_d2_pct_rank":     {"inputs": ["sbcomp", "equity"],                                        "func": dla_drv3_024_sbcomp_to_equity_d2_pct_rank},
    "dla_drv3_025_dilution_jerk_composite":          {"inputs": ["sharesbas", "shareswadil", "ncfcommon", "sbcomp", "equity"], "func": dla_drv3_025_dilution_jerk_composite},
}
