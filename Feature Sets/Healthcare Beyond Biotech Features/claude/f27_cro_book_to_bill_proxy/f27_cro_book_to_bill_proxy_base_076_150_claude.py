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
def _f27_revenue_accel(revenue, w):
    g1 = revenue.pct_change(periods=w)
    g2 = revenue.pct_change(periods=w).shift(w)
    return g1 - g2


def _f27_book_to_bill(revenue, deferredrev, w):
    backlog_chg = deferredrev.diff(periods=w)
    rev_chg = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (backlog_chg + rev_chg) / rev_chg.replace(0, np.nan)


def _f27_bill_growth_signature(revenue, w):
    g = revenue.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


# EMA revenue accel x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_5d_base_v076_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 5)
    ema = a.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_10d_base_v077_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 10)
    ema = a.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_21d_base_v078_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    ema = a.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_42d_base_v079_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 42)
    ema = a.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_63d_base_v080_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    ema = a.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=126
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_126d_base_v081_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 126)
    ema = a.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=189
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_189d_base_v082_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 189)
    ema = a.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_252d_base_v083_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    ema = a.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=378
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_378d_base_v084_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 378)
    ema = a.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA revenue accel x close w=504
def f27cbb_f27_cro_book_to_bill_proxy_revaccelema_504d_base_v085_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 504)
    ema = a.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_btbema_5d_base_v086_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    ema = btb.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_btbema_10d_base_v087_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    ema = btb.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_btbema_21d_base_v088_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    ema = btb.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbema_42d_base_v089_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    ema = btb.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_btbema_63d_base_v090_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    ema = btb.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbema_126d_base_v091_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    ema = btb.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=189
def f27cbb_f27_cro_book_to_bill_proxy_btbema_189d_base_v092_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 189)
    ema = btb.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=252
def f27cbb_f27_cro_book_to_bill_proxy_btbema_252d_base_v093_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    ema = btb.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=378
def f27cbb_f27_cro_book_to_bill_proxy_btbema_378d_base_v094_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 378)
    ema = btb.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA book-to-bill x close w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbema_504d_base_v095_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    ema = btb.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_5d_base_v096_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 5)
    ema = bg.ewm(span=5, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_10d_base_v097_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 10)
    ema = bg.ewm(span=10, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_21d_base_v098_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    ema = bg.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_42d_base_v099_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 42)
    ema = bg.ewm(span=42, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_63d_base_v100_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    ema = bg.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=126
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_126d_base_v101_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 126)
    ema = bg.ewm(span=126, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=189
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_189d_base_v102_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 189)
    ema = bg.ewm(span=189, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=252
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_252d_base_v103_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    ema = bg.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=378
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_378d_base_v104_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 378)
    ema = bg.ewm(span=378, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# EMA bill growth x close w=504
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_504d_base_v105_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 504)
    ema = bg.ewm(span=504, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=5
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_5d_base_v106_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 5)
    vm = _mean(closeadj * volume, 5)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=10
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_10d_base_v107_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 10)
    vm = _mean(closeadj * volume, 10)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_21d_base_v108_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 21)
    vm = _mean(closeadj * volume, 21)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=42
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_42d_base_v109_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 42)
    vm = _mean(closeadj * volume, 42)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_63d_base_v110_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 63)
    vm = _mean(closeadj * volume, 63)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=126
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_126d_base_v111_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 126)
    vm = _mean(closeadj * volume, 126)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=189
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_189d_base_v112_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 189)
    vm = _mean(closeadj * volume, 189)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_252d_base_v113_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 252)
    vm = _mean(closeadj * volume, 252)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=378
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_378d_base_v114_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 378)
    vm = _mean(closeadj * volume, 378)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel x dollar vol mean w=504
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_504d_base_v115_signal(revenue, closeadj, volume):
    a = _f27_revenue_accel(revenue, 504)
    vm = _mean(closeadj * volume, 504)
    result = a * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=5
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_5d_base_v116_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    vm = _mean(closeadj * volume, 5)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=10
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_10d_base_v117_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    vm = _mean(closeadj * volume, 10)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=21
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_21d_base_v118_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    vm = _mean(closeadj * volume, 21)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_42d_base_v119_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    vm = _mean(closeadj * volume, 42)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=63
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_63d_base_v120_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    vm = _mean(closeadj * volume, 63)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=126
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_126d_base_v121_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    vm = _mean(closeadj * volume, 126)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=189
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_189d_base_v122_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 189)
    vm = _mean(closeadj * volume, 189)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=252
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_252d_base_v123_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    vm = _mean(closeadj * volume, 252)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=378
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_378d_base_v124_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 378)
    vm = _mean(closeadj * volume, 378)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill x dollar vol mean w=504
