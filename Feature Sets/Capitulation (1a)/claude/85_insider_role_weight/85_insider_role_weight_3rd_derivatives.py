"""
85_insider_role_weight — 3rd-Derivative Features 001-075
Domain: rate-of-change of 2nd-derivative insider role-weighting features
Asset class: US equities | Sharadar SF2 insider transactions (daily event-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily Event-Aggregated Series Contract
-------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series
aggregated from Sharadar SF2 insider transaction filings.  The pipeline produces
one row per (ticker, date) summing all transactions filed on that date.
IMPORTANT: these are EVENT-DRIVEN series — most days are ZERO because no filing
occurred.  Do NOT forward-fill.  The 3rd-derivative series are EXTREMELY SPARSE on
a daily index — this is correct and expected for event-driven insider data.
All functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day cadence: 1 week = 5 days, 1 month = 21 days,
1 quarter = 63 days, 1 year = 252 days, 2 years = 504 days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WEEK  = 5
_TD_MONTH = 21
_TD_QTR   = 63
_TD_HALF  = 126
_TD_YEAR  = 252
_TD_2Y    = 504
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


# ── 2nd-derivative concept helpers (self-contained; no cross-file imports) ─────

def _rws_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """1Q role-weighted score."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )


def _rws_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """2nd-derivative: QoQ diff of 1Q role-weighted score."""
    base = _rws_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return base - base.shift(_TD_QTR)


def _sci_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """1Q seniority conviction index."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_QTR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def _sci_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """2nd-derivative: QoQ diff of 1Q SCI."""
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    return base - base.shift(_TD_QTR)


def _top_officer_share_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """1Q top-officer share."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def _top_officer_share_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """2nd-derivative: QoQ diff of 1Q top-officer share."""
    base = _top_officer_share_1q(ceo_buy_value, cfo_buy_value, insider_buy_value)
    return base - base.shift(_TD_QTR)


def _ceo_buy_1q(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _TD_QTR)


def _ceo_buy_1q_qoq_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ diff of 1Q CEO buy value."""
    base = _ceo_buy_1q(ceo_buy_value)
    return base - base.shift(_TD_QTR)


def _officer_to_dir_ratio_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(director_buy_value, _TD_QTR))


