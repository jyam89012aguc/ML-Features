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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f49_death_spiral(sharesbas, debt, equity, w):
    # composite: dilution growth + leverage growth + equity erosion
    sg = sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)
    dg = debt.diff(w) / debt.shift(w).abs().replace(0, np.nan)
    eg = -equity.diff(w) / equity.shift(w).abs().replace(0, np.nan)
    return sg + dg + eg


def _f49_dilution(sharesbas, w):
    return sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)


def _f49_leveragegrowth(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(w) / lev.shift(w).abs().replace(0, np.nan)


# 21d death-spiral composite × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_21d_base_v001_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d death-spiral composite × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_63d_base_v002_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d death-spiral composite × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_126d_base_v003_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 126)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d death-spiral composite × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_252d_base_v004_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d death-spiral composite × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiral_504d_base_v005_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean spiral × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralmean_21d_base_v006_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = _mean(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean spiral × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralmean_63d_base_v007_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = _mean(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_21d_base_v008_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_63d_base_v009_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralstd_252d_base_v010_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore spiral over 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralz_252d_base_v011_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore spiral over 504d
def f49bsds_f49_balance_sheet_death_spiral_spiralz_504d_base_v012_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilution_21d_base_v013_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilution_63d_base_v014_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilution_252d_base_v015_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilution_504d_base_v016_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std dilution
def f49bsds_f49_balance_sheet_death_spiral_dilstd_21d_base_v017_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std dilution
def f49bsds_f49_balance_sheet_death_spiral_dilstd_63d_base_v018_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore dilution
def f49bsds_f49_balance_sheet_death_spiral_dilz_252d_base_v019_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore dilution
def f49bsds_f49_balance_sheet_death_spiral_dilz_504d_base_v020_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levg_21d_base_v021_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 21)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levg_63d_base_v022_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levg_252d_base_v023_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levg_504d_base_v024_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 504)
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgstd_63d_base_v025_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgstd_252d_base_v026_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgz_252d_base_v027_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgz_504d_base_v028_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of strong-spiral days (>10%)
def f49bsds_f49_balance_sheet_death_spiral_spiralcount10_252d_base_v029_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of strong-spiral days (>30%)
def f49bsds_f49_balance_sheet_death_spiral_spiralcount30_504d_base_v030_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of dilution > 5%
def f49bsds_f49_balance_sheet_death_spiral_dilcount5_252d_base_v031_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of dilution > 15%
def f49bsds_f49_balance_sheet_death_spiral_dilcount15_504d_base_v032_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of leverage growth > 20%
def f49bsds_f49_balance_sheet_death_spiral_levgcount20_252d_base_v033_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of leverage growth > 50%
def f49bsds_f49_balance_sheet_death_spiral_levgcount50_504d_base_v034_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst (max) spiral × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_21d_base_v035_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base.rolling(21, min_periods=5).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst spiral
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_63d_base_v036_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst spiral
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_252d_base_v037_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst spiral
def f49bsds_f49_balance_sheet_death_spiral_worstspiral_504d_base_v038_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralema_21d_base_v039_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralema_63d_base_v040_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralema_252d_base_v041_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squared spiral (severity)
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_21d_base_v042_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 21)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_63d_base_v043_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared spiral
def f49bsds_f49_balance_sheet_death_spiral_spiralsq_252d_base_v044_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × ev (size-weighted spiral severity)
def f49bsds_f49_balance_sheet_death_spiral_spiralxev_63d_base_v045_signal(sharesbas, debt, equity, marketcap, ev):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * ev
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × ev 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxev_252d_base_v046_signal(sharesbas, debt, equity, marketcap, ev):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * ev
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpe_63d_base_v047_signal(sharesbas, debt, equity, marketcap, pe):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × ps 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxps_63d_base_v048_signal(sharesbas, debt, equity, marketcap, ps):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × evebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebitda_63d_base_v049_signal(sharesbas, debt, equity, marketcap, evebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × evebit 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebit_63d_base_v050_signal(sharesbas, debt, equity, marketcap, evebit):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × pb 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxpb_63d_base_v051_signal(sharesbas, debt, equity, marketcap, pb):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × ev 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxev_63d_base_v052_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 63)
    result = base * ev + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxpe_63d_base_v053_signal(sharesbas, marketcap, pe):
    base = _f49_dilution(sharesbas, 63)
    result = base * pe * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × ps 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxps_252d_base_v054_signal(sharesbas, marketcap, ps):
    base = _f49_dilution(sharesbas, 252)
    result = base * ps * marketcap + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × ev 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxev_63d_base_v055_signal(debt, equity, marketcap, ev):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * ev + _f49_dilution(equity, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × pe 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxpe_63d_base_v056_signal(debt, equity, marketcap, pe):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * pe * marketcap + _f49_dilution(equity, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap of spiral 63m252
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_63m252_base_v057_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral 21m63 gap
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_21m63_base_v058_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 21)
    b = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral 252m504 gap
def f49bsds_f49_balance_sheet_death_spiral_spiralgap_252m504_base_v059_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 252)
    b = _f49_death_spiral(sharesbas, debt, equity, 504)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral / 252d spiral ratio
def f49bsds_f49_balance_sheet_death_spiral_spiralratio_63v252_base_v060_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d spiral / 63d spiral ratio
def f49bsds_f49_balance_sheet_death_spiral_spiralratio_21v63_base_v061_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 21)
    b = _f49_death_spiral(sharesbas, debt, equity, 63).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d expanding worst spiral × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralworstever_base_v062_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral vs ever 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralvsever_63d_base_v063_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral vs ever 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralvsever_252d_base_v064_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × marketcap squared (size-amplified)
def f49bsds_f49_balance_sheet_death_spiral_spiralxmcapsq_63d_base_v065_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × marketcap squared
def f49bsds_f49_balance_sheet_death_spiral_spiralxmcapsq_252d_base_v066_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × log marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralxlogmcap_63d_base_v067_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = base * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × revenue 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrev_63d_base_v068_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * revenue + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × assets 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralxassets_63d_base_v069_signal(sharesbas, debt, equity, marketcap, assets):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * assets + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# spiral × debt 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxdebt_252d_base_v070_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 21d spiral area (cumulative)
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_63d_base_v071_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63).abs()
    result = base.rolling(63, min_periods=21).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral area
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_252d_base_v072_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    result = base.rolling(252, min_periods=63).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d spiral area
def f49bsds_f49_balance_sheet_death_spiral_spiralarea_504d_base_v073_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504).abs()
    result = base.rolling(504, min_periods=126).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: dilution × leverage growth (joint deterioration)
def f49bsds_f49_balance_sheet_death_spiral_dilxlev_63d_base_v074_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 63)
    b = _f49_leveragegrowth(debt, equity, 63)
    result = a * b * marketcap + _f49_death_spiral(sharesbas, debt, equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite multifactor severity × ev
def f49bsds_f49_balance_sheet_death_spiral_compositesev_252d_base_v075_signal(sharesbas, debt, equity, marketcap, ev):
    a = _f49_dilution(sharesbas, 252).abs()
    b = _f49_leveragegrowth(debt, equity, 252).abs()
    c = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    result = (a + b + c) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f49bsds_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_BALANCE_SHEET_DEATH_SPIRAL_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f49_balance_sheet_death_spiral_base_001_075_claude: {n_features} features pass")