def f27cbb_f27_cro_book_to_bill_proxy_btbxdv_504d_base_v125_signal(revenue, deferredrev, closeadj, volume):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    vm = _mean(closeadj * volume, 504)
    result = btb * vm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_5d_base_v126_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 5)
    r = a.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_10d_base_v127_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 10)
    r = a.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_21d_base_v128_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    r = a.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_42d_base_v129_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 42)
    r = a.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_63d_base_v130_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    r = a.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=126
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_126d_base_v131_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 126)
    r = a.rolling(126, min_periods=max(1, 126 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=189
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_189d_base_v132_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 189)
    r = a.rolling(189, min_periods=max(1, 189 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=252
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_252d_base_v133_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    r = a.rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=378
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_378d_base_v134_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 378)
    r = a.rolling(378, min_periods=max(1, 378 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# revenue accel rank x close w=504
def f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_504d_base_v135_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 504)
    r = a.rolling(504, min_periods=max(1, 504 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill rank x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_btbrk_5d_base_v136_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    r = btb.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill rank x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_btbrk_10d_base_v137_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    r = btb.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill rank x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_btbrk_21d_base_v138_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    r = btb.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill rank x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_btbrk_42d_base_v139_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    r = btb.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# book-to-bill rank x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_btbrk_63d_base_v140_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    r = btb.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# bill growth rank x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_5d_base_v141_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 5)
    r = bg.rolling(5, min_periods=max(1, 5 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# bill growth rank x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_10d_base_v142_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 10)
    r = bg.rolling(10, min_periods=max(1, 10 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# bill growth rank x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_21d_base_v143_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    r = bg.rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# bill growth rank x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_42d_base_v144_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 42)
    r = bg.rolling(42, min_periods=max(1, 42 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# bill growth rank x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_63d_base_v145_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    r = bg.rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# avg revenue accel + btb x close w=5
def f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_5d_base_v146_signal(revenue, deferredrev, closeadj):
    a = _f27_revenue_accel(revenue, 5)
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    result = (a + btb) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# avg revenue accel + btb x close w=10
def f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_10d_base_v147_signal(revenue, deferredrev, closeadj):
    a = _f27_revenue_accel(revenue, 10)
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    result = (a + btb) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# avg revenue accel + btb x close w=21
def f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_21d_base_v148_signal(revenue, deferredrev, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    result = (a + btb) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# avg revenue accel + btb x close w=42
def f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_42d_base_v149_signal(revenue, deferredrev, closeadj):
    a = _f27_revenue_accel(revenue, 42)
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    result = (a + btb) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# avg revenue accel + btb x close w=63
def f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_63d_base_v150_signal(revenue, deferredrev, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    result = (a + btb) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_5d_base_v076_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_10d_base_v077_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_21d_base_v078_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_42d_base_v079_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_63d_base_v080_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_126d_base_v081_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_189d_base_v082_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_252d_base_v083_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_378d_base_v084_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelema_504d_base_v085_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_5d_base_v086_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_10d_base_v087_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_21d_base_v088_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_42d_base_v089_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_63d_base_v090_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_126d_base_v091_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_189d_base_v092_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_252d_base_v093_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_378d_base_v094_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbema_504d_base_v095_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_5d_base_v096_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_10d_base_v097_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_21d_base_v098_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_42d_base_v099_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_63d_base_v100_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_126d_base_v101_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_189d_base_v102_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_252d_base_v103_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_378d_base_v104_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthema_504d_base_v105_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_5d_base_v106_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_10d_base_v107_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_21d_base_v108_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_42d_base_v109_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_63d_base_v110_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_126d_base_v111_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_189d_base_v112_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_252d_base_v113_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_378d_base_v114_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxdv_504d_base_v115_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_5d_base_v116_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_10d_base_v117_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_21d_base_v118_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_42d_base_v119_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_63d_base_v120_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_126d_base_v121_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_189d_base_v122_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_252d_base_v123_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_378d_base_v124_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxdv_504d_base_v125_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_5d_base_v126_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_10d_base_v127_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_21d_base_v128_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_42d_base_v129_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_63d_base_v130_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_126d_base_v131_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_189d_base_v132_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_252d_base_v133_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_378d_base_v134_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelrk_504d_base_v135_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbrk_5d_base_v136_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbrk_10d_base_v137_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbrk_21d_base_v138_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbrk_42d_base_v139_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbrk_63d_base_v140_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_5d_base_v141_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_10d_base_v142_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_21d_base_v143_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_42d_base_v144_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthrk_63d_base_v145_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_5d_base_v146_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_10d_base_v147_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_21d_base_v148_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_42d_base_v149_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelbtbavg_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CRO_BOOK_TO_BILL_PROXY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f27_revenue_accel", "_f27_book_to_bill", "_f27_bill_growth_signature",)
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
    print(f"OK f27_cro_book_to_bill_proxy_base_076_150_claude: {n_features} features pass")
