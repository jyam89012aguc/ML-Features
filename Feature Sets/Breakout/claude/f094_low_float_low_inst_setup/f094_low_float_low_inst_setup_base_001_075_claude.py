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
def _f094_small_mc(marketcap, w):
    return 1.0 / (1.0 + _mean(marketcap, w) / 1e9)


def _f094_low_share_growth(sharesbas, w):
    g = sharesbas.pct_change(w)
    return -g.fillna(0)


def _f094_low_float_setup(marketcap, sharesbas, w):
    small = 1.0 / (1.0 + _mean(marketcap, w) / 1e9)
    low_g = -sharesbas.pct_change(w).fillna(0)
    return small + low_g


def f094lfl_f094_low_float_low_inst_setup_smamcraw_5d_base_v001_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_5d_base_v002_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_5d_base_v003_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_10d_base_v004_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_10d_base_v005_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_10d_base_v006_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_21d_base_v007_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_21d_base_v008_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_21d_base_v009_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_42d_base_v010_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_42d_base_v011_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_42d_base_v012_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_63d_base_v013_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_63d_base_v014_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_63d_base_v015_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_126d_base_v016_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_126d_base_v017_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_126d_base_v018_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_189d_base_v019_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_189d_base_v020_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_189d_base_v021_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_252d_base_v022_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_252d_base_v023_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_252d_base_v024_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_378d_base_v025_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_378d_base_v026_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_378d_base_v027_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcraw_504d_base_v028_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrraw_504d_base_v029_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstraw_504d_base_v030_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_5d_base_v031_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_5d_base_v032_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_5d_base_v033_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_10d_base_v034_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_10d_base_v035_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_10d_base_v036_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_21d_base_v037_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_21d_base_v038_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_21d_base_v039_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_42d_base_v040_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_42d_base_v041_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_42d_base_v042_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_63d_base_v043_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_63d_base_v044_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_63d_base_v045_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_126d_base_v046_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_126d_base_v047_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_126d_base_v048_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_189d_base_v049_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_189d_base_v050_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_189d_base_v051_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_252d_base_v052_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_252d_base_v053_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_252d_base_v054_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_378d_base_v055_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_378d_base_v056_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_378d_base_v057_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcabs_504d_base_v058_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrabs_504d_base_v059_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstabs_504d_base_v060_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcsqs_5d_base_v061_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrsqs_5d_base_v062_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstsqs_5d_base_v063_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcsqs_10d_base_v064_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrsqs_10d_base_v065_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstsqs_10d_base_v066_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcsqs_21d_base_v067_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrsqs_21d_base_v068_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstsqs_21d_base_v069_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcsqs_42d_base_v070_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrsqs_42d_base_v071_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstsqs_42d_base_v072_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcsqs_63d_base_v073_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrsqs_63d_base_v074_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstsqs_63d_base_v075_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f094lfl_f094_low_float_low_inst_setup_smamcraw_5d_base_v001_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_5d_base_v002_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_5d_base_v003_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_10d_base_v004_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_10d_base_v005_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_10d_base_v006_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_21d_base_v007_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_21d_base_v008_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_21d_base_v009_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_42d_base_v010_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_42d_base_v011_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_42d_base_v012_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_63d_base_v013_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_63d_base_v014_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_63d_base_v015_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_126d_base_v016_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_126d_base_v017_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_126d_base_v018_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_189d_base_v019_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_189d_base_v020_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_189d_base_v021_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_252d_base_v022_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_252d_base_v023_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_252d_base_v024_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_378d_base_v025_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_378d_base_v026_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_378d_base_v027_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcraw_504d_base_v028_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrraw_504d_base_v029_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstraw_504d_base_v030_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_5d_base_v031_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_5d_base_v032_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_5d_base_v033_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_10d_base_v034_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_10d_base_v035_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_10d_base_v036_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_21d_base_v037_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_21d_base_v038_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_21d_base_v039_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_42d_base_v040_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_42d_base_v041_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_42d_base_v042_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_63d_base_v043_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_63d_base_v044_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_63d_base_v045_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_126d_base_v046_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_126d_base_v047_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_126d_base_v048_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_189d_base_v049_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_189d_base_v050_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_189d_base_v051_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_252d_base_v052_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_252d_base_v053_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_252d_base_v054_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_378d_base_v055_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_378d_base_v056_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_378d_base_v057_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcabs_504d_base_v058_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrabs_504d_base_v059_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstabs_504d_base_v060_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcsqs_5d_base_v061_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrsqs_5d_base_v062_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstsqs_5d_base_v063_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcsqs_10d_base_v064_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrsqs_10d_base_v065_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstsqs_10d_base_v066_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcsqs_21d_base_v067_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrsqs_21d_base_v068_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstsqs_21d_base_v069_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcsqs_42d_base_v070_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrsqs_42d_base_v071_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstsqs_42d_base_v072_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcsqs_63d_base_v073_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrsqs_63d_base_v074_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstsqs_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F094_LOW_FLOAT_LOW_INST_SETUP_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f094_low_float_low_inst_setup_base_001_075_claude: {n_features} features pass")
