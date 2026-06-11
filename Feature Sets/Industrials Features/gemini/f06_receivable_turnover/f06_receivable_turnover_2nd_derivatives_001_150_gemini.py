import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f06_receivable_turnover_receivables_slope_pct_5d_v001_signal(receivables):
    res = _slope_pct(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_5d_v003_signal(cashneq):
    res = _slope_pct(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_5d_v004_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_5d_v005_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_10d_v006_signal(receivables):
    res = _slope_pct(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_10d_v007_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_10d_v008_signal(cashneq):
    res = _slope_pct(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_10d_v009_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_10d_v010_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_21d_v011_signal(receivables):
    res = _slope_pct(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_21d_v012_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_21d_v013_signal(cashneq):
    res = _slope_pct(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_21d_v014_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_21d_v015_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_42d_v016_signal(receivables):
    res = _slope_pct(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_42d_v017_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_42d_v018_signal(cashneq):
    res = _slope_pct(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_42d_v019_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_42d_v020_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_63d_v021_signal(receivables):
    res = _slope_pct(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_63d_v022_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_63d_v023_signal(cashneq):
    res = _slope_pct(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_63d_v024_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_63d_v025_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_126d_v026_signal(receivables):
    res = _slope_pct(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_126d_v027_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_126d_v028_signal(cashneq):
    res = _slope_pct(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_126d_v029_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_126d_v030_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_252d_v031_signal(receivables):
    res = _slope_pct(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_252d_v032_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_252d_v033_signal(cashneq):
    res = _slope_pct(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_252d_v034_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_252d_v035_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_504d_v036_signal(receivables):
    res = _slope_pct(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_504d_v037_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_504d_v038_signal(cashneq):
    res = _slope_pct(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_504d_v039_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_504d_v040_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_756d_v041_signal(receivables):
    res = _slope_pct(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_756d_v042_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_756d_v043_signal(cashneq):
    res = _slope_pct(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_756d_v044_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_756d_v045_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_1008d_v046_signal(receivables):
    res = _slope_pct(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_1008d_v047_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_1008d_v048_signal(cashneq):
    res = _slope_pct(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_1008d_v049_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_1008d_v050_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_pct_1260d_v051_signal(receivables):
    res = _slope_pct(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_pct_1260d_v052_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_pct_1260d_v053_signal(cashneq):
    res = _slope_pct(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_pct_1260d_v054_signal(receivables, revenue):
    res = _slope_pct(_ratio(receivables, revenue) * 365, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_pct_1260d_v055_signal(cashneq, revenue):
    res = _slope_pct(_ratio(cashneq, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_5d_v056_signal(receivables):
    res = _jerk(receivables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_5d_v057_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_5d_v058_signal(cashneq):
    res = _jerk(cashneq, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_5d_v059_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_5d_v060_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_10d_v061_signal(receivables):
    res = _jerk(receivables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_10d_v062_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_10d_v063_signal(cashneq):
    res = _jerk(cashneq, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_10d_v064_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_10d_v065_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_21d_v066_signal(receivables):
    res = _jerk(receivables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_21d_v067_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_21d_v068_signal(cashneq):
    res = _jerk(cashneq, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_21d_v069_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_21d_v070_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_42d_v071_signal(receivables):
    res = _jerk(receivables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_42d_v072_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_42d_v073_signal(cashneq):
    res = _jerk(cashneq, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_42d_v074_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_42d_v075_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_63d_v076_signal(receivables):
    res = _jerk(receivables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_63d_v077_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_63d_v078_signal(cashneq):
    res = _jerk(cashneq, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_63d_v079_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_63d_v080_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_126d_v081_signal(receivables):
    res = _jerk(receivables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_126d_v082_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_126d_v083_signal(cashneq):
    res = _jerk(cashneq, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_126d_v084_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_126d_v085_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_252d_v086_signal(receivables):
    res = _jerk(receivables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_252d_v087_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_252d_v088_signal(cashneq):
    res = _jerk(cashneq, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_252d_v089_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_252d_v090_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_504d_v091_signal(receivables):
    res = _jerk(receivables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_504d_v092_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_504d_v093_signal(cashneq):
    res = _jerk(cashneq, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_504d_v094_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_504d_v095_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_756d_v096_signal(receivables):
    res = _jerk(receivables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_756d_v097_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_756d_v098_signal(cashneq):
    res = _jerk(cashneq, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_756d_v099_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_756d_v100_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_1008d_v101_signal(receivables):
    res = _jerk(receivables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_1008d_v102_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_1008d_v103_signal(cashneq):
    res = _jerk(cashneq, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_1008d_v104_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_1008d_v105_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_jerk_1260d_v106_signal(receivables):
    res = _jerk(receivables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_jerk_1260d_v107_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_jerk_1260d_v108_signal(cashneq):
    res = _jerk(cashneq, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_jerk_1260d_v109_signal(receivables, revenue):
    res = _jerk(_ratio(receivables, revenue) * 365, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_jerk_1260d_v110_signal(cashneq, revenue):
    res = _jerk(_ratio(cashneq, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_5d_v111_signal(receivables):
    res = (_slope_pct(receivables, 5).diff(5) / _sma(receivables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_5d_v112_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_5d_v113_signal(cashneq):
    res = (_slope_pct(cashneq, 5).diff(5) / _sma(cashneq.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_5d_v114_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 5).diff(5) / _sma(_ratio(receivables, revenue) * 365.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_5d_v115_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 5).diff(5) / _sma(_ratio(cashneq, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_10d_v116_signal(receivables):
    res = (_slope_pct(receivables, 10).diff(10) / _sma(receivables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_10d_v117_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_10d_v118_signal(cashneq):
    res = (_slope_pct(cashneq, 10).diff(10) / _sma(cashneq.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_10d_v119_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 10).diff(10) / _sma(_ratio(receivables, revenue) * 365.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_10d_v120_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 10).diff(10) / _sma(_ratio(cashneq, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_21d_v121_signal(receivables):
    res = (_slope_pct(receivables, 21).diff(21) / _sma(receivables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_21d_v122_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_21d_v123_signal(cashneq):
    res = (_slope_pct(cashneq, 21).diff(21) / _sma(cashneq.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_21d_v124_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 21).diff(21) / _sma(_ratio(receivables, revenue) * 365.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_21d_v125_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 21).diff(21) / _sma(_ratio(cashneq, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_42d_v126_signal(receivables):
    res = (_slope_pct(receivables, 42).diff(42) / _sma(receivables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_42d_v127_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_42d_v128_signal(cashneq):
    res = (_slope_pct(cashneq, 42).diff(42) / _sma(cashneq.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_42d_v129_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 42).diff(42) / _sma(_ratio(receivables, revenue) * 365.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_42d_v130_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 42).diff(42) / _sma(_ratio(cashneq, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_63d_v131_signal(receivables):
    res = (_slope_pct(receivables, 63).diff(63) / _sma(receivables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_63d_v132_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_63d_v133_signal(cashneq):
    res = (_slope_pct(cashneq, 63).diff(63) / _sma(cashneq.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_63d_v134_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 63).diff(63) / _sma(_ratio(receivables, revenue) * 365.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_63d_v135_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 63).diff(63) / _sma(_ratio(cashneq, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_126d_v136_signal(receivables):
    res = (_slope_pct(receivables, 126).diff(126) / _sma(receivables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_126d_v137_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_126d_v138_signal(cashneq):
    res = (_slope_pct(cashneq, 126).diff(126) / _sma(cashneq.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_126d_v139_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 126).diff(126) / _sma(_ratio(receivables, revenue) * 365.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_126d_v140_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 126).diff(126) / _sma(_ratio(cashneq, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_252d_v141_signal(receivables):
    res = (_slope_pct(receivables, 252).diff(252) / _sma(receivables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_252d_v142_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_252d_v143_signal(cashneq):
    res = (_slope_pct(cashneq, 252).diff(252) / _sma(cashneq.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_252d_v144_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 252).diff(252) / _sma(_ratio(receivables, revenue) * 365.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_252d_v145_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 252).diff(252) / _sma(_ratio(cashneq, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_slope_diff_norm_504d_v146_signal(receivables):
    res = (_slope_pct(receivables, 504).diff(504) / _sma(receivables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_slope_diff_norm_504d_v147_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_slope_diff_norm_504d_v148_signal(cashneq):
    res = (_slope_pct(cashneq, 504).diff(504) / _sma(cashneq.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_slope_diff_norm_504d_v149_signal(receivables, revenue):
    res = (_slope_pct(_ratio(receivables, revenue) * 365, 504).diff(504) / _sma(_ratio(receivables, revenue) * 365.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_slope_diff_norm_504d_v150_signal(cashneq, revenue):
    res = (_slope_pct(_ratio(cashneq, revenue), 504).diff(504) / _sma(_ratio(cashneq, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 06...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        try:
            res = func(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            break
    print("Success.")
