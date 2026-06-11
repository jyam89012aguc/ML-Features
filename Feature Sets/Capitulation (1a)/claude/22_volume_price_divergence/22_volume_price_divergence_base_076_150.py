"""
22_volume_price_divergence — Base Features 076-150
Domain: volume rising while price falls — volume-weighted price decline, rolling OLS
residuals of volume vs price, high-volume down-day intensity metrics, divergence
z-scores, conditional volume statistics on new-lows, EWM divergence signals,
intraday low-volume price depth measures, multi-window composite divergence scores.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


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
    return _log_safe(s) - _log_safe(s.shift(1))


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Volume-weighted price decline metrics ---

def vpd_076_vwap_decline_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted avg price change: sum(ret*vol) / sum(vol)."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    return _safe_div(num, den)


def vpd_077_vwap_decline_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    return _safe_div(num, den)


def vpd_078_vwap_decline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day volume-weighted avg price change."""
    ret = _daily_ret(close)
    num = _rolling_sum(ret * volume, _TD_YEAR)
    den = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(num, den)


def vpd_079_vol_weighted_down_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted avg return on down days over 21 days."""
    ret = _daily_ret(close)
    down_ret = ret.where(ret < 0, np.nan)
    down_vol = volume.where(ret < 0, np.nan)
    num = _rolling_sum((down_ret * down_vol).fillna(0), _TD_MON)
    den = _rolling_sum(down_vol.fillna(0), _TD_MON)
    return _safe_div(num, den)


def vpd_080_vol_weighted_down_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted avg return on down days over 63 days."""
    ret = _daily_ret(close)
    down_ret = ret.where(ret < 0, np.nan)
    down_vol = volume.where(ret < 0, np.nan)
    num = _rolling_sum((down_ret * down_vol).fillna(0), _TD_QTR)
    den = _rolling_sum(down_vol.fillna(0), _TD_QTR)
    return _safe_div(num, den)


def vpd_081_vol_weighted_cum_decline_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume-weighted log return over 21 days."""
    lret = _log_ret(close)
    num = _rolling_sum(lret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    return _safe_div(num, den)


def vpd_082_vol_weighted_cum_decline_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume-weighted log return over 63 days."""
    lret = _log_ret(close)
    num = _rolling_sum(lret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    return _safe_div(num, den)


def vpd_083_down_vwap_vs_up_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of vol-weighted down-day return to vol-weighted up-day return, 21d."""
    ret = _daily_ret(close)
    d_r = ret.where(ret < 0, np.nan)
    u_r = ret.where(ret > 0, np.nan)
    d_v = volume.where(ret < 0, np.nan)
    u_v = volume.where(ret > 0, np.nan)
    d_num = _rolling_sum((d_r * d_v).fillna(0), _TD_MON)
    d_den = _rolling_sum(d_v.fillna(0), _TD_MON)
    u_num = _rolling_sum((u_r * u_v).fillna(0), _TD_MON)
    u_den = _rolling_sum(u_v.fillna(0), _TD_MON)
    down_vwap = _safe_div(d_num, d_den)
    up_vwap = _safe_div(u_num, u_den)
    return _safe_div(down_vwap, up_vwap.abs().clip(lower=_EPS))


def vpd_084_down_vwap_vs_up_vwap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of vol-weighted down-day return to vol-weighted up-day return, 63d."""
    ret = _daily_ret(close)
    d_r = ret.where(ret < 0, np.nan)
    u_r = ret.where(ret > 0, np.nan)
    d_v = volume.where(ret < 0, np.nan)
    u_v = volume.where(ret > 0, np.nan)
    d_num = _rolling_sum((d_r * d_v).fillna(0), _TD_QTR)
    d_den = _rolling_sum(d_v.fillna(0), _TD_QTR)
    u_num = _rolling_sum((u_r * u_v).fillna(0), _TD_QTR)
    u_den = _rolling_sum(u_v.fillna(0), _TD_QTR)
    down_vwap = _safe_div(d_num, d_den)
    up_vwap = _safe_div(u_num, u_den)
    return _safe_div(down_vwap, up_vwap.abs().clip(lower=_EPS))


def vpd_085_vol_weighted_low_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average intraday low over 21 days (distress depth)."""
    num = _rolling_sum(low * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    return _safe_div(num, den)


def vpd_086_vw_low_vs_close_ratio_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day vol-weighted avg low to 21-day avg close."""
    vw_low = vpd_085_vol_weighted_low_21d(close, low, volume)
    avg_close = _rolling_mean(close, _TD_MON)
    return _safe_div(vw_low, avg_close)


def vpd_087_vol_weighted_high_low_range_down_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg (high-low) range on down-price days over 21 days."""
    ret = _daily_ret(close)
    rng = high - low
    down_rng = rng.where(ret < 0, np.nan)
    down_vol = volume.where(ret < 0, np.nan)
    num = _rolling_sum((down_rng * down_vol).fillna(0), _TD_MON)
    den = _rolling_sum(down_vol.fillna(0), _TD_MON)
    return _safe_div(num, den)


def vpd_088_vol_on_down_days_vs_total_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on down-price days."""
    ret = _daily_ret(close)
    down_vol = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(down_vol, total_vol)


def vpd_089_vol_on_down_days_vs_total_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume occurring on down-price days."""
    ret = _daily_ret(close)
    down_vol = _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(down_vol, total_vol)


def vpd_090_vol_on_down_days_vs_total_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day total volume occurring on down-price days."""
    ret = _daily_ret(close)
    down_vol = _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR)
    total_vol = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(down_vol, total_vol)


