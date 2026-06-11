import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _dlog(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ===== folder domain primitives (operating leverage economics) =====
def _f32_incr_margin(profit, revenue, w):
    dp = profit - profit.shift(w)
    dr = revenue - revenue.shift(w)
    return dp / dr.replace(0, np.nan)


def _f32_dol(profit, revenue, w):
    gp2 = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr2 = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp2 / gr2.replace(0, np.nan)


def _f32_growth_spread(profit, revenue, w):
    return _dlog(profit.abs() + 1.0, w) - _dlog(revenue, w)


def _f32_margin(profit, revenue):
    return profit / revenue.replace(0, np.nan)


def _f32_absorption(profit, revenue, w):
    m = profit / revenue.replace(0, np.nan)
    return m - m.shift(w)


def _f32_opexratio(opex, revenue):
    return opex / revenue.replace(0, np.nan)



def f32ol_f32_operating_leverage_contribxem_21d_slope_v001_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxem_63d_slope_v002_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxem_126d_slope_v003_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitem_21d_slope_v004_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 126) / 5.0)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincem_21d_slope_v005_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitem_63d_slope_v006_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 252) / 5.0)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincem_63d_slope_v007_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitem_126d_slope_v008_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 504) / 5.0)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincem_126d_slope_v009_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 504) / 5.0)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitem_21d_slope_v010_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 126) / _dlog(revenue, 126).replace(0, np.nan))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastopincem_21d_slope_v011_signal(opinc, revenue):
    bse = np.tanh(_dlog(opinc.abs() + 1.0, 126) / _dlog(revenue, 126).replace(0, np.nan))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitem_63d_slope_v012_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 252) / _dlog(revenue, 252).replace(0, np.nan))
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitem_126d_slope_v013_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 504) / _dlog(revenue, 504).replace(0, np.nan))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastopincem_126d_slope_v014_signal(opinc, revenue):
    bse = np.tanh(_dlog(opinc.abs() + 1.0, 504) / _dlog(revenue, 504).replace(0, np.nan))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitem_21d_slope_v015_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 126)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpem_21d_slope_v016_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 126)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincem_21d_slope_v017_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 126)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitem_63d_slope_v018_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 252)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpem_63d_slope_v019_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 252)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincem_63d_slope_v020_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 252)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitem_126d_slope_v021_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 504)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpem_126d_slope_v022_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 504)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincem_126d_slope_v023_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 504)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpem_21d_slope_v024_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 126))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpem_63d_slope_v025_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 252))
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpem_126d_slope_v026_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 504))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxem_21d_slope_v027_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxem_63d_slope_v028_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxem_126d_slope_v029_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitem_21d_slope_v030_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngpem_21d_slope_v031_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincem_21d_slope_v032_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitem_63d_slope_v033_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngpem_63d_slope_v034_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincem_63d_slope_v035_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincem_126d_slope_v036_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitem_21d_slope_v037_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpem_21d_slope_v038_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincem_21d_slope_v039_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitem_63d_slope_v040_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpem_63d_slope_v041_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincem_63d_slope_v042_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitem_126d_slope_v043_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpem_126d_slope_v044_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincem_126d_slope_v045_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxem_21d_slope_v046_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxem_63d_slope_v047_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxem_126d_slope_v048_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxem_21d_slope_v049_signal(opex, revenue):
    bse = _dlog(revenue, 126) - _dlog(opex, 126)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxem_63d_slope_v050_signal(opex, revenue):
    bse = _dlog(revenue, 252) - _dlog(opex, 252)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxem_126d_slope_v051_signal(opex, revenue):
    bse = _dlog(revenue, 504) - _dlog(opex, 504)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_wedgexem_21d_slope_v052_signal(gp, opinc, revenue):
    bse = _f32_margin(gp, revenue) - _f32_margin(opinc, revenue)
    bse = bse.ewm(span=63, min_periods=max(2, 126 // 2)).mean()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_wedgexem_63d_slope_v053_signal(gp, opinc, revenue):
    bse = _f32_margin(gp, revenue) - _f32_margin(opinc, revenue)
    bse = bse.ewm(span=126, min_periods=max(2, 252 // 2)).mean()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_wedgexem_126d_slope_v054_signal(gp, opinc, revenue):
    bse = _f32_margin(gp, revenue) - _f32_margin(opinc, revenue)
    bse = bse.ewm(span=252, min_periods=max(2, 504 // 2)).mean()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxmd_21d_slope_v055_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxmd_63d_slope_v056_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxmd_126d_slope_v057_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitmd_21d_slope_v058_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 126) / 5.0)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincmd_21d_slope_v059_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitmd_63d_slope_v060_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 252) / 5.0)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincmd_63d_slope_v061_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitmd_126d_slope_v062_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 504) / 5.0)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincmd_126d_slope_v063_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 504) / 5.0)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitmd_21d_slope_v064_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 126) / _dlog(revenue, 126).replace(0, np.nan))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastopincmd_21d_slope_v065_signal(opinc, revenue):
    bse = np.tanh(_dlog(opinc.abs() + 1.0, 126) / _dlog(revenue, 126).replace(0, np.nan))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitmd_63d_slope_v066_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 252) / _dlog(revenue, 252).replace(0, np.nan))
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastebitmd_126d_slope_v067_signal(ebit, revenue):
    bse = np.tanh(_dlog(ebit.abs() + 1.0, 504) / _dlog(revenue, 504).replace(0, np.nan))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_elastopincmd_126d_slope_v068_signal(opinc, revenue):
    bse = np.tanh(_dlog(opinc.abs() + 1.0, 504) / _dlog(revenue, 504).replace(0, np.nan))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitmd_21d_slope_v069_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 126)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpmd_21d_slope_v070_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 126)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincmd_21d_slope_v071_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 126)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitmd_63d_slope_v072_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 252)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpmd_63d_slope_v073_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 252)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincmd_63d_slope_v074_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 252)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitmd_126d_slope_v075_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 504)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgpmd_126d_slope_v076_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 504)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincmd_126d_slope_v077_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 504)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpmd_21d_slope_v078_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 126))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpmd_63d_slope_v079_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 252))
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngpmd_126d_slope_v080_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 504))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxmd_21d_slope_v081_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxmd_63d_slope_v082_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxmd_126d_slope_v083_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitmd_21d_slope_v084_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngpmd_21d_slope_v085_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincmd_21d_slope_v086_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitmd_63d_slope_v087_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngpmd_63d_slope_v088_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincmd_63d_slope_v089_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitmd_126d_slope_v090_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngpmd_126d_slope_v091_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincmd_126d_slope_v092_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitmd_21d_slope_v093_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpmd_21d_slope_v094_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincmd_21d_slope_v095_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitmd_63d_slope_v096_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpmd_63d_slope_v097_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincmd_63d_slope_v098_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitmd_126d_slope_v099_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgpmd_126d_slope_v100_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincmd_126d_slope_v101_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxmd_21d_slope_v102_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxmd_63d_slope_v103_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_revfixxmd_126d_slope_v104_signal(gp, opinc, revenue):
    bse = np.log(revenue.replace(0, np.nan)) - np.log((gp - opinc).abs() + 1.0)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxmd_21d_slope_v105_signal(opex, revenue):
    bse = _dlog(revenue, 126) - _dlog(opex, 126)
    bse = bse - bse.rolling(126, min_periods=max(2, 126 // 3)).median()
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxmd_63d_slope_v106_signal(opex, revenue):
    bse = _dlog(revenue, 252) - _dlog(opex, 252)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_scalegapxmd_126d_slope_v107_signal(opex, revenue):
    bse = _dlog(revenue, 504) - _dlog(opex, 504)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_wedgexmd_63d_slope_v108_signal(gp, opinc, revenue):
    bse = _f32_margin(gp, revenue) - _f32_margin(opinc, revenue)
    bse = bse - bse.rolling(252, min_periods=max(2, 252 // 3)).median()
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_wedgexmd_126d_slope_v109_signal(gp, opinc, revenue):
    bse = _f32_margin(gp, revenue) - _f32_margin(opinc, revenue)
    bse = bse - bse.rolling(504, min_periods=max(2, 504 // 3)).median()
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxrk_21d_slope_v110_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxrk_63d_slope_v111_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_contribxrk_126d_slope_v112_signal(gp, opinc):
    bse = (gp - opinc) / gp.replace(0, np.nan)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitrk_21d_slope_v113_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 126) / 5.0)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincrk_21d_slope_v114_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitrk_63d_slope_v115_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 252) / 5.0)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincrk_63d_slope_v116_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolebitrk_126d_slope_v117_signal(ebit, revenue):
    bse = np.tanh(_f32_dol(ebit, revenue, 504) / 5.0)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_dolopincrk_126d_slope_v118_signal(opinc, revenue):
    bse = np.tanh(_f32_dol(opinc, revenue, 504) / 5.0)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitrk_21d_slope_v119_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 126)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgprk_21d_slope_v120_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 126)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincrk_21d_slope_v121_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 126)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitrk_63d_slope_v122_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 252)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgprk_63d_slope_v123_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 252)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincrk_63d_slope_v124_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 252)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadebitrk_126d_slope_v125_signal(ebit, revenue):
    bse = _f32_growth_spread(ebit, revenue, 504)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadgprk_126d_slope_v126_signal(gp, revenue):
    bse = _f32_growth_spread(gp, revenue, 504)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_gspreadopincrk_126d_slope_v127_signal(opinc, revenue):
    bse = _f32_growth_spread(opinc, revenue, 504)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngprk_21d_slope_v128_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 126))
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgnebitrk_63d_slope_v129_signal(ebit, revenue):
    bse = np.tanh(_f32_incr_margin(ebit, revenue, 252))
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngprk_63d_slope_v130_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 252))
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_incmgngprk_126d_slope_v131_signal(gp, revenue):
    bse = np.tanh(_f32_incr_margin(gp, revenue, 504))
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxrk_21d_slope_v132_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxrk_63d_slope_v133_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opexrevxrk_126d_slope_v134_signal(opex, revenue):
    bse = _f32_opexratio(opex, revenue)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitrk_21d_slope_v135_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngprk_21d_slope_v136_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincrk_21d_slope_v137_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitrk_63d_slope_v138_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngprk_63d_slope_v139_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincrk_63d_slope_v140_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnebitrk_126d_slope_v141_signal(ebit, revenue):
    bse = _f32_margin(ebit, revenue)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgngprk_126d_slope_v142_signal(gp, revenue):
    bse = _f32_margin(gp, revenue)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_opmgnopincrk_126d_slope_v143_signal(opinc, revenue):
    bse = _f32_margin(opinc, revenue)
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitrk_21d_slope_v144_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgprk_21d_slope_v145_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincrk_21d_slope_v146_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = _rank(bse, 126)
    result = bse - bse.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitrk_63d_slope_v147_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexgprk_63d_slope_v148_signal(gp, opex):
    bse = np.tanh(gp / opex.replace(0, np.nan))
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexopincrk_63d_slope_v149_signal(opinc, opex):
    bse = np.tanh(opinc / opex.replace(0, np.nan))
    bse = _rank(bse, 252)
    result = bse - bse.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f32ol_f32_operating_leverage_profopexebitrk_126d_slope_v150_signal(ebit, opex):
    bse = np.tanh(ebit / opex.replace(0, np.nan))
    bse = _rank(bse, 504)
    result = bse - bse.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32ol_f32_operating_leverage_contribxem_21d_slope_v001_signal,
    f32ol_f32_operating_leverage_contribxem_63d_slope_v002_signal,
    f32ol_f32_operating_leverage_contribxem_126d_slope_v003_signal,
    f32ol_f32_operating_leverage_dolebitem_21d_slope_v004_signal,
    f32ol_f32_operating_leverage_dolopincem_21d_slope_v005_signal,
    f32ol_f32_operating_leverage_dolebitem_63d_slope_v006_signal,
    f32ol_f32_operating_leverage_dolopincem_63d_slope_v007_signal,
    f32ol_f32_operating_leverage_dolebitem_126d_slope_v008_signal,
    f32ol_f32_operating_leverage_dolopincem_126d_slope_v009_signal,
    f32ol_f32_operating_leverage_elastebitem_21d_slope_v010_signal,
    f32ol_f32_operating_leverage_elastopincem_21d_slope_v011_signal,
    f32ol_f32_operating_leverage_elastebitem_63d_slope_v012_signal,
    f32ol_f32_operating_leverage_elastebitem_126d_slope_v013_signal,
    f32ol_f32_operating_leverage_elastopincem_126d_slope_v014_signal,
    f32ol_f32_operating_leverage_gspreadebitem_21d_slope_v015_signal,
    f32ol_f32_operating_leverage_gspreadgpem_21d_slope_v016_signal,
    f32ol_f32_operating_leverage_gspreadopincem_21d_slope_v017_signal,
    f32ol_f32_operating_leverage_gspreadebitem_63d_slope_v018_signal,
    f32ol_f32_operating_leverage_gspreadgpem_63d_slope_v019_signal,
    f32ol_f32_operating_leverage_gspreadopincem_63d_slope_v020_signal,
    f32ol_f32_operating_leverage_gspreadebitem_126d_slope_v021_signal,
    f32ol_f32_operating_leverage_gspreadgpem_126d_slope_v022_signal,
    f32ol_f32_operating_leverage_gspreadopincem_126d_slope_v023_signal,
    f32ol_f32_operating_leverage_incmgngpem_21d_slope_v024_signal,
    f32ol_f32_operating_leverage_incmgngpem_63d_slope_v025_signal,
    f32ol_f32_operating_leverage_incmgngpem_126d_slope_v026_signal,
    f32ol_f32_operating_leverage_opexrevxem_21d_slope_v027_signal,
    f32ol_f32_operating_leverage_opexrevxem_63d_slope_v028_signal,
    f32ol_f32_operating_leverage_opexrevxem_126d_slope_v029_signal,
    f32ol_f32_operating_leverage_opmgnebitem_21d_slope_v030_signal,
    f32ol_f32_operating_leverage_opmgngpem_21d_slope_v031_signal,
    f32ol_f32_operating_leverage_opmgnopincem_21d_slope_v032_signal,
    f32ol_f32_operating_leverage_opmgnebitem_63d_slope_v033_signal,
    f32ol_f32_operating_leverage_opmgngpem_63d_slope_v034_signal,
    f32ol_f32_operating_leverage_opmgnopincem_63d_slope_v035_signal,
    f32ol_f32_operating_leverage_opmgnopincem_126d_slope_v036_signal,
    f32ol_f32_operating_leverage_profopexebitem_21d_slope_v037_signal,
    f32ol_f32_operating_leverage_profopexgpem_21d_slope_v038_signal,
    f32ol_f32_operating_leverage_profopexopincem_21d_slope_v039_signal,
    f32ol_f32_operating_leverage_profopexebitem_63d_slope_v040_signal,
    f32ol_f32_operating_leverage_profopexgpem_63d_slope_v041_signal,
    f32ol_f32_operating_leverage_profopexopincem_63d_slope_v042_signal,
    f32ol_f32_operating_leverage_profopexebitem_126d_slope_v043_signal,
    f32ol_f32_operating_leverage_profopexgpem_126d_slope_v044_signal,
    f32ol_f32_operating_leverage_profopexopincem_126d_slope_v045_signal,
    f32ol_f32_operating_leverage_revfixxem_21d_slope_v046_signal,
    f32ol_f32_operating_leverage_revfixxem_63d_slope_v047_signal,
    f32ol_f32_operating_leverage_revfixxem_126d_slope_v048_signal,
    f32ol_f32_operating_leverage_scalegapxem_21d_slope_v049_signal,
    f32ol_f32_operating_leverage_scalegapxem_63d_slope_v050_signal,
    f32ol_f32_operating_leverage_scalegapxem_126d_slope_v051_signal,
    f32ol_f32_operating_leverage_wedgexem_21d_slope_v052_signal,
    f32ol_f32_operating_leverage_wedgexem_63d_slope_v053_signal,
    f32ol_f32_operating_leverage_wedgexem_126d_slope_v054_signal,
    f32ol_f32_operating_leverage_contribxmd_21d_slope_v055_signal,
    f32ol_f32_operating_leverage_contribxmd_63d_slope_v056_signal,
    f32ol_f32_operating_leverage_contribxmd_126d_slope_v057_signal,
    f32ol_f32_operating_leverage_dolebitmd_21d_slope_v058_signal,
    f32ol_f32_operating_leverage_dolopincmd_21d_slope_v059_signal,
    f32ol_f32_operating_leverage_dolebitmd_63d_slope_v060_signal,
    f32ol_f32_operating_leverage_dolopincmd_63d_slope_v061_signal,
    f32ol_f32_operating_leverage_dolebitmd_126d_slope_v062_signal,
    f32ol_f32_operating_leverage_dolopincmd_126d_slope_v063_signal,
    f32ol_f32_operating_leverage_elastebitmd_21d_slope_v064_signal,
    f32ol_f32_operating_leverage_elastopincmd_21d_slope_v065_signal,
    f32ol_f32_operating_leverage_elastebitmd_63d_slope_v066_signal,
    f32ol_f32_operating_leverage_elastebitmd_126d_slope_v067_signal,
    f32ol_f32_operating_leverage_elastopincmd_126d_slope_v068_signal,
    f32ol_f32_operating_leverage_gspreadebitmd_21d_slope_v069_signal,
    f32ol_f32_operating_leverage_gspreadgpmd_21d_slope_v070_signal,
    f32ol_f32_operating_leverage_gspreadopincmd_21d_slope_v071_signal,
    f32ol_f32_operating_leverage_gspreadebitmd_63d_slope_v072_signal,
    f32ol_f32_operating_leverage_gspreadgpmd_63d_slope_v073_signal,
    f32ol_f32_operating_leverage_gspreadopincmd_63d_slope_v074_signal,
    f32ol_f32_operating_leverage_gspreadebitmd_126d_slope_v075_signal,
    f32ol_f32_operating_leverage_gspreadgpmd_126d_slope_v076_signal,
    f32ol_f32_operating_leverage_gspreadopincmd_126d_slope_v077_signal,
    f32ol_f32_operating_leverage_incmgngpmd_21d_slope_v078_signal,
    f32ol_f32_operating_leverage_incmgngpmd_63d_slope_v079_signal,
    f32ol_f32_operating_leverage_incmgngpmd_126d_slope_v080_signal,
    f32ol_f32_operating_leverage_opexrevxmd_21d_slope_v081_signal,
    f32ol_f32_operating_leverage_opexrevxmd_63d_slope_v082_signal,
    f32ol_f32_operating_leverage_opexrevxmd_126d_slope_v083_signal,
    f32ol_f32_operating_leverage_opmgnebitmd_21d_slope_v084_signal,
    f32ol_f32_operating_leverage_opmgngpmd_21d_slope_v085_signal,
    f32ol_f32_operating_leverage_opmgnopincmd_21d_slope_v086_signal,
    f32ol_f32_operating_leverage_opmgnebitmd_63d_slope_v087_signal,
    f32ol_f32_operating_leverage_opmgngpmd_63d_slope_v088_signal,
    f32ol_f32_operating_leverage_opmgnopincmd_63d_slope_v089_signal,
    f32ol_f32_operating_leverage_opmgnebitmd_126d_slope_v090_signal,
    f32ol_f32_operating_leverage_opmgngpmd_126d_slope_v091_signal,
    f32ol_f32_operating_leverage_opmgnopincmd_126d_slope_v092_signal,
    f32ol_f32_operating_leverage_profopexebitmd_21d_slope_v093_signal,
    f32ol_f32_operating_leverage_profopexgpmd_21d_slope_v094_signal,
    f32ol_f32_operating_leverage_profopexopincmd_21d_slope_v095_signal,
    f32ol_f32_operating_leverage_profopexebitmd_63d_slope_v096_signal,
    f32ol_f32_operating_leverage_profopexgpmd_63d_slope_v097_signal,
    f32ol_f32_operating_leverage_profopexopincmd_63d_slope_v098_signal,
    f32ol_f32_operating_leverage_profopexebitmd_126d_slope_v099_signal,
    f32ol_f32_operating_leverage_profopexgpmd_126d_slope_v100_signal,
    f32ol_f32_operating_leverage_profopexopincmd_126d_slope_v101_signal,
    f32ol_f32_operating_leverage_revfixxmd_21d_slope_v102_signal,
    f32ol_f32_operating_leverage_revfixxmd_63d_slope_v103_signal,
    f32ol_f32_operating_leverage_revfixxmd_126d_slope_v104_signal,
    f32ol_f32_operating_leverage_scalegapxmd_21d_slope_v105_signal,
    f32ol_f32_operating_leverage_scalegapxmd_63d_slope_v106_signal,
    f32ol_f32_operating_leverage_scalegapxmd_126d_slope_v107_signal,
    f32ol_f32_operating_leverage_wedgexmd_63d_slope_v108_signal,
    f32ol_f32_operating_leverage_wedgexmd_126d_slope_v109_signal,
    f32ol_f32_operating_leverage_contribxrk_21d_slope_v110_signal,
    f32ol_f32_operating_leverage_contribxrk_63d_slope_v111_signal,
    f32ol_f32_operating_leverage_contribxrk_126d_slope_v112_signal,
    f32ol_f32_operating_leverage_dolebitrk_21d_slope_v113_signal,
    f32ol_f32_operating_leverage_dolopincrk_21d_slope_v114_signal,
    f32ol_f32_operating_leverage_dolebitrk_63d_slope_v115_signal,
    f32ol_f32_operating_leverage_dolopincrk_63d_slope_v116_signal,
    f32ol_f32_operating_leverage_dolebitrk_126d_slope_v117_signal,
    f32ol_f32_operating_leverage_dolopincrk_126d_slope_v118_signal,
    f32ol_f32_operating_leverage_gspreadebitrk_21d_slope_v119_signal,
    f32ol_f32_operating_leverage_gspreadgprk_21d_slope_v120_signal,
    f32ol_f32_operating_leverage_gspreadopincrk_21d_slope_v121_signal,
    f32ol_f32_operating_leverage_gspreadebitrk_63d_slope_v122_signal,
    f32ol_f32_operating_leverage_gspreadgprk_63d_slope_v123_signal,
    f32ol_f32_operating_leverage_gspreadopincrk_63d_slope_v124_signal,
    f32ol_f32_operating_leverage_gspreadebitrk_126d_slope_v125_signal,
    f32ol_f32_operating_leverage_gspreadgprk_126d_slope_v126_signal,
    f32ol_f32_operating_leverage_gspreadopincrk_126d_slope_v127_signal,
    f32ol_f32_operating_leverage_incmgngprk_21d_slope_v128_signal,
    f32ol_f32_operating_leverage_incmgnebitrk_63d_slope_v129_signal,
    f32ol_f32_operating_leverage_incmgngprk_63d_slope_v130_signal,
    f32ol_f32_operating_leverage_incmgngprk_126d_slope_v131_signal,
    f32ol_f32_operating_leverage_opexrevxrk_21d_slope_v132_signal,
    f32ol_f32_operating_leverage_opexrevxrk_63d_slope_v133_signal,
    f32ol_f32_operating_leverage_opexrevxrk_126d_slope_v134_signal,
    f32ol_f32_operating_leverage_opmgnebitrk_21d_slope_v135_signal,
    f32ol_f32_operating_leverage_opmgngprk_21d_slope_v136_signal,
    f32ol_f32_operating_leverage_opmgnopincrk_21d_slope_v137_signal,
    f32ol_f32_operating_leverage_opmgnebitrk_63d_slope_v138_signal,
    f32ol_f32_operating_leverage_opmgngprk_63d_slope_v139_signal,
    f32ol_f32_operating_leverage_opmgnopincrk_63d_slope_v140_signal,
    f32ol_f32_operating_leverage_opmgnebitrk_126d_slope_v141_signal,
    f32ol_f32_operating_leverage_opmgngprk_126d_slope_v142_signal,
    f32ol_f32_operating_leverage_opmgnopincrk_126d_slope_v143_signal,
    f32ol_f32_operating_leverage_profopexebitrk_21d_slope_v144_signal,
    f32ol_f32_operating_leverage_profopexgprk_21d_slope_v145_signal,
    f32ol_f32_operating_leverage_profopexopincrk_21d_slope_v146_signal,
    f32ol_f32_operating_leverage_profopexebitrk_63d_slope_v147_signal,
    f32ol_f32_operating_leverage_profopexgprk_63d_slope_v148_signal,
    f32ol_f32_operating_leverage_profopexopincrk_63d_slope_v149_signal,
    f32ol_f32_operating_leverage_profopexebitrk_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_OPERATING_LEVERAGE_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=1e9, drift=0.03, vol=0.05).rename("revenue")
    opex = _fund(102, base=6e8, drift=0.025, vol=0.05).rename("opex")
    gp = _fund(103, base=4e8, drift=0.03, vol=0.06).rename("gp")
    opinc = _fund(104, base=1.5e8, drift=0.03, vol=0.09, allow_neg=True).rename("opinc")
    ebit = _fund(105, base=1.4e8, drift=0.03, vol=0.10, allow_neg=True).rename("ebit")
    cols = {"revenue": revenue, "opex": opex, "gp": gp, "opinc": opinc, "ebit": ebit}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, name
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok"

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR " + ni + " vs " + nj + (" = %.4f" % c)

    print("OK f32_operating_leverage_2nd_derivatives_001_150_claude: %d features pass" % n_features)
