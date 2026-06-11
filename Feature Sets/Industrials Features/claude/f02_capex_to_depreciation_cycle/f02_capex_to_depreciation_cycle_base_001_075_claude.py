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
def _f02_capex_dep_ratio(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f02_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f02_net_investment(capex, depamor, closeadj):
    net = (capex - depamor) / depamor.replace(0, np.nan).abs()
    return net * closeadj

def f02cdc_f02_capex_to_depreciation_cycle_ratio_5d_base_v001_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_10d_base_v002_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_21d_base_v003_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_42d_base_v004_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_63d_base_v005_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_126d_base_v006_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_189d_base_v007_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_252d_base_v008_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_5d_base_v009_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_10d_base_v010_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_21d_base_v011_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_42d_base_v012_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_63d_base_v013_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_126d_base_v014_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_189d_base_v015_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_252d_base_v016_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_5d_base_v017_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_10d_base_v018_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_21d_base_v019_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_42d_base_v020_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_63d_base_v021_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_126d_base_v022_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_189d_base_v023_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_252d_base_v024_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _mean(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_5d_base_v025_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_10d_base_v026_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_21d_base_v027_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_42d_base_v028_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_63d_base_v029_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_126d_base_v030_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_189d_base_v031_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_252d_base_v032_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_5d_base_v033_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_10d_base_v034_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_21d_base_v035_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_42d_base_v036_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_63d_base_v037_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_126d_base_v038_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_189d_base_v039_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_252d_base_v040_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_21d_base_v041_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_63d_base_v042_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_126d_base_v043_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_252d_base_v044_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_21d_base_v045_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_63d_base_v046_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_126d_base_v047_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_252d_base_v048_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_21d_base_v049_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _z(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_63d_base_v050_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_126d_base_v051_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_252d_base_v052_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_21d_base_v053_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_63d_base_v054_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_126d_base_v055_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_252d_base_v056_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    result = _std(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_21d_base_v057_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_63d_base_v058_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_126d_base_v059_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_252d_base_v060_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_21d_base_v061_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_63d_base_v062_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_126d_base_v063_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_252d_base_v064_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_21d_base_v065_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_63d_base_v066_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_126d_base_v067_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_252d_base_v068_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_21d_base_v069_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_63d_base_v070_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_126d_base_v071_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_252d_base_v072_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_21d_base_v073_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    result = _mean(a * b, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_63d_base_v074_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    result = _mean(a * b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_126d_base_v075_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    result = _mean(a * b, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cdc_f02_capex_to_depreciation_cycle_ratio_5d_base_v001_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_10d_base_v002_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_21d_base_v003_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_42d_base_v004_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_63d_base_v005_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_126d_base_v006_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_189d_base_v007_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_252d_base_v008_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_5d_base_v009_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_10d_base_v010_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_21d_base_v011_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_42d_base_v012_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_63d_base_v013_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_126d_base_v014_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_189d_base_v015_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_252d_base_v016_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_5d_base_v017_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_10d_base_v018_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_21d_base_v019_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_42d_base_v020_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_63d_base_v021_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_126d_base_v022_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_189d_base_v023_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_252d_base_v024_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_5d_base_v025_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_10d_base_v026_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_21d_base_v027_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_42d_base_v028_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_63d_base_v029_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_126d_base_v030_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_189d_base_v031_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_252d_base_v032_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_5d_base_v033_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_10d_base_v034_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_21d_base_v035_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_42d_base_v036_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_63d_base_v037_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_126d_base_v038_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_189d_base_v039_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_252d_base_v040_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_21d_base_v041_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_63d_base_v042_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_126d_base_v043_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_252d_base_v044_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_21d_base_v045_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_63d_base_v046_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_126d_base_v047_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_252d_base_v048_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_21d_base_v049_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_63d_base_v050_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_126d_base_v051_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_252d_base_v052_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_21d_base_v053_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_63d_base_v054_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_126d_base_v055_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_252d_base_v056_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_21d_base_v057_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_63d_base_v058_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_126d_base_v059_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_252d_base_v060_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_21d_base_v061_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_63d_base_v062_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_126d_base_v063_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_252d_base_v064_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_21d_base_v065_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_63d_base_v066_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_126d_base_v067_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_252d_base_v068_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_21d_base_v069_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_63d_base_v070_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_126d_base_v071_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_252d_base_v072_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_21d_base_v073_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_63d_base_v074_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_CAPEX_TO_DEPRECIATION_CYCLE_REGISTRY_001_075 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f02_capex_dep_ratio', '_f02_capex_intensity', '_f02_net_investment')
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
    print(f"OK f02_capex_to_depreciation_cycle_base_001_075_claude: {n_features} features pass")
