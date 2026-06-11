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
def _f039_price_progress(close, w):
    return close.pct_change(periods=w)


def _f039_volume_effort(volume, w):
    return volume.rolling(w, min_periods=max(1, w // 2)).sum()


def _f039_effort_result_ratio(close, volume, w):
    progress = close.pct_change(periods=w)
    effort = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return progress / (effort + 1.0).replace(0, np.nan)


# Helper to assemble base templates
_W_LIST = [5, 10, 21, 42, 63, 126, 189, 252, 378, 504]


# 21d price progress × close
def f039evr_f039_effort_vs_result_pprog_21d_base_v001_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d price progress × close
def f039evr_f039_effort_vs_result_pprog_63d_base_v002_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d price progress × close
def f039evr_f039_effort_vs_result_pprog_126d_base_v003_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d price progress × close
def f039evr_f039_effort_vs_result_pprog_252d_base_v004_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d price progress × close
def f039evr_f039_effort_vs_result_pprog_504d_base_v005_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d price progress × close
def f039evr_f039_effort_vs_result_pprog_5d_base_v006_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d price progress × close
def f039evr_f039_effort_vs_result_pprog_10d_base_v007_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d price progress × close
def f039evr_f039_effort_vs_result_pprog_42d_base_v008_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d price progress × close
def f039evr_f039_effort_vs_result_pprog_189d_base_v009_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d price progress × close
def f039evr_f039_effort_vs_result_pprog_378d_base_v010_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume effort × close / 1e6
def f039evr_f039_effort_vs_result_veff_21d_base_v011_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume effort × close
def f039evr_f039_effort_vs_result_veff_63d_base_v012_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume effort × close
def f039evr_f039_effort_vs_result_veff_126d_base_v013_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 126) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume effort × close
def f039evr_f039_effort_vs_result_veff_252d_base_v014_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 504d volume effort × close
def f039evr_f039_effort_vs_result_veff_504d_base_v015_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 504) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 5d volume effort × close
def f039evr_f039_effort_vs_result_veff_5d_base_v016_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 5) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 10d volume effort × close
def f039evr_f039_effort_vs_result_veff_10d_base_v017_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 10) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 42d volume effort × close
def f039evr_f039_effort_vs_result_veff_42d_base_v018_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 42) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 189d volume effort × close
def f039evr_f039_effort_vs_result_veff_189d_base_v019_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 189) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 378d volume effort × close
def f039evr_f039_effort_vs_result_veff_378d_base_v020_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 378) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d effort/result ratio × close
def f039evr_f039_effort_vs_result_evr_21d_base_v021_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d effort/result ratio × close
def f039evr_f039_effort_vs_result_evr_63d_base_v022_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d effort/result ratio × close
def f039evr_f039_effort_vs_result_evr_126d_base_v023_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d effort/result ratio × close
def f039evr_f039_effort_vs_result_evr_252d_base_v024_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d effort/result ratio × close
def f039evr_f039_effort_vs_result_evr_504d_base_v025_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d evr × close
def f039evr_f039_effort_vs_result_evr_5d_base_v026_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d evr × close
def f039evr_f039_effort_vs_result_evr_10d_base_v027_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d evr × close
def f039evr_f039_effort_vs_result_evr_42d_base_v028_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d evr × close
def f039evr_f039_effort_vs_result_evr_189d_base_v029_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d evr × close
def f039evr_f039_effort_vs_result_evr_378d_base_v030_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs price progress × close (effort strength)
def f039evr_f039_effort_vs_result_absprog_21d_base_v031_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs price progress × close
def f039evr_f039_effort_vs_result_absprog_63d_base_v032_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs price progress × close
def f039evr_f039_effort_vs_result_absprog_252d_base_v033_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d price progress / volume effort ratio × close
def f039evr_f039_effort_vs_result_prog_per_eff_21d_base_v034_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 21), _f039_volume_effort(volume, 21) + 1.0)
    result = base * closeadj * 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d price progress / volume effort × close
def f039evr_f039_effort_vs_result_prog_per_eff_63d_base_v035_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 63), _f039_volume_effort(volume, 63) + 1.0)
    result = base * closeadj * 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d price progress / volume effort × close
