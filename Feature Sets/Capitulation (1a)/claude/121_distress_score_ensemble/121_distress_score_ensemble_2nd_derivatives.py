"""
121_distress_score_ensemble — 2nd Derivatives (Features dse_drv2_001-025)
Domain: rate of change / velocity of base distress score ensemble features
        — how fast Ohlson, Zmijewski, Springate, Merton DD, CA-Score are moving
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 4):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = np.nanmean(x)
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 4)).apply(slope, raw=True)


def _vol_annual(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=max(2, w // 4)).std() * np.sqrt(_TD_YEAR)


# ── Core score helpers (identical to base files) ───────────────────────────────

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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dse_drv2_001_ohlson_oscore_63d_diff(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """63-day diff of Ohlson O-score (quarterly velocity of distress change)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return o.diff(_TD_QTR)


def dse_drv2_002_ohlson_prob_63d_diff(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """63-day diff of Ohlson bankruptcy probability (velocity of prob change)."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return prob.diff(_TD_QTR)


def dse_drv2_003_zmijewski_score_63d_diff(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """63-day diff of Zmijewski score (quarterly velocity)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm.diff(_TD_QTR)


def dse_drv2_004_springate_score_63d_diff(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """63-day diff of Springate score (quarterly velocity; negative = deterioration)."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return s.diff(_TD_QTR)


def dse_drv2_005_merton_dd_63d_diff(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """63-day diff of Merton DD proxy (velocity of approach to / retreat from default)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd.diff(_TD_QTR)


def dse_drv2_006_ohlson_oscore_21d_diff(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """21-day diff of Ohlson O-score (monthly velocity)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return o.diff(_TD_MON)


def dse_drv2_007_zmijewski_score_21d_diff(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """21-day diff of Zmijewski score (monthly velocity)."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return zm.diff(_TD_MON)


def dse_drv2_008_ohlson_oscore_zscore_63d_diff(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """63-day diff of the 252-day z-score of Ohlson O-score."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    z = _zscore_rolling(o, _TD_YEAR)
    return z.diff(_TD_QTR)


def dse_drv2_009_zmijewski_score_zscore_63d_diff(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """63-day diff of the 252-day z-score of Zmijewski score."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    z  = _zscore_rolling(zm, _TD_YEAR)
    return z.diff(_TD_QTR)


def dse_drv2_010_springate_score_zscore_63d_diff(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """63-day diff of the 252-day z-score of Springate score."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    z = _zscore_rolling(s, _TD_YEAR)
    return z.diff(_TD_QTR)


def dse_drv2_011_merton_dd_zscore_63d_diff(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """63-day diff of the 252-day z-score of Merton DD proxy."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    z  = _zscore_rolling(dd, _TD_YEAR)
    return z.diff(_TD_QTR)


def dse_drv2_012_ohlson_oscore_slope_63d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """OLS slope of Ohlson O-score over trailing 63 days (linear trend in distress)."""
    o = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    return _linslope(o, _TD_QTR)


def dse_drv2_013_zmijewski_score_slope_63d(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
) -> pd.Series:
    """OLS slope of Zmijewski score over trailing 63 days."""
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    return _linslope(zm, _TD_QTR)


def dse_drv2_014_springate_score_slope_63d(
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """OLS slope of Springate score over trailing 63 days."""
    s = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    return _linslope(s, _TD_QTR)


def dse_drv2_015_merton_dd_slope_63d(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of Merton DD proxy over trailing 63 days."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return _linslope(dd, _TD_QTR)


def dse_drv2_016_ohlson_tlta_63d_diff(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """63-day diff of Ohlson leverage component TLTA (liabilities/assets)."""
    tlta = _safe_div(liabilities, assets)
    return tlta.diff(_TD_QTR)


def dse_drv2_017_ohlson_nita_63d_diff(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """63-day diff of Ohlson profitability component NITA (netinc/assets)."""
    nita = _safe_div(netinc, assets)
    return nita.diff(_TD_QTR)


def dse_drv2_018_merton_vol_63d_diff(close: pd.Series) -> pd.Series:
    """63-day diff of annualized equity volatility (vol velocity — stress escalation)."""
    vol = _vol_annual(close, _TD_QTR)
    return vol.diff(_TD_QTR)


def dse_drv2_019_merton_leverage_21d_diff(debt: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of Merton leverage ratio (debt/marketcap) — fast leverage drift."""
    lev = _safe_div(debt, marketcap.clip(lower=_EPS))
    return lev.diff(_TD_MON)


def dse_drv2_020_three_model_zscore_avg_63d_diff(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    ebit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """63-day diff of the 3-model average z-score composite (Ohlson, Zmijewski, -Springate)."""
    o  = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    zm = _zmijewski_score(netinc, assets, liabilities, currentassets, currentliabilities)
    sp = _springate_score(currentassets, currentliabilities, assets, ebit, revenue)
    composite = (_zscore_rolling(o, _TD_YEAR).fillna(0)
                 + _zscore_rolling(zm, _TD_YEAR).fillna(0)
                 + _zscore_rolling(-sp, _TD_YEAR).fillna(0)) / 3.0
    return composite.diff(_TD_QTR)


def dse_drv2_021_ohlson_prob_slope_63d(
    assets: pd.Series,
    liabilities: pd.Series,
    currentassets: pd.Series,
    currentliabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """OLS slope of Ohlson bankruptcy probability over trailing 63 days."""
    o    = _ohlson_score(assets, liabilities, currentassets, currentliabilities, netinc, ncfo)
    prob = 1.0 / (1.0 + np.exp(-o))
    return _linslope(prob, _TD_QTR)


def dse_drv2_022_zmijewski_roa_63d_diff(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """63-day diff of ROA (netinc/assets) — earnings trend velocity."""
    roa = _safe_div(netinc, assets)
    return roa.diff(_TD_QTR)


def dse_drv2_023_springate_ebit_ratio_63d_diff(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """63-day diff of EBIT/assets — operating performance velocity."""
    r = _safe_div(ebit, assets)
    return r.diff(_TD_QTR)


def dse_drv2_024_merton_dd_126d_diff(debt: pd.Series, marketcap: pd.Series, close: pd.Series) -> pd.Series:
    """126-day diff of Merton DD proxy (half-year velocity)."""
    dd = _merton_dd(debt, marketcap, close, _TD_QTR)
    return dd.diff(_TD_2Q)


def dse_drv2_025_ohlson_futl_63d_diff(ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """63-day diff of Ohlson FUTL component (ncfo/liabilities) — cash coverage velocity."""
    futl = _safe_div(ncfo, liabilities)
    return futl.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

DISTRESS_SCORE_ENSEMBLE_REGISTRY_2ND_DERIVATIVES = {
    "dse_drv2_001_ohlson_oscore_63d_diff": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_001_ohlson_oscore_63d_diff},
    "dse_drv2_002_ohlson_prob_63d_diff": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_002_ohlson_prob_63d_diff},
    "dse_drv2_003_zmijewski_score_63d_diff": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_drv2_003_zmijewski_score_63d_diff},
    "dse_drv2_004_springate_score_63d_diff": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_drv2_004_springate_score_63d_diff},
    "dse_drv2_005_merton_dd_63d_diff": {"inputs": ["debt", "marketcap", "close"], "func": dse_drv2_005_merton_dd_63d_diff},
    "dse_drv2_006_ohlson_oscore_21d_diff": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_006_ohlson_oscore_21d_diff},
    "dse_drv2_007_zmijewski_score_21d_diff": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_drv2_007_zmijewski_score_21d_diff},
    "dse_drv2_008_ohlson_oscore_zscore_63d_diff": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_008_ohlson_oscore_zscore_63d_diff},
    "dse_drv2_009_zmijewski_score_zscore_63d_diff": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_drv2_009_zmijewski_score_zscore_63d_diff},
    "dse_drv2_010_springate_score_zscore_63d_diff": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_drv2_010_springate_score_zscore_63d_diff},
    "dse_drv2_011_merton_dd_zscore_63d_diff": {"inputs": ["debt", "marketcap", "close"], "func": dse_drv2_011_merton_dd_zscore_63d_diff},
    "dse_drv2_012_ohlson_oscore_slope_63d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_012_ohlson_oscore_slope_63d},
    "dse_drv2_013_zmijewski_score_slope_63d": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliabilities"], "func": dse_drv2_013_zmijewski_score_slope_63d},
    "dse_drv2_014_springate_score_slope_63d": {"inputs": ["currentassets", "currentliabilities", "assets", "ebit", "revenue"], "func": dse_drv2_014_springate_score_slope_63d},
    "dse_drv2_015_merton_dd_slope_63d": {"inputs": ["debt", "marketcap", "close"], "func": dse_drv2_015_merton_dd_slope_63d},
    "dse_drv2_016_ohlson_tlta_63d_diff": {"inputs": ["liabilities", "assets"], "func": dse_drv2_016_ohlson_tlta_63d_diff},
    "dse_drv2_017_ohlson_nita_63d_diff": {"inputs": ["netinc", "assets"], "func": dse_drv2_017_ohlson_nita_63d_diff},
    "dse_drv2_018_merton_vol_63d_diff": {"inputs": ["close"], "func": dse_drv2_018_merton_vol_63d_diff},
    "dse_drv2_019_merton_leverage_21d_diff": {"inputs": ["debt", "marketcap"], "func": dse_drv2_019_merton_leverage_21d_diff},
    "dse_drv2_020_three_model_zscore_avg_63d_diff": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo", "ebit", "revenue"], "func": dse_drv2_020_three_model_zscore_avg_63d_diff},
    "dse_drv2_021_ohlson_prob_slope_63d": {"inputs": ["assets", "liabilities", "currentassets", "currentliabilities", "netinc", "ncfo"], "func": dse_drv2_021_ohlson_prob_slope_63d},
    "dse_drv2_022_zmijewski_roa_63d_diff": {"inputs": ["netinc", "assets"], "func": dse_drv2_022_zmijewski_roa_63d_diff},
    "dse_drv2_023_springate_ebit_ratio_63d_diff": {"inputs": ["ebit", "assets"], "func": dse_drv2_023_springate_ebit_ratio_63d_diff},
    "dse_drv2_024_merton_dd_126d_diff": {"inputs": ["debt", "marketcap", "close"], "func": dse_drv2_024_merton_dd_126d_diff},
    "dse_drv2_025_ohlson_futl_63d_diff": {"inputs": ["ncfo", "liabilities"], "func": dse_drv2_025_ohlson_futl_63d_diff},
}
