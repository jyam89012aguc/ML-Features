import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _dlog(s, k):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(k).replace(0, np.nan))


# ===== f22 operating-leverage primitives =====
def _f22ol_dol(opinc, revenue, k):
    gr = revenue.pct_change(k)
    go = opinc.pct_change(k)
    return go / gr.replace(0, np.nan)


def _f22ol_dol_ebit(ebit, revenue, k):
    gr = revenue.pct_change(k)
    ge = ebit.pct_change(k)
    return ge / gr.replace(0, np.nan)


def _f22ol_incmargin(opinc, revenue, k):
    do = opinc - opinc.shift(k)
    dr = revenue - revenue.shift(k)
    return do / dr.replace(0, np.nan)


def _f22ol_incgm(gp, revenue, k):
    dg = gp - gp.shift(k)
    dr = revenue - revenue.shift(k)
    return dg / dr.replace(0, np.nan)


def _f22ol_spread_op(opinc, revenue, k):
    return _dlog(opinc, k) - _dlog(revenue, k)


def _f22ol_spread_gp(gp, revenue, k):
    return _dlog(gp, k) - _dlog(revenue, k)


def _f22ol_spread_ebit(ebit, revenue, k):
    return _dlog(ebit, k) - _dlog(revenue, k)


def _f22ol_opexscale(opex, revenue, k):
    r = opex / revenue.replace(0, np.nan)
    return -(r - r.shift(k))


def _f22ol_gpscale(gp, revenue, k):
    r = gp / revenue.replace(0, np.nan)
    return r - r.shift(k)


def _f22ol_fixedabsorb(opinc, opex, k):
    do = opinc - opinc.shift(k)
    dx = opex - opex.shift(k)
    return do / dx.replace(0, np.nan)


