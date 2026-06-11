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
def _f30_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f30_capital_light_score(capex, revenue, fcf, w):
    ci = capex / revenue.replace(0, np.nan)
    fci = fcf / revenue.replace(0, np.nan)
    return (fci - ci).rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_capital_light_compound(fcf, revenue, w):
    fcfm = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    revm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (fcfm / revm.replace(0, np.nan)).pct_change(periods=w)


# EMA capex intensity x close w=5
def f30clc_f30_cro_capital_light_compounder_capexintema_5d_base_v076_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=10
def f30clc_f30_cro_capital_light_compounder_capexintema_10d_base_v077_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=21
def f30clc_f30_cro_capital_light_compounder_capexintema_21d_base_v078_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=42
def f30clc_f30_cro_capital_light_compounder_capexintema_42d_base_v079_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=63
def f30clc_f30_cro_capital_light_compounder_capexintema_63d_base_v080_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=126
def f30clc_f30_cro_capital_light_compounder_capexintema_126d_base_v081_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=189
def f30clc_f30_cro_capital_light_compounder_capexintema_189d_base_v082_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=252
def f30clc_f30_cro_capital_light_compounder_capexintema_252d_base_v083_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=378
def f30clc_f30_cro_capital_light_compounder_capexintema_378d_base_v084_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capex intensity x close w=504
def f30clc_f30_cro_capital_light_compounder_capexintema_504d_base_v085_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    ema = ci.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=5
def f30clc_f30_cro_capital_light_compounder_clscoreema_5d_base_v086_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    ema = cls.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=10
def f30clc_f30_cro_capital_light_compounder_clscoreema_10d_base_v087_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    ema = cls.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=21
def f30clc_f30_cro_capital_light_compounder_clscoreema_21d_base_v088_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    ema = cls.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=42
def f30clc_f30_cro_capital_light_compounder_clscoreema_42d_base_v089_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    ema = cls.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=63
def f30clc_f30_cro_capital_light_compounder_clscoreema_63d_base_v090_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    ema = cls.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=126
def f30clc_f30_cro_capital_light_compounder_clscoreema_126d_base_v091_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    ema = cls.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=189
def f30clc_f30_cro_capital_light_compounder_clscoreema_189d_base_v092_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 189)
    ema = cls.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=252
def f30clc_f30_cro_capital_light_compounder_clscoreema_252d_base_v093_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    ema = cls.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=378
def f30clc_f30_cro_capital_light_compounder_clscoreema_378d_base_v094_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 378)
    ema = cls.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light score x close w=504
def f30clc_f30_cro_capital_light_compounder_clscoreema_504d_base_v095_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    ema = cls.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=5
def f30clc_f30_cro_capital_light_compounder_clcompema_5d_base_v096_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    ema = clc.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=10
def f30clc_f30_cro_capital_light_compounder_clcompema_10d_base_v097_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    ema = clc.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=21
def f30clc_f30_cro_capital_light_compounder_clcompema_21d_base_v098_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    ema = clc.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=42
def f30clc_f30_cro_capital_light_compounder_clcompema_42d_base_v099_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    ema = clc.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=63
def f30clc_f30_cro_capital_light_compounder_clcompema_63d_base_v100_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    ema = clc.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=126
def f30clc_f30_cro_capital_light_compounder_clcompema_126d_base_v101_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 126)
    ema = clc.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=189
def f30clc_f30_cro_capital_light_compounder_clcompema_189d_base_v102_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 189)
    ema = clc.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=252
def f30clc_f30_cro_capital_light_compounder_clcompema_252d_base_v103_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    ema = clc.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=378
def f30clc_f30_cro_capital_light_compounder_clcompema_378d_base_v104_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 378)
    ema = clc.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA capital-light compound x close w=504
def f30clc_f30_cro_capital_light_compounder_clcompema_504d_base_v105_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 504)
    ema = clc.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=5
