"""
85_insider_role_weight — 2nd-Derivative Features 001-075
Domain: rate-of-change of base insider role-weighting features
Asset class: US equities | Sharadar SF2 insider transactions (daily event-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily Event-Aggregated Series Contract
-------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series
aggregated from Sharadar SF2 insider transaction filings.  The pipeline produces
one row per (ticker, date) summing all transactions filed on that date.
IMPORTANT: these are EVENT-DRIVEN series — most days are ZERO because no filing
occurred.  Do NOT forward-fill.  The 2nd-derivative series are VERY SPARSE on a
daily index because the underlying insider series is event-driven — this is
correct and expected.  Features aggregate and differentiate using rolling SUMS
and .shift() on backward-looking windows only.
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


# ── Base concept helpers (self-contained; no cross-file imports) ───────────────

def _role_weighted_score_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )


def _top_officer_share_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def _officer_share_1q(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(insider_buy_value, _TD_QTR))


def _sci_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_QTR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def _officer_to_director_ratio_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(director_buy_value, _TD_QTR))


def _ceo_buy_1q(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _TD_QTR)


def _cfo_buy_1q(cfo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(cfo_buy_value, _TD_QTR)


def _officer_net_buy_1q(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)


def _director_net_buy_1q(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_value - director_sell_value, _TD_QTR)


# ── 2nd-derivative feature functions ──────────────────────────────────────────

def irw_drv2_001_role_weighted_score_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q role-weighted buy score (acceleration of seniority-weighted flow)."""
    base = _role_weighted_score_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_002_top_officer_share_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q top-officer (CEO+CFO) value share."""
    base = _top_officer_share_1q(ceo_buy_value, cfo_buy_value, insider_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_003_officer_share_1q_qoq_diff(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q officer value share."""
    base = _officer_share_1q(officer_buy_value, insider_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_004_sci_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q seniority conviction index."""
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_005_officer_to_director_ratio_1q_qoq_diff(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q officer-to-director buy value ratio."""
    base = _officer_to_director_ratio_1q(officer_buy_value, director_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_006_ceo_buy_1q_qoq_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """QoQ change in the rolling 1Q CEO buy value."""
    base = _ceo_buy_1q(ceo_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_007_cfo_buy_1q_qoq_diff(cfo_buy_value: pd.Series) -> pd.Series:
    """QoQ change in the rolling 1Q CFO buy value."""
    base = _cfo_buy_1q(cfo_buy_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_008_officer_net_buy_1q_qoq_diff(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q officer net buy value."""
    base = _officer_net_buy_1q(officer_buy_value, officer_sell_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_009_director_net_buy_1q_qoq_diff(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """QoQ change in the 1Q director net buy value."""
    base = _director_net_buy_1q(director_buy_value, director_sell_value)
    return base - base.shift(_TD_QTR)


def irw_drv2_010_role_weighted_score_1q_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q role-weighted buy score."""
    base = _role_weighted_score_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_011_sci_1q_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q seniority conviction index."""
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_012_top_officer_share_1q_yoy_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q top-officer value share."""
    base = _top_officer_share_1q(ceo_buy_value, cfo_buy_value, insider_buy_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_013_ceo_buy_1q_slope(ceo_buy_value: pd.Series) -> pd.Series:
    """
    Rolling 4Q (252-day) OLS slope of the 1Q CEO buy value series.
    Captures trend in CEO buying activity.
    """
    base = _ceo_buy_1q(ceo_buy_value)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def irw_drv2_014_sci_1q_slope(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Rolling 4Q OLS slope of the 1Q seniority conviction index series.
    Captures trend in seniority of buying.
    """
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def irw_drv2_015_role_weighted_score_1q_pct_chg_qoq(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """QoQ percent change in the 1Q role-weighted buy score."""
    base = _role_weighted_score_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_016_officer_to_director_ratio_1q_yoy_diff(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q officer-to-director buy value ratio."""
    base = _officer_to_director_ratio_1q(officer_buy_value, director_buy_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_017_ceo_buy_1q_pct_chg_qoq(ceo_buy_value: pd.Series) -> pd.Series:
    """QoQ percent change in rolling 1Q CEO buy value."""
    base = _ceo_buy_1q(ceo_buy_value)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_018_officer_share_1q_yoy_diff(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q officer value share."""
    base = _officer_share_1q(officer_buy_value, insider_buy_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_019_sci_1q_ewm_deviation(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    1Q SCI minus its EWM (span=252): whether current seniority conviction
    is above or below its own rolling trend.
    """
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value).fillna(0.0)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def irw_drv2_020_top_officer_share_1q_pct_chg_qoq(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """QoQ percent change in the 1Q top-officer value share."""
    base = _top_officer_share_1q(ceo_buy_value, cfo_buy_value, insider_buy_value)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_021_officer_net_buy_1q_yoy_diff(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q officer net buy value."""
    base = _officer_net_buy_1q(officer_buy_value, officer_sell_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_022_director_net_buy_1q_yoy_diff(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """YoY change in the 1Q director net buy value."""
    base = _director_net_buy_1q(director_buy_value, director_sell_value)
    return base - base.shift(_TD_YEAR)


def irw_drv2_023_role_weighted_score_1q_acceleration(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """
    Second difference of 1Q role-weighted buy score over 1Q steps:
    (score_now - score_1q_ago) - (score_1q_ago - score_2q_ago).
    Positive = accelerating seniority-weighted buying.
    """
    base = _role_weighted_score_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2


def irw_drv2_024_sci_1q_acceleration(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Second difference of 1Q seniority conviction index over 1Q steps.
    Positive = SCI accelerating toward higher seniority.
    """
    base = _sci_1q(ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value, insider_buy_value)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2


def irw_drv2_025_ceo_cfo_combined_1q_qoq_diff(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """QoQ change in the combined CEO+CFO 1Q buy value."""
    base = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    return base - base.shift(_TD_QTR)


# ── Additional base helpers for drv2_026-075 ──────────────────────────────────

def _rws_1y(c, cf, o, d, t):
    return (4.0*_rolling_sum(c,_TD_YEAR)+4.0*_rolling_sum(cf,_TD_YEAR)
            +3.0*_rolling_sum(o,_TD_YEAR)+2.0*_rolling_sum(d,_TD_YEAR)
            +1.0*_rolling_sum(t,_TD_YEAR))

def _rws_half(c, cf, o, d, t):
    return (4.0*_rolling_sum(c,_TD_HALF)+4.0*_rolling_sum(cf,_TD_HALF)
            +3.0*_rolling_sum(o,_TD_HALF)+2.0*_rolling_sum(d,_TD_HALF)
            +1.0*_rolling_sum(t,_TD_HALF))

def _sci_1y(c, cf, o, d, t, ins):
    num = (1.0*_rolling_sum(c,_TD_YEAR)+0.9*_rolling_sum(cf,_TD_YEAR)
           +0.6*_rolling_sum(o,_TD_YEAR)+0.4*_rolling_sum(d,_TD_YEAR)
           +0.2*_rolling_sum(t,_TD_YEAR))
    return _safe_div(num, _rolling_sum(ins,_TD_YEAR))

def _sci_half(c, cf, o, d, t, ins):
    num = (1.0*_rolling_sum(c,_TD_HALF)+0.9*_rolling_sum(cf,_TD_HALF)
           +0.6*_rolling_sum(o,_TD_HALF)+0.4*_rolling_sum(d,_TD_HALF)
           +0.2*_rolling_sum(t,_TD_HALF))
    return _safe_div(num, _rolling_sum(ins,_TD_HALF))

def _top_off_share_1y(c, cf, ins):
    return _safe_div(_rolling_sum(c+cf,_TD_YEAR), _rolling_sum(ins,_TD_YEAR))

def _top_off_share_half(c, cf, ins):
    return _safe_div(_rolling_sum(c+cf,_TD_HALF), _rolling_sum(ins,_TD_HALF))

def _off_share_1y(o, ins):
    return _safe_div(_rolling_sum(o,_TD_YEAR), _rolling_sum(ins,_TD_YEAR))

def _off_dir_ratio_1y(o, d):
    return _safe_div(_rolling_sum(o,_TD_YEAR), _rolling_sum(d,_TD_YEAR))

def _off_dir_ratio_half(o, d):
    return _safe_div(_rolling_sum(o,_TD_HALF), _rolling_sum(d,_TD_HALF))

def _off_net_1y(obv, osv):
    return _rolling_sum(obv-osv, _TD_YEAR)

def _dir_net_1y(dbv, dsv):
    return _rolling_sum(dbv-dsv, _TD_YEAR)

def _ceo_buy_1y(c):
    return _rolling_sum(c, _TD_YEAR)

def _ceo_buy_half(c):
    return _rolling_sum(c, _TD_HALF)

def _cfo_buy_1q(cf):
    return _rolling_sum(cf, _TD_QTR)

def _slope_fn(arr):
    n = len(arr)
    if n < 2: return np.nan
    x = np.arange(n, dtype=float)
    xm, ym = x.mean(), arr.mean()
    denom = ((x-xm)**2).sum()
    if denom == 0: return np.nan
    return ((x-xm)*(arr-ym)).sum()/denom


# ── 2nd-derivative feature functions 026-075 ──────────────────────────────────

def irw_drv2_026_rws_1y_yoy_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """YoY change in the 1Y role-weighted buy score."""
    base = _rws_1y(c, cf, o, d, t)
    return base - base.shift(_TD_YEAR)


def irw_drv2_027_sci_1y_yoy_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY change in the 1Y seniority conviction index."""
    base = _sci_1y(c, cf, o, d, t, ins)
    return base - base.shift(_TD_YEAR)


def irw_drv2_028_top_officer_share_1y_yoy_diff(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY change in the 1Y top-officer (CEO+CFO) value share."""
    base = _top_off_share_1y(c, cf, ins)
    return base - base.shift(_TD_YEAR)


def irw_drv2_029_off_dir_ratio_1y_yoy_diff(o: pd.Series, d: pd.Series) -> pd.Series:
    """YoY change in the 1Y officer-to-director buy value ratio."""
    base = _off_dir_ratio_1y(o, d)
    return base - base.shift(_TD_YEAR)


def irw_drv2_030_officer_net_1y_yoy_diff(obv: pd.Series, osv: pd.Series) -> pd.Series:
    """YoY change in the 1Y officer net buy value."""
    base = _off_net_1y(obv, osv)
    return base - base.shift(_TD_YEAR)


def irw_drv2_031_rws_half_qoq_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """QoQ change in the half-year role-weighted buy score."""
    base = _rws_half(c, cf, o, d, t)
    return base - base.shift(_TD_QTR)


def irw_drv2_032_sci_half_qoq_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """QoQ change in the half-year seniority conviction index."""
    base = _sci_half(c, cf, o, d, t, ins)
    return base - base.shift(_TD_QTR)


def irw_drv2_033_top_off_share_half_qoq_diff(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """QoQ change in the half-year top-officer value share."""
    base = _top_off_share_half(c, cf, ins)
    return base - base.shift(_TD_QTR)


def irw_drv2_034_off_dir_ratio_half_qoq_diff(o: pd.Series, d: pd.Series) -> pd.Series:
    """QoQ change in the half-year officer-to-director ratio."""
    base = _off_dir_ratio_half(o, d)
    return base - base.shift(_TD_QTR)


def irw_drv2_035_ceo_buy_1y_yoy_diff(c: pd.Series) -> pd.Series:
    """YoY change in the rolling 1Y CEO buy value."""
    base = _ceo_buy_1y(c)
    return base - base.shift(_TD_YEAR)


def irw_drv2_036_ceo_buy_half_qoq_diff(c: pd.Series) -> pd.Series:
    """QoQ change in the rolling half-year CEO buy value."""
    base = _ceo_buy_half(c)
    return base - base.shift(_TD_QTR)


def irw_drv2_037_cfo_buy_1q_yoy_diff(cf: pd.Series) -> pd.Series:
    """YoY change in the rolling 1Q CFO buy value."""
    base = _cfo_buy_1q(cf)
    return base - base.shift(_TD_YEAR)


def irw_drv2_038_rws_1q_slope_half(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """OLS slope of the 1Q role-weighted score over trailing half year (126d)."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    return base.rolling(_TD_HALF, min_periods=max(2, _TD_HALF//4)).apply(_slope_fn, raw=True)


def irw_drv2_039_sci_1q_slope_half(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """OLS slope of the 1Q SCI series over trailing half year."""
    base = _sci_1q(c, cf, o, d, t, ins).fillna(0.0)
    return base.rolling(_TD_HALF, min_periods=max(2, _TD_HALF//4)).apply(_slope_fn, raw=True)


def irw_drv2_040_top_off_share_1q_slope(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """OLS slope of the 1Q top-officer share series over trailing 1 year."""
    base = _top_officer_share_1q(c, cf, ins).fillna(0.0)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).apply(_slope_fn, raw=True)


def irw_drv2_041_off_dir_ratio_1q_slope(o: pd.Series, d: pd.Series) -> pd.Series:
    """OLS slope of the 1Q officer-to-director ratio over trailing 1 year."""
    base = _officer_to_director_ratio_1q(o, d).fillna(0.0)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).apply(_slope_fn, raw=True)


def irw_drv2_042_officer_net_1q_slope(obv: pd.Series, osv: pd.Series) -> pd.Series:
    """OLS slope of the 1Q officer net buy series over trailing 1 year."""
    base = _officer_net_buy_1q(obv, osv)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).apply(_slope_fn, raw=True)


def irw_drv2_043_dir_net_1q_slope(dbv: pd.Series, dsv: pd.Series) -> pd.Series:
    """OLS slope of the 1Q director net buy series over trailing 1 year."""
    base = _director_net_buy_1q(dbv, dsv)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).apply(_slope_fn, raw=True)


def irw_drv2_044_rws_1q_pct_chg_yoy(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """YoY percent change in the 1Q role-weighted buy score."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    prior = base.shift(_TD_YEAR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_045_sci_1q_pct_chg_yoy(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY percent change in the 1Q seniority conviction index."""
    base = _sci_1q(c, cf, o, d, t, ins)
    prior = base.shift(_TD_YEAR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_046_top_off_share_1q_pct_chg_yoy(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY percent change in the 1Q top-officer value share."""
    base = _top_officer_share_1q(c, cf, ins)
    prior = base.shift(_TD_YEAR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_047_ceo_buy_1q_pct_chg_yoy(c: pd.Series) -> pd.Series:
    """YoY percent change in the rolling 1Q CEO buy value."""
    base = _ceo_buy_1q(c)
    prior = base.shift(_TD_YEAR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_048_officer_net_1q_pct_chg_qoq(obv: pd.Series, osv: pd.Series) -> pd.Series:
    """QoQ percent change in the 1Q officer net buy value."""
    base = _officer_net_buy_1q(obv, osv)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def irw_drv2_049_dir_net_1q_qoq_diff(dbv: pd.Series, dsv: pd.Series) -> pd.Series:
    """QoQ change in the 1Q director net buy value (2nd derivative)."""
    base = _director_net_buy_1q(dbv, dsv)
    return base - base.shift(_TD_QTR)


def irw_drv2_050_rws_1q_ewm_deviation_1y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """1Q RWS minus its EWM (span=252): deviation from 1Y exponential trend."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    return base - base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()


def irw_drv2_051_off_share_1q_ewm_deviation(o: pd.Series, ins: pd.Series) -> pd.Series:
    """1Q officer share minus its EWM (span=252): deviation of officer share from trend."""
    base = _officer_share_1q(o, ins).fillna(0.0)
    return base - base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()


def irw_drv2_052_off_dir_ratio_1q_ewm_deviation(o: pd.Series, d: pd.Series) -> pd.Series:
    """1Q officer-to-director ratio minus its EWM (span=252)."""
    base = _officer_to_director_ratio_1q(o, d).fillna(0.0)
    return base - base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()


def irw_drv2_053_ceo_buy_1q_ewm_deviation(c: pd.Series) -> pd.Series:
    """1Q CEO buy value minus its EWM (span=252)."""
    base = _ceo_buy_1q(c)
    return base - base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()


def irw_drv2_054_sci_1q_zscore_2y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """Z-score of the 1Q SCI within trailing 2-year window."""
    base = _sci_1q(c, cf, o, d, t, ins).fillna(0.0)
    m  = base.rolling(_TD_2Y, min_periods=max(1, _TD_2Y//4)).mean()
    sd = base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_055_rws_1q_zscore_2y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """Z-score of the 1Q role-weighted score within trailing 2-year window."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    m  = base.rolling(_TD_2Y, min_periods=max(1, _TD_2Y//4)).mean()
    sd = base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_056_top_off_share_1q_zscore_1y(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """Z-score of the 1Q top-officer share within trailing 1-year window."""
    base = _top_officer_share_1q(c, cf, ins).fillna(0.0)
    m  = base.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()
    sd = base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_057_off_share_1q_zscore_1y(o: pd.Series, ins: pd.Series) -> pd.Series:
    """Z-score of the 1Q officer value share within trailing 1-year window."""
    base = _officer_share_1q(o, ins).fillna(0.0)
    m  = base.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR//4)).mean()
    sd = base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_058_ceo_buy_1q_zscore_2y(c: pd.Series) -> pd.Series:
    """Z-score of the 1Q CEO buy value within trailing 2-year window."""
    base = _ceo_buy_1q(c)
    m  = base.rolling(_TD_2Y, min_periods=max(1, _TD_2Y//4)).mean()
    sd = base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_059_sci_1q_pct_rank_2y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """Percentile rank of 1Q SCI within trailing 2-year window."""
    base = _sci_1q(c, cf, o, d, t, ins).fillna(0.0)
    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).rank(pct=True)


def irw_drv2_060_rws_1q_pct_rank_2y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """Percentile rank of 1Q role-weighted score within trailing 2-year window."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    return base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).rank(pct=True)


def irw_drv2_061_rws_1q_pct_rank_1y(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """Percentile rank of 1Q role-weighted score within trailing 1-year window."""
    base = _role_weighted_score_1q(c, cf, o, d, t)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR//4)).rank(pct=True)


def irw_drv2_062_off_dir_ratio_1q_zscore_2y(o: pd.Series, d: pd.Series) -> pd.Series:
    """Z-score of the 1Q officer-to-director ratio within trailing 2-year window."""
    base = _officer_to_director_ratio_1q(o, d).fillna(0.0)
    m  = base.rolling(_TD_2Y, min_periods=max(1, _TD_2Y//4)).mean()
    sd = base.rolling(_TD_2Y, min_periods=max(2, _TD_2Y//4)).std()
    return _safe_div(base - m, sd)


def irw_drv2_063_rws_half_yoy_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series) -> pd.Series:
    """YoY change in the half-year role-weighted buy score."""
    base = _rws_half(c, cf, o, d, t)
    return base - base.shift(_TD_YEAR)


def irw_drv2_064_sci_half_yoy_diff(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY change in the half-year seniority conviction index."""
    base = _sci_half(c, cf, o, d, t, ins)
    return base - base.shift(_TD_YEAR)


def irw_drv2_065_top_off_share_half_yoy_diff(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """YoY change in the half-year top-officer value share."""
    base = _top_off_share_half(c, cf, ins)
    return base - base.shift(_TD_YEAR)


def irw_drv2_066_officer_net_1y_qoq_diff(obv: pd.Series, osv: pd.Series) -> pd.Series:
    """QoQ change in the 1Y officer net buy value."""
    base = _off_net_1y(obv, osv)
    return base - base.shift(_TD_QTR)


def irw_drv2_067_director_net_1y_qoq_diff(dbv: pd.Series, dsv: pd.Series) -> pd.Series:
    """QoQ change in the 1Y director net buy value."""
    base = _dir_net_1y(dbv, dsv)
    return base - base.shift(_TD_QTR)


def irw_drv2_068_ceo_buy_1q_acceleration(c: pd.Series) -> pd.Series:
    """Second difference of 1Q CEO buy value (QoQ acceleration)."""
    base = _ceo_buy_1q(c)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def irw_drv2_069_cfo_buy_1q_acceleration(cf: pd.Series) -> pd.Series:
    """Second difference of 1Q CFO buy value (QoQ acceleration)."""
    base = _cfo_buy_1q(cf)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def irw_drv2_070_officer_net_1q_acceleration(obv: pd.Series, osv: pd.Series) -> pd.Series:
    """Second difference of 1Q officer net buy (QoQ acceleration)."""
    base = _officer_net_buy_1q(obv, osv)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def irw_drv2_071_top_off_share_1q_acceleration(c: pd.Series, cf: pd.Series, ins: pd.Series) -> pd.Series:
    """Second difference of 1Q top-officer share (QoQ acceleration)."""
    base = _top_officer_share_1q(c, cf, ins)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def irw_drv2_072_off_share_1q_qoq_diff(o: pd.Series, ins: pd.Series) -> pd.Series:
    """QoQ change in the 1Q officer value share (2nd derivative)."""
    base = _officer_share_1q(o, ins)
    return base - base.shift(_TD_QTR)


def irw_drv2_073_off_share_1y_qoq_diff(o: pd.Series, ins: pd.Series) -> pd.Series:
    """QoQ change in the 1Y officer value share."""
    base = _off_share_1y(o, ins)
    return base - base.shift(_TD_QTR)


def irw_drv2_074_composite_2nd_deriv_momentum(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """Composite 2nd-derivative momentum: equally weighted z-scores of QoQ RWS diff and QoQ SCI diff."""
    rws_d = _role_weighted_score_1q(c, cf, o, d, t)
    rws_qoq = rws_d - rws_d.shift(_TD_QTR)
    sci_d = _sci_1q(c, cf, o, d, t, ins).fillna(0.0)
    sci_qoq = sci_d - sci_d.shift(_TD_QTR)
    def _z(s):
        m = s.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
        sd = s.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
        return _safe_div(s-m, sd).fillna(0.0)
    return (_z(rws_qoq) + _z(sci_qoq)) / 2.0


def irw_drv2_075_composite_2nd_deriv_acceleration(c: pd.Series, cf: pd.Series, o: pd.Series, d: pd.Series, t: pd.Series, ins: pd.Series) -> pd.Series:
    """Composite 2nd-derivative acceleration: avg z-score of QoQ-of-QoQ RWS and SCI diffs."""
    rws_b = _role_weighted_score_1q(c, cf, o, d, t)
    rws_d1 = rws_b - rws_b.shift(_TD_QTR)
    rws_d2 = rws_d1 - rws_d1.shift(_TD_QTR)
    sci_b = _sci_1q(c, cf, o, d, t, ins).fillna(0.0)
    sci_d1 = sci_b - sci_b.shift(_TD_QTR)
    sci_d2 = sci_d1 - sci_d1.shift(_TD_QTR)
    def _z(s):
        m = s.rolling(_TD_YEAR, min_periods=max(1,_TD_YEAR//4)).mean()
        sd = s.rolling(_TD_YEAR, min_periods=max(2,_TD_YEAR//4)).std()
        return _safe_div(s-m, sd).fillna(0.0)
    return (_z(rws_d2) + _z(sci_d2)) / 2.0


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_ROLE_WEIGHT_REGISTRY_2ND_DERIVATIVES = {
    "irw_drv2_001_role_weighted_score_1q_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_001_role_weighted_score_1q_qoq_diff,
    },
    "irw_drv2_002_top_officer_share_1q_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_002_top_officer_share_1q_qoq_diff,
    },
    "irw_drv2_003_officer_share_1q_qoq_diff": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_003_officer_share_1q_qoq_diff,
    },
    "irw_drv2_004_sci_1q_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_004_sci_1q_qoq_diff,
    },
    "irw_drv2_005_officer_to_director_ratio_1q_qoq_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_005_officer_to_director_ratio_1q_qoq_diff,
    },
    "irw_drv2_006_ceo_buy_1q_qoq_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_006_ceo_buy_1q_qoq_diff,
    },
    "irw_drv2_007_cfo_buy_1q_qoq_diff": {
        "inputs": ["cfo_buy_value"],
        "func": irw_drv2_007_cfo_buy_1q_qoq_diff,
    },
    "irw_drv2_008_officer_net_buy_1q_qoq_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_008_officer_net_buy_1q_qoq_diff,
    },
    "irw_drv2_009_director_net_buy_1q_qoq_diff": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_drv2_009_director_net_buy_1q_qoq_diff,
    },
    "irw_drv2_010_role_weighted_score_1q_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_010_role_weighted_score_1q_yoy_diff,
    },
    "irw_drv2_011_sci_1q_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_011_sci_1q_yoy_diff,
    },
    "irw_drv2_012_top_officer_share_1q_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_012_top_officer_share_1q_yoy_diff,
    },
    "irw_drv2_013_ceo_buy_1q_slope": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_013_ceo_buy_1q_slope,
    },
    "irw_drv2_014_sci_1q_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_014_sci_1q_slope,
    },
    "irw_drv2_015_role_weighted_score_1q_pct_chg_qoq": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_015_role_weighted_score_1q_pct_chg_qoq,
    },
    "irw_drv2_016_officer_to_director_ratio_1q_yoy_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_016_officer_to_director_ratio_1q_yoy_diff,
    },
    "irw_drv2_017_ceo_buy_1q_pct_chg_qoq": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_017_ceo_buy_1q_pct_chg_qoq,
    },
    "irw_drv2_018_officer_share_1q_yoy_diff": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_018_officer_share_1q_yoy_diff,
    },
    "irw_drv2_019_sci_1q_ewm_deviation": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_019_sci_1q_ewm_deviation,
    },
    "irw_drv2_020_top_officer_share_1q_pct_chg_qoq": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_020_top_officer_share_1q_pct_chg_qoq,
    },
    "irw_drv2_021_officer_net_buy_1q_yoy_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_021_officer_net_buy_1q_yoy_diff,
    },
    "irw_drv2_022_director_net_buy_1q_yoy_diff": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_drv2_022_director_net_buy_1q_yoy_diff,
    },
    "irw_drv2_023_role_weighted_score_1q_acceleration": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_023_role_weighted_score_1q_acceleration,
    },
    "irw_drv2_024_sci_1q_acceleration": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_024_sci_1q_acceleration,
    },
    "irw_drv2_025_ceo_cfo_combined_1q_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_drv2_025_ceo_cfo_combined_1q_qoq_diff,
    },
    "irw_drv2_026_rws_1y_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_026_rws_1y_yoy_diff,
    },
    "irw_drv2_027_sci_1y_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_027_sci_1y_yoy_diff,
    },
    "irw_drv2_028_top_officer_share_1y_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_028_top_officer_share_1y_yoy_diff,
    },
    "irw_drv2_029_off_dir_ratio_1y_yoy_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_029_off_dir_ratio_1y_yoy_diff,
    },
    "irw_drv2_030_officer_net_1y_yoy_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_030_officer_net_1y_yoy_diff,
    },
    "irw_drv2_031_rws_half_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_031_rws_half_qoq_diff,
    },
    "irw_drv2_032_sci_half_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_032_sci_half_qoq_diff,
    },
    "irw_drv2_033_top_off_share_half_qoq_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_033_top_off_share_half_qoq_diff,
    },
    "irw_drv2_034_off_dir_ratio_half_qoq_diff": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_034_off_dir_ratio_half_qoq_diff,
    },
    "irw_drv2_035_ceo_buy_1y_yoy_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_035_ceo_buy_1y_yoy_diff,
    },
    "irw_drv2_036_ceo_buy_half_qoq_diff": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_036_ceo_buy_half_qoq_diff,
    },
    "irw_drv2_037_cfo_buy_1q_yoy_diff": {
        "inputs": ["cfo_buy_value"],
        "func": irw_drv2_037_cfo_buy_1q_yoy_diff,
    },
    "irw_drv2_038_rws_1q_slope_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_038_rws_1q_slope_half,
    },
    "irw_drv2_039_sci_1q_slope_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_039_sci_1q_slope_half,
    },
    "irw_drv2_040_top_off_share_1q_slope": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_040_top_off_share_1q_slope,
    },
    "irw_drv2_041_off_dir_ratio_1q_slope": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_041_off_dir_ratio_1q_slope,
    },
    "irw_drv2_042_officer_net_1q_slope": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_042_officer_net_1q_slope,
    },
    "irw_drv2_043_dir_net_1q_slope": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_drv2_043_dir_net_1q_slope,
    },
    "irw_drv2_044_rws_1q_pct_chg_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_044_rws_1q_pct_chg_yoy,
    },
    "irw_drv2_045_sci_1q_pct_chg_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_045_sci_1q_pct_chg_yoy,
    },
    "irw_drv2_046_top_off_share_1q_pct_chg_yoy": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_046_top_off_share_1q_pct_chg_yoy,
    },
    "irw_drv2_047_ceo_buy_1q_pct_chg_yoy": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_047_ceo_buy_1q_pct_chg_yoy,
    },
    "irw_drv2_048_officer_net_1q_pct_chg_qoq": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_048_officer_net_1q_pct_chg_qoq,
    },
    "irw_drv2_049_dir_net_1q_qoq_diff": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_drv2_049_dir_net_1q_qoq_diff,
    },
    "irw_drv2_050_rws_1q_ewm_deviation_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_050_rws_1q_ewm_deviation_1y,
    },
    "irw_drv2_051_off_share_1q_ewm_deviation": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_051_off_share_1q_ewm_deviation,
    },
    "irw_drv2_052_off_dir_ratio_1q_ewm_deviation": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_052_off_dir_ratio_1q_ewm_deviation,
    },
    "irw_drv2_053_ceo_buy_1q_ewm_deviation": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_053_ceo_buy_1q_ewm_deviation,
    },
    "irw_drv2_054_sci_1q_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_054_sci_1q_zscore_2y,
    },
    "irw_drv2_055_rws_1q_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_055_rws_1q_zscore_2y,
    },
    "irw_drv2_056_top_off_share_1q_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_056_top_off_share_1q_zscore_1y,
    },
    "irw_drv2_057_off_share_1q_zscore_1y": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_057_off_share_1q_zscore_1y,
    },
    "irw_drv2_058_ceo_buy_1q_zscore_2y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_058_ceo_buy_1q_zscore_2y,
    },
    "irw_drv2_059_sci_1q_pct_rank_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_059_sci_1q_pct_rank_2y,
    },
    "irw_drv2_060_rws_1q_pct_rank_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_060_rws_1q_pct_rank_2y,
    },
    "irw_drv2_061_rws_1q_pct_rank_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_061_rws_1q_pct_rank_1y,
    },
    "irw_drv2_062_off_dir_ratio_1q_zscore_2y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_drv2_062_off_dir_ratio_1q_zscore_2y,
    },
    "irw_drv2_063_rws_half_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_drv2_063_rws_half_yoy_diff,
    },
    "irw_drv2_064_sci_half_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_064_sci_half_yoy_diff,
    },
    "irw_drv2_065_top_off_share_half_yoy_diff": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_065_top_off_share_half_yoy_diff,
    },
    "irw_drv2_066_officer_net_1y_qoq_diff": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_066_officer_net_1y_qoq_diff,
    },
    "irw_drv2_067_director_net_1y_qoq_diff": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_drv2_067_director_net_1y_qoq_diff,
    },
    "irw_drv2_068_ceo_buy_1q_acceleration": {
        "inputs": ["ceo_buy_value"],
        "func": irw_drv2_068_ceo_buy_1q_acceleration,
    },
    "irw_drv2_069_cfo_buy_1q_acceleration": {
        "inputs": ["cfo_buy_value"],
        "func": irw_drv2_069_cfo_buy_1q_acceleration,
    },
    "irw_drv2_070_officer_net_1q_acceleration": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_drv2_070_officer_net_1q_acceleration,
    },
    "irw_drv2_071_top_off_share_1q_acceleration": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_drv2_071_top_off_share_1q_acceleration,
    },
    "irw_drv2_072_off_share_1q_qoq_diff": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_072_off_share_1q_qoq_diff,
    },
    "irw_drv2_073_off_share_1y_qoq_diff": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_drv2_073_off_share_1y_qoq_diff,
    },
    "irw_drv2_074_composite_2nd_deriv_momentum": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_074_composite_2nd_deriv_momentum,
    },
    "irw_drv2_075_composite_2nd_deriv_acceleration": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_drv2_075_composite_2nd_deriv_acceleration,
    },
}
