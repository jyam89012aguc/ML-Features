"""
42_volatility_of_volatility — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended vol-of-vol base concepts — velocity of Parkinson,
        Garman-Klass, Rogers-Satchell, cross-estimator, entropy and regime vov measures.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9
_SQRT252 = 252 ** 0.5

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized close-to-close realized volatility."""
    lr = _log_ret(close)
    return lr.rolling(w, min_periods=max(2, w // 2)).std() * _SQRT252


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson (1980) high-low range volatility estimator, annualized."""
    hl2 = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2
    factor = 1.0 / (4.0 * np.log(2.0))
    daily_var = factor * hl2
    return (daily_var.rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _garman_klass_vol(close: pd.Series, high: pd.Series, low: pd.Series,
                      open_: pd.Series, w: int) -> pd.Series:
    """Garman-Klass (1980) OHLC volatility estimator, annualized."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2.0 * np.log(2.0) - 1.0) * log_co ** 2
    return (gk.rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _rogers_satchell_vol(close: pd.Series, high: pd.Series, low: pd.Series,
                         open_: pd.Series, w: int) -> pd.Series:
    """Rogers-Satchell (1991) volatility estimator, annualized."""
    lhc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS) / open_.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS) / open_.clip(lower=_EPS))
    rs = lhc * lho + llc * llo
    return (rs.clip(lower=0).rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

def vov_extdrv2_001_park_vov_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d std of 21d Parkinson vol (velocity of Parkinson vov)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv = _rolling_std(pv, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_extdrv2_002_park_vov_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63d std of 21d Parkinson vol (monthly velocity of Parkinson vov)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv = _rolling_std(pv, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_extdrv2_003_cv_park_vol21_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d CV of 21d Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    cv = _safe_div(_rolling_std(pv, _TD_QTR), _rolling_mean(pv, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vov_extdrv2_004_gk_vov_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                        open: pd.Series) -> pd.Series:
    """5-day diff of 63d std of 21d Garman-Klass vol (velocity of GK vov)."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(gk, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_extdrv2_005_gk_vov_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                         open: pd.Series) -> pd.Series:
    """21-day diff of 63d std of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(gk, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_extdrv2_006_cv_gk_vol21_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                              open: pd.Series) -> pd.Series:
    """5-day diff of 63d CV of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    cv = _safe_div(_rolling_std(gk, _TD_QTR), _rolling_mean(gk, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vov_extdrv2_007_rs_vov_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                        open: pd.Series) -> pd.Series:
    """5-day diff of 63d std of 21d Rogers-Satchell vol (velocity of RS vov)."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(rs, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_extdrv2_008_rs_vov_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                         open: pd.Series) -> pd.Series:
    """21-day diff of 63d std of 21d Rogers-Satchell vol."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(rs, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_extdrv2_009_cross_estimator_vov_composite_5d_diff(close: pd.Series, high: pd.Series,
                                                            low: pd.Series,
                                                            open: pd.Series) -> pd.Series:
    """5-day diff of mean of CC/Parkinson/GK/RS vov composite."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    comp = (cc + pk + gk + rs) / 4.0
    return comp.diff(_TD_WEEK)


def vov_extdrv2_010_park_vol21_zscore_252d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of 21d Parkinson vol (velocity of Parkinson extremity)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    m = _rolling_mean(pv, _TD_YEAR)
    s = _rolling_std(pv, _TD_YEAR)
    z = _safe_div(pv - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def vov_extdrv2_011_gk_vol21_zscore_252d_5d_diff(close: pd.Series, high: pd.Series,
                                                   low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of 21d GK vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    m = _rolling_mean(gk, _TD_YEAR)
    s = _rolling_std(gk, _TD_YEAR)
    z = _safe_div(gk - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def vov_extdrv2_012_vol_tail_freq_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of tail-frequency (21d rvol > mean+2std, 252d) over 63-day window."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    tail = (rv > m + 2.0 * s).astype(float)
    freq = _rolling_sum(tail, _TD_QTR)
    return freq.diff(_TD_WEEK)


def vov_extdrv2_013_vol_regime_switch_freq_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol regime-switch frequency over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_YEAR)
    high_regime = (rv > med).astype(int)
    switch = high_regime.diff(1).abs()
    freq = _rolling_sum(switch, _TD_QTR)
    return freq.diff(_TD_WEEK)


def vov_extdrv2_014_hl_range_norm_vov_63d_5d_diff(close: pd.Series, high: pd.Series,
                                                    low: pd.Series) -> pd.Series:
    """5-day diff of std of normalized HL range over 63 days."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    vv = _rolling_std(hl_norm, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_extdrv2_015_hl_range_norm_vov_63d_21d_diff(close: pd.Series, high: pd.Series,
                                                     low: pd.Series) -> pd.Series:
    """21-day diff of std of normalized HL range over 63 days."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    vv = _rolling_std(hl_norm, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_extdrv2_016_close_open_gap_vov_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 63d overnight-gap vov (std of log(open/prev_close))."""
    gap = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    gvov = _rolling_std(gap, _TD_QTR)
    return gvov.diff(_TD_WEEK)


def vov_extdrv2_017_park_vov_zscore_252d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of z-score of 63d Parkinson vov within 252d distribution."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv63 = _rolling_std(pv, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    z = _safe_div(vv63 - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def vov_extdrv2_018_gk_vov_zscore_252d_5d_diff(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of z-score of 63d Garman-Klass vov within 252d distribution."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv63 = _rolling_std(gk, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    z = _safe_div(vv63 - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def vov_extdrv2_019_cross_estimator_dispersion_5d_diff(close: pd.Series, high: pd.Series,
                                                         low: pd.Series,
                                                         open: pd.Series) -> pd.Series:
    """5-day diff of cross-estimator vov dispersion (std of CC/PK/GK/RS vov estimates)."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    disp = pd.concat([cc, pk, gk, rs], axis=1).std(axis=1)
    return disp.diff(_TD_WEEK)


def vov_extdrv2_020_rvol21_trend_instability_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d trend-residual instability of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    def _resid_std(x):
        if len(x) < max(3, len(x) // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den < _EPS:
            return np.nan
        slope = ((xi - xi_m) * (x - x_m)).sum() / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        return resid.std()
    inst = rv.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_resid_std, raw=True)
    return inst.diff(_TD_WEEK)


def vov_extdrv2_021_park_vol21_mac_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d MAC of 21d Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    mac = pv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.diff(_TD_WEEK)


def vov_extdrv2_022_gk_vol21_mac_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series,
                                               open: pd.Series) -> pd.Series:
    """5-day diff of 63d MAC of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    mac = gk.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.diff(_TD_WEEK)


def vov_extdrv2_023_vol_frac_above_mean_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of fraction of days (63d window) where rvol21 > 252d rolling mean."""
    rv = _realized_vol(close, _TD_MON)
    avg = _rolling_mean(rv, _TD_YEAR)
    above = (rv > avg).astype(float)
    frac = _rolling_mean(above, _TD_QTR)
    return frac.diff(_TD_WEEK)


def vov_extdrv2_024_park_vov_pct_rank_252d_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 252d pct-rank of 63d Parkinson vov."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv63 = _rolling_std(pv, _TD_QTR)
    rank = vv63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_MON)


def vov_extdrv2_025_max_cross_estimator_vov_5d_diff(close: pd.Series, high: pd.Series,
                                                      low: pd.Series,
                                                      open: pd.Series) -> pd.Series:
    """5-day diff of max(CC, Parkinson, GK, RS) vov (worst-case vov velocity)."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    mx = pd.concat([cc, pk, gk, rs], axis=1).max(axis=1)
    return mx.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "vov_extdrv2_001_park_vov_63d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_001_park_vov_63d_5d_diff},
    "vov_extdrv2_002_park_vov_63d_21d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_002_park_vov_63d_21d_diff},
    "vov_extdrv2_003_cv_park_vol21_63d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_003_cv_park_vol21_63d_5d_diff},
    "vov_extdrv2_004_gk_vov_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_004_gk_vov_63d_5d_diff},
    "vov_extdrv2_005_gk_vov_63d_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_005_gk_vov_63d_21d_diff},
    "vov_extdrv2_006_cv_gk_vol21_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_006_cv_gk_vol21_63d_5d_diff},
    "vov_extdrv2_007_rs_vov_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_007_rs_vov_63d_5d_diff},
    "vov_extdrv2_008_rs_vov_63d_21d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_008_rs_vov_63d_21d_diff},
    "vov_extdrv2_009_cross_estimator_vov_composite_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_009_cross_estimator_vov_composite_5d_diff},
    "vov_extdrv2_010_park_vol21_zscore_252d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_010_park_vol21_zscore_252d_5d_diff},
    "vov_extdrv2_011_gk_vol21_zscore_252d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_011_gk_vol21_zscore_252d_5d_diff},
    "vov_extdrv2_012_vol_tail_freq_63d_5d_diff": {"inputs": ["close"], "func": vov_extdrv2_012_vol_tail_freq_63d_5d_diff},
    "vov_extdrv2_013_vol_regime_switch_freq_63d_5d_diff": {"inputs": ["close"], "func": vov_extdrv2_013_vol_regime_switch_freq_63d_5d_diff},
    "vov_extdrv2_014_hl_range_norm_vov_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_extdrv2_014_hl_range_norm_vov_63d_5d_diff},
    "vov_extdrv2_015_hl_range_norm_vov_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": vov_extdrv2_015_hl_range_norm_vov_63d_21d_diff},
    "vov_extdrv2_016_close_open_gap_vov_63d_5d_diff": {"inputs": ["close", "open"], "func": vov_extdrv2_016_close_open_gap_vov_63d_5d_diff},
    "vov_extdrv2_017_park_vov_zscore_252d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_017_park_vov_zscore_252d_5d_diff},
    "vov_extdrv2_018_gk_vov_zscore_252d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_018_gk_vov_zscore_252d_5d_diff},
    "vov_extdrv2_019_cross_estimator_dispersion_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_019_cross_estimator_dispersion_5d_diff},
    "vov_extdrv2_020_rvol21_trend_instability_63d_5d_diff": {"inputs": ["close"], "func": vov_extdrv2_020_rvol21_trend_instability_63d_5d_diff},
    "vov_extdrv2_021_park_vol21_mac_63d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv2_021_park_vol21_mac_63d_5d_diff},
    "vov_extdrv2_022_gk_vol21_mac_63d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_022_gk_vol21_mac_63d_5d_diff},
    "vov_extdrv2_023_vol_frac_above_mean_63d_5d_diff": {"inputs": ["close"], "func": vov_extdrv2_023_vol_frac_above_mean_63d_5d_diff},
    "vov_extdrv2_024_park_vov_pct_rank_252d_slope_21d": {"inputs": ["high", "low"], "func": vov_extdrv2_024_park_vov_pct_rank_252d_slope_21d},
    "vov_extdrv2_025_max_cross_estimator_vov_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv2_025_max_cross_estimator_vov_5d_diff},
}
