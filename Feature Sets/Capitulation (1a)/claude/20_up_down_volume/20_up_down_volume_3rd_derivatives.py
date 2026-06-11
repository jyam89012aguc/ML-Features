"""
20_up_down_volume — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative up/down volume features — acceleration of
        the velocity of direction-conditioned volume balance (inflection/exhaustion).
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

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


def _down_vol_share(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling down-vol share helper."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), w)
    tv = _rolling_sum(volume, w)
    return _safe_div(dv, tv)


def _down_up_avg_vol_ratio(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling avg down-day vol / avg up-day vol helper."""
    dv = volume.where(close < close.shift(1), np.nan).rolling(w, min_periods=1).mean()
    uv = volume.where(close > close.shift(1), np.nan).rolling(w, min_periods=1).mean()
    return _safe_div(dv, uv)


def _net_vol(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling net volume (up minus down) helper."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), w)
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), w)
    return uv - dv


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd derivative = diff/slope of a 2nd-derivative concept

def udv_drv3_001_down_vol_share_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-vol share (jerk in distribution pressure)."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_002_down_vol_share_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21d down-vol share (acceleration of monthly shift)."""
    vel21 = _down_vol_share(close, volume, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def udv_drv3_003_down_up_avg_vol_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down/up avg-vol ratio (jerk in ratio velocity)."""
    vel = _down_up_avg_vol_ratio(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_004_net_vol_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day net volume (acceleration of flow direction change)."""
    vel = _net_vol(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_005_net_vol_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day net volume."""
    vel21 = _net_vol(close, volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def udv_drv3_006_down_vol_share_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day down-vol share."""
    vel = _down_vol_share(close, volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_007_down_vol_share_21d_slope_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day down-vol share over 63 days."""
    slp = _linslope(_down_vol_share(close, volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_WEEK)


def udv_drv3_008_ret_wtd_down_up_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day return-weighted down/up volume ratio."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_009_obv_5d_diff_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21d OLS slope of 5d OBV change (slope-of-slope acceleration)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg5 = obv.diff(_TD_WEEK)
    slp = _linslope(chg5, _TD_MON)
    return slp.diff(_TD_WEEK)


def udv_drv3_010_cmf_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Chaikin Money Flow (jerk in money flow)."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf = _safe_div(_rolling_sum(mfv, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = cmf.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_011_down_vol_share_21d_5d_diff_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21d slope of 5d-velocity of 21d down-vol share."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    slp = _linslope(vel, _TD_MON)
    return slp.diff(_TD_WEEK)


def udv_drv3_012_vol_wtd_down_up_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol-weighted down/up ratio."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    wt_d = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    wt_u = _safe_div(volume, avg_vol).where(close > close.shift(1), 0.0)
    ratio = _safe_div(_rolling_sum(wt_d, _TD_MON), _rolling_sum(wt_u, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_013_net_vol_21d_slope_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day net volume over 63 days."""
    slp = _linslope(_net_vol(close, volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_WEEK)


def udv_drv3_014_down_vol_share_21d_21d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day change in 21d down-vol share."""
    vel21 = _down_vol_share(close, volume, _TD_MON).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def udv_drv3_015_bear_candle_vol_share_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bear-candle volume share."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    s = _safe_div(bv, tv)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_016_down_up_avg_vol_ratio_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day down/up avg-vol ratio."""
    vel21 = _down_up_avg_vol_ratio(close, volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def udv_drv3_017_vol_asymmetry_index_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of the 21-day volume asymmetry index."""
    share = _down_vol_share(close, volume, _TD_MON)
    asym = (share - 0.5) * 2.0
    vel = asym.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_018_down_up_intensity_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down/up return-intensity ratio."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_019_obv_21d_change_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day OBV change."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg21 = obv.diff(_TD_MON)
    slp = _linslope(chg21, _TD_MON)
    return slp.diff(_TD_WEEK)


def udv_drv3_020_net_vol_ewm21_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM21 signed net volume."""
    signed = volume.where(close > close.shift(1), -volume)
    signed = signed.where(close != close.shift(1), 0.0)
    s = _ewm_mean(signed, _TD_MON)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_021_down_vol_share_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day down-vol share (long-run jerk in distribution)."""
    vel = _down_vol_share(close, volume, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_022_ret_wtd_vol_balance_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in net return-weighted volume balance."""
    ret = close.pct_change(1)
    signed_rv = ret.abs() * volume * np.sign(-ret).fillna(0)
    bal = _rolling_sum(signed_rv, _TD_MON)
    vel21 = bal.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def udv_drv3_023_down_vol_share_21d_ewm_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM21 down-vol share (smoothed jerk)."""
    ret = close.diff(1)
    dv_frac = volume.where(ret < 0, 0.0) / volume.replace(0, np.nan)
    s = _ewm_mean(dv_frac, _TD_MON)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def udv_drv3_024_down_up_avg_vol_ratio_21d_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day down/up avg-vol ratio over 21 days."""
    slp = _linslope(_down_up_avg_vol_ratio(close, volume, _TD_MON), _TD_MON)
    return slp.diff(_TD_WEEK)


def udv_drv3_025_cmf_21d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21-day CMF (jerk in money flow trend)."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf = _safe_div(_rolling_sum(mfv, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel21 = cmf.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

UP_DOWN_VOLUME_REGISTRY_3RD_DERIVATIVES = {
    "udv_drv3_001_down_vol_share_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_001_down_vol_share_21d_5d_diff_5d_diff},
    "udv_drv3_002_down_vol_share_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_002_down_vol_share_21d_21d_diff_5d_diff},
    "udv_drv3_003_down_up_avg_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_003_down_up_avg_vol_ratio_21d_5d_diff_5d_diff},
    "udv_drv3_004_net_vol_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_004_net_vol_21d_5d_diff_5d_diff},
    "udv_drv3_005_net_vol_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_005_net_vol_63d_21d_diff_5d_diff},
    "udv_drv3_006_down_vol_share_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_006_down_vol_share_63d_5d_diff_5d_diff},
    "udv_drv3_007_down_vol_share_21d_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_007_down_vol_share_21d_slope_63d_5d_diff},
    "udv_drv3_008_ret_wtd_down_up_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_008_ret_wtd_down_up_ratio_21d_5d_diff_5d_diff},
    "udv_drv3_009_obv_5d_diff_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_009_obv_5d_diff_slope_21d_5d_diff},
    "udv_drv3_010_cmf_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv3_010_cmf_21d_5d_diff_5d_diff},
    "udv_drv3_011_down_vol_share_21d_5d_diff_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_011_down_vol_share_21d_5d_diff_slope_21d_5d_diff},
    "udv_drv3_012_vol_wtd_down_up_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_012_vol_wtd_down_up_ratio_21d_5d_diff_5d_diff},
    "udv_drv3_013_net_vol_21d_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_013_net_vol_21d_slope_63d_5d_diff},
    "udv_drv3_014_down_vol_share_21d_21d_diff_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv3_014_down_vol_share_21d_21d_diff_slope_21d},
    "udv_drv3_015_bear_candle_vol_share_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "volume"], "func": udv_drv3_015_bear_candle_vol_share_21d_5d_diff_5d_diff},
    "udv_drv3_016_down_up_avg_vol_ratio_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_016_down_up_avg_vol_ratio_63d_21d_diff_5d_diff},
    "udv_drv3_017_vol_asymmetry_index_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_017_vol_asymmetry_index_21d_5d_diff_5d_diff},
    "udv_drv3_018_down_up_intensity_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_018_down_up_intensity_ratio_21d_5d_diff_5d_diff},
    "udv_drv3_019_obv_21d_change_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_019_obv_21d_change_slope_21d_5d_diff},
    "udv_drv3_020_net_vol_ewm21_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_020_net_vol_ewm21_5d_diff_5d_diff},
    "udv_drv3_021_down_vol_share_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_021_down_vol_share_252d_5d_diff_5d_diff},
    "udv_drv3_022_ret_wtd_vol_balance_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_022_ret_wtd_vol_balance_21d_21d_diff_5d_diff},
    "udv_drv3_023_down_vol_share_21d_ewm_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_023_down_vol_share_21d_ewm_5d_diff_5d_diff},
    "udv_drv3_024_down_up_avg_vol_ratio_21d_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv3_024_down_up_avg_vol_ratio_21d_slope_21d_5d_diff},
    "udv_drv3_025_cmf_21d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv3_025_cmf_21d_21d_diff_5d_diff},
}