# --- Group G (091-105): High-volume down-day intensity & abnormal volume on lows ---

def vpd_091_avg_vol_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over 21 days."""
    ret = _daily_ret(close)
    down_vol = volume.where(ret < 0, np.nan)
    return down_vol.rolling(_TD_MON, min_periods=1).mean()


def vpd_092_avg_vol_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over 63 days."""
    ret = _daily_ret(close)
    down_vol = volume.where(ret < 0, np.nan)
    return down_vol.rolling(_TD_QTR, min_periods=1).mean()


def vpd_093_avg_vol_on_up_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-price days over 21 days."""
    ret = _daily_ret(close)
    up_vol = volume.where(ret > 0, np.nan)
    return up_vol.rolling(_TD_MON, min_periods=1).mean()


def vpd_094_avg_vol_on_down_vs_up_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on down days to avg volume on up days, 21d."""
    down_avg = vpd_091_avg_vol_on_down_days_21d(close, volume)
    up_avg = vpd_093_avg_vol_on_up_days_21d(close, volume)
    return _safe_div(down_avg, up_avg)


def vpd_095_avg_vol_on_down_vs_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on down days to avg volume on up days, 63d."""
    ret = _daily_ret(close)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(down_vol, up_vol)


def vpd_096_vol_surge_on_newlow21_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol-to-21d-mean ratio on 21-day-new-low days over 21 days."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    is_newlow = (close < roll_min)
    return vol_norm.where(is_newlow, np.nan).rolling(_TD_MON, min_periods=1).mean()


def vpd_097_vol_surge_on_newlow63_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol-to-21d-mean ratio on 63-day-new-low days over 63 days."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    is_newlow = (close < roll_min)
    return vol_norm.where(is_newlow, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def vpd_098_total_vol_on_newlow21_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume accumulated on 21-day-new-low days in trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    is_newlow = (close < roll_min).astype(float)
    return _rolling_sum(volume * is_newlow, _TD_QTR)


def vpd_099_max_vol_single_down_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum volume on any single down-price day in trailing 21 days."""
    ret = _daily_ret(close)
    down_vol = volume.where(ret < 0, np.nan)
    return down_vol.rolling(_TD_MON, min_periods=1).max()


def vpd_100_max_vol_single_down_day_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum volume on any single down-price day in trailing 63 days."""
    ret = _daily_ret(close)
    down_vol = volume.where(ret < 0, np.nan)
    return down_vol.rolling(_TD_QTR, min_periods=1).max()


def vpd_101_down_vol_above_2std_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down-day volume spikes (vol > mean + 2*std) in trailing 63 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_spike = volume > (avg_vol + 2 * std_vol)
    down_spike = (ret < 0) & vol_spike
    return _rolling_count_true(down_spike, _TD_QTR)


def vpd_102_down_vol_above_2std_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down-day volume spikes (vol > mean + 2*std) in trailing 252 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_spike = volume > (avg_vol + 2 * std_vol)
    down_spike = (ret < 0) & vol_spike
    return _rolling_count_true(down_spike, _TD_YEAR)


def vpd_103_vol_x_abs_ret_down_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(return) on down days over 21 days (sell-pressure intensity)."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    return _rolling_sum(intensity, _TD_MON)


def vpd_104_vol_x_abs_ret_down_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(return) on down days over 63 days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    return _rolling_sum(intensity, _TD_QTR)


def vpd_105_vol_x_abs_ret_down_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(return) on down days over 252 days."""
    ret = _daily_ret(close)
    intensity = (volume * ret.abs()).where(ret < 0, 0.0)
    return _rolling_sum(intensity, _TD_YEAR)


# --- Group H (106-120): OLS residual divergence and z-scores ---

def vpd_106_corr_vol_ret_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day corr(vol, ret) vs 252-day distribution."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    m = _rolling_mean(corr, _TD_YEAR)
    s = _rolling_std(corr, _TD_YEAR)
    return _safe_div(corr - m, s)


def vpd_107_corr_vol_ret_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day corr(vol, ret) vs 252-day distribution."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    m = _rolling_mean(corr, _TD_YEAR)
    s = _rolling_std(corr, _TD_YEAR)
    return _safe_div(corr - m, s)


def vpd_108_cov_vol_ret_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day cov(vol, ret) vs 252-day distribution."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    m = _rolling_mean(cov, _TD_YEAR)
    s = _rolling_std(cov, _TD_YEAR)
    return _safe_div(cov - m, s)


def vpd_109_down_ret_x_vol_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day down_ret*vol sum vs 252-day distribution."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    m = _rolling_mean(interaction, _TD_YEAR)
    s = _rolling_std(interaction, _TD_YEAR)
    return _safe_div(interaction - m, s)


def vpd_110_down_ret_x_vol_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day down_ret*vol sum vs 252-day distribution."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_QTR)
    m = _rolling_mean(interaction, _TD_YEAR)
    s = _rolling_std(interaction, _TD_YEAR)
    return _safe_div(interaction - m, s)


def vpd_111_vol_on_down_frac_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day down-day volume fraction vs 252-day distribution."""
    ret = _daily_ret(close)
    down_vol = _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    frac = _safe_div(down_vol, total_vol)
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def vpd_112_vol_ret_beta_21d_minus_long_term(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Short-term (21d) minus long-term (252d) vol-return beta (regime shift)."""
    ret = _daily_ret(close)
    cov_short = _rolling_cov(volume, ret, _TD_MON)
    var_short = _rolling_std(ret, _TD_MON) ** 2
    beta_short = _safe_div(cov_short, var_short)
    cov_long = _rolling_cov(volume, ret, _TD_YEAR)
    var_long = _rolling_std(ret, _TD_YEAR) ** 2
    beta_long = _safe_div(cov_long, var_long)
    return beta_short - beta_long


