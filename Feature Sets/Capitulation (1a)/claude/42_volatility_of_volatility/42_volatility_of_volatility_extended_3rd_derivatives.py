"""
42_volatility_of_volatility — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of 2nd-derivative extended vov concepts — acceleration of
        Parkinson, Garman-Klass, Rogers-Satchell, cross-estimator and regime vov velocities.
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


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each = diff/slope of a 2nd-derivative extended concept

def vov_extdrv3_001_park_vov_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d Parkinson vov (acceleration of Parkinson vov velocity)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv = _rolling_std(pv, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_002_park_vov_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d Parkinson vov (jerk of monthly PK vov change)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv = _rolling_std(pv, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_extdrv3_003_cv_park_vol21_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d CV of 21d Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    cv = _safe_div(_rolling_std(pv, _TD_QTR), _rolling_mean(pv, _TD_QTR).clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_004_gk_vov_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d Garman-Klass vov (acceleration of GK vov)."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(gk, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_005_gk_vov_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                  low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d GK vov."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(gk, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_extdrv3_006_rs_vov_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d Rogers-Satchell vov (acceleration of RS vov)."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(rs, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_007_rs_vov_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                  low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d Rogers-Satchell vov."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(rs, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_extdrv3_008_cross_vov_composite_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                          low: pd.Series,
                                                          open: pd.Series) -> pd.Series:
    """Second 5-day diff of cross-estimator (CC/PK/GK/RS) vov composite."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    comp = (cc + pk + gk + rs) / 4.0
    vel = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_009_cv_gk_vol21_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                      low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d CV of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    cv = _safe_div(_rolling_std(gk, _TD_QTR), _rolling_mean(gk, _TD_QTR).clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_010_park_vol21_zscore_252d_5d_diff_5d_diff(high: pd.Series,
                                                             low: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d z-score of 21d Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    m = _rolling_mean(pv, _TD_YEAR)
    s = _rolling_std(pv, _TD_YEAR)
    z = _safe_div(pv - m, s.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_011_gk_vol21_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                           low: pd.Series,
                                                           open: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d z-score of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    m = _rolling_mean(gk, _TD_YEAR)
    s = _rolling_std(gk, _TD_YEAR)
    z = _safe_div(gk - m, s.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_012_vol_tail_freq_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d tail-frequency of rvol (acceleration of tail freq)."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    tail = (rv > m + 2.0 * s).astype(float)
    freq = _rolling_sum(tail, _TD_QTR)
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_013_hl_range_norm_vov_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                            low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d std of normalized HL range."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    vv = _rolling_std(hl_norm, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_014_close_open_gap_vov_63d_5d_diff_5d_diff(close: pd.Series,
                                                             open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d overnight-gap vov."""
    gap = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    gvov = _rolling_std(gap, _TD_QTR)
    vel = gvov.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_015_vol_regime_switch_freq_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of vol regime-switch frequency over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_YEAR)
    high_regime = (rv > med).astype(int)
    switch = high_regime.diff(1).abs()
    freq = _rolling_sum(switch, _TD_QTR)
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_016_park_vov_zscore_252d_5d_diff_5d_diff(high: pd.Series,
                                                           low: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 63d Parkinson vov within 252d distribution."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv63 = _rolling_std(pv, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    z = _safe_div(vv63 - m, s.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_017_gk_vov_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                         low: pd.Series,
                                                         open: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 63d GK vov within 252d distribution."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv63 = _rolling_std(gk, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    z = _safe_div(vv63 - m, s.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_018_cross_estimator_dispersion_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                                 low: pd.Series,
                                                                 open: pd.Series) -> pd.Series:
    """Second 5-day diff of cross-estimator vov dispersion."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    disp = pd.concat([cc, pk, gk, rs], axis=1).std(axis=1)
    vel = disp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_019_rvol21_trend_instability_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d trend-residual instability of 21d rvol."""
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
    vel = inst.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_020_park_vol21_mac_63d_5d_diff_5d_diff(high: pd.Series,
                                                         low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d MAC of 21d Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    mac = pv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel = mac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_021_gk_vol21_mac_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                       low: pd.Series,
                                                       open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d MAC of 21d Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    mac = gk.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel = mac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_022_vol_frac_above_mean_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of fraction of days (63d) where 21d rvol > 252d mean."""
    rv = _realized_vol(close, _TD_MON)
    avg = _rolling_mean(rv, _TD_YEAR)
    above = (rv > avg).astype(float)
    frac = _rolling_mean(above, _TD_QTR)
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_023_park_vov_pct_rank_252d_slope_21d_5d_diff(high: pd.Series,
                                                               low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of the 252d pct-rank of 63d Parkinson vov."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv63 = _rolling_std(pv, _TD_QTR)
    rank = vv63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    slp = _linslope(rank, _TD_MON)
    return slp.diff(_TD_WEEK)


def vov_extdrv3_024_max_cross_vov_5d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                    low: pd.Series,
                                                    open: pd.Series) -> pd.Series:
    """Second 5-day diff of max(CC, Parkinson, GK, RS) vov (worst-case vov jerk)."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    mx = pd.concat([cc, pk, gk, rs], axis=1).max(axis=1)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_extdrv3_025_hl_range_norm_vov_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series,
                                                             low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d std of normalized HL range."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    vv = _rolling_std(hl_norm, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "vov_extdrv3_001_park_vov_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_001_park_vov_63d_5d_diff_5d_diff},
    "vov_extdrv3_002_park_vov_63d_21d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_002_park_vov_63d_21d_diff_5d_diff},
    "vov_extdrv3_003_cv_park_vol21_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_003_cv_park_vol21_63d_5d_diff_5d_diff},
    "vov_extdrv3_004_gk_vov_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_004_gk_vov_63d_5d_diff_5d_diff},
    "vov_extdrv3_005_gk_vov_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_005_gk_vov_63d_21d_diff_5d_diff},
    "vov_extdrv3_006_rs_vov_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_006_rs_vov_63d_5d_diff_5d_diff},
    "vov_extdrv3_007_rs_vov_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_007_rs_vov_63d_21d_diff_5d_diff},
    "vov_extdrv3_008_cross_vov_composite_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_008_cross_vov_composite_5d_diff_5d_diff},
    "vov_extdrv3_009_cv_gk_vol21_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_009_cv_gk_vol21_63d_5d_diff_5d_diff},
    "vov_extdrv3_010_park_vol21_zscore_252d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_010_park_vol21_zscore_252d_5d_diff_5d_diff},
    "vov_extdrv3_011_gk_vol21_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_011_gk_vol21_zscore_252d_5d_diff_5d_diff},
    "vov_extdrv3_012_vol_tail_freq_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_extdrv3_012_vol_tail_freq_63d_5d_diff_5d_diff},
    "vov_extdrv3_013_hl_range_norm_vov_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_extdrv3_013_hl_range_norm_vov_63d_5d_diff_5d_diff},
    "vov_extdrv3_014_close_open_gap_vov_63d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": vov_extdrv3_014_close_open_gap_vov_63d_5d_diff_5d_diff},
    "vov_extdrv3_015_vol_regime_switch_freq_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_extdrv3_015_vol_regime_switch_freq_5d_diff_5d_diff},
    "vov_extdrv3_016_park_vov_zscore_252d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_016_park_vov_zscore_252d_5d_diff_5d_diff},
    "vov_extdrv3_017_gk_vov_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_017_gk_vov_zscore_252d_5d_diff_5d_diff},
    "vov_extdrv3_018_cross_estimator_dispersion_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_018_cross_estimator_dispersion_5d_diff_5d_diff},
    "vov_extdrv3_019_rvol21_trend_instability_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_extdrv3_019_rvol21_trend_instability_63d_5d_diff_5d_diff},
    "vov_extdrv3_020_park_vol21_mac_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_020_park_vol21_mac_63d_5d_diff_5d_diff},
    "vov_extdrv3_021_gk_vol21_mac_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_021_gk_vol21_mac_63d_5d_diff_5d_diff},
    "vov_extdrv3_022_vol_frac_above_mean_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_extdrv3_022_vol_frac_above_mean_63d_5d_diff_5d_diff},
    "vov_extdrv3_023_park_vov_pct_rank_252d_slope_21d_5d_diff": {"inputs": ["high", "low"], "func": vov_extdrv3_023_park_vov_pct_rank_252d_slope_21d_5d_diff},
    "vov_extdrv3_024_max_cross_vov_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": vov_extdrv3_024_max_cross_vov_5d_diff_5d_diff},
    "vov_extdrv3_025_hl_range_norm_vov_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_extdrv3_025_hl_range_norm_vov_63d_21d_diff_5d_diff},
}
