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


# 21d ema(21)-ema(21) capex/rev (regime cross)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema_xover_21d_base_v001_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(21)-ema(63) capex/rev (regime cross)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema_xover_63d_base_v002_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(21)-ema(126) capex/rev (regime cross)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema_xover_126d_base_v003_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(21)-ema(252) capex/rev (regime cross)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema_xover_252d_base_v004_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(21)-ema(504) capex/rev (regime cross)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema_xover_504d_base_v005_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of ema(21)-ema(21) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_signxo_21d_base_v006_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of ema(21)-ema(63) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_signxo_63d_base_v007_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sign of ema(21)-ema(126) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_signxo_126d_base_v008_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of ema(21)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_signxo_252d_base_v009_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sign of ema(21)-ema(504) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_signxo_504d_base_v010_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    x = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    result = pd.Series(np.sign(x), index=x.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mask capex/rev above 21d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above_lt_21d_base_v011_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = (ratio > m).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mask capex/rev above 63d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above_lt_63d_base_v012_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = (ratio > m).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mask capex/rev above 126d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above_lt_126d_base_v013_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = (ratio > m).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mask capex/rev above 252d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above_lt_252d_base_v014_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = (ratio > m).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mask capex/rev above 504d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above_lt_504d_base_v015_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = (ratio > m).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mask z(21) capex/rev > 1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_above1_21d_base_v016_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = (z > 1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mask z(63) capex/rev > 1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_above1_63d_base_v017_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = (z > 1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mask z(126) capex/rev > 1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_above1_126d_base_v018_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = (z > 1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mask z(252) capex/rev > 1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_above1_252d_base_v019_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = (z > 1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mask z(504) capex/rev > 1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_above1_504d_base_v020_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = (z > 1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mask z(21) capex/rev < -1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_below_n1_21d_base_v021_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = (z < -1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mask z(63) capex/rev < -1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_below_n1_63d_base_v022_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = (z < -1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mask z(126) capex/rev < -1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_below_n1_126d_base_v023_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = (z < -1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mask z(252) capex/rev < -1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_below_n1_252d_base_v024_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = (z < -1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mask z(504) capex/rev < -1
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_below_n1_504d_base_v025_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = (z < -1).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration above 21d mean (rolling sum)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup_21d_base_v026_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = (ratio > m).astype(float).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration above 63d mean (rolling sum)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup_63d_base_v027_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = (ratio > m).astype(float).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration above 126d mean (rolling sum)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup_126d_base_v028_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = (ratio > m).astype(float).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration above 252d mean (rolling sum)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup_252d_base_v029_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = (ratio > m).astype(float).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration above 504d mean (rolling sum)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup_504d_base_v030_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = (ratio > m).astype(float).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration below 21d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn_21d_base_v031_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = (ratio < m).astype(float).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration below 63d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn_63d_base_v032_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = (ratio < m).astype(float).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration below 126d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn_126d_base_v033_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = (ratio < m).astype(float).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration below 252d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn_252d_base_v034_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = (ratio < m).astype(float).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration below 504d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn_504d_base_v035_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = (ratio < m).astype(float).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/rev minus its 21d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff_21d_base_v036_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/rev minus its 63d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff_63d_base_v037_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/rev minus its 126d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff_126d_base_v038_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/rev minus its 252d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff_252d_base_v039_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/rev minus its 504d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff_504d_base_v040_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/rev divided by its 21d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio_21d_base_v041_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio / _mean(ratio, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/rev divided by its 63d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio_63d_base_v042_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio / _mean(ratio, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/rev divided by its 126d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio_126d_base_v043_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio / _mean(ratio, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/rev divided by its 252d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio_252d_base_v044_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio / _mean(ratio, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/rev divided by its 504d mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio_504d_base_v045_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio / _mean(ratio, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance to 21d peak capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peakdist_21d_base_v046_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 21) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance to 63d peak capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peakdist_63d_base_v047_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 63) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# 126d distance to 126d peak capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peakdist_126d_base_v048_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 126) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance to 252d peak capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peakdist_252d_base_v049_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 252) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distance to 504d peak capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peakdist_504d_base_v050_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 504) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance to 21d trough capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_troughdist_21d_base_v051_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance to 63d trough capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_troughdist_63d_base_v052_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d distance to 126d trough capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_troughdist_126d_base_v053_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance to 252d trough capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_troughdist_252d_base_v054_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d distance to 504d trough capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_troughdist_504d_base_v055_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/rev centered (ratio - midpoint)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered_21d_base_v056_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 21) + _min(ratio, 21))
    result = ratio - mid
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/rev centered (ratio - midpoint)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered_63d_base_v057_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    result = ratio - mid
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/rev centered (ratio - midpoint)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered_126d_base_v058_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 126) + _min(ratio, 126))
    result = ratio - mid
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/rev centered (ratio - midpoint)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered_252d_base_v059_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 252) + _min(ratio, 252))
    result = ratio - mid
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/rev centered (ratio - midpoint)
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered_504d_base_v060_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 504) + _min(ratio, 504))
    result = ratio - mid
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of z(21) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_mean_21d_base_v061_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _mean(z, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of z(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_mean_63d_base_v062_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = _mean(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of z(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_mean_126d_base_v063_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = _mean(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of z(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_mean_252d_base_v064_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _mean(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of z(504) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_mean_504d_base_v065_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = _mean(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of z(21) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_std_21d_base_v066_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = _std(z, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of z(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_std_63d_base_v067_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = _std(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of z(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_std_126d_base_v068_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = _std(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of z(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_std_252d_base_v069_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = _std(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of z(504) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_z_std_504d_base_v070_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = _std(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration-fraction z(21) > 0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hiz_durfrac_21d_base_v071_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 21)
    result = (z > 0).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration-fraction z(63) > 0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hiz_durfrac_63d_base_v072_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    result = (z > 0).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration-fraction z(126) > 0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hiz_durfrac_126d_base_v073_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 126)
    result = (z > 0).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration-fraction z(252) > 0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hiz_durfrac_252d_base_v074_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 252)
    result = (z > 0).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration-fraction z(504) > 0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hiz_durfrac_504d_base_v075_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 504)
    result = (z > 0).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)
