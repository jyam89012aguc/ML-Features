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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _f45_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f45_roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f45_share(s, w):
    return s / _mean(s, w).replace(0, np.nan)


def _f45_eff(s, w):
    net = s - s.shift(w)
    path = s.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return np.sign(net) * net.abs() / path.replace(0, np.nan)


def _f45_slope(s, w):
    def _f(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        denom = (xc * xc).sum()
        if denom == 0:
            return np.nan
        return float((xc * (a - a.mean())).sum() / denom)

    raw = s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)
    return raw / _mean(s, w).replace(0, np.nan)


def _f45_avgsize(value, units):
    return value / units.replace(0, np.nan)


# jerk (2nd deriv) of holdgrow_63d; step=10d
def f45ia_f45_institutional_accumulation_holdgrow_63d_jerk_v001_signal(shrholders):
    b = _f45_growth(shrholders, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_holdgrow_126d_jerk_v002_signal(shrholders):
    b = _f45_growth(shrholders, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdgrow_252d; step=21d
def f45ia_f45_institutional_accumulation_holdgrow_252d_jerk_v003_signal(shrholders):
    b = _f45_growth(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrow_63d; step=10d
def f45ia_f45_institutional_accumulation_valgrow_63d_jerk_v004_signal(shrvalue):
    b = _f45_growth(shrvalue, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_valgrow_126d_jerk_v005_signal(shrvalue):
    b = _f45_growth(shrvalue, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrow_252d; step=21d
def f45ia_f45_institutional_accumulation_valgrow_252d_jerk_v006_signal(shrvalue):
    b = _f45_growth(shrvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totvalgrow_63d; step=10d
def f45ia_f45_institutional_accumulation_totvalgrow_63d_jerk_v007_signal(totalvalue):
    b = _f45_growth(totalvalue, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totvalgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_totvalgrow_126d_jerk_v008_signal(totalvalue):
    b = _f45_growth(totalvalue, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrow_63d; step=10d
def f45ia_f45_institutional_accumulation_unitgrow_63d_jerk_v009_signal(shrunits):
    b = _f45_growth(shrunits, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_unitgrow_126d_jerk_v010_signal(shrunits):
    b = _f45_growth(shrunits, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrow_252d; step=21d
def f45ia_f45_institutional_accumulation_unitgrow_252d_jerk_v011_signal(shrunits):
    b = _f45_growth(shrunits, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownpct; step=21d
def f45ia_f45_institutional_accumulation_ownpct_jerk_v012_signal(shrvalue, marketcap):
    b = shrvalue / marketcap.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totownpct; step=21d
def f45ia_f45_institutional_accumulation_totownpct_jerk_v013_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own / _mean(own, 252).replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownpctmom_63d; step=10d
def f45ia_f45_institutional_accumulation_ownpctmom_63d_jerk_v014_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownpctmom_126d; step=21d
def f45ia_f45_institutional_accumulation_ownpctmom_126d_jerk_v015_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdroc_21d; step=5d
def f45ia_f45_institutional_accumulation_holdroc_21d_jerk_v016_signal(shrholders):
    b = _f45_roc(shrholders, 21)
    _d1 = b - b.shift(5)
    _d2 = _d1 - _d1.shift(5)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitroc_21d; step=5d
def f45ia_f45_institutional_accumulation_unitroc_21d_jerk_v017_signal(shrunits):
    b = _f45_roc(shrunits, 21)
    _d1 = b - b.shift(5)
    _d2 = _d1 - _d1.shift(5)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of avgpos; step=21d
def f45ia_f45_institutional_accumulation_avgpos_jerk_v018_signal(shrvalue, shrholders):
    b = _f45_avgsize(shrvalue, shrholders)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of avgposgrow_63d; step=10d
def f45ia_f45_institutional_accumulation_avgposgrow_63d_jerk_v019_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    b = _f45_growth(avg, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valperunit; step=21d
def f45ia_f45_institutional_accumulation_valperunit_jerk_v020_signal(shrvalue, shrunits):
    b = _f45_avgsize(shrvalue, shrunits)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdshare_252d; step=21d
def f45ia_f45_institutional_accumulation_holdshare_252d_jerk_v021_signal(shrholders):
    b = _f45_share(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valshare_252d; step=21d
def f45ia_f45_institutional_accumulation_valshare_252d_jerk_v022_signal(shrvalue):
    b = _f45_share(shrvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitshare_126d; step=21d
def f45ia_f45_institutional_accumulation_unitshare_126d_jerk_v023_signal(shrunits):
    b = _f45_share(shrunits, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdz_252d; step=21d
def f45ia_f45_institutional_accumulation_holdz_252d_jerk_v024_signal(shrholders):
    b = _z(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valz_252d; step=21d
def f45ia_f45_institutional_accumulation_valz_252d_jerk_v025_signal(shrvalue):
    b = _z(shrvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitz_126d; step=21d
def f45ia_f45_institutional_accumulation_unitz_126d_jerk_v026_signal(shrunits):
    b = _z(shrunits, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdeff_126d; step=21d
def f45ia_f45_institutional_accumulation_holdeff_126d_jerk_v027_signal(shrholders):
    net = (shrholders - shrholders.shift(126)).abs()
    path = shrholders.diff().abs().rolling(126, min_periods=42).sum()
    b = np.sign(shrholders - shrholders.shift(126)) * net / path.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valslope_126d; step=21d
def f45ia_f45_institutional_accumulation_valslope_126d_jerk_v028_signal(shrvalue):
    b = _f45_slope(shrvalue, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitslope_126d; step=21d
def f45ia_f45_institutional_accumulation_unitslope_126d_jerk_v029_signal(shrunits):
    b = _f45_slope(shrunits, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of breadthspr_63d; step=10d
def f45ia_f45_institutional_accumulation_breadthspr_63d_jerk_v030_signal(shrholders, shrunits):
    b = _f45_growth(shrholders, 63) - _f45_growth(shrunits, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitvaldiv_63d; step=10d
def f45ia_f45_institutional_accumulation_unitvaldiv_63d_jerk_v031_signal(shrunits, shrvalue):
    b = _f45_growth(shrunits, 63) - _f45_growth(shrvalue, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valvscap_63d; step=10d
def f45ia_f45_institutional_accumulation_valvscap_63d_jerk_v032_signal(shrvalue, marketcap):
    b = _f45_growth(shrvalue, 63) - _f45_growth(marketcap, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitvscap_126d; step=21d
def f45ia_f45_institutional_accumulation_unitvscap_126d_jerk_v033_signal(shrunits, marketcap):
    b = _f45_growth(shrunits, 126) - _f45_growth(marketcap, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdgrowmom; step=21d
def f45ia_f45_institutional_accumulation_holdgrowmom_jerk_v034_signal(shrholders):
    g = _f45_growth(shrholders, 63)
    b = g - g.shift(63)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrowmom; step=21d
def f45ia_f45_institutional_accumulation_valgrowmom_jerk_v035_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    b = g - g.shift(63)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownpctz_252d; step=21d
def f45ia_f45_institutional_accumulation_ownpctz_252d_jerk_v036_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = _z(own, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdrank_504d; step=42d
def f45ia_f45_institutional_accumulation_holdrank_504d_jerk_v037_signal(shrholders):
    b = shrholders.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valrank_504d; step=42d
def f45ia_f45_institutional_accumulation_valrank_504d_jerk_v038_signal(shrvalue):
    b = shrvalue.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitrank_504d; step=42d
def f45ia_f45_institutional_accumulation_unitrank_504d_jerk_v039_signal(shrunits):
    b = shrunits.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of blockconc; step=21d
def f45ia_f45_institutional_accumulation_blockconc_jerk_v040_signal(shrvalue, shrholders, marketcap):
    per_holder = shrvalue / shrholders.replace(0, np.nan)
    b = per_holder / marketcap.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitsperhold; step=21d
def f45ia_f45_institutional_accumulation_unitsperhold_jerk_v041_signal(shrunits, shrholders):
    b = shrunits / shrholders.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitsperholdgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_unitsperholdgrow_126d_jerk_v042_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _f45_growth(uph, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of inflow_21d; step=5d
def f45ia_f45_institutional_accumulation_inflow_21d_jerk_v043_signal(shrvalue):
    b = (shrvalue - shrvalue.shift(21)) / _mean(shrvalue, 63).replace(0, np.nan)
    _d1 = b - b.shift(5)
    _d2 = _d1 - _d1.shift(5)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitaccfrac; step=21d
def f45ia_f45_institutional_accumulation_unitaccfrac_jerk_v044_signal(shrunits):
    pos = (_f45_growth(shrunits, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).mean() - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of coverage; step=21d
def f45ia_f45_institutional_accumulation_coverage_jerk_v045_signal(shrvalue, totalvalue):
    b = shrvalue / totalvalue.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of coveragemom_63d; step=10d
def f45ia_f45_institutional_accumulation_coveragemom_63d_jerk_v046_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov - cov.shift(63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdupfrac_63d; step=10d
def f45ia_f45_institutional_accumulation_holdupfrac_63d_jerk_v047_signal(shrholders):
    up = (shrholders.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitupfrac_63d; step=10d
def f45ia_f45_institutional_accumulation_unitupfrac_63d_jerk_v048_signal(shrunits):
    up = (shrunits.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownbuild; step=21d
def f45ia_f45_institutional_accumulation_ownbuild_jerk_v049_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    up = (own > own.shift(21)).astype(float)
    b = up.rolling(126, min_periods=42).mean() - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrowspr; step=21d
def f45ia_f45_institutional_accumulation_valgrowspr_jerk_v050_signal(shrvalue):
    b = _f45_roc(shrvalue, 63) - _f45_roc(shrvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdgrowspr; step=21d
def f45ia_f45_institutional_accumulation_holdgrowspr_jerk_v051_signal(shrholders):
    b = _f45_roc(shrholders, 63) - _f45_roc(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrowspr; step=21d
def f45ia_f45_institutional_accumulation_unitgrowspr_jerk_v052_signal(shrunits):
    b = _f45_roc(shrunits, 63) - _f45_roc(shrunits, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownrank_504d; step=42d
def f45ia_f45_institutional_accumulation_ownrank_504d_jerk_v053_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of crowdconv; step=21d
def f45ia_f45_institutional_accumulation_crowdconv_jerk_v054_signal(shrholders, shrunits):
    spr = _f45_growth(shrholders, 126) - _f45_growth(shrunits, 126)
    b = spr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vphtanh; step=21d
def f45ia_f45_institutional_accumulation_vphtanh_jerk_v055_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    chg = _f45_growth(avg, 21)
    b = np.tanh(8.0 * chg)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdsignmag; step=21d
def f45ia_f45_institutional_accumulation_holdsignmag_jerk_v056_signal(shrholders):
    g = _f45_growth(shrholders, 63)
    b = np.sign(g) * (g.abs() ** 0.5)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valstreak; step=21d
def f45ia_f45_institutional_accumulation_valstreak_jerk_v057_signal(shrvalue):
    pos = (_f45_growth(shrvalue, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).sum()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of uphz_252d; step=21d
def f45ia_f45_institutional_accumulation_uphz_252d_jerk_v058_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _z(uph, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownaccel; step=21d
def f45ia_f45_institutional_accumulation_ownaccel_jerk_v059_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    mom = own - own.shift(63)
    b = mom - mom.shift(63)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vpugrow_126d; step=21d
def f45ia_f45_institutional_accumulation_vpugrow_126d_jerk_v060_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _f45_growth(vpu, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of accqual; step=21d
def f45ia_f45_institutional_accumulation_accqual_jerk_v061_signal(shrholders, shrvalue):
    hs = _f45_slope(shrholders, 126)
    vs = _f45_slope(shrvalue, 126)
    b = np.sign(hs) * np.sign(vs) * (hs.abs() + vs.abs())
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of othervalgrow_126d; step=21d
def f45ia_f45_institutional_accumulation_othervalgrow_126d_jerk_v062_signal(totalvalue, shrvalue):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = _f45_growth(other + 1.0, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holddrawup; step=21d
def f45ia_f45_institutional_accumulation_holddrawup_jerk_v063_signal(shrholders):
    peak = _rmax(shrholders, 252)
    b = shrholders / peak.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valrecov; step=21d
def f45ia_f45_institutional_accumulation_valrecov_jerk_v064_signal(shrvalue):
    trough = _rmin(shrvalue, 252)
    b = shrvalue / trough.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitnewhi; step=21d
def f45ia_f45_institutional_accumulation_unitnewhi_jerk_v065_signal(shrunits):
    hi = _rmax(shrunits, 252)
    is_hi = (shrunits >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of riskadjflow; step=21d
def f45ia_f45_institutional_accumulation_riskadjflow_jerk_v066_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    vol = _f45_growth(shrvalue, 21).rolling(126, min_periods=42).std()
    b = g / vol.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of deepbroad; step=21d
def f45ia_f45_institutional_accumulation_deepbroad_jerk_v067_signal(shrvalue, marketcap, shrholders):
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(63)
    breadth_g = _f45_growth(shrholders, 63)
    b = own_mom * breadth_g
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of growdisp; step=21d
def f45ia_f45_institutional_accumulation_growdisp_jerk_v068_signal(shrvalue):
    g1 = _f45_roc(shrvalue, 63)
    g2 = _f45_roc(shrvalue, 126)
    g3 = _f45_roc(shrvalue, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totownmom_126d; step=21d
def f45ia_f45_institutional_accumulation_totownmom_126d_jerk_v069_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdyoy; step=21d
def f45ia_f45_institutional_accumulation_holdyoy_jerk_v070_signal(shrholders):
    g = _f45_growth(shrholders, 21)
    b = g - g.shift(252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valstability; step=21d
def f45ia_f45_institutional_accumulation_valstability_jerk_v071_signal(shrvalue):
    g = _f45_growth(shrvalue, 21)
    mu = g.rolling(126, min_periods=42).mean()
    sd = g.rolling(126, min_periods=42).std()
    b = mu / sd.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of avgposrank; step=21d
def f45ia_f45_institutional_accumulation_avgposrank_jerk_v072_signal(shrvalue, shrholders):
    avg = shrvalue / shrholders.replace(0, np.nan)
    b = avg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of netacc; step=21d
def f45ia_f45_institutional_accumulation_netacc_jerk_v073_signal(shrunits, shrvalue, marketcap):
    ug = _f45_growth(shrunits, 63)
    own = shrvalue / marketcap.replace(0, np.nan)
    b = ug * own
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of coveragez; step=21d
def f45ia_f45_institutional_accumulation_coveragez_jerk_v074_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = _z(cov, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of accbalance; step=21d
def f45ia_f45_institutional_accumulation_accbalance_jerk_v075_signal(shrunits, shrholders):
    ug = _f45_growth(shrunits, 63).clip(lower=-1.0, upper=1.0)
    hg = _f45_growth(shrholders, 63).clip(lower=-1.0, upper=1.0)
    b = (ug - hg) / (ug.abs() + hg.abs() + 1e-6)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valgrow_5d; step=5d
def f45ia_f45_institutional_accumulation_valgrow_5d_jerk_v076_signal(shrvalue):
    b = _f45_growth(shrvalue, 5)
    _d1 = b - b.shift(5)
    _d2 = _d1 - _d1.shift(5)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdgrow_504d; step=42d
def f45ia_f45_institutional_accumulation_holdgrow_504d_jerk_v077_signal(shrholders):
    b = _f45_growth(shrholders, 504)
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrow_504d; step=42d
def f45ia_f45_institutional_accumulation_unitgrow_504d_jerk_v078_signal(shrunits):
    b = _f45_growth(shrunits, 504)
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totvalgrow_252d; step=21d
def f45ia_f45_institutional_accumulation_totvalgrow_252d_jerk_v079_signal(totalvalue):
    b = _f45_growth(totalvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownpctrank_504d; step=42d
def f45ia_f45_institutional_accumulation_ownpctrank_504d_jerk_v080_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdeff_252d; step=21d
def f45ia_f45_institutional_accumulation_holdeff_252d_jerk_v081_signal(shrholders):
    b = _f45_eff(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of uniteff_252d; step=21d
def f45ia_f45_institutional_accumulation_uniteff_252d_jerk_v082_signal(shrunits):
    b = _f45_eff(shrunits, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valeff_504d; step=42d
def f45ia_f45_institutional_accumulation_valeff_504d_jerk_v083_signal(shrvalue):
    b = _f45_eff(shrvalue, 504)
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of uphvscap; step=21d
def f45ia_f45_institutional_accumulation_uphvscap_jerk_v084_signal(shrunits, shrholders, marketcap):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = uph / marketcap.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valshare_63d; step=10d
def f45ia_f45_institutional_accumulation_valshare_63d_jerk_v085_signal(shrvalue):
    b = _f45_share(shrvalue, 63) - 1.0
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdshare_126d; step=21d
def f45ia_f45_institutional_accumulation_holdshare_126d_jerk_v086_signal(shrholders):
    b = _f45_share(shrholders, 126) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitshare_252d; step=21d
def f45ia_f45_institutional_accumulation_unitshare_252d_jerk_v087_signal(shrunits):
    b = _f45_share(shrunits, 252) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdz_126d; step=21d
def f45ia_f45_institutional_accumulation_holdz_126d_jerk_v088_signal(shrholders):
    b = _z(shrholders, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totvalz_252d; step=21d
def f45ia_f45_institutional_accumulation_totvalz_252d_jerk_v089_signal(totalvalue):
    b = _z(totalvalue, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitz_252d; step=21d
def f45ia_f45_institutional_accumulation_unitz_252d_jerk_v090_signal(shrunits):
    b = _z(shrunits, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valvscap_504d; step=42d
def f45ia_f45_institutional_accumulation_valvscap_504d_jerk_v091_signal(shrvalue, marketcap):
    b = _f45_growth(shrvalue, 504) - _f45_growth(marketcap, 504)
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitvscap_63d; step=10d
def f45ia_f45_institutional_accumulation_unitvscap_63d_jerk_v092_signal(shrunits, marketcap):
    b = _f45_growth(shrunits, 63) - _f45_growth(marketcap, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valholddiv_126d; step=21d
def f45ia_f45_institutional_accumulation_valholddiv_126d_jerk_v093_signal(shrvalue, shrholders):
    b = _f45_growth(shrvalue, 126) - _f45_growth(shrholders, 126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitholddiv_252d; step=21d
def f45ia_f45_institutional_accumulation_unitholddiv_252d_jerk_v094_signal(shrunits, shrholders):
    b = _f45_growth(shrunits, 252) - _f45_growth(shrholders, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valaccel_126d; step=21d
def f45ia_f45_institutional_accumulation_valaccel_126d_jerk_v095_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    b = g - g.shift(126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitaccel_63d; step=10d
def f45ia_f45_institutional_accumulation_unitaccel_63d_jerk_v096_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    b = g - g.shift(63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdaccel_126d; step=21d
def f45ia_f45_institutional_accumulation_holdaccel_126d_jerk_v097_signal(shrholders):
    g = _f45_growth(shrholders, 126)
    b = g - g.shift(126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of coveragerank; step=21d
def f45ia_f45_institutional_accumulation_coveragerank_jerk_v098_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of covgrowspr; step=21d
def f45ia_f45_institutional_accumulation_covgrowspr_jerk_v099_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = _f45_roc(cov, 63) - _f45_roc(cov, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of flowtilt; step=21d
def f45ia_f45_institutional_accumulation_flowtilt_jerk_v100_signal(totalvalue):
    b = (totalvalue - totalvalue.shift(21)) / _mean(totalvalue, 504).replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitflowratio; step=21d
def f45ia_f45_institutional_accumulation_unitflowratio_jerk_v101_signal(shrunits):
    fast = (shrunits - shrunits.shift(21)) / _mean(shrunits, 252).replace(0, np.nan)
    slow = (shrunits - shrunits.shift(126)) / _mean(shrunits, 252).replace(0, np.nan)
    b = fast - slow / 6.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdnewhi; step=21d
def f45ia_f45_institutional_accumulation_holdnewhi_jerk_v102_signal(shrholders):
    hi = _rmax(shrholders, 252)
    is_hi = (shrholders >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valnewhi; step=21d
def f45ia_f45_institutional_accumulation_valnewhi_jerk_v103_signal(shrvalue):
    hi = _rmax(shrvalue, 252)
    is_hi = (shrvalue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitdrawup; step=21d
def f45ia_f45_institutional_accumulation_unitdrawup_jerk_v104_signal(shrunits):
    peak = _rmax(shrunits, 252)
    b = shrunits / peak.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valrecov_504d; step=42d
def f45ia_f45_institutional_accumulation_valrecov_504d_jerk_v105_signal(shrvalue):
    trough = _rmin(shrvalue, 504)
    b = shrvalue / trough.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(42)
    _d2 = _d1 - _d1.shift(42)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdrecov; step=21d
def f45ia_f45_institutional_accumulation_holdrecov_jerk_v106_signal(shrholders):
    trough = _rmin(shrholders, 252)
    b = shrholders / trough.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vphgrow_252d; step=21d
def f45ia_f45_institutional_accumulation_vphgrow_252d_jerk_v107_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    b = _f45_growth(vph, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vphz_252d; step=21d
def f45ia_f45_institutional_accumulation_vphz_252d_jerk_v108_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    b = _z(vph, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vpuz_252d; step=21d
def f45ia_f45_institutional_accumulation_vpuz_252d_jerk_v109_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _z(vpu, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vpugrow_252d; step=21d
def f45ia_f45_institutional_accumulation_vpugrow_252d_jerk_v110_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _f45_growth(vpu, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vpuaccel; step=21d
def f45ia_f45_institutional_accumulation_vpuaccel_jerk_v111_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    g = _f45_growth(vpu, 63)
    b = g - g.shift(63)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of covsignmag; step=21d
def f45ia_f45_institutional_accumulation_covsignmag_jerk_v112_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    mom = cov - cov.shift(126)
    b = np.sign(mom) * (mom.abs() ** 0.5)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valsignmag; step=21d
def f45ia_f45_institutional_accumulation_valsignmag_jerk_v113_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    b = np.sign(g) * (g.abs() ** 0.5)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdstreak; step=21d
def f45ia_f45_institutional_accumulation_holdstreak_jerk_v114_signal(shrholders):
    pos = (_f45_growth(shrholders, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).sum()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitstreak; step=21d
def f45ia_f45_institutional_accumulation_unitstreak_jerk_v115_signal(shrunits):
    pos = (_f45_growth(shrunits, 21) > 0).astype(float)
    b = pos.rolling(252, min_periods=84).sum()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of tottanh; step=21d
def f45ia_f45_institutional_accumulation_tottanh_jerk_v116_signal(totalvalue):
    chg = _f45_growth(totalvalue, 63)
    b = np.tanh(10.0 * chg)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unittanh; step=21d
def f45ia_f45_institutional_accumulation_unittanh_jerk_v117_signal(shrunits):
    chg = _f45_growth(shrunits, 63)
    b = np.tanh(8.0 * chg)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valdownside; step=21d
def f45ia_f45_institutional_accumulation_valdownside_jerk_v118_signal(shrvalue):
    g = _f45_growth(shrvalue, 21)
    neg = g.where(g < 0)
    b = neg.rolling(252, min_periods=84).std()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdsharpe; step=21d
def f45ia_f45_institutional_accumulation_holdsharpe_jerk_v119_signal(shrholders):
    g = _f45_growth(shrholders, 21)
    mu = g.rolling(126, min_periods=42).mean()
    sd = g.rolling(126, min_periods=42).std()
    b = mu / sd.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of deepreal; step=21d
def f45ia_f45_institutional_accumulation_deepreal_jerk_v120_signal(shrvalue, marketcap, shrunits):
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(126)
    ug = _f45_growth(shrunits, 126)
    b = own_mom * ug
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of accqual2; step=21d
def f45ia_f45_institutional_accumulation_accqual2_jerk_v121_signal(shrholders, shrvalue):
    he = _f45_eff(shrholders, 252)
    ve = _f45_eff(shrvalue, 252)
    b = np.sign(he) * np.sign(ve) * (he.abs() + ve.abs())
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of growdisp2; step=21d
def f45ia_f45_institutional_accumulation_growdisp2_jerk_v122_signal(shrvalue):
    g1 = _f45_roc(shrvalue, 21)
    g2 = _f45_roc(shrvalue, 63)
    g3 = _f45_roc(shrvalue, 126)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitgrowdisp; step=21d
def f45ia_f45_institutional_accumulation_unitgrowdisp_jerk_v123_signal(shrunits):
    g1 = _f45_roc(shrunits, 63)
    g2 = _f45_roc(shrunits, 126)
    g3 = _f45_roc(shrunits, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of otherownpct; step=21d
def f45ia_f45_institutional_accumulation_otherownpct_jerk_v124_signal(totalvalue, shrvalue, marketcap):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = other / marketcap.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of othergrow_63d; step=10d
def f45ia_f45_institutional_accumulation_othergrow_63d_jerk_v125_signal(totalvalue, shrvalue):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = _f45_growth(other + 1.0, 63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totownmom_63d; step=10d
def f45ia_f45_institutional_accumulation_totownmom_63d_jerk_v126_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(63)
    _d1 = b - b.shift(10)
    _d2 = _d1 - _d1.shift(10)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totownaccel; step=21d
def f45ia_f45_institutional_accumulation_totownaccel_jerk_v127_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    mom = own - own.shift(63)
    b = mom - mom.shift(63)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of riskadjflow126; step=21d
def f45ia_f45_institutional_accumulation_riskadjflow126_jerk_v128_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    vol = _f45_growth(shrvalue, 21).rolling(252, min_periods=84).std()
    b = g / vol.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitriskadj; step=21d
def f45ia_f45_institutional_accumulation_unitriskadj_jerk_v129_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    vol = _f45_growth(shrunits, 21).rolling(126, min_periods=42).std()
    b = g / vol.replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of covmedrev; step=21d
def f45ia_f45_institutional_accumulation_covmedrev_jerk_v130_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    med = cov.rolling(252, min_periods=84).median()
    b = cov / med.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitasym; step=21d
def f45ia_f45_institutional_accumulation_unitasym_jerk_v131_signal(shrunits):
    chg = shrunits.pct_change()
    up = chg.clip(lower=0).rolling(126, min_periods=42).mean()
    dn = (-chg.clip(upper=0)).rolling(126, min_periods=42).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of concregime; step=21d
def f45ia_f45_institutional_accumulation_concregime_jerk_v132_signal(shrvalue, shrholders):
    spr = _f45_growth(shrvalue, 63) - _f45_growth(shrholders, 63)
    b = spr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of totowndisp252; step=21d
def f45ia_f45_institutional_accumulation_totowndisp252_jerk_v133_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.ewm(span=252, min_periods=84).mean()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of covdisp; step=21d
def f45ia_f45_institutional_accumulation_covdisp_jerk_v134_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov - cov.ewm(span=126, min_periods=42).mean()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valyoy; step=21d
def f45ia_f45_institutional_accumulation_valyoy_jerk_v135_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    b = g - g.shift(252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unityoy; step=21d
def f45ia_f45_institutional_accumulation_unityoy_jerk_v136_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    b = g - g.shift(252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of netacc2; step=21d
def f45ia_f45_institutional_accumulation_netacc2_jerk_v137_signal(shrholders, shrvalue, marketcap):
    hg = _f45_growth(shrholders, 126)
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(126)
    b = hg + 5.0 * own_mom
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vphaccel; step=21d
def f45ia_f45_institutional_accumulation_vphaccel_jerk_v138_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    g = _f45_growth(vph, 126)
    b = g - g.shift(126)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of vpurank; step=21d
def f45ia_f45_institutional_accumulation_vpurank_jerk_v139_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = vpu.rolling(504, min_periods=126).rank(pct=True) - 0.5
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of breadthvalbal; step=21d
def f45ia_f45_institutional_accumulation_breadthvalbal_jerk_v140_signal(shrholders, shrvalue):
    hg = _f45_growth(shrholders, 63).clip(lower=-1.0, upper=1.0)
    vg = _f45_growth(shrvalue, 63).clip(lower=-1.0, upper=1.0)
    b = (hg - vg) / (hg.abs() + vg.abs() + 1e-6)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of activebal; step=21d
def f45ia_f45_institutional_accumulation_activebal_jerk_v141_signal(shrvalue, totalvalue):
    vg = _f45_growth(shrvalue, 63).clip(lower=-1.0, upper=1.0)
    tg = _f45_growth(totalvalue, 63).clip(lower=-1.0, upper=1.0)
    b = (vg - tg) / (vg.abs() + tg.abs() + 1e-6)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of unitbreakout; step=21d
def f45ia_f45_institutional_accumulation_unitbreakout_jerk_v142_signal(shrunits):
    prior_hi = shrunits.shift(21).rolling(252, min_periods=84).max()
    b = shrunits / prior_hi.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valbreakout; step=21d
def f45ia_f45_institutional_accumulation_valbreakout_jerk_v143_signal(shrvalue):
    prior_hi = shrvalue.shift(1).rolling(252, min_periods=84).max()
    b = shrvalue / prior_hi.replace(0, np.nan) - 1.0
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of covflow; step=21d
def f45ia_f45_institutional_accumulation_covflow_jerk_v144_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = (cov - cov.shift(21)) / _mean(cov, 126).replace(0, np.nan)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of upheff; step=21d
def f45ia_f45_institutional_accumulation_upheff_jerk_v145_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _f45_eff(uph, 252)
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of ownchurn; step=21d
def f45ia_f45_institutional_accumulation_ownchurn_jerk_v146_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own.pct_change().rolling(126, min_periods=42).std()
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of valtotcompress; step=21d
def f45ia_f45_institutional_accumulation_valtotcompress_jerk_v147_signal(shrvalue, totalvalue):
    spr = _f45_growth(shrvalue, 126) - _f45_growth(totalvalue, 126)
    typ = spr.rolling(252, min_periods=84).mean()
    b = spr - typ
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of holdtotcompress; step=21d
def f45ia_f45_institutional_accumulation_holdtotcompress_jerk_v148_signal(shrholders, totalvalue):
    spr = _f45_growth(shrholders, 126) - _f45_growth(totalvalue, 126)
    typ = spr.rolling(252, min_periods=84).mean()
    b = spr - typ
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of triplecomp; step=21d
def f45ia_f45_institutional_accumulation_triplecomp_jerk_v149_signal(shrvalue, marketcap, shrholders):
    own = shrvalue / marketcap.replace(0, np.nan)
    breadth = _f45_share(shrholders, 252) - 1.0
    valsurge = _f45_share(shrvalue, 126) - 1.0
    b = breadth * valsurge * np.sign(own - own.shift(63))
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of smartflow; step=21d
def f45ia_f45_institutional_accumulation_smartflow_jerk_v150_signal(shrvalue, shrholders, marketcap):
    vph = shrvalue / shrholders.replace(0, np.nan)
    vphg = _f45_growth(vph, 63)
    own = shrvalue / marketcap.replace(0, np.nan)
    b = vphg * own
    _d1 = b - b.shift(21)
    _d2 = _d1 - _d1.shift(21)
    result = _d2
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f45ia_f45_institutional_accumulation_holdgrow_63d_jerk_v001_signal,
    f45ia_f45_institutional_accumulation_holdgrow_126d_jerk_v002_signal,
    f45ia_f45_institutional_accumulation_holdgrow_252d_jerk_v003_signal,
    f45ia_f45_institutional_accumulation_valgrow_63d_jerk_v004_signal,
    f45ia_f45_institutional_accumulation_valgrow_126d_jerk_v005_signal,
    f45ia_f45_institutional_accumulation_valgrow_252d_jerk_v006_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_63d_jerk_v007_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_126d_jerk_v008_signal,
    f45ia_f45_institutional_accumulation_unitgrow_63d_jerk_v009_signal,
    f45ia_f45_institutional_accumulation_unitgrow_126d_jerk_v010_signal,
    f45ia_f45_institutional_accumulation_unitgrow_252d_jerk_v011_signal,
    f45ia_f45_institutional_accumulation_ownpct_jerk_v012_signal,
    f45ia_f45_institutional_accumulation_totownpct_jerk_v013_signal,
    f45ia_f45_institutional_accumulation_ownpctmom_63d_jerk_v014_signal,
    f45ia_f45_institutional_accumulation_ownpctmom_126d_jerk_v015_signal,
    f45ia_f45_institutional_accumulation_holdroc_21d_jerk_v016_signal,
    f45ia_f45_institutional_accumulation_unitroc_21d_jerk_v017_signal,
    f45ia_f45_institutional_accumulation_avgpos_jerk_v018_signal,
    f45ia_f45_institutional_accumulation_avgposgrow_63d_jerk_v019_signal,
    f45ia_f45_institutional_accumulation_valperunit_jerk_v020_signal,
    f45ia_f45_institutional_accumulation_holdshare_252d_jerk_v021_signal,
    f45ia_f45_institutional_accumulation_valshare_252d_jerk_v022_signal,
    f45ia_f45_institutional_accumulation_unitshare_126d_jerk_v023_signal,
    f45ia_f45_institutional_accumulation_holdz_252d_jerk_v024_signal,
    f45ia_f45_institutional_accumulation_valz_252d_jerk_v025_signal,
    f45ia_f45_institutional_accumulation_unitz_126d_jerk_v026_signal,
    f45ia_f45_institutional_accumulation_holdeff_126d_jerk_v027_signal,
    f45ia_f45_institutional_accumulation_valslope_126d_jerk_v028_signal,
    f45ia_f45_institutional_accumulation_unitslope_126d_jerk_v029_signal,
    f45ia_f45_institutional_accumulation_breadthspr_63d_jerk_v030_signal,
    f45ia_f45_institutional_accumulation_unitvaldiv_63d_jerk_v031_signal,
    f45ia_f45_institutional_accumulation_valvscap_63d_jerk_v032_signal,
    f45ia_f45_institutional_accumulation_unitvscap_126d_jerk_v033_signal,
    f45ia_f45_institutional_accumulation_holdgrowmom_jerk_v034_signal,
    f45ia_f45_institutional_accumulation_valgrowmom_jerk_v035_signal,
    f45ia_f45_institutional_accumulation_ownpctz_252d_jerk_v036_signal,
    f45ia_f45_institutional_accumulation_holdrank_504d_jerk_v037_signal,
    f45ia_f45_institutional_accumulation_valrank_504d_jerk_v038_signal,
    f45ia_f45_institutional_accumulation_unitrank_504d_jerk_v039_signal,
    f45ia_f45_institutional_accumulation_blockconc_jerk_v040_signal,
    f45ia_f45_institutional_accumulation_unitsperhold_jerk_v041_signal,
    f45ia_f45_institutional_accumulation_unitsperholdgrow_126d_jerk_v042_signal,
    f45ia_f45_institutional_accumulation_inflow_21d_jerk_v043_signal,
    f45ia_f45_institutional_accumulation_unitaccfrac_jerk_v044_signal,
    f45ia_f45_institutional_accumulation_coverage_jerk_v045_signal,
    f45ia_f45_institutional_accumulation_coveragemom_63d_jerk_v046_signal,
    f45ia_f45_institutional_accumulation_holdupfrac_63d_jerk_v047_signal,
    f45ia_f45_institutional_accumulation_unitupfrac_63d_jerk_v048_signal,
    f45ia_f45_institutional_accumulation_ownbuild_jerk_v049_signal,
    f45ia_f45_institutional_accumulation_valgrowspr_jerk_v050_signal,
    f45ia_f45_institutional_accumulation_holdgrowspr_jerk_v051_signal,
    f45ia_f45_institutional_accumulation_unitgrowspr_jerk_v052_signal,
    f45ia_f45_institutional_accumulation_ownrank_504d_jerk_v053_signal,
    f45ia_f45_institutional_accumulation_crowdconv_jerk_v054_signal,
    f45ia_f45_institutional_accumulation_vphtanh_jerk_v055_signal,
    f45ia_f45_institutional_accumulation_holdsignmag_jerk_v056_signal,
    f45ia_f45_institutional_accumulation_valstreak_jerk_v057_signal,
    f45ia_f45_institutional_accumulation_uphz_252d_jerk_v058_signal,
    f45ia_f45_institutional_accumulation_ownaccel_jerk_v059_signal,
    f45ia_f45_institutional_accumulation_vpugrow_126d_jerk_v060_signal,
    f45ia_f45_institutional_accumulation_accqual_jerk_v061_signal,
    f45ia_f45_institutional_accumulation_othervalgrow_126d_jerk_v062_signal,
    f45ia_f45_institutional_accumulation_holddrawup_jerk_v063_signal,
    f45ia_f45_institutional_accumulation_valrecov_jerk_v064_signal,
    f45ia_f45_institutional_accumulation_unitnewhi_jerk_v065_signal,
    f45ia_f45_institutional_accumulation_riskadjflow_jerk_v066_signal,
    f45ia_f45_institutional_accumulation_deepbroad_jerk_v067_signal,
    f45ia_f45_institutional_accumulation_growdisp_jerk_v068_signal,
    f45ia_f45_institutional_accumulation_totownmom_126d_jerk_v069_signal,
    f45ia_f45_institutional_accumulation_holdyoy_jerk_v070_signal,
    f45ia_f45_institutional_accumulation_valstability_jerk_v071_signal,
    f45ia_f45_institutional_accumulation_avgposrank_jerk_v072_signal,
    f45ia_f45_institutional_accumulation_netacc_jerk_v073_signal,
    f45ia_f45_institutional_accumulation_coveragez_jerk_v074_signal,
    f45ia_f45_institutional_accumulation_accbalance_jerk_v075_signal,
    f45ia_f45_institutional_accumulation_valgrow_5d_jerk_v076_signal,
    f45ia_f45_institutional_accumulation_holdgrow_504d_jerk_v077_signal,
    f45ia_f45_institutional_accumulation_unitgrow_504d_jerk_v078_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_252d_jerk_v079_signal,
    f45ia_f45_institutional_accumulation_ownpctrank_504d_jerk_v080_signal,
    f45ia_f45_institutional_accumulation_holdeff_252d_jerk_v081_signal,
    f45ia_f45_institutional_accumulation_uniteff_252d_jerk_v082_signal,
    f45ia_f45_institutional_accumulation_valeff_504d_jerk_v083_signal,
    f45ia_f45_institutional_accumulation_uphvscap_jerk_v084_signal,
    f45ia_f45_institutional_accumulation_valshare_63d_jerk_v085_signal,
    f45ia_f45_institutional_accumulation_holdshare_126d_jerk_v086_signal,
    f45ia_f45_institutional_accumulation_unitshare_252d_jerk_v087_signal,
    f45ia_f45_institutional_accumulation_holdz_126d_jerk_v088_signal,
    f45ia_f45_institutional_accumulation_totvalz_252d_jerk_v089_signal,
    f45ia_f45_institutional_accumulation_unitz_252d_jerk_v090_signal,
    f45ia_f45_institutional_accumulation_valvscap_504d_jerk_v091_signal,
    f45ia_f45_institutional_accumulation_unitvscap_63d_jerk_v092_signal,
    f45ia_f45_institutional_accumulation_valholddiv_126d_jerk_v093_signal,
    f45ia_f45_institutional_accumulation_unitholddiv_252d_jerk_v094_signal,
    f45ia_f45_institutional_accumulation_valaccel_126d_jerk_v095_signal,
    f45ia_f45_institutional_accumulation_unitaccel_63d_jerk_v096_signal,
    f45ia_f45_institutional_accumulation_holdaccel_126d_jerk_v097_signal,
    f45ia_f45_institutional_accumulation_coveragerank_jerk_v098_signal,
    f45ia_f45_institutional_accumulation_covgrowspr_jerk_v099_signal,
    f45ia_f45_institutional_accumulation_flowtilt_jerk_v100_signal,
    f45ia_f45_institutional_accumulation_unitflowratio_jerk_v101_signal,
    f45ia_f45_institutional_accumulation_holdnewhi_jerk_v102_signal,
    f45ia_f45_institutional_accumulation_valnewhi_jerk_v103_signal,
    f45ia_f45_institutional_accumulation_unitdrawup_jerk_v104_signal,
    f45ia_f45_institutional_accumulation_valrecov_504d_jerk_v105_signal,
    f45ia_f45_institutional_accumulation_holdrecov_jerk_v106_signal,
    f45ia_f45_institutional_accumulation_vphgrow_252d_jerk_v107_signal,
    f45ia_f45_institutional_accumulation_vphz_252d_jerk_v108_signal,
    f45ia_f45_institutional_accumulation_vpuz_252d_jerk_v109_signal,
    f45ia_f45_institutional_accumulation_vpugrow_252d_jerk_v110_signal,
    f45ia_f45_institutional_accumulation_vpuaccel_jerk_v111_signal,
    f45ia_f45_institutional_accumulation_covsignmag_jerk_v112_signal,
    f45ia_f45_institutional_accumulation_valsignmag_jerk_v113_signal,
    f45ia_f45_institutional_accumulation_holdstreak_jerk_v114_signal,
    f45ia_f45_institutional_accumulation_unitstreak_jerk_v115_signal,
    f45ia_f45_institutional_accumulation_tottanh_jerk_v116_signal,
    f45ia_f45_institutional_accumulation_unittanh_jerk_v117_signal,
    f45ia_f45_institutional_accumulation_valdownside_jerk_v118_signal,
    f45ia_f45_institutional_accumulation_holdsharpe_jerk_v119_signal,
    f45ia_f45_institutional_accumulation_deepreal_jerk_v120_signal,
    f45ia_f45_institutional_accumulation_accqual2_jerk_v121_signal,
    f45ia_f45_institutional_accumulation_growdisp2_jerk_v122_signal,
    f45ia_f45_institutional_accumulation_unitgrowdisp_jerk_v123_signal,
    f45ia_f45_institutional_accumulation_otherownpct_jerk_v124_signal,
    f45ia_f45_institutional_accumulation_othergrow_63d_jerk_v125_signal,
    f45ia_f45_institutional_accumulation_totownmom_63d_jerk_v126_signal,
    f45ia_f45_institutional_accumulation_totownaccel_jerk_v127_signal,
    f45ia_f45_institutional_accumulation_riskadjflow126_jerk_v128_signal,
    f45ia_f45_institutional_accumulation_unitriskadj_jerk_v129_signal,
    f45ia_f45_institutional_accumulation_covmedrev_jerk_v130_signal,
    f45ia_f45_institutional_accumulation_unitasym_jerk_v131_signal,
    f45ia_f45_institutional_accumulation_concregime_jerk_v132_signal,
    f45ia_f45_institutional_accumulation_totowndisp252_jerk_v133_signal,
    f45ia_f45_institutional_accumulation_covdisp_jerk_v134_signal,
    f45ia_f45_institutional_accumulation_valyoy_jerk_v135_signal,
    f45ia_f45_institutional_accumulation_unityoy_jerk_v136_signal,
    f45ia_f45_institutional_accumulation_netacc2_jerk_v137_signal,
    f45ia_f45_institutional_accumulation_vphaccel_jerk_v138_signal,
    f45ia_f45_institutional_accumulation_vpurank_jerk_v139_signal,
    f45ia_f45_institutional_accumulation_breadthvalbal_jerk_v140_signal,
    f45ia_f45_institutional_accumulation_activebal_jerk_v141_signal,
    f45ia_f45_institutional_accumulation_unitbreakout_jerk_v142_signal,
    f45ia_f45_institutional_accumulation_valbreakout_jerk_v143_signal,
    f45ia_f45_institutional_accumulation_covflow_jerk_v144_signal,
    f45ia_f45_institutional_accumulation_upheff_jerk_v145_signal,
    f45ia_f45_institutional_accumulation_ownchurn_jerk_v146_signal,
    f45ia_f45_institutional_accumulation_valtotcompress_jerk_v147_signal,
    f45ia_f45_institutional_accumulation_holdtotcompress_jerk_v148_signal,
    f45ia_f45_institutional_accumulation_triplecomp_jerk_v149_signal,
    f45ia_f45_institutional_accumulation_smartflow_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_INSTITUTIONAL_ACCUMULATION_REGISTRY_3RD_DERIVATIVES_001_150 = REGISTRY


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

    shrholders = _fund(101, base=350.0, drift=0.05, vol=0.10).rename("shrholders")
    shrunits = _fund(102, base=4.0e7, drift=0.06, vol=0.12).rename("shrunits")
    shrvalue = _fund(103, base=6.0e8, drift=0.05, vol=0.11).rename("shrvalue")
    totalvalue = _fund(104, base=9.0e8, drift=0.045, vol=0.10).rename("totalvalue")
    marketcap = _fund(105, base=1.5e9, drift=0.035, vol=0.13).rename("marketcap")

    cols = {
        "shrholders": shrholders, "shrunits": shrunits, "shrvalue": shrvalue,
        "totalvalue": totalvalue, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f45_institutional_accumulation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
