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
def _f29_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f29_revenue_diversification(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return m / (sd.replace(0, np.nan) + 1e-6)


def _f29_concentration_proxy(revenue, w):
    g = revenue.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).std()


# EMA revenue cv x close w=5
def f29ccc_f29_cro_client_concentration_revcvema_5d_base_v076_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 5)
    ema = cv.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=10
def f29ccc_f29_cro_client_concentration_revcvema_10d_base_v077_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 10)
    ema = cv.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=21
def f29ccc_f29_cro_client_concentration_revcvema_21d_base_v078_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    ema = cv.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=42
def f29ccc_f29_cro_client_concentration_revcvema_42d_base_v079_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 42)
    ema = cv.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=63
def f29ccc_f29_cro_client_concentration_revcvema_63d_base_v080_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    ema = cv.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=126
def f29ccc_f29_cro_client_concentration_revcvema_126d_base_v081_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 126)
    ema = cv.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=189
def f29ccc_f29_cro_client_concentration_revcvema_189d_base_v082_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 189)
    ema = cv.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=252
def f29ccc_f29_cro_client_concentration_revcvema_252d_base_v083_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 252)
    ema = cv.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=378
def f29ccc_f29_cro_client_concentration_revcvema_378d_base_v084_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 378)
    ema = cv.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue cv x close w=504
def f29ccc_f29_cro_client_concentration_revcvema_504d_base_v085_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 504)
    ema = cv.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=5
def f29ccc_f29_cro_client_concentration_revdivema_5d_base_v086_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 5)
    ema = d.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=10
def f29ccc_f29_cro_client_concentration_revdivema_10d_base_v087_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 10)
    ema = d.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=21
def f29ccc_f29_cro_client_concentration_revdivema_21d_base_v088_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    ema = d.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=42
def f29ccc_f29_cro_client_concentration_revdivema_42d_base_v089_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 42)
    ema = d.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=63
def f29ccc_f29_cro_client_concentration_revdivema_63d_base_v090_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    ema = d.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=126
def f29ccc_f29_cro_client_concentration_revdivema_126d_base_v091_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 126)
    ema = d.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=189
def f29ccc_f29_cro_client_concentration_revdivema_189d_base_v092_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 189)
    ema = d.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=252
def f29ccc_f29_cro_client_concentration_revdivema_252d_base_v093_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 252)
    ema = d.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=378
def f29ccc_f29_cro_client_concentration_revdivema_378d_base_v094_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 378)
    ema = d.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue diversification x close w=504
def f29ccc_f29_cro_client_concentration_revdivema_504d_base_v095_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 504)
    ema = d.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=5
def f29ccc_f29_cro_client_concentration_conprxema_5d_base_v096_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 5)
    ema = cp.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=10
def f29ccc_f29_cro_client_concentration_conprxema_10d_base_v097_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 10)
    ema = cp.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=21
def f29ccc_f29_cro_client_concentration_conprxema_21d_base_v098_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    ema = cp.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=42
def f29ccc_f29_cro_client_concentration_conprxema_42d_base_v099_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 42)
    ema = cp.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=63
def f29ccc_f29_cro_client_concentration_conprxema_63d_base_v100_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    ema = cp.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=126
def f29ccc_f29_cro_client_concentration_conprxema_126d_base_v101_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 126)
    ema = cp.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=189
def f29ccc_f29_cro_client_concentration_conprxema_189d_base_v102_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 189)
    ema = cp.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=252
def f29ccc_f29_cro_client_concentration_conprxema_252d_base_v103_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    ema = cp.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=378
def f29ccc_f29_cro_client_concentration_conprxema_378d_base_v104_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 378)
    ema = cp.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA concentration proxy x close w=504
def f29ccc_f29_cro_client_concentration_conprxema_504d_base_v105_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 504)
    ema = cp.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=5
def f29ccc_f29_cro_client_concentration_revcvxdv_5d_base_v106_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 5)
    vm = _mean(closeadj * volume, 5)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=10
def f29ccc_f29_cro_client_concentration_revcvxdv_10d_base_v107_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 10)
    vm = _mean(closeadj * volume, 10)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=21
