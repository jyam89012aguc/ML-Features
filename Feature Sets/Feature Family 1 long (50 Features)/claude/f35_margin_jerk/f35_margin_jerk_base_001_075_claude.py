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


# ===== folder domain primitives (margin jerk = 3rd derivative of margin) =====
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


# 21d net-margin jerk scaled by close
def f35mj_f35_margin_jerk_netmargin_21d_base_v001_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-margin jerk scaled by close
def f35mj_f35_margin_jerk_netmargin_63d_base_v002_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-margin jerk scaled by close
def f35mj_f35_margin_jerk_netmargin_126d_base_v003_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-margin jerk scaled by close
def f35mj_f35_margin_jerk_netmargin_252d_base_v004_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d operating margin jerk scaled by close
def f35mj_f35_margin_jerk_opmargin_21d_base_v005_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin jerk scaled by close
def f35mj_f35_margin_jerk_opmargin_63d_base_v006_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d operating margin jerk scaled by close
def f35mj_f35_margin_jerk_opmargin_126d_base_v007_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin jerk scaled by close
def f35mj_f35_margin_jerk_opmargin_252d_base_v008_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gross margin jerk scaled by close
def f35mj_f35_margin_jerk_grossmargin_21d_base_v009_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin jerk scaled by close
def f35mj_f35_margin_jerk_grossmargin_63d_base_v010_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gross margin jerk scaled by close
def f35mj_f35_margin_jerk_grossmargin_126d_base_v011_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk scaled by close
def f35mj_f35_margin_jerk_grossmargin_252d_base_v012_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda margin jerk scaled by close
def f35mj_f35_margin_jerk_ebitdamargin_21d_base_v013_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda margin jerk scaled by close
def f35mj_f35_margin_jerk_ebitdamargin_63d_base_v014_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ebitda margin jerk scaled by close
def f35mj_f35_margin_jerk_ebitdamargin_126d_base_v015_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin jerk scaled by close
def f35mj_f35_margin_jerk_ebitdamargin_252d_base_v016_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin jerk magnitude (abs)
def f35mj_f35_margin_jerk_netmargin_abs_21d_base_v017_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk magnitude
def f35mj_f35_margin_jerk_netmargin_abs_63d_base_v018_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net margin jerk magnitude
def f35mj_f35_margin_jerk_netmargin_abs_126d_base_v019_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d op margin jerk squared
def f35mj_f35_margin_jerk_opmargin_sq_21d_base_v020_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    result = j * j.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d op margin jerk squared
def f35mj_f35_margin_jerk_opmargin_sq_63d_base_v021_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    result = j * j.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk squared
def f35mj_f35_margin_jerk_grossmargin_sq_252d_base_v022_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 252)
    result = j * j.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of net margin jerk
