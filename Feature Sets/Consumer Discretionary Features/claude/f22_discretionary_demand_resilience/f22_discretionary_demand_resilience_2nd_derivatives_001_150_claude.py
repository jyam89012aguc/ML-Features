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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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

def f22ddr_f22_discretionary_demand_resilience_revdd_5d_sl5_slope_v001_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_10d_sl10_slope_v002_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_21d_sl21_slope_v003_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_42d_sl42_slope_v004_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_63d_sl63_slope_v005_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_84d_sl126_slope_v006_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_126d_sl5_slope_v007_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_168d_sl10_slope_v008_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_189d_sl21_slope_v009_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_252d_sl42_slope_v010_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_315d_sl63_slope_v011_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_378d_sl126_slope_v012_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revdd_504d_sl5_slope_v013_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_5d_sl10_slope_v014_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_10d_sl21_slope_v015_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_21d_sl42_slope_v016_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_42d_sl63_slope_v017_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_63d_sl126_slope_v018_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_84d_sl5_slope_v019_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_126d_sl10_slope_v020_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_168d_sl21_slope_v021_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_189d_sl42_slope_v022_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_252d_sl63_slope_v023_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_315d_sl126_slope_v024_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_378d_sl5_slope_v025_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = base * base.abs() * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddsq_504d_sl10_slope_v026_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = base * base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_5d_sl21_slope_v027_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = _mean(base, 5) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_10d_sl42_slope_v028_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = _mean(base, 10) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_21d_sl63_slope_v029_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = _mean(base, 21) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_42d_sl126_slope_v030_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = _mean(base, 42) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_63d_sl5_slope_v031_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = _mean(base, 63) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_84d_sl10_slope_v032_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = _mean(base, 84) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_126d_sl21_slope_v033_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = _mean(base, 126) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_168d_sl42_slope_v034_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = _mean(base, 168) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_189d_sl63_slope_v035_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = _mean(base, 189) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_252d_sl126_slope_v036_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = _mean(base, 252) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_315d_sl5_slope_v037_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = _mean(base, 315) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_378d_sl10_slope_v038_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = _mean(base, 378) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddmean_504d_sl21_slope_v039_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = _mean(base, 504) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_5d_sl42_slope_v040_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_10d_sl63_slope_v041_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_21d_sl126_slope_v042_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_42d_sl5_slope_v043_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_63d_sl10_slope_v044_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_84d_sl21_slope_v045_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_126d_sl42_slope_v046_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_168d_sl63_slope_v047_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_189d_sl126_slope_v048_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_252d_sl5_slope_v049_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_315d_sl10_slope_v050_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_378d_sl21_slope_v051_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrec_504d_sl42_slope_v052_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_5d_sl63_slope_v053_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = _std(base, 5) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_10d_sl126_slope_v054_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = _std(base, 10) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_21d_sl5_slope_v055_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = _std(base, 21) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_42d_sl10_slope_v056_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = _std(base, 42) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_63d_sl21_slope_v057_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = _std(base, 63) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_84d_sl42_slope_v058_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = _std(base, 84) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_126d_sl63_slope_v059_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = _std(base, 126) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_168d_sl126_slope_v060_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = _std(base, 168) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_189d_sl5_slope_v061_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = _std(base, 189) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_252d_sl10_slope_v062_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = _std(base, 252) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_315d_sl21_slope_v063_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = _std(base, 315) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_378d_sl42_slope_v064_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = _std(base, 378) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecstd_504d_sl63_slope_v065_signal(revenue, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = _std(base, 504) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_5d_sl126_slope_v066_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_10d_sl5_slope_v067_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_21d_sl10_slope_v068_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_42d_sl21_slope_v069_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_63d_sl42_slope_v070_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_84d_sl63_slope_v071_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_126d_sl126_slope_v072_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_168d_sl5_slope_v073_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_189d_sl10_slope_v074_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_252d_sl21_slope_v075_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_315d_sl42_slope_v076_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_378d_sl63_slope_v077_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_res_504d_sl126_slope_v078_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_5d_sl5_slope_v079_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = _ema(base, 5) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_10d_sl10_slope_v080_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = _ema(base, 10) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_21d_sl21_slope_v081_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = _ema(base, 21) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_42d_sl42_slope_v082_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = _ema(base, 42) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_63d_sl63_slope_v083_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = _ema(base, 63) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_84d_sl126_slope_v084_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = _ema(base, 84) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_126d_sl5_slope_v085_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = _ema(base, 126) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_168d_sl10_slope_v086_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = _ema(base, 168) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_189d_sl21_slope_v087_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = _ema(base, 189) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_252d_sl42_slope_v088_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = _ema(base, 252) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_315d_sl63_slope_v089_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = _ema(base, 315) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_378d_sl126_slope_v090_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = _ema(base, 378) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resema_504d_sl5_slope_v091_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = _ema(base, 504) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_5d_sl10_slope_v092_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    eg = ebitda.pct_change(periods=5)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_10d_sl21_slope_v093_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    eg = ebitda.pct_change(periods=10)
    result = base * eg * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_21d_sl42_slope_v094_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    eg = ebitda.pct_change(periods=21)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_42d_sl63_slope_v095_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    eg = ebitda.pct_change(periods=42)
    result = base * eg * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_63d_sl126_slope_v096_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    eg = ebitda.pct_change(periods=63)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_84d_sl5_slope_v097_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    eg = ebitda.pct_change(periods=84)
    result = base * eg * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_126d_sl10_slope_v098_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    eg = ebitda.pct_change(periods=126)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_168d_sl21_slope_v099_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    eg = ebitda.pct_change(periods=168)
    result = base * eg * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_189d_sl42_slope_v100_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    eg = ebitda.pct_change(periods=189)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_252d_sl63_slope_v101_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    eg = ebitda.pct_change(periods=252)
    result = base * eg * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_315d_sl126_slope_v102_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    eg = ebitda.pct_change(periods=315)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_378d_sl5_slope_v103_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    eg = ebitda.pct_change(periods=378)
    result = base * eg * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddxebgr_504d_sl10_slope_v104_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    eg = ebitda.pct_change(periods=504)
    result = base * eg * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_5d_sl21_slope_v105_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 5)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_10d_sl42_slope_v106_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 10)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_21d_sl63_slope_v107_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 21)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_42d_sl126_slope_v108_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 42)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_63d_sl5_slope_v109_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 63)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_84d_sl10_slope_v110_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 84)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_126d_sl21_slope_v111_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 126)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_168d_sl42_slope_v112_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 168)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_189d_sl63_slope_v113_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 189)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_252d_sl126_slope_v114_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 252)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_315d_sl5_slope_v115_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 315)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_378d_sl10_slope_v116_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 378)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxeb_504d_sl21_slope_v117_signal(revenue, ebitda, closeadj):
    base = _f22_resilience_score(revenue, 504)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_5d_sl42_slope_v118_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 5)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_10d_sl63_slope_v119_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 10)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_21d_sl126_slope_v120_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 21)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_42d_sl5_slope_v121_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 42)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_63d_sl10_slope_v122_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 63)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_84d_sl21_slope_v123_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 84)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_126d_sl42_slope_v124_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 126)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_168d_sl63_slope_v125_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 168)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_189d_sl126_slope_v126_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 189)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_252d_sl5_slope_v127_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 252)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_315d_sl10_slope_v128_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 315)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_378d_sl21_slope_v129_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 378)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revrecxeb_504d_sl42_slope_v130_signal(revenue, ebitda, closeadj):
    base = _f22_revenue_recovery(revenue, 504)
    result = base * (ebitda / 1e8) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_5d_sl63_slope_v131_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 5)
    result = _z(base, 5) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_10d_sl126_slope_v132_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 10)
    result = _z(base, 10) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_21d_sl5_slope_v133_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 21)
    result = _z(base, 21) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_42d_sl10_slope_v134_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 42)
    result = _z(base, 42) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_63d_sl21_slope_v135_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 63)
    result = _z(base, 63) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_84d_sl42_slope_v136_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 84)
    result = _z(base, 84) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_126d_sl63_slope_v137_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 126)
    result = _z(base, 126) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_168d_sl126_slope_v138_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 168)
    result = _z(base, 168) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_189d_sl5_slope_v139_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 189)
    result = _z(base, 189) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_252d_sl10_slope_v140_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 252)
    result = _z(base, 252) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_315d_sl21_slope_v141_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 315)
    result = _z(base, 315) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_378d_sl42_slope_v142_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 378)
    result = _z(base, 378) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_revddz_504d_sl63_slope_v143_signal(revenue, closeadj):
    base = _f22_revenue_drawdown(revenue, 504)
    result = _z(base, 504) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_5d_sl126_slope_v144_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 5)
    dd = _f22_revenue_drawdown(revenue, 5)
    result = (base - dd.abs()) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_10d_sl5_slope_v145_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 10)
    dd = _f22_revenue_drawdown(revenue, 10)
    result = (base - dd.abs()) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_21d_sl10_slope_v146_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 21)
    dd = _f22_revenue_drawdown(revenue, 21)
    result = (base - dd.abs()) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_42d_sl21_slope_v147_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 42)
    dd = _f22_revenue_drawdown(revenue, 42)
    result = (base - dd.abs()) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_63d_sl42_slope_v148_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 63)
    dd = _f22_revenue_drawdown(revenue, 63)
    result = (base - dd.abs()) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_84d_sl63_slope_v149_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 84)
    dd = _f22_revenue_drawdown(revenue, 84)
    result = (base - dd.abs()) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22ddr_f22_discretionary_demand_resilience_resxrevdd_126d_sl126_slope_v150_signal(revenue, closeadj):
    base = _f22_resilience_score(revenue, 126)
    dd = _f22_revenue_drawdown(revenue, 126)
    result = (base - dd.abs()) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ddr_f22_discretionary_demand_resilience_revdd_5d_sl5_slope_v001_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_10d_sl10_slope_v002_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_21d_sl21_slope_v003_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_42d_sl42_slope_v004_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_63d_sl63_slope_v005_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_84d_sl126_slope_v006_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_126d_sl5_slope_v007_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_168d_sl10_slope_v008_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_189d_sl21_slope_v009_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_252d_sl42_slope_v010_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_315d_sl63_slope_v011_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_378d_sl126_slope_v012_signal,
    f22ddr_f22_discretionary_demand_resilience_revdd_504d_sl5_slope_v013_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_5d_sl10_slope_v014_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_10d_sl21_slope_v015_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_21d_sl42_slope_v016_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_42d_sl63_slope_v017_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_63d_sl126_slope_v018_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_84d_sl5_slope_v019_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_126d_sl10_slope_v020_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_168d_sl21_slope_v021_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_189d_sl42_slope_v022_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_252d_sl63_slope_v023_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_315d_sl126_slope_v024_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_378d_sl5_slope_v025_signal,
    f22ddr_f22_discretionary_demand_resilience_revddsq_504d_sl10_slope_v026_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_5d_sl21_slope_v027_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_10d_sl42_slope_v028_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_21d_sl63_slope_v029_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_42d_sl126_slope_v030_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_63d_sl5_slope_v031_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_84d_sl10_slope_v032_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_126d_sl21_slope_v033_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_168d_sl42_slope_v034_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_189d_sl63_slope_v035_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_252d_sl126_slope_v036_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_315d_sl5_slope_v037_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_378d_sl10_slope_v038_signal,
    f22ddr_f22_discretionary_demand_resilience_revddmean_504d_sl21_slope_v039_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_5d_sl42_slope_v040_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_10d_sl63_slope_v041_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_21d_sl126_slope_v042_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_42d_sl5_slope_v043_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_63d_sl10_slope_v044_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_84d_sl21_slope_v045_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_126d_sl42_slope_v046_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_168d_sl63_slope_v047_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_189d_sl126_slope_v048_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_252d_sl5_slope_v049_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_315d_sl10_slope_v050_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_378d_sl21_slope_v051_signal,
    f22ddr_f22_discretionary_demand_resilience_revrec_504d_sl42_slope_v052_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_5d_sl63_slope_v053_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_10d_sl126_slope_v054_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_21d_sl5_slope_v055_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_42d_sl10_slope_v056_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_63d_sl21_slope_v057_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_84d_sl42_slope_v058_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_126d_sl63_slope_v059_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_168d_sl126_slope_v060_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_189d_sl5_slope_v061_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_252d_sl10_slope_v062_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_315d_sl21_slope_v063_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_378d_sl42_slope_v064_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecstd_504d_sl63_slope_v065_signal,
    f22ddr_f22_discretionary_demand_resilience_res_5d_sl126_slope_v066_signal,
    f22ddr_f22_discretionary_demand_resilience_res_10d_sl5_slope_v067_signal,
    f22ddr_f22_discretionary_demand_resilience_res_21d_sl10_slope_v068_signal,
    f22ddr_f22_discretionary_demand_resilience_res_42d_sl21_slope_v069_signal,
    f22ddr_f22_discretionary_demand_resilience_res_63d_sl42_slope_v070_signal,
    f22ddr_f22_discretionary_demand_resilience_res_84d_sl63_slope_v071_signal,
    f22ddr_f22_discretionary_demand_resilience_res_126d_sl126_slope_v072_signal,
    f22ddr_f22_discretionary_demand_resilience_res_168d_sl5_slope_v073_signal,
    f22ddr_f22_discretionary_demand_resilience_res_189d_sl10_slope_v074_signal,
    f22ddr_f22_discretionary_demand_resilience_res_252d_sl21_slope_v075_signal,
    f22ddr_f22_discretionary_demand_resilience_res_315d_sl42_slope_v076_signal,
    f22ddr_f22_discretionary_demand_resilience_res_378d_sl63_slope_v077_signal,
    f22ddr_f22_discretionary_demand_resilience_res_504d_sl126_slope_v078_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_5d_sl5_slope_v079_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_10d_sl10_slope_v080_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_21d_sl21_slope_v081_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_42d_sl42_slope_v082_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_63d_sl63_slope_v083_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_84d_sl126_slope_v084_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_126d_sl5_slope_v085_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_168d_sl10_slope_v086_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_189d_sl21_slope_v087_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_252d_sl42_slope_v088_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_315d_sl63_slope_v089_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_378d_sl126_slope_v090_signal,
    f22ddr_f22_discretionary_demand_resilience_resema_504d_sl5_slope_v091_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_5d_sl10_slope_v092_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_10d_sl21_slope_v093_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_21d_sl42_slope_v094_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_42d_sl63_slope_v095_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_63d_sl126_slope_v096_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_84d_sl5_slope_v097_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_126d_sl10_slope_v098_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_168d_sl21_slope_v099_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_189d_sl42_slope_v100_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_252d_sl63_slope_v101_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_315d_sl126_slope_v102_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_378d_sl5_slope_v103_signal,
    f22ddr_f22_discretionary_demand_resilience_revddxebgr_504d_sl10_slope_v104_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_5d_sl21_slope_v105_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_10d_sl42_slope_v106_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_21d_sl63_slope_v107_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_42d_sl126_slope_v108_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_63d_sl5_slope_v109_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_84d_sl10_slope_v110_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_126d_sl21_slope_v111_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_168d_sl42_slope_v112_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_189d_sl63_slope_v113_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_252d_sl126_slope_v114_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_315d_sl5_slope_v115_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_378d_sl10_slope_v116_signal,
    f22ddr_f22_discretionary_demand_resilience_resxeb_504d_sl21_slope_v117_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_5d_sl42_slope_v118_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_10d_sl63_slope_v119_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_21d_sl126_slope_v120_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_42d_sl5_slope_v121_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_63d_sl10_slope_v122_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_84d_sl21_slope_v123_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_126d_sl42_slope_v124_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_168d_sl63_slope_v125_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_189d_sl126_slope_v126_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_252d_sl5_slope_v127_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_315d_sl10_slope_v128_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_378d_sl21_slope_v129_signal,
    f22ddr_f22_discretionary_demand_resilience_revrecxeb_504d_sl42_slope_v130_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_5d_sl63_slope_v131_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_10d_sl126_slope_v132_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_21d_sl5_slope_v133_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_42d_sl10_slope_v134_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_63d_sl21_slope_v135_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_84d_sl42_slope_v136_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_126d_sl63_slope_v137_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_168d_sl126_slope_v138_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_189d_sl5_slope_v139_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_252d_sl10_slope_v140_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_315d_sl21_slope_v141_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_378d_sl42_slope_v142_signal,
    f22ddr_f22_discretionary_demand_resilience_revddz_504d_sl63_slope_v143_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_5d_sl126_slope_v144_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_10d_sl5_slope_v145_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_21d_sl10_slope_v146_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_42d_sl21_slope_v147_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_63d_sl42_slope_v148_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_84d_sl63_slope_v149_signal,
    f22ddr_f22_discretionary_demand_resilience_resxrevdd_126d_sl126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DISCRETIONARY_DEMAND_RESILIENCE_REGISTRY_SLOPE_001_150 = REGISTRY


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
        "ebitda": ebitda,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f22_discretionary_demand_resilience_2nd_derivatives_001_150_claude: {n_features} features pass")
