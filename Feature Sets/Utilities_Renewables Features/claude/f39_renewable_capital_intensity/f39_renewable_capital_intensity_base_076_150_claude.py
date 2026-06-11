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


# ===== folder domain primitives =====
def _f39_capex_to_equity(capex, equity):
    return capex / equity.replace(0, np.nan).abs()


def _f39_capital_intensity(capex, equity, w):
    ratio = capex / equity.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_capital_burden(capex, fcf, equity, w):
    burden = (capex - fcf) / equity.replace(0, np.nan).abs()
    return burden.rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====

# p0_qrank window=126
def f39rci_f39_renewable_capital_intensity_p0_qrank_126d_base_v076_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=189
def f39rci_f39_renewable_capital_intensity_p0_qrank_189d_base_v077_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(189, min_periods=max(1, 189//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=252
def f39rci_f39_renewable_capital_intensity_p0_qrank_252d_base_v078_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=378
def f39rci_f39_renewable_capital_intensity_p0_qrank_378d_base_v079_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(378, min_periods=max(1, 378//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=504
def f39rci_f39_renewable_capital_intensity_p0_qrank_504d_base_v080_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=5
def f39rci_f39_renewable_capital_intensity_p0_diffw_5d_base_v081_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=10
def f39rci_f39_renewable_capital_intensity_p0_diffw_10d_base_v082_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=21
def f39rci_f39_renewable_capital_intensity_p0_diffw_21d_base_v083_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=42
def f39rci_f39_renewable_capital_intensity_p0_diffw_42d_base_v084_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=63
def f39rci_f39_renewable_capital_intensity_p0_diffw_63d_base_v085_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=126
def f39rci_f39_renewable_capital_intensity_p0_diffw_126d_base_v086_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=189
def f39rci_f39_renewable_capital_intensity_p0_diffw_189d_base_v087_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=252
def f39rci_f39_renewable_capital_intensity_p0_diffw_252d_base_v088_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=378
def f39rci_f39_renewable_capital_intensity_p0_diffw_378d_base_v089_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_diffw window=504
def f39rci_f39_renewable_capital_intensity_p0_diffw_504d_base_v090_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).diff(504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=5
def f39rci_f39_renewable_capital_intensity_p0_pctchg_5d_base_v091_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=10
def f39rci_f39_renewable_capital_intensity_p0_pctchg_10d_base_v092_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=21
def f39rci_f39_renewable_capital_intensity_p0_pctchg_21d_base_v093_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=42
def f39rci_f39_renewable_capital_intensity_p0_pctchg_42d_base_v094_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=63
def f39rci_f39_renewable_capital_intensity_p0_pctchg_63d_base_v095_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=126
def f39rci_f39_renewable_capital_intensity_p0_pctchg_126d_base_v096_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=189
def f39rci_f39_renewable_capital_intensity_p0_pctchg_189d_base_v097_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=252
def f39rci_f39_renewable_capital_intensity_p0_pctchg_252d_base_v098_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=378
def f39rci_f39_renewable_capital_intensity_p0_pctchg_378d_base_v099_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_pctchg window=504
def f39rci_f39_renewable_capital_intensity_p0_pctchg_504d_base_v100_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).pct_change(periods=504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=5
def f39rci_f39_renewable_capital_intensity_p0_rangew_5d_base_v101_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(5, min_periods=max(1, 5//2)).max() - b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=10
def f39rci_f39_renewable_capital_intensity_p0_rangew_10d_base_v102_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(10, min_periods=max(1, 10//2)).max() - b.rolling(10, min_periods=max(1, 10//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=21
def f39rci_f39_renewable_capital_intensity_p0_rangew_21d_base_v103_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(21, min_periods=max(1, 21//2)).max() - b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=42
def f39rci_f39_renewable_capital_intensity_p0_rangew_42d_base_v104_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(42, min_periods=max(1, 42//2)).max() - b.rolling(42, min_periods=max(1, 42//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=63
def f39rci_f39_renewable_capital_intensity_p0_rangew_63d_base_v105_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(63, min_periods=max(1, 63//2)).max() - b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=126
def f39rci_f39_renewable_capital_intensity_p0_rangew_126d_base_v106_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(126, min_periods=max(1, 126//2)).max() - b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=189
def f39rci_f39_renewable_capital_intensity_p0_rangew_189d_base_v107_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(189, min_periods=max(1, 189//2)).max() - b.rolling(189, min_periods=max(1, 189//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=252
def f39rci_f39_renewable_capital_intensity_p0_rangew_252d_base_v108_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(252, min_periods=max(1, 252//2)).max() - b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=378
def f39rci_f39_renewable_capital_intensity_p0_rangew_378d_base_v109_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(378, min_periods=max(1, 378//2)).max() - b.rolling(378, min_periods=max(1, 378//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_rangew window=504
def f39rci_f39_renewable_capital_intensity_p0_rangew_504d_base_v110_signal(closeadj, equity, capex):
    b = _f39_capex_to_equity(capex, equity)
    base = (b.rolling(504, min_periods=max(1, 504//2)).max() - b.rolling(504, min_periods=max(1, 504//2)).min()) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=5
def f39rci_f39_renewable_capital_intensity_p0_minw_5d_base_v111_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(5, min_periods=max(1, 5//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=10
def f39rci_f39_renewable_capital_intensity_p0_minw_10d_base_v112_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(10, min_periods=max(1, 10//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=21
def f39rci_f39_renewable_capital_intensity_p0_minw_21d_base_v113_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(21, min_periods=max(1, 21//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=42
def f39rci_f39_renewable_capital_intensity_p0_minw_42d_base_v114_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(42, min_periods=max(1, 42//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=63
def f39rci_f39_renewable_capital_intensity_p0_minw_63d_base_v115_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(63, min_periods=max(1, 63//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=126
def f39rci_f39_renewable_capital_intensity_p0_minw_126d_base_v116_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(126, min_periods=max(1, 126//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=189
def f39rci_f39_renewable_capital_intensity_p0_minw_189d_base_v117_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(189, min_periods=max(1, 189//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=252
def f39rci_f39_renewable_capital_intensity_p0_minw_252d_base_v118_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=378
def f39rci_f39_renewable_capital_intensity_p0_minw_378d_base_v119_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(378, min_periods=max(1, 378//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_minw window=504
def f39rci_f39_renewable_capital_intensity_p0_minw_504d_base_v120_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=5
def f39rci_f39_renewable_capital_intensity_p0_maxw_5d_base_v121_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(5, min_periods=max(1, 5//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=10
def f39rci_f39_renewable_capital_intensity_p0_maxw_10d_base_v122_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(10, min_periods=max(1, 10//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=21
def f39rci_f39_renewable_capital_intensity_p0_maxw_21d_base_v123_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(21, min_periods=max(1, 21//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=42
def f39rci_f39_renewable_capital_intensity_p0_maxw_42d_base_v124_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(42, min_periods=max(1, 42//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=63
def f39rci_f39_renewable_capital_intensity_p0_maxw_63d_base_v125_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(63, min_periods=max(1, 63//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=126
def f39rci_f39_renewable_capital_intensity_p0_maxw_126d_base_v126_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(126, min_periods=max(1, 126//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=189
def f39rci_f39_renewable_capital_intensity_p0_maxw_189d_base_v127_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(189, min_periods=max(1, 189//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=252
def f39rci_f39_renewable_capital_intensity_p0_maxw_252d_base_v128_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=378
def f39rci_f39_renewable_capital_intensity_p0_maxw_378d_base_v129_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(378, min_periods=max(1, 378//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_maxw window=504
def f39rci_f39_renewable_capital_intensity_p0_maxw_504d_base_v130_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=5
def f39rci_f39_renewable_capital_intensity_p0_skew_5d_base_v131_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(5, min_periods=max(1, 5//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=10
def f39rci_f39_renewable_capital_intensity_p0_skew_10d_base_v132_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(10, min_periods=max(1, 10//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=21
def f39rci_f39_renewable_capital_intensity_p0_skew_21d_base_v133_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(21, min_periods=max(1, 21//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=42
def f39rci_f39_renewable_capital_intensity_p0_skew_42d_base_v134_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(42, min_periods=max(1, 42//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=63
def f39rci_f39_renewable_capital_intensity_p0_skew_63d_base_v135_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(63, min_periods=max(1, 63//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=126
def f39rci_f39_renewable_capital_intensity_p0_skew_126d_base_v136_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(126, min_periods=max(1, 126//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=189
def f39rci_f39_renewable_capital_intensity_p0_skew_189d_base_v137_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(189, min_periods=max(1, 189//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=252
def f39rci_f39_renewable_capital_intensity_p0_skew_252d_base_v138_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(252, min_periods=max(1, 252//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=378
def f39rci_f39_renewable_capital_intensity_p0_skew_378d_base_v139_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(378, min_periods=max(1, 378//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_skew window=504
def f39rci_f39_renewable_capital_intensity_p0_skew_504d_base_v140_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(504, min_periods=max(1, 504//2)).skew() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=5
def f39rci_f39_renewable_capital_intensity_p0_kurt_5d_base_v141_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(5, min_periods=max(1, 5//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=10
def f39rci_f39_renewable_capital_intensity_p0_kurt_10d_base_v142_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(10, min_periods=max(1, 10//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=21
def f39rci_f39_renewable_capital_intensity_p0_kurt_21d_base_v143_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(21, min_periods=max(1, 21//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=42
def f39rci_f39_renewable_capital_intensity_p0_kurt_42d_base_v144_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(42, min_periods=max(1, 42//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=63
def f39rci_f39_renewable_capital_intensity_p0_kurt_63d_base_v145_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(63, min_periods=max(1, 63//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=126
def f39rci_f39_renewable_capital_intensity_p0_kurt_126d_base_v146_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(126, min_periods=max(1, 126//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=189
def f39rci_f39_renewable_capital_intensity_p0_kurt_189d_base_v147_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(189, min_periods=max(1, 189//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=252
def f39rci_f39_renewable_capital_intensity_p0_kurt_252d_base_v148_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(252, min_periods=max(1, 252//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=378
def f39rci_f39_renewable_capital_intensity_p0_kurt_378d_base_v149_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(378, min_periods=max(1, 378//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_kurt window=504
def f39rci_f39_renewable_capital_intensity_p0_kurt_504d_base_v150_signal(closeadj, equity, capex):
    base = (_f39_capex_to_equity(capex, equity)).rolling(504, min_periods=max(1, 504//2)).kurt() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39rci_f39_renewable_capital_intensity_p0_qrank_126d_base_v076_signal,
    f39rci_f39_renewable_capital_intensity_p0_qrank_189d_base_v077_signal,
    f39rci_f39_renewable_capital_intensity_p0_qrank_252d_base_v078_signal,
    f39rci_f39_renewable_capital_intensity_p0_qrank_378d_base_v079_signal,
    f39rci_f39_renewable_capital_intensity_p0_qrank_504d_base_v080_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_5d_base_v081_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_10d_base_v082_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_21d_base_v083_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_42d_base_v084_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_63d_base_v085_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_126d_base_v086_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_189d_base_v087_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_252d_base_v088_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_378d_base_v089_signal,
    f39rci_f39_renewable_capital_intensity_p0_diffw_504d_base_v090_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_5d_base_v091_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_10d_base_v092_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_21d_base_v093_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_42d_base_v094_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_63d_base_v095_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_126d_base_v096_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_189d_base_v097_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_252d_base_v098_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_378d_base_v099_signal,
    f39rci_f39_renewable_capital_intensity_p0_pctchg_504d_base_v100_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_5d_base_v101_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_10d_base_v102_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_21d_base_v103_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_42d_base_v104_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_63d_base_v105_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_126d_base_v106_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_189d_base_v107_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_252d_base_v108_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_378d_base_v109_signal,
    f39rci_f39_renewable_capital_intensity_p0_rangew_504d_base_v110_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_5d_base_v111_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_10d_base_v112_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_21d_base_v113_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_42d_base_v114_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_63d_base_v115_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_126d_base_v116_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_189d_base_v117_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_252d_base_v118_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_378d_base_v119_signal,
    f39rci_f39_renewable_capital_intensity_p0_minw_504d_base_v120_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_5d_base_v121_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_10d_base_v122_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_21d_base_v123_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_42d_base_v124_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_63d_base_v125_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_126d_base_v126_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_189d_base_v127_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_252d_base_v128_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_378d_base_v129_signal,
    f39rci_f39_renewable_capital_intensity_p0_maxw_504d_base_v130_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_5d_base_v131_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_10d_base_v132_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_21d_base_v133_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_42d_base_v134_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_63d_base_v135_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_126d_base_v136_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_189d_base_v137_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_252d_base_v138_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_378d_base_v139_signal,
    f39rci_f39_renewable_capital_intensity_p0_skew_504d_base_v140_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_5d_base_v141_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_10d_base_v142_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_21d_base_v143_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_42d_base_v144_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_63d_base_v145_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_126d_base_v146_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_189d_base_v147_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_252d_base_v148_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_378d_base_v149_signal,
    f39rci_f39_renewable_capital_intensity_p0_kurt_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_RENEWABLE_CAPITAL_INTENSITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    de        = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "debt": debt, "equity": equity, "ebitda": ebitda, "fcf": fcf,
        "capex": capex, "sharesbas": sharesbas, "shareswa": shareswa, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_capex_to_equity", "_f39_capital_intensity", "_f39_capital_burden")
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
    print(f"OK f39_renewable_capital_intensity_base_076_150_claude: {n_features} features pass")
