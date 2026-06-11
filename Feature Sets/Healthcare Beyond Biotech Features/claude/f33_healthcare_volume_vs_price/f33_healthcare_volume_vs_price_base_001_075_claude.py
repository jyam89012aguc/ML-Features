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
def _f33_volume_proxy(revenue, ppnenet, w):
    rp = revenue / ppnenet.replace(0, np.nan)
    return _mean(rp, w)


def _f33_price_proxy(revenue, assets, w):
    ra = revenue / assets.replace(0, np.nan)
    return _mean(ra, w)


def _f33_volume_price_gap(revenue, ppnenet, assets, w):
    vp = revenue / ppnenet.replace(0, np.nan)
    pp = revenue / assets.replace(0, np.nan)
    return _mean(vp, w) - _mean(pp, w)


# ---- features ----

def f33hvp_f33_healthcare_volume_vs_price_volp_21d_base_v001_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_63d_base_v002_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_126d_base_v003_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_252d_base_v004_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_504d_base_v005_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_5d_base_v006_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_10d_base_v007_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_42d_base_v008_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_189d_base_v009_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_378d_base_v010_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_21d_base_v011_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_63d_base_v012_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_126d_base_v013_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_252d_base_v014_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_504d_base_v015_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_5d_base_v016_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_10d_base_v017_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_42d_base_v018_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_189d_base_v019_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_378d_base_v020_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_base_v021_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_base_v022_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_126d_base_v023_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_252d_base_v024_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_504d_base_v025_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_base_v026_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_base_v027_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_z_63d_base_v028_signal(revenue, ppnenet, closeadj):
    result = _z(_f33_volume_proxy(revenue, ppnenet, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_z_252d_base_v029_signal(revenue, ppnenet, closeadj):
    result = _z(_f33_volume_proxy(revenue, ppnenet, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_z_63d_base_v030_signal(revenue, assets, closeadj):
    result = _z(_f33_price_proxy(revenue, assets, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_z_252d_base_v031_signal(revenue, assets, closeadj):
    result = _z(_f33_price_proxy(revenue, assets, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_z_252d_base_v032_signal(revenue, ppnenet, assets, closeadj):
    result = _z(_f33_volume_price_gap(revenue, ppnenet, assets, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_std_63d_base_v033_signal(revenue, ppnenet, closeadj):
    result = _std(_f33_volume_proxy(revenue, ppnenet, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_std_252d_base_v034_signal(revenue, ppnenet, closeadj):
    result = _std(_f33_volume_proxy(revenue, ppnenet, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_std_63d_base_v035_signal(revenue, assets, closeadj):
    result = _std(_f33_price_proxy(revenue, assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_std_252d_base_v036_signal(revenue, assets, closeadj):
    result = _std(_f33_price_proxy(revenue, assets, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_std_252d_base_v037_signal(revenue, ppnenet, assets, closeadj):
    result = _std(_f33_volume_price_gap(revenue, ppnenet, assets, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_ema_63d_base_v038_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_ema_252d_base_v039_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_ema_63d_base_v040_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_ema_252d_base_v041_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_ema_252d_base_v042_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_diff_63d_base_v043_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_diff_252d_base_v044_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_diff_63d_base_v045_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_diff_252d_base_v046_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_diff_252d_base_v047_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_pctchg_63d_base_v048_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_pctchg_252d_base_v049_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_pctchg_63d_base_v050_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_pctchg_252d_base_v051_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xprice_63d_base_v052_signal(revenue, ppnenet, closeadj):
    result = _f33_volume_proxy(revenue, ppnenet, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xprice_63d_base_v053_signal(revenue, assets, closeadj):
    result = _f33_price_proxy(revenue, assets, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xprice_252d_base_v054_signal(revenue, ppnenet, assets, closeadj):
    result = _f33_volume_price_gap(revenue, ppnenet, assets, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_rank_252d_base_v055_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_rank_252d_base_v056_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_rank_252d_base_v057_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_max_252d_base_v058_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_min_252d_base_v059_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_range_252d_base_v060_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_max_252d_base_v061_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_min_252d_base_v062_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_range_252d_base_v063_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_sq_252d_base_v064_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_sq_252d_base_v065_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_ratio_63v252_base_v066_signal(revenue, ppnenet, closeadj):
    a = _f33_volume_proxy(revenue, ppnenet, 63)
    b = _f33_volume_proxy(revenue, ppnenet, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_ratio_63v252_base_v067_signal(revenue, assets, closeadj):
    a = _f33_price_proxy(revenue, assets, 63)
    b = _f33_price_proxy(revenue, assets, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_log_252d_base_v068_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_log_252d_base_v069_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_sign_252d_base_v070_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = np.sign(base.diff(63)) * _mean(closeadj, 63) * (1.0 + base.abs() * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_sign_252d_base_v071_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = np.sign(base.diff(63)) * _mean(closeadj, 63) * (1.0 + base.abs() * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_mean_63d_base_v072_signal(revenue, ppnenet, assets, closeadj):
    result = _mean(_f33_volume_price_gap(revenue, ppnenet, assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_mean_252d_base_v073_signal(revenue, ppnenet, assets, closeadj):
    result = _mean(_f33_volume_price_gap(revenue, ppnenet, assets, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_cumsum_252d_base_v074_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_signxprice_252d_base_v075_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = np.sign(base) * _mean(closeadj, 63) * (1.0 + base.abs() * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33hvp_f33_healthcare_volume_vs_price_volp_21d_base_v001_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_63d_base_v002_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_126d_base_v003_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_252d_base_v004_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_504d_base_v005_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_5d_base_v006_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_10d_base_v007_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_42d_base_v008_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_189d_base_v009_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_378d_base_v010_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_21d_base_v011_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_63d_base_v012_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_126d_base_v013_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_252d_base_v014_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_504d_base_v015_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_5d_base_v016_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_10d_base_v017_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_42d_base_v018_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_189d_base_v019_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_378d_base_v020_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_21d_base_v021_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_63d_base_v022_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_126d_base_v023_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_252d_base_v024_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_504d_base_v025_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_5d_base_v026_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_42d_base_v027_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_z_63d_base_v028_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_z_252d_base_v029_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_z_63d_base_v030_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_z_252d_base_v031_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_z_252d_base_v032_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_std_63d_base_v033_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_std_252d_base_v034_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_std_63d_base_v035_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_std_252d_base_v036_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_std_252d_base_v037_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_ema_63d_base_v038_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_ema_252d_base_v039_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_ema_63d_base_v040_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_ema_252d_base_v041_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_ema_252d_base_v042_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_diff_63d_base_v043_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_diff_252d_base_v044_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_diff_63d_base_v045_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_diff_252d_base_v046_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_diff_252d_base_v047_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_pctchg_63d_base_v048_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_pctchg_252d_base_v049_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_pctchg_63d_base_v050_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_pctchg_252d_base_v051_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xprice_63d_base_v052_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xprice_63d_base_v053_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xprice_252d_base_v054_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_rank_252d_base_v055_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_rank_252d_base_v056_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_rank_252d_base_v057_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_max_252d_base_v058_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_min_252d_base_v059_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_range_252d_base_v060_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_max_252d_base_v061_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_min_252d_base_v062_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_range_252d_base_v063_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_sq_252d_base_v064_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_sq_252d_base_v065_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_ratio_63v252_base_v066_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_ratio_63v252_base_v067_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_log_252d_base_v068_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_log_252d_base_v069_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_sign_252d_base_v070_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_sign_252d_base_v071_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_mean_63d_base_v072_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_mean_252d_base_v073_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_cumsum_252d_base_v074_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_signxprice_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_HEALTHCARE_VOLUME_VS_PRICE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "assets": assets, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_volume_proxy", "_f33_price_proxy", "_f33_volume_price_gap")
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
    print(f"OK f33_healthcare_volume_vs_price_base_001_075_claude: {n_features} features pass")