def _f22ol_opexelas(opex, revenue, k):
    return _dlog(opex, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpelas(gp, revenue, k):
    return _dlog(gp, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_ebitelas(ebit, revenue, k):
    return _dlog(ebit, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpopxlev(gp, opex, k):
    return _dlog(gp, k) / _dlog(opex, k).replace(0, np.nan)


def _f22ol_flowthru(gp, opinc, k):
    do = opinc - opinc.shift(k)
    dg = gp - gp.shift(k)
    return do / dg.replace(0, np.nan)


def _f22ol_breakeven_rev(opex, gp, revenue, k):
    cm = (gp / revenue.replace(0, np.nan)).rolling(k, min_periods=max(2, k // 2)).mean()
    be = opex / cm.replace(0, np.nan)
    return (revenue - be) / revenue.replace(0, np.nan)


def _f22ol_dolexc(opinc, revenue, k):
    d = _f22ol_dol(opinc, revenue, k) - 1.0
    return np.sign(d) * (d.abs() ** 0.5)


# dolop base, roc 21d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_63d_jerk_v001_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0)
    d1 = base.diff(21) / float(21)
    d = d1.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 28d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_63d_jerk_v002_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 63) / 5.0)
    d1 = base.diff(28) / float(28)
    d = d1.diff(28) / float(28)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_63d_jerk_v003_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 63)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_63d_jerk_v004_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 63)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 21d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_63d_jerk_v005_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 63)
    d1 = base.diff(21) / float(21)
    d = d1.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 28d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_63d_jerk_v006_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 63)
    d1 = base.diff(28) / float(28)
    d = d1.diff(28) / float(28)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_63d_jerk_v007_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 63)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_63d_jerk_v008_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 63)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 21d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_63d_jerk_v009_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(63, min_periods=max(2, 63 // 2)).mean()
    d1 = base.diff(21) / float(21)
    d = d1.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 28d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_63d_jerk_v010_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 63) / 3.0)
    d1 = base.diff(28) / float(28)
    d = d1.diff(28) / float(28)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_63d_jerk_v011_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 63)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_63d_jerk_v012_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(63, min_periods=max(2, 63 // 2)).std()
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 21d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_63d_jerk_v013_signal(gp, opex):
    base = np.tanh((_dlog(opex, 63) / _dlog(gp, 63).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(21) / float(21)
    d = d1.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 28d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_63d_jerk_v014_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 63) / 3.0)
    d1 = base.diff(28) / float(28)
    d = d1.diff(28) / float(28)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_63d_jerk_v015_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 63) / 3.0)
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_63d_jerk_v016_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 63) - _f22ol_spread_op(opinc, revenue, 63))
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# mosbe base, roc 21d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_mosbe_63d_jerk_v017_signal(opex, gp, revenue):
    base = _f22ol_breakeven_rev(opex, gp, revenue, 63)
    d1 = base.diff(21) / float(21)
    d = d1.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opmrg base, roc 28d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opmrg_63d_jerk_v018_signal(opinc, revenue):
    base = (opinc / revenue.replace(0, np.nan)).ewm(span=max(5, 63 // 2), min_periods=max(2, 63 // 4)).mean()
    d1 = base.diff(28) / float(28)
    d = d1.diff(28) / float(28)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# safetygp base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_safetygp_63d_jerk_v019_signal(gp, opex):
    base = ((gp - opex) / gp.replace(0, np.nan)).ewm(span=max(5, 63 // 2), min_periods=max(2, 63 // 4)).mean()
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# ebitmrg base, roc 31d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_ebitmrg_63d_jerk_v020_signal(ebit, revenue):
    base = (ebit / revenue.replace(0, np.nan)).ewm(span=max(5, 63 // 2), min_periods=max(2, 63 // 4)).mean()
    d1 = base.diff(31) / float(31)
    d = d1.diff(31) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 49d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_126d_jerk_v021_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 126) / 5.0)
    d1 = base.diff(49) / float(49)
    d = d1.diff(49) / float(49)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_126d_jerk_v022_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 126) / 5.0)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_126d_jerk_v023_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 126)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 42d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_126d_jerk_v024_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 126)
    d1 = base.diff(42) / float(42)
    d = d1.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 49d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_126d_jerk_v025_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 126)
    d1 = base.diff(49) / float(49)
    d = d1.diff(49) / float(49)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_126d_jerk_v026_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 126)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_126d_jerk_v027_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 126)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 42d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_126d_jerk_v028_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 126)
    d1 = base.diff(42) / float(42)
    d = d1.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 49d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_126d_jerk_v029_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(126, min_periods=max(2, 126 // 2)).mean()
    d1 = base.diff(49) / float(49)
    d = d1.diff(49) / float(49)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_126d_jerk_v030_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 126) / 3.0)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_126d_jerk_v031_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 126)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 42d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_126d_jerk_v032_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(126, min_periods=max(2, 126 // 2)).std()
    d1 = base.diff(42) / float(42)
    d = d1.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 49d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_126d_jerk_v033_signal(gp, opex):
    base = np.tanh((_dlog(opex, 126) / _dlog(gp, 126).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(49) / float(49)
    d = d1.diff(49) / float(49)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_126d_jerk_v034_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 126) / 3.0)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_126d_jerk_v035_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 126) / 3.0)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 42d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_126d_jerk_v036_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 126) - _f22ol_spread_op(opinc, revenue, 126))
    d1 = base.diff(42) / float(42)
    d = d1.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_252d_jerk_v037_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 252) / 5.0)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_252d_jerk_v038_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 252) / 5.0)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_252d_jerk_v039_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 252)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_252d_jerk_v040_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 252)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_252d_jerk_v041_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 252)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_252d_jerk_v042_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 252)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_252d_jerk_v043_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 252)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_252d_jerk_v044_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 252)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_252d_jerk_v045_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(252, min_periods=max(2, 252 // 2)).mean()
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_252d_jerk_v046_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 252) / 3.0)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_252d_jerk_v047_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 252)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_252d_jerk_v048_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(252, min_periods=max(2, 252 // 2)).std()
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_252d_jerk_v049_signal(gp, opex):
    base = np.tanh((_dlog(opex, 252) / _dlog(gp, 252).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_252d_jerk_v050_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 252) / 3.0)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_252d_jerk_v051_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 252) / 3.0)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_252d_jerk_v052_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 252) - _f22ol_spread_op(opinc, revenue, 252))
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# mosbe base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_mosbe_252d_jerk_v053_signal(opex, gp, revenue):
    base = _f22ol_breakeven_rev(opex, gp, revenue, 252)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opmrg base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opmrg_252d_jerk_v054_signal(opinc, revenue):
    base = (opinc / revenue.replace(0, np.nan)).ewm(span=max(5, 252 // 2), min_periods=max(2, 252 // 4)).mean()
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# safetygp base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_safetygp_252d_jerk_v055_signal(gp, opex):
    base = ((gp - opex) / gp.replace(0, np.nan)).ewm(span=max(5, 252 // 2), min_periods=max(2, 252 // 4)).mean()
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# ebitmrg base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_ebitmrg_252d_jerk_v056_signal(ebit, revenue):
    base = (ebit / revenue.replace(0, np.nan)).ewm(span=max(5, 252 // 2), min_periods=max(2, 252 // 4)).mean()
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 189d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_504d_jerk_v057_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 504) / 5.0)
    d1 = base.diff(189) / float(189)
    d = d1.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_504d_jerk_v058_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 504) / 5.0)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 175d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_504d_jerk_v059_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 504)
    d1 = base.diff(175) / float(175)
    d = d1.diff(175) / float(175)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 182d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_504d_jerk_v060_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 504)
    d1 = base.diff(182) / float(182)
    d = d1.diff(182) / float(182)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 189d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_504d_jerk_v061_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 504)
    d1 = base.diff(189) / float(189)
    d = d1.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_504d_jerk_v062_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 504)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 175d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_504d_jerk_v063_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 504)
    d1 = base.diff(175) / float(175)
    d = d1.diff(175) / float(175)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 182d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_504d_jerk_v064_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 504)
    d1 = base.diff(182) / float(182)
    d = d1.diff(182) / float(182)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 189d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_504d_jerk_v065_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(504, min_periods=max(2, 504 // 2)).mean()
    d1 = base.diff(189) / float(189)
    d = d1.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_504d_jerk_v066_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 504) / 3.0)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 175d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_504d_jerk_v067_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 504)
    d1 = base.diff(175) / float(175)
    d = d1.diff(175) / float(175)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 182d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_504d_jerk_v068_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(504, min_periods=max(2, 504 // 2)).std()
    d1 = base.diff(182) / float(182)
    d = d1.diff(182) / float(182)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 189d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_504d_jerk_v069_signal(gp, opex):
    base = np.tanh((_dlog(opex, 504) / _dlog(gp, 504).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(189) / float(189)
    d = d1.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_504d_jerk_v070_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 504) / 3.0)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 175d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_504d_jerk_v071_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 504) / 3.0)
    d1 = base.diff(175) / float(175)
    d = d1.diff(175) / float(175)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 182d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_504d_jerk_v072_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 504) - _f22ol_spread_op(opinc, revenue, 504))
    d1 = base.diff(182) / float(182)
    d = d1.diff(182) / float(182)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# mosbe base, roc 189d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_mosbe_504d_jerk_v073_signal(opex, gp, revenue):
    base = _f22ol_breakeven_rev(opex, gp, revenue, 504)
    d1 = base.diff(189) / float(189)
    d = d1.diff(189) / float(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opmrg base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opmrg_504d_jerk_v074_signal(opinc, revenue):
    base = (opinc / revenue.replace(0, np.nan)).ewm(span=max(5, 504 // 2), min_periods=max(2, 504 // 4)).mean()
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# safetygp base, roc 175d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_safetygp_504d_jerk_v075_signal(gp, opex):
    base = ((gp - opex) / gp.replace(0, np.nan)).ewm(span=max(5, 504 // 2), min_periods=max(2, 504 // 4)).mean()
    d1 = base.diff(175) / float(175)
    d = d1.diff(175) / float(175)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# ebitmrg base, roc 182d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_ebitmrg_504d_jerk_v076_signal(ebit, revenue):
    base = (ebit / revenue.replace(0, np.nan)).ewm(span=max(5, 504 // 2), min_periods=max(2, 504 // 4)).mean()
    d1 = base.diff(182) / float(182)
    d = d1.diff(182) / float(182)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_168d_jerk_v077_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 168) / 5.0)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_168d_jerk_v078_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 168) / 5.0)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_168d_jerk_v079_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 168)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_168d_jerk_v080_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 168)
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_168d_jerk_v081_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 168)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_168d_jerk_v082_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 168)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_168d_jerk_v083_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 168)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_168d_jerk_v084_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 168)
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_168d_jerk_v085_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(168, min_periods=max(2, 168 // 2)).mean()
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_168d_jerk_v086_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 168) / 3.0)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_168d_jerk_v087_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 168)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_168d_jerk_v088_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(168, min_periods=max(2, 168 // 2)).std()
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 56d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_168d_jerk_v089_signal(gp, opex):
    base = np.tanh((_dlog(opex, 168) / _dlog(gp, 168).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(56) / float(56)
    d = d1.diff(56) / float(56)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 63d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_168d_jerk_v090_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 168) / 3.0)
    d1 = base.diff(63) / float(63)
    d = d1.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_168d_jerk_v091_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 168) / 3.0)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_168d_jerk_v092_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 168) - _f22ol_spread_op(opinc, revenue, 168))
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_210d_jerk_v093_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 210) / 5.0)
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_210d_jerk_v094_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 210) / 5.0)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_210d_jerk_v095_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 210)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_210d_jerk_v096_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 210)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_210d_jerk_v097_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 210)
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_210d_jerk_v098_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 210)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_210d_jerk_v099_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 210)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_210d_jerk_v100_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 210)
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_210d_jerk_v101_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(210, min_periods=max(2, 210 // 2)).mean()
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_210d_jerk_v102_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 210) / 3.0)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_210d_jerk_v103_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 210)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_210d_jerk_v104_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(210, min_periods=max(2, 210 // 2)).std()
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 77d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_210d_jerk_v105_signal(gp, opex):
    base = np.tanh((_dlog(opex, 210) / _dlog(gp, 210).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(77) / float(77)
    d = d1.diff(77) / float(77)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 84d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_210d_jerk_v106_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 210) / 3.0)
    d1 = base.diff(84) / float(84)
    d = d1.diff(84) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 91d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_210d_jerk_v107_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 210) / 3.0)
    d1 = base.diff(91) / float(91)
    d = d1.diff(91) / float(91)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 70d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_210d_jerk_v108_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 210) - _f22ol_spread_op(opinc, revenue, 210))
    d1 = base.diff(70) / float(70)
    d = d1.diff(70) / float(70)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_294d_jerk_v109_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 294) / 5.0)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_294d_jerk_v110_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 294) / 5.0)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_294d_jerk_v111_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 294)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_294d_jerk_v112_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 294)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_294d_jerk_v113_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 294)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_294d_jerk_v114_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 294)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_294d_jerk_v115_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 294)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_294d_jerk_v116_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 294)
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolampf base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolampf_294d_jerk_v117_signal(opinc, revenue):
    base = (_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling(294, min_periods=max(2, 294 // 2)).mean()
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# fixlev base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_fixlev_294d_jerk_v118_signal(opinc, opex):
    base = np.tanh(_f22ol_fixedabsorb(opinc, opex, 294) / 3.0)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolexc base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolexc_294d_jerk_v119_signal(opinc, revenue):
    base = _f22ol_dolexc(opinc, revenue, 294)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolopvol base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolopvol_294d_jerk_v120_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling(294, min_periods=max(2, 294 // 2)).std()
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprdrag base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprdrag_294d_jerk_v121_signal(gp, opex):
    base = np.tanh((_dlog(opex, 294) / _dlog(gp, 294).replace(0, np.nan) - 1.0) / 2.0)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# gpopxlev base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_gpopxlev_294d_jerk_v122_signal(gp, opex):
    base = np.tanh(_f22ol_gpopxlev(gp, opex, 294) / 3.0)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# flowthru base, roc 98d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_flowthru_294d_jerk_v123_signal(gp, opinc):
    base = np.tanh(_f22ol_flowthru(gp, opinc, 294) / 3.0)
    d1 = base.diff(98) / float(98)
    d = d1.diff(98) / float(98)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprlinediv base, roc 105d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprlinediv_294d_jerk_v124_signal(ebit, opinc, revenue):
    base = (_f22ol_spread_ebit(ebit, revenue, 294) - _f22ol_spread_op(opinc, revenue, 294))
    d1 = base.diff(105) / float(105)
    d = d1.diff(105) / float(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 133d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_378d_jerk_v125_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 378) / 5.0)
    d1 = base.diff(133) / float(133)
    d = d1.diff(133) / float(133)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 140d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_378d_jerk_v126_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 378) / 5.0)
    d1 = base.diff(140) / float(140)
    d = d1.diff(140) / float(140)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 147d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_378d_jerk_v127_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 378)
    d1 = base.diff(147) / float(147)
    d = d1.diff(147) / float(147)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 126d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_378d_jerk_v128_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 378)
    d1 = base.diff(126) / float(126)
    d = d1.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 133d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_378d_jerk_v129_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 378)
    d1 = base.diff(133) / float(133)
    d = d1.diff(133) / float(133)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 140d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_378d_jerk_v130_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 378)
    d1 = base.diff(140) / float(140)
    d = d1.diff(140) / float(140)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 147d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_378d_jerk_v131_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 378)
    d1 = base.diff(147) / float(147)
    d = d1.diff(147) / float(147)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 126d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_378d_jerk_v132_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 378)
    d1 = base.diff(126) / float(126)
    d = d1.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_336d_jerk_v133_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 336) / 5.0)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 126d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_336d_jerk_v134_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 336) / 5.0)
    d1 = base.diff(126) / float(126)
    d = d1.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 133d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_336d_jerk_v135_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 336)
    d1 = base.diff(133) / float(133)
    d = d1.diff(133) / float(133)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_336d_jerk_v136_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 336)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_336d_jerk_v137_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 336)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 126d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_336d_jerk_v138_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 336)
    d1 = base.diff(126) / float(126)
    d = d1.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 133d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_336d_jerk_v139_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 336)
    d1 = base.diff(133) / float(133)
    d = d1.diff(133) / float(133)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_336d_jerk_v140_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 336)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 154d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_441d_jerk_v141_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 441) / 5.0)
    d1 = base.diff(154) / float(154)
    d = d1.diff(154) / float(154)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 161d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_441d_jerk_v142_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 441) / 5.0)
    d1 = base.diff(161) / float(161)
    d = d1.diff(161) / float(161)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmop base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmop_441d_jerk_v143_signal(opinc, revenue):
    base = _f22ol_incmargin(opinc, revenue, 441)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# incmgp base, roc 147d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_incmgp_441d_jerk_v144_signal(gp, revenue):
    base = _f22ol_incgm(gp, revenue, 441)
    d1 = base.diff(147) / float(147)
    d = d1.diff(147) / float(147)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprop base, roc 154d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprop_441d_jerk_v145_signal(opinc, revenue):
    base = _f22ol_spread_op(opinc, revenue, 441)
    d1 = base.diff(154) / float(154)
    d = d1.diff(154) / float(154)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprgp base, roc 161d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprgp_441d_jerk_v146_signal(gp, revenue):
    base = _f22ol_spread_gp(gp, revenue, 441)
    d1 = base.diff(161) / float(161)
    d = d1.diff(161) / float(161)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# sprebit base, roc 168d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_sprebit_441d_jerk_v147_signal(ebit, revenue):
    base = _f22ol_spread_ebit(ebit, revenue, 441)
    d1 = base.diff(168) / float(168)
    d = d1.diff(168) / float(168)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# opxabs base, roc 147d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_opxabs_441d_jerk_v148_signal(opex, revenue):
    base = _f22ol_opexscale(opex, revenue, 441)
    d1 = base.diff(147) / float(147)
    d = d1.diff(147) / float(147)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolop base, roc 112d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolop_315d_jerk_v149_signal(opinc, revenue):
    base = np.tanh(_f22ol_dol(opinc, revenue, 315) / 5.0)
    d1 = base.diff(112) / float(112)
    d = d1.diff(112) / float(112)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# dolebit base, roc 119d (jerk = 2nd derivative)
