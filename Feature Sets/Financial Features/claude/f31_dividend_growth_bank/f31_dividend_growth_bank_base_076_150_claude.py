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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f31_dps_growth(dps, w):
    return dps.pct_change(periods=w)


def _f31_dividend_compound(dps, w):
    return (dps / dps.shift(w).replace(0, np.nan)).apply(np.log)


def _f31_dividend_coverage(dps, eps, w):
    cov = eps / dps.replace(0, np.nan)
    return cov.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====
def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_5d_base_v076_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 5) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_10d_base_v077_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 10) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_21d_base_v078_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 21) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_42d_base_v079_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 42) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_63d_base_v080_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 63) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_126d_base_v081_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 126) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_189d_base_v082_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 189) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_252d_base_v083_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 252) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_378d_base_v084_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 378) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_504d_base_v085_signal(dps, closeadj):
    result = _f31_dps_growth(dps, 504) * closeadj * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_10d_base_v086_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_21d_base_v087_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_42d_base_v088_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_63d_base_v089_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_126d_base_v090_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_252d_base_v091_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_378d_base_v092_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_504d_base_v093_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_189d_base_v094_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragealt_5d_base_v095_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_21d_base_v096_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 21)
    result = _mean(c, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_42d_base_v097_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 42)
    result = _mean(c, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_63d_base_v098_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 63)
    result = _mean(c, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_126d_base_v099_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 126)
    result = _mean(c, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_189d_base_v100_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 189)
    result = _mean(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_252d_base_v101_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 252)
    result = _mean(c, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_378d_base_v102_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 378)
    result = _mean(c, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_504d_base_v103_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 504)
    result = _mean(c, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_10d_base_v104_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 10)
    result = _mean(c, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcompoundsmooth_5d_base_v105_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 5)
    result = _mean(c, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_63d_base_v106_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 63)
    result = _qrank(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_126d_base_v107_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 126)
    result = _qrank(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_252d_base_v108_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 252)
    result = _qrank(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_504d_base_v109_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 504)
    result = _qrank(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_21d_base_v110_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 21)
    result = _qrank(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_42d_base_v111_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 42)
    result = _qrank(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_21d_base_v112_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 21)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_63d_base_v113_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 63)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_126d_base_v114_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 126)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_252d_base_v115_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 252)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_504d_base_v116_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 504)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covsurplus_42d_base_v117_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 42)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_21d_base_v118_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 21) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_63d_base_v119_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 63) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_126d_base_v120_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 126) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_252d_base_v121_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 252) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_504d_base_v122_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 504) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_42d_base_v123_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 42) * (1.0 - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcomxepsg_21d_base_v124_signal(dps, eps, closeadj):
    c = _f31_dividend_compound(dps, 21)
    eg = eps.pct_change(periods=21)
    result = c * eg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcomxepsg_63d_base_v125_signal(dps, eps, closeadj):
    c = _f31_dividend_compound(dps, 63)
    eg = eps.pct_change(periods=63)
    result = c * eg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcomxepsg_126d_base_v126_signal(dps, eps, closeadj):
    c = _f31_dividend_compound(dps, 126)
    eg = eps.pct_change(periods=126)
    result = c * eg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcomxepsg_252d_base_v127_signal(dps, eps, closeadj):
    c = _f31_dividend_compound(dps, 252)
    eg = eps.pct_change(periods=252)
    result = c * eg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcomxepsg_504d_base_v128_signal(dps, eps, closeadj):
    c = _f31_dividend_compound(dps, 504)
    eg = eps.pct_change(periods=504)
    result = c * eg.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragexc_63d_base_v129_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 63)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragexc_126d_base_v130_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 126)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragexc_252d_base_v131_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 252)
    result = base * _mean(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragexc_504d_base_v132_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 504)
    result = base * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcoveragexc_21d_base_v133_signal(dps, eps, closeadj):
    base = _f31_dividend_coverage(dps, eps, 21)
    result = base * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthema_21d_base_v134_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 21)
    result = _ema(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthema_63d_base_v135_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 63)
    result = _ema(g, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthema_126d_base_v136_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 126)
    result = _ema(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthema_252d_base_v137_signal(dps, closeadj):
    g = _f31_dps_growth(dps, 252)
    result = _ema(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcumcompound_252d_base_v138_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 252)
    result = c.cumsum() * 0.0 + c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcumcompound_504d_base_v139_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 504)
    result = c.cumsum() * 0.0 + c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_divcumcompound_378d_base_v140_signal(dps, closeadj):
    c = _f31_dividend_compound(dps, 378)
    result = c.cumsum() * 0.0 + c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covzminuspayout_63d_base_v141_signal(dps, eps, payoutratio, closeadj):
    base = _f31_dividend_coverage(dps, eps, 63)
    result = (_z(base, 63) - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covzminuspayout_126d_base_v142_signal(dps, eps, payoutratio, closeadj):
    base = _f31_dividend_coverage(dps, eps, 126)
    result = (_z(base, 126) - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covzminuspayout_252d_base_v143_signal(dps, eps, payoutratio, closeadj):
    base = _f31_dividend_coverage(dps, eps, 252)
    result = (_z(base, 252) - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covzminuspayout_504d_base_v144_signal(dps, eps, payoutratio, closeadj):
    base = _f31_dividend_coverage(dps, eps, 504)
    result = (_z(base, 504) - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_covzminuspayout_42d_base_v145_signal(dps, eps, payoutratio, closeadj):
    base = _f31_dividend_coverage(dps, eps, 42)
    result = (_z(base, 42) - payoutratio) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_21d_base_v146_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 21) * (1.0 / (payoutratio.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_63d_base_v147_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 63) * (1.0 / (payoutratio.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_126d_base_v148_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 126) * (1.0 / (payoutratio.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_252d_base_v149_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 252) * (1.0 / (payoutratio.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_504d_base_v150_signal(dps, payoutratio, closeadj):
    result = _f31_dps_growth(dps, 504) * (1.0 / (payoutratio.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_5d_base_v076_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_10d_base_v077_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_21d_base_v078_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_42d_base_v079_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_63d_base_v080_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_126d_base_v081_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_189d_base_v082_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_252d_base_v083_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_378d_base_v084_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxprice_504d_base_v085_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_10d_base_v086_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_21d_base_v087_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_42d_base_v088_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_63d_base_v089_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_126d_base_v090_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_252d_base_v091_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_378d_base_v092_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_504d_base_v093_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_189d_base_v094_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragealt_5d_base_v095_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_21d_base_v096_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_42d_base_v097_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_63d_base_v098_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_126d_base_v099_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_189d_base_v100_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_252d_base_v101_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_378d_base_v102_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_504d_base_v103_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_10d_base_v104_signal,
    f31dgb_f31_dividend_growth_bank_divcompoundsmooth_5d_base_v105_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_63d_base_v106_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_126d_base_v107_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_252d_base_v108_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_504d_base_v109_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_21d_base_v110_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthqrank_42d_base_v111_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_21d_base_v112_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_63d_base_v113_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_126d_base_v114_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_252d_base_v115_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_504d_base_v116_signal,
    f31dgb_f31_dividend_growth_bank_covsurplus_42d_base_v117_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_21d_base_v118_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_63d_base_v119_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_126d_base_v120_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_252d_base_v121_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_504d_base_v122_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthxsafety_42d_base_v123_signal,
    f31dgb_f31_dividend_growth_bank_divcomxepsg_21d_base_v124_signal,
    f31dgb_f31_dividend_growth_bank_divcomxepsg_63d_base_v125_signal,
    f31dgb_f31_dividend_growth_bank_divcomxepsg_126d_base_v126_signal,
    f31dgb_f31_dividend_growth_bank_divcomxepsg_252d_base_v127_signal,
    f31dgb_f31_dividend_growth_bank_divcomxepsg_504d_base_v128_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragexc_63d_base_v129_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragexc_126d_base_v130_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragexc_252d_base_v131_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragexc_504d_base_v132_signal,
    f31dgb_f31_dividend_growth_bank_divcoveragexc_21d_base_v133_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthema_21d_base_v134_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthema_63d_base_v135_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthema_126d_base_v136_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthema_252d_base_v137_signal,
    f31dgb_f31_dividend_growth_bank_divcumcompound_252d_base_v138_signal,
    f31dgb_f31_dividend_growth_bank_divcumcompound_504d_base_v139_signal,
    f31dgb_f31_dividend_growth_bank_divcumcompound_378d_base_v140_signal,
    f31dgb_f31_dividend_growth_bank_covzminuspayout_63d_base_v141_signal,
    f31dgb_f31_dividend_growth_bank_covzminuspayout_126d_base_v142_signal,
    f31dgb_f31_dividend_growth_bank_covzminuspayout_252d_base_v143_signal,
    f31dgb_f31_dividend_growth_bank_covzminuspayout_504d_base_v144_signal,
    f31dgb_f31_dividend_growth_bank_covzminuspayout_42d_base_v145_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_21d_base_v146_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_63d_base_v147_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_126d_base_v148_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_252d_base_v149_signal,
    f31dgb_f31_dividend_growth_bank_dpsgrowthinvpayout_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_DIVIDEND_GROWTH_BANK_REGISTRY_076_150 = REGISTRY



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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_dps_growth", "_f31_dividend_compound", "_f31_dividend_coverage",)
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
    print(f"OK f31_dividend_growth_bank_base_076_150_claude: {n_features} features pass")
