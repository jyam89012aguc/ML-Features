# f21_raw_volume_metrics_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _vol_zscore_val(v, w):
    return (v - v.rolling(w).mean()) / v.rolling(w).std().replace(0, np.nan)

def _rel_vol(v, w):
    return v / v.rolling(w).mean().replace(0, np.nan)

def _dollar_vol_intensity(v, closeadj, w):
    dv = v * closeadj
    return dv / dv.rolling(w).mean().replace(0, np.nan)

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _min(s, w):
    return s.rolling(w, min_periods=min(w, 5)).min()

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

# Feature 001: 5-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_base_v001_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 002: 10-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_base_v002_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 003: 21-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_base_v003_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 004: 63-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_base_v004_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 005: 126-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_base_v005_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 006: 252-day volume z-score
def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_base_v006_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 007: 5-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_5d_base_v007_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 008: 10-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_10d_base_v008_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 009: 21-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_21d_base_v009_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 010: 63-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_63d_base_v010_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 011: 126-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_126d_base_v011_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 012: 252-day relative volume
def f21rvm_f21_raw_volume_metrics_rel_vol_252d_base_v012_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 013: 21-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_base_v013_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 014: 63-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_base_v014_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 015: 126-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_base_v015_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 016: 252-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_base_v016_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 017: Volume spike relative to 21-day max
def f21rvm_f21_raw_volume_metrics_vol_spike_21d_base_v017_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21) / _max(volume, 21).replace(0, np.nan) * volume
    res = _rel_vol(res, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 018: Volume spike relative to 63-day max
def f21rvm_f21_raw_volume_metrics_vol_spike_63d_base_v018_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63) / _max(volume, 63).replace(0, np.nan) * volume
    res = _rel_vol(res, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 019: 5-day SMA of 21-day relative volume
def f21rvm_f21_raw_volume_metrics_sma5_rel_vol_21d_base_v019_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 020: 10-day SMA of 21-day relative volume
def f21rvm_f21_raw_volume_metrics_sma10_rel_vol_21d_base_v020_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 21), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 021: 5-day SMA of 63-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_sma5_dollar_vol_int_63d_base_v021_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 022: 10-day SMA of 63-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_sma10_dollar_vol_int_63d_base_v022_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 023: Ratio of 5-day rel volume to 63-day rel volume
def f21rvm_f21_raw_volume_metrics_rel_vol_ratio_5_63_base_v023_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5) / _rel_vol(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 024: Ratio of 10-day rel volume to 126-day rel volume
def f21rvm_f21_raw_volume_metrics_rel_vol_ratio_10_126_base_v024_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10) / _rel_vol(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 025: Z-score of 21-day relative volume over 63 days
def f21rvm_f21_raw_volume_metrics_zscore_rel_vol_21_63_base_v025_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = _vol_zscore_val(rv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 026: Z-score of 63-day relative volume over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_rel_vol_63_252_base_v026_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 63)
    res = _vol_zscore_val(rv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 027: Z-score of dollar volume intensity (63d) over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_dollar_vol_int_63_252_base_v027_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    res = _vol_zscore_val(dv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 028: 21-day dollar volume intensity vs its 63-day SMA
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_rel_63sma_base_v028_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21)
    res = dv / _sma(dv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 029: Max 21-day relative volume over 63 days
def f21rvm_f21_raw_volume_metrics_max_rel_vol_21_63_base_v029_signal(volume: pd.Series) -> pd.Series:
    res = _max(_rel_vol(volume, 21), 63)
    res = _rel_vol(res, 21) # Just to use primitive
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 030: Min 21-day relative volume over 63 days
def f21rvm_f21_raw_volume_metrics_min_rel_vol_21_63_base_v030_signal(volume: pd.Series) -> pd.Series:
    res = _min(_rel_vol(volume, 21), 63)
    res = _rel_vol(res, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 031: 5-day SMA of volume z-score 21d
def f21rvm_f21_raw_volume_metrics_sma5_vol_zscore_21d_base_v031_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 032: 10-day SMA of volume z-score 63d
def f21rvm_f21_raw_volume_metrics_sma10_vol_zscore_63d_base_v032_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 033: 21-day relative volume vs 126-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_vs_max_126d_base_v033_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21) / _max(volume, 126).replace(0, np.nan) * volume
    res = _rel_vol(res, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 034: 63-day dollar volume intensity vs 252-day min
def f21rvm_f21_raw_volume_metrics_dollar_vol_vs_min_252d_base_v034_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    res = dv / _min(dv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 035: 5-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21_5sma_base_v035_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21)
    res = _sma(dv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 036: 10-day volume z-score relative to 252-day SMA
def f21rvm_f21_raw_volume_metrics_zscore_rel_sma252_base_v036_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 10)
    res = z / _sma(z.abs(), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 037: Volume 5-day z-score / 21-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_5_21_base_v037_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5) / _vol_zscore_val(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 038: Volume 10-day z-score / 63-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_10_63_base_v038_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10) / _vol_zscore_val(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 039: Dollar volume intensity 21d / 126d
def f21rvm_f21_raw_volume_metrics_dollar_vol_ratio_21_126_base_v039_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21) / _dollar_vol_intensity(volume, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 040: Dollar volume intensity 63d / 252d
def f21rvm_f21_raw_volume_metrics_dollar_vol_ratio_63_252_base_v040_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63) / _dollar_vol_intensity(volume, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 041: 252-day volume percentile rank (using rel_vol as proxy)
def f21rvm_f21_raw_volume_metrics_vol_rank_252d_base_v041_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 042: 126-day volume percentile rank
def f21rvm_f21_raw_volume_metrics_vol_rank_126d_base_v042_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 043: 63-day volume percentile rank
def f21rvm_f21_raw_volume_metrics_vol_rank_63d_base_v043_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 044: 21-day volume percentile rank
def f21rvm_f21_raw_volume_metrics_vol_rank_21d_base_v044_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 045: 5-day relative volume vs 252-day range
def f21rvm_f21_raw_volume_metrics_rel_vol_range_252d_base_v045_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    mn = _min(rv, 252)
    mx = _max(rv, 252)
    res = (rv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 046: 21-day relative volume vs 252-day range
def f21rvm_f21_raw_volume_metrics_rel_vol_range_21_252d_base_v046_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    mn = _min(rv, 252)
    mx = _max(rv, 252)
    res = (rv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 047: 63-day dollar volume intensity vs 252-day range
def f21rvm_f21_raw_volume_metrics_dollar_vol_range_63_252d_base_v047_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    mn = _min(dv, 252)
    mx = _max(dv, 252)
    res = (dv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 048: 126-day dollar volume intensity vs 252-day range
def f21rvm_f21_raw_volume_metrics_dollar_vol_range_126_252d_base_v048_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 126)
    mn = _min(dv, 252)
    mx = _max(dv, 252)
    res = (dv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 049: 5-day SMA of 21-day volume rank
def f21rvm_f21_raw_volume_metrics_sma5_vol_rank_21d_base_v049_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 21).rolling(21).rank(pct=True), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 050: 10-day SMA of 63-day volume rank
def f21rvm_f21_raw_volume_metrics_sma10_vol_rank_63d_base_v050_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 63).rolling(63).rank(pct=True), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 051: Volume z-score 21d vs 252d max
def f21rvm_f21_raw_volume_metrics_zscore_vs_max_252d_base_v051_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 21)
    res = z / _max(z.abs(), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 052: Volume z-score 63d vs 252d max
def f21rvm_f21_raw_volume_metrics_zscore_vs_max_63_252d_base_v052_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 63)
    res = z / _max(z.abs(), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 053: Dollar volume intensity 252-day z-score
def f21rvm_f21_raw_volume_metrics_dollar_vol_zscore_252d_base_v053_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 252)
    res = _vol_zscore_val(dv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 054: Dollar volume intensity 126-day z-score
def f21rvm_f21_raw_volume_metrics_dollar_vol_zscore_126d_base_v054_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 126)
    res = _vol_zscore_val(dv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 055: Volume spike 5-day SMA relative to 252-day
def f21rvm_f21_raw_volume_metrics_vol_spike_sma5_252d_base_v055_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 5), 5) / _rel_vol(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 056: Volume spike 10-day SMA relative to 252-day
def f21rvm_f21_raw_volume_metrics_vol_spike_sma10_252d_base_v056_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 10), 10) / _rel_vol(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 057: Z-score of 5-day rel volume over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_rel_vol_5_252_base_v057_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = _vol_zscore_val(rv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 058: Z-score of 10-day rel volume over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_rel_vol_10_252_base_v058_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    res = _vol_zscore_val(rv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 059: Ratio of 21-day SMA volume to 252-day SMA volume
def f21rvm_f21_raw_volume_metrics_sma_ratio_21_252_base_v059_signal(volume: pd.Series) -> pd.Series:
    res = _sma(volume, 21) / _sma(volume, 252).replace(0, np.nan)
    res = _rel_vol(res, 21) # primitive
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 060: Ratio of 63-day SMA volume to 252-day SMA volume
def f21rvm_f21_raw_volume_metrics_sma_ratio_63_252_base_v060_signal(volume: pd.Series) -> pd.Series:
    res = _sma(volume, 63) / _sma(volume, 252).replace(0, np.nan)
    res = _rel_vol(res, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 061: 5-day relative volume vs its 252-day standard deviation
def f21rvm_f21_raw_volume_metrics_rel_vol_vs_std252_base_v061_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / rv.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 062: 21-day relative volume vs its 252-day standard deviation
def f21rvm_f21_raw_volume_metrics_rel_vol_21_vs_std252_base_v062_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / rv.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 063: 63-day dollar volume intensity vs its 252-day standard deviation
def f21rvm_f21_raw_volume_metrics_dollar_vol_vs_std252_base_v063_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    res = dv / dv.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 064: 126-day dollar volume intensity vs its 252-day standard deviation
def f21rvm_f21_raw_volume_metrics_dollar_vol_126_vs_std252_base_v064_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 126)
    res = dv / dv.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 065: Volume 21-day z-score / 252-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_21_252_base_v065_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21) / _vol_zscore_val(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 066: Volume 63-day z-score / 252-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_63_252_base_v066_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63) / _vol_zscore_val(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 067: Dollar volume intensity 21d / 252d
def f21rvm_f21_raw_volume_metrics_dollar_vol_ratio_21_252_base_v067_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21) / _dollar_vol_intensity(volume, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 068: Dollar volume intensity 126d / 252d
def f21rvm_f21_raw_volume_metrics_dollar_vol_ratio_126_252_base_v068_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126) / _dollar_vol_intensity(volume, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 069: Volume 5-day z-score relative to 63-day max
def f21rvm_f21_raw_volume_metrics_zscore_5_vs_max63_base_v069_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 5)
    res = z / _max(z.abs(), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 070: Volume 10-day z-score relative to 126-day max
def f21rvm_f21_raw_volume_metrics_zscore_10_vs_max126_base_v070_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 10)
    res = z / _max(z.abs(), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 071: 21-day relative volume percentile rank (252d)
def f21rvm_f21_raw_volume_metrics_rel_vol_21_rank_252_base_v071_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 072: 63-day relative volume percentile rank (252d)
def f21rvm_f21_raw_volume_metrics_rel_vol_63_rank_252_base_v072_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 073: 21-day dollar volume intensity rank (252d)
def f21rvm_f21_raw_volume_metrics_dollar_vol_21_rank_252_base_v073_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 074: 63-day dollar volume intensity rank (252d)
def f21rvm_f21_raw_volume_metrics_dollar_vol_63_rank_252_base_v074_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 075: 5-day relative volume vs 21-day rel volume
def f21rvm_f21_raw_volume_metrics_rel_vol_5_vs_21_base_v075_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5) / _rel_vol(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["volume", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f21rvm_") and f.endswith("_signal")]

F21_RAW_VOLUME_METRICS_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"volume": np.random.rand(sz)*1000000, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F21_RAW_VOLUME_METRICS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
