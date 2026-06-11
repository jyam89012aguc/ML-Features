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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f02_capex_dep_ratio(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f02_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f02_net_investment(capex, depamor, closeadj):
    net = (capex - depamor) / depamor.replace(0, np.nan).abs()
    return net * closeadj

def f02cdc_f02_capex_to_depreciation_cycle_ratio_5d_slope_v001_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 5) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_10d_slope_v002_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 10) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_21d_slope_v003_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_42d_slope_v004_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 42) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_63d_slope_v005_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_126d_slope_v006_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_189d_slope_v007_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 189) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratio_252d_slope_v008_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_5d_slope_v009_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 5) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_10d_slope_v010_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 10) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_21d_slope_v011_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_42d_slope_v012_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 42) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_63d_slope_v013_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_126d_slope_v014_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_189d_slope_v015_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 189) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intens_252d_slope_v016_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_5d_slope_v017_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 5)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_10d_slope_v018_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 10)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_21d_slope_v019_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 21)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_42d_slope_v020_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 42)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_63d_slope_v021_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 63)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_126d_slope_v022_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 126)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_189d_slope_v023_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 189)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinv_252d_slope_v024_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(base, 252)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_5d_slope_v025_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 5) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_10d_slope_v026_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 10) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_21d_slope_v027_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 21) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_42d_slope_v028_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 42) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_63d_slope_v029_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_126d_slope_v030_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_189d_slope_v031_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 189) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiostd_252d_slope_v032_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _std(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_5d_slope_v033_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 5) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_10d_slope_v034_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 10) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_21d_slope_v035_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 21) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_42d_slope_v036_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 42) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_63d_slope_v037_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_126d_slope_v038_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_189d_slope_v039_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 189) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensstd_252d_slope_v040_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _std(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_21d_slope_v041_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_63d_slope_v042_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_126d_slope_v043_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioz_252d_slope_v044_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_21d_slope_v045_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_63d_slope_v046_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_126d_slope_v047_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensz_252d_slope_v048_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_21d_slope_v049_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _z(base, 42)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_63d_slope_v050_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _z(base, 126)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_126d_slope_v051_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _z(base, 252)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvz_252d_slope_v052_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _z(base, 504)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_21d_slope_v053_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _std(base, 21)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_63d_slope_v054_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _std(base, 63)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_126d_slope_v055_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _std(base, 126)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvstd_252d_slope_v056_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = _std(base, 252)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_21d_slope_v057_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_63d_slope_v058_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _mean(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_126d_slope_v059_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _mean(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppne_252d_slope_v060_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_21d_slope_v061_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_63d_slope_v062_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _mean(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_126d_slope_v063_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _mean(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassets_252d_slope_v064_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_21d_slope_v065_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_63d_slope_v066_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_126d_slope_v067_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensppnez_252d_slope_v068_signal(capex, ppnenet, closeadj):
    base = _f02_capex_intensity(capex, ppnenet)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_21d_slope_v069_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_63d_slope_v070_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_126d_slope_v071_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_252d_slope_v072_signal(capex, assets, closeadj):
    base = _f02_capex_intensity(capex, assets)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_21d_slope_v073_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    _b = _mean(a * b, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_63d_slope_v074_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    _b = _mean(a * b, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_126d_slope_v075_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    _b = _mean(a * b, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_252d_slope_v076_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    _b = _mean(a * b, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_21d_slope_v077_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 21)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_63d_slope_v078_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 63)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_126d_slope_v079_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 126)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_252d_slope_v080_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 252)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_21d_slope_v081_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 21)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_63d_slope_v082_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 63)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_126d_slope_v083_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 126)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_252d_slope_v084_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    b = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a * b, 252)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_21d_slope_v085_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.pct_change(21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_63d_slope_v086_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.pct_change(63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_126d_slope_v087_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.pct_change(126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_252d_slope_v088_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.pct_change(252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgrow_21d_slope_v089_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.pct_change(21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgrow_63d_slope_v090_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.pct_change(63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgrow_126d_slope_v091_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.pct_change(126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgrow_252d_slope_v092_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.pct_change(252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_21d_slope_v093_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.pct_change(21)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_63d_slope_v094_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.pct_change(63)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_126d_slope_v095_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.pct_change(126)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_252d_slope_v096_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.pct_change(252)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxret_21d_slope_v097_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    ret = closeadj.pct_change(21)
    _b = a * ret * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxret_63d_slope_v098_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    ret = closeadj.pct_change(63)
    _b = a * ret * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxret_126d_slope_v099_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    ret = closeadj.pct_change(126)
    _b = a * ret * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxret_21d_slope_v100_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    ret = closeadj.pct_change(21)
    _b = a * ret * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxret_63d_slope_v101_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    ret = closeadj.pct_change(63)
    _b = a * ret * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxret_126d_slope_v102_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    ret = closeadj.pct_change(126)
    _b = a * ret * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxret_21d_slope_v103_signal(capex, depamor, closeadj):
    a = _f02_net_investment(capex, depamor, closeadj)
    ret = closeadj.pct_change(21)
    _b = a * ret
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxret_63d_slope_v104_signal(capex, depamor, closeadj):
    a = _f02_net_investment(capex, depamor, closeadj)
    ret = closeadj.pct_change(63)
    _b = a * ret
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxret_126d_slope_v105_signal(capex, depamor, closeadj):
    a = _f02_net_investment(capex, depamor, closeadj)
    ret = closeadj.pct_change(126)
    _b = a * ret
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_21d_slope_v106_signal(capex, depamor, closeadj, volume):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 21) * _mean(closeadj * volume, 21)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_63d_slope_v107_signal(capex, depamor, closeadj, volume):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 63) * _mean(closeadj * volume, 63)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_126d_slope_v108_signal(capex, depamor, closeadj, volume):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 126) * _mean(closeadj * volume, 126)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxvol_21d_slope_v109_signal(capex, revenue, closeadj, volume):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 21) * _mean(closeadj * volume, 21)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxvol_63d_slope_v110_signal(capex, revenue, closeadj, volume):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 63) * _mean(closeadj * volume, 63)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxvol_126d_slope_v111_signal(capex, revenue, closeadj, volume):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 126) * _mean(closeadj * volume, 126)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_21d_slope_v112_signal(capex, depamor, closeadj, volume):
    a = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a, 21) * _z(volume, 21)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_63d_slope_v113_signal(capex, depamor, closeadj, volume):
    a = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a, 63) * _z(volume, 63)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_126d_slope_v114_signal(capex, depamor, closeadj, volume):
    a = _f02_net_investment(capex, depamor, closeadj)
    _b = _mean(a, 126) * _z(volume, 126)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_trio_21d_slope_v115_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    c = _f02_net_investment(capex, depamor, closeadj)
    _b = (_mean(a, 21) + _mean(b, 21)) * closeadj + _mean(c, 21) * 0.0001
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_trio_63d_slope_v116_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    c = _f02_net_investment(capex, depamor, closeadj)
    _b = (_mean(a, 63) + _mean(b, 63)) * closeadj + _mean(c, 63) * 0.0001
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_trio_126d_slope_v117_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    c = _f02_net_investment(capex, depamor, closeadj)
    _b = (_mean(a, 126) + _mean(b, 126)) * closeadj + _mean(c, 126) * 0.0001
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_trio_252d_slope_v118_signal(capex, depamor, revenue, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    b = _f02_capex_intensity(capex, revenue)
    c = _f02_net_investment(capex, depamor, closeadj)
    _b = (_mean(a, 252) + _mean(b, 252)) * closeadj + _mean(c, 252) * 0.0001
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioema_21d_slope_v119_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioema_63d_slope_v120_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioema_126d_slope_v121_signal(capex, depamor, closeadj):
    base = _f02_capex_dep_ratio(capex, depamor)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensema_21d_slope_v122_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensema_63d_slope_v123_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensema_126d_slope_v124_signal(capex, revenue, closeadj):
    base = _f02_capex_intensity(capex, revenue)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvema_21d_slope_v125_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvema_63d_slope_v126_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.ewm(span=63, min_periods=31).mean()
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_netinvema_126d_slope_v127_signal(capex, depamor, closeadj):
    base = _f02_net_investment(capex, depamor, closeadj)
    _b = base.ewm(span=126, min_periods=63).mean()
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_21d_slope_v128_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 21) * (depamor / 1e7) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_63d_slope_v129_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 63) * (depamor / 1e7) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_126d_slope_v130_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 126) * (depamor / 1e7) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_252d_slope_v131_signal(capex, depamor, closeadj):
    a = _f02_capex_dep_ratio(capex, depamor)
    _b = _mean(a, 252) * (depamor / 1e7) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxrev_21d_slope_v132_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 21) * (revenue / 1e9) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxrev_63d_slope_v133_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 63) * (revenue / 1e9) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxrev_126d_slope_v134_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 126) * (revenue / 1e9) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensxrev_252d_slope_v135_signal(capex, revenue, closeadj):
    a = _f02_capex_intensity(capex, revenue)
    _b = _mean(a, 252) * (revenue / 1e9) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebit_21d_slope_v136_signal(capex, ebit, closeadj):
    base = _f02_capex_intensity(capex, ebit)
    _b = _mean(base, 21) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebit_63d_slope_v137_signal(capex, ebit, closeadj):
    base = _f02_capex_intensity(capex, ebit)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebit_126d_slope_v138_signal(capex, ebit, closeadj):
    base = _f02_capex_intensity(capex, ebit)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebit_252d_slope_v139_signal(capex, ebit, closeadj):
    base = _f02_capex_intensity(capex, ebit)
    _b = _mean(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebitda_21d_slope_v140_signal(capex, ebitda, closeadj):
    base = _f02_capex_intensity(capex, ebitda)
    _b = _mean(base, 21) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebitda_63d_slope_v141_signal(capex, ebitda, closeadj):
    base = _f02_capex_intensity(capex, ebitda)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebitda_126d_slope_v142_signal(capex, ebitda, closeadj):
    base = _f02_capex_intensity(capex, ebitda)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensebitda_252d_slope_v143_signal(capex, ebitda, closeadj):
    base = _f02_capex_intensity(capex, ebitda)
    _b = _mean(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_21d_slope_v144_signal(capex, netinc, closeadj):
    base = _f02_capex_intensity(capex, netinc)
    _b = _mean(base, 21) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_63d_slope_v145_signal(capex, netinc, closeadj):
    base = _f02_capex_intensity(capex, netinc)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_126d_slope_v146_signal(capex, netinc, closeadj):
    base = _f02_capex_intensity(capex, netinc)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_252d_slope_v147_signal(capex, netinc, closeadj):
    base = _f02_capex_intensity(capex, netinc)
    _b = _mean(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgp_21d_slope_v148_signal(capex, gp, closeadj):
    base = _f02_capex_intensity(capex, gp)
    _b = _mean(base, 21) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgp_63d_slope_v149_signal(capex, gp, closeadj):
    base = _f02_capex_intensity(capex, gp)
    _b = _mean(base, 63) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02cdc_f02_capex_to_depreciation_cycle_intensgp_126d_slope_v150_signal(capex, gp, closeadj):
    base = _f02_capex_intensity(capex, gp)
    _b = _mean(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cdc_f02_capex_to_depreciation_cycle_ratio_5d_slope_v001_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_10d_slope_v002_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_21d_slope_v003_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_42d_slope_v004_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_63d_slope_v005_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_126d_slope_v006_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_189d_slope_v007_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratio_252d_slope_v008_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_5d_slope_v009_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_10d_slope_v010_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_21d_slope_v011_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_42d_slope_v012_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_63d_slope_v013_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_126d_slope_v014_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_189d_slope_v015_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intens_252d_slope_v016_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_5d_slope_v017_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_10d_slope_v018_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_21d_slope_v019_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_42d_slope_v020_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_63d_slope_v021_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_126d_slope_v022_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_189d_slope_v023_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinv_252d_slope_v024_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_5d_slope_v025_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_10d_slope_v026_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_21d_slope_v027_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_42d_slope_v028_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_63d_slope_v029_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_126d_slope_v030_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_189d_slope_v031_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiostd_252d_slope_v032_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_5d_slope_v033_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_10d_slope_v034_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_21d_slope_v035_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_42d_slope_v036_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_63d_slope_v037_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_126d_slope_v038_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_189d_slope_v039_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensstd_252d_slope_v040_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_21d_slope_v041_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_63d_slope_v042_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_126d_slope_v043_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioz_252d_slope_v044_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_21d_slope_v045_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_63d_slope_v046_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_126d_slope_v047_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensz_252d_slope_v048_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_21d_slope_v049_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_63d_slope_v050_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_126d_slope_v051_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvz_252d_slope_v052_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_21d_slope_v053_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_63d_slope_v054_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_126d_slope_v055_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvstd_252d_slope_v056_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_21d_slope_v057_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_63d_slope_v058_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_126d_slope_v059_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppne_252d_slope_v060_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_21d_slope_v061_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_63d_slope_v062_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_126d_slope_v063_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassets_252d_slope_v064_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_21d_slope_v065_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_63d_slope_v066_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_126d_slope_v067_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensppnez_252d_slope_v068_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_21d_slope_v069_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_63d_slope_v070_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_126d_slope_v071_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensassetsz_252d_slope_v072_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_21d_slope_v073_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_63d_slope_v074_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_126d_slope_v075_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxintens_252d_slope_v076_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_21d_slope_v077_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_63d_slope_v078_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_126d_slope_v079_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxnetinv_252d_slope_v080_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_21d_slope_v081_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_63d_slope_v082_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_126d_slope_v083_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxnetinv_252d_slope_v084_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_21d_slope_v085_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_63d_slope_v086_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_126d_slope_v087_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratiogrow_252d_slope_v088_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgrow_21d_slope_v089_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgrow_63d_slope_v090_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgrow_126d_slope_v091_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgrow_252d_slope_v092_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_21d_slope_v093_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_63d_slope_v094_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_126d_slope_v095_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvgrow_252d_slope_v096_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxret_21d_slope_v097_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxret_63d_slope_v098_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxret_126d_slope_v099_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxret_21d_slope_v100_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxret_63d_slope_v101_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxret_126d_slope_v102_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxret_21d_slope_v103_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxret_63d_slope_v104_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxret_126d_slope_v105_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_21d_slope_v106_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_63d_slope_v107_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxvol_126d_slope_v108_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxvol_21d_slope_v109_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxvol_63d_slope_v110_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxvol_126d_slope_v111_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_21d_slope_v112_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_63d_slope_v113_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvxvol_126d_slope_v114_signal,
    f02cdc_f02_capex_to_depreciation_cycle_trio_21d_slope_v115_signal,
    f02cdc_f02_capex_to_depreciation_cycle_trio_63d_slope_v116_signal,
    f02cdc_f02_capex_to_depreciation_cycle_trio_126d_slope_v117_signal,
    f02cdc_f02_capex_to_depreciation_cycle_trio_252d_slope_v118_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioema_21d_slope_v119_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioema_63d_slope_v120_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioema_126d_slope_v121_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensema_21d_slope_v122_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensema_63d_slope_v123_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensema_126d_slope_v124_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvema_21d_slope_v125_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvema_63d_slope_v126_signal,
    f02cdc_f02_capex_to_depreciation_cycle_netinvema_126d_slope_v127_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_21d_slope_v128_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_63d_slope_v129_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_126d_slope_v130_signal,
    f02cdc_f02_capex_to_depreciation_cycle_ratioxdep_252d_slope_v131_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxrev_21d_slope_v132_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxrev_63d_slope_v133_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxrev_126d_slope_v134_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensxrev_252d_slope_v135_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebit_21d_slope_v136_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebit_63d_slope_v137_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebit_126d_slope_v138_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebit_252d_slope_v139_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebitda_21d_slope_v140_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebitda_63d_slope_v141_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebitda_126d_slope_v142_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensebitda_252d_slope_v143_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_21d_slope_v144_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_63d_slope_v145_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_126d_slope_v146_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensnetinc_252d_slope_v147_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgp_21d_slope_v148_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgp_63d_slope_v149_signal,
    f02cdc_f02_capex_to_depreciation_cycle_intensgp_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_CAPEX_TO_DEPRECIATION_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f02_capex_to_depreciation_cycle_2nd_derivatives_001_150_claude: {n_features} features pass")
