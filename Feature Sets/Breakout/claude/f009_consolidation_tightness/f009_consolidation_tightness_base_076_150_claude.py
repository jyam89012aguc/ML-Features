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
def _f009_close_std_norm(close, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / m.replace(0, np.nan).abs()


def _f009_coiling_score(close, w):
    sd_short = close.rolling(max(2, w // 3), min_periods=max(1, w // 6)).std()
    sd_long = close.rolling(w, min_periods=max(1, w // 2)).std()
    return sd_short / sd_long.replace(0, np.nan).abs()


def _f009_tightness_signature(close, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    cv = sd / m.replace(0, np.nan).abs()
    med = cv.rolling(252, min_periods=63).median()
    return (med - cv) / med.replace(0, np.nan).abs()


# v076-v080: in-range count × rolling close mean
def f009ctn_f009_consolidation_tightness_inrxcmean_21d_base_v076_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcmean_63d_base_v077_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcmean_126d_base_v078_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcmean_252d_base_v079_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcmean_504d_base_v080_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 504) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v081-v085: base length × rolling close mean
def f009ctn_f009_consolidation_tightness_blenxcmean_21d_base_v081_signal(closeadj):
    result = _f009_coiling_score(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcmean_63d_base_v082_signal(closeadj):
    result = _f009_coiling_score(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcmean_126d_base_v083_signal(closeadj):
    result = _f009_coiling_score(closeadj, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcmean_252d_base_v084_signal(closeadj):
    result = _f009_coiling_score(closeadj, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcmean_504d_base_v085_signal(closeadj):
    result = _f009_coiling_score(closeadj, 504) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v086-v090: in-range × close std
def f009ctn_f009_consolidation_tightness_inrxcstd_21d_base_v086_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcstd_63d_base_v087_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcstd_126d_base_v088_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcstd_252d_base_v089_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxcstd_504d_base_v090_signal(closeadj):
    result = _f009_close_std_norm(closeadj, 504) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v095: base length × close std
def f009ctn_f009_consolidation_tightness_blenxcstd_21d_base_v091_signal(closeadj):
    result = _f009_coiling_score(closeadj, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcstd_63d_base_v092_signal(closeadj):
    result = _f009_coiling_score(closeadj, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcstd_126d_base_v093_signal(closeadj):
    result = _f009_coiling_score(closeadj, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcstd_252d_base_v094_signal(closeadj):
    result = _f009_coiling_score(closeadj, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxcstd_504d_base_v095_signal(closeadj):
    result = _f009_coiling_score(closeadj, 504) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v096-v100: consolidation × close
def f009ctn_f009_consolidation_tightness_consxc_21d_base_v096_signal(closeadj):
    result = _f009_tightness_signature(closeadj, 21) * closeadj * 1.1
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxc_63d_base_v097_signal(closeadj):
    result = _f009_tightness_signature(closeadj, 63) * closeadj * 1.2
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxc_126d_base_v098_signal(closeadj):
    result = _f009_tightness_signature(closeadj, 126) * closeadj * 1.3
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxc_252d_base_v099_signal(closeadj):
    result = _f009_tightness_signature(closeadj, 252) * closeadj * 1.4
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxc_504d_base_v100_signal(closeadj):
    result = _f009_tightness_signature(closeadj, 504) * closeadj * 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# v101-v105: in-range × volume
def f009ctn_f009_consolidation_tightness_inrxvol_21d_base_v101_signal(closeadj, volume):
    result = _f009_close_std_norm(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_63d_base_v102_signal(closeadj, volume):
    result = _f009_close_std_norm(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_126d_base_v103_signal(closeadj, volume):
    result = _f009_close_std_norm(closeadj, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_252d_base_v104_signal(closeadj, volume):
    result = _f009_close_std_norm(closeadj, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_504d_base_v105_signal(closeadj, volume):
    result = _f009_close_std_norm(closeadj, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v110: in-range × dollar volume
def f009ctn_f009_consolidation_tightness_inrxdv_21d_base_v106_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f009_close_std_norm(closeadj, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_63d_base_v107_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f009_close_std_norm(closeadj, 63) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_126d_base_v108_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f009_close_std_norm(closeadj, 126) * _mean(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_252d_base_v109_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f009_close_std_norm(closeadj, 252) * _mean(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_504d_base_v110_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f009_close_std_norm(closeadj, 504) * _mean(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v111-v115: base length × volume
def f009ctn_f009_consolidation_tightness_blenxvol_21d_base_v111_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_63d_base_v112_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_126d_base_v113_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_252d_base_v114_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_504d_base_v115_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v116-v120: in-range × high-low range
def f009ctn_f009_consolidation_tightness_inrxhlr_21d_base_v116_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f009_close_std_norm(closeadj, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_63d_base_v117_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f009_close_std_norm(closeadj, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_126d_base_v118_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    result = _f009_close_std_norm(closeadj, 126) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_252d_base_v119_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    result = _f009_close_std_norm(closeadj, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_504d_base_v120_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    result = _f009_close_std_norm(closeadj, 504) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v125: log(1 + base length) × close
def f009ctn_f009_consolidation_tightness_lnbase_21d_base_v121_signal(closeadj):
    result = np.log1p(np.abs(_f009_coiling_score(closeadj, 21)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnbase_63d_base_v122_signal(closeadj):
    result = np.log1p(np.abs(_f009_coiling_score(closeadj, 63)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnbase_126d_base_v123_signal(closeadj):
    result = np.log1p(np.abs(_f009_coiling_score(closeadj, 126)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnbase_252d_base_v124_signal(closeadj):
    result = np.log1p(np.abs(_f009_coiling_score(closeadj, 252)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnbase_504d_base_v125_signal(closeadj):
    result = np.log1p(np.abs(_f009_coiling_score(closeadj, 504)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126-v130: sqrt(in-range) × close
def f009ctn_f009_consolidation_tightness_sqrtinr_21d_base_v126_signal(closeadj):
    result = np.sqrt(np.abs(_f009_close_std_norm(closeadj, 21)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_sqrtinr_63d_base_v127_signal(closeadj):
    result = np.sqrt(np.abs(_f009_close_std_norm(closeadj, 63)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_sqrtinr_126d_base_v128_signal(closeadj):
    result = np.sqrt(np.abs(_f009_close_std_norm(closeadj, 126)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_sqrtinr_252d_base_v129_signal(closeadj):
    result = np.sqrt(np.abs(_f009_close_std_norm(closeadj, 252)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_sqrtinr_504d_base_v130_signal(closeadj):
    result = np.sqrt(np.abs(_f009_close_std_norm(closeadj, 504)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131-v135: cube of in-range fraction × close
def f009ctn_f009_consolidation_tightness_inrcube_21d_base_v131_signal(closeadj):
    frac = _f009_close_std_norm(closeadj, 21) / 21.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrcube_63d_base_v132_signal(closeadj):
    frac = _f009_close_std_norm(closeadj, 63) / 63.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrcube_126d_base_v133_signal(closeadj):
    frac = _f009_close_std_norm(closeadj, 126) / 126.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrcube_252d_base_v134_signal(closeadj):
    frac = _f009_close_std_norm(closeadj, 252) / 252.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrcube_504d_base_v135_signal(closeadj):
    frac = _f009_close_std_norm(closeadj, 504) / 504.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v140: base length × volume z
def f009ctn_f009_consolidation_tightness_blenxvolz_21d_base_v136_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvolz_63d_base_v137_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvolz_126d_base_v138_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 126) * _z(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvolz_252d_base_v139_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvolz_504d_base_v140_signal(closeadj, volume):
    result = _f009_coiling_score(closeadj, 504) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141-v145: consolidation × volume
def f009ctn_f009_consolidation_tightness_consxvol_21d_base_v141_signal(closeadj, volume):
    result = _f009_tightness_signature(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_63d_base_v142_signal(closeadj, volume):
    result = _f009_tightness_signature(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_126d_base_v143_signal(closeadj, volume):
    result = _f009_tightness_signature(closeadj, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_252d_base_v144_signal(closeadj, volume):
    result = _f009_tightness_signature(closeadj, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_504d_base_v145_signal(closeadj, volume):
    result = _f009_tightness_signature(closeadj, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v146-v150: EMA of base length × close
def f009ctn_f009_consolidation_tightness_blenema_21d_base_v146_signal(closeadj):
    base = _f009_coiling_score(closeadj, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_63d_base_v147_signal(closeadj):
    base = _f009_coiling_score(closeadj, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_126d_base_v148_signal(closeadj):
    base = _f009_coiling_score(closeadj, 126)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_252d_base_v149_signal(closeadj):
    base = _f009_coiling_score(closeadj, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_504d_base_v150_signal(closeadj):
    base = _f009_coiling_score(closeadj, 504)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f009ctn_f009_consolidation_tightness_inrxcmean_21d_base_v076_signal,
    f009ctn_f009_consolidation_tightness_inrxcmean_63d_base_v077_signal,
    f009ctn_f009_consolidation_tightness_inrxcmean_126d_base_v078_signal,
    f009ctn_f009_consolidation_tightness_inrxcmean_252d_base_v079_signal,
    f009ctn_f009_consolidation_tightness_inrxcmean_504d_base_v080_signal,
    f009ctn_f009_consolidation_tightness_blenxcmean_21d_base_v081_signal,
    f009ctn_f009_consolidation_tightness_blenxcmean_63d_base_v082_signal,
    f009ctn_f009_consolidation_tightness_blenxcmean_126d_base_v083_signal,
    f009ctn_f009_consolidation_tightness_blenxcmean_252d_base_v084_signal,
    f009ctn_f009_consolidation_tightness_blenxcmean_504d_base_v085_signal,
    f009ctn_f009_consolidation_tightness_inrxcstd_21d_base_v086_signal,
    f009ctn_f009_consolidation_tightness_inrxcstd_63d_base_v087_signal,
    f009ctn_f009_consolidation_tightness_inrxcstd_126d_base_v088_signal,
    f009ctn_f009_consolidation_tightness_inrxcstd_252d_base_v089_signal,
    f009ctn_f009_consolidation_tightness_inrxcstd_504d_base_v090_signal,
    f009ctn_f009_consolidation_tightness_blenxcstd_21d_base_v091_signal,
    f009ctn_f009_consolidation_tightness_blenxcstd_63d_base_v092_signal,
    f009ctn_f009_consolidation_tightness_blenxcstd_126d_base_v093_signal,
    f009ctn_f009_consolidation_tightness_blenxcstd_252d_base_v094_signal,
    f009ctn_f009_consolidation_tightness_blenxcstd_504d_base_v095_signal,
    f009ctn_f009_consolidation_tightness_consxc_21d_base_v096_signal,
    f009ctn_f009_consolidation_tightness_consxc_63d_base_v097_signal,
    f009ctn_f009_consolidation_tightness_consxc_126d_base_v098_signal,
    f009ctn_f009_consolidation_tightness_consxc_252d_base_v099_signal,
    f009ctn_f009_consolidation_tightness_consxc_504d_base_v100_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_21d_base_v101_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_63d_base_v102_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_126d_base_v103_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_252d_base_v104_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_504d_base_v105_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_21d_base_v106_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_63d_base_v107_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_126d_base_v108_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_252d_base_v109_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_504d_base_v110_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_21d_base_v111_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_63d_base_v112_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_126d_base_v113_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_252d_base_v114_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_504d_base_v115_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_21d_base_v116_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_63d_base_v117_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_126d_base_v118_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_252d_base_v119_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_504d_base_v120_signal,
    f009ctn_f009_consolidation_tightness_lnbase_21d_base_v121_signal,
    f009ctn_f009_consolidation_tightness_lnbase_63d_base_v122_signal,
    f009ctn_f009_consolidation_tightness_lnbase_126d_base_v123_signal,
    f009ctn_f009_consolidation_tightness_lnbase_252d_base_v124_signal,
    f009ctn_f009_consolidation_tightness_lnbase_504d_base_v125_signal,
    f009ctn_f009_consolidation_tightness_sqrtinr_21d_base_v126_signal,
    f009ctn_f009_consolidation_tightness_sqrtinr_63d_base_v127_signal,
    f009ctn_f009_consolidation_tightness_sqrtinr_126d_base_v128_signal,
    f009ctn_f009_consolidation_tightness_sqrtinr_252d_base_v129_signal,
    f009ctn_f009_consolidation_tightness_sqrtinr_504d_base_v130_signal,
    f009ctn_f009_consolidation_tightness_inrcube_21d_base_v131_signal,
    f009ctn_f009_consolidation_tightness_inrcube_63d_base_v132_signal,
    f009ctn_f009_consolidation_tightness_inrcube_126d_base_v133_signal,
    f009ctn_f009_consolidation_tightness_inrcube_252d_base_v134_signal,
    f009ctn_f009_consolidation_tightness_inrcube_504d_base_v135_signal,
    f009ctn_f009_consolidation_tightness_blenxvolz_21d_base_v136_signal,
    f009ctn_f009_consolidation_tightness_blenxvolz_63d_base_v137_signal,
    f009ctn_f009_consolidation_tightness_blenxvolz_126d_base_v138_signal,
    f009ctn_f009_consolidation_tightness_blenxvolz_252d_base_v139_signal,
    f009ctn_f009_consolidation_tightness_blenxvolz_504d_base_v140_signal,
    f009ctn_f009_consolidation_tightness_consxvol_21d_base_v141_signal,
    f009ctn_f009_consolidation_tightness_consxvol_63d_base_v142_signal,
    f009ctn_f009_consolidation_tightness_consxvol_126d_base_v143_signal,
    f009ctn_f009_consolidation_tightness_consxvol_252d_base_v144_signal,
    f009ctn_f009_consolidation_tightness_consxvol_504d_base_v145_signal,
    f009ctn_f009_consolidation_tightness_blenema_21d_base_v146_signal,
    f009ctn_f009_consolidation_tightness_blenema_63d_base_v147_signal,
    f009ctn_f009_consolidation_tightness_blenema_126d_base_v148_signal,
    f009ctn_f009_consolidation_tightness_blenema_252d_base_v149_signal,
    f009ctn_f009_consolidation_tightness_blenema_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F009_CONSOLIDATION_TIGHTNESS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f009_close_std_norm", "_f009_coiling_score", "_f009_tightness_signature")
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
    print(f"OK f009_consolidation_tightness_base_076_150_claude: {n_features} features pass")