def f22ol_f22_operating_leverage_dolebit_315d_jerk_v150_signal(ebit, revenue):
    base = np.tanh(_f22ol_dol_ebit(ebit, revenue, 315) / 5.0)
    d1 = base.diff(119) / float(119)
    d = d1.diff(119) / float(119)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ol_f22_operating_leverage_dolop_63d_jerk_v001_signal,
    f22ol_f22_operating_leverage_dolebit_63d_jerk_v002_signal,
    f22ol_f22_operating_leverage_incmop_63d_jerk_v003_signal,
    f22ol_f22_operating_leverage_incmgp_63d_jerk_v004_signal,
    f22ol_f22_operating_leverage_sprop_63d_jerk_v005_signal,
    f22ol_f22_operating_leverage_sprgp_63d_jerk_v006_signal,
    f22ol_f22_operating_leverage_sprebit_63d_jerk_v007_signal,
    f22ol_f22_operating_leverage_opxabs_63d_jerk_v008_signal,
    f22ol_f22_operating_leverage_dolampf_63d_jerk_v009_signal,
    f22ol_f22_operating_leverage_fixlev_63d_jerk_v010_signal,
    f22ol_f22_operating_leverage_dolexc_63d_jerk_v011_signal,
    f22ol_f22_operating_leverage_dolopvol_63d_jerk_v012_signal,
    f22ol_f22_operating_leverage_sprdrag_63d_jerk_v013_signal,
    f22ol_f22_operating_leverage_gpopxlev_63d_jerk_v014_signal,
    f22ol_f22_operating_leverage_flowthru_63d_jerk_v015_signal,
    f22ol_f22_operating_leverage_sprlinediv_63d_jerk_v016_signal,
    f22ol_f22_operating_leverage_mosbe_63d_jerk_v017_signal,
    f22ol_f22_operating_leverage_opmrg_63d_jerk_v018_signal,
    f22ol_f22_operating_leverage_safetygp_63d_jerk_v019_signal,
    f22ol_f22_operating_leverage_ebitmrg_63d_jerk_v020_signal,
    f22ol_f22_operating_leverage_dolop_126d_jerk_v021_signal,
    f22ol_f22_operating_leverage_dolebit_126d_jerk_v022_signal,
    f22ol_f22_operating_leverage_incmop_126d_jerk_v023_signal,
    f22ol_f22_operating_leverage_incmgp_126d_jerk_v024_signal,
    f22ol_f22_operating_leverage_sprop_126d_jerk_v025_signal,
    f22ol_f22_operating_leverage_sprgp_126d_jerk_v026_signal,
    f22ol_f22_operating_leverage_sprebit_126d_jerk_v027_signal,
    f22ol_f22_operating_leverage_opxabs_126d_jerk_v028_signal,
    f22ol_f22_operating_leverage_dolampf_126d_jerk_v029_signal,
    f22ol_f22_operating_leverage_fixlev_126d_jerk_v030_signal,
    f22ol_f22_operating_leverage_dolexc_126d_jerk_v031_signal,
    f22ol_f22_operating_leverage_dolopvol_126d_jerk_v032_signal,
    f22ol_f22_operating_leverage_sprdrag_126d_jerk_v033_signal,
    f22ol_f22_operating_leverage_gpopxlev_126d_jerk_v034_signal,
    f22ol_f22_operating_leverage_flowthru_126d_jerk_v035_signal,
    f22ol_f22_operating_leverage_sprlinediv_126d_jerk_v036_signal,
    f22ol_f22_operating_leverage_dolop_252d_jerk_v037_signal,
    f22ol_f22_operating_leverage_dolebit_252d_jerk_v038_signal,
    f22ol_f22_operating_leverage_incmop_252d_jerk_v039_signal,
    f22ol_f22_operating_leverage_incmgp_252d_jerk_v040_signal,
    f22ol_f22_operating_leverage_sprop_252d_jerk_v041_signal,
    f22ol_f22_operating_leverage_sprgp_252d_jerk_v042_signal,
    f22ol_f22_operating_leverage_sprebit_252d_jerk_v043_signal,
    f22ol_f22_operating_leverage_opxabs_252d_jerk_v044_signal,
    f22ol_f22_operating_leverage_dolampf_252d_jerk_v045_signal,
    f22ol_f22_operating_leverage_fixlev_252d_jerk_v046_signal,
    f22ol_f22_operating_leverage_dolexc_252d_jerk_v047_signal,
    f22ol_f22_operating_leverage_dolopvol_252d_jerk_v048_signal,
    f22ol_f22_operating_leverage_sprdrag_252d_jerk_v049_signal,
    f22ol_f22_operating_leverage_gpopxlev_252d_jerk_v050_signal,
    f22ol_f22_operating_leverage_flowthru_252d_jerk_v051_signal,
    f22ol_f22_operating_leverage_sprlinediv_252d_jerk_v052_signal,
    f22ol_f22_operating_leverage_mosbe_252d_jerk_v053_signal,
    f22ol_f22_operating_leverage_opmrg_252d_jerk_v054_signal,
    f22ol_f22_operating_leverage_safetygp_252d_jerk_v055_signal,
    f22ol_f22_operating_leverage_ebitmrg_252d_jerk_v056_signal,
    f22ol_f22_operating_leverage_dolop_504d_jerk_v057_signal,
    f22ol_f22_operating_leverage_dolebit_504d_jerk_v058_signal,
    f22ol_f22_operating_leverage_incmop_504d_jerk_v059_signal,
    f22ol_f22_operating_leverage_incmgp_504d_jerk_v060_signal,
    f22ol_f22_operating_leverage_sprop_504d_jerk_v061_signal,
    f22ol_f22_operating_leverage_sprgp_504d_jerk_v062_signal,
    f22ol_f22_operating_leverage_sprebit_504d_jerk_v063_signal,
    f22ol_f22_operating_leverage_opxabs_504d_jerk_v064_signal,
    f22ol_f22_operating_leverage_dolampf_504d_jerk_v065_signal,
    f22ol_f22_operating_leverage_fixlev_504d_jerk_v066_signal,
    f22ol_f22_operating_leverage_dolexc_504d_jerk_v067_signal,
    f22ol_f22_operating_leverage_dolopvol_504d_jerk_v068_signal,
    f22ol_f22_operating_leverage_sprdrag_504d_jerk_v069_signal,
    f22ol_f22_operating_leverage_gpopxlev_504d_jerk_v070_signal,
    f22ol_f22_operating_leverage_flowthru_504d_jerk_v071_signal,
    f22ol_f22_operating_leverage_sprlinediv_504d_jerk_v072_signal,
    f22ol_f22_operating_leverage_mosbe_504d_jerk_v073_signal,
    f22ol_f22_operating_leverage_opmrg_504d_jerk_v074_signal,
    f22ol_f22_operating_leverage_safetygp_504d_jerk_v075_signal,
    f22ol_f22_operating_leverage_ebitmrg_504d_jerk_v076_signal,
    f22ol_f22_operating_leverage_dolop_168d_jerk_v077_signal,
    f22ol_f22_operating_leverage_dolebit_168d_jerk_v078_signal,
    f22ol_f22_operating_leverage_incmop_168d_jerk_v079_signal,
    f22ol_f22_operating_leverage_incmgp_168d_jerk_v080_signal,
    f22ol_f22_operating_leverage_sprop_168d_jerk_v081_signal,
    f22ol_f22_operating_leverage_sprgp_168d_jerk_v082_signal,
    f22ol_f22_operating_leverage_sprebit_168d_jerk_v083_signal,
    f22ol_f22_operating_leverage_opxabs_168d_jerk_v084_signal,
    f22ol_f22_operating_leverage_dolampf_168d_jerk_v085_signal,
    f22ol_f22_operating_leverage_fixlev_168d_jerk_v086_signal,
    f22ol_f22_operating_leverage_dolexc_168d_jerk_v087_signal,
    f22ol_f22_operating_leverage_dolopvol_168d_jerk_v088_signal,
    f22ol_f22_operating_leverage_sprdrag_168d_jerk_v089_signal,
    f22ol_f22_operating_leverage_gpopxlev_168d_jerk_v090_signal,
    f22ol_f22_operating_leverage_flowthru_168d_jerk_v091_signal,
    f22ol_f22_operating_leverage_sprlinediv_168d_jerk_v092_signal,
    f22ol_f22_operating_leverage_dolop_210d_jerk_v093_signal,
    f22ol_f22_operating_leverage_dolebit_210d_jerk_v094_signal,
    f22ol_f22_operating_leverage_incmop_210d_jerk_v095_signal,
    f22ol_f22_operating_leverage_incmgp_210d_jerk_v096_signal,
    f22ol_f22_operating_leverage_sprop_210d_jerk_v097_signal,
    f22ol_f22_operating_leverage_sprgp_210d_jerk_v098_signal,
    f22ol_f22_operating_leverage_sprebit_210d_jerk_v099_signal,
    f22ol_f22_operating_leverage_opxabs_210d_jerk_v100_signal,
    f22ol_f22_operating_leverage_dolampf_210d_jerk_v101_signal,
    f22ol_f22_operating_leverage_fixlev_210d_jerk_v102_signal,
    f22ol_f22_operating_leverage_dolexc_210d_jerk_v103_signal,
    f22ol_f22_operating_leverage_dolopvol_210d_jerk_v104_signal,
    f22ol_f22_operating_leverage_sprdrag_210d_jerk_v105_signal,
    f22ol_f22_operating_leverage_gpopxlev_210d_jerk_v106_signal,
    f22ol_f22_operating_leverage_flowthru_210d_jerk_v107_signal,
    f22ol_f22_operating_leverage_sprlinediv_210d_jerk_v108_signal,
    f22ol_f22_operating_leverage_dolop_294d_jerk_v109_signal,
    f22ol_f22_operating_leverage_dolebit_294d_jerk_v110_signal,
    f22ol_f22_operating_leverage_incmop_294d_jerk_v111_signal,
    f22ol_f22_operating_leverage_incmgp_294d_jerk_v112_signal,
    f22ol_f22_operating_leverage_sprop_294d_jerk_v113_signal,
    f22ol_f22_operating_leverage_sprgp_294d_jerk_v114_signal,
    f22ol_f22_operating_leverage_sprebit_294d_jerk_v115_signal,
    f22ol_f22_operating_leverage_opxabs_294d_jerk_v116_signal,
    f22ol_f22_operating_leverage_dolampf_294d_jerk_v117_signal,
    f22ol_f22_operating_leverage_fixlev_294d_jerk_v118_signal,
    f22ol_f22_operating_leverage_dolexc_294d_jerk_v119_signal,
    f22ol_f22_operating_leverage_dolopvol_294d_jerk_v120_signal,
    f22ol_f22_operating_leverage_sprdrag_294d_jerk_v121_signal,
    f22ol_f22_operating_leverage_gpopxlev_294d_jerk_v122_signal,
    f22ol_f22_operating_leverage_flowthru_294d_jerk_v123_signal,
    f22ol_f22_operating_leverage_sprlinediv_294d_jerk_v124_signal,
    f22ol_f22_operating_leverage_dolop_378d_jerk_v125_signal,
    f22ol_f22_operating_leverage_dolebit_378d_jerk_v126_signal,
    f22ol_f22_operating_leverage_incmop_378d_jerk_v127_signal,
    f22ol_f22_operating_leverage_incmgp_378d_jerk_v128_signal,
    f22ol_f22_operating_leverage_sprop_378d_jerk_v129_signal,
    f22ol_f22_operating_leverage_sprgp_378d_jerk_v130_signal,
    f22ol_f22_operating_leverage_sprebit_378d_jerk_v131_signal,
    f22ol_f22_operating_leverage_opxabs_378d_jerk_v132_signal,
    f22ol_f22_operating_leverage_dolop_336d_jerk_v133_signal,
    f22ol_f22_operating_leverage_dolebit_336d_jerk_v134_signal,
    f22ol_f22_operating_leverage_incmop_336d_jerk_v135_signal,
    f22ol_f22_operating_leverage_incmgp_336d_jerk_v136_signal,
    f22ol_f22_operating_leverage_sprop_336d_jerk_v137_signal,
    f22ol_f22_operating_leverage_sprgp_336d_jerk_v138_signal,
    f22ol_f22_operating_leverage_sprebit_336d_jerk_v139_signal,
    f22ol_f22_operating_leverage_opxabs_336d_jerk_v140_signal,
    f22ol_f22_operating_leverage_dolop_441d_jerk_v141_signal,
    f22ol_f22_operating_leverage_dolebit_441d_jerk_v142_signal,
    f22ol_f22_operating_leverage_incmop_441d_jerk_v143_signal,
    f22ol_f22_operating_leverage_incmgp_441d_jerk_v144_signal,
    f22ol_f22_operating_leverage_sprop_441d_jerk_v145_signal,
    f22ol_f22_operating_leverage_sprgp_441d_jerk_v146_signal,
    f22ol_f22_operating_leverage_sprebit_441d_jerk_v147_signal,
    f22ol_f22_operating_leverage_opxabs_441d_jerk_v148_signal,
    f22ol_f22_operating_leverage_dolop_315d_jerk_v149_signal,
    f22ol_f22_operating_leverage_dolebit_315d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