def vpd_113_corr_vol_ret_short_minus_long(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Short-term (21d) corr minus long-term (252d) corr of vol vs return."""
    ret = _daily_ret(close)
    short_corr = _rolling_corr(volume, ret, _TD_MON)
    long_corr = _rolling_corr(volume, ret, _TD_YEAR)
    return short_corr - long_corr


def vpd_114_corr_vol_ret_medium_minus_long(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Medium-term (63d) corr minus long-term (252d) corr of vol vs return."""
    ret = _daily_ret(close)
    med_corr = _rolling_corr(volume, ret, _TD_QTR)
    long_corr = _rolling_corr(volume, ret, _TD_YEAR)
    return med_corr - long_corr


def vpd_115_price_down_vol_up_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 21-day divergence-day fraction in 252-day history."""
    ret = _daily_ret(close)
    div_cnt = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON)
    frac = div_cnt / _TD_MON
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_116_vol_price_divergence_composite_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite 21d divergence: avg of (neg corr flag, divergence frac, down_vol frac)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON) / _TD_MON
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    return (neg_corr + div_frac + dv_frac) / 3.0


def vpd_117_vol_price_divergence_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite 63d divergence: avg of (neg corr flag, divergence frac, down_vol frac)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_QTR)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR) / _TD_QTR
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    return (neg_corr + div_frac + dv_frac) / 3.0


def vpd_118_vol_price_divergence_expanding_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding pct rank of 21d divergence composite (all-history extremity)."""
    feat = vpd_116_vol_price_divergence_composite_21d(close, volume)
    return feat.expanding(min_periods=5).rank(pct=True)


def vpd_119_vol_price_divergence_composite_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite 252d divergence: avg of (neg corr flag, divergence frac, down_vol frac)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_YEAR)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_YEAR) / _TD_YEAR
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    return (neg_corr + div_frac + dv_frac) / 3.0


def vpd_120_cov_vol_ret_expanding_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day cov(vol, ret) (all-history extremity)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    m = cov.expanding(min_periods=5).mean()
    s = cov.expanding(min_periods=5).std()
    return _safe_div(cov - m, s)


# --- Group I (121-135): EWM divergence signals and cross-window spreads ---

def vpd_121_ewm_corr_vol_ret_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(21) of corr(vol,ret) minus EWM(63) of corr(vol,ret)."""
    ret = _daily_ret(close)
    daily_prod = volume * ret
    fast = _ewm_mean(daily_prod, _TD_MON)
    slow = _ewm_mean(daily_prod, _TD_QTR)
    return fast - slow


def vpd_122_ewm_down_interaction_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(21) of (down_ret * vol_norm) — fast-decay divergence signal."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, 0.0)
    return _ewm_mean(interaction, _TD_MON)


def vpd_123_ewm_down_interaction_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(63) of (down_ret * vol_norm) — slower divergence signal."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, 0.0)
    return _ewm_mean(interaction, _TD_QTR)


def vpd_124_ewm_divergence_macd_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD-style: EWM(21) minus EWM(63) of daily (price_down * vol_norm) interaction."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, 0.0)
    fast = _ewm_mean(interaction, _TD_MON)
    slow = _ewm_mean(interaction, _TD_QTR)
    return fast - slow


def vpd_125_vol_down_frac_ewm21_minus_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of daily down-day volume fraction."""
    ret = _daily_ret(close)
    down_flag = (ret < 0).astype(float)
    fast = _ewm_mean(down_flag, _TD_MON)
    slow = _ewm_mean(down_flag, _TD_QTR)
    return fast - slow


def vpd_126_vol_x_price_decline_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(21) of (volume * price-decline magnitude) on down days."""
    ret = _daily_ret(close)
    product = (volume * ret.abs()).where(ret < 0, 0.0)
    return _ewm_mean(product, _TD_MON)


def vpd_127_vol_x_price_decline_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(63) of (volume * price-decline magnitude) on down days."""
    ret = _daily_ret(close)
    product = (volume * ret.abs()).where(ret < 0, 0.0)
    return _ewm_mean(product, _TD_QTR)


def vpd_128_down_vol_frac_21d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day down-volume fraction to 252-day down-volume fraction."""
    ret = _daily_ret(close)
    frac_21 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    frac_252 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    return _safe_div(frac_21, frac_252)


def vpd_129_down_vol_frac_63d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day down-volume fraction to 252-day down-volume fraction."""
    ret = _daily_ret(close)
    frac_63 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    frac_252 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    return _safe_div(frac_63, frac_252)


