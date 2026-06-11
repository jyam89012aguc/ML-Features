"""
121_distress_score_ensemble — Base Features 076-150
Domain: ensemble of academic bankruptcy / distress scores — multi-window history,
        normalized variants, cross-model comparisons, and structural credit proxies.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily) + SEP close price
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  All feature functions in this file look strictly backward.
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63
_TD_2Q   = 126
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _vol_annual(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    """Annualized close-to-close log-return volatility over w trading days."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=max(2, w // 4)).std() * np.sqrt(_TD_YEAR)


# ── Helper: assemble core distress scores (reused across features) ─────────────

def _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo):
    size  = np.log(assets.clip(lower=_EPS))
    tlta  = _safe_div(liabilities, assets).fillna(0)
    wc    = currentassets - currentliabilities
    wcta  = _safe_div(wc, assets).fillna(0)
    clca  = _safe_div(currentliabilities, currentassets).fillna(0)
    oeneg = (liabilities > assets).astype(float)
    nita  = _safe_div(netinc, assets).fillna(0)
    futl  = _safe_div(ncfo, liabilities).fillna(0)
    ni_prev = netinc.shift(_TD_QTR)
    intwo = ((netinc < 0) & (ni_prev < 0)).astype(float)
    chin  = _safe_div(netinc - ni_prev, netinc.abs() + ni_prev.abs()).fillna(0)
    return (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
            + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
            - 1.83 * futl + 0.285 * intwo - 0.521 * chin)


def _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities):
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    return -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl


def _springate_score(currentassets, currentliabilities, assets, ebit, revenue):
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    return 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d


def _merton_dd(debt, marketcap, close, vol_window=_TD_QTR):
    sigma = _vol_annual(close, vol_window).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    return _safe_div(ln_vd, sigma) + 0.5 * sigma


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Ohlson O-score multi-window history ---

def dse_076_ohlson_oscore_max_504d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Trailing 504-day (2-year) maximum of Ohlson O-score (highest distress reached)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _rolling_max(o, _TD_2Y)


def dse_077_ohlson_oscore_median_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Trailing 252-day median of Ohlson O-score."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _rolling_median(o, _TD_YEAR)


