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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


def f28ecb_engineering_construction_backlog_bproxy_basic_jerk_v001_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ma21_jerk_v002_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_proxy(deferredrev, revenue), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ma63_jerk_v003_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_proxy(deferredrev, revenue), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ma126_jerk_v004_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_proxy(deferredrev, revenue), 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ma252_jerk_v005_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_proxy(deferredrev, revenue), 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_std21_jerk_v006_signal(deferredrev, revenue, closeadj):
    base = (_std(_f28_backlog_proxy(deferredrev, revenue), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_std63_jerk_v007_signal(deferredrev, revenue, closeadj):
    base = (_std(_f28_backlog_proxy(deferredrev, revenue), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_std252_jerk_v008_signal(deferredrev, revenue, closeadj):
    base = (_std(_f28_backlog_proxy(deferredrev, revenue), 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_z252_jerk_v009_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_proxy(deferredrev, revenue), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_z504_jerk_v010_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_proxy(deferredrev, revenue), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ema21_jerk_v011_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ema63_jerk_v012_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_ema252_jerk_v013_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).ewm(span=252, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_rank252_jerk_v014_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_rank504_jerk_v015_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_abs_jerk_v016_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_sq_jerk_v017_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_proxy(deferredrev, revenue).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xlogrev_jerk_v018_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xlogpx_252_jerk_v019_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xpxgap_252_jerk_v020_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xpxdet_252_jerk_v021_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xpkgap_252_jerk_v022_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xrange_252_jerk_v023_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xstd_252_jerk_v024_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xvolz_252_jerk_v025_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xrevg_252_jerk_v026_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xpxchg_63_jerk_v027_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xpxchg_252_jerk_v028_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xlogdr_jerk_v029_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_diff_63_jerk_v030_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).diff(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_diff_252_jerk_v031_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).diff(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_dev_252_jerk_v032_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) - _mean(_f28_backlog_proxy(deferredrev, revenue), 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_dev_504_jerk_v033_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) - _mean(_f28_backlog_proxy(deferredrev, revenue), 504))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_var_63_jerk_v034_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).rolling(63, min_periods=21).var() * 100.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_var_252_jerk_v035_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_zema_252_jerk_v036_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_proxy(deferredrev, revenue), 252).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_zema_504_jerk_v037_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_proxy(deferredrev, revenue), 504).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_inv_jerk_v038_signal(deferredrev, revenue, closeadj):
    base = ((1.0 - _f28_backlog_proxy(deferredrev, revenue))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_sign_jerk_v039_signal(deferredrev, revenue, closeadj):
    base = (np.sign(_f28_backlog_proxy(deferredrev, revenue) - 0.1) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xebmgn_jerk_v040_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * revenue.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_xebmgn252_jerk_v041_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_logema_63_jerk_v042_signal(deferredrev, revenue, closeadj):
    base = (np.log(_f28_backlog_proxy(deferredrev, revenue).replace(0, np.nan).abs() + 1.0).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_x_pgrowth_jerk_v043_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _f28_pipeline_growth(deferredrev, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_x_pgrowth252_jerk_v044_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _f28_pipeline_growth(deferredrev, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_x_bconsum_jerk_v045_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_x_bconsum252_jerk_v046_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_consumption(deferredrev, revenue, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_plus_pgrowth_jerk_v047_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_minus_pgrowth_jerk_v048_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) - _f28_pipeline_growth(deferredrev, 63))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_minus_bconsum_jerk_v049_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) - _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_plus_bconsum_jerk_v050_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_21_jerk_v051_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_63_jerk_v052_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_126_jerk_v053_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 126)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_252_jerk_v054_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_504_jerk_v055_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_5_jerk_v056_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_42_jerk_v057_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 42)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_189_jerk_v058_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 189)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ma21_jerk_v059_signal(deferredrev, closeadj):
    base = (_mean(_f28_pipeline_growth(deferredrev, 63), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ma63_jerk_v060_signal(deferredrev, closeadj):
    base = (_mean(_f28_pipeline_growth(deferredrev, 252), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ma126_jerk_v061_signal(deferredrev, closeadj):
    base = (_mean(_f28_pipeline_growth(deferredrev, 252), 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_std63_jerk_v062_signal(deferredrev, closeadj):
    base = (_std(_f28_pipeline_growth(deferredrev, 252), 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_std252_jerk_v063_signal(deferredrev, closeadj):
    base = (_std(_f28_pipeline_growth(deferredrev, 504), 126)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_z252_jerk_v064_signal(deferredrev, closeadj):
    base = (_z(_f28_pipeline_growth(deferredrev, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_z504_jerk_v065_signal(deferredrev, closeadj):
    base = (_z(_f28_pipeline_growth(deferredrev, 252), 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ema21_jerk_v066_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ema63_jerk_v067_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_ema126_jerk_v068_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252).ewm(span=126, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_rank252_jerk_v069_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_rank504_jerk_v070_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_abs63_jerk_v071_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_abs252_jerk_v072_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_sq63_jerk_v073_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * _f28_pipeline_growth(deferredrev, 63).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_sq252_jerk_v074_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * _f28_pipeline_growth(deferredrev, 252).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xlogpx_63_jerk_v075_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xlogpx_252_jerk_v076_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpxgap_63_jerk_v077_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * (closeadj - _mean(closeadj, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpxgap_252_jerk_v078_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpxdet_252_jerk_v079_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpkgap_252_jerk_v080_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xrange_252_jerk_v081_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xstd_63_jerk_v082_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * _std(closeadj, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xstd_252_jerk_v083_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xvolz_252_jerk_v084_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpxchg_63_jerk_v085_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xpxchg_252_jerk_v086_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * closeadj.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_diff63_jerk_v087_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63).diff(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_diff252_jerk_v088_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252).diff(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_dev252_jerk_v089_signal(deferredrev, closeadj):
    base = ((_f28_pipeline_growth(deferredrev, 252) - _mean(_f28_pipeline_growth(deferredrev, 252), 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_var252_jerk_v090_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xlogdr_252_jerk_v091_signal(deferredrev, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_x_revg_252_jerk_v092_signal(deferredrev, revenue, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_x_revg_63_jerk_v093_signal(deferredrev, revenue, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * revenue.pct_change(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_x_bproxy_jerk_v094_signal(deferredrev, revenue, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * _f28_backlog_proxy(deferredrev, revenue)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_x_bconsum_jerk_v095_signal(deferredrev, revenue, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 63) * _f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_logema_63_jerk_v096_signal(deferredrev, closeadj):
    base = (np.log(_f28_pipeline_growth(deferredrev, 63).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_minus_bconsum_jerk_v097_signal(deferredrev, revenue, closeadj):
    base = ((_f28_pipeline_growth(deferredrev, 63) - _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_plus_bconsum_jerk_v098_signal(deferredrev, revenue, closeadj):
    base = ((_f28_pipeline_growth(deferredrev, 252) + _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_xlogrev_252_jerk_v099_signal(deferredrev, revenue, closeadj):
    base = (_f28_pipeline_growth(deferredrev, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_pgrowth_sign_63_jerk_v100_signal(deferredrev, closeadj):
    base = (np.sign(_f28_pipeline_growth(deferredrev, 63)) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_21_jerk_v101_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_63_jerk_v102_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_126_jerk_v103_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_252_jerk_v104_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_504_jerk_v105_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_5_jerk_v106_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 5)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_42_jerk_v107_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 42)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_189_jerk_v108_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 189)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_ma21_jerk_v109_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_consumption(deferredrev, revenue, 63), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_ma63_jerk_v110_signal(deferredrev, revenue, closeadj):
    base = (_mean(_f28_backlog_consumption(deferredrev, revenue, 252), 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_std63_jerk_v111_signal(deferredrev, revenue, closeadj):
    base = (_std(_f28_backlog_consumption(deferredrev, revenue, 252), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_std252_jerk_v112_signal(deferredrev, revenue, closeadj):
    base = (_std(_f28_backlog_consumption(deferredrev, revenue, 504), 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_z252_jerk_v113_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_consumption(deferredrev, revenue, 63), 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_z504_jerk_v114_signal(deferredrev, revenue, closeadj):
    base = (_z(_f28_backlog_consumption(deferredrev, revenue, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_ema21_jerk_v115_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_ema63_jerk_v116_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_rank252_jerk_v117_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_rank504_jerk_v118_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_abs63_jerk_v119_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_abs252_jerk_v120_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_sq63_jerk_v121_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * _f28_backlog_consumption(deferredrev, revenue, 63).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_sq252_jerk_v122_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * _f28_backlog_consumption(deferredrev, revenue, 252).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xlogpx_63_jerk_v123_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xlogpx_252_jerk_v124_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpxgap_63_jerk_v125_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * (closeadj - _mean(closeadj, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpxgap_252_jerk_v126_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpxdet_252_jerk_v127_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpkgap_252_jerk_v128_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xrange_252_jerk_v129_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xstd_63_jerk_v130_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * _std(closeadj, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xstd_252_jerk_v131_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xvolz_252_jerk_v132_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpxchg_63_jerk_v133_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xpxchg_252_jerk_v134_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * closeadj.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_diff63_jerk_v135_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63).diff(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_diff252_jerk_v136_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252).diff(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_dev252_jerk_v137_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_consumption(deferredrev, revenue, 252) - _mean(_f28_backlog_consumption(deferredrev, revenue, 252), 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_var252_jerk_v138_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xlogdr_252_jerk_v139_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_xlogrev_252_jerk_v140_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_x_revg_252_jerk_v141_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 252) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_logema_63_jerk_v142_signal(deferredrev, revenue, closeadj):
    base = (np.log(_f28_backlog_consumption(deferredrev, revenue, 63).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_x_bproxy_jerk_v143_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * _f28_backlog_proxy(deferredrev, revenue)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_x_pgrowth_jerk_v144_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_consumption(deferredrev, revenue, 63) * _f28_pipeline_growth(deferredrev, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bconsum_sign_63_jerk_v145_signal(deferredrev, revenue, closeadj):
    base = (np.sign(_f28_backlog_consumption(deferredrev, revenue, 63)) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_compo_all_252_jerk_v146_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 252) + _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_compow_all_252_jerk_v147_signal(deferredrev, revenue, closeadj):
    base = ((0.5 * _f28_backlog_proxy(deferredrev, revenue) + 0.3 * _f28_pipeline_growth(deferredrev, 252) + 0.2 * _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_compo_all_63_jerk_v148_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 63) + _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_minus_bconsum_252_jerk_v149_signal(deferredrev, revenue, closeadj):
    base = ((_f28_backlog_proxy(deferredrev, revenue) - _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_engineering_construction_backlog_bproxy_x_bconsum_log_jerk_v150_signal(deferredrev, revenue, closeadj):
    base = (_f28_backlog_proxy(deferredrev, revenue) * np.log(_f28_backlog_consumption(deferredrev, revenue, 63).abs() + 1.0)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28ecb_engineering_construction_backlog_bproxy_basic_jerk_v001_signal,
    f28ecb_engineering_construction_backlog_bproxy_ma21_jerk_v002_signal,
    f28ecb_engineering_construction_backlog_bproxy_ma63_jerk_v003_signal,
    f28ecb_engineering_construction_backlog_bproxy_ma126_jerk_v004_signal,
    f28ecb_engineering_construction_backlog_bproxy_ma252_jerk_v005_signal,
    f28ecb_engineering_construction_backlog_bproxy_std21_jerk_v006_signal,
    f28ecb_engineering_construction_backlog_bproxy_std63_jerk_v007_signal,
    f28ecb_engineering_construction_backlog_bproxy_std252_jerk_v008_signal,
    f28ecb_engineering_construction_backlog_bproxy_z252_jerk_v009_signal,
    f28ecb_engineering_construction_backlog_bproxy_z504_jerk_v010_signal,
    f28ecb_engineering_construction_backlog_bproxy_ema21_jerk_v011_signal,
    f28ecb_engineering_construction_backlog_bproxy_ema63_jerk_v012_signal,
    f28ecb_engineering_construction_backlog_bproxy_ema252_jerk_v013_signal,
    f28ecb_engineering_construction_backlog_bproxy_rank252_jerk_v014_signal,
    f28ecb_engineering_construction_backlog_bproxy_rank504_jerk_v015_signal,
    f28ecb_engineering_construction_backlog_bproxy_abs_jerk_v016_signal,
    f28ecb_engineering_construction_backlog_bproxy_sq_jerk_v017_signal,
    f28ecb_engineering_construction_backlog_bproxy_xlogrev_jerk_v018_signal,
    f28ecb_engineering_construction_backlog_bproxy_xlogpx_252_jerk_v019_signal,
    f28ecb_engineering_construction_backlog_bproxy_xpxgap_252_jerk_v020_signal,
    f28ecb_engineering_construction_backlog_bproxy_xpxdet_252_jerk_v021_signal,
    f28ecb_engineering_construction_backlog_bproxy_xpkgap_252_jerk_v022_signal,
    f28ecb_engineering_construction_backlog_bproxy_xrange_252_jerk_v023_signal,
    f28ecb_engineering_construction_backlog_bproxy_xstd_252_jerk_v024_signal,
    f28ecb_engineering_construction_backlog_bproxy_xvolz_252_jerk_v025_signal,
    f28ecb_engineering_construction_backlog_bproxy_xrevg_252_jerk_v026_signal,
    f28ecb_engineering_construction_backlog_bproxy_xpxchg_63_jerk_v027_signal,
    f28ecb_engineering_construction_backlog_bproxy_xpxchg_252_jerk_v028_signal,
    f28ecb_engineering_construction_backlog_bproxy_xlogdr_jerk_v029_signal,
    f28ecb_engineering_construction_backlog_bproxy_diff_63_jerk_v030_signal,
    f28ecb_engineering_construction_backlog_bproxy_diff_252_jerk_v031_signal,
    f28ecb_engineering_construction_backlog_bproxy_dev_252_jerk_v032_signal,
    f28ecb_engineering_construction_backlog_bproxy_dev_504_jerk_v033_signal,
    f28ecb_engineering_construction_backlog_bproxy_var_63_jerk_v034_signal,
    f28ecb_engineering_construction_backlog_bproxy_var_252_jerk_v035_signal,
    f28ecb_engineering_construction_backlog_bproxy_zema_252_jerk_v036_signal,
    f28ecb_engineering_construction_backlog_bproxy_zema_504_jerk_v037_signal,
    f28ecb_engineering_construction_backlog_bproxy_inv_jerk_v038_signal,
    f28ecb_engineering_construction_backlog_bproxy_sign_jerk_v039_signal,
    f28ecb_engineering_construction_backlog_bproxy_xebmgn_jerk_v040_signal,
    f28ecb_engineering_construction_backlog_bproxy_xebmgn252_jerk_v041_signal,
    f28ecb_engineering_construction_backlog_bproxy_logema_63_jerk_v042_signal,
    f28ecb_engineering_construction_backlog_bproxy_x_pgrowth_jerk_v043_signal,
    f28ecb_engineering_construction_backlog_bproxy_x_pgrowth252_jerk_v044_signal,
    f28ecb_engineering_construction_backlog_bproxy_x_bconsum_jerk_v045_signal,
    f28ecb_engineering_construction_backlog_bproxy_x_bconsum252_jerk_v046_signal,
    f28ecb_engineering_construction_backlog_bproxy_plus_pgrowth_jerk_v047_signal,
    f28ecb_engineering_construction_backlog_bproxy_minus_pgrowth_jerk_v048_signal,
    f28ecb_engineering_construction_backlog_bproxy_minus_bconsum_jerk_v049_signal,
    f28ecb_engineering_construction_backlog_bproxy_plus_bconsum_jerk_v050_signal,
    f28ecb_engineering_construction_backlog_pgrowth_21_jerk_v051_signal,
    f28ecb_engineering_construction_backlog_pgrowth_63_jerk_v052_signal,
    f28ecb_engineering_construction_backlog_pgrowth_126_jerk_v053_signal,
    f28ecb_engineering_construction_backlog_pgrowth_252_jerk_v054_signal,
    f28ecb_engineering_construction_backlog_pgrowth_504_jerk_v055_signal,
    f28ecb_engineering_construction_backlog_pgrowth_5_jerk_v056_signal,
    f28ecb_engineering_construction_backlog_pgrowth_42_jerk_v057_signal,
    f28ecb_engineering_construction_backlog_pgrowth_189_jerk_v058_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ma21_jerk_v059_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ma63_jerk_v060_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ma126_jerk_v061_signal,
    f28ecb_engineering_construction_backlog_pgrowth_std63_jerk_v062_signal,
    f28ecb_engineering_construction_backlog_pgrowth_std252_jerk_v063_signal,
    f28ecb_engineering_construction_backlog_pgrowth_z252_jerk_v064_signal,
    f28ecb_engineering_construction_backlog_pgrowth_z504_jerk_v065_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ema21_jerk_v066_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ema63_jerk_v067_signal,
    f28ecb_engineering_construction_backlog_pgrowth_ema126_jerk_v068_signal,
    f28ecb_engineering_construction_backlog_pgrowth_rank252_jerk_v069_signal,
    f28ecb_engineering_construction_backlog_pgrowth_rank504_jerk_v070_signal,
    f28ecb_engineering_construction_backlog_pgrowth_abs63_jerk_v071_signal,
    f28ecb_engineering_construction_backlog_pgrowth_abs252_jerk_v072_signal,
    f28ecb_engineering_construction_backlog_pgrowth_sq63_jerk_v073_signal,
    f28ecb_engineering_construction_backlog_pgrowth_sq252_jerk_v074_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xlogpx_63_jerk_v075_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xlogpx_252_jerk_v076_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpxgap_63_jerk_v077_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpxgap_252_jerk_v078_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpxdet_252_jerk_v079_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpkgap_252_jerk_v080_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xrange_252_jerk_v081_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xstd_63_jerk_v082_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xstd_252_jerk_v083_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xvolz_252_jerk_v084_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpxchg_63_jerk_v085_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xpxchg_252_jerk_v086_signal,
    f28ecb_engineering_construction_backlog_pgrowth_diff63_jerk_v087_signal,
    f28ecb_engineering_construction_backlog_pgrowth_diff252_jerk_v088_signal,
    f28ecb_engineering_construction_backlog_pgrowth_dev252_jerk_v089_signal,
    f28ecb_engineering_construction_backlog_pgrowth_var252_jerk_v090_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xlogdr_252_jerk_v091_signal,
    f28ecb_engineering_construction_backlog_pgrowth_x_revg_252_jerk_v092_signal,
    f28ecb_engineering_construction_backlog_pgrowth_x_revg_63_jerk_v093_signal,
    f28ecb_engineering_construction_backlog_pgrowth_x_bproxy_jerk_v094_signal,
    f28ecb_engineering_construction_backlog_pgrowth_x_bconsum_jerk_v095_signal,
    f28ecb_engineering_construction_backlog_pgrowth_logema_63_jerk_v096_signal,
    f28ecb_engineering_construction_backlog_pgrowth_minus_bconsum_jerk_v097_signal,
    f28ecb_engineering_construction_backlog_pgrowth_plus_bconsum_jerk_v098_signal,
    f28ecb_engineering_construction_backlog_pgrowth_xlogrev_252_jerk_v099_signal,
    f28ecb_engineering_construction_backlog_pgrowth_sign_63_jerk_v100_signal,
    f28ecb_engineering_construction_backlog_bconsum_21_jerk_v101_signal,
    f28ecb_engineering_construction_backlog_bconsum_63_jerk_v102_signal,
    f28ecb_engineering_construction_backlog_bconsum_126_jerk_v103_signal,
    f28ecb_engineering_construction_backlog_bconsum_252_jerk_v104_signal,
    f28ecb_engineering_construction_backlog_bconsum_504_jerk_v105_signal,
    f28ecb_engineering_construction_backlog_bconsum_5_jerk_v106_signal,
    f28ecb_engineering_construction_backlog_bconsum_42_jerk_v107_signal,
    f28ecb_engineering_construction_backlog_bconsum_189_jerk_v108_signal,
    f28ecb_engineering_construction_backlog_bconsum_ma21_jerk_v109_signal,
    f28ecb_engineering_construction_backlog_bconsum_ma63_jerk_v110_signal,
    f28ecb_engineering_construction_backlog_bconsum_std63_jerk_v111_signal,
    f28ecb_engineering_construction_backlog_bconsum_std252_jerk_v112_signal,
    f28ecb_engineering_construction_backlog_bconsum_z252_jerk_v113_signal,
    f28ecb_engineering_construction_backlog_bconsum_z504_jerk_v114_signal,
    f28ecb_engineering_construction_backlog_bconsum_ema21_jerk_v115_signal,
    f28ecb_engineering_construction_backlog_bconsum_ema63_jerk_v116_signal,
    f28ecb_engineering_construction_backlog_bconsum_rank252_jerk_v117_signal,
    f28ecb_engineering_construction_backlog_bconsum_rank504_jerk_v118_signal,
    f28ecb_engineering_construction_backlog_bconsum_abs63_jerk_v119_signal,
    f28ecb_engineering_construction_backlog_bconsum_abs252_jerk_v120_signal,
    f28ecb_engineering_construction_backlog_bconsum_sq63_jerk_v121_signal,
    f28ecb_engineering_construction_backlog_bconsum_sq252_jerk_v122_signal,
    f28ecb_engineering_construction_backlog_bconsum_xlogpx_63_jerk_v123_signal,
    f28ecb_engineering_construction_backlog_bconsum_xlogpx_252_jerk_v124_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpxgap_63_jerk_v125_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpxgap_252_jerk_v126_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpxdet_252_jerk_v127_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpkgap_252_jerk_v128_signal,
    f28ecb_engineering_construction_backlog_bconsum_xrange_252_jerk_v129_signal,
    f28ecb_engineering_construction_backlog_bconsum_xstd_63_jerk_v130_signal,
    f28ecb_engineering_construction_backlog_bconsum_xstd_252_jerk_v131_signal,
    f28ecb_engineering_construction_backlog_bconsum_xvolz_252_jerk_v132_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpxchg_63_jerk_v133_signal,
    f28ecb_engineering_construction_backlog_bconsum_xpxchg_252_jerk_v134_signal,
    f28ecb_engineering_construction_backlog_bconsum_diff63_jerk_v135_signal,
    f28ecb_engineering_construction_backlog_bconsum_diff252_jerk_v136_signal,
    f28ecb_engineering_construction_backlog_bconsum_dev252_jerk_v137_signal,
    f28ecb_engineering_construction_backlog_bconsum_var252_jerk_v138_signal,
    f28ecb_engineering_construction_backlog_bconsum_xlogdr_252_jerk_v139_signal,
    f28ecb_engineering_construction_backlog_bconsum_xlogrev_252_jerk_v140_signal,
    f28ecb_engineering_construction_backlog_bconsum_x_revg_252_jerk_v141_signal,
    f28ecb_engineering_construction_backlog_bconsum_logema_63_jerk_v142_signal,
    f28ecb_engineering_construction_backlog_bconsum_x_bproxy_jerk_v143_signal,
    f28ecb_engineering_construction_backlog_bconsum_x_pgrowth_jerk_v144_signal,
    f28ecb_engineering_construction_backlog_bconsum_sign_63_jerk_v145_signal,
    f28ecb_engineering_construction_backlog_compo_all_252_jerk_v146_signal,
    f28ecb_engineering_construction_backlog_compow_all_252_jerk_v147_signal,
    f28ecb_engineering_construction_backlog_compo_all_63_jerk_v148_signal,
    f28ecb_engineering_construction_backlog_bproxy_minus_bconsum_252_jerk_v149_signal,
    f28ecb_engineering_construction_backlog_bproxy_x_bconsum_log_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_ENGINEERING_CONSTRUCTION_BACKLOG_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_engineering_construction_backlog_3rd_derivatives_001_150_claude: {n_features} features pass")
