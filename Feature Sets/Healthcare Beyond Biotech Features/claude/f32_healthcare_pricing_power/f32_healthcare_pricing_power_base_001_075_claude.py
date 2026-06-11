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
def _f32_rev_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f32_pricing_uplift(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    return rpa - rpa.shift(w)


def _f32_unit_economics_lift(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    return _mean(rpa, w) - _mean(rpa, w).shift(w)


# ---- features ----

def f32hpp_f32_healthcare_pricing_power_rpa_base_v001_signal(revenue, assets, closeadj):
    result = _f32_rev_per_asset(revenue, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_21d_base_v002_signal(revenue, assets, closeadj):
    result = _mean(_f32_rev_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_63d_base_v003_signal(revenue, assets, closeadj):
    result = _mean(_f32_rev_per_asset(revenue, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_126d_base_v004_signal(revenue, assets, closeadj):
    result = _mean(_f32_rev_per_asset(revenue, assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_252d_base_v005_signal(revenue, assets, closeadj):
    result = _mean(_f32_rev_per_asset(revenue, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_504d_base_v006_signal(revenue, assets, closeadj):
    result = _mean(_f32_rev_per_asset(revenue, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpastd_21d_base_v007_signal(revenue, assets, closeadj):
    result = _std(_f32_rev_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpastd_63d_base_v008_signal(revenue, assets, closeadj):
    result = _std(_f32_rev_per_asset(revenue, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpastd_252d_base_v009_signal(revenue, assets, closeadj):
    result = _std(_f32_rev_per_asset(revenue, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaz_63d_base_v010_signal(revenue, assets, closeadj):
    result = _z(_f32_rev_per_asset(revenue, assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaz_252d_base_v011_signal(revenue, assets, closeadj):
    result = _z(_f32_rev_per_asset(revenue, assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaz_504d_base_v012_signal(revenue, assets, closeadj):
    result = _z(_f32_rev_per_asset(revenue, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_21d_base_v013_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_63d_base_v014_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_126d_base_v015_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_252d_base_v016_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_504d_base_v017_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_5d_base_v018_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_10d_base_v019_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_42d_base_v020_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_189d_base_v021_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_378d_base_v022_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_21d_base_v023_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_63d_base_v024_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_126d_base_v025_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_252d_base_v026_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_5d_base_v027_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_10d_base_v028_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlift_42d_base_v029_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaema_21d_base_v030_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaema_63d_base_v031_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaema_252d_base_v032_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftmean_63d_base_v033_signal(revenue, ppnenet, closeadj):
    result = _mean(_f32_pricing_uplift(revenue, ppnenet, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftmean_252d_base_v034_signal(revenue, ppnenet, closeadj):
    result = _mean(_f32_pricing_uplift(revenue, ppnenet, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftstd_63d_base_v035_signal(revenue, ppnenet, closeadj):
    result = _std(_f32_pricing_uplift(revenue, ppnenet, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftstd_252d_base_v036_signal(revenue, ppnenet, closeadj):
    result = _std(_f32_pricing_uplift(revenue, ppnenet, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftz_63d_base_v037_signal(revenue, ppnenet, closeadj):
    result = _z(_f32_pricing_uplift(revenue, ppnenet, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftz_252d_base_v038_signal(revenue, ppnenet, closeadj):
    result = _z(_f32_pricing_uplift(revenue, ppnenet, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpasq_63d_base_v039_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = _mean(base * base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpasq_252d_base_v040_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpamax_252d_base_v041_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpamin_252d_base_v042_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparange_252d_base_v043_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparank_63d_base_v044_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    rank = base.rolling(63, min_periods=20).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparank_252d_base_v045_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparank_504d_base_v046_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpadiff_63d_base_v047_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpadiff_252d_base_v048_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapctchg_63d_base_v049_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapctchg_252d_base_v050_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftxprice_63d_base_v051_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftxprice_252d_base_v052_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlxprice_63d_base_v053_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlxprice_252d_base_v054_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftmean_42d_base_v055_signal(revenue, ppnenet, closeadj):
    result = _mean(_f32_pricing_uplift(revenue, ppnenet, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftmean_126d_base_v056_signal(revenue, ppnenet, closeadj):
    result = _mean(_f32_pricing_uplift(revenue, ppnenet, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlmean_63d_base_v057_signal(revenue, assets, closeadj):
    result = _mean(_f32_unit_economics_lift(revenue, assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlmean_252d_base_v058_signal(revenue, assets, closeadj):
    result = _mean(_f32_unit_economics_lift(revenue, assets, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlstd_252d_base_v059_signal(revenue, assets, closeadj):
    result = _std(_f32_unit_economics_lift(revenue, assets, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlz_252d_base_v060_signal(revenue, assets, closeadj):
    result = _z(_f32_unit_economics_lift(revenue, assets, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftsign_63d_base_v061_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftsign_252d_base_v062_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 252)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftsq_63d_base_v063_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftsq_252d_base_v064_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftrank_252d_base_v065_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlrank_252d_base_v066_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparatio_63v252_base_v067_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = _mean(base, 63) / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rparatio_21v126_base_v068_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = _mean(base, 21) / _mean(base, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpalog_252d_base_v069_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftxclose_63d_base_v070_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_upliftxclose_252d_base_v071_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlxclose_63d_base_v072_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitlxclose_252d_base_v073_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpacumsum_252d_base_v074_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets) - _mean(_f32_rev_per_asset(revenue, assets), 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpasignchg_252d_base_v075_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    diff = base.diff(63)
    result = np.sign(diff) * _mean(closeadj, 63) * (1.0 + base.abs() * 0.01)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32hpp_f32_healthcare_pricing_power_rpa_base_v001_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_21d_base_v002_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_63d_base_v003_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_126d_base_v004_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_252d_base_v005_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_504d_base_v006_signal,
    f32hpp_f32_healthcare_pricing_power_rpastd_21d_base_v007_signal,
    f32hpp_f32_healthcare_pricing_power_rpastd_63d_base_v008_signal,
    f32hpp_f32_healthcare_pricing_power_rpastd_252d_base_v009_signal,
    f32hpp_f32_healthcare_pricing_power_rpaz_63d_base_v010_signal,
    f32hpp_f32_healthcare_pricing_power_rpaz_252d_base_v011_signal,
    f32hpp_f32_healthcare_pricing_power_rpaz_504d_base_v012_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_21d_base_v013_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_63d_base_v014_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_126d_base_v015_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_252d_base_v016_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_504d_base_v017_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_5d_base_v018_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_10d_base_v019_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_42d_base_v020_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_189d_base_v021_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_378d_base_v022_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_21d_base_v023_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_63d_base_v024_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_126d_base_v025_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_252d_base_v026_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_5d_base_v027_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_10d_base_v028_signal,
    f32hpp_f32_healthcare_pricing_power_unitlift_42d_base_v029_signal,
    f32hpp_f32_healthcare_pricing_power_rpaema_21d_base_v030_signal,
    f32hpp_f32_healthcare_pricing_power_rpaema_63d_base_v031_signal,
    f32hpp_f32_healthcare_pricing_power_rpaema_252d_base_v032_signal,
    f32hpp_f32_healthcare_pricing_power_upliftmean_63d_base_v033_signal,
    f32hpp_f32_healthcare_pricing_power_upliftmean_252d_base_v034_signal,
    f32hpp_f32_healthcare_pricing_power_upliftstd_63d_base_v035_signal,
    f32hpp_f32_healthcare_pricing_power_upliftstd_252d_base_v036_signal,
    f32hpp_f32_healthcare_pricing_power_upliftz_63d_base_v037_signal,
    f32hpp_f32_healthcare_pricing_power_upliftz_252d_base_v038_signal,
    f32hpp_f32_healthcare_pricing_power_rpasq_63d_base_v039_signal,
    f32hpp_f32_healthcare_pricing_power_rpasq_252d_base_v040_signal,
    f32hpp_f32_healthcare_pricing_power_rpamax_252d_base_v041_signal,
    f32hpp_f32_healthcare_pricing_power_rpamin_252d_base_v042_signal,
    f32hpp_f32_healthcare_pricing_power_rparange_252d_base_v043_signal,
    f32hpp_f32_healthcare_pricing_power_rparank_63d_base_v044_signal,
    f32hpp_f32_healthcare_pricing_power_rparank_252d_base_v045_signal,
    f32hpp_f32_healthcare_pricing_power_rparank_504d_base_v046_signal,
    f32hpp_f32_healthcare_pricing_power_rpadiff_63d_base_v047_signal,
    f32hpp_f32_healthcare_pricing_power_rpadiff_252d_base_v048_signal,
    f32hpp_f32_healthcare_pricing_power_rpapctchg_63d_base_v049_signal,
    f32hpp_f32_healthcare_pricing_power_rpapctchg_252d_base_v050_signal,
    f32hpp_f32_healthcare_pricing_power_upliftxprice_63d_base_v051_signal,
    f32hpp_f32_healthcare_pricing_power_upliftxprice_252d_base_v052_signal,
    f32hpp_f32_healthcare_pricing_power_unitlxprice_63d_base_v053_signal,
    f32hpp_f32_healthcare_pricing_power_unitlxprice_252d_base_v054_signal,
    f32hpp_f32_healthcare_pricing_power_upliftmean_42d_base_v055_signal,
    f32hpp_f32_healthcare_pricing_power_upliftmean_126d_base_v056_signal,
    f32hpp_f32_healthcare_pricing_power_unitlmean_63d_base_v057_signal,
    f32hpp_f32_healthcare_pricing_power_unitlmean_252d_base_v058_signal,
    f32hpp_f32_healthcare_pricing_power_unitlstd_252d_base_v059_signal,
    f32hpp_f32_healthcare_pricing_power_unitlz_252d_base_v060_signal,
    f32hpp_f32_healthcare_pricing_power_upliftsign_63d_base_v061_signal,
    f32hpp_f32_healthcare_pricing_power_upliftsign_252d_base_v062_signal,
    f32hpp_f32_healthcare_pricing_power_upliftsq_63d_base_v063_signal,
    f32hpp_f32_healthcare_pricing_power_upliftsq_252d_base_v064_signal,
    f32hpp_f32_healthcare_pricing_power_upliftrank_252d_base_v065_signal,
    f32hpp_f32_healthcare_pricing_power_unitlrank_252d_base_v066_signal,
    f32hpp_f32_healthcare_pricing_power_rparatio_63v252_base_v067_signal,
    f32hpp_f32_healthcare_pricing_power_rparatio_21v126_base_v068_signal,
    f32hpp_f32_healthcare_pricing_power_rpalog_252d_base_v069_signal,
    f32hpp_f32_healthcare_pricing_power_upliftxclose_63d_base_v070_signal,
    f32hpp_f32_healthcare_pricing_power_upliftxclose_252d_base_v071_signal,
    f32hpp_f32_healthcare_pricing_power_unitlxclose_63d_base_v072_signal,
    f32hpp_f32_healthcare_pricing_power_unitlxclose_252d_base_v073_signal,
    f32hpp_f32_healthcare_pricing_power_rpacumsum_252d_base_v074_signal,
    f32hpp_f32_healthcare_pricing_power_rpasignchg_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_HEALTHCARE_PRICING_POWER_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f32_rev_per_asset", "_f32_pricing_uplift", "_f32_unit_economics_lift")
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
    print(f"OK f32_healthcare_pricing_power_base_001_075_claude: {n_features} features pass")
