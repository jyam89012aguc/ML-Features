import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _roc(s, w): return s.pct_change(w)
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _vp_conf(p_roc, v_roc):
    # High volume on positive returns = strong confirmation
    return (p_roc * v_roc)

def _vp_corr(p, v, w):
    return p.rolling(w).corr(v)

def _vp_trend_strength(p, v, w):
    p_up = (p > p.shift(1)).astype(float)
    return (p_up * v).rolling(w).sum() / v.rolling(w).sum().replace(0, np.nan)

# --- Feature Functions 076-150 ---

# 076-090: Long-term VP Confirmation and Smoothing
def f24vpc_f24_volume_price_confirmation_vp_conf_p252_v63_base_v076_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VP confirmation: 252-day price ROC and 63-day volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 252), _roc(arg_volume, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p63_v252_base_v077_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VP confirmation: 63-day price ROC and 252-day volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p504_v504_base_v078_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VP confirmation: 504-day price ROC and 504-day volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 504), _roc(arg_volume, 504))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma252_base_v079_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day SMA of 22-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma504_base_v080_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day SMA of 22-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema63_base_v081_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day EMA of 22-day VP confirmation."""
    res = _ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p44_v44_ema126_base_v082_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day EMA of 44-day VP confirmation."""
    res = _ema(_vp_conf(_roc(arg_closeadj, 44), _roc(arg_volume, 44)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p66_v66_ema252_base_v083_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day EMA of 66-day VP confirmation."""
    res = _ema(_vp_conf(_roc(arg_closeadj, 66), _roc(arg_volume, 66)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_cumsum_base_v084_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Cumulative sum of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).cumsum()
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_rolling_sum_252_base_v085_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling sum of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_rolling_std_252_base_v086_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling volatility of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_max_252_base_v087_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling maximum of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_min_252_base_v088_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling minimum of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_rank_252_base_v089_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling rank of 22-day VP confirmation."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)


# 091-105: More VP Correlation variations
def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w22_base_v091_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day correlation between price and log volume."""
    res = _vp_corr(arg_closeadj, np.log1p(arg_volume), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w63_base_v092_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day correlation between price and log volume."""
    res = _vp_corr(arg_closeadj, np.log1p(arg_volume), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w252_base_v093_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day correlation between price and log volume."""
    res = _vp_corr(arg_closeadj, np.log1p(arg_volume), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc63_w252_base_v094_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day correlation between 63-day price ROC and 63-day volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 63), _roc(arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc126_w252_base_v095_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day correlation between 126-day price ROC and 126-day volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 126), _roc(arg_volume, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc252_w504_base_v096_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day correlation between 252-day price ROC and 252-day volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 252), _roc(arg_volume, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_w63_base_v097_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day correlation between 22-day price SMA and 22-day volume SMA."""
    res = _vp_corr(_sma(arg_closeadj, 22), _sma(arg_volume, 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma63_w252_base_v098_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day correlation between 63-day price SMA and 63-day volume SMA."""
    res = _vp_corr(_sma(arg_closeadj, 63), _sma(arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma252_w1260_base_v099_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day correlation between 252-day price SMA and 252-day volume SMA."""
    res = _vp_corr(_sma(arg_closeadj, 252), _sma(arg_volume, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema22_w63_base_v100_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day correlation between 22-day price EMA and 22-day volume EMA."""
    res = _vp_corr(_ema(arg_closeadj, 22), _ema(arg_volume, 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema63_w252_base_v101_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day correlation between 63-day price EMA and 63-day volume EMA."""
    res = _vp_corr(_ema(arg_closeadj, 63), _ema(arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema252_w1260_base_v102_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day correlation between 252-day price EMA and 252-day volume EMA."""
    res = _vp_corr(_ema(arg_closeadj, 252), _ema(arg_volume, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z63_w22_base_v103_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day Z-score of 22-day price-volume correlation."""
    res = _z(_vp_corr(arg_closeadj, arg_volume, 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_z252_w22_base_v104_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day Z-score of 22-day SMA of 22-day price-volume correlation."""
    res = _z(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 22), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_diff252_w22_base_v105_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day difference in 22-day price-volume correlation."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = corr - corr.shift(252)
    return res.replace([np.inf, -np.inf], np.nan)

# 106-120: More VP Trend Strength variations
def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_vol_sma63_w22_base_v106_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength scaled by (volume / 63-day volume SMA)."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = ts * (arg_volume / _sma(arg_volume, 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_vol_sma252_w63_base_v107_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day VP trend strength scaled by (volume / 252-day volume SMA)."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 63)
    res = ts * (arg_volume / _sma(arg_volume, 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema126_w22_base_v108_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day EMA of 22-day VP trend strength."""
    res = _ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema252_w63_base_v109_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day EMA of 63-day VP trend strength."""
    res = _ema(_vp_trend_strength(arg_closeadj, arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma1260_w252_base_v110_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day SMA of 252-day VP trend strength."""
    res = _sma(_vp_trend_strength(arg_closeadj, arg_volume, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z504_w63_base_v111_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day Z-score of 63-day VP trend strength."""
    res = _z(_vp_trend_strength(arg_closeadj, arg_volume, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z1260_w252_base_v112_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day Z-score of 252-day VP trend strength."""
    res = _z(_vp_trend_strength(arg_closeadj, arg_volume, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


def f24vpc_f24_volume_price_confirmation_vp_trend_strength_roc252_w63_base_v114_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day ROC of 63-day VP trend strength."""
    res = _roc(_vp_trend_strength(arg_closeadj, arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_diff252_w63_base_v115_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day difference in 63-day VP trend strength."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 63)
    res = ts - ts.shift(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma22_z252_w22_base_v116_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day Z-score of 22-day SMA of 22-day VP trend strength."""
    res = _z(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema63_z504_w63_base_v117_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day Z-score of 63-day EMA of 63-day VP trend strength."""
    res = _z(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 63), 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_roc22_w22_base_v118_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength multiplied by 22-day price ROC."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 22) * _roc(arg_closeadj, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_roc63_w63_base_v119_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day VP trend strength multiplied by 63-day price ROC."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 63) * _roc(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_div_vol_z252_w22_base_v120_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength divided by 252-day volume Z-score."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 22) / _z(arg_volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 121-135: Divergence and Agreement variations using primitives
def f24vpc_f24_volume_price_confirmation_vp_div_sma63_base_v121_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VP Divergence: Difference between 63-day Price SMA and 63-day VP confirmation SMA."""
    p_sma = _sma(_roc(arg_closeadj, 22), 63)
    v_sma = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63)
    res = p_sma - v_sma
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_div_sma252_base_v122_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VP Divergence: Difference between 252-day Price SMA and 252-day VP confirmation SMA."""
    p_sma = _sma(_roc(arg_closeadj, 22), 252)
    v_sma = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252)
    res = p_sma - v_sma
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_negative_w22_base_v123_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for negative 22-day price-volume correlation (divergence)."""
    res = (_vp_corr(arg_closeadj, arg_volume, 22) < 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_negative_w63_base_v124_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for negative 63-day price-volume correlation."""
    res = (_vp_corr(arg_closeadj, arg_volume, 63) < 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_negative_w252_base_v125_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for negative 252-day price-volume correlation."""
    res = (_vp_corr(arg_closeadj, arg_volume, 252) < 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_negative_p22_v22_base_v126_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for negative 22-day VP confirmation (divergence)."""
    res = (_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)) < 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_negative_p63_v63_base_v127_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for negative 63-day VP confirmation."""
    res = (_vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 63)) < 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_low_w22_base_v128_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for low 22-day VP trend strength (< 0.4)."""
    res = (_vp_trend_strength(arg_closeadj, arg_volume, 22) < 0.4).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_high_w22_base_v129_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Indicator for high 22-day VP trend strength (> 0.6)."""
    res = (_vp_trend_strength(arg_closeadj, arg_volume, 22) > 0.6).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_sma22_div_sma252_base_v130_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 22-day VP confirmation SMA to 252-day VP confirmation SMA."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = _sma(conf, 22) / _sma(conf, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_div_sma252_base_v131_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 22-day price-volume correlation SMA to 252-day correlation SMA."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = _sma(corr, 22) / _sma(corr, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma22_div_sma252_base_v132_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 22-day VP trend strength SMA to 252-day trend strength SMA."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = _sma(ts, 22) / _sma(ts, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z252_abs_base_v133_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Absolute value of 252-day Z-score of 22-day VP confirmation."""
    res = np.abs(_z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z252_abs_base_v134_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Absolute value of 252-day Z-score of 22-day price-volume correlation."""
    res = np.abs(_z(_vp_corr(arg_closeadj, arg_volume, 22), 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z252_abs_base_v135_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Absolute value of 252-day Z-score of 22-day VP trend strength."""
    res = np.abs(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 252))
    return res.replace([np.inf, -np.inf], np.nan)

# 136-150: Cumulative and weighted metrics
def f24vpc_f24_volume_price_confirmation_vp_conf_weighted_sma63_base_v136_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-weighted SMA of 22-day price ROC using _vp_conf primitive logic."""
    p_roc = _roc(arg_closeadj, 22)
    res = (p_roc * arg_volume).rolling(63).sum() / arg_volume.rolling(63).sum().replace(0, np.nan)
    # This is essentially _vp_conf logic embedded in a weighted mean
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_weighted_sma252_base_v137_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-weighted SMA of 22-day price ROC (252-day)."""
    p_roc = _roc(arg_closeadj, 22)
    res = (p_roc * arg_volume).rolling(252).sum() / arg_volume.rolling(252).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_cumsum_z252_base_v138_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of cumulative 22-day VP confirmation over 252 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).cumsum(), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_cumsum_z252_base_v139_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of cumulative 22-day price-volume correlation over 252 days."""
    res = _z(_vp_corr(arg_closeadj, arg_volume, 22).cumsum(), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_cumsum_z252_base_v140_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of cumulative 22-day VP trend strength over 252 days."""
    res = _z(_vp_trend_strength(arg_closeadj, arg_volume, 22).cumsum(), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema1260_base_v141_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day EMA of 22-day VP confirmation."""
    res = _ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema1260_w22_base_v142_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day EMA of 22-day price-volume correlation."""
    res = _ema(_vp_corr(arg_closeadj, arg_volume, 22), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema1260_w22_base_v143_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day EMA of 22-day VP trend strength."""
    res = _ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p63_v63_sma1260_base_v144_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day SMA of 63-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 63)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma1260_w63_base_v145_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day SMA of 63-day price-volume correlation."""
    res = _sma(_vp_corr(arg_closeadj, arg_volume, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma1260_w63_base_v146_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day SMA of 63-day VP trend strength."""
    res = _sma(_vp_trend_strength(arg_closeadj, arg_volume, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


def f24vpc_f24_volume_price_confirmation_vp_corr_roc126_w22_base_v148_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day ROC of 22-day price-volume correlation."""
    res = _roc(_vp_corr(arg_closeadj, arg_volume, 22), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_roc126_w22_base_v149_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day ROC of 22-day VP trend strength."""
    res = _roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_closeadj", "arg_volume"]}

F24_VOLUME_PRICE_CONFIRMATION_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([k for k in globals() if k.startswith('f24vpc_f24_volume_price_confirmation_') and k.endswith('_signal')])
}

if __name__ == "__main__":
    sz = 2000
    np.random.seed(42)
    d = pd.DataFrame({
        "arg_closeadj": pd.Series(np.exp(np.cumsum(np.random.normal(0.0001, 0.01, sz))) * 100),
        "arg_volume": pd.Series(np.random.lognormal(15, 1, sz)),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F24_VOLUME_PRICE_CONFIRMATION_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
    print(f"OK")