def vpd_130_price_down_vol_up_count_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day divergence-day count vs 252-day distribution."""
    flag = ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def vpd_131_vol_weighted_price_depth_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg of (close - low) / close over 21 days — tail-risk depth."""
    depth = _safe_div(close - low, close)
    num = _rolling_sum(depth * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    return _safe_div(num, den)


def vpd_132_vol_weighted_price_depth_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg of (close - low) / close over 63 days."""
    depth = _safe_div(close - low, close)
    num = _rolling_sum(depth * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    return _safe_div(num, den)


def vpd_133_vol_surge_on_price_drop_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: price drops >1% AND volume > 1.5x 21-day avg."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((ret < -0.01) & (volume > 1.5 * avg_vol)).astype(float)


def vpd_134_vol_surge_on_price_drop_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of (ret < -1% and vol > 1.5x avg) days in trailing 63 days."""
    flag = vpd_133_vol_surge_on_price_drop_flag(close, volume)
    return _rolling_sum(flag, _TD_QTR)


def vpd_135_vol_surge_on_price_drop_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of (ret < -1% and vol > 1.5x avg) days in trailing 252 days."""
    flag = vpd_133_vol_surge_on_price_drop_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


# --- Group J (136-150): Advanced multi-factor and intraday divergence metrics ---

def vpd_136_intraday_low_vol_concentration_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume occurring when close is near intraday low (bottom 25% range)."""
    rng = (close.rolling(1).max() - low).clip(lower=_EPS)
    near_low = ((close - low) / rng) <= 0.25
    low_vol = _rolling_sum(volume.where(near_low, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(low_vol, total_vol)


def vpd_137_intraday_low_vol_concentration_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume occurring when close is near intraday low."""
    rng = (close.rolling(1).max() - low).clip(lower=_EPS)
    near_low = ((close - low) / rng) <= 0.25
    low_vol = _rolling_sum(volume.where(near_low, 0.0), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(low_vol, total_vol)


def vpd_138_vol_x_ret_negative_sum_vs_positive_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of |sum(vol*neg_ret)| to sum(vol*pos_ret) over 21 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    neg_sum = _rolling_sum((vol_norm * ret).where(ret < 0, 0.0), _TD_MON).abs()
    pos_sum = _rolling_sum((vol_norm * ret).where(ret > 0, 0.0), _TD_MON)
    return _safe_div(neg_sum, pos_sum.clip(lower=_EPS))


def vpd_139_vol_x_ret_negative_sum_vs_positive_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of |sum(vol*neg_ret)| to sum(vol*pos_ret) over 63 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    neg_sum = _rolling_sum((vol_norm * ret).where(ret < 0, 0.0), _TD_QTR).abs()
    pos_sum = _rolling_sum((vol_norm * ret).where(ret > 0, 0.0), _TD_QTR)
    return _safe_div(neg_sum, pos_sum.clip(lower=_EPS))


def vpd_140_corr_volchg_price_chg_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume daily-diff and price daily-diff."""
    price_chg = close.diff(1)
    vol_chg = volume.diff(1)
    return _rolling_corr(vol_chg, price_chg, _TD_MON)


def vpd_141_corr_volchg_price_chg_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume daily-diff and price daily-diff."""
    price_chg = close.diff(1)
    vol_chg = volume.diff(1)
    return _rolling_corr(vol_chg, price_chg, _TD_QTR)


def vpd_142_vol_slope_63d_when_price_falling(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over 63d, masked to NaN when 63d price slope >= 0."""
    vol_slope = _linslope(volume, _TD_QTR)
    price_slope = _linslope(close, _TD_QTR)
    return vol_slope.where(price_slope < 0, np.nan)


def vpd_143_newlow252_high_vol_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 252-day-new-low days with above-average volume in trailing 252 days."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = ((close < roll_min) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_144_price_ret_vol_product_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (daily_return * volume) over 21 days (signed vol-weighted return)."""
    ret = _daily_ret(close)
    return _rolling_mean(ret * volume, _TD_MON)


def vpd_145_price_ret_vol_product_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (daily_return * volume) over 63 days."""
    ret = _daily_ret(close)
    return _rolling_mean(ret * volume, _TD_QTR)


def vpd_146_price_ret_vol_product_std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std dev of (daily_return * volume) over 21 days."""
    ret = _daily_ret(close)
    return _rolling_std(ret * volume, _TD_MON)


def vpd_147_high_vol_new_low_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of vol_norm on 252d-new-low days over 252 days (capitulation pressure)."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    is_newlow = (close < roll_min).astype(float)
    return _rolling_sum(vol_norm * is_newlow, _TD_YEAR)


def vpd_148_divergence_days_frac_of_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days that also have rising volume, 21-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_MON)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON)
    return _safe_div(div_days, down_days)


def vpd_149_divergence_days_frac_of_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days that also have rising volume, 63-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_QTR)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR)
    return _safe_div(div_days, down_days)


def vpd_150_combined_divergence_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined distress: vol-frac-on-down * neg-corr-flag * down_ret_vol_zscore."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_MON),
        _rolling_sum(volume, _TD_MON)
    )
    corr = _rolling_corr(volume, ret, _TD_MON)
    neg_flag = (corr < 0).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    m = _rolling_mean(interaction, _TD_YEAR)
    s = _rolling_std(interaction, _TD_YEAR)
    z = _safe_div(interaction - m, s)
    return frac * neg_flag * z.clip(lower=0)


# --- Group K (176-200): New base features ---

def vpd_176_vol_surge_on_price_drop_2pct_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: price drops >2% AND volume > 1.5x 21-day avg (severe sell-off with volume)."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((ret < -0.02) & (volume > 1.5 * avg_vol)).astype(float)


