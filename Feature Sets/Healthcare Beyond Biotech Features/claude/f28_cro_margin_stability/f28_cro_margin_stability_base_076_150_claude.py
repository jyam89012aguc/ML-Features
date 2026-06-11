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
def _f28_service_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f28_margin_stability(ebitdamargin, w):
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (sd.replace(0, np.nan) + 1e-6)


def _f28_durability_score(ebitdamargin, grossmargin, w):
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (em * gm) / (sd.replace(0, np.nan) + 1e-6)


# EMA service margin floor x close w=5
def f28cms_f28_cro_margin_stability_smfloorema_5d_base_v076_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    ema = f.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=10
def f28cms_f28_cro_margin_stability_smfloorema_10d_base_v077_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    ema = f.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=21
def f28cms_f28_cro_margin_stability_smfloorema_21d_base_v078_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    ema = f.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=42
def f28cms_f28_cro_margin_stability_smfloorema_42d_base_v079_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    ema = f.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=63
def f28cms_f28_cro_margin_stability_smfloorema_63d_base_v080_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    ema = f.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=126
def f28cms_f28_cro_margin_stability_smfloorema_126d_base_v081_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 126)
    ema = f.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=189
def f28cms_f28_cro_margin_stability_smfloorema_189d_base_v082_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 189)
    ema = f.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=252
def f28cms_f28_cro_margin_stability_smfloorema_252d_base_v083_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    ema = f.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=378
def f28cms_f28_cro_margin_stability_smfloorema_378d_base_v084_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 378)
    ema = f.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA service margin floor x close w=504
def f28cms_f28_cro_margin_stability_smfloorema_504d_base_v085_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 504)
    ema = f.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=5
def f28cms_f28_cro_margin_stability_mstabema_5d_base_v086_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 5)
    ema = ms.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=10
def f28cms_f28_cro_margin_stability_mstabema_10d_base_v087_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 10)
    ema = ms.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=21
def f28cms_f28_cro_margin_stability_mstabema_21d_base_v088_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    ema = ms.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=42
def f28cms_f28_cro_margin_stability_mstabema_42d_base_v089_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 42)
    ema = ms.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=63
def f28cms_f28_cro_margin_stability_mstabema_63d_base_v090_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    ema = ms.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=126
def f28cms_f28_cro_margin_stability_mstabema_126d_base_v091_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 126)
    ema = ms.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=189
def f28cms_f28_cro_margin_stability_mstabema_189d_base_v092_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 189)
    ema = ms.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=252
def f28cms_f28_cro_margin_stability_mstabema_252d_base_v093_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    ema = ms.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=378
def f28cms_f28_cro_margin_stability_mstabema_378d_base_v094_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 378)
    ema = ms.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA margin stability x close w=504
def f28cms_f28_cro_margin_stability_mstabema_504d_base_v095_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 504)
    ema = ms.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=5
def f28cms_f28_cro_margin_stability_durscoreema_5d_base_v096_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 5)
    ema = ds.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=10
def f28cms_f28_cro_margin_stability_durscoreema_10d_base_v097_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 10)
    ema = ds.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=21
def f28cms_f28_cro_margin_stability_durscoreema_21d_base_v098_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    ema = ds.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=42
def f28cms_f28_cro_margin_stability_durscoreema_42d_base_v099_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    ema = ds.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=63
def f28cms_f28_cro_margin_stability_durscoreema_63d_base_v100_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    ema = ds.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=126
def f28cms_f28_cro_margin_stability_durscoreema_126d_base_v101_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    ema = ds.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=189
def f28cms_f28_cro_margin_stability_durscoreema_189d_base_v102_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 189)
    ema = ds.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=252
def f28cms_f28_cro_margin_stability_durscoreema_252d_base_v103_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    ema = ds.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=378
def f28cms_f28_cro_margin_stability_durscoreema_378d_base_v104_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 378)
    ema = ds.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA durability score x close w=504