F22_OPERATING_LEVERAGE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp) * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp) * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _margin(seed, lo, hi, rho=0.995):
        g = np.random.default_rng(seed)
        e = g.normal(0, 0.01, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = rho * ar[t - 1] + e[t]
        m = (ar - ar.min()) / (ar.max() - ar.min() + 1e-9)
        return pd.Series(lo + (hi - lo) * m, name=None)

    revenue = _fund(1, base=1.2e8, drift=0.035, vol=0.06).rename("revenue")
    opex = _fund(2, base=7.0e7, drift=0.030, vol=0.05).rename("opex")
    gp = (revenue * _margin(10, 0.34, 0.62)).rename("gp")
    opinc = (revenue * _margin(11, -0.16, 0.26)).rename("opinc")
    ebit = (revenue * _margin(12, -0.05, 0.27)).rename("ebit")

    cols = {"closeadj": closeadj, "close": close, "open": openp, "high": high,
            "low": low, "volume": volume, "revenue": revenue, "opex": opex,
            "gp": gp, "opinc": opinc, "ebit": ebit}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume", "revenue", "revenueusd",
             "deferredrev", "gp", "grossmargin", "opinc", "opex", "sgna", "cor", "rnd",
             "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc", "netinccmn", "netmargin",
             "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt",
             "ncfbus", "capex", "depamor", "sharesbas", "shareswa", "shareswadil", "assets",
             "assetsc", "tangibles", "intangibles", "ppnenet", "investments", "inventory",
             "receivables", "payables", "equity", "retearn", "workingcapital", "debt", "debtc",
             "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio", "roic", "roe",
             "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps",
             "de", "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis", "marketcap", "ev",
             "evebit", "evebitda", "pe", "pb", "ps", "shrholders", "shrvalue", "shrunits",
             "totalvalue", "percentoftotal", "fndholders", "undholders", "prfholders",
             "dbtholders", "putholders", "putvalue", "cllholders", "cllvalue", "wntholders",
             "wntvalue", "dbtvalue"}
    FUND = {"revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
            "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
            "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
            "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
            "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
            "investments", "inventory", "receivables", "payables", "equity", "retearn",
            "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
            "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
            "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
            "payoutratio", "prefdivis"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        inp = meta["inputs"]
        assert set(inp) <= ALLOW, "%s inputs not in allowlist: %s" % (name, inp)
        assert len(set(inp) & FUND) >= 1, "%s has no fundamental column" % name
        fn = meta["func"]
        args = [cols[c] for c in inp]
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

    print("OK f22_operating_leverage_3rd_derivatives_001_150_claude: %d features pass" % n_features)