def f35mj_f35_margin_jerk_netmargin_mean_63d_base_v023_signal(netinc, revenue, closeadj):
    result = _mean(_f35_margin_jerk_net(netinc, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of net margin jerk
def f35mj_f35_margin_jerk_netmargin_mean_252d_base_v024_signal(netinc, revenue, closeadj):
    result = _mean(_f35_margin_jerk_net(netinc, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of op margin jerk
def f35mj_f35_margin_jerk_opmargin_mean_63d_base_v025_signal(opinc, revenue, closeadj):
    result = _mean(_f35_margin_jerk_op(opinc, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_mean_252d_base_v026_signal(gp, revenue, closeadj):
    result = _mean(_f35_margin_jerk_gross(gp, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of net margin jerk
def f35mj_f35_margin_jerk_netmargin_std_63d_base_v027_signal(netinc, revenue, closeadj):
    result = _std(_f35_margin_jerk_net(netinc, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of op margin jerk
def f35mj_f35_margin_jerk_opmargin_std_252d_base_v028_signal(opinc, revenue, closeadj):
    result = _std(_f35_margin_jerk_op(opinc, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_std_252d_base_v029_signal(ebitda, revenue, closeadj):
    result = _std(_f35_margin_jerk_ebitda(ebitda, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of net margin jerk
def f35mj_f35_margin_jerk_netmargin_z_252d_base_v030_signal(netinc, revenue, closeadj):
    result = _z(_f35_margin_jerk_net(netinc, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of op margin jerk
def f35mj_f35_margin_jerk_opmargin_z_252d_base_v031_signal(opinc, revenue, closeadj):
    result = _z(_f35_margin_jerk_op(opinc, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_z_252d_base_v032_signal(gp, revenue, closeadj):
    result = _z(_f35_margin_jerk_gross(gp, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_z_252d_base_v033_signal(ebitda, revenue, closeadj):
    result = _z(_f35_margin_jerk_ebitda(ebitda, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk weighted by revenue level
def f35mj_f35_margin_jerk_netmargin_xrev_63d_base_v034_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk weighted by revenue level
def f35mj_f35_margin_jerk_opmargin_xrev_252d_base_v035_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk weighted by revenue level
def f35mj_f35_margin_jerk_grossmargin_xrev_252d_base_v036_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 252) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × ebitda
def f35mj_f35_margin_jerk_netmargin_xebitda_63d_base_v037_signal(netinc, revenue, ebitda, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × ebitda
def f35mj_f35_margin_jerk_opmargin_xebitda_252d_base_v038_signal(opinc, revenue, ebitda, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk minus 252d net margin jerk
def f35mj_f35_margin_jerk_netmargin_diff_63m252_base_v039_signal(netinc, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_net(netinc, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d op margin jerk minus 63d op margin jerk
def f35mj_f35_margin_jerk_opmargin_diff_21m63_base_v040_signal(opinc, revenue, closeadj):
    a = _f35_margin_jerk_op(opinc, revenue, 21)
    b = _f35_margin_jerk_op(opinc, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk minus 252d net margin jerk (mix shift)
def f35mj_f35_margin_jerk_grossvsnet_252d_base_v041_signal(gp, netinc, revenue, closeadj):
    a = _f35_margin_jerk_gross(gp, revenue, 252)
    b = _f35_margin_jerk_net(netinc, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda jerk minus 63d net jerk
def f35mj_f35_margin_jerk_ebitdavsnet_63d_base_v042_signal(ebitda, netinc, revenue, closeadj):
    a = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    b = _f35_margin_jerk_net(netinc, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of net margin jerk
def f35mj_f35_margin_jerk_netmargin_ema_21d_base_v043_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of op margin jerk
def f35mj_f35_margin_jerk_opmargin_ema_63d_base_v044_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    result = j.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_ema_252d_base_v045_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 252)
    result = j.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of negative net margin jerk days
def f35mj_f35_margin_jerk_netmargin_negcount_252d_base_v046_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    result = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of positive op margin jerk days
def f35mj_f35_margin_jerk_opmargin_poscount_252d_base_v047_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 63)
    result = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of large jerk events (|jerk|>2sigma) for net margin
def f35mj_f35_margin_jerk_netmargin_extremecount_504d_base_v048_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    z = _z(j, 252)
    flag = (z.abs() > 2.0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of net margin jerk
def f35mj_f35_margin_jerk_netmargin_sum_252d_base_v049_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of op margin jerk
def f35mj_f35_margin_jerk_opmargin_sum_252d_base_v050_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_sum_252d_base_v051_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_sum_252d_base_v052_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin jerk × close-momentum
def f35mj_f35_margin_jerk_netmargin_xmom_21d_base_v053_signal(netinc, revenue, closeadj):
    mom = closeadj.pct_change(21)
    result = _f35_margin_jerk_net(netinc, revenue, 21) * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d op margin jerk × close-momentum
def f35mj_f35_margin_jerk_opmargin_xmom_63d_base_v054_signal(opinc, revenue, closeadj):
    mom = closeadj.pct_change(63)
    result = _f35_margin_jerk_op(opinc, revenue, 63) * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk × close-momentum
def f35mj_f35_margin_jerk_grossmargin_xmom_252d_base_v055_signal(gp, revenue, closeadj):
    mom = closeadj.pct_change(252)
    result = _f35_margin_jerk_gross(gp, revenue, 252) * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk normalized by 63d revenue std
def f35mj_f35_margin_jerk_netmargin_normrev_63d_base_v056_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 63)
    rs = _std(revenue, 63).replace(0, np.nan)
    result = j / rs * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk normalized by revenue std
def f35mj_f35_margin_jerk_opmargin_normrev_252d_base_v057_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 252)
    rs = _std(revenue, 252).replace(0, np.nan)
    result = j / rs * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × asset turnover proxy (rev/assets)
def f35mj_f35_margin_jerk_netmargin_xato_63d_base_v058_signal(netinc, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    result = _f35_margin_jerk_net(netinc, revenue, 63) * ato * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × asset turnover
def f35mj_f35_margin_jerk_opmargin_xato_252d_base_v059_signal(opinc, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    result = _f35_margin_jerk_op(opinc, revenue, 252) * ato * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × current ratio
def f35mj_f35_margin_jerk_netmargin_xcr_63d_base_v060_signal(netinc, revenue, currentratio, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × current ratio
def f35mj_f35_margin_jerk_opmargin_xcr_252d_base_v061_signal(opinc, revenue, currentratio, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × debt level (leverage-amplified)
def f35mj_f35_margin_jerk_netmargin_xdebt_63d_base_v062_signal(netinc, revenue, debt, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * debt.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × debt level
def f35mj_f35_margin_jerk_opmargin_xdebt_252d_base_v063_signal(opinc, revenue, debt, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * debt.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × equity (size-scaled)
def f35mj_f35_margin_jerk_netmargin_xequity_63d_base_v064_signal(netinc, revenue, equity, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * equity.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk × equity
def f35mj_f35_margin_jerk_grossmargin_xequity_252d_base_v065_signal(gp, revenue, equity, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 252) * equity.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × eps
def f35mj_f35_margin_jerk_netmargin_xeps_63d_base_v066_signal(netinc, revenue, eps, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × eps
def f35mj_f35_margin_jerk_opmargin_xeps_252d_base_v067_signal(opinc, revenue, eps, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × ncfo
def f35mj_f35_margin_jerk_netmargin_xncfo_63d_base_v068_signal(netinc, revenue, ncfo, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * ncfo.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin jerk × ncfo
def f35mj_f35_margin_jerk_ebitdamargin_xncfo_252d_base_v069_signal(ebitda, revenue, ncfo, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * ncfo.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × workingcapital
def f35mj_f35_margin_jerk_netmargin_xwc_63d_base_v070_signal(netinc, revenue, workingcapital, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * workingcapital.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × workingcapital
def f35mj_f35_margin_jerk_opmargin_xwc_252d_base_v071_signal(opinc, revenue, workingcapital, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * workingcapital.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk normalized by 21d return volatility
def f35mj_f35_margin_jerk_netmargin_normretvol_63d_base_v072_signal(netinc, revenue, closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = _f35_margin_jerk_net(netinc, revenue, 63) / rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk normalized by 63d return volatility
def f35mj_f35_margin_jerk_opmargin_normretvol_252d_base_v073_signal(opinc, revenue, closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = _f35_margin_jerk_op(opinc, revenue, 252) / rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × revenue trend (rev pct change)
def f35mj_f35_margin_jerk_netmargin_xrevtrend_63d_base_v074_signal(netinc, revenue, closeadj):
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    result = _f35_margin_jerk_net(netinc, revenue, 63) * rt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: net margin jerk + op margin jerk + gross margin jerk all × close
def f35mj_f35_margin_jerk_composite_3jerk_252d_base_v075_signal(netinc, opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252)
    b = _f35_margin_jerk_op(opinc, revenue, 252)
    c = _f35_margin_jerk_gross(gp, revenue, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35mj_f35_margin_jerk_netmargin_21d_base_v001_signal,
    f35mj_f35_margin_jerk_netmargin_63d_base_v002_signal,
    f35mj_f35_margin_jerk_netmargin_126d_base_v003_signal,
    f35mj_f35_margin_jerk_netmargin_252d_base_v004_signal,
    f35mj_f35_margin_jerk_opmargin_21d_base_v005_signal,
    f35mj_f35_margin_jerk_opmargin_63d_base_v006_signal,
    f35mj_f35_margin_jerk_opmargin_126d_base_v007_signal,
    f35mj_f35_margin_jerk_opmargin_252d_base_v008_signal,
    f35mj_f35_margin_jerk_grossmargin_21d_base_v009_signal,
    f35mj_f35_margin_jerk_grossmargin_63d_base_v010_signal,
    f35mj_f35_margin_jerk_grossmargin_126d_base_v011_signal,
    f35mj_f35_margin_jerk_grossmargin_252d_base_v012_signal,
    f35mj_f35_margin_jerk_ebitdamargin_21d_base_v013_signal,
    f35mj_f35_margin_jerk_ebitdamargin_63d_base_v014_signal,
    f35mj_f35_margin_jerk_ebitdamargin_126d_base_v015_signal,
    f35mj_f35_margin_jerk_ebitdamargin_252d_base_v016_signal,
    f35mj_f35_margin_jerk_netmargin_abs_21d_base_v017_signal,
    f35mj_f35_margin_jerk_netmargin_abs_63d_base_v018_signal,
    f35mj_f35_margin_jerk_netmargin_abs_126d_base_v019_signal,
    f35mj_f35_margin_jerk_opmargin_sq_21d_base_v020_signal,
    f35mj_f35_margin_jerk_opmargin_sq_63d_base_v021_signal,
    f35mj_f35_margin_jerk_grossmargin_sq_252d_base_v022_signal,
    f35mj_f35_margin_jerk_netmargin_mean_63d_base_v023_signal,
    f35mj_f35_margin_jerk_netmargin_mean_252d_base_v024_signal,
    f35mj_f35_margin_jerk_opmargin_mean_63d_base_v025_signal,
    f35mj_f35_margin_jerk_grossmargin_mean_252d_base_v026_signal,
    f35mj_f35_margin_jerk_netmargin_std_63d_base_v027_signal,
    f35mj_f35_margin_jerk_opmargin_std_252d_base_v028_signal,
    f35mj_f35_margin_jerk_ebitdamargin_std_252d_base_v029_signal,
    f35mj_f35_margin_jerk_netmargin_z_252d_base_v030_signal,
    f35mj_f35_margin_jerk_opmargin_z_252d_base_v031_signal,
    f35mj_f35_margin_jerk_grossmargin_z_252d_base_v032_signal,
    f35mj_f35_margin_jerk_ebitdamargin_z_252d_base_v033_signal,
    f35mj_f35_margin_jerk_netmargin_xrev_63d_base_v034_signal,
    f35mj_f35_margin_jerk_opmargin_xrev_252d_base_v035_signal,
    f35mj_f35_margin_jerk_grossmargin_xrev_252d_base_v036_signal,
    f35mj_f35_margin_jerk_netmargin_xebitda_63d_base_v037_signal,
    f35mj_f35_margin_jerk_opmargin_xebitda_252d_base_v038_signal,
    f35mj_f35_margin_jerk_netmargin_diff_63m252_base_v039_signal,
    f35mj_f35_margin_jerk_opmargin_diff_21m63_base_v040_signal,
    f35mj_f35_margin_jerk_grossvsnet_252d_base_v041_signal,
    f35mj_f35_margin_jerk_ebitdavsnet_63d_base_v042_signal,
    f35mj_f35_margin_jerk_netmargin_ema_21d_base_v043_signal,
    f35mj_f35_margin_jerk_opmargin_ema_63d_base_v044_signal,
    f35mj_f35_margin_jerk_grossmargin_ema_252d_base_v045_signal,
    f35mj_f35_margin_jerk_netmargin_negcount_252d_base_v046_signal,
    f35mj_f35_margin_jerk_opmargin_poscount_252d_base_v047_signal,
    f35mj_f35_margin_jerk_netmargin_extremecount_504d_base_v048_signal,
    f35mj_f35_margin_jerk_netmargin_sum_252d_base_v049_signal,
    f35mj_f35_margin_jerk_opmargin_sum_252d_base_v050_signal,
    f35mj_f35_margin_jerk_grossmargin_sum_252d_base_v051_signal,
    f35mj_f35_margin_jerk_ebitdamargin_sum_252d_base_v052_signal,
    f35mj_f35_margin_jerk_netmargin_xmom_21d_base_v053_signal,
    f35mj_f35_margin_jerk_opmargin_xmom_63d_base_v054_signal,
    f35mj_f35_margin_jerk_grossmargin_xmom_252d_base_v055_signal,
    f35mj_f35_margin_jerk_netmargin_normrev_63d_base_v056_signal,
    f35mj_f35_margin_jerk_opmargin_normrev_252d_base_v057_signal,
    f35mj_f35_margin_jerk_netmargin_xato_63d_base_v058_signal,
    f35mj_f35_margin_jerk_opmargin_xato_252d_base_v059_signal,
    f35mj_f35_margin_jerk_netmargin_xcr_63d_base_v060_signal,
    f35mj_f35_margin_jerk_opmargin_xcr_252d_base_v061_signal,
    f35mj_f35_margin_jerk_netmargin_xdebt_63d_base_v062_signal,
    f35mj_f35_margin_jerk_opmargin_xdebt_252d_base_v063_signal,
    f35mj_f35_margin_jerk_netmargin_xequity_63d_base_v064_signal,
    f35mj_f35_margin_jerk_grossmargin_xequity_252d_base_v065_signal,
    f35mj_f35_margin_jerk_netmargin_xeps_63d_base_v066_signal,
    f35mj_f35_margin_jerk_opmargin_xeps_252d_base_v067_signal,
    f35mj_f35_margin_jerk_netmargin_xncfo_63d_base_v068_signal,
    f35mj_f35_margin_jerk_ebitdamargin_xncfo_252d_base_v069_signal,
    f35mj_f35_margin_jerk_netmargin_xwc_63d_base_v070_signal,
    f35mj_f35_margin_jerk_opmargin_xwc_252d_base_v071_signal,
    f35mj_f35_margin_jerk_netmargin_normretvol_63d_base_v072_signal,
    f35mj_f35_margin_jerk_opmargin_normretvol_252d_base_v073_signal,
    f35mj_f35_margin_jerk_netmargin_xrevtrend_63d_base_v074_signal,
    f35mj_f35_margin_jerk_composite_3jerk_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_MARGIN_JERK_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    opinc = pd.Series(1.5e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.011, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="opinc")
    gp = pd.Series(3e6 * np.exp(np.cumsum(np.random.normal(0.0007, 0.009, n))), name="gp")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "opinc": opinc,
        "gp": gp, "ebitda": ebitda, "assets": assets, "debt": debt, "equity": equity,
        "eps": eps, "ncfo": ncfo, "workingcapital": workingcapital, "currentratio": currentratio,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f35_margin_jerk_base_001_075_claude: {n_features} features pass")