def _off_dir_ratio_1q_qoq_diff(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """2nd-derivative: QoQ diff of officer-to-director ratio."""
    base = _officer_to_dir_ratio_1q(officer_buy_value, director_buy_value)
    return base - base.shift(_TD_QTR)


def _officer_net_buy_1q(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)


def _officer_net_1q_qoq_diff(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ diff of officer net buy."""
    base = _officer_net_buy_1q(officer_buy_value, officer_sell_value)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ──────────────────────────────────────────

def irw_drv3_001_rws_1q_qoq_diff_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in 1Q RWS). Acceleration of the acceleration."""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_002_sci_1q_qoq_diff_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in 1Q SCI). Acceleration of SCI acceleration."""
    d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_003_top_officer_share_1q_qoq_diff_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in 1Q top-officer share)."""
    d2 = _top_officer_share_1q_qoq_diff(ceo_buy_value, cfo_buy_value, insider_buy_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_004_ceo_buy_1q_qoq_diff_qoq_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in 1Q CEO buy value)."""
    d2 = _ceo_buy_1q_qoq_diff(ceo_buy_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_005_off_dir_ratio_1q_qoq_diff_qoq_diff(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in officer-to-director ratio)."""
    d2 = _off_dir_ratio_1q_qoq_diff(officer_buy_value, director_buy_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_006_officer_net_1q_qoq_diff_qoq_diff(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in officer net buy)."""
    d2 = _officer_net_1q_qoq_diff(officer_buy_value, officer_sell_value)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_007_rws_1q_qoq_diff_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: YoY change in (QoQ change in 1Q RWS). Cross-horizon acceleration."""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_008_sci_1q_qoq_diff_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: YoY change in (QoQ change in 1Q SCI)."""
    d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_009_rws_1q_qoq_diff_slope(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """
    OLS slope of the (QoQ RWS diff) series over trailing 4Q.
    Trend-in-trend: is the RWS acceleration itself trending up or down?
    """
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def irw_drv3_010_sci_1q_qoq_diff_slope(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    OLS slope of the (QoQ SCI diff) series over trailing 4Q.
    Trend-in-trend for seniority conviction.
    """
    d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def irw_drv3_011_rws_1q_qoq_diff_pct_chg(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """QoQ percent change in (QoQ diff of 1Q RWS). Third-order percent acceleration."""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs().replace(0, np.nan))


def irw_drv3_012_sci_1q_qoq_diff_ewm_deviation(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """(QoQ SCI diff) minus its EWM (span=252). 3rd-order EWM deviation."""
    d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def irw_drv3_013_top_officer_share_qoq_diff_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: YoY change in (QoQ change in top-officer share)."""
    d2 = _top_officer_share_1q_qoq_diff(ceo_buy_value, cfo_buy_value, insider_buy_value)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_014_ceo_buy_1q_qoq_diff_yoy_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """3rd-order: YoY change in (QoQ change in 1Q CEO buy value)."""
    d2 = _ceo_buy_1q_qoq_diff(ceo_buy_value)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_015_officer_net_1q_qoq_diff_yoy_diff(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """3rd-order: YoY change in (QoQ change in officer net buy)."""
    d2 = _officer_net_1q_qoq_diff(officer_buy_value, officer_sell_value)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_016_rws_1q_qoq_diff_zscore_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of (QoQ RWS diff) within trailing 1 year. How extreme is the current acceleration?"""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_017_sci_1q_qoq_diff_zscore_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of (QoQ SCI diff) within trailing 1 year."""
    d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_018_rws_1q_qoq_diff_pct_rank_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Percentile rank of (QoQ RWS diff) within trailing 1 year."""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def irw_drv3_019_sci_1q_acceleration_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    3rd-order: QoQ diff of the SCI acceleration (2nd-order diff itself).
    = ((SCI_t - SCI_{t-1q}) - (SCI_{t-1q} - SCI_{t-2q})) - same_thing_1q_ago.
    """
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_020_rws_1q_acceleration_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ diff of the RWS acceleration. 4th difference but 3rd-derivative concept."""
    base = _rws_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_021_ceo_cfo_1q_qoq_diff_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """3rd-order: QoQ change in (QoQ change in 1Q CEO+CFO buy value)."""
    base = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_022_officer_to_dir_ratio_qoq_diff_zscore_1y(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of (QoQ officer-to-director ratio diff) within trailing 1 year."""
    d2 = _off_dir_ratio_1q_qoq_diff(officer_buy_value, director_buy_value).fillna(0.0)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_023_top_officer_share_qoq_diff_slope(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """OLS slope of (QoQ top-officer share diff) over trailing 4Q. Trend in momentum of share shift."""
    d2 = _top_officer_share_1q_qoq_diff(ceo_buy_value, cfo_buy_value, insider_buy_value).fillna(0.0)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def irw_drv3_024_rws_1q_qoq_diff_ewm_deviation(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """(QoQ RWS diff) minus its EWM (span=252). 3rd-order EWM deviation of RWS."""
    d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def irw_drv3_025_composite_3rd_order_signal(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Composite 3rd-order signal: equally weighted average of z-scored
    (a) QoQ RWS acceleration and (b) QoQ SCI acceleration.
    Positive = both seniority-weighted flow and conviction are inflecting upward.
    """
    rws_d2 = _rws_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    sci_d2 = _sci_1q_qoq_diff(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)

    def _z(s: pd.Series) -> pd.Series:
        m  = s.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
        sd = s.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
        return _safe_div(s - m, sd).fillna(0.0)

    rws_d3 = rws_d2 - rws_d2.shift(_TD_QTR)
    sci_d3 = sci_d2 - sci_d2.shift(_TD_QTR)
    return (_z(rws_d3) + _z(sci_d3)) / 2.0


# ── Additional helpers for drv3_026-075 ───────────────────────────────────────

def _rws_1y_qoq_diff(c, cf, o, d, t):
    base = (4.0*_rolling_sum(c,_TD_YEAR)+4.0*_rolling_sum(cf,_TD_YEAR)
            +3.0*_rolling_sum(o,_TD_YEAR)+2.0*_rolling_sum(d,_TD_YEAR)
            +1.0*_rolling_sum(t,_TD_YEAR))
    return base - base.shift(_TD_QTR)

def _rws_1y_yoy_diff(c, cf, o, d, t):
    base = (4.0*_rolling_sum(c,_TD_YEAR)+4.0*_rolling_sum(cf,_TD_YEAR)
            +3.0*_rolling_sum(o,_TD_YEAR)+2.0*_rolling_sum(d,_TD_YEAR)
            +1.0*_rolling_sum(t,_TD_YEAR))
    return base - base.shift(_TD_YEAR)

def _sci_1y(c, cf, o, d, t, ins):
    num = (1.0*_rolling_sum(c,_TD_YEAR)+0.9*_rolling_sum(cf,_TD_YEAR)
           +0.6*_rolling_sum(o,_TD_YEAR)+0.4*_rolling_sum(d,_TD_YEAR)
           +0.2*_rolling_sum(t,_TD_YEAR))
    return _safe_div(num, _rolling_sum(ins,_TD_YEAR))

def _sci_1y_qoq_diff(c, cf, o, d, t, ins):
    base = _sci_1y(c, cf, o, d, t, ins)
    return base - base.shift(_TD_QTR)

def _sci_1y_yoy_diff(c, cf, o, d, t, ins):
    base = _sci_1y(c, cf, o, d, t, ins)
    return base - base.shift(_TD_YEAR)

def _top_off_share_1y_qoq_diff(c, cf, ins):
    base = _safe_div(_rolling_sum(c+cf,_TD_YEAR), _rolling_sum(ins,_TD_YEAR))
    return base - base.shift(_TD_QTR)

def _off_dir_ratio_1y_qoq_diff(o, d):
    base = _safe_div(_rolling_sum(o,_TD_YEAR), _rolling_sum(d,_TD_YEAR))
    return base - base.shift(_TD_QTR)

def _ceo_buy_1y_qoq_diff(c):
    base = _rolling_sum(c, _TD_YEAR)
    return base - base.shift(_TD_QTR)

def _slope_fn3(arr):
    n = len(arr)
    if n < 2: return np.nan
    x = np.arange(n, dtype=float)
    xm, ym = x.mean(), arr.mean()
    denom = ((x-xm)**2).sum()
    if denom == 0: return np.nan
    return ((x-xm)*(arr-ym)).sum()/denom


# ── 3rd-derivative feature functions 026-075 ──────────────────────────────────

def irw_drv3_026_rws_1y_qoq_diff_qoq_diff(c, cf, o, d, t):
    """3rd-order: QoQ change in (QoQ change in 1Y RWS)."""
    d2 = _rws_1y_qoq_diff(c, cf, o, d, t)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_027_sci_1y_qoq_diff_qoq_diff(c, cf, o, d, t, ins):
    """3rd-order: QoQ change in (QoQ change in 1Y SCI)."""
    d2 = _sci_1y_qoq_diff(c, cf, o, d, t, ins)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_028_top_off_share_1y_qoq_diff_qoq_diff(c, cf, ins):
    """3rd-order: QoQ change in (QoQ change in 1Y top-officer share)."""
    d2 = _top_off_share_1y_qoq_diff(c, cf, ins)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_029_rws_1y_yoy_diff_qoq_diff(c, cf, o, d, t):
    """3rd-order: QoQ change in (YoY change in 1Y RWS). Cross-window 3rd derivative."""
    d2 = _rws_1y_yoy_diff(c, cf, o, d, t)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_030_sci_1y_yoy_diff_qoq_diff(c, cf, o, d, t, ins):
    """3rd-order: QoQ change in (YoY change in 1Y SCI)."""
    d2 = _sci_1y_yoy_diff(c, cf, o, d, t, ins)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_031_off_dir_ratio_1y_qoq_diff_qoq_diff(o, d):
    """3rd-order: QoQ change in (QoQ change in 1Y officer-to-director ratio)."""
    d2 = _off_dir_ratio_1y_qoq_diff(o, d)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_032_ceo_buy_1y_qoq_diff_qoq_diff(c):
    """3rd-order: QoQ change in (QoQ change in 1Y CEO buy value)."""
    d2 = _ceo_buy_1y_qoq_diff(c)
    return d2 - d2.shift(_TD_QTR)


def irw_drv3_033_rws_1q_qoq_diff_slope_half(c, cf, o, d, t):
    """OLS slope of (QoQ RWS diff) series over trailing half year."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    return d2.rolling(_TD_HALF, min_periods=max(2,_TD_HALF//4)).apply(_slope_fn3, raw=True)


def irw_drv3_034_sci_1q_qoq_diff_slope_half(c, cf, o, d, t, ins):
    """OLS slope of (QoQ SCI diff) series over trailing half year."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2.rolling(_TD_HALF, min_periods=max(2,_TD_HALF//4)).apply(_slope_fn3, raw=True)


def irw_drv3_035_top_off_share_qoq_diff_slope_half(c, cf, ins):
    """OLS slope of (QoQ top-officer share diff) over trailing half year."""
    d2 = _top_officer_share_1q_qoq_diff(c, cf, ins).fillna(0.0)
    return d2.rolling(_TD_HALF, min_periods=max(2,_TD_HALF//4)).apply(_slope_fn3, raw=True)


def irw_drv3_036_rws_1q_qoq_diff_zscore_2y(c, cf, o, d, t):
    """Z-score of (QoQ RWS diff) within trailing 2-year window."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    m  = d2.rolling(_TD_2Y, min_periods=max(1,_TD_2Y//4)).mean()
    sd = d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_037_sci_1q_qoq_diff_zscore_2y(c, cf, o, d, t, ins):
    """Z-score of (QoQ SCI diff) within trailing 2-year window."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    m  = d2.rolling(_TD_2Y, min_periods=max(1,_TD_2Y//4)).mean()
    sd = d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_038_rws_1q_qoq_diff_pct_rank_2y(c, cf, o, d, t):
    """Percentile rank of (QoQ RWS diff) within trailing 2-year window."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    return d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).rank(pct=True)


def irw_drv3_039_sci_1q_qoq_diff_pct_rank_1y(c, cf, o, d, t, ins):
    """Percentile rank of (QoQ SCI diff) within trailing 1-year window."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).rank(pct=True)


def irw_drv3_040_rws_1q_qoq_diff_ewm_deviation_half(c, cf, o, d, t):
    """(QoQ RWS diff) minus its EWM (span=126). 3rd-order half-year EWM deviation."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    return d2 - d2.ewm(span=_TD_HALF, min_periods=max(1,_TD_HALF//4)).mean()


def irw_drv3_041_sci_1q_qoq_diff_ewm_deviation_half(c, cf, o, d, t, ins):
    """(QoQ SCI diff) minus its EWM (span=126). 3rd-order half-year EWM deviation."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2 - d2.ewm(span=_TD_HALF, min_periods=max(1,_TD_HALF//4)).mean()


def irw_drv3_042_rws_1y_qoq_diff_yoy_diff(c, cf, o, d, t):
    """3rd-order: YoY change in (QoQ change in 1Y RWS)."""
    d2 = _rws_1y_qoq_diff(c, cf, o, d, t)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_043_sci_1y_qoq_diff_yoy_diff(c, cf, o, d, t, ins):
    """3rd-order: YoY change in (QoQ change in 1Y SCI)."""
    d2 = _sci_1y_qoq_diff(c, cf, o, d, t, ins)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_044_rws_1q_qoq_diff_pct_chg_yoy(c, cf, o, d, t):
    """YoY percent change in (QoQ RWS diff). 3rd-order percent acceleration."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    prior = d2.shift(_TD_YEAR)
    return _safe_div(d2 - prior, prior.abs().replace(0, np.nan))


def irw_drv3_045_sci_1q_qoq_diff_pct_chg_yoy(c, cf, o, d, t, ins):
    """YoY percent change in (QoQ SCI diff)."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    prior = d2.shift(_TD_YEAR)
    return _safe_div(d2 - prior, prior.abs().replace(0, np.nan))


def irw_drv3_046_rws_1y_qoq_diff_zscore_1y(c, cf, o, d, t):
    """Z-score of (QoQ 1Y-RWS diff) within trailing 1-year window."""
    d2 = _rws_1y_qoq_diff(c, cf, o, d, t)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_047_sci_1y_qoq_diff_zscore_1y(c, cf, o, d, t, ins):
    """Z-score of (QoQ 1Y-SCI diff) within trailing 1-year window."""
    d2 = _sci_1y_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_048_off_dir_ratio_1q_qoq_diff_slope(o, d):
    """OLS slope of (QoQ officer-to-director ratio diff) over trailing 1 year."""
    d2 = _off_dir_ratio_1q_qoq_diff(o, d).fillna(0.0)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True)


def irw_drv3_049_off_dir_ratio_1q_qoq_diff_pct_rank(o, d):
    """Percentile rank of (QoQ officer-to-director ratio diff) within 1 year."""
    d2 = _off_dir_ratio_1q_qoq_diff(o, d).fillna(0.0)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).rank(pct=True)


def irw_drv3_050_ceo_cfo_1q_qoq_diff_yoy_diff(c, cf):
    """3rd-order: YoY change in (QoQ change in 1Q CEO+CFO buy value)."""
    base = _rolling_sum(c+cf, _TD_QTR)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_YEAR)


def irw_drv3_051_rws_1q_qoq_diff_yoy_diff_zscore(c, cf, o, d, t):
    """Z-score of (YoY change in QoQ RWS diff) within trailing 1-year window."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    d3 = d2 - d2.shift(_TD_YEAR)
    m  = d3.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d3.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d3 - m, sd)


def irw_drv3_052_sci_1q_qoq_diff_yoy_diff_zscore(c, cf, o, d, t, ins):
    """Z-score of (YoY change in QoQ SCI diff) within trailing 1-year window."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    d3 = d2 - d2.shift(_TD_YEAR)
    m  = d3.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d3.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d3 - m, sd)


def irw_drv3_053_officer_net_1q_qoq_diff_yoy_diff(obv, osv):
    """3rd-order: YoY change in (QoQ change in officer net buy)."""
    d2 = _officer_net_1q_qoq_diff(obv, osv)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_054_top_off_share_qoq_diff_pct_rank(c, cf, ins):
    """Percentile rank of (QoQ top-officer share diff) within trailing 1 year."""
    d2 = _top_officer_share_1q_qoq_diff(c, cf, ins).fillna(0.0)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).rank(pct=True)


def irw_drv3_055_rws_1q_acceleration_yoy_diff(c, cf, o, d, t):
    """3rd-order: YoY change in (QoQ acceleration of 1Q RWS)."""
    base = _rws_1q(c, cf, o, d, t)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_056_sci_1q_acceleration_yoy_diff(c, cf, o, d, t, ins):
    """3rd-order: YoY change in (QoQ acceleration of 1Q SCI)."""
    base = _sci_1q(c, cf, o, d, t, ins)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_YEAR)


