"""
22_volume_price_divergence — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base volume-price divergence features — velocity of
correlation shifts, acceleration of divergence day counts, diff/slope of
signed interaction terms and volume-weighted decline metrics.
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


def _log_ret(s: pd.Series) -> pd.Series:
    """Daily log return (backward-looking)."""
    return _log_safe(s).diff(1)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vpd_drv2_001_corr_vol_ret_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day corr(volume, return) — velocity of correlation shift."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return corr.diff(_TD_WEEK)


def vpd_drv2_002_corr_vol_ret_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day corr(volume, return) — monthly velocity."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return corr.diff(_TD_MON)


def vpd_drv2_003_corr_vol_ret_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day corr(volume, return) — monthly change in medium-term corr."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    return corr.diff(_TD_MON)


def vpd_drv2_004_price_down_vol_up_count_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day divergence-day count."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def vpd_drv2_005_price_down_vol_up_count_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day divergence-day count."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def vpd_drv2_006_down_ret_x_volnorm_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day sum(down_ret * vol_norm) interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    return interaction.diff(_TD_WEEK)


def vpd_drv2_007_down_ret_x_volnorm_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day sum(down_ret * vol_norm) interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_QTR)
    return interaction.diff(_TD_MON)


def vpd_drv2_008_vol_on_down_frac_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of volume on down-price days."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    return frac.diff(_TD_WEEK)


def vpd_drv2_009_vol_on_down_frac_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction of volume on down-price days."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    return frac.diff(_TD_MON)


def vpd_drv2_010_cov_vol_ret_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day cov(volume, return)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    return cov.diff(_TD_WEEK)


def vpd_drv2_011_cov_vol_ret_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day cov(volume, return)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    return cov.diff(_TD_MON)


def vpd_drv2_012_vwap_decline_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(num, den)
    return vwap.diff(_TD_WEEK)


def vpd_drv2_013_vwap_decline_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    vwap = _safe_div(num, den)
    return vwap.diff(_TD_MON)


def vpd_drv2_014_corr_vol_ret_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day corr(vol, ret) over trailing 63-day window."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return _linslope(corr, _TD_QTR)


def vpd_drv2_015_corr_vol_ret_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day corr(vol, ret) over trailing 63-day window."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    return _linslope(corr, _TD_QTR)


def vpd_drv2_016_newlow_vol_flag_21_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21d-new-low & high-vol) flag."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < roll_min) & (volume > avg_vol)).astype(float)
    return flag.diff(_TD_WEEK)


def vpd_drv2_017_vol_ret_beta_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    var_r = _rolling_std(ret, _TD_MON) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_WEEK)


def vpd_drv2_018_vol_ret_beta_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    var_r = _rolling_std(ret, _TD_QTR) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_MON)


def vpd_drv2_019_vol_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS volume slope."""
    vol_slope = _linslope(volume, _TD_MON)
    return vol_slope.diff(_TD_WEEK)


