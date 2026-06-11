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
def _f22_revenue_drawdown(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - peak) / peak.replace(0, np.nan).abs()


def _f22_revenue_recovery(revenue, w):
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan)
    return (revenue - trough) / trough.abs()


def _f22_resilience_score(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan)
    band = (peak - trough).replace(0, np.nan)
    return (revenue - trough) / band

# ===== features =====

def f22ddr_f22_discretionary_demand_resilience_res_315d_base_v076_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_378d_base_v077_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_504d_base_v078_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_5d_base_v079_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_10d_base_v080_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_21d_base_v081_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_42d_base_v082_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_63d_base_v083_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_84d_base_v084_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_126d_base_v085_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_168d_base_v086_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_189d_base_v087_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_252d_base_v088_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_315d_base_v089_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_378d_base_v090_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_504d_base_v091_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_5d_base_v092_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    eg = ebitda.pct_change(periods=5)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_10d_base_v093_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    eg = ebitda.pct_change(periods=10)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_21d_base_v094_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    eg = ebitda.pct_change(periods=21)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_42d_base_v095_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    eg = ebitda.pct_change(periods=42)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_63d_base_v096_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    eg = ebitda.pct_change(periods=63)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_84d_base_v097_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    eg = ebitda.pct_change(periods=84)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_126d_base_v098_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    eg = ebitda.pct_change(periods=126)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_168d_base_v099_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    eg = ebitda.pct_change(periods=168)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_189d_base_v100_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    eg = ebitda.pct_change(periods=189)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_252d_base_v101_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    eg = ebitda.pct_change(periods=252)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_315d_base_v102_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    eg = ebitda.pct_change(periods=315)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_378d_base_v103_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    eg = ebitda.pct_change(periods=378)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_504d_base_v104_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    eg = ebitda.pct_change(periods=504)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_5d_base_v105_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_10d_base_v106_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_21d_base_v107_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_42d_base_v108_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_63d_base_v109_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_84d_base_v110_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_126d_base_v111_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_168d_base_v112_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_189d_base_v113_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_252d_base_v114_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_315d_base_v115_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_378d_base_v116_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_504d_base_v117_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_5d_base_v118_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_10d_base_v119_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_21d_base_v120_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_42d_base_v121_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_63d_base_v122_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_84d_base_v123_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_126d_base_v124_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_168d_base_v125_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_189d_base_v126_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_252d_base_v127_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_315d_base_v128_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_378d_base_v129_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_504d_base_v130_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = base * (ebitda / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_5d_base_v131_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_10d_base_v132_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_21d_base_v133_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_42d_base_v134_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_63d_base_v135_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_84d_base_v136_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = _z(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_126d_base_v137_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_168d_base_v138_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = _z(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_189d_base_v139_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_252d_base_v140_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_315d_base_v141_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = _z(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_378d_base_v142_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_504d_base_v143_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_5d_base_v144_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    dd = _f22_revenue_drawdown(revenue, 5)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_10d_base_v145_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    dd = _f22_revenue_drawdown(revenue, 10)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_21d_base_v146_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    dd = _f22_revenue_drawdown(revenue, 21)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_42d_base_v147_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    dd = _f22_revenue_drawdown(revenue, 42)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_63d_base_v148_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    dd = _f22_revenue_drawdown(revenue, 63)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_84d_base_v149_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    dd = _f22_revenue_drawdown(revenue, 84)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_126d_base_v150_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    dd = _f22_revenue_drawdown(revenue, 126)
    result = (base - dd.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ddr_f22_discretionary_demand_resilience_res_315d_base_v076_signal,
    f22ddr_f22_discretionary_demand_resilience_res_378d_base_v077_signal,
    f22ddr_f22_discretionary_demand_resilience_res_504d_base_v078_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_5d_base_v079_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_10d_base_v080_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_21d_base_v081_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_42d_base_v082_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_63d_base_v083_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_84d_base_v084_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_126d_base_v085_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_168d_base_v086_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_189d_base_v087_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_252d_base_v088_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_315d_base_v089_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_378d_base_v090_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_504d_base_v091_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_5d_base_v092_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_10d_base_v093_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_21d_base_v094_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_42d_base_v095_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_63d_base_v096_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_84d_base_v097_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_126d_base_v098_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_168d_base_v099_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_189d_base_v100_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_252d_base_v101_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_315d_base_v102_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_378d_base_v103_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_504d_base_v104_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_5d_base_v105_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_10d_base_v106_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_21d_base_v107_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_42d_base_v108_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_63d_base_v109_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_84d_base_v110_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_126d_base_v111_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_168d_base_v112_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_189d_base_v113_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_252d_base_v114_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_315d_base_v115_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_378d_base_v116_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_504d_base_v117_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_5d_base_v118_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_10d_base_v119_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_21d_base_v120_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_42d_base_v121_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_63d_base_v122_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_84d_base_v123_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_126d_base_v124_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_168d_base_v125_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_189d_base_v126_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_252d_base_v127_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_315d_base_v128_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_378d_base_v129_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_504d_base_v130_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_5d_base_v131_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_10d_base_v132_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_21d_base_v133_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_42d_base_v134_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_63d_base_v135_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_84d_base_v136_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_126d_base_v137_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_168d_base_v138_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_189d_base_v139_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_252d_base_v140_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_315d_base_v141_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_378d_base_v142_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_504d_base_v143_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_5d_base_v144_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_10d_base_v145_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_21d_base_v146_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_42d_base_v147_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_63d_base_v148_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_84d_base_v149_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DISCRETIONARY_DEMAND_RESILIENCE_REGISTRY_076_150 = REGISTRY


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
        "revenue": revenue,
        "closeadj": closeadj,
        "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_revenue_drawdown", "_f22_revenue_recovery", "_f22_resilience_score",)
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
    print(f"OK f22_discretionary_demand_resilience_base_076_150_claude: {n_features} features pass")
