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
def _f28_service_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f28_margin_stability(ebitdamargin, w):
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (sd.replace(0, np.nan) + 1e-6)


def _f28_durability_score(ebitdamargin, grossmargin, w):
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (em * gm) / (sd.replace(0, np.nan) + 1e-6)


# 5d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_5d_base_v001_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_10d_base_v002_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_21d_base_v003_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_42d_base_v004_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_63d_base_v005_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_126d_base_v006_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 126)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_189d_base_v007_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 189)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_252d_base_v008_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_378d_base_v009_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 378)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d service margin floor x close
def f28cms_f28_cro_margin_stability_smfloor_504d_base_v010_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 504)
    result = f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_5d_base_v011_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 5)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_10d_base_v012_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 10)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_21d_base_v013_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_42d_base_v014_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 42)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_63d_base_v015_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_126d_base_v016_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 126)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_189d_base_v017_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 189)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_252d_base_v018_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_378d_base_v019_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 378)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d margin stability x close
def f28cms_f28_cro_margin_stability_mstab_504d_base_v020_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 504)
    result = ms * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d durability score x close
def f28cms_f28_cro_margin_stability_durscore_5d_base_v021_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 5)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d durability score x close
def f28cms_f28_cro_margin_stability_durscore_10d_base_v022_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 10)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d durability score x close
def f28cms_f28_cro_margin_stability_durscore_21d_base_v023_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d durability score x close
def f28cms_f28_cro_margin_stability_durscore_42d_base_v024_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d durability score x close
def f28cms_f28_cro_margin_stability_durscore_63d_base_v025_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d durability score x close
def f28cms_f28_cro_margin_stability_durscore_126d_base_v026_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d durability score x close
def f28cms_f28_cro_margin_stability_durscore_189d_base_v027_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 189)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d durability score x close
def f28cms_f28_cro_margin_stability_durscore_252d_base_v028_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d durability score x close
def f28cms_f28_cro_margin_stability_durscore_378d_base_v029_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 378)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d durability score x close
def f28cms_f28_cro_margin_stability_durscore_504d_base_v030_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    result = ds * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_5d_base_v031_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    result = _z(f, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_10d_base_v032_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    result = _z(f, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_21d_base_v033_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    result = _z(f, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_42d_base_v034_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    result = _z(f, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_63d_base_v035_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    result = _z(f, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_126d_base_v036_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 126)
    result = _z(f, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_189d_base_v037_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 189)
    result = _z(f, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_252d_base_v038_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    result = _z(f, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_378d_base_v039_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 378)
    result = _z(f, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d service margin floor zscore x close
def f28cms_f28_cro_margin_stability_smfloorz_504d_base_v040_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 504)
    result = _z(f, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_5d_base_v041_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 5)
    result = _z(ms, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_10d_base_v042_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 10)
    result = _z(ms, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_21d_base_v043_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    result = _z(ms, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_42d_base_v044_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 42)
    result = _z(ms, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_63d_base_v045_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    result = _z(ms, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_126d_base_v046_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 126)
    result = _z(ms, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_189d_base_v047_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 189)
    result = _z(ms, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_252d_base_v048_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    result = _z(ms, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_378d_base_v049_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 378)
    result = _z(ms, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d margin stability zscore x close
def f28cms_f28_cro_margin_stability_mstabz_504d_base_v050_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 504)
    result = _z(ms, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_5d_base_v051_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 5)
    result = ds.rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_10d_base_v052_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 10)
    result = ds.rolling(10, min_periods=max(1, 10 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_21d_base_v053_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    result = ds.rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_42d_base_v054_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    result = ds.rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_63d_base_v055_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    result = ds.rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_126d_base_v056_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    result = ds.rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_189d_base_v057_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 189)
    result = ds.rolling(189, min_periods=max(1, 189 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_252d_base_v058_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    result = ds.rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_378d_base_v059_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 378)
    result = ds.rolling(378, min_periods=max(1, 378 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d durability score mean x close
def f28cms_f28_cro_margin_stability_durscorem_504d_base_v060_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    result = ds.rolling(504, min_periods=max(1, 504 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d service margin floor x revenue mean
def f28cms_f28_cro_margin_stability_smfloorxrev_5d_base_v061_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = f * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d service margin floor x revenue mean
def f28cms_f28_cro_margin_stability_smfloorxrev_10d_base_v062_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = f * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d service margin floor x revenue mean
def f28cms_f28_cro_margin_stability_smfloorxrev_21d_base_v063_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = f * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d service margin floor x revenue mean
def f28cms_f28_cro_margin_stability_smfloorxrev_42d_base_v064_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = f * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d service margin floor x revenue mean
def f28cms_f28_cro_margin_stability_smfloorxrev_63d_base_v065_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = f * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d margin stab x revenue mean
def f28cms_f28_cro_margin_stability_mstabxrev_5d_base_v066_signal(ebitdamargin, revenue):
    ms = _f28_margin_stability(ebitdamargin, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = ms * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d margin stab x revenue mean
def f28cms_f28_cro_margin_stability_mstabxrev_10d_base_v067_signal(ebitdamargin, revenue):
    ms = _f28_margin_stability(ebitdamargin, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = ms * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d margin stab x revenue mean
def f28cms_f28_cro_margin_stability_mstabxrev_21d_base_v068_signal(ebitdamargin, revenue):
    ms = _f28_margin_stability(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = ms * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d margin stab x revenue mean
def f28cms_f28_cro_margin_stability_mstabxrev_42d_base_v069_signal(ebitdamargin, revenue):
    ms = _f28_margin_stability(ebitdamargin, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = ms * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d margin stab x revenue mean
def f28cms_f28_cro_margin_stability_mstabxrev_63d_base_v070_signal(ebitdamargin, revenue):
    ms = _f28_margin_stability(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = ms * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d durability score x revenue mean
def f28cms_f28_cro_margin_stability_durscorexrev_5d_base_v071_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = ds * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d durability score x revenue mean
def f28cms_f28_cro_margin_stability_durscorexrev_10d_base_v072_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = ds * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d durability score x revenue mean
def f28cms_f28_cro_margin_stability_durscorexrev_21d_base_v073_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = ds * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d durability score x revenue mean
def f28cms_f28_cro_margin_stability_durscorexrev_42d_base_v074_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = ds * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d durability score x revenue mean
def f28cms_f28_cro_margin_stability_durscorexrev_63d_base_v075_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = ds * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28cms_f28_cro_margin_stability_smfloor_5d_base_v001_signal,
    f28cms_f28_cro_margin_stability_smfloor_10d_base_v002_signal,
    f28cms_f28_cro_margin_stability_smfloor_21d_base_v003_signal,
    f28cms_f28_cro_margin_stability_smfloor_42d_base_v004_signal,
    f28cms_f28_cro_margin_stability_smfloor_63d_base_v005_signal,
    f28cms_f28_cro_margin_stability_smfloor_126d_base_v006_signal,
    f28cms_f28_cro_margin_stability_smfloor_189d_base_v007_signal,
    f28cms_f28_cro_margin_stability_smfloor_252d_base_v008_signal,
    f28cms_f28_cro_margin_stability_smfloor_378d_base_v009_signal,
    f28cms_f28_cro_margin_stability_smfloor_504d_base_v010_signal,
    f28cms_f28_cro_margin_stability_mstab_5d_base_v011_signal,
    f28cms_f28_cro_margin_stability_mstab_10d_base_v012_signal,
    f28cms_f28_cro_margin_stability_mstab_21d_base_v013_signal,
    f28cms_f28_cro_margin_stability_mstab_42d_base_v014_signal,
    f28cms_f28_cro_margin_stability_mstab_63d_base_v015_signal,
    f28cms_f28_cro_margin_stability_mstab_126d_base_v016_signal,
    f28cms_f28_cro_margin_stability_mstab_189d_base_v017_signal,
    f28cms_f28_cro_margin_stability_mstab_252d_base_v018_signal,
    f28cms_f28_cro_margin_stability_mstab_378d_base_v019_signal,
    f28cms_f28_cro_margin_stability_mstab_504d_base_v020_signal,
    f28cms_f28_cro_margin_stability_durscore_5d_base_v021_signal,
    f28cms_f28_cro_margin_stability_durscore_10d_base_v022_signal,
    f28cms_f28_cro_margin_stability_durscore_21d_base_v023_signal,
    f28cms_f28_cro_margin_stability_durscore_42d_base_v024_signal,
    f28cms_f28_cro_margin_stability_durscore_63d_base_v025_signal,
    f28cms_f28_cro_margin_stability_durscore_126d_base_v026_signal,
    f28cms_f28_cro_margin_stability_durscore_189d_base_v027_signal,
    f28cms_f28_cro_margin_stability_durscore_252d_base_v028_signal,
    f28cms_f28_cro_margin_stability_durscore_378d_base_v029_signal,
    f28cms_f28_cro_margin_stability_durscore_504d_base_v030_signal,
    f28cms_f28_cro_margin_stability_smfloorz_5d_base_v031_signal,
    f28cms_f28_cro_margin_stability_smfloorz_10d_base_v032_signal,
    f28cms_f28_cro_margin_stability_smfloorz_21d_base_v033_signal,
    f28cms_f28_cro_margin_stability_smfloorz_42d_base_v034_signal,
    f28cms_f28_cro_margin_stability_smfloorz_63d_base_v035_signal,
    f28cms_f28_cro_margin_stability_smfloorz_126d_base_v036_signal,
    f28cms_f28_cro_margin_stability_smfloorz_189d_base_v037_signal,
    f28cms_f28_cro_margin_stability_smfloorz_252d_base_v038_signal,
    f28cms_f28_cro_margin_stability_smfloorz_378d_base_v039_signal,
    f28cms_f28_cro_margin_stability_smfloorz_504d_base_v040_signal,
    f28cms_f28_cro_margin_stability_mstabz_5d_base_v041_signal,
    f28cms_f28_cro_margin_stability_mstabz_10d_base_v042_signal,
    f28cms_f28_cro_margin_stability_mstabz_21d_base_v043_signal,
    f28cms_f28_cro_margin_stability_mstabz_42d_base_v044_signal,
    f28cms_f28_cro_margin_stability_mstabz_63d_base_v045_signal,
    f28cms_f28_cro_margin_stability_mstabz_126d_base_v046_signal,
    f28cms_f28_cro_margin_stability_mstabz_189d_base_v047_signal,
    f28cms_f28_cro_margin_stability_mstabz_252d_base_v048_signal,
    f28cms_f28_cro_margin_stability_mstabz_378d_base_v049_signal,
    f28cms_f28_cro_margin_stability_mstabz_504d_base_v050_signal,
    f28cms_f28_cro_margin_stability_durscorem_5d_base_v051_signal,
    f28cms_f28_cro_margin_stability_durscorem_10d_base_v052_signal,
    f28cms_f28_cro_margin_stability_durscorem_21d_base_v053_signal,
    f28cms_f28_cro_margin_stability_durscorem_42d_base_v054_signal,
    f28cms_f28_cro_margin_stability_durscorem_63d_base_v055_signal,
    f28cms_f28_cro_margin_stability_durscorem_126d_base_v056_signal,
    f28cms_f28_cro_margin_stability_durscorem_189d_base_v057_signal,
    f28cms_f28_cro_margin_stability_durscorem_252d_base_v058_signal,
    f28cms_f28_cro_margin_stability_durscorem_378d_base_v059_signal,
    f28cms_f28_cro_margin_stability_durscorem_504d_base_v060_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_5d_base_v061_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_10d_base_v062_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_21d_base_v063_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_42d_base_v064_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_63d_base_v065_signal,
    f28cms_f28_cro_margin_stability_mstabxrev_5d_base_v066_signal,
    f28cms_f28_cro_margin_stability_mstabxrev_10d_base_v067_signal,
    f28cms_f28_cro_margin_stability_mstabxrev_21d_base_v068_signal,
    f28cms_f28_cro_margin_stability_mstabxrev_42d_base_v069_signal,
    f28cms_f28_cro_margin_stability_mstabxrev_63d_base_v070_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_5d_base_v071_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_10d_base_v072_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_21d_base_v073_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_42d_base_v074_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CRO_MARGIN_STABILITY_REGISTRY_001_075 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_service_margin_floor", "_f28_margin_stability", "_f28_durability_score",)
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
    print(f"OK f28_cro_margin_stability_base_001_075_claude: {n_features} features pass")
