import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _burn_opex(opex, ncfo):
    return (opex - ncfo).clip(lower=0)


def _burn_fcf(ncfo, capex):
    return (-ncfo - capex).clip(lower=0)


def _runway_opex(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _runway_fcf(cashneq, ncfo, capex):
    burn = _burn_fcf(ncfo, capex)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _coverage(ncfo, opex):
    return ncfo / opex.replace(0, np.nan)


def _logwarp(s):
    return np.sign(s) * np.log1p(s.abs())


def f31cr_f31_cash_burn_runway_runwayopx_42d_jerk_v001_signal(cashneq, opex, ncfo):
    base = _mean(_runway_opex(cashneq, opex, ncfo).clip(upper=120.0), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayfcf_42d_jerk_v002_signal(cashneq, ncfo, capex):
    rf = _runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    base = _rank(rf, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnopx_42d_jerk_v003_signal(opex, ncfo):
    base = _mean(np.log1p(_burn_opex(opex, ncfo)), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfcf_42d_jerk_v004_signal(ncfo, capex):
    base = _mean(np.log1p(_burn_fcf(ncfo, capex)), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnintens_42d_jerk_v005_signal(cashneq, opex, ncfo):
    intens = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = intens.ewm(span=42, min_periods=21).mean() - intens.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnintfcf_42d_jerk_v006_signal(cashneq, ncfo, capex):
    base = _mean(_burn_fcf(ncfo, capex) / cashneq.replace(0, np.nan), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfrac_42d_jerk_v007_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    frac = bn / opex.replace(0, np.nan)
    hot = (frac > frac.rolling(252, min_periods=126).median()).astype(float)
    base = hot.rolling(126, min_periods=63).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cover_42d_jerk_v008_signal(ncfo, opex):
    base = _mean(_coverage(ncfo, opex), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covergap_42d_jerk_v009_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = _rmax(cov, 126) - cov
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashcover_42d_jerk_v010_signal(cashneq, ncfo, capex):
    cov = np.log1p((cashneq / _burn_fcf(ncfo, capex).replace(0, np.nan)).clip(lower=0, upper=240.0))
    base = cov.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfcapex_42d_jerk_v011_signal(ncfo, capex):
    r = ncfo / capex.abs().replace(0, np.nan)
    lo = _rmin(r, 252)
    hi = _rmax(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashlevel_42d_jerk_v012_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayz_42d_jerk_v013_signal(cashneq, opex, ncfo):
    base = _z(_runway_opex(cashneq, opex, ncfo).clip(upper=120.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnz_42d_jerk_v014_signal(opex, ncfo, capex):
    base = _z(_burn_fcf(ncfo, capex) / (opex + 1.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverz_42d_jerk_v015_signal(ncfo, opex):
    base = _z(_coverage(ncfo, opex), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashz_42d_jerk_v016_signal(cashneq):
    base = _z(cashneq, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayrank_42d_jerk_v017_signal(cashneq, opex, ncfo):
    base = _rank(_runway_opex(cashneq, opex, ncfo), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfracrank_42d_jerk_v018_signal(opex, ncfo):
    bn = np.log1p(_burn_opex(opex, ncfo))
    base = bn.ewm(span=42, min_periods=21).mean() - bn.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverrank_42d_jerk_v019_signal(ncfo, opex):
    base = _rank(_coverage(ncfo, opex), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysl_42d_jerk_v020_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _mean(rw, 63) / _mean(rw, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnsl_42d_jerk_v021_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean(bn, 63) / _mean(bn, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashsl_42d_jerk_v022_signal(cashneq):
    base = _mean(cashneq, 63) / _mean(cashneq, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayvol_42d_jerk_v023_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _std(rw, 126) / _mean(rw, 126).abs().replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnvol_42d_jerk_v024_signal(opex, ncfo):
    base = _std(np.log1p(_burn_opex(opex, ncfo)), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covervol_42d_jerk_v025_signal(ncfo, opex):
    base = _std(_coverage(ncfo, opex), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_critfrac_42d_jerk_v026_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo)
    crit = ((rw < 12.0) & rw.notna()).astype(float)
    base = crit.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_negocffrac_42d_jerk_v027_signal(ncfo):
    base = (ncfo < 0).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_fcfburnfrac_42d_jerk_v028_signal(ncfo, capex):
    base = (_burn_fcf(ncfo, capex) > 0).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_distress_42d_jerk_v029_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    bn = _burn_opex(opex, ncfo)
    accel = (np.log1p(bn) - np.log1p(bn.shift(63))).clip(lower=0)
    base = _mean(short * accel * 10.0, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_quality_42d_jerk_v030_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _coverage(ncfo, opex)
    q = np.log1p(rw.clip(lower=0)) * (1.0 + cov.clip(-1.0, 2.0))
    base = _rank(q, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayfcfz_42d_jerk_v031_signal(cashneq, ncfo, capex):
    base = _z(_runway_fcf(cashneq, ncfo, capex).clip(upper=120.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayspr_42d_jerk_v032_signal(cashneq, opex, ncfo, capex):
    ro = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    rf = _runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    base = _rank((ro - rf).clip(upper=120.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexburn_42d_jerk_v033_signal(capex, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean(capex.abs() / (bn + capex.abs()).replace(0, np.nan), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexselffund_42d_jerk_v034_signal(ncfo, capex):
    base = _mean((ncfo - capex.abs()) / ncfo.abs().replace(0, np.nan), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finlifeline_42d_jerk_v035_signal(ncff, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean((ncff / (bn + 1.0)).clip(-50, 50), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finburn_42d_jerk_v036_signal(ncff, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    raised = ncff.clip(lower=0)
    base = _mean(raised / (bn + raised).replace(0, np.nan), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_selffundgap_42d_jerk_v037_signal(ncfo, ncff):
    denom = (ncfo.abs() + ncff.abs()).replace(0, np.nan)
    base = _mean((ncfo - ncff) / denom, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashdd_42d_jerk_v038_signal(cashneq):
    base = cashneq / _rmax(cashneq, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnpeak_42d_jerk_v039_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = bn / _rmin(bn, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaycushion_42d_jerk_v040_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = rw - _rmin(rw, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnvscapex_42d_jerk_v041_signal(opex, ncfo, capex):
    bn = _burn_opex(opex, ncfo)
    ratio = bn / (capex.abs() + 1.0)
    base = _z(np.log1p(ratio), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coversurplus_42d_jerk_v042_signal(ncfo, opex):
    base = (_coverage(ncfo, opex) - 1.0).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverstab_42d_jerk_v043_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = -_std(cov, 126) / _mean(cov, 126).abs().replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfopexdisp_42d_jerk_v044_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    base = _std(r, 63) / _std(r, 252).replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfgro_42d_jerk_v045_signal(ncfo):
    base = _logwarp(ncfo).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfturn_42d_jerk_v046_signal(ncfo):
    worst = _rmin(ncfo, 504)
    span = (_rmax(ncfo, 504) - worst).replace(0, np.nan)
    base = ((ncfo - worst) / span).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysnr_42d_jerk_v047_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = (rw - rw.shift(63)) / _std(rw, 252).replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaydisp_42d_jerk_v048_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = pd.concat([_mean(rw, 63), _mean(rw, 126), _mean(rw, 252)], axis=1).std(axis=1)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_survival_42d_jerk_v049_signal(cashneq, opex, ncfo, ncff):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _coverage(ncfo, opex).clip(-2, 2)
    finrel = ncff.clip(lower=0) / (cashneq.abs() + 1.0)
    base = _mean(np.log1p(rw.clip(lower=0)) + cov - finrel, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_floorprox_42d_jerk_v050_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    lo = _rmin(rw, 504)
    hi = _rmax(rw, 504)
    base = (rw - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finratio_42d_jerk_v051_signal(ncff, cashneq):
    base = (ncff / (cashneq.abs() + 1.0)).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_netdrain_42d_jerk_v052_signal(cashneq, ncfo, capex, ncff):
    bn = _burn_fcf(ncfo, capex)
    net = bn - ncff.clip(lower=0)
    base = _mean((net / (cashneq.abs() + 1.0)).clip(-5, 5), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayblend_42d_jerk_v053_signal(cashneq, opex, ncfo, capex):
    ro = _runway_opex(cashneq, opex, ncfo).clip(1, 120)
    rf = _runway_fcf(cashneq, ncfo, capex).clip(1, 120)
    blend = 2.0 / (1.0 / ro + 1.0 / rf)
    base = blend.ewm(span=42, min_periods=21).mean() - blend.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnspike_42d_jerk_v054_signal(ncfo, capex):
    bn = _burn_fcf(ncfo, capex)
    base = bn / _mean(bn, 252).replace(0, np.nan)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_stresshaircut_42d_jerk_v055_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _rank(bn / _rmax(bn, 252).replace(0, np.nan), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysens_42d_jerk_v056_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean((_rmax(bn, 252) - _rmin(bn, 252)) / _mean(bn, 252).replace(0, np.nan), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverroom_42d_jerk_v057_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = _rmax(cov, 252) - cov
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverfloor_42d_jerk_v058_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = cov - _rmin(cov, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashtrough_42d_jerk_v059_signal(cashneq):
    base = cashneq / _rmin(cashneq, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexshare_42d_jerk_v060_signal(opex, ncfo, capex):
    ob = _burn_opex(opex, ncfo)
    cx = capex.abs()
    share = cx / (ob + cx).replace(0, np.nan)
    base = _rank(share, 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexocf_42d_jerk_v061_signal(capex, ncfo):
    r = capex.abs() / ncfo.abs().replace(0, np.nan)
    base = _rank(np.log1p(r), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexgro_42d_jerk_v062_signal(capex):
    base = np.log(capex.abs().replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finshare_42d_jerk_v063_signal(ncff, ncfo):
    pf = ncff.clip(lower=0)
    po = ncfo.clip(lower=0)
    base = _rank(pf / (pf + po + 1.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finvol_42d_jerk_v064_signal(ncff):
    base = _std(_logwarp(ncff), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_compound_42d_jerk_v065_signal(cashneq, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    intens = bn / cashneq.replace(0, np.nan)
    rising = (intens - intens.shift(63)).clip(lower=0)
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    base = _mean(rising * short * 100.0, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocflog_42d_jerk_v066_signal(ncfo):
    base = _mean(_logwarp(ncfo), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_netfund_42d_jerk_v067_signal(cashneq, ncfo, ncff):
    base = _mean((ncfo + ncff) / (cashneq.abs() + 1.0), 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaystable_42d_jerk_v068_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _mean(rw, 126) / (_std(rw, 126) + 1.0)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashopexmo_42d_jerk_v069_signal(cashneq, opex):
    base = _z((cashneq / opex.replace(0, np.nan) * 12.0).clip(upper=120.0), 252)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covrunway_42d_jerk_v070_signal(cashneq, opex, ncfo):
    rw = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0, upper=120.0))
    prox = 1.0 - (1.0 - _coverage(ncfo, opex)).clip(0, 1)
    base = _mean(rw * prox, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnopexfrac_42d_jerk_v071_signal(opex, ncfo):
    base = (_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocftotal_42d_jerk_v072_signal(ncfo, opex, capex):
    r = ncfo / (opex + capex.abs()).replace(0, np.nan)
    base = r.ewm(span=42, min_periods=21).mean() - r.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_dilutiondep_42d_jerk_v073_signal(cashneq, opex, ncfo, ncff):
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=2.0)).clip(upper=0.5)
    finrel = (ncff.clip(lower=0) / (cashneq.abs() + 1.0)).clip(upper=1.0)
    base = _mean(short * finrel * 10.0, 126)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexfunded_42d_jerk_v074_signal(ncfo, capex):
    base = (ncfo.clip(lower=0) / (capex.abs() + 1.0)).ewm(span=63, min_periods=21).mean().clip(upper=10.0)
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaydownside_42d_jerk_v075_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    chg = rw.diff()
    down = chg.where(chg < 0, 0.0)
    base = np.sqrt((down ** 2).rolling(126, min_periods=63).mean())
    d1 = base - base.shift(42)
    s = (d1 - d1.shift(42)) / (42.0 * 42.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayopx_84d_jerk_v076_signal(cashneq, opex, ncfo):
    base = _mean(_runway_opex(cashneq, opex, ncfo).clip(upper=120.0), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayfcf_84d_jerk_v077_signal(cashneq, ncfo, capex):
    rf = _runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    base = _rank(rf, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnopx_84d_jerk_v078_signal(opex, ncfo):
    base = _mean(np.log1p(_burn_opex(opex, ncfo)), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfcf_84d_jerk_v079_signal(ncfo, capex):
    base = _mean(np.log1p(_burn_fcf(ncfo, capex)), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnintens_84d_jerk_v080_signal(cashneq, opex, ncfo):
    intens = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = intens.ewm(span=42, min_periods=21).mean() - intens.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnintfcf_84d_jerk_v081_signal(cashneq, ncfo, capex):
    base = _mean(_burn_fcf(ncfo, capex) / cashneq.replace(0, np.nan), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfrac_84d_jerk_v082_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    frac = bn / opex.replace(0, np.nan)
    hot = (frac > frac.rolling(252, min_periods=126).median()).astype(float)
    base = hot.rolling(126, min_periods=63).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cover_84d_jerk_v083_signal(ncfo, opex):
    base = _mean(_coverage(ncfo, opex), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covergap_84d_jerk_v084_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = _rmax(cov, 126) - cov
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashcover_84d_jerk_v085_signal(cashneq, ncfo, capex):
    cov = np.log1p((cashneq / _burn_fcf(ncfo, capex).replace(0, np.nan)).clip(lower=0, upper=240.0))
    base = cov.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfcapex_84d_jerk_v086_signal(ncfo, capex):
    r = ncfo / capex.abs().replace(0, np.nan)
    lo = _rmin(r, 252)
    hi = _rmax(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashlevel_84d_jerk_v087_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayz_84d_jerk_v088_signal(cashneq, opex, ncfo):
    base = _z(_runway_opex(cashneq, opex, ncfo).clip(upper=120.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnz_84d_jerk_v089_signal(opex, ncfo, capex):
    base = _z(_burn_fcf(ncfo, capex) / (opex + 1.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverz_84d_jerk_v090_signal(ncfo, opex):
    base = _z(_coverage(ncfo, opex), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashz_84d_jerk_v091_signal(cashneq):
    base = _z(cashneq, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayrank_84d_jerk_v092_signal(cashneq, opex, ncfo):
    base = _rank(_runway_opex(cashneq, opex, ncfo), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnfracrank_84d_jerk_v093_signal(opex, ncfo):
    bn = np.log1p(_burn_opex(opex, ncfo))
    base = bn.ewm(span=42, min_periods=21).mean() - bn.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverrank_84d_jerk_v094_signal(ncfo, opex):
    base = _rank(_coverage(ncfo, opex), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysl_84d_jerk_v095_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _mean(rw, 63) / _mean(rw, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnsl_84d_jerk_v096_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean(bn, 63) / _mean(bn, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashsl_84d_jerk_v097_signal(cashneq):
    base = _mean(cashneq, 63) / _mean(cashneq, 252).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayvol_84d_jerk_v098_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _std(rw, 126) / _mean(rw, 126).abs().replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnvol_84d_jerk_v099_signal(opex, ncfo):
    base = _std(np.log1p(_burn_opex(opex, ncfo)), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covervol_84d_jerk_v100_signal(ncfo, opex):
    base = _std(_coverage(ncfo, opex), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_critfrac_84d_jerk_v101_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo)
    crit = ((rw < 12.0) & rw.notna()).astype(float)
    base = crit.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_negocffrac_84d_jerk_v102_signal(ncfo):
    base = (ncfo < 0).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_fcfburnfrac_84d_jerk_v103_signal(ncfo, capex):
    base = (_burn_fcf(ncfo, capex) > 0).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_distress_84d_jerk_v104_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    bn = _burn_opex(opex, ncfo)
    accel = (np.log1p(bn) - np.log1p(bn.shift(63))).clip(lower=0)
    base = _mean(short * accel * 10.0, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_quality_84d_jerk_v105_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _coverage(ncfo, opex)
    q = np.log1p(rw.clip(lower=0)) * (1.0 + cov.clip(-1.0, 2.0))
    base = _rank(q, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayfcfz_84d_jerk_v106_signal(cashneq, ncfo, capex):
    base = _z(_runway_fcf(cashneq, ncfo, capex).clip(upper=120.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayspr_84d_jerk_v107_signal(cashneq, opex, ncfo, capex):
    ro = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    rf = _runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    base = _rank((ro - rf).clip(upper=120.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexburn_84d_jerk_v108_signal(capex, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean(capex.abs() / (bn + capex.abs()).replace(0, np.nan), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexselffund_84d_jerk_v109_signal(ncfo, capex):
    base = _mean((ncfo - capex.abs()) / ncfo.abs().replace(0, np.nan), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finlifeline_84d_jerk_v110_signal(ncff, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean((ncff / (bn + 1.0)).clip(-50, 50), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finburn_84d_jerk_v111_signal(ncff, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    raised = ncff.clip(lower=0)
    base = _mean(raised / (bn + raised).replace(0, np.nan), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_selffundgap_84d_jerk_v112_signal(ncfo, ncff):
    denom = (ncfo.abs() + ncff.abs()).replace(0, np.nan)
    base = _mean((ncfo - ncff) / denom, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashdd_84d_jerk_v113_signal(cashneq):
    base = cashneq / _rmax(cashneq, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnpeak_84d_jerk_v114_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = bn / _rmin(bn, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaycushion_84d_jerk_v115_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = rw - _rmin(rw, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnvscapex_84d_jerk_v116_signal(opex, ncfo, capex):
    bn = _burn_opex(opex, ncfo)
    ratio = bn / (capex.abs() + 1.0)
    base = _z(np.log1p(ratio), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coversurplus_84d_jerk_v117_signal(ncfo, opex):
    base = (_coverage(ncfo, opex) - 1.0).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverstab_84d_jerk_v118_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = -_std(cov, 126) / _mean(cov, 126).abs().replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfopexdisp_84d_jerk_v119_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    base = _std(r, 63) / _std(r, 252).replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfgro_84d_jerk_v120_signal(ncfo):
    base = _logwarp(ncfo).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocfturn_84d_jerk_v121_signal(ncfo):
    worst = _rmin(ncfo, 504)
    span = (_rmax(ncfo, 504) - worst).replace(0, np.nan)
    base = ((ncfo - worst) / span).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysnr_84d_jerk_v122_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = (rw - rw.shift(63)) / _std(rw, 252).replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaydisp_84d_jerk_v123_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = pd.concat([_mean(rw, 63), _mean(rw, 126), _mean(rw, 252)], axis=1).std(axis=1)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_survival_84d_jerk_v124_signal(cashneq, opex, ncfo, ncff):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _coverage(ncfo, opex).clip(-2, 2)
    finrel = ncff.clip(lower=0) / (cashneq.abs() + 1.0)
    base = _mean(np.log1p(rw.clip(lower=0)) + cov - finrel, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_floorprox_84d_jerk_v125_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    lo = _rmin(rw, 504)
    hi = _rmax(rw, 504)
    base = (rw - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finratio_84d_jerk_v126_signal(ncff, cashneq):
    base = (ncff / (cashneq.abs() + 1.0)).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_netdrain_84d_jerk_v127_signal(cashneq, ncfo, capex, ncff):
    bn = _burn_fcf(ncfo, capex)
    net = bn - ncff.clip(lower=0)
    base = _mean((net / (cashneq.abs() + 1.0)).clip(-5, 5), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwayblend_84d_jerk_v128_signal(cashneq, opex, ncfo, capex):
    ro = _runway_opex(cashneq, opex, ncfo).clip(1, 120)
    rf = _runway_fcf(cashneq, ncfo, capex).clip(1, 120)
    blend = 2.0 / (1.0 / ro + 1.0 / rf)
    base = blend.ewm(span=42, min_periods=21).mean() - blend.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnspike_84d_jerk_v129_signal(ncfo, capex):
    bn = _burn_fcf(ncfo, capex)
    base = bn / _mean(bn, 252).replace(0, np.nan)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_stresshaircut_84d_jerk_v130_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _rank(bn / _rmax(bn, 252).replace(0, np.nan), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaysens_84d_jerk_v131_signal(opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    base = _mean((_rmax(bn, 252) - _rmin(bn, 252)) / _mean(bn, 252).replace(0, np.nan), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverroom_84d_jerk_v132_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = _rmax(cov, 252) - cov
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_coverfloor_84d_jerk_v133_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = cov - _rmin(cov, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashtrough_84d_jerk_v134_signal(cashneq):
    base = cashneq / _rmin(cashneq, 504).replace(0, np.nan) - 1.0
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexshare_84d_jerk_v135_signal(opex, ncfo, capex):
    ob = _burn_opex(opex, ncfo)
    cx = capex.abs()
    share = cx / (ob + cx).replace(0, np.nan)
    base = _rank(share, 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexocf_84d_jerk_v136_signal(capex, ncfo):
    r = capex.abs() / ncfo.abs().replace(0, np.nan)
    base = _rank(np.log1p(r), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexgro_84d_jerk_v137_signal(capex):
    base = np.log(capex.abs().replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finshare_84d_jerk_v138_signal(ncff, ncfo):
    pf = ncff.clip(lower=0)
    po = ncfo.clip(lower=0)
    base = _rank(pf / (pf + po + 1.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_finvol_84d_jerk_v139_signal(ncff):
    base = _std(_logwarp(ncff), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_compound_84d_jerk_v140_signal(cashneq, opex, ncfo):
    bn = _burn_opex(opex, ncfo)
    intens = bn / cashneq.replace(0, np.nan)
    rising = (intens - intens.shift(63)).clip(lower=0)
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    base = _mean(rising * short * 100.0, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocflog_84d_jerk_v141_signal(ncfo):
    base = _mean(_logwarp(ncfo), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_netfund_84d_jerk_v142_signal(cashneq, ncfo, ncff):
    base = _mean((ncfo + ncff) / (cashneq.abs() + 1.0), 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaystable_84d_jerk_v143_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    base = _mean(rw, 126) / (_std(rw, 126) + 1.0)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_cashopexmo_84d_jerk_v144_signal(cashneq, opex):
    base = _z((cashneq / opex.replace(0, np.nan) * 12.0).clip(upper=120.0), 252)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_covrunway_84d_jerk_v145_signal(cashneq, opex, ncfo):
    rw = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0, upper=120.0))
    prox = 1.0 - (1.0 - _coverage(ncfo, opex)).clip(0, 1)
    base = _mean(rw * prox, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_burnopexfrac_84d_jerk_v146_signal(opex, ncfo):
    base = (_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_ocftotal_84d_jerk_v147_signal(ncfo, opex, capex):
    r = ncfo / (opex + capex.abs()).replace(0, np.nan)
    base = r.ewm(span=42, min_periods=21).mean() - r.ewm(span=126, min_periods=42).mean()
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_dilutiondep_84d_jerk_v148_signal(cashneq, opex, ncfo, ncff):
    rw = _runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=2.0)).clip(upper=0.5)
    finrel = (ncff.clip(lower=0) / (cashneq.abs() + 1.0)).clip(upper=1.0)
    base = _mean(short * finrel * 10.0, 126)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_capexfunded_84d_jerk_v149_signal(ncfo, capex):
    base = (ncfo.clip(lower=0) / (capex.abs() + 1.0)).ewm(span=63, min_periods=21).mean().clip(upper=10.0)
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


def f31cr_f31_cash_burn_runway_runwaydownside_84d_jerk_v150_signal(cashneq, opex, ncfo):
    rw = _runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    chg = rw.diff()
    down = chg.where(chg < 0, 0.0)
    base = np.sqrt((down ** 2).rolling(126, min_periods=63).mean())
    d1 = base - base.shift(84)
    s = (d1 - d1.shift(84)) / (84.0 * 84.0)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cr_f31_cash_burn_runway_runwayopx_42d_jerk_v001_signal,
    f31cr_f31_cash_burn_runway_runwayfcf_42d_jerk_v002_signal,
    f31cr_f31_cash_burn_runway_burnopx_42d_jerk_v003_signal,
    f31cr_f31_cash_burn_runway_burnfcf_42d_jerk_v004_signal,
    f31cr_f31_cash_burn_runway_burnintens_42d_jerk_v005_signal,
    f31cr_f31_cash_burn_runway_burnintfcf_42d_jerk_v006_signal,
    f31cr_f31_cash_burn_runway_burnfrac_42d_jerk_v007_signal,
    f31cr_f31_cash_burn_runway_cover_42d_jerk_v008_signal,
    f31cr_f31_cash_burn_runway_covergap_42d_jerk_v009_signal,
    f31cr_f31_cash_burn_runway_cashcover_42d_jerk_v010_signal,
    f31cr_f31_cash_burn_runway_ocfcapex_42d_jerk_v011_signal,
    f31cr_f31_cash_burn_runway_cashlevel_42d_jerk_v012_signal,
    f31cr_f31_cash_burn_runway_runwayz_42d_jerk_v013_signal,
    f31cr_f31_cash_burn_runway_burnz_42d_jerk_v014_signal,
    f31cr_f31_cash_burn_runway_coverz_42d_jerk_v015_signal,
    f31cr_f31_cash_burn_runway_cashz_42d_jerk_v016_signal,
    f31cr_f31_cash_burn_runway_runwayrank_42d_jerk_v017_signal,
    f31cr_f31_cash_burn_runway_burnfracrank_42d_jerk_v018_signal,
    f31cr_f31_cash_burn_runway_coverrank_42d_jerk_v019_signal,
    f31cr_f31_cash_burn_runway_runwaysl_42d_jerk_v020_signal,
    f31cr_f31_cash_burn_runway_burnsl_42d_jerk_v021_signal,
    f31cr_f31_cash_burn_runway_cashsl_42d_jerk_v022_signal,
    f31cr_f31_cash_burn_runway_runwayvol_42d_jerk_v023_signal,
    f31cr_f31_cash_burn_runway_burnvol_42d_jerk_v024_signal,
    f31cr_f31_cash_burn_runway_covervol_42d_jerk_v025_signal,
    f31cr_f31_cash_burn_runway_critfrac_42d_jerk_v026_signal,
    f31cr_f31_cash_burn_runway_negocffrac_42d_jerk_v027_signal,
    f31cr_f31_cash_burn_runway_fcfburnfrac_42d_jerk_v028_signal,
    f31cr_f31_cash_burn_runway_distress_42d_jerk_v029_signal,
    f31cr_f31_cash_burn_runway_quality_42d_jerk_v030_signal,
    f31cr_f31_cash_burn_runway_runwayfcfz_42d_jerk_v031_signal,
    f31cr_f31_cash_burn_runway_runwayspr_42d_jerk_v032_signal,
    f31cr_f31_cash_burn_runway_capexburn_42d_jerk_v033_signal,
    f31cr_f31_cash_burn_runway_capexselffund_42d_jerk_v034_signal,
    f31cr_f31_cash_burn_runway_finlifeline_42d_jerk_v035_signal,
    f31cr_f31_cash_burn_runway_finburn_42d_jerk_v036_signal,
    f31cr_f31_cash_burn_runway_selffundgap_42d_jerk_v037_signal,
    f31cr_f31_cash_burn_runway_cashdd_42d_jerk_v038_signal,
    f31cr_f31_cash_burn_runway_burnpeak_42d_jerk_v039_signal,
    f31cr_f31_cash_burn_runway_runwaycushion_42d_jerk_v040_signal,
    f31cr_f31_cash_burn_runway_burnvscapex_42d_jerk_v041_signal,
    f31cr_f31_cash_burn_runway_coversurplus_42d_jerk_v042_signal,
    f31cr_f31_cash_burn_runway_coverstab_42d_jerk_v043_signal,
    f31cr_f31_cash_burn_runway_ocfopexdisp_42d_jerk_v044_signal,
    f31cr_f31_cash_burn_runway_ocfgro_42d_jerk_v045_signal,
    f31cr_f31_cash_burn_runway_ocfturn_42d_jerk_v046_signal,
    f31cr_f31_cash_burn_runway_runwaysnr_42d_jerk_v047_signal,
    f31cr_f31_cash_burn_runway_runwaydisp_42d_jerk_v048_signal,
    f31cr_f31_cash_burn_runway_survival_42d_jerk_v049_signal,
    f31cr_f31_cash_burn_runway_floorprox_42d_jerk_v050_signal,
    f31cr_f31_cash_burn_runway_finratio_42d_jerk_v051_signal,
    f31cr_f31_cash_burn_runway_netdrain_42d_jerk_v052_signal,
    f31cr_f31_cash_burn_runway_runwayblend_42d_jerk_v053_signal,
    f31cr_f31_cash_burn_runway_burnspike_42d_jerk_v054_signal,
    f31cr_f31_cash_burn_runway_stresshaircut_42d_jerk_v055_signal,
    f31cr_f31_cash_burn_runway_runwaysens_42d_jerk_v056_signal,
    f31cr_f31_cash_burn_runway_coverroom_42d_jerk_v057_signal,
    f31cr_f31_cash_burn_runway_coverfloor_42d_jerk_v058_signal,
    f31cr_f31_cash_burn_runway_cashtrough_42d_jerk_v059_signal,
    f31cr_f31_cash_burn_runway_capexshare_42d_jerk_v060_signal,
    f31cr_f31_cash_burn_runway_capexocf_42d_jerk_v061_signal,
    f31cr_f31_cash_burn_runway_capexgro_42d_jerk_v062_signal,
    f31cr_f31_cash_burn_runway_finshare_42d_jerk_v063_signal,
    f31cr_f31_cash_burn_runway_finvol_42d_jerk_v064_signal,
    f31cr_f31_cash_burn_runway_compound_42d_jerk_v065_signal,
    f31cr_f31_cash_burn_runway_ocflog_42d_jerk_v066_signal,
    f31cr_f31_cash_burn_runway_netfund_42d_jerk_v067_signal,
    f31cr_f31_cash_burn_runway_runwaystable_42d_jerk_v068_signal,
    f31cr_f31_cash_burn_runway_cashopexmo_42d_jerk_v069_signal,
    f31cr_f31_cash_burn_runway_covrunway_42d_jerk_v070_signal,
    f31cr_f31_cash_burn_runway_burnopexfrac_42d_jerk_v071_signal,
    f31cr_f31_cash_burn_runway_ocftotal_42d_jerk_v072_signal,
    f31cr_f31_cash_burn_runway_dilutiondep_42d_jerk_v073_signal,
    f31cr_f31_cash_burn_runway_capexfunded_42d_jerk_v074_signal,
    f31cr_f31_cash_burn_runway_runwaydownside_42d_jerk_v075_signal,
    f31cr_f31_cash_burn_runway_runwayopx_84d_jerk_v076_signal,
    f31cr_f31_cash_burn_runway_runwayfcf_84d_jerk_v077_signal,
    f31cr_f31_cash_burn_runway_burnopx_84d_jerk_v078_signal,
    f31cr_f31_cash_burn_runway_burnfcf_84d_jerk_v079_signal,
    f31cr_f31_cash_burn_runway_burnintens_84d_jerk_v080_signal,
    f31cr_f31_cash_burn_runway_burnintfcf_84d_jerk_v081_signal,
    f31cr_f31_cash_burn_runway_burnfrac_84d_jerk_v082_signal,
    f31cr_f31_cash_burn_runway_cover_84d_jerk_v083_signal,
    f31cr_f31_cash_burn_runway_covergap_84d_jerk_v084_signal,
    f31cr_f31_cash_burn_runway_cashcover_84d_jerk_v085_signal,
    f31cr_f31_cash_burn_runway_ocfcapex_84d_jerk_v086_signal,
    f31cr_f31_cash_burn_runway_cashlevel_84d_jerk_v087_signal,
    f31cr_f31_cash_burn_runway_runwayz_84d_jerk_v088_signal,
    f31cr_f31_cash_burn_runway_burnz_84d_jerk_v089_signal,
    f31cr_f31_cash_burn_runway_coverz_84d_jerk_v090_signal,
    f31cr_f31_cash_burn_runway_cashz_84d_jerk_v091_signal,
    f31cr_f31_cash_burn_runway_runwayrank_84d_jerk_v092_signal,
    f31cr_f31_cash_burn_runway_burnfracrank_84d_jerk_v093_signal,
    f31cr_f31_cash_burn_runway_coverrank_84d_jerk_v094_signal,
    f31cr_f31_cash_burn_runway_runwaysl_84d_jerk_v095_signal,
    f31cr_f31_cash_burn_runway_burnsl_84d_jerk_v096_signal,
    f31cr_f31_cash_burn_runway_cashsl_84d_jerk_v097_signal,
    f31cr_f31_cash_burn_runway_runwayvol_84d_jerk_v098_signal,
    f31cr_f31_cash_burn_runway_burnvol_84d_jerk_v099_signal,
    f31cr_f31_cash_burn_runway_covervol_84d_jerk_v100_signal,
    f31cr_f31_cash_burn_runway_critfrac_84d_jerk_v101_signal,
    f31cr_f31_cash_burn_runway_negocffrac_84d_jerk_v102_signal,
    f31cr_f31_cash_burn_runway_fcfburnfrac_84d_jerk_v103_signal,
    f31cr_f31_cash_burn_runway_distress_84d_jerk_v104_signal,
    f31cr_f31_cash_burn_runway_quality_84d_jerk_v105_signal,
    f31cr_f31_cash_burn_runway_runwayfcfz_84d_jerk_v106_signal,
    f31cr_f31_cash_burn_runway_runwayspr_84d_jerk_v107_signal,
    f31cr_f31_cash_burn_runway_capexburn_84d_jerk_v108_signal,
    f31cr_f31_cash_burn_runway_capexselffund_84d_jerk_v109_signal,
    f31cr_f31_cash_burn_runway_finlifeline_84d_jerk_v110_signal,
    f31cr_f31_cash_burn_runway_finburn_84d_jerk_v111_signal,
    f31cr_f31_cash_burn_runway_selffundgap_84d_jerk_v112_signal,
    f31cr_f31_cash_burn_runway_cashdd_84d_jerk_v113_signal,
    f31cr_f31_cash_burn_runway_burnpeak_84d_jerk_v114_signal,
    f31cr_f31_cash_burn_runway_runwaycushion_84d_jerk_v115_signal,
    f31cr_f31_cash_burn_runway_burnvscapex_84d_jerk_v116_signal,
    f31cr_f31_cash_burn_runway_coversurplus_84d_jerk_v117_signal,
    f31cr_f31_cash_burn_runway_coverstab_84d_jerk_v118_signal,
    f31cr_f31_cash_burn_runway_ocfopexdisp_84d_jerk_v119_signal,
    f31cr_f31_cash_burn_runway_ocfgro_84d_jerk_v120_signal,
    f31cr_f31_cash_burn_runway_ocfturn_84d_jerk_v121_signal,
    f31cr_f31_cash_burn_runway_runwaysnr_84d_jerk_v122_signal,
    f31cr_f31_cash_burn_runway_runwaydisp_84d_jerk_v123_signal,
    f31cr_f31_cash_burn_runway_survival_84d_jerk_v124_signal,
    f31cr_f31_cash_burn_runway_floorprox_84d_jerk_v125_signal,
    f31cr_f31_cash_burn_runway_finratio_84d_jerk_v126_signal,
    f31cr_f31_cash_burn_runway_netdrain_84d_jerk_v127_signal,
    f31cr_f31_cash_burn_runway_runwayblend_84d_jerk_v128_signal,
    f31cr_f31_cash_burn_runway_burnspike_84d_jerk_v129_signal,
    f31cr_f31_cash_burn_runway_stresshaircut_84d_jerk_v130_signal,
    f31cr_f31_cash_burn_runway_runwaysens_84d_jerk_v131_signal,
    f31cr_f31_cash_burn_runway_coverroom_84d_jerk_v132_signal,
    f31cr_f31_cash_burn_runway_coverfloor_84d_jerk_v133_signal,
    f31cr_f31_cash_burn_runway_cashtrough_84d_jerk_v134_signal,
    f31cr_f31_cash_burn_runway_capexshare_84d_jerk_v135_signal,
    f31cr_f31_cash_burn_runway_capexocf_84d_jerk_v136_signal,
    f31cr_f31_cash_burn_runway_capexgro_84d_jerk_v137_signal,
    f31cr_f31_cash_burn_runway_finshare_84d_jerk_v138_signal,
    f31cr_f31_cash_burn_runway_finvol_84d_jerk_v139_signal,
    f31cr_f31_cash_burn_runway_compound_84d_jerk_v140_signal,
    f31cr_f31_cash_burn_runway_ocflog_84d_jerk_v141_signal,
    f31cr_f31_cash_burn_runway_netfund_84d_jerk_v142_signal,
    f31cr_f31_cash_burn_runway_runwaystable_84d_jerk_v143_signal,
    f31cr_f31_cash_burn_runway_cashopexmo_84d_jerk_v144_signal,
    f31cr_f31_cash_burn_runway_covrunway_84d_jerk_v145_signal,
    f31cr_f31_cash_burn_runway_burnopexfrac_84d_jerk_v146_signal,
    f31cr_f31_cash_burn_runway_ocftotal_84d_jerk_v147_signal,
    f31cr_f31_cash_burn_runway_dilutiondep_84d_jerk_v148_signal,
    f31cr_f31_cash_burn_runway_capexfunded_84d_jerk_v149_signal,
    f31cr_f31_cash_burn_runway_runwaydownside_84d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_BURN_RUNWAY_REGISTRY_3RD_DERIV_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    cashneq = _fund(101, base=2e8, drift=-0.02, vol=0.07).rename("cashneq")
    opex = _fund(102, base=1.0e8, drift=0.01, vol=0.06).rename("opex")
    capex = _fund(103, base=2e7, drift=0.02, vol=0.08).rename("capex")
    ncfo = _fund(104, base=1.6e8, drift=-0.13, vol=0.32, allow_neg=True).rename("ncfo")
    ncff = _fund(105, base=6e7, drift=0.01, vol=0.20, allow_neg=True).rename("ncff")

    cols = {"cashneq": cashneq, "opex": opex, "capex": capex,
            "ncfo": ncfo, "ncff": ncff}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK %s: %d features pass" % ("f31_cash_burn_runway_3rd_derivatives_001_150_claude", n_features))
