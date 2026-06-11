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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f01_gp_per_unit(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f01_margin_uplift(grossmargin, w):
    base = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return grossmargin - base


def _f01_pricing_strength(grossmargin, cor, w):
    gm_z = (grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()) / grossmargin.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    cor_g = cor.pct_change(w)
    return gm_z - cor_g
def f01bep_f01_brand_equity_pricing_gppu_mean_5d_base_v001_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_10d_base_v002_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_21d_base_v003_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_42d_base_v004_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_63d_base_v005_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_126d_base_v006_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_189d_base_v007_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_252d_base_v008_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_378d_base_v009_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_mean_504d_base_v010_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_std_21d_base_v011_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_std_63d_base_v012_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_std_252d_base_v013_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_z_21d_base_v014_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_gppu_z_63d_base_v015_signal(gp, revenue, closeadj):
    base = _f01_gp_per_unit(gp, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_5d_base_v016_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_10d_base_v017_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_21d_base_v018_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_42d_base_v019_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_63d_base_v020_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_126d_base_v021_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_189d_base_v022_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_252d_base_v023_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_378d_base_v024_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 378)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_mean_504d_base_v025_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_std_10d_base_v026_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_std_21d_base_v027_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_std_63d_base_v028_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_std_126d_base_v029_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_std_252d_base_v030_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_z_21d_base_v031_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_z_63d_base_v032_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_z_126d_base_v033_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_z_252d_base_v034_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_ema_21d_base_v035_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_ema_63d_base_v036_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_ema_126d_base_v037_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_ema_252d_base_v038_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_21d_base_v039_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 21).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_63d_base_v040_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_126d_base_v041_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 126).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_252d_base_v042_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 252).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_378d_base_v043_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 378).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_504d_base_v044_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 504).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_mu_abs_5d_base_v045_signal(grossmargin, closeadj):
    base = _f01_margin_uplift(grossmargin, 5).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_5d_base_v046_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_10d_base_v047_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_21d_base_v048_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_42d_base_v049_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_63d_base_v050_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_126d_base_v051_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_189d_base_v052_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_252d_base_v053_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_378d_base_v054_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_raw_504d_base_v055_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_mean_21d_base_v056_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_mean_63d_base_v057_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_mean_126d_base_v058_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_mean_252d_base_v059_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_mean_378d_base_v060_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_std_21d_base_v061_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_std_63d_base_v062_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_std_126d_base_v063_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_std_252d_base_v064_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_std_378d_base_v065_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_z_21d_base_v066_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_z_63d_base_v067_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_z_126d_base_v068_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_z_252d_base_v069_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_ema_21d_base_v070_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_ema_63d_base_v071_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_ema_126d_base_v072_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_ema_252d_base_v073_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_absmean_21d_base_v074_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 21).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
