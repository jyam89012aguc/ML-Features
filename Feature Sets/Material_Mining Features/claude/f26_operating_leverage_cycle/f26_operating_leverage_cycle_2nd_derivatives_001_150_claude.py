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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== operating-leverage primitives (growth-sensitivity ONLY) =====
def _dgrow(s, w):
    return s - s.shift(w)


def _pctg(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _grow(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _dol(profit, revenue, w):
    gp = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp / gr.replace(0, np.nan)


def _incmgn(profit, revenue, w):
    return (profit - profit.shift(w)) / (revenue - revenue.shift(w)).replace(0, np.nan)


def _gspread(profit, revenue, w):
    return _grow(profit, w) - _grow(revenue, w)


def _be_rev(gp, opex, revenue):
    cm = gp / revenue.replace(0, np.nan)
    return opex / cm.replace(0, np.nan)


def f26ol_f26_operating_leverage_cycle_dolop63r21_slope_v001_signal(opinc, revenue):
    b = _dol(opinc, revenue, 63).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop126r21_slope_v002_signal(opinc, revenue):
    b = _dol(opinc, revenue, 126).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop252r21_slope_v003_signal(opinc, revenue):
    b = _dol(opinc, revenue, 252).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop504r21_slope_v004_signal(opinc, revenue):
    b = _mean(_dol(opinc, revenue, 504).clip(-15, 15), 63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doleb126r21_slope_v005_signal(ebit, revenue):
    b = _dol(ebit, revenue, 126).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doleb252r21_slope_v006_signal(ebit, revenue):
    b = _rank(_dol(ebit, revenue, 252).clip(-15, 15), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolcogs126r21_slope_v007_signal(gp, revenue):
    cogs = revenue - gp
    b = _z(_dol(cogs, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolcogs252r21_slope_v008_signal(gp, revenue):
    cogs = revenue - gp
    b = _rank(_dol(cogs, revenue, 252).clip(-15, 15), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolmag252r21_slope_v009_signal(opinc, revenue):
    b = _mean(_dol(opinc, revenue, 252).abs().clip(0, 15), 63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolexc252r21_slope_v010_signal(opinc, revenue):
    d = _dol(opinc, revenue, 252).clip(-15, 15) - 1.0
    b = _rank(np.sign(d) * (d.abs() ** 0.5), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doltermshortr21_slope_v011_signal(opinc, revenue):
    b = _dol(opinc, revenue, 63).clip(-15, 15) - _dol(opinc, revenue, 252).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doltermlongr21_slope_v012_signal(opinc, revenue):
    b = _dol(opinc, revenue, 504).clip(-15, 15) - _dol(opinc, revenue, 126).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolz126r21_slope_v013_signal(opinc, revenue):
    b = _z(_dol(opinc, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolratioebr21_slope_v014_signal(ebit, opinc, revenue):
    b = (_dol(ebit, revenue, 252).clip(-15, 15) / _dol(opinc, revenue, 252).clip(-15, 15).replace(0, np.nan)).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolinstabr21_slope_v015_signal(opinc, revenue):
    b = _std(_dol(opinc, revenue, 63).clip(-15, 15), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop63r21_slope_v016_signal(opinc, revenue):
    inc = _incmgn(opinc, revenue, 63).clip(-5, 5)
    b = inc.where(_grow(revenue, 63) > 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop126r21_slope_v017_signal(opinc, revenue):
    b = _rank(_incmgn(opinc, revenue, 126).clip(-5, 5), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop252r21_slope_v018_signal(opinc, revenue):
    b = _z(_incmgn(opinc, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop504r21_slope_v019_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 504).clip(-5, 5)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incgp126r21_slope_v020_signal(gp, revenue):
    b = _rank(_incmgn(gp, revenue, 126).clip(-3, 3), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incgp252r21_slope_v021_signal(gp, revenue):
    b = _z(_incmgn(gp, revenue, 252).clip(-3, 3), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inceb126r21_slope_v022_signal(ebit, revenue):
    b = _z(_incmgn(ebit, revenue, 126).clip(-5, 5), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inceb252r21_slope_v023_signal(ebit, revenue):
    b = _z(_incmgn(ebit, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incemar21_slope_v024_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 126).clip(-5, 5).ewm(span=126, min_periods=42).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incspreadr21_slope_v025_signal(gp, opinc, revenue):
    b = _incmgn(gp, revenue, 252).clip(-3, 3) - _incmgn(opinc, revenue, 252).clip(-3, 3)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inctermr21_slope_v026_signal(opinc, revenue):
    b = _z(_incmgn(opinc, revenue, 63).clip(-5, 5) - _incmgn(opinc, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incdispr21_slope_v027_signal(opinc, revenue):
    b = pd.concat([_incmgn(opinc, revenue, 63).clip(-5, 5), _incmgn(opinc, revenue, 126).clip(-5, 5), _incmgn(opinc, revenue, 252).clip(-5, 5)], axis=1).std(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incconsistr21_slope_v028_signal(opinc, revenue):
    agree = (np.sign(_dgrow(opinc, 63)) == np.sign(_dgrow(revenue, 63))).astype(float)
    b = agree.rolling(252, min_periods=63).mean() - 0.5
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incopex252r21_slope_v029_signal(opex, revenue):
    b = _z(_incmgn(opex, revenue, 252).clip(-3, 3), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incovhr21_slope_v030_signal(gp, opinc):
    ov = gp - opinc
    b = (_dgrow(ov, 252) / _dgrow(gp, 252).replace(0, np.nan)).clip(-5, 5)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap63r21_slope_v031_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap126r21_slope_v032_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap252r21_slope_v033_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap504r21_slope_v034_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapeb126r21_slope_v035_signal(ebit, revenue):
    b = _gspread(ebit, revenue, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapeb252r21_slope_v036_signal(ebit, revenue):
    b = _gspread(ebit, revenue, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapgp126r21_slope_v037_signal(gp, revenue):
    b = _gspread(gp, revenue, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapgp252r21_slope_v038_signal(gp, revenue):
    b = _gspread(gp, revenue, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapsignmagr21_slope_v039_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapemar21_slope_v040_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 126).ewm(span=189, min_periods=63).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapcascader21_slope_v041_signal(gp, opinc, revenue):
    b = _gspread(opinc, revenue, 252) - _gspread(gp, revenue, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapvolr21_slope_v042_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 252)
    v = _std(_grow(revenue, 63), 252)
    b = (g / v.replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapampr21_slope_v043_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 63).abs().rolling(252, min_periods=63).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapstackr21_slope_v044_signal(gp, opinc, ebit, revenue):
    b = pd.concat([_gspread(gp, revenue, 252), _gspread(opinc, revenue, 252), _gspread(ebit, revenue, 252)], axis=1).mean(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapdispr21_slope_v045_signal(opinc, revenue):
    b = pd.concat([_gspread(opinc, revenue, 63), _gspread(opinc, revenue, 126), _gspread(opinc, revenue, 252)], axis=1).std(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swing252r21_slope_v046_signal(opinc, revenue):
    b = (_std(_grow(opinc, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swingebr21_slope_v047_signal(ebit, revenue):
    b = (_std(_grow(ebit, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swinggpr21_slope_v048_signal(gp, revenue):
    b = (_std(_grow(gp, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_rigidr21_slope_v049_signal(opinc, revenue):
    b = (_std(_grow(revenue, 63), 252) / _std(_grow(opinc, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_beta252r21_slope_v050_signal(opinc, revenue):
    go = _grow(opinc, 21)
    gr = _grow(revenue, 21)
    b = (go.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_betaebr21_slope_v051_signal(ebit, revenue):
    ge = _grow(ebit, 21)
    gr = _grow(revenue, 21)
    b = (ge.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_betagpr21_slope_v052_signal(gp, revenue):
    gg = _grow(gp, 21)
    gr = _grow(revenue, 21)
    b = (gg.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_comover21_slope_v053_signal(opinc, revenue):
    b = _grow(opinc, 21).rolling(252, min_periods=63).corr(_grow(revenue, 21))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_fixabsgap252r21_slope_v054_signal(opex, revenue):
    b = _grow(revenue, 252) - _grow(opex, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_fixabsgap126r21_slope_v055_signal(opex, revenue):
    b = _grow(revenue, 126) - _grow(opex, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_costelas252r21_slope_v056_signal(opex, revenue):
    b = _mean(_dol(opex, revenue, 252).clip(-15, 15), 63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_costelas126r21_slope_v057_signal(opex, revenue):
    b = _z(_dol(opex, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_opexgap252r21_slope_v058_signal(opex, revenue):
    b = _rank(_gspread(opex, revenue, 252), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_absel252r21_slope_v059_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    b = _rank(((r - r.shift(252)) / _grow(revenue, 252).replace(0, np.nan)).clip(-5, 5), 504)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_stick252r21_slope_v060_signal(opex, revenue):
    gox = _grow(opex, 252)
    b = gox.where(_grow(revenue, 252) < 0, 0.0).rolling(126, min_periods=42).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_mos252r21_slope_v061_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _mean((1.0 - be / revenue.replace(0, np.nan)).clip(-5, 5), 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gear252r21_slope_v062_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _mean((revenue / (revenue - be).replace(0, np.nan)).clip(-50, 50), 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_begap252r21_slope_v063_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _grow(revenue, 252) - _grow(be, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_geardriver21_slope_v064_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    g = (revenue / (revenue - be).replace(0, np.nan)).clip(-50, 50)
    b = g * _grow(revenue, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_covincr21_slope_v065_signal(gp, opex):
    b = (_dgrow(gp, 252) / _dgrow(opex, 252).replace(0, np.nan)).clip(-15, 15)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_besensr21_slope_v066_signal(gp, opex, revenue):
    cm = gp / revenue.replace(0, np.nan)
    be = opex / cm.replace(0, np.nan)
    b = (_grow(be, 126) / (cm - cm.shift(126)).replace(0, np.nan)).clip(-20, 20)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incthrustr21_slope_v067_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 252).clip(-5, 5) * _grow(revenue, 252).abs()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_ebleakr21_slope_v068_signal(ebit, opinc):
    b = _z((_dgrow(ebit, 252) / _dgrow(opinc, 252).replace(0, np.nan)).clip(-15, 15), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapmacdr21_slope_v069_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 126)
    b = g.ewm(span=63, min_periods=21).mean() - g.ewm(span=252, min_periods=63).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_capeffr21_slope_v070_signal(opinc, revenue):
    rz = _gspread(opinc, revenue, 252)
    d = _dol(opinc, revenue, 252).clip(-15, 15)
    b = (rz - (d - 1.0) * _grow(revenue, 252)).clip(-10, 10)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolupr21_slope_v071_signal(opinc, revenue):
    d = _dol(opinc, revenue, 126).clip(-15, 15)
    b = d.where(_grow(revenue, 126) > 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doldnr21_slope_v072_signal(opinc, revenue):
    d = _dol(opinc, revenue, 126).clip(-15, 15)
    b = d.where(_grow(revenue, 126) < 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inccorrr21_slope_v073_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 21).clip(-5, 5).rolling(252, min_periods=63).corr(_grow(revenue, 21))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_loadedr21_slope_v074_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    mos = (1.0 - be / revenue.replace(0, np.nan)).clip(-5, 5)
    gear = (1.0 / mos.replace(0, np.nan)).clip(-50, 50)
    b = _z(gear * _grow(revenue, 126), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolleverr21_slope_v075_signal(opinc, revenue):
    lev = (_dol(opinc, revenue, 126) > 1.0).astype(float)
    b = lev.rolling(252, min_periods=63).mean() - 0.5
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop63r63_slope_v076_signal(opinc, revenue):
    b = _dol(opinc, revenue, 63).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop126r63_slope_v077_signal(opinc, revenue):
    b = _dol(opinc, revenue, 126).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop252r63_slope_v078_signal(opinc, revenue):
    b = _dol(opinc, revenue, 252).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolop504r63_slope_v079_signal(opinc, revenue):
    b = _mean(_dol(opinc, revenue, 504).clip(-15, 15), 63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doleb126r63_slope_v080_signal(ebit, revenue):
    b = _dol(ebit, revenue, 126).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doleb252r63_slope_v081_signal(ebit, revenue):
    b = _rank(_dol(ebit, revenue, 252).clip(-15, 15), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolcogs126r63_slope_v082_signal(gp, revenue):
    cogs = revenue - gp
    b = _z(_dol(cogs, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolcogs252r63_slope_v083_signal(gp, revenue):
    cogs = revenue - gp
    b = _rank(_dol(cogs, revenue, 252).clip(-15, 15), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolmag252r63_slope_v084_signal(opinc, revenue):
    b = _mean(_dol(opinc, revenue, 252).abs().clip(0, 15), 63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolexc252r63_slope_v085_signal(opinc, revenue):
    d = _dol(opinc, revenue, 252).clip(-15, 15) - 1.0
    b = _rank(np.sign(d) * (d.abs() ** 0.5), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doltermshortr63_slope_v086_signal(opinc, revenue):
    b = _dol(opinc, revenue, 63).clip(-15, 15) - _dol(opinc, revenue, 252).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doltermlongr63_slope_v087_signal(opinc, revenue):
    b = _dol(opinc, revenue, 504).clip(-15, 15) - _dol(opinc, revenue, 126).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolz126r63_slope_v088_signal(opinc, revenue):
    b = _z(_dol(opinc, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolratioebr63_slope_v089_signal(ebit, opinc, revenue):
    b = (_dol(ebit, revenue, 252).clip(-15, 15) / _dol(opinc, revenue, 252).clip(-15, 15).replace(0, np.nan)).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolinstabr63_slope_v090_signal(opinc, revenue):
    b = _std(_dol(opinc, revenue, 63).clip(-15, 15), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop63r63_slope_v091_signal(opinc, revenue):
    inc = _incmgn(opinc, revenue, 63).clip(-5, 5)
    b = inc.where(_grow(revenue, 63) > 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop126r63_slope_v092_signal(opinc, revenue):
    b = _rank(_incmgn(opinc, revenue, 126).clip(-5, 5), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop252r63_slope_v093_signal(opinc, revenue):
    b = _z(_incmgn(opinc, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incop504r63_slope_v094_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 504).clip(-5, 5)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incgp126r63_slope_v095_signal(gp, revenue):
    b = _rank(_incmgn(gp, revenue, 126).clip(-3, 3), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incgp252r63_slope_v096_signal(gp, revenue):
    b = _z(_incmgn(gp, revenue, 252).clip(-3, 3), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inceb126r63_slope_v097_signal(ebit, revenue):
    b = _z(_incmgn(ebit, revenue, 126).clip(-5, 5), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inceb252r63_slope_v098_signal(ebit, revenue):
    b = _z(_incmgn(ebit, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incemar63_slope_v099_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 126).clip(-5, 5).ewm(span=126, min_periods=42).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incspreadr63_slope_v100_signal(gp, opinc, revenue):
    b = _incmgn(gp, revenue, 252).clip(-3, 3) - _incmgn(opinc, revenue, 252).clip(-3, 3)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inctermr63_slope_v101_signal(opinc, revenue):
    b = _z(_incmgn(opinc, revenue, 63).clip(-5, 5) - _incmgn(opinc, revenue, 252).clip(-5, 5), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incdispr63_slope_v102_signal(opinc, revenue):
    b = pd.concat([_incmgn(opinc, revenue, 63).clip(-5, 5), _incmgn(opinc, revenue, 126).clip(-5, 5), _incmgn(opinc, revenue, 252).clip(-5, 5)], axis=1).std(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incconsistr63_slope_v103_signal(opinc, revenue):
    agree = (np.sign(_dgrow(opinc, 63)) == np.sign(_dgrow(revenue, 63))).astype(float)
    b = agree.rolling(252, min_periods=63).mean() - 0.5
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incopex252r63_slope_v104_signal(opex, revenue):
    b = _z(_incmgn(opex, revenue, 252).clip(-3, 3), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incovhr63_slope_v105_signal(gp, opinc):
    ov = gp - opinc
    b = (_dgrow(ov, 252) / _dgrow(gp, 252).replace(0, np.nan)).clip(-5, 5)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap63r63_slope_v106_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap126r63_slope_v107_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap252r63_slope_v108_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gap504r63_slope_v109_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapeb126r63_slope_v110_signal(ebit, revenue):
    b = _gspread(ebit, revenue, 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapeb252r63_slope_v111_signal(ebit, revenue):
    b = _gspread(ebit, revenue, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapgp126r63_slope_v112_signal(gp, revenue):
    b = _gspread(gp, revenue, 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapgp252r63_slope_v113_signal(gp, revenue):
    b = _gspread(gp, revenue, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapsignmagr63_slope_v114_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapemar63_slope_v115_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 126).ewm(span=189, min_periods=63).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapcascader63_slope_v116_signal(gp, opinc, revenue):
    b = _gspread(opinc, revenue, 252) - _gspread(gp, revenue, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapvolr63_slope_v117_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 252)
    v = _std(_grow(revenue, 63), 252)
    b = (g / v.replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapampr63_slope_v118_signal(opinc, revenue):
    b = _gspread(opinc, revenue, 63).abs().rolling(252, min_periods=63).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapstackr63_slope_v119_signal(gp, opinc, ebit, revenue):
    b = pd.concat([_gspread(gp, revenue, 252), _gspread(opinc, revenue, 252), _gspread(ebit, revenue, 252)], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapdispr63_slope_v120_signal(opinc, revenue):
    b = pd.concat([_gspread(opinc, revenue, 63), _gspread(opinc, revenue, 126), _gspread(opinc, revenue, 252)], axis=1).std(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swing252r63_slope_v121_signal(opinc, revenue):
    b = (_std(_grow(opinc, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swingebr63_slope_v122_signal(ebit, revenue):
    b = (_std(_grow(ebit, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_swinggpr63_slope_v123_signal(gp, revenue):
    b = (_std(_grow(gp, 63), 252) / _std(_grow(revenue, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_rigidr63_slope_v124_signal(opinc, revenue):
    b = (_std(_grow(revenue, 63), 252) / _std(_grow(opinc, 63), 252).replace(0, np.nan)).clip(0, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_beta252r63_slope_v125_signal(opinc, revenue):
    go = _grow(opinc, 21)
    gr = _grow(revenue, 21)
    b = (go.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_betaebr63_slope_v126_signal(ebit, revenue):
    ge = _grow(ebit, 21)
    gr = _grow(revenue, 21)
    b = (ge.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_betagpr63_slope_v127_signal(gp, revenue):
    gg = _grow(gp, 21)
    gr = _grow(revenue, 21)
    b = (gg.rolling(252, min_periods=63).cov(gr) / gr.rolling(252, min_periods=63).var().replace(0, np.nan)).clip(-25, 25)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_comover63_slope_v128_signal(opinc, revenue):
    b = _grow(opinc, 21).rolling(252, min_periods=63).corr(_grow(revenue, 21))
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_fixabsgap252r63_slope_v129_signal(opex, revenue):
    b = _grow(revenue, 252) - _grow(opex, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_fixabsgap126r63_slope_v130_signal(opex, revenue):
    b = _grow(revenue, 126) - _grow(opex, 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_costelas252r63_slope_v131_signal(opex, revenue):
    b = _mean(_dol(opex, revenue, 252).clip(-15, 15), 63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_costelas126r63_slope_v132_signal(opex, revenue):
    b = _z(_dol(opex, revenue, 126).clip(-15, 15), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_opexgap252r63_slope_v133_signal(opex, revenue):
    b = _rank(_gspread(opex, revenue, 252), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_absel252r63_slope_v134_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    b = _rank(((r - r.shift(252)) / _grow(revenue, 252).replace(0, np.nan)).clip(-5, 5), 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_stick252r63_slope_v135_signal(opex, revenue):
    gox = _grow(opex, 252)
    b = gox.where(_grow(revenue, 252) < 0, 0.0).rolling(126, min_periods=42).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_mos252r63_slope_v136_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _mean((1.0 - be / revenue.replace(0, np.nan)).clip(-5, 5), 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gear252r63_slope_v137_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _mean((revenue / (revenue - be).replace(0, np.nan)).clip(-50, 50), 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_begap252r63_slope_v138_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    b = _grow(revenue, 252) - _grow(be, 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_geardriver63_slope_v139_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    g = (revenue / (revenue - be).replace(0, np.nan)).clip(-50, 50)
    b = g * _grow(revenue, 126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_covincr63_slope_v140_signal(gp, opex):
    b = (_dgrow(gp, 252) / _dgrow(opex, 252).replace(0, np.nan)).clip(-15, 15)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_besensr63_slope_v141_signal(gp, opex, revenue):
    cm = gp / revenue.replace(0, np.nan)
    be = opex / cm.replace(0, np.nan)
    b = (_grow(be, 126) / (cm - cm.shift(126)).replace(0, np.nan)).clip(-20, 20)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_incthrustr63_slope_v142_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 252).clip(-5, 5) * _grow(revenue, 252).abs()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_ebleakr63_slope_v143_signal(ebit, opinc):
    b = _z((_dgrow(ebit, 252) / _dgrow(opinc, 252).replace(0, np.nan)).clip(-15, 15), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_gapmacdr63_slope_v144_signal(opinc, revenue):
    g = _gspread(opinc, revenue, 126)
    b = g.ewm(span=63, min_periods=21).mean() - g.ewm(span=252, min_periods=63).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_capeffr63_slope_v145_signal(opinc, revenue):
    rz = _gspread(opinc, revenue, 252)
    d = _dol(opinc, revenue, 252).clip(-15, 15)
    b = (rz - (d - 1.0) * _grow(revenue, 252)).clip(-10, 10)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolupr63_slope_v146_signal(opinc, revenue):
    d = _dol(opinc, revenue, 126).clip(-15, 15)
    b = d.where(_grow(revenue, 126) > 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_doldnr63_slope_v147_signal(opinc, revenue):
    d = _dol(opinc, revenue, 126).clip(-15, 15)
    b = d.where(_grow(revenue, 126) < 0).rolling(252, min_periods=42).mean()
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_inccorrr63_slope_v148_signal(opinc, revenue):
    b = _incmgn(opinc, revenue, 21).clip(-5, 5).rolling(252, min_periods=63).corr(_grow(revenue, 21))
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_loadedr63_slope_v149_signal(gp, opex, revenue):
    be = _be_rev(gp, opex, revenue)
    mos = (1.0 - be / revenue.replace(0, np.nan)).clip(-5, 5)
    gear = (1.0 / mos.replace(0, np.nan)).clip(-50, 50)
    b = _z(gear * _grow(revenue, 126), 252)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f26ol_f26_operating_leverage_cycle_dolleverr63_slope_v150_signal(opinc, revenue):
    lev = (_dol(opinc, revenue, 126) > 1.0).astype(float)
    b = lev.rolling(252, min_periods=63).mean() - 0.5
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f26ol_f26_operating_leverage_cycle_dolop63r21_slope_v001_signal,
    f26ol_f26_operating_leverage_cycle_dolop126r21_slope_v002_signal,
    f26ol_f26_operating_leverage_cycle_dolop252r21_slope_v003_signal,
    f26ol_f26_operating_leverage_cycle_dolop504r21_slope_v004_signal,
    f26ol_f26_operating_leverage_cycle_doleb126r21_slope_v005_signal,
    f26ol_f26_operating_leverage_cycle_doleb252r21_slope_v006_signal,
    f26ol_f26_operating_leverage_cycle_dolcogs126r21_slope_v007_signal,
    f26ol_f26_operating_leverage_cycle_dolcogs252r21_slope_v008_signal,
    f26ol_f26_operating_leverage_cycle_dolmag252r21_slope_v009_signal,
    f26ol_f26_operating_leverage_cycle_dolexc252r21_slope_v010_signal,
    f26ol_f26_operating_leverage_cycle_doltermshortr21_slope_v011_signal,
    f26ol_f26_operating_leverage_cycle_doltermlongr21_slope_v012_signal,
    f26ol_f26_operating_leverage_cycle_dolz126r21_slope_v013_signal,
    f26ol_f26_operating_leverage_cycle_dolratioebr21_slope_v014_signal,
    f26ol_f26_operating_leverage_cycle_dolinstabr21_slope_v015_signal,
    f26ol_f26_operating_leverage_cycle_incop63r21_slope_v016_signal,
    f26ol_f26_operating_leverage_cycle_incop126r21_slope_v017_signal,
    f26ol_f26_operating_leverage_cycle_incop252r21_slope_v018_signal,
    f26ol_f26_operating_leverage_cycle_incop504r21_slope_v019_signal,
    f26ol_f26_operating_leverage_cycle_incgp126r21_slope_v020_signal,
    f26ol_f26_operating_leverage_cycle_incgp252r21_slope_v021_signal,
    f26ol_f26_operating_leverage_cycle_inceb126r21_slope_v022_signal,
    f26ol_f26_operating_leverage_cycle_inceb252r21_slope_v023_signal,
    f26ol_f26_operating_leverage_cycle_incemar21_slope_v024_signal,
    f26ol_f26_operating_leverage_cycle_incspreadr21_slope_v025_signal,
    f26ol_f26_operating_leverage_cycle_inctermr21_slope_v026_signal,
    f26ol_f26_operating_leverage_cycle_incdispr21_slope_v027_signal,
    f26ol_f26_operating_leverage_cycle_incconsistr21_slope_v028_signal,
    f26ol_f26_operating_leverage_cycle_incopex252r21_slope_v029_signal,
    f26ol_f26_operating_leverage_cycle_incovhr21_slope_v030_signal,
    f26ol_f26_operating_leverage_cycle_gap63r21_slope_v031_signal,
    f26ol_f26_operating_leverage_cycle_gap126r21_slope_v032_signal,
    f26ol_f26_operating_leverage_cycle_gap252r21_slope_v033_signal,
    f26ol_f26_operating_leverage_cycle_gap504r21_slope_v034_signal,
    f26ol_f26_operating_leverage_cycle_gapeb126r21_slope_v035_signal,
    f26ol_f26_operating_leverage_cycle_gapeb252r21_slope_v036_signal,
    f26ol_f26_operating_leverage_cycle_gapgp126r21_slope_v037_signal,
    f26ol_f26_operating_leverage_cycle_gapgp252r21_slope_v038_signal,
    f26ol_f26_operating_leverage_cycle_gapsignmagr21_slope_v039_signal,
    f26ol_f26_operating_leverage_cycle_gapemar21_slope_v040_signal,
    f26ol_f26_operating_leverage_cycle_gapcascader21_slope_v041_signal,
    f26ol_f26_operating_leverage_cycle_gapvolr21_slope_v042_signal,
    f26ol_f26_operating_leverage_cycle_gapampr21_slope_v043_signal,
    f26ol_f26_operating_leverage_cycle_gapstackr21_slope_v044_signal,
    f26ol_f26_operating_leverage_cycle_gapdispr21_slope_v045_signal,
    f26ol_f26_operating_leverage_cycle_swing252r21_slope_v046_signal,
    f26ol_f26_operating_leverage_cycle_swingebr21_slope_v047_signal,
    f26ol_f26_operating_leverage_cycle_swinggpr21_slope_v048_signal,
    f26ol_f26_operating_leverage_cycle_rigidr21_slope_v049_signal,
    f26ol_f26_operating_leverage_cycle_beta252r21_slope_v050_signal,
    f26ol_f26_operating_leverage_cycle_betaebr21_slope_v051_signal,
    f26ol_f26_operating_leverage_cycle_betagpr21_slope_v052_signal,
    f26ol_f26_operating_leverage_cycle_comover21_slope_v053_signal,
    f26ol_f26_operating_leverage_cycle_fixabsgap252r21_slope_v054_signal,
    f26ol_f26_operating_leverage_cycle_fixabsgap126r21_slope_v055_signal,
    f26ol_f26_operating_leverage_cycle_costelas252r21_slope_v056_signal,
    f26ol_f26_operating_leverage_cycle_costelas126r21_slope_v057_signal,
    f26ol_f26_operating_leverage_cycle_opexgap252r21_slope_v058_signal,
    f26ol_f26_operating_leverage_cycle_absel252r21_slope_v059_signal,
    f26ol_f26_operating_leverage_cycle_stick252r21_slope_v060_signal,
    f26ol_f26_operating_leverage_cycle_mos252r21_slope_v061_signal,
    f26ol_f26_operating_leverage_cycle_gear252r21_slope_v062_signal,
    f26ol_f26_operating_leverage_cycle_begap252r21_slope_v063_signal,
    f26ol_f26_operating_leverage_cycle_geardriver21_slope_v064_signal,
    f26ol_f26_operating_leverage_cycle_covincr21_slope_v065_signal,
    f26ol_f26_operating_leverage_cycle_besensr21_slope_v066_signal,
    f26ol_f26_operating_leverage_cycle_incthrustr21_slope_v067_signal,
    f26ol_f26_operating_leverage_cycle_ebleakr21_slope_v068_signal,
    f26ol_f26_operating_leverage_cycle_gapmacdr21_slope_v069_signal,
    f26ol_f26_operating_leverage_cycle_capeffr21_slope_v070_signal,
    f26ol_f26_operating_leverage_cycle_dolupr21_slope_v071_signal,
    f26ol_f26_operating_leverage_cycle_doldnr21_slope_v072_signal,
    f26ol_f26_operating_leverage_cycle_inccorrr21_slope_v073_signal,
    f26ol_f26_operating_leverage_cycle_loadedr21_slope_v074_signal,
    f26ol_f26_operating_leverage_cycle_dolleverr21_slope_v075_signal,
    f26ol_f26_operating_leverage_cycle_dolop63r63_slope_v076_signal,
    f26ol_f26_operating_leverage_cycle_dolop126r63_slope_v077_signal,
    f26ol_f26_operating_leverage_cycle_dolop252r63_slope_v078_signal,
    f26ol_f26_operating_leverage_cycle_dolop504r63_slope_v079_signal,
    f26ol_f26_operating_leverage_cycle_doleb126r63_slope_v080_signal,
    f26ol_f26_operating_leverage_cycle_doleb252r63_slope_v081_signal,
    f26ol_f26_operating_leverage_cycle_dolcogs126r63_slope_v082_signal,
    f26ol_f26_operating_leverage_cycle_dolcogs252r63_slope_v083_signal,
    f26ol_f26_operating_leverage_cycle_dolmag252r63_slope_v084_signal,
    f26ol_f26_operating_leverage_cycle_dolexc252r63_slope_v085_signal,
    f26ol_f26_operating_leverage_cycle_doltermshortr63_slope_v086_signal,
    f26ol_f26_operating_leverage_cycle_doltermlongr63_slope_v087_signal,
    f26ol_f26_operating_leverage_cycle_dolz126r63_slope_v088_signal,
    f26ol_f26_operating_leverage_cycle_dolratioebr63_slope_v089_signal,
    f26ol_f26_operating_leverage_cycle_dolinstabr63_slope_v090_signal,
    f26ol_f26_operating_leverage_cycle_incop63r63_slope_v091_signal,
    f26ol_f26_operating_leverage_cycle_incop126r63_slope_v092_signal,
    f26ol_f26_operating_leverage_cycle_incop252r63_slope_v093_signal,
    f26ol_f26_operating_leverage_cycle_incop504r63_slope_v094_signal,
    f26ol_f26_operating_leverage_cycle_incgp126r63_slope_v095_signal,
    f26ol_f26_operating_leverage_cycle_incgp252r63_slope_v096_signal,
    f26ol_f26_operating_leverage_cycle_inceb126r63_slope_v097_signal,
    f26ol_f26_operating_leverage_cycle_inceb252r63_slope_v098_signal,
    f26ol_f26_operating_leverage_cycle_incemar63_slope_v099_signal,
    f26ol_f26_operating_leverage_cycle_incspreadr63_slope_v100_signal,
    f26ol_f26_operating_leverage_cycle_inctermr63_slope_v101_signal,
    f26ol_f26_operating_leverage_cycle_incdispr63_slope_v102_signal,
    f26ol_f26_operating_leverage_cycle_incconsistr63_slope_v103_signal,
    f26ol_f26_operating_leverage_cycle_incopex252r63_slope_v104_signal,
    f26ol_f26_operating_leverage_cycle_incovhr63_slope_v105_signal,
    f26ol_f26_operating_leverage_cycle_gap63r63_slope_v106_signal,
    f26ol_f26_operating_leverage_cycle_gap126r63_slope_v107_signal,
    f26ol_f26_operating_leverage_cycle_gap252r63_slope_v108_signal,
    f26ol_f26_operating_leverage_cycle_gap504r63_slope_v109_signal,
    f26ol_f26_operating_leverage_cycle_gapeb126r63_slope_v110_signal,
    f26ol_f26_operating_leverage_cycle_gapeb252r63_slope_v111_signal,
    f26ol_f26_operating_leverage_cycle_gapgp126r63_slope_v112_signal,
    f26ol_f26_operating_leverage_cycle_gapgp252r63_slope_v113_signal,
    f26ol_f26_operating_leverage_cycle_gapsignmagr63_slope_v114_signal,
    f26ol_f26_operating_leverage_cycle_gapemar63_slope_v115_signal,
    f26ol_f26_operating_leverage_cycle_gapcascader63_slope_v116_signal,
    f26ol_f26_operating_leverage_cycle_gapvolr63_slope_v117_signal,
    f26ol_f26_operating_leverage_cycle_gapampr63_slope_v118_signal,
    f26ol_f26_operating_leverage_cycle_gapstackr63_slope_v119_signal,
    f26ol_f26_operating_leverage_cycle_gapdispr63_slope_v120_signal,
    f26ol_f26_operating_leverage_cycle_swing252r63_slope_v121_signal,
    f26ol_f26_operating_leverage_cycle_swingebr63_slope_v122_signal,
    f26ol_f26_operating_leverage_cycle_swinggpr63_slope_v123_signal,
    f26ol_f26_operating_leverage_cycle_rigidr63_slope_v124_signal,
    f26ol_f26_operating_leverage_cycle_beta252r63_slope_v125_signal,
    f26ol_f26_operating_leverage_cycle_betaebr63_slope_v126_signal,
    f26ol_f26_operating_leverage_cycle_betagpr63_slope_v127_signal,
    f26ol_f26_operating_leverage_cycle_comover63_slope_v128_signal,
    f26ol_f26_operating_leverage_cycle_fixabsgap252r63_slope_v129_signal,
    f26ol_f26_operating_leverage_cycle_fixabsgap126r63_slope_v130_signal,
    f26ol_f26_operating_leverage_cycle_costelas252r63_slope_v131_signal,
    f26ol_f26_operating_leverage_cycle_costelas126r63_slope_v132_signal,
    f26ol_f26_operating_leverage_cycle_opexgap252r63_slope_v133_signal,
    f26ol_f26_operating_leverage_cycle_absel252r63_slope_v134_signal,
    f26ol_f26_operating_leverage_cycle_stick252r63_slope_v135_signal,
    f26ol_f26_operating_leverage_cycle_mos252r63_slope_v136_signal,
    f26ol_f26_operating_leverage_cycle_gear252r63_slope_v137_signal,
    f26ol_f26_operating_leverage_cycle_begap252r63_slope_v138_signal,
    f26ol_f26_operating_leverage_cycle_geardriver63_slope_v139_signal,
    f26ol_f26_operating_leverage_cycle_covincr63_slope_v140_signal,
    f26ol_f26_operating_leverage_cycle_besensr63_slope_v141_signal,
    f26ol_f26_operating_leverage_cycle_incthrustr63_slope_v142_signal,
    f26ol_f26_operating_leverage_cycle_ebleakr63_slope_v143_signal,
    f26ol_f26_operating_leverage_cycle_gapmacdr63_slope_v144_signal,
    f26ol_f26_operating_leverage_cycle_capeffr63_slope_v145_signal,
    f26ol_f26_operating_leverage_cycle_dolupr63_slope_v146_signal,
    f26ol_f26_operating_leverage_cycle_doldnr63_slope_v147_signal,
    f26ol_f26_operating_leverage_cycle_inccorrr63_slope_v148_signal,
    f26ol_f26_operating_leverage_cycle_loadedr63_slope_v149_signal,
    f26ol_f26_operating_leverage_cycle_dolleverr63_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_OPERATING_LEVERAGE_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    revenue = _fund(101, base=2e8, drift=0.01, vol=0.10).rename("revenue")
    opex = _fund(102, base=6e7, drift=0.005, vol=0.07).rename("opex")
    gp = _fund(103, base=9e7, drift=0.008, vol=0.11).rename("gp")
    opinc = _fund(104, base=5e7, drift=0.004, vol=0.16, allow_neg=True).rename("opinc")
    ebit = _fund(105, base=4.5e7, drift=0.004, vol=0.17, allow_neg=True).rename("ebit")

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
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

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
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f26_operating_leverage_cycle_2nd_derivatives_001_150_claude: %d features pass" % n_features)
