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

def f49_tax_arbitrage_taxexp_slope_pct_5d_v001_signal(taxexp):
    res = _slope_pct(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_5d_v002_signal(ebt):
    res = _slope_pct(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_5d_v003_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_5d_v004_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_10d_v005_signal(taxexp):
    res = _slope_pct(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_10d_v006_signal(ebt):
    res = _slope_pct(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_10d_v007_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_10d_v008_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_21d_v009_signal(taxexp):
    res = _slope_pct(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_21d_v010_signal(ebt):
    res = _slope_pct(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_21d_v011_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_21d_v012_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_42d_v013_signal(taxexp):
    res = _slope_pct(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_42d_v014_signal(ebt):
    res = _slope_pct(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_42d_v015_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_42d_v016_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_63d_v017_signal(taxexp):
    res = _slope_pct(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_63d_v018_signal(ebt):
    res = _slope_pct(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_63d_v019_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_63d_v020_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_126d_v021_signal(taxexp):
    res = _slope_pct(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_126d_v022_signal(ebt):
    res = _slope_pct(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_126d_v023_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_126d_v024_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_252d_v025_signal(taxexp):
    res = _slope_pct(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_252d_v026_signal(ebt):
    res = _slope_pct(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_252d_v027_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_252d_v028_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_504d_v029_signal(taxexp):
    res = _slope_pct(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_504d_v030_signal(ebt):
    res = _slope_pct(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_504d_v031_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_504d_v032_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_756d_v033_signal(taxexp):
    res = _slope_pct(taxexp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_756d_v034_signal(ebt):
    res = _slope_pct(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_756d_v035_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_756d_v036_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_1008d_v037_signal(taxexp):
    res = _slope_pct(taxexp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_1008d_v038_signal(ebt):
    res = _slope_pct(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_1008d_v039_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_1008d_v040_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_pct_1260d_v041_signal(taxexp):
    res = _slope_pct(taxexp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_pct_1260d_v042_signal(ebt):
    res = _slope_pct(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_pct_1260d_v043_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_pct_1260d_v044_signal(taxexp, ebt):
    res = _slope_pct(_ratio(taxexp, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_5d_v045_signal(taxexp):
    res = _jerk(taxexp, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_5d_v046_signal(ebt):
    res = _jerk(ebt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_5d_v047_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_5d_v048_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_10d_v049_signal(taxexp):
    res = _jerk(taxexp, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_10d_v050_signal(ebt):
    res = _jerk(ebt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_10d_v051_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_10d_v052_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_21d_v053_signal(taxexp):
    res = _jerk(taxexp, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_21d_v054_signal(ebt):
    res = _jerk(ebt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_21d_v055_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_21d_v056_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_42d_v057_signal(taxexp):
    res = _jerk(taxexp, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_42d_v058_signal(ebt):
    res = _jerk(ebt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_42d_v059_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_42d_v060_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_63d_v061_signal(taxexp):
    res = _jerk(taxexp, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_63d_v062_signal(ebt):
    res = _jerk(ebt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_63d_v063_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_63d_v064_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_126d_v065_signal(taxexp):
    res = _jerk(taxexp, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_126d_v066_signal(ebt):
    res = _jerk(ebt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_126d_v067_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_126d_v068_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_252d_v069_signal(taxexp):
    res = _jerk(taxexp, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_252d_v070_signal(ebt):
    res = _jerk(ebt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_252d_v071_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_252d_v072_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_504d_v073_signal(taxexp):
    res = _jerk(taxexp, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_504d_v074_signal(ebt):
    res = _jerk(ebt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_504d_v075_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_504d_v076_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_756d_v077_signal(taxexp):
    res = _jerk(taxexp, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_756d_v078_signal(ebt):
    res = _jerk(ebt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_756d_v079_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_756d_v080_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_1008d_v081_signal(taxexp):
    res = _jerk(taxexp, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_1008d_v082_signal(ebt):
    res = _jerk(ebt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_1008d_v083_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_1008d_v084_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_jerk_1260d_v085_signal(taxexp):
    res = _jerk(taxexp, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_jerk_1260d_v086_signal(ebt):
    res = _jerk(ebt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_jerk_1260d_v087_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_jerk_1260d_v088_signal(taxexp, ebt):
    res = _jerk(_ratio(taxexp, ebt), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_5d_v089_signal(taxexp):
    res = (_slope_pct(taxexp, 5).diff(5) / _sma(taxexp.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_5d_v090_signal(ebt):
    res = (_slope_pct(ebt, 5).diff(5) / _sma(ebt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_5d_v091_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_5d_v092_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 5).diff(5) / _sma(_ratio(taxexp, ebt).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_10d_v093_signal(taxexp):
    res = (_slope_pct(taxexp, 10).diff(10) / _sma(taxexp.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_10d_v094_signal(ebt):
    res = (_slope_pct(ebt, 10).diff(10) / _sma(ebt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_10d_v095_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_10d_v096_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 10).diff(10) / _sma(_ratio(taxexp, ebt).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_21d_v097_signal(taxexp):
    res = (_slope_pct(taxexp, 21).diff(21) / _sma(taxexp.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_21d_v098_signal(ebt):
    res = (_slope_pct(ebt, 21).diff(21) / _sma(ebt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_21d_v099_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_21d_v100_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 21).diff(21) / _sma(_ratio(taxexp, ebt).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_42d_v101_signal(taxexp):
    res = (_slope_pct(taxexp, 42).diff(42) / _sma(taxexp.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_42d_v102_signal(ebt):
    res = (_slope_pct(ebt, 42).diff(42) / _sma(ebt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_42d_v103_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_42d_v104_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 42).diff(42) / _sma(_ratio(taxexp, ebt).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_63d_v105_signal(taxexp):
    res = (_slope_pct(taxexp, 63).diff(63) / _sma(taxexp.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_63d_v106_signal(ebt):
    res = (_slope_pct(ebt, 63).diff(63) / _sma(ebt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_63d_v107_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_63d_v108_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 63).diff(63) / _sma(_ratio(taxexp, ebt).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_126d_v109_signal(taxexp):
    res = (_slope_pct(taxexp, 126).diff(126) / _sma(taxexp.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_126d_v110_signal(ebt):
    res = (_slope_pct(ebt, 126).diff(126) / _sma(ebt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_126d_v111_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_126d_v112_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 126).diff(126) / _sma(_ratio(taxexp, ebt).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_252d_v113_signal(taxexp):
    res = (_slope_pct(taxexp, 252).diff(252) / _sma(taxexp.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_252d_v114_signal(ebt):
    res = (_slope_pct(ebt, 252).diff(252) / _sma(ebt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_252d_v115_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_252d_v116_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 252).diff(252) / _sma(_ratio(taxexp, ebt).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_504d_v117_signal(taxexp):
    res = (_slope_pct(taxexp, 504).diff(504) / _sma(taxexp.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_504d_v118_signal(ebt):
    res = (_slope_pct(ebt, 504).diff(504) / _sma(ebt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_504d_v119_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_504d_v120_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 504).diff(504) / _sma(_ratio(taxexp, ebt).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_756d_v121_signal(taxexp):
    res = (_slope_pct(taxexp, 756).diff(756) / _sma(taxexp.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_756d_v122_signal(ebt):
    res = (_slope_pct(ebt, 756).diff(756) / _sma(ebt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_756d_v123_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_756d_v124_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 756).diff(756) / _sma(_ratio(taxexp, ebt).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_1008d_v125_signal(taxexp):
    res = (_slope_pct(taxexp, 1008).diff(1008) / _sma(taxexp.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_1008d_v126_signal(ebt):
    res = (_slope_pct(ebt, 1008).diff(1008) / _sma(ebt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_1008d_v127_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_1008d_v128_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 1008).diff(1008) / _sma(_ratio(taxexp, ebt).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_slope_diff_norm_1260d_v129_signal(taxexp):
    res = (_slope_pct(taxexp, 1260).diff(1260) / _sma(taxexp.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_slope_diff_norm_1260d_v130_signal(ebt):
    res = (_slope_pct(ebt, 1260).diff(1260) / _sma(ebt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_slope_diff_norm_1260d_v131_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_slope_diff_norm_1260d_v132_signal(taxexp, ebt):
    res = (_slope_pct(_ratio(taxexp, ebt), 1260).diff(1260) / _sma(_ratio(taxexp, ebt).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_mom_z_5d_v133_signal(taxexp):
    res = _z(_slope_pct(taxexp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_mom_z_5d_v134_signal(ebt):
    res = _z(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_mom_z_5d_v135_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_mom_z_5d_v136_signal(taxexp, ebt):
    res = _z(_slope_pct(_ratio(taxexp, ebt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_mom_z_10d_v137_signal(taxexp):
    res = _z(_slope_pct(taxexp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_mom_z_10d_v138_signal(ebt):
    res = _z(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_mom_z_10d_v139_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_mom_z_10d_v140_signal(taxexp, ebt):
    res = _z(_slope_pct(_ratio(taxexp, ebt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_mom_z_21d_v141_signal(taxexp):
    res = _z(_slope_pct(taxexp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_mom_z_21d_v142_signal(ebt):
    res = _z(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_mom_z_21d_v143_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_mom_z_21d_v144_signal(taxexp, ebt):
    res = _z(_slope_pct(_ratio(taxexp, ebt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_mom_z_42d_v145_signal(taxexp):
    res = _z(_slope_pct(taxexp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_mom_z_42d_v146_signal(ebt):
    res = _z(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_mom_z_42d_v147_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_mom_z_42d_v148_signal(taxexp, ebt):
    res = _z(_slope_pct(_ratio(taxexp, ebt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_mom_z_63d_v149_signal(taxexp):
    res = _z(_slope_pct(taxexp, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_mom_z_63d_v150_signal(ebt):
    res = _z(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 49...")
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
