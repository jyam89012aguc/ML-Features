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


def _slope(s, w):
    return s.diff(periods=w)


# ===== folder domain primitives =====
def _f35_margin_jerk_net(netinc, revenue, w):
    m = _safe_div(netinc, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


def _f35_margin_jerk_op(opinc, revenue, w):
    m = _safe_div(opinc, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


def _f35_margin_jerk_gross(gp, revenue, w):
    m = _safe_div(gp, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


def _f35_margin_jerk_ebitda(ebitda, revenue, w):
    m = _safe_div(ebitda, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


# 5d slope of 21d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_21d_slope_v001_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_21d_slope_v002_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_63d_slope_v003_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_63d_slope_v004_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_126d_slope_v005_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_126d_slope_v006_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_252d_slope_v007_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_252d_slope_v008_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_21d_slope_v009_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_21d_slope_v010_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_63d_slope_v011_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_63d_slope_v012_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_126d_slope_v013_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_126d_slope_v014_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_252d_slope_v015_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_252d_slope_v016_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_21d_slope_v017_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_21d_slope_v018_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_63d_slope_v019_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_63d_slope_v020_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_126d_slope_v021_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_126d_slope_v022_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_252d_slope_v023_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_252d_slope_v024_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_21d_slope_v025_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_21d_slope_v026_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_63d_slope_v027_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_63d_slope_v028_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_126d_slope_v029_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 126) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_126d_slope_v030_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 126) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_252d_slope_v031_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_252d_slope_v032_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d net margin |jerk| × close
def f35mj_f35_margin_jerk_netmargin_abs_21d_slope_v033_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 21).abs() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d net margin |jerk| × close
def f35mj_f35_margin_jerk_netmargin_abs_63d_slope_v034_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63).abs() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d net margin |jerk| × close
def f35mj_f35_margin_jerk_netmargin_abs_126d_slope_v035_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 126).abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d op margin jerk squared × close
def f35mj_f35_margin_jerk_opmargin_sq_21d_slope_v036_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    base = j * j.abs() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d op margin jerk squared × close
def f35mj_f35_margin_jerk_opmargin_sq_63d_slope_v037_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    base = j * j.abs() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gross margin jerk squared × close
def f35mj_f35_margin_jerk_grossmargin_sq_252d_slope_v038_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 252)
    base = j * j.abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk mean (63d window) × close
