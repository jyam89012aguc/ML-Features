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
def _f19_margin_floor(netmargin, w):
    return netmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f19_uw_quality(netmargin, w):
    m = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = netmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f19_uw_durability(netmargin, ebitdamargin, w):
    nm = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return nm / em.replace(0, np.nan)

def f19iuq_f19_insurance_underwriting_quality_uwqstd_5d_base_v076_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    result = _std(q, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_8d_base_v077_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    result = _std(q, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_10d_base_v078_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    result = _std(q, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_15d_base_v079_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    result = _std(q, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_21d_base_v080_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    result = _std(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_30d_base_v081_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    result = _std(q, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_42d_base_v082_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    result = _std(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_63d_base_v083_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    result = _std(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_90d_base_v084_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    result = _std(q, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_126d_base_v085_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    result = _std(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_150d_base_v086_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    result = _std(q, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_189d_base_v087_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    result = _std(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_252d_base_v088_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    result = _std(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_378d_base_v089_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    result = _std(q, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_504d_base_v090_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    result = _std(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_5d_base_v091_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_8d_base_v092_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_10d_base_v093_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_15d_base_v094_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_21d_base_v095_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_30d_base_v096_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_42d_base_v097_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_63d_base_v098_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_90d_base_v099_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_126d_base_v100_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_150d_base_v101_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_189d_base_v102_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_252d_base_v103_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_378d_base_v104_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_504d_base_v105_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_5d_base_v106_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    result = _ema(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_8d_base_v107_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    result = _ema(d, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_10d_base_v108_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_15d_base_v109_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    result = _ema(d, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_21d_base_v110_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_30d_base_v111_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    result = _ema(d, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_42d_base_v112_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_63d_base_v113_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_90d_base_v114_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    result = _ema(d, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_126d_base_v115_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_150d_base_v116_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    result = _ema(d, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_189d_base_v117_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    result = _ema(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_252d_base_v118_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_378d_base_v119_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_504d_base_v120_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_5d_base_v121_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    result = _z(d, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_8d_base_v122_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    result = _z(d, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_10d_base_v123_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    result = _z(d, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_15d_base_v124_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    result = _z(d, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_21d_base_v125_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    result = _z(d, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_30d_base_v126_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    result = _z(d, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_42d_base_v127_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    result = _z(d, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_63d_base_v128_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    result = _z(d, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_90d_base_v129_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    result = _z(d, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_126d_base_v130_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    result = _z(d, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_150d_base_v131_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    result = _z(d, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_189d_base_v132_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    result = _z(d, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_252d_base_v133_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    result = _z(d, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_378d_base_v134_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    result = _z(d, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_504d_base_v135_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    result = _z(d, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_5d_base_v136_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    result = (mf - mf.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_8d_base_v137_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    result = (mf - mf.shift(8)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_10d_base_v138_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    result = (mf - mf.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_15d_base_v139_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    result = (mf - mf.shift(15)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_21d_base_v140_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    result = (mf - mf.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_30d_base_v141_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    result = (mf - mf.shift(30)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_42d_base_v142_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    result = (mf - mf.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_63d_base_v143_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    result = (mf - mf.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_90d_base_v144_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    result = (mf - mf.shift(90)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_126d_base_v145_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    result = (mf - mf.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_150d_base_v146_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    result = (mf - mf.shift(150)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_189d_base_v147_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    result = (mf - mf.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_252d_base_v148_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    result = (mf - mf.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_378d_base_v149_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    result = (mf - mf.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_504d_base_v150_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    result = (mf - mf.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19iuq_f19_insurance_underwriting_quality_uwqstd_5d_base_v076_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_8d_base_v077_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_10d_base_v078_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_15d_base_v079_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_21d_base_v080_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_30d_base_v081_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_42d_base_v082_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_63d_base_v083_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_90d_base_v084_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_126d_base_v085_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_150d_base_v086_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_189d_base_v087_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_252d_base_v088_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_378d_base_v089_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_504d_base_v090_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_5d_base_v091_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_8d_base_v092_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_10d_base_v093_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_15d_base_v094_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_21d_base_v095_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_30d_base_v096_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_42d_base_v097_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_63d_base_v098_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_90d_base_v099_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_126d_base_v100_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_150d_base_v101_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_189d_base_v102_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_252d_base_v103_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_378d_base_v104_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_504d_base_v105_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_5d_base_v106_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_8d_base_v107_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_10d_base_v108_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_15d_base_v109_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_21d_base_v110_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_30d_base_v111_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_42d_base_v112_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_63d_base_v113_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_90d_base_v114_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_126d_base_v115_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_150d_base_v116_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_189d_base_v117_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_252d_base_v118_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_378d_base_v119_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_504d_base_v120_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_5d_base_v121_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_8d_base_v122_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_10d_base_v123_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_15d_base_v124_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_21d_base_v125_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_30d_base_v126_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_42d_base_v127_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_63d_base_v128_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_90d_base_v129_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_126d_base_v130_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_150d_base_v131_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_189d_base_v132_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_252d_base_v133_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_378d_base_v134_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_504d_base_v135_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_5d_base_v136_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_8d_base_v137_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_10d_base_v138_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_15d_base_v139_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_21d_base_v140_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_30d_base_v141_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_42d_base_v142_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_63d_base_v143_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_90d_base_v144_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_126d_base_v145_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_150d_base_v146_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_189d_base_v147_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_252d_base_v148_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_378d_base_v149_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_INSURANCE_UNDERWRITING_QUALITY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f19_margin_floor", "_f19_uw_quality", "_f19_uw_durability",)
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
    print(f"OK f19_insurance_underwriting_quality_076_150_claude: {n_features} features pass")
