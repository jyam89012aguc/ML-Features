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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f094_small_mc(marketcap, w):
    return 1.0 / (1.0 + _mean(marketcap, w) / 1e9)


def _f094_low_share_growth(sharesbas, w):
    g = sharesbas.pct_change(w)
    return -g.fillna(0)


def _f094_low_float_setup(marketcap, sharesbas, w):
    small = 1.0 / (1.0 + _mean(marketcap, w) / 1e9)
    low_g = -sharesbas.pct_change(w).fillna(0)
    return small + low_g


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose_m1_jerk_v001_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_base_m2_jerk_v002_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose21_m5_jerk_v003_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose63_m10_jerk_v004_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose126_m100_jerk_v005_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose_m1_jerk_v006_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_base_m2_jerk_v007_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose21_m5_jerk_v008_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose63_m10_jerk_v009_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose126_m100_jerk_v010_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose_m1_jerk_v011_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_base_m2_jerk_v012_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose21_m5_jerk_v013_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose63_m10_jerk_v014_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose126_m100_jerk_v015_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose_m1_jerk_v016_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_base_m2_jerk_v017_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose21_m5_jerk_v018_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose63_m10_jerk_v019_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose126_m100_jerk_v020_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose_m1_jerk_v021_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_base_m2_jerk_v022_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose21_m5_jerk_v023_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose63_m10_jerk_v024_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose126_m100_jerk_v025_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose_m1_jerk_v026_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 126)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_base_m2_jerk_v027_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 126)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose21_m5_jerk_v028_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose63_m10_jerk_v029_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose126_m100_jerk_v030_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose_m1_jerk_v031_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 189)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_base_m2_jerk_v032_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 189)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose21_m5_jerk_v033_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose63_m10_jerk_v034_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose126_m100_jerk_v035_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose_m1_jerk_v036_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 252)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_base_m2_jerk_v037_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 252)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose21_m5_jerk_v038_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose63_m10_jerk_v039_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose126_m100_jerk_v040_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose_m1_jerk_v041_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_base_m2_jerk_v042_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose21_m5_jerk_v043_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose63_m10_jerk_v044_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose126_m100_jerk_v045_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose_m1_jerk_v046_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_base_m2_jerk_v047_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose21_m5_jerk_v048_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose63_m10_jerk_v049_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose126_m100_jerk_v050_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose_m1_jerk_v051_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_base_m2_jerk_v052_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose21_m5_jerk_v053_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose63_m10_jerk_v054_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose126_m100_jerk_v055_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose_m1_jerk_v056_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_base_m2_jerk_v057_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose21_m5_jerk_v058_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose63_m10_jerk_v059_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose126_m100_jerk_v060_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose_m1_jerk_v061_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_base_m2_jerk_v062_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose21_m5_jerk_v063_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose63_m10_jerk_v064_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose126_m100_jerk_v065_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose_m1_jerk_v066_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_base_m2_jerk_v067_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose21_m5_jerk_v068_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose63_m10_jerk_v069_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose126_m100_jerk_v070_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose_m1_jerk_v071_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_base_m2_jerk_v072_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose21_m5_jerk_v073_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose63_m10_jerk_v074_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose126_m100_jerk_v075_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose_m1_jerk_v076_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_base_m2_jerk_v077_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose21_m5_jerk_v078_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose63_m10_jerk_v079_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose126_m100_jerk_v080_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose_m1_jerk_v081_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_base_m2_jerk_v082_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose21_m5_jerk_v083_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose63_m10_jerk_v084_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose126_m100_jerk_v085_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose_m1_jerk_v086_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_base_m2_jerk_v087_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose21_m5_jerk_v088_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose63_m10_jerk_v089_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose126_m100_jerk_v090_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose_m1_jerk_v091_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_base_m2_jerk_v092_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose21_m5_jerk_v093_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose63_m10_jerk_v094_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose126_m100_jerk_v095_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose_m1_jerk_v096_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_base_m2_jerk_v097_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose21_m5_jerk_v098_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose63_m10_jerk_v099_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose126_m100_jerk_v100_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose_m1_jerk_v101_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_base_m2_jerk_v102_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose21_m5_jerk_v103_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose63_m10_jerk_v104_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose126_m100_jerk_v105_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose_m1_jerk_v106_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_base_m2_jerk_v107_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose21_m5_jerk_v108_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose63_m10_jerk_v109_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose126_m100_jerk_v110_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose_m1_jerk_v111_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_base_m2_jerk_v112_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose21_m5_jerk_v113_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose63_m10_jerk_v114_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose126_m100_jerk_v115_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose_m1_jerk_v116_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_base_m2_jerk_v117_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose21_m5_jerk_v118_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose63_m10_jerk_v119_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose126_m100_jerk_v120_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose_m1_jerk_v121_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_base_m2_jerk_v122_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose21_m5_jerk_v123_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose63_m10_jerk_v124_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose126_m100_jerk_v125_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose_m1_jerk_v126_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_base_m2_jerk_v127_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose21_m5_jerk_v128_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose63_m10_jerk_v129_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose126_m100_jerk_v130_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 126)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose_m1_jerk_v131_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_base_m2_jerk_v132_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose21_m5_jerk_v133_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose63_m10_jerk_v134_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose126_m100_jerk_v135_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 189)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose_m1_jerk_v136_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_base_m2_jerk_v137_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose21_m5_jerk_v138_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose63_m10_jerk_v139_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose126_m100_jerk_v140_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    deriv = _jerk(base, 252)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose_m1_jerk_v141_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_base_m2_jerk_v142_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose21_m5_jerk_v143_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose63_m10_jerk_v144_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose126_m100_jerk_v145_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose_m1_jerk_v146_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_base_m2_jerk_v147_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose21_m5_jerk_v148_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose63_m10_jerk_v149_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose126_m100_jerk_v150_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    deriv = _jerk(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose_m1_jerk_v001_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_base_m2_jerk_v002_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose21_m5_jerk_v003_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose63_m10_jerk_v004_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_5d_xclose126_m100_jerk_v005_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose_m1_jerk_v006_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_base_m2_jerk_v007_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose21_m5_jerk_v008_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose63_m10_jerk_v009_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_10d_xclose126_m100_jerk_v010_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose_m1_jerk_v011_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_base_m2_jerk_v012_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose21_m5_jerk_v013_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose63_m10_jerk_v014_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_21d_xclose126_m100_jerk_v015_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose_m1_jerk_v016_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_base_m2_jerk_v017_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose21_m5_jerk_v018_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose63_m10_jerk_v019_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_42d_xclose126_m100_jerk_v020_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose_m1_jerk_v021_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_base_m2_jerk_v022_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose21_m5_jerk_v023_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose63_m10_jerk_v024_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_63d_xclose126_m100_jerk_v025_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose_m1_jerk_v026_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_base_m2_jerk_v027_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose21_m5_jerk_v028_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose63_m10_jerk_v029_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_126d_xclose126_m100_jerk_v030_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose_m1_jerk_v031_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_base_m2_jerk_v032_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose21_m5_jerk_v033_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose63_m10_jerk_v034_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_189d_xclose126_m100_jerk_v035_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose_m1_jerk_v036_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_base_m2_jerk_v037_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose21_m5_jerk_v038_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose63_m10_jerk_v039_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_5d_jerk_252d_xclose126_m100_jerk_v040_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose_m1_jerk_v041_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_base_m2_jerk_v042_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose21_m5_jerk_v043_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose63_m10_jerk_v044_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_5d_xclose126_m100_jerk_v045_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose_m1_jerk_v046_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_base_m2_jerk_v047_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose21_m5_jerk_v048_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose63_m10_jerk_v049_signal,
    f094lfl_f094_low_float_low_inst_setup_smallmc_21d_jerk_10d_xclose126_m100_jerk_v050_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose_m1_jerk_v051_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_base_m2_jerk_v052_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose21_m5_jerk_v053_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose63_m10_jerk_v054_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_5d_xclose126_m100_jerk_v055_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose_m1_jerk_v056_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_base_m2_jerk_v057_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose21_m5_jerk_v058_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose63_m10_jerk_v059_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_10d_xclose126_m100_jerk_v060_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose_m1_jerk_v061_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_base_m2_jerk_v062_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose21_m5_jerk_v063_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose63_m10_jerk_v064_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_21d_xclose126_m100_jerk_v065_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose_m1_jerk_v066_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_base_m2_jerk_v067_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose21_m5_jerk_v068_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose63_m10_jerk_v069_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_42d_xclose126_m100_jerk_v070_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose_m1_jerk_v071_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_base_m2_jerk_v072_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose21_m5_jerk_v073_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose63_m10_jerk_v074_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_63d_xclose126_m100_jerk_v075_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose_m1_jerk_v076_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_base_m2_jerk_v077_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose21_m5_jerk_v078_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose63_m10_jerk_v079_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_126d_xclose126_m100_jerk_v080_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose_m1_jerk_v081_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_base_m2_jerk_v082_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose21_m5_jerk_v083_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose63_m10_jerk_v084_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_189d_xclose126_m100_jerk_v085_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose_m1_jerk_v086_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_base_m2_jerk_v087_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose21_m5_jerk_v088_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose63_m10_jerk_v089_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_5d_jerk_252d_xclose126_m100_jerk_v090_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose_m1_jerk_v091_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_base_m2_jerk_v092_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose21_m5_jerk_v093_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose63_m10_jerk_v094_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_5d_xclose126_m100_jerk_v095_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose_m1_jerk_v096_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_base_m2_jerk_v097_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose21_m5_jerk_v098_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose63_m10_jerk_v099_signal,
    f094lfl_f094_low_float_low_inst_setup_lowsharegrowth_21d_jerk_10d_xclose126_m100_jerk_v100_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose_m1_jerk_v101_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_base_m2_jerk_v102_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose21_m5_jerk_v103_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose63_m10_jerk_v104_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_5d_xclose126_m100_jerk_v105_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose_m1_jerk_v106_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_base_m2_jerk_v107_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose21_m5_jerk_v108_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose63_m10_jerk_v109_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_10d_xclose126_m100_jerk_v110_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose_m1_jerk_v111_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_base_m2_jerk_v112_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose21_m5_jerk_v113_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose63_m10_jerk_v114_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_21d_xclose126_m100_jerk_v115_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose_m1_jerk_v116_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_base_m2_jerk_v117_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose21_m5_jerk_v118_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose63_m10_jerk_v119_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_42d_xclose126_m100_jerk_v120_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose_m1_jerk_v121_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_base_m2_jerk_v122_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose21_m5_jerk_v123_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose63_m10_jerk_v124_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_63d_xclose126_m100_jerk_v125_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose_m1_jerk_v126_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_base_m2_jerk_v127_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose21_m5_jerk_v128_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose63_m10_jerk_v129_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_126d_xclose126_m100_jerk_v130_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose_m1_jerk_v131_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_base_m2_jerk_v132_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose21_m5_jerk_v133_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose63_m10_jerk_v134_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_189d_xclose126_m100_jerk_v135_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose_m1_jerk_v136_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_base_m2_jerk_v137_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose21_m5_jerk_v138_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose63_m10_jerk_v139_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_5d_jerk_252d_xclose126_m100_jerk_v140_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose_m1_jerk_v141_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_base_m2_jerk_v142_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose21_m5_jerk_v143_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose63_m10_jerk_v144_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_5d_xclose126_m100_jerk_v145_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose_m1_jerk_v146_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_base_m2_jerk_v147_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose21_m5_jerk_v148_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose63_m10_jerk_v149_signal,
    f094lfl_f094_low_float_low_inst_setup_lowfloatsetup_21d_jerk_10d_xclose126_m100_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F094_LOW_FLOAT_LOW_INST_SETUP_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f094_small_mc", "_f094_low_share_growth", "_f094_low_float_setup")
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f094_low_float_low_inst_setup_3rd_derivatives_001_150_claude: {n_features} features pass")