def f35mj_f35_margin_jerk_netmargin_mean_63d_slope_v039_signal(netinc, revenue, closeadj):
    base = _mean(_f35_margin_jerk_net(netinc, revenue, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk mean (252d window) × close
def f35mj_f35_margin_jerk_netmargin_mean_252d_slope_v040_signal(netinc, revenue, closeadj):
    base = _mean(_f35_margin_jerk_net(netinc, revenue, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op margin jerk mean (63d) × close
def f35mj_f35_margin_jerk_opmargin_mean_63d_slope_v041_signal(opinc, revenue, closeadj):
    base = _mean(_f35_margin_jerk_op(opinc, revenue, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk mean (252d) × close
def f35mj_f35_margin_jerk_grossmargin_mean_252d_slope_v042_signal(gp, revenue, closeadj):
    base = _mean(_f35_margin_jerk_gross(gp, revenue, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk std (63d) × close
def f35mj_f35_margin_jerk_netmargin_std_63d_slope_v043_signal(netinc, revenue, closeadj):
    base = _std(_f35_margin_jerk_net(netinc, revenue, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk std (252d) × close
def f35mj_f35_margin_jerk_opmargin_std_252d_slope_v044_signal(opinc, revenue, closeadj):
    base = _std(_f35_margin_jerk_op(opinc, revenue, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin jerk std (252d) × close
def f35mj_f35_margin_jerk_ebitdamargin_std_252d_slope_v045_signal(ebitda, revenue, closeadj):
    base = _std(_f35_margin_jerk_ebitda(ebitda, revenue, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk z (252d) × close
def f35mj_f35_margin_jerk_netmargin_z_252d_slope_v046_signal(netinc, revenue, closeadj):
    base = _z(_f35_margin_jerk_net(netinc, revenue, 63), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk z (252d) × close
def f35mj_f35_margin_jerk_opmargin_z_252d_slope_v047_signal(opinc, revenue, closeadj):
    base = _z(_f35_margin_jerk_op(opinc, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk z (252d) × close
def f35mj_f35_margin_jerk_grossmargin_z_252d_slope_v048_signal(gp, revenue, closeadj):
    base = _z(_f35_margin_jerk_gross(gp, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin jerk z (252d) × close
def f35mj_f35_margin_jerk_ebitdamargin_z_252d_slope_v049_signal(ebitda, revenue, closeadj):
    base = _z(_f35_margin_jerk_ebitda(ebitda, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × revenue × close
def f35mj_f35_margin_jerk_netmargin_xrev_63d_slope_v050_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * revenue.abs() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × revenue × close
def f35mj_f35_margin_jerk_opmargin_xrev_252d_slope_v051_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * revenue.abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk × revenue × close
def f35mj_f35_margin_jerk_grossmargin_xrev_252d_slope_v052_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 252) * revenue.abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net jerk × ebitda × close
def f35mj_f35_margin_jerk_netmargin_xebitda_63d_slope_v053_signal(netinc, revenue, ebitda, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * ebitda.abs() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op jerk × ebitda × close
def f35mj_f35_margin_jerk_opmargin_xebitda_252d_slope_v054_signal(opinc, revenue, ebitda, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * ebitda.abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net jerk diff (63m252) × close
def f35mj_f35_margin_jerk_netmargin_diff_63m252_slope_v055_signal(netinc, revenue, closeadj):
    base = (_f35_margin_jerk_net(netinc, revenue, 63) - _f35_margin_jerk_net(netinc, revenue, 252)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of op jerk diff (21m63) × close
def f35mj_f35_margin_jerk_opmargin_diff_21m63_slope_v056_signal(opinc, revenue, closeadj):
    base = (_f35_margin_jerk_op(opinc, revenue, 21) - _f35_margin_jerk_op(opinc, revenue, 63)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of grossvsnet jerk × close
def f35mj_f35_margin_jerk_grossvsnet_252d_slope_v057_signal(gp, netinc, revenue, closeadj):
    base = (_f35_margin_jerk_gross(gp, revenue, 252) - _f35_margin_jerk_net(netinc, revenue, 252)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ebitdavsnet jerk × close
def f35mj_f35_margin_jerk_ebitdavsnet_63d_slope_v058_signal(ebitda, netinc, revenue, closeadj):
    base = (_f35_margin_jerk_ebitda(ebitda, revenue, 63) - _f35_margin_jerk_net(netinc, revenue, 63)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of net margin jerk EMA (21d) × close
def f35mj_f35_margin_jerk_netmargin_ema_21d_slope_v059_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op margin jerk EMA (63d) × close
def f35mj_f35_margin_jerk_opmargin_ema_63d_slope_v060_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    base = j.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk EMA (252d) × close
def f35mj_f35_margin_jerk_grossmargin_ema_252d_slope_v061_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 252)
    base = j.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk negcount × close
def f35mj_f35_margin_jerk_netmargin_negcount_252d_slope_v062_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    base = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk poscount × close
def f35mj_f35_margin_jerk_opmargin_poscount_252d_slope_v063_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    base = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk extremecount × close
def f35mj_f35_margin_jerk_netmargin_extremecount_504d_slope_v064_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    z = _z(j, 252)
    flag = (z.abs() > 2.0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj * 0.001
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk sum × close
def f35mj_f35_margin_jerk_netmargin_sum_252d_slope_v065_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk sum × close
def f35mj_f35_margin_jerk_opmargin_sum_252d_slope_v066_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk sum × close
def f35mj_f35_margin_jerk_grossmargin_sum_252d_slope_v067_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin jerk sum × close
def f35mj_f35_margin_jerk_ebitdamargin_sum_252d_slope_v068_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d net margin jerk × momentum × close
def f35mj_f35_margin_jerk_netmargin_xmom_21d_slope_v069_signal(netinc, revenue, closeadj):
    mom = closeadj.pct_change(21)
    base = _f35_margin_jerk_net(netinc, revenue, 21) * mom * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d op margin jerk × momentum × close
def f35mj_f35_margin_jerk_opmargin_xmom_63d_slope_v070_signal(opinc, revenue, closeadj):
    mom = closeadj.pct_change(63)
    base = _f35_margin_jerk_op(opinc, revenue, 63) * mom * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gross margin jerk × momentum × close
def f35mj_f35_margin_jerk_grossmargin_xmom_252d_slope_v071_signal(gp, revenue, closeadj):
    mom = closeadj.pct_change(252)
    base = _f35_margin_jerk_gross(gp, revenue, 252) * mom * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d net margin jerk normalized by rev std × revenue × close
def f35mj_f35_margin_jerk_netmargin_normrev_63d_slope_v072_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    rs = _std(revenue, 63).replace(0, np.nan)
    base = j / rs * revenue.abs() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk normalized by rev std × revenue × close
def f35mj_f35_margin_jerk_opmargin_normrev_252d_slope_v073_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 252)
    rs = _std(revenue, 252).replace(0, np.nan)
    base = j / rs * revenue.abs() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d net margin jerk × asset turnover × close
def f35mj_f35_margin_jerk_netmargin_xato_63d_slope_v074_signal(netinc, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    base = _f35_margin_jerk_net(netinc, revenue, 63) * ato * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × asset turnover × close
def f35mj_f35_margin_jerk_opmargin_xato_252d_slope_v075_signal(opinc, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    base = _f35_margin_jerk_op(opinc, revenue, 252) * ato * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × current ratio × close
def f35mj_f35_margin_jerk_netmargin_xcr_63d_slope_v076_signal(netinc, revenue, currentratio, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * currentratio * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × current ratio × close
def f35mj_f35_margin_jerk_opmargin_xcr_252d_slope_v077_signal(opinc, revenue, currentratio, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * currentratio * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × debt × close
def f35mj_f35_margin_jerk_netmargin_xdebt_63d_slope_v078_signal(netinc, revenue, debt, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * debt.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × debt × close
def f35mj_f35_margin_jerk_opmargin_xdebt_252d_slope_v079_signal(opinc, revenue, debt, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * debt.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × equity × close
def f35mj_f35_margin_jerk_netmargin_xequity_63d_slope_v080_signal(netinc, revenue, equity, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * equity.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk × equity × close
def f35mj_f35_margin_jerk_grossmargin_xequity_252d_slope_v081_signal(gp, revenue, equity, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 252) * equity.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × eps × close
def f35mj_f35_margin_jerk_netmargin_xeps_63d_slope_v082_signal(netinc, revenue, eps, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * eps * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × eps × close
def f35mj_f35_margin_jerk_opmargin_xeps_252d_slope_v083_signal(opinc, revenue, eps, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * eps * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × ncfo × close
def f35mj_f35_margin_jerk_netmargin_xncfo_63d_slope_v084_signal(netinc, revenue, ncfo, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * ncfo.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin jerk × ncfo × close
def f35mj_f35_margin_jerk_ebitdamargin_xncfo_252d_slope_v085_signal(ebitda, revenue, ncfo, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * ncfo.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × workingcapital × close
def f35mj_f35_margin_jerk_netmargin_xwc_63d_slope_v086_signal(netinc, revenue, workingcapital, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * workingcapital.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × workingcapital × close
def f35mj_f35_margin_jerk_opmargin_xwc_252d_slope_v087_signal(opinc, revenue, workingcapital, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * workingcapital.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk normalized by retvol × close
def f35mj_f35_margin_jerk_netmargin_normretvol_63d_slope_v088_signal(netinc, revenue, closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = _f35_margin_jerk_net(netinc, revenue, 63) / rv * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk normalized by retvol × close
def f35mj_f35_margin_jerk_opmargin_normretvol_252d_slope_v089_signal(opinc, revenue, closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = _f35_margin_jerk_op(opinc, revenue, 252) / rv * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × revenue trend × close
def f35mj_f35_margin_jerk_netmargin_xrevtrend_63d_slope_v090_signal(netinc, revenue, closeadj):
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    base = _f35_margin_jerk_net(netinc, revenue, 63) * rt * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite 3-jerk (252d) × close
def f35mj_f35_margin_jerk_composite_3jerk_252d_slope_v091_signal(netinc, opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252)
    b = _f35_margin_jerk_op(opinc, revenue, 252)
    c = _f35_margin_jerk_gross(gp, revenue, 252)
    base = (a + b + c) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_5d_slope_v092_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_10d_slope_v093_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 10) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_42d_slope_v094_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_189d_slope_v095_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 189) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_378d_slope_v096_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 378) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_5d_slope_v097_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_10d_slope_v098_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 10) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_42d_slope_v099_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_189d_slope_v100_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 189) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_378d_slope_v101_signal(opinc, revenue, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 378) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_5d_slope_v102_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_42d_slope_v103_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_189d_slope_v104_signal(gp, revenue, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 189) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_5d_slope_v105_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 5) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_42d_slope_v106_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 42) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d ebitda margin jerk × close
def f35mj_f35_margin_jerk_ebitdamargin_189d_slope_v107_signal(ebitda, revenue, closeadj):
    base = _f35_margin_jerk_ebitda(ebitda, revenue, 189) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × growth × close
def f35mj_f35_margin_jerk_netmargin_xgrowth_63d_slope_v108_signal(netinc, revenue, closeadj):
    g = revenue.pct_change(63)
    base = _f35_margin_jerk_net(netinc, revenue, 63) * g * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × growth × close
def f35mj_f35_margin_jerk_opmargin_xgrowth_252d_slope_v109_signal(opinc, revenue, closeadj):
    g = revenue.pct_change(252)
    base = _f35_margin_jerk_op(opinc, revenue, 252) * g * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk × growth × close
def f35mj_f35_margin_jerk_grossmargin_xgrowth_252d_slope_v110_signal(gp, revenue, closeadj):
    g = revenue.pct_change(252)
    base = _f35_margin_jerk_gross(gp, revenue, 252) * g * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × dollar volume
def f35mj_f35_margin_jerk_netmargin_xdv_63d_slope_v111_signal(netinc, revenue, closeadj, volume):
    dv = closeadj * volume
    base = _f35_margin_jerk_net(netinc, revenue, 63) * dv
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × dollar volume
def f35mj_f35_margin_jerk_opmargin_xdv_252d_slope_v112_signal(opinc, revenue, closeadj, volume):
    dv = closeadj * volume
    base = _f35_margin_jerk_op(opinc, revenue, 252) * dv
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × volume z × close
def f35mj_f35_margin_jerk_netmargin_xvolz_63d_slope_v113_signal(netinc, revenue, closeadj, volume):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * _z(volume, 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of net margin jerk × shortret × close
def f35mj_f35_margin_jerk_netmargin_xshortret_21d_slope_v114_signal(netinc, revenue, closeadj):
    r = closeadj.pct_change(5)
    base = _f35_margin_jerk_net(netinc, revenue, 21) * r * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of op margin jerk × longret × close
def f35mj_f35_margin_jerk_opmargin_xlongret_63d_slope_v115_signal(opinc, revenue, closeadj):
    r = closeadj.pct_change(126)
    base = _f35_margin_jerk_op(opinc, revenue, 63) * r * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk EMA (252d) × close
def f35mj_f35_margin_jerk_netmargin_ema_252d_slope_v116_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 252)
    base = j.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of op margin jerk EMA (21d) × close
def f35mj_f35_margin_jerk_opmargin_ema_21d_slope_v117_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gross margin jerk EMA (21d) × close
def f35mj_f35_margin_jerk_grossmargin_ema_21d_slope_v118_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ebitda margin jerk EMA (63d) × close
def f35mj_f35_margin_jerk_ebitdamargin_ema_63d_slope_v119_signal(ebitda, revenue, closeadj):
    j = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    base = j.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net jerk × ebitda jerk × close
def f35mj_f35_margin_jerk_netxebitda_63d_slope_v120_signal(netinc, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    base = a * b * closeadj * 100.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op jerk × gross jerk × close
def f35mj_f35_margin_jerk_opxgross_252d_slope_v121_signal(opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_op(opinc, revenue, 252)
    b = _f35_margin_jerk_gross(gp, revenue, 252)
    base = a * b * closeadj * 100.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net minus op × close
def f35mj_f35_margin_jerk_netminusop_63d_slope_v122_signal(netinc, opinc, revenue, closeadj):
    base = (_f35_margin_jerk_net(netinc, revenue, 63) - _f35_margin_jerk_op(opinc, revenue, 63)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda minus net × close
def f35mj_f35_margin_jerk_ebitdaminusnet_252d_slope_v123_signal(ebitda, netinc, revenue, closeadj):
    base = (_f35_margin_jerk_ebitda(ebitda, revenue, 252) - _f35_margin_jerk_net(netinc, revenue, 252)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of net margin jerk × intexp × close
def f35mj_f35_margin_jerk_netmargin_xintexp_21d_slope_v124_signal(netinc, revenue, intexp, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 21) * intexp.abs() * closeadj * 1e-5
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × taxexp × close
def f35mj_f35_margin_jerk_opmargin_xtaxexp_252d_slope_v125_signal(opinc, revenue, taxexp, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * taxexp.abs() * closeadj * 1e-5
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × capex × close
def f35mj_f35_margin_jerk_netmargin_xcapex_63d_slope_v126_signal(netinc, revenue, capex, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * capex.abs() * closeadj * 1e-5
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk × capex × close
def f35mj_f35_margin_jerk_grossmargin_xcapex_252d_slope_v127_signal(gp, revenue, capex, closeadj):
    base = _f35_margin_jerk_gross(gp, revenue, 252) * capex.abs() * closeadj * 1e-5
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × range × close
def f35mj_f35_margin_jerk_netmargin_xrange_63d_slope_v128_signal(netinc, revenue, closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f35_margin_jerk_net(netinc, revenue, 63) * rng * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × range × close
def f35mj_f35_margin_jerk_opmargin_xrange_252d_slope_v129_signal(opinc, revenue, closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f35_margin_jerk_op(opinc, revenue, 252) * rng * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × sqrt(rev) × close
def f35mj_f35_margin_jerk_netmargin_xrevsq_63d_slope_v130_signal(netinc, revenue, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * (revenue.abs() ** 0.5) * closeadj * 1e-3
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of meanof4 (252d) × close
def f35mj_f35_margin_jerk_meanof4_252d_slope_v131_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252)
    b = _f35_margin_jerk_op(opinc, revenue, 252)
    c = _f35_margin_jerk_gross(gp, revenue, 252)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 252)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of meanof4 (63d) × close
def f35mj_f35_margin_jerk_meanof4_63d_slope_v132_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_op(opinc, revenue, 63)
    c = _f35_margin_jerk_gross(gp, revenue, 63)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of meanof4 (21d) × close
def f35mj_f35_margin_jerk_meanof4_21d_slope_v133_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 21)
    b = _f35_margin_jerk_op(opinc, revenue, 21)
    c = _f35_margin_jerk_gross(gp, revenue, 21)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 21)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk dispersion (63d) × close
def f35mj_f35_margin_jerk_netmargin_dispersion_63d_slope_v134_signal(netinc, revenue, closeadj):
    base = _std(_f35_margin_jerk_net(netinc, revenue, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk dispersion (252d) × close
def f35mj_f35_margin_jerk_opmargin_dispersion_252d_slope_v135_signal(opinc, revenue, closeadj):
    base = _std(_f35_margin_jerk_op(opinc, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gross margin jerk dispersion (252d) × close
def f35mj_f35_margin_jerk_grossmargin_dispersion_252d_slope_v136_signal(gp, revenue, closeadj):
    base = _std(_f35_margin_jerk_gross(gp, revenue, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × sharesbas × close
def f35mj_f35_margin_jerk_netmargin_xsharesbas_63d_slope_v137_signal(netinc, revenue, sharesbas, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * sharesbas * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × sharesbas × close
def f35mj_f35_margin_jerk_opmargin_xsharesbas_252d_slope_v138_signal(opinc, revenue, sharesbas, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * sharesbas * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk × ncfi × close
def f35mj_f35_margin_jerk_netmargin_xncfi_252d_slope_v139_signal(netinc, revenue, ncfi, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 252) * ncfi.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × liab × close
def f35mj_f35_margin_jerk_netmargin_xliab_63d_slope_v140_signal(netinc, revenue, liabilities, closeadj):
    base = _f35_margin_jerk_net(netinc, revenue, 63) * liabilities.abs() * closeadj * 1e-6
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × liab × close
def f35mj_f35_margin_jerk_opmargin_xliab_252d_slope_v141_signal(opinc, revenue, liabilities, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * liabilities.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk range × close
def f35mj_f35_margin_jerk_netmargin_range_252d_slope_v142_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk range × close
def f35mj_f35_margin_jerk_opmargin_range_252d_slope_v143_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk skew (63d) × close
def f35mj_f35_margin_jerk_netmargin_skew_63d_slope_v144_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    base = j.rolling(63, min_periods=21).skew() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net margin jerk skew (252d) × close
def f35mj_f35_margin_jerk_netmargin_skew_252d_slope_v145_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    base = j.rolling(252, min_periods=63).skew() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net margin jerk × eps trend × close
def f35mj_f35_margin_jerk_netmargin_xepstrend_63d_slope_v146_signal(netinc, revenue, eps, closeadj):
    et = _diff(eps, 63)
    base = _f35_margin_jerk_net(netinc, revenue, 63) * et * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × ebitda growth × close
def f35mj_f35_margin_jerk_netmargin_xebitdagrowth_63d_slope_v147_signal(netinc, revenue, ebitda, closeadj):
    g = ebitda.pct_change(63)
    base = _f35_margin_jerk_net(netinc, revenue, 63) * g * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin jerk × fcf × close
def f35mj_f35_margin_jerk_opmargin_xfcf_252d_slope_v148_signal(opinc, revenue, fcf, closeadj):
    base = _f35_margin_jerk_op(opinc, revenue, 252) * fcf.abs() * closeadj * 1e-6
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of severitysum (252d) × close
def f35mj_f35_margin_jerk_severitysum_252d_slope_v149_signal(netinc, opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252).abs()
    b = _f35_margin_jerk_op(opinc, revenue, 252).abs()
    c = _f35_margin_jerk_gross(gp, revenue, 252).abs()
    base = (a + b + c) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of severityxrev (63d) × close
def f35mj_f35_margin_jerk_severityxrev_63d_slope_v150_signal(netinc, opinc, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63).abs()
    b = _f35_margin_jerk_op(opinc, revenue, 63).abs()
    base = (a + b) * revenue.abs() * closeadj * 1e-3
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35mj_f35_margin_jerk_netmargin_21d_slope_v001_signal,
    f35mj_f35_margin_jerk_netmargin_21d_slope_v002_signal,
    f35mj_f35_margin_jerk_netmargin_63d_slope_v003_signal,
    f35mj_f35_margin_jerk_netmargin_63d_slope_v004_signal,
    f35mj_f35_margin_jerk_netmargin_126d_slope_v005_signal,
    f35mj_f35_margin_jerk_netmargin_126d_slope_v006_signal,
    f35mj_f35_margin_jerk_netmargin_252d_slope_v007_signal,
    f35mj_f35_margin_jerk_netmargin_252d_slope_v008_signal,
    f35mj_f35_margin_jerk_opmargin_21d_slope_v009_signal,
    f35mj_f35_margin_jerk_opmargin_21d_slope_v010_signal,
    f35mj_f35_margin_jerk_opmargin_63d_slope_v011_signal,
    f35mj_f35_margin_jerk_opmargin_63d_slope_v012_signal,
    f35mj_f35_margin_jerk_opmargin_126d_slope_v013_signal,
    f35mj_f35_margin_jerk_opmargin_126d_slope_v014_signal,
    f35mj_f35_margin_jerk_opmargin_252d_slope_v015_signal,
    f35mj_f35_margin_jerk_opmargin_252d_slope_v016_signal,
    f35mj_f35_margin_jerk_grossmargin_21d_slope_v017_signal,
    f35mj_f35_margin_jerk_grossmargin_21d_slope_v018_signal,
    f35mj_f35_margin_jerk_grossmargin_63d_slope_v019_signal,
    f35mj_f35_margin_jerk_grossmargin_63d_slope_v020_signal,
    f35mj_f35_margin_jerk_grossmargin_126d_slope_v021_signal,
    f35mj_f35_margin_jerk_grossmargin_126d_slope_v022_signal,
    f35mj_f35_margin_jerk_grossmargin_252d_slope_v023_signal,
    f35mj_f35_margin_jerk_grossmargin_252d_slope_v024_signal,
    f35mj_f35_margin_jerk_ebitdamargin_21d_slope_v025_signal,
    f35mj_f35_margin_jerk_ebitdamargin_21d_slope_v026_signal,
    f35mj_f35_margin_jerk_ebitdamargin_63d_slope_v027_signal,
    f35mj_f35_margin_jerk_ebitdamargin_63d_slope_v028_signal,
    f35mj_f35_margin_jerk_ebitdamargin_126d_slope_v029_signal,
    f35mj_f35_margin_jerk_ebitdamargin_126d_slope_v030_signal,
    f35mj_f35_margin_jerk_ebitdamargin_252d_slope_v031_signal,
    f35mj_f35_margin_jerk_ebitdamargin_252d_slope_v032_signal,
    f35mj_f35_margin_jerk_netmargin_abs_21d_slope_v033_signal,
    f35mj_f35_margin_jerk_netmargin_abs_63d_slope_v034_signal,
    f35mj_f35_margin_jerk_netmargin_abs_126d_slope_v035_signal,
    f35mj_f35_margin_jerk_opmargin_sq_21d_slope_v036_signal,
    f35mj_f35_margin_jerk_opmargin_sq_63d_slope_v037_signal,
    f35mj_f35_margin_jerk_grossmargin_sq_252d_slope_v038_signal,
    f35mj_f35_margin_jerk_netmargin_mean_63d_slope_v039_signal,
    f35mj_f35_margin_jerk_netmargin_mean_252d_slope_v040_signal,
    f35mj_f35_margin_jerk_opmargin_mean_63d_slope_v041_signal,
    f35mj_f35_margin_jerk_grossmargin_mean_252d_slope_v042_signal,
    f35mj_f35_margin_jerk_netmargin_std_63d_slope_v043_signal,
    f35mj_f35_margin_jerk_opmargin_std_252d_slope_v044_signal,
    f35mj_f35_margin_jerk_ebitdamargin_std_252d_slope_v045_signal,
    f35mj_f35_margin_jerk_netmargin_z_252d_slope_v046_signal,
    f35mj_f35_margin_jerk_opmargin_z_252d_slope_v047_signal,
    f35mj_f35_margin_jerk_grossmargin_z_252d_slope_v048_signal,
    f35mj_f35_margin_jerk_ebitdamargin_z_252d_slope_v049_signal,
    f35mj_f35_margin_jerk_netmargin_xrev_63d_slope_v050_signal,
    f35mj_f35_margin_jerk_opmargin_xrev_252d_slope_v051_signal,
    f35mj_f35_margin_jerk_grossmargin_xrev_252d_slope_v052_signal,
    f35mj_f35_margin_jerk_netmargin_xebitda_63d_slope_v053_signal,
    f35mj_f35_margin_jerk_opmargin_xebitda_252d_slope_v054_signal,
    f35mj_f35_margin_jerk_netmargin_diff_63m252_slope_v055_signal,
    f35mj_f35_margin_jerk_opmargin_diff_21m63_slope_v056_signal,
    f35mj_f35_margin_jerk_grossvsnet_252d_slope_v057_signal,
    f35mj_f35_margin_jerk_ebitdavsnet_63d_slope_v058_signal,
    f35mj_f35_margin_jerk_netmargin_ema_21d_slope_v059_signal,
    f35mj_f35_margin_jerk_opmargin_ema_63d_slope_v060_signal,
    f35mj_f35_margin_jerk_grossmargin_ema_252d_slope_v061_signal,
    f35mj_f35_margin_jerk_netmargin_negcount_252d_slope_v062_signal,
    f35mj_f35_margin_jerk_opmargin_poscount_252d_slope_v063_signal,
    f35mj_f35_margin_jerk_netmargin_extremecount_504d_slope_v064_signal,
    f35mj_f35_margin_jerk_netmargin_sum_252d_slope_v065_signal,
    f35mj_f35_margin_jerk_opmargin_sum_252d_slope_v066_signal,
    f35mj_f35_margin_jerk_grossmargin_sum_252d_slope_v067_signal,
    f35mj_f35_margin_jerk_ebitdamargin_sum_252d_slope_v068_signal,
    f35mj_f35_margin_jerk_netmargin_xmom_21d_slope_v069_signal,
    f35mj_f35_margin_jerk_opmargin_xmom_63d_slope_v070_signal,
    f35mj_f35_margin_jerk_grossmargin_xmom_252d_slope_v071_signal,
    f35mj_f35_margin_jerk_netmargin_normrev_63d_slope_v072_signal,
    f35mj_f35_margin_jerk_opmargin_normrev_252d_slope_v073_signal,
    f35mj_f35_margin_jerk_netmargin_xato_63d_slope_v074_signal,
    f35mj_f35_margin_jerk_opmargin_xato_252d_slope_v075_signal,
    f35mj_f35_margin_jerk_netmargin_xcr_63d_slope_v076_signal,
    f35mj_f35_margin_jerk_opmargin_xcr_252d_slope_v077_signal,
    f35mj_f35_margin_jerk_netmargin_xdebt_63d_slope_v078_signal,
    f35mj_f35_margin_jerk_opmargin_xdebt_252d_slope_v079_signal,
    f35mj_f35_margin_jerk_netmargin_xequity_63d_slope_v080_signal,
    f35mj_f35_margin_jerk_grossmargin_xequity_252d_slope_v081_signal,
    f35mj_f35_margin_jerk_netmargin_xeps_63d_slope_v082_signal,
    f35mj_f35_margin_jerk_opmargin_xeps_252d_slope_v083_signal,
    f35mj_f35_margin_jerk_netmargin_xncfo_63d_slope_v084_signal,
    f35mj_f35_margin_jerk_ebitdamargin_xncfo_252d_slope_v085_signal,
    f35mj_f35_margin_jerk_netmargin_xwc_63d_slope_v086_signal,
    f35mj_f35_margin_jerk_opmargin_xwc_252d_slope_v087_signal,
    f35mj_f35_margin_jerk_netmargin_normretvol_63d_slope_v088_signal,
    f35mj_f35_margin_jerk_opmargin_normretvol_252d_slope_v089_signal,
    f35mj_f35_margin_jerk_netmargin_xrevtrend_63d_slope_v090_signal,
    f35mj_f35_margin_jerk_composite_3jerk_252d_slope_v091_signal,
    f35mj_f35_margin_jerk_netmargin_5d_slope_v092_signal,
    f35mj_f35_margin_jerk_netmargin_10d_slope_v093_signal,
    f35mj_f35_margin_jerk_netmargin_42d_slope_v094_signal,
    f35mj_f35_margin_jerk_netmargin_189d_slope_v095_signal,
    f35mj_f35_margin_jerk_netmargin_378d_slope_v096_signal,
    f35mj_f35_margin_jerk_opmargin_5d_slope_v097_signal,
    f35mj_f35_margin_jerk_opmargin_10d_slope_v098_signal,
    f35mj_f35_margin_jerk_opmargin_42d_slope_v099_signal,
    f35mj_f35_margin_jerk_opmargin_189d_slope_v100_signal,
    f35mj_f35_margin_jerk_opmargin_378d_slope_v101_signal,
    f35mj_f35_margin_jerk_grossmargin_5d_slope_v102_signal,
    f35mj_f35_margin_jerk_grossmargin_42d_slope_v103_signal,
    f35mj_f35_margin_jerk_grossmargin_189d_slope_v104_signal,
    f35mj_f35_margin_jerk_ebitdamargin_5d_slope_v105_signal,
    f35mj_f35_margin_jerk_ebitdamargin_42d_slope_v106_signal,
    f35mj_f35_margin_jerk_ebitdamargin_189d_slope_v107_signal,
    f35mj_f35_margin_jerk_netmargin_xgrowth_63d_slope_v108_signal,
    f35mj_f35_margin_jerk_opmargin_xgrowth_252d_slope_v109_signal,
    f35mj_f35_margin_jerk_grossmargin_xgrowth_252d_slope_v110_signal,
    f35mj_f35_margin_jerk_netmargin_xdv_63d_slope_v111_signal,
    f35mj_f35_margin_jerk_opmargin_xdv_252d_slope_v112_signal,
    f35mj_f35_margin_jerk_netmargin_xvolz_63d_slope_v113_signal,
    f35mj_f35_margin_jerk_netmargin_xshortret_21d_slope_v114_signal,
    f35mj_f35_margin_jerk_opmargin_xlongret_63d_slope_v115_signal,
    f35mj_f35_margin_jerk_netmargin_ema_252d_slope_v116_signal,
    f35mj_f35_margin_jerk_opmargin_ema_21d_slope_v117_signal,
    f35mj_f35_margin_jerk_grossmargin_ema_21d_slope_v118_signal,
    f35mj_f35_margin_jerk_ebitdamargin_ema_63d_slope_v119_signal,
    f35mj_f35_margin_jerk_netxebitda_63d_slope_v120_signal,
    f35mj_f35_margin_jerk_opxgross_252d_slope_v121_signal,
    f35mj_f35_margin_jerk_netminusop_63d_slope_v122_signal,
    f35mj_f35_margin_jerk_ebitdaminusnet_252d_slope_v123_signal,
    f35mj_f35_margin_jerk_netmargin_xintexp_21d_slope_v124_signal,
    f35mj_f35_margin_jerk_opmargin_xtaxexp_252d_slope_v125_signal,
    f35mj_f35_margin_jerk_netmargin_xcapex_63d_slope_v126_signal,
    f35mj_f35_margin_jerk_grossmargin_xcapex_252d_slope_v127_signal,
    f35mj_f35_margin_jerk_netmargin_xrange_63d_slope_v128_signal,
    f35mj_f35_margin_jerk_opmargin_xrange_252d_slope_v129_signal,
    f35mj_f35_margin_jerk_netmargin_xrevsq_63d_slope_v130_signal,
    f35mj_f35_margin_jerk_meanof4_252d_slope_v131_signal,
    f35mj_f35_margin_jerk_meanof4_63d_slope_v132_signal,
    f35mj_f35_margin_jerk_meanof4_21d_slope_v133_signal,
    f35mj_f35_margin_jerk_netmargin_dispersion_63d_slope_v134_signal,
    f35mj_f35_margin_jerk_opmargin_dispersion_252d_slope_v135_signal,
    f35mj_f35_margin_jerk_grossmargin_dispersion_252d_slope_v136_signal,
    f35mj_f35_margin_jerk_netmargin_xsharesbas_63d_slope_v137_signal,
    f35mj_f35_margin_jerk_opmargin_xsharesbas_252d_slope_v138_signal,
    f35mj_f35_margin_jerk_netmargin_xncfi_252d_slope_v139_signal,
    f35mj_f35_margin_jerk_netmargin_xliab_63d_slope_v140_signal,
    f35mj_f35_margin_jerk_opmargin_xliab_252d_slope_v141_signal,
    f35mj_f35_margin_jerk_netmargin_range_252d_slope_v142_signal,
    f35mj_f35_margin_jerk_opmargin_range_252d_slope_v143_signal,
    f35mj_f35_margin_jerk_netmargin_skew_63d_slope_v144_signal,
    f35mj_f35_margin_jerk_netmargin_skew_252d_slope_v145_signal,
    f35mj_f35_margin_jerk_netmargin_xepstrend_63d_slope_v146_signal,
    f35mj_f35_margin_jerk_netmargin_xebitdagrowth_63d_slope_v147_signal,
    f35mj_f35_margin_jerk_opmargin_xfcf_252d_slope_v148_signal,
    f35mj_f35_margin_jerk_severitysum_252d_slope_v149_signal,
    f35mj_f35_margin_jerk_severityxrev_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_MARGIN_JERK_REGISTRY_SLOPE = REGISTRY


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
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    opinc = pd.Series(1.5e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.011, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="opinc")
    gp = pd.Series(3e6 * np.exp(np.cumsum(np.random.normal(0.0007, 0.009, n))), name="gp")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    ncfi = pd.Series(7e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))) * np.sign(np.random.normal(0.4, 1.0, n)), name="ncfi")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    liabilities = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="liabilities")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "opinc": opinc, "gp": gp, "ebitda": ebitda,
        "eps": eps, "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas, "liabilities": liabilities,
        "assets": assets, "debt": debt, "equity": equity, "workingcapital": workingcapital, "currentratio": currentratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_margin_jerk_net", "_f35_margin_jerk_op", "_f35_margin_jerk_gross", "_f35_margin_jerk_ebitda")
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
    print(f"OK f35_margin_jerk_2nd_derivatives_001_150_claude: {n_features} features pass")
