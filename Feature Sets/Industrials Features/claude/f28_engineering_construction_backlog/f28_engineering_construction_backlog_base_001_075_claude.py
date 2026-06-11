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
def _f28_backlog_proxy(deferredrev, revenue):
    # backlog proxy: deferred revenue as fraction of trailing 252d revenue mean
    rev_ma = revenue.rolling(252, min_periods=63).mean()
    return deferredrev / rev_ma.replace(0, np.nan)


def _f28_pipeline_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f28_backlog_consumption(deferredrev, revenue, w):
    # backlog consumption: revenue growth relative to backlog growth
    rg = revenue.pct_change(periods=w)
    bg = deferredrev.pct_change(periods=w)
    return rg - bg


def f28ecb_f28_engineering_construction_backlog_bproxy_5d_base_v001_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_10d_base_v002_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_21d_base_v003_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_42d_base_v004_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_63d_base_v005_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_126d_base_v006_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_189d_base_v007_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_252d_base_v008_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_378d_base_v009_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_504d_base_v010_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_proxy(deferredrev, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_std21_base_v011_signal(deferredrev, revenue, closeadj):
    result = _std(_f28_backlog_proxy(deferredrev, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_std63_base_v012_signal(deferredrev, revenue, closeadj):
    result = _std(_f28_backlog_proxy(deferredrev, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_std126_base_v013_signal(deferredrev, revenue, closeadj):
    result = _std(_f28_backlog_proxy(deferredrev, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_std252_base_v014_signal(deferredrev, revenue, closeadj):
    result = _std(_f28_backlog_proxy(deferredrev, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_z21_base_v015_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_proxy(deferredrev, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_z63_base_v016_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_proxy(deferredrev, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_z126_base_v017_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_proxy(deferredrev, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_z252_base_v018_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_proxy(deferredrev, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_5d_base_v019_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_10d_base_v020_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_21d_base_v021_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_42d_base_v022_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_63d_base_v023_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_126d_base_v024_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_189d_base_v025_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_252d_base_v026_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_378d_base_v027_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_504d_base_v028_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthma_21d_base_v029_signal(deferredrev, closeadj):
    result = _mean(_f28_pipeline_growth(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthma_63d_base_v030_signal(deferredrev, closeadj):
    result = _mean(_f28_pipeline_growth(deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthma_126d_base_v031_signal(deferredrev, closeadj):
    result = _mean(_f28_pipeline_growth(deferredrev, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthma_252d_base_v032_signal(deferredrev, closeadj):
    result = _mean(_f28_pipeline_growth(deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthstd_63d_base_v033_signal(deferredrev, closeadj):
    result = _std(_f28_pipeline_growth(deferredrev, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthstd_252d_base_v034_signal(deferredrev, closeadj):
    result = _std(_f28_pipeline_growth(deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthz_63d_base_v035_signal(deferredrev, closeadj):
    result = _z(_f28_pipeline_growth(deferredrev, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthz_252d_base_v036_signal(deferredrev, closeadj):
    result = _z(_f28_pipeline_growth(deferredrev, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_5d_base_v037_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_10d_base_v038_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_21d_base_v039_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_42d_base_v040_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_63d_base_v041_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_126d_base_v042_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_189d_base_v043_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_252d_base_v044_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_378d_base_v045_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsum_504d_base_v046_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumma_21d_base_v047_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_consumption(deferredrev, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumma_63d_base_v048_signal(deferredrev, revenue, closeadj):
    result = _mean(_f28_backlog_consumption(deferredrev, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumz_63d_base_v049_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_consumption(deferredrev, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumz_252d_base_v050_signal(deferredrev, revenue, closeadj):
    result = _z(_f28_backlog_consumption(deferredrev, revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpgrowth_base_v051_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_pipeline_growth(deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpgrowth252_base_v052_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_pipeline_growth(deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxbconsum_base_v053_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxbconsum252_base_v054_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_consumption(deferredrev, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxbconsum_base_v055_signal(deferredrev, revenue, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63) * _f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxbconsum252_base_v056_signal(deferredrev, revenue, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 252) * _f28_backlog_consumption(deferredrev, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxysq_base_v057_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthsq_base_v058_signal(deferredrev, revenue, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63) * _f28_pipeline_growth(deferredrev, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumsq_base_v059_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63) * _f28_backlog_consumption(deferredrev, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxypluspgrowth_base_v060_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxlogpx_252d_base_v061_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxlogpx_63d_base_v062_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxgap_252d_base_v063_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxpxgap_252d_base_v064_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpxgap_63d_base_v065_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63) * (closeadj - _mean(closeadj, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyema_63d_base_v066_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthema_21d_base_v067_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumema_63d_base_v068_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyrank_252d_base_v069_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthrank_252d_base_v070_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumrank_252d_base_v071_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyabs_base_v072_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthabs_63d_base_v073_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxysq_base_v074_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_proxy(deferredrev, revenue).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_dev252_base_v075_signal(deferredrev, revenue, closeadj):
    result = ((_f28_backlog_proxy(deferredrev, revenue) - _mean(_f28_backlog_proxy(deferredrev, revenue), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28ecb_f28_engineering_construction_backlog_bproxy_5d_base_v001_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_10d_base_v002_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_21d_base_v003_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_42d_base_v004_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_63d_base_v005_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_126d_base_v006_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_189d_base_v007_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_252d_base_v008_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_378d_base_v009_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_504d_base_v010_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_std21_base_v011_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_std63_base_v012_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_std126_base_v013_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_std252_base_v014_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_z21_base_v015_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_z63_base_v016_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_z126_base_v017_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_z252_base_v018_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_5d_base_v019_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_10d_base_v020_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_21d_base_v021_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_42d_base_v022_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_63d_base_v023_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_126d_base_v024_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_189d_base_v025_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_252d_base_v026_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_378d_base_v027_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_504d_base_v028_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthma_21d_base_v029_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthma_63d_base_v030_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthma_126d_base_v031_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthma_252d_base_v032_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthstd_63d_base_v033_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthstd_252d_base_v034_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthz_63d_base_v035_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthz_252d_base_v036_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_5d_base_v037_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_10d_base_v038_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_21d_base_v039_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_42d_base_v040_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_63d_base_v041_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_126d_base_v042_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_189d_base_v043_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_252d_base_v044_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_378d_base_v045_signal,
    f28ecb_f28_engineering_construction_backlog_bconsum_504d_base_v046_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumma_21d_base_v047_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumma_63d_base_v048_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumz_63d_base_v049_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumz_252d_base_v050_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpgrowth_base_v051_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpgrowth252_base_v052_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxbconsum_base_v053_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxbconsum252_base_v054_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxbconsum_base_v055_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxbconsum252_base_v056_signal,
    f28ecb_f28_engineering_construction_backlog_bproxysq_base_v057_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthsq_base_v058_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumsq_base_v059_signal,
    f28ecb_f28_engineering_construction_backlog_bproxypluspgrowth_base_v060_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxlogpx_252d_base_v061_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxlogpx_63d_base_v062_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxgap_252d_base_v063_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxpxgap_252d_base_v064_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpxgap_63d_base_v065_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyema_63d_base_v066_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthema_21d_base_v067_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumema_63d_base_v068_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyrank_252d_base_v069_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthrank_252d_base_v070_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumrank_252d_base_v071_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyabs_base_v072_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthabs_63d_base_v073_signal,
    f28ecb_f28_engineering_construction_backlog_bproxysq_base_v074_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_dev252_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_ENGINEERING_CONSTRUCTION_BACKLOG_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "deferredrev": deferredrev,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_backlog_proxy", "_f28_pipeline_growth", "_f28_backlog_consumption")
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
    print(f"OK f28_engineering_construction_backlog_base_001_075_claude: {n_features} features pass")
