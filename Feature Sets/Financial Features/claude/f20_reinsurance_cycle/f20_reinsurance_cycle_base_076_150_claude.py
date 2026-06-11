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
def _f20_reinsurance_pulse(revenue, w):
    return revenue.pct_change(periods=w)


def _f20_cycle_position(revenue, netmargin, w):
    rev_g = revenue.pct_change(periods=w)
    nm_sm = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rev_g * nm_sm


def _f20_pricing_cycle(revenue, netmargin, w):
    rev_z_m = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    rev_z_s = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).std()
    rev_z = (revenue.pct_change(periods=w) - rev_z_m) / rev_z_s.replace(0, np.nan)
    return rev_z * netmargin

def f20rcy_f20_reinsurance_cycle_cycposema_5d_base_v076_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    result = _ema(cp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_8d_base_v077_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    result = _ema(cp, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_10d_base_v078_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    result = _ema(cp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_15d_base_v079_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    result = _ema(cp, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_21d_base_v080_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    result = _ema(cp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_30d_base_v081_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    result = _ema(cp, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_42d_base_v082_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    result = _ema(cp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_63d_base_v083_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    result = _ema(cp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_90d_base_v084_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    result = _ema(cp, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_126d_base_v085_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    result = _ema(cp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_150d_base_v086_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    result = _ema(cp, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_189d_base_v087_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    result = _ema(cp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_252d_base_v088_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    result = _ema(cp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_378d_base_v089_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    result = _ema(cp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_504d_base_v090_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    result = _ema(cp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_5d_base_v091_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    result = _z(cp, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_8d_base_v092_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    result = _z(cp, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_10d_base_v093_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    result = _z(cp, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_15d_base_v094_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    result = _z(cp, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_21d_base_v095_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    result = _z(cp, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_30d_base_v096_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    result = _z(cp, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_42d_base_v097_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    result = _z(cp, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_63d_base_v098_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    result = _z(cp, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_90d_base_v099_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    result = _z(cp, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_126d_base_v100_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    result = _z(cp, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_150d_base_v101_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    result = _z(cp, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_189d_base_v102_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    result = _z(cp, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_252d_base_v103_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    result = _z(cp, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_378d_base_v104_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    result = _z(cp, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_504d_base_v105_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    result = _z(cp, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_5d_base_v106_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 5)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_8d_base_v107_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 8)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_10d_base_v108_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 10)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_15d_base_v109_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 15)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_21d_base_v110_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 21)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_30d_base_v111_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 30)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_42d_base_v112_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 42)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_63d_base_v113_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 63)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_90d_base_v114_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 90)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_126d_base_v115_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 126)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_150d_base_v116_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 150)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_189d_base_v117_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 189)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_252d_base_v118_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 252)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_378d_base_v119_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 378)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_504d_base_v120_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 504)
    result = pc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_5d_base_v121_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 5)
    result = _ema(pc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_8d_base_v122_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 8)
    result = _ema(pc, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_10d_base_v123_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 10)
    result = _ema(pc, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_15d_base_v124_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 15)
    result = _ema(pc, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_21d_base_v125_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 21)
    result = _ema(pc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_30d_base_v126_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 30)
    result = _ema(pc, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_42d_base_v127_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 42)
    result = _ema(pc, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_63d_base_v128_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 63)
    result = _ema(pc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_90d_base_v129_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 90)
    result = _ema(pc, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_126d_base_v130_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 126)
    result = _ema(pc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_150d_base_v131_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 150)
    result = _ema(pc, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_189d_base_v132_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 189)
    result = _ema(pc, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_252d_base_v133_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 252)
    result = _ema(pc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_378d_base_v134_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 378)
    result = _ema(pc, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_504d_base_v135_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 504)
    result = _ema(pc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_5d_base_v136_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    result = (p - p.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_8d_base_v137_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    result = (p - p.shift(8)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_10d_base_v138_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    result = (p - p.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_15d_base_v139_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    result = (p - p.shift(15)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_21d_base_v140_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    result = (p - p.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_30d_base_v141_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    result = (p - p.shift(30)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_42d_base_v142_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    result = (p - p.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_63d_base_v143_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    result = (p - p.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_90d_base_v144_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    result = (p - p.shift(90)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_126d_base_v145_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    result = (p - p.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_150d_base_v146_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    result = (p - p.shift(150)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_189d_base_v147_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    result = (p - p.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_252d_base_v148_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    result = (p - p.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_378d_base_v149_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    result = (p - p.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_504d_base_v150_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    result = (p - p.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rcy_f20_reinsurance_cycle_cycposema_5d_base_v076_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_8d_base_v077_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_10d_base_v078_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_15d_base_v079_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_21d_base_v080_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_30d_base_v081_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_42d_base_v082_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_63d_base_v083_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_90d_base_v084_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_126d_base_v085_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_150d_base_v086_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_189d_base_v087_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_252d_base_v088_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_378d_base_v089_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_504d_base_v090_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_5d_base_v091_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_8d_base_v092_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_10d_base_v093_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_15d_base_v094_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_21d_base_v095_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_30d_base_v096_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_42d_base_v097_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_63d_base_v098_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_90d_base_v099_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_126d_base_v100_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_150d_base_v101_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_189d_base_v102_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_252d_base_v103_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_378d_base_v104_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_504d_base_v105_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_5d_base_v106_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_8d_base_v107_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_10d_base_v108_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_15d_base_v109_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_21d_base_v110_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_30d_base_v111_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_42d_base_v112_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_63d_base_v113_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_90d_base_v114_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_126d_base_v115_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_150d_base_v116_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_189d_base_v117_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_252d_base_v118_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_378d_base_v119_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_504d_base_v120_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_5d_base_v121_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_8d_base_v122_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_10d_base_v123_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_15d_base_v124_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_21d_base_v125_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_30d_base_v126_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_42d_base_v127_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_63d_base_v128_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_90d_base_v129_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_126d_base_v130_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_150d_base_v131_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_189d_base_v132_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_252d_base_v133_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_378d_base_v134_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_504d_base_v135_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_5d_base_v136_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_8d_base_v137_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_10d_base_v138_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_15d_base_v139_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_21d_base_v140_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_30d_base_v141_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_42d_base_v142_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_63d_base_v143_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_90d_base_v144_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_126d_base_v145_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_150d_base_v146_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_189d_base_v147_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_252d_base_v148_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_378d_base_v149_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REINSURANCE_CYCLE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f20_reinsurance_pulse", "_f20_cycle_position", "_f20_pricing_cycle",)
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
    print(f"OK f20_reinsurance_cycle_076_150_claude: {n_features} features pass")
