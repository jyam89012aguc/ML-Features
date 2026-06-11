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
def _f26_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f26_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f26_backlog_acceleration(deferredrev, w):
    g1 = deferredrev.pct_change(periods=w)
    g2 = deferredrev.pct_change(periods=w).shift(w)
    return g1 - g2


# EMA backlog growth x close w=5
def f26cbg_f26_cro_backlog_growth_blggrowthema_5d_base_v076_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    ema = g.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=10
def f26cbg_f26_cro_backlog_growth_blggrowthema_10d_base_v077_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    ema = g.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=21
def f26cbg_f26_cro_backlog_growth_blggrowthema_21d_base_v078_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    ema = g.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=42
def f26cbg_f26_cro_backlog_growth_blggrowthema_42d_base_v079_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    ema = g.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=63
def f26cbg_f26_cro_backlog_growth_blggrowthema_63d_base_v080_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    ema = g.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=126
def f26cbg_f26_cro_backlog_growth_blggrowthema_126d_base_v081_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 126)
    ema = g.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=189
def f26cbg_f26_cro_backlog_growth_blggrowthema_189d_base_v082_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 189)
    ema = g.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=252
def f26cbg_f26_cro_backlog_growth_blggrowthema_252d_base_v083_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    ema = g.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=378
def f26cbg_f26_cro_backlog_growth_blggrowthema_378d_base_v084_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 378)
    ema = g.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog growth x close w=504
def f26cbg_f26_cro_backlog_growth_blggrowthema_504d_base_v085_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 504)
    ema = g.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=5
