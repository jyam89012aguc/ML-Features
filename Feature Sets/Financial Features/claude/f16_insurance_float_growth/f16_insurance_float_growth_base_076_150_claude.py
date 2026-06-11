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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f16_float_proxy(liabilities, equity):
    return liabilities - equity * 0.0


def _f16_float_growth(liabilities, w):
    return liabilities.pct_change(periods=w)


def _f16_float_leverage(liabilities, equity, w):
    proxy = liabilities - equity * 0.0
    eq = equity.rolling(w, min_periods=max(1, w // 2)).mean()
    return proxy / eq.replace(0, np.nan)

def f16ifg_f16_insurance_float_growth_floatlevsm_5d_base_v076_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    result = _mean(lev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_8d_base_v077_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    result = _mean(lev, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_10d_base_v078_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    result = _mean(lev, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_15d_base_v079_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    result = _mean(lev, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_21d_base_v080_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    result = _mean(lev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_30d_base_v081_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    result = _mean(lev, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_42d_base_v082_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    result = _mean(lev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_63d_base_v083_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    result = _mean(lev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_90d_base_v084_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    result = _mean(lev, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_126d_base_v085_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    result = _mean(lev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_150d_base_v086_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    result = _mean(lev, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_189d_base_v087_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    result = _mean(lev, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_252d_base_v088_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    result = _mean(lev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_378d_base_v089_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    result = _mean(lev, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_504d_base_v090_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    result = _mean(lev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_5d_base_v091_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    result = _ema(g, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_8d_base_v092_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    result = _ema(g, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_10d_base_v093_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    result = _ema(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_15d_base_v094_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    result = _ema(g, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_21d_base_v095_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_30d_base_v096_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    result = _ema(g, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_42d_base_v097_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    result = _ema(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_63d_base_v098_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    result = _ema(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_90d_base_v099_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    result = _ema(g, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_126d_base_v100_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    result = _ema(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_150d_base_v101_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    result = _ema(g, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_189d_base_v102_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    result = _ema(g, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_252d_base_v103_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    result = _ema(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_378d_base_v104_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    result = _ema(g, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_504d_base_v105_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    result = _ema(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_5d_base_v106_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_8d_base_v107_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_10d_base_v108_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_15d_base_v109_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_21d_base_v110_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_30d_base_v111_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_42d_base_v112_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_63d_base_v113_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_90d_base_v114_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_126d_base_v115_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_150d_base_v116_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_189d_base_v117_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_252d_base_v118_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_378d_base_v119_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_504d_base_v120_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _z(fp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_5d_base_v121_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    result = _z(lev, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_8d_base_v122_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    result = _z(lev, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_10d_base_v123_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    result = _z(lev, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_15d_base_v124_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    result = _z(lev, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_21d_base_v125_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    result = _z(lev, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_30d_base_v126_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    result = _z(lev, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_42d_base_v127_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    result = _z(lev, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_63d_base_v128_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    result = _z(lev, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_90d_base_v129_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    result = _z(lev, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_126d_base_v130_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    result = _z(lev, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_150d_base_v131_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    result = _z(lev, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_189d_base_v132_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    result = _z(lev, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_252d_base_v133_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    result = _z(lev, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_378d_base_v134_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    result = _z(lev, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_504d_base_v135_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    result = _z(lev, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_5d_base_v136_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    result = _std(g, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_8d_base_v137_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    result = _std(g, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_10d_base_v138_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    result = _std(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_15d_base_v139_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    result = _std(g, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_21d_base_v140_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_30d_base_v141_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    result = _std(g, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_42d_base_v142_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    result = _std(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_63d_base_v143_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_90d_base_v144_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    result = _std(g, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_126d_base_v145_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    result = _std(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_150d_base_v146_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    result = _std(g, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_189d_base_v147_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    result = _std(g, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_252d_base_v148_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_378d_base_v149_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    result = _std(g, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_504d_base_v150_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    result = _std(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ifg_f16_insurance_float_growth_floatlevsm_5d_base_v076_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_8d_base_v077_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_10d_base_v078_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_15d_base_v079_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_21d_base_v080_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_30d_base_v081_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_42d_base_v082_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_63d_base_v083_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_90d_base_v084_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_126d_base_v085_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_150d_base_v086_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_189d_base_v087_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_252d_base_v088_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_378d_base_v089_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_504d_base_v090_signal,
    f16ifg_f16_insurance_float_growth_floatgema_5d_base_v091_signal,
    f16ifg_f16_insurance_float_growth_floatgema_8d_base_v092_signal,
    f16ifg_f16_insurance_float_growth_floatgema_10d_base_v093_signal,
    f16ifg_f16_insurance_float_growth_floatgema_15d_base_v094_signal,
    f16ifg_f16_insurance_float_growth_floatgema_21d_base_v095_signal,
    f16ifg_f16_insurance_float_growth_floatgema_30d_base_v096_signal,
    f16ifg_f16_insurance_float_growth_floatgema_42d_base_v097_signal,
    f16ifg_f16_insurance_float_growth_floatgema_63d_base_v098_signal,
    f16ifg_f16_insurance_float_growth_floatgema_90d_base_v099_signal,
    f16ifg_f16_insurance_float_growth_floatgema_126d_base_v100_signal,
    f16ifg_f16_insurance_float_growth_floatgema_150d_base_v101_signal,
    f16ifg_f16_insurance_float_growth_floatgema_189d_base_v102_signal,
    f16ifg_f16_insurance_float_growth_floatgema_252d_base_v103_signal,
    f16ifg_f16_insurance_float_growth_floatgema_378d_base_v104_signal,
    f16ifg_f16_insurance_float_growth_floatgema_504d_base_v105_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_5d_base_v106_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_8d_base_v107_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_10d_base_v108_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_15d_base_v109_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_21d_base_v110_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_30d_base_v111_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_42d_base_v112_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_63d_base_v113_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_90d_base_v114_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_126d_base_v115_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_150d_base_v116_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_189d_base_v117_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_252d_base_v118_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_378d_base_v119_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_504d_base_v120_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_5d_base_v121_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_8d_base_v122_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_10d_base_v123_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_15d_base_v124_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_21d_base_v125_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_30d_base_v126_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_42d_base_v127_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_63d_base_v128_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_90d_base_v129_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_126d_base_v130_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_150d_base_v131_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_189d_base_v132_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_252d_base_v133_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_378d_base_v134_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_504d_base_v135_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_5d_base_v136_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_8d_base_v137_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_10d_base_v138_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_15d_base_v139_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_21d_base_v140_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_30d_base_v141_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_42d_base_v142_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_63d_base_v143_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_90d_base_v144_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_126d_base_v145_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_150d_base_v146_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_189d_base_v147_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_252d_base_v148_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_378d_base_v149_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_INSURANCE_FLOAT_GROWTH_REGISTRY_076_150 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "liabilities": liabilities, "equity": equity,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f16_float_proxy", "_f16_float_growth", "_f16_float_leverage",)
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
    print(f"OK f16_insurance_float_growth_076_150_claude: {n_features} features pass")
