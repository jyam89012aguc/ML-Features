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

# --- Feature Functions 001-075 ---

# 001-015: Base VP Confirmation (ROC Product)
def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_base_v001_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 22-day ROCs."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p44_v44_base_v002_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 44-day ROCs."""
    res = _vp_conf(_roc(arg_closeadj, 44), _roc(arg_volume, 44))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p66_v66_base_v003_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 66-day ROCs."""
    res = _vp_conf(_roc(arg_closeadj, 66), _roc(arg_volume, 66))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p126_v126_base_v004_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 126-day ROCs."""
    res = _vp_conf(_roc(arg_closeadj, 126), _roc(arg_volume, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p252_v252_base_v005_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 252-day ROCs."""
    res = _vp_conf(_roc(arg_closeadj, 252), _roc(arg_volume, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v5_base_v006_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 22-day Price ROC and 5-day Volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v10_base_v007_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 22-day Price ROC and 10-day Volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v63_base_v008_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 22-day Price ROC and 63-day Volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p63_v22_base_v009_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 63-day Price ROC and 22-day Volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 22))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p126_v22_base_v010_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Volume-price confirmation using 126-day Price ROC and 22-day Volume ROC."""
    res = _vp_conf(_roc(arg_closeadj, 126), _roc(arg_volume, 22))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma22_base_v011_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 22-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma63_base_v012_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 63-day VP confirmation (p22/v22)."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p44_v44_sma44_base_v013_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 44-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 44), _roc(arg_volume, 44)), 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p66_v66_sma66_base_v014_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 66-day VP confirmation."""
    res = _sma(_vp_conf(_roc(arg_closeadj, 66), _roc(arg_volume, 66)), 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema22_base_v015_signal(arg_closeadj, arg_volume) -> pd.Series:
    """EMA of 22-day VP confirmation."""
    res = _ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22)
    return res.replace([np.inf, -np.inf], np.nan)

# 016-030: VP Correlation
def f24vpc_f24_volume_price_confirmation_vp_corr_w22_base_v016_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w44_base_v017_signal(arg_closeadj, arg_volume) -> pd.Series:
    """44-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w66_base_v018_signal(arg_closeadj, arg_volume) -> pd.Series:
    """66-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w126_base_v019_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w252_base_v020_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w504_base_v021_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day rolling correlation between price and volume."""
    res = _vp_corr(arg_closeadj, arg_volume, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc22_w22_base_v022_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day correlation between price ROC and volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 22), _roc(arg_volume, 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc22_w44_base_v023_signal(arg_closeadj, arg_volume) -> pd.Series:
    """44-day correlation between price ROC and volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 22), _roc(arg_volume, 22), 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc22_w66_base_v024_signal(arg_closeadj, arg_volume) -> pd.Series:
    """66-day correlation between price ROC and volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 22), _roc(arg_volume, 22), 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc44_w44_base_v025_signal(arg_closeadj, arg_volume) -> pd.Series:
    """44-day correlation between 44-day price ROC and 44-day volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 44), _roc(arg_volume, 44), 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc66_w66_base_v026_signal(arg_closeadj, arg_volume) -> pd.Series:
    """66-day correlation between 66-day price ROC and 66-day volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 66), _roc(arg_volume, 66), 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc22_w126_base_v027_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day correlation between price ROC and volume ROC."""
    res = _vp_corr(_roc(arg_closeadj, 22), _roc(arg_volume, 22), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc1_w22_base_v028_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day correlation between 1-day price returns and 1-day volume change."""
    res = _vp_corr(_roc(arg_closeadj, 1), _roc(arg_volume, 1), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc5_w22_base_v029_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day correlation between 5-day price returns and 5-day volume change."""
    res = _vp_corr(_roc(arg_closeadj, 5), _roc(arg_volume, 5), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc10_w63_base_v030_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day correlation between 10-day price returns and 10-day volume change."""
    res = _vp_corr(_roc(arg_closeadj, 10), _roc(arg_volume, 10), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 031-045: VP Trend Strength
def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_base_v031_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength (ratio of volume on up days)."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w44_base_v032_signal(arg_closeadj, arg_volume) -> pd.Series:
    """44-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w63_base_v033_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w126_base_v034_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w252_base_v035_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema22_base_v036_signal(arg_closeadj, arg_volume) -> pd.Series:
    """EMA of 22-day VP trend strength."""
    res = _ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma63_base_v037_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 63-day VP trend strength."""
    res = _sma(_vp_trend_strength(arg_closeadj, arg_volume, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z252_base_v038_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 252-day VP trend strength."""
    res = _z(_vp_trend_strength(arg_closeadj, arg_volume, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_diff22_base_v039_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Difference in VP trend strength over 22 days."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = ts - ts.shift(22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_roc22_base_v040_signal(arg_closeadj, arg_volume) -> pd.Series:
    """ROC of 22-day VP trend strength."""
    res = _roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w504_base_v041_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w756_base_v042_signal(arg_closeadj, arg_volume) -> pd.Series:
    """756-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w1008_base_v043_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1008-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w1260_base_v044_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260-day VP trend strength."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma252_base_v045_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 252-day VP trend strength."""
    res = _sma(_vp_trend_strength(arg_closeadj, arg_volume, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 046-060: Z-scores of VP Confirmation
def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p22_v22_base_v046_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day VP confirmation over 63 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z126_p22_v22_base_v047_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day VP confirmation over 126 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z252_p22_v22_base_v048_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day VP confirmation over 252 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p44_v44_base_v049_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 44-day VP confirmation over 63 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 44), _roc(arg_volume, 44)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p66_v66_base_v050_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 66-day VP confirmation over 63 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 66), _roc(arg_volume, 66)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z252_p126_v126_base_v051_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 126-day VP confirmation over 252 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 126), _roc(arg_volume, 126)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z504_p22_v22_base_v052_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day VP confirmation over 504 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z1260_p22_v22_base_v053_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day VP confirmation over 1260 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p22_v5_base_v054_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of (p22/v5) VP confirmation over 63 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 5)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p22_v10_base_v055_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of (p22/v10) VP confirmation over 63 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 10)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z126_p22_v63_base_v056_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of (p22/v63) VP confirmation over 126 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 63)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z126_p63_v22_base_v057_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of (p63/v22) VP confirmation over 126 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 22)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z252_p126_v22_base_v058_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of (p126/v22) VP confirmation over 252 days."""
    res = _z(_vp_conf(_roc(arg_closeadj, 126), _roc(arg_volume, 22)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z63_p22_v22_sma22_base_v059_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of SMA22 of VP confirmation over 63 days."""
    res = _z(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_z252_p22_v22_sma63_base_v060_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of SMA63 of VP confirmation over 252 days."""
    res = _z(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 061-075: Mixed and Relative VP confirmation
def f24vpc_f24_volume_price_confirmation_vp_conf_rel_sma252_p22_v22_base_v061_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP confirmation relative to its 252-day SMA."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = conf / _sma(conf, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_rel_sma1260_p22_v22_base_v062_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP confirmation relative to its 1260-day SMA."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = conf / _sma(conf, 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z252_w22_base_v063_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 22-day price-volume correlation over 252 days."""
    res = _z(_vp_corr(arg_closeadj, arg_volume, 22), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z252_w63_base_v064_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 63-day price-volume correlation over 252 days."""
    res = _z(_vp_corr(arg_closeadj, arg_volume, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z504_w126_base_v065_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Z-score of 126-day price-volume correlation over 504 days."""
    res = _z(_vp_corr(arg_closeadj, arg_volume, 126), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_sma252_w22_base_v066_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength relative to its 252-day SMA."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = ts / _sma(ts, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_sma1260_w22_base_v067_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP trend strength relative to its 1260-day SMA."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = ts / _sma(ts, 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_diff63_base_v068_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day difference in 22-day VP confirmation."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = conf - conf.shift(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_roc63_base_v069_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day ROC in 22-day VP confirmation."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = _roc(conf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_diff63_w22_base_v070_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day difference in 22-day price-volume correlation."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = corr - corr.shift(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc63_w22_base_v071_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day ROC in 22-day price-volume correlation."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = _roc(corr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_div_v63_base_v072_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP confirmation divided by 63-day volume SMA."""
    res = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)) / _sma(arg_volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_conf_w22_base_v073_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Product of 22-day VP trend strength and 22-day VP confirmation."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 22) * _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_corr_w22_base_v074_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Product of 22-day VP trend strength and 22-day price-volume correlation."""
    res = _vp_trend_strength(arg_closeadj, arg_volume, 22) * _vp_corr(arg_closeadj, arg_volume, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_min252_base_v075_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22-day VP confirmation relative to its 252-day rolling minimum."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = conf / conf.rolling(252).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_closeadj", "arg_volume"]}

F24_VOLUME_PRICE_CONFIRMATION_BASE_REGISTRY_001_075 = {
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
    for n, c in F24_VOLUME_PRICE_CONFIRMATION_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
    print(f"OK")
