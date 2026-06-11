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
# slope (5d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t0_5d_slope_v001_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t0_5d_slope_v002_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t0_5d_slope_v003_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t0_5d_slope_v004_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t0_5d_slope_v005_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 63) / _mean(_tt, 63).replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t0_5d_slope_v006_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t0_5d_slope_v007_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t0_5d_slope_v008_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t0_5d_slope_v009_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t0_5d_slope_v010_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t0_5d_slope_v011_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t0_5d_slope_v012_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t0_5d_slope_v013_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t0_5d_slope_v014_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t0_5d_slope_v015_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t0_5d_slope_v016_signal(cor):
    base = _logret(cor, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t0_5d_slope_v017_signal(opex):
    base = _logret(opex, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t0_5d_slope_v018_signal(sgna):
    base = _logret(sgna, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t0_5d_slope_v019_signal(opex, sgna):
    base = _logret(opex + sgna, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t0_5d_slope_v020_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t0_5d_slope_v021_signal(sgna, cor):
    base = _logret(sgna, 63) - _logret(cor, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t0_5d_slope_v022_signal(opex, sgna):
    base = _logret(opex, 63) - _logret(sgna, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t0_5d_slope_v023_signal(cor, opex):
    base = _logret(cor, 63) - _logret(opex, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t0_5d_slope_v024_signal(cor, opex, sgna):
    base = _logret(cor, 63) - _logret(opex + sgna, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (5d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t0_5d_slope_v025_signal(gp, cor):
    base = _logret(gp, 63) - _logret(cor, 63)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t1_10d_slope_v026_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t1_10d_slope_v027_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t1_10d_slope_v028_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t1_10d_slope_v029_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t1_10d_slope_v030_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 126) / _mean(_tt, 126).replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t1_10d_slope_v031_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t1_10d_slope_v032_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t1_10d_slope_v033_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t1_10d_slope_v034_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t1_10d_slope_v035_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t1_10d_slope_v036_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t1_10d_slope_v037_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t1_10d_slope_v038_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t1_10d_slope_v039_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t1_10d_slope_v040_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t1_10d_slope_v041_signal(cor):
    base = _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t1_10d_slope_v042_signal(opex):
    base = _logret(opex, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t1_10d_slope_v043_signal(sgna):
    base = _logret(sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t1_10d_slope_v044_signal(opex, sgna):
    base = _logret(opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t1_10d_slope_v045_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t1_10d_slope_v046_signal(sgna, cor):
    base = _logret(sgna, 126) - _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t1_10d_slope_v047_signal(opex, sgna):
    base = _logret(opex, 126) - _logret(sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t1_10d_slope_v048_signal(cor, opex):
    base = _logret(cor, 126) - _logret(opex, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t1_10d_slope_v049_signal(cor, opex, sgna):
    base = _logret(cor, 126) - _logret(opex + sgna, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (10d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t1_10d_slope_v050_signal(gp, cor):
    base = _logret(gp, 126) - _logret(cor, 126)
    base = base.rolling(5, min_periods=2).mean()
    d1 = base - base.shift(10)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t2_21d_slope_v051_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t2_21d_slope_v052_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t2_21d_slope_v053_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t2_21d_slope_v054_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t2_21d_slope_v055_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 252) / _mean(_tt, 252).replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t2_21d_slope_v056_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t2_21d_slope_v057_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t2_21d_slope_v058_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t2_21d_slope_v059_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t2_21d_slope_v060_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t2_21d_slope_v061_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t2_21d_slope_v062_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t2_21d_slope_v063_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t2_21d_slope_v064_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t2_21d_slope_v065_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t2_21d_slope_v066_signal(cor):
    base = _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t2_21d_slope_v067_signal(opex):
    base = _logret(opex, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t2_21d_slope_v068_signal(sgna):
    base = _logret(sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t2_21d_slope_v069_signal(opex, sgna):
    base = _logret(opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t2_21d_slope_v070_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t2_21d_slope_v071_signal(sgna, cor):
    base = _logret(sgna, 252) - _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t2_21d_slope_v072_signal(opex, sgna):
    base = _logret(opex, 252) - _logret(sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t2_21d_slope_v073_signal(cor, opex):
    base = _logret(cor, 252) - _logret(opex, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t2_21d_slope_v074_signal(cor, opex, sgna):
    base = _logret(cor, 252) - _logret(opex + sgna, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (21d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t2_21d_slope_v075_signal(gp, cor):
    base = _logret(gp, 252) - _logret(cor, 252)
    base = base.rolling(10, min_periods=5).mean()
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t3_42d_slope_v076_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t3_42d_slope_v077_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t3_42d_slope_v078_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t3_42d_slope_v079_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t3_42d_slope_v080_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 504) / _mean(_tt, 504).replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t3_42d_slope_v081_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t3_42d_slope_v082_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t3_42d_slope_v083_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t3_42d_slope_v084_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t3_42d_slope_v085_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t3_42d_slope_v086_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t3_42d_slope_v087_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t3_42d_slope_v088_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t3_42d_slope_v089_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t3_42d_slope_v090_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t3_42d_slope_v091_signal(cor):
    base = _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t3_42d_slope_v092_signal(opex):
    base = _logret(opex, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t3_42d_slope_v093_signal(sgna):
    base = _logret(sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t3_42d_slope_v094_signal(opex, sgna):
    base = _logret(opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t3_42d_slope_v095_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t3_42d_slope_v096_signal(sgna, cor):
    base = _logret(sgna, 504) - _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t3_42d_slope_v097_signal(opex, sgna):
    base = _logret(opex, 504) - _logret(sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t3_42d_slope_v098_signal(cor, opex):
    base = _logret(cor, 504) - _logret(opex, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t3_42d_slope_v099_signal(cor, opex, sgna):
    base = _logret(cor, 504) - _logret(opex + sgna, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (42d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t3_42d_slope_v100_signal(gp, cor):
    base = _logret(gp, 504) - _logret(cor, 504)
    base = base.rolling(21, min_periods=10).mean()
    d1 = base - base.shift(42)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t4_84d_slope_v101_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t4_84d_slope_v102_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t4_84d_slope_v103_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t4_84d_slope_v104_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t4_84d_slope_v105_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 189) / _mean(_tt, 189).replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t4_84d_slope_v106_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t4_84d_slope_v107_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t4_84d_slope_v108_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t4_84d_slope_v109_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t4_84d_slope_v110_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t4_84d_slope_v111_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t4_84d_slope_v112_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t4_84d_slope_v113_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t4_84d_slope_v114_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t4_84d_slope_v115_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t4_84d_slope_v116_signal(cor):
    base = _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t4_84d_slope_v117_signal(opex):
    base = _logret(opex, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t4_84d_slope_v118_signal(sgna):
    base = _logret(sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t4_84d_slope_v119_signal(opex, sgna):
    base = _logret(opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t4_84d_slope_v120_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t4_84d_slope_v121_signal(sgna, cor):
    base = _logret(sgna, 189) - _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t4_84d_slope_v122_signal(opex, sgna):
    base = _logret(opex, 189) - _logret(sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t4_84d_slope_v123_signal(cor, opex):
    base = _logret(cor, 189) - _logret(opex, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t4_84d_slope_v124_signal(cor, opex, sgna):
    base = _logret(cor, 189) - _logret(opex + sgna, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (84d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t4_84d_slope_v125_signal(gp, cor):
    base = _logret(gp, 189) - _logret(cor, 189)
    base = base.rolling(42, min_periods=21).mean()
    d1 = base - base.shift(84)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of cormix cost base
def f27ce_f27_cost_efficiency_cormix_t5_168d_slope_v126_signal(cor, opex, sgna):
    base = _f27_cor_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of opexmix cost base
def f27ce_f27_cost_efficiency_opexmix_t5_168d_slope_v127_signal(cor, opex, sgna):
    base = _f27_opex_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of sgnamix cost base
def f27ce_f27_cost_efficiency_sgnamix_t5_168d_slope_v128_signal(cor, opex, sgna):
    base = _f27_sgna_mix(cor, opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of ovhsplit cost base
def f27ce_f27_cost_efficiency_ovhsplit_t5_168d_slope_v129_signal(opex, sgna):
    base = _f27_overhead_split(opex, sgna)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of costcv cost base
def f27ce_f27_cost_efficiency_costcv_t5_168d_slope_v130_signal(cor, opex, sgna):
    _tt = cor + opex + sgna
    base = _std(_tt, 378) / _mean(_tt, 378).replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of mixentropy cost base
def f27ce_f27_cost_efficiency_mixentropy_t5_168d_slope_v131_signal(cor, opex, sgna):
    _t = (cor + opex + sgna).replace(0, np.nan)
    _s1 = (cor / _t).clip(lower=1e-9)
    _s2 = (opex / _t).clip(lower=1e-9)
    _s3 = (sgna / _t).clip(lower=1e-9)
    base = -(_s1 * np.log(_s1) + _s2 * np.log(_s2) + _s3 * np.log(_s3))
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of corpass cost base
def f27ce_f27_cost_efficiency_corpass_t5_168d_slope_v132_signal(cor, revenue):
    base = _f27_growth_gap(cor, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of opexpass cost base
def f27ce_f27_cost_efficiency_opexpass_t5_168d_slope_v133_signal(opex, revenue):
    base = _f27_growth_gap(opex, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of sgnapass cost base
def f27ce_f27_cost_efficiency_sgnapass_t5_168d_slope_v134_signal(sgna, revenue):
    base = _f27_growth_gap(sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of ovhpass cost base
def f27ce_f27_cost_efficiency_ovhpass_t5_168d_slope_v135_signal(opex, sgna, revenue):
    base = _f27_growth_gap(opex + sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of totpass cost base
def f27ce_f27_cost_efficiency_totpass_t5_168d_slope_v136_signal(cor, opex, sgna, revenue):
    base = _f27_growth_gap(cor + opex + sgna, revenue, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of aiscunit cost base
def f27ce_f27_cost_efficiency_aiscunit_t5_168d_slope_v137_signal(cor, sgna, revenue):
    base = (cor + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of totunit cost base
def f27ce_f27_cost_efficiency_totunit_t5_168d_slope_v138_signal(cor, opex, sgna, revenue):
    base = (cor + opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of sgnaunit cost base
def f27ce_f27_cost_efficiency_sgnaunit_t5_168d_slope_v139_signal(sgna, revenue):
    base = sgna / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of ovhunit cost base
def f27ce_f27_cost_efficiency_ovhunit_t5_168d_slope_v140_signal(opex, sgna, revenue):
    base = (opex + sgna) / revenue.replace(0, np.nan)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of corgrw cost base
def f27ce_f27_cost_efficiency_corgrw_t5_168d_slope_v141_signal(cor):
    base = _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of opexgrw cost base
def f27ce_f27_cost_efficiency_opexgrw_t5_168d_slope_v142_signal(opex):
    base = _logret(opex, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of sgnagrw cost base
def f27ce_f27_cost_efficiency_sgnagrw_t5_168d_slope_v143_signal(sgna):
    base = _logret(sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of ovhgrw cost base
def f27ce_f27_cost_efficiency_ovhgrw_t5_168d_slope_v144_signal(opex, sgna):
    base = _logret(opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of costgrw cost base
def f27ce_f27_cost_efficiency_costgrw_t5_168d_slope_v145_signal(cor, opex, sgna):
    base = _logret(cor + opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of sgnacorgrw cost base
def f27ce_f27_cost_efficiency_sgnacorgrw_t5_168d_slope_v146_signal(sgna, cor):
    base = _logret(sgna, 378) - _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of opexsgnagrw cost base
def f27ce_f27_cost_efficiency_opexsgnagrw_t5_168d_slope_v147_signal(opex, sgna):
    base = _logret(opex, 378) - _logret(sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of coropexgrw cost base
def f27ce_f27_cost_efficiency_coropexgrw_t5_168d_slope_v148_signal(cor, opex):
    base = _logret(cor, 378) - _logret(opex, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of corovhgrw cost base
def f27ce_f27_cost_efficiency_corovhgrw_t5_168d_slope_v149_signal(cor, opex, sgna):
    base = _logret(cor, 378) - _logret(opex + sgna, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


# slope (168d ROC) of gpvscor cost base
def f27ce_f27_cost_efficiency_gpvscor_t5_168d_slope_v150_signal(gp, cor):
    base = _logret(gp, 378) - _logret(cor, 378)
    base = base.rolling(63, min_periods=31).mean()
    d1 = base - base.shift(168)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ce_f27_cost_efficiency_cormix_t0_5d_slope_v001_signal,
    f27ce_f27_cost_efficiency_opexmix_t0_5d_slope_v002_signal,
    f27ce_f27_cost_efficiency_sgnamix_t0_5d_slope_v003_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t0_5d_slope_v004_signal,
    f27ce_f27_cost_efficiency_costcv_t0_5d_slope_v005_signal,
    f27ce_f27_cost_efficiency_mixentropy_t0_5d_slope_v006_signal,
    f27ce_f27_cost_efficiency_corpass_t0_5d_slope_v007_signal,
    f27ce_f27_cost_efficiency_opexpass_t0_5d_slope_v008_signal,
    f27ce_f27_cost_efficiency_sgnapass_t0_5d_slope_v009_signal,
    f27ce_f27_cost_efficiency_ovhpass_t0_5d_slope_v010_signal,
    f27ce_f27_cost_efficiency_totpass_t0_5d_slope_v011_signal,
    f27ce_f27_cost_efficiency_aiscunit_t0_5d_slope_v012_signal,
    f27ce_f27_cost_efficiency_totunit_t0_5d_slope_v013_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t0_5d_slope_v014_signal,
    f27ce_f27_cost_efficiency_ovhunit_t0_5d_slope_v015_signal,
    f27ce_f27_cost_efficiency_corgrw_t0_5d_slope_v016_signal,
    f27ce_f27_cost_efficiency_opexgrw_t0_5d_slope_v017_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t0_5d_slope_v018_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t0_5d_slope_v019_signal,
    f27ce_f27_cost_efficiency_costgrw_t0_5d_slope_v020_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t0_5d_slope_v021_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t0_5d_slope_v022_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t0_5d_slope_v023_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t0_5d_slope_v024_signal,
    f27ce_f27_cost_efficiency_gpvscor_t0_5d_slope_v025_signal,
    f27ce_f27_cost_efficiency_cormix_t1_10d_slope_v026_signal,
    f27ce_f27_cost_efficiency_opexmix_t1_10d_slope_v027_signal,
    f27ce_f27_cost_efficiency_sgnamix_t1_10d_slope_v028_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t1_10d_slope_v029_signal,
    f27ce_f27_cost_efficiency_costcv_t1_10d_slope_v030_signal,
    f27ce_f27_cost_efficiency_mixentropy_t1_10d_slope_v031_signal,
    f27ce_f27_cost_efficiency_corpass_t1_10d_slope_v032_signal,
    f27ce_f27_cost_efficiency_opexpass_t1_10d_slope_v033_signal,
    f27ce_f27_cost_efficiency_sgnapass_t1_10d_slope_v034_signal,
    f27ce_f27_cost_efficiency_ovhpass_t1_10d_slope_v035_signal,
    f27ce_f27_cost_efficiency_totpass_t1_10d_slope_v036_signal,
    f27ce_f27_cost_efficiency_aiscunit_t1_10d_slope_v037_signal,
    f27ce_f27_cost_efficiency_totunit_t1_10d_slope_v038_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t1_10d_slope_v039_signal,
    f27ce_f27_cost_efficiency_ovhunit_t1_10d_slope_v040_signal,
    f27ce_f27_cost_efficiency_corgrw_t1_10d_slope_v041_signal,
    f27ce_f27_cost_efficiency_opexgrw_t1_10d_slope_v042_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t1_10d_slope_v043_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t1_10d_slope_v044_signal,
    f27ce_f27_cost_efficiency_costgrw_t1_10d_slope_v045_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t1_10d_slope_v046_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t1_10d_slope_v047_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t1_10d_slope_v048_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t1_10d_slope_v049_signal,
    f27ce_f27_cost_efficiency_gpvscor_t1_10d_slope_v050_signal,
    f27ce_f27_cost_efficiency_cormix_t2_21d_slope_v051_signal,
    f27ce_f27_cost_efficiency_opexmix_t2_21d_slope_v052_signal,
    f27ce_f27_cost_efficiency_sgnamix_t2_21d_slope_v053_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t2_21d_slope_v054_signal,
    f27ce_f27_cost_efficiency_costcv_t2_21d_slope_v055_signal,
    f27ce_f27_cost_efficiency_mixentropy_t2_21d_slope_v056_signal,
    f27ce_f27_cost_efficiency_corpass_t2_21d_slope_v057_signal,
    f27ce_f27_cost_efficiency_opexpass_t2_21d_slope_v058_signal,
    f27ce_f27_cost_efficiency_sgnapass_t2_21d_slope_v059_signal,
    f27ce_f27_cost_efficiency_ovhpass_t2_21d_slope_v060_signal,
    f27ce_f27_cost_efficiency_totpass_t2_21d_slope_v061_signal,
    f27ce_f27_cost_efficiency_aiscunit_t2_21d_slope_v062_signal,
    f27ce_f27_cost_efficiency_totunit_t2_21d_slope_v063_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t2_21d_slope_v064_signal,
    f27ce_f27_cost_efficiency_ovhunit_t2_21d_slope_v065_signal,
    f27ce_f27_cost_efficiency_corgrw_t2_21d_slope_v066_signal,
    f27ce_f27_cost_efficiency_opexgrw_t2_21d_slope_v067_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t2_21d_slope_v068_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t2_21d_slope_v069_signal,
    f27ce_f27_cost_efficiency_costgrw_t2_21d_slope_v070_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t2_21d_slope_v071_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t2_21d_slope_v072_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t2_21d_slope_v073_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t2_21d_slope_v074_signal,
    f27ce_f27_cost_efficiency_gpvscor_t2_21d_slope_v075_signal,
    f27ce_f27_cost_efficiency_cormix_t3_42d_slope_v076_signal,
    f27ce_f27_cost_efficiency_opexmix_t3_42d_slope_v077_signal,
    f27ce_f27_cost_efficiency_sgnamix_t3_42d_slope_v078_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t3_42d_slope_v079_signal,
    f27ce_f27_cost_efficiency_costcv_t3_42d_slope_v080_signal,
    f27ce_f27_cost_efficiency_mixentropy_t3_42d_slope_v081_signal,
    f27ce_f27_cost_efficiency_corpass_t3_42d_slope_v082_signal,
    f27ce_f27_cost_efficiency_opexpass_t3_42d_slope_v083_signal,
    f27ce_f27_cost_efficiency_sgnapass_t3_42d_slope_v084_signal,
    f27ce_f27_cost_efficiency_ovhpass_t3_42d_slope_v085_signal,
    f27ce_f27_cost_efficiency_totpass_t3_42d_slope_v086_signal,
    f27ce_f27_cost_efficiency_aiscunit_t3_42d_slope_v087_signal,
    f27ce_f27_cost_efficiency_totunit_t3_42d_slope_v088_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t3_42d_slope_v089_signal,
    f27ce_f27_cost_efficiency_ovhunit_t3_42d_slope_v090_signal,
    f27ce_f27_cost_efficiency_corgrw_t3_42d_slope_v091_signal,
    f27ce_f27_cost_efficiency_opexgrw_t3_42d_slope_v092_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t3_42d_slope_v093_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t3_42d_slope_v094_signal,
    f27ce_f27_cost_efficiency_costgrw_t3_42d_slope_v095_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t3_42d_slope_v096_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t3_42d_slope_v097_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t3_42d_slope_v098_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t3_42d_slope_v099_signal,
    f27ce_f27_cost_efficiency_gpvscor_t3_42d_slope_v100_signal,
    f27ce_f27_cost_efficiency_cormix_t4_84d_slope_v101_signal,
    f27ce_f27_cost_efficiency_opexmix_t4_84d_slope_v102_signal,
    f27ce_f27_cost_efficiency_sgnamix_t4_84d_slope_v103_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t4_84d_slope_v104_signal,
    f27ce_f27_cost_efficiency_costcv_t4_84d_slope_v105_signal,
    f27ce_f27_cost_efficiency_mixentropy_t4_84d_slope_v106_signal,
    f27ce_f27_cost_efficiency_corpass_t4_84d_slope_v107_signal,
    f27ce_f27_cost_efficiency_opexpass_t4_84d_slope_v108_signal,
    f27ce_f27_cost_efficiency_sgnapass_t4_84d_slope_v109_signal,
    f27ce_f27_cost_efficiency_ovhpass_t4_84d_slope_v110_signal,
    f27ce_f27_cost_efficiency_totpass_t4_84d_slope_v111_signal,
    f27ce_f27_cost_efficiency_aiscunit_t4_84d_slope_v112_signal,
    f27ce_f27_cost_efficiency_totunit_t4_84d_slope_v113_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t4_84d_slope_v114_signal,
    f27ce_f27_cost_efficiency_ovhunit_t4_84d_slope_v115_signal,
    f27ce_f27_cost_efficiency_corgrw_t4_84d_slope_v116_signal,
    f27ce_f27_cost_efficiency_opexgrw_t4_84d_slope_v117_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t4_84d_slope_v118_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t4_84d_slope_v119_signal,
    f27ce_f27_cost_efficiency_costgrw_t4_84d_slope_v120_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t4_84d_slope_v121_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t4_84d_slope_v122_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t4_84d_slope_v123_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t4_84d_slope_v124_signal,
    f27ce_f27_cost_efficiency_gpvscor_t4_84d_slope_v125_signal,
    f27ce_f27_cost_efficiency_cormix_t5_168d_slope_v126_signal,
    f27ce_f27_cost_efficiency_opexmix_t5_168d_slope_v127_signal,
    f27ce_f27_cost_efficiency_sgnamix_t5_168d_slope_v128_signal,
    f27ce_f27_cost_efficiency_ovhsplit_t5_168d_slope_v129_signal,
    f27ce_f27_cost_efficiency_costcv_t5_168d_slope_v130_signal,
    f27ce_f27_cost_efficiency_mixentropy_t5_168d_slope_v131_signal,
    f27ce_f27_cost_efficiency_corpass_t5_168d_slope_v132_signal,
    f27ce_f27_cost_efficiency_opexpass_t5_168d_slope_v133_signal,
    f27ce_f27_cost_efficiency_sgnapass_t5_168d_slope_v134_signal,
    f27ce_f27_cost_efficiency_ovhpass_t5_168d_slope_v135_signal,
    f27ce_f27_cost_efficiency_totpass_t5_168d_slope_v136_signal,
    f27ce_f27_cost_efficiency_aiscunit_t5_168d_slope_v137_signal,
    f27ce_f27_cost_efficiency_totunit_t5_168d_slope_v138_signal,
    f27ce_f27_cost_efficiency_sgnaunit_t5_168d_slope_v139_signal,
    f27ce_f27_cost_efficiency_ovhunit_t5_168d_slope_v140_signal,
    f27ce_f27_cost_efficiency_corgrw_t5_168d_slope_v141_signal,
    f27ce_f27_cost_efficiency_opexgrw_t5_168d_slope_v142_signal,
    f27ce_f27_cost_efficiency_sgnagrw_t5_168d_slope_v143_signal,
    f27ce_f27_cost_efficiency_ovhgrw_t5_168d_slope_v144_signal,
    f27ce_f27_cost_efficiency_costgrw_t5_168d_slope_v145_signal,
    f27ce_f27_cost_efficiency_sgnacorgrw_t5_168d_slope_v146_signal,
    f27ce_f27_cost_efficiency_opexsgnagrw_t5_168d_slope_v147_signal,
    f27ce_f27_cost_efficiency_coropexgrw_t5_168d_slope_v148_signal,
    f27ce_f27_cost_efficiency_corovhgrw_t5_168d_slope_v149_signal,
    f27ce_f27_cost_efficiency_gpvscor_t5_168d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_COST_EFFICIENCY_REGISTRY_2ND_001_150 = REGISTRY


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

    print("OK f27_cost_efficiency_2nd_derivatives_001_150_claude: %d features pass" % n_features)
