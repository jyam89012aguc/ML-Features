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
def _f27_revenue_floor(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).min()


def _f27_non_cyclical_share_proxy(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / m.replace(0, np.nan)


def _f27_durability_score(revenue, ebitdamargin, w):
    rsd = revenue.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    msd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / ((rsd.replace(0, np.nan) + 1e-6) * (msd.replace(0, np.nan) + 1e-6))


def _f27_revenue_floor_norm(revenue, w):
    return _f27_revenue_floor(revenue, w) / revenue.replace(0, np.nan)


def _f27_non_cyclical_share_proxy_v(revenue, w):
    return _f27_non_cyclical_share_proxy(revenue, w)


def _f27_durability_score_log(revenue, ebitdamargin, w):
    return np.log(_f27_durability_score(revenue, ebitdamargin, w).replace(0, np.nan).abs() + 1.0)


# === Floor jerks (v001-v050) ===
def f27rrd_f27_repair_remodel_durability_floor_21d_jerk_v001_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_21d_jerk_v002_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_63d_jerk_v003_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_63d_jerk_v004_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_126d_jerk_v005_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_126d_jerk_v006_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_252d_jerk_v007_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_252d_jerk_v008_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_504d_jerk_v009_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_42d_jerk_v010_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_189d_jerk_v011_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_378d_jerk_v012_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorma_63d_jerk_v013_signal(revenue, closeadj):
    base = _mean(_f27_revenue_floor_norm(revenue, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorma_252d_jerk_v014_signal(revenue, closeadj):
    base = _mean(_f27_revenue_floor_norm(revenue, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorstd_63d_jerk_v015_signal(revenue, closeadj):
    base = _std(_f27_revenue_floor_norm(revenue, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorstd_252d_jerk_v016_signal(revenue, closeadj):
    base = _std(_f27_revenue_floor_norm(revenue, 504), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorz_63d_jerk_v017_signal(revenue, closeadj):
    base = _z(_f27_revenue_floor_norm(revenue, 252), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorz_252d_jerk_v018_signal(revenue, closeadj):
    base = _z(_f27_revenue_floor_norm(revenue, 504), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorlog_63d_jerk_v019_signal(revenue, closeadj):
    base = np.log(_f27_revenue_floor(revenue, 63).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorlog_252d_jerk_v020_signal(revenue, closeadj):
    base = np.log(_f27_revenue_floor(revenue, 252).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floordiff_21d_jerk_v021_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 63).diff(21) / revenue.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floordiff_63d_jerk_v022_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 252).diff(63) / revenue.replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorema_21d_jerk_v023_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorema_63d_jerk_v024_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorrank_252d_jerk_v025_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorrank_504d_jerk_v026_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorsq_63d_jerk_v027_signal(revenue, closeadj):
    f = _f27_revenue_floor_norm(revenue, 63)
    base = f * f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxebmgn_63d_jerk_v028_signal(revenue, ebitdamargin, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63) * ebitdamargin * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxebmgn_252d_jerk_v029_signal(revenue, ebitdamargin, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * ebitdamargin * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxpx_63d_jerk_v030_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63) * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logclose_63d_jerk_v031_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logclose_252d_jerk_v032_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxpkgap_252d_jerk_v033_signal(revenue, closeadj):
    f = _f27_revenue_floor_norm(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    base = f * gap * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxpxdet_252d_jerk_v034_signal(revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    base = _f27_revenue_floor_norm(revenue, 252) * det * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxrange_252d_jerk_v035_signal(revenue, closeadj):
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    base = _f27_revenue_floor_norm(revenue, 252) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxstd_252d_jerk_v036_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * _std(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorinv_63d_jerk_v037_signal(revenue, closeadj):
    base = (1.0 - _f27_revenue_floor_norm(revenue, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_pxratio_252d_jerk_v038_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_minusmean_63d_jerk_v039_signal(revenue, closeadj):
    f = _f27_revenue_floor_norm(revenue, 63)
    base = (f - _mean(f, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxvolz_252d_jerk_v040_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * _z(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_revchg_252d_jerk_v041_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * revenue.pct_change(252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_ebmgnchg_63d_jerk_v042_signal(revenue, ebitdamargin, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63) * ebitdamargin.diff(63) * closeadj * 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorvar_63d_jerk_v043_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63).rolling(63, min_periods=21).var() * closeadj * 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxlogrev_252d_jerk_v044_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_sigxclose_252d_jerk_v045_signal(revenue, closeadj):
    base = np.sign(_f27_revenue_floor_norm(revenue, 252) - 0.5) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_5d_jerk_v046_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_10d_jerk_v047_signal(revenue, closeadj):
    result = _jerk(_f27_revenue_floor_norm(revenue, 10) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logemamean_63d_jerk_v048_signal(revenue, closeadj):
    base = np.log(_f27_revenue_floor_norm(revenue, 63).replace(0, np.nan).abs() + 1.0).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_dur_252d_jerk_v049_signal(revenue, ebitdamargin, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * _f27_durability_score_log(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_share_63d_jerk_v050_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 63) * _f27_non_cyclical_share_proxy_v(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# === Share jerks (v051-v100) ===
def f27rrd_f27_repair_remodel_durability_share_21d_jerk_v051_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_63d_jerk_v052_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_63d_jerk_v053_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_126d_jerk_v054_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_252d_jerk_v055_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_252d_jerk_v056_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_504d_jerk_v057_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_42d_jerk_v058_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_189d_jerk_v059_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_378d_jerk_v060_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharema_21d_jerk_v061_signal(revenue, closeadj):
    base = _mean(_f27_non_cyclical_share_proxy_v(revenue, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharema_63d_jerk_v062_signal(revenue, closeadj):
    base = _mean(_f27_non_cyclical_share_proxy_v(revenue, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharestd_63d_jerk_v063_signal(revenue, closeadj):
    base = _std(_f27_non_cyclical_share_proxy_v(revenue, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharestd_252d_jerk_v064_signal(revenue, closeadj):
    base = _std(_f27_non_cyclical_share_proxy_v(revenue, 504), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharez_63d_jerk_v065_signal(revenue, closeadj):
    base = _z(_f27_non_cyclical_share_proxy_v(revenue, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharez_252d_jerk_v066_signal(revenue, closeadj):
    base = _z(_f27_non_cyclical_share_proxy_v(revenue, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharediff_21d_jerk_v067_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63).diff(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharediff_63d_jerk_v068_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252).diff(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareema_21d_jerk_v069_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareema_63d_jerk_v070_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharerank_252d_jerk_v071_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharerank_504d_jerk_v072_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharesq_63d_jerk_v073_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy_v(revenue, 63)
    base = s * s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexebmgn_63d_jerk_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * ebitdamargin * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexebmgn_252d_jerk_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * ebitdamargin * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexpx_63d_jerk_v076_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_logclose_63d_jerk_v077_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexpkgap_252d_jerk_v078_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy_v(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    base = s * gap * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexrange_252d_jerk_v079_signal(revenue, closeadj):
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexstd_252d_jerk_v080_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * _std(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareinv_252d_jerk_v081_signal(revenue, closeadj):
    base = (1.0 - _f27_non_cyclical_share_proxy_v(revenue, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_pxratio_252d_jerk_v082_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_minusmean_252d_jerk_v083_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy_v(revenue, 252)
    base = (s - _mean(s, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexvolz_252d_jerk_v084_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * _z(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_revchg_63d_jerk_v085_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * revenue.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_ebmgnchg_63d_jerk_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * ebitdamargin.diff(63) * closeadj * 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharevar_252d_jerk_v087_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252).rolling(252, min_periods=63).var() * closeadj * 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexlogrev_252d_jerk_v088_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_sigxclose_252d_jerk_v089_signal(revenue, closeadj):
    base = np.sign(_f27_non_cyclical_share_proxy_v(revenue, 252) - 0.5) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_5d_jerk_v090_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_10d_jerk_v091_signal(revenue, closeadj):
    result = _jerk(_f27_non_cyclical_share_proxy_v(revenue, 10) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_logemamean_63d_jerk_v092_signal(revenue, closeadj):
    base = np.log(_f27_non_cyclical_share_proxy_v(revenue, 63).replace(0, np.nan).abs() + 1.0).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_dur_252d_jerk_v093_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * _f27_durability_score_log(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_pxdet_252d_jerk_v094_signal(revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * det * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_pxgap_63d_jerk_v095_signal(revenue, closeadj):
    px_gap = closeadj - _mean(closeadj, 63)
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * px_gap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexebmgnma_63d_jerk_v096_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_zema_252d_jerk_v097_signal(revenue, closeadj):
    base = _z(_f27_non_cyclical_share_proxy_v(revenue, 504), 504).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_x_logclose_63d_jerk_v098_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_x_share_252d_jerk_v099_signal(revenue, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * _f27_non_cyclical_share_proxy_v(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorinv_x_share_63d_jerk_v100_signal(revenue, closeadj):
    base = (1.0 - _f27_revenue_floor_norm(revenue, 63)) * _f27_non_cyclical_share_proxy_v(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# === Durability jerks (v101-v150) ===
def f27rrd_f27_repair_remodel_durability_dur_21d_jerk_v101_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_63d_jerk_v102_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_63d_jerk_v103_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_126d_jerk_v104_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_252d_jerk_v105_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_252d_jerk_v106_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_504d_jerk_v107_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_42d_jerk_v108_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_189d_jerk_v109_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_378d_jerk_v110_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durma_63d_jerk_v111_signal(revenue, ebitdamargin, closeadj):
    base = _mean(_f27_durability_score_log(revenue, ebitdamargin, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durma_252d_jerk_v112_signal(revenue, ebitdamargin, closeadj):
    base = _mean(_f27_durability_score_log(revenue, ebitdamargin, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durstd_252d_jerk_v113_signal(revenue, ebitdamargin, closeadj):
    base = _std(_f27_durability_score_log(revenue, ebitdamargin, 252), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durz_63d_jerk_v114_signal(revenue, ebitdamargin, closeadj):
    base = _z(_f27_durability_score_log(revenue, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durz_252d_jerk_v115_signal(revenue, ebitdamargin, closeadj):
    base = _z(_f27_durability_score_log(revenue, ebitdamargin, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durema_63d_jerk_v116_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durema_126d_jerk_v117_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durrank_252d_jerk_v118_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durrank_504d_jerk_v119_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durdiff_63d_jerk_v120_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63).diff(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durdiff_252d_jerk_v121_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252).diff(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxpx_63d_jerk_v122_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63) * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxlogclose_252d_jerk_v123_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxpxgap_252d_jerk_v124_signal(revenue, ebitdamargin, closeadj):
    px_gap = closeadj - _mean(closeadj, 252)
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * px_gap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxrange_252d_jerk_v125_signal(revenue, ebitdamargin, closeadj):
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * rng
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxstd_252d_jerk_v126_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * _std(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durvslog_252d_jerk_v127_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_minusmean_252d_jerk_v128_signal(revenue, ebitdamargin, closeadj):
    d = _f27_durability_score_log(revenue, ebitdamargin, 252)
    base = (d - _mean(d, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_volz_63d_jerk_v129_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 63) * _z(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_revchg_252d_jerk_v130_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * revenue.pct_change(252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_ebmgnchg_252d_jerk_v131_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * ebitdamargin.diff(252) * closeadj * 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_pxratio_252d_jerk_v132_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_zema_252d_jerk_v133_signal(revenue, ebitdamargin, closeadj):
    base = _z(_f27_durability_score_log(revenue, ebitdamargin, 252), 504).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_floor_252d_jerk_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * _f27_revenue_floor_norm(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_share_252d_jerk_v135_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score_log(revenue, ebitdamargin, 252) * _f27_non_cyclical_share_proxy_v(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_share_dur_252d_jerk_v136_signal(revenue, ebitdamargin, closeadj):
    base = (_f27_revenue_floor_norm(revenue, 252) + _f27_non_cyclical_share_proxy_v(revenue, 252) + _f27_durability_score_log(revenue, ebitdamargin, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_minusshare_63d_jerk_v137_signal(revenue, closeadj):
    base = (_f27_revenue_floor_norm(revenue, 63) - _f27_non_cyclical_share_proxy_v(revenue, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_plusshare_252d_jerk_v138_signal(revenue, closeadj):
    base = (_f27_revenue_floor_norm(revenue, 252) + _f27_non_cyclical_share_proxy_v(revenue, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_compow2_252d_jerk_v139_signal(revenue, ebitdamargin, closeadj):
    base = (0.4 * _f27_revenue_floor_norm(revenue, 252) + 0.4 * _f27_non_cyclical_share_proxy_v(revenue, 252) + 0.2 * _f27_durability_score_log(revenue, ebitdamargin, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_x_durz_252d_jerk_v140_signal(revenue, ebitdamargin, closeadj):
    base = _f27_revenue_floor_norm(revenue, 252) * _z(_f27_durability_score_log(revenue, ebitdamargin, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_x_durz_252d_jerk_v141_signal(revenue, ebitdamargin, closeadj):
    base = _f27_non_cyclical_share_proxy_v(revenue, 252) * _z(_f27_durability_score_log(revenue, ebitdamargin, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_5d_jerk_v142_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_10d_jerk_v143_signal(revenue, ebitdamargin, closeadj):
    result = _jerk(_f27_durability_score_log(revenue, ebitdamargin, 10) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_dur_minus_252d_jerk_v144_signal(revenue, ebitdamargin, closeadj):
    base = (_f27_revenue_floor_norm(revenue, 252) - _mean(_f27_durability_score_log(revenue, ebitdamargin, 252), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_dur_minus_252d_jerk_v145_signal(revenue, ebitdamargin, closeadj):
    base = (_f27_non_cyclical_share_proxy_v(revenue, 252) - _mean(_f27_durability_score_log(revenue, ebitdamargin, 252), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logminus_252d_jerk_v146_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252)
    base = (np.log(revenue.replace(0, np.nan).abs() + 1.0) - np.log(f.replace(0, np.nan).abs() + 1.0)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexshareratio_63d_jerk_v147_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor_norm(revenue, 63)
    s = _f27_non_cyclical_share_proxy_v(revenue, 63)
    base = f / s.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_sharediff_252d_jerk_v148_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy_v(revenue, 252)
    base = (_f27_revenue_floor_norm(revenue, 252) - s.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durmean_63d_jerk_v149_signal(revenue, ebitdamargin, closeadj):
    base = _mean(_f27_durability_score_log(revenue, ebitdamargin, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durstd_63d_jerk_v150_signal(revenue, ebitdamargin, closeadj):
    base = _std(_f27_durability_score_log(revenue, ebitdamargin, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27rrd_f27_repair_remodel_durability_floor_21d_jerk_v001_signal,
    f27rrd_f27_repair_remodel_durability_floor_21d_jerk_v002_signal,
    f27rrd_f27_repair_remodel_durability_floor_63d_jerk_v003_signal,
    f27rrd_f27_repair_remodel_durability_floor_63d_jerk_v004_signal,
    f27rrd_f27_repair_remodel_durability_floor_126d_jerk_v005_signal,
    f27rrd_f27_repair_remodel_durability_floor_126d_jerk_v006_signal,
    f27rrd_f27_repair_remodel_durability_floor_252d_jerk_v007_signal,
    f27rrd_f27_repair_remodel_durability_floor_252d_jerk_v008_signal,
    f27rrd_f27_repair_remodel_durability_floor_504d_jerk_v009_signal,
    f27rrd_f27_repair_remodel_durability_floor_42d_jerk_v010_signal,
    f27rrd_f27_repair_remodel_durability_floor_189d_jerk_v011_signal,
    f27rrd_f27_repair_remodel_durability_floor_378d_jerk_v012_signal,
    f27rrd_f27_repair_remodel_durability_floorma_63d_jerk_v013_signal,
    f27rrd_f27_repair_remodel_durability_floorma_252d_jerk_v014_signal,
    f27rrd_f27_repair_remodel_durability_floorstd_63d_jerk_v015_signal,
    f27rrd_f27_repair_remodel_durability_floorstd_252d_jerk_v016_signal,
    f27rrd_f27_repair_remodel_durability_floorz_63d_jerk_v017_signal,
    f27rrd_f27_repair_remodel_durability_floorz_252d_jerk_v018_signal,
    f27rrd_f27_repair_remodel_durability_floorlog_63d_jerk_v019_signal,
    f27rrd_f27_repair_remodel_durability_floorlog_252d_jerk_v020_signal,
    f27rrd_f27_repair_remodel_durability_floordiff_21d_jerk_v021_signal,
    f27rrd_f27_repair_remodel_durability_floordiff_63d_jerk_v022_signal,
    f27rrd_f27_repair_remodel_durability_floorema_21d_jerk_v023_signal,
    f27rrd_f27_repair_remodel_durability_floorema_63d_jerk_v024_signal,
    f27rrd_f27_repair_remodel_durability_floorrank_252d_jerk_v025_signal,
    f27rrd_f27_repair_remodel_durability_floorrank_504d_jerk_v026_signal,
    f27rrd_f27_repair_remodel_durability_floorsq_63d_jerk_v027_signal,
    f27rrd_f27_repair_remodel_durability_floorxebmgn_63d_jerk_v028_signal,
    f27rrd_f27_repair_remodel_durability_floorxebmgn_252d_jerk_v029_signal,
    f27rrd_f27_repair_remodel_durability_floorxpx_63d_jerk_v030_signal,
    f27rrd_f27_repair_remodel_durability_floor_logclose_63d_jerk_v031_signal,
    f27rrd_f27_repair_remodel_durability_floor_logclose_252d_jerk_v032_signal,
    f27rrd_f27_repair_remodel_durability_floorxpkgap_252d_jerk_v033_signal,
    f27rrd_f27_repair_remodel_durability_floorxpxdet_252d_jerk_v034_signal,
    f27rrd_f27_repair_remodel_durability_floorxrange_252d_jerk_v035_signal,
    f27rrd_f27_repair_remodel_durability_floorxstd_252d_jerk_v036_signal,
    f27rrd_f27_repair_remodel_durability_floorinv_63d_jerk_v037_signal,
    f27rrd_f27_repair_remodel_durability_floor_pxratio_252d_jerk_v038_signal,
    f27rrd_f27_repair_remodel_durability_floor_minusmean_63d_jerk_v039_signal,
    f27rrd_f27_repair_remodel_durability_floorxvolz_252d_jerk_v040_signal,
    f27rrd_f27_repair_remodel_durability_floor_revchg_252d_jerk_v041_signal,
    f27rrd_f27_repair_remodel_durability_floor_ebmgnchg_63d_jerk_v042_signal,
    f27rrd_f27_repair_remodel_durability_floorvar_63d_jerk_v043_signal,
    f27rrd_f27_repair_remodel_durability_floorxlogrev_252d_jerk_v044_signal,
    f27rrd_f27_repair_remodel_durability_floor_sigxclose_252d_jerk_v045_signal,
    f27rrd_f27_repair_remodel_durability_floor_5d_jerk_v046_signal,
    f27rrd_f27_repair_remodel_durability_floor_10d_jerk_v047_signal,
    f27rrd_f27_repair_remodel_durability_floor_logemamean_63d_jerk_v048_signal,
    f27rrd_f27_repair_remodel_durability_floor_dur_252d_jerk_v049_signal,
    f27rrd_f27_repair_remodel_durability_floor_share_63d_jerk_v050_signal,
    f27rrd_f27_repair_remodel_durability_share_21d_jerk_v051_signal,
    f27rrd_f27_repair_remodel_durability_share_63d_jerk_v052_signal,
    f27rrd_f27_repair_remodel_durability_share_63d_jerk_v053_signal,
    f27rrd_f27_repair_remodel_durability_share_126d_jerk_v054_signal,
    f27rrd_f27_repair_remodel_durability_share_252d_jerk_v055_signal,
    f27rrd_f27_repair_remodel_durability_share_252d_jerk_v056_signal,
    f27rrd_f27_repair_remodel_durability_share_504d_jerk_v057_signal,
    f27rrd_f27_repair_remodel_durability_share_42d_jerk_v058_signal,
    f27rrd_f27_repair_remodel_durability_share_189d_jerk_v059_signal,
    f27rrd_f27_repair_remodel_durability_share_378d_jerk_v060_signal,
    f27rrd_f27_repair_remodel_durability_sharema_21d_jerk_v061_signal,
    f27rrd_f27_repair_remodel_durability_sharema_63d_jerk_v062_signal,
    f27rrd_f27_repair_remodel_durability_sharestd_63d_jerk_v063_signal,
    f27rrd_f27_repair_remodel_durability_sharestd_252d_jerk_v064_signal,
    f27rrd_f27_repair_remodel_durability_sharez_63d_jerk_v065_signal,
    f27rrd_f27_repair_remodel_durability_sharez_252d_jerk_v066_signal,
    f27rrd_f27_repair_remodel_durability_sharediff_21d_jerk_v067_signal,
    f27rrd_f27_repair_remodel_durability_sharediff_63d_jerk_v068_signal,
    f27rrd_f27_repair_remodel_durability_shareema_21d_jerk_v069_signal,
    f27rrd_f27_repair_remodel_durability_shareema_63d_jerk_v070_signal,
    f27rrd_f27_repair_remodel_durability_sharerank_252d_jerk_v071_signal,
    f27rrd_f27_repair_remodel_durability_sharerank_504d_jerk_v072_signal,
    f27rrd_f27_repair_remodel_durability_sharesq_63d_jerk_v073_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgn_63d_jerk_v074_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgn_252d_jerk_v075_signal,
    f27rrd_f27_repair_remodel_durability_sharexpx_63d_jerk_v076_signal,
    f27rrd_f27_repair_remodel_durability_share_logclose_63d_jerk_v077_signal,
    f27rrd_f27_repair_remodel_durability_sharexpkgap_252d_jerk_v078_signal,
    f27rrd_f27_repair_remodel_durability_sharexrange_252d_jerk_v079_signal,
    f27rrd_f27_repair_remodel_durability_sharexstd_252d_jerk_v080_signal,
    f27rrd_f27_repair_remodel_durability_shareinv_252d_jerk_v081_signal,
    f27rrd_f27_repair_remodel_durability_share_pxratio_252d_jerk_v082_signal,
    f27rrd_f27_repair_remodel_durability_share_minusmean_252d_jerk_v083_signal,
    f27rrd_f27_repair_remodel_durability_sharexvolz_252d_jerk_v084_signal,
    f27rrd_f27_repair_remodel_durability_share_revchg_63d_jerk_v085_signal,
    f27rrd_f27_repair_remodel_durability_share_ebmgnchg_63d_jerk_v086_signal,
    f27rrd_f27_repair_remodel_durability_sharevar_252d_jerk_v087_signal,
    f27rrd_f27_repair_remodel_durability_sharexlogrev_252d_jerk_v088_signal,
    f27rrd_f27_repair_remodel_durability_share_sigxclose_252d_jerk_v089_signal,
    f27rrd_f27_repair_remodel_durability_share_5d_jerk_v090_signal,
    f27rrd_f27_repair_remodel_durability_share_10d_jerk_v091_signal,
    f27rrd_f27_repair_remodel_durability_share_logemamean_63d_jerk_v092_signal,
    f27rrd_f27_repair_remodel_durability_share_dur_252d_jerk_v093_signal,
    f27rrd_f27_repair_remodel_durability_share_pxdet_252d_jerk_v094_signal,
    f27rrd_f27_repair_remodel_durability_share_pxgap_63d_jerk_v095_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgnma_63d_jerk_v096_signal,
    f27rrd_f27_repair_remodel_durability_share_zema_252d_jerk_v097_signal,
    f27rrd_f27_repair_remodel_durability_share_x_logclose_63d_jerk_v098_signal,
    f27rrd_f27_repair_remodel_durability_floor_x_share_252d_jerk_v099_signal,
    f27rrd_f27_repair_remodel_durability_floorinv_x_share_63d_jerk_v100_signal,
    f27rrd_f27_repair_remodel_durability_dur_21d_jerk_v101_signal,
    f27rrd_f27_repair_remodel_durability_dur_63d_jerk_v102_signal,
    f27rrd_f27_repair_remodel_durability_dur_63d_jerk_v103_signal,
    f27rrd_f27_repair_remodel_durability_dur_126d_jerk_v104_signal,
    f27rrd_f27_repair_remodel_durability_dur_252d_jerk_v105_signal,
    f27rrd_f27_repair_remodel_durability_dur_252d_jerk_v106_signal,
    f27rrd_f27_repair_remodel_durability_dur_504d_jerk_v107_signal,
    f27rrd_f27_repair_remodel_durability_dur_42d_jerk_v108_signal,
    f27rrd_f27_repair_remodel_durability_dur_189d_jerk_v109_signal,
    f27rrd_f27_repair_remodel_durability_dur_378d_jerk_v110_signal,
    f27rrd_f27_repair_remodel_durability_durma_63d_jerk_v111_signal,
    f27rrd_f27_repair_remodel_durability_durma_252d_jerk_v112_signal,
    f27rrd_f27_repair_remodel_durability_durstd_252d_jerk_v113_signal,
    f27rrd_f27_repair_remodel_durability_durz_63d_jerk_v114_signal,
    f27rrd_f27_repair_remodel_durability_durz_252d_jerk_v115_signal,
    f27rrd_f27_repair_remodel_durability_durema_63d_jerk_v116_signal,
    f27rrd_f27_repair_remodel_durability_durema_126d_jerk_v117_signal,
    f27rrd_f27_repair_remodel_durability_durrank_252d_jerk_v118_signal,
    f27rrd_f27_repair_remodel_durability_durrank_504d_jerk_v119_signal,
    f27rrd_f27_repair_remodel_durability_durdiff_63d_jerk_v120_signal,
    f27rrd_f27_repair_remodel_durability_durdiff_252d_jerk_v121_signal,
    f27rrd_f27_repair_remodel_durability_durxpx_63d_jerk_v122_signal,
    f27rrd_f27_repair_remodel_durability_durxlogclose_252d_jerk_v123_signal,
    f27rrd_f27_repair_remodel_durability_durxpxgap_252d_jerk_v124_signal,
    f27rrd_f27_repair_remodel_durability_durxrange_252d_jerk_v125_signal,
    f27rrd_f27_repair_remodel_durability_durxstd_252d_jerk_v126_signal,
    f27rrd_f27_repair_remodel_durability_durvslog_252d_jerk_v127_signal,
    f27rrd_f27_repair_remodel_durability_dur_minusmean_252d_jerk_v128_signal,
    f27rrd_f27_repair_remodel_durability_dur_volz_63d_jerk_v129_signal,
    f27rrd_f27_repair_remodel_durability_dur_revchg_252d_jerk_v130_signal,
    f27rrd_f27_repair_remodel_durability_dur_ebmgnchg_252d_jerk_v131_signal,
    f27rrd_f27_repair_remodel_durability_dur_pxratio_252d_jerk_v132_signal,
    f27rrd_f27_repair_remodel_durability_dur_zema_252d_jerk_v133_signal,
    f27rrd_f27_repair_remodel_durability_dur_floor_252d_jerk_v134_signal,
    f27rrd_f27_repair_remodel_durability_dur_share_252d_jerk_v135_signal,
    f27rrd_f27_repair_remodel_durability_floor_share_dur_252d_jerk_v136_signal,
    f27rrd_f27_repair_remodel_durability_floor_minusshare_63d_jerk_v137_signal,
    f27rrd_f27_repair_remodel_durability_floor_plusshare_252d_jerk_v138_signal,
    f27rrd_f27_repair_remodel_durability_compow2_252d_jerk_v139_signal,
    f27rrd_f27_repair_remodel_durability_floor_x_durz_252d_jerk_v140_signal,
    f27rrd_f27_repair_remodel_durability_share_x_durz_252d_jerk_v141_signal,
    f27rrd_f27_repair_remodel_durability_dur_5d_jerk_v142_signal,
    f27rrd_f27_repair_remodel_durability_dur_10d_jerk_v143_signal,
    f27rrd_f27_repair_remodel_durability_floor_dur_minus_252d_jerk_v144_signal,
    f27rrd_f27_repair_remodel_durability_share_dur_minus_252d_jerk_v145_signal,
    f27rrd_f27_repair_remodel_durability_floor_logminus_252d_jerk_v146_signal,
    f27rrd_f27_repair_remodel_durability_sharexshareratio_63d_jerk_v147_signal,
    f27rrd_f27_repair_remodel_durability_share_sharediff_252d_jerk_v148_signal,
    f27rrd_f27_repair_remodel_durability_durmean_63d_jerk_v149_signal,
    f27rrd_f27_repair_remodel_durability_durstd_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REPAIR_REMODEL_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_revenue_floor", "_f27_non_cyclical_share_proxy", "_f27_durability_score")
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
    print(f"OK f27_repair_remodel_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
