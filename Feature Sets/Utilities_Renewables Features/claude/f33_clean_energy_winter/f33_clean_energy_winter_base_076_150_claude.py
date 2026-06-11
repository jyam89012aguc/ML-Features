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
def _f33_revenue_drawdown(revenue, w):
    pk = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    return (revenue - pk) / pk.abs()


def _f33_collapse_signature(revenue, ebitda, w):
    pk_r = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    pk_e = ebitda.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    return ((revenue - pk_r) / pk_r.abs()) + ((ebitda - pk_e) / pk_e.abs())


def _f33_winter_score(revenue, fcf, w):
    rdd = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).max()) / revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan).abs()
    fcf_neg = (fcf < 0).astype(float)
    return rdd.abs() * (1.0 + fcf_neg)

def f33cew_f33_clean_energy_winter_p0_xclsema21_189d_base_v076_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_189d_base_v077_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_189d_base_v078_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)).rolling(94, min_periods=max(1, 94//2)).sum() * closeadj / 94
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_252d_base_v079_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_252d_base_v080_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_252d_base_v081_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)) * closeadj * (_f33_revenue_drawdown(revenue, 252)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_252d_base_v082_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_252d_base_v083_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_252d_base_v084_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_252d_base_v085_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_252d_base_v086_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 252)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_252d_base_v087_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 252)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 252)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_252d_base_v088_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)) * closeadj * closeadj.pct_change(84)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_252d_base_v089_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_252d_base_v090_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_252d_base_v091_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 252)).rolling(126, min_periods=max(1, 126//2)).sum() * closeadj / 126
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_378d_base_v092_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_378d_base_v093_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_378d_base_v094_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)) * closeadj * (_f33_revenue_drawdown(revenue, 378)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_378d_base_v095_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_378d_base_v096_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_378d_base_v097_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_378d_base_v098_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)).ewm(span=189, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_378d_base_v099_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 378)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_378d_base_v100_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 378)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 378)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_378d_base_v101_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)) * closeadj * closeadj.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_378d_base_v102_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_378d_base_v103_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_378d_base_v104_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 378)).rolling(189, min_periods=max(1, 189//2)).sum() * closeadj / 189
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_504d_base_v105_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_504d_base_v106_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_504d_base_v107_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)) * closeadj * (_f33_revenue_drawdown(revenue, 504)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_504d_base_v108_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_504d_base_v109_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_504d_base_v110_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_504d_base_v111_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_504d_base_v112_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 504)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_504d_base_v113_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 504)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 504)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_504d_base_v114_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)) * closeadj * closeadj.pct_change(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_504d_base_v115_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_504d_base_v116_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_504d_base_v117_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 504)).rolling(252, min_periods=max(1, 252//2)).sum() * closeadj / 252
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xcls_10d_base_v118_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsabs_10d_base_v119_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclssq_10d_base_v120_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)) * closeadj * (_f33_collapse_signature(revenue, ebitda, 10)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xmcls_10d_base_v121_signal(closeadj, revenue, ebitda):
    result = _mean(_f33_collapse_signature(revenue, ebitda, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xstdcls_10d_base_v122_signal(closeadj, revenue, ebitda):
    result = _std(_f33_collapse_signature(revenue, ebitda, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xzcls_10d_base_v123_signal(closeadj, revenue, ebitda):
    result = _z(_f33_collapse_signature(revenue, ebitda, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xemacls_10d_base_v124_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xlogcls_10d_base_v125_signal(closeadj, revenue, ebitda):
    result = np.log((_f33_collapse_signature(revenue, ebitda, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xsgncls_10d_base_v126_signal(closeadj, revenue, ebitda):
    result = np.sign(_f33_collapse_signature(revenue, ebitda, 10)) * closeadj * (1.0 + (_f33_collapse_signature(revenue, ebitda, 10)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsret_10d_base_v127_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)) * closeadj * closeadj.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsema21_10d_base_v128_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsma63_10d_base_v129_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xcumcls_10d_base_v130_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xcls_21d_base_v131_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsabs_21d_base_v132_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclssq_21d_base_v133_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)) * closeadj * (_f33_collapse_signature(revenue, ebitda, 21)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xmcls_21d_base_v134_signal(closeadj, revenue, ebitda):
    result = _mean(_f33_collapse_signature(revenue, ebitda, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xstdcls_21d_base_v135_signal(closeadj, revenue, ebitda):
    result = _std(_f33_collapse_signature(revenue, ebitda, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xzcls_21d_base_v136_signal(closeadj, revenue, ebitda):
    result = _z(_f33_collapse_signature(revenue, ebitda, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xemacls_21d_base_v137_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)).ewm(span=10, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xlogcls_21d_base_v138_signal(closeadj, revenue, ebitda):
    result = np.log((_f33_collapse_signature(revenue, ebitda, 21)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xsgncls_21d_base_v139_signal(closeadj, revenue, ebitda):
    result = np.sign(_f33_collapse_signature(revenue, ebitda, 21)) * closeadj * (1.0 + (_f33_collapse_signature(revenue, ebitda, 21)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsret_21d_base_v140_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)) * closeadj * closeadj.pct_change(7)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsema21_21d_base_v141_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsma63_21d_base_v142_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xcumcls_21d_base_v143_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 21)).rolling(10, min_periods=max(1, 10//2)).sum() * closeadj / 10
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xcls_42d_base_v144_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclsabs_42d_base_v145_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 42)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xclssq_42d_base_v146_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 42)) * closeadj * (_f33_collapse_signature(revenue, ebitda, 42)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xmcls_42d_base_v147_signal(closeadj, revenue, ebitda):
    result = _mean(_f33_collapse_signature(revenue, ebitda, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xstdcls_42d_base_v148_signal(closeadj, revenue, ebitda):
    result = _std(_f33_collapse_signature(revenue, ebitda, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xzcls_42d_base_v149_signal(closeadj, revenue, ebitda):
    result = _z(_f33_collapse_signature(revenue, ebitda, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p1_xemacls_42d_base_v150_signal(closeadj, revenue, ebitda):
    result = (_f33_collapse_signature(revenue, ebitda, 42)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33cew_f33_clean_energy_winter_p0_xclsema21_189d_base_v076_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_189d_base_v077_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_189d_base_v078_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_252d_base_v079_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_252d_base_v080_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_252d_base_v081_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_252d_base_v082_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_252d_base_v083_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_252d_base_v084_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_252d_base_v085_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_252d_base_v086_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_252d_base_v087_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_252d_base_v088_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_252d_base_v089_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_252d_base_v090_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_252d_base_v091_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_378d_base_v092_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_378d_base_v093_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_378d_base_v094_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_378d_base_v095_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_378d_base_v096_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_378d_base_v097_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_378d_base_v098_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_378d_base_v099_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_378d_base_v100_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_378d_base_v101_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_378d_base_v102_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_378d_base_v103_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_378d_base_v104_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_504d_base_v105_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_504d_base_v106_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_504d_base_v107_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_504d_base_v108_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_504d_base_v109_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_504d_base_v110_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_504d_base_v111_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_504d_base_v112_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_504d_base_v113_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_504d_base_v114_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_504d_base_v115_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_504d_base_v116_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_504d_base_v117_signal,
    f33cew_f33_clean_energy_winter_p1_xcls_10d_base_v118_signal,
    f33cew_f33_clean_energy_winter_p1_xclsabs_10d_base_v119_signal,
    f33cew_f33_clean_energy_winter_p1_xclssq_10d_base_v120_signal,
    f33cew_f33_clean_energy_winter_p1_xmcls_10d_base_v121_signal,
    f33cew_f33_clean_energy_winter_p1_xstdcls_10d_base_v122_signal,
    f33cew_f33_clean_energy_winter_p1_xzcls_10d_base_v123_signal,
    f33cew_f33_clean_energy_winter_p1_xemacls_10d_base_v124_signal,
    f33cew_f33_clean_energy_winter_p1_xlogcls_10d_base_v125_signal,
    f33cew_f33_clean_energy_winter_p1_xsgncls_10d_base_v126_signal,
    f33cew_f33_clean_energy_winter_p1_xclsret_10d_base_v127_signal,
    f33cew_f33_clean_energy_winter_p1_xclsema21_10d_base_v128_signal,
    f33cew_f33_clean_energy_winter_p1_xclsma63_10d_base_v129_signal,
    f33cew_f33_clean_energy_winter_p1_xcumcls_10d_base_v130_signal,
    f33cew_f33_clean_energy_winter_p1_xcls_21d_base_v131_signal,
    f33cew_f33_clean_energy_winter_p1_xclsabs_21d_base_v132_signal,
    f33cew_f33_clean_energy_winter_p1_xclssq_21d_base_v133_signal,
    f33cew_f33_clean_energy_winter_p1_xmcls_21d_base_v134_signal,
    f33cew_f33_clean_energy_winter_p1_xstdcls_21d_base_v135_signal,
    f33cew_f33_clean_energy_winter_p1_xzcls_21d_base_v136_signal,
    f33cew_f33_clean_energy_winter_p1_xemacls_21d_base_v137_signal,
    f33cew_f33_clean_energy_winter_p1_xlogcls_21d_base_v138_signal,
    f33cew_f33_clean_energy_winter_p1_xsgncls_21d_base_v139_signal,
    f33cew_f33_clean_energy_winter_p1_xclsret_21d_base_v140_signal,
    f33cew_f33_clean_energy_winter_p1_xclsema21_21d_base_v141_signal,
    f33cew_f33_clean_energy_winter_p1_xclsma63_21d_base_v142_signal,
    f33cew_f33_clean_energy_winter_p1_xcumcls_21d_base_v143_signal,
    f33cew_f33_clean_energy_winter_p1_xcls_42d_base_v144_signal,
    f33cew_f33_clean_energy_winter_p1_xclsabs_42d_base_v145_signal,
    f33cew_f33_clean_energy_winter_p1_xclssq_42d_base_v146_signal,
    f33cew_f33_clean_energy_winter_p1_xmcls_42d_base_v147_signal,
    f33cew_f33_clean_energy_winter_p1_xstdcls_42d_base_v148_signal,
    f33cew_f33_clean_energy_winter_p1_xzcls_42d_base_v149_signal,
    f33cew_f33_clean_energy_winter_p1_xemacls_42d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CLEAN_ENERGY_WINTER_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f33_revenue_drawdown', '_f33_collapse_signature', '_f33_winter_score')
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
    print(f"OK f33_clean_energy_winter_base_076_150_claude: {n_features} features pass")
