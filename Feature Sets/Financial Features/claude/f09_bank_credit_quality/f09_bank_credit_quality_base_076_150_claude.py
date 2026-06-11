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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _f09_earnings_vol(netinc, w):
    return netinc.rolling(w, min_periods=max(1, w // 2)).std()


def _f09_credit_quality_score(netinc, revenue, w):
    ratio = netinc / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f09_provision_proxy(netinc, w):
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return sd / m.replace(0, np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_63d_base_v076_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    rnk = cq.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_126d_base_v077_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    rnk = cq.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrank_252d_base_v078_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    rnk = cq.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_63d_base_v079_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    rnk = pp.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_126d_base_v080_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    rnk = pp.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxrank_252d_base_v081_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    rnk = pp.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_21d_base_v082_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21)
    result = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_63d_base_v083_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    result = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvollog_252d_base_v084_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    result = np.log(ev.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_21d_base_v085_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = ev * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_63d_base_v086_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = ev * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_126d_base_v087_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = ev * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxqual_252d_base_v088_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = ev * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_21d_base_v089_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = pp * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_63d_base_v090_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = pp * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_126d_base_v091_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = pp * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provxqual_252d_base_v092_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = pp * cq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_21v63_base_v093_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 21)
    b = _f09_earnings_vol(netinc, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_21v63_base_v094_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 21)
    b = _f09_credit_quality_score(netinc, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_63v252_base_v095_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 63)
    b = _f09_earnings_vol(netinc, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_63v252_base_v096_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 63)
    b = _f09_credit_quality_score(netinc, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_126v504_base_v097_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 126)
    b = _f09_earnings_vol(netinc, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_126v504_base_v098_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 126)
    b = _f09_credit_quality_score(netinc, revenue, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolratio_42v189_base_v099_signal(netinc, closeadj):
    a = _f09_earnings_vol(netinc, 42)
    b = _f09_earnings_vol(netinc, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualratio_42v189_base_v100_signal(netinc, revenue, closeadj):
    a = _f09_credit_quality_score(netinc, revenue, 42)
    b = _f09_credit_quality_score(netinc, revenue, 189)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_21d_base_v101_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 21)
    rev_chg = revenue.pct_change(periods=21)
    result = ev / _mean(revenue.abs(), 21).replace(0, np.nan) * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_63d_base_v102_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 63)
    rev_chg = revenue.pct_change(periods=63)
    result = ev / _mean(revenue.abs(), 63).replace(0, np.nan) * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_126d_base_v103_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 126)
    rev_chg = revenue.pct_change(periods=126)
    result = ev / _mean(revenue.abs(), 126).replace(0, np.nan) * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxrev_252d_base_v104_signal(netinc, revenue, closeadj):
    ev = _f09_earnings_vol(netinc, 252)
    rev_chg = revenue.pct_change(periods=252)
    result = ev / _mean(revenue.abs(), 252).replace(0, np.nan) * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_63d_base_v105_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    rng = cq.rolling(63, min_periods=max(1, 63//2)).max() - cq.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_126d_base_v106_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    rng = cq.rolling(126, min_periods=max(1, 126//2)).max() - cq.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualrange_252d_base_v107_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    rng = cq.rolling(252, min_periods=max(1, 252//2)).max() - cq.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_21d_base_v108_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    result = _std(pp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_63d_base_v109_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    result = _std(pp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_126d_base_v110_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    result = _std(pp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxstd_252d_base_v111_signal(netinc, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    result = _std(pp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_21d_base_v112_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    result = _std(cq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_63d_base_v113_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    result = _std(cq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_126d_base_v114_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    result = _std(cq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualstd_252d_base_v115_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    result = _std(cq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_21d_base_v116_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    result = ev * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_63d_base_v117_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    result = ev * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_126d_base_v118_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    result = ev * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxprcvol_252d_base_v119_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    result = ev * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_5d_base_v120_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 5)
    rev_m = _mean(revenue.abs(), 5).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_10d_base_v121_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 10)
    rev_m = _mean(revenue.abs(), 10).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_21d_base_v122_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 21)
    rev_m = _mean(revenue.abs(), 21).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_42d_base_v123_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 42)
    rev_m = _mean(revenue.abs(), 42).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_63d_base_v124_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 63)
    rev_m = _mean(revenue.abs(), 63).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_126d_base_v125_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 126)
    rev_m = _mean(revenue.abs(), 126).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_189d_base_v126_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 189)
    rev_m = _mean(revenue.abs(), 189).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_252d_base_v127_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 252)
    rev_m = _mean(revenue.abs(), 252).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_378d_base_v128_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 378)
    rev_m = _mean(revenue.abs(), 378).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolxclose_504d_base_v129_signal(netinc, revenue, closeadj):
    base = _f09_earnings_vol(netinc, 504)
    rev_m = _mean(revenue.abs(), 504).replace(0, np.nan)
    result = base / rev_m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_21d_base_v130_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = ev.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_42d_base_v131_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    result = ev.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_63d_base_v132_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = ev.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_126d_base_v133_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = ev.rolling(126, min_periods=max(1, 126//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_189d_base_v134_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 189) / _mean(netinc.abs(), 189).replace(0, np.nan)
    result = ev.rolling(189, min_periods=max(1, 189//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_252d_base_v135_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = ev.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_378d_base_v136_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 378) / _mean(netinc.abs(), 378).replace(0, np.nan)
    result = ev.rolling(378, min_periods=max(1, 378//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolacc_504d_base_v137_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 504) / _mean(netinc.abs(), 504).replace(0, np.nan)
    result = ev.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_21d_base_v138_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 21)
    cv = _std(closeadj.pct_change(), 21)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_42d_base_v139_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 42)
    cv = _std(closeadj.pct_change(), 42)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_63d_base_v140_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 63)
    cv = _std(closeadj.pct_change(), 63)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_126d_base_v141_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 126)
    cv = _std(closeadj.pct_change(), 126)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_189d_base_v142_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 189)
    cv = _std(closeadj.pct_change(), 189)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_creditqualxvol_252d_base_v143_signal(netinc, revenue, closeadj):
    cq = _f09_credit_quality_score(netinc, revenue, 252)
    cv = _std(closeadj.pct_change(), 252)
    result = cq * cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_21d_base_v144_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 21)
    rg = revenue.pct_change(periods=21)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_42d_base_v145_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 42)
    rg = revenue.pct_change(periods=42)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_63d_base_v146_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 63)
    rg = revenue.pct_change(periods=63)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_126d_base_v147_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 126)
    rg = revenue.pct_change(periods=126)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_189d_base_v148_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 189)
    rg = revenue.pct_change(periods=189)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_provproxxrev_252d_base_v149_signal(netinc, revenue, closeadj):
    pp = _f09_provision_proxy(netinc, 252)
    rg = revenue.pct_change(periods=252)
    result = pp * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09bcq_f09_bank_credit_quality_earnvolemapct_21d_base_v150_signal(netinc, closeadj):
    ev = _f09_earnings_vol(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = _ema(ev, 21).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09bcq_f09_bank_credit_quality_creditqualrank_63d_base_v076_signal,
    f09bcq_f09_bank_credit_quality_creditqualrank_126d_base_v077_signal,
    f09bcq_f09_bank_credit_quality_creditqualrank_252d_base_v078_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_63d_base_v079_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_126d_base_v080_signal,
    f09bcq_f09_bank_credit_quality_provproxrank_252d_base_v081_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_21d_base_v082_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_63d_base_v083_signal,
    f09bcq_f09_bank_credit_quality_earnvollog_252d_base_v084_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_21d_base_v085_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_63d_base_v086_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_126d_base_v087_signal,
    f09bcq_f09_bank_credit_quality_earnvolxqual_252d_base_v088_signal,
    f09bcq_f09_bank_credit_quality_provxqual_21d_base_v089_signal,
    f09bcq_f09_bank_credit_quality_provxqual_63d_base_v090_signal,
    f09bcq_f09_bank_credit_quality_provxqual_126d_base_v091_signal,
    f09bcq_f09_bank_credit_quality_provxqual_252d_base_v092_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_21v63_base_v093_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_21v63_base_v094_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_63v252_base_v095_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_63v252_base_v096_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_126v504_base_v097_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_126v504_base_v098_signal,
    f09bcq_f09_bank_credit_quality_earnvolratio_42v189_base_v099_signal,
    f09bcq_f09_bank_credit_quality_creditqualratio_42v189_base_v100_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_21d_base_v101_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_63d_base_v102_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_126d_base_v103_signal,
    f09bcq_f09_bank_credit_quality_earnvolxrev_252d_base_v104_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_63d_base_v105_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_126d_base_v106_signal,
    f09bcq_f09_bank_credit_quality_creditqualrange_252d_base_v107_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_21d_base_v108_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_63d_base_v109_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_126d_base_v110_signal,
    f09bcq_f09_bank_credit_quality_provproxstd_252d_base_v111_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_21d_base_v112_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_63d_base_v113_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_126d_base_v114_signal,
    f09bcq_f09_bank_credit_quality_creditqualstd_252d_base_v115_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_21d_base_v116_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_63d_base_v117_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_126d_base_v118_signal,
    f09bcq_f09_bank_credit_quality_earnvolxprcvol_252d_base_v119_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_5d_base_v120_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_10d_base_v121_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_21d_base_v122_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_42d_base_v123_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_63d_base_v124_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_126d_base_v125_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_189d_base_v126_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_252d_base_v127_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_378d_base_v128_signal,
    f09bcq_f09_bank_credit_quality_earnvolxclose_504d_base_v129_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_21d_base_v130_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_42d_base_v131_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_63d_base_v132_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_126d_base_v133_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_189d_base_v134_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_252d_base_v135_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_378d_base_v136_signal,
    f09bcq_f09_bank_credit_quality_earnvolacc_504d_base_v137_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_21d_base_v138_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_42d_base_v139_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_63d_base_v140_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_126d_base_v141_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_189d_base_v142_signal,
    f09bcq_f09_bank_credit_quality_creditqualxvol_252d_base_v143_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_21d_base_v144_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_42d_base_v145_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_63d_base_v146_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_126d_base_v147_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_189d_base_v148_signal,
    f09bcq_f09_bank_credit_quality_provproxxrev_252d_base_v149_signal,
    f09bcq_f09_bank_credit_quality_earnvolemapct_21d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_BANK_CREDIT_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f09_earnings_vol', '_f09_credit_quality_score', '_f09_provision_proxy')
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
    print(f"OK f09_bank_credit_quality_base_076_150_claude: {n_features} features pass")
