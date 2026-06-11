"""
121_distress_score_ensemble — Base Features 001-075
Domain: ensemble of academic bankruptcy / distress scores beyond Altman-Z and Piotroski:
        Ohlson O-score, Zmijewski score, Merton distance-to-default proxy,
        Springate, Fulmer, CA-Score, component sub-scores, and normalized variants.
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Ohlson O-score components ---
# Ohlson (1980) logit model for bankruptcy probability
# O = -1.32 - 0.407*SIZE + 6.03*TLTA - 1.43*WCTA + 0.076*CLCA
#     - 1.72*OENEG - 2.37*NITA - 1.83*FUTL + 0.285*INTWO - 0.521*CHIN
# OENEG=1 if total liabilities > total assets; INTWO=1 if net loss in 2 prior yrs;
# CHIN=(NI_t-NI_{t-1})/(|NI_t|+|NI_{t-1}|)

def dse_001_ohlson_size(assets: pd.Series) -> pd.Series:
    """Ohlson SIZE component: log(total assets). Core O-score input."""
    return np.log(assets.clip(lower=_EPS))


def dse_002_ohlson_tlta(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson TLTA: total liabilities / total assets (leverage ratio in O-score)."""
    return _safe_div(liabilities, assets)


def dse_003_ohlson_wcta(currentassets: pd.Series, currentliabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson WCTA: working capital / total assets (liquidity in O-score)."""
    wc = currentassets - currentliabilities
    return _safe_div(wc, assets)


def dse_004_ohlson_clca(currentliabilities: pd.Series, currentassets: pd.Series) -> pd.Series:
    """Ohlson CLCA: current liabilities / current assets (short-term stress in O-score)."""
    return _safe_div(currentliabilities, currentassets)


def dse_005_ohlson_oeneg(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson OENEG flag: 1 if total liabilities > total assets (negative equity proxy)."""
    return (liabilities > assets).astype(float)


def dse_006_ohlson_nita(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson NITA: net income / total assets (profitability in O-score)."""
    return _safe_div(netinc, assets)


def dse_007_ohlson_futl(ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Ohlson FUTL: funds from operations (ncfo) / total liabilities (cash coverage)."""
    return _safe_div(ncfo, liabilities)


def dse_008_ohlson_intwo(netinc: pd.Series) -> pd.Series:
    """Ohlson INTWO: 1 if net income < 0 in current AND prior quarter (two-year loss)."""
    loss_now  = (netinc < 0).astype(float)
    loss_prev = (netinc.shift(_TD_QTR) < 0).astype(float)
    return (loss_now * loss_prev)


def dse_009_ohlson_chin(netinc: pd.Series) -> pd.Series:
    """Ohlson CHIN: (NI_t - NI_{t-1}) / (|NI_t| + |NI_{t-1}|) — earnings momentum."""
    ni_prev = netinc.shift(_TD_QTR)
    num = netinc - ni_prev
    den = netinc.abs() + ni_prev.abs()
    return _safe_div(num, den)


def dse_010_ohlson_oscore(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """
    Assembled Ohlson O-score (logit index, NOT converted to probability).
    O = -1.32 - 0.407*SIZE + 6.03*TLTA - 1.43*WCTA + 0.076*CLCA
        - 1.72*OENEG - 2.37*NITA - 1.83*FUTL + 0.285*INTWO - 0.521*CHIN
    Higher O-score = higher probability of bankruptcy.
    """
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
    chin_num = netinc - ni_prev
    chin_den = netinc.abs() + ni_prev.abs()
    chin  = _safe_div(chin_num, chin_den).fillna(0)
    return (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
            + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
            - 1.83 * futl + 0.285 * intwo - 0.521 * chin)


def dse_011_ohlson_bankruptcy_prob(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Ohlson O-score converted to bankruptcy probability via logistic function."""
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
    chin_num = netinc - ni_prev
    chin_den = netinc.abs() + ni_prev.abs()
    chin  = _safe_div(chin_num, chin_den).fillna(0)
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
         + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
         - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    return 1.0 / (1.0 + np.exp(-o))


def dse_012_ohlson_distress_flag(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Binary: 1 if Ohlson bankruptcy probability > 0.5 (distress threshold)."""
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
    chin_num = netinc - ni_prev
    chin_den = netinc.abs() + ni_prev.abs()
    chin  = _safe_div(chin_num, chin_den).fillna(0)
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
         + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
         - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    prob = 1.0 / (1.0 + np.exp(-o))
    return (prob > 0.5).astype(float)


# --- Group B (013-022): Zmijewski score components ---
# Zmijewski (1984) probit model
# ZM = -4.336 - 4.513*ROA + 5.679*TLTA + 0.004*CACL
# ROA = netinc/assets; TLTA = liabilities/assets; CACL = currentassets/currentliabilities

def dse_013_zmijewski_roa(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski ROA component: net income / total assets."""
    return _safe_div(netinc, assets)


def dse_014_zmijewski_tlta(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski leverage component: total liabilities / total assets."""
    return _safe_div(liabilities, assets)


def dse_015_zmijewski_cacl(currentassets: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Zmijewski liquidity component: current assets / current liabilities."""
    return _safe_div(currentassets, currentliabilities)


def dse_016_zmijewski_score(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """
    Assembled Zmijewski score (probit index, NOT converted to probability).
    ZM = -4.336 - 4.513*ROA + 5.679*TLTA + 0.004*CACL
    Higher score = higher distress probability.
    """
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    return -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl


def dse_017_zmijewski_distress_flag(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Binary: 1 if Zmijewski score > 0 (distress zone per probit threshold)."""
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    return (zm > 0).astype(float)


def dse_018_zmijewski_roa_weighted(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski ROA weighted contribution: -4.513 * (netinc/assets)."""
    return -4.513 * _safe_div(netinc, assets).fillna(0)


def dse_019_zmijewski_leverage_weighted(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski leverage weighted contribution: 5.679 * (liabilities/assets)."""
    return 5.679 * _safe_div(liabilities, assets).fillna(0)


def dse_020_zmijewski_liquidity_weighted(currentassets: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Zmijewski liquidity weighted contribution: 0.004 * (currentassets/currentliabilities)."""
    return 0.004 * _safe_div(currentassets, currentliabilities).fillna(0)


def dse_021_zmijewski_score_zscore_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Z-score of Zmijewski score relative to its trailing 252-day distribution."""
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    return _zscore_rolling(zm, _TD_YEAR)


def dse_022_zmijewski_score_pct_rank_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Zmijewski score within trailing 252-day distribution."""
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    return _rolling_rank_pct(zm, _TD_YEAR)


# --- Group C (023-032): Merton distance-to-default proxy ---
# Structural proxy: uses equity market cap, debt, and equity volatility
# DD proxy = (ln(V/D) + (mu - 0.5*sigma^2)*T) / (sigma*sqrt(T))
# Simplified: DD ≈ (ln(marketcap / debt) + 0.5*sigma^2*T) / (sigma*sqrt(T))
# We use close price volatility as sigma proxy (annualized)

def dse_023_merton_leverage_ratio(debt: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Merton proxy: debt / marketcap (face value of debt / equity market value)."""
    return _safe_div(debt, marketcap.clip(lower=_EPS))


def dse_024_merton_equity_vol_63d(close: pd.Series) -> pd.Series:
    """Annualized equity volatility over 63-day window (sigma proxy for Merton DD)."""
    return _vol_annual(close, _TD_QTR)


def dse_025_merton_equity_vol_126d(close: pd.Series) -> pd.Series:
    """Annualized equity volatility over 126-day window (half-year sigma proxy)."""
    return _vol_annual(close, _TD_2Q)


def dse_026_merton_dd_proxy_63d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """
    Merton distance-to-default proxy (63-day vol window).
    DD = ln(marketcap / debt.clip(eps)) / sigma + 0.5 * sigma * sqrt(T)
    where T=1 year, sigma = annualized vol from 63-day window.
    Lower DD = closer to default.
    """
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    return _safe_div(ln_vd, sigma) + 0.5 * sigma


def dse_027_merton_dd_proxy_126d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Merton distance-to-default proxy using 126-day volatility window."""
    sigma = _vol_annual(close, _TD_2Q).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    return _safe_div(ln_vd, sigma) + 0.5 * sigma


def dse_028_merton_dd_below1_flag(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if Merton DD proxy < 1.0 (very high default risk)."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    dd = _safe_div(ln_vd, sigma) + 0.5 * sigma
    return (dd < 1.0).astype(float)


def dse_029_merton_dd_below2_flag(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if Merton DD proxy < 2.0 (elevated default risk)."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    dd = _safe_div(ln_vd, sigma) + 0.5 * sigma
    return (dd < 2.0).astype(float)


def dse_030_merton_dd_pct_rank_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of Merton DD proxy within trailing 252-day distribution."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    dd = _safe_div(ln_vd, sigma) + 0.5 * sigma
    return _rolling_rank_pct(dd, _TD_YEAR)


def dse_031_merton_expected_loss_proxy(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """
    Merton expected-loss proxy: debt/(marketcap + debt) * sigma.
    Approximates expected loss rate weighting leverage by volatility.
    """
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    total = marketcap.clip(lower=_EPS) + debt.clip(lower=_EPS)
    lev_ratio = _safe_div(debt.clip(lower=_EPS), total)
    return lev_ratio * sigma


def dse_032_merton_dd_zscore_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Merton DD proxy relative to its trailing 252-day distribution."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    dd = _safe_div(ln_vd, sigma) + 0.5 * sigma
    return _zscore_rolling(dd, _TD_YEAR)


# --- Group D (033-042): Springate score ---
# Springate (1978): S = 1.03*A + 3.07*B + 0.66*C + 0.4*D
# A = workingcapital/assets; B = ebit/assets; C = ebt/currentliabilities;
# D = revenue/assets; S < 0.862 = distress

def dse_033_springate_a(currentassets: pd.Series, currentliabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate component A: working capital / total assets."""
    wc = currentassets - currentliabilities
    return _safe_div(wc, assets)


def dse_034_springate_b(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate component B: EBIT / total assets."""
    return _safe_div(ebit, assets)


def dse_035_springate_c(ebit: pd.Series, currentliabilities: pd.Series) -> pd.Series:
    """Springate component C: EBIT / current liabilities (interest coverage proxy)."""
    return _safe_div(ebit, currentliabilities)


def dse_036_springate_d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate component D: revenue / total assets (asset turnover)."""
    return _safe_div(revenue, assets)


def dse_037_springate_score(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Assembled Springate S-score.
    S = 1.03*A + 3.07*B + 0.66*C + 0.4*D
    S < 0.862 = predicted failure (distress zone).
    """
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    return 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d


def dse_038_springate_distress_flag(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if Springate S-score < 0.862 (distress zone)."""
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    s  = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return (s < 0.862).astype(float)


def dse_039_springate_score_zscore_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Z-score of Springate score relative to its trailing 252-day distribution."""
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    s  = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return _zscore_rolling(s, _TD_YEAR)


def dse_040_springate_score_pct_rank_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Percentile rank of Springate score within trailing 252-day distribution."""
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    s  = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return _rolling_rank_pct(s, _TD_YEAR)


def dse_041_springate_a_weighted(currentassets: pd.Series, currentliabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate weighted A contribution: 1.03 * (workingcapital/assets)."""
    wc = currentassets - currentliabilities
    return 1.03 * _safe_div(wc, assets).fillna(0)


def dse_042_springate_b_weighted(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate weighted B contribution: 3.07 * (ebit/assets)."""
    return 3.07 * _safe_div(ebit, assets).fillna(0)


# --- Group E (043-052): Fulmer H-score ---
# Fulmer (1984): H = 5.528*V1 + 0.212*V2 + 0.073*V3 + 1.27*V4 - 0.12*V5
#                    + 2.335*V6 + 0.575*V7 + 1.083*V8 + 0.894*V9 - 6.075
# V1=retearn/assets; V2=revenue/assets; V3=ebt/equity; V4=ncfo/liabilities;
# V5=debt/assets; V6=currentliabilities/assets; V7=log(tangible_assets);
# V8=workingcapital/liabilities; V9=log(ebit/interest_expense)
# Simplified: we approximate tangible assets as assets, interest coverage via ebit/intexp

def dse_043_fulmer_v1_retearn_to_assets(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Fulmer V1: retained earnings / total assets."""
    return _safe_div(retearn, assets)


def dse_044_fulmer_v2_revenue_to_assets(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Fulmer V2: revenue / total assets."""
    return _safe_div(revenue, assets)


def dse_045_fulmer_v3_ebt_to_equity(ebit: pd.Series, equity: pd.Series) -> pd.Series:
    """Fulmer V3: EBIT (as EBT proxy) / book equity."""
    return _safe_div(ebit, equity)


def dse_046_fulmer_v4_ncfo_to_liabilities(ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Fulmer V4: operating cash flow / total liabilities."""
    return _safe_div(ncfo, liabilities)


def dse_047_fulmer_v5_debt_to_assets(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Fulmer V5: total debt / total assets (leverage)."""
    return _safe_div(debt, assets)


def dse_048_fulmer_v6_currentliab_to_assets(currentliabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Fulmer V6: current liabilities / total assets (short-term leverage)."""
    return _safe_div(currentliabilities, assets)


def dse_049_fulmer_v7_log_assets(assets: pd.Series) -> pd.Series:
    """Fulmer V7: log(total assets) as tangible assets proxy."""
    return np.log(assets.clip(lower=_EPS))


def dse_050_fulmer_v8_wc_to_liabilities(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Fulmer V8: working capital / total liabilities."""
    wc = currentassets - currentliabilities
    return _safe_div(wc, liabilities)


def dse_051_fulmer_score(
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
    """
    Assembled Fulmer H-score (simplified 8-variable version).
    H = 5.528*V1 + 0.212*V2 + 0.073*V3 + 1.27*V4 - 0.12*V5
        + 2.335*V6 + 0.575*V7 + 1.083*V8 - 6.075
    H < 0 = distress predicted.
    Note: V9 (log(ebit/interest)) omitted — interest expense not reliably in SF1.
    """
    v1 = _safe_div(retearn, assets).fillna(0)
    v2 = _safe_div(revenue, assets).fillna(0)
    v3 = _safe_div(ebit, equity).fillna(0)
    v4 = _safe_div(ncfo, liabilities).fillna(0)
    v5 = _safe_div(debt, assets).fillna(0)
    v6 = _safe_div(currentliabilities, assets).fillna(0)
    v7 = np.log(assets.clip(lower=_EPS))
    wc = currentassets - currentliabilities
    v8 = _safe_div(wc, liabilities).fillna(0)
    return (5.528 * v1 + 0.212 * v2 + 0.073 * v3 + 1.27 * v4
            - 0.12 * v5 + 2.335 * v6 + 0.575 * v7 + 1.083 * v8
            - 6.075)


def dse_052_fulmer_distress_flag(
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
    """Binary: 1 if Fulmer H-score < 0 (distress zone)."""
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
         - 0.12 * v5 + 2.335 * v6 + 0.575 * v7 + 1.083 * v8
         - 6.075)
    return (h < 0).astype(float)


# --- Group F (053-062): CA-Score (Legault 1987) ---
# CA-Score for Canadian firms (applicable to US as a cross-sectional distress proxy)
# CA = -4.5913*A1 + 1.9985*A2 - 0.3979*A3
# A1 = (shareholders_equity + minority_interests) / assets  -> approx equity/assets
# A2 = (netinc + depreciation) / (liabilities)  -> cash earnings / liabilities
# A3 = sales_lag / sales_current - 1  -> revenue decline rate
# CA < -0.3 = distress

def dse_053_ca_score_a1(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """CA-Score component A1: book equity / total assets (financial strength)."""
    return _safe_div(equity, assets)


def dse_054_ca_score_a2(netinc: pd.Series, depreciation: pd.Series, liabilities: pd.Series) -> pd.Series:
    """CA-Score component A2: (net income + depreciation) / liabilities (cash earnings coverage)."""
    cash_earn = netinc + depreciation
    return _safe_div(cash_earn, liabilities)


def dse_055_ca_score_a3(revenue: pd.Series) -> pd.Series:
    """CA-Score component A3: prior-year revenue / current revenue - 1 (revenue decline)."""
    rev_lag = revenue.shift(_TD_YEAR)
    return _safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0


def dse_056_ca_score(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Assembled CA-Score (Legault 1987).
    CA = -4.5913*A1 + 1.9985*A2 - 0.3979*A3
    CA < -0.3 = predicted failure.
    """
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    return -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3


def dse_057_ca_score_distress_flag(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if CA-Score < -0.3 (distress zone)."""
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    return (ca < -0.3).astype(float)


def dse_058_ca_score_zscore_252d(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Z-score of CA-Score relative to trailing 252-day distribution."""
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    return _zscore_rolling(ca, _TD_YEAR)


def dse_059_ca_score_pct_rank_252d(
    equity: pd.Series,
    assets: pd.Series,
    netinc: pd.Series,
    depreciation: pd.Series,
    liabilities: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Percentile rank of CA-Score within trailing 252-day distribution."""
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    return _rolling_rank_pct(ca, _TD_YEAR)


def dse_060_ca_score_a1_weighted(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """CA-Score weighted A1 contribution: -4.5913 * (equity/assets)."""
    return -4.5913 * _safe_div(equity, assets).fillna(0)


def dse_061_ca_score_a2_weighted(netinc: pd.Series, depreciation: pd.Series, liabilities: pd.Series) -> pd.Series:
    """CA-Score weighted A2 contribution: 1.9985 * ((netinc+depreciation)/liabilities)."""
    return 1.9985 * _safe_div(netinc + depreciation, liabilities).fillna(0)


def dse_062_ca_score_a3_weighted(revenue: pd.Series) -> pd.Series:
    """CA-Score weighted A3 contribution: -0.3979 * (revenue_lag/revenue - 1)."""
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    return -0.3979 * a3


# --- Group G (063-075): Multi-model ensemble composites and distress flag aggregates ---

def dse_063_ohlson_zscore_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Z-score of Ohlson O-score relative to trailing 252-day distribution."""
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
    chin_num = netinc - ni_prev
    chin_den = netinc.abs() + ni_prev.abs()
    chin  = _safe_div(chin_num, chin_den).fillna(0)
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
         + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
         - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    return _zscore_rolling(o, _TD_YEAR)


def dse_064_ohlson_pct_rank_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Percentile rank of Ohlson O-score within trailing 252-day distribution."""
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
    chin_num = netinc - ni_prev
    chin_den = netinc.abs() + ni_prev.abs()
    chin  = _safe_div(chin_num, chin_den).fillna(0)
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta
         + 0.076 * clca - 1.72 * oeneg - 2.37 * nita
         - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    return _rolling_rank_pct(o, _TD_YEAR)


def dse_065_springate_zscore_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Z-score of Springate S-score relative to trailing 252-day distribution."""
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    s  = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return _zscore_rolling(s, _TD_YEAR)


def dse_066_fulmer_zscore_252d(
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
    """Z-score of Fulmer H-score relative to trailing 252-day distribution."""
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
    return _zscore_rolling(h, _TD_YEAR)


def dse_067_distress_flag_count_3models(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Count of distress flags (0-3): Ohlson > 0.5 prob + Zmijewski > 0 + Springate < 0.862."""
    # Ohlson flag
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
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca
         - 1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    ohlson_flag = (1.0 / (1.0 + np.exp(-o)) > 0.5).astype(float)
    # Zmijewski flag
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta2 = _safe_div(liabilities, assets).fillna(0)
    cacl  = _safe_div(currentassets, currentliabilities).fillna(0)
    zm    = -4.336 - 4.513 * roa + 5.679 * tlta2 + 0.004 * cacl
    zm_flag = (zm > 0).astype(float)
    # Springate flag
    a = _safe_div(wc, assets).fillna(0)
    b = _safe_div(ebit, assets).fillna(0)
    c = _safe_div(ebit, currentliabilities).fillna(0)
    d = _safe_div(revenue, assets).fillna(0)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    sp_flag = (s < 0.862).astype(float)
    return ohlson_flag + zm_flag + sp_flag


def dse_068_ensemble_distress_all3_flag(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if ALL 3 models (Ohlson, Zmijewski, Springate) simultaneously flag distress."""
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
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca
         - 1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    ohlson_flag = (1.0 / (1.0 + np.exp(-o)) > 0.5).astype(float)
    roa  = _safe_div(netinc, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    zm_flag = (zm > 0).astype(float)
    a = _safe_div(wc, assets).fillna(0)
    b = _safe_div(ebit, assets).fillna(0)
    c = _safe_div(ebit, currentliabilities).fillna(0)
    d = _safe_div(revenue, assets).fillna(0)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    sp_flag = (s < 0.862).astype(float)
    return (ohlson_flag * zm_flag * sp_flag)


def dse_069_ohlson_min_252d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """Trailing 252-day minimum of Ohlson O-score (worst distress reading)."""
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
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca
         - 1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    return _rolling_max(o, _TD_YEAR)


def dse_070_zmijewski_min_252d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """Trailing 252-day maximum of Zmijewski score (higher = more distress)."""
    roa  = _safe_div(netinc, assets).fillna(0)
    tlta = _safe_div(liabilities, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    return _rolling_max(zm, _TD_YEAR)


def dse_071_springate_min_252d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Trailing 252-day minimum of Springate score (lower = more distress)."""
    wc = currentassets - currentliabilities
    a  = _safe_div(wc, assets).fillna(0)
    b  = _safe_div(ebit, assets).fillna(0)
    c  = _safe_div(ebit, currentliabilities).fillna(0)
    d  = _safe_div(revenue, assets).fillna(0)
    s  = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return _rolling_min(s, _TD_YEAR)


def dse_072_fulmer_min_252d(
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
    """Trailing 252-day minimum of Fulmer H-score (lower = more distress)."""
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
    return _rolling_min(h, _TD_YEAR)


def dse_073_merton_dd_min_252d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252-day minimum of Merton DD proxy (lower = more distress)."""
    sigma = _vol_annual(close, _TD_QTR).clip(lower=_EPS)
    ln_vd = np.log((marketcap.clip(lower=_EPS)) / debt.clip(lower=_EPS))
    dd = _safe_div(ln_vd, sigma) + 0.5 * sigma
    return _rolling_min(dd, _TD_YEAR)


def dse_074_ohlson_expanding_max(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """All-time expanding maximum of Ohlson O-score (worst ever distress reading)."""
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
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca
         - 1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    return o.expanding(min_periods=4).max()


def dse_075_distress_flag_count_4models(
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
    """Count of distress flags (0-4): Ohlson + Zmijewski + Springate + CA-Score."""
    wc = currentassets - currentliabilities
    # Ohlson
    size  = np.log(assets.clip(lower=_EPS))
    tlta  = _safe_div(liabilities, assets).fillna(0)
    wcta  = _safe_div(wc, assets).fillna(0)
    clca  = _safe_div(currentliabilities, currentassets).fillna(0)
    oeneg = (liabilities > assets).astype(float)
    nita  = _safe_div(netinc, assets).fillna(0)
    futl  = _safe_div(ncfo, liabilities).fillna(0)
    ni_prev = netinc.shift(_TD_QTR)
    intwo = ((netinc < 0) & (ni_prev < 0)).astype(float)
    chin  = _safe_div(netinc - ni_prev, netinc.abs() + ni_prev.abs()).fillna(0)
    o = (-1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.076 * clca
         - 1.72 * oeneg - 2.37 * nita - 1.83 * futl + 0.285 * intwo - 0.521 * chin)
    ohlson_flag = (1.0 / (1.0 + np.exp(-o)) > 0.5).astype(float)
    # Zmijewski
    roa  = _safe_div(netinc, assets).fillna(0)
    cacl = _safe_div(currentassets, currentliabilities).fillna(0)
    zm   = -4.336 - 4.513 * roa + 5.679 * tlta + 0.004 * cacl
    zm_flag = (zm > 0).astype(float)
    # Springate
    a = _safe_div(wc, assets).fillna(0)
    b = _safe_div(ebit, assets).fillna(0)
    c = _safe_div(ebit, currentliabilities).fillna(0)
    d = _safe_div(revenue, assets).fillna(0)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    sp_flag = (s < 0.862).astype(float)
    # CA-Score
    a1 = _safe_div(equity, assets).fillna(0)
    a2 = _safe_div(netinc + depreciation, liabilities).fillna(0)
    rev_lag = revenue.shift(_TD_YEAR)
    a3 = (_safe_div(rev_lag, revenue.clip(lower=_EPS)) - 1.0).fillna(0)
    ca = -4.5913 * a1 + 1.9985 * a2 - 0.3979 * a3
    ca_flag = (ca < -0.3).astype(float)
    return ohlson_flag + zm_flag + sp_flag + ca_flag


# ── Registry ──────────────────────────────────────────────────────────────────

DISTRESS_SCORE_ENSEMBLE_REGISTRY_001_075 = {
    "dse_001_ohlson_size": {"inputs": ["assets"], "func": dse_001_ohlson_size},
    "dse_002_ohlson_tlta": {"inputs": ["liabilities", "assets"], "func": dse_002_ohlson_tlta},
    "dse_003_ohlson_wcta": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_003_ohlson_wcta},
    "dse_004_ohlson_clca": {"inputs": ["currentliabilities", "currentassets"], "func": dse_004_ohlson_clca},
    "dse_005_ohlson_oeneg": {"inputs": ["liabilities", "assets"], "func": dse_005_ohlson_oeneg},
    "dse_006_ohlson_nita": {"inputs": ["netinc", "assets"], "func": dse_006_ohlson_nita},
    "dse_007_ohlson_futl": {"inputs": ["ncfo", "liabilities"], "func": dse_007_ohlson_futl},
    "dse_008_ohlson_intwo": {"inputs": ["netinc"], "func": dse_008_ohlson_intwo},
    "dse_009_ohlson_chin": {"inputs": ["netinc"], "func": dse_009_ohlson_chin},
    "dse_010_ohlson_oscore": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_010_ohlson_oscore},
    "dse_011_ohlson_bankruptcy_prob": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_011_ohlson_bankruptcy_prob},
    "dse_012_ohlson_distress_flag": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_012_ohlson_distress_flag},
    "dse_013_zmijewski_roa": {"inputs": ["netinc", "assets"], "func": dse_013_zmijewski_roa},
    "dse_014_zmijewski_tlta": {"inputs": ["liabilities", "assets"], "func": dse_014_zmijewski_tlta},
    "dse_015_zmijewski_cacl": {"inputs": ["currentassets", "currentliabilities"], "func": dse_015_zmijewski_cacl},
    "dse_016_zmijewski_score": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_016_zmijewski_score},
    "dse_017_zmijewski_distress_flag": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_017_zmijewski_distress_flag},
    "dse_018_zmijewski_roa_weighted": {"inputs": ["netinc", "assets"], "func": dse_018_zmijewski_roa_weighted},
    "dse_019_zmijewski_leverage_weighted": {"inputs": ["liabilities", "assets"], "func": dse_019_zmijewski_leverage_weighted},
    "dse_020_zmijewski_liquidity_weighted": {"inputs": ["currentassets", "currentliabilities"], "func": dse_020_zmijewski_liquidity_weighted},
    "dse_021_zmijewski_score_zscore_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_021_zmijewski_score_zscore_252d},
    "dse_022_zmijewski_score_pct_rank_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_022_zmijewski_score_pct_rank_252d},
    "dse_023_merton_leverage_ratio": {"inputs": ["debt", "marketcap"], "func": dse_023_merton_leverage_ratio},
    "dse_024_merton_equity_vol_63d": {"inputs": ["close"], "func": dse_024_merton_equity_vol_63d},
    "dse_025_merton_equity_vol_126d": {"inputs": ["close"], "func": dse_025_merton_equity_vol_126d},
    "dse_026_merton_dd_proxy_63d": {"inputs": ["debt", "marketcap", "close"], "func": dse_026_merton_dd_proxy_63d},
    "dse_027_merton_dd_proxy_126d": {"inputs": ["debt", "marketcap", "close"], "func": dse_027_merton_dd_proxy_126d},
    "dse_028_merton_dd_below1_flag": {"inputs": ["debt", "marketcap", "close"], "func": dse_028_merton_dd_below1_flag},
    "dse_029_merton_dd_below2_flag": {"inputs": ["debt", "marketcap", "close"], "func": dse_029_merton_dd_below2_flag},
    "dse_030_merton_dd_pct_rank_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_030_merton_dd_pct_rank_252d},
    "dse_031_merton_expected_loss_proxy": {"inputs": ["debt", "marketcap", "close"], "func": dse_031_merton_expected_loss_proxy},
    "dse_032_merton_dd_zscore_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_032_merton_dd_zscore_252d},
    "dse_033_springate_a": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_033_springate_a},
    "dse_034_springate_b": {"inputs": ["ebit", "assets"], "func": dse_034_springate_b},
    "dse_035_springate_c": {"inputs": ["ebit", "currentliabilities"], "func": dse_035_springate_c},
    "dse_036_springate_d": {"inputs": ["revenue", "assets"], "func": dse_036_springate_d},
    "dse_037_springate_score": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_037_springate_score},
    "dse_038_springate_distress_flag": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_038_springate_distress_flag},
    "dse_039_springate_score_zscore_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_039_springate_score_zscore_252d},
    "dse_040_springate_score_pct_rank_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_040_springate_score_pct_rank_252d},
    "dse_041_springate_a_weighted": {"inputs": ["currentassets", "currentliabilities", "assets"], "func": dse_041_springate_a_weighted},
    "dse_042_springate_b_weighted": {"inputs": ["ebit", "assets"], "func": dse_042_springate_b_weighted},
    "dse_043_fulmer_v1_retearn_to_assets": {"inputs": ["retearn", "assets"], "func": dse_043_fulmer_v1_retearn_to_assets},
    "dse_044_fulmer_v2_revenue_to_assets": {"inputs": ["revenue", "assets"], "func": dse_044_fulmer_v2_revenue_to_assets},
    "dse_045_fulmer_v3_ebt_to_equity": {"inputs": ["ebit", "equity"], "func": dse_045_fulmer_v3_ebt_to_equity},
    "dse_046_fulmer_v4_ncfo_to_liabilities": {"inputs": ["ncfo", "liabilities"], "func": dse_046_fulmer_v4_ncfo_to_liabilities},
    "dse_047_fulmer_v5_debt_to_assets": {"inputs": ["debt", "assets"], "func": dse_047_fulmer_v5_debt_to_assets},
    "dse_048_fulmer_v6_currentliab_to_assets": {"inputs": ["currentliabilities", "assets"], "func": dse_048_fulmer_v6_currentliab_to_assets},
    "dse_049_fulmer_v7_log_assets": {"inputs": ["assets"], "func": dse_049_fulmer_v7_log_assets},
    "dse_050_fulmer_v8_wc_to_liabilities": {"inputs": ["currentassets", "currentliabilities", "liabilities"], "func": dse_050_fulmer_v8_wc_to_liabilities},
    "dse_051_fulmer_score": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_051_fulmer_score},
    "dse_052_fulmer_distress_flag": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_052_fulmer_distress_flag},
    "dse_053_ca_score_a1": {"inputs": ["equity", "assets"], "func": dse_053_ca_score_a1},
    "dse_054_ca_score_a2": {"inputs": ["netinc", "depreciation", "liabilities"], "func": dse_054_ca_score_a2},
    "dse_055_ca_score_a3": {"inputs": ["revenue"], "func": dse_055_ca_score_a3},
    "dse_056_ca_score": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_056_ca_score},
    "dse_057_ca_score_distress_flag": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_057_ca_score_distress_flag},
    "dse_058_ca_score_zscore_252d": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_058_ca_score_zscore_252d},
    "dse_059_ca_score_pct_rank_252d": {"inputs": ["equity", "assets", "netinc", "depreciation", "liabilities", "revenue"], "func": dse_059_ca_score_pct_rank_252d},
    "dse_060_ca_score_a1_weighted": {"inputs": ["equity", "assets"], "func": dse_060_ca_score_a1_weighted},
    "dse_061_ca_score_a2_weighted": {"inputs": ["netinc", "depreciation", "liabilities"], "func": dse_061_ca_score_a2_weighted},
    "dse_062_ca_score_a3_weighted": {"inputs": ["revenue"], "func": dse_062_ca_score_a3_weighted},
    "dse_063_ohlson_zscore_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_063_ohlson_zscore_252d},
    "dse_064_ohlson_pct_rank_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_064_ohlson_pct_rank_252d},
    "dse_065_springate_zscore_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_065_springate_zscore_252d},
    "dse_066_fulmer_zscore_252d": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_066_fulmer_zscore_252d},
    "dse_067_distress_flag_count_3models": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_067_distress_flag_count_3models},
    "dse_068_ensemble_distress_all3_flag": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_068_ensemble_distress_all3_flag},
    "dse_069_ohlson_min_252d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_069_ohlson_min_252d},
    "dse_070_zmijewski_min_252d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_070_zmijewski_min_252d},
    "dse_071_springate_min_252d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_071_springate_min_252d},
    "dse_072_fulmer_min_252d": {"inputs": ["retearn", "assets", "revenue", "ebit", "equity", "ncfo", "liabilities", "debt", "currentassets", "currentliabilities"], "func": dse_072_fulmer_min_252d},
    "dse_073_merton_dd_min_252d": {"inputs": ["debt", "marketcap", "close"], "func": dse_073_merton_dd_min_252d},
    "dse_074_ohlson_expanding_max": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_074_ohlson_expanding_max},
    "dse_075_distress_flag_count_4models": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue", "equity", "depreciation"], "func": dse_075_distress_flag_count_4models},
}
