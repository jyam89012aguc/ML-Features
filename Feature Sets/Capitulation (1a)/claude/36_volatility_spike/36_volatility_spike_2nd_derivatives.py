"""
36_volatility_spike — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base realized-vol-spike concepts — velocity /
        acceleration of vol-spike levels, ratios, and z-scores; includes
        ATR velocity, Rogers-Satchell velocity, and Yang-Zhang velocity.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vsp_drv2_001_rvol5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day realized vol (velocity of short-term vol level)."""
    return _realized_vol(close, _TD_WEEK).diff(_TD_WEEK)


def vsp_drv2_002_rvol5_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day realized vol (monthly velocity of short-term vol)."""
    return _realized_vol(close, _TD_WEEK).diff(_TD_MON)


def vsp_drv2_003_rvol21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day realized vol (weekly change in monthly vol)."""
    return _realized_vol(close, _TD_MON).diff(_TD_WEEK)


def vsp_drv2_004_rvol21_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day realized vol (monthly change in monthly vol)."""
    return _realized_vol(close, _TD_MON).diff(_TD_MON)


def vsp_drv2_005_rvol5_vs_median63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5d/63d-median vol ratio (velocity of spike ratio)."""
    v = _realized_vol(close, _TD_WEEK)
    ratio = _safe_div(v, _rolling_median(v, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vsp_drv2_006_rvol5_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day vol z-score (252d) — velocity of extremity."""
    v = _realized_vol(close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vsp_drv2_007_rvol21_zscore_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day vol z-score (monthly change in vol extremity)."""
    v = _realized_vol(close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_MON)


def vsp_drv2_008_rvol5_vs_rvol252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/252d vol ratio (short/long spread velocity)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vsp_drv2_009_pk_vol5_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day Parkinson vol."""
    return _parkinson_vol(high, low, _TD_WEEK).diff(_TD_WEEK)


def vsp_drv2_010_pk_vol5_zscore_252d_5d_diff(high: pd.Series,
                                              low: pd.Series) -> pd.Series:
    """5-day diff of 5-day Parkinson vol z-score (252d)."""
    v = _parkinson_vol(high, low, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vsp_drv2_011_atr14_5d_diff(high: pd.Series, low: pd.Series,
                                close: pd.Series) -> pd.Series:
    """5-day diff of 14-day ATR (velocity of ATR level)."""
    return _atr(high, low, close, 14).diff(_TD_WEEK)


def vsp_drv2_012_atr14_21d_diff(high: pd.Series, low: pd.Series,
                                 close: pd.Series) -> pd.Series:
    """21-day diff of 14-day ATR (monthly velocity of ATR)."""
    return _atr(high, low, close, 14).diff(_TD_MON)


def vsp_drv2_013_atr14_zscore_252d_5d_diff(high: pd.Series, low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """5-day diff of 14-day ATR z-score (velocity of ATR extremity)."""
    v = _atr(high, low, close, 14)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vsp_drv2_014_natr14_5d_diff(high: pd.Series, low: pd.Series,
                                 close: pd.Series) -> pd.Series:
    """5-day diff of normalized ATR/close (velocity of normalized ATR)."""
    natr = _safe_div(_atr(high, low, close, 14), close.clip(lower=_EPS))
    return natr.diff(_TD_WEEK)


def vsp_drv2_015_rs_vol21_5d_diff(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Rogers-Satchell vol (RS vol velocity)."""
    return _rs_vol(open, high, low, close, _TD_MON).diff(_TD_WEEK)


def vsp_drv2_016_rs_vol21_zscore_252d_5d_diff(open: pd.Series, high: pd.Series,
                                               low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of 21-day RS vol z-score (velocity of RS extremity)."""
    v = _rs_vol(open, high, low, close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vsp_drv2_017_rs_vol21_vs_median63_5d_diff(open: pd.Series, high: pd.Series,
                                               low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of 21-day RS vol / 63-day median ratio (RS spike velocity)."""
    v = _rs_vol(open, high, low, close, _TD_MON)
    ratio = _safe_div(v, _rolling_median(v, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vsp_drv2_018_yz_vol21_5d_diff(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Yang-Zhang vol (YZ vol velocity)."""
    return _yz_vol(open, high, low, close, _TD_MON).diff(_TD_WEEK)


def vsp_drv2_019_yz_vol21_zscore_252d_5d_diff(open: pd.Series, high: pd.Series,
                                               low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of 21-day YZ vol z-score (velocity of YZ extremity)."""
    v = _yz_vol(open, high, low, close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vsp_drv2_020_yz_vol21_vs_median63_5d_diff(open: pd.Series, high: pd.Series,
                                               low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of 21-day YZ vol / 63-day median ratio (YZ spike velocity)."""
    v = _yz_vol(open, high, low, close, _TD_MON)
    ratio = _safe_div(v, _rolling_median(v, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vsp_drv2_021_gk_vol5_5d_diff(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 5-day Garman-Klass vol."""
    return _gk_vol(open, high, low, close, _TD_WEEK).diff(_TD_WEEK)


def vsp_drv2_022_rvol5_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day realized vol over trailing 21 days."""
    return _linslope(_realized_vol(close, _TD_WEEK), _TD_MON)


def vsp_drv2_023_atr14_slope_21d(high: pd.Series, low: pd.Series,
                                  close: pd.Series) -> pd.Series:
    """OLS slope of 14-day ATR over trailing 21 days."""
    return _linslope(_atr(high, low, close, 14), _TD_MON)


def vsp_drv2_024_rvol_term_slope_5_63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol term-structure slope (5d minus 63d realized vol)."""
    slope_ts = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_QTR)
    return slope_ts.diff(_TD_WEEK)


def vsp_drv2_025_composite_spike_idx_5d_diff(close: pd.Series,
                                              high: pd.Series,
                                              low: pd.Series) -> pd.Series:
    """5-day diff of composite vol spike index (mean z-score of rv5, pk5, hl5)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    pk5 = _parkinson_vol(high, low, _TD_WEEK)
    hl  = _safe_div(high - low, low)
    hl5 = _rolling_mean(hl, _TD_WEEK)
    def zs(v):
        m = _rolling_mean(v, _TD_YEAR)
        s = _rolling_std(v, _TD_YEAR)
        return _safe_div(v - m, s)
    composite = (zs(rv5) + zs(pk5) + zs(hl5)) / 3.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_REGISTRY_2ND_DERIVATIVES = {
    "vsp_drv2_001_rvol5_5d_diff": {"inputs": ["close"], "func": vsp_drv2_001_rvol5_5d_diff},
    "vsp_drv2_002_rvol5_21d_diff": {"inputs": ["close"], "func": vsp_drv2_002_rvol5_21d_diff},
    "vsp_drv2_003_rvol21_5d_diff": {"inputs": ["close"], "func": vsp_drv2_003_rvol21_5d_diff},
    "vsp_drv2_004_rvol21_21d_diff": {"inputs": ["close"], "func": vsp_drv2_004_rvol21_21d_diff},
    "vsp_drv2_005_rvol5_vs_median63_5d_diff": {"inputs": ["close"], "func": vsp_drv2_005_rvol5_vs_median63_5d_diff},
    "vsp_drv2_006_rvol5_zscore_252d_5d_diff": {"inputs": ["close"], "func": vsp_drv2_006_rvol5_zscore_252d_5d_diff},
    "vsp_drv2_007_rvol21_zscore_252d_21d_diff": {"inputs": ["close"], "func": vsp_drv2_007_rvol21_zscore_252d_21d_diff},
    "vsp_drv2_008_rvol5_vs_rvol252_5d_diff": {"inputs": ["close"], "func": vsp_drv2_008_rvol5_vs_rvol252_5d_diff},
    "vsp_drv2_009_pk_vol5_5d_diff": {"inputs": ["high", "low"], "func": vsp_drv2_009_pk_vol5_5d_diff},
    "vsp_drv2_010_pk_vol5_zscore_252d_5d_diff": {"inputs": ["high", "low"], "func": vsp_drv2_010_pk_vol5_zscore_252d_5d_diff},
    "vsp_drv2_011_atr14_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv2_011_atr14_5d_diff},
    "vsp_drv2_012_atr14_21d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv2_012_atr14_21d_diff},
    "vsp_drv2_013_atr14_zscore_252d_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv2_013_atr14_zscore_252d_5d_diff},
    "vsp_drv2_014_natr14_5d_diff": {"inputs": ["high", "low", "close"], "func": vsp_drv2_014_natr14_5d_diff},
    "vsp_drv2_015_rs_vol21_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_015_rs_vol21_5d_diff},
    "vsp_drv2_016_rs_vol21_zscore_252d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_016_rs_vol21_zscore_252d_5d_diff},
    "vsp_drv2_017_rs_vol21_vs_median63_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_017_rs_vol21_vs_median63_5d_diff},
    "vsp_drv2_018_yz_vol21_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_018_yz_vol21_5d_diff},
    "vsp_drv2_019_yz_vol21_zscore_252d_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_019_yz_vol21_zscore_252d_5d_diff},
    "vsp_drv2_020_yz_vol21_vs_median63_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_020_yz_vol21_vs_median63_5d_diff},
    "vsp_drv2_021_gk_vol5_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vsp_drv2_021_gk_vol5_5d_diff},
    "vsp_drv2_022_rvol5_slope_21d": {"inputs": ["close"], "func": vsp_drv2_022_rvol5_slope_21d},
    "vsp_drv2_023_atr14_slope_21d": {"inputs": ["high", "low", "close"], "func": vsp_drv2_023_atr14_slope_21d},
    "vsp_drv2_024_rvol_term_slope_5_63_5d_diff": {"inputs": ["close"], "func": vsp_drv2_024_rvol_term_slope_5_63_5d_diff},
    "vsp_drv2_025_composite_spike_idx_5d_diff": {"inputs": ["close", "high", "low"], "func": vsp_drv2_025_composite_spike_idx_5d_diff},
}
