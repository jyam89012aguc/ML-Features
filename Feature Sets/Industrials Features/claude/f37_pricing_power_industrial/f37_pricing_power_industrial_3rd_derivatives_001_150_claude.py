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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f37_revenue_per_unit_asset(revenue, ppnenet):
    """Revenue per dollar of PP&E - pricing/utilization signal."""
    return revenue / ppnenet.replace(0, np.nan)


def _f37_pricing_uplift_signal(revenue, assets, w):
    """Rolling change in revenue / assets vs baseline."""
    rpu = revenue / assets.replace(0, np.nan)
    base = rpu.rolling(w, min_periods=max(2, w // 2)).mean()
    return rpu - base


def _f37_unit_economics_lift(revenue, ppnenet, w):
    """Rolling change in revenue/ppnenet ratio - pricing improvement."""
    rpu = revenue / ppnenet.replace(0, np.nan)
    return rpu.pct_change(periods=w)


def f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag0_5d_jerk_v001_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet).shift(0)
    base_ = base * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag21_21d_jerk_v002_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet).shift(21)
    base_ = base * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag63_63d_jerk_v003_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet).shift(63)
    base_ = base * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag126_126d_jerk_v004_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet).shift(126)
    base_ = base * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_assets_lag0_252d_jerk_v005_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets).shift(0)
    base_ = base * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_assets_lag21_5d_jerk_v006_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets).shift(21)
    base_ = base * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_assets_lag63_21d_jerk_v007_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets).shift(63)
    base_ = base * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunit_assets_lag126_63d_jerk_v008_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets).shift(126)
    base_ = base * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_5d_126d_jerk_v009_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 5) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_10d_252d_jerk_v010_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 10) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_21d_5d_jerk_v011_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_42d_21d_jerk_v012_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 42) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_63d_63d_jerk_v013_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 63) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_126d_126d_jerk_v014_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 126) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_189d_252d_jerk_v015_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 189) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_252d_5d_jerk_v016_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 252) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_378d_21d_jerk_v017_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 378) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperunitsm_504d_63d_jerk_v018_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 504) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_5d_126d_jerk_v019_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 5) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_10d_252d_jerk_v020_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 10) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_21d_5d_jerk_v021_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_42d_21d_jerk_v022_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 42) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_63d_63d_jerk_v023_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 63) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_126d_126d_jerk_v024_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 126) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_189d_252d_jerk_v025_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 189) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_252d_5d_jerk_v026_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 252) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_378d_21d_jerk_v027_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 378) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperasset_504d_63d_jerk_v028_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = _mean(base, 504) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_5d_126d_jerk_v029_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 5)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_10d_252d_jerk_v030_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 10)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_21d_5d_jerk_v031_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 21)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_42d_21d_jerk_v032_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 42)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_63d_63d_jerk_v033_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_126d_126d_jerk_v034_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 126)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_189d_252d_jerk_v035_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 189)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_252d_5d_jerk_v036_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 252)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_378d_21d_jerk_v037_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 378)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uplift_504d_63d_jerk_v038_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 504)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_5d_126d_jerk_v039_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 5)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_10d_252d_jerk_v040_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 10)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_21d_5d_jerk_v041_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 21)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_42d_21d_jerk_v042_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 42)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_63d_63d_jerk_v043_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 63)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_126d_126d_jerk_v044_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 126)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_189d_252d_jerk_v045_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 189)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_252d_5d_jerk_v046_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 252)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_378d_21d_jerk_v047_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 378)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftppne_504d_63d_jerk_v048_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 504)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_5d_126d_jerk_v049_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 5)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_10d_252d_jerk_v050_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 10)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_21d_5d_jerk_v051_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_42d_21d_jerk_v052_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 42)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_63d_63d_jerk_v053_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 63)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_126d_126d_jerk_v054_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 126)
    base_ = u * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_189d_252d_jerk_v055_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 189)
    base_ = u * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_252d_5d_jerk_v056_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 252)
    base_ = u * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_378d_21d_jerk_v057_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 378)
    base_ = u * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_unitecon_504d_63d_jerk_v058_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 504)
    base_ = u * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_5d_126d_jerk_v059_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 5) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_10d_252d_jerk_v060_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 10) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_21d_5d_jerk_v061_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_42d_21d_jerk_v062_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 42) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_63d_63d_jerk_v063_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 63) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_126d_126d_jerk_v064_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 126) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_189d_252d_jerk_v065_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 189) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_252d_5d_jerk_v066_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 252) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_378d_21d_jerk_v067_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 378) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsm_504d_63d_jerk_v068_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _mean(u, 504) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_21_252_126d_jerk_v069_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 21)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_63_252_252d_jerk_v070_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_126_252_5d_jerk_v071_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 126)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_21_504_21d_jerk_v072_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 21)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_63_504_63d_jerk_v073_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftz_126_504_126d_jerk_v074_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 126)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_21_252_252d_jerk_v075_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_63_252_5d_jerk_v076_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 63)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_126_252_21d_jerk_v077_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 126)
    base_ = _z(u, 252) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_21_504_63d_jerk_v078_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_63_504_126d_jerk_v079_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 63)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconz_126_504_252d_jerk_v080_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 126)
    base_ = _z(u, 504) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_5d_5d_jerk_v081_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 5) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_10d_21d_jerk_v082_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 10) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_21d_63d_jerk_v083_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 21) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_42d_126d_jerk_v084_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 42) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_63d_252d_jerk_v085_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 63) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_126d_5d_jerk_v086_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 126) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_189d_21d_jerk_v087_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 189) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_252d_63d_jerk_v088_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 252) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_378d_126d_jerk_v089_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 378) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperppnxasset_504d_252d_jerk_v090_signal(revenue, ppnenet, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _mean(base, 504) * _safe_div(assets, ppnenet) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_5d_5d_jerk_v091_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 5)
    base_ = u * revenue.pct_change(5) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_10d_21d_jerk_v092_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 10)
    base_ = u * revenue.pct_change(10) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_21d_63d_jerk_v093_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 21)
    base_ = u * revenue.pct_change(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_42d_126d_jerk_v094_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 42)
    base_ = u * revenue.pct_change(42) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_63d_252d_jerk_v095_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 63)
    base_ = u * revenue.pct_change(63) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_126d_5d_jerk_v096_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 126)
    base_ = u * revenue.pct_change(126) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_189d_21d_jerk_v097_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 189)
    base_ = u * revenue.pct_change(189) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_252d_63d_jerk_v098_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 252)
    base_ = u * revenue.pct_change(252) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_378d_126d_jerk_v099_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 378)
    base_ = u * revenue.pct_change(378) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftxrevg_504d_252d_jerk_v100_signal(revenue, ppnenet, closeadj):
    u = _f37_pricing_uplift_signal(revenue, ppnenet, 504)
    base_ = u * revenue.pct_change(504) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_5d_5d_jerk_v101_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 5)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_10d_21d_jerk_v102_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 10)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_21d_63d_jerk_v103_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_42d_126d_jerk_v104_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 42)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_63d_252d_jerk_v105_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 63)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_126d_5d_jerk_v106_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 126)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_189d_21d_jerk_v107_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 189)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_252d_63d_jerk_v108_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 252)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_378d_126d_jerk_v109_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 378)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconema_504d_252d_jerk_v110_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 504)
    base_ = _ema(u, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_5d_5d_jerk_v111_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(5) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_10d_21d_jerk_v112_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(10) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_21d_63d_jerk_v113_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_42d_126d_jerk_v114_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(42) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_63d_252d_jerk_v115_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(63) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_126d_5d_jerk_v116_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(126) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_189d_21d_jerk_v117_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(189) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_252d_63d_jerk_v118_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(252) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_378d_126d_jerk_v119_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(378) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revperassetdiff_504d_252d_jerk_v120_signal(revenue, assets, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = base.diff(504) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_63d_5d_jerk_v121_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 63) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_126d_21d_jerk_v122_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 126) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_189d_63d_jerk_v123_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 189) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_252d_126d_jerk_v124_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 252) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_378d_252d_jerk_v125_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 378) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_upliftstd_504d_5d_jerk_v126_signal(revenue, assets, closeadj):
    u = _f37_pricing_uplift_signal(revenue, assets, 63)
    base_ = _std(u, 504) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_5d_21d_jerk_v127_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 5) + _mean(ra, 5)) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_10d_63d_jerk_v128_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 10) + _mean(ra, 10)) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_21d_126d_jerk_v129_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 21) + _mean(ra, 21)) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_42d_252d_jerk_v130_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 42) + _mean(ra, 42)) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_63d_5d_jerk_v131_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 63) + _mean(ra, 63)) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_126d_21d_jerk_v132_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 126) + _mean(ra, 126)) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_189d_63d_jerk_v133_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 189) + _mean(ra, 189)) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_252d_126d_jerk_v134_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 252) + _mean(ra, 252)) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_378d_252d_jerk_v135_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 378) + _mean(ra, 378)) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_composite_504d_5d_jerk_v136_signal(revenue, ppnenet, assets, closeadj):
    rp = _f37_revenue_per_unit_asset(revenue, ppnenet)
    ra = _f37_revenue_per_unit_asset(revenue, assets)
    base_ = (_mean(rp, 504) + _mean(ra, 504)) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_5d_21d_jerk_v137_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 5)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_10d_63d_jerk_v138_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 10)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_21d_126d_jerk_v139_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 21)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_42d_252d_jerk_v140_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 42)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_63d_5d_jerk_v141_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 63)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_126d_21d_jerk_v142_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 126)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_189d_63d_jerk_v143_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 189)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_252d_126d_jerk_v144_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 252)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_378d_252d_jerk_v145_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 378)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_uniteconsq_504d_5d_jerk_v146_signal(revenue, ppnenet, closeadj):
    u = _f37_unit_economics_lift(revenue, ppnenet, 504)
    base_ = u * u.abs() * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revppneema_5d_21d_jerk_v147_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _ema(base, 5) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revppneema_10d_63d_jerk_v148_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _ema(base, 10) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revppneema_21d_126d_jerk_v149_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _ema(base, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f37ppi_f37_pricing_power_industrial_revppneema_42d_252d_jerk_v150_signal(revenue, ppnenet, closeadj):
    base = _f37_revenue_per_unit_asset(revenue, ppnenet)
    base_ = _ema(base, 42) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag0_5d_jerk_v001_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag21_21d_jerk_v002_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag63_63d_jerk_v003_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_ppnenet_lag126_126d_jerk_v004_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_assets_lag0_252d_jerk_v005_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_assets_lag21_5d_jerk_v006_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_assets_lag63_21d_jerk_v007_signal,
    f37ppi_f37_pricing_power_industrial_revperunit_assets_lag126_63d_jerk_v008_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_5d_126d_jerk_v009_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_10d_252d_jerk_v010_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_21d_5d_jerk_v011_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_42d_21d_jerk_v012_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_63d_63d_jerk_v013_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_126d_126d_jerk_v014_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_189d_252d_jerk_v015_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_252d_5d_jerk_v016_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_378d_21d_jerk_v017_signal,
    f37ppi_f37_pricing_power_industrial_revperunitsm_504d_63d_jerk_v018_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_5d_126d_jerk_v019_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_10d_252d_jerk_v020_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_21d_5d_jerk_v021_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_42d_21d_jerk_v022_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_63d_63d_jerk_v023_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_126d_126d_jerk_v024_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_189d_252d_jerk_v025_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_252d_5d_jerk_v026_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_378d_21d_jerk_v027_signal,
    f37ppi_f37_pricing_power_industrial_revperasset_504d_63d_jerk_v028_signal,
    f37ppi_f37_pricing_power_industrial_uplift_5d_126d_jerk_v029_signal,
    f37ppi_f37_pricing_power_industrial_uplift_10d_252d_jerk_v030_signal,
    f37ppi_f37_pricing_power_industrial_uplift_21d_5d_jerk_v031_signal,
    f37ppi_f37_pricing_power_industrial_uplift_42d_21d_jerk_v032_signal,
    f37ppi_f37_pricing_power_industrial_uplift_63d_63d_jerk_v033_signal,
    f37ppi_f37_pricing_power_industrial_uplift_126d_126d_jerk_v034_signal,
    f37ppi_f37_pricing_power_industrial_uplift_189d_252d_jerk_v035_signal,
    f37ppi_f37_pricing_power_industrial_uplift_252d_5d_jerk_v036_signal,
    f37ppi_f37_pricing_power_industrial_uplift_378d_21d_jerk_v037_signal,
    f37ppi_f37_pricing_power_industrial_uplift_504d_63d_jerk_v038_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_5d_126d_jerk_v039_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_10d_252d_jerk_v040_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_21d_5d_jerk_v041_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_42d_21d_jerk_v042_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_63d_63d_jerk_v043_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_126d_126d_jerk_v044_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_189d_252d_jerk_v045_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_252d_5d_jerk_v046_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_378d_21d_jerk_v047_signal,
    f37ppi_f37_pricing_power_industrial_upliftppne_504d_63d_jerk_v048_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_5d_126d_jerk_v049_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_10d_252d_jerk_v050_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_21d_5d_jerk_v051_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_42d_21d_jerk_v052_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_63d_63d_jerk_v053_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_126d_126d_jerk_v054_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_189d_252d_jerk_v055_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_252d_5d_jerk_v056_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_378d_21d_jerk_v057_signal,
    f37ppi_f37_pricing_power_industrial_unitecon_504d_63d_jerk_v058_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_5d_126d_jerk_v059_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_10d_252d_jerk_v060_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_21d_5d_jerk_v061_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_42d_21d_jerk_v062_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_63d_63d_jerk_v063_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_126d_126d_jerk_v064_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_189d_252d_jerk_v065_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_252d_5d_jerk_v066_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_378d_21d_jerk_v067_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsm_504d_63d_jerk_v068_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_21_252_126d_jerk_v069_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_63_252_252d_jerk_v070_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_126_252_5d_jerk_v071_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_21_504_21d_jerk_v072_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_63_504_63d_jerk_v073_signal,
    f37ppi_f37_pricing_power_industrial_upliftz_126_504_126d_jerk_v074_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_21_252_252d_jerk_v075_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_63_252_5d_jerk_v076_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_126_252_21d_jerk_v077_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_21_504_63d_jerk_v078_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_63_504_126d_jerk_v079_signal,
    f37ppi_f37_pricing_power_industrial_uniteconz_126_504_252d_jerk_v080_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_5d_5d_jerk_v081_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_10d_21d_jerk_v082_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_21d_63d_jerk_v083_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_42d_126d_jerk_v084_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_63d_252d_jerk_v085_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_126d_5d_jerk_v086_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_189d_21d_jerk_v087_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_252d_63d_jerk_v088_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_378d_126d_jerk_v089_signal,
    f37ppi_f37_pricing_power_industrial_revperppnxasset_504d_252d_jerk_v090_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_5d_5d_jerk_v091_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_10d_21d_jerk_v092_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_21d_63d_jerk_v093_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_42d_126d_jerk_v094_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_63d_252d_jerk_v095_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_126d_5d_jerk_v096_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_189d_21d_jerk_v097_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_252d_63d_jerk_v098_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_378d_126d_jerk_v099_signal,
    f37ppi_f37_pricing_power_industrial_upliftxrevg_504d_252d_jerk_v100_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_5d_5d_jerk_v101_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_10d_21d_jerk_v102_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_21d_63d_jerk_v103_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_42d_126d_jerk_v104_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_63d_252d_jerk_v105_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_126d_5d_jerk_v106_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_189d_21d_jerk_v107_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_252d_63d_jerk_v108_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_378d_126d_jerk_v109_signal,
    f37ppi_f37_pricing_power_industrial_uniteconema_504d_252d_jerk_v110_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_5d_5d_jerk_v111_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_10d_21d_jerk_v112_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_21d_63d_jerk_v113_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_42d_126d_jerk_v114_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_63d_252d_jerk_v115_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_126d_5d_jerk_v116_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_189d_21d_jerk_v117_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_252d_63d_jerk_v118_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_378d_126d_jerk_v119_signal,
    f37ppi_f37_pricing_power_industrial_revperassetdiff_504d_252d_jerk_v120_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_63d_5d_jerk_v121_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_126d_21d_jerk_v122_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_189d_63d_jerk_v123_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_252d_126d_jerk_v124_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_378d_252d_jerk_v125_signal,
    f37ppi_f37_pricing_power_industrial_upliftstd_504d_5d_jerk_v126_signal,
    f37ppi_f37_pricing_power_industrial_composite_5d_21d_jerk_v127_signal,
    f37ppi_f37_pricing_power_industrial_composite_10d_63d_jerk_v128_signal,
    f37ppi_f37_pricing_power_industrial_composite_21d_126d_jerk_v129_signal,
    f37ppi_f37_pricing_power_industrial_composite_42d_252d_jerk_v130_signal,
    f37ppi_f37_pricing_power_industrial_composite_63d_5d_jerk_v131_signal,
    f37ppi_f37_pricing_power_industrial_composite_126d_21d_jerk_v132_signal,
    f37ppi_f37_pricing_power_industrial_composite_189d_63d_jerk_v133_signal,
    f37ppi_f37_pricing_power_industrial_composite_252d_126d_jerk_v134_signal,
    f37ppi_f37_pricing_power_industrial_composite_378d_252d_jerk_v135_signal,
    f37ppi_f37_pricing_power_industrial_composite_504d_5d_jerk_v136_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_5d_21d_jerk_v137_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_10d_63d_jerk_v138_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_21d_126d_jerk_v139_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_42d_252d_jerk_v140_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_63d_5d_jerk_v141_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_126d_21d_jerk_v142_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_189d_63d_jerk_v143_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_252d_126d_jerk_v144_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_378d_252d_jerk_v145_signal,
    f37ppi_f37_pricing_power_industrial_uniteconsq_504d_5d_jerk_v146_signal,
    f37ppi_f37_pricing_power_industrial_revppneema_5d_21d_jerk_v147_signal,
    f37ppi_f37_pricing_power_industrial_revppneema_10d_63d_jerk_v148_signal,
    f37ppi_f37_pricing_power_industrial_revppneema_21d_126d_jerk_v149_signal,
    f37ppi_f37_pricing_power_industrial_revppneema_42d_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_PRICING_POWER_INDUSTRIAL_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f37_revenue_per_unit_asset", "_f37_pricing_uplift_signal", "_f37_unit_economics_lift")
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
    print(f"OK f37_pricing_power_industrial_3rd_derivatives_001_150_claude: {n_features} features pass")
