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
def _f18_netinc_revenue_ratio(netinc, revenue):
    return netinc / revenue.replace(0, np.nan)


def _f18_investment_income_share(netinc, revenue, w):
    rev_sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    ni_sm = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return ni_sm / rev_sm.replace(0, np.nan)


def _f18_income_quality(netinc, revenue, w):
    ratio = netinc / revenue.replace(0, np.nan)
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)

def f18iii_f18_insurance_investment_income_iishareema_5d_base_v076_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    result = _ema(s, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_8d_base_v077_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    result = _ema(s, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_10d_base_v078_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    result = _ema(s, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_15d_base_v079_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    result = _ema(s, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_21d_base_v080_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    result = _ema(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_30d_base_v081_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    result = _ema(s, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_42d_base_v082_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    result = _ema(s, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_63d_base_v083_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    result = _ema(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_90d_base_v084_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    result = _ema(s, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_126d_base_v085_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    result = _ema(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_150d_base_v086_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    result = _ema(s, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_189d_base_v087_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    result = _ema(s, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_252d_base_v088_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    result = _ema(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_378d_base_v089_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    result = _ema(s, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_504d_base_v090_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    result = _ema(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_5d_base_v091_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    result = _z(s, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_8d_base_v092_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    result = _z(s, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_10d_base_v093_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    result = _z(s, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_15d_base_v094_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    result = _z(s, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_21d_base_v095_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    result = _z(s, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_30d_base_v096_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    result = _z(s, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_42d_base_v097_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    result = _z(s, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_63d_base_v098_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    result = _z(s, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_90d_base_v099_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    result = _z(s, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_126d_base_v100_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    result = _z(s, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_150d_base_v101_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    result = _z(s, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_189d_base_v102_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    result = _z(s, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_252d_base_v103_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    result = _z(s, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_378d_base_v104_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    result = _z(s, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_504d_base_v105_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    result = _z(s, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_5d_base_v106_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 5)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_8d_base_v107_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 8)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_10d_base_v108_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 10)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_15d_base_v109_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 15)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_21d_base_v110_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 21)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_30d_base_v111_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 30)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_42d_base_v112_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 42)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_63d_base_v113_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 63)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_90d_base_v114_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 90)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_126d_base_v115_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 126)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_150d_base_v116_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 150)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_189d_base_v117_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 189)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_252d_base_v118_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 252)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_378d_base_v119_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 378)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_504d_base_v120_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 504)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_5d_base_v121_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 5)
    result = _ema(q, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_8d_base_v122_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 8)
    result = _ema(q, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_10d_base_v123_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 10)
    result = _ema(q, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_15d_base_v124_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 15)
    result = _ema(q, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_21d_base_v125_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 21)
    result = _ema(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_30d_base_v126_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 30)
    result = _ema(q, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_42d_base_v127_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 42)
    result = _ema(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_63d_base_v128_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 63)
    result = _ema(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_90d_base_v129_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 90)
    result = _ema(q, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_126d_base_v130_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 126)
    result = _ema(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_150d_base_v131_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 150)
    result = _ema(q, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_189d_base_v132_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 189)
    result = _ema(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_252d_base_v133_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 252)
    result = _ema(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_378d_base_v134_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 378)
    result = _ema(q, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_504d_base_v135_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 504)
    result = _ema(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_5d_base_v136_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    result = (s - s.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_8d_base_v137_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    result = (s - s.shift(8)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_10d_base_v138_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    result = (s - s.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_15d_base_v139_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    result = (s - s.shift(15)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_21d_base_v140_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    result = (s - s.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_30d_base_v141_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    result = (s - s.shift(30)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_42d_base_v142_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    result = (s - s.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_63d_base_v143_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    result = (s - s.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_90d_base_v144_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    result = (s - s.shift(90)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_126d_base_v145_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    result = (s - s.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_150d_base_v146_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    result = (s - s.shift(150)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_189d_base_v147_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    result = (s - s.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_252d_base_v148_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    result = (s - s.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_378d_base_v149_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    result = (s - s.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_504d_base_v150_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    result = (s - s.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18iii_f18_insurance_investment_income_iishareema_5d_base_v076_signal,
    f18iii_f18_insurance_investment_income_iishareema_8d_base_v077_signal,
    f18iii_f18_insurance_investment_income_iishareema_10d_base_v078_signal,
    f18iii_f18_insurance_investment_income_iishareema_15d_base_v079_signal,
    f18iii_f18_insurance_investment_income_iishareema_21d_base_v080_signal,
    f18iii_f18_insurance_investment_income_iishareema_30d_base_v081_signal,
    f18iii_f18_insurance_investment_income_iishareema_42d_base_v082_signal,
    f18iii_f18_insurance_investment_income_iishareema_63d_base_v083_signal,
    f18iii_f18_insurance_investment_income_iishareema_90d_base_v084_signal,
    f18iii_f18_insurance_investment_income_iishareema_126d_base_v085_signal,
    f18iii_f18_insurance_investment_income_iishareema_150d_base_v086_signal,
    f18iii_f18_insurance_investment_income_iishareema_189d_base_v087_signal,
    f18iii_f18_insurance_investment_income_iishareema_252d_base_v088_signal,
    f18iii_f18_insurance_investment_income_iishareema_378d_base_v089_signal,
    f18iii_f18_insurance_investment_income_iishareema_504d_base_v090_signal,
    f18iii_f18_insurance_investment_income_iisharez_5d_base_v091_signal,
    f18iii_f18_insurance_investment_income_iisharez_8d_base_v092_signal,
    f18iii_f18_insurance_investment_income_iisharez_10d_base_v093_signal,
    f18iii_f18_insurance_investment_income_iisharez_15d_base_v094_signal,
    f18iii_f18_insurance_investment_income_iisharez_21d_base_v095_signal,
    f18iii_f18_insurance_investment_income_iisharez_30d_base_v096_signal,
    f18iii_f18_insurance_investment_income_iisharez_42d_base_v097_signal,
    f18iii_f18_insurance_investment_income_iisharez_63d_base_v098_signal,
    f18iii_f18_insurance_investment_income_iisharez_90d_base_v099_signal,
    f18iii_f18_insurance_investment_income_iisharez_126d_base_v100_signal,
    f18iii_f18_insurance_investment_income_iisharez_150d_base_v101_signal,
    f18iii_f18_insurance_investment_income_iisharez_189d_base_v102_signal,
    f18iii_f18_insurance_investment_income_iisharez_252d_base_v103_signal,
    f18iii_f18_insurance_investment_income_iisharez_378d_base_v104_signal,
    f18iii_f18_insurance_investment_income_iisharez_504d_base_v105_signal,
    f18iii_f18_insurance_investment_income_iq_5d_base_v106_signal,
    f18iii_f18_insurance_investment_income_iq_8d_base_v107_signal,
    f18iii_f18_insurance_investment_income_iq_10d_base_v108_signal,
    f18iii_f18_insurance_investment_income_iq_15d_base_v109_signal,
    f18iii_f18_insurance_investment_income_iq_21d_base_v110_signal,
    f18iii_f18_insurance_investment_income_iq_30d_base_v111_signal,
    f18iii_f18_insurance_investment_income_iq_42d_base_v112_signal,
    f18iii_f18_insurance_investment_income_iq_63d_base_v113_signal,
    f18iii_f18_insurance_investment_income_iq_90d_base_v114_signal,
    f18iii_f18_insurance_investment_income_iq_126d_base_v115_signal,
    f18iii_f18_insurance_investment_income_iq_150d_base_v116_signal,
    f18iii_f18_insurance_investment_income_iq_189d_base_v117_signal,
    f18iii_f18_insurance_investment_income_iq_252d_base_v118_signal,
    f18iii_f18_insurance_investment_income_iq_378d_base_v119_signal,
    f18iii_f18_insurance_investment_income_iq_504d_base_v120_signal,
    f18iii_f18_insurance_investment_income_iqema_5d_base_v121_signal,
    f18iii_f18_insurance_investment_income_iqema_8d_base_v122_signal,
    f18iii_f18_insurance_investment_income_iqema_10d_base_v123_signal,
    f18iii_f18_insurance_investment_income_iqema_15d_base_v124_signal,
    f18iii_f18_insurance_investment_income_iqema_21d_base_v125_signal,
    f18iii_f18_insurance_investment_income_iqema_30d_base_v126_signal,
    f18iii_f18_insurance_investment_income_iqema_42d_base_v127_signal,
    f18iii_f18_insurance_investment_income_iqema_63d_base_v128_signal,
    f18iii_f18_insurance_investment_income_iqema_90d_base_v129_signal,
    f18iii_f18_insurance_investment_income_iqema_126d_base_v130_signal,
    f18iii_f18_insurance_investment_income_iqema_150d_base_v131_signal,
    f18iii_f18_insurance_investment_income_iqema_189d_base_v132_signal,
    f18iii_f18_insurance_investment_income_iqema_252d_base_v133_signal,
    f18iii_f18_insurance_investment_income_iqema_378d_base_v134_signal,
    f18iii_f18_insurance_investment_income_iqema_504d_base_v135_signal,
    f18iii_f18_insurance_investment_income_iisharediff_5d_base_v136_signal,
    f18iii_f18_insurance_investment_income_iisharediff_8d_base_v137_signal,
    f18iii_f18_insurance_investment_income_iisharediff_10d_base_v138_signal,
    f18iii_f18_insurance_investment_income_iisharediff_15d_base_v139_signal,
    f18iii_f18_insurance_investment_income_iisharediff_21d_base_v140_signal,
    f18iii_f18_insurance_investment_income_iisharediff_30d_base_v141_signal,
    f18iii_f18_insurance_investment_income_iisharediff_42d_base_v142_signal,
    f18iii_f18_insurance_investment_income_iisharediff_63d_base_v143_signal,
    f18iii_f18_insurance_investment_income_iisharediff_90d_base_v144_signal,
    f18iii_f18_insurance_investment_income_iisharediff_126d_base_v145_signal,
    f18iii_f18_insurance_investment_income_iisharediff_150d_base_v146_signal,
    f18iii_f18_insurance_investment_income_iisharediff_189d_base_v147_signal,
    f18iii_f18_insurance_investment_income_iisharediff_252d_base_v148_signal,
    f18iii_f18_insurance_investment_income_iisharediff_378d_base_v149_signal,
    f18iii_f18_insurance_investment_income_iisharediff_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INSURANCE_INVESTMENT_INCOME_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f18_netinc_revenue_ratio", "_f18_investment_income_share", "_f18_income_quality",)
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
    print(f"OK f18_insurance_investment_income_076_150_claude: {n_features} features pass")
