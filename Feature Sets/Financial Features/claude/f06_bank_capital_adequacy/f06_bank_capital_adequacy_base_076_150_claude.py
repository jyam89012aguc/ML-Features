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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _f06_capital_ratio(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f06_capital_dynamics(equity, assets, w):
    cr = equity / assets.replace(0, np.nan)
    return cr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_capital_buffer(equity, debt, w):
    buf = equity / (equity + debt).replace(0, np.nan)
    return buf.rolling(w, min_periods=max(1, w // 2)).mean()


def f06bca_f06_bank_capital_adequacy_capratiorange_63d_base_v076_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(63, min_periods=max(1, 63//2)).max() - cr.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_126d_base_v077_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(126, min_periods=max(1, 126//2)).max() - cr.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorange_252d_base_v078_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rng = cr.rolling(252, min_periods=max(1, 252//2)).max() - cr.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_21d_base_v079_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    rv = _std(closeadj.pct_change(), 21)
    result = cd * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_63d_base_v080_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    rv = _std(closeadj.pct_change(), 63)
    result = cd * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynxretvol_126d_base_v081_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    rv = _std(closeadj.pct_change(), 126)
    result = cd * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_21d_base_v082_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 21)
    rv = _std(closeadj.pct_change(), 21)
    result = cb * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_63d_base_v083_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    rv = _std(closeadj.pct_change(), 63)
    result = cb * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufxretvol_126d_base_v084_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    rv = _std(closeadj.pct_change(), 126)
    result = cb * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_63d_base_v085_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_126d_base_v086_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiorank_252d_base_v087_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    rnk = cr.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_63d_base_v088_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 63)
    rnk = cb.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_126d_base_v089_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 126)
    rnk = cb.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufrank_252d_base_v090_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 252)
    rnk = cb.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_21d_base_v091_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.sign(cr.diff(periods=21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_63d_base_v092_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.sign(cr.diff(periods=63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratiochgsign_252d_base_v093_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = np.sign(cr.diff(periods=252)) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_10d_base_v094_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _mean(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_10d_base_v095_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    result = _mean(cb, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_10d_base_v096_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_10d_base_v097_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    result = _std(cb, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_10d_base_v098_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_10d_base_v099_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    result = _z(cb, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_10d_base_v100_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 10) * closeadj * np.log1p(_mean(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_10d_base_v101_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 10)
    result = _ema(cb, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_42d_base_v102_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _mean(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_42d_base_v103_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    result = _mean(cb, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_42d_base_v104_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_42d_base_v105_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    result = _std(cb, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_42d_base_v106_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_42d_base_v107_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    result = _z(cb, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_42d_base_v108_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_42d_base_v109_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 42)
    result = _ema(cb, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_189d_base_v110_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _mean(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_189d_base_v111_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    result = _mean(cb, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_189d_base_v112_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_189d_base_v113_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    result = _std(cb, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_189d_base_v114_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_189d_base_v115_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    result = _z(cb, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_189d_base_v116_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_189d_base_v117_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 189)
    result = _ema(cb, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_mean_378d_base_v118_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _mean(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_mean_378d_base_v119_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    result = _mean(cb, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_std_378d_base_v120_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _std(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_std_378d_base_v121_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    result = _std(cb, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_z_378d_base_v122_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _z(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_z_378d_base_v123_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    result = _z(cb, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capratio_ema_378d_base_v124_signal(equity, assets, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    result = _ema(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbuf_ema_378d_base_v125_signal(equity, debt, closeadj):
    cb = _f06_capital_buffer(equity, debt, 378)
    result = _ema(cb, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_21v63_base_v126_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_21v63_base_v127_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_63v252_base_v128_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 63)
    b = _f06_capital_dynamics(equity, assets, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_63v252_base_v129_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 63)
    b = _f06_capital_buffer(equity, debt, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_21v252_base_v130_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_21v252_base_v131_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_126v504_base_v132_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 126)
    b = _f06_capital_dynamics(equity, assets, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_126v504_base_v133_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 126)
    b = _f06_capital_buffer(equity, debt, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynratio_42v189_base_v134_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 42)
    b = _f06_capital_dynamics(equity, assets, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufratio_42v189_base_v135_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 42)
    b = _f06_capital_buffer(equity, debt, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_21m63_base_v136_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 21)
    b = _f06_capital_dynamics(equity, assets, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_21m63_base_v137_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 21)
    b = _f06_capital_buffer(equity, debt, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_63m252_base_v138_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 63)
    b = _f06_capital_dynamics(equity, assets, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_63m252_base_v139_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 63)
    b = _f06_capital_buffer(equity, debt, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdyndiff_126m504_base_v140_signal(equity, assets, closeadj):
    a = _f06_capital_dynamics(equity, assets, 126)
    b = _f06_capital_dynamics(equity, assets, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capbufdiff_126m504_base_v141_signal(equity, debt, closeadj):
    a = _f06_capital_buffer(equity, debt, 126)
    b = _f06_capital_buffer(equity, debt, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_21d_base_v142_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 21)
    result = (cr + cb) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_63d_base_v143_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 63)
    result = (cr + cb) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_126d_base_v144_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 126)
    result = (cr + cb) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_252d_base_v145_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 252)
    result = (cr + cb) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capcompound_504d_base_v146_signal(equity, assets, debt, closeadj):
    cr = _f06_capital_ratio(equity, assets)
    cb = _f06_capital_buffer(equity, debt, 504)
    result = (cr + cb) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_21d_base_v147_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 21)
    result = cd.pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_63d_base_v148_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 63)
    result = cd.pct_change(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_126d_base_v149_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 126)
    result = cd.pct_change(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06bca_f06_bank_capital_adequacy_capdynpct_252d_base_v150_signal(equity, assets, closeadj):
    cd = _f06_capital_dynamics(equity, assets, 252)
    result = cd.pct_change(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bca_f06_bank_capital_adequacy_capratiorange_63d_base_v076_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_126d_base_v077_signal,
    f06bca_f06_bank_capital_adequacy_capratiorange_252d_base_v078_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_21d_base_v079_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_63d_base_v080_signal,
    f06bca_f06_bank_capital_adequacy_capdynxretvol_126d_base_v081_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_21d_base_v082_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_63d_base_v083_signal,
    f06bca_f06_bank_capital_adequacy_capbufxretvol_126d_base_v084_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_63d_base_v085_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_126d_base_v086_signal,
    f06bca_f06_bank_capital_adequacy_capratiorank_252d_base_v087_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_63d_base_v088_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_126d_base_v089_signal,
    f06bca_f06_bank_capital_adequacy_capbufrank_252d_base_v090_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_21d_base_v091_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_63d_base_v092_signal,
    f06bca_f06_bank_capital_adequacy_capratiochgsign_252d_base_v093_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_10d_base_v094_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_10d_base_v095_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_10d_base_v096_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_10d_base_v097_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_10d_base_v098_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_10d_base_v099_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_10d_base_v100_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_10d_base_v101_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_42d_base_v102_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_42d_base_v103_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_42d_base_v104_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_42d_base_v105_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_42d_base_v106_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_42d_base_v107_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_42d_base_v108_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_42d_base_v109_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_189d_base_v110_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_189d_base_v111_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_189d_base_v112_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_189d_base_v113_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_189d_base_v114_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_189d_base_v115_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_189d_base_v116_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_189d_base_v117_signal,
    f06bca_f06_bank_capital_adequacy_capratio_mean_378d_base_v118_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_mean_378d_base_v119_signal,
    f06bca_f06_bank_capital_adequacy_capratio_std_378d_base_v120_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_std_378d_base_v121_signal,
    f06bca_f06_bank_capital_adequacy_capratio_z_378d_base_v122_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_z_378d_base_v123_signal,
    f06bca_f06_bank_capital_adequacy_capratio_ema_378d_base_v124_signal,
    f06bca_f06_bank_capital_adequacy_capbuf_ema_378d_base_v125_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_21v63_base_v126_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_21v63_base_v127_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_63v252_base_v128_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_63v252_base_v129_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_21v252_base_v130_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_21v252_base_v131_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_126v504_base_v132_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_126v504_base_v133_signal,
    f06bca_f06_bank_capital_adequacy_capdynratio_42v189_base_v134_signal,
    f06bca_f06_bank_capital_adequacy_capbufratio_42v189_base_v135_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_21m63_base_v136_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_21m63_base_v137_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_63m252_base_v138_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_63m252_base_v139_signal,
    f06bca_f06_bank_capital_adequacy_capdyndiff_126m504_base_v140_signal,
    f06bca_f06_bank_capital_adequacy_capbufdiff_126m504_base_v141_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_21d_base_v142_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_63d_base_v143_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_126d_base_v144_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_252d_base_v145_signal,
    f06bca_f06_bank_capital_adequacy_capcompound_504d_base_v146_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_21d_base_v147_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_63d_base_v148_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_126d_base_v149_signal,
    f06bca_f06_bank_capital_adequacy_capdynpct_252d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BANK_CAPITAL_ADEQUACY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f06_capital_ratio', '_f06_capital_dynamics', '_f06_capital_buffer')
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
    print(f"OK f06_bank_capital_adequacy_base_076_150_claude: {n_features} features pass")
