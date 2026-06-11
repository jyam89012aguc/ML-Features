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


# ===== folder domain primitives =====
def _f08_ppe_growth(ppnenet, w):
    return ppnenet.pct_change(periods=w)


def _f08_installed_base_proxy(ppnenet, revenue, w):
    g = ppnenet.pct_change(periods=w)
    return g * (revenue / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


def _f08_install_acceleration(ppnenet, capex, w):
    return (capex / ppnenet.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()

def f08dib_f08_device_installed_base_growth_p0log_126d_base_v076_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 126.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0log_189d_base_v077_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 189.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0log_252d_base_v078_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 252.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0log_378d_base_v079_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 378.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0log_504d_base_v080_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 504.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_5d_base_v081_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    result = base.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_10d_base_v082_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    result = base.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_21d_base_v083_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    result = base.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_42d_base_v084_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    result = base.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_63d_base_v085_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    result = base.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_126d_base_v086_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = base.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_189d_base_v087_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = base.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_252d_base_v088_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = base.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_378d_base_v089_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = base.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0rank_504d_base_v090_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = base.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_5d_base_v091_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    med = base.rolling(5, min_periods=max(1, 5 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_10d_base_v092_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    med = base.rolling(10, min_periods=max(1, 10 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_21d_base_v093_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_42d_base_v094_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    med = base.rolling(42, min_periods=max(1, 42 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_63d_base_v095_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_126d_base_v096_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_189d_base_v097_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    med = base.rolling(189, min_periods=max(1, 189 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_252d_base_v098_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_378d_base_v099_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    med = base.rolling(378, min_periods=max(1, 378 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0mednorm_504d_base_v100_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    med = base.rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (base - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_5d_base_v101_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    result = base.rolling(5, min_periods=max(1, 5 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_10d_base_v102_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    result = base.rolling(10, min_periods=max(1, 10 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_21d_base_v103_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    result = base.rolling(21, min_periods=max(1, 21 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_42d_base_v104_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    result = base.rolling(42, min_periods=max(1, 42 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_63d_base_v105_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    result = base.rolling(63, min_periods=max(1, 63 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_126d_base_v106_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = base.rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_189d_base_v107_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = base.rolling(189, min_periods=max(1, 189 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_252d_base_v108_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = base.rolling(252, min_periods=max(1, 252 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_378d_base_v109_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = base.rolling(378, min_periods=max(1, 378 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0max_504d_base_v110_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = base.rolling(504, min_periods=max(1, 504 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_5d_base_v111_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    result = base.rolling(5, min_periods=max(1, 5 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_10d_base_v112_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    result = base.rolling(10, min_periods=max(1, 10 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_21d_base_v113_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    result = base.rolling(21, min_periods=max(1, 21 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_42d_base_v114_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    result = base.rolling(42, min_periods=max(1, 42 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_63d_base_v115_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    result = base.rolling(63, min_periods=max(1, 63 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_126d_base_v116_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = base.rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_189d_base_v117_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = base.rolling(189, min_periods=max(1, 189 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_252d_base_v118_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = base.rolling(252, min_periods=max(1, 252 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_378d_base_v119_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = base.rolling(378, min_periods=max(1, 378 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0min_504d_base_v120_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = base.rolling(504, min_periods=max(1, 504 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_5d_base_v121_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    rmax = base.rolling(5, min_periods=max(1, 5 // 2)).max()
    rmin = base.rolling(5, min_periods=max(1, 5 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_10d_base_v122_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    rmax = base.rolling(10, min_periods=max(1, 10 // 2)).max()
    rmin = base.rolling(10, min_periods=max(1, 10 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_21d_base_v123_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    rmax = base.rolling(21, min_periods=max(1, 21 // 2)).max()
    rmin = base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_42d_base_v124_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    rmax = base.rolling(42, min_periods=max(1, 42 // 2)).max()
    rmin = base.rolling(42, min_periods=max(1, 42 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_63d_base_v125_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    rmax = base.rolling(63, min_periods=max(1, 63 // 2)).max()
    rmin = base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_126d_base_v126_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    rmax = base.rolling(126, min_periods=max(1, 126 // 2)).max()
    rmin = base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_189d_base_v127_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    rmax = base.rolling(189, min_periods=max(1, 189 // 2)).max()
    rmin = base.rolling(189, min_periods=max(1, 189 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_252d_base_v128_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    rmax = base.rolling(252, min_periods=max(1, 252 // 2)).max()
    rmin = base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_378d_base_v129_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    rmax = base.rolling(378, min_periods=max(1, 378 // 2)).max()
    rmin = base.rolling(378, min_periods=max(1, 378 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0range_504d_base_v130_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    rmax = base.rolling(504, min_periods=max(1, 504 // 2)).max()
    rmin = base.rolling(504, min_periods=max(1, 504 // 2)).min()
    result = (rmax - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_5d_base_v131_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    result = (base - _mean(base, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_10d_base_v132_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    result = (base - _mean(base, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_21d_base_v133_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    result = (base - _mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_42d_base_v134_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    result = (base - _mean(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_63d_base_v135_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    result = (base - _mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_126d_base_v136_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = (base - _mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_189d_base_v137_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = (base - _mean(base, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_252d_base_v138_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_378d_base_v139_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = (base - _mean(base, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0xmean_504d_base_v140_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_5d_base_v141_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 5)
    result = (base * base.abs()) * closeadj * 5.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_10d_base_v142_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 10)
    result = (base * base.abs()) * closeadj * 10.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_21d_base_v143_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    result = (base * base.abs()) * closeadj * 21.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_42d_base_v144_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 42)
    result = (base * base.abs()) * closeadj * 42.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_63d_base_v145_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    result = (base * base.abs()) * closeadj * 63.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_126d_base_v146_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    result = (base * base.abs()) * closeadj * 126.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_189d_base_v147_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 189)
    result = (base * base.abs()) * closeadj * 189.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_252d_base_v148_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    result = (base * base.abs()) * closeadj * 252.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_378d_base_v149_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 378)
    result = (base * base.abs()) * closeadj * 378.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0sq_504d_base_v150_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    result = (base * base.abs()) * closeadj * 504.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08dib_f08_device_installed_base_growth_p0log_126d_base_v076_signal,
    f08dib_f08_device_installed_base_growth_p0log_189d_base_v077_signal,
    f08dib_f08_device_installed_base_growth_p0log_252d_base_v078_signal,
    f08dib_f08_device_installed_base_growth_p0log_378d_base_v079_signal,
    f08dib_f08_device_installed_base_growth_p0log_504d_base_v080_signal,
    f08dib_f08_device_installed_base_growth_p0rank_5d_base_v081_signal,
    f08dib_f08_device_installed_base_growth_p0rank_10d_base_v082_signal,
    f08dib_f08_device_installed_base_growth_p0rank_21d_base_v083_signal,
    f08dib_f08_device_installed_base_growth_p0rank_42d_base_v084_signal,
    f08dib_f08_device_installed_base_growth_p0rank_63d_base_v085_signal,
    f08dib_f08_device_installed_base_growth_p0rank_126d_base_v086_signal,
    f08dib_f08_device_installed_base_growth_p0rank_189d_base_v087_signal,
    f08dib_f08_device_installed_base_growth_p0rank_252d_base_v088_signal,
    f08dib_f08_device_installed_base_growth_p0rank_378d_base_v089_signal,
    f08dib_f08_device_installed_base_growth_p0rank_504d_base_v090_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_5d_base_v091_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_10d_base_v092_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_21d_base_v093_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_42d_base_v094_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_63d_base_v095_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_126d_base_v096_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_189d_base_v097_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_252d_base_v098_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_378d_base_v099_signal,
    f08dib_f08_device_installed_base_growth_p0mednorm_504d_base_v100_signal,
    f08dib_f08_device_installed_base_growth_p0max_5d_base_v101_signal,
    f08dib_f08_device_installed_base_growth_p0max_10d_base_v102_signal,
    f08dib_f08_device_installed_base_growth_p0max_21d_base_v103_signal,
    f08dib_f08_device_installed_base_growth_p0max_42d_base_v104_signal,
    f08dib_f08_device_installed_base_growth_p0max_63d_base_v105_signal,
    f08dib_f08_device_installed_base_growth_p0max_126d_base_v106_signal,
    f08dib_f08_device_installed_base_growth_p0max_189d_base_v107_signal,
    f08dib_f08_device_installed_base_growth_p0max_252d_base_v108_signal,
    f08dib_f08_device_installed_base_growth_p0max_378d_base_v109_signal,
    f08dib_f08_device_installed_base_growth_p0max_504d_base_v110_signal,
    f08dib_f08_device_installed_base_growth_p0min_5d_base_v111_signal,
    f08dib_f08_device_installed_base_growth_p0min_10d_base_v112_signal,
    f08dib_f08_device_installed_base_growth_p0min_21d_base_v113_signal,
    f08dib_f08_device_installed_base_growth_p0min_42d_base_v114_signal,
    f08dib_f08_device_installed_base_growth_p0min_63d_base_v115_signal,
    f08dib_f08_device_installed_base_growth_p0min_126d_base_v116_signal,
    f08dib_f08_device_installed_base_growth_p0min_189d_base_v117_signal,
    f08dib_f08_device_installed_base_growth_p0min_252d_base_v118_signal,
    f08dib_f08_device_installed_base_growth_p0min_378d_base_v119_signal,
    f08dib_f08_device_installed_base_growth_p0min_504d_base_v120_signal,
    f08dib_f08_device_installed_base_growth_p0range_5d_base_v121_signal,
    f08dib_f08_device_installed_base_growth_p0range_10d_base_v122_signal,
    f08dib_f08_device_installed_base_growth_p0range_21d_base_v123_signal,
    f08dib_f08_device_installed_base_growth_p0range_42d_base_v124_signal,
    f08dib_f08_device_installed_base_growth_p0range_63d_base_v125_signal,
    f08dib_f08_device_installed_base_growth_p0range_126d_base_v126_signal,
    f08dib_f08_device_installed_base_growth_p0range_189d_base_v127_signal,
    f08dib_f08_device_installed_base_growth_p0range_252d_base_v128_signal,
    f08dib_f08_device_installed_base_growth_p0range_378d_base_v129_signal,
    f08dib_f08_device_installed_base_growth_p0range_504d_base_v130_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_5d_base_v131_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_10d_base_v132_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_21d_base_v133_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_42d_base_v134_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_63d_base_v135_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_126d_base_v136_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_189d_base_v137_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_252d_base_v138_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_378d_base_v139_signal,
    f08dib_f08_device_installed_base_growth_p0xmean_504d_base_v140_signal,
    f08dib_f08_device_installed_base_growth_p0sq_5d_base_v141_signal,
    f08dib_f08_device_installed_base_growth_p0sq_10d_base_v142_signal,
    f08dib_f08_device_installed_base_growth_p0sq_21d_base_v143_signal,
    f08dib_f08_device_installed_base_growth_p0sq_42d_base_v144_signal,
    f08dib_f08_device_installed_base_growth_p0sq_63d_base_v145_signal,
    f08dib_f08_device_installed_base_growth_p0sq_126d_base_v146_signal,
    f08dib_f08_device_installed_base_growth_p0sq_189d_base_v147_signal,
    f08dib_f08_device_installed_base_growth_p0sq_252d_base_v148_signal,
    f08dib_f08_device_installed_base_growth_p0sq_378d_base_v149_signal,
    f08dib_f08_device_installed_base_growth_p0sq_504d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_DEVICE_INSTALLED_BASE_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    inventory   = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "assets": assets, "ppnenet": ppnenet, "capex": capex,
        "inventory": inventory, "receivables": receivables, "cor": cor,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_ppe_growth", "_f08_installed_base_proxy", "_f08_install_acceleration",)
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
    print(f"OK f08_device_installed_base_growth_base_076_150_claude: {n_features} features pass")