def irw_drv3_057_rws_1q_qoq_diff_slope_2y(c, cf, o, d, t):
    """OLS slope of (QoQ RWS diff) series over trailing 2 years."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    return d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).apply(_slope_fn3, raw=True)


def irw_drv3_058_sci_1q_qoq_diff_slope_2y(c, cf, o, d, t, ins):
    """OLS slope of (QoQ SCI diff) series over trailing 2 years."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).apply(_slope_fn3, raw=True)


def irw_drv3_059_ceo_buy_1q_qoq_diff_slope(c):
    """OLS slope of (QoQ CEO buy diff) series over trailing 1 year."""
    d2 = _ceo_buy_1q_qoq_diff(c)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True)


def irw_drv3_060_officer_net_1q_qoq_diff_slope(obv, osv):
    """OLS slope of (QoQ officer net buy diff) series over trailing 1 year."""
    d2 = _officer_net_1q_qoq_diff(obv, osv)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True)


def irw_drv3_061_rws_1q_qoq_diff_ewm_deviation_2y(c, cf, o, d, t):
    """(QoQ RWS diff) minus its EWM (span=504). 3rd-order 2Y EWM deviation."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    return d2 - d2.ewm(span=_TD_2Y, min_periods=max(1,_TD_2Y//4)).mean()


def irw_drv3_062_sci_1q_qoq_diff_ewm_deviation_2y(c, cf, o, d, t, ins):
    """(QoQ SCI diff) minus its EWM (span=504)."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2 - d2.ewm(span=_TD_2Y, min_periods=max(1,_TD_2Y//4)).mean()


