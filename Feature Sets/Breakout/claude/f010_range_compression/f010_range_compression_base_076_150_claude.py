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
def _f010_n_day_range(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo)


def _f010_range_compression(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    rng_short = (hi - lo)
    rng_long = (high.rolling(w * 2, min_periods=max(1, w)).max()
                - low.rolling(w * 2, min_periods=max(1, w)).min())
    return rng_short / rng_long.replace(0, np.nan).abs()


def _f010_compression_ratio(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (hi - lo)
    med = rng.rolling(252, min_periods=63).median()
    return (med - rng) / med.replace(0, np.nan).abs()


# v076-v080: in-range count × rolling close mean
def f010rcm_f010_range_compression_inrxcmean_21d_base_v076_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcmean_63d_base_v077_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcmean_126d_base_v078_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcmean_252d_base_v079_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcmean_504d_base_v080_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 504) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v081-v085: base length × rolling close mean
def f010rcm_f010_range_compression_blenxcmean_21d_base_v081_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcmean_63d_base_v082_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcmean_126d_base_v083_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcmean_252d_base_v084_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcmean_504d_base_v085_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 504) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v086-v090: in-range × close std
def f010rcm_f010_range_compression_inrxcstd_21d_base_v086_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcstd_63d_base_v087_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcstd_126d_base_v088_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcstd_252d_base_v089_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxcstd_504d_base_v090_signal(closeadj, high, low):
    result = _f010_n_day_range(high, low, 504) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v095: base length × close std
def f010rcm_f010_range_compression_blenxcstd_21d_base_v091_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcstd_63d_base_v092_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcstd_126d_base_v093_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcstd_252d_base_v094_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxcstd_504d_base_v095_signal(closeadj, high, low):
    result = _f010_range_compression(high, low, 504) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v096-v100: consolidation × close
def f010rcm_f010_range_compression_consxc_21d_base_v096_signal(closeadj, high, low):
    result = _f010_compression_ratio(high, low, 21) * closeadj * 1.1
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxc_63d_base_v097_signal(closeadj, high, low):
    result = _f010_compression_ratio(high, low, 63) * closeadj * 1.2
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxc_126d_base_v098_signal(closeadj, high, low):
    result = _f010_compression_ratio(high, low, 126) * closeadj * 1.3
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxc_252d_base_v099_signal(closeadj, high, low):
    result = _f010_compression_ratio(high, low, 252) * closeadj * 1.4
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxc_504d_base_v100_signal(closeadj, high, low):
    result = _f010_compression_ratio(high, low, 504) * closeadj * 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# v101-v105: in-range × volume