def f039evr_f039_effort_vs_result_prog_per_eff_252d_base_v036_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 252), _f039_volume_effort(volume, 252) + 1.0)
    result = base * closeadj * 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign price progress × close
def f039evr_f039_effort_vs_result_signprog_21d_base_v037_signal(closeadj, volume):
    result = np.sign(_f039_price_progress(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign price progress × close
def f039evr_f039_effort_vs_result_signprog_63d_base_v038_signal(closeadj, volume):
    result = np.sign(_f039_price_progress(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign price progress × close
def f039evr_f039_effort_vs_result_signprog_252d_base_v039_signal(closeadj, volume):
    result = np.sign(_f039_price_progress(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean price progress × close
def f039evr_f039_effort_vs_result_meanprog_21d_base_v040_signal(closeadj, volume):
    result = _mean(_f039_price_progress(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean price progress × close
def f039evr_f039_effort_vs_result_meanprog_63d_base_v041_signal(closeadj, volume):
    result = _mean(_f039_price_progress(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean price progress × close
def f039evr_f039_effort_vs_result_meanprog_252d_base_v042_signal(closeadj, volume):
    result = _mean(_f039_price_progress(closeadj, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std price progress × close
def f039evr_f039_effort_vs_result_stdprog_21d_base_v043_signal(closeadj, volume):
    result = _std(_f039_price_progress(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std price progress × close
def f039evr_f039_effort_vs_result_stdprog_63d_base_v044_signal(closeadj, volume):
    result = _std(_f039_price_progress(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z price progress × close
def f039evr_f039_effort_vs_result_zprog_21d_base_v045_signal(closeadj, volume):
    result = _z(_f039_price_progress(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z price progress × close
def f039evr_f039_effort_vs_result_zprog_63d_base_v046_signal(closeadj, volume):
    result = _z(_f039_price_progress(closeadj, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume effort × price progress × close (composite force)
def f039evr_f039_effort_vs_result_veffxprog_21d_base_v047_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * _f039_price_progress(closeadj, 21) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume effort × price progress × close
def f039evr_f039_effort_vs_result_veffxprog_63d_base_v048_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * _f039_price_progress(closeadj, 63) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume effort × price progress × close
def f039evr_f039_effort_vs_result_veffxprog_252d_base_v049_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * _f039_price_progress(closeadj, 252) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d efficient effort: progress / sqrt(effort) × close
def f039evr_f039_effort_vs_result_eff_eff_21d_base_v050_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 21), np.sqrt(_f039_volume_effort(volume, 21).abs()) + 1.0)
    result = base * closeadj * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d efficient effort × close
def f039evr_f039_effort_vs_result_eff_eff_63d_base_v051_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 63), np.sqrt(_f039_volume_effort(volume, 63).abs()) + 1.0)
    result = base * closeadj * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d efficient effort × close
def f039evr_f039_effort_vs_result_eff_eff_252d_base_v052_signal(closeadj, volume):
    base = _safe_div(_f039_price_progress(closeadj, 252), np.sqrt(_f039_volume_effort(volume, 252).abs()) + 1.0)
    result = base * closeadj * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume effort × log close
def f039evr_f039_effort_vs_result_veffxlogcl_21d_base_v053_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume effort × log close
def f039evr_f039_effort_vs_result_veffxlogcl_63d_base_v054_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d volume effort × log close
def f039evr_f039_effort_vs_result_veffxlogcl_252d_base_v055_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * np.log(closeadj.replace(0, np.nan).abs()) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d effort × abs progress × close
def f039evr_f039_effort_vs_result_effxabsp_21d_base_v056_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * _f039_price_progress(closeadj, 21).abs() * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d effort × abs progress × close
def f039evr_f039_effort_vs_result_effxabsp_63d_base_v057_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * _f039_price_progress(closeadj, 63).abs() * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evr abs × close
def f039evr_f039_effort_vs_result_absevr_21d_base_v058_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evr abs × close
def f039evr_f039_effort_vs_result_absevr_63d_base_v059_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evr abs × close
def f039evr_f039_effort_vs_result_absevr_252d_base_v060_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean evr × close
def f039evr_f039_effort_vs_result_meanevr_21d_base_v061_signal(closeadj, volume):
    result = _mean(_f039_effort_result_ratio(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean evr × close
def f039evr_f039_effort_vs_result_meanevr_63d_base_v062_signal(closeadj, volume):
    result = _mean(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean evr × close
def f039evr_f039_effort_vs_result_meanevr_252d_base_v063_signal(closeadj, volume):
    result = _mean(_f039_effort_result_ratio(closeadj, volume, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std evr × close
def f039evr_f039_effort_vs_result_stdevr_21d_base_v064_signal(closeadj, volume):
    result = _std(_f039_effort_result_ratio(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std evr × close
def f039evr_f039_effort_vs_result_stdevr_63d_base_v065_signal(closeadj, volume):
    result = _std(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z evr × close
def f039evr_f039_effort_vs_result_zevr_21d_base_v066_signal(closeadj, volume):
    result = _z(_f039_effort_result_ratio(closeadj, volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z evr × close
def f039evr_f039_effort_vs_result_zevr_63d_base_v067_signal(closeadj, volume):
    result = _z(_f039_effort_result_ratio(closeadj, volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA evr × close
def f039evr_f039_effort_vs_result_emaevr_21d_base_v068_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA evr × close
def f039evr_f039_effort_vs_result_emaevr_63d_base_v069_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d progress × close × volume z
def f039evr_f039_effort_vs_result_progxvolz_21d_base_v070_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d progress × close × volume z
def f039evr_f039_effort_vs_result_progxvolz_63d_base_v071_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evr × close × volume z
def f039evr_f039_effort_vs_result_evrxvolz_21d_base_v072_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evr × close × volume z
def f039evr_f039_effort_vs_result_evrxvolz_63d_base_v073_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log effort × close
def f039evr_f039_effort_vs_result_logeff_21d_base_v074_signal(closeadj, volume):
    result = np.log(_f039_volume_effort(volume, 21).abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log effort × close
def f039evr_f039_effort_vs_result_logeff_63d_base_v075_signal(closeadj, volume):
    result = np.log(_f039_volume_effort(volume, 63).abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f039evr_f039_effort_vs_result_pprog_21d_base_v001_signal,
    f039evr_f039_effort_vs_result_pprog_63d_base_v002_signal,
    f039evr_f039_effort_vs_result_pprog_126d_base_v003_signal,
    f039evr_f039_effort_vs_result_pprog_252d_base_v004_signal,
    f039evr_f039_effort_vs_result_pprog_504d_base_v005_signal,
    f039evr_f039_effort_vs_result_pprog_5d_base_v006_signal,
    f039evr_f039_effort_vs_result_pprog_10d_base_v007_signal,
    f039evr_f039_effort_vs_result_pprog_42d_base_v008_signal,
    f039evr_f039_effort_vs_result_pprog_189d_base_v009_signal,
    f039evr_f039_effort_vs_result_pprog_378d_base_v010_signal,
    f039evr_f039_effort_vs_result_veff_21d_base_v011_signal,
    f039evr_f039_effort_vs_result_veff_63d_base_v012_signal,
    f039evr_f039_effort_vs_result_veff_126d_base_v013_signal,
    f039evr_f039_effort_vs_result_veff_252d_base_v014_signal,
    f039evr_f039_effort_vs_result_veff_504d_base_v015_signal,
    f039evr_f039_effort_vs_result_veff_5d_base_v016_signal,
    f039evr_f039_effort_vs_result_veff_10d_base_v017_signal,
    f039evr_f039_effort_vs_result_veff_42d_base_v018_signal,
    f039evr_f039_effort_vs_result_veff_189d_base_v019_signal,
    f039evr_f039_effort_vs_result_veff_378d_base_v020_signal,
    f039evr_f039_effort_vs_result_evr_21d_base_v021_signal,
    f039evr_f039_effort_vs_result_evr_63d_base_v022_signal,
    f039evr_f039_effort_vs_result_evr_126d_base_v023_signal,
    f039evr_f039_effort_vs_result_evr_252d_base_v024_signal,
    f039evr_f039_effort_vs_result_evr_504d_base_v025_signal,
    f039evr_f039_effort_vs_result_evr_5d_base_v026_signal,
    f039evr_f039_effort_vs_result_evr_10d_base_v027_signal,
    f039evr_f039_effort_vs_result_evr_42d_base_v028_signal,
    f039evr_f039_effort_vs_result_evr_189d_base_v029_signal,
    f039evr_f039_effort_vs_result_evr_378d_base_v030_signal,
    f039evr_f039_effort_vs_result_absprog_21d_base_v031_signal,
    f039evr_f039_effort_vs_result_absprog_63d_base_v032_signal,
    f039evr_f039_effort_vs_result_absprog_252d_base_v033_signal,
    f039evr_f039_effort_vs_result_prog_per_eff_21d_base_v034_signal,
    f039evr_f039_effort_vs_result_prog_per_eff_63d_base_v035_signal,
    f039evr_f039_effort_vs_result_prog_per_eff_252d_base_v036_signal,
    f039evr_f039_effort_vs_result_signprog_21d_base_v037_signal,
    f039evr_f039_effort_vs_result_signprog_63d_base_v038_signal,
    f039evr_f039_effort_vs_result_signprog_252d_base_v039_signal,
    f039evr_f039_effort_vs_result_meanprog_21d_base_v040_signal,
    f039evr_f039_effort_vs_result_meanprog_63d_base_v041_signal,
    f039evr_f039_effort_vs_result_meanprog_252d_base_v042_signal,
    f039evr_f039_effort_vs_result_stdprog_21d_base_v043_signal,
    f039evr_f039_effort_vs_result_stdprog_63d_base_v044_signal,
    f039evr_f039_effort_vs_result_zprog_21d_base_v045_signal,
    f039evr_f039_effort_vs_result_zprog_63d_base_v046_signal,
    f039evr_f039_effort_vs_result_veffxprog_21d_base_v047_signal,
    f039evr_f039_effort_vs_result_veffxprog_63d_base_v048_signal,
    f039evr_f039_effort_vs_result_veffxprog_252d_base_v049_signal,
    f039evr_f039_effort_vs_result_eff_eff_21d_base_v050_signal,
    f039evr_f039_effort_vs_result_eff_eff_63d_base_v051_signal,
    f039evr_f039_effort_vs_result_eff_eff_252d_base_v052_signal,
    f039evr_f039_effort_vs_result_veffxlogcl_21d_base_v053_signal,
    f039evr_f039_effort_vs_result_veffxlogcl_63d_base_v054_signal,
    f039evr_f039_effort_vs_result_veffxlogcl_252d_base_v055_signal,
    f039evr_f039_effort_vs_result_effxabsp_21d_base_v056_signal,
    f039evr_f039_effort_vs_result_effxabsp_63d_base_v057_signal,
    f039evr_f039_effort_vs_result_absevr_21d_base_v058_signal,
    f039evr_f039_effort_vs_result_absevr_63d_base_v059_signal,
    f039evr_f039_effort_vs_result_absevr_252d_base_v060_signal,
    f039evr_f039_effort_vs_result_meanevr_21d_base_v061_signal,
    f039evr_f039_effort_vs_result_meanevr_63d_base_v062_signal,
    f039evr_f039_effort_vs_result_meanevr_252d_base_v063_signal,
    f039evr_f039_effort_vs_result_stdevr_21d_base_v064_signal,
    f039evr_f039_effort_vs_result_stdevr_63d_base_v065_signal,
    f039evr_f039_effort_vs_result_zevr_21d_base_v066_signal,
    f039evr_f039_effort_vs_result_zevr_63d_base_v067_signal,
    f039evr_f039_effort_vs_result_emaevr_21d_base_v068_signal,
    f039evr_f039_effort_vs_result_emaevr_63d_base_v069_signal,
    f039evr_f039_effort_vs_result_progxvolz_21d_base_v070_signal,
    f039evr_f039_effort_vs_result_progxvolz_63d_base_v071_signal,
    f039evr_f039_effort_vs_result_evrxvolz_21d_base_v072_signal,
    f039evr_f039_effort_vs_result_evrxvolz_63d_base_v073_signal,
    f039evr_f039_effort_vs_result_logeff_21d_base_v074_signal,
    f039evr_f039_effort_vs_result_logeff_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F039_EFFORT_VS_RESULT_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f039_price_progress", "_f039_volume_effort", "_f039_effort_result_ratio")
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
    print(f"OK f039_effort_vs_result_base_001_075_claude: {n_features} features pass")