def irw_drv3_063_top_off_share_qoq_diff_zscore_2y(c, cf, ins):
    """Z-score of (QoQ top-officer share diff) within trailing 2 years."""
    d2 = _top_officer_share_1q_qoq_diff(c, cf, ins).fillna(0.0)
    m  = d2.rolling(_TD_2Y, min_periods=max(1,_TD_2Y//4)).mean()
    sd = d2.rolling(_TD_2Y, min_periods=max(2,_TD_2Y//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_064_ceo_buy_qoq_diff_zscore_1y(c):
    """Z-score of (QoQ CEO buy diff) within trailing 1 year."""
    d2 = _ceo_buy_1q_qoq_diff(c)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_065_officer_net_qoq_diff_zscore_1y(obv, osv):
    """Z-score of (QoQ officer net buy diff) within trailing 1 year."""
    d2 = _officer_net_1q_qoq_diff(obv, osv).fillna(0.0)
    m  = d2.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
    sd = d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
    return _safe_div(d2 - m, sd)


def irw_drv3_066_rws_1y_qoq_diff_slope(c, cf, o, d, t):
    """OLS slope of (QoQ 1Y-RWS diff) over trailing 1 year."""
    d2 = _rws_1y_qoq_diff(c, cf, o, d, t)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True)


def irw_drv3_067_sci_1y_qoq_diff_slope(c, cf, o, d, t, ins):
    """OLS slope of (QoQ 1Y-SCI diff) over trailing 1 year."""
    d2 = _sci_1y_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    return d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True)


def irw_drv3_068_composite_3rd_deriv_yoy(c, cf, o, d, t, ins):
    """Composite 3rd-order: avg z-score of YoY RWS-QoQ-diff and YoY SCI-QoQ-diff."""
    rws_d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    sci_d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    rws_d3 = rws_d2 - rws_d2.shift(_TD_YEAR)
    sci_d3 = sci_d2 - sci_d2.shift(_TD_YEAR)
    def _z(s):
        m = s.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
        sd = s.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
        return _safe_div(s-m, sd).fillna(0.0)
    return (_z(rws_d3) + _z(sci_d3)) / 2.0


def irw_drv3_069_composite_3rd_deriv_1y_slope(c, cf, o, d, t, ins):
    """Composite 3rd-order slope: avg of OLS slopes of (QoQ RWS diff) and (QoQ SCI diff)."""
    rws_d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    sci_d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    rws_sl = rws_d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True).fillna(0.0)
    sci_sl = sci_d2.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).apply(_slope_fn3, raw=True).fillna(0.0)
    return (rws_sl + sci_sl) / 2.0