def f010rcm_f010_range_compression_inrxvol_21d_base_v101_signal(closeadj, high, low, volume):
    result = _f010_n_day_range(high, low, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_63d_base_v102_signal(closeadj, high, low, volume):
    result = _f010_n_day_range(high, low, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_126d_base_v103_signal(closeadj, high, low, volume):
    result = _f010_n_day_range(high, low, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_252d_base_v104_signal(closeadj, high, low, volume):
    result = _f010_n_day_range(high, low, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_504d_base_v105_signal(closeadj, high, low, volume):
    result = _f010_n_day_range(high, low, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v110: in-range × dollar volume
def f010rcm_f010_range_compression_inrxdv_21d_base_v106_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f010_n_day_range(high, low, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_63d_base_v107_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f010_n_day_range(high, low, 63) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_126d_base_v108_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f010_n_day_range(high, low, 126) * _mean(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_252d_base_v109_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f010_n_day_range(high, low, 252) * _mean(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_504d_base_v110_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f010_n_day_range(high, low, 504) * _mean(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v111-v115: base length × volume
def f010rcm_f010_range_compression_blenxvol_21d_base_v111_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_63d_base_v112_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_126d_base_v113_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_252d_base_v114_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_504d_base_v115_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v116-v120: in-range × high-low range
def f010rcm_f010_range_compression_inrxhlr_21d_base_v116_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f010_n_day_range(high, low, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_63d_base_v117_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f010_n_day_range(high, low, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_126d_base_v118_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    result = _f010_n_day_range(high, low, 126) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_252d_base_v119_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    result = _f010_n_day_range(high, low, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_504d_base_v120_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    result = _f010_n_day_range(high, low, 504) * rng
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v125: log(1 + base length) × close
def f010rcm_f010_range_compression_lnbase_21d_base_v121_signal(closeadj, high, low):
    result = np.log1p(np.abs(_f010_range_compression(high, low, 21)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnbase_63d_base_v122_signal(closeadj, high, low):
    result = np.log1p(np.abs(_f010_range_compression(high, low, 63)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnbase_126d_base_v123_signal(closeadj, high, low):
    result = np.log1p(np.abs(_f010_range_compression(high, low, 126)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnbase_252d_base_v124_signal(closeadj, high, low):
    result = np.log1p(np.abs(_f010_range_compression(high, low, 252)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnbase_504d_base_v125_signal(closeadj, high, low):
    result = np.log1p(np.abs(_f010_range_compression(high, low, 504)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126-v130: sqrt(in-range) × close
def f010rcm_f010_range_compression_sqrtinr_21d_base_v126_signal(closeadj, high, low):
    result = np.sqrt(np.abs(_f010_n_day_range(high, low, 21)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_sqrtinr_63d_base_v127_signal(closeadj, high, low):
    result = np.sqrt(np.abs(_f010_n_day_range(high, low, 63)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_sqrtinr_126d_base_v128_signal(closeadj, high, low):
    result = np.sqrt(np.abs(_f010_n_day_range(high, low, 126)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_sqrtinr_252d_base_v129_signal(closeadj, high, low):
    result = np.sqrt(np.abs(_f010_n_day_range(high, low, 252)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_sqrtinr_504d_base_v130_signal(closeadj, high, low):
    result = np.sqrt(np.abs(_f010_n_day_range(high, low, 504)) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131-v135: cube of in-range fraction × close
def f010rcm_f010_range_compression_inrcube_21d_base_v131_signal(closeadj, high, low):
    frac = _f010_n_day_range(high, low, 21) / 21.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrcube_63d_base_v132_signal(closeadj, high, low):
    frac = _f010_n_day_range(high, low, 63) / 63.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrcube_126d_base_v133_signal(closeadj, high, low):
    frac = _f010_n_day_range(high, low, 126) / 126.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrcube_252d_base_v134_signal(closeadj, high, low):
    frac = _f010_n_day_range(high, low, 252) / 252.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrcube_504d_base_v135_signal(closeadj, high, low):
    frac = _f010_n_day_range(high, low, 504) / 504.0
    result = (frac ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v140: base length × volume z
def f010rcm_f010_range_compression_blenxvolz_21d_base_v136_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvolz_63d_base_v137_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvolz_126d_base_v138_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 126) * _z(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvolz_252d_base_v139_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvolz_504d_base_v140_signal(closeadj, high, low, volume):
    result = _f010_range_compression(high, low, 504) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141-v145: consolidation × volume
def f010rcm_f010_range_compression_consxvol_21d_base_v141_signal(closeadj, high, low, volume):
    result = _f010_compression_ratio(high, low, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_63d_base_v142_signal(closeadj, high, low, volume):
    result = _f010_compression_ratio(high, low, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_126d_base_v143_signal(closeadj, high, low, volume):
    result = _f010_compression_ratio(high, low, 126) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_252d_base_v144_signal(closeadj, high, low, volume):
    result = _f010_compression_ratio(high, low, 252) * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_504d_base_v145_signal(closeadj, high, low, volume):
    result = _f010_compression_ratio(high, low, 504) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# v146-v150: EMA of base length × close
def f010rcm_f010_range_compression_blenema_21d_base_v146_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_63d_base_v147_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_126d_base_v148_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 126)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_252d_base_v149_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_504d_base_v150_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 504)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f010rcm_f010_range_compression_inrxcmean_21d_base_v076_signal,
    f010rcm_f010_range_compression_inrxcmean_63d_base_v077_signal,
    f010rcm_f010_range_compression_inrxcmean_126d_base_v078_signal,
    f010rcm_f010_range_compression_inrxcmean_252d_base_v079_signal,
    f010rcm_f010_range_compression_inrxcmean_504d_base_v080_signal,
    f010rcm_f010_range_compression_blenxcmean_21d_base_v081_signal,
    f010rcm_f010_range_compression_blenxcmean_63d_base_v082_signal,
    f010rcm_f010_range_compression_blenxcmean_126d_base_v083_signal,
    f010rcm_f010_range_compression_blenxcmean_252d_base_v084_signal,
    f010rcm_f010_range_compression_blenxcmean_504d_base_v085_signal,
    f010rcm_f010_range_compression_inrxcstd_21d_base_v086_signal,
    f010rcm_f010_range_compression_inrxcstd_63d_base_v087_signal,
    f010rcm_f010_range_compression_inrxcstd_126d_base_v088_signal,
    f010rcm_f010_range_compression_inrxcstd_252d_base_v089_signal,
    f010rcm_f010_range_compression_inrxcstd_504d_base_v090_signal,
    f010rcm_f010_range_compression_blenxcstd_21d_base_v091_signal,
    f010rcm_f010_range_compression_blenxcstd_63d_base_v092_signal,
    f010rcm_f010_range_compression_blenxcstd_126d_base_v093_signal,
    f010rcm_f010_range_compression_blenxcstd_252d_base_v094_signal,
    f010rcm_f010_range_compression_blenxcstd_504d_base_v095_signal,
    f010rcm_f010_range_compression_consxc_21d_base_v096_signal,
    f010rcm_f010_range_compression_consxc_63d_base_v097_signal,
    f010rcm_f010_range_compression_consxc_126d_base_v098_signal,
    f010rcm_f010_range_compression_consxc_252d_base_v099_signal,
    f010rcm_f010_range_compression_consxc_504d_base_v100_signal,
    f010rcm_f010_range_compression_inrxvol_21d_base_v101_signal,
    f010rcm_f010_range_compression_inrxvol_63d_base_v102_signal,
    f010rcm_f010_range_compression_inrxvol_126d_base_v103_signal,
    f010rcm_f010_range_compression_inrxvol_252d_base_v104_signal,
    f010rcm_f010_range_compression_inrxvol_504d_base_v105_signal,
    f010rcm_f010_range_compression_inrxdv_21d_base_v106_signal,
    f010rcm_f010_range_compression_inrxdv_63d_base_v107_signal,
    f010rcm_f010_range_compression_inrxdv_126d_base_v108_signal,
    f010rcm_f010_range_compression_inrxdv_252d_base_v109_signal,
    f010rcm_f010_range_compression_inrxdv_504d_base_v110_signal,
    f010rcm_f010_range_compression_blenxvol_21d_base_v111_signal,
    f010rcm_f010_range_compression_blenxvol_63d_base_v112_signal,
    f010rcm_f010_range_compression_blenxvol_126d_base_v113_signal,
    f010rcm_f010_range_compression_blenxvol_252d_base_v114_signal,
    f010rcm_f010_range_compression_blenxvol_504d_base_v115_signal,
    f010rcm_f010_range_compression_inrxhlr_21d_base_v116_signal,
    f010rcm_f010_range_compression_inrxhlr_63d_base_v117_signal,
    f010rcm_f010_range_compression_inrxhlr_126d_base_v118_signal,
    f010rcm_f010_range_compression_inrxhlr_252d_base_v119_signal,
    f010rcm_f010_range_compression_inrxhlr_504d_base_v120_signal,
    f010rcm_f010_range_compression_lnbase_21d_base_v121_signal,
    f010rcm_f010_range_compression_lnbase_63d_base_v122_signal,
    f010rcm_f010_range_compression_lnbase_126d_base_v123_signal,
    f010rcm_f010_range_compression_lnbase_252d_base_v124_signal,
    f010rcm_f010_range_compression_lnbase_504d_base_v125_signal,
    f010rcm_f010_range_compression_sqrtinr_21d_base_v126_signal,
    f010rcm_f010_range_compression_sqrtinr_63d_base_v127_signal,
    f010rcm_f010_range_compression_sqrtinr_126d_base_v128_signal,
    f010rcm_f010_range_compression_sqrtinr_252d_base_v129_signal,
    f010rcm_f010_range_compression_sqrtinr_504d_base_v130_signal,
    f010rcm_f010_range_compression_inrcube_21d_base_v131_signal,
    f010rcm_f010_range_compression_inrcube_63d_base_v132_signal,
    f010rcm_f010_range_compression_inrcube_126d_base_v133_signal,
    f010rcm_f010_range_compression_inrcube_252d_base_v134_signal,
    f010rcm_f010_range_compression_inrcube_504d_base_v135_signal,
    f010rcm_f010_range_compression_blenxvolz_21d_base_v136_signal,
    f010rcm_f010_range_compression_blenxvolz_63d_base_v137_signal,
    f010rcm_f010_range_compression_blenxvolz_126d_base_v138_signal,
    f010rcm_f010_range_compression_blenxvolz_252d_base_v139_signal,
    f010rcm_f010_range_compression_blenxvolz_504d_base_v140_signal,
    f010rcm_f010_range_compression_consxvol_21d_base_v141_signal,
    f010rcm_f010_range_compression_consxvol_63d_base_v142_signal,
    f010rcm_f010_range_compression_consxvol_126d_base_v143_signal,
    f010rcm_f010_range_compression_consxvol_252d_base_v144_signal,
    f010rcm_f010_range_compression_consxvol_504d_base_v145_signal,
    f010rcm_f010_range_compression_blenema_21d_base_v146_signal,
    f010rcm_f010_range_compression_blenema_63d_base_v147_signal,
    f010rcm_f010_range_compression_blenema_126d_base_v148_signal,
    f010rcm_f010_range_compression_blenema_252d_base_v149_signal,
    f010rcm_f010_range_compression_blenema_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F010_RANGE_COMPRESSION_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f010_n_day_range", "_f010_range_compression", "_f010_compression_ratio")
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
    print(f"OK f010_range_compression_base_076_150_claude: {n_features} features pass")
