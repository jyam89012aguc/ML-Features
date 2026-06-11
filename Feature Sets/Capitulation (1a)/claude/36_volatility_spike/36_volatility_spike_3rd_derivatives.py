"""
36_volatility_spike — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative vol-spike concepts — acceleration of
        velocity: jerk in realized-vol, ATR, Rogers-Satchell, and Yang-Zhang
        spike levels, ratios, and z-scores.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_ANN     = np.sqrt(_TD_YEAR)
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _log_ret(close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    return _rolling_std(_log_ret(close), w) * _ANN


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    hl2 = (np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2)
    return np.sqrt(_rolling_mean(hl2, w) / (4.0 * np.log(2.0))) * _ANN


def _gk_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    hl  = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    co  = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    return np.sqrt(_rolling_mean(gk_day, w) * _TD_YEAR)


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily True Range = max(H-L, |H-prevC|, |L-prevC|)."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low  - prev_close).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Wilder-smoothed Average True Range."""
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1.0 / w, min_periods=max(1, w // 2), adjust=False).mean()


def _rs_day(open: pd.Series, high: pd.Series,
            low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily Rogers-Satchell term."""
    lhc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS)  / close.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS)  / open.clip(lower=_EPS))
    return lhc * lho + llc * llo


def _rs_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Rogers-Satchell annualized volatility."""
    rs = _rs_day(open, high, low, close)
    return np.sqrt(_rolling_mean(rs.clip(lower=0.0), w) * _TD_YEAR)


def _yz_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Yang-Zhang annualized volatility estimator."""
    if w < 2:
        w = 2
    prev_close = close.shift(1)
    ln_oc = np.log(open.clip(lower=_EPS) / prev_close.clip(lower=_EPS))
    ln_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    ov_mean = _rolling_mean(ln_oc, w)
    overnight_var = _rolling_mean((ln_oc - ov_mean) ** 2, w)
    oc_mean = _rolling_mean(ln_co, w)
    oc_var = _rolling_mean((ln_co - oc_mean) ** 2, w)
    rs = _rs_day(open, high, low, close)
    rs_var = _rolling_mean(rs.clip(lower=0.0), w)
    k = 0.34 / (1.34 + (w + 1.0) / max(w - 1.0, 1e-9))
    yz_var = (overnight_var + k * oc_var + (1.0 - k) * rs_var).clip(lower=0.0)
    return np.sqrt(yz_var * _TD_YEAR)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept.

def vsp_drv3_001_rvol5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day realized vol (acceleration of vol velocity)."""
    vel = _realized_vol(close, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_002_rvol5_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 5-day vol (jerk in monthly vol change)."""
    vel21 = _realized_vol(close, _TD_WEEK).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vsp_drv3_003_rvol21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day realized vol (acceleration of monthly vol)."""
    vel = _realized_vol(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_004_rvol5_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day vol z-score (acceleration of extremity growth)."""
    v = _realized_vol(close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_005_rvol5_vs_rvol252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of the 5d/252d vol ratio (jerk in short/long ratio)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_006_rvol5_vs_median63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of the 5d/63d-median vol ratio."""
    v = _realized_vol(close, _TD_WEEK)
    ratio = _safe_div(v, _rolling_median(v, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_007_pk_vol5_5d_diff_5d_diff(high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day Parkinson vol (acceleration of range vol)."""
    vel = _parkinson_vol(high, low, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_008_atr14_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of 14-day ATR (acceleration of ATR velocity)."""
    vel = _atr(high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_009_atr14_zscore_252d_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                    close: pd.Series) -> pd.Series:
    """Second 5-day diff of 14-day ATR z-score (acceleration of ATR extremity)."""
    v = _atr(high, low, close, 14)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_010_natr14_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                         close: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized ATR (acceleration of normalized ATR)."""
    natr = _safe_div(_atr(high, low, close, 14), close.clip(lower=_EPS))
    vel = natr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_011_rs_vol21_5d_diff_5d_diff(open: pd.Series, high: pd.Series,
                                            low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Rogers-Satchell vol (RS acceleration)."""
    vel = _rs_vol(open, high, low, close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_012_rs_vol21_zscore_252d_5d_diff_5d_diff(open: pd.Series,
                                                        high: pd.Series,
                                                        low: pd.Series,
                                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day RS vol z-score (acceleration of RS extremity)."""
    v = _rs_vol(open, high, low, close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_013_yz_vol21_5d_diff_5d_diff(open: pd.Series, high: pd.Series,
                                            low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Yang-Zhang vol (YZ acceleration)."""
    vel = _yz_vol(open, high, low, close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_014_yz_vol21_zscore_252d_5d_diff_5d_diff(open: pd.Series,
                                                        high: pd.Series,
                                                        low: pd.Series,
                                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day YZ vol z-score (acceleration of YZ extremity)."""
    v = _yz_vol(open, high, low, close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_015_gk_vol5_5d_diff_5d_diff(open: pd.Series, high: pd.Series,
                                           low: pd.Series,
                                           close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day GK vol (jerk in GK vol level)."""
    vel = _gk_vol(open, high, low, close, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_016_hl_range_5d_mean_5d_diff_5d_diff(high: pd.Series,
                                                    low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day mean HL range (jerk in intraday range)."""
    hl = _safe_div(high - low, low)
    vel = _rolling_mean(hl, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_017_rvol5_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day vol over 21 days (slope acceleration)."""
    slp = _linslope(_realized_vol(close, _TD_WEEK), _TD_MON)
    return slp.diff(_TD_WEEK)


def vsp_drv3_018_atr14_slope_21d_5d_diff(high: pd.Series, low: pd.Series,
                                          close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 14-day ATR over 21 days (ATR slope acceleration)."""
    slp = _linslope(_atr(high, low, close, 14), _TD_MON)
    return slp.diff(_TD_WEEK)


def vsp_drv3_019_rvol_term_slope_5_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of vol term-structure slope (5d - 63d)."""
    ts = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_QTR)
    vel = ts.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_020_rvol_term_slope_5_252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of vol term-structure slope (5d - 252d)."""
    ts = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)
    vel = ts.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_021_composite_spike_idx_5d_diff_5d_diff(close: pd.Series,
                                                       high: pd.Series,
                                                       low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite vol spike index."""
    rv5 = _realized_vol(close, _TD_WEEK)
    pk5 = _parkinson_vol(high, low, _TD_WEEK)
    hl  = _safe_div(high - low, low)
    hl5 = _rolling_mean(hl, _TD_WEEK)
    def zs(v):
        m = _rolling_mean(v, _TD_YEAR)
        s = _rolling_std(v, _TD_YEAR)
        return _safe_div(v - m, s)
    composite = (zs(rv5) + zs(pk5) + zs(hl5)) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_022_pk_vol5_vs_rvol5_5d_diff_5d_diff(close: pd.Series,
                                                    high: pd.Series,
                                                    low: pd.Series) -> pd.Series:
    """Second 5-day diff of Parkinson-to-close-vol ratio (range/close jerk)."""
    ratio = _safe_div(_parkinson_vol(high, low, _TD_WEEK),
                      _realized_vol(close, _TD_WEEK))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_023_sq_ret5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day mean squared log-return (variance jerk)."""
    lr2 = _log_ret(close) ** 2
    vel = _rolling_mean(lr2, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_drv3_024_rs_vol21_slope_5d_diff(open: pd.Series, high: pd.Series,
                                         low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day RS vol over 21 days."""
    slp = _linslope(_rs_vol(open, high, low, close, _TD_MON), _TD_MON)
    return slp.diff(_TD_WEEK)


def vsp_drv3_025_yz_vol21_slope_5d_diff(open: pd.Series, high: pd.Series,
                                         low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day YZ vol over 21 days."""
    slp = _linslope(_yz_vol(open, high, low, close, _TD_MON), _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_REGISTRY_3RD_DERIVATIVES = {
    "vsp_drv3_001_rvol5_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_001_rvol5_5d_diff_5d_diff},
    "vsp_drv3_002_rvol5_21d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_002_rvol5_21d_diff_5d_diff},
    "vsp_drv3_003_rvol21_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_003_rvol21_5d_diff_5d_diff},
    "vsp_drv3_004_rvol5_zscore_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_004_rvol5_zscore_252d_5d_diff_5d_diff},
    "vsp_drv3_005_rvol5_vs_rvol252_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_005_rvol5_vs_rvol252_5d_diff_5d_diff},
    "vsp_drv3_006_rvol5_vs_median63_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_006_rvol5_vs_median63_5d_diff_5d_diff},
    "vsp_drv3_007_pk_vol5_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vsp_drv3_007_pk_vol5_5d_diff_5d_diff},
    "vsp_drv3_008_atr14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv3_008_atr14_5d_diff_5d_diff},
    "vsp_drv3_009_atr14_zscore_252d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv3_009_atr14_zscore_252d_5d_diff_5d_diff},
    "vsp_drv3_010_natr14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv3_010_natr14_5d_diff_5d_diff},
    "vsp_drv3_011_rs_vol21_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_011_rs_vol21_5d_diff_5d_diff},
    "vsp_drv3_012_rs_vol21_zscore_252d_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_012_rs_vol21_zscore_252d_5d_diff_5d_diff},
    "vsp_drv3_013_yz_vol21_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_013_yz_vol21_5d_diff_5d_diff},
    "vsp_drv3_014_yz_vol21_zscore_252d_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_014_yz_vol21_zscore_252d_5d_diff_5d_diff},
    "vsp_drv3_015_gk_vol5_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_015_gk_vol5_5d_diff_5d_diff},
    "vsp_drv3_016_hl_range_5d_mean_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": vsp_drv3_016_hl_range_5d_mean_5d_diff_5d_diff},
    "vsp_drv3_017_rvol5_slope_21d_5d_diff": {"inputs": ["close"], "func": vsp_drv3_017_rvol5_slope_21d_5d_diff},
    "vsp_drv3_018_atr14_slope_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv3_018_atr14_slope_21d_5d_diff},
    "vsp_drv3_019_rvol_term_slope_5_63_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_019_rvol_term_slope_5_63_5d_diff_5d_diff},
    "vsp_drv3_020_rvol_term_slope_5_252_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_020_rvol_term_slope_5_252_5d_diff_5d_diff},
    "vsp_drv3_021_composite_spike_idx_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vsp_drv3_021_composite_spike_idx_5d_diff_5d_diff},
    "vsp_drv3_022_pk_vol5_vs_rvol5_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": vsp_drv3_022_pk_vol5_vs_rvol5_5d_diff_5d_diff},
    "vsp_drv3_023_sq_ret5_5d_diff_5d_diff": {"inputs": ["close"], "func": vsp_drv3_023_sq_ret5_5d_diff_5d_diff},
    "vsp_drv3_024_rs_vol21_slope_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_024_rs_vol21_slope_5d_diff},
    "vsp_drv3_025_yz_vol21_slope_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv3_025_yz_vol21_slope_5d_diff},
}
