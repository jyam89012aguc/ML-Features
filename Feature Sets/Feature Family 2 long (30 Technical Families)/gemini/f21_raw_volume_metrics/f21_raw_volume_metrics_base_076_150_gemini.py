# f21_raw_volume_metrics_base_076_150_gemini.py
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

# Feature 076: 10-day relative volume vs 63-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_10_sma63_base_v076_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    res = rv / _sma(rv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 077: 21-day relative volume vs 126-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_21_sma126_base_v077_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _sma(rv, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 078: 63-day relative volume vs 252-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_63_sma252_base_v078_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 63)
    res = rv / _sma(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 079: Z-score of 5-day SMA volume over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_sma5_252_base_v079_signal(volume: pd.Series) -> pd.Series:
    s5 = _sma(volume, 5)
    res = _vol_zscore_val(s5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 080: Z-score of 21-day SMA volume over 252 days
def f21rvm_f21_raw_volume_metrics_zscore_sma21_252_base_v080_signal(volume: pd.Series) -> pd.Series:
    s21 = _sma(volume, 21)
    res = _vol_zscore_val(s21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 081: 252-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_dollar_vol_int_504_base_v081_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 082: 5-day relative volume vs 252-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_5_vs_max252_base_v082_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _max(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 083: 10-day relative volume vs 252-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_10_vs_max252_base_v083_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    res = rv / _max(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 084: 21-day relative volume vs 252-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_21_vs_max252_base_v084_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _max(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 085: 63-day relative volume vs 252-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_63_vs_max252_base_v085_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 63)
    res = rv / _max(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 086: 5-day relative volume vs 252-day min
def f21rvm_f21_raw_volume_metrics_rel_vol_5_vs_min252_base_v086_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _min(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 087: 21-day relative volume vs 252-day min
def f21rvm_f21_raw_volume_metrics_rel_vol_21_vs_min252_base_v087_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _min(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 088: 63-day dollar volume intensity vs 252-day max
def f21rvm_f21_raw_volume_metrics_dollar_vol_63_vs_max252_base_v088_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    res = dv / _max(dv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 089: 126-day dollar volume intensity vs 252-day max
def f21rvm_f21_raw_volume_metrics_dollar_vol_126_vs_max252_base_v089_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 126)
    res = dv / _max(dv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 090: Ratio of 252-day volume z-score to its absolute mean
def f21rvm_f21_raw_volume_metrics_zscore_norm_252_base_v090_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 252)
    res = z / _sma(z.abs(), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 091: Ratio of 126-day volume z-score to its absolute mean
def f21rvm_f21_raw_volume_metrics_zscore_norm_126_base_v091_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 126)
    res = z / _sma(z.abs(), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 092: 21-day SMA of 5-day volume z-score
def f21rvm_f21_raw_volume_metrics_sma21_zscore5_base_v092_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 093: 63-day SMA of 21-day volume z-score
def f21rvm_f21_raw_volume_metrics_sma63_zscore21_base_v093_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 094: 126-day SMA of 63-day volume z-score
def f21rvm_f21_raw_volume_metrics_sma126_zscore63_base_v094_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 095: 5-day relative volume percentile rank (126d)
def f21rvm_f21_raw_volume_metrics_rel_vol_5_rank_126_base_v095_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 096: 10-day relative volume percentile rank (126d)
def f21rvm_f21_raw_volume_metrics_rel_vol_10_rank_126_base_v096_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 097: 21-day relative volume percentile rank (126d)
def f21rvm_f21_raw_volume_metrics_rel_vol_21_rank_126_base_v097_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 098: 63-day relative volume percentile rank (126d)
def f21rvm_f21_raw_volume_metrics_rel_vol_63_rank_126_base_v098_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 099: 21-day dollar volume intensity rank (126d)
def f21rvm_f21_raw_volume_metrics_dollar_vol_21_rank_126_base_v099_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 100: 63-day dollar volume intensity rank (126d)
def f21rvm_f21_raw_volume_metrics_dollar_vol_63_rank_126_base_v100_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 101: 5-day z-score of 21-day relative volume
def f21rvm_f21_raw_volume_metrics_zscore5_rel_vol_21_base_v101_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = _vol_zscore_val(rv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 102: 10-day z-score of 63-day relative volume
def f21rvm_f21_raw_volume_metrics_zscore10_rel_vol_63_base_v102_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 63)
    res = _vol_zscore_val(rv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 103: 21-day z-score of 126-day relative volume
def f21rvm_f21_raw_volume_metrics_zscore21_rel_vol_126_base_v103_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 126)
    res = _vol_zscore_val(rv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 104: 5-day relative volume vs 63-day range
def f21rvm_f21_raw_volume_metrics_rel_vol_5_range63_base_v104_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    mn = _min(rv, 63)
    mx = _max(rv, 63)
    res = (rv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 105: 10-day relative volume vs 63-day range
def f21rvm_f21_raw_volume_metrics_rel_vol_10_range63_base_v105_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    mn = _min(rv, 63)
    mx = _max(rv, 63)
    res = (rv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 106: 21-day dollar volume intensity vs 63-day range
def f21rvm_f21_raw_volume_metrics_dollar_vol_21_range63_base_v106_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21)
    mn = _min(dv, 63)
    mx = _max(dv, 63)
    res = (dv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 107: 63-day dollar volume intensity vs 126-day range
def f21rvm_f21_raw_volume_metrics_dollar_vol_63_range126_base_v107_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    mn = _min(dv, 126)
    mx = _max(dv, 126)
    res = (dv - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 108: Ratio of 5-day z-score to 252-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_5_252_base_v108_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5) / _vol_zscore_val(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 109: Ratio of 10-day z-score to 252-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_ratio_10_252_base_v109_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10) / _vol_zscore_val(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 110: 21-day volume z-score vs 126-day SMA of z-score
def f21rvm_f21_raw_volume_metrics_zscore_21_rel_sma126_base_v110_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 21)
    res = z / _sma(z.abs(), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 111: 63-day volume z-score vs 126-day SMA of z-score
def f21rvm_f21_raw_volume_metrics_zscore_63_rel_sma126_base_v111_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 63)
    res = z / _sma(z.abs(), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 112: 5-day SMA of dollar volume intensity 21d
def f21rvm_f21_raw_volume_metrics_sma5_dollar_vol_21_base_v112_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 113: 10-day SMA of dollar volume intensity 63d

# Feature 114: 21-day SMA of dollar volume intensity 126d
def f21rvm_f21_raw_volume_metrics_sma21_dollar_vol_126_base_v114_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 126), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 115: 5-day relative volume vs its 63-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_5_rel_sma63_base_v115_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _sma(rv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 116: 10-day relative volume vs its 63-day SMA

# Feature 117: 21-day relative volume vs its 63-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_21_rel_sma63_base_v117_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _sma(rv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 118: 63-day dollar volume intensity vs its 63-day SMA
def f21rvm_f21_raw_volume_metrics_dollar_vol_63_rel_sma63_base_v118_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 63)
    res = dv / _sma(dv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 119: 5-day volume z-score vs its 63-day standard deviation
def f21rvm_f21_raw_volume_metrics_zscore5_vs_std63_base_v119_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 5)
    res = z / z.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 120: 10-day volume z-score vs its 63-day standard deviation
def f21rvm_f21_raw_volume_metrics_zscore10_vs_std63_base_v120_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 10)
    res = z / z.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 121: 21-day volume z-score vs its 63-day standard deviation
def f21rvm_f21_raw_volume_metrics_zscore21_vs_std63_base_v121_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 21)
    res = z / z.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 122: 5-day relative volume vs 21-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_5_vs_max21_base_v122_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _max(rv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 123: 5-day relative volume vs 21-day min
def f21rvm_f21_raw_volume_metrics_rel_vol_5_vs_min21_base_v123_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _min(rv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 124: 10-day relative volume vs 21-day max
def f21rvm_f21_raw_volume_metrics_rel_vol_10_vs_max21_base_v124_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    res = rv / _max(rv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 125: 10-day relative volume vs 21-day min
def f21rvm_f21_raw_volume_metrics_rel_vol_10_vs_min21_base_v125_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 10)
    res = rv / _min(rv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 126: 21-day dollar volume intensity vs 21-day max
def f21rvm_f21_raw_volume_metrics_dollar_vol_21_vs_max21_base_v126_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21)
    res = dv / _max(dv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 127: 21-day dollar volume intensity vs 21-day min
def f21rvm_f21_raw_volume_metrics_dollar_vol_21_vs_min21_base_v127_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21)
    res = dv / _min(dv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 128: 5-day volume z-score vs 252-day range
def f21rvm_f21_raw_volume_metrics_zscore5_range252_base_v128_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 5)
    mn = _min(z, 252)
    mx = _max(z, 252)
    res = (z - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 129: 10-day volume z-score vs 252-day range
def f21rvm_f21_raw_volume_metrics_zscore10_range252_base_v129_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 10)
    mn = _min(z, 252)
    mx = _max(z, 252)
    res = (z - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 130: 21-day volume z-score vs 252-day range
def f21rvm_f21_raw_volume_metrics_zscore21_range252_base_v130_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 21)
    mn = _min(z, 252)
    mx = _max(z, 252)
    res = (z - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 131: 63-day volume z-score vs 252-day range
def f21rvm_f21_raw_volume_metrics_zscore63_range252_base_v131_signal(volume: pd.Series) -> pd.Series:
    z = _vol_zscore_val(volume, 63)
    mn = _min(z, 252)
    mx = _max(z, 252)
    res = (z - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 132: 21-day dollar volume intensity vs 252-day percentile rank

# Feature 133: 63-day dollar volume intensity vs 252-day percentile rank

# Feature 134: 126-day dollar volume intensity vs 252-day percentile rank
def f21rvm_f21_raw_volume_metrics_dollar_vol_126_rank_252_v2_base_v134_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 135: 5-day SMA of 21-day dollar volume intensity

# Feature 136: 10-day SMA of 21-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_sma10_dollar_vol_21_v2_base_v136_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 21), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 137: 21-day SMA of 21-day dollar volume intensity
def f21rvm_f21_raw_volume_metrics_sma21_dollar_vol_21_v2_base_v137_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 138: 5-day relative volume vs its 252-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_5_rel_sma252_base_v138_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _sma(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 139: 21-day relative volume vs its 252-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_21_rel_sma252_base_v139_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _sma(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 140: 63-day relative volume vs its 252-day SMA

# Feature 141: 5-day z-score of volume vs 21-day z-score

# Feature 142: 10-day z-score of volume vs 63-day z-score

# Feature 143: 21-day z-score of volume vs 126-day z-score
def f21rvm_f21_raw_volume_metrics_zscore_21_126_ratio_base_v143_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21) / _vol_zscore_val(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 144: 63-day z-score of volume vs 252-day z-score

# Feature 145: 5-day relative volume vs its 5-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_5_rel_sma5_base_v145_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 5)
    res = rv / _sma(rv, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 146: 21-day relative volume vs its 21-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_21_rel_sma21_base_v146_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 21)
    res = rv / _sma(rv, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 147: 63-day relative volume vs its 63-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_63_rel_sma63_v2_base_v147_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 63)
    res = rv / _sma(rv, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 148: 126-day relative volume vs its 126-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_126_rel_sma126_base_v148_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 126)
    res = rv / _sma(rv, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 149: 252-day relative volume vs its 252-day SMA
def f21rvm_f21_raw_volume_metrics_rel_vol_252_rel_sma252_base_v149_signal(volume: pd.Series) -> pd.Series:
    rv = _rel_vol(volume, 252)
    res = rv / _sma(rv, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 150: 5-day dollar volume intensity vs its 5-day SMA
def f21rvm_f21_raw_volume_metrics_dollar_vol_5_rel_sma5_base_v150_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = _dollar_vol_intensity(volume, closeadj, 21) # min 21
    res = dv / _sma(dv, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["volume", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f21rvm_") and f.endswith("_signal")]

F21_RAW_VOLUME_METRICS_BASE_REGISTRY_076_150 = {
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
    for n, c in F21_RAW_VOLUME_METRICS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
