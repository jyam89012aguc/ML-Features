"""
121_distress_score_ensemble — Extended Features 001-075
Domain: ensemble distress scores — additional sub-components, cross-model variants,
        structural credit stress indicators, multi-period comparisons, and hybrid composites.
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


# ── Core score helpers ─────────────────────────────────────────────────────────

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


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Ohlson component cross-windows and extreme flags ---

def dse_ext_001_ohlson_wcta_zscore_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
) -> pd.Series:
    """Z-score of Ohlson WCTA (workingcapital/assets) within 252-day distribution."""
    wc   = currentassets - currentliabilities
    wcta = _safe_div(wc, assets)
    return _zscore_rolling(wcta, _TD_YEAR)


def dse_ext_002_ohlson_clca_zscore_252d(
    currentliabilities: pd.Series,
    currentassets: pd.Series,
) -> pd.Series:
    """Z-score of Ohlson CLCA (currentliab/currentassets) within 252-day distribution."""
    clca = _safe_div(currentliabilities, currentassets)
    return _zscore_rolling(clca, _TD_YEAR)


def dse_ext_003_ohlson_chin_zscore_252d(netinc: pd.Series) -> pd.Series:
    """Z-score of Ohlson CHIN (earnings change ratio) within 252-day distribution."""
    ni_prev = netinc.shift(_TD_QTR)
    chin = _safe_div(netinc - ni_prev, netinc.abs() + ni_prev.abs())
    return _zscore_rolling(chin, _TD_YEAR)


def dse_ext_004_ohlson_futl_zscore_252d(ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Z-score of Ohlson FUTL (ncfo/liabilities) within 252-day distribution."""
    futl = _safe_div(ncfo, liabilities)
    return _zscore_rolling(futl, _TD_YEAR)


