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
def _f48_gp_lift(gp, revenue, w):
    gpr = gp / revenue.replace(0, np.nan)
    return gpr - gpr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f48_pricing_pass_through(grossmargin, cor, revenue, w):
    cost_intensity = cor / revenue.replace(0, np.nan)
    cost_change = cost_intensity.diff(w)
    margin_change = grossmargin.diff(w)
    return margin_change - (-cost_change)


def _f48_packaging_durability(grossmargin, ebitdamargin, w):
    gm_floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    eb_floor = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    gm_mean = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    eb_mean = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (gm_floor / gm_mean.replace(0, np.nan).abs()) + (eb_floor / eb_mean.replace(0, np.nan).abs())



def f48ppp_f48_packaging_pricing_power_gplift_21d_raw_base_v001_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_mean_base_v002_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_std_base_v003_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_21d_z_base_v004_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_raw_base_v005_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_mean_base_v006_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_std_base_v007_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_42d_z_base_v008_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_raw_base_v009_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_mean_base_v010_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_std_base_v011_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_63d_z_base_v012_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_raw_base_v013_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_mean_base_v014_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_std_base_v015_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_126d_z_base_v016_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_raw_base_v017_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_mean_base_v018_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_std_base_v019_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_189d_z_base_v020_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_raw_base_v021_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_mean_base_v022_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_std_base_v023_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_252d_z_base_v024_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_raw_base_v025_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_mean_base_v026_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_std_base_v027_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_378d_z_base_v028_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_raw_base_v029_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_mean_base_v030_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_std_base_v031_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_gplift_504d_z_base_v032_signal(gp, revenue, closeadj):
    base = _f48_gp_lift(gp, revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_raw_base_v033_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_mean_base_v034_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_std_base_v035_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_21d_z_base_v036_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_raw_base_v037_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_mean_base_v038_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_std_base_v039_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_42d_z_base_v040_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_raw_base_v041_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_mean_base_v042_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_std_base_v043_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_63d_z_base_v044_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_raw_base_v045_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_mean_base_v046_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_std_base_v047_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_126d_z_base_v048_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_raw_base_v049_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_mean_base_v050_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_std_base_v051_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_189d_z_base_v052_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_252d_raw_base_v053_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_252d_mean_base_v054_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_252d_std_base_v055_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_252d_z_base_v056_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_378d_raw_base_v057_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_378d_mean_base_v058_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_378d_std_base_v059_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_378d_z_base_v060_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_504d_raw_base_v061_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_504d_mean_base_v062_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_504d_std_base_v063_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_ppt_504d_z_base_v064_signal(grossmargin, cor, revenue, closeadj):
    base = _f48_pricing_pass_through(grossmargin, cor, revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_21d_raw_base_v065_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_21d_mean_base_v066_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_21d_std_base_v067_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_21d_z_base_v068_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_42d_raw_base_v069_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_42d_mean_base_v070_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_42d_std_base_v071_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_42d_z_base_v072_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_63d_raw_base_v073_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_63d_mean_base_v074_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48ppp_f48_packaging_pricing_power_pkgdur_63d_std_base_v075_signal(grossmargin, ebitdamargin, closeadj):
    base = _f48_packaging_durability(grossmargin, ebitdamargin, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ppp_f48_packaging_pricing_power_gplift_21d_raw_base_v001_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_mean_base_v002_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_std_base_v003_signal,
    f48ppp_f48_packaging_pricing_power_gplift_21d_z_base_v004_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_raw_base_v005_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_mean_base_v006_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_std_base_v007_signal,
    f48ppp_f48_packaging_pricing_power_gplift_42d_z_base_v008_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_raw_base_v009_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_mean_base_v010_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_std_base_v011_signal,
    f48ppp_f48_packaging_pricing_power_gplift_63d_z_base_v012_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_raw_base_v013_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_mean_base_v014_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_std_base_v015_signal,
    f48ppp_f48_packaging_pricing_power_gplift_126d_z_base_v016_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_raw_base_v017_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_mean_base_v018_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_std_base_v019_signal,
    f48ppp_f48_packaging_pricing_power_gplift_189d_z_base_v020_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_raw_base_v021_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_mean_base_v022_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_std_base_v023_signal,
    f48ppp_f48_packaging_pricing_power_gplift_252d_z_base_v024_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_raw_base_v025_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_mean_base_v026_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_std_base_v027_signal,
    f48ppp_f48_packaging_pricing_power_gplift_378d_z_base_v028_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_raw_base_v029_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_mean_base_v030_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_std_base_v031_signal,
    f48ppp_f48_packaging_pricing_power_gplift_504d_z_base_v032_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_raw_base_v033_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_mean_base_v034_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_std_base_v035_signal,
    f48ppp_f48_packaging_pricing_power_ppt_21d_z_base_v036_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_raw_base_v037_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_mean_base_v038_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_std_base_v039_signal,
    f48ppp_f48_packaging_pricing_power_ppt_42d_z_base_v040_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_raw_base_v041_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_mean_base_v042_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_std_base_v043_signal,
    f48ppp_f48_packaging_pricing_power_ppt_63d_z_base_v044_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_raw_base_v045_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_mean_base_v046_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_std_base_v047_signal,
    f48ppp_f48_packaging_pricing_power_ppt_126d_z_base_v048_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_raw_base_v049_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_mean_base_v050_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_std_base_v051_signal,
    f48ppp_f48_packaging_pricing_power_ppt_189d_z_base_v052_signal,
    f48ppp_f48_packaging_pricing_power_ppt_252d_raw_base_v053_signal,
    f48ppp_f48_packaging_pricing_power_ppt_252d_mean_base_v054_signal,
    f48ppp_f48_packaging_pricing_power_ppt_252d_std_base_v055_signal,
    f48ppp_f48_packaging_pricing_power_ppt_252d_z_base_v056_signal,
    f48ppp_f48_packaging_pricing_power_ppt_378d_raw_base_v057_signal,
    f48ppp_f48_packaging_pricing_power_ppt_378d_mean_base_v058_signal,
    f48ppp_f48_packaging_pricing_power_ppt_378d_std_base_v059_signal,
    f48ppp_f48_packaging_pricing_power_ppt_378d_z_base_v060_signal,
    f48ppp_f48_packaging_pricing_power_ppt_504d_raw_base_v061_signal,
    f48ppp_f48_packaging_pricing_power_ppt_504d_mean_base_v062_signal,
    f48ppp_f48_packaging_pricing_power_ppt_504d_std_base_v063_signal,
    f48ppp_f48_packaging_pricing_power_ppt_504d_z_base_v064_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_21d_raw_base_v065_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_21d_mean_base_v066_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_21d_std_base_v067_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_21d_z_base_v068_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_42d_raw_base_v069_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_42d_mean_base_v070_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_42d_std_base_v071_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_42d_z_base_v072_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_63d_raw_base_v073_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_63d_mean_base_v074_signal,
    f48ppp_f48_packaging_pricing_power_pkgdur_63d_std_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_PACKAGING_PRICING_POWER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {"closeadj": closeadj, "cor": cor, "ebitdamargin": ebitdamargin, "gp": gp, "grossmargin": grossmargin, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_gp_lift", "_f48_pricing_pass_through", "_f48_packaging_durability")
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
    print(f"OK f48_packaging_pricing_power_base_001_075_claude: {n_features} features pass")