def vpd_177_vol_surge_on_price_drop_2pct_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of (ret < -2% and vol > 1.5x avg) days in trailing 63 days."""
    flag = vpd_176_vol_surge_on_price_drop_2pct_flag(close, volume)
    return _rolling_sum(flag, _TD_QTR)


def vpd_178_vol_surge_on_price_drop_2pct_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of (ret < -2% and vol > 1.5x avg) days in trailing 252 days."""
    flag = vpd_176_vol_surge_on_price_drop_2pct_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_179_avg_vol_on_newlow21_vs_avg_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio: avg vol on 21d-new-low days vs overall avg vol, over 63-day window."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    is_newlow = (close < roll_min)
    avg_newlow_vol = volume.where(is_newlow, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    avg_vol = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg_newlow_vol, avg_vol)


def vpd_180_down_ret_x_volnorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * vol_norm) on down days over 126-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_HALF)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = ret.where(ret < 0, 0.0) * vol_norm
    return _rolling_sum(interaction, _TD_HALF)


def vpd_181_down_vol_frac_126d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 126-day down-volume fraction to 252-day down-volume fraction."""
    ret = _daily_ret(close)
    frac_126 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_HALF),
        _rolling_sum(volume, _TD_HALF)
    )
    frac_252 = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    return _safe_div(frac_126, frac_252)


def vpd_182_cov_vol_logret_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 126-day covariance between volume and log return."""
    lret = _log_ret(close)
    return _rolling_cov(volume, lret, _TD_HALF)


def vpd_183_vol_price_divergence_composite_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite 126d divergence: avg of (neg corr flag, divergence frac, down_vol frac)."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_HALF)
    neg_corr = (corr < 0).astype(float)
    div_frac = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_HALF) / _TD_HALF
    dv_frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_HALF),
        _rolling_sum(volume, _TD_HALF)
    )
    return (neg_corr + div_frac + dv_frac) / 3.0


def vpd_184_vol_weighted_price_depth_126d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg of (close - low) / close over 126 days."""
    depth = _safe_div(close - low, close)
    num = _rolling_sum(depth * volume, _TD_HALF)
    den = _rolling_sum(volume, _TD_HALF)
    return _safe_div(num, den)


def vpd_185_high_vol_down_day_count_above_3std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with vol > mean + 3*std in trailing 252 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    extreme_spike = volume > (avg_vol + 3.0 * std_vol)
    return _rolling_count_true((ret < 0) & extreme_spike, _TD_YEAR)


def vpd_186_vol_x_abs_logret_down_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(log_return) on down days over 21 days."""
    lret = _log_ret(close)
    intensity = (volume * lret.abs()).where(lret < 0, 0.0)
    return _rolling_sum(intensity, _TD_MON)


def vpd_187_vol_x_abs_logret_down_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(log_return) on down days over 63 days."""
    lret = _log_ret(close)
    intensity = (volume * lret.abs()).where(lret < 0, 0.0)
    return _rolling_sum(intensity, _TD_QTR)


def vpd_188_down_logret_x_volnorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (log_return * vol_norm) on down days over 21 days."""
    lret = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_sum((lret * vol_norm).where(lret < 0, 0.0), _TD_MON)


def vpd_189_down_logret_x_volnorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (log_return * vol_norm) on down days over 63 days."""
    lret = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return _rolling_sum((lret * vol_norm).where(lret < 0, 0.0), _TD_QTR)


def vpd_190_vol_ewm5_vs_ewm21_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of EWM(5) to EWM(21) of volume (short-term vol surge detector)."""
    fast = _ewm_mean(volume, _TD_WEEK)
    slow = _ewm_mean(volume, _TD_MON)
    return _safe_div(fast, slow)


def vpd_191_vol_ewm21_vs_ewm63_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of EWM(21) to EWM(63) of volume (medium-term vol surge detector)."""
    fast = _ewm_mean(volume, _TD_MON)
    slow = _ewm_mean(volume, _TD_QTR)
    return _safe_div(fast, slow)


def vpd_192_price_down_vol_ewm_surge_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days price down and EWM(5)/EWM(21) vol ratio > 1.5, trailing 21d."""
    fast = _ewm_mean(volume, _TD_WEEK)
    slow = _ewm_mean(volume, _TD_MON)
    surge = (fast / slow.replace(0, np.nan)) > 1.5
    ret = _daily_ret(close)
    return _rolling_count_true((ret < 0) & surge, _TD_MON)