def irw_drv3_070_rws_1q_qoq_diff_sign_change(c, cf, o, d, t):
    """Binary: 1 if (QoQ RWS diff) changed sign vs prior quarter (inflection point)."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    sign_now  = (d2 > 0).astype(float)
    sign_prev = (d2.shift(_TD_QTR) > 0).astype(float)
    return (sign_now != sign_prev).astype(float)


def irw_drv3_071_sci_1q_qoq_diff_sign_change(c, cf, o, d, t, ins):
    """Binary: 1 if (QoQ SCI diff) changed sign vs prior quarter (inflection)."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    sign_now  = (d2 > 0).astype(float)
    sign_prev = (d2.shift(_TD_QTR) > 0).astype(float)
    return (sign_now != sign_prev).astype(float)


def irw_drv3_072_top_off_share_qoq_diff_sign_change(c, cf, ins):
    """Binary: 1 if (QoQ top-officer share diff) changed sign vs prior quarter."""
    d2 = _top_officer_share_1q_qoq_diff(c, cf, ins).fillna(0.0)
    sign_now  = (d2 > 0).astype(float)
    sign_prev = (d2.shift(_TD_QTR) > 0).astype(float)
    return (sign_now != sign_prev).astype(float)


def irw_drv3_073_rws_1q_qoq_diff_consecutive_pos(c, cf, o, d, t):
    """Count of consecutive quarters with positive QoQ RWS diff (streak in trailing 1Y)."""
    d2 = _rws_1q_qoq_diff(c, cf, o, d, t)
    pos = (d2 > 0).astype(float)
    return pos.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).sum()