def f29ccc_f29_cro_client_concentration_revcvxdv_21d_base_v108_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 21)
    vm = _mean(closeadj * volume, 21)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=42
def f29ccc_f29_cro_client_concentration_revcvxdv_42d_base_v109_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 42)
    vm = _mean(closeadj * volume, 42)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=63
def f29ccc_f29_cro_client_concentration_revcvxdv_63d_base_v110_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 63)
    vm = _mean(closeadj * volume, 63)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=126
def f29ccc_f29_cro_client_concentration_revcvxdv_126d_base_v111_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 126)
    vm = _mean(closeadj * volume, 126)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=189
def f29ccc_f29_cro_client_concentration_revcvxdv_189d_base_v112_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 189)
    vm = _mean(closeadj * volume, 189)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=252
def f29ccc_f29_cro_client_concentration_revcvxdv_252d_base_v113_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 252)
    vm = _mean(closeadj * volume, 252)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=378
def f29ccc_f29_cro_client_concentration_revcvxdv_378d_base_v114_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 378)
    vm = _mean(closeadj * volume, 378)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv x dollar vol mean w=504
def f29ccc_f29_cro_client_concentration_revcvxdv_504d_base_v115_signal(revenue, closeadj, volume):
    cv = _f29_revenue_cv(revenue, 504)
    vm = _mean(closeadj * volume, 504)
    result = cv * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=5
def f29ccc_f29_cro_client_concentration_revdivxdv_5d_base_v116_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 5)
    vm = _mean(closeadj * volume, 5)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=10
def f29ccc_f29_cro_client_concentration_revdivxdv_10d_base_v117_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 10)
    vm = _mean(closeadj * volume, 10)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=21
def f29ccc_f29_cro_client_concentration_revdivxdv_21d_base_v118_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 21)
    vm = _mean(closeadj * volume, 21)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=42
def f29ccc_f29_cro_client_concentration_revdivxdv_42d_base_v119_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 42)
    vm = _mean(closeadj * volume, 42)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=63
def f29ccc_f29_cro_client_concentration_revdivxdv_63d_base_v120_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 63)
    vm = _mean(closeadj * volume, 63)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=126
def f29ccc_f29_cro_client_concentration_revdivxdv_126d_base_v121_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 126)
    vm = _mean(closeadj * volume, 126)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=189
def f29ccc_f29_cro_client_concentration_revdivxdv_189d_base_v122_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 189)
    vm = _mean(closeadj * volume, 189)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=252
def f29ccc_f29_cro_client_concentration_revdivxdv_252d_base_v123_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 252)
    vm = _mean(closeadj * volume, 252)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=378
def f29ccc_f29_cro_client_concentration_revdivxdv_378d_base_v124_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 378)
    vm = _mean(closeadj * volume, 378)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers x dollar vol mean w=504
def f29ccc_f29_cro_client_concentration_revdivxdv_504d_base_v125_signal(revenue, closeadj, volume):
    d = _f29_revenue_diversification(revenue, 504)
    vm = _mean(closeadj * volume, 504)
    result = d * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=5
def f29ccc_f29_cro_client_concentration_conprxrk_5d_base_v126_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 5)
    r = cp.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=10
def f29ccc_f29_cro_client_concentration_conprxrk_10d_base_v127_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 10)
    r = cp.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=21
def f29ccc_f29_cro_client_concentration_conprxrk_21d_base_v128_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 21)
    r = cp.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=42
def f29ccc_f29_cro_client_concentration_conprxrk_42d_base_v129_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 42)
    r = cp.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=63
def f29ccc_f29_cro_client_concentration_conprxrk_63d_base_v130_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 63)
    r = cp.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=126
def f29ccc_f29_cro_client_concentration_conprxrk_126d_base_v131_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 126)
    r = cp.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=189
def f29ccc_f29_cro_client_concentration_conprxrk_189d_base_v132_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 189)
    r = cp.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=252
def f29ccc_f29_cro_client_concentration_conprxrk_252d_base_v133_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 252)
    r = cp.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=378
def f29ccc_f29_cro_client_concentration_conprxrk_378d_base_v134_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 378)
    r = cp.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# concentration proxy rank x close w=504
