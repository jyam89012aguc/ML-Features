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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f17_rev_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)

def _f17_rev_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)

def _f17_pricing_uplift(revenue, assets, w):
    ratio = revenue / assets.replace(0, np.nan)
    return ratio - _mean(ratio, w)


# ===== features =====
def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rmean_c_sw5_v001_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 5)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rmean_c_sw252_v002_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 5)) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rmean_c_sw126_v003_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_mean(p, 5)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_rmean_logc_sw126_v004_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_rmean_logc_sw63_v005_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_rmean_logc_sw21_v006_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (_mean(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_rmean_cmean_sw21_v007_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_rmean_cmean_sw10_v008_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_rmean_cmean_sw5_v009_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (_mean(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_rmean_revn_sw5_v010_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_rmean_revn_sw252_v011_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_rmean_revn_sw126_v012_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (_mean(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_rmean_c_sw126_v013_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 63)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_rmean_c_sw63_v014_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 63)) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_rmean_c_sw21_v015_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (_mean(p, 63)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_rmean_logc_sw21_v016_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_rmean_logc_sw10_v017_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_rmean_logc_sw5_v018_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (_mean(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_rmean_cmean_sw5_v019_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_rmean_cmean_sw252_v020_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_rmean_cmean_sw126_v021_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (_mean(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rstd_c_sw5_v022_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 5)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rstd_c_sw252_v023_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 5)) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rstd_c_sw126_v024_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_std(p, 5)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_rstd_logc_sw126_v025_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_rstd_logc_sw63_v026_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_rstd_logc_sw21_v027_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (_std(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_rstd_cmean_sw21_v028_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_rstd_cmean_sw10_v029_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_rstd_cmean_sw5_v030_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (_std(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_rstd_revn_sw5_v031_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_rstd_revn_sw252_v032_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_rstd_revn_sw126_v033_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (_std(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_rstd_c_sw126_v034_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 63)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_rstd_c_sw63_v035_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 63)) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_rstd_c_sw21_v036_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (_std(p, 63)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_rstd_logc_sw21_v037_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_rstd_logc_sw10_v038_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_rstd_logc_sw5_v039_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (_std(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_rstd_cmean_sw5_v040_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_std(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_rstd_cmean_sw252_v041_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_std(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_rstd_cmean_sw126_v042_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (_std(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_ema_c_sw5_v043_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 5)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_ema_c_sw252_v044_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 5)) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_ema_c_sw126_v045_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_ema(p, 5)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_ema_logc_sw126_v046_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_ema_logc_sw63_v047_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_ema_logc_sw21_v048_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (_ema(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_ema_cmean_sw21_v049_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_ema_cmean_sw10_v050_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_ema_cmean_sw5_v051_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (_ema(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_ema_revn_sw5_v052_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_ema_revn_sw252_v053_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_ema_revn_sw126_v054_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (_ema(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_ema_c_sw126_v055_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 63)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_ema_c_sw63_v056_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 63)) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_ema_c_sw21_v057_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (_ema(p, 63)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_ema_logc_sw21_v058_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_ema_logc_sw10_v059_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_ema_logc_sw5_v060_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (_ema(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_ema_cmean_sw5_v061_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_ema(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_ema_cmean_sw252_v062_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_ema(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_ema_cmean_sw126_v063_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (_ema(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_zscore_c_sw5_v064_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 5)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_zscore_c_sw252_v065_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 5)) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_zscore_c_sw126_v066_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_z(p, 5)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_zscore_logc_sw126_v067_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_zscore_logc_sw63_v068_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_zscore_logc_sw21_v069_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (_z(p, 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_zscore_cmean_sw21_v070_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_zscore_cmean_sw10_v071_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_zscore_cmean_sw5_v072_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (_z(p, 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_zscore_revn_sw5_v073_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_zscore_revn_sw252_v074_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_zscore_revn_sw126_v075_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (_z(p, 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_zscore_c_sw126_v076_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 63)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_zscore_c_sw63_v077_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 63)) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_zscore_c_sw21_v078_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (_z(p, 63)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_zscore_logc_sw21_v079_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_zscore_logc_sw10_v080_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_zscore_logc_sw5_v081_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (_z(p, 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_zscore_cmean_sw5_v082_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_z(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_zscore_cmean_sw252_v083_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_z(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_zscore_cmean_sw126_v084_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (_z(p, 252)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_logm_c_sw5_v085_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 5).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_logm_c_sw252_v086_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 5).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_logm_c_sw126_v087_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (np.log(_mean(p, 5).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_logm_logc_sw126_v088_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 10).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_logm_logc_sw63_v089_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 10).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_logm_logc_sw21_v090_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (np.log(_mean(p, 10).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_logm_cmean_sw21_v091_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 21).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_logm_cmean_sw10_v092_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 21).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_logm_cmean_sw5_v093_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (np.log(_mean(p, 21).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_logm_revn_sw5_v094_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 42).abs() + 1.0)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_logm_revn_sw252_v095_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 42).abs() + 1.0)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_logm_revn_sw126_v096_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (np.log(_mean(p, 42).abs() + 1.0)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_logm_c_sw126_v097_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 63).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_logm_c_sw63_v098_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 63).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_logm_c_sw21_v099_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (np.log(_mean(p, 63).abs() + 1.0)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_logm_logc_sw21_v100_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 126).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_logm_logc_sw10_v101_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 126).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_logm_logc_sw5_v102_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (np.log(_mean(p, 126).abs() + 1.0)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_logm_cmean_sw5_v103_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.log(_mean(p, 252).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_logm_cmean_sw252_v104_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.log(_mean(p, 252).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_logm_cmean_sw126_v105_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (np.log(_mean(p, 252).abs() + 1.0)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_ssqrt_c_sw5_v106_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 5)) * np.sqrt(_mean(p, 5).abs())) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_ssqrt_c_sw252_v107_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 5)) * np.sqrt(_mean(p, 5).abs())) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_ssqrt_c_sw126_v108_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (np.sign(_mean(p, 5)) * np.sqrt(_mean(p, 5).abs())) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_ssqrt_logc_sw126_v109_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 10)) * np.sqrt(_mean(p, 10).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_ssqrt_logc_sw63_v110_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 10)) * np.sqrt(_mean(p, 10).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_ssqrt_logc_sw21_v111_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (np.sign(_mean(p, 10)) * np.sqrt(_mean(p, 10).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_ssqrt_cmean_sw21_v112_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 21)) * np.sqrt(_mean(p, 21).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_ssqrt_cmean_sw10_v113_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 21)) * np.sqrt(_mean(p, 21).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_ssqrt_cmean_sw5_v114_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (np.sign(_mean(p, 21)) * np.sqrt(_mean(p, 21).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_ssqrt_revn_sw5_v115_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 42)) * np.sqrt(_mean(p, 42).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_ssqrt_revn_sw252_v116_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 42)) * np.sqrt(_mean(p, 42).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_ssqrt_revn_sw126_v117_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (np.sign(_mean(p, 42)) * np.sqrt(_mean(p, 42).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_ssqrt_c_sw126_v118_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 63)) * np.sqrt(_mean(p, 63).abs())) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_ssqrt_c_sw63_v119_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 63)) * np.sqrt(_mean(p, 63).abs())) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_ssqrt_c_sw21_v120_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (np.sign(_mean(p, 63)) * np.sqrt(_mean(p, 63).abs())) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_ssqrt_logc_sw21_v121_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 126)) * np.sqrt(_mean(p, 126).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_ssqrt_logc_sw10_v122_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 126)) * np.sqrt(_mean(p, 126).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_ssqrt_logc_sw5_v123_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (np.sign(_mean(p, 126)) * np.sqrt(_mean(p, 126).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_ssqrt_cmean_sw5_v124_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (np.sign(_mean(p, 252)) * np.sqrt(_mean(p, 252).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_ssqrt_cmean_sw252_v125_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (np.sign(_mean(p, 252)) * np.sqrt(_mean(p, 252).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_ssqrt_cmean_sw126_v126_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (np.sign(_mean(p, 252)) * np.sqrt(_mean(p, 252).abs())) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_diffxc_c_sw5_v127_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 5) * closeadj) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_diffxc_c_sw252_v128_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 5) * closeadj) * (closeadj)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_diffxc_c_sw126_v129_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_diff(p, 5) * closeadj) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_diffxc_logc_sw126_v130_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 10) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_diffxc_logc_sw63_v131_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 10) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_diffxc_logc_sw21_v132_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 10)
    base = (_diff(p, 10) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_diffxc_cmean_sw21_v133_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 21) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_diffxc_cmean_sw10_v134_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 21) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_diffxc_cmean_sw5_v135_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 21)
    base = (_diff(p, 21) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_diffxc_revn_sw5_v136_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 42) * closeadj) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_diffxc_revn_sw252_v137_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 42) * closeadj) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_diffxc_revn_sw126_v138_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 42)
    base = (_diff(p, 42) * closeadj) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_diffxc_c_sw126_v139_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 63) * closeadj) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_diffxc_c_sw63_v140_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 63) * closeadj) * (closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_diffxc_c_sw21_v141_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 63)
    base = (_diff(p, 63) * closeadj) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_diffxc_logc_sw21_v142_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 126) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_diffxc_logc_sw10_v143_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 126) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_diffxc_logc_sw5_v144_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 126)
    base = (_diff(p, 126) * closeadj) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_diffxc_cmean_sw5_v145_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_diff(p, 252) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_diffxc_cmean_sw252_v146_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_diff(p, 252) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_diffxc_cmean_sw126_v147_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 252)
    base = (_diff(p, 252) * closeadj) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rmean_logc_sw63_v148_signal(revenue, assets, closeadj):
    p = _f17_rev_per_asset(revenue, assets)
    base = (_mean(p, 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rmean_logc_sw21_v149_signal(revenue, ppnenet, closeadj):
    p = _f17_rev_per_ppe(revenue, ppnenet)
    base = (_mean(p, 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rmean_logc_sw10_v150_signal(revenue, assets, closeadj):
    p = _f17_pricing_uplift(revenue, assets, 5)
    base = (_mean(p, 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rmean_c_sw5_v001_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rmean_c_sw252_v002_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rmean_c_sw126_v003_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_rmean_logc_sw126_v004_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_rmean_logc_sw63_v005_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_rmean_logc_sw21_v006_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_rmean_cmean_sw21_v007_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_rmean_cmean_sw10_v008_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_rmean_cmean_sw5_v009_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_rmean_revn_sw5_v010_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_rmean_revn_sw252_v011_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_rmean_revn_sw126_v012_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_rmean_c_sw126_v013_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_rmean_c_sw63_v014_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_rmean_c_sw21_v015_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_rmean_logc_sw21_v016_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_rmean_logc_sw10_v017_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_rmean_logc_sw5_v018_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_rmean_cmean_sw5_v019_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_rmean_cmean_sw252_v020_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_rmean_cmean_sw126_v021_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rstd_c_sw5_v022_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rstd_c_sw252_v023_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rstd_c_sw126_v024_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_rstd_logc_sw126_v025_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_rstd_logc_sw63_v026_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_rstd_logc_sw21_v027_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_rstd_cmean_sw21_v028_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_rstd_cmean_sw10_v029_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_rstd_cmean_sw5_v030_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_rstd_revn_sw5_v031_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_rstd_revn_sw252_v032_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_rstd_revn_sw126_v033_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_rstd_c_sw126_v034_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_rstd_c_sw63_v035_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_rstd_c_sw21_v036_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_rstd_logc_sw21_v037_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_rstd_logc_sw10_v038_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_rstd_logc_sw5_v039_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_rstd_cmean_sw5_v040_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_rstd_cmean_sw252_v041_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_rstd_cmean_sw126_v042_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_ema_c_sw5_v043_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_ema_c_sw252_v044_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_ema_c_sw126_v045_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_ema_logc_sw126_v046_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_ema_logc_sw63_v047_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_ema_logc_sw21_v048_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_ema_cmean_sw21_v049_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_ema_cmean_sw10_v050_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_ema_cmean_sw5_v051_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_ema_revn_sw5_v052_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_ema_revn_sw252_v053_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_ema_revn_sw126_v054_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_ema_c_sw126_v055_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_ema_c_sw63_v056_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_ema_c_sw21_v057_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_ema_logc_sw21_v058_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_ema_logc_sw10_v059_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_ema_logc_sw5_v060_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_ema_cmean_sw5_v061_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_ema_cmean_sw252_v062_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_ema_cmean_sw126_v063_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_zscore_c_sw5_v064_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_zscore_c_sw252_v065_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_zscore_c_sw126_v066_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_zscore_logc_sw126_v067_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_zscore_logc_sw63_v068_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_zscore_logc_sw21_v069_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_zscore_cmean_sw21_v070_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_zscore_cmean_sw10_v071_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_zscore_cmean_sw5_v072_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_zscore_revn_sw5_v073_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_zscore_revn_sw252_v074_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_zscore_revn_sw126_v075_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_zscore_c_sw126_v076_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_zscore_c_sw63_v077_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_zscore_c_sw21_v078_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_zscore_logc_sw21_v079_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_zscore_logc_sw10_v080_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_zscore_logc_sw5_v081_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_zscore_cmean_sw5_v082_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_zscore_cmean_sw252_v083_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_zscore_cmean_sw126_v084_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_logm_c_sw5_v085_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_logm_c_sw252_v086_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_logm_c_sw126_v087_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_logm_logc_sw126_v088_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_logm_logc_sw63_v089_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_logm_logc_sw21_v090_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_logm_cmean_sw21_v091_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_logm_cmean_sw10_v092_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_logm_cmean_sw5_v093_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_logm_revn_sw5_v094_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_logm_revn_sw252_v095_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_logm_revn_sw126_v096_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_logm_c_sw126_v097_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_logm_c_sw63_v098_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_logm_c_sw21_v099_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_logm_logc_sw21_v100_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_logm_logc_sw10_v101_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_logm_logc_sw5_v102_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_logm_cmean_sw5_v103_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_logm_cmean_sw252_v104_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_logm_cmean_sw126_v105_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_ssqrt_c_sw5_v106_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_ssqrt_c_sw252_v107_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_ssqrt_c_sw126_v108_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_ssqrt_logc_sw126_v109_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_ssqrt_logc_sw63_v110_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_ssqrt_logc_sw21_v111_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_ssqrt_cmean_sw21_v112_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_ssqrt_cmean_sw10_v113_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_ssqrt_cmean_sw5_v114_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_ssqrt_revn_sw5_v115_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_ssqrt_revn_sw252_v116_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_ssqrt_revn_sw126_v117_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_ssqrt_c_sw126_v118_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_ssqrt_c_sw63_v119_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_ssqrt_c_sw21_v120_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_ssqrt_logc_sw21_v121_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_ssqrt_logc_sw10_v122_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_ssqrt_logc_sw5_v123_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_ssqrt_cmean_sw5_v124_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_ssqrt_cmean_sw252_v125_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_ssqrt_cmean_sw126_v126_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_diffxc_c_sw5_v127_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_diffxc_c_sw252_v128_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_diffxc_c_sw126_v129_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw10_diffxc_logc_sw126_v130_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw10_diffxc_logc_sw63_v131_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw10_diffxc_logc_sw21_v132_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw21_diffxc_cmean_sw21_v133_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw21_diffxc_cmean_sw10_v134_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw21_diffxc_cmean_sw5_v135_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw42_diffxc_revn_sw5_v136_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw42_diffxc_revn_sw252_v137_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw42_diffxc_revn_sw126_v138_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw63_diffxc_c_sw126_v139_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw63_diffxc_c_sw63_v140_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw63_diffxc_c_sw21_v141_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw126_diffxc_logc_sw21_v142_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw126_diffxc_logc_sw10_v143_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw126_diffxc_logc_sw5_v144_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw252_diffxc_cmean_sw5_v145_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw252_diffxc_cmean_sw252_v146_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw252_diffxc_cmean_sw126_v147_signal,
    f17epp_f17_electrical_pricing_power_rev_per_asset_iw5_rmean_logc_sw63_v148_signal,
    f17epp_f17_electrical_pricing_power_rev_per_ppe_iw5_rmean_logc_sw21_v149_signal,
    f17epp_f17_electrical_pricing_power_pricing_uplift_iw5_rmean_logc_sw10_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_ELECTRICAL_PRICING_POWER_REGISTRY_SLOPE_001_150 = REGISTRY


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
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "capex": capex, "assets": assets,
        "ppnenet": ppnenet, "deferredrev": deferredrev,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f17_rev_per_asset", "_f17_rev_per_ppe", "_f17_pricing_uplift")
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
        src_text = inspect.getsource(fn)
        assert any(p in src_text for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_electrical_pricing_power_2nd_derivatives_001_150_claude: {n_features} features pass")
