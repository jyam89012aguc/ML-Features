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
def _f35_revenue_cycle(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (revenue - m) / m


def _f35_subsidy_proxy(revenue, ebitdamargin, w):
    g = revenue.pct_change(w)
    mm = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * mm


def _f35_policy_cycle_score(revenue, w):
    g_long = revenue.pct_change(w)
    g_short = revenue.pct_change(max(5, w // 4))
    return g_long - g_short

def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_126d_base_v076_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 126)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_126d_base_v077_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 126)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_126d_base_v078_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 126)).rolling(63, min_periods=max(1, 63//2)).sum() * closeadj / 63
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_189d_base_v079_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_189d_base_v080_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_189d_base_v081_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)) * closeadj * (_f35_revenue_cycle(revenue, 189)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_189d_base_v082_signal(closeadj, revenue):
    result = _mean(_f35_revenue_cycle(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_189d_base_v083_signal(closeadj, revenue):
    result = _std(_f35_revenue_cycle(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_189d_base_v084_signal(closeadj, revenue):
    result = _z(_f35_revenue_cycle(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_189d_base_v085_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)).ewm(span=94, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_189d_base_v086_signal(closeadj, revenue):
    result = np.log((_f35_revenue_cycle(revenue, 189)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_189d_base_v087_signal(closeadj, revenue):
    result = np.sign(_f35_revenue_cycle(revenue, 189)) * closeadj * (1.0 + (_f35_revenue_cycle(revenue, 189)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_189d_base_v088_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)) * closeadj * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_189d_base_v089_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_189d_base_v090_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_189d_base_v091_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 189)).rolling(94, min_periods=max(1, 94//2)).sum() * closeadj / 94
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_252d_base_v092_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_252d_base_v093_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_252d_base_v094_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)) * closeadj * (_f35_revenue_cycle(revenue, 252)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_252d_base_v095_signal(closeadj, revenue):
    result = _mean(_f35_revenue_cycle(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_252d_base_v096_signal(closeadj, revenue):
    result = _std(_f35_revenue_cycle(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_252d_base_v097_signal(closeadj, revenue):
    result = _z(_f35_revenue_cycle(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_252d_base_v098_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_252d_base_v099_signal(closeadj, revenue):
    result = np.log((_f35_revenue_cycle(revenue, 252)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_252d_base_v100_signal(closeadj, revenue):
    result = np.sign(_f35_revenue_cycle(revenue, 252)) * closeadj * (1.0 + (_f35_revenue_cycle(revenue, 252)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_252d_base_v101_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)) * closeadj * closeadj.pct_change(84)
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_252d_base_v102_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_252d_base_v103_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_252d_base_v104_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 252)).rolling(126, min_periods=max(1, 126//2)).sum() * closeadj / 126
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_378d_base_v105_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_378d_base_v106_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_378d_base_v107_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)) * closeadj * (_f35_revenue_cycle(revenue, 378)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_378d_base_v108_signal(closeadj, revenue):
    result = _mean(_f35_revenue_cycle(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_378d_base_v109_signal(closeadj, revenue):
    result = _std(_f35_revenue_cycle(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_378d_base_v110_signal(closeadj, revenue):
    result = _z(_f35_revenue_cycle(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_378d_base_v111_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)).ewm(span=189, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_378d_base_v112_signal(closeadj, revenue):
    result = np.log((_f35_revenue_cycle(revenue, 378)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_378d_base_v113_signal(closeadj, revenue):
    result = np.sign(_f35_revenue_cycle(revenue, 378)) * closeadj * (1.0 + (_f35_revenue_cycle(revenue, 378)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_378d_base_v114_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)) * closeadj * closeadj.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_378d_base_v115_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_378d_base_v116_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_378d_base_v117_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 378)).rolling(189, min_periods=max(1, 189//2)).sum() * closeadj / 189
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_504d_base_v118_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_504d_base_v119_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_504d_base_v120_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)) * closeadj * (_f35_revenue_cycle(revenue, 504)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_504d_base_v121_signal(closeadj, revenue):
    result = _mean(_f35_revenue_cycle(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_504d_base_v122_signal(closeadj, revenue):
    result = _std(_f35_revenue_cycle(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_504d_base_v123_signal(closeadj, revenue):
    result = _z(_f35_revenue_cycle(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_504d_base_v124_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_504d_base_v125_signal(closeadj, revenue):
    result = np.log((_f35_revenue_cycle(revenue, 504)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_504d_base_v126_signal(closeadj, revenue):
    result = np.sign(_f35_revenue_cycle(revenue, 504)) * closeadj * (1.0 + (_f35_revenue_cycle(revenue, 504)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_504d_base_v127_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)) * closeadj * closeadj.pct_change(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_504d_base_v128_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_504d_base_v129_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_504d_base_v130_signal(closeadj, revenue):
    result = (_f35_revenue_cycle(revenue, 504)).rolling(252, min_periods=max(1, 252//2)).sum() * closeadj / 252
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xcls_5d_base_v131_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclsabs_5d_base_v132_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclssq_5d_base_v133_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj * (_f35_subsidy_proxy(revenue, ebitdamargin, 5)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xmcls_5d_base_v134_signal(closeadj, revenue, ebitdamargin):
    result = _mean(_f35_subsidy_proxy(revenue, ebitdamargin, 5), 26) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xstdcls_5d_base_v135_signal(closeadj, revenue, ebitdamargin):
    result = _std(_f35_subsidy_proxy(revenue, ebitdamargin, 5), 26) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xzcls_5d_base_v136_signal(closeadj, revenue, ebitdamargin):
    result = _z(_f35_subsidy_proxy(revenue, ebitdamargin, 5), 26) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xemacls_5d_base_v137_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)).ewm(span=26, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xlogcls_5d_base_v138_signal(closeadj, revenue, ebitdamargin):
    result = np.log((_f35_subsidy_proxy(revenue, ebitdamargin, 5)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xsgncls_5d_base_v139_signal(closeadj, revenue, ebitdamargin):
    result = np.sign(_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj * (1.0 + (_f35_subsidy_proxy(revenue, ebitdamargin, 5)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclsret_5d_base_v140_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj * closeadj.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclsema21_5d_base_v141_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclsma63_5d_base_v142_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xcumcls_5d_base_v143_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 5)).rolling(26, min_periods=max(1, 26//2)).sum() * closeadj / 26
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xcls_10d_base_v144_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclsabs_10d_base_v145_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xclssq_10d_base_v146_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 10)) * closeadj * (_f35_subsidy_proxy(revenue, ebitdamargin, 10)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xmcls_10d_base_v147_signal(closeadj, revenue, ebitdamargin):
    result = _mean(_f35_subsidy_proxy(revenue, ebitdamargin, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xstdcls_10d_base_v148_signal(closeadj, revenue, ebitdamargin):
    result = _std(_f35_subsidy_proxy(revenue, ebitdamargin, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xzcls_10d_base_v149_signal(closeadj, revenue, ebitdamargin):
    result = _z(_f35_subsidy_proxy(revenue, ebitdamargin, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35rsc_f35_regulatory_subsidy_cycle_p1_xemacls_10d_base_v150_signal(closeadj, revenue, ebitdamargin):
    result = (_f35_subsidy_proxy(revenue, ebitdamargin, 10)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_126d_base_v076_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_126d_base_v077_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_126d_base_v078_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_189d_base_v079_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_189d_base_v080_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_189d_base_v081_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_189d_base_v082_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_189d_base_v083_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_189d_base_v084_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_189d_base_v085_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_189d_base_v086_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_189d_base_v087_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_189d_base_v088_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_189d_base_v089_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_189d_base_v090_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_189d_base_v091_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_252d_base_v092_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_252d_base_v093_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_252d_base_v094_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_252d_base_v095_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_252d_base_v096_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_252d_base_v097_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_252d_base_v098_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_252d_base_v099_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_252d_base_v100_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_252d_base_v101_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_252d_base_v102_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_252d_base_v103_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_252d_base_v104_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_378d_base_v105_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_378d_base_v106_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_378d_base_v107_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_378d_base_v108_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_378d_base_v109_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_378d_base_v110_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_378d_base_v111_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_378d_base_v112_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_378d_base_v113_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_378d_base_v114_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_378d_base_v115_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_378d_base_v116_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_378d_base_v117_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcls_504d_base_v118_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsabs_504d_base_v119_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclssq_504d_base_v120_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xmcls_504d_base_v121_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xstdcls_504d_base_v122_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xzcls_504d_base_v123_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xemacls_504d_base_v124_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xlogcls_504d_base_v125_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xsgncls_504d_base_v126_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsret_504d_base_v127_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsema21_504d_base_v128_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xclsma63_504d_base_v129_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p0_xcumcls_504d_base_v130_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xcls_5d_base_v131_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclsabs_5d_base_v132_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclssq_5d_base_v133_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xmcls_5d_base_v134_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xstdcls_5d_base_v135_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xzcls_5d_base_v136_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xemacls_5d_base_v137_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xlogcls_5d_base_v138_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xsgncls_5d_base_v139_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclsret_5d_base_v140_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclsema21_5d_base_v141_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclsma63_5d_base_v142_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xcumcls_5d_base_v143_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xcls_10d_base_v144_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclsabs_10d_base_v145_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xclssq_10d_base_v146_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xmcls_10d_base_v147_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xstdcls_10d_base_v148_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xzcls_10d_base_v149_signal,
    f35rsc_f35_regulatory_subsidy_cycle_p1_xemacls_10d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_REGULATORY_SUBSIDY_CYCLE_REGISTRY_076_150 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f35_revenue_cycle', '_f35_subsidy_proxy', '_f35_policy_cycle_score')
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
    print(f"OK f35_regulatory_subsidy_cycle_base_076_150_claude: {n_features} features pass")
