"""
20_up_down_volume — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base up/down volume balance features — velocity of direction-
        conditioned volume asymmetry shifting over time.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def udv_drv2_001_down_vol_share_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-vol share (velocity of distribution shift)."""
    return _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)


def udv_drv2_002_down_vol_share_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day down-vol share (monthly change in distribution dominance)."""
    return _down_vol_share(close, volume, _TD_MON).diff(_TD_MON)


def udv_drv2_003_down_up_avg_vol_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up avg-volume ratio."""
    return _down_up_avg_vol_ratio(close, volume, _TD_MON).diff(_TD_WEEK)


def udv_drv2_004_down_up_avg_vol_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down/up avg-volume ratio."""
    return _down_up_avg_vol_ratio(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_005_net_vol_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day net volume (velocity of accumulation/distribution)."""
    return _net_vol(close, volume, _TD_MON).diff(_TD_WEEK)


def udv_drv2_006_net_vol_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day net volume."""
    return _net_vol(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_007_obv_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day OBV change (trend in OBV velocity)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg5 = obv.diff(_TD_WEEK)
    return _linslope(chg5, _TD_MON)


def udv_drv2_008_down_vol_share_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day down-vol share."""
    return _down_vol_share(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_009_down_vol_share_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-vol share."""
    return _down_vol_share(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_010_ret_wtd_down_up_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day return-weighted down/up volume ratio."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    return ratio.diff(_TD_WEEK)


def udv_drv2_011_cmf_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day Chaikin Money Flow."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf = _safe_div(_rolling_sum(mfv, _TD_MON), _rolling_sum(volume, _TD_MON))
    return cmf.diff(_TD_WEEK)


def udv_drv2_012_cmf_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day Chaikin Money Flow."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    cmf = _safe_div(_rolling_sum(mfv, _TD_MON), _rolling_sum(volume, _TD_MON))
    return cmf.diff(_TD_MON)


def udv_drv2_013_down_vol_share_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-vol share over trailing 63 days."""
    return _linslope(_down_vol_share(close, volume, _TD_MON), _TD_QTR)


def udv_drv2_014_net_vol_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day net volume over trailing 63 days."""
    return _linslope(_net_vol(close, volume, _TD_MON), _TD_QTR)


def udv_drv2_015_vol_wtd_down_up_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-weighted down/up day ratio."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    wt_d = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    wt_u = _safe_div(volume, avg_vol).where(close > close.shift(1), 0.0)
    ratio = _safe_div(_rolling_sum(wt_d, _TD_MON), _rolling_sum(wt_u, _TD_MON))
    return ratio.diff(_TD_WEEK)


def udv_drv2_016_down_vol_share_21d_ewm_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21 down-vol share (smoothed velocity)."""
    ret = close.diff(1)
    dv_frac = volume.where(ret < 0, 0.0) / volume.replace(0, np.nan)
    s = _ewm_mean(dv_frac, _TD_MON)
    return s.diff(_TD_WEEK)


def udv_drv2_017_obv_21d_change_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day OBV change."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg21 = obv.diff(_TD_MON)
    return _linslope(chg21, _TD_MON)


def udv_drv2_018_down_up_intensity_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up return-intensity ratio."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), _TD_MON)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), _TD_MON)
    ratio = _safe_div(d_int, u_int)
    return ratio.diff(_TD_WEEK)


def udv_drv2_019_bear_candle_vol_share_21d_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day bear-candle volume share."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    s = _safe_div(bv, tv)
    return s.diff(_TD_WEEK)


def udv_drv2_020_net_vol_ewm21_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21 signed (net) volume."""
    signed = volume.where(close > close.shift(1), -volume)
    signed = signed.where(close != close.shift(1), 0.0)
    s = _ewm_mean(signed, _TD_MON)
    return s.diff(_TD_WEEK)


def udv_drv2_021_down_vol_share_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of 21d down-vol share (accel trend)."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def udv_drv2_022_down_up_avg_vol_ratio_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day down/up avg-volume ratio."""
    return _linslope(_down_up_avg_vol_ratio(close, volume, _TD_MON), _TD_MON)


def udv_drv2_023_down_vol_share_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day down-vol share (long-run distribution trend velocity)."""
    return _down_vol_share(close, volume, _TD_YEAR).diff(_TD_WEEK)


def udv_drv2_024_vol_asymmetry_index_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day volume asymmetry index."""
    share = _down_vol_share(close, volume, _TD_MON)
    asym = (share - 0.5) * 2.0
    return asym.diff(_TD_WEEK)


def udv_drv2_025_ret_wtd_vol_balance_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 21-day net return-weighted volume balance."""
    ret = close.pct_change(1)
    signed_rv = ret.abs() * volume * np.sign(-ret).fillna(0)
    bal = _rolling_sum(signed_rv, _TD_MON)
    return bal.diff(_TD_MON)


# ── 2nd-Derivative Feature Functions (drv2_026-075) ──────────────────────────

def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-balance volume helper."""
    return (np.sign(close.diff(1)).fillna(0) * volume).cumsum()


def _signed_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-day volume positive, down-day volume negative, unchanged 0."""
    signed = volume.where(close > close.shift(1), -volume)
    return signed.where(close != close.shift(1), 0.0)


def _cmf(close: pd.Series, high: pd.Series, low: pd.Series,
         volume: pd.Series, w: int) -> pd.Series:
    """Rolling Chaikin Money Flow over w periods."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    mfv = mfm * volume
    return _safe_div(_rolling_sum(mfv, w), _rolling_sum(volume, w))


def _vol_wtd_down_up_ratio(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling volume-weighted down-day vs up-day volume ratio."""
    avg_vol = _rolling_mean(volume, w)
    wt_d = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    wt_u = _safe_div(volume, avg_vol).where(close > close.shift(1), 0.0)
    return _safe_div(_rolling_sum(wt_d, w), _rolling_sum(wt_u, w))


def _ret_intensity_ratio(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling down-day vs up-day return-weighted volume intensity ratio."""
    ret = close.pct_change(1)
    d_int = _rolling_sum((ret.abs() * volume).where(ret < 0, 0.0), w)
    u_int = _rolling_sum((ret.abs() * volume).where(ret > 0, 0.0), w)
    return _safe_div(d_int, u_int)


def _ret_wtd_vol_balance(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling net return-weighted volume balance (positive = net selling)."""
    ret = close.pct_change(1)
    signed_rv = ret.abs() * volume * np.sign(-ret).fillna(0)
    return _rolling_sum(signed_rv, w)


def udv_drv2_026_down_vol_share_126d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day down-vol share."""
    return _down_vol_share(close, volume, _TD_HALF).diff(_TD_WEEK)


def udv_drv2_027_down_vol_share_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day down-vol share."""
    return _down_vol_share(close, volume, _TD_HALF).diff(_TD_MON)


def udv_drv2_028_net_vol_126d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day net volume."""
    return _net_vol(close, volume, _TD_HALF).diff(_TD_WEEK)


def udv_drv2_029_net_vol_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day net volume."""
    return _net_vol(close, volume, _TD_HALF).diff(_TD_MON)


def udv_drv2_030_down_up_avg_vol_ratio_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day down/up avg-volume ratio."""
    return _down_up_avg_vol_ratio(close, volume, _TD_MON).diff(_TD_MON)


def udv_drv2_031_down_up_avg_vol_ratio_126d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day down/up avg-volume ratio."""
    return _down_up_avg_vol_ratio(close, volume, _TD_HALF).diff(_TD_WEEK)


def udv_drv2_032_down_up_avg_vol_ratio_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day down/up avg-volume ratio."""
    return _down_up_avg_vol_ratio(close, volume, _TD_HALF).diff(_TD_MON)


def udv_drv2_033_net_vol_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day net volume over trailing 21 days."""
    return _linslope(_net_vol(close, volume, _TD_MON), _TD_MON)


def udv_drv2_034_down_vol_share_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-vol share over trailing 21 days."""
    return _linslope(_down_vol_share(close, volume, _TD_MON), _TD_MON)


def udv_drv2_035_down_vol_share_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day down-vol share over trailing 63 days."""
    return _linslope(_down_vol_share(close, volume, _TD_QTR), _TD_QTR)


def udv_drv2_036_down_vol_share_63d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day down-vol share over trailing 21 days."""
    return _linslope(_down_vol_share(close, volume, _TD_QTR), _TD_MON)


def udv_drv2_037_obv_21d_change_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OBV change."""
    return _obv(close, volume).diff(_TD_MON).diff(_TD_WEEK)


def udv_drv2_038_obv_63d_change_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day OBV change."""
    return _obv(close, volume).diff(_TD_QTR).diff(_TD_WEEK)


def udv_drv2_039_obv_126d_change_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 126-day OBV change."""
    return _obv(close, volume).diff(_TD_HALF).diff(_TD_WEEK)


def udv_drv2_040_vol_wtd_down_up_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume-weighted down/up day ratio."""
    return _vol_wtd_down_up_ratio(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_041_vol_wtd_down_up_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume-weighted down/up day ratio."""
    return _vol_wtd_down_up_ratio(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_042_down_vol_share_21d_ewm_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of EWM21 down-vol share."""
    ret = close.diff(1)
    dv_frac = volume.where(ret < 0, 0.0) / volume.replace(0, np.nan)
    return _ewm_mean(dv_frac, _TD_MON).diff(_TD_MON)


def udv_drv2_043_net_vol_ewm63_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM63 signed (net) volume."""
    return _ewm_mean(_signed_vol(close, volume), _TD_QTR).diff(_TD_WEEK)


def udv_drv2_044_ret_wtd_down_up_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day return-weighted down/up volume ratio."""
    return _ret_intensity_ratio(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_045_ret_wtd_down_up_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day return-weighted down/up volume ratio."""
    return _ret_intensity_ratio(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_046_cmf_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day Chaikin Money Flow."""
    return _cmf(close, high, low, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_047_cmf_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day Chaikin Money Flow."""
    return _cmf(close, high, low, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_048_ad_line_21d_change_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day Accumulation/Distribution line change."""
    rng = (high - low).replace(0, np.nan)
    mfm = _safe_div((close - low) - (high - close), rng)
    ad = (mfm * volume).cumsum()
    return ad.diff(_TD_MON).diff(_TD_WEEK)


def udv_drv2_049_down_vol_share_21d_5d_diff_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 smoothing of the 5-day diff of 21-day down-vol share."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_MON)


def udv_drv2_050_down_up_intensity_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day down/up return-intensity ratio."""
    return _ret_intensity_ratio(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_051_down_up_intensity_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down/up return-intensity ratio."""
    return _ret_intensity_ratio(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_052_down_vol_share_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day down-vol share."""
    return _down_vol_share(close, volume, _TD_YEAR).diff(_TD_MON)


def udv_drv2_053_net_vol_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day net volume over trailing 63 days."""
    return _linslope(_net_vol(close, volume, _TD_QTR), _TD_QTR)


def udv_drv2_054_down_vol_share_21d_21d_diff_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 smoothing of the 21-day diff of 21-day down-vol share."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_MON)
    return _ewm_mean(vel, _TD_MON)


def udv_drv2_055_bear_candle_vol_share_21d_21d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day bear-candle volume share."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(bv, tv).diff(_TD_MON)


def udv_drv2_056_bear_candle_vol_share_63d_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day bear-candle volume share."""
    bv = _rolling_sum(volume.where(close < open, 0.0), _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(bv, tv).diff(_TD_WEEK)


def udv_drv2_057_gap_down_vol_share_21d_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day share of volume on gap-down opens."""
    gv = _rolling_sum(volume.where(open < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(gv, tv).diff(_TD_WEEK)


def udv_drv2_058_down_vol_share_21d_slope_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-vol share over trailing 126 days."""
    return _linslope(_down_vol_share(close, volume, _TD_MON), _TD_HALF)


def udv_drv2_059_net_vol_21d_5d_diff_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 smoothing of the 5-day diff of 21-day net volume."""
    return _ewm_mean(_net_vol(close, volume, _TD_MON).diff(_TD_WEEK), _TD_MON)


def udv_drv2_060_down_up_avg_vol_ratio_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down/up avg-volume ratio over trailing 63 days."""
    return _linslope(_down_up_avg_vol_ratio(close, volume, _TD_MON), _TD_QTR)


def udv_drv2_061_obv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of OBV over trailing 63 days."""
    return _linslope(_obv(close, volume), _TD_QTR)


def udv_drv2_062_obv_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of OBV over trailing 21 days."""
    return _linslope(_obv(close, volume), _TD_MON)


def udv_drv2_063_vol_asymmetry_index_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day volume asymmetry index."""
    asym = (_down_vol_share(close, volume, _TD_QTR) - 0.5) * 2.0
    return asym.diff(_TD_WEEK)


def udv_drv2_064_vol_asymmetry_index_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 21-day volume asymmetry index."""
    asym = (_down_vol_share(close, volume, _TD_MON) - 0.5) * 2.0
    return asym.diff(_TD_MON)


def udv_drv2_065_down_vol_share_21d_vs_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21-day minus 63-day) down-vol share spread."""
    spread = (_down_vol_share(close, volume, _TD_MON)
              - _down_vol_share(close, volume, _TD_QTR))
    return spread.diff(_TD_WEEK)


def udv_drv2_066_net_vol_21d_slope_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day net volume over trailing 126 days."""
    return _linslope(_net_vol(close, volume, _TD_MON), _TD_HALF)


def udv_drv2_067_ret_wtd_vol_balance_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day net return-weighted volume balance."""
    return _ret_wtd_vol_balance(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_068_ret_wtd_vol_balance_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day net return-weighted volume balance."""
    return _ret_wtd_vol_balance(close, volume, _TD_QTR).diff(_TD_MON)


def udv_drv2_069_down_vol_share_21d_5d_diff_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 5-day diff of 21-day down-vol share."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_QTR)


def udv_drv2_070_net_vol_ewm21_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of EWM21 signed (net) volume."""
    return _ewm_mean(_signed_vol(close, volume), _TD_MON).diff(_TD_MON)


def udv_drv2_071_down_vol_share_21d_abs_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute 5-day diff of 21-day down-vol share (unsigned velocity)."""
    return _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK).abs()


def udv_drv2_072_cmf_21d_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Chaikin Money Flow over trailing 63 days."""
    return _linslope(_cmf(close, high, low, volume, _TD_MON), _TD_QTR)


def udv_drv2_073_net_vol_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day net volume."""
    return _net_vol(close, volume, _TD_QTR).diff(_TD_WEEK)


def udv_drv2_074_down_up_avg_vol_ratio_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day down/up avg-volume ratio over trailing 63 days."""
    return _linslope(_down_up_avg_vol_ratio(close, volume, _TD_QTR), _TD_QTR)


def udv_drv2_075_down_vol_share_21d_5d_diff_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-252-day percentile rank of the 5-day diff of 21d down-vol share."""
    vel = _down_vol_share(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.rolling(_TD_YEAR, min_periods=max(2, _TD_MON)).apply(
        lambda x: float((x <= x[-1]).mean()), raw=True)


# ── Registry ──────────────────────────────────────────────────────────────────

UP_DOWN_VOLUME_REGISTRY_2ND_DERIVATIVES = {
    "udv_drv2_001_down_vol_share_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_001_down_vol_share_21d_5d_diff},
    "udv_drv2_002_down_vol_share_21d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_002_down_vol_share_21d_21d_diff},
    "udv_drv2_003_down_up_avg_vol_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_003_down_up_avg_vol_ratio_21d_5d_diff},
    "udv_drv2_004_down_up_avg_vol_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_004_down_up_avg_vol_ratio_63d_21d_diff},
    "udv_drv2_005_net_vol_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_005_net_vol_21d_5d_diff},
    "udv_drv2_006_net_vol_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_006_net_vol_63d_21d_diff},
    "udv_drv2_007_obv_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_007_obv_5d_diff_slope_21d},
    "udv_drv2_008_down_vol_share_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_008_down_vol_share_63d_5d_diff},
    "udv_drv2_009_down_vol_share_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_009_down_vol_share_63d_21d_diff},
    "udv_drv2_010_ret_wtd_down_up_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_010_ret_wtd_down_up_ratio_21d_5d_diff},
    "udv_drv2_011_cmf_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_011_cmf_21d_5d_diff},
    "udv_drv2_012_cmf_21d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_012_cmf_21d_21d_diff},
    "udv_drv2_013_down_vol_share_21d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_013_down_vol_share_21d_slope_63d},
    "udv_drv2_014_net_vol_21d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_014_net_vol_21d_slope_63d},
    "udv_drv2_015_vol_wtd_down_up_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_015_vol_wtd_down_up_ratio_21d_5d_diff},
    "udv_drv2_016_down_vol_share_21d_ewm_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_016_down_vol_share_21d_ewm_5d_diff},
    "udv_drv2_017_obv_21d_change_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_017_obv_21d_change_slope_21d},
    "udv_drv2_018_down_up_intensity_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_018_down_up_intensity_ratio_21d_5d_diff},
    "udv_drv2_019_bear_candle_vol_share_21d_5d_diff": {"inputs": ["close", "open", "volume"], "func": udv_drv2_019_bear_candle_vol_share_21d_5d_diff},
    "udv_drv2_020_net_vol_ewm21_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_020_net_vol_ewm21_5d_diff},
    "udv_drv2_021_down_vol_share_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_021_down_vol_share_21d_5d_diff_slope_21d},
    "udv_drv2_022_down_up_avg_vol_ratio_21d_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_022_down_up_avg_vol_ratio_21d_slope_21d},
    "udv_drv2_023_down_vol_share_252d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_023_down_vol_share_252d_5d_diff},
    "udv_drv2_024_vol_asymmetry_index_21d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_024_vol_asymmetry_index_21d_5d_diff},
    "udv_drv2_025_ret_wtd_vol_balance_21d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_025_ret_wtd_vol_balance_21d_21d_diff},
    "udv_drv2_026_down_vol_share_126d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_026_down_vol_share_126d_5d_diff},
    "udv_drv2_027_down_vol_share_126d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_027_down_vol_share_126d_21d_diff},
    "udv_drv2_028_net_vol_126d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_028_net_vol_126d_5d_diff},
    "udv_drv2_029_net_vol_126d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_029_net_vol_126d_21d_diff},
    "udv_drv2_030_down_up_avg_vol_ratio_21d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_030_down_up_avg_vol_ratio_21d_21d_diff},
    "udv_drv2_031_down_up_avg_vol_ratio_126d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_031_down_up_avg_vol_ratio_126d_5d_diff},
    "udv_drv2_032_down_up_avg_vol_ratio_126d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_032_down_up_avg_vol_ratio_126d_21d_diff},
    "udv_drv2_033_net_vol_21d_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_033_net_vol_21d_slope_21d},
    "udv_drv2_034_down_vol_share_21d_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_034_down_vol_share_21d_slope_21d},
    "udv_drv2_035_down_vol_share_63d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_035_down_vol_share_63d_slope_63d},
    "udv_drv2_036_down_vol_share_63d_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_036_down_vol_share_63d_slope_21d},
    "udv_drv2_037_obv_21d_change_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_037_obv_21d_change_5d_diff},
    "udv_drv2_038_obv_63d_change_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_038_obv_63d_change_5d_diff},
    "udv_drv2_039_obv_126d_change_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_039_obv_126d_change_5d_diff},
    "udv_drv2_040_vol_wtd_down_up_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_040_vol_wtd_down_up_ratio_63d_5d_diff},
    "udv_drv2_041_vol_wtd_down_up_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_041_vol_wtd_down_up_ratio_63d_21d_diff},
    "udv_drv2_042_down_vol_share_21d_ewm_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_042_down_vol_share_21d_ewm_21d_diff},
    "udv_drv2_043_net_vol_ewm63_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_043_net_vol_ewm63_5d_diff},
    "udv_drv2_044_ret_wtd_down_up_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_044_ret_wtd_down_up_ratio_63d_5d_diff},
    "udv_drv2_045_ret_wtd_down_up_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_045_ret_wtd_down_up_ratio_63d_21d_diff},
    "udv_drv2_046_cmf_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_046_cmf_63d_5d_diff},
    "udv_drv2_047_cmf_63d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_047_cmf_63d_21d_diff},
    "udv_drv2_048_ad_line_21d_change_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_048_ad_line_21d_change_5d_diff},
    "udv_drv2_049_down_vol_share_21d_5d_diff_ewm21": {"inputs": ["close", "volume"], "func": udv_drv2_049_down_vol_share_21d_5d_diff_ewm21},
    "udv_drv2_050_down_up_intensity_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_050_down_up_intensity_ratio_63d_5d_diff},
    "udv_drv2_051_down_up_intensity_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_051_down_up_intensity_ratio_63d_21d_diff},
    "udv_drv2_052_down_vol_share_252d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_052_down_vol_share_252d_21d_diff},
    "udv_drv2_053_net_vol_63d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_053_net_vol_63d_slope_63d},
    "udv_drv2_054_down_vol_share_21d_21d_diff_ewm21": {"inputs": ["close", "volume"], "func": udv_drv2_054_down_vol_share_21d_21d_diff_ewm21},
    "udv_drv2_055_bear_candle_vol_share_21d_21d_diff": {"inputs": ["close", "open", "volume"], "func": udv_drv2_055_bear_candle_vol_share_21d_21d_diff},
    "udv_drv2_056_bear_candle_vol_share_63d_5d_diff": {"inputs": ["close", "open", "volume"], "func": udv_drv2_056_bear_candle_vol_share_63d_5d_diff},
    "udv_drv2_057_gap_down_vol_share_21d_5d_diff": {"inputs": ["close", "open", "volume"], "func": udv_drv2_057_gap_down_vol_share_21d_5d_diff},
    "udv_drv2_058_down_vol_share_21d_slope_126d": {"inputs": ["close", "volume"], "func": udv_drv2_058_down_vol_share_21d_slope_126d},
    "udv_drv2_059_net_vol_21d_5d_diff_ewm21": {"inputs": ["close", "volume"], "func": udv_drv2_059_net_vol_21d_5d_diff_ewm21},
    "udv_drv2_060_down_up_avg_vol_ratio_21d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_060_down_up_avg_vol_ratio_21d_slope_63d},
    "udv_drv2_061_obv_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_061_obv_slope_63d},
    "udv_drv2_062_obv_slope_21d": {"inputs": ["close", "volume"], "func": udv_drv2_062_obv_slope_21d},
    "udv_drv2_063_vol_asymmetry_index_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_063_vol_asymmetry_index_63d_5d_diff},
    "udv_drv2_064_vol_asymmetry_index_21d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_064_vol_asymmetry_index_21d_21d_diff},
    "udv_drv2_065_down_vol_share_21d_vs_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_065_down_vol_share_21d_vs_63d_5d_diff},
    "udv_drv2_066_net_vol_21d_slope_126d": {"inputs": ["close", "volume"], "func": udv_drv2_066_net_vol_21d_slope_126d},
    "udv_drv2_067_ret_wtd_vol_balance_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_067_ret_wtd_vol_balance_63d_5d_diff},
    "udv_drv2_068_ret_wtd_vol_balance_63d_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_068_ret_wtd_vol_balance_63d_21d_diff},
    "udv_drv2_069_down_vol_share_21d_5d_diff_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_069_down_vol_share_21d_5d_diff_slope_63d},
    "udv_drv2_070_net_vol_ewm21_21d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_070_net_vol_ewm21_21d_diff},
    "udv_drv2_071_down_vol_share_21d_abs_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_071_down_vol_share_21d_abs_5d_diff},
    "udv_drv2_072_cmf_21d_slope_63d": {"inputs": ["close", "high", "low", "volume"], "func": udv_drv2_072_cmf_21d_slope_63d},
    "udv_drv2_073_net_vol_63d_5d_diff": {"inputs": ["close", "volume"], "func": udv_drv2_073_net_vol_63d_5d_diff},
    "udv_drv2_074_down_up_avg_vol_ratio_63d_slope_63d": {"inputs": ["close", "volume"], "func": udv_drv2_074_down_up_avg_vol_ratio_63d_slope_63d},
    "udv_drv2_075_down_vol_share_21d_5d_diff_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_drv2_075_down_vol_share_21d_5d_diff_pct_rank_252d},
}