def dse_078_ohlson_oscore_vs_252d_max(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """O-score as fraction of its 252-day maximum (1.0 = at worst)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    mx = _rolling_max(o, _TD_YEAR)
    return _safe_div(o, mx.clip(lower=_EPS))


def dse_079_ohlson_oscore_ewm_63d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) Ohlson O-score (slow trend)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _ewm_mean(o, 63)


def dse_080_ohlson_prob_ewm_63d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) Ohlson bankruptcy probability."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _ewm_mean(prob, 63)


def dse_081_ohlson_prob_max_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Trailing 252-day maximum of Ohlson bankruptcy probability."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _rolling_max(prob, _TD_YEAR)


def dse_082_ohlson_prob_above50_consec(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Consecutive days Ohlson bankruptcy probability > 0.5 (sustained distress streak)."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    cond = prob > 0.5
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_083_ohlson_oscore_3y_expanding_pct_rank(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Expanding all-time percentile rank of Ohlson O-score."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return o.expanding(min_periods=4).rank(pct=True)


def dse_084_ohlson_oscore_2y_zscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Z-score of Ohlson O-score relative to its trailing 504-day (2-year) distribution."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _zscore_rolling(o, _TD_2Y)


def dse_085_ohlson_prob_days_above50_in_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where Ohlson prob > 0.5."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    flag = (prob > 0.5).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


# --- Group I (086-095): Zmijewski score multi-window history ---

def dse_086_zmijewski_score_max_504d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Trailing 504-day maximum of Zmijewski score (highest distress reached in 2 years)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _rolling_max(zm, _TD_2Y)


def dse_087_zmijewski_score_median_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Trailing 252-day median of Zmijewski score."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _rolling_median(zm, _TD_YEAR)


def dse_088_zmijewski_score_ewm_63d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) Zmijewski score."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _ewm_mean(zm, 63)


def dse_089_zmijewski_score_2y_zscore(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Z-score of Zmijewski score relative to trailing 504-day (2-year) distribution."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _zscore_rolling(zm, _TD_2Y)


def dse_090_zmijewski_score_expanding_pct_rank(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Expanding all-time percentile rank of Zmijewski score."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm.expanding(min_periods=4).rank(pct=True)


def dse_091_zmijewski_distress_days_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where Zmijewski score > 0 (distress zone)."""
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    flag = (zm > 0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def dse_092_zmijewski_score_vs_252d_max(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Zmijewski score minus its 252-day maximum (distance from worst)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    mx = _rolling_max(zm, _TD_YEAR)
    return zm - mx


def dse_093_zmijewski_consec_distress_days(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Consecutive days Zmijewski score has been > 0 (distress streak)."""
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    cond = zm > 0
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_094_zmijewski_roa_rolling_mean_4q(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski ROA averaged over trailing 4 quarters (252 days)."""
    roa = _safe_div(netinc, assets)
    return _rolling_mean(roa, _TD_YEAR)


def dse_095_zmijewski_leverage_rolling_mean_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski leverage (liabilities/assets) averaged over trailing 4 quarters."""
    lev = _safe_div(liabilities, assets)
    return _rolling_mean(lev, _TD_YEAR)


# --- Group J (096-105): Merton distance-to-default multi-window and combinations ---

def dse_096_merton_dd_252d_vol(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton DD proxy using 252-day annual volatility window."""
    return _merton_dd(debt, marketcap, close, _TD_YEAR)


def dse_097_merton_dd_21d_vol(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton DD proxy using 21-day (monthly) volatility window — fast signal."""
    return _merton_dd(debt, marketcap, close, _TD_MON)


def dse_098_merton_dd_expanding_min(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """All-time expanding minimum of Merton DD proxy (worst default proximity ever)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd.expanding(min_periods=4).min()


def dse_099_merton_dd_vs_expanding_min(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton DD minus its expanding minimum (distance from all-time worst)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd - dd.expanding(min_periods=4).min()


def dse_100_merton_dd_median_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252-day median of Merton DD proxy."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _rolling_median(dd, _TD_YEAR)


def dse_101_merton_dd_ewm_63d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) Merton DD proxy."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _ewm_mean(dd, 63)


def dse_102_merton_dd_below3_days_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where Merton DD proxy < 3.0."""
    dd   = _merton_dd(debt, marketcap, close, _TD_QTR)
    flag = (dd < 3.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def dse_103_merton_dd_consec_below2(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days Merton DD proxy has been < 2.0."""
    dd   = _merton_dd(debt, marketcap, close, _TD_QTR)
    cond = dd < 2.0
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_104_merton_vol_times_leverage(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton composite stress: annualized vol * (debt/marketcap). Measures vol-scaled leverage."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    lev   = _safe_div(debt, marketcap.clip(lower=_EPS))
    return sigma * lev


def dse_105_merton_dd_2y_zscore(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Merton DD proxy relative to trailing 504-day (2-year) distribution."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _zscore_rolling(dd, _TD_2Y)


# --- Group K (106-115): Springate and Fulmer multi-window history ---

def dse_106_springate_score_max_504d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Trailing 504-day minimum of Springate score (worst health in 2 years)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _rolling_min(s, _TD_2Y)


def dse_107_springate_score_median_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Trailing 252-day median of Springate score."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _rolling_median(s, _TD_YEAR)


def dse_108_springate_score_ewm_63d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) Springate score."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _ewm_mean(s, 63)


def dse_109_springate_distress_days_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where Springate score < 0.862."""
    s    = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    flag = (s < 0.862).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def dse_110_springate_expanding_pct_rank(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Expanding all-time percentile rank of Springate score."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return s.expanding(min_periods=4).rank(pct=True)


def dse_111_fulmer_score_pct_rank_252d(
    retearn: pd.Series,
    assets: pd.Series,
    revenue: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    ncfo: pd.Series,
    liabilities: pd.Series,
    debt: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Fulmer H-score within trailing 252-day distribution."""
    v1 = _safe_div(retearn, assets).fillna(0)
    v2 = _safe_div(revenue, assets).fillna(0)
    v3 = _safe_div(ebit, equity).fillna(0)
    v4 = _safe_div(ncfo, liabilities).fillna(0)
    v5 = _safe_div(debt, assets).fillna(0)
    v6 = _safe_div(currentliabilities, assets).fillna(0)
    v7 = np.log(assets.clip(lower=_EPS))
    wc = currentassets - currentliabilities
    v8 = _safe_div(wc, liabilities).fillna(0)
    h = (5.528 * v1 + 0.212 * v2 + 0.073 * v3 + 1.27 * v4
         - 0.12 * v5 + 2.335 * v6 + 0.575 * v7 + 1.083 * v8 - 6.075)
    return _rolling_rank_pct(h, _TD_YEAR)


def dse_112_fulmer_score_ewm_63d(
    retearn: pd.Series,
    assets: pd.Series,
    revenue: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    ncfo: pd.Series,
    liabilities: pd.Series,
    debt: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) Fulmer H-score."""
    v1 = _safe_div(retearn, assets).fillna(0)
    v2 = _safe_div(revenue, assets).fillna(0)
    v3 = _safe_div(ebit, equity).fillna(0)
    v4 = _safe_div(ncfo, liabilities).fillna(0)
    v5 = _safe_div(debt, assets).fillna(0)
    v6 = _safe_div(currentliabilities, assets).fillna(0)
    v7 = np.log(assets.clip(lower=_EPS))
    wc = currentassets - currentliabilities
    v8 = _safe_div(wc, liabilities).fillna(0)
    h = (5.528 * v1 + 0.212 * v2 + 0.073 * v3 + 1.27 * v4
         - 0.12 * v5 + 2.335 * v6 + 0.575 * v7 + 1.083 * v8 - 6.075)
    return _ewm_mean(h, 63)


def dse_113_fulmer_distress_days_252d(
    retearn: pd.Series,
    assets: pd.Series,
    revenue: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    ncfo: pd.Series,
    liabilities: pd.Series,
    debt: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where Fulmer H-score < 0."""
    v1 = _safe_div(retearn, assets).fillna(0)
    v2 = _safe_div(revenue, assets).fillna(0)
    v3 = _safe_div(ebit, equity).fillna(0)
    v4 = _safe_div(ncfo, liabilities).fillna(0)
    v5 = _safe_div(debt, assets).fillna(0)
    v6 = _safe_div(currentliabilities, assets).fillna(0)
    v7 = np.log(assets.clip(lower=_EPS))
    wc = currentassets - currentliabilities
    v8 = _safe_div(wc, liabilities).fillna(0)
    h    = (5.528 * v1 + 0.212 * v2 + 0.073 * v3 + 1.27 * v4
            - 0.12 * v5 + 2.335 * v6 + 0.575 * v7 + 1.083 * v8 - 6.075)
    flag = (h < 0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def dse_114_ca_score_max_504d(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Trailing 504-day minimum of CA-Score (worst in 2 years; lower = more distress)."""
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    return _rolling_min(ca, _TD_2Y)


def dse_115_ca_score_ewm_63d(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=63) CA-Score."""
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    return _ewm_mean(ca, 63)


# --- Group L (116-130): Cross-model composites, normalized aggregates ---

def dse_116_ohlson_zmijewski_combined_zscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Average of z-scored Ohlson and Zmijewski (both normalized to 252d)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    oz = _zscore_rolling(o, _TD_YEAR)
    zz = _zscore_rolling(zm, _TD_YEAR)
    return (oz + zz) / 2.0


def dse_117_three_model_avg_zscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Average of z-scored Ohlson, Zmijewski, and Springate (all normalized to 252d)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    oz = _zscore_rolling(o, _TD_YEAR)
    zz = _zscore_rolling(zm, _TD_YEAR)
    sz = _zscore_rolling(-sp, _TD_YEAR)  # flip Springate: lower = more distress
    return (oz + zz + sz) / 3.0


def dse_118_ohlson_springate_distress_both_flag(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if both Ohlson prob > 0.5 AND Springate < 0.862."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    sp   = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return ((prob > 0.5) & (sp < 0.862)).astype(float)


def dse_119_ohlson_vs_zmijewski_direction(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Agreement direction: z_ohlson * z_zmijewski (positive = both models agree on trend)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    oz = _zscore_rolling(o, _TD_YEAR).fillna(0)
    zz = _zscore_rolling(zm, _TD_YEAR).fillna(0)
    return oz * zz


def dse_120_ensemble_distress_score_4model_norm(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
    equity: pd.Series,
    depreciation: pd.Series,
) -> pd.Series:
    """
    Normalized 4-model ensemble distress score.
    Average of percentile ranks of Ohlson (higher=worse), Zmijewski (higher=worse),
    1-Springate_pct (lower Springate=worse), and CA-Score negated pct (lower CA=worse).
    Score in [0,1]; higher = more distress.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    o_pct  = _rolling_rank_pct(o, _TD_YEAR).fillna(0.5)
    zm_pct = _rolling_rank_pct(zm, _TD_YEAR).fillna(0.5)
    sp_pct = 1.0 - _rolling_rank_pct(sp, _TD_YEAR).fillna(0.5)
    ca_pct = 1.0 - _rolling_rank_pct(ca, _TD_YEAR).fillna(0.5)
    return (o_pct + zm_pct + sp_pct + ca_pct) / 4.0


def dse_121_ohlson_prob_change_63d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """63-day change in Ohlson bankruptcy probability (worsening rate)."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return prob - prob.shift(_TD_QTR)


def dse_122_zmijewski_score_change_63d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """63-day change in Zmijewski score (distress velocity)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm - zm.shift(_TD_QTR)


def dse_123_springate_score_change_63d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """63-day change in Springate score (health improvement/deterioration velocity)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return s - s.shift(_TD_QTR)


def dse_124_merton_dd_change_63d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """63-day change in Merton DD proxy (approaching/receding from default)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd - dd.shift(_TD_QTR)


def dse_125_ensemble_flag_worsened_3models(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if all 3 models have worsened QoQ (Ohlson up, Zmijewski up, Springate down)."""
    o   = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm  = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp  = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    o_worse  = (o  > o.shift(_TD_QTR)).astype(float)
    zm_worse = (zm > zm.shift(_TD_QTR)).astype(float)
    sp_worse = (sp < sp.shift(_TD_QTR)).astype(float)
    return o_worse * zm_worse * sp_worse


def dse_126_credit_deterioration_composite(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
    debt: pd.Series,
    marketcap: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Composite credit deterioration score combining 4 models.
    Ohlson z-score + Zmijewski z-score + negative-Springate z-score + negative-Merton-DD z-score.
    All normalized to 252-day distribution. Higher = more distress.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return (_zscore_rolling(o, _TD_YEAR).fillna(0)
            + _zscore_rolling(zm, _TD_YEAR).fillna(0)
            + _zscore_rolling(-sp, _TD_YEAR).fillna(0)
            + _zscore_rolling(-dd, _TD_YEAR).fillna(0))


def dse_127_ohlson_tlta_trend_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Trend in Ohlson leverage (TLTA) over last 4 quarters: current vs 1-year lag."""
    tlta = _safe_div(liabilities, assets)
    return tlta - tlta.shift(_TD_YEAR)


def dse_128_ohlson_nita_trend_4q(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Trend in Ohlson profitability (NITA) over last 4 quarters."""
    nita = _safe_div(netinc, assets)
    return nita - nita.shift(_TD_YEAR)


def dse_129_merton_vol_change_63d(close: pd.Series) -> pd.Series:
    """63-day change in annualized equity volatility (volatility drift)."""
    vol = _vol_annual(close, _TD_QTR)
    return vol - vol.shift(_TD_QTR)


def dse_130_merton_leverage_change_63d(debt: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day change in Merton leverage ratio (debt/marketcap)."""
    lev = _safe_div(debt, marketcap.clip(lower=_EPS))
    return lev - lev.shift(_TD_QTR)


# --- Group M (131-150): Additional normalized variants and structural credit proxies ---

def dse_131_ohlson_wcta_expanding_min(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
) -> pd.Series:
    """Expanding all-time minimum of Ohlson WCTA (most extreme working capital stress ever)."""
    wc   = currentassets - currentliabilities
    wcta = _safe_div(wc, assets)
    return wcta.expanding(min_periods=4).min()


def dse_132_ohlson_futl_expanding_min(ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Expanding all-time minimum of Ohlson FUTL (worst cash coverage ever)."""
    futl = _safe_div(ncfo, liabilities)
    return futl.expanding(min_periods=4).min()


def dse_133_zmijewski_roa_pct_rank_252d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of ROA (netinc/assets) within trailing 252-day distribution."""
    roa = _safe_div(netinc, assets)
    return _rolling_rank_pct(roa, _TD_YEAR)


def dse_134_zmijewski_leverage_pct_rank_252d(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of leverage (liabilities/assets) within trailing 252-day distribution."""
    lev = _safe_div(liabilities, assets)
    return _rolling_rank_pct(lev, _TD_YEAR)


def dse_135_springate_ebit_to_assets_zscore(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of EBIT/assets within trailing 252-day distribution."""
    r = _safe_div(ebit, assets)
    return _zscore_rolling(r, _TD_YEAR)


def dse_136_springate_wc_to_assets_zscore(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
) -> pd.Series:
    """Z-score of working capital / assets within trailing 252-day distribution."""
    wc   = currentassets - currentliabilities
    wcta = _safe_div(wc, assets)
    return _zscore_rolling(wcta, _TD_YEAR)


def dse_137_debt_to_ebitda_ratio(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Debt / EBITDA leverage ratio (structural credit metric; higher = more levered)."""
    return _safe_div(debt, ebitda.clip(lower=_EPS))


def dse_138_debt_to_ebitda_zscore_252d(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of debt/EBITDA within trailing 252-day distribution."""
    r = _safe_div(debt, ebitda.clip(lower=_EPS))
    return _zscore_rolling(r, _TD_YEAR)


def dse_139_debt_to_ebitda_pct_rank_252d(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Percentile rank of debt/EBITDA within trailing 252-day distribution."""
    r = _safe_div(debt, ebitda.clip(lower=_EPS))
    return _rolling_rank_pct(r, _TD_YEAR)


def dse_140_ncfo_to_debt_ratio(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Operating cash flow / total debt (ability to service debt from operations)."""
    return _safe_div(ncfo, debt.clip(lower=_EPS))


def dse_141_ncfo_to_debt_zscore_252d(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of ncfo/debt within trailing 252-day distribution."""
    r = _safe_div(ncfo, debt.clip(lower=_EPS))
    return _zscore_rolling(r, _TD_YEAR)


def dse_142_equity_to_assets_pct_rank_252d(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of equity/assets within trailing 252-day distribution."""
    r = _safe_div(equity, assets)
    return _rolling_rank_pct(r, _TD_YEAR)


def dse_143_retained_earnings_to_assets_pct_rank(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of retearn/assets within trailing 252-day distribution."""
    r = _safe_div(retearn, assets)
    return _rolling_rank_pct(r, _TD_YEAR)


def dse_144_current_ratio_zscore_252d(currentassets: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Z-score of current ratio (currentassets/currentliabilities) within 252-day distribution."""
    cr = _safe_div(currentassets, currentliabilities)
    return _zscore_rolling(cr, _TD_YEAR)


def dse_145_current_ratio_pct_rank_252d(currentassets: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Percentile rank of current ratio within trailing 252-day distribution."""
    cr = _safe_div(currentassets, currentliabilities)
    return _rolling_rank_pct(cr, _TD_YEAR)


def dse_146_equity_erosion_rate_4q(equity: pd.Series) -> pd.Series:
    """Rate of equity erosion: (equity - equity_1yr_ago) / |equity_1yr_ago|."""
    eq_lag = equity.shift(_TD_YEAR)
    return _safe_div(equity - eq_lag, eq_lag.abs().clip(lower=_EPS))


def dse_147_equity_erosion_rate_zscore_252d(equity: pd.Series) -> pd.Series:
    """Z-score of equity erosion rate within trailing 252-day distribution."""
    eq_lag = equity.shift(_TD_YEAR)
    rate   = _safe_div(equity - eq_lag, eq_lag.abs().clip(lower=_EPS))
    return _zscore_rolling(rate, _TD_YEAR)


def dse_148_asset_shrinkage_rate_4q(assets: pd.Series) -> pd.Series:
    """Rate of asset shrinkage: (assets - assets_1yr_ago) / assets_1yr_ago."""
    a_lag = assets.shift(_TD_YEAR)
    return _safe_div(assets - a_lag, a_lag.clip(lower=_EPS))


def dse_149_revenue_decline_rate_4q(revenue: pd.Series) -> pd.Series:
    """Rate of revenue decline: (revenue - revenue_1yr_ago) / revenue_1yr_ago."""
    r_lag = revenue.shift(_TD_YEAR)
    return _safe_div(revenue - r_lag, r_lag.clip(lower=_EPS))


def dse_150_net_debt_to_assets(debt: pd.Series, currentassets: pd.Series, assets: pd.Series) -> pd.Series:
    """Net debt proxy / assets: (debt - currentassets) / assets. Higher = more net leverage."""
    net_debt = debt - currentassets
    return _safe_div(net_debt, assets)


# ── Registry ──────────────────────────────────────────────────────────────────

DISTRESS_SCORE_ENSEMBLE_REGISTRY_076_150 = {
    "dse_076_ohlson_oscore_max_504d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_076_ohlson_oscore_max_504d},
    "dse_077_ohlson_oscore_median_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_077_ohlson_oscore_median_252d},
    "dse_078_ohlson_oscore_vs_252d_max": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_078_ohlson_oscore_vs_252d_max},
    "dse_079_ohlson_oscore_ewm_63d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_079_ohlson_oscore_ewm_63d},
    "dse_080_ohlson_prob_ewm_63d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_080_ohlson_prob_ewm_63d},
    "dse_081_ohlson_prob_max_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_081_ohlson_prob_max_252d},
    "dse_082_ohlson_prob_above50_consec": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_082_ohlson_prob_above50_consec},
    "dse_083_ohlson_oscore_3y_expanding_pct_rank": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_083_ohlson_oscore_3y_expanding_pct_rank},
    "dse_084_ohlson_oscore_2y_zscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_084_ohlson_oscore_2y_zscore},
    "dse_085_ohlson_prob_days_above50_in_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_085_ohlson_prob_days_above50_in_252d},
    "dse_086_zmijewski_score_max_504d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_086_zmijewski_score_max_504d},
    "dse_087_zmijewski_score_median_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_087_zmijewski_score_median_252d},
    "dse_088_zmijewski_score_ewm_63d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_088_zmijewski_score_ewm_63d},
    "dse_089_zmijewski_score_2y_zscore": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_089_zmijewski_score_2y_zscore},
    "dse_090_zmijewski_score_expanding_pct_rank": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_090_zmijewski_score_expanding_pct_rank},
    "dse_091_zmijewski_distress_days_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_091_zmijewski_distress_days_252d},
    "dse_092_zmijewski_score_vs_252d_max": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_092_zmijewski_score_vs_252d_max},
    "dse_093_zmijewski_consec_distress_days": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_093_zmijewski_consec_distress_days},
    "dse_094_zmijewski_roa_rolling_mean_4q": {"inputs": ["netinc", "assets"], "func": dse_094_zmijewski_roa_rolling_mean_4q},
    "dse_095_zmijewski_leverage_rolling_mean_4q": {"inputs": ["liabilities", "assets"], "func": dse_095_zmijewski_leverage_rolling_mean_4q},
    "dse_096_merton_dd_252d_vol": {"inputs": ["debt", "marketcap", "close"], "func": dse_096_merton_dd_252d_vol},
    "dse_097_merton_dd_21d_vol": {"inputs": ["debt", "marketcap", "close"], "func": dse_097_merton_dd_21d_vol},
    "dse_098_merton_dd_expanding_min": {"inputs": ["debt", "marketcap", "close"], "func": dse_098_merton_dd_expanding_min},
    "dse_099_merton_dd_vs_expanding_min": {"inputs": ["debt", "marketcap", "close"], "func": dse_099_merton_dd_vs_expanding_min},
    "dse_100_merton_dd_median_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_100_merton_dd_median_252d},
    "dse_101_merton_dd_ewm_63d": {"inputs": ["debt", "marketcap", "close"], "func": dse_101_merton_dd_ewm_63d},
    "dse_102_merton_dd_below3_days_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_102_merton_dd_below3_days_252d},
    "dse_103_merton_dd_consec_below2": {"inputs": ["debt", "marketcap", "close"], "func": dse_103_merton_dd_consec_below2},
    "dse_104_merton_vol_times_leverage": {"inputs": ["debt", "marketcap", "close"], "func": dse_104_merton_vol_times_leverage},
    "dse_105_merton_dd_2y_zscore": {"inputs": ["debt", "marketcap", "close"], "func": dse_105_merton_dd_2y_zscore},
    "dse_106_springate_score_max_504d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_106_springate_score_max_504d},
    "dse_107_springate_score_median_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_107_springate_score_median_252d},
    "dse_108_springate_score_ewm_63d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_108_springate_score_ewm_63d},
    "dse_109_springate_distress_days_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_109_springate_distress_days_252d},
    "dse_110_springate_expanding_pct_rank": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_110_springate_expanding_pct_rank},
    "dse_111_fulmer_score_pct_rank_252d": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_111_fulmer_score_pct_rank_252d},
    "dse_112_fulmer_score_ewm_63d": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_112_fulmer_score_ewm_63d},
    "dse_113_fulmer_distress_days_252d": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_113_fulmer_distress_days_252d},
    "dse_114_ca_score_max_504d": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_114_ca_score_max_504d},
    "dse_115_ca_score_ewm_63d": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_115_ca_score_ewm_63d},
    "dse_116_ohlson_zmijewski_combined_zscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_116_ohlson_zmijewski_combined_zscore},
    "dse_117_three_model_avg_zscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_117_three_model_avg_zscore},
    "dse_118_ohlson_springate_distress_both_flag": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_118_ohlson_springate_distress_both_flag},
    "dse_119_ohlson_vs_zmijewski_direction": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_119_ohlson_vs_zmijewski_direction},
    "dse_120_ensemble_distress_score_4model_norm": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "equity", "depreciation"], "func": dse_120_ensemble_distress_score_4model_norm},
    "dse_121_ohlson_prob_change_63d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_121_ohlson_prob_change_63d},
    "dse_122_zmijewski_score_change_63d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_122_zmijewski_score_change_63d},
    "dse_123_springate_score_change_63d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_123_springate_score_change_63d},
    "dse_124_merton_dd_change_63d": {"inputs": ["debt", "marketcap", "close"], "func": dse_124_merton_dd_change_63d},
    "dse_125_ensemble_flag_worsened_3models": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_125_ensemble_flag_worsened_3models},
    "dse_126_credit_deterioration_composite": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_126_credit_deterioration_composite},
    "dse_127_ohlson_tlta_trend_4q": {"inputs": ["liabilities", "assets"], "func": dse_127_ohlson_tlta_trend_4q},
    "dse_128_ohlson_nita_trend_4q": {"inputs": ["netinc", "assets"], "func": dse_128_ohlson_nita_trend_4q},
    "dse_129_merton_vol_change_63d": {"inputs": ["close"], "func": dse_129_merton_vol_change_63d},
    "dse_130_merton_leverage_change_63d": {"inputs": ["debt", "marketcap"], "func": dse_130_merton_leverage_change_63d},
    "dse_131_ohlson_wcta_expanding_min": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_131_ohlson_wcta_expanding_min},
    "dse_132_ohlson_futl_expanding_min": {"inputs": ["ncfo", "liabilities"], "func": dse_132_ohlson_futl_expanding_min},
    "dse_133_zmijewski_roa_pct_rank_252d": {"inputs": ["netinc", "assets"], "func": dse_133_zmijewski_roa_pct_rank_252d},
    "dse_134_zmijewski_leverage_pct_rank_252d": {"inputs": ["liabilities", "assets"], "func": dse_134_zmijewski_leverage_pct_rank_252d},
    "dse_135_springate_ebit_to_assets_zscore": {"inputs": ["ebit", "assets"], "func": dse_135_springate_ebit_to_assets_zscore},
    "dse_136_springate_wc_to_assets_zscore": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_136_springate_wc_to_assets_zscore},
    "dse_137_debt_to_ebitda_ratio": {"inputs": ["debt", "ebitda"], "func": dse_137_debt_to_ebitda_ratio},
    "dse_138_debt_to_ebitda_zscore_252d": {"inputs": ["debt", "ebitda"], "func": dse_138_debt_to_ebitda_zscore_252d},
    "dse_139_debt_to_ebitda_pct_rank_252d": {"inputs": ["debt", "ebitda"], "func": dse_139_debt_to_ebitda_pct_rank_252d},
    "dse_140_ncfo_to_debt_ratio": {"inputs": ["ncfo", "debt"], "func": dse_140_ncfo_to_debt_ratio},
    "dse_141_ncfo_to_debt_zscore_252d": {"inputs": ["ncfo", "debt"], "func": dse_141_ncfo_to_debt_zscore_252d},
    "dse_142_equity_to_assets_pct_rank_252d": {"inputs": ["equity", "assets"], "func": dse_142_equity_to_assets_pct_rank_252d},
    "dse_143_retained_earnings_to_assets_pct_rank": {"inputs": ["retearn", "assets"], "func": dse_143_retained_earnings_to_assets_pct_rank},
    "dse_144_current_ratio_zscore_252d": {"inputs": ["currentassets", "currentliabilities"], "func": dse_144_current_ratio_zscore_252d},
    "dse_145_current_ratio_pct_rank_252d": {"inputs": ["currentassets", "currentliabilities"], "func": dse_145_current_ratio_pct_rank_252d},
    "dse_146_equity_erosion_rate_4q": {"inputs": ["equity"], "func": dse_146_equity_erosion_rate_4q},
    "dse_147_equity_erosion_rate_zscore_252d": {"inputs": ["equity"], "func": dse_147_equity_erosion_rate_zscore_252d},
    "dse_148_asset_shrinkage_rate_4q": {"inputs": ["assets"], "func": dse_148_asset_shrinkage_rate_4q},
    "dse_149_revenue_decline_rate_4q": {"inputs": ["revenue"], "func": dse_149_revenue_decline_rate_4q},
    "dse_150_net_debt_to_assets": {"inputs": ["debt", "currentassets", "assets"], "func": dse_150_net_debt_to_assets},
}
