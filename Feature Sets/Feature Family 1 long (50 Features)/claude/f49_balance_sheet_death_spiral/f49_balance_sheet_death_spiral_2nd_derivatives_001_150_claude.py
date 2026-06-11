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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w)


# ===== folder domain primitives =====
def _f49_death_spiral(sharesbas, debt, equity, w):
    sg = sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)
    dg = debt.diff(w) / debt.shift(w).abs().replace(0, np.nan)
    eg = -equity.diff(w) / equity.shift(w).abs().replace(0, np.nan)
    return sg + dg + eg


def _f49_dilution(sharesbas, w):
    return sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)


def _f49_leveragegrowth(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(w) / lev.shift(w).abs().replace(0, np.nan)


# Use a registry-driven generator approach via inline definitions
# Pattern: 150 features = (5 base shapes) x (10 win combinations) plus extras

# Shape A: spiral × marketcap, varying windows
# Shape B: dilution × marketcap, varying windows
# Shape C: leverage growth × marketcap, varying windows
# Shape D: spiral × valuation_metric × marketcap
# Shape E: composite/anomaly

# 5d slope of 21d spiral × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_21d_slope_v001_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_21d_slope_v002_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_63d_slope_v003_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_63d_slope_v004_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_63d_slope_v005_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_126d_slope_v006_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 126) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_126d_slope_v007_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_252d_slope_v008_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_252d_slope_v009_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_504d_slope_v010_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_504d_slope_v011_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d spiral
def f49bsds_f49_balance_sheet_death_spiral_spiral_504d_slope_v012_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral mean 21d
def f49bsds_f49_balance_sheet_death_spiral_spiralmean_21d_slope_v013_signal(sharesbas, debt, equity, marketcap):
    base = _mean(_f49_death_spiral(sharesbas, debt, equity, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral mean 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralmean_63d_slope_v014_signal(sharesbas, debt, equity, marketcap):
    base = _mean(_f49_death_spiral(sharesbas, debt, equity, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral std 21d
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_21d_slope_v015_signal(sharesbas, debt, equity, marketcap):
    base = _std(_f49_death_spiral(sharesbas, debt, equity, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral std 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_63d_slope_v016_signal(sharesbas, debt, equity, marketcap):
    base = _std(_f49_death_spiral(sharesbas, debt, equity, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral std 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_252d_slope_v017_signal(sharesbas, debt, equity, marketcap):
    base = _std(_f49_death_spiral(sharesbas, debt, equity, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral z 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralz_252d_slope_v018_signal(sharesbas, debt, equity, marketcap):
    base = _z(_f49_death_spiral(sharesbas, debt, equity, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral z 504d
def f49bsds_f49_balance_sheet_death_spiral_spiralz_504d_slope_v019_signal(sharesbas, debt, equity, marketcap):
    base = _z(_f49_death_spiral(sharesbas, debt, equity, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_21d_slope_v020_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_63d_slope_v021_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_63d_slope_v022_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_252d_slope_v023_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_252d_slope_v024_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dilution
def f49bsds_f49_balance_sheet_death_spiral_dilution_504d_slope_v025_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution std 21d
def f49bsds_f49_balance_sheet_death_spiral_dilstd_21d_slope_v026_signal(sharesbas, marketcap):
    base = _std(_f49_dilution(sharesbas, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution std 63d
def f49bsds_f49_balance_sheet_death_spiral_dilstd_63d_slope_v027_signal(sharesbas, marketcap):
    base = _std(_f49_dilution(sharesbas, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution z 252d
def f49bsds_f49_balance_sheet_death_spiral_dilz_252d_slope_v028_signal(sharesbas, marketcap):
    base = _z(_f49_dilution(sharesbas, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution z 504d
def f49bsds_f49_balance_sheet_death_spiral_dilz_504d_slope_v029_signal(sharesbas, marketcap):
    base = _z(_f49_dilution(sharesbas, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_21d_slope_v030_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_63d_slope_v031_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_63d_slope_v032_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_252d_slope_v033_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_252d_slope_v034_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levg_504d_slope_v035_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage growth std 63d
def f49bsds_f49_balance_sheet_death_spiral_levgstd_63d_slope_v036_signal(debt, equity, marketcap):
    base = _std(_f49_leveragegrowth(debt, equity, 252), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage growth std 252d
def f49bsds_f49_balance_sheet_death_spiral_levgstd_252d_slope_v037_signal(debt, equity, marketcap):
    base = _std(_f49_leveragegrowth(debt, equity, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage z 252d
def f49bsds_f49_balance_sheet_death_spiral_levgz_252d_slope_v038_signal(debt, equity, marketcap):
    base = _z(_f49_leveragegrowth(debt, equity, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage z 504d
def f49bsds_f49_balance_sheet_death_spiral_levgz_504d_slope_v039_signal(debt, equity, marketcap):
    base = _z(_f49_leveragegrowth(debt, equity, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral count 10 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralcount10_252d_slope_v040_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of spiral mean × marketcap (504d window)
def f49bsds_f49_balance_sheet_death_spiral_spiralcount30_504d_slope_v041_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    base = base.rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution count 5 252d
def f49bsds_f49_balance_sheet_death_spiral_dilcount5_252d_slope_v042_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dilution count 15 504d
def f49bsds_f49_balance_sheet_death_spiral_dilcount15_504d_slope_v043_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    base = base.rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage count 20 252d
def f49bsds_f49_balance_sheet_death_spiral_levgcount20_252d_slope_v044_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    base = base.rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of leverage count 50 504d
def f49bsds_f49_balance_sheet_death_spiral_levgcount50_504d_slope_v045_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst spiral 21d
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_21d_slope_v046_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).rolling(21, min_periods=5).max() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst spiral 63d
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_63d_slope_v047_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst spiral 252d
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_252d_slope_v048_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst spiral 504d
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_504d_slope_v049_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral EMA 21d
def f49bsds_f49_balance_sheet_death_spiral_spiralema_21d_slope_v050_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral EMA 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralema_63d_slope_v051_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral EMA 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralema_252d_slope_v052_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral squared 21d
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_21d_slope_v053_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 21)
    base = s * s.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral squared 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_63d_slope_v054_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 63)
    base = s * s.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral squared 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_252d_slope_v055_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 252)
    base = s * s.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × ev 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxev_63d_slope_v056_signal(sharesbas, debt, equity, marketcap, ev):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × ev 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxev_252d_slope_v057_signal(sharesbas, debt, equity, marketcap, ev):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpe_63d_slope_v058_signal(sharesbas, debt, equity, marketcap, pe):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × ps 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxps_63d_slope_v059_signal(sharesbas, debt, equity, marketcap, ps):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × evebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebitda_63d_slope_v060_signal(sharesbas, debt, equity, marketcap, evebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × evebit 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebit_63d_slope_v061_signal(sharesbas, debt, equity, marketcap, evebit):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * evebit * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × pb 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpb_63d_slope_v062_signal(sharesbas, debt, equity, marketcap, pb):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * pb * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution × ev 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxev_63d_slope_v063_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 63) * ev + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxpe_63d_slope_v064_signal(sharesbas, marketcap, pe):
    base = _f49_dilution(sharesbas, 63) * pe * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution × ps 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxps_252d_slope_v065_signal(sharesbas, marketcap, ps):
    base = _f49_dilution(sharesbas, 252) * ps * marketcap + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage × ev 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxev_63d_slope_v066_signal(debt, equity, marketcap, ev):
    base = _f49_leveragegrowth(debt, equity, 63) * ev + _f49_dilution(equity, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxpe_63d_slope_v067_signal(debt, equity, marketcap, pe):
    base = _f49_leveragegrowth(debt, equity, 63) * pe * marketcap + _f49_dilution(equity, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral gap 63m252
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_63m252_slope_v068_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252)
    base = (a - b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of spiral gap 21m63
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_21m63_slope_v069_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 21)
    b = _f49_death_spiral(sharesbas, debt, equity, 63)
    base = (a - b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral gap 252m504
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_252m504_slope_v070_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 252)
    b = _f49_death_spiral(sharesbas, debt, equity, 504)
    base = (a - b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral ratio 63v252
def f49bsds_f49_balance_sheet_death_spiral_spiralratio_63v252_slope_v071_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of spiral ratio 21v63
def f49bsds_f49_balance_sheet_death_spiral_spiralratio_21v63_slope_v072_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 21)
    b = _f49_death_spiral(sharesbas, debt, equity, 63).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral worst-ever
def f49bsds_f49_balance_sheet_death_spiral_spiralworstever_slope_v073_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).expanding(min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral vs ever 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralvsever_63d_slope_v074_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 63)
    worst = s.expanding(min_periods=63).max()
    base = (worst - s) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral vs ever 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralvsever_252d_slope_v075_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 252)
    worst = s.expanding(min_periods=63).max()
    base = (worst - s) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × marketcap squared 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxmcapsq_63d_slope_v076_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * marketcap * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × marketcap squared 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxmcapsq_252d_slope_v077_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * marketcap * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × log marketcap 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxlogmcap_63d_slope_v078_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = base * lm * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × revenue 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrev_63d_slope_v079_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * revenue + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × assets 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxassets_63d_slope_v080_signal(sharesbas, debt, equity, marketcap, assets):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * assets + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × debt 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxdebt_252d_slope_v081_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * debt
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral area 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_63d_slope_v082_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).abs().rolling(63, min_periods=21).sum() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral area 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_252d_slope_v083_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).abs().rolling(252, min_periods=63).sum() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of spiral area 504d
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_504d_slope_v084_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504).abs().rolling(504, min_periods=126).sum() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilxlev 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxlev_63d_slope_v085_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 63)
    b = _f49_leveragegrowth(debt, equity, 63)
    base = a * b * marketcap + _f49_death_spiral(sharesbas, debt, equity, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositesev 252d
def f49bsds_f49_balance_sheet_death_spiral_compositesev_252d_slope_v086_signal(sharesbas, debt, equity, marketcap, ev):
    a = _f49_dilution(sharesbas, 252).abs()
    b = _f49_leveragegrowth(debt, equity, 252).abs()
    c = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    base = (a + b + c) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution EMA 21d
def f49bsds_f49_balance_sheet_death_spiral_dilema_21d_slope_v087_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution EMA 63d
def f49bsds_f49_balance_sheet_death_spiral_dilema_63d_slope_v088_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution EMA 252d
def f49bsds_f49_balance_sheet_death_spiral_dilema_252d_slope_v089_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage EMA 21d
def f49bsds_f49_balance_sheet_death_spiral_levgema_21d_slope_v090_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage EMA 63d
def f49bsds_f49_balance_sheet_death_spiral_levgema_63d_slope_v091_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage EMA 252d
def f49bsds_f49_balance_sheet_death_spiral_levgema_252d_slope_v092_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst dilution 21d
def f49bsds_f49_balance_sheet_death_spiral_worstdil_21d_slope_v093_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63).rolling(21, min_periods=5).max() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst dilution 63d
def f49bsds_f49_balance_sheet_death_spiral_worstdil_63d_slope_v094_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst dilution 252d
def f49bsds_f49_balance_sheet_death_spiral_worstdil_252d_slope_v095_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst dilution 504d
def f49bsds_f49_balance_sheet_death_spiral_worstdil_504d_slope_v096_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst leverage 63d
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_63d_slope_v097_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst leverage 252d
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_252d_slope_v098_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst leverage 504d
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_504d_slope_v099_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution sq 63d
def f49bsds_f49_balance_sheet_death_spiral_dilsq_63d_slope_v100_signal(sharesbas, marketcap):
    d = _f49_dilution(sharesbas, 63)
    base = d * d.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilution sq 252d
def f49bsds_f49_balance_sheet_death_spiral_dilsq_252d_slope_v101_signal(sharesbas, marketcap):
    d = _f49_dilution(sharesbas, 252)
    base = d * d.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage sq 63d
def f49bsds_f49_balance_sheet_death_spiral_levgsq_63d_slope_v102_signal(debt, equity, marketcap):
    l = _f49_leveragegrowth(debt, equity, 63)
    base = l * l.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage sq 252d
def f49bsds_f49_balance_sheet_death_spiral_levgsq_252d_slope_v103_signal(debt, equity, marketcap):
    l = _f49_leveragegrowth(debt, equity, 252)
    base = l * l.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilxev 21d
def f49bsds_f49_balance_sheet_death_spiral_dilxev_21d_slope_v104_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 21) * ev + _f49_leveragegrowth(marketcap, marketcap, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilxev 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxev_252d_slope_v105_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 252) * ev + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of levgxev 252d
def f49bsds_f49_balance_sheet_death_spiral_levgxev_252d_slope_v106_signal(debt, equity, marketcap, ev):
    base = _f49_leveragegrowth(debt, equity, 252) * ev + _f49_dilution(equity, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilxevebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxevebitda_63d_slope_v107_signal(sharesbas, marketcap, evebitda):
    base = _f49_dilution(sharesbas, 63) * evebitda * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilxevebit 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxevebit_252d_slope_v108_signal(sharesbas, marketcap, evebit):
    base = _f49_dilution(sharesbas, 252) * evebit * marketcap + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilxpb 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxpb_63d_slope_v109_signal(sharesbas, marketcap, pb):
    base = _f49_dilution(sharesbas, 63) * pb * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilxps 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxps_63d_slope_v110_signal(sharesbas, marketcap, ps):
    base = _f49_dilution(sharesbas, 63) * ps * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of levgxevebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxevebitda_63d_slope_v111_signal(debt, equity, marketcap, evebitda):
    base = _f49_leveragegrowth(debt, equity, 63) * evebitda * marketcap + _f49_dilution(equity, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of levgxevebit 252d
def f49bsds_f49_balance_sheet_death_spiral_levgxevebit_252d_slope_v112_signal(debt, equity, marketcap, evebit):
    base = _f49_leveragegrowth(debt, equity, 252) * evebit * marketcap + _f49_dilution(equity, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of levgxpb 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxpb_63d_slope_v113_signal(debt, equity, marketcap, pb):
    base = _f49_leveragegrowth(debt, equity, 63) * pb * marketcap + _f49_dilution(equity, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of levgxps 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxps_63d_slope_v114_signal(debt, equity, marketcap, ps):
    base = _f49_leveragegrowth(debt, equity, 63) * ps * marketcap + _f49_dilution(equity, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of equity erosion count 252d
def f49bsds_f49_balance_sheet_death_spiral_eqerodecount5_252d_slope_v115_signal(equity, marketcap):
    eg = -equity.diff(63) / equity.shift(63).abs().replace(0, np.nan)
    base = (eg).rolling(252, min_periods=63).mean() * marketcap + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of equity erosion count 504d
def f49bsds_f49_balance_sheet_death_spiral_eqerodecount15_504d_slope_v116_signal(equity, marketcap):
    eg = -equity.diff(252) / equity.shift(252).abs().replace(0, np.nan)
    base = (eg).rolling(504, min_periods=126).mean() * marketcap + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dilxlev 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxlev_252d_slope_v117_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 252)
    b = _f49_leveragegrowth(debt, equity, 252)
    base = a * b * marketcap + _f49_death_spiral(sharesbas, debt, equity, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × debt-to-marketcap 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxdtomcap_63d_slope_v118_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * (debt / marketcap.replace(0, np.nan)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × debt-to-marketcap 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxdtomcap_252d_slope_v119_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * (debt / marketcap.replace(0, np.nan)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × inverse equity 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxinveq_63d_slope_v120_signal(sharesbas, debt, equity, marketcap):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * inveq * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × inverse equity 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxinveq_252d_slope_v121_signal(sharesbas, debt, equity, marketcap):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * inveq * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral anomaly 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralanomaly_63d_slope_v122_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252)
    base = (a - b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral anomaly 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralanomaly_252d_slope_v123_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 252)
    b = _f49_death_spiral(sharesbas, debt, equity, 504)
    base = (a - b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × evebitda 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebitda_252d_slope_v124_signal(sharesbas, debt, equity, marketcap, evebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * evebitda * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × evebit 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebit_252d_slope_v125_signal(sharesbas, debt, equity, marketcap, evebit):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * evebit * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × pb 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpb_252d_slope_v126_signal(sharesbas, debt, equity, marketcap, pb):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * pb * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × pe 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpe_252d_slope_v127_signal(sharesbas, debt, equity, marketcap, pe):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * pe * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × ps 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxps_252d_slope_v128_signal(sharesbas, debt, equity, marketcap, ps):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * ps * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × log marketcap 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxlogmcap_252d_slope_v129_signal(sharesbas, debt, equity, marketcap):
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * lm * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × revenue 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrev_252d_slope_v130_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * revenue + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × assets 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxassets_252d_slope_v131_signal(sharesbas, debt, equity, marketcap, assets):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * assets + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × debt 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxdebt_63d_slope_v132_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * debt
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × equity 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxequity_63d_slope_v133_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * equity.abs()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × equity 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxequity_252d_slope_v134_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * equity.abs()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × ebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxebitda_63d_slope_v135_signal(sharesbas, debt, equity, marketcap, ebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * ebitda + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × ebitda 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxebitda_252d_slope_v136_signal(sharesbas, debt, equity, marketcap, ebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * ebitda + _f49_dilution(equity, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral area frac 63v252
def f49bsds_f49_balance_sheet_death_spiral_spiralareafrac_63v252_slope_v137_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    a = s.rolling(63, min_periods=21).sum()
    b = s.rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral area frac 252v504
def f49bsds_f49_balance_sheet_death_spiral_spiralareafrac_252v504_slope_v138_signal(sharesbas, debt, equity, marketcap):
    s = _f49_death_spiral(sharesbas, debt, equity, 504).abs()
    a = s.rolling(252, min_periods=63).sum()
    b = s.rolling(504, min_periods=126).sum().replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral volvol 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralvolvol_63d_slope_v139_signal(sharesbas, debt, equity, marketcap):
    sd = _std(_f49_death_spiral(sharesbas, debt, equity, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral volvol 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralvolvol_252d_slope_v140_signal(sharesbas, debt, equity, marketcap):
    sd = _std(_f49_death_spiral(sharesbas, debt, equity, 504), 252)
    base = _std(sd, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dilution volvol 63d
def f49bsds_f49_balance_sheet_death_spiral_dilvolvol_63d_slope_v141_signal(sharesbas, marketcap):
    sd = _std(_f49_dilution(sharesbas, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leverage volvol 63d
def f49bsds_f49_balance_sheet_death_spiral_levgvolvol_63d_slope_v142_signal(debt, equity, marketcap):
    sd = _std(_f49_leveragegrowth(debt, equity, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × close 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxclose_63d_slope_v143_signal(sharesbas, debt, equity, marketcap, closeadj):
    base = _f49_death_spiral(sharesbas, debt, equity, 63) * closeadj * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × close 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxclose_252d_slope_v144_signal(sharesbas, debt, equity, marketcap, closeadj):
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * closeadj * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of spiral × revenue growth 21d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrevg_21d_slope_v145_signal(sharesbas, debt, equity, marketcap, revenue):
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f49_death_spiral(sharesbas, debt, equity, 21) * rg * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of spiral × revenue growth 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrevg_252d_slope_v146_signal(sharesbas, debt, equity, marketcap, revenue):
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f49_death_spiral(sharesbas, debt, equity, 252) * rg * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multifactor 63d
def f49bsds_f49_balance_sheet_death_spiral_multifactor_63d_slope_v147_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 63)
    b = _f49_leveragegrowth(debt, equity, 63)
    c = _f49_death_spiral(sharesbas, debt, equity, 63)
    base = (a + b + c) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of multifactor 252d
def f49bsds_f49_balance_sheet_death_spiral_multifactor_252d_slope_v148_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 252)
    b = _f49_leveragegrowth(debt, equity, 252)
    c = _f49_death_spiral(sharesbas, debt, equity, 252)
    base = (a + b + c) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of multifactor 504d
def f49bsds_f49_balance_sheet_death_spiral_multifactor_504d_slope_v149_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 504)
    b = _f49_leveragegrowth(debt, equity, 504)
    c = _f49_death_spiral(sharesbas, debt, equity, 504)
    base = (a + b + c) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of compositesev 252d × ev
def f49bsds_f49_balance_sheet_death_spiral_compositesev_252d_extra_slope_v150_signal(sharesbas, debt, equity, marketcap, ev):
    a = _f49_dilution(sharesbas, 252).abs()
    b = _f49_leveragegrowth(debt, equity, 252).abs()
    c = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    base = (a + b + c) * ev
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f49bsds_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_BALANCE_SHEET_DEATH_SPIRAL_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_death_spiral", "_f49_dilution", "_f49_leveragegrowth")
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
    print(f"OK f49_balance_sheet_death_spiral_2nd_derivatives_001_150_claude: {n_features} features pass")
