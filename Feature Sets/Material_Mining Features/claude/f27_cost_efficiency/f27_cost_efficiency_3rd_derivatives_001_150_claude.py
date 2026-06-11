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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _logret(s, w):
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


# ===== folder domain primitives (cost STRUCTURE / MIX / INFLATION only) =====
def _f27_cor_mix(cor, opex, sgna):
    return cor / (cor + opex + sgna).replace(0, np.nan)


def _f27_opex_mix(cor, opex, sgna):
    return opex / (cor + opex + sgna).replace(0, np.nan)


def _f27_sgna_mix(cor, opex, sgna):
    return sgna / (cor + opex + sgna).replace(0, np.nan)


def _f27_overhead_split(opex, sgna):
    return sgna / (opex + sgna).replace(0, np.nan)


def _f27_growth_gap(cost, revenue, w):
    cg = np.log(cost.replace(0, np.nan).abs()) - np.log(cost.shift(w).replace(0, np.nan).abs())
    rg = np.log(revenue.replace(0, np.nan).abs()) - np.log(revenue.shift(w).replace(0, np.nan).abs())
    return cg - rg



# ============================================================
# jerk (5d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t0_5d_jerk_v001_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t0_5d_jerk_v002_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t0_5d_jerk_v003_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t0_5d_jerk_v004_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t0_5d_jerk_v005_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 63) / _mean(_tt, 63).replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t0_5d_jerk_v006_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t0_5d_jerk_v007_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t0_5d_jerk_v008_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t0_5d_jerk_v009_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t0_5d_jerk_v010_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t0_5d_jerk_v011_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t0_5d_jerk_v012_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t0_5d_jerk_v013_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t0_5d_jerk_v014_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t0_5d_jerk_v015_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t0_5d_jerk_v016_signal(cor):
    base = _logret(cor, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t0_5d_jerk_v017_signal(opex):
    base = _logret(opex, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t0_5d_jerk_v018_signal(sgna):
    base = _logret(sgna, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t0_5d_jerk_v019_signal(opex, sgna):
    base = _logret(opex + sgna, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t0_5d_jerk_v020_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t0_5d_jerk_v021_signal(sgna, cor):
    base = _logret(sgna, 63) - _logret(cor, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t0_5d_jerk_v022_signal(opex, sgna):
    base = _logret(opex, 63) - _logret(sgna, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t0_5d_jerk_v023_signal(cor, opex):
    base = _logret(cor, 63) - _logret(opex, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t0_5d_jerk_v024_signal(cor, opex, sgna):
    base = _logret(cor, 63) - _logret(opex + sgna, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (5d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t0_5d_jerk_v025_signal(gp, cor):
    base = _logret(gp, 63) - _logret(cor, 63)
    d1 = base - base.shift(5)
    d2 = d1 - d1.shift(5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t1_8d_jerk_v026_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t1_8d_jerk_v027_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t1_8d_jerk_v028_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t1_8d_jerk_v029_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t1_8d_jerk_v030_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 126) / _mean(_tt, 126).replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t1_8d_jerk_v031_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t1_8d_jerk_v032_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t1_8d_jerk_v033_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t1_8d_jerk_v034_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t1_8d_jerk_v035_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t1_8d_jerk_v036_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t1_8d_jerk_v037_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t1_8d_jerk_v038_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t1_8d_jerk_v039_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t1_8d_jerk_v040_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t1_8d_jerk_v041_signal(cor):
    base = _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t1_8d_jerk_v042_signal(opex):
    base = _logret(opex, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t1_8d_jerk_v043_signal(sgna):
    base = _logret(sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t1_8d_jerk_v044_signal(opex, sgna):
    base = _logret(opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t1_8d_jerk_v045_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t1_8d_jerk_v046_signal(sgna, cor):
    base = _logret(sgna, 126) - _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t1_8d_jerk_v047_signal(opex, sgna):
    base = _logret(opex, 126) - _logret(sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t1_8d_jerk_v048_signal(cor, opex):
    base = _logret(cor, 126) - _logret(opex, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t1_8d_jerk_v049_signal(cor, opex, sgna):
    base = _logret(cor, 126) - _logret(opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (8d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t1_8d_jerk_v050_signal(gp, cor):
    base = _logret(gp, 126) - _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(8)
    d2 = d1 - d1.shift(8)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t2_16d_jerk_v051_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t2_16d_jerk_v052_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t2_16d_jerk_v053_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t2_16d_jerk_v054_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t2_16d_jerk_v055_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 252) / _mean(_tt, 252).replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t2_16d_jerk_v056_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t2_16d_jerk_v057_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t2_16d_jerk_v058_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t2_16d_jerk_v059_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t2_16d_jerk_v060_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t2_16d_jerk_v061_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t2_16d_jerk_v062_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t2_16d_jerk_v063_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t2_16d_jerk_v064_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t2_16d_jerk_v065_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t2_16d_jerk_v066_signal(cor):
    base = _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t2_16d_jerk_v067_signal(opex):
    base = _logret(opex, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t2_16d_jerk_v068_signal(sgna):
    base = _logret(sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t2_16d_jerk_v069_signal(opex, sgna):
    base = _logret(opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t2_16d_jerk_v070_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t2_16d_jerk_v071_signal(sgna, cor):
    base = _logret(sgna, 252) - _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t2_16d_jerk_v072_signal(opex, sgna):
    base = _logret(opex, 252) - _logret(sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t2_16d_jerk_v073_signal(cor, opex):
    base = _logret(cor, 252) - _logret(opex, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t2_16d_jerk_v074_signal(cor, opex, sgna):
    base = _logret(cor, 252) - _logret(opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (16d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t2_16d_jerk_v075_signal(gp, cor):
    base = _logret(gp, 252) - _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(16)
    d2 = d1 - d1.shift(16)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t3_34d_jerk_v076_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t3_34d_jerk_v077_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t3_34d_jerk_v078_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t3_34d_jerk_v079_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t3_34d_jerk_v080_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 504) / _mean(_tt, 504).replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t3_34d_jerk_v081_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t3_34d_jerk_v082_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t3_34d_jerk_v083_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t3_34d_jerk_v084_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t3_34d_jerk_v085_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t3_34d_jerk_v086_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t3_34d_jerk_v087_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t3_34d_jerk_v088_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t3_34d_jerk_v089_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t3_34d_jerk_v090_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t3_34d_jerk_v091_signal(cor):
    base = _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t3_34d_jerk_v092_signal(opex):
    base = _logret(opex, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t3_34d_jerk_v093_signal(sgna):
    base = _logret(sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t3_34d_jerk_v094_signal(opex, sgna):
    base = _logret(opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t3_34d_jerk_v095_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t3_34d_jerk_v096_signal(sgna, cor):
    base = _logret(sgna, 504) - _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t3_34d_jerk_v097_signal(opex, sgna):
    base = _logret(opex, 504) - _logret(sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t3_34d_jerk_v098_signal(cor, opex):
    base = _logret(cor, 504) - _logret(opex, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t3_34d_jerk_v099_signal(cor, opex, sgna):
    base = _logret(cor, 504) - _logret(opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (34d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t3_34d_jerk_v100_signal(gp, cor):
    base = _logret(gp, 504) - _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(34)
    d2 = d1 - d1.shift(34)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t4_63d_jerk_v101_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t4_63d_jerk_v102_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t4_63d_jerk_v103_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t4_63d_jerk_v104_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t4_63d_jerk_v105_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 189) / _mean(_tt, 189).replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t4_63d_jerk_v106_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t4_63d_jerk_v107_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t4_63d_jerk_v108_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t4_63d_jerk_v109_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t4_63d_jerk_v110_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t4_63d_jerk_v111_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t4_63d_jerk_v112_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t4_63d_jerk_v113_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t4_63d_jerk_v114_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t4_63d_jerk_v115_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t4_63d_jerk_v116_signal(cor):
    base = _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t4_63d_jerk_v117_signal(opex):
    base = _logret(opex, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t4_63d_jerk_v118_signal(sgna):
    base = _logret(sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t4_63d_jerk_v119_signal(opex, sgna):
    base = _logret(opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t4_63d_jerk_v120_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t4_63d_jerk_v121_signal(sgna, cor):
    base = _logret(sgna, 189) - _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t4_63d_jerk_v122_signal(opex, sgna):
    base = _logret(opex, 189) - _logret(sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t4_63d_jerk_v123_signal(cor, opex):
    base = _logret(cor, 189) - _logret(opex, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t4_63d_jerk_v124_signal(cor, opex, sgna):
    base = _logret(cor, 189) - _logret(opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (63d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t4_63d_jerk_v125_signal(gp, cor):
    base = _logret(gp, 189) - _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t5_126d_jerk_v126_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t5_126d_jerk_v127_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t5_126d_jerk_v128_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t5_126d_jerk_v129_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t5_126d_jerk_v130_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 378) / _mean(_tt, 378).replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t5_126d_jerk_v131_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t5_126d_jerk_v132_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t5_126d_jerk_v133_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t5_126d_jerk_v134_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t5_126d_jerk_v135_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t5_126d_jerk_v136_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t5_126d_jerk_v137_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t5_126d_jerk_v138_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t5_126d_jerk_v139_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t5_126d_jerk_v140_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t5_126d_jerk_v141_signal(cor):
    base = _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t5_126d_jerk_v142_signal(opex):
    base = _logret(opex, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t5_126d_jerk_v143_signal(sgna):
    base = _logret(sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t5_126d_jerk_v144_signal(opex, sgna):
    base = _logret(opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t5_126d_jerk_v145_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t5_126d_jerk_v146_signal(sgna, cor):
    base = _logret(sgna, 378) - _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t5_126d_jerk_v147_signal(opex, sgna):
    base = _logret(opex, 378) - _logret(sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t5_126d_jerk_v148_signal(cor, opex):
    base = _logret(cor, 378) - _logret(opex, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t5_126d_jerk_v149_signal(cor, opex, sgna):
    base = _logret(cor, 378) - _logret(opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (126d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t5_126d_jerk_v150_signal(gp, cor):
    base = _logret(gp, 378) - _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(126)
    d2 = d1 - d1.shift(126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ce_f27_cost_efficiency_cormix_t0_5d_jerk_v001_signal,
    f27ce_f27_cost_efficiency_opexmix_t0_5d_jerk_v002_signal,
    f27ce_f27_cost_efficiency_sgnamix_t0_5d_jerk_v003_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t0_5d_jerk_v004_signal,
    f27ce_f27_cost_efficiency_costcv_t0_5d_jerk_v005_signal,
    f27ce_f27_cost_efficiency_mixentropy_t0_5d_jerk_v006_signal,
    f27ce_f27_cost_efficiency_corpass_t0_5d_jerk_v007_signal,
    f27ce_f27_cost_efficiency_opexpass_t0_5d_jerk_v008_signal,
    f27ce_f27_cost_efficiency_sgnapass_t0_5d_jerk_v009_signal,
    f27ce_f27_cost_efficiency_ovhpass_t0_5d_jerk_v010_signal,
    f27ce_f27_cost_efficiency_totpass_t0_5d_jerk_v011_signal,
    f27ce_f27_cost_efficiency_aiscunit_t0_5d_jerk_v012_signal,
    f27ce_f27_cost_efficiency_totunit_t0_5d_jerk_v013_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t0_5d_jerk_v014_signal,
    f27ce_f27_cost_efficiency_ovhunit_t0_5d_jerk_v015_signal,
    f27ce_f27_cost_efficiency_corgrw_t0_5d_jerk_v016_signal,
    f27ce_f27_cost_efficiency_opexgrw_t0_5d_jerk_v017_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t0_5d_jerk_v018_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t0_5d_jerk_v019_signal,
    f27ce_f27_cost_efficiency_costgrw_t0_5d_jerk_v020_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t0_5d_jerk_v021_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t0_5d_jerk_v022_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t0_5d_jerk_v023_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t0_5d_jerk_v024_signal,
    f27ce_f27_cost_efficiency_gpvscor_t0_5d_jerk_v025_signal,
    f27ce_f27_cost_efficiency_cormix_t1_8d_jerk_v026_signal,
    f27ce_f27_cost_efficiency_opexmix_t1_8d_jerk_v027_signal,
    f27ce_f27_cost_efficiency_sgnamix_t1_8d_jerk_v028_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t1_8d_jerk_v029_signal,
    f27ce_f27_cost_efficiency_costcv_t1_8d_jerk_v030_signal,
    f27ce_f27_cost_efficiency_mixentropy_t1_8d_jerk_v031_signal,
    f27ce_f27_cost_efficiency_corpass_t1_8d_jerk_v032_signal,
    f27ce_f27_cost_efficiency_opexpass_t1_8d_jerk_v033_signal,
    f27ce_f27_cost_efficiency_sgnapass_t1_8d_jerk_v034_signal,
    f27ce_f27_cost_efficiency_ovhpass_t1_8d_jerk_v035_signal,
    f27ce_f27_cost_efficiency_totpass_t1_8d_jerk_v036_signal,
    f27ce_f27_cost_efficiency_aiscunit_t1_8d_jerk_v037_signal,
    f27ce_f27_cost_efficiency_totunit_t1_8d_jerk_v038_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t1_8d_jerk_v039_signal,
    f27ce_f27_cost_efficiency_ovhunit_t1_8d_jerk_v040_signal,
    f27ce_f27_cost_efficiency_corgrw_t1_8d_jerk_v041_signal,
    f27ce_f27_cost_efficiency_opexgrw_t1_8d_jerk_v042_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t1_8d_jerk_v043_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t1_8d_jerk_v044_signal,
    f27ce_f27_cost_efficiency_costgrw_t1_8d_jerk_v045_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t1_8d_jerk_v046_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t1_8d_jerk_v047_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t1_8d_jerk_v048_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t1_8d_jerk_v049_signal,
    f27ce_f27_cost_efficiency_gpvscor_t1_8d_jerk_v050_signal,
    f27ce_f27_cost_efficiency_cormix_t2_16d_jerk_v051_signal,
    f27ce_f27_cost_efficiency_opexmix_t2_16d_jerk_v052_signal,
    f27ce_f27_cost_efficiency_sgnamix_t2_16d_jerk_v053_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t2_16d_jerk_v054_signal,
    f27ce_f27_cost_efficiency_costcv_t2_16d_jerk_v055_signal,
    f27ce_f27_cost_efficiency_mixentropy_t2_16d_jerk_v056_signal,
    f27ce_f27_cost_efficiency_corpass_t2_16d_jerk_v057_signal,
    f27ce_f27_cost_efficiency_opexpass_t2_16d_jerk_v058_signal,
    f27ce_f27_cost_efficiency_sgnapass_t2_16d_jerk_v059_signal,
    f27ce_f27_cost_efficiency_ovhpass_t2_16d_jerk_v060_signal,
    f27ce_f27_cost_efficiency_totpass_t2_16d_jerk_v061_signal,
    f27ce_f27_cost_efficiency_aiscunit_t2_16d_jerk_v062_signal,
    f27ce_f27_cost_efficiency_totunit_t2_16d_jerk_v063_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t2_16d_jerk_v064_signal,
    f27ce_f27_cost_efficiency_ovhunit_t2_16d_jerk_v065_signal,
    f27ce_f27_cost_efficiency_corgrw_t2_16d_jerk_v066_signal,
    f27ce_f27_cost_efficiency_opexgrw_t2_16d_jerk_v067_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t2_16d_jerk_v068_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t2_16d_jerk_v069_signal,
    f27ce_f27_cost_efficiency_costgrw_t2_16d_jerk_v070_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t2_16d_jerk_v071_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t2_16d_jerk_v072_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t2_16d_jerk_v073_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t2_16d_jerk_v074_signal,
    f27ce_f27_cost_efficiency_gpvscor_t2_16d_jerk_v075_signal,
    f27ce_f27_cost_efficiency_cormix_t3_34d_jerk_v076_signal,
    f27ce_f27_cost_efficiency_opexmix_t3_34d_jerk_v077_signal,
    f27ce_f27_cost_efficiency_sgnamix_t3_34d_jerk_v078_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t3_34d_jerk_v079_signal,
    f27ce_f27_cost_efficiency_costcv_t3_34d_jerk_v080_signal,
    f27ce_f27_cost_efficiency_mixentropy_t3_34d_jerk_v081_signal,
    f27ce_f27_cost_efficiency_corpass_t3_34d_jerk_v082_signal,
    f27ce_f27_cost_efficiency_opexpass_t3_34d_jerk_v083_signal,
    f27ce_f27_cost_efficiency_sgnapass_t3_34d_jerk_v084_signal,
    f27ce_f27_cost_efficiency_ovhpass_t3_34d_jerk_v085_signal,
    f27ce_f27_cost_efficiency_totpass_t3_34d_jerk_v086_signal,
    f27ce_f27_cost_efficiency_aiscunit_t3_34d_jerk_v087_signal,
    f27ce_f27_cost_efficiency_totunit_t3_34d_jerk_v088_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t3_34d_jerk_v089_signal,
    f27ce_f27_cost_efficiency_ovhunit_t3_34d_jerk_v090_signal,
    f27ce_f27_cost_efficiency_corgrw_t3_34d_jerk_v091_signal,
    f27ce_f27_cost_efficiency_opexgrw_t3_34d_jerk_v092_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t3_34d_jerk_v093_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t3_34d_jerk_v094_signal,
    f27ce_f27_cost_efficiency_costgrw_t3_34d_jerk_v095_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t3_34d_jerk_v096_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t3_34d_jerk_v097_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t3_34d_jerk_v098_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t3_34d_jerk_v099_signal,
    f27ce_f27_cost_efficiency_gpvscor_t3_34d_jerk_v100_signal,
    f27ce_f27_cost_efficiency_cormix_t4_63d_jerk_v101_signal,
    f27ce_f27_cost_efficiency_opexmix_t4_63d_jerk_v102_signal,
    f27ce_f27_cost_efficiency_sgnamix_t4_63d_jerk_v103_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t4_63d_jerk_v104_signal,
    f27ce_f27_cost_efficiency_costcv_t4_63d_jerk_v105_signal,
    f27ce_f27_cost_efficiency_mixentropy_t4_63d_jerk_v106_signal,
    f27ce_f27_cost_efficiency_corpass_t4_63d_jerk_v107_signal,
    f27ce_f27_cost_efficiency_opexpass_t4_63d_jerk_v108_signal,
    f27ce_f27_cost_efficiency_sgnapass_t4_63d_jerk_v109_signal,
    f27ce_f27_cost_efficiency_ovhpass_t4_63d_jerk_v110_signal,
    f27ce_f27_cost_efficiency_totpass_t4_63d_jerk_v111_signal,
    f27ce_f27_cost_efficiency_aiscunit_t4_63d_jerk_v112_signal,
    f27ce_f27_cost_efficiency_totunit_t4_63d_jerk_v113_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t4_63d_jerk_v114_signal,
    f27ce_f27_cost_efficiency_ovhunit_t4_63d_jerk_v115_signal,
    f27ce_f27_cost_efficiency_corgrw_t4_63d_jerk_v116_signal,
    f27ce_f27_cost_efficiency_opexgrw_t4_63d_jerk_v117_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t4_63d_jerk_v118_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t4_63d_jerk_v119_signal,
    f27ce_f27_cost_efficiency_costgrw_t4_63d_jerk_v120_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t4_63d_jerk_v121_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t4_63d_jerk_v122_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t4_63d_jerk_v123_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t4_63d_jerk_v124_signal,
    f27ce_f27_cost_efficiency_gpvscor_t4_63d_jerk_v125_signal,
    f27ce_f27_cost_efficiency_cormix_t5_126d_jerk_v126_signal,
    f27ce_f27_cost_efficiency_opexmix_t5_126d_jerk_v127_signal,
    f27ce_f27_cost_efficiency_sgnamix_t5_126d_jerk_v128_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t5_126d_jerk_v129_signal,
    f27ce_f27_cost_efficiency_costcv_t5_126d_jerk_v130_signal,
    f27ce_f27_cost_efficiency_mixentropy_t5_126d_jerk_v131_signal,
    f27ce_f27_cost_efficiency_corpass_t5_126d_jerk_v132_signal,
    f27ce_f27_cost_efficiency_opexpass_t5_126d_jerk_v133_signal,
    f27ce_f27_cost_efficiency_sgnapass_t5_126d_jerk_v134_signal,
    f27ce_f27_cost_efficiency_ovhpass_t5_126d_jerk_v135_signal,
    f27ce_f27_cost_efficiency_totpass_t5_126d_jerk_v136_signal,
    f27ce_f27_cost_efficiency_aiscunit_t5_126d_jerk_v137_signal,
    f27ce_f27_cost_efficiency_totunit_t5_126d_jerk_v138_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t5_126d_jerk_v139_signal,
    f27ce_f27_cost_efficiency_ovhunit_t5_126d_jerk_v140_signal,
    f27ce_f27_cost_efficiency_corgrw_t5_126d_jerk_v141_signal,
    f27ce_f27_cost_efficiency_opexgrw_t5_126d_jerk_v142_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t5_126d_jerk_v143_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t5_126d_jerk_v144_signal,
    f27ce_f27_cost_efficiency_costgrw_t5_126d_jerk_v145_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t5_126d_jerk_v146_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t5_126d_jerk_v147_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t5_126d_jerk_v148_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t5_126d_jerk_v149_signal,
    f27ce_f27_cost_efficiency_gpvscor_t5_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_COST_EFFICIENCY_REGISTRY_3RD_001_150 = REGISTRY


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

    revenue = _fund(101, base=5e8, drift=0.012, vol=0.10).rename("revenue")
    cor = _fund(202, base=2.4e8, drift=0.006, vol=0.14).rename("cor")
    opex = _fund(303, base=1.6e8, drift=0.011, vol=0.20).rename("opex")
    sgna = _fund(404, base=9e7, drift=0.003, vol=0.22).rename("sgna")
    gp = (revenue - cor).rename("gp")

    cols = {"revenue": revenue, "cor": cor, "opex": opex, "sgna": sgna, "gp": gp}

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

    print("OK f27_cost_efficiency_3rd_derivatives_001_150_claude: %d features pass" % n_features)