def irw_drv3_074_sci_1q_qoq_diff_consecutive_pos(c, cf, o, d, t, ins):
    """Count of trailing 1Y days with positive QoQ SCI diff."""
    d2 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    pos = (d2 > 0).astype(float)
    return pos.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).sum()


def irw_drv3_075_composite_3rd_deriv_multi(c, cf, o, d, t, ins):
    """
    Multi-component 3rd-order composite: z-scored avg of
    (a) QoQ-of-QoQ RWS diff, (b) QoQ-of-QoQ SCI diff,
    (c) YoY-of-QoQ top-officer share diff.
    Captures acceleration across seniority dimensions.
    """
    rws_d3 = _rws_1q_qoq_diff(c, cf, o, d, t)
    rws_d3 = rws_d3 - rws_d3.shift(_TD_QTR)
    sci_d3 = _sci_1q_qoq_diff(c, cf, o, d, t, ins).fillna(0.0)
    sci_d3 = sci_d3 - sci_d3.shift(_TD_QTR)
    top_d2 = _top_officer_share_1q_qoq_diff(c, cf, ins).fillna(0.0)
    top_d3 = top_d2 - top_d2.shift(_TD_YEAR)
    def _z(s):
        m = s.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
        sd = s.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
        return _safe_div(s-m, sd).fillna(0.0)
    return (_z(rws_d3) + _z(sci_d3) + _z(top_d3)) / 3.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_ROLE_WEIGHT_REGISTRY_3RD_DERIVATIVES = {
    "irw_drv3_001_rws_1q_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_001_rws_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_002_sci_1q_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_002_sci_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_003_top_officer_share_1q_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_003_top_officer_share_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_004_ceo_buy_1q_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv3_004_ceo_buy_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_005_off_dir_ratio_1q_qoq_diff_qoq_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv3_005_off_dir_ratio_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_006_officer_net_1q_qoq_diff_qoq_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv3_006_officer_net_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_007_rws_1q_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_007_rws_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_008_sci_1q_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_008_sci_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_009_rws_1q_qoq_diff_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_009_rws_1q_qoq_diff_slope,
    },
    "irw_drv3_010_sci_1q_qoq_diff_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_010_sci_1q_qoq_diff_slope,
    },
    "irw_drv3_011_rws_1q_qoq_diff_pct_chg": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_011_rws_1q_qoq_diff_pct_chg,
    },
    "irw_drv3_012_sci_1q_qoq_diff_ewm_deviation": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_012_sci_1q_qoq_diff_ewm_deviation,
    },
    "irw_drv3_013_top_officer_share_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_013_top_officer_share_qoq_diff_yoy_diff,
    },
    "irw_drv3_014_ceo_buy_1q_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv3_014_ceo_buy_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_015_officer_net_1q_qoq_diff_yoy_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv3_015_officer_net_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_016_rws_1q_qoq_diff_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_016_rws_1q_qoq_diff_zscore_1y,
    },
    "irw_drv3_017_sci_1q_qoq_diff_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_017_sci_1q_qoq_diff_zscore_1y,
    },
    "irw_drv3_018_rws_1q_qoq_diff_pct_rank_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_018_rws_1q_qoq_diff_pct_rank_1y,
    },
    "irw_drv3_019_sci_1q_acceleration_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_019_sci_1q_acceleration_qoq_diff,
    },
    "irw_drv3_020_rws_1q_acceleration_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_020_rws_1q_acceleration_qoq_diff,
    },
    "irw_drv3_021_ceo_cfo_1q_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_drv3_021_ceo_cfo_1q_qoq_diff_qoq_diff,
    },
    "irw_drv3_022_officer_to_dir_ratio_qoq_diff_zscore_1y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv3_022_officer_to_dir_ratio_qoq_diff_zscore_1y,
    },
    "irw_drv3_023_top_officer_share_qoq_diff_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_023_top_officer_share_qoq_diff_slope,
    },
    "irw_drv3_024_rws_1q_qoq_diff_ewm_deviation": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_024_rws_1q_qoq_diff_ewm_deviation,
    },
    "irw_drv3_025_composite_3rd_order_signal": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_025_composite_3rd_order_signal,
    },
    "irw_drv3_026_rws_1y_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_026_rws_1y_qoq_diff_qoq_diff,
    },
    "irw_drv3_027_sci_1y_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_027_sci_1y_qoq_diff_qoq_diff,
    },
    "irw_drv3_028_top_off_share_1y_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_028_top_off_share_1y_qoq_diff_qoq_diff,
    },
    "irw_drv3_029_rws_1y_yoy_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_029_rws_1y_yoy_diff_qoq_diff,
    },
    "irw_drv3_030_sci_1y_yoy_diff_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_030_sci_1y_yoy_diff_qoq_diff,
    },
    "irw_drv3_031_off_dir_ratio_1y_qoq_diff_qoq_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv3_031_off_dir_ratio_1y_qoq_diff_qoq_diff,
    },
    "irw_drv3_032_ceo_buy_1y_qoq_diff_qoq_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv3_032_ceo_buy_1y_qoq_diff_qoq_diff,
    },
    "irw_drv3_033_rws_1q_qoq_diff_slope_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_033_rws_1q_qoq_diff_slope_half,
    },
    "irw_drv3_034_sci_1q_qoq_diff_slope_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_034_sci_1q_qoq_diff_slope_half,
    },
    "irw_drv3_035_top_off_share_qoq_diff_slope_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_035_top_off_share_qoq_diff_slope_half,
    },
    "irw_drv3_036_rws_1q_qoq_diff_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_036_rws_1q_qoq_diff_zscore_2y,
    },
    "irw_drv3_037_sci_1q_qoq_diff_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_037_sci_1q_qoq_diff_zscore_2y,
    },
    "irw_drv3_038_rws_1q_qoq_diff_pct_rank_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_038_rws_1q_qoq_diff_pct_rank_2y,
    },
    "irw_drv3_039_sci_1q_qoq_diff_pct_rank_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_039_sci_1q_qoq_diff_pct_rank_1y,
    },
    "irw_drv3_040_rws_1q_qoq_diff_ewm_deviation_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_040_rws_1q_qoq_diff_ewm_deviation_half,
    },
    "irw_drv3_041_sci_1q_qoq_diff_ewm_deviation_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_041_sci_1q_qoq_diff_ewm_deviation_half,
    },
    "irw_drv3_042_rws_1y_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_042_rws_1y_qoq_diff_yoy_diff,
    },
    "irw_drv3_043_sci_1y_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_043_sci_1y_qoq_diff_yoy_diff,
    },
    "irw_drv3_044_rws_1q_qoq_diff_pct_chg_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_044_rws_1q_qoq_diff_pct_chg_yoy,
    },
    "irw_drv3_045_sci_1q_qoq_diff_pct_chg_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_045_sci_1q_qoq_diff_pct_chg_yoy,
    },
    "irw_drv3_046_rws_1y_qoq_diff_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_046_rws_1y_qoq_diff_zscore_1y,
    },
    "irw_drv3_047_sci_1y_qoq_diff_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_047_sci_1y_qoq_diff_zscore_1y,
    },
    "irw_drv3_048_off_dir_ratio_1q_qoq_diff_slope": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv3_048_off_dir_ratio_1q_qoq_diff_slope,
    },
    "irw_drv3_049_off_dir_ratio_1q_qoq_diff_pct_rank": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv3_049_off_dir_ratio_1q_qoq_diff_pct_rank,
    },
    "irw_drv3_050_ceo_cfo_1q_qoq_diff_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_drv3_050_ceo_cfo_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_051_rws_1q_qoq_diff_yoy_diff_zscore": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_051_rws_1q_qoq_diff_yoy_diff_zscore,
    },
    "irw_drv3_052_sci_1q_qoq_diff_yoy_diff_zscore": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_052_sci_1q_qoq_diff_yoy_diff_zscore,
    },
    "irw_drv3_053_officer_net_1q_qoq_diff_yoy_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv3_053_officer_net_1q_qoq_diff_yoy_diff,
    },
    "irw_drv3_054_top_off_share_qoq_diff_pct_rank": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_054_top_off_share_qoq_diff_pct_rank,
    },
    "irw_drv3_055_rws_1q_acceleration_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_055_rws_1q_acceleration_yoy_diff,
    },
    "irw_drv3_056_sci_1q_acceleration_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_056_sci_1q_acceleration_yoy_diff,
    },
    "irw_drv3_057_rws_1q_qoq_diff_slope_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_057_rws_1q_qoq_diff_slope_2y,
    },
    "irw_drv3_058_sci_1q_qoq_diff_slope_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_058_sci_1q_qoq_diff_slope_2y,
    },
    "irw_drv3_059_ceo_buy_1q_qoq_diff_slope": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv3_059_ceo_buy_1q_qoq_diff_slope,
    },
    "irw_drv3_060_officer_net_1q_qoq_diff_slope": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv3_060_officer_net_1q_qoq_diff_slope,
    },
    "irw_drv3_061_rws_1q_qoq_diff_ewm_deviation_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_061_rws_1q_qoq_diff_ewm_deviation_2y,
    },
    "irw_drv3_062_sci_1q_qoq_diff_ewm_deviation_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_062_sci_1q_qoq_diff_ewm_deviation_2y,
    },
    "irw_drv3_063_top_off_share_qoq_diff_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_063_top_off_share_qoq_diff_zscore_2y,
    },
    "irw_drv3_064_ceo_buy_qoq_diff_zscore_1y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv3_064_ceo_buy_qoq_diff_zscore_1y,
    },
    "irw_drv3_065_officer_net_qoq_diff_zscore_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv3_065_officer_net_qoq_diff_zscore_1y,
    },
    "irw_drv3_066_rws_1y_qoq_diff_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_066_rws_1y_qoq_diff_slope,
    },
    "irw_drv3_067_sci_1y_qoq_diff_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_067_sci_1y_qoq_diff_slope,
    },
    "irw_drv3_068_composite_3rd_deriv_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_068_composite_3rd_deriv_yoy,
    },
    "irw_drv3_069_composite_3rd_deriv_1y_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_069_composite_3rd_deriv_1y_slope,
    },
    "irw_drv3_070_rws_1q_qoq_diff_sign_change": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_070_rws_1q_qoq_diff_sign_change,
    },
    "irw_drv3_071_sci_1q_qoq_diff_sign_change": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_071_sci_1q_qoq_diff_sign_change,
    },
    "irw_drv3_072_top_off_share_qoq_diff_sign_change": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv3_072_top_off_share_qoq_diff_sign_change,
    },
    "irw_drv3_073_rws_1q_qoq_diff_consecutive_pos": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv3_073_rws_1q_qoq_diff_consecutive_pos,
    },
    "irw_drv3_074_sci_1q_qoq_diff_consecutive_pos": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_074_sci_1q_qoq_diff_consecutive_pos,
    },
    "irw_drv3_075_composite_3rd_deriv_multi": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv3_075_composite_3rd_deriv_multi,
    },
}
