"""
42_volatility_of_volatility — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base vol-of-vol concepts — velocity of vov instability
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vov_drv2_001_std_rvol21_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d std of 21d rvol (velocity of core vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_drv2_002_std_rvol21_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d std of 21d rvol (monthly velocity of vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_drv2_003_cv_rvol21_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d CV of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vov_drv2_004_cv_rvol21_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d CV of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_MON)


def vov_drv2_005_mac_rvol21_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d MAC of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.diff(_TD_WEEK)


def vov_drv2_006_mac_rvol21_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d MAC of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    mac = rv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.diff(_TD_MON)


def vov_drv2_007_range_rvol21_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d range of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    return rng.diff(_TD_WEEK)


def vov_drv2_008_range_rvol21_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d range of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    rng = _rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)
    return rng.diff(_TD_MON)


def vov_drv2_009_ewm_std_rvol21_span63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM std (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    vv = _ewm_std(rv, _TD_QTR)
    return vv.diff(_TD_WEEK)


def vov_drv2_010_ewm_std_rvol21_span63_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of EWM std (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    vv = _ewm_std(rv, _TD_QTR)
    return vv.diff(_TD_MON)


def vov_drv2_011_cv_atr21_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d CV of 21d ATR."""
    a = _atr(close, high, low, _TD_MON)
    cv = _safe_div(_rolling_std(a, _TD_QTR), _rolling_mean(a, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vov_drv2_012_vol_jaggedness_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d vol jaggedness (path erraticism velocity)."""
    rv = _realized_vol(close, _TD_MON)
    abs_chg = rv.diff(1).abs()
    total_abs = abs_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    total_var = (_rolling_max(rv, _TD_QTR) - _rolling_min(rv, _TD_QTR)).clip(lower=_EPS)
    jag = _safe_div(total_abs, total_var)
    return jag.diff(_TD_WEEK)


def vov_drv2_013_std_tr_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d std of TR (velocity of TR instability)."""
    tr = _tr(close, high, low)
    s = _rolling_std(tr, _TD_QTR)
    return s.diff(_TD_WEEK)


def vov_drv2_014_cv_tr_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63d CV of TR."""
    tr = _tr(close, high, low)
    cv = _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_MON)


def vov_drv2_015_vov_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of 63d vov (velocity of vov extremity)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_QTR)
    m = _rolling_mean(vv, _TD_YEAR)
    s = _rolling_std(vv, _TD_YEAR)
    z = _safe_div(vv - m, s.clip(lower=_EPS))
    return z.diff(_TD_WEEK)


def vov_drv2_016_vol_step_std_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d std of daily vol-step changes."""
    rv = _realized_vol(close, _TD_MON)
    s = _rolling_std(rv.diff(1), _TD_QTR)
    return s.diff(_TD_WEEK)


def vov_drv2_017_vov_trend_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d vov over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    slp = _linslope(vv, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vov_drv2_018_iqr_rvol21_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of IQR of 21d rvol over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    q75 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    return iqr.diff(_TD_WEEK)


def vov_drv2_019_vov_composite_3scale_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 3-scale normalized vov composite."""
    rv = _realized_vol(close, _TD_MON)
    v21 = _rolling_std(rv, _TD_MON)
    v63 = _rolling_std(rv, _TD_QTR)
    v126 = _rolling_std(rv, _TD_HALF)
    avg21 = _rolling_mean(v21, _TD_YEAR).clip(lower=_EPS)
    avg63 = _rolling_mean(v63, _TD_YEAR).clip(lower=_EPS)
    avg126 = _rolling_mean(v126, _TD_YEAR).clip(lower=_EPS)
    comp = (v21 / avg21 + v63 / avg63 + v126 / avg126) / 3.0
    return comp.diff(_TD_WEEK)


def vov_drv2_020_cv_rvol21_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252d CV of 21d rvol (long-run CV velocity)."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_rolling_std(rv, _TD_YEAR), _rolling_mean(rv, _TD_YEAR).clip(lower=_EPS))
    return cv.diff(_TD_MON)


def vov_drv2_021_vol_reversal_freq_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d vol reversal frequency."""
    rv = _realized_vol(close, _TD_MON)
    d = rv.diff(1)
    rev = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    freq = rev.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return freq.diff(_TD_WEEK)


def vov_drv2_022_ewm_cv_rvol21_span63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM CV (span=63) of 21d rvol."""
    rv = _realized_vol(close, _TD_MON)
    cv = _safe_div(_ewm_std(rv, _TD_QTR), _ewm_mean(rv, _TD_QTR).clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vov_drv2_023_mac_tr_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63d MAC of TR (velocity of TR erraticism)."""
    tr = _tr(close, high, low)
    mac = tr.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.diff(_TD_MON)


def vov_drv2_024_vov_slope_252d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope over 63d of the 252d vov slope (trend of trend in vov)."""
    rv = _realized_vol(close, _TD_MON)
    vv = _rolling_std(rv, _TD_MON)
    slp252 = _linslope(vv, _TD_YEAR)
    return _linslope(slp252, _TD_QTR)


def vov_drv2_025_rvol_spread_std_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of std of (21d rvol minus 63d rvol) spread over 63d."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    s = _rolling_std(spread, _TD_QTR)
    return s.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_REGISTRY_2ND_DERIVATIVES = {
    "vov_drv2_001_std_rvol21_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_001_std_rvol21_63d_5d_diff},
    "vov_drv2_002_std_rvol21_63d_21d_diff": {"inputs": ["close"], "func": vov_drv2_002_std_rvol21_63d_21d_diff},
    "vov_drv2_003_cv_rvol21_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_003_cv_rvol21_63d_5d_diff},
    "vov_drv2_004_cv_rvol21_63d_21d_diff": {"inputs": ["close"], "func": vov_drv2_004_cv_rvol21_63d_21d_diff},
    "vov_drv2_005_mac_rvol21_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_005_mac_rvol21_63d_5d_diff},
    "vov_drv2_006_mac_rvol21_63d_21d_diff": {"inputs": ["close"], "func": vov_drv2_006_mac_rvol21_63d_21d_diff},
    "vov_drv2_007_range_rvol21_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_007_range_rvol21_63d_5d_diff},
    "vov_drv2_008_range_rvol21_63d_21d_diff": {"inputs": ["close"], "func": vov_drv2_008_range_rvol21_63d_21d_diff},
    "vov_drv2_009_ewm_std_rvol21_span63_5d_diff": {"inputs": ["close"], "func": vov_drv2_009_ewm_std_rvol21_span63_5d_diff},
    "vov_drv2_010_ewm_std_rvol21_span63_21d_diff": {"inputs": ["close"], "func": vov_drv2_010_ewm_std_rvol21_span63_21d_diff},
    "vov_drv2_011_cv_atr21_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv2_011_cv_atr21_63d_5d_diff},
    "vov_drv2_012_vol_jaggedness_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_012_vol_jaggedness_63d_5d_diff},
    "vov_drv2_013_std_tr_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv2_013_std_tr_63d_5d_diff},
    "vov_drv2_014_cv_tr_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv2_014_cv_tr_63d_21d_diff},
    "vov_drv2_015_vov_zscore_252d_5d_diff": {"inputs": ["close"], "func": vov_drv2_015_vov_zscore_252d_5d_diff},
    "vov_drv2_016_vol_step_std_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_016_vol_step_std_63d_5d_diff},
    "vov_drv2_017_vov_trend_slope_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_017_vov_trend_slope_63d_5d_diff},
    "vov_drv2_018_iqr_rvol21_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_018_iqr_rvol21_63d_5d_diff},
    "vov_drv2_019_vov_composite_3scale_5d_diff": {"inputs": ["close"], "func": vov_drv2_019_vov_composite_3scale_5d_diff},
    "vov_drv2_020_cv_rvol21_252d_21d_diff": {"inputs": ["close"], "func": vov_drv2_020_cv_rvol21_252d_21d_diff},
    "vov_drv2_021_vol_reversal_freq_63d_5d_diff": {"inputs": ["close"], "func": vov_drv2_021_vol_reversal_freq_63d_5d_diff},
    "vov_drv2_022_ewm_cv_rvol21_span63_5d_diff": {"inputs": ["close"], "func": vov_drv2_022_ewm_cv_rvol21_span63_5d_diff},
    "vov_drv2_023_mac_tr_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": vov_drv2_023_mac_tr_63d_21d_diff},
    "vov_drv2_024_vov_slope_252d_slope_63d": {"inputs": ["close"], "func": vov_drv2_024_vov_slope_252d_slope_63d},
    "vov_drv2_025_rvol_spread_std_63d_21d_diff": {"inputs": ["close"], "func": vov_drv2_025_rvol_spread_std_63d_21d_diff},
}
