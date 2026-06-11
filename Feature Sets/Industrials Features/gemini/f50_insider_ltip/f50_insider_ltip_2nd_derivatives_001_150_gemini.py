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

def f50_insider_ltip_sbcomp_slope_pct_5d_v001_signal(sbcomp):
    res = _slope_pct(sbcomp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_5d_v002_signal(shareswa):
    res = _slope_pct(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_5d_v003_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_5d_v004_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_5d_v005_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_10d_v006_signal(sbcomp):
    res = _slope_pct(sbcomp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_10d_v007_signal(shareswa):
    res = _slope_pct(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_10d_v008_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_10d_v009_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_10d_v010_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_21d_v011_signal(sbcomp):
    res = _slope_pct(sbcomp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_21d_v012_signal(shareswa):
    res = _slope_pct(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_21d_v013_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_21d_v014_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_21d_v015_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_42d_v016_signal(sbcomp):
    res = _slope_pct(sbcomp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_42d_v017_signal(shareswa):
    res = _slope_pct(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_42d_v018_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_42d_v019_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_42d_v020_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_63d_v021_signal(sbcomp):
    res = _slope_pct(sbcomp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_63d_v022_signal(shareswa):
    res = _slope_pct(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_63d_v023_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_63d_v024_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_63d_v025_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_126d_v026_signal(sbcomp):
    res = _slope_pct(sbcomp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_126d_v027_signal(shareswa):
    res = _slope_pct(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_126d_v028_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_126d_v029_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_126d_v030_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_252d_v031_signal(sbcomp):
    res = _slope_pct(sbcomp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_252d_v032_signal(shareswa):
    res = _slope_pct(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_252d_v033_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_252d_v034_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_252d_v035_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_504d_v036_signal(sbcomp):
    res = _slope_pct(sbcomp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_504d_v037_signal(shareswa):
    res = _slope_pct(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_504d_v038_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_504d_v039_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_504d_v040_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_756d_v041_signal(sbcomp):
    res = _slope_pct(sbcomp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_756d_v042_signal(shareswa):
    res = _slope_pct(shareswa, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_756d_v043_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_756d_v044_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_756d_v045_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_1008d_v046_signal(sbcomp):
    res = _slope_pct(sbcomp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_1008d_v047_signal(shareswa):
    res = _slope_pct(shareswa, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_1008d_v048_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_1008d_v049_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_1008d_v050_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_pct_1260d_v051_signal(sbcomp):
    res = _slope_pct(sbcomp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_pct_1260d_v052_signal(shareswa):
    res = _slope_pct(shareswa, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_pct_1260d_v053_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_pct_1260d_v054_signal(sbcomp, netinc):
    res = _slope_pct(_ratio(sbcomp, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_pct_1260d_v055_signal(sbcomp, shareswa):
    res = _slope_pct(_ratio(sbcomp, shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_5d_v056_signal(sbcomp):
    res = _jerk(sbcomp, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_5d_v057_signal(shareswa):
    res = _jerk(shareswa, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_5d_v058_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_5d_v059_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_5d_v060_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_10d_v061_signal(sbcomp):
    res = _jerk(sbcomp, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_10d_v062_signal(shareswa):
    res = _jerk(shareswa, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_10d_v063_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_10d_v064_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_10d_v065_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_21d_v066_signal(sbcomp):
    res = _jerk(sbcomp, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_21d_v067_signal(shareswa):
    res = _jerk(shareswa, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_21d_v068_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_21d_v069_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_21d_v070_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_42d_v071_signal(sbcomp):
    res = _jerk(sbcomp, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_42d_v072_signal(shareswa):
    res = _jerk(shareswa, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_42d_v073_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_42d_v074_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_42d_v075_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_63d_v076_signal(sbcomp):
    res = _jerk(sbcomp, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_63d_v077_signal(shareswa):
    res = _jerk(shareswa, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_63d_v078_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_63d_v079_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_63d_v080_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_126d_v081_signal(sbcomp):
    res = _jerk(sbcomp, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_126d_v082_signal(shareswa):
    res = _jerk(shareswa, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_126d_v083_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_126d_v084_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_126d_v085_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_252d_v086_signal(sbcomp):
    res = _jerk(sbcomp, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_252d_v087_signal(shareswa):
    res = _jerk(shareswa, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_252d_v088_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_252d_v089_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_252d_v090_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_504d_v091_signal(sbcomp):
    res = _jerk(sbcomp, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_504d_v092_signal(shareswa):
    res = _jerk(shareswa, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_504d_v093_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_504d_v094_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_504d_v095_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_756d_v096_signal(sbcomp):
    res = _jerk(sbcomp, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_756d_v097_signal(shareswa):
    res = _jerk(shareswa, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_756d_v098_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_756d_v099_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_756d_v100_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_1008d_v101_signal(sbcomp):
    res = _jerk(sbcomp, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_1008d_v102_signal(shareswa):
    res = _jerk(shareswa, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_1008d_v103_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_1008d_v104_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_1008d_v105_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_jerk_1260d_v106_signal(sbcomp):
    res = _jerk(sbcomp, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_jerk_1260d_v107_signal(shareswa):
    res = _jerk(shareswa, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_jerk_1260d_v108_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_jerk_1260d_v109_signal(sbcomp, netinc):
    res = _jerk(_ratio(sbcomp, netinc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_jerk_1260d_v110_signal(sbcomp, shareswa):
    res = _jerk(_ratio(sbcomp, shareswa), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_5d_v111_signal(sbcomp):
    res = (_slope_pct(sbcomp, 5).diff(5) / _sma(sbcomp.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_5d_v112_signal(shareswa):
    res = (_slope_pct(shareswa, 5).diff(5) / _sma(shareswa.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_5d_v113_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_5d_v114_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 5).diff(5) / _sma(_ratio(sbcomp, netinc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_5d_v115_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 5).diff(5) / _sma(_ratio(sbcomp, shareswa).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_10d_v116_signal(sbcomp):
    res = (_slope_pct(sbcomp, 10).diff(10) / _sma(sbcomp.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_10d_v117_signal(shareswa):
    res = (_slope_pct(shareswa, 10).diff(10) / _sma(shareswa.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_10d_v118_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_10d_v119_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 10).diff(10) / _sma(_ratio(sbcomp, netinc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_10d_v120_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 10).diff(10) / _sma(_ratio(sbcomp, shareswa).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_21d_v121_signal(sbcomp):
    res = (_slope_pct(sbcomp, 21).diff(21) / _sma(sbcomp.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_21d_v122_signal(shareswa):
    res = (_slope_pct(shareswa, 21).diff(21) / _sma(shareswa.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_21d_v123_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_21d_v124_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 21).diff(21) / _sma(_ratio(sbcomp, netinc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_21d_v125_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 21).diff(21) / _sma(_ratio(sbcomp, shareswa).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_42d_v126_signal(sbcomp):
    res = (_slope_pct(sbcomp, 42).diff(42) / _sma(sbcomp.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_42d_v127_signal(shareswa):
    res = (_slope_pct(shareswa, 42).diff(42) / _sma(shareswa.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_42d_v128_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_42d_v129_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 42).diff(42) / _sma(_ratio(sbcomp, netinc).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_42d_v130_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 42).diff(42) / _sma(_ratio(sbcomp, shareswa).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_63d_v131_signal(sbcomp):
    res = (_slope_pct(sbcomp, 63).diff(63) / _sma(sbcomp.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_63d_v132_signal(shareswa):
    res = (_slope_pct(shareswa, 63).diff(63) / _sma(shareswa.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_63d_v133_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_63d_v134_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 63).diff(63) / _sma(_ratio(sbcomp, netinc).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_63d_v135_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 63).diff(63) / _sma(_ratio(sbcomp, shareswa).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_126d_v136_signal(sbcomp):
    res = (_slope_pct(sbcomp, 126).diff(126) / _sma(sbcomp.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_126d_v137_signal(shareswa):
    res = (_slope_pct(shareswa, 126).diff(126) / _sma(shareswa.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_126d_v138_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_126d_v139_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 126).diff(126) / _sma(_ratio(sbcomp, netinc).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_126d_v140_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 126).diff(126) / _sma(_ratio(sbcomp, shareswa).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_252d_v141_signal(sbcomp):
    res = (_slope_pct(sbcomp, 252).diff(252) / _sma(sbcomp.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_252d_v142_signal(shareswa):
    res = (_slope_pct(shareswa, 252).diff(252) / _sma(shareswa.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_252d_v143_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_252d_v144_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 252).diff(252) / _sma(_ratio(sbcomp, netinc).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_252d_v145_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 252).diff(252) / _sma(_ratio(sbcomp, shareswa).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_504d_v146_signal(sbcomp):
    res = (_slope_pct(sbcomp, 504).diff(504) / _sma(sbcomp.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_504d_v147_signal(shareswa):
    res = (_slope_pct(shareswa, 504).diff(504) / _sma(shareswa.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_504d_v148_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_504d_v149_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 504).diff(504) / _sma(_ratio(sbcomp, netinc).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_504d_v150_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 504).diff(504) / _sma(_ratio(sbcomp, shareswa).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 50...")
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