def vpd_drv2_020_vol_slope_minus_price_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of normalized (vol_slope - price_slope) divergence, 21d window."""
    vol_slope = _linslope(volume, _TD_MON)
    price_slope = _linslope(close, _TD_MON)
    vol_std = _rolling_std(volume, _TD_MON).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    diverg = _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)
    return diverg.diff(_TD_WEEK)


def vpd_drv2_021_down_vol_frac_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-volume fraction over 21-day rolling window."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    return _linslope(frac, _TD_MON)


def vpd_drv2_022_divergence_composite_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day composite divergence score."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON) / _TD_MON
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    return composite.diff(_TD_WEEK)


def vpd_drv2_023_vol_x_abs_ret_down_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_MON)
    return feat.diff(_TD_WEEK)


def vpd_drv2_024_vol_x_abs_ret_down_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_QTR)
    return feat.diff(_TD_MON)


def vpd_drv2_025_divergence_days_frac_down_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of (divergence days / down days) fraction over 21-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_MON)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON)
    frac = _safe_div(div_days, down_days)
    return _linslope(frac, _TD_MON)


# --- New 2nd derivatives (drv2_026-075) ---

def vpd_drv2_026_corr_vol_ret_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day corr(volume, return) — monthly change in half-year corr."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_HALF)
    return corr.diff(_TD_MON)


def vpd_drv2_027_corr_vol_ret_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day corr(vol, ret) over trailing 21-day window."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return _linslope(corr, _TD_MON)


def vpd_drv2_028_cov_vol_ret_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day cov(volume, return)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    return cov.diff(_TD_WEEK)


def vpd_drv2_029_vol_on_down_frac_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day fraction of volume on down-price days."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    return frac.diff(_TD_MON)


def vpd_drv2_030_vwap_decline_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day volume-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_YEAR)
    den = _rolling_sum(volume, _TD_YEAR)
    vwap = _safe_div(num, den)
    return vwap.diff(_TD_MON)


def vpd_drv2_031_down_ret_x_volnorm_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day sum(down_ret * vol_norm) interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_YEAR)
    return interaction.diff(_TD_MON)


def vpd_drv2_032_corr_vol_ret_21d_63d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day corr(volume, return) — quarterly change in corr."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return corr.diff(_TD_QTR)


def vpd_drv2_033_corr_vol_ret_63d_63d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day diff of 63-day corr(volume, return)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    return corr.diff(_TD_QTR)


def vpd_drv2_034_vol_ret_beta_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    var_r = _rolling_std(ret, _TD_MON) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_MON)


def vpd_drv2_035_vol_ret_beta_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_HALF)
    var_r = _rolling_std(ret, _TD_HALF) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_MON)


def vpd_drv2_036_vol_slope_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS volume slope."""
    vol_slope = _linslope(volume, _TD_QTR)
    return vol_slope.diff(_TD_WEEK)


def vpd_drv2_037_price_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS price slope (acceleration of price trend)."""
    price_slope = _linslope(close, _TD_MON)
    return price_slope.diff(_TD_WEEK)


def vpd_drv2_038_price_slope_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day OLS price slope."""
    price_slope = _linslope(close, _TD_QTR)
    return price_slope.diff(_TD_MON)


def vpd_drv2_039_vol_slope_minus_price_slope_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of normalized (vol_slope - price_slope) divergence, 63d window."""
    vol_slope = _linslope(volume, _TD_QTR)
    price_slope = _linslope(close, _TD_QTR)
    vol_std = _rolling_std(volume, _TD_QTR).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_QTR).clip(lower=_EPS)
    diverg = _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)
    return diverg.diff(_TD_WEEK)


def vpd_drv2_040_divergence_composite_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day composite divergence score."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR) / _TD_QTR
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    return composite.diff(_TD_WEEK)


def vpd_drv2_041_price_down_vol_up_count_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day divergence-day count."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_YEAR)
    return cnt.diff(_TD_MON)


def vpd_drv2_042_vol_x_abs_ret_down_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_MON)
    return feat.diff(_TD_MON)


def vpd_drv2_043_vol_x_abs_ret_down_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_YEAR)
    return feat.diff(_TD_MON)


def vpd_drv2_044_down_vol_frac_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-volume fraction over 63-day rolling window."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    return _linslope(frac, _TD_QTR)


def vpd_drv2_045_corr_vol_ret_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day corr(vol, ret) over trailing 21-day window (short trend)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return _linslope(corr, _TD_MON)


def vpd_drv2_046_cov_vol_ret_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day cov(vol, ret) over trailing 21-day window."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    return _linslope(cov, _TD_MON)


def vpd_drv2_047_cov_vol_ret_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day cov(vol, ret) over trailing 63-day window."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    return _linslope(cov, _TD_QTR)


def vpd_drv2_048_newlow21_vol_rising_count_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of (21d-new-low + high-vol) days over trailing 63-day."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < roll_min) & (volume > avg_vol)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_WEEK)


def vpd_drv2_049_vol_surge_on_price_drop_count_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of (ret < -1% and vol > 1.5x avg) days in 63d window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((ret < -0.01) & (volume > 1.5 * avg_vol)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_WEEK)


def vpd_drv2_050_vol_ewm5_vs_ewm21_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM(5)/EWM(21) volume ratio (velocity of short-term vol surge)."""
    fast = _ewm_mean(volume, _TD_WEEK)
    slow = _ewm_mean(volume, _TD_MON)
    ratio = _safe_div(fast, slow)
    return ratio.diff(_TD_WEEK)