def dse_ext_005_ohlson_tlta_zscore_252d(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of Ohlson TLTA (liabilities/assets) within 252-day distribution."""
    tlta = _safe_div(liabilities, assets)
    return _zscore_rolling(tlta, _TD_YEAR)


def dse_ext_006_ohlson_prob_median_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Trailing 252-day median of Ohlson bankruptcy probability."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _rolling_median(prob, _TD_YEAR)


def dse_ext_007_ohlson_prob_ewm_21d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=21) Ohlson bankruptcy probability — fast trend."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _ewm_mean(prob, 21)


def dse_ext_008_ohlson_prob_above75_flag(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Binary: 1 if Ohlson bankruptcy probability > 0.75 (severe distress)."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return (prob > 0.75).astype(float)


def dse_ext_009_ohlson_prob_days_above75_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where Ohlson prob > 0.75 (severe distress duration)."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    flag = (prob > 0.75).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def dse_ext_010_ohlson_oscore_pct_rank_504d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Percentile rank of Ohlson O-score within trailing 504-day (2-year) distribution."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _rolling_rank_pct(o, _TD_2Y)


# --- Group B (011-020): Zmijewski extended variants ---

def dse_ext_011_zmijewski_score_pct_rank_504d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Zmijewski score within trailing 504-day (2-year) distribution."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _rolling_rank_pct(zm, _TD_2Y)


def dse_ext_012_zmijewski_score_ewm_21d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=21) Zmijewski score — fast trend."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _ewm_mean(zm, 21)


def dse_ext_013_zmijewski_distress_frac_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Fraction of trailing 252 days where Zmijewski score > 0 (distress prevalence)."""
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    flag = (zm > 0).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def dse_ext_014_zmijewski_cacl_pct_rank_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Zmijewski CACL (currentassets/currentliab) within 252-day distribution."""
    cacl = _safe_div(currentassets, currentliabilities)
    return _rolling_rank_pct(cacl, _TD_YEAR)


def dse_ext_015_zmijewski_score_vs_expanding_max(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Zmijewski score minus its all-time expanding maximum (distance from worst ever)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm - zm.expanding(min_periods=4).max()


def dse_ext_016_zmijewski_roa_expanding_min(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Expanding all-time minimum of ROA (worst profitability ever, Zmijewski context)."""
    roa = _safe_div(netinc, assets)
    return roa.expanding(min_periods=4).min()


def dse_ext_017_zmijewski_leverage_expanding_max(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Expanding all-time maximum of leverage (liabilities/assets) (worst ever Zmijewski leverage)."""
    lev = _safe_div(liabilities, assets)
    return lev.expanding(min_periods=4).max()


def dse_ext_018_zmijewski_score_vs_504d_median(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Zmijewski score minus its 504-day median (deviation from 2-year normal level)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm - _rolling_median(zm, _TD_2Y)


def dse_ext_019_zmijewski_score_above0_consec(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Consecutive days Zmijewski score > 0 (prolonged distress streak)."""
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    cond = zm > 0
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_ext_020_zmijewski_roa_3y_zscore(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of ROA within trailing 756-day (3-year) distribution (long-horizon context)."""
    roa = _safe_div(netinc, assets)
    return _zscore_rolling(roa, _TD_3Y)


# --- Group C (021-030): Springate extended variants ---

def dse_ext_021_springate_score_pct_rank_504d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Percentile rank of Springate score within trailing 504-day (2-year) distribution."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _rolling_rank_pct(s, _TD_2Y)


def dse_ext_022_springate_score_ewm_21d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """EWM-smoothed (span=21) Springate score — fast trend."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _ewm_mean(s, 21)


def dse_ext_023_springate_distress_frac_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Fraction of trailing 252 days where Springate score < 0.862 (distress prevalence)."""
    s    = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    flag = (s < 0.862).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def dse_ext_024_springate_score_vs_expanding_min(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Springate score minus its all-time expanding minimum (distance from worst ever)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return s - s.expanding(min_periods=4).min()


def dse_ext_025_springate_c_ratio_zscore_252d(ebit: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Z-score of Springate C ratio (EBIT/currentliabilities) within 252-day distribution."""
    c = _safe_div(ebit, currentliabilities)
    return _zscore_rolling(c, _TD_YEAR)


def dse_ext_026_springate_d_ratio_zscore_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of Springate D ratio (revenue/assets) within 252-day distribution."""
    d = _safe_div(revenue, assets)
    return _zscore_rolling(d, _TD_YEAR)


def dse_ext_027_springate_score_3y_zscore(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Z-score of Springate score within trailing 756-day (3-year) distribution."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _zscore_rolling(s, _TD_3Y)


def dse_ext_028_springate_below0_flag(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if Springate score < 0 (severe distress well below 0.862 threshold)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return (s < 0.0).astype(float)


def dse_ext_029_springate_score_vs_504d_median(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Springate score minus its 504-day median (deviation from 2-year normal)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return s - _rolling_median(s, _TD_2Y)


def dse_ext_030_springate_consec_distress_days(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Consecutive days Springate score < 0.862 (prolonged distress streak)."""
    s    = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    cond = s < 0.862
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# --- Group D (031-040): Merton DD extended variants ---

def dse_ext_031_merton_dd_pct_rank_504d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Merton DD proxy within trailing 504-day (2-year) distribution."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _rolling_rank_pct(dd, _TD_2Y)


def dse_ext_032_merton_dd_expanding_pct_rank(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of Merton DD proxy."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd.expanding(min_periods=4).rank(pct=True)


def dse_ext_033_merton_dd_vs_504d_median(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton DD minus its 504-day median (deviation from 2-year normal)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd - _rolling_median(dd, _TD_2Y)


def dse_ext_034_merton_vol_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of annualized equity vol within trailing 252-day distribution."""
    vol = _vol_annual(close, _TD_QTR)
    return _rolling_rank_pct(vol, _TD_YEAR)


def dse_ext_035_merton_vol_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of annualized equity volatility (worst vol ever seen)."""
    vol = _vol_annual(close, _TD_QTR)
    return vol.expanding(min_periods=4).max()


def dse_ext_036_merton_leverage_pct_rank_252d(debt: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Percentile rank of Merton leverage ratio (debt/marketcap) within 252-day distribution."""
    lev = _safe_div(debt, marketcap.clip(lower=_EPS))
    return _rolling_rank_pct(lev, _TD_YEAR)


def dse_ext_037_merton_vol_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of annualized equity volatility within trailing 252-day distribution."""
    vol = _vol_annual(close, _TD_QTR)
    return _zscore_rolling(vol, _TD_YEAR)


def dse_ext_038_merton_dd_below3_frac_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where Merton DD < 3.0 (near-default prevalence)."""
    dd   = _merton_dd(debt, marketcap, close, _TD_QTR)
    flag = (dd < 3.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def dse_ext_039_merton_dd_3y_zscore(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Merton DD proxy within trailing 756-day (3-year) distribution."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _zscore_rolling(dd, _TD_3Y)


def dse_ext_040_merton_implied_default_prob(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """
    Merton implied default probability proxy: standard normal CDF of -DD.
    Uses logistic approximation: 1/(1+exp(1.7*DD)) as CDF(-DD) proxy.
    Higher = more likely to default per structural model.
    """
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return 1.0 / (1.0 + np.exp(1.7 * dd))


# --- Group E (041-055): Hybrid cross-model composites and stress indices ---

def dse_ext_041_ohlson_merton_combined_score(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    debt: pd.Series,
    marketcap: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Hybrid: z-scored Ohlson + z-scored inverted Merton DD.
    Combines accounting-based logit with structural credit model.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _zscore_rolling(o, _TD_YEAR).fillna(0) + _zscore_rolling(-dd, _TD_YEAR).fillna(0)


def dse_ext_042_zmijewski_merton_combined_score(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    debt: pd.Series,
    marketcap: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """Hybrid: z-scored Zmijewski + z-scored inverted Merton DD."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _zscore_rolling(zm, _TD_YEAR).fillna(0) + _zscore_rolling(-dd, _TD_YEAR).fillna(0)


def dse_ext_043_four_model_pct_rank_ensemble(
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
    4-model ensemble: average of pct-ranks of Ohlson, Zmijewski, 1-Springate, 1-Merton-DD_pct.
    Score in [0,1]; higher = more distress.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    o_pct  = _rolling_rank_pct(o,  _TD_YEAR).fillna(0.5)
    zm_pct = _rolling_rank_pct(zm, _TD_YEAR).fillna(0.5)
    sp_pct = 1.0 - _rolling_rank_pct(sp, _TD_YEAR).fillna(0.5)
    dd_pct = 1.0 - _rolling_rank_pct(dd, _TD_YEAR).fillna(0.5)
    return (o_pct + zm_pct + sp_pct + dd_pct) / 4.0


def dse_ext_044_all4_distress_flag(
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
    """Binary: 1 if all 4 models (Ohlson, Zmijewski, Springate, Merton DD < 2) flag distress."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp   = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd   = _merton_dd(debt, marketcap, close, _TD_QTR)
    return ((prob > 0.5) & (zm > 0) & (sp < 0.862) & (dd < 2.0)).astype(float)


def dse_ext_045_distress_composite_severity(
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
    Composite distress severity: sum of z-scores with consistent polarity.
    z(Ohlson) + z(Zmijewski) + z(-Springate) + z(-MertonDD).
    Higher = more severe distress from multiple models simultaneously.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return (_zscore_rolling(o,   _TD_YEAR).fillna(0)
            + _zscore_rolling(zm,  _TD_YEAR).fillna(0)
            + _zscore_rolling(-sp, _TD_YEAR).fillna(0)
            + _zscore_rolling(-dd, _TD_YEAR).fillna(0))


def dse_ext_046_distress_composite_severity_pct_rank_252d(
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
    """Percentile rank of 4-model composite distress severity within trailing 252-day window."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    composite = (_zscore_rolling(o,   _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm,  _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-dd, _TD_YEAR).fillna(0))
    return _rolling_rank_pct(composite, _TD_YEAR)


def dse_ext_047_distress_composite_severity_max_252d(
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
    """Trailing 252-day maximum of 4-model composite distress severity."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    composite = (_zscore_rolling(o,   _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm,  _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-dd, _TD_YEAR).fillna(0))
    return _rolling_max(composite, _TD_YEAR)


def dse_ext_048_ohlson_merton_flag_both(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    debt: pd.Series,
    marketcap: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """Binary: 1 if Ohlson prob > 0.5 AND Merton DD < 2.0 simultaneously."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    dd   = _merton_dd(debt, marketcap, close, _TD_QTR)
    return ((prob > 0.5) & (dd < 2.0)).astype(float)


def dse_ext_049_zmijewski_springate_flag_both(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if both Zmijewski > 0 AND Springate < 0.862 simultaneously."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return ((zm > 0) & (sp < 0.862)).astype(float)


def dse_ext_050_distress_score_flag_count_in_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Count of days in trailing 252d where at least 2 of 3 models flag distress."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    zm   = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp   = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    multi_flag = (((prob > 0.5).astype(float)
                   + (zm > 0).astype(float)
                   + (sp < 0.862).astype(float)) >= 2).astype(float)
    return _rolling_sum(multi_flag, _TD_YEAR)


# --- Group F (051-065): Structural credit stress ratio proxies ---

def dse_ext_051_interest_burden_proxy(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """Interest burden proxy: netinc / ebit (lower = higher interest expense relative to EBIT)."""
    return _safe_div(netinc, ebit.replace(0, np.nan))


def dse_ext_052_interest_burden_zscore_252d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """Z-score of interest burden proxy within 252-day distribution."""
    r = _safe_div(netinc, ebit.replace(0, np.nan))
    return _zscore_rolling(r, _TD_YEAR)


def dse_ext_053_debt_capacity_ratio(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Debt capacity ratio: ncfo / debt (capacity to service debt from operations)."""
    return _safe_div(ncfo, debt.clip(lower=_EPS))


def dse_ext_054_debt_capacity_pct_rank_252d(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Percentile rank of debt capacity (ncfo/debt) within 252-day distribution."""
    r = _safe_div(ncfo, debt.clip(lower=_EPS))
    return _rolling_rank_pct(r, _TD_YEAR)


def dse_ext_055_equity_cushion_ratio(equity: pd.Series, debt: pd.Series) -> pd.Series:
    """Equity cushion: equity / debt (buffer above debt; negative = insolvent)."""
    return _safe_div(equity, debt.clip(lower=_EPS))


def dse_ext_056_equity_cushion_zscore_252d(equity: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of equity cushion (equity/debt) within 252-day distribution."""
    r = _safe_div(equity, debt.clip(lower=_EPS))
    return _zscore_rolling(r, _TD_YEAR)


def dse_ext_057_negative_equity_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if book equity < 0 (technical insolvency)."""
    return (equity < 0).astype(float)


def dse_ext_058_negative_retearn_flag(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retained earnings < 0 (accumulated deficit)."""
    return (retearn < 0).astype(float)


def dse_ext_059_negative_ncfo_flag(ncfo: pd.Series) -> pd.Series:
    """Binary: 1 if operating cash flow < 0 (cash burn from operations)."""
    return (ncfo < 0).astype(float)


def dse_ext_060_consecutive_negative_ncfo(ncfo: pd.Series) -> pd.Series:
    """Consecutive quarters (as daily count) of negative operating cash flow."""
    cond = ncfo < 0
    c    = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_ext_061_liabilities_to_equity_zscore_252d(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of liabilities/equity within 252-day distribution (book leverage stress)."""
    r = _safe_div(liabilities, equity.replace(0, np.nan))
    return _zscore_rolling(r, _TD_YEAR)


def dse_ext_062_asset_coverage_ratio(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Asset coverage: assets / liabilities (higher = more cushion over obligations)."""
    return _safe_div(assets, liabilities.clip(lower=_EPS))


def dse_ext_063_asset_coverage_pct_rank_252d(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Percentile rank of asset coverage ratio within 252-day distribution."""
    r = _safe_div(assets, liabilities.clip(lower=_EPS))
    return _rolling_rank_pct(r, _TD_YEAR)


def dse_ext_064_ebitda_to_assets_zscore_252d(ebitda: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of EBITDA/assets within 252-day distribution (cash generation per asset)."""
    r = _safe_div(ebitda, assets)
    return _zscore_rolling(r, _TD_YEAR)


def dse_ext_065_fcf_to_assets_zscore_252d(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of free cash flow / assets within 252-day distribution."""
    r = _safe_div(fcf, assets)
    return _zscore_rolling(r, _TD_YEAR)


# --- Group G (066-075): Long-horizon history, expanding windows, final composites ---

def dse_ext_066_ohlson_prob_3y_zscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Z-score of Ohlson bankruptcy probability within trailing 756-day (3-year) distribution."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _zscore_rolling(prob, _TD_3Y)


def dse_ext_067_zmijewski_score_3y_zscore(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Z-score of Zmijewski score within trailing 756-day (3-year) distribution."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _zscore_rolling(zm, _TD_3Y)


def dse_ext_068_merton_dd_expanding_zscore(
    debt: pd.Series, marketcap: pd.Series, close: pd.Series,
) -> pd.Series:
    """Expanding all-time z-score of Merton DD proxy (standardized against full history)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    m  = dd.expanding(min_periods=4).mean()
    s  = dd.expanding(min_periods=4).std()
    return _safe_div(dd - m, s)


def dse_ext_069_ohlson_oscore_expanding_zscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Expanding all-time z-score of Ohlson O-score."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    m = o.expanding(min_periods=4).mean()
    s = o.expanding(min_periods=4).std()
    return _safe_div(o - m, s)


def dse_ext_070_zmijewski_score_expanding_zscore(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Expanding all-time z-score of Zmijewski score."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    m  = zm.expanding(min_periods=4).mean()
    s  = zm.expanding(min_periods=4).std()
    return _safe_div(zm - m, s)


def dse_ext_071_springate_score_expanding_zscore(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Expanding all-time z-score of Springate score."""
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    m  = sp.expanding(min_periods=4).mean()
    s  = sp.expanding(min_periods=4).std()
    return _safe_div(sp - m, s)


def dse_ext_072_distress_composite_ewm_126d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """EWM (span=126) of 3-model z-score composite (slow-trend distress ensemble)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    composite = (_zscore_rolling(o, _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)) / 3.0
    return _ewm_mean(composite, 126)


def dse_ext_073_distress_composite_consec_high_days(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Consecutive days 3-model composite z-score > 1.0 (sustained multi-model distress streak)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    composite = (_zscore_rolling(o, _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)) / 3.0
    cond  = composite > 1.0
    c     = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dse_ext_074_net_working_capital_to_revenue(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Net working capital / revenue (liquidity relative to top-line size)."""
    wc = currentassets - currentliabilities
    return _safe_div(wc, revenue.clip(lower=_EPS))


def dse_ext_075_distress_score_ensemble_capitulation_index(
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
    Distress Score Ensemble Capitulation Index — final composite signal.
    Percentile rank of the 4-model composite severity score within trailing 252 days.
    Inputs: Ohlson, Zmijewski, Springate, Merton DD; all z-scored and averaged.
    Score near 1.0 = near worst-ever multi-model distress reading.
    """
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    composite = (_zscore_rolling(o,   _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm,  _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-dd, _TD_YEAR).fillna(0))
    return _rolling_rank_pct(composite, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

DISTRESS_SCORE_ENSEMBLE_EXTENDED_REGISTRY_001_075 = {
    "dse_ext_001_ohlson_wcta_zscore_252d": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_ext_001_ohlson_wcta_zscore_252d},
    "dse_ext_002_ohlson_clca_zscore_252d": {"inputs": ["currentliabilities", "currentassets"], "func": dse_ext_002_ohlson_clca_zscore_252d},
    "dse_ext_003_ohlson_chin_zscore_252d": {"inputs": ["netinc"], "func": dse_ext_003_ohlson_chin_zscore_252d},
    "dse_ext_004_ohlson_futl_zscore_252d": {"inputs": ["ncfo", "liabilities"], "func": dse_ext_004_ohlson_futl_zscore_252d},
    "dse_ext_005_ohlson_tlta_zscore_252d": {"inputs": ["liabilities", "assets"], "func": dse_ext_005_ohlson_tlta_zscore_252d},
    "dse_ext_006_ohlson_prob_median_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_006_ohlson_prob_median_252d},
    "dse_ext_007_ohlson_prob_ewm_21d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_007_ohlson_prob_ewm_21d},
    "dse_ext_008_ohlson_prob_above75_flag": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_008_ohlson_prob_above75_flag},
    "dse_ext_009_ohlson_prob_days_above75_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_009_ohlson_prob_days_above75_252d},
    "dse_ext_010_ohlson_oscore_pct_rank_504d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_010_ohlson_oscore_pct_rank_504d},
    "dse_ext_011_zmijewski_score_pct_rank_504d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_011_zmijewski_score_pct_rank_504d},
    "dse_ext_012_zmijewski_score_ewm_21d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_012_zmijewski_score_ewm_21d},
    "dse_ext_013_zmijewski_distress_frac_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_013_zmijewski_distress_frac_252d},
    "dse_ext_014_zmijewski_cacl_pct_rank_252d": {"inputs": ["currentassets", "currentliabilities"], "func": dse_ext_014_zmijewski_cacl_pct_rank_252d},
    "dse_ext_015_zmijewski_score_vs_expanding_max": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_015_zmijewski_score_vs_expanding_max},
    "dse_ext_016_zmijewski_roa_expanding_min": {"inputs": ["netinc", "assets"], "func": dse_ext_016_zmijewski_roa_expanding_min},
    "dse_ext_017_zmijewski_leverage_expanding_max": {"inputs": ["liabilities", "assets"], "func": dse_ext_017_zmijewski_leverage_expanding_max},
    "dse_ext_018_zmijewski_score_vs_504d_median": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_018_zmijewski_score_vs_504d_median},
    "dse_ext_019_zmijewski_score_above0_consec": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_019_zmijewski_score_above0_consec},
    "dse_ext_020_zmijewski_roa_3y_zscore": {"inputs": ["netinc", "assets"], "func": dse_ext_020_zmijewski_roa_3y_zscore},
    "dse_ext_021_springate_score_pct_rank_504d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_021_springate_score_pct_rank_504d},
    "dse_ext_022_springate_score_ewm_21d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_022_springate_score_ewm_21d},
    "dse_ext_023_springate_distress_frac_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_023_springate_distress_frac_252d},
    "dse_ext_024_springate_score_vs_expanding_min": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_024_springate_score_vs_expanding_min},
    "dse_ext_025_springate_c_ratio_zscore_252d": {"inputs": ["ebit", "currentliabilities"], "func": dse_ext_025_springate_c_ratio_zscore_252d},
    "dse_ext_026_springate_d_ratio_zscore_252d": {"inputs": ["revenue", "assets"], "func": dse_ext_026_springate_d_ratio_zscore_252d},
    "dse_ext_027_springate_score_3y_zscore": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_027_springate_score_3y_zscore},
    "dse_ext_028_springate_below0_flag": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_028_springate_below0_flag},
    "dse_ext_029_springate_score_vs_504d_median": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_029_springate_score_vs_504d_median},
    "dse_ext_030_springate_consec_distress_days": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_030_springate_consec_distress_days},
    "dse_ext_031_merton_dd_pct_rank_504d": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_031_merton_dd_pct_rank_504d},
    "dse_ext_032_merton_dd_expanding_pct_rank": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_032_merton_dd_expanding_pct_rank},
    "dse_ext_033_merton_dd_vs_504d_median": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_033_merton_dd_vs_504d_median},
    "dse_ext_034_merton_vol_pct_rank_252d": {"inputs": ["close"], "func": dse_ext_034_merton_vol_pct_rank_252d},
    "dse_ext_035_merton_vol_expanding_max": {"inputs": ["close"], "func": dse_ext_035_merton_vol_expanding_max},
    "dse_ext_036_merton_leverage_pct_rank_252d": {"inputs": ["debt", "marketcap"], "func": dse_ext_036_merton_leverage_pct_rank_252d},
    "dse_ext_037_merton_vol_zscore_252d": {"inputs": ["close"], "func": dse_ext_037_merton_vol_zscore_252d},
    "dse_ext_038_merton_dd_below3_frac_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_038_merton_dd_below3_frac_252d},
    "dse_ext_039_merton_dd_3y_zscore": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_039_merton_dd_3y_zscore},
    "dse_ext_040_merton_implied_default_prob": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_040_merton_implied_default_prob},
    "dse_ext_041_ohlson_merton_combined_score": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "debt", "marketcap", "close"], "func": dse_ext_041_ohlson_merton_combined_score},
    "dse_ext_042_zmijewski_merton_combined_score": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities", "debt", "marketcap", "close"], "func": dse_ext_042_zmijewski_merton_combined_score},
    "dse_ext_043_four_model_pct_rank_ensemble": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_043_four_model_pct_rank_ensemble},
    "dse_ext_044_all4_distress_flag": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_044_all4_distress_flag},
    "dse_ext_045_distress_composite_severity": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_045_distress_composite_severity},
    "dse_ext_046_distress_composite_severity_pct_rank_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_046_distress_composite_severity_pct_rank_252d},
    "dse_ext_047_distress_composite_severity_max_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_047_distress_composite_severity_max_252d},
    "dse_ext_048_ohlson_merton_flag_both": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "debt", "marketcap", "close"], "func": dse_ext_048_ohlson_merton_flag_both},
    "dse_ext_049_zmijewski_springate_flag_both": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities", "ebit", "revenue"], "func": dse_ext_049_zmijewski_springate_flag_both},
    "dse_ext_050_distress_score_flag_count_in_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_ext_050_distress_score_flag_count_in_252d},
    "dse_ext_051_interest_burden_proxy": {"inputs": ["ebit", "netinc"], "func": dse_ext_051_interest_burden_proxy},
    "dse_ext_052_interest_burden_zscore_252d": {"inputs": ["ebit", "netinc"], "func": dse_ext_052_interest_burden_zscore_252d},
    "dse_ext_053_debt_capacity_ratio": {"inputs": ["ncfo", "debt"], "func": dse_ext_053_debt_capacity_ratio},
    "dse_ext_054_debt_capacity_pct_rank_252d": {"inputs": ["ncfo", "debt"], "func": dse_ext_054_debt_capacity_pct_rank_252d},
    "dse_ext_055_equity_cushion_ratio": {"inputs": ["equity", "debt"], "func": dse_ext_055_equity_cushion_ratio},
    "dse_ext_056_equity_cushion_zscore_252d": {"inputs": ["equity", "debt"], "func": dse_ext_056_equity_cushion_zscore_252d},
    "dse_ext_057_negative_equity_flag": {"inputs": ["equity"], "func": dse_ext_057_negative_equity_flag},
    "dse_ext_058_negative_retearn_flag": {"inputs": ["retearn"], "func": dse_ext_058_negative_retearn_flag},
    "dse_ext_059_negative_ncfo_flag": {"inputs": ["ncfo"], "func": dse_ext_059_negative_ncfo_flag},
    "dse_ext_060_consecutive_negative_ncfo": {"inputs": ["ncfo"], "func": dse_ext_060_consecutive_negative_ncfo},
    "dse_ext_061_liabilities_to_equity_zscore_252d": {"inputs": ["liabilities", "equity"], "func": dse_ext_061_liabilities_to_equity_zscore_252d},
    "dse_ext_062_asset_coverage_ratio": {"inputs": ["assets", "liabilities"], "func": dse_ext_062_asset_coverage_ratio},
    "dse_ext_063_asset_coverage_pct_rank_252d": {"inputs": ["assets", "liabilities"], "func": dse_ext_063_asset_coverage_pct_rank_252d},
    "dse_ext_064_ebitda_to_assets_zscore_252d": {"inputs": ["ebitda", "assets"], "func": dse_ext_064_ebitda_to_assets_zscore_252d},
    "dse_ext_065_fcf_to_assets_zscore_252d": {"inputs": ["fcf", "assets"], "func": dse_ext_065_fcf_to_assets_zscore_252d},
    "dse_ext_066_ohlson_prob_3y_zscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_066_ohlson_prob_3y_zscore},
    "dse_ext_067_zmijewski_score_3y_zscore": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_067_zmijewski_score_3y_zscore},
    "dse_ext_068_merton_dd_expanding_zscore": {"inputs": ["debt", "marketcap", "close"], "func": dse_ext_068_merton_dd_expanding_zscore},
    "dse_ext_069_ohlson_oscore_expanding_zscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_ext_069_ohlson_oscore_expanding_zscore},
    "dse_ext_070_zmijewski_score_expanding_zscore": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_ext_070_zmijewski_score_expanding_zscore},
    "dse_ext_071_springate_score_expanding_zscore": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_ext_071_springate_score_expanding_zscore},
    "dse_ext_072_distress_composite_ewm_126d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_ext_072_distress_composite_ewm_126d},
    "dse_ext_073_distress_composite_consec_high_days": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_ext_073_distress_composite_consec_high_days},
    "dse_ext_074_net_working_capital_to_revenue": {"inputs": ["currentassets", "currentliabilities", "revenue"], "func": dse_ext_074_net_working_capital_to_revenue},
    "dse_ext_075_distress_score_ensemble_capitulation_index": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "debt", "marketcap", "close"], "func": dse_ext_075_distress_score_ensemble_capitulation_index},
}
