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

def _f36_op_leverage_proxy(ebit, revenue, w):
    em = (ebit / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()
    eb = ebit.rolling(w, min_periods=max(1, w // 2)).mean()
    rv = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return em * eb / rv.replace(0, np.nan)


def _f36_margin_revenue_beta(ebitdamargin, revenue, w):
    dm = ebitdamargin.diff(periods=w)
    dr = revenue.pct_change(periods=w)
    return dm / dr.replace(0, np.nan)


def _f36_drop_through(ebit, revenue, w):
    deb = ebit.diff(periods=w)
    drv = revenue.diff(periods=w)
    return deb / drv.replace(0, np.nan)




def f36hol_f36_healthcare_operating_leverage_mrbdivclose_126d_base_v076_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_189d_base_v077_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_252d_base_v078_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_378d_base_v079_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_504d_base_v080_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_5d_base_v081_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_10d_base_v082_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_21d_base_v083_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_42d_base_v084_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_63d_base_v085_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_126d_base_v086_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_189d_base_v087_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_252d_base_v088_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_378d_base_v089_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpdivclose_504d_base_v090_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d5d_base_v091_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d10d_base_v092_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d21d_base_v093_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d42d_base_v094_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d63d_base_v095_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d126d_base_v096_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d189d_base_v097_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d252d_base_v098_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d378d_base_v099_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d504d_base_v100_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d5d_base_v101_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d10d_base_v102_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d21d_base_v103_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d42d_base_v104_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d63d_base_v105_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d126d_base_v106_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d189d_base_v107_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d252d_base_v108_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d378d_base_v109_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d504d_base_v110_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d5d_base_v111_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d10d_base_v112_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d21d_base_v113_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d42d_base_v114_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d63d_base_v115_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d126d_base_v116_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d189d_base_v117_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d252d_base_v118_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d378d_base_v119_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d504d_base_v120_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d5d_base_v121_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d10d_base_v122_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d21d_base_v123_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d42d_base_v124_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d63d_base_v125_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d126d_base_v126_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d189d_base_v127_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d252d_base_v128_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d378d_base_v129_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d504d_base_v130_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d5d_base_v131_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d10d_base_v132_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d21d_base_v133_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d42d_base_v134_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d63d_base_v135_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d126d_base_v136_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d189d_base_v137_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d252d_base_v138_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d378d_base_v139_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d504d_base_v140_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d5d_base_v141_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d10d_base_v142_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d21d_base_v143_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d42d_base_v144_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d63d_base_v145_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d126d_base_v146_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d189d_base_v147_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d252d_base_v148_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d378d_base_v149_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d504d_base_v150_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_126d_base_v076_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_189d_base_v077_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_252d_base_v078_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_378d_base_v079_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_504d_base_v080_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_5d_base_v081_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_10d_base_v082_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_21d_base_v083_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_42d_base_v084_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_63d_base_v085_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_126d_base_v086_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_189d_base_v087_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_252d_base_v088_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_378d_base_v089_signal,
    f36hol_f36_healthcare_operating_leverage_drpdivclose_504d_base_v090_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d5d_base_v091_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d10d_base_v092_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d21d_base_v093_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d42d_base_v094_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d63d_base_v095_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d126d_base_v096_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d189d_base_v097_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d252d_base_v098_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d378d_base_v099_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_5d504d_base_v100_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d5d_base_v101_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d10d_base_v102_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d21d_base_v103_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d42d_base_v104_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d63d_base_v105_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d126d_base_v106_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d189d_base_v107_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d252d_base_v108_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d378d_base_v109_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_10d504d_base_v110_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d5d_base_v111_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d10d_base_v112_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d21d_base_v113_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d42d_base_v114_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d63d_base_v115_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d126d_base_v116_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d189d_base_v117_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d252d_base_v118_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d378d_base_v119_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_21d504d_base_v120_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d5d_base_v121_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d10d_base_v122_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d21d_base_v123_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d42d_base_v124_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d63d_base_v125_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d126d_base_v126_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d189d_base_v127_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d252d_base_v128_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d378d_base_v129_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_42d504d_base_v130_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d5d_base_v131_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d10d_base_v132_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d21d_base_v133_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d42d_base_v134_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d63d_base_v135_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d126d_base_v136_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d189d_base_v137_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d252d_base_v138_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d378d_base_v139_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_63d504d_base_v140_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d5d_base_v141_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d10d_base_v142_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d21d_base_v143_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d42d_base_v144_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d63d_base_v145_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d126d_base_v146_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d189d_base_v147_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d252d_base_v148_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d378d_base_v149_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanmulclose_126d504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F36_HEALTHCARE_OPERATING_LEVERAGE_REGISTRY_076_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "sgna": sgna, "opex": opex, "rnd": rnd,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_op_leverage_proxy", "_f36_margin_revenue_beta", "_f36_drop_through")
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
    print(f"OK f36_healthcare_operating_leverage_base_076_150_claude: {n_features} features pass")