def vpd_drv2_051_vol_ewm21_vs_ewm63_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM(21)/EWM(63) volume ratio."""
    fast = _ewm_mean(volume, _TD_MON)
    slow = _ewm_mean(volume, _TD_QTR)
    ratio = _safe_div(fast, slow)
    return ratio.diff(_TD_WEEK)


def vpd_drv2_052_down_vwap_vs_up_vwap_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day ratio of vol-weighted down-day vs up-day return."""
    ret = _daily_ret(close)
    d_v = volume.where(ret < 0, np.nan)
    u_v = volume.where(ret > 0, np.nan)
    d_num = _rolling_sum((ret.where(ret < 0, np.nan) * d_v).fillna(0), _TD_MON)
    d_den = _rolling_sum(d_v.fillna(0), _TD_MON)
    u_num = _rolling_sum((ret.where(ret > 0, np.nan) * u_v).fillna(0), _TD_MON)
    u_den = _rolling_sum(u_v.fillna(0), _TD_MON)
    ratio = _safe_div(_safe_div(d_num, d_den), _safe_div(u_num, u_den).abs().clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vpd_drv2_053_vol_on_down_vs_up_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day ratio of avg vol on down days to avg vol on up days."""
    ret = _daily_ret(close)
    down_avg = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up_avg = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(down_avg, up_avg)
    return ratio.diff(_TD_WEEK)


def vpd_drv2_054_vol_price_divergence_composite_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day composite divergence score."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR) / _TD_QTR
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    return composite.diff(_TD_MON)


def vpd_drv2_055_corr_vol_close_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day corr(volume, close price)."""
    corr = _rolling_corr(volume, close, _TD_MON)
    return corr.diff(_TD_WEEK)


def vpd_drv2_056_corr_vol_close_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day corr(volume, close price)."""
    corr = _rolling_corr(volume, close, _TD_QTR)
    return corr.diff(_TD_MON)


def vpd_drv2_057_corr_vol_logret_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day corr(volume, log return)."""
    lret = _log_ret(close)
    corr = _rolling_corr(volume, lret, _TD_MON)
    return corr.diff(_TD_WEEK)


def vpd_drv2_058_corr_vol_logret_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day corr(volume, log return)."""
    lret = _log_ret(close)
    corr = _rolling_corr(volume, lret, _TD_QTR)
    return corr.diff(_TD_MON)


def vpd_drv2_059_vol_x_abs_ret_down_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day sum(vol * abs(ret)) on down days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    feat = _rolling_sum(intensity, _TD_QTR)
    return feat.diff(_TD_WEEK)


def vpd_drv2_060_divergence_days_frac_down_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of (divergence days / down days) fraction over 63-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_QTR)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR)
    frac = _safe_div(div_days, down_days)
    return frac.diff(_TD_MON)


def vpd_drv2_061_divergence_days_frac_down_63d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of (divergence days / down days) fraction over 63-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_QTR)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR)
    frac = _safe_div(div_days, down_days)
    return _linslope(frac, _TD_QTR)


def vpd_drv2_062_vol_ret_beta_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    var_r = _rolling_std(ret, _TD_QTR) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_WEEK)


def vpd_drv2_063_vol_ret_beta_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day OLS beta of volume on daily return."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_YEAR)
    var_r = _rolling_std(ret, _TD_YEAR) ** 2
    beta = _safe_div(cov, var_r)
    return beta.diff(_TD_MON)


def vpd_drv2_064_vol_on_down_frac_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day fraction of volume on down-price days."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    return frac.diff(_TD_MON)


def vpd_drv2_065_cov_vol_logret_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day cov(volume, log return)."""
    lret = _log_ret(close)
    cov = _rolling_cov(volume, lret, _TD_MON)
    return cov.diff(_TD_WEEK)


def vpd_drv2_066_cov_vol_logret_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day cov(volume, log return)."""
    lret = _log_ret(close)
    cov = _rolling_cov(volume, lret, _TD_QTR)
    return cov.diff(_TD_MON)


def vpd_drv2_067_vol_weighted_cum_decline_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day vol-weighted cumulative log return."""
    lret = _log_ret(close)
    num = _rolling_sum(lret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    vw = _safe_div(num, den)
    return vw.diff(_TD_WEEK)


def vpd_drv2_068_vol_weighted_cum_decline_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day vol-weighted cumulative log return."""
    lret = _log_ret(close)
    num = _rolling_sum(lret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    vw = _safe_div(num, den)
    return vw.diff(_TD_MON)


def vpd_drv2_069_down_ret_x_volnorm_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day sum(down_ret * vol_norm) interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_HALF)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_HALF)
    return interaction.diff(_TD_MON)


def vpd_drv2_070_corr_vol_ret_21d_ewm21_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of daily (vol * ret) product."""
    ret = _daily_ret(close)
    prod = volume * ret
    ewm_prod = _ewm_mean(prod, _TD_MON)
    return ewm_prod.diff(_TD_WEEK)


def vpd_drv2_071_down_logret_x_volnorm_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day sum(down_logret * vol_norm)."""
    lret = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    feat = _rolling_sum((lret * vol_norm).where(lret < 0, 0.0), _TD_MON)
    return feat.diff(_TD_WEEK)


def vpd_drv2_072_down_logret_x_volnorm_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day sum(down_logret * vol_norm)."""
    lret = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    feat = _rolling_sum((lret * vol_norm).where(lret < 0, 0.0), _TD_QTR)
    return feat.diff(_TD_MON)


def vpd_drv2_073_vol_price_divergence_composite_126d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day composite divergence score."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_HALF)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_HALF) / _TD_HALF
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_HALF),
        _rolling_sum(volume, _TD_HALF)
    )
    composite = (neg_corr + div_frac + dv_frac) / 3.0
    return composite.diff(_TD_MON)


