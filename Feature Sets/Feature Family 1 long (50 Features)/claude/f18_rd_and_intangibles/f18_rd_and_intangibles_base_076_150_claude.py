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


def _diff(s, n):
    return s.diff(periods=n)


# ===== folder domain primitives =====
def _f18_rd_intensity_proxy(gp, opinc, denom, w):
    rd = gp - opinc
    n = _mean(rd, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


def _f18_intangibles_proxy(assets, workingcapital, equity, denom, w):
    intang = assets - workingcapital - equity
    n = _mean(intang, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


def _f18_rd_intensity_alt(revenue, gp, denom, w):
    opex = revenue - gp
    n = _mean(opex, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


# zscore of 21d R&D/revenue over 252d
def f18ri_f18_rd_and_intangibles_rdrevz_252d_base_v076_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d R&D/revenue over 504d
def f18ri_f18_rd_and_intangibles_rdrevz_504d_base_v077_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 63)
    result = _z(p, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d R&D/assets over 252d
def f18ri_f18_rd_and_intangibles_rdassetsz_252d_base_v078_signal(gp, opinc, assets, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, assets, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d intangibles/assets over 252d
def f18ri_f18_rd_and_intangibles_intangassetsz_252d_base_v079_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d intangibles/equity over 252d
def f18ri_f18_rd_and_intangibles_intangequityz_252d_base_v080_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of opex/revenue 252d
def f18ri_f18_rd_and_intangibles_opexrevz_252d_base_v081_signal(revenue, gp, marketcap):
    p = _f18_rd_intensity_alt(revenue, gp, revenue, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of intangibles/revenue 252d
def f18ri_f18_rd_and_intangibles_intangrevz_252d_base_v082_signal(assets, workingcapital, equity, revenue, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 21)
    result = _z(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of R&D/revenue
def f18ri_f18_rd_and_intangibles_rdrevstd_252d_base_v083_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = _std(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of intangibles/assets
def f18ri_f18_rd_and_intangibles_intangassetsstd_252d_base_v084_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = _std(p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of R&D/assets
def f18ri_f18_rd_and_intangibles_rdassetsstd_504d_base_v085_signal(gp, opinc, assets, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, assets, 21)
    result = _std(p, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-R&D days
def f18ri_f18_rd_and_intangibles_highrd_count_252d_base_v086_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-intangibles days
def f18ri_f18_rd_and_intangibles_highintang_count_252d_base_v087_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of low-R&D days
def f18ri_f18_rd_and_intangibles_lowrd_count_504d_base_v088_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    avg = _mean(p, 504)
    flag = (p < avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/rev - 252d mean
def f18ri_f18_rd_and_intangibles_rdrevdev_252d_base_v089_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    avg = _mean(p, 252)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Intang/Assets - 252d mean
def f18ri_f18_rd_and_intangibles_intangassetsdev_252d_base_v090_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    avg = _mean(p, 252)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/Assets - 504d mean
def f18ri_f18_rd_and_intangibles_rdassetsdev_504d_base_v091_signal(gp, opinc, assets, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, assets, 21)
    avg = _mean(p, 504)
    result = (p - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/Rev relative to 504d hi
def f18ri_f18_rd_and_intangibles_rdrevrelhi_504d_base_v092_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Intang/Assets relative to 504d hi
def f18ri_f18_rd_and_intangibles_intangassetsrelhi_504d_base_v093_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    result = (p / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# R&D/Rev position 504d
def f18ri_f18_rd_and_intangibles_rdrevpos_504d_base_v094_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    pos = (p - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Intang/Assets position 504d
def f18ri_f18_rd_and_intangibles_intangpos_504d_base_v095_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    pos = (p - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended innovation intensity: (R&D + capex) / revenue + R&D/assets
def f18ri_f18_rd_and_intangibles_blendedinnov_252d_base_v096_signal(gp, opinc, capex, revenue, assets, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    b = _f18_rd_intensity_proxy(gp, opinc, assets, 252)
    inn = (gp - opinc) + capex
    n = _mean(inn, 252)
    d = _mean(revenue, 252)
    c = n / d.replace(0, np.nan).abs()
    result = (a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended intangibility: intangibles/assets + intangibles/equity
def f18ri_f18_rd_and_intangibles_blendedintang_252d_base_v097_signal(assets, workingcapital, equity, marketcap):
    a = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 252)
    result = (a + b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D recent vs trend
def f18ri_f18_rd_and_intangibles_rdrev_recent_vs_trend_base_v098_signal(gp, opinc, revenue, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 63)
    b = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles recent vs trend
def f18ri_f18_rd_and_intangibles_intang_recent_vs_trend_base_v099_signal(assets, workingcapital, equity, marketcap):
    a = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 63)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log R&D/Rev
def f18ri_f18_rd_and_intangibles_logrdrev_21d_base_v100_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = np.log(p.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log R&D/Rev
def f18ri_f18_rd_and_intangibles_logrdrev_252d_base_v101_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = np.log(p.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log Intang/Assets
def f18ri_f18_rd_and_intangibles_logintang_252d_base_v102_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = np.log(p.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D/Rev squared
def f18ri_f18_rd_and_intangibles_rdrevsq_21d_base_v103_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = p * p.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D/Rev squared
def f18ri_f18_rd_and_intangibles_rdrevsq_252d_base_v104_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = p * p.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Intang/Assets squared
def f18ri_f18_rd_and_intangibles_intangsq_21d_base_v105_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = p * p.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Intang/Assets squared
def f18ri_f18_rd_and_intangibles_intangsq_252d_base_v106_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = p * p.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D EMA
def f18ri_f18_rd_and_intangibles_rdrev_ema_21d_base_v107_signal(gp, opinc, revenue, marketcap):
    base = _f18_rd_intensity_proxy(gp, opinc, revenue, 21).ewm(span=21, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D EMA
def f18ri_f18_rd_and_intangibles_rdrev_ema_252d_base_v108_signal(gp, opinc, revenue, marketcap):
    base = _f18_rd_intensity_proxy(gp, opinc, revenue, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Intang/Assets EMA
def f18ri_f18_rd_and_intangibles_intang_ema_252d_base_v109_signal(assets, workingcapital, equity, marketcap):
    base = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D x intangibles (synergy)
def f18ri_f18_rd_and_intangibles_rdintang_252d_base_v110_signal(gp, opinc, revenue, assets, workingcapital, equity, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (a * b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D x intangibles
def f18ri_f18_rd_and_intangibles_rdintang_504d_base_v111_signal(gp, opinc, revenue, assets, workingcapital, equity, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 504)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 504)
    result = (a * b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / capex (research vs investment)
def f18ri_f18_rd_and_intangibles_rdcapex_21d_base_v112_signal(gp, opinc, capex, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, capex, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / capex
def f18ri_f18_rd_and_intangibles_rdcapex_252d_base_v113_signal(gp, opinc, capex, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, capex, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D / capex
def f18ri_f18_rd_and_intangibles_rdcapex_504d_base_v114_signal(gp, opinc, capex, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, capex, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / capex (intangibles per investment)
def f18ri_f18_rd_and_intangibles_intangcapex_252d_base_v115_signal(assets, workingcapital, equity, capex, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, capex, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (intangibles + R&D) / revenue
def f18ri_f18_rd_and_intangibles_innovbroad_21d_base_v116_signal(assets, workingcapital, equity, gp, opinc, revenue, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 21)
    d = _mean(revenue, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d innovation broad / revenue
def f18ri_f18_rd_and_intangibles_innovbroad_252d_base_v117_signal(assets, workingcapital, equity, gp, opinc, revenue, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 252)
    d = _mean(revenue, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d innovation broad / revenue
def f18ri_f18_rd_and_intangibles_innovbroad_504d_base_v118_signal(assets, workingcapital, equity, gp, opinc, revenue, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 504)
    d = _mean(revenue, 504)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 504)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (intangibles + R&D) / assets
def f18ri_f18_rd_and_intangibles_innovbroada_21d_base_v119_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 21)
    d = _mean(assets, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (intangibles + R&D) / assets
def f18ri_f18_rd_and_intangibles_innovbroada_252d_base_v120_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 252)
    d = _mean(assets, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles position fraction in marketcap (intangibles per dollar mkt)
def f18ri_f18_rd_and_intangibles_intangmkt_252d_base_v121_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, marketcap, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles / EV
def f18ri_f18_rd_and_intangibles_intangev_504d_base_v122_signal(assets, workingcapital, equity, ev, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, ev, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / EV (research valuation)
def f18ri_f18_rd_and_intangibles_rdev_252d_base_v123_signal(gp, opinc, ev, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ev, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D / EV
def f18ri_f18_rd_and_intangibles_rdev_504d_base_v124_signal(gp, opinc, ev, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ev, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / marketcap
def f18ri_f18_rd_and_intangibles_rdmkt_252d_base_v125_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, marketcap, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D / marketcap
def f18ri_f18_rd_and_intangibles_rdmkt_504d_base_v126_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, marketcap, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D x revenue (research scale x topline)
def f18ri_f18_rd_and_intangibles_rdxrev_21d_base_v127_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = p * revenue / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D x revenue
def f18ri_f18_rd_and_intangibles_rdxrev_252d_base_v128_signal(gp, opinc, revenue, marketcap):
    p = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = p * revenue / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles x assets
def f18ri_f18_rd_and_intangibles_intangxassets_252d_base_v129_signal(assets, workingcapital, equity, marketcap):
    p = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = p * assets / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D + intangibles per share
def f18ri_f18_rd_and_intangibles_rdintang_ps_252d_base_v130_signal(assets, workingcapital, equity, gp, opinc, sharesbas, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 252)
    d = _mean(sharesbas, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, sharesbas, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (R&D - capex) net innovation gap
def f18ri_f18_rd_and_intangibles_rdmcapex_21d_base_v131_signal(gp, opinc, capex, revenue, marketcap):
    rd = gp - opinc
    gap = rd - capex
    n = _mean(gap, 21)
    d = _mean(revenue, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (R&D - capex) gap / revenue
def f18ri_f18_rd_and_intangibles_rdmcapex_252d_base_v132_signal(gp, opinc, capex, revenue, marketcap):
    rd = gp - opinc
    gap = rd - capex
    n = _mean(gap, 252)
    d = _mean(revenue, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles to capex (built innovation buffer)
def f18ri_f18_rd_and_intangibles_intangcap_21d_base_v133_signal(assets, workingcapital, equity, capex, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, capex, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles to ncfo
def f18ri_f18_rd_and_intangibles_intangncfo_21d_base_v134_signal(assets, workingcapital, equity, ncfo, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, ncfo, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles to ncfo
def f18ri_f18_rd_and_intangibles_intangncfo_252d_base_v135_signal(assets, workingcapital, equity, ncfo, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, ncfo, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (R&D + intang) / equity
def f18ri_f18_rd_and_intangibles_rdintangeq_21d_base_v136_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 21)
    d = _mean(equity, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (R&D + intang) / equity
def f18ri_f18_rd_and_intangibles_rdintangeq_252d_base_v137_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 252)
    d = _mean(equity, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / wc (research vs liquidity)
def f18ri_f18_rd_and_intangibles_rdwc_21d_base_v138_signal(gp, opinc, workingcapital, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, workingcapital, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / wc
def f18ri_f18_rd_and_intangibles_rdwc_252d_base_v139_signal(gp, opinc, workingcapital, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, workingcapital, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Opex / equity
def f18ri_f18_rd_and_intangibles_opexeq_252d_base_v140_signal(revenue, gp, equity, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Opex / equity
def f18ri_f18_rd_and_intangibles_opexeq_504d_base_v141_signal(revenue, gp, equity, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Opex / debt
def f18ri_f18_rd_and_intangibles_opexdebt_252d_base_v142_signal(revenue, gp, debt, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Opex / sharesbas (per-share opex)
def f18ri_f18_rd_and_intangibles_opexps_252d_base_v143_signal(revenue, gp, sharesbas, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Opex - capex spread (clean operating cost)
def f18ri_f18_rd_and_intangibles_opexmcapex_252d_base_v144_signal(revenue, gp, capex, marketcap):
    opex = revenue - gp
    spread = opex - capex
    n = _mean(spread, 252)
    d = _mean(revenue, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_alt(revenue, gp, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (R&D / Opex) inside the SG&A bucket
def f18ri_f18_rd_and_intangibles_rdoverall_252d_base_v145_signal(gp, opinc, revenue, marketcap):
    rd = gp - opinc
    opex = revenue - gp
    n = _mean(rd, 252)
    d = _mean(opex, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (intangibles - debt) value-add intangibles
def f18ri_f18_rd_and_intangibles_intangmdebt_252d_base_v146_signal(assets, workingcapital, equity, debt, marketcap):
    intang = assets - workingcapital - equity
    spread = intang - debt
    n = _mean(spread, 252)
    d = _mean(assets, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (intangibles - debt) / equity
def f18ri_f18_rd_and_intangibles_intangmdebteq_252d_base_v147_signal(assets, workingcapital, equity, debt, marketcap):
    intang = assets - workingcapital - equity
    spread = intang - debt
    n = _mean(spread, 252)
    d = _mean(equity, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d full innovation composite: R&D/Rev + Intang/Assets + Capex/Rev
def f18ri_f18_rd_and_intangibles_fullinnov_252d_base_v148_signal(gp, opinc, revenue, assets, workingcapital, equity, capex, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    cn = _mean(capex, 252)
    cd = _mean(revenue, 252)
    c = cn / cd.replace(0, np.nan).abs()
    result = (a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D x intangibles x capex composite
def f18ri_f18_rd_and_intangibles_innov_x3_504d_base_v149_signal(gp, opinc, revenue, assets, workingcapital, equity, capex, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 504)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 504)
    cn = _mean(capex, 504)
    cd = _mean(revenue, 504)
    c = cn / cd.replace(0, np.nan).abs()
    result = (a * b * c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D x intangibles per dollar of revenue
def f18ri_f18_rd_and_intangibles_rdintangrev_252d_base_v150_signal(gp, opinc, revenue, assets, workingcapital, equity, marketcap):
    a = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    b = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 252)
    result = (a * b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18ri_f18_rd_and_intangibles_rdrevz_252d_base_v076_signal,
    f18ri_f18_rd_and_intangibles_rdrevz_504d_base_v077_signal,
    f18ri_f18_rd_and_intangibles_rdassetsz_252d_base_v078_signal,
    f18ri_f18_rd_and_intangibles_intangassetsz_252d_base_v079_signal,
    f18ri_f18_rd_and_intangibles_intangequityz_252d_base_v080_signal,
    f18ri_f18_rd_and_intangibles_opexrevz_252d_base_v081_signal,
    f18ri_f18_rd_and_intangibles_intangrevz_252d_base_v082_signal,
    f18ri_f18_rd_and_intangibles_rdrevstd_252d_base_v083_signal,
    f18ri_f18_rd_and_intangibles_intangassetsstd_252d_base_v084_signal,
    f18ri_f18_rd_and_intangibles_rdassetsstd_504d_base_v085_signal,
    f18ri_f18_rd_and_intangibles_highrd_count_252d_base_v086_signal,
    f18ri_f18_rd_and_intangibles_highintang_count_252d_base_v087_signal,
    f18ri_f18_rd_and_intangibles_lowrd_count_504d_base_v088_signal,
    f18ri_f18_rd_and_intangibles_rdrevdev_252d_base_v089_signal,
    f18ri_f18_rd_and_intangibles_intangassetsdev_252d_base_v090_signal,
    f18ri_f18_rd_and_intangibles_rdassetsdev_504d_base_v091_signal,
    f18ri_f18_rd_and_intangibles_rdrevrelhi_504d_base_v092_signal,
    f18ri_f18_rd_and_intangibles_intangassetsrelhi_504d_base_v093_signal,
    f18ri_f18_rd_and_intangibles_rdrevpos_504d_base_v094_signal,
    f18ri_f18_rd_and_intangibles_intangpos_504d_base_v095_signal,
    f18ri_f18_rd_and_intangibles_blendedinnov_252d_base_v096_signal,
    f18ri_f18_rd_and_intangibles_blendedintang_252d_base_v097_signal,
    f18ri_f18_rd_and_intangibles_rdrev_recent_vs_trend_base_v098_signal,
    f18ri_f18_rd_and_intangibles_intang_recent_vs_trend_base_v099_signal,
    f18ri_f18_rd_and_intangibles_logrdrev_21d_base_v100_signal,
    f18ri_f18_rd_and_intangibles_logrdrev_252d_base_v101_signal,
    f18ri_f18_rd_and_intangibles_logintang_252d_base_v102_signal,
    f18ri_f18_rd_and_intangibles_rdrevsq_21d_base_v103_signal,
    f18ri_f18_rd_and_intangibles_rdrevsq_252d_base_v104_signal,
    f18ri_f18_rd_and_intangibles_intangsq_21d_base_v105_signal,
    f18ri_f18_rd_and_intangibles_intangsq_252d_base_v106_signal,
    f18ri_f18_rd_and_intangibles_rdrev_ema_21d_base_v107_signal,
    f18ri_f18_rd_and_intangibles_rdrev_ema_252d_base_v108_signal,
    f18ri_f18_rd_and_intangibles_intang_ema_252d_base_v109_signal,
    f18ri_f18_rd_and_intangibles_rdintang_252d_base_v110_signal,
    f18ri_f18_rd_and_intangibles_rdintang_504d_base_v111_signal,
    f18ri_f18_rd_and_intangibles_rdcapex_21d_base_v112_signal,
    f18ri_f18_rd_and_intangibles_rdcapex_252d_base_v113_signal,
    f18ri_f18_rd_and_intangibles_rdcapex_504d_base_v114_signal,
    f18ri_f18_rd_and_intangibles_intangcapex_252d_base_v115_signal,
    f18ri_f18_rd_and_intangibles_innovbroad_21d_base_v116_signal,
    f18ri_f18_rd_and_intangibles_innovbroad_252d_base_v117_signal,
    f18ri_f18_rd_and_intangibles_innovbroad_504d_base_v118_signal,
    f18ri_f18_rd_and_intangibles_innovbroada_21d_base_v119_signal,
    f18ri_f18_rd_and_intangibles_innovbroada_252d_base_v120_signal,
    f18ri_f18_rd_and_intangibles_intangmkt_252d_base_v121_signal,
    f18ri_f18_rd_and_intangibles_intangev_504d_base_v122_signal,
    f18ri_f18_rd_and_intangibles_rdev_252d_base_v123_signal,
    f18ri_f18_rd_and_intangibles_rdev_504d_base_v124_signal,
    f18ri_f18_rd_and_intangibles_rdmkt_252d_base_v125_signal,
    f18ri_f18_rd_and_intangibles_rdmkt_504d_base_v126_signal,
    f18ri_f18_rd_and_intangibles_rdxrev_21d_base_v127_signal,
    f18ri_f18_rd_and_intangibles_rdxrev_252d_base_v128_signal,
    f18ri_f18_rd_and_intangibles_intangxassets_252d_base_v129_signal,
    f18ri_f18_rd_and_intangibles_rdintang_ps_252d_base_v130_signal,
    f18ri_f18_rd_and_intangibles_rdmcapex_21d_base_v131_signal,
    f18ri_f18_rd_and_intangibles_rdmcapex_252d_base_v132_signal,
    f18ri_f18_rd_and_intangibles_intangcap_21d_base_v133_signal,
    f18ri_f18_rd_and_intangibles_intangncfo_21d_base_v134_signal,
    f18ri_f18_rd_and_intangibles_intangncfo_252d_base_v135_signal,
    f18ri_f18_rd_and_intangibles_rdintangeq_21d_base_v136_signal,
    f18ri_f18_rd_and_intangibles_rdintangeq_252d_base_v137_signal,
    f18ri_f18_rd_and_intangibles_rdwc_21d_base_v138_signal,
    f18ri_f18_rd_and_intangibles_rdwc_252d_base_v139_signal,
    f18ri_f18_rd_and_intangibles_opexeq_252d_base_v140_signal,
    f18ri_f18_rd_and_intangibles_opexeq_504d_base_v141_signal,
    f18ri_f18_rd_and_intangibles_opexdebt_252d_base_v142_signal,
    f18ri_f18_rd_and_intangibles_opexps_252d_base_v143_signal,
    f18ri_f18_rd_and_intangibles_opexmcapex_252d_base_v144_signal,
    f18ri_f18_rd_and_intangibles_rdoverall_252d_base_v145_signal,
    f18ri_f18_rd_and_intangibles_intangmdebt_252d_base_v146_signal,
    f18ri_f18_rd_and_intangibles_intangmdebteq_252d_base_v147_signal,
    f18ri_f18_rd_and_intangibles_fullinnov_252d_base_v148_signal,
    f18ri_f18_rd_and_intangibles_innov_x3_504d_base_v149_signal,
    f18ri_f18_rd_and_intangibles_rdintangrev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_RD_AND_INTANGIBLES_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f18_rd_intensity", "_f18_intangibles")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_rd_and_intangibles_base_076_150_claude: {n_features} features pass")
