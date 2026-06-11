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
def _f086_debt_change(debt, w):
    return debt.diff(periods=w)


def _f086_debt_paydown(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return -(debt - base.shift(w)) / base.shift(w).abs().replace(0, np.nan)


def _f086_deleverage_score(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -(lev - lev.shift(w)) / lev.abs().shift(w).replace(0, np.nan)


# v076 21d smoothed debt change × close (5d ma)
def f086dpt_f086_debt_paydown_trend_chgsm_21d_base_v076_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077 63d smoothed debt change × close
def f086dpt_f086_debt_paydown_trend_chgsm_63d_base_v077_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078 252d smoothed debt change × close
def f086dpt_f086_debt_paydown_trend_chgsm_252d_base_v078_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079 21d deleverage × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_21d_base_v079_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v080 63d deleverage × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_63d_base_v080_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v081 252d deleverage × log close
def f086dpt_f086_debt_paydown_trend_delevxlog_252d_base_v081_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v082 21d shift paydown × close (lagged paydown signal)
def f086dpt_f086_debt_paydown_trend_paydownlag_21d_base_v082_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21).shift(5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083 63d shift paydown × close
def f086dpt_f086_debt_paydown_trend_paydownlag_63d_base_v083_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63).shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084 252d shift paydown × close
def f086dpt_f086_debt_paydown_trend_paydownlag_252d_base_v084_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252).shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085 21d paydown × tanh transform × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_21d_base_v085_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = np.tanh(base * 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086 63d paydown × tanh × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_63d_base_v086_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = np.tanh(base * 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087 252d paydown × tanh × close
def f086dpt_f086_debt_paydown_trend_paydowntanh_252d_base_v087_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = np.tanh(base * 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088 21d debt change × dollar volume proxy (close²)
def f086dpt_f086_debt_paydown_trend_chgxcsq_21d_base_v088_signal(debt, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089 63d debt change × close²
def f086dpt_f086_debt_paydown_trend_chgxcsq_63d_base_v089_signal(debt, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090 252d debt change × close²
def f086dpt_f086_debt_paydown_trend_chgxcsq_252d_base_v090_signal(debt, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091 21d paydown / std × close (sharpe-like)
def f086dpt_f086_debt_paydown_trend_paydownsharpe_21d_base_v091_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    s = _std(base, 252).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092 63d paydown sharpe × close
def f086dpt_f086_debt_paydown_trend_paydownsharpe_63d_base_v092_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    s = _std(base, 252).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093 252d paydown sharpe × close
def f086dpt_f086_debt_paydown_trend_paydownsharpe_252d_base_v093_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    s = _std(base, 504).replace(0, np.nan)
    result = (base / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094 21d ratio paydown to debt change (efficiency)
def f086dpt_f086_debt_paydown_trend_paydowneff_21d_base_v094_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 21)
    chg = _f086_debt_change(debt, 21).abs() / debt.abs().replace(0, np.nan) + 1e-9
    result = (pd_ / chg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095 63d paydown efficiency × close
def f086dpt_f086_debt_paydown_trend_paydowneff_63d_base_v095_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 63)
    chg = _f086_debt_change(debt, 63).abs() / debt.abs().replace(0, np.nan) + 1e-9
    result = (pd_ / chg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096 252d paydown efficiency × close
def f086dpt_f086_debt_paydown_trend_paydowneff_252d_base_v096_signal(debt, closeadj):
    pd_ = _f086_debt_paydown(debt, 252)
    chg = _f086_debt_change(debt, 252).abs() / debt.abs().replace(0, np.nan) + 1e-9
    result = (pd_ / chg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097 21d deleverage × paydown composite × close
def f086dpt_f086_debt_paydown_trend_delevpd_21d_base_v097_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    result = (a + b) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098 63d deleverage × paydown composite × close
def f086dpt_f086_debt_paydown_trend_delevpd_63d_base_v098_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 63)
    b = _f086_debt_paydown(debt, 63)
    result = (a + b) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099 252d deleverage × paydown composite × close
def f086dpt_f086_debt_paydown_trend_delevpd_252d_base_v099_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    result = (a + b) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100 21d debt change × equity/debt
def f086dpt_f086_debt_paydown_trend_chgxer_21d_base_v100_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    eqr = equity / debt.replace(0, np.nan)
    result = base * eqr.clip(-10, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101 63d debt change × equity/debt
def f086dpt_f086_debt_paydown_trend_chgxer_63d_base_v101_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    eqr = equity / debt.replace(0, np.nan)
    result = base * eqr.clip(-10, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102 252d debt change × equity/debt
def f086dpt_f086_debt_paydown_trend_chgxer_252d_base_v102_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    eqr = equity / debt.replace(0, np.nan)
    result = base * eqr.clip(-10, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103 21d paydown × abs equity change × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_21d_base_v103_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 21)
    eqd = (equity - equity.shift(21)) / equity.abs().shift(21).replace(0, np.nan)
    result = a * eqd.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104 63d paydown × abs equity change × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_63d_base_v104_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 63)
    eqd = (equity - equity.shift(63)) / equity.abs().shift(63).replace(0, np.nan)
    result = a * eqd.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105 252d paydown × abs equity change × close
def f086dpt_f086_debt_paydown_trend_pdxeqd_252d_base_v105_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 252)
    eqd = (equity - equity.shift(252)) / equity.abs().shift(252).replace(0, np.nan)
    result = a * eqd.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106 21d cumulative paydown (1y window)
def f086dpt_f086_debt_paydown_trend_paydowncum_252d_base_v106_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107 63d cumulative paydown (1y window)
def f086dpt_f086_debt_paydown_trend_paydowncum_504d_base_v107_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108 21d range-normalized paydown × close
def f086dpt_f086_debt_paydown_trend_paydownrange_21d_base_v108_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    mx = base.rolling(252, min_periods=63).max()
    mn = base.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109 63d range-normalized paydown × close
def f086dpt_f086_debt_paydown_trend_paydownrange_63d_base_v109_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    mx = base.rolling(252, min_periods=63).max()
    mn = base.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110 252d range-normalized paydown × close
def f086dpt_f086_debt_paydown_trend_paydownrange_252d_base_v110_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    mx = base.rolling(504, min_periods=126).max()
    mn = base.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((base - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111 21d ratio of paydown to deleverage × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_21d_base_v111_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_deleverage_score(debt, equity, 21).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112 63d ratio paydown/deleverage × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_63d_base_v112_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_deleverage_score(debt, equity, 63).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113 252d ratio paydown/deleverage × close
def f086dpt_f086_debt_paydown_trend_pddelevratio_252d_base_v113_signal(debt, equity, closeadj):
    a = _f086_debt_paydown(debt, 252)
    b = _f086_deleverage_score(debt, equity, 252).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114 21d paydown × close shifted by 5d (lag scaling)
def f086dpt_f086_debt_paydown_trend_paydownxlag_21d_base_v114_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base * closeadj.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# v115 63d paydown × close shifted by 21d
def f086dpt_f086_debt_paydown_trend_paydownxlag_63d_base_v115_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base * closeadj.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# v116 252d paydown × close shifted by 63d
def f086dpt_f086_debt_paydown_trend_paydownxlag_252d_base_v116_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base * closeadj.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v117 21d debt change × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_21d_base_v117_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 21) / debt.abs().replace(0, np.nan)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v118 63d debt change × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_63d_base_v118_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 63) / debt.abs().replace(0, np.nan)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v119 252d debt change × close × log equity
def f086dpt_f086_debt_paydown_trend_chgxleq_252d_base_v119_signal(debt, equity, closeadj):
    base = _f086_debt_change(debt, 252) / debt.abs().replace(0, np.nan)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v120 21d streak of paydown (consecutive positive) × close
def f086dpt_f086_debt_paydown_trend_paydownstreak_21d_base_v120_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    pos = (base > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121 63d streak × close
def f086dpt_f086_debt_paydown_trend_paydownstreak_63d_base_v121_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    pos = (base > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122 252d streak × close × log close
def f086dpt_f086_debt_paydown_trend_paydownstreak_252d_base_v122_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    pos = (base > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    result = (streak + 1.0) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v123 21d deleverage × close × sqrt(equity/debt)
def f086dpt_f086_debt_paydown_trend_delevxsqr_21d_base_v123_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124 63d deleverage × close × sqrt(equity/debt)
def f086dpt_f086_debt_paydown_trend_delevxsqr_63d_base_v124_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125 252d deleverage × close × sqrt(equity/debt)
def f086dpt_f086_debt_paydown_trend_delevxsqr_252d_base_v125_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    ratio = (equity / debt.replace(0, np.nan)).clip(lower=0).pow(0.5)
    result = base * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126 21d ratio short/long paydown × close
def f086dpt_f086_debt_paydown_trend_pdratio_21v252_base_v126_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 252).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127 63d ratio short/long paydown × close
def f086dpt_f086_debt_paydown_trend_pdratio_63v504_base_v127_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_debt_paydown(debt, 504).abs() + 1e-9
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128 21d-63d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_21m63_base_v128_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129 63d-252d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_63m252_base_v129_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 63)
    b = _f086_debt_paydown(debt, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130 21d-252d paydown diff × close
def f086dpt_f086_debt_paydown_trend_pddiff_21m252_base_v130_signal(debt, closeadj):
    a = _f086_debt_paydown(debt, 21)
    b = _f086_debt_paydown(debt, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131 21d deleverage min × close
def f086dpt_f086_debt_paydown_trend_delevmin_21d_base_v131_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132 63d deleverage min × close
def f086dpt_f086_debt_paydown_trend_delevmin_63d_base_v132_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    result = base.rolling(126, min_periods=42).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133 252d deleverage min × close
def f086dpt_f086_debt_paydown_trend_delevmin_252d_base_v133_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134 21d deleverage range × close
def f086dpt_f086_debt_paydown_trend_delevrange_21d_base_v134_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 21)
    rng = base.rolling(126, min_periods=42).max() - base.rolling(126, min_periods=42).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135 63d deleverage range × close
def f086dpt_f086_debt_paydown_trend_delevrange_63d_base_v135_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136 252d deleverage range × close
def f086dpt_f086_debt_paydown_trend_delevrange_252d_base_v136_signal(debt, equity, closeadj):
    base = _f086_deleverage_score(debt, equity, 252)
    rng = base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137 21d paydown count > 0 × close
def f086dpt_f086_debt_paydown_trend_paydowncount_21d_base_v137_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    cnt = (base > 0).astype(float).rolling(126, min_periods=21).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138 63d paydown count > 0 × close
def f086dpt_f086_debt_paydown_trend_paydowncount_63d_base_v138_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    cnt = (base > 0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139 252d paydown count > 0 × close
def f086dpt_f086_debt_paydown_trend_paydowncount_252d_base_v139_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    cnt = (base > 0).astype(float).rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140 21d paydown × equity scaling factor (clipped)
def f086dpt_f086_debt_paydown_trend_paydownxeqf_21d_base_v140_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 21)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    result = base * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141 63d paydown × eqf × close
def f086dpt_f086_debt_paydown_trend_paydownxeqf_63d_base_v141_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 63)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    result = base * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142 252d paydown × eqf × close
def f086dpt_f086_debt_paydown_trend_paydownxeqf_252d_base_v142_signal(debt, equity, closeadj):
    base = _f086_debt_paydown(debt, 252)
    f = (equity / equity.shift(252).replace(0, np.nan)).clip(0.1, 5.0)
    result = base * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143 21d deleverage × paydown × close (product)
def f086dpt_f086_debt_paydown_trend_delevxpd_21d_base_v143_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144 63d deleverage × paydown × close
def f086dpt_f086_debt_paydown_trend_delevxpd_63d_base_v144_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 63)
    b = _f086_debt_paydown(debt, 63)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145 252d deleverage × paydown × close
def f086dpt_f086_debt_paydown_trend_delevxpd_252d_base_v145_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146 21d paydown × close × debt log
def f086dpt_f086_debt_paydown_trend_paydownxld_21d_base_v146_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 21)
    result = base * np.log(debt.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147 63d paydown × close × debt log
def f086dpt_f086_debt_paydown_trend_paydownxld_63d_base_v147_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 63)
    result = base * np.log(debt.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148 252d paydown × close × debt log
def f086dpt_f086_debt_paydown_trend_paydownxld_252d_base_v148_signal(debt, closeadj):
    base = _f086_debt_paydown(debt, 252)
    result = base * np.log(debt.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149 21d composite paydown × deleverage × close × log close
def f086dpt_f086_debt_paydown_trend_pdcomp_21d_base_v149_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 21)
    b = _f086_debt_paydown(debt, 21)
    result = (a + b) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v150 252d composite paydown × deleverage × close × log close
def f086dpt_f086_debt_paydown_trend_pdcomp_252d_base_v150_signal(debt, equity, closeadj):
    a = _f086_deleverage_score(debt, equity, 252)
    b = _f086_debt_paydown(debt, 252)
    result = (a + b) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f086dpt_f086_debt_paydown_trend_chgsm_21d_base_v076_signal,
    f086dpt_f086_debt_paydown_trend_chgsm_63d_base_v077_signal,
    f086dpt_f086_debt_paydown_trend_chgsm_252d_base_v078_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_21d_base_v079_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_63d_base_v080_signal,
    f086dpt_f086_debt_paydown_trend_delevxlog_252d_base_v081_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_21d_base_v082_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_63d_base_v083_signal,
    f086dpt_f086_debt_paydown_trend_paydownlag_252d_base_v084_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_21d_base_v085_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_63d_base_v086_signal,
    f086dpt_f086_debt_paydown_trend_paydowntanh_252d_base_v087_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_21d_base_v088_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_63d_base_v089_signal,
    f086dpt_f086_debt_paydown_trend_chgxcsq_252d_base_v090_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_21d_base_v091_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_63d_base_v092_signal,
    f086dpt_f086_debt_paydown_trend_paydownsharpe_252d_base_v093_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_21d_base_v094_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_63d_base_v095_signal,
    f086dpt_f086_debt_paydown_trend_paydowneff_252d_base_v096_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_21d_base_v097_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_63d_base_v098_signal,
    f086dpt_f086_debt_paydown_trend_delevpd_252d_base_v099_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_21d_base_v100_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_63d_base_v101_signal,
    f086dpt_f086_debt_paydown_trend_chgxer_252d_base_v102_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_21d_base_v103_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_63d_base_v104_signal,
    f086dpt_f086_debt_paydown_trend_pdxeqd_252d_base_v105_signal,
    f086dpt_f086_debt_paydown_trend_paydowncum_252d_base_v106_signal,
    f086dpt_f086_debt_paydown_trend_paydowncum_504d_base_v107_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_21d_base_v108_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_63d_base_v109_signal,
    f086dpt_f086_debt_paydown_trend_paydownrange_252d_base_v110_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_21d_base_v111_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_63d_base_v112_signal,
    f086dpt_f086_debt_paydown_trend_pddelevratio_252d_base_v113_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlag_21d_base_v114_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlag_63d_base_v115_signal,
    f086dpt_f086_debt_paydown_trend_paydownxlag_252d_base_v116_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_21d_base_v117_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_63d_base_v118_signal,
    f086dpt_f086_debt_paydown_trend_chgxleq_252d_base_v119_signal,
    f086dpt_f086_debt_paydown_trend_paydownstreak_21d_base_v120_signal,
    f086dpt_f086_debt_paydown_trend_paydownstreak_63d_base_v121_signal,
    f086dpt_f086_debt_paydown_trend_paydownstreak_252d_base_v122_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_21d_base_v123_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_63d_base_v124_signal,
    f086dpt_f086_debt_paydown_trend_delevxsqr_252d_base_v125_signal,
    f086dpt_f086_debt_paydown_trend_pdratio_21v252_base_v126_signal,
    f086dpt_f086_debt_paydown_trend_pdratio_63v504_base_v127_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_21m63_base_v128_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_63m252_base_v129_signal,
    f086dpt_f086_debt_paydown_trend_pddiff_21m252_base_v130_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_21d_base_v131_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_63d_base_v132_signal,
    f086dpt_f086_debt_paydown_trend_delevmin_252d_base_v133_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_21d_base_v134_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_63d_base_v135_signal,
    f086dpt_f086_debt_paydown_trend_delevrange_252d_base_v136_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_21d_base_v137_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_63d_base_v138_signal,
    f086dpt_f086_debt_paydown_trend_paydowncount_252d_base_v139_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_21d_base_v140_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_63d_base_v141_signal,
    f086dpt_f086_debt_paydown_trend_paydownxeqf_252d_base_v142_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_21d_base_v143_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_63d_base_v144_signal,
    f086dpt_f086_debt_paydown_trend_delevxpd_252d_base_v145_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_21d_base_v146_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_63d_base_v147_signal,
    f086dpt_f086_debt_paydown_trend_paydownxld_252d_base_v148_signal,
    f086dpt_f086_debt_paydown_trend_pdcomp_21d_base_v149_signal,
    f086dpt_f086_debt_paydown_trend_pdcomp_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F086_DEBT_PAYDOWN_TREND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")

    cols = {"closeadj": closeadj, "debt": debt, "equity": equity}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f086_debt_change", "_f086_debt_paydown", "_f086_deleverage_score")
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
    print(f"OK f086_debt_paydown_trend_base_076_150_claude: {n_features} features pass")
