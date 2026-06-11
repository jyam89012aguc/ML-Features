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


# ===== folder domain primitives (margin jerk) =====
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


# 5d short-window net margin jerk
def f35mj_f35_margin_jerk_netmargin_5d_base_v076_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d short-window net margin jerk
def f35mj_f35_margin_jerk_netmargin_10d_base_v077_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d net margin jerk
def f35mj_f35_margin_jerk_netmargin_42d_base_v078_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d net margin jerk
def f35mj_f35_margin_jerk_netmargin_189d_base_v079_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d net margin jerk
def f35mj_f35_margin_jerk_netmargin_378d_base_v080_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d op margin jerk
def f35mj_f35_margin_jerk_opmargin_5d_base_v081_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d op margin jerk
def f35mj_f35_margin_jerk_opmargin_10d_base_v082_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d op margin jerk
def f35mj_f35_margin_jerk_opmargin_42d_base_v083_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d op margin jerk
def f35mj_f35_margin_jerk_opmargin_189d_base_v084_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d op margin jerk
def f35mj_f35_margin_jerk_opmargin_378d_base_v085_signal(opinc, revenue, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_5d_base_v086_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_42d_base_v087_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_189d_base_v088_signal(gp, revenue, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_5d_base_v089_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_42d_base_v090_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ebitda margin jerk
def f35mj_f35_margin_jerk_ebitdamargin_189d_base_v091_signal(ebitda, revenue, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × revenue growth pct
def f35mj_f35_margin_jerk_netmargin_xgrowth_63d_base_v092_signal(netinc, revenue, closeadj):
    g = revenue.pct_change(63)
    result = _f35_margin_jerk_net(netinc, revenue, 63) * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × revenue growth
def f35mj_f35_margin_jerk_opmargin_xgrowth_252d_base_v093_signal(opinc, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _f35_margin_jerk_op(opinc, revenue, 252) * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk × revenue growth
def f35mj_f35_margin_jerk_grossmargin_xgrowth_252d_base_v094_signal(gp, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _f35_margin_jerk_gross(gp, revenue, 252) * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × dollar volume
def f35mj_f35_margin_jerk_netmargin_xdv_63d_base_v095_signal(netinc, revenue, closeadj, volume):
    dv = closeadj * volume
    result = _f35_margin_jerk_net(netinc, revenue, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × dollar volume
def f35mj_f35_margin_jerk_opmargin_xdv_252d_base_v096_signal(opinc, revenue, closeadj, volume):
    dv = closeadj * volume
    result = _f35_margin_jerk_op(opinc, revenue, 252) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × volume zscore
def f35mj_f35_margin_jerk_netmargin_xvolz_63d_base_v097_signal(netinc, revenue, closeadj, volume):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin jerk × short-term return
def f35mj_f35_margin_jerk_netmargin_xshortret_21d_base_v098_signal(netinc, revenue, closeadj):
    r = closeadj.pct_change(5)
    result = _f35_margin_jerk_net(netinc, revenue, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d op margin jerk × longer-term return
def f35mj_f35_margin_jerk_opmargin_xlongret_63d_base_v099_signal(opinc, revenue, closeadj):
    r = closeadj.pct_change(126)
    result = _f35_margin_jerk_op(opinc, revenue, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin jerk EMA × close
def f35mj_f35_margin_jerk_netmargin_ema_252d_base_v100_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 252)
    result = j.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d op margin jerk EMA × close
def f35mj_f35_margin_jerk_opmargin_ema_21d_base_v101_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gross margin jerk EMA × close
def f35mj_f35_margin_jerk_grossmargin_ema_21d_base_v102_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda margin jerk EMA × close
def f35mj_f35_margin_jerk_ebitdamargin_ema_63d_base_v103_signal(ebitda, revenue, closeadj):
    j = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    result = j.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × ebitda margin jerk (correlated jerk)
def f35mj_f35_margin_jerk_netxebitda_63d_base_v104_signal(netinc, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    result = a * b * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × gross margin jerk
def f35mj_f35_margin_jerk_opxgross_252d_base_v105_signal(opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_op(opinc, revenue, 252)
    b = _f35_margin_jerk_gross(gp, revenue, 252)
    result = a * b * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk minus op margin jerk
def f35mj_f35_margin_jerk_netminusop_63d_base_v106_signal(netinc, opinc, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_op(opinc, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin jerk minus net margin jerk (D&A jerk proxy)
def f35mj_f35_margin_jerk_ebitdaminusnet_252d_base_v107_signal(ebitda, netinc, revenue, closeadj):
    a = _f35_margin_jerk_ebitda(ebitda, revenue, 252)
    b = _f35_margin_jerk_net(netinc, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin jerk × interest expense (debt-burden interaction)
def f35mj_f35_margin_jerk_netmargin_xintexp_21d_base_v108_signal(netinc, revenue, intexp, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 21) * intexp.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × tax expense
def f35mj_f35_margin_jerk_opmargin_xtaxexp_252d_base_v109_signal(opinc, revenue, taxexp, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * taxexp.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × capex (capital intensity adjusted jerk)
def f35mj_f35_margin_jerk_netmargin_xcapex_63d_base_v110_signal(netinc, revenue, capex, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * capex.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk × capex
def f35mj_f35_margin_jerk_grossmargin_xcapex_252d_base_v111_signal(gp, revenue, capex, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 252) * capex.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × ATR-style range (volatility-amplified)
def f35mj_f35_margin_jerk_netmargin_xrange_63d_base_v112_signal(netinc, revenue, closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f35_margin_jerk_net(netinc, revenue, 63) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × ATR-style range
def f35mj_f35_margin_jerk_opmargin_xrange_252d_base_v113_signal(opinc, revenue, closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f35_margin_jerk_op(opinc, revenue, 252) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × revenue squared (size-amplified)
def f35mj_f35_margin_jerk_netmargin_xrevsq_63d_base_v114_signal(netinc, revenue, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * (revenue.abs() ** 0.5) * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite jerk (mean of all 4 margin jerks)
def f35mj_f35_margin_jerk_meanof4_252d_base_v115_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252)
    b = _f35_margin_jerk_op(opinc, revenue, 252)
    c = _f35_margin_jerk_gross(gp, revenue, 252)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 252)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite jerk
def f35mj_f35_margin_jerk_meanof4_63d_base_v116_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63)
    b = _f35_margin_jerk_op(opinc, revenue, 63)
    c = _f35_margin_jerk_gross(gp, revenue, 63)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 63)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite jerk
def f35mj_f35_margin_jerk_meanof4_21d_base_v117_signal(netinc, opinc, gp, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 21)
    b = _f35_margin_jerk_op(opinc, revenue, 21)
    c = _f35_margin_jerk_gross(gp, revenue, 21)
    d = _f35_margin_jerk_ebitda(ebitda, revenue, 21)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of net margin jerk × close
def f35mj_f35_margin_jerk_netmargin_dispersion_63d_base_v118_signal(netinc, revenue, closeadj):
    result = _std(_f35_margin_jerk_net(netinc, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_dispersion_252d_base_v119_signal(opinc, revenue, closeadj):
    result = _std(_f35_margin_jerk_op(opinc, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of gross margin jerk × close
def f35mj_f35_margin_jerk_grossmargin_dispersion_252d_base_v120_signal(gp, revenue, closeadj):
    result = _std(_f35_margin_jerk_gross(gp, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × sharesbas (dilution interaction)
def f35mj_f35_margin_jerk_netmargin_xsharesbas_63d_base_v121_signal(netinc, revenue, sharesbas, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * sharesbas * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × sharesbas
def f35mj_f35_margin_jerk_opmargin_xsharesbas_252d_base_v122_signal(opinc, revenue, sharesbas, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * sharesbas * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin jerk × ncfi (investment cash interaction)
def f35mj_f35_margin_jerk_netmargin_xncfi_252d_base_v123_signal(netinc, revenue, ncfi, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 252) * ncfi.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × liabilities (leverage-jerk)
def f35mj_f35_margin_jerk_netmargin_xliab_63d_base_v124_signal(netinc, revenue, liabilities, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * liabilities.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × liabilities
def f35mj_f35_margin_jerk_opmargin_xliab_252d_base_v125_signal(opinc, revenue, liabilities, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * liabilities.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of net margin jerk (max - min) × close
def f35mj_f35_margin_jerk_netmargin_range_252d_base_v126_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of op margin jerk × close
def f35mj_f35_margin_jerk_opmargin_range_252d_base_v127_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of gross margin jerk
def f35mj_f35_margin_jerk_grossmargin_range_504d_base_v128_signal(gp, revenue, closeadj):
    j = _f35_margin_jerk_gross(gp, revenue, 63)
    rng = j.rolling(504, min_periods=126).max() - j.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk skew × close
def f35mj_f35_margin_jerk_netmargin_skew_63d_base_v129_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    result = j.rolling(63, min_periods=21).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin jerk skew × close
def f35mj_f35_margin_jerk_netmargin_skew_252d_base_v130_signal(netinc, revenue, closeadj):
    j = _f35_margin_jerk_net(netinc, revenue, 21)
    result = j.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk kurtosis × close
def f35mj_f35_margin_jerk_opmargin_kurt_252d_base_v131_signal(opinc, revenue, closeadj):
    j = _f35_margin_jerk_op(opinc, revenue, 21)
    result = j.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × eps trend
def f35mj_f35_margin_jerk_netmargin_xepstrend_63d_base_v132_signal(netinc, revenue, eps, closeadj):
    et = _diff(eps, 63)
    result = _f35_margin_jerk_net(netinc, revenue, 63) * et * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × eps trend
def f35mj_f35_margin_jerk_opmargin_xepstrend_252d_base_v133_signal(opinc, revenue, eps, closeadj):
    et = _diff(eps, 252)
    result = _f35_margin_jerk_op(opinc, revenue, 252) * et * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × ebitda growth
def f35mj_f35_margin_jerk_netmargin_xebitdagrowth_63d_base_v134_signal(netinc, revenue, ebitda, closeadj):
    g = ebitda.pct_change(63)
    result = _f35_margin_jerk_net(netinc, revenue, 63) * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × fcf
def f35mj_f35_margin_jerk_opmargin_xfcf_252d_base_v135_signal(opinc, revenue, fcf, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * fcf.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin jerk × fcf
def f35mj_f35_margin_jerk_grossmargin_xfcf_63d_base_v136_signal(gp, revenue, fcf, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 63) * fcf.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin jerk × ncff (financing-cash interaction)
def f35mj_f35_margin_jerk_ebitdamargin_xncff_252d_base_v137_signal(ebitda, revenue, ncff, closeadj):
    result = _f35_margin_jerk_ebitda(ebitda, revenue, 252) * ncff.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net margin jerk minus 252d ebitda margin jerk
def f35mj_f35_margin_jerk_netvsebitda_252d_base_v138_signal(netinc, ebitda, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252)
    b = _f35_margin_jerk_ebitda(ebitda, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin jerk minus 63d op margin jerk (overhead jerk)
def f35mj_f35_margin_jerk_grossvsop_63d_base_v139_signal(gp, opinc, revenue, closeadj):
    a = _f35_margin_jerk_gross(gp, revenue, 63)
    b = _f35_margin_jerk_op(opinc, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk minus 252d op margin jerk
def f35mj_f35_margin_jerk_grossvsop_252d_base_v140_signal(gp, opinc, revenue, closeadj):
    a = _f35_margin_jerk_gross(gp, revenue, 252)
    b = _f35_margin_jerk_op(opinc, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × retained earnings
def f35mj_f35_margin_jerk_netmargin_xretearn_63d_base_v141_signal(netinc, revenue, retearn, closeadj):
    result = _f35_margin_jerk_net(netinc, revenue, 63) * retearn.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × retained earnings
def f35mj_f35_margin_jerk_opmargin_xretearn_252d_base_v142_signal(opinc, revenue, retearn, closeadj):
    result = _f35_margin_jerk_op(opinc, revenue, 252) * retearn.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross margin jerk × retained earnings
def f35mj_f35_margin_jerk_grossmargin_xretearn_252d_base_v143_signal(gp, revenue, retearn, closeadj):
    result = _f35_margin_jerk_gross(gp, revenue, 252) * retearn.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × volume sum
def f35mj_f35_margin_jerk_netmargin_xvolsum_63d_base_v144_signal(netinc, revenue, closeadj, volume):
    vs = volume.rolling(21, min_periods=5).sum()
    result = _f35_margin_jerk_net(netinc, revenue, 63) * vs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × dollar-volume sum
def f35mj_f35_margin_jerk_opmargin_xdvsum_252d_base_v145_signal(opinc, revenue, closeadj, volume):
    dvs = (closeadj * volume).rolling(63, min_periods=21).sum()
    result = _f35_margin_jerk_op(opinc, revenue, 252) * dvs
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net margin jerk × close zscore
def f35mj_f35_margin_jerk_netmargin_xclosez_21d_base_v146_signal(netinc, revenue, closeadj):
    cz = _z(closeadj, 252)
    result = _f35_margin_jerk_net(netinc, revenue, 21) * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d op margin jerk × close zscore
def f35mj_f35_margin_jerk_opmargin_xclosez_252d_base_v147_signal(opinc, revenue, closeadj):
    cz = _z(closeadj, 504)
    result = _f35_margin_jerk_op(opinc, revenue, 252) * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net margin jerk × log(1+revenue) for size weighting
def f35mj_f35_margin_jerk_netmargin_xlogrev_63d_base_v148_signal(netinc, revenue, closeadj):
    lr = np.log(revenue.abs() + 1.0)
    result = _f35_margin_jerk_net(netinc, revenue, 63) * lr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity: |netjerk|+|opjerk|+|grossjerk| × close
def f35mj_f35_margin_jerk_severitysum_252d_base_v149_signal(netinc, opinc, gp, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 252).abs()
    b = _f35_margin_jerk_op(opinc, revenue, 252).abs()
    c = _f35_margin_jerk_gross(gp, revenue, 252).abs()
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite severity: |netjerk|+|opjerk| × revenue × close
def f35mj_f35_margin_jerk_severityxrev_63d_base_v150_signal(netinc, opinc, revenue, closeadj):
    a = _f35_margin_jerk_net(netinc, revenue, 63).abs()
    b = _f35_margin_jerk_op(opinc, revenue, 63).abs()
    result = (a + b) * revenue.abs() * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35mj_f35_margin_jerk_netmargin_5d_base_v076_signal,
    f35mj_f35_margin_jerk_netmargin_10d_base_v077_signal,
    f35mj_f35_margin_jerk_netmargin_42d_base_v078_signal,
    f35mj_f35_margin_jerk_netmargin_189d_base_v079_signal,
    f35mj_f35_margin_jerk_netmargin_378d_base_v080_signal,
    f35mj_f35_margin_jerk_opmargin_5d_base_v081_signal,
    f35mj_f35_margin_jerk_opmargin_10d_base_v082_signal,
    f35mj_f35_margin_jerk_opmargin_42d_base_v083_signal,
    f35mj_f35_margin_jerk_opmargin_189d_base_v084_signal,
    f35mj_f35_margin_jerk_opmargin_378d_base_v085_signal,
    f35mj_f35_margin_jerk_grossmargin_5d_base_v086_signal,
    f35mj_f35_margin_jerk_grossmargin_42d_base_v087_signal,
    f35mj_f35_margin_jerk_grossmargin_189d_base_v088_signal,
    f35mj_f35_margin_jerk_ebitdamargin_5d_base_v089_signal,
    f35mj_f35_margin_jerk_ebitdamargin_42d_base_v090_signal,
    f35mj_f35_margin_jerk_ebitdamargin_189d_base_v091_signal,
    f35mj_f35_margin_jerk_netmargin_xgrowth_63d_base_v092_signal,
    f35mj_f35_margin_jerk_opmargin_xgrowth_252d_base_v093_signal,
    f35mj_f35_margin_jerk_grossmargin_xgrowth_252d_base_v094_signal,
    f35mj_f35_margin_jerk_netmargin_xdv_63d_base_v095_signal,
    f35mj_f35_margin_jerk_opmargin_xdv_252d_base_v096_signal,
    f35mj_f35_margin_jerk_netmargin_xvolz_63d_base_v097_signal,
    f35mj_f35_margin_jerk_netmargin_xshortret_21d_base_v098_signal,
    f35mj_f35_margin_jerk_opmargin_xlongret_63d_base_v099_signal,
    f35mj_f35_margin_jerk_netmargin_ema_252d_base_v100_signal,
    f35mj_f35_margin_jerk_opmargin_ema_21d_base_v101_signal,
    f35mj_f35_margin_jerk_grossmargin_ema_21d_base_v102_signal,
    f35mj_f35_margin_jerk_ebitdamargin_ema_63d_base_v103_signal,
    f35mj_f35_margin_jerk_netxebitda_63d_base_v104_signal,
    f35mj_f35_margin_jerk_opxgross_252d_base_v105_signal,
    f35mj_f35_margin_jerk_netminusop_63d_base_v106_signal,
    f35mj_f35_margin_jerk_ebitdaminusnet_252d_base_v107_signal,
    f35mj_f35_margin_jerk_netmargin_xintexp_21d_base_v108_signal,
    f35mj_f35_margin_jerk_opmargin_xtaxexp_252d_base_v109_signal,
    f35mj_f35_margin_jerk_netmargin_xcapex_63d_base_v110_signal,
    f35mj_f35_margin_jerk_grossmargin_xcapex_252d_base_v111_signal,
    f35mj_f35_margin_jerk_netmargin_xrange_63d_base_v112_signal,
    f35mj_f35_margin_jerk_opmargin_xrange_252d_base_v113_signal,
    f35mj_f35_margin_jerk_netmargin_xrevsq_63d_base_v114_signal,
    f35mj_f35_margin_jerk_meanof4_252d_base_v115_signal,
    f35mj_f35_margin_jerk_meanof4_63d_base_v116_signal,
    f35mj_f35_margin_jerk_meanof4_21d_base_v117_signal,
    f35mj_f35_margin_jerk_netmargin_dispersion_63d_base_v118_signal,
    f35mj_f35_margin_jerk_opmargin_dispersion_252d_base_v119_signal,
    f35mj_f35_margin_jerk_grossmargin_dispersion_252d_base_v120_signal,
    f35mj_f35_margin_jerk_netmargin_xsharesbas_63d_base_v121_signal,
    f35mj_f35_margin_jerk_opmargin_xsharesbas_252d_base_v122_signal,
    f35mj_f35_margin_jerk_netmargin_xncfi_252d_base_v123_signal,
    f35mj_f35_margin_jerk_netmargin_xliab_63d_base_v124_signal,
    f35mj_f35_margin_jerk_opmargin_xliab_252d_base_v125_signal,
    f35mj_f35_margin_jerk_netmargin_range_252d_base_v126_signal,
    f35mj_f35_margin_jerk_opmargin_range_252d_base_v127_signal,
    f35mj_f35_margin_jerk_grossmargin_range_504d_base_v128_signal,
    f35mj_f35_margin_jerk_netmargin_skew_63d_base_v129_signal,
    f35mj_f35_margin_jerk_netmargin_skew_252d_base_v130_signal,
    f35mj_f35_margin_jerk_opmargin_kurt_252d_base_v131_signal,
    f35mj_f35_margin_jerk_netmargin_xepstrend_63d_base_v132_signal,
    f35mj_f35_margin_jerk_opmargin_xepstrend_252d_base_v133_signal,
    f35mj_f35_margin_jerk_netmargin_xebitdagrowth_63d_base_v134_signal,
    f35mj_f35_margin_jerk_opmargin_xfcf_252d_base_v135_signal,
    f35mj_f35_margin_jerk_grossmargin_xfcf_63d_base_v136_signal,
    f35mj_f35_margin_jerk_ebitdamargin_xncff_252d_base_v137_signal,
    f35mj_f35_margin_jerk_netvsebitda_252d_base_v138_signal,
    f35mj_f35_margin_jerk_grossvsop_63d_base_v139_signal,
    f35mj_f35_margin_jerk_grossvsop_252d_base_v140_signal,
    f35mj_f35_margin_jerk_netmargin_xretearn_63d_base_v141_signal,
    f35mj_f35_margin_jerk_opmargin_xretearn_252d_base_v142_signal,
    f35mj_f35_margin_jerk_grossmargin_xretearn_252d_base_v143_signal,
    f35mj_f35_margin_jerk_netmargin_xvolsum_63d_base_v144_signal,
    f35mj_f35_margin_jerk_opmargin_xdvsum_252d_base_v145_signal,
    f35mj_f35_margin_jerk_netmargin_xclosez_21d_base_v146_signal,
    f35mj_f35_margin_jerk_opmargin_xclosez_252d_base_v147_signal,
    f35mj_f35_margin_jerk_netmargin_xlogrev_63d_base_v148_signal,
    f35mj_f35_margin_jerk_severitysum_252d_base_v149_signal,
    f35mj_f35_margin_jerk_severityxrev_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_MARGIN_JERK_REGISTRY_076_150 = REGISTRY


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
    ncff = pd.Series(6e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))) * np.sign(np.random.normal(0.3, 1.0, n)), name="ncff")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    liabilities = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="liabilities")
    retearn = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="retearn")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "opinc": opinc, "gp": gp, "ebitda": ebitda,
        "eps": eps, "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "ncff": ncff, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas, "liabilities": liabilities,
        "retearn": retearn,
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
    print(f"OK f35_margin_jerk_base_076_150_claude: {n_features} features pass")
