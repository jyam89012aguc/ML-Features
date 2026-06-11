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
def _f46_low_vol_signal(close, w):
    r = close.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std()
    inv_vol = 1.0 / vol.replace(0, np.nan)
    return inv_vol * close


def _f46_steady_earnings_growth(netinc, w):
    g = netinc.pct_change(periods=w)
    smooth = g.rolling(w, min_periods=max(1, w // 2)).mean()
    stab = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return smooth / stab


def _f46_compounder_composite(close, netinc, w):
    r = close.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    g = netinc.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return (g / vol) * close



# ===== features =====

def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_5d_slope_v001_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 5), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_5d_slope_v002_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 5), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_5d_slope_v003_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_10d_slope_v004_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 10), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_10d_slope_v005_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 10), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_10d_slope_v006_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 10), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_21d_slope_v007_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 21), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_21d_slope_v008_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 21), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_21d_slope_v009_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_42d_slope_v010_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 42), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_42d_slope_v011_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 42), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_42d_slope_v012_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 42), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_63d_slope_v013_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 63), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_63d_slope_v014_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 63), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_63d_slope_v015_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_126d_slope_v016_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 126), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_126d_slope_v017_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 126), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_126d_slope_v018_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 126), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_189d_slope_v019_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 189), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_189d_slope_v020_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 189), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_189d_slope_v021_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 189), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_252d_slope_v022_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 252), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_252d_slope_v023_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 252), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_252d_slope_v024_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_378d_slope_v025_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 378), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_378d_slope_v026_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 378), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_378d_slope_v027_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 378), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_504d_slope_v028_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 504), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_504d_slope_v029_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 504), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_504d_slope_v030_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 504), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_5d_slope_v031_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 5), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_5d_slope_v032_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_5d_slope_v033_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 5), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_10d_slope_v034_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 10), 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_10d_slope_v035_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 10), 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_10d_slope_v036_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 10), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_21d_slope_v037_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 21), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_21d_slope_v038_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 21), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_21d_slope_v039_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 21), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_42d_slope_v040_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 42), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_42d_slope_v041_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 42), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_42d_slope_v042_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 42), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_63d_slope_v043_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 63), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_63d_slope_v044_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 63), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_63d_slope_v045_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 63), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_126d_slope_v046_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 126), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_126d_slope_v047_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 126), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_126d_slope_v048_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 126), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_189d_slope_v049_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 189), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_189d_slope_v050_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 189), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_189d_slope_v051_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 189), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_252d_slope_v052_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 252), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_252d_slope_v053_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 252), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_252d_slope_v054_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 252), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_378d_slope_v055_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 378), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_378d_slope_v056_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 378), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_378d_slope_v057_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 378), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_504d_slope_v058_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 504), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_504d_slope_v059_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 504), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_504d_slope_v060_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 504), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_5d_slope_v061_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_5d_slope_v062_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 5), 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_5d_slope_v063_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 5), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_10d_slope_v064_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 10), 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_10d_slope_v065_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 10), 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_10d_slope_v066_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 10), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_21d_slope_v067_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 21), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_21d_slope_v068_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 21), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_21d_slope_v069_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 21), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_42d_slope_v070_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 42), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_42d_slope_v071_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 42), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_42d_slope_v072_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 42), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_63d_slope_v073_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 63), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_63d_slope_v074_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 63), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_63d_slope_v075_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 63), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_126d_slope_v076_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 126), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_126d_slope_v077_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 126), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_126d_slope_v078_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 126), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_189d_slope_v079_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 189), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_189d_slope_v080_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 189), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_189d_slope_v081_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 189), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_252d_slope_v082_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 252), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_252d_slope_v083_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 252), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_252d_slope_v084_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 252), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_378d_slope_v085_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 378), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_378d_slope_v086_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 378), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_378d_slope_v087_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 378), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_504d_slope_v088_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 504), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_504d_slope_v089_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 504), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_504d_slope_v090_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 504), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_5d_slope_v091_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 5), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_5d_slope_v092_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 5), 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_5d_slope_v093_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 5), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_10d_slope_v094_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 10), 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_10d_slope_v095_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 10), 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_10d_slope_v096_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 10), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_21d_slope_v097_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 21), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_21d_slope_v098_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 21), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_21d_slope_v099_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 21), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_42d_slope_v100_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 42), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_42d_slope_v101_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 42), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_42d_slope_v102_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 42), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_63d_slope_v103_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 63), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_63d_slope_v104_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 63), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_63d_slope_v105_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 63), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_126d_slope_v106_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 126), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_126d_slope_v107_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 126), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_126d_slope_v108_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 126), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_189d_slope_v109_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 189), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_189d_slope_v110_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 189), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_189d_slope_v111_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 189), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_252d_slope_v112_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 252), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_252d_slope_v113_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 252), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_252d_slope_v114_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 252), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_378d_slope_v115_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 378), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_378d_slope_v116_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 378), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_378d_slope_v117_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 378), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_504d_slope_v118_signal(closeadj):
    result = (_slope_pct(_f46_low_vol_signal(closeadj, 504), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_504d_slope_v119_signal(netinc, closeadj):
    result = (_slope_pct(_f46_steady_earnings_growth(netinc, 504), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_504d_slope_v120_signal(closeadj, netinc):
    result = (_slope_pct(_f46_compounder_composite(closeadj, netinc, 504), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_5d_slope_v121_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 5), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_5d_slope_v122_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 5), 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_5d_slope_v123_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 5), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_10d_slope_v124_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 10), 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_10d_slope_v125_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 10), 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_10d_slope_v126_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 10), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_21d_slope_v127_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 21), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_21d_slope_v128_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 21), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_21d_slope_v129_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 21), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_42d_slope_v130_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 42), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_42d_slope_v131_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 42), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_42d_slope_v132_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 42), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_63d_slope_v133_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 63), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_63d_slope_v134_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 63), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_63d_slope_v135_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 63), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_126d_slope_v136_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 126), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_126d_slope_v137_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 126), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_126d_slope_v138_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 126), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_189d_slope_v139_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 189), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_189d_slope_v140_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 189), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_189d_slope_v141_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 189), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_252d_slope_v142_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 252), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_252d_slope_v143_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 252), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_252d_slope_v144_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 252), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_378d_slope_v145_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 378), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_378d_slope_v146_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 378), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_378d_slope_v147_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 378), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_504d_slope_v148_signal(closeadj):
    result = (_slope_diff_norm(_f46_low_vol_signal(closeadj, 504), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_504d_slope_v149_signal(netinc, closeadj):
    result = (_slope_diff_norm(_f46_steady_earnings_growth(netinc, 504), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_504d_slope_v150_signal(closeadj, netinc):
    result = (_slope_diff_norm(_f46_compounder_composite(closeadj, netinc, 504), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_5d_slope_v001_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_5d_slope_v002_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_5d_slope_v003_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_10d_slope_v004_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_10d_slope_v005_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_10d_slope_v006_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_21d_slope_v007_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_21d_slope_v008_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_21d_slope_v009_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_42d_slope_v010_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_42d_slope_v011_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_42d_slope_v012_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_63d_slope_v013_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_63d_slope_v014_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_63d_slope_v015_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_126d_slope_v016_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_126d_slope_v017_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_126d_slope_v018_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_189d_slope_v019_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_189d_slope_v020_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_189d_slope_v021_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_252d_slope_v022_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_252d_slope_v023_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_252d_slope_v024_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_378d_slope_v025_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_378d_slope_v026_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_378d_slope_v027_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_504d_slope_v028_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_504d_slope_v029_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_504d_slope_v030_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_5d_slope_v031_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_5d_slope_v032_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_5d_slope_v033_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_10d_slope_v034_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_10d_slope_v035_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_10d_slope_v036_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_21d_slope_v037_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_21d_slope_v038_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_21d_slope_v039_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_42d_slope_v040_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_42d_slope_v041_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_42d_slope_v042_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_63d_slope_v043_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_63d_slope_v044_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_63d_slope_v045_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_126d_slope_v046_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_126d_slope_v047_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_126d_slope_v048_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_189d_slope_v049_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_189d_slope_v050_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_189d_slope_v051_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_252d_slope_v052_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_252d_slope_v053_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_252d_slope_v054_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_378d_slope_v055_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_378d_slope_v056_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_378d_slope_v057_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_504d_slope_v058_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_504d_slope_v059_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_504d_slope_v060_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_5d_slope_v061_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_5d_slope_v062_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_5d_slope_v063_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_10d_slope_v064_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_10d_slope_v065_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_10d_slope_v066_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_21d_slope_v067_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_21d_slope_v068_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_21d_slope_v069_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_42d_slope_v070_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_42d_slope_v071_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_42d_slope_v072_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_63d_slope_v073_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_63d_slope_v074_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_63d_slope_v075_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_126d_slope_v076_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_126d_slope_v077_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_126d_slope_v078_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_189d_slope_v079_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_189d_slope_v080_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_189d_slope_v081_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_252d_slope_v082_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_252d_slope_v083_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_252d_slope_v084_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_378d_slope_v085_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_378d_slope_v086_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_378d_slope_v087_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_504d_slope_v088_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_504d_slope_v089_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_504d_slope_v090_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_5d_slope_v091_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_5d_slope_v092_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_5d_slope_v093_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_10d_slope_v094_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_10d_slope_v095_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_10d_slope_v096_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_21d_slope_v097_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_21d_slope_v098_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_21d_slope_v099_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_42d_slope_v100_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_42d_slope_v101_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_42d_slope_v102_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_63d_slope_v103_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_63d_slope_v104_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_63d_slope_v105_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_126d_slope_v106_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_126d_slope_v107_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_126d_slope_v108_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_189d_slope_v109_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_189d_slope_v110_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_189d_slope_v111_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_252d_slope_v112_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_252d_slope_v113_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_252d_slope_v114_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_378d_slope_v115_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_378d_slope_v116_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_378d_slope_v117_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_504d_slope_v118_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_504d_slope_v119_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_504d_slope_v120_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_5d_slope_v121_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_5d_slope_v122_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_5d_slope_v123_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_10d_slope_v124_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_10d_slope_v125_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_10d_slope_v126_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_21d_slope_v127_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_21d_slope_v128_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_21d_slope_v129_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_42d_slope_v130_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_42d_slope_v131_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_42d_slope_v132_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_63d_slope_v133_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_63d_slope_v134_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_63d_slope_v135_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_126d_slope_v136_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_126d_slope_v137_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_126d_slope_v138_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_189d_slope_v139_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_189d_slope_v140_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_189d_slope_v141_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_252d_slope_v142_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_252d_slope_v143_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_252d_slope_v144_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_378d_slope_v145_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_378d_slope_v146_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_378d_slope_v147_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_504d_slope_v148_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_504d_slope_v149_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_504d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_MEDTECH_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_low_vol_signal", "_f46_steady_earnings_growth", "_f46_compounder_composite")
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
    print(f"OK f46_quiet_medtech_compounder_2nd_derivatives_001_150_claude: {n_features} features pass")
