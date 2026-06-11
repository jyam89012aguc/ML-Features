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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f25_wc_ratio(inventory, receivables, payables, revenue):
    wc = inventory + receivables - payables
    return wc / revenue.replace(0, np.nan)


def _f25_operating_cycle(inventory, receivables, payables, cor):
    dio = inventory / cor.replace(0, np.nan) * 365.0
    dso = receivables / cor.replace(0, np.nan) * 365.0
    dpo = payables / cor.replace(0, np.nan) * 365.0
    return dio + dso - dpo


def _f25_wc_efficiency(workingcapital, revenue, w):
    ratio = workingcapital / revenue.replace(0, np.nan)
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ratio.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return -((ratio - m) / sd)

# ===== features =====

def f25wcc_f25_working_capital_consumer_opcycstd_315d_base_v076_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 315) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_378d_base_v077_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 378) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_504d_base_v078_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 504) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_5d_base_v079_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_10d_base_v080_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_21d_base_v081_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_42d_base_v082_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_63d_base_v083_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_84d_base_v084_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_126d_base_v085_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_168d_base_v086_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_189d_base_v087_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_252d_base_v088_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_315d_base_v089_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_378d_base_v090_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_504d_base_v091_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_5d_base_v092_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 5) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_10d_base_v093_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 10) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_21d_base_v094_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 21) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_42d_base_v095_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 42) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_63d_base_v096_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 63) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_84d_base_v097_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 84) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_126d_base_v098_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 126) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_168d_base_v099_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 168) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_189d_base_v100_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 189) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_252d_base_v101_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 252) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_315d_base_v102_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 315) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_378d_base_v103_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 378) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_504d_base_v104_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 504) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_5d_base_v105_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_10d_base_v106_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_21d_base_v107_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_42d_base_v108_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_63d_base_v109_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_84d_base_v110_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_126d_base_v111_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_168d_base_v112_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_189d_base_v113_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_252d_base_v114_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_315d_base_v115_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_378d_base_v116_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_504d_base_v117_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_5d_base_v118_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_10d_base_v119_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_21d_base_v120_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_42d_base_v121_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_63d_base_v122_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_84d_base_v123_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_126d_base_v124_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_168d_base_v125_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_189d_base_v126_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_252d_base_v127_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_315d_base_v128_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_378d_base_v129_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_504d_base_v130_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_5d_base_v131_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_10d_base_v132_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_21d_base_v133_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_42d_base_v134_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_63d_base_v135_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_84d_base_v136_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_126d_base_v137_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_168d_base_v138_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_189d_base_v139_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_252d_base_v140_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_315d_base_v141_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_378d_base_v142_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_504d_base_v143_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_5d_base_v144_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 5) * _mean(oc, 5) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_10d_base_v145_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 10) * _mean(oc, 10) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_21d_base_v146_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 21) * _mean(oc, 21) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_42d_base_v147_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 42) * _mean(oc, 42) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_63d_base_v148_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 63) * _mean(oc, 63) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_84d_base_v149_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 84) * _mean(oc, 84) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_126d_base_v150_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 126) * _mean(oc, 126) / 365.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25wcc_f25_working_capital_consumer_opcycstd_315d_base_v076_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_378d_base_v077_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_504d_base_v078_signal,
    f25wcc_f25_working_capital_consumer_opcycz_5d_base_v079_signal,
    f25wcc_f25_working_capital_consumer_opcycz_10d_base_v080_signal,
    f25wcc_f25_working_capital_consumer_opcycz_21d_base_v081_signal,
    f25wcc_f25_working_capital_consumer_opcycz_42d_base_v082_signal,
    f25wcc_f25_working_capital_consumer_opcycz_63d_base_v083_signal,
    f25wcc_f25_working_capital_consumer_opcycz_84d_base_v084_signal,
    f25wcc_f25_working_capital_consumer_opcycz_126d_base_v085_signal,
    f25wcc_f25_working_capital_consumer_opcycz_168d_base_v086_signal,
    f25wcc_f25_working_capital_consumer_opcycz_189d_base_v087_signal,
    f25wcc_f25_working_capital_consumer_opcycz_252d_base_v088_signal,
    f25wcc_f25_working_capital_consumer_opcycz_315d_base_v089_signal,
    f25wcc_f25_working_capital_consumer_opcycz_378d_base_v090_signal,
    f25wcc_f25_working_capital_consumer_opcycz_504d_base_v091_signal,
    f25wcc_f25_working_capital_consumer_opcycema_5d_base_v092_signal,
    f25wcc_f25_working_capital_consumer_opcycema_10d_base_v093_signal,
    f25wcc_f25_working_capital_consumer_opcycema_21d_base_v094_signal,
    f25wcc_f25_working_capital_consumer_opcycema_42d_base_v095_signal,
    f25wcc_f25_working_capital_consumer_opcycema_63d_base_v096_signal,
    f25wcc_f25_working_capital_consumer_opcycema_84d_base_v097_signal,
    f25wcc_f25_working_capital_consumer_opcycema_126d_base_v098_signal,
    f25wcc_f25_working_capital_consumer_opcycema_168d_base_v099_signal,
    f25wcc_f25_working_capital_consumer_opcycema_189d_base_v100_signal,
    f25wcc_f25_working_capital_consumer_opcycema_252d_base_v101_signal,
    f25wcc_f25_working_capital_consumer_opcycema_315d_base_v102_signal,
    f25wcc_f25_working_capital_consumer_opcycema_378d_base_v103_signal,
    f25wcc_f25_working_capital_consumer_opcycema_504d_base_v104_signal,
    f25wcc_f25_working_capital_consumer_wceff_5d_base_v105_signal,
    f25wcc_f25_working_capital_consumer_wceff_10d_base_v106_signal,
    f25wcc_f25_working_capital_consumer_wceff_21d_base_v107_signal,
    f25wcc_f25_working_capital_consumer_wceff_42d_base_v108_signal,
    f25wcc_f25_working_capital_consumer_wceff_63d_base_v109_signal,
    f25wcc_f25_working_capital_consumer_wceff_84d_base_v110_signal,
    f25wcc_f25_working_capital_consumer_wceff_126d_base_v111_signal,
    f25wcc_f25_working_capital_consumer_wceff_168d_base_v112_signal,
    f25wcc_f25_working_capital_consumer_wceff_189d_base_v113_signal,
    f25wcc_f25_working_capital_consumer_wceff_252d_base_v114_signal,
    f25wcc_f25_working_capital_consumer_wceff_315d_base_v115_signal,
    f25wcc_f25_working_capital_consumer_wceff_378d_base_v116_signal,
    f25wcc_f25_working_capital_consumer_wceff_504d_base_v117_signal,
    f25wcc_f25_working_capital_consumer_wceffema_5d_base_v118_signal,
    f25wcc_f25_working_capital_consumer_wceffema_10d_base_v119_signal,
    f25wcc_f25_working_capital_consumer_wceffema_21d_base_v120_signal,
    f25wcc_f25_working_capital_consumer_wceffema_42d_base_v121_signal,
    f25wcc_f25_working_capital_consumer_wceffema_63d_base_v122_signal,
    f25wcc_f25_working_capital_consumer_wceffema_84d_base_v123_signal,
    f25wcc_f25_working_capital_consumer_wceffema_126d_base_v124_signal,
    f25wcc_f25_working_capital_consumer_wceffema_168d_base_v125_signal,
    f25wcc_f25_working_capital_consumer_wceffema_189d_base_v126_signal,
    f25wcc_f25_working_capital_consumer_wceffema_252d_base_v127_signal,
    f25wcc_f25_working_capital_consumer_wceffema_315d_base_v128_signal,
    f25wcc_f25_working_capital_consumer_wceffema_378d_base_v129_signal,
    f25wcc_f25_working_capital_consumer_wceffema_504d_base_v130_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_5d_base_v131_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_10d_base_v132_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_21d_base_v133_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_42d_base_v134_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_63d_base_v135_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_84d_base_v136_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_126d_base_v137_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_168d_base_v138_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_189d_base_v139_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_252d_base_v140_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_315d_base_v141_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_378d_base_v142_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_504d_base_v143_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_5d_base_v144_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_10d_base_v145_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_21d_base_v146_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_42d_base_v147_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_63d_base_v148_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_84d_base_v149_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_WORKING_CAPITAL_CONSUMER_REGISTRY_076_150 = REGISTRY


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
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "inventory": inventory,
        "receivables": receivables,
        "payables": payables,
        "cor": cor,
        "closeadj": closeadj,
        "workingcapital": workingcapital,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_wc_ratio", "_f25_operating_cycle", "_f25_wc_efficiency",)
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
    print(f"OK f25_working_capital_consumer_base_076_150_claude: {n_features} features pass")