def vpd_drv2_074_price_down_vol_up_count_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day divergence-day count."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_MON)


def vpd_drv2_075_vol_surge_on_price_drop_count_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of count of (ret < -1% and vol > 1.5x avg) days in 252d window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((ret < -0.01) & (volume > 1.5 * avg_vol)).astype(float)
    cnt = _rolling_sum(flag, _TD_YEAR)
    return cnt.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PRICE_DIVERGENCE_REGISTRY_2ND_DERIVATIVES = {
    "vpd_drv2_001_corr_vol_ret_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_001_corr_vol_ret_21d_5d_diff},
    "vpd_drv2_002_corr_vol_ret_21d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_002_corr_vol_ret_21d_21d_diff},
    "vpd_drv2_003_corr_vol_ret_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_003_corr_vol_ret_63d_21d_diff},
    "vpd_drv2_004_price_down_vol_up_count_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_004_price_down_vol_up_count_21d_5d_diff},
    "vpd_drv2_005_price_down_vol_up_count_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_005_price_down_vol_up_count_63d_21d_diff},
    "vpd_drv2_006_down_ret_x_volnorm_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_006_down_ret_x_volnorm_21d_5d_diff},
    "vpd_drv2_007_down_ret_x_volnorm_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_007_down_ret_x_volnorm_63d_21d_diff},
    "vpd_drv2_008_vol_on_down_frac_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_008_vol_on_down_frac_21d_5d_diff},
    "vpd_drv2_009_vol_on_down_frac_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_009_vol_on_down_frac_63d_21d_diff},
    "vpd_drv2_010_cov_vol_ret_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_010_cov_vol_ret_21d_5d_diff},
    "vpd_drv2_011_cov_vol_ret_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_011_cov_vol_ret_63d_21d_diff},
    "vpd_drv2_012_vwap_decline_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_012_vwap_decline_21d_5d_diff},
    "vpd_drv2_013_vwap_decline_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_013_vwap_decline_63d_21d_diff},
    "vpd_drv2_014_corr_vol_ret_21d_slope_63d": {"inputs": ["close", "volume"], "func": vpd_drv2_014_corr_vol_ret_21d_slope_63d},
    "vpd_drv2_015_corr_vol_ret_63d_slope_63d": {"inputs": ["close", "volume"], "func": vpd_drv2_015_corr_vol_ret_63d_slope_63d},
    "vpd_drv2_016_newlow_vol_flag_21_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_016_newlow_vol_flag_21_5d_diff},
    "vpd_drv2_017_vol_ret_beta_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_017_vol_ret_beta_21d_5d_diff},
    "vpd_drv2_018_vol_ret_beta_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_018_vol_ret_beta_63d_21d_diff},
    "vpd_drv2_019_vol_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_019_vol_slope_21d_5d_diff},
    "vpd_drv2_020_vol_slope_minus_price_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_020_vol_slope_minus_price_slope_21d_5d_diff},
    "vpd_drv2_021_down_vol_frac_21d_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv2_021_down_vol_frac_21d_slope_21d},
    "vpd_drv2_022_divergence_composite_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_022_divergence_composite_21d_5d_diff},
    "vpd_drv2_023_vol_x_abs_ret_down_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_023_vol_x_abs_ret_down_21d_5d_diff},
    "vpd_drv2_024_vol_x_abs_ret_down_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_024_vol_x_abs_ret_down_63d_21d_diff},
    "vpd_drv2_025_divergence_days_frac_down_21d_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv2_025_divergence_days_frac_down_21d_slope_21d},
    # --- new drv2_026-075 ---
    "vpd_drv2_026_corr_vol_ret_126d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_026_corr_vol_ret_126d_21d_diff},
    "vpd_drv2_027_corr_vol_ret_21d_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv2_027_corr_vol_ret_21d_slope_21d},
    "vpd_drv2_028_cov_vol_ret_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_028_cov_vol_ret_63d_5d_diff},
    "vpd_drv2_029_vol_on_down_frac_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_029_vol_on_down_frac_252d_21d_diff},
    "vpd_drv2_030_vwap_decline_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_030_vwap_decline_252d_21d_diff},
    "vpd_drv2_031_down_ret_x_volnorm_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_031_down_ret_x_volnorm_252d_21d_diff},
    "vpd_drv2_032_corr_vol_ret_21d_63d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_032_corr_vol_ret_21d_63d_diff},
    "vpd_drv2_033_corr_vol_ret_63d_63d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_033_corr_vol_ret_63d_63d_diff},
    "vpd_drv2_034_vol_ret_beta_21d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_034_vol_ret_beta_21d_21d_diff},
    "vpd_drv2_035_vol_ret_beta_126d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_035_vol_ret_beta_126d_21d_diff},
    "vpd_drv2_036_vol_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_036_vol_slope_63d_5d_diff},
    "vpd_drv2_037_price_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_037_price_slope_21d_5d_diff},
    "vpd_drv2_038_price_slope_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_038_price_slope_63d_21d_diff},
    "vpd_drv2_039_vol_slope_minus_price_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_039_vol_slope_minus_price_slope_63d_5d_diff},
    "vpd_drv2_040_divergence_composite_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_040_divergence_composite_63d_5d_diff},
    "vpd_drv2_041_price_down_vol_up_count_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_041_price_down_vol_up_count_252d_21d_diff},
    "vpd_drv2_042_vol_x_abs_ret_down_21d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_042_vol_x_abs_ret_down_21d_21d_diff},
    "vpd_drv2_043_vol_x_abs_ret_down_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_043_vol_x_abs_ret_down_252d_21d_diff},
    "vpd_drv2_044_down_vol_frac_21d_slope_63d": {"inputs": ["close", "volume"], "func": vpd_drv2_044_down_vol_frac_21d_slope_63d},
    "vpd_drv2_045_corr_vol_ret_21d_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv2_045_corr_vol_ret_21d_slope_21d},
    "vpd_drv2_046_cov_vol_ret_21d_slope_21d": {"inputs": ["close", "volume"], "func": vpd_drv2_046_cov_vol_ret_21d_slope_21d},
    "vpd_drv2_047_cov_vol_ret_63d_slope_63d": {"inputs": ["close", "volume"], "func": vpd_drv2_047_cov_vol_ret_63d_slope_63d},
    "vpd_drv2_048_newlow21_vol_rising_count_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_048_newlow21_vol_rising_count_21d_diff},
    "vpd_drv2_049_vol_surge_on_price_drop_count_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_049_vol_surge_on_price_drop_count_21d_diff},
    "vpd_drv2_050_vol_ewm5_vs_ewm21_ratio_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_050_vol_ewm5_vs_ewm21_ratio_5d_diff},
    "vpd_drv2_051_vol_ewm21_vs_ewm63_ratio_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_051_vol_ewm21_vs_ewm63_ratio_5d_diff},
    "vpd_drv2_052_down_vwap_vs_up_vwap_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_052_down_vwap_vs_up_vwap_21d_5d_diff},
    "vpd_drv2_053_vol_on_down_vs_up_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_053_vol_on_down_vs_up_ratio_21d_5d_diff},
    "vpd_drv2_054_vol_price_divergence_composite_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_054_vol_price_divergence_composite_63d_21d_diff},
    "vpd_drv2_055_corr_vol_close_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_055_corr_vol_close_21d_5d_diff},
    "vpd_drv2_056_corr_vol_close_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_056_corr_vol_close_63d_21d_diff},
    "vpd_drv2_057_corr_vol_logret_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_057_corr_vol_logret_21d_5d_diff},
    "vpd_drv2_058_corr_vol_logret_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_058_corr_vol_logret_63d_21d_diff},
    "vpd_drv2_059_vol_x_abs_ret_down_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_059_vol_x_abs_ret_down_63d_5d_diff},
    "vpd_drv2_060_divergence_days_frac_down_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_060_divergence_days_frac_down_63d_21d_diff},
    "vpd_drv2_061_divergence_days_frac_down_63d_slope_63d": {"inputs": ["close", "volume"], "func": vpd_drv2_061_divergence_days_frac_down_63d_slope_63d},
    "vpd_drv2_062_vol_ret_beta_63d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_062_vol_ret_beta_63d_5d_diff},
    "vpd_drv2_063_vol_ret_beta_252d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_063_vol_ret_beta_252d_21d_diff},
    "vpd_drv2_064_vol_on_down_frac_21d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_064_vol_on_down_frac_21d_21d_diff},
    "vpd_drv2_065_cov_vol_logret_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_065_cov_vol_logret_21d_5d_diff},
    "vpd_drv2_066_cov_vol_logret_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_066_cov_vol_logret_63d_21d_diff},
    "vpd_drv2_067_vol_weighted_cum_decline_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_067_vol_weighted_cum_decline_21d_5d_diff},
    "vpd_drv2_068_vol_weighted_cum_decline_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_068_vol_weighted_cum_decline_63d_21d_diff},
    "vpd_drv2_069_down_ret_x_volnorm_126d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_069_down_ret_x_volnorm_126d_21d_diff},
    "vpd_drv2_070_corr_vol_ret_21d_ewm21_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_070_corr_vol_ret_21d_ewm21_5d_diff},
    "vpd_drv2_071_down_logret_x_volnorm_21d_5d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_071_down_logret_x_volnorm_21d_5d_diff},
    "vpd_drv2_072_down_logret_x_volnorm_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_072_down_logret_x_volnorm_63d_21d_diff},
    "vpd_drv2_073_vol_price_divergence_composite_126d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_073_vol_price_divergence_composite_126d_21d_diff},
    "vpd_drv2_074_price_down_vol_up_count_21d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_074_price_down_vol_up_count_21d_21d_diff},
    "vpd_drv2_075_vol_surge_on_price_drop_count_63d_21d_diff": {"inputs": ["close", "volume"], "func": vpd_drv2_075_vol_surge_on_price_drop_count_63d_21d_diff},
}
