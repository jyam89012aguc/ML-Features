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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)



# ===== folder domain primitives =====
def _f15_consolidation_premium(marketcap, equity):
    return marketcap / equity.replace(0, np.nan)


def _f15_premium_dynamics(marketcap, equity, w):
    r = marketcap / equity.replace(0, np.nan)
    return r - r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f15_consolidation_signal(pb, ps, w):
    sig = pb * ps
    return sig - sig.rolling(w, min_periods=max(1, w // 2)).mean()



def f15mcp_f15_ma_consolidation_premium_conspre_21d_jw5_jerk_v001_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_21d_jw21_jerk_v002_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_21d_jw63_jerk_v003_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_21d_jw126_jerk_v004_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_21d_jw252_jerk_v005_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_42d_jw5_jerk_v006_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_42d_jw21_jerk_v007_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_42d_jw63_jerk_v008_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_42d_jw126_jerk_v009_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_42d_jw252_jerk_v010_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 42)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_63d_jw5_jerk_v011_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_63d_jw21_jerk_v012_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_63d_jw63_jerk_v013_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_63d_jw126_jerk_v014_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_63d_jw252_jerk_v015_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_126d_jw5_jerk_v016_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_126d_jw21_jerk_v017_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_126d_jw63_jerk_v018_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_126d_jw126_jerk_v019_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_126d_jw252_jerk_v020_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 126)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_252d_jw5_jerk_v021_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_252d_jw21_jerk_v022_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_252d_jw63_jerk_v023_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_252d_jw126_jerk_v024_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_252d_jw252_jerk_v025_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_504d_jw5_jerk_v026_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_504d_jw21_jerk_v027_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 504)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_504d_jw63_jerk_v028_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_504d_jw126_jerk_v029_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 504)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conspre_504d_jw252_jerk_v030_signal(marketcap, equity, closeadj):
    base = _f15_consolidation_premium(marketcap, equity) * _mean(closeadj, 504)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_21d_jw5_jerk_v031_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_21d_jw21_jerk_v032_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_21d_jw63_jerk_v033_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_21d_jw126_jerk_v034_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_21d_jw252_jerk_v035_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_42d_jw5_jerk_v036_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_42d_jw21_jerk_v037_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_42d_jw63_jerk_v038_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_42d_jw126_jerk_v039_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_42d_jw252_jerk_v040_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_63d_jw5_jerk_v041_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_63d_jw21_jerk_v042_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_63d_jw63_jerk_v043_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_63d_jw126_jerk_v044_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_63d_jw252_jerk_v045_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_126d_jw5_jerk_v046_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_126d_jw21_jerk_v047_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_126d_jw63_jerk_v048_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_126d_jw126_jerk_v049_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_126d_jw252_jerk_v050_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_252d_jw5_jerk_v051_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_252d_jw21_jerk_v052_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_252d_jw63_jerk_v053_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_252d_jw126_jerk_v054_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_252d_jw252_jerk_v055_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_504d_jw5_jerk_v056_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_504d_jw21_jerk_v057_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_504d_jw63_jerk_v058_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_504d_jw126_jerk_v059_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predyn_504d_jw252_jerk_v060_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_21d_jw5_jerk_v061_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_21d_jw21_jerk_v062_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_21d_jw63_jerk_v063_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_21d_jw126_jerk_v064_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_21d_jw252_jerk_v065_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_42d_jw5_jerk_v066_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_42d_jw21_jerk_v067_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_42d_jw63_jerk_v068_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_42d_jw126_jerk_v069_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_42d_jw252_jerk_v070_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_63d_jw5_jerk_v071_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_63d_jw21_jerk_v072_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_63d_jw63_jerk_v073_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_63d_jw126_jerk_v074_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_63d_jw252_jerk_v075_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_126d_jw5_jerk_v076_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_126d_jw21_jerk_v077_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_126d_jw63_jerk_v078_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_126d_jw126_jerk_v079_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_126d_jw252_jerk_v080_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_252d_jw5_jerk_v081_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_252d_jw21_jerk_v082_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_252d_jw63_jerk_v083_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_252d_jw126_jerk_v084_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_252d_jw252_jerk_v085_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_504d_jw5_jerk_v086_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_504d_jw21_jerk_v087_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_504d_jw63_jerk_v088_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_504d_jw126_jerk_v089_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssig_504d_jw252_jerk_v090_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw5_jerk_v091_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw21_jerk_v092_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw63_jerk_v093_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw126_jerk_v094_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw252_jerk_v095_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 21).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw5_jerk_v096_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw21_jerk_v097_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw63_jerk_v098_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw126_jerk_v099_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw252_jerk_v100_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 42).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw5_jerk_v101_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw21_jerk_v102_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw63_jerk_v103_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw126_jerk_v104_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw252_jerk_v105_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 63).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw5_jerk_v106_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw21_jerk_v107_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw63_jerk_v108_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw126_jerk_v109_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw252_jerk_v110_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 126).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw5_jerk_v111_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw21_jerk_v112_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw63_jerk_v113_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw126_jerk_v114_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw252_jerk_v115_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 252).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw5_jerk_v116_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw21_jerk_v117_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw63_jerk_v118_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw126_jerk_v119_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw252_jerk_v120_signal(marketcap, equity, closeadj):
    base = _f15_premium_dynamics(marketcap, equity, 504).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw5_jerk_v121_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw21_jerk_v122_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw63_jerk_v123_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw126_jerk_v124_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw252_jerk_v125_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 21).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw5_jerk_v126_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw21_jerk_v127_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw63_jerk_v128_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw126_jerk_v129_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw252_jerk_v130_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 42).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw5_jerk_v131_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw21_jerk_v132_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw63_jerk_v133_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw126_jerk_v134_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw252_jerk_v135_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 63).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw5_jerk_v136_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw21_jerk_v137_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw63_jerk_v138_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw126_jerk_v139_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw252_jerk_v140_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 126).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw5_jerk_v141_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw21_jerk_v142_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw63_jerk_v143_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw126_jerk_v144_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw252_jerk_v145_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 252).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw5_jerk_v146_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504).pow(2.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw21_jerk_v147_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504).pow(2.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw63_jerk_v148_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504).pow(2.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw126_jerk_v149_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504).pow(2.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw252_jerk_v150_signal(pb, ps, closeadj):
    base = _f15_consolidation_signal(pb, ps, 504).pow(2.0) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15mcp_f15_ma_consolidation_premium_conspre_21d_jw5_jerk_v001_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_21d_jw21_jerk_v002_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_21d_jw63_jerk_v003_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_21d_jw126_jerk_v004_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_21d_jw252_jerk_v005_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_42d_jw5_jerk_v006_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_42d_jw21_jerk_v007_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_42d_jw63_jerk_v008_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_42d_jw126_jerk_v009_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_42d_jw252_jerk_v010_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_63d_jw5_jerk_v011_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_63d_jw21_jerk_v012_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_63d_jw63_jerk_v013_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_63d_jw126_jerk_v014_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_63d_jw252_jerk_v015_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_126d_jw5_jerk_v016_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_126d_jw21_jerk_v017_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_126d_jw63_jerk_v018_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_126d_jw126_jerk_v019_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_126d_jw252_jerk_v020_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_252d_jw5_jerk_v021_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_252d_jw21_jerk_v022_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_252d_jw63_jerk_v023_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_252d_jw126_jerk_v024_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_252d_jw252_jerk_v025_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_504d_jw5_jerk_v026_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_504d_jw21_jerk_v027_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_504d_jw63_jerk_v028_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_504d_jw126_jerk_v029_signal,
    f15mcp_f15_ma_consolidation_premium_conspre_504d_jw252_jerk_v030_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_21d_jw5_jerk_v031_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_21d_jw21_jerk_v032_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_21d_jw63_jerk_v033_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_21d_jw126_jerk_v034_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_21d_jw252_jerk_v035_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_42d_jw5_jerk_v036_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_42d_jw21_jerk_v037_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_42d_jw63_jerk_v038_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_42d_jw126_jerk_v039_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_42d_jw252_jerk_v040_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_63d_jw5_jerk_v041_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_63d_jw21_jerk_v042_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_63d_jw63_jerk_v043_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_63d_jw126_jerk_v044_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_63d_jw252_jerk_v045_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_126d_jw5_jerk_v046_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_126d_jw21_jerk_v047_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_126d_jw63_jerk_v048_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_126d_jw126_jerk_v049_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_126d_jw252_jerk_v050_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_252d_jw5_jerk_v051_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_252d_jw21_jerk_v052_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_252d_jw63_jerk_v053_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_252d_jw126_jerk_v054_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_252d_jw252_jerk_v055_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_504d_jw5_jerk_v056_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_504d_jw21_jerk_v057_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_504d_jw63_jerk_v058_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_504d_jw126_jerk_v059_signal,
    f15mcp_f15_ma_consolidation_premium_predyn_504d_jw252_jerk_v060_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_21d_jw5_jerk_v061_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_21d_jw21_jerk_v062_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_21d_jw63_jerk_v063_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_21d_jw126_jerk_v064_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_21d_jw252_jerk_v065_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_42d_jw5_jerk_v066_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_42d_jw21_jerk_v067_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_42d_jw63_jerk_v068_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_42d_jw126_jerk_v069_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_42d_jw252_jerk_v070_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_63d_jw5_jerk_v071_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_63d_jw21_jerk_v072_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_63d_jw63_jerk_v073_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_63d_jw126_jerk_v074_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_63d_jw252_jerk_v075_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_126d_jw5_jerk_v076_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_126d_jw21_jerk_v077_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_126d_jw63_jerk_v078_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_126d_jw126_jerk_v079_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_126d_jw252_jerk_v080_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_252d_jw5_jerk_v081_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_252d_jw21_jerk_v082_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_252d_jw63_jerk_v083_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_252d_jw126_jerk_v084_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_252d_jw252_jerk_v085_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_504d_jw5_jerk_v086_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_504d_jw21_jerk_v087_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_504d_jw63_jerk_v088_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_504d_jw126_jerk_v089_signal,
    f15mcp_f15_ma_consolidation_premium_conssig_504d_jw252_jerk_v090_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw5_jerk_v091_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw21_jerk_v092_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw63_jerk_v093_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw126_jerk_v094_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_21d_jw252_jerk_v095_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw5_jerk_v096_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw21_jerk_v097_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw63_jerk_v098_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw126_jerk_v099_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_42d_jw252_jerk_v100_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw5_jerk_v101_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw21_jerk_v102_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw63_jerk_v103_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw126_jerk_v104_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_63d_jw252_jerk_v105_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw5_jerk_v106_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw21_jerk_v107_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw63_jerk_v108_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw126_jerk_v109_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_126d_jw252_jerk_v110_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw5_jerk_v111_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw21_jerk_v112_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw63_jerk_v113_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw126_jerk_v114_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_252d_jw252_jerk_v115_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw5_jerk_v116_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw21_jerk_v117_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw63_jerk_v118_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw126_jerk_v119_signal,
    f15mcp_f15_ma_consolidation_premium_predynsq_504d_jw252_jerk_v120_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw5_jerk_v121_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw21_jerk_v122_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw63_jerk_v123_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw126_jerk_v124_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_21d_jw252_jerk_v125_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw5_jerk_v126_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw21_jerk_v127_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw63_jerk_v128_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw126_jerk_v129_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_42d_jw252_jerk_v130_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw5_jerk_v131_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw21_jerk_v132_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw63_jerk_v133_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw126_jerk_v134_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_63d_jw252_jerk_v135_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw5_jerk_v136_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw21_jerk_v137_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw63_jerk_v138_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw126_jerk_v139_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_126d_jw252_jerk_v140_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw5_jerk_v141_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw21_jerk_v142_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw63_jerk_v143_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw126_jerk_v144_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_252d_jw252_jerk_v145_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw5_jerk_v146_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw21_jerk_v147_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw63_jerk_v148_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw126_jerk_v149_signal,
    f15mcp_f15_ma_consolidation_premium_conssigsq_504d_jw252_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_MA_CONSOLIDATION_PREMIUM_REGISTRY_JERK_001_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_consolidation_premium", "_f15_premium_dynamics", "_f15_consolidation_signal")
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
    print(f"OK ma_consolidation_premium_3rd_derivatives_001_150_claude: {n_features} features pass")
