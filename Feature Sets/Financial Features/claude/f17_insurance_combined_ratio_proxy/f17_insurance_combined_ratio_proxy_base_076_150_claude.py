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
def _f17_combined_ratio_proxy(opex, revenue):
    return opex / revenue.replace(0, np.nan)


def _f17_combined_ratio_trend(opex, revenue, w):
    cr = opex / revenue.replace(0, np.nan)
    return cr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_underwriting_efficiency(opex, sgna, revenue, w):
    cr = opex / revenue.replace(0, np.nan)
    sg = sgna / revenue.replace(0, np.nan)
    blend = cr + sg
    return blend.rolling(w, min_periods=max(1, w // 2)).mean()

def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_5d_base_v076_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    result = _z(t, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_8d_base_v077_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    result = _z(t, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_10d_base_v078_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    result = _z(t, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_15d_base_v079_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    result = _z(t, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_21d_base_v080_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    result = _z(t, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_30d_base_v081_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    result = _z(t, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_42d_base_v082_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    result = _z(t, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_63d_base_v083_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    result = _z(t, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_90d_base_v084_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    result = _z(t, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_126d_base_v085_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    result = _z(t, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_150d_base_v086_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    result = _z(t, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_189d_base_v087_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    result = _z(t, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_252d_base_v088_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    result = _z(t, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_378d_base_v089_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    result = _z(t, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_504d_base_v090_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    result = _z(t, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_5d_base_v091_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_8d_base_v092_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_10d_base_v093_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_15d_base_v094_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_21d_base_v095_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_30d_base_v096_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_42d_base_v097_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_63d_base_v098_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_90d_base_v099_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_126d_base_v100_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_150d_base_v101_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_189d_base_v102_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_252d_base_v103_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_378d_base_v104_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_504d_base_v105_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    result = ue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_5d_base_v106_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    result = _ema(ue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_8d_base_v107_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    result = _ema(ue, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_10d_base_v108_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    result = _ema(ue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_15d_base_v109_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    result = _ema(ue, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_21d_base_v110_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    result = _ema(ue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_30d_base_v111_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    result = _ema(ue, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_42d_base_v112_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    result = _ema(ue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_63d_base_v113_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    result = _ema(ue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_90d_base_v114_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    result = _ema(ue, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_126d_base_v115_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    result = _ema(ue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_150d_base_v116_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    result = _ema(ue, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_189d_base_v117_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    result = _ema(ue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_252d_base_v118_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    result = _ema(ue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_378d_base_v119_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    result = _ema(ue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_504d_base_v120_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    result = _ema(ue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_5d_base_v121_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    result = _z(ue, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_8d_base_v122_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    result = _z(ue, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_10d_base_v123_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    result = _z(ue, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_15d_base_v124_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    result = _z(ue, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_21d_base_v125_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    result = _z(ue, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_30d_base_v126_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    result = _z(ue, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_42d_base_v127_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    result = _z(ue, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_63d_base_v128_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    result = _z(ue, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_90d_base_v129_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    result = _z(ue, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_126d_base_v130_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    result = _z(ue, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_150d_base_v131_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    result = _z(ue, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_189d_base_v132_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    result = _z(ue, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_252d_base_v133_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    result = _z(ue, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_378d_base_v134_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    result = _z(ue, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_504d_base_v135_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    result = _z(ue, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_5d_base_v136_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    result = (t - t.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_8d_base_v137_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    result = (t - t.shift(8)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_10d_base_v138_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    result = (t - t.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_15d_base_v139_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    result = (t - t.shift(15)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_21d_base_v140_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    result = (t - t.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_30d_base_v141_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    result = (t - t.shift(30)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_42d_base_v142_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    result = (t - t.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_63d_base_v143_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    result = (t - t.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_90d_base_v144_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    result = (t - t.shift(90)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_126d_base_v145_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    result = (t - t.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_150d_base_v146_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    result = (t - t.shift(150)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_189d_base_v147_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    result = (t - t.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_252d_base_v148_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    result = (t - t.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_378d_base_v149_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    result = (t - t.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_504d_base_v150_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    result = (t - t.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_5d_base_v076_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_8d_base_v077_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_10d_base_v078_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_15d_base_v079_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_21d_base_v080_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_30d_base_v081_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_42d_base_v082_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_63d_base_v083_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_90d_base_v084_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_126d_base_v085_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_150d_base_v086_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_189d_base_v087_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_252d_base_v088_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_378d_base_v089_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_504d_base_v090_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_5d_base_v091_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_8d_base_v092_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_10d_base_v093_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_15d_base_v094_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_21d_base_v095_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_30d_base_v096_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_42d_base_v097_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_63d_base_v098_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_90d_base_v099_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_126d_base_v100_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_150d_base_v101_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_189d_base_v102_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_252d_base_v103_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_378d_base_v104_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_504d_base_v105_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_5d_base_v106_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_8d_base_v107_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_10d_base_v108_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_15d_base_v109_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_21d_base_v110_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_30d_base_v111_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_42d_base_v112_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_63d_base_v113_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_90d_base_v114_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_126d_base_v115_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_150d_base_v116_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_189d_base_v117_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_252d_base_v118_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_378d_base_v119_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_504d_base_v120_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_5d_base_v121_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_8d_base_v122_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_10d_base_v123_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_15d_base_v124_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_21d_base_v125_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_30d_base_v126_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_42d_base_v127_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_63d_base_v128_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_90d_base_v129_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_126d_base_v130_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_150d_base_v131_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_189d_base_v132_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_252d_base_v133_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_378d_base_v134_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_504d_base_v135_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_5d_base_v136_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_8d_base_v137_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_10d_base_v138_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_15d_base_v139_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_21d_base_v140_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_30d_base_v141_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_42d_base_v142_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_63d_base_v143_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_90d_base_v144_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_126d_base_v145_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_150d_base_v146_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_189d_base_v147_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_252d_base_v148_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_378d_base_v149_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_INSURANCE_COMBINED_RATIO_PROXY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f17_combined_ratio_proxy", "_f17_combined_ratio_trend", "_f17_underwriting_efficiency",)
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
    print(f"OK f17_insurance_combined_ratio_proxy_076_150_claude: {n_features} features pass")