def f28cms_f28_cro_margin_stability_durscoreema_504d_base_v105_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    ema = ds.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=5
def f28cms_f28_cro_margin_stability_smfloorxdv_5d_base_v106_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    vm = _mean(closeadj * volume, 5)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=10
def f28cms_f28_cro_margin_stability_smfloorxdv_10d_base_v107_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    vm = _mean(closeadj * volume, 10)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=21
def f28cms_f28_cro_margin_stability_smfloorxdv_21d_base_v108_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    vm = _mean(closeadj * volume, 21)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=42
def f28cms_f28_cro_margin_stability_smfloorxdv_42d_base_v109_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    vm = _mean(closeadj * volume, 42)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=63
def f28cms_f28_cro_margin_stability_smfloorxdv_63d_base_v110_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    vm = _mean(closeadj * volume, 63)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=126
def f28cms_f28_cro_margin_stability_smfloorxdv_126d_base_v111_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 126)
    vm = _mean(closeadj * volume, 126)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=189
def f28cms_f28_cro_margin_stability_smfloorxdv_189d_base_v112_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 189)
    vm = _mean(closeadj * volume, 189)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=252
def f28cms_f28_cro_margin_stability_smfloorxdv_252d_base_v113_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    vm = _mean(closeadj * volume, 252)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=378
def f28cms_f28_cro_margin_stability_smfloorxdv_378d_base_v114_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 378)
    vm = _mean(closeadj * volume, 378)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor x dollar vol mean w=504
def f28cms_f28_cro_margin_stability_smfloorxdv_504d_base_v115_signal(ebitdamargin, closeadj, volume):
    f = _f28_service_margin_floor(ebitdamargin, 504)
    vm = _mean(closeadj * volume, 504)
    result = f * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=5
def f28cms_f28_cro_margin_stability_mstabxdv_5d_base_v116_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 5)
    vm = _mean(closeadj * volume, 5)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=10
def f28cms_f28_cro_margin_stability_mstabxdv_10d_base_v117_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 10)
    vm = _mean(closeadj * volume, 10)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=21
def f28cms_f28_cro_margin_stability_mstabxdv_21d_base_v118_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 21)
    vm = _mean(closeadj * volume, 21)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=42
def f28cms_f28_cro_margin_stability_mstabxdv_42d_base_v119_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 42)
    vm = _mean(closeadj * volume, 42)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=63
def f28cms_f28_cro_margin_stability_mstabxdv_63d_base_v120_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 63)
    vm = _mean(closeadj * volume, 63)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=126
def f28cms_f28_cro_margin_stability_mstabxdv_126d_base_v121_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 126)
    vm = _mean(closeadj * volume, 126)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=189
def f28cms_f28_cro_margin_stability_mstabxdv_189d_base_v122_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 189)
    vm = _mean(closeadj * volume, 189)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=252
def f28cms_f28_cro_margin_stability_mstabxdv_252d_base_v123_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 252)
    vm = _mean(closeadj * volume, 252)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=378
def f28cms_f28_cro_margin_stability_mstabxdv_378d_base_v124_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 378)
    vm = _mean(closeadj * volume, 378)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# margin stab x dollar vol mean w=504
def f28cms_f28_cro_margin_stability_mstabxdv_504d_base_v125_signal(ebitdamargin, closeadj, volume):
    ms = _f28_margin_stability(ebitdamargin, 504)
    vm = _mean(closeadj * volume, 504)
    result = ms * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=5
def f28cms_f28_cro_margin_stability_durscorerk_5d_base_v126_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 5)
    r = ds.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=10
def f28cms_f28_cro_margin_stability_durscorerk_10d_base_v127_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 10)
    r = ds.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=21
def f28cms_f28_cro_margin_stability_durscorerk_21d_base_v128_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    r = ds.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=42
def f28cms_f28_cro_margin_stability_durscorerk_42d_base_v129_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    r = ds.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=63
def f28cms_f28_cro_margin_stability_durscorerk_63d_base_v130_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    r = ds.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=126
def f28cms_f28_cro_margin_stability_durscorerk_126d_base_v131_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    r = ds.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=189
def f28cms_f28_cro_margin_stability_durscorerk_189d_base_v132_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 189)
    r = ds.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=252
def f28cms_f28_cro_margin_stability_durscorerk_252d_base_v133_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    r = ds.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=378
def f28cms_f28_cro_margin_stability_durscorerk_378d_base_v134_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 378)
    r = ds.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# durability score rank x close w=504
