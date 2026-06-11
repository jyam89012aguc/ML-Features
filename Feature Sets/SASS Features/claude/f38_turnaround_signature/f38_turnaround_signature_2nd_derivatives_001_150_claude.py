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


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (turnaround signature) =====
def _f38_margin_floor_gap(grossmargin, w):
    lo = _rmin(grossmargin, w)
    return (grossmargin - lo) / (grossmargin.abs() + lo.abs()).replace(0, np.nan)


def _f38_loss_narrow(netinc, w):
    base = _rmin(netinc, w)
    return (netinc - base) / (netinc.abs() + base.abs() + 1.0)


def _f38_fcf_cross(fcf, w):
    lo = _rmin(fcf, w)
    return (fcf - lo) / (fcf.abs() + lo.abs()).replace(0, np.nan)


def _f38_delever(debt, w):
    hi = _rmax(debt, w)
    return (hi - debt) / hi.replace(0, np.nan)


def _f38_rev_stab(revenue, w):
    g = revenue.pct_change()
    return _mean(g, w) / (_std(g, w).replace(0, np.nan))


def _f38_recover_off_low(s, w):
    lo = _rmin(s, w)
    return s / lo.replace(0, np.nan) - 1.0


def f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v001_signal(grossmargin, revenue):
    b = _f38_margin_floor_gap(grossmargin, 252) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(21)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v002_signal(grossmargin, debt):
    b = _f38_margin_floor_gap(grossmargin, 504) + 0.5 * _f38_delever(debt, 504)
    d = b - b.shift(49)
    result = d.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mlift_126d_slope_v003_signal(grossmargin, revenue):
    b = (grossmargin - _rmin(grossmargin, 126)) * (revenue / _rmax(revenue, 126).replace(0, np.nan))
    d = b - b.shift(24)
    result = d.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mliftcash_252d_slope_v004_signal(grossmargin, ncfo):
    c = _f38_recover_off_low(ncfo, 252)
    b = _f38_margin_floor_gap(grossmargin, 252) * np.sign(c) * (c.abs() ** 0.5)
    d = b - b.shift(25)
    result = d.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mz_252d_slope_v005_signal(grossmargin, equity):
    b = _z(grossmargin, 252) * (equity / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(32)
    result = d.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v006_signal(netinc, revenue):
    b = _f38_loss_narrow(netinc, 252) * (1.0 - np.tanh(5.0 * (netinc / revenue.replace(0, np.nan))))
    d = b - b.shift(22)
    result = d.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v007_signal(netinc, fcf):
    b = _f38_loss_narrow(netinc, 504) * (1.0 + _f38_fcf_cross(fcf, 504))
    d = b - b.shift(50)
    result = d.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nirecov_252d_slope_v008_signal(netinc, revenue):
    b = (netinc - _rmin(netinc, 252)) / _mean(revenue, 252).replace(0, np.nan)
    d = b - b.shift(36)
    result = d.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_252d_slope_v009_signal(fcf, equity):
    b = _f38_fcf_cross(fcf, 252) + np.tanh(fcf / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(26)
    result = d.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_504d_slope_v010_signal(fcf, revenue):
    b = _f38_fcf_cross(fcf, 504) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(54)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v011_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    b = fm - _rmin(fm, 252)
    d = b - b.shift(23)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncforec_252d_slope_v012_signal(ncfo, debt):
    b = _f38_fcf_cross(ncfo, 252) * (0.5 + _f38_delever(debt, 252))
    d = b - b.shift(30)
    result = d.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_252d_slope_v013_signal(debt, revenue):
    b = _f38_delever(debt, 252) * np.tanh(_f38_rev_stab(revenue, 252))
    d = b - b.shift(37)
    result = d.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_504d_slope_v014_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    b = _z(-lev, 252) + np.tanh(_f38_recover_off_low(equity, 504))
    d = b - b.shift(48)
    result = d.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_levimprove_252d_slope_v015_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    hi = _rmax(lev, 252)
    b = (hi - lev) / (hi.abs() + 1.0)
    d = b - b.shift(34)
    result = d.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinrev_252d_slope_v016_signal(revenue, netinc):
    b = np.tanh(_f38_rev_stab(revenue, 252)) * _f38_loss_narrow(netinc, 252)
    d = b - b.shift(24)
    result = d.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_252d_slope_v017_signal(grossmargin, fcf, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_loss_narrow(netinc, 252)) / 3.0
    d = b - b.shift(31)
    result = d.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_504d_slope_v018_signal(grossmargin, ncfo, debt):
    b = (_f38_margin_floor_gap(grossmargin, 504) + _f38_fcf_cross(ncfo, 504)) * (0.5 + _f38_delever(debt, 504))
    d = b - b.shift(42)
    result = d.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_qualconv_252d_slope_v019_signal(ncfo, netinc):
    conv = ncfo / (netinc.abs() + 1.0)
    b = conv - _rmin(conv, 252)
    d = b - b.shift(28)
    result = d.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roerec_252d_slope_v020_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    lo = _rmin(roe, 252)
    b = (roe - lo) / (roe.abs() + lo.abs() + 0.01)
    d = b - b.shift(35)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nmcross_252d_slope_v021_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    b = nm - _rmin(nm, 252)
    d = b - b.shift(25)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_breadth_252d_slope_v022_signal(grossmargin, ncfo, equity):
    s1 = (grossmargin.diff(63) > 0).astype(float)
    s2 = (ncfo.diff(63) > 0).astype(float)
    s3 = (equity.diff(63) > 0).astype(float)
    b = (s1 + s2 + s3).rolling(126, min_periods=63).mean() - 1.5
    d = b - b.shift(32)
    result = d.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevfcf_252d_slope_v023_signal(debt, fcf):
    b = _f38_delever(debt, 252) * (0.5 + _f38_fcf_cross(fcf, 252))
    d = b - b.shift(22)
    result = d.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revmargturn_252d_slope_v024_signal(revenue, grossmargin):
    rg = revenue / _rmin(revenue, 252).replace(0, np.nan) - 1.0
    b = np.tanh(rg) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(29)
    result = d.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_bsheal_504d_slope_v025_signal(equity, debt):
    b = np.tanh(_f38_recover_off_low(equity, 504)) + _f38_delever(debt, 504)
    d = b - b.shift(57)
    result = d.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_cashlead_252d_slope_v026_signal(ncfo, netinc):
    b = np.tanh(_f38_recover_off_low(ncfo, 252)) - np.tanh(_f38_recover_off_low(netinc, 252))
    d = b - b.shift(26)
    result = d.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v027_signal(fcf, equity):
    yld = fcf / equity.replace(0, np.nan)
    lo = _rmin(yld, 252)
    b = (yld - lo) / (yld.abs() + lo.abs() + 0.01)
    d = b - b.shift(33)
    result = d.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v028_signal(debt, revenue):
    ratio = debt / revenue.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    b = (hi - ratio) / (hi.abs() + 0.01)
    d = b - b.shift(23)
    result = d.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distfade_504d_slope_v029_signal(netinc, equity):
    b = np.tanh((netinc - _rmin(netinc, 504)) / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(51)
    result = d.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v030_signal(grossmargin, revenue, equity):
    gp = grossmargin * revenue
    b = (gp - _rmin(gp, 252)) / _mean(equity.abs(), 252).replace(0, np.nan)
    d = b - b.shift(37)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_accrualturn_252d_slope_v031_signal(ncfo, netinc, revenue):
    gap = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = gap - _rmin(gap, 252)
    d = b - b.shift(27)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v032_signal(fcf, debt):
    cov = fcf / debt.replace(0, np.nan)
    lo = _rmin(cov, 252)
    b = (cov - lo) / (cov.abs() + lo.abs() + 0.01)
    d = b - b.shift(34)
    result = d.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v033_signal(equity, debt):
    r = equity / debt.replace(0, np.nan)
    b = _z(r, 126) * np.tanh(_f38_recover_off_low(equity, 252))
    d = b - b.shift(24)
    result = d.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v034_signal(ncfo, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    b = _z(cm, 126) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(31)
    result = d.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_allengine_252d_slope_v035_signal(grossmargin, fcf, debt, revenue, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_delever(debt, 252) + np.tanh(_f38_rev_stab(revenue, 252)) + _f38_loss_narrow(netinc, 252)) / 5.0
    d = b - b.shift(21)
    result = d.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v036_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    g = gp.pct_change(63)
    b = np.tanh(g - _rmin(g, 252))
    d = b - b.shift(28)
    result = d.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v037_signal(debt, equity):
    nd = debt - equity.clip(lower=0)
    b = -_z(nd, 126) + 0.5 * _f38_delever(debt, 252)
    d = b - b.shift(35)
    result = d.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roacaprec_252d_slope_v038_signal(netinc, equity, debt):
    cap = (equity.abs() + debt.abs()).replace(0, np.nan)
    roa = netinc / cap
    b = np.tanh(10.0 * (roa - _rmin(roa, 252)))
    d = b - b.shift(25)
    result = d.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_durturn_252d_slope_v039_signal(revenue, grossmargin):
    stab = _f38_rev_stab(revenue, 126)
    b = np.tanh(stab - _rmin(stab, 252)) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(32)
    result = d.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_dualturn_252d_slope_v040_signal(grossmargin, revenue):
    rg = revenue.pct_change(21)
    b = _z(grossmargin, 126) + np.tanh(50.0 * (rg - _rmin(rg, 252)))
    d = b - b.shift(22)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_epowerrec_252d_slope_v041_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    znow = _z(nm, 126)
    b = znow - _rmin(znow, 252)
    d = b - b.shift(29)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ndestab_504d_slope_v042_signal(debt, equity, revenue):
    lev = debt / equity.replace(0, np.nan)
    decl = (_rmax(lev, 504) - lev) / (_rmax(lev, 504).abs() + 1.0)
    b = decl * (0.5 + np.tanh(_f38_rev_stab(revenue, 252)))
    d = b - b.shift(57)
    result = d.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v043_signal(ncfo, debt):
    cov = ncfo / debt.replace(0, np.nan)
    b = cov - _rmin(cov, 252)
    d = b - b.shift(26)
    result = d.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mqturn_252d_slope_v044_signal(grossmargin, ncfo):
    msl = _z(grossmargin - grossmargin.shift(63), 126)
    csl = _z(ncfo - ncfo.shift(63), 126)
    b = (msl + csl) / 2.0
    d = b - b.shift(33)
    result = d.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_selffund_252d_slope_v045_signal(ncfo, debt):
    paydown = (-debt.diff(63)).clip(lower=0)
    cover = ncfo / (paydown + _mean(debt, 252) * 0.01).replace(0, np.nan)
    b = cover - _rmin(cover, 252)
    d = b - b.shift(23)
    result = d.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distqual_252d_slope_v046_signal(ncfo, netinc, debt):
    s1 = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    s2 = _f38_loss_narrow(netinc, 252)
    s3 = _f38_delever(debt, 252)
    b = (s1 + s2 + s3) / 3.0
    d = b - b.shift(30)
    result = d.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v047_signal(revenue, ncfo):
    b = np.tanh(_f38_recover_off_low(revenue, 252)) * (0.5 + np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan)))
    d = b - b.shift(37)
    result = d.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinfade_252d_slope_v048_signal(debt, equity, netinc):
    lev = debt / equity.replace(0, np.nan)
    b = np.tanh(-(lev - lev.shift(63))) + _f38_loss_narrow(netinc, 252)
    d = b - b.shift(27)
    result = d.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_floordepth_504d_slope_v049_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 504)
    depth = (_mean(grossmargin, 504) - lo).clip(lower=0)
    b = (grossmargin - lo) * np.tanh(depth) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(55)
    result = d.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v050_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    b = gp / _mean(gp, 252).replace(0, np.nan)
    d = b - b.shift(24)
    result = d.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v051_signal(grossmargin, revenue):
    b = _f38_margin_floor_gap(grossmargin, 252) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(63)
    dn = d / (_std(b, 189).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v052_signal(grossmargin, debt):
    b = _f38_margin_floor_gap(grossmargin, 504) + 0.5 * _f38_delever(debt, 504)
    d = b - b.shift(70)
    dn = d / (_std(b, 210).replace(0, np.nan))
    result = dn - dn.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mlift_126d_slope_v053_signal(grossmargin, revenue):
    b = (grossmargin - _rmin(grossmargin, 126)) * (revenue / _rmax(revenue, 126).replace(0, np.nan))
    d = b - b.shift(35)
    dn = d / (_std(b, 105).replace(0, np.nan))
    result = dn - dn.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mliftcash_252d_slope_v054_signal(grossmargin, ncfo):
    c = _f38_recover_off_low(ncfo, 252)
    b = _f38_margin_floor_gap(grossmargin, 252) * np.sign(c) * (c.abs() ** 0.5)
    d = b - b.shift(67)
    dn = d / (_std(b, 201).replace(0, np.nan))
    result = dn - dn.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mz_252d_slope_v055_signal(grossmargin, equity):
    b = _z(grossmargin, 252) * (equity / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(74)
    dn = d / (_std(b, 222).replace(0, np.nan))
    result = dn - dn.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v056_signal(netinc, revenue):
    b = _f38_loss_narrow(netinc, 252) * (1.0 - np.tanh(5.0 * (netinc / revenue.replace(0, np.nan))))
    d = b - b.shift(64)
    dn = d / (_std(b, 192).replace(0, np.nan))
    result = dn - dn.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v057_signal(netinc, fcf):
    b = _f38_loss_narrow(netinc, 504) * (1.0 + _f38_fcf_cross(fcf, 504))
    d = b - b.shift(71)
    dn = d / (_std(b, 213).replace(0, np.nan))
    result = dn - dn.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nirecov_252d_slope_v058_signal(netinc, revenue):
    b = (netinc - _rmin(netinc, 252)) / _mean(revenue, 252).replace(0, np.nan)
    d = b - b.shift(78)
    dn = d / (_std(b, 234).replace(0, np.nan))
    result = dn - dn.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_252d_slope_v059_signal(fcf, equity):
    b = _f38_fcf_cross(fcf, 252) + np.tanh(fcf / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(68)
    dn = d / (_std(b, 204).replace(0, np.nan))
    result = dn - dn.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_504d_slope_v060_signal(fcf, revenue):
    b = _f38_fcf_cross(fcf, 504) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(75)
    dn = d / (_std(b, 225).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v061_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    b = fm - _rmin(fm, 252)
    d = b - b.shift(65)
    dn = d / (_std(b, 195).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncforec_252d_slope_v062_signal(ncfo, debt):
    b = _f38_fcf_cross(ncfo, 252) * (0.5 + _f38_delever(debt, 252))
    d = b - b.shift(72)
    dn = d / (_std(b, 216).replace(0, np.nan))
    result = dn - dn.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_252d_slope_v063_signal(debt, revenue):
    b = _f38_delever(debt, 252) * np.tanh(_f38_rev_stab(revenue, 252))
    d = b - b.shift(79)
    dn = d / (_std(b, 237).replace(0, np.nan))
    result = dn - dn.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_504d_slope_v064_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    b = _z(-lev, 252) + np.tanh(_f38_recover_off_low(equity, 504))
    d = b - b.shift(69)
    dn = d / (_std(b, 207).replace(0, np.nan))
    result = dn - dn.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_levimprove_252d_slope_v065_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    hi = _rmax(lev, 252)
    b = (hi - lev) / (hi.abs() + 1.0)
    d = b - b.shift(76)
    dn = d / (_std(b, 228).replace(0, np.nan))
    result = dn - dn.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinrev_252d_slope_v066_signal(revenue, netinc):
    b = np.tanh(_f38_rev_stab(revenue, 252)) * _f38_loss_narrow(netinc, 252)
    d = b - b.shift(66)
    dn = d / (_std(b, 198).replace(0, np.nan))
    result = dn - dn.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_252d_slope_v067_signal(grossmargin, fcf, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_loss_narrow(netinc, 252)) / 3.0
    d = b - b.shift(73)
    dn = d / (_std(b, 219).replace(0, np.nan))
    result = dn - dn.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_504d_slope_v068_signal(grossmargin, ncfo, debt):
    b = (_f38_margin_floor_gap(grossmargin, 504) + _f38_fcf_cross(ncfo, 504)) * (0.5 + _f38_delever(debt, 504))
    d = b - b.shift(63)
    dn = d / (_std(b, 189).replace(0, np.nan))
    result = dn - dn.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_qualconv_252d_slope_v069_signal(ncfo, netinc):
    conv = ncfo / (netinc.abs() + 1.0)
    b = conv - _rmin(conv, 252)
    d = b - b.shift(70)
    dn = d / (_std(b, 210).replace(0, np.nan))
    result = dn - dn.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roerec_252d_slope_v070_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    lo = _rmin(roe, 252)
    b = (roe - lo) / (roe.abs() + lo.abs() + 0.01)
    d = b - b.shift(77)
    dn = d / (_std(b, 231).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nmcross_252d_slope_v071_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    b = nm - _rmin(nm, 252)
    d = b - b.shift(67)
    dn = d / (_std(b, 201).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_breadth_252d_slope_v072_signal(grossmargin, ncfo, equity):
    s1 = (grossmargin.diff(63) > 0).astype(float)
    s2 = (ncfo.diff(63) > 0).astype(float)
    s3 = (equity.diff(63) > 0).astype(float)
    b = (s1 + s2 + s3).rolling(126, min_periods=63).mean() - 1.5
    d = b - b.shift(74)
    dn = d / (_std(b, 222).replace(0, np.nan))
    result = dn - dn.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevfcf_252d_slope_v073_signal(debt, fcf):
    b = _f38_delever(debt, 252) * (0.5 + _f38_fcf_cross(fcf, 252))
    d = b - b.shift(64)
    dn = d / (_std(b, 192).replace(0, np.nan))
    result = dn - dn.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revmargturn_252d_slope_v074_signal(revenue, grossmargin):
    rg = revenue / _rmin(revenue, 252).replace(0, np.nan) - 1.0
    b = np.tanh(rg) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(71)
    dn = d / (_std(b, 213).replace(0, np.nan))
    result = dn - dn.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_bsheal_504d_slope_v075_signal(equity, debt):
    b = np.tanh(_f38_recover_off_low(equity, 504)) + _f38_delever(debt, 504)
    d = b - b.shift(78)
    dn = d / (_std(b, 234).replace(0, np.nan))
    result = dn - dn.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_cashlead_252d_slope_v076_signal(ncfo, netinc):
    b = np.tanh(_f38_recover_off_low(ncfo, 252)) - np.tanh(_f38_recover_off_low(netinc, 252))
    d = b - b.shift(68)
    dn = d / (_std(b, 204).replace(0, np.nan))
    result = dn - dn.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v077_signal(fcf, equity):
    yld = fcf / equity.replace(0, np.nan)
    lo = _rmin(yld, 252)
    b = (yld - lo) / (yld.abs() + lo.abs() + 0.01)
    d = b - b.shift(75)
    dn = d / (_std(b, 225).replace(0, np.nan))
    result = dn - dn.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v078_signal(debt, revenue):
    ratio = debt / revenue.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    b = (hi - ratio) / (hi.abs() + 0.01)
    d = b - b.shift(65)
    dn = d / (_std(b, 195).replace(0, np.nan))
    result = dn - dn.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distfade_504d_slope_v079_signal(netinc, equity):
    b = np.tanh((netinc - _rmin(netinc, 504)) / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(72)
    dn = d / (_std(b, 216).replace(0, np.nan))
    result = dn - dn.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v080_signal(grossmargin, revenue, equity):
    gp = grossmargin * revenue
    b = (gp - _rmin(gp, 252)) / _mean(equity.abs(), 252).replace(0, np.nan)
    d = b - b.shift(79)
    dn = d / (_std(b, 237).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_accrualturn_252d_slope_v081_signal(ncfo, netinc, revenue):
    gap = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = gap - _rmin(gap, 252)
    d = b - b.shift(69)
    dn = d / (_std(b, 207).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v082_signal(fcf, debt):
    cov = fcf / debt.replace(0, np.nan)
    lo = _rmin(cov, 252)
    b = (cov - lo) / (cov.abs() + lo.abs() + 0.01)
    d = b - b.shift(76)
    dn = d / (_std(b, 228).replace(0, np.nan))
    result = dn - dn.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v083_signal(equity, debt):
    r = equity / debt.replace(0, np.nan)
    b = _z(r, 126) * np.tanh(_f38_recover_off_low(equity, 252))
    d = b - b.shift(66)
    dn = d / (_std(b, 198).replace(0, np.nan))
    result = dn - dn.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v084_signal(ncfo, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    b = _z(cm, 126) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(73)
    dn = d / (_std(b, 219).replace(0, np.nan))
    result = dn - dn.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_allengine_252d_slope_v085_signal(grossmargin, fcf, debt, revenue, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_delever(debt, 252) + np.tanh(_f38_rev_stab(revenue, 252)) + _f38_loss_narrow(netinc, 252)) / 5.0
    d = b - b.shift(63)
    dn = d / (_std(b, 189).replace(0, np.nan))
    result = dn - dn.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v086_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    g = gp.pct_change(63)
    b = np.tanh(g - _rmin(g, 252))
    d = b - b.shift(70)
    dn = d / (_std(b, 210).replace(0, np.nan))
    result = dn - dn.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v087_signal(debt, equity):
    nd = debt - equity.clip(lower=0)
    b = -_z(nd, 126) + 0.5 * _f38_delever(debt, 252)
    d = b - b.shift(77)
    dn = d / (_std(b, 231).replace(0, np.nan))
    result = dn - dn.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roacaprec_252d_slope_v088_signal(netinc, equity, debt):
    cap = (equity.abs() + debt.abs()).replace(0, np.nan)
    roa = netinc / cap
    b = np.tanh(10.0 * (roa - _rmin(roa, 252)))
    d = b - b.shift(67)
    dn = d / (_std(b, 201).replace(0, np.nan))
    result = dn - dn.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_durturn_252d_slope_v089_signal(revenue, grossmargin):
    stab = _f38_rev_stab(revenue, 126)
    b = np.tanh(stab - _rmin(stab, 252)) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(74)
    dn = d / (_std(b, 222).replace(0, np.nan))
    result = dn - dn.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_dualturn_252d_slope_v090_signal(grossmargin, revenue):
    rg = revenue.pct_change(21)
    b = _z(grossmargin, 126) + np.tanh(50.0 * (rg - _rmin(rg, 252)))
    d = b - b.shift(64)
    dn = d / (_std(b, 192).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_epowerrec_252d_slope_v091_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    znow = _z(nm, 126)
    b = znow - _rmin(znow, 252)
    d = b - b.shift(71)
    dn = d / (_std(b, 213).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ndestab_504d_slope_v092_signal(debt, equity, revenue):
    lev = debt / equity.replace(0, np.nan)
    decl = (_rmax(lev, 504) - lev) / (_rmax(lev, 504).abs() + 1.0)
    b = decl * (0.5 + np.tanh(_f38_rev_stab(revenue, 252)))
    d = b - b.shift(78)
    dn = d / (_std(b, 234).replace(0, np.nan))
    result = dn - dn.ewm(span=13, min_periods=6).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v093_signal(ncfo, debt):
    cov = ncfo / debt.replace(0, np.nan)
    b = cov - _rmin(cov, 252)
    d = b - b.shift(68)
    dn = d / (_std(b, 204).replace(0, np.nan))
    result = dn - dn.ewm(span=34, min_periods=17).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mqturn_252d_slope_v094_signal(grossmargin, ncfo):
    msl = _z(grossmargin - grossmargin.shift(63), 126)
    csl = _z(ncfo - ncfo.shift(63), 126)
    b = (msl + csl) / 2.0
    d = b - b.shift(75)
    dn = d / (_std(b, 225).replace(0, np.nan))
    result = dn - dn.ewm(span=8, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_selffund_252d_slope_v095_signal(ncfo, debt):
    paydown = (-debt.diff(63)).clip(lower=0)
    cover = ncfo / (paydown + _mean(debt, 252) * 0.01).replace(0, np.nan)
    b = cover - _rmin(cover, 252)
    d = b - b.shift(65)
    dn = d / (_std(b, 195).replace(0, np.nan))
    result = dn - dn.ewm(span=26, min_periods=13).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distqual_252d_slope_v096_signal(ncfo, netinc, debt):
    s1 = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    s2 = _f38_loss_narrow(netinc, 252)
    s3 = _f38_delever(debt, 252)
    b = (s1 + s2 + s3) / 3.0
    d = b - b.shift(72)
    dn = d / (_std(b, 216).replace(0, np.nan))
    result = dn - dn.ewm(span=17, min_periods=8).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v097_signal(revenue, ncfo):
    b = np.tanh(_f38_recover_off_low(revenue, 252)) * (0.5 + np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan)))
    d = b - b.shift(79)
    dn = d / (_std(b, 237).replace(0, np.nan))
    result = dn - dn.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinfade_252d_slope_v098_signal(debt, equity, netinc):
    lev = debt / equity.replace(0, np.nan)
    b = np.tanh(-(lev - lev.shift(63))) + _f38_loss_narrow(netinc, 252)
    d = b - b.shift(69)
    dn = d / (_std(b, 207).replace(0, np.nan))
    result = dn - dn.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_floordepth_504d_slope_v099_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 504)
    depth = (_mean(grossmargin, 504) - lo).clip(lower=0)
    b = (grossmargin - lo) * np.tanh(depth) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(76)
    dn = d / (_std(b, 228).replace(0, np.nan))
    result = dn - dn.ewm(span=30, min_periods=15).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v100_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    b = gp / _mean(gp, 252).replace(0, np.nan)
    d = b - b.shift(66)
    dn = d / (_std(b, 198).replace(0, np.nan))
    result = dn - dn.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v101_signal(grossmargin, revenue):
    b = _f38_margin_floor_gap(grossmargin, 252) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(126)
    result = _rank(d, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v102_signal(grossmargin, debt):
    b = _f38_margin_floor_gap(grossmargin, 504) + 0.5 * _f38_delever(debt, 504)
    d = b - b.shift(133)
    result = _rank(d, 399)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mlift_126d_slope_v103_signal(grossmargin, revenue):
    b = (grossmargin - _rmin(grossmargin, 126)) * (revenue / _rmax(revenue, 126).replace(0, np.nan))
    d = b - b.shift(56)
    result = _rank(d, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mliftcash_252d_slope_v104_signal(grossmargin, ncfo):
    c = _f38_recover_off_low(ncfo, 252)
    b = _f38_margin_floor_gap(grossmargin, 252) * np.sign(c) * (c.abs() ** 0.5)
    d = b - b.shift(130)
    result = _rank(d, 390)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mz_252d_slope_v105_signal(grossmargin, equity):
    b = _z(grossmargin, 252) * (equity / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(137)
    result = _rank(d, 411)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v106_signal(netinc, revenue):
    b = _f38_loss_narrow(netinc, 252) * (1.0 - np.tanh(5.0 * (netinc / revenue.replace(0, np.nan))))
    d = b - b.shift(127)
    result = _rank(d, 381)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v107_signal(netinc, fcf):
    b = _f38_loss_narrow(netinc, 504) * (1.0 + _f38_fcf_cross(fcf, 504))
    d = b - b.shift(134)
    result = _rank(d, 402)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nirecov_252d_slope_v108_signal(netinc, revenue):
    b = (netinc - _rmin(netinc, 252)) / _mean(revenue, 252).replace(0, np.nan)
    d = b - b.shift(141)
    result = _rank(d, 423)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_252d_slope_v109_signal(fcf, equity):
    b = _f38_fcf_cross(fcf, 252) + np.tanh(fcf / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(131)
    result = _rank(d, 393)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfcross_504d_slope_v110_signal(fcf, revenue):
    b = _f38_fcf_cross(fcf, 504) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(138)
    result = _rank(d, 414)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v111_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    b = fm - _rmin(fm, 252)
    d = b - b.shift(128)
    result = _rank(d, 384)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncforec_252d_slope_v112_signal(ncfo, debt):
    b = _f38_fcf_cross(ncfo, 252) * (0.5 + _f38_delever(debt, 252))
    d = b - b.shift(135)
    result = _rank(d, 405)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_252d_slope_v113_signal(debt, revenue):
    b = _f38_delever(debt, 252) * np.tanh(_f38_rev_stab(revenue, 252))
    d = b - b.shift(142)
    result = _rank(d, 426)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevstab_504d_slope_v114_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    b = _z(-lev, 252) + np.tanh(_f38_recover_off_low(equity, 504))
    d = b - b.shift(132)
    result = _rank(d, 396)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_levimprove_252d_slope_v115_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    hi = _rmax(lev, 252)
    b = (hi - lev) / (hi.abs() + 1.0)
    d = b - b.shift(139)
    result = _rank(d, 417)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinrev_252d_slope_v116_signal(revenue, netinc):
    b = np.tanh(_f38_rev_stab(revenue, 252)) * _f38_loss_narrow(netinc, 252)
    d = b - b.shift(129)
    result = _rank(d, 387)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_252d_slope_v117_signal(grossmargin, fcf, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_loss_narrow(netinc, 252)) / 3.0
    d = b - b.shift(136)
    result = _rank(d, 408)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_recovcomp_504d_slope_v118_signal(grossmargin, ncfo, debt):
    b = (_f38_margin_floor_gap(grossmargin, 504) + _f38_fcf_cross(ncfo, 504)) * (0.5 + _f38_delever(debt, 504))
    d = b - b.shift(126)
    result = _rank(d, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_qualconv_252d_slope_v119_signal(ncfo, netinc):
    conv = ncfo / (netinc.abs() + 1.0)
    b = conv - _rmin(conv, 252)
    d = b - b.shift(133)
    result = _rank(d, 399)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roerec_252d_slope_v120_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    lo = _rmin(roe, 252)
    b = (roe - lo) / (roe.abs() + lo.abs() + 0.01)
    d = b - b.shift(140)
    result = _rank(d, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_nmcross_252d_slope_v121_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    b = nm - _rmin(nm, 252)
    d = b - b.shift(130)
    result = _rank(d, 390)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_breadth_252d_slope_v122_signal(grossmargin, ncfo, equity):
    s1 = (grossmargin.diff(63) > 0).astype(float)
    s2 = (ncfo.diff(63) > 0).astype(float)
    s3 = (equity.diff(63) > 0).astype(float)
    b = (s1 + s2 + s3).rolling(126, min_periods=63).mean() - 1.5
    d = b - b.shift(137)
    result = _rank(d, 411)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_delevfcf_252d_slope_v123_signal(debt, fcf):
    b = _f38_delever(debt, 252) * (0.5 + _f38_fcf_cross(fcf, 252))
    d = b - b.shift(127)
    result = _rank(d, 381)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revmargturn_252d_slope_v124_signal(revenue, grossmargin):
    rg = revenue / _rmin(revenue, 252).replace(0, np.nan) - 1.0
    b = np.tanh(rg) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(134)
    result = _rank(d, 402)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_bsheal_504d_slope_v125_signal(equity, debt):
    b = np.tanh(_f38_recover_off_low(equity, 504)) + _f38_delever(debt, 504)
    d = b - b.shift(141)
    result = _rank(d, 423)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_cashlead_252d_slope_v126_signal(ncfo, netinc):
    b = np.tanh(_f38_recover_off_low(ncfo, 252)) - np.tanh(_f38_recover_off_low(netinc, 252))
    d = b - b.shift(131)
    result = _rank(d, 393)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v127_signal(fcf, equity):
    yld = fcf / equity.replace(0, np.nan)
    lo = _rmin(yld, 252)
    b = (yld - lo) / (yld.abs() + lo.abs() + 0.01)
    d = b - b.shift(138)
    result = _rank(d, 414)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v128_signal(debt, revenue):
    ratio = debt / revenue.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    b = (hi - ratio) / (hi.abs() + 0.01)
    d = b - b.shift(128)
    result = _rank(d, 384)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distfade_504d_slope_v129_signal(netinc, equity):
    b = np.tanh((netinc - _rmin(netinc, 504)) / _mean(equity.abs(), 252).replace(0, np.nan))
    d = b - b.shift(135)
    result = _rank(d, 405)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v130_signal(grossmargin, revenue, equity):
    gp = grossmargin * revenue
    b = (gp - _rmin(gp, 252)) / _mean(equity.abs(), 252).replace(0, np.nan)
    d = b - b.shift(142)
    result = _rank(d, 426)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_accrualturn_252d_slope_v131_signal(ncfo, netinc, revenue):
    gap = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = gap - _rmin(gap, 252)
    d = b - b.shift(132)
    result = _rank(d, 396)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v132_signal(fcf, debt):
    cov = fcf / debt.replace(0, np.nan)
    lo = _rmin(cov, 252)
    b = (cov - lo) / (cov.abs() + lo.abs() + 0.01)
    d = b - b.shift(139)
    result = _rank(d, 417)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v133_signal(equity, debt):
    r = equity / debt.replace(0, np.nan)
    b = _z(r, 126) * np.tanh(_f38_recover_off_low(equity, 252))
    d = b - b.shift(129)
    result = _rank(d, 387)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v134_signal(ncfo, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    b = _z(cm, 126) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(136)
    result = _rank(d, 408)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_allengine_252d_slope_v135_signal(grossmargin, fcf, debt, revenue, netinc):
    b = (_f38_margin_floor_gap(grossmargin, 252) + _f38_fcf_cross(fcf, 252) + _f38_delever(debt, 252) + np.tanh(_f38_rev_stab(revenue, 252)) + _f38_loss_narrow(netinc, 252)) / 5.0
    d = b - b.shift(126)
    result = _rank(d, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v136_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    g = gp.pct_change(63)
    b = np.tanh(g - _rmin(g, 252))
    d = b - b.shift(133)
    result = _rank(d, 399)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v137_signal(debt, equity):
    nd = debt - equity.clip(lower=0)
    b = -_z(nd, 126) + 0.5 * _f38_delever(debt, 252)
    d = b - b.shift(140)
    result = _rank(d, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_roacaprec_252d_slope_v138_signal(netinc, equity, debt):
    cap = (equity.abs() + debt.abs()).replace(0, np.nan)
    roa = netinc / cap
    b = np.tanh(10.0 * (roa - _rmin(roa, 252)))
    d = b - b.shift(130)
    result = _rank(d, 390)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_durturn_252d_slope_v139_signal(revenue, grossmargin):
    stab = _f38_rev_stab(revenue, 126)
    b = np.tanh(stab - _rmin(stab, 252)) * _f38_margin_floor_gap(grossmargin, 252)
    d = b - b.shift(137)
    result = _rank(d, 411)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_dualturn_252d_slope_v140_signal(grossmargin, revenue):
    rg = revenue.pct_change(21)
    b = _z(grossmargin, 126) + np.tanh(50.0 * (rg - _rmin(rg, 252)))
    d = b - b.shift(127)
    result = _rank(d, 381)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_epowerrec_252d_slope_v141_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    znow = _z(nm, 126)
    b = znow - _rmin(znow, 252)
    d = b - b.shift(134)
    result = _rank(d, 402)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ndestab_504d_slope_v142_signal(debt, equity, revenue):
    lev = debt / equity.replace(0, np.nan)
    decl = (_rmax(lev, 504) - lev) / (_rmax(lev, 504).abs() + 1.0)
    b = decl * (0.5 + np.tanh(_f38_rev_stab(revenue, 252)))
    d = b - b.shift(141)
    result = _rank(d, 423)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v143_signal(ncfo, debt):
    cov = ncfo / debt.replace(0, np.nan)
    b = cov - _rmin(cov, 252)
    d = b - b.shift(131)
    result = _rank(d, 393)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_mqturn_252d_slope_v144_signal(grossmargin, ncfo):
    msl = _z(grossmargin - grossmargin.shift(63), 126)
    csl = _z(ncfo - ncfo.shift(63), 126)
    b = (msl + csl) / 2.0
    d = b - b.shift(138)
    result = _rank(d, 414)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_selffund_252d_slope_v145_signal(ncfo, debt):
    paydown = (-debt.diff(63)).clip(lower=0)
    cover = ncfo / (paydown + _mean(debt, 252) * 0.01).replace(0, np.nan)
    b = cover - _rmin(cover, 252)
    d = b - b.shift(128)
    result = _rank(d, 384)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_distqual_252d_slope_v146_signal(ncfo, netinc, debt):
    s1 = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    s2 = _f38_loss_narrow(netinc, 252)
    s3 = _f38_delever(debt, 252)
    b = (s1 + s2 + s3) / 3.0
    d = b - b.shift(135)
    result = _rank(d, 405)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v147_signal(revenue, ncfo):
    b = np.tanh(_f38_recover_off_low(revenue, 252)) * (0.5 + np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan)))
    d = b - b.shift(142)
    result = _rank(d, 426)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_twinfade_252d_slope_v148_signal(debt, equity, netinc):
    lev = debt / equity.replace(0, np.nan)
    b = np.tanh(-(lev - lev.shift(63))) + _f38_loss_narrow(netinc, 252)
    d = b - b.shift(132)
    result = _rank(d, 396)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_floordepth_504d_slope_v149_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 504)
    depth = (_mean(grossmargin, 504) - lo).clip(lower=0)
    b = (grossmargin - lo) * np.tanh(depth) * (revenue / _mean(revenue, 252).replace(0, np.nan))
    d = b - b.shift(139)
    result = _rank(d, 417)
    return result.replace([np.inf, -np.inf], np.nan)

def f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v150_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    b = gp / _mean(gp, 252).replace(0, np.nan)
    d = b - b.shift(129)
    result = _rank(d, 387)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v001_signal,
    f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v002_signal,
    f38ts_f38_turnaround_signature_mlift_126d_slope_v003_signal,
    f38ts_f38_turnaround_signature_mliftcash_252d_slope_v004_signal,
    f38ts_f38_turnaround_signature_mz_252d_slope_v005_signal,
    f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v006_signal,
    f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v007_signal,
    f38ts_f38_turnaround_signature_nirecov_252d_slope_v008_signal,
    f38ts_f38_turnaround_signature_fcfcross_252d_slope_v009_signal,
    f38ts_f38_turnaround_signature_fcfcross_504d_slope_v010_signal,
    f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v011_signal,
    f38ts_f38_turnaround_signature_ncforec_252d_slope_v012_signal,
    f38ts_f38_turnaround_signature_delevstab_252d_slope_v013_signal,
    f38ts_f38_turnaround_signature_delevstab_504d_slope_v014_signal,
    f38ts_f38_turnaround_signature_levimprove_252d_slope_v015_signal,
    f38ts_f38_turnaround_signature_twinrev_252d_slope_v016_signal,
    f38ts_f38_turnaround_signature_recovcomp_252d_slope_v017_signal,
    f38ts_f38_turnaround_signature_recovcomp_504d_slope_v018_signal,
    f38ts_f38_turnaround_signature_qualconv_252d_slope_v019_signal,
    f38ts_f38_turnaround_signature_roerec_252d_slope_v020_signal,
    f38ts_f38_turnaround_signature_nmcross_252d_slope_v021_signal,
    f38ts_f38_turnaround_signature_breadth_252d_slope_v022_signal,
    f38ts_f38_turnaround_signature_delevfcf_252d_slope_v023_signal,
    f38ts_f38_turnaround_signature_revmargturn_252d_slope_v024_signal,
    f38ts_f38_turnaround_signature_bsheal_504d_slope_v025_signal,
    f38ts_f38_turnaround_signature_cashlead_252d_slope_v026_signal,
    f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v027_signal,
    f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v028_signal,
    f38ts_f38_turnaround_signature_distfade_504d_slope_v029_signal,
    f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v030_signal,
    f38ts_f38_turnaround_signature_accrualturn_252d_slope_v031_signal,
    f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v032_signal,
    f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v033_signal,
    f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v034_signal,
    f38ts_f38_turnaround_signature_allengine_252d_slope_v035_signal,
    f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v036_signal,
    f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v037_signal,
    f38ts_f38_turnaround_signature_roacaprec_252d_slope_v038_signal,
    f38ts_f38_turnaround_signature_durturn_252d_slope_v039_signal,
    f38ts_f38_turnaround_signature_dualturn_252d_slope_v040_signal,
    f38ts_f38_turnaround_signature_epowerrec_252d_slope_v041_signal,
    f38ts_f38_turnaround_signature_ndestab_504d_slope_v042_signal,
    f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v043_signal,
    f38ts_f38_turnaround_signature_mqturn_252d_slope_v044_signal,
    f38ts_f38_turnaround_signature_selffund_252d_slope_v045_signal,
    f38ts_f38_turnaround_signature_distqual_252d_slope_v046_signal,
    f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v047_signal,
    f38ts_f38_turnaround_signature_twinfade_252d_slope_v048_signal,
    f38ts_f38_turnaround_signature_floordepth_504d_slope_v049_signal,
    f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v050_signal,
    f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v051_signal,
    f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v052_signal,
    f38ts_f38_turnaround_signature_mlift_126d_slope_v053_signal,
    f38ts_f38_turnaround_signature_mliftcash_252d_slope_v054_signal,
    f38ts_f38_turnaround_signature_mz_252d_slope_v055_signal,
    f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v056_signal,
    f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v057_signal,
    f38ts_f38_turnaround_signature_nirecov_252d_slope_v058_signal,
    f38ts_f38_turnaround_signature_fcfcross_252d_slope_v059_signal,
    f38ts_f38_turnaround_signature_fcfcross_504d_slope_v060_signal,
    f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v061_signal,
    f38ts_f38_turnaround_signature_ncforec_252d_slope_v062_signal,
    f38ts_f38_turnaround_signature_delevstab_252d_slope_v063_signal,
    f38ts_f38_turnaround_signature_delevstab_504d_slope_v064_signal,
    f38ts_f38_turnaround_signature_levimprove_252d_slope_v065_signal,
    f38ts_f38_turnaround_signature_twinrev_252d_slope_v066_signal,
    f38ts_f38_turnaround_signature_recovcomp_252d_slope_v067_signal,
    f38ts_f38_turnaround_signature_recovcomp_504d_slope_v068_signal,
    f38ts_f38_turnaround_signature_qualconv_252d_slope_v069_signal,
    f38ts_f38_turnaround_signature_roerec_252d_slope_v070_signal,
    f38ts_f38_turnaround_signature_nmcross_252d_slope_v071_signal,
    f38ts_f38_turnaround_signature_breadth_252d_slope_v072_signal,
    f38ts_f38_turnaround_signature_delevfcf_252d_slope_v073_signal,
    f38ts_f38_turnaround_signature_revmargturn_252d_slope_v074_signal,
    f38ts_f38_turnaround_signature_bsheal_504d_slope_v075_signal,
    f38ts_f38_turnaround_signature_cashlead_252d_slope_v076_signal,
    f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v077_signal,
    f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v078_signal,
    f38ts_f38_turnaround_signature_distfade_504d_slope_v079_signal,
    f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v080_signal,
    f38ts_f38_turnaround_signature_accrualturn_252d_slope_v081_signal,
    f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v082_signal,
    f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v083_signal,
    f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v084_signal,
    f38ts_f38_turnaround_signature_allengine_252d_slope_v085_signal,
    f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v086_signal,
    f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v087_signal,
    f38ts_f38_turnaround_signature_roacaprec_252d_slope_v088_signal,
    f38ts_f38_turnaround_signature_durturn_252d_slope_v089_signal,
    f38ts_f38_turnaround_signature_dualturn_252d_slope_v090_signal,
    f38ts_f38_turnaround_signature_epowerrec_252d_slope_v091_signal,
    f38ts_f38_turnaround_signature_ndestab_504d_slope_v092_signal,
    f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v093_signal,
    f38ts_f38_turnaround_signature_mqturn_252d_slope_v094_signal,
    f38ts_f38_turnaround_signature_selffund_252d_slope_v095_signal,
    f38ts_f38_turnaround_signature_distqual_252d_slope_v096_signal,
    f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v097_signal,
    f38ts_f38_turnaround_signature_twinfade_252d_slope_v098_signal,
    f38ts_f38_turnaround_signature_floordepth_504d_slope_v099_signal,
    f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v100_signal,
    f38ts_f38_turnaround_signature_mfloorgap_252d_slope_v101_signal,
    f38ts_f38_turnaround_signature_mfloorgap_504d_slope_v102_signal,
    f38ts_f38_turnaround_signature_mlift_126d_slope_v103_signal,
    f38ts_f38_turnaround_signature_mliftcash_252d_slope_v104_signal,
    f38ts_f38_turnaround_signature_mz_252d_slope_v105_signal,
    f38ts_f38_turnaround_signature_lossnarrow_252d_slope_v106_signal,
    f38ts_f38_turnaround_signature_lossnarrow_504d_slope_v107_signal,
    f38ts_f38_turnaround_signature_nirecov_252d_slope_v108_signal,
    f38ts_f38_turnaround_signature_fcfcross_252d_slope_v109_signal,
    f38ts_f38_turnaround_signature_fcfcross_504d_slope_v110_signal,
    f38ts_f38_turnaround_signature_fcfmargrec_252d_slope_v111_signal,
    f38ts_f38_turnaround_signature_ncforec_252d_slope_v112_signal,
    f38ts_f38_turnaround_signature_delevstab_252d_slope_v113_signal,
    f38ts_f38_turnaround_signature_delevstab_504d_slope_v114_signal,
    f38ts_f38_turnaround_signature_levimprove_252d_slope_v115_signal,
    f38ts_f38_turnaround_signature_twinrev_252d_slope_v116_signal,
    f38ts_f38_turnaround_signature_recovcomp_252d_slope_v117_signal,
    f38ts_f38_turnaround_signature_recovcomp_504d_slope_v118_signal,
    f38ts_f38_turnaround_signature_qualconv_252d_slope_v119_signal,
    f38ts_f38_turnaround_signature_roerec_252d_slope_v120_signal,
    f38ts_f38_turnaround_signature_nmcross_252d_slope_v121_signal,
    f38ts_f38_turnaround_signature_breadth_252d_slope_v122_signal,
    f38ts_f38_turnaround_signature_delevfcf_252d_slope_v123_signal,
    f38ts_f38_turnaround_signature_revmargturn_252d_slope_v124_signal,
    f38ts_f38_turnaround_signature_bsheal_504d_slope_v125_signal,
    f38ts_f38_turnaround_signature_cashlead_252d_slope_v126_signal,
    f38ts_f38_turnaround_signature_fcfyldrec_252d_slope_v127_signal,
    f38ts_f38_turnaround_signature_debtrevheal_252d_slope_v128_signal,
    f38ts_f38_turnaround_signature_distfade_504d_slope_v129_signal,
    f38ts_f38_turnaround_signature_gpdollrec_252d_slope_v130_signal,
    f38ts_f38_turnaround_signature_accrualturn_252d_slope_v131_signal,
    f38ts_f38_turnaround_signature_fcfdebtcov_252d_slope_v132_signal,
    f38ts_f38_turnaround_signature_eqdebtturn_252d_slope_v133_signal,
    f38ts_f38_turnaround_signature_ncfomargturn_252d_slope_v134_signal,
    f38ts_f38_turnaround_signature_allengine_252d_slope_v135_signal,
    f38ts_f38_turnaround_signature_gpgrowthturn_252d_slope_v136_signal,
    f38ts_f38_turnaround_signature_netdebtturn_252d_slope_v137_signal,
    f38ts_f38_turnaround_signature_roacaprec_252d_slope_v138_signal,
    f38ts_f38_turnaround_signature_durturn_252d_slope_v139_signal,
    f38ts_f38_turnaround_signature_dualturn_252d_slope_v140_signal,
    f38ts_f38_turnaround_signature_epowerrec_252d_slope_v141_signal,
    f38ts_f38_turnaround_signature_ndestab_504d_slope_v142_signal,
    f38ts_f38_turnaround_signature_ncfodebtturn_252d_slope_v143_signal,
    f38ts_f38_turnaround_signature_mqturn_252d_slope_v144_signal,
    f38ts_f38_turnaround_signature_selffund_252d_slope_v145_signal,
    f38ts_f38_turnaround_signature_distqual_252d_slope_v146_signal,
    f38ts_f38_turnaround_signature_revtroughcash_252d_slope_v147_signal,
    f38ts_f38_turnaround_signature_twinfade_252d_slope_v148_signal,
    f38ts_f38_turnaround_signature_floordepth_504d_slope_v149_signal,
    f38ts_f38_turnaround_signature_gpdolllvl_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_TURNAROUND_SIGNATURE_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    netinc = _fund(101, base=6e7, drift=0.03, vol=0.16, allow_neg=True, n=n).rename("netinc")
    grossmargin = _fund(102, base=0.35, drift=0.005, vol=0.05, allow_neg=False, n=n).rename("grossmargin")
    revenue = _fund(103, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=n).rename("revenue")
    debt = _fund(104, base=8e7, drift=-0.01, vol=0.06, allow_neg=False, n=n).rename("debt")
    fcf = _fund(105, base=5e7, drift=0.03, vol=0.18, allow_neg=True, n=n).rename("fcf")
    equity = _fund(106, base=1.2e8, drift=0.015, vol=0.05, allow_neg=True, n=n).rename("equity")
    ncfo = _fund(107, base=7e7, drift=0.025, vol=0.13, allow_neg=True, n=n).rename("ncfo")

    cols = {"netinc": netinc, "grossmargin": grossmargin, "revenue": revenue,
            "debt": debt, "fcf": fcf, "equity": equity, "ncfo": ncfo}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f38_turnaround_signature_2nd_derivatives_001_150_claude: %d features pass" % n_features)
