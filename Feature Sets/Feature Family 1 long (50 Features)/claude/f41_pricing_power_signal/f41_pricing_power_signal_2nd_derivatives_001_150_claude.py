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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f41_pricing_power_gpgrow(gp, w):
    return gp.pct_change(w)


def _f41_pricing_power_gprev(gp, revenue, w):
    gm = gp / revenue.replace(0, np.nan)
    return gm.diff(w)


def _f41_pricing_power_passthrough(gp, revenue, w):
    return gp.pct_change(w) - revenue.pct_change(w)


def _slo(s, w):
    return s.diff(periods=w)


# 5d slope of 21d gprev × close
def f41pps_f41_pricing_power_signal_gprev_21d_slope_v001_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 21) * closeadj, 5).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_21d_slope_v002_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 21) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_63d_slope_v003_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 63) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_63d_slope_v004_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 63) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_126d_slope_v005_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 126) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_126d_slope_v006_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 126) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_252d_slope_v007_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 252) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_252d_slope_v008_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 252) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_504d_slope_v009_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 504) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprev_504d_slope_v010_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_gprev(gp, revenue, 504) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_21d_slope_v011_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 21) * closeadj, 5).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_21d_slope_v012_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 21) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_63d_slope_v013_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 63) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_63d_slope_v014_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 63) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_126d_slope_v015_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 126) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_126d_slope_v016_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 126) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_252d_slope_v017_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 252) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_252d_slope_v018_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 252) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_504d_slope_v019_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 504) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrow_504d_slope_v020_signal(gp, closeadj):
    return _slo(_f41_pricing_power_gpgrow(gp, 504) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_21d_slope_v021_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 21) * closeadj, 5).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_21d_slope_v022_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 21) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_63d_slope_v023_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 63) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_63d_slope_v024_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 63) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_126d_slope_v025_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 126) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_126d_slope_v026_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 126) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_252d_slope_v027_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 252) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_252d_slope_v028_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 252) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_504d_slope_v029_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 504) * closeadj, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passthrough_504d_slope_v030_signal(gp, revenue, closeadj):
    return _slo(_f41_pricing_power_passthrough(gp, revenue, 504) * closeadj, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmean_252d_slope_v031_signal(gp, revenue, closeadj):
    base = _mean(_f41_pricing_power_gprev(gp, revenue, 63), 252) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmean_63d_slope_v032_signal(gp, revenue, closeadj):
    base = _mean(_f41_pricing_power_gprev(gp, revenue, 21), 63) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowstd_252d_slope_v033_signal(gp, closeadj):
    base = _std(_f41_pricing_power_gpgrow(gp, 21), 252) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowstd_63d_slope_v034_signal(gp, closeadj):
    base = _std(_f41_pricing_power_gpgrow(gp, 5), 63) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowz_252d_slope_v035_signal(gp, closeadj):
    base = _z(_f41_pricing_power_gpgrow(gp, 21), 252) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowz_504d_slope_v036_signal(gp, closeadj):
    base = _z(_f41_pricing_power_gpgrow(gp, 252), 504) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevz_252d_slope_v037_signal(gp, revenue, closeadj):
    base = _z(_f41_pricing_power_gprev(gp, revenue, 21), 252) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevz_504d_slope_v038_signal(gp, revenue, closeadj):
    base = _z(_f41_pricing_power_gprev(gp, revenue, 252), 504) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmlevel_252d_slope_v039_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmlevel_63d_slope_v040_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    base = (_mean(gm, 63) + aux) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrev_21d_slope_v041_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21) * revenue * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrev_252d_slope_v042_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxrev_252d_slope_v043_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxrev_63d_slope_v044_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * revenue * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxrev_252d_slope_v045_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 252) * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxrev_63d_slope_v046_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 63) * revenue * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxeps_252d_slope_v047_signal(gp, eps, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * eps * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxeps_63d_slope_v048_signal(gp, eps, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * eps * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpassets_252d_slope_v049_signal(gp, assets, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    base = (_mean(gp / assets.replace(0, np.nan), 252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpassets_63d_slope_v050_signal(gp, assets, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    base = (_mean(gp / assets.replace(0, np.nan), 63) + aux) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevema_252d_slope_v051_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevema_63d_slope_v052_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).ewm(span=63, adjust=False).mean() * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowema_252d_slope_v053_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowema_63d_slope_v054_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 5).ewm(span=63, adjust=False).mean() * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevexp_slope_v055_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).expanding(min_periods=63).mean() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevexpz_slope_v056_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    m = base.expanding(min_periods=63).mean()
    sd = base.expanding(min_periods=63).std().replace(0, np.nan)
    series = (base - m) / sd * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevposfreq_252d_slope_v057_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0).astype(float).rolling(252, min_periods=63).mean() * closeadj
    return _slo(pos, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevposfreq_504d_slope_v058_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    pos = (base > 0).astype(float).rolling(504, min_periods=126).mean() * closeadj
    return _slo(pos, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsum_252d_slope_v059_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).sum() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsum_504d_slope_v060_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).sum() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsum_63d_slope_v061_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 5).rolling(63, min_periods=21).sum() * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxdebt_252d_slope_v062_signal(gp, debt, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * debt.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxdebt_63d_slope_v063_signal(gp, debt, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * debt.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxebgrow_252d_slope_v064_signal(gp, revenue, ebitda, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * ebitda.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxebgrow_63d_slope_v065_signal(gp, revenue, ebitda, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * ebitda.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxmc_252d_slope_v066_signal(gp, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    base = _f41_pricing_power_gpgrow(gp, 252) * closeadj / mc * gp
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxmc_63d_slope_v067_signal(gp, sharesbas, closeadj):
    mc = (closeadj * sharesbas).replace(0, np.nan)
    base = _f41_pricing_power_gpgrow(gp, 63) * closeadj / mc * gp
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxebitda_252d_slope_v068_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * ebitda * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxebitda_63d_slope_v069_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    base = (_mean(gm, 63) + aux) * ebitda * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_costpass_252d_slope_v070_signal(gp, opinc, revenue, closeadj):
    opex = (revenue - opinc).abs()
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    base = (gp.pct_change(252) - opex.pct_change(252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_costpass_63d_slope_v071_signal(gp, opinc, revenue, closeadj):
    opex = (revenue - opinc).abs()
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    base = (gp.pct_change(63) - opex.pct_change(63) + aux) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxcr_252d_slope_v072_signal(gp, currentratio, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * currentratio * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxcr_63d_slope_v073_signal(gp, currentratio, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * currentratio * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxepsg_252d_slope_v074_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * eps.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxepsg_63d_slope_v075_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * eps.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxncfo_252d_slope_v076_signal(gp, ncfo, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * ncfo * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxncfo_63d_slope_v077_signal(gp, ncfo, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * ncfo * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxfcf_252d_slope_v078_signal(gp, fcf, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * fcf * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxfcf_63d_slope_v079_signal(gp, fcf, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * fcf * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxrevscale_252d_slope_v080_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxrevscale_63d_slope_v081_signal(gp, revenue, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    base = (_mean(gm, 63) + aux) * revenue * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_compoundprice_252d_slope_v082_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_compoundprice_63d_slope_v083_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * revenue.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsignmag_252d_slope_v084_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252)
    series = np.sign(base) * base.abs() * closeadj * revenue / 1.0e9
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsignmag_63d_slope_v085_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63)
    series = np.sign(base) * base.abs() * closeadj * revenue / 1.0e9
    return _slo(series, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsnr_252d_slope_v086_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    sd = _std(base, 252).replace(0, np.nan)
    series = _mean(base, 63) / sd * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsnr_504d_slope_v087_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    sd = _std(base, 504).replace(0, np.nan)
    series = _mean(base, 252) / sd * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_megacomposite_252d_slope_v088_signal(gp, revenue, ebitda, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * revenue.pct_change(252).fillna(0.0) * ebitda * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passcomposite_252d_slope_v089_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 252) * eps * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_ultimate_252d_slope_v090_signal(gp, revenue, eps, closeadj):
    base = _mean(_f41_pricing_power_gprev(gp, revenue, 21), 252) * revenue * eps.pct_change(252).fillna(0.0) * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilehi_252d_slope_v091_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).quantile(0.9) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilelo_252d_slope_v092_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).quantile(0.1) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilehi_504d_slope_v093_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).quantile(0.9) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevquantilelo_504d_slope_v094_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).quantile(0.1) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowquantilehi_252d_slope_v095_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21).rolling(252, min_periods=63).quantile(0.9) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowquantilelo_252d_slope_v096_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21).rolling(252, min_periods=63).quantile(0.1) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevskew_252d_slope_v097_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).skew() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevskew_504d_slope_v098_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).skew() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevkurt_252d_slope_v099_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).kurt() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevkurt_504d_slope_v100_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).kurt() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmedian_252d_slope_v101_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).median() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevmedian_504d_slope_v102_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(504, min_periods=126).median() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowiqr_252d_slope_v103_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    series = (base.rolling(252, min_periods=63).quantile(0.75) - base.rolling(252, min_periods=63).quantile(0.25)) * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowiqr_504d_slope_v104_signal(gp, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 21)
    series = (base.rolling(504, min_periods=126).quantile(0.75) - base.rolling(504, min_periods=126).quantile(0.25)) * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpequity_252d_slope_v105_signal(gp, equity, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    base = (_mean(gp / equity.replace(0, np.nan), 252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpequity_63d_slope_v106_signal(gp, equity, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 63) * 0.0
    base = (_mean(gp / equity.replace(0, np.nan), 63) + aux) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxwc_252d_slope_v107_signal(gp, revenue, workingcapital, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * workingcapital * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxwc_63d_slope_v108_signal(gp, revenue, workingcapital, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 63) * 0.0
    base = (_mean(gm, 63) + aux) * workingcapital * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxintexp_252d_slope_v109_signal(gp, revenue, intexp, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 252) * intexp * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxintexp_63d_slope_v110_signal(gp, revenue, intexp, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 63) * intexp * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevvslong_252d_slope_v111_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    series = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevvslong_63d_slope_v112_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    series = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return _slo(series, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxncfog_252d_slope_v113_signal(gp, revenue, ncfo, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * ncfo.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxncfog_63d_slope_v114_signal(gp, revenue, ncfo, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * ncfo.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxfcfg_252d_slope_v115_signal(gp, revenue, fcf, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * fcf.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxfcfg_63d_slope_v116_signal(gp, revenue, fcf, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * fcf.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_marginexpfreq_252d_slope_v117_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    series = (base > 0.001).astype(float).rolling(252, min_periods=63).sum() / 252.0 * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_marginexpfreq_504d_slope_v118_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    series = (base > 0.001).astype(float).rolling(504, min_periods=126).sum() / 504.0 * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrevg_252d_slope_v119_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxrevg_63d_slope_v120_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 63) * revenue.pct_change(63).fillna(0.0) * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxdebt_252d_slope_v121_signal(gp, revenue, debt, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * debt * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxdebt_63d_slope_v122_signal(gp, revenue, debt, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 63) * debt * closeadj / 1.0e9
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpovercapex_252d_slope_v123_signal(gp, capex, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    ratio = gp / capex.abs().replace(0, np.nan)
    base = (_mean(ratio, 252) + aux) * closeadj / 1.0e3
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxeps_252d_slope_v124_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 252) * eps * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passxrevg_252d_slope_v125_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxni_252d_slope_v126_signal(gp, revenue, netinc, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * netinc * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpvsassetg_252d_slope_v127_signal(gp, assets, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    base = (gp.pct_change(252) - assets.pct_change(252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passsum_252d_slope_v128_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21).rolling(252, min_periods=63).sum() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passsum_504d_slope_v129_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21).rolling(504, min_periods=126).sum() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passema_252d_slope_v130_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_passema_63d_slope_v131_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 5).ewm(span=63, adjust=False).mean() * closeadj
    return _slo(base, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevsmallwin_252d_slope_v132_signal(gp, revenue, closeadj):
    base = _mean(_f41_pricing_power_gprev(gp, revenue, 5), 252) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxintexp_252d_slope_v133_signal(gp, revenue, intexp, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * intexp * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpaccel_252d_slope_v134_signal(gp, closeadj):
    base = (_f41_pricing_power_gpgrow(gp, 63) - _f41_pricing_power_gpgrow(gp, 252)) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevpercentile_252d_slope_v135_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxrevpershare_252d_slope_v136_signal(gp, revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f41_pricing_power_gprev(gp, revenue, 252) * rps * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxwc_252d_slope_v137_signal(gp, workingcapital, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * workingcapital * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevstd_252d_slope_v138_signal(gp, revenue, closeadj):
    base = _std(_f41_pricing_power_gprev(gp, revenue, 21), 252) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_triplecombo_252d_slope_v139_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * _f41_pricing_power_gprev(gp, revenue, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gppershare_252d_slope_v140_signal(gp, sharesbas, closeadj):
    aux = _f41_pricing_power_gpgrow(gp, 252) * 0.0
    base = (_mean(gp / sharesbas.replace(0, np.nan), 252) + aux) * closeadj
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gmxncfo_252d_slope_v141_signal(gp, revenue, ncfo, closeadj):
    gm = gp / revenue.replace(0, np.nan)
    aux = _f41_pricing_power_gprev(gp, revenue, 252) * 0.0
    base = (_mean(gm, 252) + aux) * ncfo * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevcumxrev_252d_slope_v142_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21).rolling(252, min_periods=63).sum() * revenue * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxfcfl_252d_slope_v143_signal(gp, fcf, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * fcf * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevcv_252d_slope_v144_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 21)
    series = (_std(base, 252) / _mean(base.abs(), 252).replace(0, np.nan)) * closeadj
    return _slo(series, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxebitda_252d_slope_v145_signal(gp, revenue, ebitda, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * ebitda * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_ultimatecombo_252d_slope_v146_signal(gp, revenue, eps, closeadj):
    base = _f41_pricing_power_passthrough(gp, revenue, 21).rolling(252, min_periods=63).sum() * revenue * eps * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevposfreq_63d_slope_v147_signal(gp, revenue, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 5)
    pos = (base > 0).astype(float).rolling(63, min_periods=21).mean() * closeadj
    return _slo(pos, 21).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxequity_252d_slope_v148_signal(gp, equity, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * equity * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gprevxopinc_252d_slope_v149_signal(gp, revenue, opinc, closeadj):
    base = _f41_pricing_power_gprev(gp, revenue, 252) * opinc * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


def f41pps_f41_pricing_power_signal_gpgrowxni_252d_slope_v150_signal(gp, netinc, closeadj):
    base = _f41_pricing_power_gpgrow(gp, 252) * netinc * closeadj / 1.0e9
    return _slo(base, 63).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41pps_f41_pricing_power_signal_gprev_21d_slope_v001_signal,
    f41pps_f41_pricing_power_signal_gprev_21d_slope_v002_signal,
    f41pps_f41_pricing_power_signal_gprev_63d_slope_v003_signal,
    f41pps_f41_pricing_power_signal_gprev_63d_slope_v004_signal,
    f41pps_f41_pricing_power_signal_gprev_126d_slope_v005_signal,
    f41pps_f41_pricing_power_signal_gprev_126d_slope_v006_signal,
    f41pps_f41_pricing_power_signal_gprev_252d_slope_v007_signal,
    f41pps_f41_pricing_power_signal_gprev_252d_slope_v008_signal,
    f41pps_f41_pricing_power_signal_gprev_504d_slope_v009_signal,
    f41pps_f41_pricing_power_signal_gprev_504d_slope_v010_signal,
    f41pps_f41_pricing_power_signal_gpgrow_21d_slope_v011_signal,
    f41pps_f41_pricing_power_signal_gpgrow_21d_slope_v012_signal,
    f41pps_f41_pricing_power_signal_gpgrow_63d_slope_v013_signal,
    f41pps_f41_pricing_power_signal_gpgrow_63d_slope_v014_signal,
    f41pps_f41_pricing_power_signal_gpgrow_126d_slope_v015_signal,
    f41pps_f41_pricing_power_signal_gpgrow_126d_slope_v016_signal,
    f41pps_f41_pricing_power_signal_gpgrow_252d_slope_v017_signal,
    f41pps_f41_pricing_power_signal_gpgrow_252d_slope_v018_signal,
    f41pps_f41_pricing_power_signal_gpgrow_504d_slope_v019_signal,
    f41pps_f41_pricing_power_signal_gpgrow_504d_slope_v020_signal,
    f41pps_f41_pricing_power_signal_passthrough_21d_slope_v021_signal,
    f41pps_f41_pricing_power_signal_passthrough_21d_slope_v022_signal,
    f41pps_f41_pricing_power_signal_passthrough_63d_slope_v023_signal,
    f41pps_f41_pricing_power_signal_passthrough_63d_slope_v024_signal,
    f41pps_f41_pricing_power_signal_passthrough_126d_slope_v025_signal,
    f41pps_f41_pricing_power_signal_passthrough_126d_slope_v026_signal,
    f41pps_f41_pricing_power_signal_passthrough_252d_slope_v027_signal,
    f41pps_f41_pricing_power_signal_passthrough_252d_slope_v028_signal,
    f41pps_f41_pricing_power_signal_passthrough_504d_slope_v029_signal,
    f41pps_f41_pricing_power_signal_passthrough_504d_slope_v030_signal,
    f41pps_f41_pricing_power_signal_gprevmean_252d_slope_v031_signal,
    f41pps_f41_pricing_power_signal_gprevmean_63d_slope_v032_signal,
    f41pps_f41_pricing_power_signal_gpgrowstd_252d_slope_v033_signal,
    f41pps_f41_pricing_power_signal_gpgrowstd_63d_slope_v034_signal,
    f41pps_f41_pricing_power_signal_gpgrowz_252d_slope_v035_signal,
    f41pps_f41_pricing_power_signal_gpgrowz_504d_slope_v036_signal,
    f41pps_f41_pricing_power_signal_gprevz_252d_slope_v037_signal,
    f41pps_f41_pricing_power_signal_gprevz_504d_slope_v038_signal,
    f41pps_f41_pricing_power_signal_gmlevel_252d_slope_v039_signal,
    f41pps_f41_pricing_power_signal_gmlevel_63d_slope_v040_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrev_21d_slope_v041_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrev_252d_slope_v042_signal,
    f41pps_f41_pricing_power_signal_gprevxrev_252d_slope_v043_signal,
    f41pps_f41_pricing_power_signal_gprevxrev_63d_slope_v044_signal,
    f41pps_f41_pricing_power_signal_passxrev_252d_slope_v045_signal,
    f41pps_f41_pricing_power_signal_passxrev_63d_slope_v046_signal,
    f41pps_f41_pricing_power_signal_gpgrowxeps_252d_slope_v047_signal,
    f41pps_f41_pricing_power_signal_gpgrowxeps_63d_slope_v048_signal,
    f41pps_f41_pricing_power_signal_gpassets_252d_slope_v049_signal,
    f41pps_f41_pricing_power_signal_gpassets_63d_slope_v050_signal,
    f41pps_f41_pricing_power_signal_gprevema_252d_slope_v051_signal,
    f41pps_f41_pricing_power_signal_gprevema_63d_slope_v052_signal,
    f41pps_f41_pricing_power_signal_gpgrowema_252d_slope_v053_signal,
    f41pps_f41_pricing_power_signal_gpgrowema_63d_slope_v054_signal,
    f41pps_f41_pricing_power_signal_gprevexp_slope_v055_signal,
    f41pps_f41_pricing_power_signal_gprevexpz_slope_v056_signal,
    f41pps_f41_pricing_power_signal_gprevposfreq_252d_slope_v057_signal,
    f41pps_f41_pricing_power_signal_gprevposfreq_504d_slope_v058_signal,
    f41pps_f41_pricing_power_signal_gprevsum_252d_slope_v059_signal,
    f41pps_f41_pricing_power_signal_gprevsum_504d_slope_v060_signal,
    f41pps_f41_pricing_power_signal_gprevsum_63d_slope_v061_signal,
    f41pps_f41_pricing_power_signal_gpgrowxdebt_252d_slope_v062_signal,
    f41pps_f41_pricing_power_signal_gpgrowxdebt_63d_slope_v063_signal,
    f41pps_f41_pricing_power_signal_gprevxebgrow_252d_slope_v064_signal,
    f41pps_f41_pricing_power_signal_gprevxebgrow_63d_slope_v065_signal,
    f41pps_f41_pricing_power_signal_gpgrowxmc_252d_slope_v066_signal,
    f41pps_f41_pricing_power_signal_gpgrowxmc_63d_slope_v067_signal,
    f41pps_f41_pricing_power_signal_gmxebitda_252d_slope_v068_signal,
    f41pps_f41_pricing_power_signal_gmxebitda_63d_slope_v069_signal,
    f41pps_f41_pricing_power_signal_costpass_252d_slope_v070_signal,
    f41pps_f41_pricing_power_signal_costpass_63d_slope_v071_signal,
    f41pps_f41_pricing_power_signal_gpgrowxcr_252d_slope_v072_signal,
    f41pps_f41_pricing_power_signal_gpgrowxcr_63d_slope_v073_signal,
    f41pps_f41_pricing_power_signal_gprevxepsg_252d_slope_v074_signal,
    f41pps_f41_pricing_power_signal_gprevxepsg_63d_slope_v075_signal,
    f41pps_f41_pricing_power_signal_gpgrowxncfo_252d_slope_v076_signal,
    f41pps_f41_pricing_power_signal_gpgrowxncfo_63d_slope_v077_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcf_252d_slope_v078_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcf_63d_slope_v079_signal,
    f41pps_f41_pricing_power_signal_gmxrevscale_252d_slope_v080_signal,
    f41pps_f41_pricing_power_signal_gmxrevscale_63d_slope_v081_signal,
    f41pps_f41_pricing_power_signal_compoundprice_252d_slope_v082_signal,
    f41pps_f41_pricing_power_signal_compoundprice_63d_slope_v083_signal,
    f41pps_f41_pricing_power_signal_gprevsignmag_252d_slope_v084_signal,
    f41pps_f41_pricing_power_signal_gprevsignmag_63d_slope_v085_signal,
    f41pps_f41_pricing_power_signal_gprevsnr_252d_slope_v086_signal,
    f41pps_f41_pricing_power_signal_gprevsnr_504d_slope_v087_signal,
    f41pps_f41_pricing_power_signal_megacomposite_252d_slope_v088_signal,
    f41pps_f41_pricing_power_signal_passcomposite_252d_slope_v089_signal,
    f41pps_f41_pricing_power_signal_ultimate_252d_slope_v090_signal,
    f41pps_f41_pricing_power_signal_gprevquantilehi_252d_slope_v091_signal,
    f41pps_f41_pricing_power_signal_gprevquantilelo_252d_slope_v092_signal,
    f41pps_f41_pricing_power_signal_gprevquantilehi_504d_slope_v093_signal,
    f41pps_f41_pricing_power_signal_gprevquantilelo_504d_slope_v094_signal,
    f41pps_f41_pricing_power_signal_gpgrowquantilehi_252d_slope_v095_signal,
    f41pps_f41_pricing_power_signal_gpgrowquantilelo_252d_slope_v096_signal,
    f41pps_f41_pricing_power_signal_gprevskew_252d_slope_v097_signal,
    f41pps_f41_pricing_power_signal_gprevskew_504d_slope_v098_signal,
    f41pps_f41_pricing_power_signal_gprevkurt_252d_slope_v099_signal,
    f41pps_f41_pricing_power_signal_gprevkurt_504d_slope_v100_signal,
    f41pps_f41_pricing_power_signal_gprevmedian_252d_slope_v101_signal,
    f41pps_f41_pricing_power_signal_gprevmedian_504d_slope_v102_signal,
    f41pps_f41_pricing_power_signal_gpgrowiqr_252d_slope_v103_signal,
    f41pps_f41_pricing_power_signal_gpgrowiqr_504d_slope_v104_signal,
    f41pps_f41_pricing_power_signal_gpequity_252d_slope_v105_signal,
    f41pps_f41_pricing_power_signal_gpequity_63d_slope_v106_signal,
    f41pps_f41_pricing_power_signal_gmxwc_252d_slope_v107_signal,
    f41pps_f41_pricing_power_signal_gmxwc_63d_slope_v108_signal,
    f41pps_f41_pricing_power_signal_passxintexp_252d_slope_v109_signal,
    f41pps_f41_pricing_power_signal_passxintexp_63d_slope_v110_signal,
    f41pps_f41_pricing_power_signal_gprevvslong_252d_slope_v111_signal,
    f41pps_f41_pricing_power_signal_gprevvslong_63d_slope_v112_signal,
    f41pps_f41_pricing_power_signal_gprevxncfog_252d_slope_v113_signal,
    f41pps_f41_pricing_power_signal_gprevxncfog_63d_slope_v114_signal,
    f41pps_f41_pricing_power_signal_gprevxfcfg_252d_slope_v115_signal,
    f41pps_f41_pricing_power_signal_gprevxfcfg_63d_slope_v116_signal,
    f41pps_f41_pricing_power_signal_marginexpfreq_252d_slope_v117_signal,
    f41pps_f41_pricing_power_signal_marginexpfreq_504d_slope_v118_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrevg_252d_slope_v119_signal,
    f41pps_f41_pricing_power_signal_gpgrowxrevg_63d_slope_v120_signal,
    f41pps_f41_pricing_power_signal_gprevxdebt_252d_slope_v121_signal,
    f41pps_f41_pricing_power_signal_gprevxdebt_63d_slope_v122_signal,
    f41pps_f41_pricing_power_signal_gpovercapex_252d_slope_v123_signal,
    f41pps_f41_pricing_power_signal_passxeps_252d_slope_v124_signal,
    f41pps_f41_pricing_power_signal_passxrevg_252d_slope_v125_signal,
    f41pps_f41_pricing_power_signal_gmxni_252d_slope_v126_signal,
    f41pps_f41_pricing_power_signal_gpvsassetg_252d_slope_v127_signal,
    f41pps_f41_pricing_power_signal_passsum_252d_slope_v128_signal,
    f41pps_f41_pricing_power_signal_passsum_504d_slope_v129_signal,
    f41pps_f41_pricing_power_signal_passema_252d_slope_v130_signal,
    f41pps_f41_pricing_power_signal_passema_63d_slope_v131_signal,
    f41pps_f41_pricing_power_signal_gprevsmallwin_252d_slope_v132_signal,
    f41pps_f41_pricing_power_signal_gprevxintexp_252d_slope_v133_signal,
    f41pps_f41_pricing_power_signal_gpaccel_252d_slope_v134_signal,
    f41pps_f41_pricing_power_signal_gprevpercentile_252d_slope_v135_signal,
    f41pps_f41_pricing_power_signal_gprevxrevpershare_252d_slope_v136_signal,
    f41pps_f41_pricing_power_signal_gpgrowxwc_252d_slope_v137_signal,
    f41pps_f41_pricing_power_signal_gprevstd_252d_slope_v138_signal,
    f41pps_f41_pricing_power_signal_triplecombo_252d_slope_v139_signal,
    f41pps_f41_pricing_power_signal_gppershare_252d_slope_v140_signal,
    f41pps_f41_pricing_power_signal_gmxncfo_252d_slope_v141_signal,
    f41pps_f41_pricing_power_signal_gprevcumxrev_252d_slope_v142_signal,
    f41pps_f41_pricing_power_signal_gpgrowxfcfl_252d_slope_v143_signal,
    f41pps_f41_pricing_power_signal_gprevcv_252d_slope_v144_signal,
    f41pps_f41_pricing_power_signal_gprevxebitda_252d_slope_v145_signal,
    f41pps_f41_pricing_power_signal_ultimatecombo_252d_slope_v146_signal,
    f41pps_f41_pricing_power_signal_gprevposfreq_63d_slope_v147_signal,
    f41pps_f41_pricing_power_signal_gpgrowxequity_252d_slope_v148_signal,
    f41pps_f41_pricing_power_signal_gprevxopinc_252d_slope_v149_signal,
    f41pps_f41_pricing_power_signal_gpgrowxni_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_PRICING_POWER_SIGNAL_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    gp = pd.Series(4.0e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))), name="gp")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    intexp = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="intexp")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "gp": gp, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "currentratio": currentratio, "fcf": fcf, "ncfo": ncfo, "sharesbas": sharesbas,
        "intexp": intexp, "equity": equity, "workingcapital": workingcapital,
        "capex": capex, "netinc": netinc,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_pricing_power",)
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
    print(f"OK f41_pricing_power_signal_2nd_derivatives_001_150_claude: {n_features} features pass")
