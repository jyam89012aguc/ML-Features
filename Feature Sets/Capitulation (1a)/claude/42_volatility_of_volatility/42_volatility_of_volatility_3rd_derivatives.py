"""
42_volatility_of_volatility — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative vol-of-vol concepts — acceleration of vov velocity
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility over w-day rolling window."""
    lr = _log_ret(close)
    return lr.rolling(w, min_periods=max(2, w // 2)).std() * _SQRT252


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_tr(close, high, low), w)


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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each = diff/slope applied to a 2nd-derivative concept

def vov_drv3_001_std_rvol21_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d vov (acceleration of vov velocity)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_002_std_rvol21_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d vov (jerk in monthly vov change)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_003_cv_rvol21_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d CV of 21d rvol (acceleration of CV velocity)."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_004_mac_rvol21_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d MAC of 21d rvol (jerk of erraticism)."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel = mac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_005_range_rvol21_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d range of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    vel = rng.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_006_ewm_std_rvol21_span63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM std (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    vv = _ewm_std(rv, _TD_QTR)
    vel = vv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_007_cv_rvol21_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d CV of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_008_vov_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d z-score of 63d vov."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(vv, _TD_YEAR)
    s = _rolling_std(vv, _TD_YEAR)
    z = _safe_div(vv - m, s.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_009_vol_step_std_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d std of vol-step changes."""
    rv = _realized_vol(close, _TD_MON)
    s = _rolling_std(rv.diff(1), _TD_QTR)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_010_mac_rvol21_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d MAC of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel21 = mac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_011_vov_trend_slope_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of 21d vov over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    slp = _linslope(vv, _TD_QTR)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_012_cv_tr_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d CV of TR."""
    tr = _tr(close, high, low)
    cv = _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR).clip(lower=_EPS))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_013_vov_composite_3scale_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-scale normalized vov composite."""
    rv = _realized_vol(close, _TD_MON)
    v21 = _rolling_std(rv, _TD_MON)
    v63 = _rolling_std(rv, _TD_QTR)
    v126 = _rolling_std(rv, _TD_HALF)
    avg21 = _rolling_mean(v21, _TD_YEAR).clip(lower=_EPS)
    avg63 = _rolling_mean(v63, _TD_YEAR).clip(lower=_EPS)
    avg126 = _rolling_mean(v126, _TD_YEAR).clip(lower=_EPS)
    comp = (v21 / avg21 + v63 / avg63 + v126 / avg126) / 3.0
    vel = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_014_vol_jaggedness_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d vol jaggedness."""
    rv = _realized_vol(close, _TD_MON)
    abs_chg = rv.diff(1).abs()
    total_abs = abs_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    total_var = (_rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)).clip(lower=_EPS)
    jag = _safe_div(total_abs, total_var)
    vel = jag.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_015_iqr_rvol21_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d IQR of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    q75 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    vel = iqr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_016_ewm_cv_rvol21_span63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM CV (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_ewm_std(rv, _TD_QTR), _ewm_mean(rv, _TD_QTR).clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_017_vol_reversal_freq_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d vol reversal frequency."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    rev = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    freq = rev.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_018_cv_atr21_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d CV of 21d ATR."""
    a = _atr(close, high, low, _TD_MON)
    cv = _safe_div(_rolling_std(a, _TD_QTR), _rolling_mean(a, _TD_QTR).clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_019_std_tr_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d std of TR."""
    tr = _tr(close, high, low)
    s = _rolling_std(tr, _TD_QTR)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vov_drv3_020_cv_rvol21_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252d CV of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_021_vov_slope_252d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the slope-of-slope of 252d vov trend."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    slp252 = _linslope(vv, _TD_YEAR)
    slp_of_slp = _linslope(slp252, _TD_QTR)
    return slp_of_slp.diff(_TD_WEEK)


def vov_drv3_022_ewm_std_rvol21_span63_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EWM std (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    vv = _ewm_std(rv, _TD_QTR)
    vel21 = vv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_023_mac_rvol21_63d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21d of the 63d MAC of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    slp = _linslope(mac, _TD_MON)
    return slp.diff(_TD_WEEK)


def vov_drv3_024_rvol_spread_std_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d std of (21d rvol minus 63d rvol) spread."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    s = _rolling_std(spread, _TD_QTR)
    vel21 = s.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vov_drv3_025_vov_composite_3scale_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21d of the 3-scale vov composite."""
    rv = _realized_vol(close, _TD_MON)
    v21 = _rolling_std(rv, _TD_MON)
    v63 = _rolling_std(rv, _TD_QTR)
    v126 = _rolling_std(rv, _TD_HALF)
    avg21 = _rolling_mean(v21, _TD_YEAR).clip(lower=_EPS)
    avg63 = _rolling_mean(v63, _TD_YEAR).clip(lower=_EPS)
    avg126 = _rolling_mean(v126, _TD_YEAR).clip(lower=_EPS)
    comp = (v21 / avg21 + v63 / avg63 + v126 / avg126) / 3.0
    slp = _linslope(comp, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_REGISTRY_3RD_DERIVATIVES = {
    "vov_drv3_001_std_rvol21_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_001_std_rvol21_63d_5d_diff_5d_diff},
    "vov_drv3_002_std_rvol21_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_002_std_rvol21_63d_21d_diff_5d_diff},
    "vov_drv3_003_cv_rvol21_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_003_cv_rvol21_63d_5d_diff_5d_diff},
    "vov_drv3_004_mac_rvol21_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_004_mac_rvol21_63d_5d_diff_5d_diff},
    "vov_drv3_005_range_rvol21_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_005_range_rvol21_63d_5d_diff_5d_diff},
    "vov_drv3_006_ewm_std_rvol21_span63_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_006_ewm_std_rvol21_span63_5d_diff_5d_diff},
    "vov_drv3_007_cv_rvol21_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_007_cv_rvol21_63d_21d_diff_5d_diff},
    "vov_drv3_008_vov_zscore_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_008_vov_zscore_252d_5d_diff_5d_diff},
    "vov_drv3_009_vol_step_std_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_009_vol_step_std_63d_5d_diff_5d_diff},
    "vov_drv3_010_mac_rvol21_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_010_mac_rvol21_63d_21d_diff_5d_diff},
    "vov_drv3_011_vov_trend_slope_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_011_vov_trend_slope_63d_5d_diff_5d_diff},
    "vov_drv3_012_cv_tr_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv3_012_cv_tr_63d_21d_diff_5d_diff},
    "vov_drv3_013_vov_composite_3scale_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_013_vov_composite_3scale_5d_diff_5d_diff},
    "vov_drv3_014_vol_jaggedness_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_014_vol_jaggedness_63d_5d_diff_5d_diff},
    "vov_drv3_015_iqr_rvol21_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_015_iqr_rvol21_63d_5d_diff_5d_diff},
    "vov_drv3_016_ewm_cv_rvol21_span63_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_016_ewm_cv_rvol21_span63_5d_diff_5d_diff},
    "vov_drv3_017_vol_reversal_freq_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_017_vol_reversal_freq_63d_5d_diff_5d_diff},
    "vov_drv3_018_cv_atr21_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv3_018_cv_atr21_63d_5d_diff_5d_diff},
    "vov_drv3_019_std_tr_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv3_019_std_tr_63d_5d_diff_5d_diff},
    "vov_drv3_020_cv_rvol21_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_020_cv_rvol21_252d_21d_diff_5d_diff},
    "vov_drv3_021_vov_slope_252d_slope_63d_5d_diff": {"inputs": ["close"], "func": vov_drv3_021_vov_slope_252d_slope_63d_5d_diff},
    "vov_drv3_022_ewm_std_rvol21_span63_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_022_ewm_std_rvol21_span63_21d_diff_5d_diff},
    "vov_drv3_023_mac_rvol21_63d_slope_21d_5d_diff": {"inputs": ["close"], "func": vov_drv3_023_mac_rvol21_63d_slope_21d_5d_diff},
    "vov_drv3_024_rvol_spread_std_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": vov_drv3_024_rvol_spread_std_63d_21d_diff_5d_diff},
    "vov_drv3_025_vov_composite_3scale_slope_21d_5d_diff": {"inputs": ["close"], "func": vov_drv3_025_vov_composite_3scale_slope_21d_5d_diff},
}