def f26cbg_f26_cro_backlog_growth_lblgtorev_5d_base_v086_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(5, min_periods=max(1, 5 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=10
def f26cbg_f26_cro_backlog_growth_lblgtorev_10d_base_v087_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(10, min_periods=max(1, 10 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=21
def f26cbg_f26_cro_backlog_growth_lblgtorev_21d_base_v088_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(21, min_periods=max(1, 21 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=42
def f26cbg_f26_cro_backlog_growth_lblgtorev_42d_base_v089_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(42, min_periods=max(1, 42 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=63
def f26cbg_f26_cro_backlog_growth_lblgtorev_63d_base_v090_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(63, min_periods=max(1, 63 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=126
def f26cbg_f26_cro_backlog_growth_lblgtorev_126d_base_v091_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(126, min_periods=max(1, 126 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=189
def f26cbg_f26_cro_backlog_growth_lblgtorev_189d_base_v092_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(189, min_periods=max(1, 189 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=252
def f26cbg_f26_cro_backlog_growth_lblgtorev_252d_base_v093_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(252, min_periods=max(1, 252 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=378
def f26cbg_f26_cro_backlog_growth_lblgtorev_378d_base_v094_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(378, min_periods=max(1, 378 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log backlog/rev mean x close w=504
def f26cbg_f26_cro_backlog_growth_lblgtorev_504d_base_v095_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue).abs()
    lbr = np.log(br.rolling(504, min_periods=max(1, 504 // 2)).mean().replace(0, np.nan))
    result = lbr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=5
def f26cbg_f26_cro_backlog_growth_blgaccelema_5d_base_v096_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 5)
    ema = a.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=10
def f26cbg_f26_cro_backlog_growth_blgaccelema_10d_base_v097_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 10)
    ema = a.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=21
def f26cbg_f26_cro_backlog_growth_blgaccelema_21d_base_v098_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    ema = a.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=42
def f26cbg_f26_cro_backlog_growth_blgaccelema_42d_base_v099_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 42)
    ema = a.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=63
def f26cbg_f26_cro_backlog_growth_blgaccelema_63d_base_v100_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    ema = a.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=126
def f26cbg_f26_cro_backlog_growth_blgaccelema_126d_base_v101_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 126)
    ema = a.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=189
def f26cbg_f26_cro_backlog_growth_blgaccelema_189d_base_v102_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 189)
    ema = a.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=252
def f26cbg_f26_cro_backlog_growth_blgaccelema_252d_base_v103_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    ema = a.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=378
def f26cbg_f26_cro_backlog_growth_blgaccelema_378d_base_v104_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 378)
    ema = a.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA backlog accel x close w=504
def f26cbg_f26_cro_backlog_growth_blgaccelema_504d_base_v105_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 504)
    ema = a.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=5
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_5d_base_v106_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 5)
    vm = _mean(closeadj * volume, 5)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=10
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_10d_base_v107_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 10)
    vm = _mean(closeadj * volume, 10)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_21d_base_v108_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 21)
    vm = _mean(closeadj * volume, 21)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=42
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_42d_base_v109_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 42)
    vm = _mean(closeadj * volume, 42)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_63d_base_v110_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 63)
    vm = _mean(closeadj * volume, 63)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=126
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_126d_base_v111_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 126)
    vm = _mean(closeadj * volume, 126)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=189
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_189d_base_v112_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 189)
    vm = _mean(closeadj * volume, 189)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_252d_base_v113_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 252)
    vm = _mean(closeadj * volume, 252)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=378
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_378d_base_v114_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 378)
    vm = _mean(closeadj * volume, 378)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth x dollar volume mean w=504
def f26cbg_f26_cro_backlog_growth_blggrowthxdv_504d_base_v115_signal(deferredrev, closeadj, volume):
    g = _f26_backlog_growth(deferredrev, 504)
    vm = _mean(closeadj * volume, 504)
    result = g * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=5
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_5d_base_v116_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 5)
    result = br.rolling(5, min_periods=max(1, 5 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=10
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_10d_base_v117_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 10)
    result = br.rolling(10, min_periods=max(1, 10 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=21
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_21d_base_v118_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 21)
    result = br.rolling(21, min_periods=max(1, 21 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=42
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_42d_base_v119_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 42)
    result = br.rolling(42, min_periods=max(1, 42 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=63
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_63d_base_v120_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 63)
    result = br.rolling(63, min_periods=max(1, 63 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=126
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_126d_base_v121_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 126)
    result = br.rolling(126, min_periods=max(1, 126 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=189
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_189d_base_v122_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 189)
    result = br.rolling(189, min_periods=max(1, 189 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=252
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_252d_base_v123_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 252)
    result = br.rolling(252, min_periods=max(1, 252 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=378
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_378d_base_v124_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 378)
    result = br.rolling(378, min_periods=max(1, 378 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog/rev x dollar volume mean w=504
def f26cbg_f26_cro_backlog_growth_blgtorevxdv_504d_base_v125_signal(deferredrev, revenue, closeadj, volume):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    vm = _mean(closeadj * volume, 504)
    result = br.rolling(504, min_periods=max(1, 504 // 2)).mean() * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=5
def f26cbg_f26_cro_backlog_growth_blggrowthrk_5d_base_v126_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    r = g.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=10
def f26cbg_f26_cro_backlog_growth_blggrowthrk_10d_base_v127_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    r = g.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=21
def f26cbg_f26_cro_backlog_growth_blggrowthrk_21d_base_v128_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    r = g.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=42
def f26cbg_f26_cro_backlog_growth_blggrowthrk_42d_base_v129_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    r = g.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=63
def f26cbg_f26_cro_backlog_growth_blggrowthrk_63d_base_v130_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    r = g.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=126
def f26cbg_f26_cro_backlog_growth_blggrowthrk_126d_base_v131_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 126)
    r = g.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=189
def f26cbg_f26_cro_backlog_growth_blggrowthrk_189d_base_v132_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 189)
    r = g.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=252
def f26cbg_f26_cro_backlog_growth_blggrowthrk_252d_base_v133_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    r = g.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=378
def f26cbg_f26_cro_backlog_growth_blggrowthrk_378d_base_v134_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 378)
    r = g.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth quantile rank x close w=504
def f26cbg_f26_cro_backlog_growth_blggrowthrk_504d_base_v135_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 504)
    r = g.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign backlog growth x close w=5
def f26cbg_f26_cro_backlog_growth_blggrowthsgn_5d_base_v136_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    sgn = np.sign(g.rolling(5, min_periods=max(1, 5 // 2)).mean())
    result = sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign backlog growth x close w=10
def f26cbg_f26_cro_backlog_growth_blggrowthsgn_10d_base_v137_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    sgn = np.sign(g.rolling(10, min_periods=max(1, 10 // 2)).mean())
    result = sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign backlog growth x close w=21
def f26cbg_f26_cro_backlog_growth_blggrowthsgn_21d_base_v138_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    sgn = np.sign(g.rolling(21, min_periods=max(1, 21 // 2)).mean())
    result = sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign backlog growth x close w=42
def f26cbg_f26_cro_backlog_growth_blggrowthsgn_42d_base_v139_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    sgn = np.sign(g.rolling(42, min_periods=max(1, 42 // 2)).mean())
    result = sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign backlog growth x close w=63
def f26cbg_f26_cro_backlog_growth_blggrowthsgn_63d_base_v140_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    sgn = np.sign(g.rolling(63, min_periods=max(1, 63 // 2)).mean())
    result = sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth minus br change x close w=5
def f26cbg_f26_cro_backlog_growth_blgcombo_5d_base_v141_signal(deferredrev, revenue, closeadj):
    g = _f26_backlog_growth(deferredrev, 5)
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    brc = br.diff(periods=5)
    result = (g - brc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth minus br change x close w=10
def f26cbg_f26_cro_backlog_growth_blgcombo_10d_base_v142_signal(deferredrev, revenue, closeadj):
    g = _f26_backlog_growth(deferredrev, 10)
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    brc = br.diff(periods=10)
    result = (g - brc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth minus br change x close w=21
def f26cbg_f26_cro_backlog_growth_blgcombo_21d_base_v143_signal(deferredrev, revenue, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    brc = br.diff(periods=21)
    result = (g - brc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth minus br change x close w=42
def f26cbg_f26_cro_backlog_growth_blgcombo_42d_base_v144_signal(deferredrev, revenue, closeadj):
    g = _f26_backlog_growth(deferredrev, 42)
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    brc = br.diff(periods=42)
    result = (g - brc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog growth minus br change x close w=63
def f26cbg_f26_cro_backlog_growth_blgcombo_63d_base_v145_signal(deferredrev, revenue, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    brc = br.diff(periods=63)
    result = (g - brc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog accel quantile rank x close w=5
def f26cbg_f26_cro_backlog_growth_blgaccelrk_5d_base_v146_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 5)
    r = a.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog accel quantile rank x close w=10
def f26cbg_f26_cro_backlog_growth_blgaccelrk_10d_base_v147_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 10)
    r = a.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog accel quantile rank x close w=21
def f26cbg_f26_cro_backlog_growth_blgaccelrk_21d_base_v148_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    r = a.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog accel quantile rank x close w=42
def f26cbg_f26_cro_backlog_growth_blgaccelrk_42d_base_v149_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 42)
    r = a.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# backlog accel quantile rank x close w=63
def f26cbg_f26_cro_backlog_growth_blgaccelrk_63d_base_v150_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    r = a.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f26cbg_f26_cro_backlog_growth_blggrowthema_5d_base_v076_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_10d_base_v077_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_21d_base_v078_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_42d_base_v079_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_63d_base_v080_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_126d_base_v081_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_189d_base_v082_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_252d_base_v083_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_378d_base_v084_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthema_504d_base_v085_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_5d_base_v086_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_10d_base_v087_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_21d_base_v088_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_42d_base_v089_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_63d_base_v090_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_126d_base_v091_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_189d_base_v092_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_252d_base_v093_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_378d_base_v094_signal,
    f26cbg_f26_cro_backlog_growth_lblgtorev_504d_base_v095_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_5d_base_v096_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_10d_base_v097_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_21d_base_v098_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_42d_base_v099_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_63d_base_v100_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_126d_base_v101_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_189d_base_v102_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_252d_base_v103_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_378d_base_v104_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelema_504d_base_v105_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_5d_base_v106_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_10d_base_v107_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_21d_base_v108_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_42d_base_v109_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_63d_base_v110_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_126d_base_v111_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_189d_base_v112_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_252d_base_v113_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_378d_base_v114_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxdv_504d_base_v115_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_5d_base_v116_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_10d_base_v117_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_21d_base_v118_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_42d_base_v119_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_63d_base_v120_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_126d_base_v121_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_189d_base_v122_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_252d_base_v123_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_378d_base_v124_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevxdv_504d_base_v125_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_5d_base_v126_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_10d_base_v127_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_21d_base_v128_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_42d_base_v129_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_63d_base_v130_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_126d_base_v131_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_189d_base_v132_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_252d_base_v133_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_378d_base_v134_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthrk_504d_base_v135_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthsgn_5d_base_v136_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthsgn_10d_base_v137_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthsgn_21d_base_v138_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthsgn_42d_base_v139_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthsgn_63d_base_v140_signal,
    f26cbg_f26_cro_backlog_growth_blgcombo_5d_base_v141_signal,
    f26cbg_f26_cro_backlog_growth_blgcombo_10d_base_v142_signal,
    f26cbg_f26_cro_backlog_growth_blgcombo_21d_base_v143_signal,
    f26cbg_f26_cro_backlog_growth_blgcombo_42d_base_v144_signal,
    f26cbg_f26_cro_backlog_growth_blgcombo_63d_base_v145_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelrk_5d_base_v146_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelrk_10d_base_v147_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelrk_21d_base_v148_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelrk_42d_base_v149_signal,
    f26cbg_f26_cro_backlog_growth_blgaccelrk_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_CRO_BACKLOG_GROWTH_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f26_backlog_growth", "_f26_backlog_to_revenue", "_f26_backlog_acceleration",)
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
    print(f"OK f26_cro_backlog_growth_base_076_150_claude: {n_features} features pass")
