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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w)


def _jerk(s, w):
    sl = s.diff(periods=w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====

def _f42_sales_machine_per_asset(revenue, assets, w):
    return (revenue / assets.replace(0, np.nan).abs()).rolling(w, min_periods=max(1, w // 2)).mean()


def _f42_sales_machine_per_share(revenue, sharesbas, w):
    return (revenue / sharesbas.replace(0, np.nan).abs()).rolling(w, min_periods=max(1, w // 2)).mean()

# raw of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_raw_21d_21d_base_v076_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean21_21d_21d_base_v077_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean63_21d_21d_base_v078_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_std63_21d_21d_base_v079_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z63_21d_21d_base_v080_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z252_21d_21d_base_v081_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema21_21d_21d_base_v082_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema63_21d_21d_base_v083_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_absmean63_21d_21d_base_v084_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 21d primitive for f42_sales_machine
def f42sm_f42_sales_machine_sqrmean63_21d_21d_base_v085_signal(revenue, assets, sharesbas, closeadj):
    base = ((_f42_sales_machine_per_asset(revenue, assets, 21)) * (_f42_sales_machine_per_asset(revenue, assets, 21)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_raw_63d_63d_base_v086_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean21_63d_63d_base_v087_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 63), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean63_63d_63d_base_v088_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_std63_63d_63d_base_v089_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z63_63d_63d_base_v090_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z252_63d_63d_base_v091_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema21_63d_63d_base_v092_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema63_63d_63d_base_v093_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_absmean63_63d_63d_base_v094_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 63d primitive for f42_sales_machine
def f42sm_f42_sales_machine_sqrmean63_63d_63d_base_v095_signal(revenue, assets, sharesbas, closeadj):
    base = ((_f42_sales_machine_per_asset(revenue, assets, 63)) * (_f42_sales_machine_per_asset(revenue, assets, 63)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_raw_126d_126d_base_v096_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 126))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean21_126d_126d_base_v097_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 126), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean63_126d_126d_base_v098_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_std63_126d_126d_base_v099_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z63_126d_126d_base_v100_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 126), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z252_126d_126d_base_v101_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 126), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema21_126d_126d_base_v102_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 126)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema63_126d_126d_base_v103_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 126)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_absmean63_126d_126d_base_v104_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 126)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 126d primitive for f42_sales_machine
def f42sm_f42_sales_machine_sqrmean63_126d_126d_base_v105_signal(revenue, assets, sharesbas, closeadj):
    base = ((_f42_sales_machine_per_asset(revenue, assets, 126)) * (_f42_sales_machine_per_asset(revenue, assets, 126)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_raw_252d_252d_base_v106_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean21_252d_252d_base_v107_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 252), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean63_252d_252d_base_v108_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_std63_252d_252d_base_v109_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z63_252d_252d_base_v110_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 252), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z252_252d_252d_base_v111_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema21_252d_252d_base_v112_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema63_252d_252d_base_v113_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_absmean63_252d_252d_base_v114_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 252d primitive for f42_sales_machine
def f42sm_f42_sales_machine_sqrmean63_252d_252d_base_v115_signal(revenue, assets, sharesbas, closeadj):
    base = ((_f42_sales_machine_per_asset(revenue, assets, 252)) * (_f42_sales_machine_per_asset(revenue, assets, 252)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# raw of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_raw_504d_504d_base_v116_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean21 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean21_504d_504d_base_v117_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 504), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_mean63_504d_504d_base_v118_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_std63_504d_504d_base_v119_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z63_504d_504d_base_v120_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 504), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z252 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_z252_504d_504d_base_v121_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 504), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema21 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema21_504d_504d_base_v122_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504)).ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_ema63_504d_504d_base_v123_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504)).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_absmean63_504d_504d_base_v124_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504)).abs().rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sqrmean63 of 504d primitive for f42_sales_machine
def f42sm_f42_sales_machine_sqrmean63_504d_504d_base_v125_signal(revenue, assets, sharesbas, closeadj):
    base = ((_f42_sales_machine_per_asset(revenue, assets, 504)) * (_f42_sales_machine_per_asset(revenue, assets, 504)).abs()).rolling(63, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f42sm_f42_sales_machine_ema126_21d_21d_base_v126_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f42sm_f42_sales_machine_ema252_63d_63d_base_v127_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f42sm_f42_sales_machine_mean126_126d_126d_base_v128_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f42sm_f42_sales_machine_mean252_252d_252d_base_v129_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f42sm_f42_sales_machine_std126_504d_504d_base_v130_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f42sm_f42_sales_machine_std21_21d_21d_base_v131_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f42sm_f42_sales_machine_z126_63d_63d_base_v132_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f42sm_f42_sales_machine_z504_126d_126d_base_v133_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f42sm_f42_sales_machine_absmean21_252d_252d_base_v134_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f42sm_f42_sales_machine_absmean252_504d_504d_base_v135_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f42sm_f42_sales_machine_ema126_21d_21d_base_v136_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f42sm_f42_sales_machine_ema252_63d_63d_base_v137_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f42sm_f42_sales_machine_mean126_126d_126d_base_v138_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f42sm_f42_sales_machine_mean252_252d_252d_base_v139_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f42sm_f42_sales_machine_std126_504d_504d_base_v140_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std21 of 21d primitive
def f42sm_f42_sales_machine_std21_21d_21d_base_v141_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z126 of 63d primitive
def f42sm_f42_sales_machine_z126_63d_63d_base_v142_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# z504 of 126d primitive
def f42sm_f42_sales_machine_z504_126d_126d_base_v143_signal(revenue, assets, sharesbas, closeadj):
    base = _z(_f42_sales_machine_per_asset(revenue, assets, 126), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean21 of 252d primitive
def f42sm_f42_sales_machine_absmean21_252d_252d_base_v144_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 252)).abs().rolling(21, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# absmean252 of 504d primitive
def f42sm_f42_sales_machine_absmean252_504d_504d_base_v145_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 504)).abs().rolling(252, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema126 of 21d primitive
def f42sm_f42_sales_machine_ema126_21d_21d_base_v146_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 21)).ewm(span=126, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# ema252 of 63d primitive
def f42sm_f42_sales_machine_ema252_63d_63d_base_v147_signal(revenue, assets, sharesbas, closeadj):
    base = (_f42_sales_machine_per_asset(revenue, assets, 63)).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean126 of 126d primitive
def f42sm_f42_sales_machine_mean126_126d_126d_base_v148_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 126), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# mean252 of 252d primitive
def f42sm_f42_sales_machine_mean252_252d_252d_base_v149_signal(revenue, assets, sharesbas, closeadj):
    base = _mean(_f42_sales_machine_per_asset(revenue, assets, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# std126 of 504d primitive
def f42sm_f42_sales_machine_std126_504d_504d_base_v150_signal(revenue, assets, sharesbas, closeadj):
    base = _std(_f42_sales_machine_per_asset(revenue, assets, 504), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f42sm_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    cols = {"revenue": revenue, "assets": assets, "sharesbas": sharesbas, "closeadj": closeadj}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f42_sales_machine_per_asset", "_f42_sales_machine_per_share",)
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f42_sales_machine_base_076_150_claude: {n_features} features pass")