def f28cms_f28_cro_margin_stability_durscorerk_504d_base_v135_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    r = ds.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor rank x close w=5
def f28cms_f28_cro_margin_stability_smfloorrk_5d_base_v136_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    r = f.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor rank x close w=10
def f28cms_f28_cro_margin_stability_smfloorrk_10d_base_v137_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    r = f.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor rank x close w=21
def f28cms_f28_cro_margin_stability_smfloorrk_21d_base_v138_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    r = f.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor rank x close w=42
def f28cms_f28_cro_margin_stability_smfloorrk_42d_base_v139_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    r = f.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# service margin floor rank x close w=63
def f28cms_f28_cro_margin_stability_smfloorrk_63d_base_v140_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    r = f.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# margin stability rank x close w=5
def f28cms_f28_cro_margin_stability_mstabrk_5d_base_v141_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 5)
    r = ms.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# margin stability rank x close w=10
def f28cms_f28_cro_margin_stability_mstabrk_10d_base_v142_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 10)
    r = ms.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# margin stability rank x close w=21
def f28cms_f28_cro_margin_stability_mstabrk_21d_base_v143_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    r = ms.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# margin stability rank x close w=42
def f28cms_f28_cro_margin_stability_mstabrk_42d_base_v144_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 42)
    r = ms.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# margin stability rank x close w=63
