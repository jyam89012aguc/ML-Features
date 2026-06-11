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

def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_5d_base_v001_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_5d_base_v002_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_5d_base_v003_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_10d_base_v004_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_10d_base_v005_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_10d_base_v006_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_21d_base_v007_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_21d_base_v008_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_21d_base_v009_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_42d_base_v010_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_42d_base_v011_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_42d_base_v012_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_63d_base_v013_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_63d_base_v014_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_63d_base_v015_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_126d_base_v016_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_126d_base_v017_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_126d_base_v018_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_189d_base_v019_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_189d_base_v020_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_189d_base_v021_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_252d_base_v022_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_252d_base_v023_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_252d_base_v024_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_378d_base_v025_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_378d_base_v026_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_378d_base_v027_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_504d_base_v028_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_504d_base_v029_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_504d_base_v030_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_5d_base_v031_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_5d_base_v032_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_5d_base_v033_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_10d_base_v034_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_10d_base_v035_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_10d_base_v036_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_21d_base_v037_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_21d_base_v038_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_21d_base_v039_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_42d_base_v040_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_42d_base_v041_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_42d_base_v042_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_63d_base_v043_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_63d_base_v044_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_63d_base_v045_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_126d_base_v046_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_126d_base_v047_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_126d_base_v048_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_189d_base_v049_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_189d_base_v050_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_189d_base_v051_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_252d_base_v052_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_252d_base_v053_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_252d_base_v054_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_378d_base_v055_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_378d_base_v056_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_378d_base_v057_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_504d_base_v058_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_504d_base_v059_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_504d_base_v060_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_5d_base_v061_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_5d_base_v062_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_5d_base_v063_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_10d_base_v064_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_10d_base_v065_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_10d_base_v066_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_21d_base_v067_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_21d_base_v068_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_21d_base_v069_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_42d_base_v070_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_42d_base_v071_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_42d_base_v072_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_63d_base_v073_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_63d_base_v074_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_63d_base_v075_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_5d_base_v001_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_5d_base_v002_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_5d_base_v003_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_10d_base_v004_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_10d_base_v005_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_10d_base_v006_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_21d_base_v007_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_21d_base_v008_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_21d_base_v009_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_42d_base_v010_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_42d_base_v011_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_42d_base_v012_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_63d_base_v013_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_63d_base_v014_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_63d_base_v015_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_126d_base_v016_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_126d_base_v017_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_126d_base_v018_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_189d_base_v019_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_189d_base_v020_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_189d_base_v021_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_252d_base_v022_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_252d_base_v023_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_252d_base_v024_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_378d_base_v025_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_378d_base_v026_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_378d_base_v027_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose_504d_base_v028_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose_504d_base_v029_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose_504d_base_v030_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_5d_base_v031_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_5d_base_v032_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_5d_base_v033_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_10d_base_v034_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_10d_base_v035_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_10d_base_v036_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_21d_base_v037_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_21d_base_v038_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_21d_base_v039_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_42d_base_v040_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_42d_base_v041_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_42d_base_v042_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_63d_base_v043_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_63d_base_v044_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_63d_base_v045_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_126d_base_v046_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_126d_base_v047_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_126d_base_v048_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_189d_base_v049_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_189d_base_v050_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_189d_base_v051_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_252d_base_v052_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_252d_base_v053_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_252d_base_v054_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_378d_base_v055_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_378d_base_v056_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_378d_base_v057_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclosemean_504d_base_v058_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclosemean_504d_base_v059_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclosemean_504d_base_v060_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_5d_base_v061_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_5d_base_v062_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_5d_base_v063_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_10d_base_v064_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_10d_base_v065_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_10d_base_v066_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_21d_base_v067_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_21d_base_v068_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_21d_base_v069_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_42d_base_v070_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_42d_base_v071_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_42d_base_v072_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_63d_base_v073_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_63d_base_v074_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_MEDTECH_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f46_quiet_medtech_compounder_base_001_075_claude: {n_features} features pass")
