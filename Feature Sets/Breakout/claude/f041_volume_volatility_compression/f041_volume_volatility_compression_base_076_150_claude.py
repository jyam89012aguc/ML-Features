import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f041_vol_range(volume, w):
    hi = volume.rolling(w, min_periods=max(1, w // 2)).max()
    lo = volume.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / lo.replace(0, np.nan)


def _f041_vol_vol_compression(volume, w):
    sd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    m = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / m.replace(0, np.nan)


def _f041_quiet_accumulation(closeadj, volume, w):
    vstd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    pstd = closeadj.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    return -(vstd * pstd) * closeadj


# v076: 21d compression squared × close
def f041vvc_f041_volume_volatility_compression_cmpsq_21d_base_v076_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = (base ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 63d compression squared × close
def f041vvc_f041_volume_volatility_compression_cmpsq_63d_base_v077_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = (base ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 252d compression squared × close
def f041vvc_f041_volume_volatility_compression_cmpsq_252d_base_v078_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    result = (base ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 21d sqrt vol range × close
def f041vvc_f041_volume_volatility_compression_vrsqrt_21d_base_v079_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21).clip(lower=0)
    result = np.sqrt(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 63d sqrt vol range × close
def f041vvc_f041_volume_volatility_compression_vrsqrt_63d_base_v080_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63).clip(lower=0)
    result = np.sqrt(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 252d sqrt vol range × close
def f041vvc_f041_volume_volatility_compression_vrsqrt_252d_base_v081_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252).clip(lower=0)
    result = np.sqrt(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d vol range minus compression × close
def f041vvc_f041_volume_volatility_compression_vrmcmp_21d_base_v082_signal(closeadj, volume):
    a = _f041_vol_range(volume, 21)
    b = _f041_vol_vol_compression(volume, 21)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d vol range minus compression × close
def f041vvc_f041_volume_volatility_compression_vrmcmp_63d_base_v083_signal(closeadj, volume):
    a = _f041_vol_range(volume, 63)
    b = _f041_vol_vol_compression(volume, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 252d vol range minus compression × close
def f041vvc_f041_volume_volatility_compression_vrmcmp_252d_base_v084_signal(closeadj, volume):
    a = _f041_vol_range(volume, 252)
    b = _f041_vol_vol_compression(volume, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 21d mean compression × close × volume
def f041vvc_f041_volume_volatility_compression_cmpmnv_21d_base_v085_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = _mean(base, 21) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 63d mean compression × close × volume
def f041vvc_f041_volume_volatility_compression_cmpmnv_63d_base_v086_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = _mean(base, 63) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 252d mean compression × close × volume
def f041vvc_f041_volume_volatility_compression_cmpmnv_252d_base_v087_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    result = _mean(base, 126) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: 21d quiet accumulation EMA
def f041vvc_f041_volume_volatility_compression_quietema_21d_base_v088_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = base.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v089: 63d quiet accumulation EMA
def f041vvc_f041_volume_volatility_compression_quietema_63d_base_v089_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = base.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v090: 252d quiet accumulation EMA
def f041vvc_f041_volume_volatility_compression_quietema_252d_base_v090_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = base.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v091: vol range z 21d × close
def f041vvc_f041_volume_volatility_compression_vrz_21d_base_v091_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: vol range z 63d × close
def f041vvc_f041_volume_volatility_compression_vrz_63d_base_v092_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: vol range z 252d × close
def f041vvc_f041_volume_volatility_compression_vrz_252d_base_v093_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: compression / vol range
def f041vvc_f041_volume_volatility_compression_cmpovr_21d_base_v094_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 21)
    b = _f041_vol_range(volume, 21)
    result = _safe_div(a, b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: compression / vol range 63d
def f041vvc_f041_volume_volatility_compression_cmpovr_63d_base_v095_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 63)
    b = _f041_vol_range(volume, 63)
    result = _safe_div(a, b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: compression / vol range 252d
def f041vvc_f041_volume_volatility_compression_cmpovr_252d_base_v096_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 252)
    b = _f041_vol_range(volume, 252)
    result = _safe_div(a, b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: vol range times log(close)
def f041vvc_f041_volume_volatility_compression_vrxlc_21d_base_v097_signal(closeadj, volume):
    result = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: vol range times log(close) 63d
def f041vvc_f041_volume_volatility_compression_vrxlc_63d_base_v098_signal(closeadj, volume):
    result = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: vol range times log(close) 252d
def f041vvc_f041_volume_volatility_compression_vrxlc_252d_base_v099_signal(closeadj, volume):
    result = _f041_vol_range(volume, 252) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: quiet acc × volume z
def f041vvc_f041_volume_volatility_compression_quietxvz_21d_base_v100_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 21) * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: quiet acc × volume z 63d
def f041vvc_f041_volume_volatility_compression_quietxvz_63d_base_v101_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 63) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: quiet acc × volume z 252d
def f041vvc_f041_volume_volatility_compression_quietxvz_252d_base_v102_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 252) * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: compression × ATR proxy
def f041vvc_f041_volume_volatility_compression_cmpxatr_21d_base_v103_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(21, min_periods=5).mean()
    result = _f041_vol_vol_compression(volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v104: compression × ATR proxy 63d
def f041vvc_f041_volume_volatility_compression_cmpxatr_63d_base_v104_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _f041_vol_vol_compression(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v105: compression × ATR proxy 252d
def f041vvc_f041_volume_volatility_compression_cmpxatr_252d_base_v105_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _f041_vol_vol_compression(volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v106: vol range × ATR
def f041vvc_f041_volume_volatility_compression_vrxatr_21d_base_v106_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(21, min_periods=5).mean()
    result = _f041_vol_range(volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v107: vol range × ATR 63d
def f041vvc_f041_volume_volatility_compression_vrxatr_63d_base_v107_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _f041_vol_range(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v108: vol range × ATR 252d
def f041vvc_f041_volume_volatility_compression_vrxatr_252d_base_v108_signal(closeadj, volume):
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _f041_vol_range(volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# v109: rolling min compression × close
def f041vvc_f041_volume_volatility_compression_cmpmin_21d_base_v109_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: rolling min compression 63d × close
def f041vvc_f041_volume_volatility_compression_cmpmin_63d_base_v110_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: rolling max compression × close
def f041vvc_f041_volume_volatility_compression_cmpmax_21d_base_v111_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: rolling max compression 63d × close
def f041vvc_f041_volume_volatility_compression_cmpmax_63d_base_v112_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: low-compression duration × close
def f041vvc_f041_volume_volatility_compression_lowcmpdur_21d_base_v113_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    grp = (flag != flag.shift(1)).cumsum()
    dur = flag.groupby(grp).cumsum()
    result = dur * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: low-compression duration 63d × close
def f041vvc_f041_volume_volatility_compression_lowcmpdur_63d_base_v114_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    grp = (flag != flag.shift(1)).cumsum()
    dur = flag.groupby(grp).cumsum()
    result = dur * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: low-vol-range duration × close
def f041vvc_f041_volume_volatility_compression_lowvrdur_21d_base_v115_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    grp = (flag != flag.shift(1)).cumsum()
    dur = flag.groupby(grp).cumsum()
    result = dur * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: low-vol-range duration 63d × close
def f041vvc_f041_volume_volatility_compression_lowvrdur_63d_base_v116_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    grp = (flag != flag.shift(1)).cumsum()
    dur = flag.groupby(grp).cumsum()
    result = dur * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: compression - long avg × close
def f041vvc_f041_volume_volatility_compression_cmpdelt_21d_base_v117_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    long_avg = base.rolling(252, min_periods=63).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: compression - long avg 63d
def f041vvc_f041_volume_volatility_compression_cmpdelt_63d_base_v118_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    long_avg = base.rolling(252, min_periods=63).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: compression - long avg 252d
def f041vvc_f041_volume_volatility_compression_cmpdelt_252d_base_v119_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    long_avg = base.rolling(504, min_periods=126).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: vol-range - long avg × close
def f041vvc_f041_volume_volatility_compression_vrdelt_21d_base_v120_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    long_avg = base.rolling(252, min_periods=63).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: vol-range - long avg 63d
def f041vvc_f041_volume_volatility_compression_vrdelt_63d_base_v121_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    long_avg = base.rolling(252, min_periods=63).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: vol-range - long avg 252d
def f041vvc_f041_volume_volatility_compression_vrdelt_252d_base_v122_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    long_avg = base.rolling(504, min_periods=126).mean()
    result = (base - long_avg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: quiet acc × marketcap proxy
def f041vvc_f041_volume_volatility_compression_quietxmc_21d_base_v123_signal(closeadj, volume):
    mc = closeadj * volume.rolling(63, min_periods=21).mean()
    result = _f041_quiet_accumulation(closeadj, volume, 21) * np.log1p(mc)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: quiet acc × marketcap proxy 63d
def f041vvc_f041_volume_volatility_compression_quietxmc_63d_base_v124_signal(closeadj, volume):
    mc = closeadj * volume.rolling(63, min_periods=21).mean()
    result = _f041_quiet_accumulation(closeadj, volume, 63) * np.log1p(mc)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: compression rank percentile × close
def f041vvc_f041_volume_volatility_compression_cmprank_21d_base_v125_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: compression rank pct 63d × close
def f041vvc_f041_volume_volatility_compression_cmprank_63d_base_v126_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: vol range rank pct × close
def f041vvc_f041_volume_volatility_compression_vrrank_21d_base_v127_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: vol range rank pct 63d × close
def f041vvc_f041_volume_volatility_compression_vrrank_63d_base_v128_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 5d EMA of compression × close
def f041vvc_f041_volume_volatility_compression_cmpema_5d_base_v129_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 10d EMA of compression × close
def f041vvc_f041_volume_volatility_compression_cmpema_10d_base_v130_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.ewm(span=10, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 5d EMA of vol range × close
def f041vvc_f041_volume_volatility_compression_vrema_5d_base_v131_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = base.ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 10d EMA of vol range × close
def f041vvc_f041_volume_volatility_compression_vrema_10d_base_v132_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = base.ewm(span=10, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: compression × signed return
def f041vvc_f041_volume_volatility_compression_cmpxsret_21d_base_v133_signal(closeadj, volume):
    r = closeadj.pct_change(periods=21)
    result = _f041_vol_vol_compression(volume, 21) * np.sign(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: compression × signed return 63d
def f041vvc_f041_volume_volatility_compression_cmpxsret_63d_base_v134_signal(closeadj, volume):
    r = closeadj.pct_change(periods=63)
    result = _f041_vol_vol_compression(volume, 63) * np.sign(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: vol range × signed return
def f041vvc_f041_volume_volatility_compression_vrxsret_21d_base_v135_signal(closeadj, volume):
    r = closeadj.pct_change(periods=21)
    result = _f041_vol_range(volume, 21) * np.sign(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: vol range × signed return 63d
def f041vvc_f041_volume_volatility_compression_vrxsret_63d_base_v136_signal(closeadj, volume):
    r = closeadj.pct_change(periods=63)
    result = _f041_vol_range(volume, 63) * np.sign(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: vol range × vol z 21d
def f041vvc_f041_volume_volatility_compression_vrxvz_21d_base_v137_signal(closeadj, volume):
    result = _f041_vol_range(volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: vol range × vol z 63d
def f041vvc_f041_volume_volatility_compression_vrxvz_63d_base_v138_signal(closeadj, volume):
    result = _f041_vol_range(volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: compression × vol z 21d
def f041vvc_f041_volume_volatility_compression_cmpxvz_21d_base_v139_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: compression × vol z 63d
def f041vvc_f041_volume_volatility_compression_cmpxvz_63d_base_v140_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: quiet acc × dollar volume 21d
def f041vvc_f041_volume_volatility_compression_quietxdv_21d_base_v141_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 21) * np.log1p(closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: quiet acc × dollar volume 63d
def f041vvc_f041_volume_volatility_compression_quietxdv_63d_base_v142_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 63) * np.log1p(closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: vol range cubed × close
def f041vvc_f041_volume_volatility_compression_vrcub_21d_base_v143_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = (base ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: compression cubed × close
def f041vvc_f041_volume_volatility_compression_cmpcub_21d_base_v144_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = (base ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: 21d compression × 21d vol range
def f041vvc_f041_volume_volatility_compression_cmpxvr_21d_base_v145_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 21)
    b = _f041_vol_range(volume, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: 63d compression × 63d vol range
def f041vvc_f041_volume_volatility_compression_cmpxvr_63d_base_v146_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 63)
    b = _f041_vol_range(volume, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: 252d compression × 252d vol range
def f041vvc_f041_volume_volatility_compression_cmpxvr_252d_base_v147_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 252)
    b = _f041_vol_range(volume, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: quiet acc squared
def f041vvc_f041_volume_volatility_compression_quietsq_21d_base_v148_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = -np.sign(base) * (base ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: quiet acc squared 63d
def f041vvc_f041_volume_volatility_compression_quietsq_63d_base_v149_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = -np.sign(base) * (base ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: composite (compression+vol range) × close × volume
def f041vvc_f041_volume_volatility_compression_compcomp_21d_base_v150_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 21)
    b = _f041_vol_range(volume, 21)
    result = (a + b) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f041vvc_f041_volume_volatility_compression_cmpsq_21d_base_v076_signal,
    f041vvc_f041_volume_volatility_compression_cmpsq_63d_base_v077_signal,
    f041vvc_f041_volume_volatility_compression_cmpsq_252d_base_v078_signal,
    f041vvc_f041_volume_volatility_compression_vrsqrt_21d_base_v079_signal,
    f041vvc_f041_volume_volatility_compression_vrsqrt_63d_base_v080_signal,
    f041vvc_f041_volume_volatility_compression_vrsqrt_252d_base_v081_signal,
    f041vvc_f041_volume_volatility_compression_vrmcmp_21d_base_v082_signal,
    f041vvc_f041_volume_volatility_compression_vrmcmp_63d_base_v083_signal,
    f041vvc_f041_volume_volatility_compression_vrmcmp_252d_base_v084_signal,
    f041vvc_f041_volume_volatility_compression_cmpmnv_21d_base_v085_signal,
    f041vvc_f041_volume_volatility_compression_cmpmnv_63d_base_v086_signal,
    f041vvc_f041_volume_volatility_compression_cmpmnv_252d_base_v087_signal,
    f041vvc_f041_volume_volatility_compression_quietema_21d_base_v088_signal,
    f041vvc_f041_volume_volatility_compression_quietema_63d_base_v089_signal,
    f041vvc_f041_volume_volatility_compression_quietema_252d_base_v090_signal,
    f041vvc_f041_volume_volatility_compression_vrz_21d_base_v091_signal,
    f041vvc_f041_volume_volatility_compression_vrz_63d_base_v092_signal,
    f041vvc_f041_volume_volatility_compression_vrz_252d_base_v093_signal,
    f041vvc_f041_volume_volatility_compression_cmpovr_21d_base_v094_signal,
    f041vvc_f041_volume_volatility_compression_cmpovr_63d_base_v095_signal,
    f041vvc_f041_volume_volatility_compression_cmpovr_252d_base_v096_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc_21d_base_v097_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc_63d_base_v098_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc_252d_base_v099_signal,
    f041vvc_f041_volume_volatility_compression_quietxvz_21d_base_v100_signal,
    f041vvc_f041_volume_volatility_compression_quietxvz_63d_base_v101_signal,
    f041vvc_f041_volume_volatility_compression_quietxvz_252d_base_v102_signal,
    f041vvc_f041_volume_volatility_compression_cmpxatr_21d_base_v103_signal,
    f041vvc_f041_volume_volatility_compression_cmpxatr_63d_base_v104_signal,
    f041vvc_f041_volume_volatility_compression_cmpxatr_252d_base_v105_signal,
    f041vvc_f041_volume_volatility_compression_vrxatr_21d_base_v106_signal,
    f041vvc_f041_volume_volatility_compression_vrxatr_63d_base_v107_signal,
    f041vvc_f041_volume_volatility_compression_vrxatr_252d_base_v108_signal,
    f041vvc_f041_volume_volatility_compression_cmpmin_21d_base_v109_signal,
    f041vvc_f041_volume_volatility_compression_cmpmin_63d_base_v110_signal,
    f041vvc_f041_volume_volatility_compression_cmpmax_21d_base_v111_signal,
    f041vvc_f041_volume_volatility_compression_cmpmax_63d_base_v112_signal,
    f041vvc_f041_volume_volatility_compression_lowcmpdur_21d_base_v113_signal,
    f041vvc_f041_volume_volatility_compression_lowcmpdur_63d_base_v114_signal,
    f041vvc_f041_volume_volatility_compression_lowvrdur_21d_base_v115_signal,
    f041vvc_f041_volume_volatility_compression_lowvrdur_63d_base_v116_signal,
    f041vvc_f041_volume_volatility_compression_cmpdelt_21d_base_v117_signal,
    f041vvc_f041_volume_volatility_compression_cmpdelt_63d_base_v118_signal,
    f041vvc_f041_volume_volatility_compression_cmpdelt_252d_base_v119_signal,
    f041vvc_f041_volume_volatility_compression_vrdelt_21d_base_v120_signal,
    f041vvc_f041_volume_volatility_compression_vrdelt_63d_base_v121_signal,
    f041vvc_f041_volume_volatility_compression_vrdelt_252d_base_v122_signal,
    f041vvc_f041_volume_volatility_compression_quietxmc_21d_base_v123_signal,
    f041vvc_f041_volume_volatility_compression_quietxmc_63d_base_v124_signal,
    f041vvc_f041_volume_volatility_compression_cmprank_21d_base_v125_signal,
    f041vvc_f041_volume_volatility_compression_cmprank_63d_base_v126_signal,
    f041vvc_f041_volume_volatility_compression_vrrank_21d_base_v127_signal,
    f041vvc_f041_volume_volatility_compression_vrrank_63d_base_v128_signal,
    f041vvc_f041_volume_volatility_compression_cmpema_5d_base_v129_signal,
    f041vvc_f041_volume_volatility_compression_cmpema_10d_base_v130_signal,
    f041vvc_f041_volume_volatility_compression_vrema_5d_base_v131_signal,
    f041vvc_f041_volume_volatility_compression_vrema_10d_base_v132_signal,
    f041vvc_f041_volume_volatility_compression_cmpxsret_21d_base_v133_signal,
    f041vvc_f041_volume_volatility_compression_cmpxsret_63d_base_v134_signal,
    f041vvc_f041_volume_volatility_compression_vrxsret_21d_base_v135_signal,
    f041vvc_f041_volume_volatility_compression_vrxsret_63d_base_v136_signal,
    f041vvc_f041_volume_volatility_compression_vrxvz_21d_base_v137_signal,
    f041vvc_f041_volume_volatility_compression_vrxvz_63d_base_v138_signal,
    f041vvc_f041_volume_volatility_compression_cmpxvz_21d_base_v139_signal,
    f041vvc_f041_volume_volatility_compression_cmpxvz_63d_base_v140_signal,
    f041vvc_f041_volume_volatility_compression_quietxdv_21d_base_v141_signal,
    f041vvc_f041_volume_volatility_compression_quietxdv_63d_base_v142_signal,
    f041vvc_f041_volume_volatility_compression_vrcub_21d_base_v143_signal,
    f041vvc_f041_volume_volatility_compression_cmpcub_21d_base_v144_signal,
    f041vvc_f041_volume_volatility_compression_cmpxvr_21d_base_v145_signal,
    f041vvc_f041_volume_volatility_compression_cmpxvr_63d_base_v146_signal,
    f041vvc_f041_volume_volatility_compression_cmpxvr_252d_base_v147_signal,
    f041vvc_f041_volume_volatility_compression_quietsq_21d_base_v148_signal,
    f041vvc_f041_volume_volatility_compression_quietsq_63d_base_v149_signal,
    f041vvc_f041_volume_volatility_compression_compcomp_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F041_VOLUME_VOLATILITY_COMPRESSION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f041_vol_range", "_f041_vol_vol_compression", "_f041_quiet_accumulation")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f041_volume_volatility_compression_base_076_150_claude: {n_features} features pass")
