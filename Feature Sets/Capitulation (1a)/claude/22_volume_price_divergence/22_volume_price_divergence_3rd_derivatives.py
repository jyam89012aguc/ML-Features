"""
22_volume_price_divergence — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative volume-price divergence features —
acceleration of correlation velocity, jerk in divergence day counts, inflection
in vol-weighted decline signals, exhaustion/acceleration of divergence regimes.
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
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _rolling_corr(x: pd.Series, y: pd.Series, w: int) -> pd.Series:
    """Rolling Pearson correlation between x and y."""
    return x.rolling(w, min_periods=max(2, w // 2)).corr(y)


def _rolling_cov(x: pd.Series, y: pd.Series, w: int) -> pd.Series:
    """Rolling covariance between x and y."""
    return x.rolling(w, min_periods=max(2, w // 2)).cov(y)


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
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept.

def vpd_drv3_001_corr_vol_ret_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day corr(vol, ret) — acceleration of correlation velocity."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    vel = corr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_002_corr_vol_ret_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day-velocity of 21d corr(vol, ret) — jerk in monthly corr change."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    vel21 = corr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_003_corr_vol_ret_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day corr(vol, ret)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    vel21 = corr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_004_price_down_vol_up_count_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day divergence-day count — acceleration."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_005_down_ret_x_volnorm_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day sum(down_ret * vol_norm) — jerk in interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    vel = interaction.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_006_vol_on_down_frac_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-volume fraction — acceleration of down-vol share."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_007_cov_vol_ret_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cov(vol, ret) — acceleration of covariance change."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    vel = cov.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_008_vwap_decline_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(num, den)
    vel = vwap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_009_corr_vol_ret_21d_slope_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day corr(vol, ret) over 63d window."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    slp = _linslope(corr, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vpd_drv3_010_down_ret_x_volnorm_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day sum(down_ret * vol_norm)."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_QTR)
    vel21 = interaction.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_011_vol_ret_beta_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol-return beta — acceleration of beta change."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    var_r = _rolling_std(ret, _TD_MON) ** 2
    beta = _safe_div(cov, var_r)
    vel = beta.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_012_vol_slope_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OLS volume slope — volume slope acceleration."""
    vol_slope = _linslope(volume, _TD_MON)
    vel = vol_slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_013_divergence_composite_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day composite divergence score — jerk in divergence."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON) / _TD_MON
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_014_vol_on_down_frac_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down-volume fraction."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_015_vol_x_abs_ret_down_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_MON)
    vel = feat.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_016_corr_vol_ret_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5-day-velocity of 21-day corr(vol, ret)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    vel = corr.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vpd_drv3_017_price_down_vol_up_count_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day divergence-day count."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_018_down_vol_frac_21d_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day down-volume fraction."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def vpd_drv3_019_vwap_decline_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day vol-weighted avg return."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    vwap = _safe_div(num, den)
    vel21 = vwap.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_020_cov_vol_ret_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5-day-velocity of 21-day cov(vol, ret)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    vel = cov.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vpd_drv3_021_vol_ret_beta_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day vol-return beta."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    var_r = _rolling_std(ret, _TD_QTR) ** 2
    beta = _safe_div(cov, var_r)
    vel21 = beta.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vpd_drv3_022_vol_slope_minus_price_slope_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized (vol_slope - price_slope) divergence, 21d."""
    vol_slope = _linslope(volume, _TD_MON)
    price_slope = _linslope(close, _TD_MON)
    vol_std = _rolling_std(volume, _TD_MON).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    diverg = _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)
    vel = diverg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vpd_drv3_023_divergence_composite_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5-day-velocity of 21d composite divergence score."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON) / _TD_MON
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    vel = composite.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vpd_drv3_024_corr_vol_ret_63d_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day corr(vol, ret) over 63d window."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    slp = _linslope(corr, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vpd_drv3_025_vol_x_abs_ret_down_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_QTR)
    vel21 = feat.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PRICE_DIVERGENCE_REGISTRY_3RD_DERIVATIVES = {
    "vpd_drv3_001_corr_vol_ret_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_001_corr_vol_ret_21d_5d_diff_5d_diff},
    "vpd_drv3_002_corr_vol_ret_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_002_corr_vol_ret_21d_21d_diff_5d_diff},
    "vpd_drv3_003_corr_vol_ret_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_003_corr_vol_ret_63d_21d_diff_5d_diff},
    "vpd_drv3_004_price_down_vol_up_count_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_004_price_down_vol_up_count_21d_5d_diff_5d_diff},
    "vpd_drv3_005_down_ret_x_volnorm_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_005_down_ret_x_volnorm_21d_5d_diff_5d_diff},
    "vpd_drv3_006_vol_on_down_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_006_vol_on_down_frac_21d_5d_diff_5d_diff},
    "vpd_drv3_007_cov_vol_ret_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_007_cov_vol_ret_21d_5d_diff_5d_diff},
    "vpd_drv3_008_vwap_decline_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_008_vwap_decline_21d_5d_diff_5d_diff},
    "vpd_drv3_009_corr_vol_ret_21d_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_009_corr_vol_ret_21d_slope_63d_5d_diff},
    "vpd_drv3_010_down_ret_x_volnorm_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_010_down_ret_x_volnorm_63d_21d_diff_5d_diff},
    "vpd_drv3_011_vol_ret_beta_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_011_vol_ret_beta_21d_5d_diff_5d_diff},
    "vpd_drv3_012_vol_slope_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_012_vol_slope_21d_5d_diff_5d_diff},
    "vpd_drv3_013_divergence_composite_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_013_divergence_composite_21d_5d_diff_5d_diff},
    "vpd_drv3_014_vol_on_down_frac_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_014_vol_on_down_frac_63d_21d_diff_5d_diff},
    "vpd_drv3_015_vol_x_abs_ret_down_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_015_vol_x_abs_ret_down_21d_5d_diff_5d_diff},
    "vpd_drv3_016_corr_vol_ret_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv3_016_corr_vol_ret_21d_5d_diff_slope_21d},
    "vpd_drv3_017_price_down_vol_up_count_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_017_price_down_vol_up_count_63d_21d_diff_5d_diff},
    "vpd_drv3_018_down_vol_frac_21d_slope_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_018_down_vol_frac_21d_slope_5d_diff},
    "vpd_drv3_019_vwap_decline_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_019_vwap_decline_63d_21d_diff_5d_diff},
    "vpd_drv3_020_cov_vol_ret_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv3_020_cov_vol_ret_21d_5d_diff_slope_21d},
    "vpd_drv3_021_vol_ret_beta_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_021_vol_ret_beta_63d_21d_diff_5d_diff},
    "vpd_drv3_022_vol_slope_minus_price_slope_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_022_vol_slope_minus_price_slope_21d_5d_diff_5d_diff},
    "vpd_drv3_023_divergence_composite_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv3_023_divergence_composite_21d_5d_diff_slope_21d},
    "vpd_drv3_024_corr_vol_ret_63d_slope_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_024_corr_vol_ret_63d_slope_5d_diff},
    "vpd_drv3_025_vol_x_abs_ret_down_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv3_025_vol_x_abs_ret_down_63d_21d_diff_5d_diff},
}