def vpd_193_price_down_vol_ewm_surge_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days price down and EWM(5)/EWM(21) vol ratio > 1.5, trailing 63d."""
    fast = _ewm_mean(volume, _TD_WEEK)
    slow = _ewm_mean(volume, _TD_MON)
    surge = (fast / slow.replace(0, np.nan)) > 1.5
    ret = _daily_ret(close)
    return _rolling_count_true((ret < 0) & surge, _TD_QTR)


def vpd_194_corr_vol_ret_21d_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day corr(vol, ret) within trailing 126-day distribution."""
    ret = _daily_ret(close)
    corr = _rolling_corr(volume, ret, _TD_MON)
    return corr.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def vpd_195_down_ret_x_volnorm_21d_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 21-day signed down-vol interaction in 126-day history."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    feat = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    return feat.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def vpd_196_vol_on_down_frac_126d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 126-day down-volume fraction vs 252-day distribution."""
    ret = _daily_ret(close)
    frac = _safe_div(
        _rolling_sum(volume.where(ret < 0, 0.0), _TD_HALF),
        _rolling_sum(volume, _TD_HALF)
    )
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def vpd_197_newlow126_vol_rising_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close makes 126-day low AND volume above 21-day avg."""
    roll_min = close.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > avg_vol)).astype(float)


def vpd_198_newlow126_vol_rising_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 126-day-new-low + high-volume days in trailing 252 days."""
    flag = vpd_197_newlow126_vol_rising_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_199_vol_weighted_cum_decline_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume-weighted log return over 126 days."""
    lret = _log_ret(close)
    num = _rolling_sum(lret * volume, _TD_HALF)
    den = _rolling_sum(volume, _TD_HALF)
    return _safe_div(num, den)


def vpd_200_divergence_days_frac_of_down_days_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days that also have rising volume, 126-day window."""
    ret = _daily_ret(close)
    down_days = _rolling_count_true(ret < 0, _TD_HALF)
    div_days = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_HALF)
    return _safe_div(div_days, down_days)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PRICE_DIVERGENCE_REGISTRY_076_150 = {
    "vpd_076_vwap_decline_21d": {"inputs": ["close", "volume"], "func": vpd_076_vwap_decline_21d},
    "vpd_077_vwap_decline_63d": {"inputs": ["close", "volume"], "func": vpd_077_vwap_decline_63d},
    "vpd_078_vwap_decline_252d": {"inputs": ["close", "volume"], "func": vpd_078_vwap_decline_252d},
    "vpd_079_vol_weighted_down_ret_21d": {"inputs": ["close", "volume"], "func": vpd_079_vol_weighted_down_ret_21d},
    "vpd_080_vol_weighted_down_ret_63d": {"inputs": ["close", "volume"], "func": vpd_080_vol_weighted_down_ret_63d},
    "vpd_081_vol_weighted_cum_decline_21d": {"inputs": ["close", "volume"], "func": vpd_081_vol_weighted_cum_decline_21d},
    "vpd_082_vol_weighted_cum_decline_63d": {"inputs": ["close", "volume"], "func": vpd_082_vol_weighted_cum_decline_63d},
    "vpd_083_down_vwap_vs_up_vwap_21d": {"inputs": ["close", "volume"], "func": vpd_083_down_vwap_vs_up_vwap_21d},
    "vpd_084_down_vwap_vs_up_vwap_63d": {"inputs": ["close", "volume"], "func": vpd_084_down_vwap_vs_up_vwap_63d},
    "vpd_085_vol_weighted_low_21d": {"inputs": ["close", "low", "volume"], "func": vpd_085_vol_weighted_low_21d},
    "vpd_086_vw_low_vs_close_ratio_21d": {"inputs": ["close", "low", "volume"], "func": vpd_086_vw_low_vs_close_ratio_21d},
    "vpd_087_vol_weighted_high_low_range_down_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_087_vol_weighted_high_low_range_down_21d},
    "vpd_088_vol_on_down_days_vs_total_vol_21d": {"inputs": ["close", "volume"], "func": vpd_088_vol_on_down_days_vs_total_vol_21d},
    "vpd_089_vol_on_down_days_vs_total_vol_63d": {"inputs": ["close", "volume"], "func": vpd_089_vol_on_down_days_vs_total_vol_63d},
    "vpd_090_vol_on_down_days_vs_total_vol_252d": {"inputs": ["close", "volume"], "func": vpd_090_vol_on_down_days_vs_total_vol_252d},
    "vpd_091_avg_vol_on_down_days_21d": {"inputs": ["close", "volume"], "func": vpd_091_avg_vol_on_down_days_21d},
    "vpd_092_avg_vol_on_down_days_63d": {"inputs": ["close", "volume"], "func": vpd_092_avg_vol_on_down_days_63d},
    "vpd_093_avg_vol_on_up_days_21d": {"inputs": ["close", "volume"], "func": vpd_093_avg_vol_on_up_days_21d},
    "vpd_094_avg_vol_on_down_vs_up_ratio_21d": {"inputs": ["close", "volume"], "func": vpd_094_avg_vol_on_down_vs_up_ratio_21d},
    "vpd_095_avg_vol_on_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": vpd_095_avg_vol_on_down_vs_up_ratio_63d},
    "vpd_096_vol_surge_on_newlow21_21d": {"inputs": ["close", "volume"], "func": vpd_096_vol_surge_on_newlow21_21d},
    "vpd_097_vol_surge_on_newlow63_63d": {"inputs": ["close", "volume"], "func": vpd_097_vol_surge_on_newlow63_63d},
    "vpd_098_total_vol_on_newlow21_63d": {"inputs": ["close", "volume"], "func": vpd_098_total_vol_on_newlow21_63d},
    "vpd_099_max_vol_single_down_day_21d": {"inputs": ["close", "volume"], "func": vpd_099_max_vol_single_down_day_21d},
    "vpd_100_max_vol_single_down_day_63d": {"inputs": ["close", "volume"], "func": vpd_100_max_vol_single_down_day_63d},
    "vpd_101_down_vol_above_2std_count_63d": {"inputs": ["close", "volume"], "func": vpd_101_down_vol_above_2std_count_63d},
    "vpd_102_down_vol_above_2std_count_252d": {"inputs": ["close", "volume"], "func": vpd_102_down_vol_above_2std_count_252d},
    "vpd_103_vol_x_abs_ret_down_21d": {"inputs": ["close", "volume"], "func": vpd_103_vol_x_abs_ret_down_21d},
    "vpd_104_vol_x_abs_ret_down_63d": {"inputs": ["close", "volume"], "func": vpd_104_vol_x_abs_ret_down_63d},
    "vpd_105_vol_x_abs_ret_down_252d": {"inputs": ["close", "volume"], "func": vpd_105_vol_x_abs_ret_down_252d},
    "vpd_106_corr_vol_ret_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_106_corr_vol_ret_21d_zscore_252d},
    "vpd_107_corr_vol_ret_63d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_107_corr_vol_ret_63d_zscore_252d},
    "vpd_108_cov_vol_ret_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_108_cov_vol_ret_21d_zscore_252d},
    "vpd_109_down_ret_x_vol_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_109_down_ret_x_vol_21d_zscore_252d},
    "vpd_110_down_ret_x_vol_63d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_110_down_ret_x_vol_63d_zscore_252d},
    "vpd_111_vol_on_down_frac_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_111_vol_on_down_frac_21d_zscore_252d},
    "vpd_112_vol_ret_beta_21d_minus_long_term": {"inputs": ["close", "volume"], "func": vpd_112_vol_ret_beta_21d_minus_long_term},
    "vpd_113_corr_vol_ret_short_minus_long": {"inputs": ["close", "volume"], "func": vpd_113_corr_vol_ret_short_minus_long},
    "vpd_114_corr_vol_ret_medium_minus_long": {"inputs": ["close", "volume"], "func": vpd_114_corr_vol_ret_medium_minus_long},
    "vpd_115_price_down_vol_up_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_115_price_down_vol_up_pct_rank_252d},
    "vpd_116_vol_price_divergence_composite_21d": {"inputs": ["close", "volume"], "func": vpd_116_vol_price_divergence_composite_21d},
    "vpd_117_vol_price_divergence_composite_63d": {"inputs": ["close", "volume"], "func": vpd_117_vol_price_divergence_composite_63d},
    "vpd_118_vol_price_divergence_expanding_rank": {"inputs": ["close", "volume"], "func": vpd_118_vol_price_divergence_expanding_rank},
    "vpd_119_vol_price_divergence_composite_252d": {"inputs": ["close", "volume"], "func": vpd_119_vol_price_divergence_composite_252d},
    "vpd_120_cov_vol_ret_expanding_zscore": {"inputs": ["close", "volume"], "func": vpd_120_cov_vol_ret_expanding_zscore},
    "vpd_121_ewm_corr_vol_ret_21_vs_63": {"inputs": ["close", "volume"], "func": vpd_121_ewm_corr_vol_ret_21_vs_63},
    "vpd_122_ewm_down_interaction_21": {"inputs": ["close", "volume"], "func": vpd_122_ewm_down_interaction_21},
    "vpd_123_ewm_down_interaction_63": {"inputs": ["close", "volume"], "func": vpd_123_ewm_down_interaction_63},
    "vpd_124_ewm_divergence_macd_signal": {"inputs": ["close", "volume"], "func": vpd_124_ewm_divergence_macd_signal},
    "vpd_125_vol_down_frac_ewm21_minus_ewm63": {"inputs": ["close", "volume"], "func": vpd_125_vol_down_frac_ewm21_minus_ewm63},
    "vpd_126_vol_x_price_decline_ewm21": {"inputs": ["close", "volume"], "func": vpd_126_vol_x_price_decline_ewm21},
    "vpd_127_vol_x_price_decline_ewm63": {"inputs": ["close", "volume"], "func": vpd_127_vol_x_price_decline_ewm63},
    "vpd_128_down_vol_frac_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": vpd_128_down_vol_frac_21d_vs_252d_ratio},
    "vpd_129_down_vol_frac_63d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": vpd_129_down_vol_frac_63d_vs_252d_ratio},
    "vpd_130_price_down_vol_up_count_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_130_price_down_vol_up_count_21d_zscore_252d},
    "vpd_131_vol_weighted_price_depth_21d": {"inputs": ["close", "low", "volume"], "func": vpd_131_vol_weighted_price_depth_21d},
    "vpd_132_vol_weighted_price_depth_63d": {"inputs": ["close", "low", "volume"], "func": vpd_132_vol_weighted_price_depth_63d},
    "vpd_133_vol_surge_on_price_drop_flag": {"inputs": ["close", "volume"], "func": vpd_133_vol_surge_on_price_drop_flag},
    "vpd_134_vol_surge_on_price_drop_count_63d": {"inputs": ["close", "volume"], "func": vpd_134_vol_surge_on_price_drop_count_63d},
    "vpd_135_vol_surge_on_price_drop_count_252d": {"inputs": ["close", "volume"], "func": vpd_135_vol_surge_on_price_drop_count_252d},
    "vpd_136_intraday_low_vol_concentration_21d": {"inputs": ["close", "low", "volume"], "func": vpd_136_intraday_low_vol_concentration_21d},
    "vpd_137_intraday_low_vol_concentration_63d": {"inputs": ["close", "low", "volume"], "func": vpd_137_intraday_low_vol_concentration_63d},
    "vpd_138_vol_x_ret_negative_sum_vs_positive_sum_21d": {"inputs": ["close", "volume"], "func": vpd_138_vol_x_ret_negative_sum_vs_positive_sum_21d},
    "vpd_139_vol_x_ret_negative_sum_vs_positive_sum_63d": {"inputs": ["close", "volume"], "func": vpd_139_vol_x_ret_negative_sum_vs_positive_sum_63d},
    "vpd_140_corr_volchg_price_chg_21d": {"inputs": ["close", "volume"], "func": vpd_140_corr_volchg_price_chg_21d},
    "vpd_141_corr_volchg_price_chg_63d": {"inputs": ["close", "volume"], "func": vpd_141_corr_volchg_price_chg_63d},
    "vpd_142_vol_slope_63d_when_price_falling": {"inputs": ["close", "volume"], "func": vpd_142_vol_slope_63d_when_price_falling},
    "vpd_143_newlow252_high_vol_count_252d": {"inputs": ["close", "volume"], "func": vpd_143_newlow252_high_vol_count_252d},
    "vpd_144_price_ret_vol_product_mean_21d": {"inputs": ["close", "volume"], "func": vpd_144_price_ret_vol_product_mean_21d},
    "vpd_145_price_ret_vol_product_mean_63d": {"inputs": ["close", "volume"], "func": vpd_145_price_ret_vol_product_mean_63d},
    "vpd_146_price_ret_vol_product_std_21d": {"inputs": ["close", "volume"], "func": vpd_146_price_ret_vol_product_std_21d},
    "vpd_147_high_vol_new_low_intensity_252d": {"inputs": ["close", "volume"], "func": vpd_147_high_vol_new_low_intensity_252d},
    "vpd_148_divergence_days_frac_of_down_days_21d": {"inputs": ["close", "volume"], "func": vpd_148_divergence_days_frac_of_down_days_21d},
    "vpd_149_divergence_days_frac_of_down_days_63d": {"inputs": ["close", "volume"], "func": vpd_149_divergence_days_frac_of_down_days_63d},
    "vpd_150_combined_divergence_distress_index": {"inputs": ["close", "volume"], "func": vpd_150_combined_divergence_distress_index},
    # --- new 176-200 ---
    "vpd_176_vol_surge_on_price_drop_2pct_flag": {"inputs": ["close", "volume"], "func": vpd_176_vol_surge_on_price_drop_2pct_flag},
    "vpd_177_vol_surge_on_price_drop_2pct_count_63d": {"inputs": ["close", "volume"], "func": vpd_177_vol_surge_on_price_drop_2pct_count_63d},
    "vpd_178_vol_surge_on_price_drop_2pct_count_252d": {"inputs": ["close", "volume"], "func": vpd_178_vol_surge_on_price_drop_2pct_count_252d},
    "vpd_179_avg_vol_on_newlow21_vs_avg_vol_63d": {"inputs": ["close", "volume"], "func": vpd_179_avg_vol_on_newlow21_vs_avg_vol_63d},
    "vpd_180_down_ret_x_volnorm_126d": {"inputs": ["close", "volume"], "func": vpd_180_down_ret_x_volnorm_126d},
    "vpd_181_down_vol_frac_126d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": vpd_181_down_vol_frac_126d_vs_252d_ratio},
    "vpd_182_cov_vol_logret_126d": {"inputs": ["close", "volume"], "func": vpd_182_cov_vol_logret_126d},
    "vpd_183_vol_price_divergence_composite_126d": {"inputs": ["close", "volume"], "func": vpd_183_vol_price_divergence_composite_126d},
    "vpd_184_vol_weighted_price_depth_126d": {"inputs": ["close", "low", "volume"], "func": vpd_184_vol_weighted_price_depth_126d},
    "vpd_185_high_vol_down_day_count_above_3std_252d": {"inputs": ["close", "volume"], "func": vpd_185_high_vol_down_day_count_above_3std_252d},
    "vpd_186_vol_x_abs_logret_down_21d": {"inputs": ["close", "volume"], "func": vpd_186_vol_x_abs_logret_down_21d},
    "vpd_187_vol_x_abs_logret_down_63d": {"inputs": ["close", "volume"], "func": vpd_187_vol_x_abs_logret_down_63d},
    "vpd_188_down_logret_x_volnorm_21d": {"inputs": ["close", "volume"], "func": vpd_188_down_logret_x_volnorm_21d},
    "vpd_189_down_logret_x_volnorm_63d": {"inputs": ["close", "volume"], "func": vpd_189_down_logret_x_volnorm_63d},
    "vpd_190_vol_ewm5_vs_ewm21_ratio": {"inputs": ["close", "volume"], "func": vpd_190_vol_ewm5_vs_ewm21_ratio},
    "vpd_191_vol_ewm21_vs_ewm63_ratio": {"inputs": ["close", "volume"], "func": vpd_191_vol_ewm21_vs_ewm63_ratio},
    "vpd_192_price_down_vol_ewm_surge_21d": {"inputs": ["close", "volume"], "func": vpd_192_price_down_vol_ewm_surge_21d},
    "vpd_193_price_down_vol_ewm_surge_63d": {"inputs": ["close", "volume"], "func": vpd_193_price_down_vol_ewm_surge_63d},
    "vpd_194_corr_vol_ret_21d_pct_rank_126d": {"inputs": ["close", "volume"], "func": vpd_194_corr_vol_ret_21d_pct_rank_126d},
    "vpd_195_down_ret_x_volnorm_21d_pct_rank_126d": {"inputs": ["close", "volume"], "func": vpd_195_down_ret_x_volnorm_21d_pct_rank_126d},
    "vpd_196_vol_on_down_frac_126d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_196_vol_on_down_frac_126d_zscore_252d},
    "vpd_197_newlow126_vol_rising_flag": {"inputs": ["close", "volume"], "func": vpd_197_newlow126_vol_rising_flag},
    "vpd_198_newlow126_vol_rising_count_252d": {"inputs": ["close", "volume"], "func": vpd_198_newlow126_vol_rising_count_252d},
    "vpd_199_vol_weighted_cum_decline_126d": {"inputs": ["close", "volume"], "func": vpd_199_vol_weighted_cum_decline_126d},
    "vpd_200_divergence_days_frac_of_down_days_126d": {"inputs": ["close", "volume"], "func": vpd_200_divergence_days_frac_of_down_days_126d},
}