def f30clc_f30_cro_capital_light_compounder_capexintxdv_5d_base_v106_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 5)
    result = ci.rolling(5, min_periods=max(1, 5 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=10
def f30clc_f30_cro_capital_light_compounder_capexintxdv_10d_base_v107_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 10)
    result = ci.rolling(10, min_periods=max(1, 10 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=21
def f30clc_f30_cro_capital_light_compounder_capexintxdv_21d_base_v108_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 21)
    result = ci.rolling(21, min_periods=max(1, 21 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=42
def f30clc_f30_cro_capital_light_compounder_capexintxdv_42d_base_v109_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 42)
    result = ci.rolling(42, min_periods=max(1, 42 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=63
def f30clc_f30_cro_capital_light_compounder_capexintxdv_63d_base_v110_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 63)
    result = ci.rolling(63, min_periods=max(1, 63 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=126
def f30clc_f30_cro_capital_light_compounder_capexintxdv_126d_base_v111_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 126)
    result = ci.rolling(126, min_periods=max(1, 126 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=189
def f30clc_f30_cro_capital_light_compounder_capexintxdv_189d_base_v112_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 189)
    result = ci.rolling(189, min_periods=max(1, 189 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=252
def f30clc_f30_cro_capital_light_compounder_capexintxdv_252d_base_v113_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 252)
    result = ci.rolling(252, min_periods=max(1, 252 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=378
def f30clc_f30_cro_capital_light_compounder_capexintxdv_378d_base_v114_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 378)
    result = ci.rolling(378, min_periods=max(1, 378 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity x dollar vol mean w=504
def f30clc_f30_cro_capital_light_compounder_capexintxdv_504d_base_v115_signal(capex, revenue, closeadj, volume):
    ci = _f30_capex_intensity(capex, revenue)
    vm = _mean(closeadj * volume, 504)
    result = ci.rolling(504, min_periods=max(1, 504 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=5
def f30clc_f30_cro_capital_light_compounder_clscorexdv_5d_base_v116_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    vm = _mean(closeadj * volume, 5)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=10
def f30clc_f30_cro_capital_light_compounder_clscorexdv_10d_base_v117_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    vm = _mean(closeadj * volume, 10)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=21
def f30clc_f30_cro_capital_light_compounder_clscorexdv_21d_base_v118_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    vm = _mean(closeadj * volume, 21)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=42
def f30clc_f30_cro_capital_light_compounder_clscorexdv_42d_base_v119_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    vm = _mean(closeadj * volume, 42)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=63
def f30clc_f30_cro_capital_light_compounder_clscorexdv_63d_base_v120_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    vm = _mean(closeadj * volume, 63)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=126
def f30clc_f30_cro_capital_light_compounder_clscorexdv_126d_base_v121_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    vm = _mean(closeadj * volume, 126)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=189
def f30clc_f30_cro_capital_light_compounder_clscorexdv_189d_base_v122_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 189)
    vm = _mean(closeadj * volume, 189)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=252
def f30clc_f30_cro_capital_light_compounder_clscorexdv_252d_base_v123_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    vm = _mean(closeadj * volume, 252)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=378
def f30clc_f30_cro_capital_light_compounder_clscorexdv_378d_base_v124_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 378)
    vm = _mean(closeadj * volume, 378)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score x dollar vol mean w=504
def f30clc_f30_cro_capital_light_compounder_clscorexdv_504d_base_v125_signal(capex, revenue, fcf, closeadj, volume):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    vm = _mean(closeadj * volume, 504)
    result = cls * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=5
def f30clc_f30_cro_capital_light_compounder_clcomprk_5d_base_v126_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    r = clc.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=10
def f30clc_f30_cro_capital_light_compounder_clcomprk_10d_base_v127_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    r = clc.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=21
def f30clc_f30_cro_capital_light_compounder_clcomprk_21d_base_v128_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    r = clc.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=42
def f30clc_f30_cro_capital_light_compounder_clcomprk_42d_base_v129_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    r = clc.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=63
def f30clc_f30_cro_capital_light_compounder_clcomprk_63d_base_v130_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    r = clc.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=126
def f30clc_f30_cro_capital_light_compounder_clcomprk_126d_base_v131_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 126)
    r = clc.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=189
def f30clc_f30_cro_capital_light_compounder_clcomprk_189d_base_v132_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 189)
    r = clc.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=252
def f30clc_f30_cro_capital_light_compounder_clcomprk_252d_base_v133_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    r = clc.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=378
def f30clc_f30_cro_capital_light_compounder_clcomprk_378d_base_v134_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 378)
    r = clc.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light compound rank x close w=504
def f30clc_f30_cro_capital_light_compounder_clcomprk_504d_base_v135_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 504)
    r = clc.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity rank x close w=5
def f30clc_f30_cro_capital_light_compounder_capexintrk_5d_base_v136_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    r = ci.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity rank x close w=10
def f30clc_f30_cro_capital_light_compounder_capexintrk_10d_base_v137_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    r = ci.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity rank x close w=21
def f30clc_f30_cro_capital_light_compounder_capexintrk_21d_base_v138_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    r = ci.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity rank x close w=42
def f30clc_f30_cro_capital_light_compounder_capexintrk_42d_base_v139_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    r = ci.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity rank x close w=63
def f30clc_f30_cro_capital_light_compounder_capexintrk_63d_base_v140_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    r = ci.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score rank x close w=5
def f30clc_f30_cro_capital_light_compounder_clscorerk_5d_base_v141_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    r = cls.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score rank x close w=10
def f30clc_f30_cro_capital_light_compounder_clscorerk_10d_base_v142_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    r = cls.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score rank x close w=21
def f30clc_f30_cro_capital_light_compounder_clscorerk_21d_base_v143_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    r = cls.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score rank x close w=42
def f30clc_f30_cro_capital_light_compounder_clscorerk_42d_base_v144_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    r = cls.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# capital-light score rank x close w=63
def f30clc_f30_cro_capital_light_compounder_clscorerk_63d_base_v145_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    r = cls.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# compound minus intensity x close w=5
def f30clc_f30_cro_capital_light_compounder_clcompminusci_5d_base_v146_signal(capex, revenue, fcf, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    result = (clc - ci) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# compound minus intensity x close w=10
def f30clc_f30_cro_capital_light_compounder_clcompminusci_10d_base_v147_signal(capex, revenue, fcf, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    result = (clc - ci) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# compound minus intensity x close w=21
def f30clc_f30_cro_capital_light_compounder_clcompminusci_21d_base_v148_signal(capex, revenue, fcf, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    result = (clc - ci) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# compound minus intensity x close w=42
def f30clc_f30_cro_capital_light_compounder_clcompminusci_42d_base_v149_signal(capex, revenue, fcf, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    result = (clc - ci) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# compound minus intensity x close w=63
def f30clc_f30_cro_capital_light_compounder_clcompminusci_63d_base_v150_signal(capex, revenue, fcf, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    result = (clc - ci) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30clc_f30_cro_capital_light_compounder_capexintema_5d_base_v076_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_10d_base_v077_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_21d_base_v078_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_42d_base_v079_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_63d_base_v080_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_126d_base_v081_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_189d_base_v082_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_252d_base_v083_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_378d_base_v084_signal,
    f30clc_f30_cro_capital_light_compounder_capexintema_504d_base_v085_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_5d_base_v086_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_10d_base_v087_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_21d_base_v088_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_42d_base_v089_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_63d_base_v090_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_126d_base_v091_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_189d_base_v092_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_252d_base_v093_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_378d_base_v094_signal,
    f30clc_f30_cro_capital_light_compounder_clscoreema_504d_base_v095_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_5d_base_v096_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_10d_base_v097_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_21d_base_v098_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_42d_base_v099_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_63d_base_v100_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_126d_base_v101_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_189d_base_v102_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_252d_base_v103_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_378d_base_v104_signal,
    f30clc_f30_cro_capital_light_compounder_clcompema_504d_base_v105_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_5d_base_v106_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_10d_base_v107_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_21d_base_v108_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_42d_base_v109_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_63d_base_v110_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_126d_base_v111_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_189d_base_v112_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_252d_base_v113_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_378d_base_v114_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxdv_504d_base_v115_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_5d_base_v116_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_10d_base_v117_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_21d_base_v118_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_42d_base_v119_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_63d_base_v120_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_126d_base_v121_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_189d_base_v122_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_252d_base_v123_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_378d_base_v124_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexdv_504d_base_v125_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_5d_base_v126_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_10d_base_v127_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_21d_base_v128_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_42d_base_v129_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_63d_base_v130_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_126d_base_v131_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_189d_base_v132_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_252d_base_v133_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_378d_base_v134_signal,
    f30clc_f30_cro_capital_light_compounder_clcomprk_504d_base_v135_signal,
    f30clc_f30_cro_capital_light_compounder_capexintrk_5d_base_v136_signal,
    f30clc_f30_cro_capital_light_compounder_capexintrk_10d_base_v137_signal,
    f30clc_f30_cro_capital_light_compounder_capexintrk_21d_base_v138_signal,
    f30clc_f30_cro_capital_light_compounder_capexintrk_42d_base_v139_signal,
    f30clc_f30_cro_capital_light_compounder_capexintrk_63d_base_v140_signal,
    f30clc_f30_cro_capital_light_compounder_clscorerk_5d_base_v141_signal,
    f30clc_f30_cro_capital_light_compounder_clscorerk_10d_base_v142_signal,
    f30clc_f30_cro_capital_light_compounder_clscorerk_21d_base_v143_signal,
    f30clc_f30_cro_capital_light_compounder_clscorerk_42d_base_v144_signal,
    f30clc_f30_cro_capital_light_compounder_clscorerk_63d_base_v145_signal,
    f30clc_f30_cro_capital_light_compounder_clcompminusci_5d_base_v146_signal,
    f30clc_f30_cro_capital_light_compounder_clcompminusci_10d_base_v147_signal,
    f30clc_f30_cro_capital_light_compounder_clcompminusci_21d_base_v148_signal,
    f30clc_f30_cro_capital_light_compounder_clcompminusci_42d_base_v149_signal,
    f30clc_f30_cro_capital_light_compounder_clcompminusci_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CRO_CAPITAL_LIGHT_COMPOUNDER_REGISTRY_076_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_capex_intensity", "_f30_capital_light_score", "_f30_capital_light_compound",)
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
    print(f"OK f30_cro_capital_light_compounder_base_076_150_claude: {n_features} features pass")
