# f20_capital_allocation_snapshot_slope_001_150_gemini.py
import pandas as pd
import numpy as np
import inspect

def _ca_ratio(num, den): 
    return num / den.replace(0, np.nan)

def _ca_zscore(s, w): 
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def _ca_slope(s, w):
    return s.diff(5)

windows = [63, 126, 252, 504, 756, 1260]
def f20_capital_allocation_snapshot_payout_ratio_63d_slope_v001_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(63).sum(), arg_netinc.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_payout_ratio_126d_slope_v002_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(126).sum(), arg_netinc.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_payout_ratio_252d_slope_v003_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(252).sum(), arg_netinc.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_payout_ratio_504d_slope_v004_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(504).sum(), arg_netinc.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_payout_ratio_756d_slope_v005_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(756).sum(), arg_netinc.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_payout_ratio_1260d_slope_v006_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs()), 1260)
def f20_capital_allocation_snapshot_reinvest_rate_63d_slope_v007_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_reinvest_rate_126d_slope_v008_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_reinvest_rate_252d_slope_v009_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_reinvest_rate_504d_slope_v010_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_reinvest_rate_756d_slope_v011_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_reinvest_rate_1260d_slope_v012_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_ratio(arg_capex.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs()), 1260)
def f20_capital_allocation_snapshot_cash_assets_63d_slope_v013_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 63)
def f20_capital_allocation_snapshot_cash_assets_126d_slope_v014_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 126)
def f20_capital_allocation_snapshot_cash_assets_252d_slope_v015_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 252)
def f20_capital_allocation_snapshot_cash_assets_504d_slope_v016_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 504)
def f20_capital_allocation_snapshot_cash_assets_756d_slope_v017_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 756)
def f20_capital_allocation_snapshot_cash_assets_1260d_slope_v018_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_ratio(arg_cashneq, arg_assets), 1260)
def f20_capital_allocation_snapshot_div_rev_63d_slope_v019_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(63).sum(), arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_div_rev_126d_slope_v020_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(126).sum(), arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_div_rev_252d_slope_v021_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(252).sum(), arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_div_rev_504d_slope_v022_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(504).sum(), arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_div_rev_756d_slope_v023_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(756).sum(), arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_div_rev_1260d_slope_v024_signal(arg_dividends, arg_revenue): return _ca_slope(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_capex_rev_63d_slope_v025_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(63).sum(), arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_capex_rev_126d_slope_v026_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(126).sum(), arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_capex_rev_252d_slope_v027_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(252).sum(), arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_capex_rev_504d_slope_v028_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(504).sum(), arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_capex_rev_756d_slope_v029_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(756).sum(), arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_capex_rev_1260d_slope_v030_signal(arg_capex, arg_revenue): return _ca_slope(_ca_ratio(arg_capex.rolling(1260).sum(), arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_buyback_intensity_63d_slope_v031_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(63), arg_shareswa.shift(63)), 63)
def f20_capital_allocation_snapshot_buyback_intensity_126d_slope_v032_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(126), arg_shareswa.shift(126)), 126)
def f20_capital_allocation_snapshot_buyback_intensity_252d_slope_v033_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(252), arg_shareswa.shift(252)), 252)
def f20_capital_allocation_snapshot_buyback_intensity_504d_slope_v034_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(504), arg_shareswa.shift(504)), 504)
def f20_capital_allocation_snapshot_buyback_intensity_756d_slope_v035_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(756), arg_shareswa.shift(756)), 756)
def f20_capital_allocation_snapshot_buyback_intensity_1260d_slope_v036_signal(arg_shareswa): return _ca_slope(_ca_ratio(-arg_shareswa.diff(1260), arg_shareswa.shift(1260)), 1260)
def f20_capital_allocation_snapshot_coverage_ratio_63d_slope_v037_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(63).sum(), arg_dividends.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_coverage_ratio_126d_slope_v038_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(126).sum(), arg_dividends.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_coverage_ratio_252d_slope_v039_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(252).sum(), arg_dividends.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_coverage_ratio_504d_slope_v040_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(504).sum(), arg_dividends.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_coverage_ratio_756d_slope_v041_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(756).sum(), arg_dividends.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_coverage_ratio_1260d_slope_v042_signal(arg_ncfo, arg_dividends): return _ca_slope(_ca_ratio(arg_ncfo.rolling(1260).sum(), arg_dividends.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_63d_slope_v043_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs()), 63), 63)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_126d_slope_v044_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs()), 126), 126)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_252d_slope_v045_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs()), 252), 252)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_504d_slope_v046_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs()), 504), 504)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_756d_slope_v047_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs()), 756), 756)
def f20_capital_allocation_snapshot_reinvest_rate_zscore_1260d_slope_v048_signal(arg_capex, arg_ncfo): return _ca_slope(_ca_zscore(_ca_ratio(arg_capex.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs()), 1260), 1260)
def f20_capital_allocation_snapshot_payout_ratio_zscore_63d_slope_v049_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(63).sum(), arg_netinc.rolling(63).sum().abs()), 63), 63)
def f20_capital_allocation_snapshot_payout_ratio_zscore_126d_slope_v050_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(126).sum(), arg_netinc.rolling(126).sum().abs()), 126), 126)
def f20_capital_allocation_snapshot_payout_ratio_zscore_252d_slope_v051_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(252).sum(), arg_netinc.rolling(252).sum().abs()), 252), 252)
def f20_capital_allocation_snapshot_payout_ratio_zscore_504d_slope_v052_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(504).sum(), arg_netinc.rolling(504).sum().abs()), 504), 504)
def f20_capital_allocation_snapshot_payout_ratio_zscore_756d_slope_v053_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(756).sum(), arg_netinc.rolling(756).sum().abs()), 756), 756)
def f20_capital_allocation_snapshot_payout_ratio_zscore_1260d_slope_v054_signal(arg_dividends, arg_netinc): return _ca_slope(_ca_zscore(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs()), 1260), 1260)
def f20_capital_allocation_snapshot_cash_assets_zscore_63d_slope_v055_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 63), 63)
def f20_capital_allocation_snapshot_cash_assets_zscore_126d_slope_v056_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 126), 126)
def f20_capital_allocation_snapshot_cash_assets_zscore_252d_slope_v057_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 252), 252)
def f20_capital_allocation_snapshot_cash_assets_zscore_504d_slope_v058_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 504), 504)
def f20_capital_allocation_snapshot_cash_assets_zscore_756d_slope_v059_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 756), 756)
def f20_capital_allocation_snapshot_cash_assets_zscore_1260d_slope_v060_signal(arg_cashneq, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_cashneq, arg_assets), 1260), 1260)
def f20_capital_allocation_snapshot_ncfo_assets_63d_slope_v061_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_ncfo_assets_126d_slope_v062_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_ncfo_assets_252d_slope_v063_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_ncfo_assets_504d_slope_v064_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_ncfo_assets_756d_slope_v065_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_ncfo_assets_1260d_slope_v066_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_ratio(arg_ncfo.rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_netinc_assets_63d_slope_v067_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_netinc_assets_126d_slope_v068_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_netinc_assets_252d_slope_v069_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_netinc_assets_504d_slope_v070_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_netinc_assets_756d_slope_v071_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_netinc_assets_1260d_slope_v072_signal(arg_netinc, arg_assets): return _ca_slope(_ca_ratio(arg_netinc.rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_div_ncfo_63d_slope_v073_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(63).sum(), arg_ncfo.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_div_ncfo_126d_slope_v074_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(126).sum(), arg_ncfo.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_div_ncfo_252d_slope_v075_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(252).sum(), arg_ncfo.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_div_ncfo_504d_slope_v076_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(504).sum(), arg_ncfo.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_div_ncfo_756d_slope_v077_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(756).sum(), arg_ncfo.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_div_ncfo_1260d_slope_v078_signal(arg_dividends, arg_ncfo): return _ca_slope(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs()), 1260)
def f20_capital_allocation_snapshot_capex_assets_63d_slope_v079_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_capex_assets_126d_slope_v080_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_capex_assets_252d_slope_v081_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_capex_assets_504d_slope_v082_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_capex_assets_756d_slope_v083_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_capex_assets_1260d_slope_v084_signal(arg_capex, arg_assets): return _ca_slope(_ca_ratio(arg_capex.rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_fcf_assets_63d_slope_v085_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_fcf_assets_126d_slope_v086_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_fcf_assets_252d_slope_v087_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_fcf_assets_504d_slope_v088_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_fcf_assets_756d_slope_v089_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_fcf_assets_1260d_slope_v090_signal(arg_ncfo, arg_capex, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_retention_assets_63d_slope_v091_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_retention_assets_126d_slope_v092_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_retention_assets_252d_slope_v093_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_retention_assets_504d_slope_v094_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_retention_assets_756d_slope_v095_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_retention_assets_1260d_slope_v096_signal(arg_ncfo, arg_dividends, arg_assets): return _ca_slope(_ca_ratio((arg_ncfo - arg_dividends).rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_cash_rev_63d_slope_v097_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_cash_rev_126d_slope_v098_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_cash_rev_252d_slope_v099_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_cash_rev_504d_slope_v100_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_cash_rev_756d_slope_v101_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_cash_rev_1260d_slope_v102_signal(arg_cashneq, arg_revenue): return _ca_slope(_ca_ratio(arg_cashneq, arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_ncfo_rev_63d_slope_v103_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(63).sum(), arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_ncfo_rev_126d_slope_v104_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(126).sum(), arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_ncfo_rev_252d_slope_v105_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(252).sum(), arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_ncfo_rev_504d_slope_v106_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(504).sum(), arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_ncfo_rev_756d_slope_v107_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(756).sum(), arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_ncfo_rev_1260d_slope_v108_signal(arg_ncfo, arg_revenue): return _ca_slope(_ca_ratio(arg_ncfo.rolling(1260).sum(), arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_netinc_rev_63d_slope_v109_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(63).sum(), arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_netinc_rev_126d_slope_v110_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(126).sum(), arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_netinc_rev_252d_slope_v111_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(252).sum(), arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_netinc_rev_504d_slope_v112_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(504).sum(), arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_netinc_rev_756d_slope_v113_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(756).sum(), arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_netinc_rev_1260d_slope_v114_signal(arg_netinc, arg_revenue): return _ca_slope(_ca_ratio(arg_netinc.rolling(1260).sum(), arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_assets_rev_63d_slope_v115_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(63).sum()), 63)
def f20_capital_allocation_snapshot_assets_rev_126d_slope_v116_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(126).sum()), 126)
def f20_capital_allocation_snapshot_assets_rev_252d_slope_v117_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(252).sum()), 252)
def f20_capital_allocation_snapshot_assets_rev_504d_slope_v118_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(504).sum()), 504)
def f20_capital_allocation_snapshot_assets_rev_756d_slope_v119_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(756).sum()), 756)
def f20_capital_allocation_snapshot_assets_rev_1260d_slope_v120_signal(arg_assets, arg_revenue): return _ca_slope(_ca_ratio(arg_assets, arg_revenue.rolling(1260).sum()), 1260)
def f20_capital_allocation_snapshot_shares_growth_63d_slope_v121_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(63), 63)
def f20_capital_allocation_snapshot_shares_growth_126d_slope_v122_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(126), 126)
def f20_capital_allocation_snapshot_shares_growth_252d_slope_v123_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(252), 252)
def f20_capital_allocation_snapshot_shares_growth_504d_slope_v124_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(504), 504)
def f20_capital_allocation_snapshot_shares_growth_756d_slope_v125_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(756), 756)
def f20_capital_allocation_snapshot_shares_growth_1260d_slope_v126_signal(arg_shareswa): return _ca_slope(arg_shareswa.pct_change(1260), 1260)
def f20_capital_allocation_snapshot_capex_netinc_63d_slope_v127_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(63).sum(), arg_netinc.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_capex_netinc_126d_slope_v128_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(126).sum(), arg_netinc.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_capex_netinc_252d_slope_v129_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(252).sum(), arg_netinc.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_capex_netinc_504d_slope_v130_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(504).sum(), arg_netinc.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_capex_netinc_756d_slope_v131_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(756).sum(), arg_netinc.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_capex_netinc_1260d_slope_v132_signal(arg_capex, arg_netinc): return _ca_slope(_ca_ratio(arg_capex.rolling(1260).sum(), arg_netinc.rolling(1260).sum().abs()), 1260)
def f20_capital_allocation_snapshot_div_assets_63d_slope_v133_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(63).sum(), arg_assets), 63)
def f20_capital_allocation_snapshot_div_assets_126d_slope_v134_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(126).sum(), arg_assets), 126)
def f20_capital_allocation_snapshot_div_assets_252d_slope_v135_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(252).sum(), arg_assets), 252)
def f20_capital_allocation_snapshot_div_assets_504d_slope_v136_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(504).sum(), arg_assets), 504)
def f20_capital_allocation_snapshot_div_assets_756d_slope_v137_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(756).sum(), arg_assets), 756)
def f20_capital_allocation_snapshot_div_assets_1260d_slope_v138_signal(arg_dividends, arg_assets): return _ca_slope(_ca_ratio(arg_dividends.rolling(1260).sum(), arg_assets), 1260)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_63d_slope_v139_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(63).sum(), arg_assets), 63), 63)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_126d_slope_v140_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(126).sum(), arg_assets), 126), 126)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_252d_slope_v141_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(252).sum(), arg_assets), 252), 252)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_504d_slope_v142_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(504).sum(), arg_assets), 504), 504)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_756d_slope_v143_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(756).sum(), arg_assets), 756), 756)
def f20_capital_allocation_snapshot_ncfo_assets_zscore_1260d_slope_v144_signal(arg_ncfo, arg_assets): return _ca_slope(_ca_zscore(_ca_ratio(arg_ncfo.rolling(1260).sum(), arg_assets), 1260), 1260)
def f20_capital_allocation_snapshot_fcf_ncfo_63d_slope_v145_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(63).sum(), arg_ncfo.rolling(63).sum().abs()), 63)
def f20_capital_allocation_snapshot_fcf_ncfo_126d_slope_v146_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(126).sum(), arg_ncfo.rolling(126).sum().abs()), 126)
def f20_capital_allocation_snapshot_fcf_ncfo_252d_slope_v147_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(252).sum(), arg_ncfo.rolling(252).sum().abs()), 252)
def f20_capital_allocation_snapshot_fcf_ncfo_504d_slope_v148_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(504).sum(), arg_ncfo.rolling(504).sum().abs()), 504)
def f20_capital_allocation_snapshot_fcf_ncfo_756d_slope_v149_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(756).sum(), arg_ncfo.rolling(756).sum().abs()), 756)
def f20_capital_allocation_snapshot_fcf_ncfo_1260d_slope_v150_signal(arg_ncfo, arg_capex): return _ca_slope(_ca_ratio((arg_ncfo - arg_capex).rolling(1260).sum(), arg_ncfo.rolling(1260).sum().abs()), 1260)
SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'dividends', 'netinc', 'revenue', 'assets', 'shareswa', 'cashneq']}
FEATURE_NAMES = [f for f in globals() if f.startswith('f20_capital_allocation_snapshot_') and f.endswith('_signal')]
F20_CAPITAL_ALLOCATION_SNAPSHOT_SLOPE_REGISTRY_001_150 = {
    n: {
        'inputs': (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        'source_table': SOURCE_TABLE,
        'source_columns': {c.replace('arg_', ''): SOURCE_COLUMNS.get(c.replace('arg_', ''), c) for c in inputs},
        'entity_column': ENTITY_COLUMN, 'date_column': DATE_COLUMN,
        'order_by': ORDER_BY, 'no_forward_looking': NO_FORWARD_LOOKING, 'func': globals()[n]
    } for n in sorted(FEATURE_NAMES)
}
if __name__ == '__main__':
    import pandas as pd; import numpy as np
    sz = 2000
    d = pd.DataFrame({
        'arg_ncfo': np.random.randn(sz).cumsum() + 1000,
        'arg_capex': np.random.randn(sz).cumsum() + 200,
        'arg_dividends': np.random.randn(sz).cumsum() + 100,
        'arg_netinc': np.random.randn(sz).cumsum() + 500,
        'arg_revenue': np.random.randn(sz).cumsum() + 5000,
        'arg_assets': np.random.randn(sz).cumsum() + 10000,
        'arg_shareswa': np.random.randn(sz).cumsum() + 1000,
        'arg_cashneq': np.random.randn(sz).cumsum() + 500,
        'ticker': ['T'] * sz,
        'date': pd.date_range('2020-01-01', periods=sz)
    })
    for n, c in F20_CAPITAL_ALLOCATION_SNAPSHOT_SLOPE_REGISTRY_001_150.items():
        r = c['func'](**{i: d[i] for i in c['inputs']})
        assert len(r) > 0, f'{n} failed len'
        assert r.nunique() > 2, f'{n} failed nunique'
        assert r.std() > 0, f'{n} failed std'
    print('Slope 001-150 OK')
