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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f27_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f27_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f27_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d ema(63)-ema(21) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff_21d_base_v001_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(63)-ema(63) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff_63d_base_v002_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(63)-ema(126) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff_126d_base_v003_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff_252d_base_v004_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(63)-ema(504) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff_504d_base_v005_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign(ema63-ema21)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emaxsig_21d_base_v006_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign(ema63-ema63)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emaxsig_63d_base_v007_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sign(ema63-ema126)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emaxsig_126d_base_v008_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign(ema63-ema252)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emaxsig_252d_base_v009_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sign(ema63-ema504)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emaxsig_504d_base_v010_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/rev / median capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq_21d_base_v011_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    result = ratio / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/rev / median capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq_63d_base_v012_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    result = ratio / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/rev / median capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq_126d_base_v013_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    result = ratio / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/rev / median capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq_252d_base_v014_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    result = ratio / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/rev / median capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq_504d_base_v015_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    result = ratio / med.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of fast 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfast_21d_base_v016_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of fast 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfast_63d_base_v017_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of fast 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfast_126d_base_v018_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of fast 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfast_252d_base_v019_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of fast 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfast_504d_base_v020_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of slow 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zslow_21d_base_v021_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of slow 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zslow_63d_base_v022_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of slow 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zslow_126d_base_v023_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of slow 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zslow_252d_base_v024_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of slow 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zslow_504d_base_v025_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fast 21d z sign
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfastdir_21d_base_v026_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = pd.Series(np.sign(z), index=z.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fast 21d z sign
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfastdir_63d_base_v027_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = pd.Series(np.sign(z), index=z.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fast 21d z sign
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfastdir_126d_base_v028_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = pd.Series(np.sign(z), index=z.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fast 21d z sign
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfastdir_252d_base_v029_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = pd.Series(np.sign(z), index=z.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fast 21d z sign
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zfastdir_504d_base_v030_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = pd.Series(np.sign(z), index=z.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d 21d z minus 252d z (regime spread)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread_21d_base_v031_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z1 = _z(ratio, 21)
    z2 = _z(ratio, 252)
    result = z1 - z2
    return result.replace([np.inf, -np.inf], np.nan)


# 63d 21d z minus 252d z (regime spread)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread_63d_base_v032_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z1 = _z(ratio, 21)
    z2 = _z(ratio, 252)
    result = z1 - z2
    return result.replace([np.inf, -np.inf], np.nan)


# 126d 21d z minus 252d z (regime spread)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread_126d_base_v033_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z1 = _z(ratio, 21)
    z2 = _z(ratio, 252)
    result = z1 - z2
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 21d z minus 252d z (regime spread)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread_252d_base_v034_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z1 = _z(ratio, 21)
    z2 = _z(ratio, 252)
    result = z1 - z2
    return result.replace([np.inf, -np.inf], np.nan)


# 504d 21d z minus 252d z (regime spread)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread_504d_base_v035_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z1 = _z(ratio, 21)
    z2 = _z(ratio, 252)
    result = z1 - z2
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration z(21) > 1 (overheat)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durabove1_21d_base_v036_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration z(63) > 1 (overheat)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durabove1_63d_base_v037_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration z(126) > 1 (overheat)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durabove1_126d_base_v038_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration z(252) > 1 (overheat)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durabove1_252d_base_v039_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration z(504) > 1 (overheat)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durabove1_504d_base_v040_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration z(21) < -1 (underspend)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durbelown1_21d_base_v041_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = (z < -1).astype(float).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration z(63) < -1 (underspend)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durbelown1_63d_base_v042_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = (z < -1).astype(float).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration z(126) < -1 (underspend)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durbelown1_126d_base_v043_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = (z < -1).astype(float).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration z(252) < -1 (underspend)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durbelown1_252d_base_v044_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = (z < -1).astype(float).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration z(504) < -1 (underspend)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_durbelown1_504d_base_v045_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = (z < -1).astype(float).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of sign flips of (capex/rev - mean)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips_21d_base_v046_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 21)
    sg = np.sign(d).diff().abs()
    result = sg.rolling(21, min_periods=max(1, 21//2)).sum() / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of sign flips of (capex/rev - mean)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips_63d_base_v047_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    result = sg.rolling(63, min_periods=max(1, 63//2)).sum() / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of sign flips of (capex/rev - mean)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips_126d_base_v048_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 126)
    sg = np.sign(d).diff().abs()
    result = sg.rolling(126, min_periods=max(1, 126//2)).sum() / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of sign flips of (capex/rev - mean)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips_252d_base_v049_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 252)
    sg = np.sign(d).diff().abs()
    result = sg.rolling(252, min_periods=max(1, 252//2)).sum() / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of sign flips of (capex/rev - mean)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips_504d_base_v050_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 504)
    sg = np.sign(d).diff().abs()
    result = sg.rolling(504, min_periods=max(1, 504//2)).sum() / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d phase: above mean AND rising
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup_21d_base_v051_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d phase: above mean AND rising
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup_63d_base_v052_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d phase: above mean AND rising
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup_126d_base_v053_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d phase: above mean AND rising
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup_252d_base_v054_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d phase: above mean AND rising
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup_504d_base_v055_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d phase: below mean AND falling
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn_21d_base_v056_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d phase: below mean AND falling
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn_63d_base_v057_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d phase: below mean AND falling
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn_126d_base_v058_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d phase: below mean AND falling
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn_252d_base_v059_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d phase: below mean AND falling
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn_504d_base_v060_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d phase: above mean AND falling (top)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasetop_21d_base_v061_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = ((ratio > m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d phase: above mean AND falling (top)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasetop_63d_base_v062_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = ((ratio > m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d phase: above mean AND falling (top)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasetop_126d_base_v063_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = ((ratio > m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d phase: above mean AND falling (top)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasetop_252d_base_v064_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = ((ratio > m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d phase: above mean AND falling (top)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasetop_504d_base_v065_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = ((ratio > m) & (ratio.diff() < 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d phase: below mean AND rising (bottom)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasebot_21d_base_v066_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = ((ratio < m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d phase: below mean AND rising (bottom)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasebot_63d_base_v067_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = ((ratio < m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d phase: below mean AND rising (bottom)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasebot_126d_base_v068_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = ((ratio < m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d phase: below mean AND rising (bottom)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasebot_252d_base_v069_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = ((ratio < m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d phase: below mean AND rising (bottom)
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasebot_504d_base_v070_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = ((ratio < m) & (ratio.diff() > 0)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z signal capex/rev cycle
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos_21d_base_v071_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z signal capex/rev cycle
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos_63d_base_v072_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z signal capex/rev cycle
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos_126d_base_v073_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z signal capex/rev cycle
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos_252d_base_v074_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z signal capex/rev cycle
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos_504d_base_v075_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)
