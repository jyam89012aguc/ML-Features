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


# 5d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_base_v001_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 5)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_base_v002_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 10)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_base_v003_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_base_v004_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 42)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_base_v005_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_base_v006_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 126)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_base_v007_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 189)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_252d_base_v008_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_378d_base_v009_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 378)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue accel x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccel_504d_base_v010_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 504)
    result = a * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_5d_base_v011_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_10d_base_v012_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_21d_base_v013_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_42d_base_v014_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_63d_base_v015_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_126d_base_v016_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_189d_base_v017_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 189)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_252d_base_v018_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_378d_base_v019_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 378)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d book-to-bill x close
def f27cbb_f27_cro_book_to_bill_proxy_btb_504d_base_v020_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    result = btb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_base_v021_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 5)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_base_v022_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 10)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_base_v023_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_base_v024_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 42)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_base_v025_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_base_v026_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 126)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_base_v027_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 189)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_252d_base_v028_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_378d_base_v029_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 378)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d bill growth signature x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowth_504d_base_v030_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 504)
    result = bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_5d_base_v031_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 5)
    result = _z(a, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_10d_base_v032_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 10)
    result = _z(a, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_21d_base_v033_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 21)
    result = _z(a, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_42d_base_v034_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 42)
    result = _z(a, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_63d_base_v035_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 63)
    result = _z(a, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_126d_base_v036_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 126)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_189d_base_v037_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 189)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_252d_base_v038_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 252)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_378d_base_v039_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 378)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue accel zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_revaccelz_504d_base_v040_signal(revenue, closeadj):
    a = _f27_revenue_accel(revenue, 504)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_5d_base_v041_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    result = _z(btb, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_10d_base_v042_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    result = _z(btb, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_21d_base_v043_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    result = _z(btb, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_42d_base_v044_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    result = _z(btb, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_63d_base_v045_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    result = _z(btb, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_126d_base_v046_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 126)
    result = _z(btb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_189d_base_v047_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 189)
    result = _z(btb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_252d_base_v048_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 252)
    result = _z(btb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_378d_base_v049_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 378)
    result = _z(btb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d btb zscore x close
def f27cbb_f27_cro_book_to_bill_proxy_btbz_504d_base_v050_signal(revenue, deferredrev, closeadj):
    btb = _f27_book_to_bill(revenue, deferredrev, 504)
    result = _z(btb, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_5d_base_v051_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 5)
    result = bg.rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_10d_base_v052_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 10)
    result = bg.rolling(10, min_periods=max(1, 10 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_21d_base_v053_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    result = bg.rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_42d_base_v054_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 42)
    result = bg.rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_63d_base_v055_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    result = bg.rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_126d_base_v056_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 126)
    result = bg.rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_189d_base_v057_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 189)
    result = bg.rolling(189, min_periods=max(1, 189 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_252d_base_v058_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 252)
    result = bg.rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_378d_base_v059_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 378)
    result = bg.rolling(378, min_periods=max(1, 378 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d bill growth rolling mean x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_504d_base_v060_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 504)
    result = bg.rolling(504, min_periods=max(1, 504 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d rev accel x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_base_v061_signal(revenue):
    a = _f27_revenue_accel(revenue, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d rev accel x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_base_v062_signal(revenue):
    a = _f27_revenue_accel(revenue, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rev accel x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_base_v063_signal(revenue):
    a = _f27_revenue_accel(revenue, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d rev accel x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_base_v064_signal(revenue):
    a = _f27_revenue_accel(revenue, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rev accel x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_base_v065_signal(revenue):
    a = _f27_revenue_accel(revenue, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = a * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d btb x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_base_v066_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = btb * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d btb x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_base_v067_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = btb * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d btb x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_base_v068_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = btb * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d btb x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_base_v069_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = btb * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d btb x revenue mean
def f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_base_v070_signal(revenue, deferredrev):
    btb = _f27_book_to_bill(revenue, deferredrev, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = btb * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d bill growth std x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_5d_base_v071_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 5)
    result = bg.rolling(5, min_periods=max(1, 5 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d bill growth std x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_10d_base_v072_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 10)
    result = bg.rolling(10, min_periods=max(1, 10 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d bill growth std x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_21d_base_v073_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 21)
    result = bg.rolling(21, min_periods=max(1, 21 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d bill growth std x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_42d_base_v074_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 42)
    result = bg.rolling(42, min_periods=max(1, 42 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d bill growth std x close
def f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_63d_base_v075_signal(revenue, closeadj):
    bg = _f27_bill_growth_signature(revenue, 63)
    result = bg.rolling(63, min_periods=max(1, 63 // 2)).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_5d_base_v001_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_10d_base_v002_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_21d_base_v003_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_42d_base_v004_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_63d_base_v005_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_126d_base_v006_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_189d_base_v007_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_252d_base_v008_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_378d_base_v009_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccel_504d_base_v010_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_5d_base_v011_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_10d_base_v012_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_21d_base_v013_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_42d_base_v014_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_63d_base_v015_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_126d_base_v016_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_189d_base_v017_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_252d_base_v018_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_378d_base_v019_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btb_504d_base_v020_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_5d_base_v021_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_10d_base_v022_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_21d_base_v023_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_42d_base_v024_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_63d_base_v025_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_126d_base_v026_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_189d_base_v027_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_252d_base_v028_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_378d_base_v029_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowth_504d_base_v030_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_5d_base_v031_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_10d_base_v032_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_21d_base_v033_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_42d_base_v034_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_63d_base_v035_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_126d_base_v036_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_189d_base_v037_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_252d_base_v038_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_378d_base_v039_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelz_504d_base_v040_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_5d_base_v041_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_10d_base_v042_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_21d_base_v043_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_42d_base_v044_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_63d_base_v045_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_126d_base_v046_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_189d_base_v047_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_252d_base_v048_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_378d_base_v049_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbz_504d_base_v050_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_5d_base_v051_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_10d_base_v052_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_21d_base_v053_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_42d_base_v054_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_63d_base_v055_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_126d_base_v056_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_189d_base_v057_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_252d_base_v058_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_378d_base_v059_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthm_504d_base_v060_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_5d_base_v061_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_10d_base_v062_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_21d_base_v063_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_42d_base_v064_signal,
    f27cbb_f27_cro_book_to_bill_proxy_revaccelxrev_63d_base_v065_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_5d_base_v066_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_10d_base_v067_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_21d_base_v068_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_42d_base_v069_signal,
    f27cbb_f27_cro_book_to_bill_proxy_btbxrev_63d_base_v070_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_5d_base_v071_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_10d_base_v072_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_21d_base_v073_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_42d_base_v074_signal,
    f27cbb_f27_cro_book_to_bill_proxy_billgrowthstd_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CRO_BOOK_TO_BILL_PROXY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f27_cro_book_to_bill_proxy_base_001_075_claude: {n_features} features pass")