def f29ccc_f29_cro_client_concentration_conprxrk_504d_base_v135_signal(revenue, closeadj):
    cp = _f29_concentration_proxy(revenue, 504)
    r = cp.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv rank x close w=5
def f29ccc_f29_cro_client_concentration_revcvrk_5d_base_v136_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 5)
    r = cv.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv rank x close w=10
def f29ccc_f29_cro_client_concentration_revcvrk_10d_base_v137_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 10)
    r = cv.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv rank x close w=21
def f29ccc_f29_cro_client_concentration_revcvrk_21d_base_v138_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    r = cv.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv rank x close w=42
def f29ccc_f29_cro_client_concentration_revcvrk_42d_base_v139_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 42)
    r = cv.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue cv rank x close w=63
def f29ccc_f29_cro_client_concentration_revcvrk_63d_base_v140_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    r = cv.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers rank x close w=5
def f29ccc_f29_cro_client_concentration_revdivrk_5d_base_v141_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 5)
    r = d.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers rank x close w=10
def f29ccc_f29_cro_client_concentration_revdivrk_10d_base_v142_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 10)
    r = d.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers rank x close w=21
def f29ccc_f29_cro_client_concentration_revdivrk_21d_base_v143_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 21)
    r = d.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers rank x close w=42
def f29ccc_f29_cro_client_concentration_revdivrk_42d_base_v144_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 42)
    r = d.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue divers rank x close w=63
def f29ccc_f29_cro_client_concentration_revdivrk_63d_base_v145_signal(revenue, closeadj):
    d = _f29_revenue_diversification(revenue, 63)
    r = d.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# cv minus inv-divers x close w=5
