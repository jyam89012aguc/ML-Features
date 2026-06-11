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
def _f043_up_day_vol(closeadj, volume, w):
    r = closeadj.pct_change()
    up = volume.where(r > 0, 0.0)
    return up.rolling(w, min_periods=max(1, w // 2)).sum()


def _f043_max_down_vol(closeadj, volume, w):
    r = closeadj.pct_change()
    down = volume.where(r < 0, 0.0)
    return down.rolling(w, min_periods=max(1, w // 2)).max()


def _f043_pocket_pivot(closeadj, volume, w):
    r = closeadj.pct_change()
    up_today = volume.where(r > 0, 0.0)
    max_down_10 = volume.where(r < 0, 0.0).rolling(w, min_periods=max(1, w // 2)).max()
    return (up_today - max_down_10) * closeadj


def f043ppf_f043_pocket_pivot_flag_upvol10x_ema63_base_v076_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol10x_sqr_base_v077_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6) * ((_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol10x_zsc63_base_v078_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_ema63_base_v079_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_sqr_base_v080_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6) * ((_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_zsc63_base_v081_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_ema63_base_v082_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_sqr_base_v083_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6) * ((_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_zsc63_base_v084_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_ema63_base_v085_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_sqr_base_v086_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6) * ((_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_zsc63_base_v087_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_ema63_base_v088_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 252) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_sqr_base_v089_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 252) * closeadj / 1e6) * ((_f043_up_day_vol(closeadj, volume, 252) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_zsc63_base_v090_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 252) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema63_base_v091_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_sqr_base_v092_signal(closeadj, volume):
    result = np.sign(_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6) * ((_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_zsc63_base_v093_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema63_base_v094_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_sqr_base_v095_signal(closeadj, volume):
    result = np.sign(_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6) * ((_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_zsc63_base_v096_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema63_base_v097_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_sqr_base_v098_signal(closeadj, volume):
    result = np.sign(_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6) * ((_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_zsc63_base_v099_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema63_base_v100_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_sqr_base_v101_signal(closeadj, volume):
    result = np.sign(_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6) * ((_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_zsc63_base_v102_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema63_base_v103_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 252) * closeadj / 1e6).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_sqr_base_v104_signal(closeadj, volume):
    result = np.sign(_f043_max_down_vol(closeadj, volume, 252) * closeadj / 1e6) * ((_f043_max_down_vol(closeadj, volume, 252) * closeadj / 1e6) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_zsc63_base_v105_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 252) * closeadj / 1e6, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_ema63_base_v106_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 10)).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_sqr_base_v107_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 10)) * ((_f043_pocket_pivot(closeadj, volume, 10)) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_zsc63_base_v108_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_ema63_base_v109_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21)).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_sqr_base_v110_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 21)) * ((_f043_pocket_pivot(closeadj, volume, 21)) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_zsc63_base_v111_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_ema63_base_v112_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63)).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_sqr_base_v113_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 63)) * ((_f043_pocket_pivot(closeadj, volume, 63)) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_zsc63_base_v114_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_ema63_base_v115_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 126)).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_sqr_base_v116_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 126)) * ((_f043_pocket_pivot(closeadj, volume, 126)) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_zsc63_base_v117_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_ema63_base_v118_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 252)).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_sqr_base_v119_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 252)) * ((_f043_pocket_pivot(closeadj, volume, 252)) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_zsc63_base_v120_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_ema63_base_v121_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_sqr_base_v122_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj) * ((_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_zsc63_base_v123_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_ema63_base_v124_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_sqr_base_v125_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj) * ((_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_zsc63_base_v126_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_ema63_base_v127_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_sqr_base_v128_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj) * ((_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_zsc63_base_v129_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_ema63_base_v130_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_sqr_base_v131_signal(closeadj, volume):
    result = np.sign(_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj) * ((_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_zsc63_base_v132_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_ema63_base_v133_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_sqr_base_v134_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())) * ((_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_zsc63_base_v135_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_ema63_base_v136_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_sqr_base_v137_signal(closeadj, volume):
    result = np.sign(_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())) * ((_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())) ** 2)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_zsc63_base_v138_signal(closeadj, volume):
    result = _z(_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_ema63_base_v139_signal(closeadj, volume):
    result = (np.log1p(_f043_up_day_vol(closeadj, volume, 21)) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_sqr_base_v140_signal(closeadj, volume):
    result = np.tanh(_z(np.log1p(_f043_up_day_vol(closeadj, volume, 21)), 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_zsc63_base_v141_signal(closeadj, volume):
    result = _z(np.log1p(_f043_up_day_vol(closeadj, volume, 21)) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_ema63_base_v142_signal(closeadj, volume):
    result = (np.log1p(_f043_up_day_vol(closeadj, volume, 63)) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_sqr_base_v143_signal(closeadj, volume):
    result = np.tanh(_z(np.log1p(_f043_up_day_vol(closeadj, volume, 63)), 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_zsc63_base_v144_signal(closeadj, volume):
    result = _z(np.log1p(_f043_up_day_vol(closeadj, volume, 63)) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_ema63_base_v145_signal(closeadj, volume):
    result = (np.log1p(_f043_max_down_vol(closeadj, volume, 21)) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_sqr_base_v146_signal(closeadj, volume):
    result = np.tanh(_z(np.log1p(_f043_max_down_vol(closeadj, volume, 21)), 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_zsc63_base_v147_signal(closeadj, volume):
    result = _z(np.log1p(_f043_max_down_vol(closeadj, volume, 21)) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_ema63_base_v148_signal(closeadj, volume):
    result = (np.log1p(_f043_max_down_vol(closeadj, volume, 63)) * closeadj).ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_sqr_base_v149_signal(closeadj, volume):
    result = np.tanh(_z(np.log1p(_f043_max_down_vol(closeadj, volume, 63)), 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_zsc63_base_v150_signal(closeadj, volume):
    result = _z(np.log1p(_f043_max_down_vol(closeadj, volume, 63)) * closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f043ppf_f043_pocket_pivot_flag_upvol10x_ema63_base_v076_signal,
    f043ppf_f043_pocket_pivot_flag_upvol10x_sqr_base_v077_signal,
    f043ppf_f043_pocket_pivot_flag_upvol10x_zsc63_base_v078_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_ema63_base_v079_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_sqr_base_v080_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_zsc63_base_v081_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_ema63_base_v082_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_sqr_base_v083_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_zsc63_base_v084_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_ema63_base_v085_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_sqr_base_v086_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_zsc63_base_v087_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_ema63_base_v088_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_sqr_base_v089_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_zsc63_base_v090_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema63_base_v091_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_sqr_base_v092_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_zsc63_base_v093_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema63_base_v094_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_sqr_base_v095_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_zsc63_base_v096_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema63_base_v097_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_sqr_base_v098_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_zsc63_base_v099_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema63_base_v100_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_sqr_base_v101_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_zsc63_base_v102_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema63_base_v103_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_sqr_base_v104_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_zsc63_base_v105_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_ema63_base_v106_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_sqr_base_v107_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_zsc63_base_v108_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_ema63_base_v109_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_sqr_base_v110_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_zsc63_base_v111_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_ema63_base_v112_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_sqr_base_v113_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_zsc63_base_v114_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_ema63_base_v115_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_sqr_base_v116_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_zsc63_base_v117_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_ema63_base_v118_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_sqr_base_v119_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_zsc63_base_v120_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_ema63_base_v121_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_sqr_base_v122_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_zsc63_base_v123_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_ema63_base_v124_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_sqr_base_v125_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_zsc63_base_v126_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_ema63_base_v127_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_sqr_base_v128_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_zsc63_base_v129_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_ema63_base_v130_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_sqr_base_v131_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_zsc63_base_v132_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_ema63_base_v133_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_sqr_base_v134_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_zsc63_base_v135_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_ema63_base_v136_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_sqr_base_v137_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_zsc63_base_v138_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_ema63_base_v139_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_sqr_base_v140_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_zsc63_base_v141_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_ema63_base_v142_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_sqr_base_v143_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_zsc63_base_v144_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_ema63_base_v145_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_sqr_base_v146_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_zsc63_base_v147_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_ema63_base_v148_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_sqr_base_v149_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_zsc63_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F043_POCKET_PIVOT_FLAG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f043_up_day_vol", "_f043_max_down_vol", "_f043_pocket_pivot")
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
    print(f"OK {__file__}: {n_features} features pass")
