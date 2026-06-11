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

def _f38_sga_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f38_sga_revenue_gap(sgna, revenue, w):
    ds = sgna.pct_change(periods=w)
    dr = revenue.pct_change(periods=w)
    return dr - ds


def _f38_sga_leverage(sgna, revenue, w):
    intensity = sgna / revenue.replace(0, np.nan)
    return -intensity.diff(periods=w)




def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d126d_base_v076_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d189d_base_v077_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d252d_base_v078_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d378d_base_v079_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d504d_base_v080_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d5d_base_v081_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d10d_base_v082_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d21d_base_v083_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d42d_base_v084_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d63d_base_v085_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d126d_base_v086_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d189d_base_v087_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d252d_base_v088_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d378d_base_v089_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d504d_base_v090_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d5d_base_v091_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d10d_base_v092_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d21d_base_v093_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d42d_base_v094_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d63d_base_v095_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d126d_base_v096_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d189d_base_v097_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d252d_base_v098_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d378d_base_v099_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d504d_base_v100_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d5d_base_v101_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d10d_base_v102_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d21d_base_v103_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d42d_base_v104_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d63d_base_v105_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d126d_base_v106_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d189d_base_v107_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d252d_base_v108_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d378d_base_v109_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d504d_base_v110_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d5d_base_v111_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d10d_base_v112_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d21d_base_v113_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d42d_base_v114_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d63d_base_v115_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d126d_base_v116_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d189d_base_v117_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d252d_base_v118_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d378d_base_v119_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d504d_base_v120_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d5d_base_v121_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d10d_base_v122_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d21d_base_v123_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d42d_base_v124_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d63d_base_v125_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d126d_base_v126_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d189d_base_v127_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d252d_base_v128_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d378d_base_v129_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d504d_base_v130_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d5d_base_v131_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d10d_base_v132_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d21d_base_v133_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d42d_base_v134_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d63d_base_v135_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d126d_base_v136_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d189d_base_v137_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d252d_base_v138_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d378d_base_v139_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d504d_base_v140_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d5d_base_v141_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d10d_base_v142_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d21d_base_v143_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d42d_base_v144_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d63d_base_v145_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d126d_base_v146_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d189d_base_v147_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d252d_base_v148_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d378d_base_v149_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d504d_base_v150_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d126d_base_v076_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d189d_base_v077_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d252d_base_v078_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d378d_base_v079_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d504d_base_v080_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d5d_base_v081_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d10d_base_v082_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d21d_base_v083_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d42d_base_v084_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d63d_base_v085_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d126d_base_v086_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d189d_base_v087_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d252d_base_v088_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d378d_base_v089_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_10d504d_base_v090_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d5d_base_v091_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d10d_base_v092_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d21d_base_v093_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d42d_base_v094_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d63d_base_v095_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d126d_base_v096_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d189d_base_v097_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d252d_base_v098_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d378d_base_v099_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_21d504d_base_v100_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d5d_base_v101_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d10d_base_v102_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d21d_base_v103_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d42d_base_v104_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d63d_base_v105_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d126d_base_v106_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d189d_base_v107_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d252d_base_v108_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d378d_base_v109_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_42d504d_base_v110_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d5d_base_v111_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d10d_base_v112_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d21d_base_v113_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d42d_base_v114_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d63d_base_v115_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d126d_base_v116_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d189d_base_v117_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d252d_base_v118_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d378d_base_v119_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_63d504d_base_v120_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d5d_base_v121_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d10d_base_v122_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d21d_base_v123_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d42d_base_v124_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d63d_base_v125_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d126d_base_v126_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d189d_base_v127_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d252d_base_v128_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d378d_base_v129_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_126d504d_base_v130_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d5d_base_v131_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d10d_base_v132_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d21d_base_v133_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d42d_base_v134_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d63d_base_v135_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d126d_base_v136_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d189d_base_v137_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d252d_base_v138_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d378d_base_v139_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_189d504d_base_v140_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d5d_base_v141_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d10d_base_v142_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d21d_base_v143_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d42d_base_v144_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d63d_base_v145_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d126d_base_v146_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d189d_base_v147_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d252d_base_v148_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d378d_base_v149_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_252d504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F38_HEALTHCARE_SGA_LEVERAGE_REGISTRY_076_150 = REGISTRY



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
    domain_primitives = ("_f38_sga_intensity", "_f38_sga_revenue_gap", "_f38_sga_leverage")
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
    print(f"OK f38_healthcare_sga_leverage_base_076_150_claude: {n_features} features pass")