def f29ccc_f29_cro_client_concentration_revcvdivcombo_5d_base_v146_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 5)
    d = _f29_revenue_diversification(revenue, 5)
    result = (cv - 1.0 / (d + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# cv minus inv-divers x close w=10
def f29ccc_f29_cro_client_concentration_revcvdivcombo_10d_base_v147_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 10)
    d = _f29_revenue_diversification(revenue, 10)
    result = (cv - 1.0 / (d + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# cv minus inv-divers x close w=21
def f29ccc_f29_cro_client_concentration_revcvdivcombo_21d_base_v148_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 21)
    d = _f29_revenue_diversification(revenue, 21)
    result = (cv - 1.0 / (d + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# cv minus inv-divers x close w=42
def f29ccc_f29_cro_client_concentration_revcvdivcombo_42d_base_v149_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 42)
    d = _f29_revenue_diversification(revenue, 42)
    result = (cv - 1.0 / (d + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# cv minus inv-divers x close w=63
def f29ccc_f29_cro_client_concentration_revcvdivcombo_63d_base_v150_signal(revenue, closeadj):
    cv = _f29_revenue_cv(revenue, 63)
    d = _f29_revenue_diversification(revenue, 63)
    result = (cv - 1.0 / (d + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f29ccc_f29_cro_client_concentration_revcvema_5d_base_v076_signal,
    f29ccc_f29_cro_client_concentration_revcvema_10d_base_v077_signal,
    f29ccc_f29_cro_client_concentration_revcvema_21d_base_v078_signal,
    f29ccc_f29_cro_client_concentration_revcvema_42d_base_v079_signal,
    f29ccc_f29_cro_client_concentration_revcvema_63d_base_v080_signal,
    f29ccc_f29_cro_client_concentration_revcvema_126d_base_v081_signal,
    f29ccc_f29_cro_client_concentration_revcvema_189d_base_v082_signal,
    f29ccc_f29_cro_client_concentration_revcvema_252d_base_v083_signal,
    f29ccc_f29_cro_client_concentration_revcvema_378d_base_v084_signal,
    f29ccc_f29_cro_client_concentration_revcvema_504d_base_v085_signal,
    f29ccc_f29_cro_client_concentration_revdivema_5d_base_v086_signal,
    f29ccc_f29_cro_client_concentration_revdivema_10d_base_v087_signal,
    f29ccc_f29_cro_client_concentration_revdivema_21d_base_v088_signal,
    f29ccc_f29_cro_client_concentration_revdivema_42d_base_v089_signal,
    f29ccc_f29_cro_client_concentration_revdivema_63d_base_v090_signal,
    f29ccc_f29_cro_client_concentration_revdivema_126d_base_v091_signal,
    f29ccc_f29_cro_client_concentration_revdivema_189d_base_v092_signal,
    f29ccc_f29_cro_client_concentration_revdivema_252d_base_v093_signal,
    f29ccc_f29_cro_client_concentration_revdivema_378d_base_v094_signal,
    f29ccc_f29_cro_client_concentration_revdivema_504d_base_v095_signal,
    f29ccc_f29_cro_client_concentration_conprxema_5d_base_v096_signal,
    f29ccc_f29_cro_client_concentration_conprxema_10d_base_v097_signal,
    f29ccc_f29_cro_client_concentration_conprxema_21d_base_v098_signal,
    f29ccc_f29_cro_client_concentration_conprxema_42d_base_v099_signal,
    f29ccc_f29_cro_client_concentration_conprxema_63d_base_v100_signal,
    f29ccc_f29_cro_client_concentration_conprxema_126d_base_v101_signal,
    f29ccc_f29_cro_client_concentration_conprxema_189d_base_v102_signal,
    f29ccc_f29_cro_client_concentration_conprxema_252d_base_v103_signal,
    f29ccc_f29_cro_client_concentration_conprxema_378d_base_v104_signal,
    f29ccc_f29_cro_client_concentration_conprxema_504d_base_v105_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_5d_base_v106_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_10d_base_v107_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_21d_base_v108_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_42d_base_v109_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_63d_base_v110_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_126d_base_v111_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_189d_base_v112_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_252d_base_v113_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_378d_base_v114_signal,
    f29ccc_f29_cro_client_concentration_revcvxdv_504d_base_v115_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_5d_base_v116_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_10d_base_v117_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_21d_base_v118_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_42d_base_v119_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_63d_base_v120_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_126d_base_v121_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_189d_base_v122_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_252d_base_v123_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_378d_base_v124_signal,
    f29ccc_f29_cro_client_concentration_revdivxdv_504d_base_v125_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_5d_base_v126_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_10d_base_v127_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_21d_base_v128_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_42d_base_v129_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_63d_base_v130_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_126d_base_v131_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_189d_base_v132_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_252d_base_v133_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_378d_base_v134_signal,
    f29ccc_f29_cro_client_concentration_conprxrk_504d_base_v135_signal,
    f29ccc_f29_cro_client_concentration_revcvrk_5d_base_v136_signal,
    f29ccc_f29_cro_client_concentration_revcvrk_10d_base_v137_signal,
    f29ccc_f29_cro_client_concentration_revcvrk_21d_base_v138_signal,
    f29ccc_f29_cro_client_concentration_revcvrk_42d_base_v139_signal,
    f29ccc_f29_cro_client_concentration_revcvrk_63d_base_v140_signal,
    f29ccc_f29_cro_client_concentration_revdivrk_5d_base_v141_signal,
    f29ccc_f29_cro_client_concentration_revdivrk_10d_base_v142_signal,
    f29ccc_f29_cro_client_concentration_revdivrk_21d_base_v143_signal,
    f29ccc_f29_cro_client_concentration_revdivrk_42d_base_v144_signal,
    f29ccc_f29_cro_client_concentration_revdivrk_63d_base_v145_signal,
    f29ccc_f29_cro_client_concentration_revcvdivcombo_5d_base_v146_signal,
    f29ccc_f29_cro_client_concentration_revcvdivcombo_10d_base_v147_signal,
    f29ccc_f29_cro_client_concentration_revcvdivcombo_21d_base_v148_signal,
    f29ccc_f29_cro_client_concentration_revcvdivcombo_42d_base_v149_signal,
    f29ccc_f29_cro_client_concentration_revcvdivcombo_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_CRO_CLIENT_CONCENTRATION_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f29_revenue_cv", "_f29_revenue_diversification", "_f29_concentration_proxy",)
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
    print(f"OK f29_cro_client_concentration_base_076_150_claude: {n_features} features pass")