def f01bep_f01_brand_equity_pricing_ps_absmean_63d_base_v075_signal(grossmargin, cor, closeadj):
    base = _f01_pricing_strength(grossmargin, cor, 63).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f01bep_f01_brand_equity_pricing_gppu_mean_5d_base_v001_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_10d_base_v002_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_21d_base_v003_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_42d_base_v004_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_63d_base_v005_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_126d_base_v006_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_189d_base_v007_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_252d_base_v008_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_378d_base_v009_signal,
    f01bep_f01_brand_equity_pricing_gppu_mean_504d_base_v010_signal,
    f01bep_f01_brand_equity_pricing_gppu_std_21d_base_v011_signal,
    f01bep_f01_brand_equity_pricing_gppu_std_63d_base_v012_signal,
    f01bep_f01_brand_equity_pricing_gppu_std_252d_base_v013_signal,
    f01bep_f01_brand_equity_pricing_gppu_z_21d_base_v014_signal,
    f01bep_f01_brand_equity_pricing_gppu_z_63d_base_v015_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_5d_base_v016_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_10d_base_v017_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_21d_base_v018_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_42d_base_v019_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_63d_base_v020_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_126d_base_v021_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_189d_base_v022_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_252d_base_v023_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_378d_base_v024_signal,
    f01bep_f01_brand_equity_pricing_mu_mean_504d_base_v025_signal,
    f01bep_f01_brand_equity_pricing_mu_std_10d_base_v026_signal,
    f01bep_f01_brand_equity_pricing_mu_std_21d_base_v027_signal,
    f01bep_f01_brand_equity_pricing_mu_std_63d_base_v028_signal,
    f01bep_f01_brand_equity_pricing_mu_std_126d_base_v029_signal,
    f01bep_f01_brand_equity_pricing_mu_std_252d_base_v030_signal,
    f01bep_f01_brand_equity_pricing_mu_z_21d_base_v031_signal,
    f01bep_f01_brand_equity_pricing_mu_z_63d_base_v032_signal,
    f01bep_f01_brand_equity_pricing_mu_z_126d_base_v033_signal,
    f01bep_f01_brand_equity_pricing_mu_z_252d_base_v034_signal,
    f01bep_f01_brand_equity_pricing_mu_ema_21d_base_v035_signal,
    f01bep_f01_brand_equity_pricing_mu_ema_63d_base_v036_signal,
    f01bep_f01_brand_equity_pricing_mu_ema_126d_base_v037_signal,
    f01bep_f01_brand_equity_pricing_mu_ema_252d_base_v038_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_21d_base_v039_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_63d_base_v040_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_126d_base_v041_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_252d_base_v042_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_378d_base_v043_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_504d_base_v044_signal,
    f01bep_f01_brand_equity_pricing_mu_abs_5d_base_v045_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_5d_base_v046_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_10d_base_v047_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_21d_base_v048_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_42d_base_v049_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_63d_base_v050_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_126d_base_v051_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_189d_base_v052_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_252d_base_v053_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_378d_base_v054_signal,
    f01bep_f01_brand_equity_pricing_ps_raw_504d_base_v055_signal,
    f01bep_f01_brand_equity_pricing_ps_mean_21d_base_v056_signal,
    f01bep_f01_brand_equity_pricing_ps_mean_63d_base_v057_signal,
    f01bep_f01_brand_equity_pricing_ps_mean_126d_base_v058_signal,
    f01bep_f01_brand_equity_pricing_ps_mean_252d_base_v059_signal,
    f01bep_f01_brand_equity_pricing_ps_mean_378d_base_v060_signal,
    f01bep_f01_brand_equity_pricing_ps_std_21d_base_v061_signal,
    f01bep_f01_brand_equity_pricing_ps_std_63d_base_v062_signal,
    f01bep_f01_brand_equity_pricing_ps_std_126d_base_v063_signal,
    f01bep_f01_brand_equity_pricing_ps_std_252d_base_v064_signal,
    f01bep_f01_brand_equity_pricing_ps_std_378d_base_v065_signal,
    f01bep_f01_brand_equity_pricing_ps_z_21d_base_v066_signal,
    f01bep_f01_brand_equity_pricing_ps_z_63d_base_v067_signal,
    f01bep_f01_brand_equity_pricing_ps_z_126d_base_v068_signal,
    f01bep_f01_brand_equity_pricing_ps_z_252d_base_v069_signal,
    f01bep_f01_brand_equity_pricing_ps_ema_21d_base_v070_signal,
    f01bep_f01_brand_equity_pricing_ps_ema_63d_base_v071_signal,
    f01bep_f01_brand_equity_pricing_ps_ema_126d_base_v072_signal,
    f01bep_f01_brand_equity_pricing_ps_ema_252d_base_v073_signal,
    f01bep_f01_brand_equity_pricing_ps_absmean_21d_base_v074_signal,
    f01bep_f01_brand_equity_pricing_ps_absmean_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_BRAND_EQUITY_PRICING_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f01_gp_per_unit", "_f01_margin_uplift", "_f01_pricing_strength")
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
    print(f"OK f01_brand_equity_pricing_base_001_075_claude: {n_features} features pass")
