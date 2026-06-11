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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f22_revenue_drawdown(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - peak) / peak.replace(0, np.nan).abs()


def _f22_revenue_recovery(revenue, w):
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan)
    return (revenue - trough) / trough.abs()


def _f22_resilience_score(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan)
    band = (peak - trough).replace(0, np.nan)
    return (revenue - trough) / band

# ===== features =====

def f22ddr_f22_discretionary_demand_resilience_revdd_5d_base_v001_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_10d_base_v002_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_21d_base_v003_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_42d_base_v004_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_63d_base_v005_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_84d_base_v006_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_126d_base_v007_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_168d_base_v008_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_189d_base_v009_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_252d_base_v010_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_315d_base_v011_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_378d_base_v012_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_504d_base_v013_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_5d_base_v014_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_10d_base_v015_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_21d_base_v016_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_42d_base_v017_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_63d_base_v018_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_84d_base_v019_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_126d_base_v020_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_168d_base_v021_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_189d_base_v022_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_252d_base_v023_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_315d_base_v024_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_378d_base_v025_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_504d_base_v026_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_5d_base_v027_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_10d_base_v028_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_21d_base_v029_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_42d_base_v030_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_63d_base_v031_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_84d_base_v032_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = _mean(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_126d_base_v033_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_168d_base_v034_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = _mean(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_189d_base_v035_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_252d_base_v036_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_315d_base_v037_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = _mean(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_378d_base_v038_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_504d_base_v039_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_5d_base_v040_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_10d_base_v041_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_21d_base_v042_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_42d_base_v043_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_63d_base_v044_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_84d_base_v045_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_126d_base_v046_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_168d_base_v047_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_189d_base_v048_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_252d_base_v049_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_315d_base_v050_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_378d_base_v051_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_504d_base_v052_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_5d_base_v053_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_10d_base_v054_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_21d_base_v055_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_42d_base_v056_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_63d_base_v057_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_84d_base_v058_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_126d_base_v059_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_168d_base_v060_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_189d_base_v061_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_252d_base_v062_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_315d_base_v063_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_378d_base_v064_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_504d_base_v065_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_5d_base_v066_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_10d_base_v067_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_21d_base_v068_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_42d_base_v069_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_63d_base_v070_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_84d_base_v071_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_126d_base_v072_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_168d_base_v073_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_189d_base_v074_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_252d_base_v075_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ddr_f22_discretionary_demand_resilience_revdd_5d_base_v001_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_10d_base_v002_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_21d_base_v003_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_42d_base_v004_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_63d_base_v005_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_84d_base_v006_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_126d_base_v007_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_168d_base_v008_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_189d_base_v009_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_252d_base_v010_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_315d_base_v011_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_378d_base_v012_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_504d_base_v013_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_5d_base_v014_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_10d_base_v015_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_21d_base_v016_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_42d_base_v017_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_63d_base_v018_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_84d_base_v019_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_126d_base_v020_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_168d_base_v021_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_189d_base_v022_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_252d_base_v023_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_315d_base_v024_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_378d_base_v025_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_504d_base_v026_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_5d_base_v027_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_10d_base_v028_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_21d_base_v029_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_42d_base_v030_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_63d_base_v031_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_84d_base_v032_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_126d_base_v033_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_168d_base_v034_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_189d_base_v035_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_252d_base_v036_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_315d_base_v037_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_378d_base_v038_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_504d_base_v039_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_5d_base_v040_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_10d_base_v041_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_21d_base_v042_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_42d_base_v043_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_63d_base_v044_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_84d_base_v045_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_126d_base_v046_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_168d_base_v047_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_189d_base_v048_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_252d_base_v049_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_315d_base_v050_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_378d_base_v051_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_504d_base_v052_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_5d_base_v053_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_10d_base_v054_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_21d_base_v055_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_42d_base_v056_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_63d_base_v057_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_84d_base_v058_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_126d_base_v059_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_168d_base_v060_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_189d_base_v061_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_252d_base_v062_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_315d_base_v063_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_378d_base_v064_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_504d_base_v065_signal,
    f22ddr_f22_discretionary_demand_resilience_res_5d_base_v066_signal,
    f22ddr_f22_discretionary_demand_resilience_res_10d_base_v067_signal,
    f22ddr_f22_discretionary_demand_resilience_res_21d_base_v068_signal,
    f22ddr_f22_discretionary_demand_resilience_res_42d_base_v069_signal,
    f22ddr_f22_discretionary_demand_resilience_res_63d_base_v070_signal,
    f22ddr_f22_discretionary_demand_resilience_res_84d_base_v071_signal,
    f22ddr_f22_discretionary_demand_resilience_res_126d_base_v072_signal,
    f22ddr_f22_discretionary_demand_resilience_res_168d_base_v073_signal,
    f22ddr_f22_discretionary_demand_resilience_res_189d_base_v074_signal,
    f22ddr_f22_discretionary_demand_resilience_res_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DISCRETIONARY_DEMAND_RESILIENCE_REGISTRY_001_075 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "revenue": revenue,
        "closeadj": closeadj,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_revenue_drawdown", "_f22_revenue_recovery", "_f22_resilience_score",)
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
    print(f"OK f22_discretionary_demand_resilience_base_001_075_claude: {n_features} features pass")