def f28cms_f28_cro_margin_stability_mstabrk_63d_base_v145_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    r = ms.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# floor x stab combo x close w=5
def f28cms_f28_cro_margin_stability_smfloormstab_5d_base_v146_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 5)
    ms = _f28_margin_stability(ebitdamargin, 5)
    result = (f * ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# floor x stab combo x close w=10
def f28cms_f28_cro_margin_stability_smfloormstab_10d_base_v147_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 10)
    ms = _f28_margin_stability(ebitdamargin, 10)
    result = (f * ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# floor x stab combo x close w=21
def f28cms_f28_cro_margin_stability_smfloormstab_21d_base_v148_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    ms = _f28_margin_stability(ebitdamargin, 21)
    result = (f * ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# floor x stab combo x close w=42
def f28cms_f28_cro_margin_stability_smfloormstab_42d_base_v149_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 42)
    ms = _f28_margin_stability(ebitdamargin, 42)
    result = (f * ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# floor x stab combo x close w=63
def f28cms_f28_cro_margin_stability_smfloormstab_63d_base_v150_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    ms = _f28_margin_stability(ebitdamargin, 63)
    result = (f * ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28cms_f28_cro_margin_stability_smfloorema_5d_base_v076_signal,
    f28cms_f28_cro_margin_stability_smfloorema_10d_base_v077_signal,
    f28cms_f28_cro_margin_stability_smfloorema_21d_base_v078_signal,
    f28cms_f28_cro_margin_stability_smfloorema_42d_base_v079_signal,
    f28cms_f28_cro_margin_stability_smfloorema_63d_base_v080_signal,
    f28cms_f28_cro_margin_stability_smfloorema_126d_base_v081_signal,
    f28cms_f28_cro_margin_stability_smfloorema_189d_base_v082_signal,
    f28cms_f28_cro_margin_stability_smfloorema_252d_base_v083_signal,
    f28cms_f28_cro_margin_stability_smfloorema_378d_base_v084_signal,
    f28cms_f28_cro_margin_stability_smfloorema_504d_base_v085_signal,
    f28cms_f28_cro_margin_stability_mstabema_5d_base_v086_signal,
    f28cms_f28_cro_margin_stability_mstabema_10d_base_v087_signal,
    f28cms_f28_cro_margin_stability_mstabema_21d_base_v088_signal,
    f28cms_f28_cro_margin_stability_mstabema_42d_base_v089_signal,
    f28cms_f28_cro_margin_stability_mstabema_63d_base_v090_signal,
    f28cms_f28_cro_margin_stability_mstabema_126d_base_v091_signal,
    f28cms_f28_cro_margin_stability_mstabema_189d_base_v092_signal,
    f28cms_f28_cro_margin_stability_mstabema_252d_base_v093_signal,
    f28cms_f28_cro_margin_stability_mstabema_378d_base_v094_signal,
    f28cms_f28_cro_margin_stability_mstabema_504d_base_v095_signal,
    f28cms_f28_cro_margin_stability_durscoreema_5d_base_v096_signal,
    f28cms_f28_cro_margin_stability_durscoreema_10d_base_v097_signal,
    f28cms_f28_cro_margin_stability_durscoreema_21d_base_v098_signal,
    f28cms_f28_cro_margin_stability_durscoreema_42d_base_v099_signal,
    f28cms_f28_cro_margin_stability_durscoreema_63d_base_v100_signal,
    f28cms_f28_cro_margin_stability_durscoreema_126d_base_v101_signal,
    f28cms_f28_cro_margin_stability_durscoreema_189d_base_v102_signal,
    f28cms_f28_cro_margin_stability_durscoreema_252d_base_v103_signal,
    f28cms_f28_cro_margin_stability_durscoreema_378d_base_v104_signal,
    f28cms_f28_cro_margin_stability_durscoreema_504d_base_v105_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_5d_base_v106_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_10d_base_v107_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_21d_base_v108_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_42d_base_v109_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_63d_base_v110_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_126d_base_v111_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_189d_base_v112_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_252d_base_v113_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_378d_base_v114_signal,
    f28cms_f28_cro_margin_stability_smfloorxdv_504d_base_v115_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_5d_base_v116_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_10d_base_v117_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_21d_base_v118_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_42d_base_v119_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_63d_base_v120_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_126d_base_v121_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_189d_base_v122_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_252d_base_v123_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_378d_base_v124_signal,
    f28cms_f28_cro_margin_stability_mstabxdv_504d_base_v125_signal,
    f28cms_f28_cro_margin_stability_durscorerk_5d_base_v126_signal,
    f28cms_f28_cro_margin_stability_durscorerk_10d_base_v127_signal,
    f28cms_f28_cro_margin_stability_durscorerk_21d_base_v128_signal,
    f28cms_f28_cro_margin_stability_durscorerk_42d_base_v129_signal,
    f28cms_f28_cro_margin_stability_durscorerk_63d_base_v130_signal,
    f28cms_f28_cro_margin_stability_durscorerk_126d_base_v131_signal,
    f28cms_f28_cro_margin_stability_durscorerk_189d_base_v132_signal,
    f28cms_f28_cro_margin_stability_durscorerk_252d_base_v133_signal,
    f28cms_f28_cro_margin_stability_durscorerk_378d_base_v134_signal,
    f28cms_f28_cro_margin_stability_durscorerk_504d_base_v135_signal,
    f28cms_f28_cro_margin_stability_smfloorrk_5d_base_v136_signal,
    f28cms_f28_cro_margin_stability_smfloorrk_10d_base_v137_signal,
    f28cms_f28_cro_margin_stability_smfloorrk_21d_base_v138_signal,
    f28cms_f28_cro_margin_stability_smfloorrk_42d_base_v139_signal,
    f28cms_f28_cro_margin_stability_smfloorrk_63d_base_v140_signal,
    f28cms_f28_cro_margin_stability_mstabrk_5d_base_v141_signal,
    f28cms_f28_cro_margin_stability_mstabrk_10d_base_v142_signal,
    f28cms_f28_cro_margin_stability_mstabrk_21d_base_v143_signal,
    f28cms_f28_cro_margin_stability_mstabrk_42d_base_v144_signal,
    f28cms_f28_cro_margin_stability_mstabrk_63d_base_v145_signal,
    f28cms_f28_cro_margin_stability_smfloormstab_5d_base_v146_signal,
    f28cms_f28_cro_margin_stability_smfloormstab_10d_base_v147_signal,
    f28cms_f28_cro_margin_stability_smfloormstab_21d_base_v148_signal,
    f28cms_f28_cro_margin_stability_smfloormstab_42d_base_v149_signal,
    f28cms_f28_cro_margin_stability_smfloormstab_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CRO_MARGIN_STABILITY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f28_service_margin_floor", "_f28_margin_stability", "_f28_durability_score",)
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
    print(f"OK f28_cro_margin_stability_base_076_150_claude: {n_features} features pass")
