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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(np.dot(x, a) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _roc(s, w):
    return s - s.shift(w)


def f24mt_f24_margin_trajectory_gmmean_126d_jerk_v001_signal(grossmargin):
    base = _mean(grossmargin, 126)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmean_63d_jerk_v002_signal(netmargin):
    base = _mean(netmargin, 63)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emmean_126d_jerk_v003_signal(ebitdamargin):
    base = _mean(ebitdamargin, 126)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ommean_63d_jerk_v004_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _mean(om, 63)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpmmean_63d_jerk_v005_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _mean(gm, 63)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmsl_126d_jerk_v006_signal(grossmargin):
    base = _slope(grossmargin, 126)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmsl_126d_jerk_v007_signal(netmargin):
    base = _slope(netmargin, 126)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emsl_252d_jerk_v008_signal(ebitdamargin):
    base = _slope(ebitdamargin, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omsl_126d_jerk_v009_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _slope(om, 126)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpsl_126d_jerk_v010_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _slope(gm, 126)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gnspr_63d_jerk_v011_signal(grossmargin, netmargin):
    base = grossmargin - netmargin
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gespr_126d_jerk_v012_signal(grossmargin, ebitdamargin):
    base = grossmargin - ebitdamargin
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_enspr_126d_jerk_v013_signal(ebitdamargin, netmargin):
    base = ebitdamargin - netmargin
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omnmspr_126d_jerk_v014_signal(opinc, revenue, netmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - netmargin
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmz_252d_jerk_v015_signal(grossmargin):
    base = _z(grossmargin, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmz_252d_jerk_v016_signal(netmargin):
    base = _z(netmargin, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emz_252d_jerk_v017_signal(ebitdamargin):
    base = _z(ebitdamargin, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omz_252d_jerk_v018_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _z(om, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmstab_252d_jerk_v019_signal(grossmargin):
    base = _mean(grossmargin, 252).abs() / _std(grossmargin, 252).replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmstab_126d_jerk_v020_signal(netmargin):
    base = _mean(netmargin, 126).abs() / _std(netmargin, 126).replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emudbal_252d_jerk_v021_signal(ebitdamargin):
    d = ebitdamargin.diff()
    up = d.where(d > 0).rolling(252, min_periods=63).sum()
    dn = (-d.where(d < 0)).rolling(252, min_periods=63).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmemad_63d_jerk_v022_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=63, min_periods=21).mean()
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmemad_63d_jerk_v023_signal(netmargin):
    base = netmargin - netmargin.ewm(span=63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ememad_126d_jerk_v024_signal(ebitdamargin):
    base = ebitdamargin - ebitdamargin.ewm(span=126, min_periods=42).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omemad_63d_jerk_v025_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - om.ewm(span=63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmrng_252d_jerk_v026_signal(grossmargin):
    hi = grossmargin.rolling(252, min_periods=63).max()
    lo = grossmargin.rolling(252, min_periods=63).min()
    base = (grossmargin - lo) / (hi - lo).replace(0, np.nan)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmrng_252d_jerk_v027_signal(netmargin):
    hi = netmargin.rolling(252, min_periods=63).max()
    lo = netmargin.rolling(252, min_periods=63).min()
    base = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emrng_252d_jerk_v028_signal(ebitdamargin):
    hi = ebitdamargin.rolling(252, min_periods=63).max()
    lo = ebitdamargin.rolling(252, min_periods=63).min()
    base = (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdev_252d_jerk_v029_signal(grossmargin):
    base = grossmargin - _mean(grossmargin, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmdev_252d_jerk_v030_signal(netmargin):
    base = netmargin - _mean(netmargin, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emdev_252d_jerk_v031_signal(ebitdamargin):
    base = ebitdamargin - _mean(ebitdamargin, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdev_252d_jerk_v032_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - _mean(om, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_passthru_252d_jerk_v033_signal(grossmargin, netmargin):
    base = netmargin / grossmargin.replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_egconv_126d_jerk_v034_signal(ebitdamargin, grossmargin):
    base = ebitdamargin / grossmargin.replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omgmconv_126d_jerk_v035_signal(opinc, revenue, grossmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om / grossmargin.replace(0, np.nan)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmtrough_252d_jerk_v036_signal(grossmargin):
    tr = grossmargin.rolling(252, min_periods=63).min()
    base = grossmargin / tr.replace(0, np.nan) - 1.0
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmpeak_252d_jerk_v037_signal(netmargin):
    pk = netmargin.rolling(252, min_periods=63).max()
    base = netmargin / pk.replace(0, np.nan) - 1.0
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omrng_252d_jerk_v038_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    hi = om.rolling(252, min_periods=63).max()
    lo = om.rolling(252, min_periods=63).min()
    base = (om - lo) / (hi - lo).replace(0, np.nan)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmtrough_252d_jerk_v039_signal(netmargin):
    tr = netmargin.rolling(252, min_periods=63).min()
    base = netmargin / tr.replace(0, np.nan) - 1.0
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emhit_252d_jerk_v040_signal(ebitdamargin):
    base = (ebitdamargin.diff() > 0).astype(float).rolling(252, min_periods=63).mean() - 0.5
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emcurv_126d_jerk_v041_signal(ebitdamargin):
    base = (ebitdamargin - ebitdamargin.shift(63)) - (ebitdamargin.shift(63) - ebitdamargin.shift(126))
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emsmooth_126d_jerk_v042_signal(ebitdamargin):
    base = ebitdamargin.ewm(span=42, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdownv_252d_jerk_v043_signal(grossmargin):
    d = grossmargin.diff()
    base = d.where(d < 0).rolling(252, min_periods=63).std()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmudbal_126d_jerk_v044_signal(netmargin):
    d = netmargin.diff()
    up = d.where(d > 0).rolling(126, min_periods=42).sum()
    dn = (-d.where(d < 0)).rolling(126, min_periods=42).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ompass_126d_jerk_v045_signal(opinc, revenue, ebitdamargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - ebitdamargin
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmpeak_252d_jerk_v046_signal(grossmargin):
    pk = grossmargin.rolling(252, min_periods=63).max()
    base = grossmargin / pk.replace(0, np.nan) - 1.0
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emtrough_252d_jerk_v047_signal(ebitdamargin):
    tr = ebitdamargin.rolling(252, min_periods=63).min()
    base = ebitdamargin / tr.replace(0, np.nan) - 1.0
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmed_252d_jerk_v048_signal(netmargin):
    base = netmargin - netmargin.rolling(252, min_periods=63).median()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdisp_126d_jerk_v049_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=126, min_periods=63).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdrift_252d_jerk_v050_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om.diff(21).rolling(252, min_periods=63).sum()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmmeanz_126d_jerk_v051_signal(grossmargin):
    base = _mean(grossmargin, 126)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmeanz_63d_jerk_v052_signal(netmargin):
    base = _mean(netmargin, 63)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emmeanz_126d_jerk_v053_signal(ebitdamargin):
    base = _mean(ebitdamargin, 126)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ommeanz_63d_jerk_v054_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _mean(om, 63)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpmmeanz_63d_jerk_v055_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _mean(gm, 63)
    base = _z(base, 252)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmslz_126d_jerk_v056_signal(grossmargin):
    base = _slope(grossmargin, 126)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmslz_126d_jerk_v057_signal(netmargin):
    base = _slope(netmargin, 126)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emslz_252d_jerk_v058_signal(ebitdamargin):
    base = _slope(ebitdamargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omslz_126d_jerk_v059_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _slope(om, 126)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpslz_126d_jerk_v060_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _slope(gm, 126)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gnsprz_63d_jerk_v061_signal(grossmargin, netmargin):
    base = grossmargin - netmargin
    base = _z(base, 252)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gesprz_126d_jerk_v062_signal(grossmargin, ebitdamargin):
    base = grossmargin - ebitdamargin
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ensprz_126d_jerk_v063_signal(ebitdamargin, netmargin):
    base = ebitdamargin - netmargin
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omnmsprz_126d_jerk_v064_signal(opinc, revenue, netmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - netmargin
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmzz_252d_jerk_v065_signal(grossmargin):
    base = _z(grossmargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmzz_252d_jerk_v066_signal(netmargin):
    base = _z(netmargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emzz_252d_jerk_v067_signal(ebitdamargin):
    base = _z(ebitdamargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omzz_252d_jerk_v068_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _z(om, 252)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmstabz_252d_jerk_v069_signal(grossmargin):
    base = _mean(grossmargin, 252).abs() / _std(grossmargin, 252).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmstabz_126d_jerk_v070_signal(netmargin):
    base = _mean(netmargin, 126).abs() / _std(netmargin, 126).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emudbalz_252d_jerk_v071_signal(ebitdamargin):
    d = ebitdamargin.diff()
    up = d.where(d > 0).rolling(252, min_periods=63).sum()
    dn = (-d.where(d < 0)).rolling(252, min_periods=63).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmemadz_63d_jerk_v072_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=63, min_periods=21).mean()
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmemadz_63d_jerk_v073_signal(netmargin):
    base = netmargin - netmargin.ewm(span=63, min_periods=21).mean()
    base = _z(base, 252)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ememadz_126d_jerk_v074_signal(ebitdamargin):
    base = ebitdamargin - ebitdamargin.ewm(span=126, min_periods=42).mean()
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omemadz_63d_jerk_v075_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - om.ewm(span=63, min_periods=21).mean()
    base = _z(base, 252)
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmrngz_252d_jerk_v076_signal(grossmargin):
    hi = grossmargin.rolling(252, min_periods=63).max()
    lo = grossmargin.rolling(252, min_periods=63).min()
    base = (grossmargin - lo) / (hi - lo).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmrngz_252d_jerk_v077_signal(netmargin):
    hi = netmargin.rolling(252, min_periods=63).max()
    lo = netmargin.rolling(252, min_periods=63).min()
    base = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emrngz_252d_jerk_v078_signal(ebitdamargin):
    hi = ebitdamargin.rolling(252, min_periods=63).max()
    lo = ebitdamargin.rolling(252, min_periods=63).min()
    base = (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdevz_252d_jerk_v079_signal(grossmargin):
    base = grossmargin - _mean(grossmargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmdevz_252d_jerk_v080_signal(netmargin):
    base = netmargin - _mean(netmargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emdevz_252d_jerk_v081_signal(ebitdamargin):
    base = ebitdamargin - _mean(ebitdamargin, 252)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdevz_252d_jerk_v082_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - _mean(om, 252)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_passthruz_252d_jerk_v083_signal(grossmargin, netmargin):
    base = netmargin / grossmargin.replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_egconvz_126d_jerk_v084_signal(ebitdamargin, grossmargin):
    base = ebitdamargin / grossmargin.replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omgmconvz_126d_jerk_v085_signal(opinc, revenue, grossmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om / grossmargin.replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmtroughz_252d_jerk_v086_signal(grossmargin):
    tr = grossmargin.rolling(252, min_periods=63).min()
    base = grossmargin / tr.replace(0, np.nan) - 1.0
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmpeakz_252d_jerk_v087_signal(netmargin):
    pk = netmargin.rolling(252, min_periods=63).max()
    base = netmargin / pk.replace(0, np.nan) - 1.0
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omrngz_252d_jerk_v088_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    hi = om.rolling(252, min_periods=63).max()
    lo = om.rolling(252, min_periods=63).min()
    base = (om - lo) / (hi - lo).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmtroughz_252d_jerk_v089_signal(netmargin):
    tr = netmargin.rolling(252, min_periods=63).min()
    base = netmargin / tr.replace(0, np.nan) - 1.0
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emhitz_252d_jerk_v090_signal(ebitdamargin):
    base = (ebitdamargin.diff() > 0).astype(float).rolling(252, min_periods=63).mean() - 0.5
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emcurvz_126d_jerk_v091_signal(ebitdamargin):
    base = (ebitdamargin - ebitdamargin.shift(63)) - (ebitdamargin.shift(63) - ebitdamargin.shift(126))
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emsmoothz_126d_jerk_v092_signal(ebitdamargin):
    base = ebitdamargin.ewm(span=42, min_periods=21).mean()
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdownvz_252d_jerk_v093_signal(grossmargin):
    d = grossmargin.diff()
    base = d.where(d < 0).rolling(252, min_periods=63).std()
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmudbalz_126d_jerk_v094_signal(netmargin):
    d = netmargin.diff()
    up = d.where(d > 0).rolling(126, min_periods=42).sum()
    dn = (-d.where(d < 0)).rolling(126, min_periods=42).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ompassz_126d_jerk_v095_signal(opinc, revenue, ebitdamargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - ebitdamargin
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmpeakz_252d_jerk_v096_signal(grossmargin):
    pk = grossmargin.rolling(252, min_periods=63).max()
    base = grossmargin / pk.replace(0, np.nan) - 1.0
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emtroughz_252d_jerk_v097_signal(ebitdamargin):
    tr = ebitdamargin.rolling(252, min_periods=63).min()
    base = ebitdamargin / tr.replace(0, np.nan) - 1.0
    base = _z(base, 252)
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmedz_252d_jerk_v098_signal(netmargin):
    base = netmargin - netmargin.rolling(252, min_periods=63).median()
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdispz_126d_jerk_v099_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=126, min_periods=63).mean()
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdriftz_252d_jerk_v100_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om.diff(21).rolling(252, min_periods=63).sum()
    base = _z(base, 252)
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmmeansm_126d_jerk_v101_signal(grossmargin):
    base = _mean(grossmargin, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmeansm_63d_jerk_v102_signal(netmargin):
    base = _mean(netmargin, 63)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emmeansm_126d_jerk_v103_signal(ebitdamargin):
    base = _mean(ebitdamargin, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ommeansm_63d_jerk_v104_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _mean(om, 63)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpmmeansm_63d_jerk_v105_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _mean(gm, 63)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmslsm_126d_jerk_v106_signal(grossmargin):
    base = _slope(grossmargin, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmslsm_126d_jerk_v107_signal(netmargin):
    base = _slope(netmargin, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emslsm_252d_jerk_v108_signal(ebitdamargin):
    base = _slope(ebitdamargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omslsm_126d_jerk_v109_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _slope(om, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gpslsm_126d_jerk_v110_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    base = _slope(gm, 126)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gnsprsm_63d_jerk_v111_signal(grossmargin, netmargin):
    base = grossmargin - netmargin
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gesprsm_126d_jerk_v112_signal(grossmargin, ebitdamargin):
    base = grossmargin - ebitdamargin
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ensprsm_126d_jerk_v113_signal(ebitdamargin, netmargin):
    base = ebitdamargin - netmargin
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omnmsprsm_126d_jerk_v114_signal(opinc, revenue, netmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - netmargin
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmzsm_252d_jerk_v115_signal(grossmargin):
    base = _z(grossmargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmzsm_252d_jerk_v116_signal(netmargin):
    base = _z(netmargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emzsm_252d_jerk_v117_signal(ebitdamargin):
    base = _z(ebitdamargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omzsm_252d_jerk_v118_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _z(om, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmstabsm_252d_jerk_v119_signal(grossmargin):
    base = _mean(grossmargin, 252).abs() / _std(grossmargin, 252).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmstabsm_126d_jerk_v120_signal(netmargin):
    base = _mean(netmargin, 126).abs() / _std(netmargin, 126).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emudbalsm_252d_jerk_v121_signal(ebitdamargin):
    d = ebitdamargin.diff()
    up = d.where(d > 0).rolling(252, min_periods=63).sum()
    dn = (-d.where(d < 0)).rolling(252, min_periods=63).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmemadsm_63d_jerk_v122_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=63, min_periods=21).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 5)
    d2 = _roc(d1, 5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmemadsm_63d_jerk_v123_signal(netmargin):
    base = netmargin - netmargin.ewm(span=63, min_periods=21).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ememadsm_126d_jerk_v124_signal(ebitdamargin):
    base = ebitdamargin - ebitdamargin.ewm(span=126, min_periods=42).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omemadsm_63d_jerk_v125_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - om.ewm(span=63, min_periods=21).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmrngsm_252d_jerk_v126_signal(grossmargin):
    hi = grossmargin.rolling(252, min_periods=63).max()
    lo = grossmargin.rolling(252, min_periods=63).min()
    base = (grossmargin - lo) / (hi - lo).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmrngsm_252d_jerk_v127_signal(netmargin):
    hi = netmargin.rolling(252, min_periods=63).max()
    lo = netmargin.rolling(252, min_periods=63).min()
    base = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emrngsm_252d_jerk_v128_signal(ebitdamargin):
    hi = ebitdamargin.rolling(252, min_periods=63).max()
    lo = ebitdamargin.rolling(252, min_periods=63).min()
    base = (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdevsm_252d_jerk_v129_signal(grossmargin):
    base = grossmargin - _mean(grossmargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmdevsm_252d_jerk_v130_signal(netmargin):
    base = netmargin - _mean(netmargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emdevsm_252d_jerk_v131_signal(ebitdamargin):
    base = ebitdamargin - _mean(ebitdamargin, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdevsm_252d_jerk_v132_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om - _mean(om, 252)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_passthrusm_252d_jerk_v133_signal(grossmargin, netmargin):
    base = netmargin / grossmargin.replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_egconvsm_126d_jerk_v134_signal(ebitdamargin, grossmargin):
    base = ebitdamargin / grossmargin.replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omgmconvsm_126d_jerk_v135_signal(opinc, revenue, grossmargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om / grossmargin.replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmtroughsm_252d_jerk_v136_signal(grossmargin):
    tr = grossmargin.rolling(252, min_periods=63).min()
    base = grossmargin / tr.replace(0, np.nan) - 1.0
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmpeaksm_252d_jerk_v137_signal(netmargin):
    pk = netmargin.rolling(252, min_periods=63).max()
    base = netmargin / pk.replace(0, np.nan) - 1.0
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omrngsm_252d_jerk_v138_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    hi = om.rolling(252, min_periods=63).max()
    lo = om.rolling(252, min_periods=63).min()
    base = (om - lo) / (hi - lo).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmtroughsm_252d_jerk_v139_signal(netmargin):
    tr = netmargin.rolling(252, min_periods=63).min()
    base = netmargin / tr.replace(0, np.nan) - 1.0
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emhitsm_252d_jerk_v140_signal(ebitdamargin):
    base = (ebitdamargin.diff() > 0).astype(float).rolling(252, min_periods=63).mean() - 0.5
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emcurvsm_126d_jerk_v141_signal(ebitdamargin):
    base = (ebitdamargin - ebitdamargin.shift(63)) - (ebitdamargin.shift(63) - ebitdamargin.shift(126))
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emsmoothsm_126d_jerk_v142_signal(ebitdamargin):
    base = ebitdamargin.ewm(span=42, min_periods=21).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdownvsm_252d_jerk_v143_signal(grossmargin):
    d = grossmargin.diff()
    base = d.where(d < 0).rolling(252, min_periods=63).std()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmudbalsm_126d_jerk_v144_signal(netmargin):
    d = netmargin.diff()
    up = d.where(d > 0).rolling(126, min_periods=42).sum()
    dn = (-d.where(d < 0)).rolling(126, min_periods=42).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_ompasssm_126d_jerk_v145_signal(opinc, revenue, ebitdamargin):
    om = opinc / revenue.replace(0, np.nan)
    base = om - ebitdamargin
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmpeaksm_252d_jerk_v146_signal(grossmargin):
    pk = grossmargin.rolling(252, min_periods=63).max()
    base = grossmargin / pk.replace(0, np.nan) - 1.0
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_emtroughsm_252d_jerk_v147_signal(ebitdamargin):
    tr = ebitdamargin.rolling(252, min_periods=63).min()
    base = ebitdamargin / tr.replace(0, np.nan) - 1.0
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 63)
    d2 = _roc(d1, 63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_nmmedsm_252d_jerk_v148_signal(netmargin):
    base = netmargin - netmargin.rolling(252, min_periods=63).median()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_gmdispsm_126d_jerk_v149_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=126, min_periods=63).mean()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f24mt_f24_margin_trajectory_omdriftsm_252d_jerk_v150_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = om.diff(21).rolling(252, min_periods=63).sum()
    base = base.rolling(63, min_periods=21).mean()
    d1 = _roc(base, 21)
    d2 = _roc(d1, 21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24mt_f24_margin_trajectory_gmmean_126d_jerk_v001_signal,
    f24mt_f24_margin_trajectory_nmmean_63d_jerk_v002_signal,
    f24mt_f24_margin_trajectory_emmean_126d_jerk_v003_signal,
    f24mt_f24_margin_trajectory_ommean_63d_jerk_v004_signal,
    f24mt_f24_margin_trajectory_gpmmean_63d_jerk_v005_signal,
    f24mt_f24_margin_trajectory_gmsl_126d_jerk_v006_signal,
    f24mt_f24_margin_trajectory_nmsl_126d_jerk_v007_signal,
    f24mt_f24_margin_trajectory_emsl_252d_jerk_v008_signal,
    f24mt_f24_margin_trajectory_omsl_126d_jerk_v009_signal,
    f24mt_f24_margin_trajectory_gpsl_126d_jerk_v010_signal,
    f24mt_f24_margin_trajectory_gnspr_63d_jerk_v011_signal,
    f24mt_f24_margin_trajectory_gespr_126d_jerk_v012_signal,
    f24mt_f24_margin_trajectory_enspr_126d_jerk_v013_signal,
    f24mt_f24_margin_trajectory_omnmspr_126d_jerk_v014_signal,
    f24mt_f24_margin_trajectory_gmz_252d_jerk_v015_signal,
    f24mt_f24_margin_trajectory_nmz_252d_jerk_v016_signal,
    f24mt_f24_margin_trajectory_emz_252d_jerk_v017_signal,
    f24mt_f24_margin_trajectory_omz_252d_jerk_v018_signal,
    f24mt_f24_margin_trajectory_gmstab_252d_jerk_v019_signal,
    f24mt_f24_margin_trajectory_nmstab_126d_jerk_v020_signal,
    f24mt_f24_margin_trajectory_emudbal_252d_jerk_v021_signal,
    f24mt_f24_margin_trajectory_gmemad_63d_jerk_v022_signal,
    f24mt_f24_margin_trajectory_nmemad_63d_jerk_v023_signal,
    f24mt_f24_margin_trajectory_ememad_126d_jerk_v024_signal,
    f24mt_f24_margin_trajectory_omemad_63d_jerk_v025_signal,
    f24mt_f24_margin_trajectory_gmrng_252d_jerk_v026_signal,
    f24mt_f24_margin_trajectory_nmrng_252d_jerk_v027_signal,
    f24mt_f24_margin_trajectory_emrng_252d_jerk_v028_signal,
    f24mt_f24_margin_trajectory_gmdev_252d_jerk_v029_signal,
    f24mt_f24_margin_trajectory_nmdev_252d_jerk_v030_signal,
    f24mt_f24_margin_trajectory_emdev_252d_jerk_v031_signal,
    f24mt_f24_margin_trajectory_omdev_252d_jerk_v032_signal,
    f24mt_f24_margin_trajectory_passthru_252d_jerk_v033_signal,
    f24mt_f24_margin_trajectory_egconv_126d_jerk_v034_signal,
    f24mt_f24_margin_trajectory_omgmconv_126d_jerk_v035_signal,
    f24mt_f24_margin_trajectory_gmtrough_252d_jerk_v036_signal,
    f24mt_f24_margin_trajectory_nmpeak_252d_jerk_v037_signal,
    f24mt_f24_margin_trajectory_omrng_252d_jerk_v038_signal,
    f24mt_f24_margin_trajectory_nmtrough_252d_jerk_v039_signal,
    f24mt_f24_margin_trajectory_emhit_252d_jerk_v040_signal,
    f24mt_f24_margin_trajectory_emcurv_126d_jerk_v041_signal,
    f24mt_f24_margin_trajectory_emsmooth_126d_jerk_v042_signal,
    f24mt_f24_margin_trajectory_gmdownv_252d_jerk_v043_signal,
    f24mt_f24_margin_trajectory_nmudbal_126d_jerk_v044_signal,
    f24mt_f24_margin_trajectory_ompass_126d_jerk_v045_signal,
    f24mt_f24_margin_trajectory_gmpeak_252d_jerk_v046_signal,
    f24mt_f24_margin_trajectory_emtrough_252d_jerk_v047_signal,
    f24mt_f24_margin_trajectory_nmmed_252d_jerk_v048_signal,
    f24mt_f24_margin_trajectory_gmdisp_126d_jerk_v049_signal,
    f24mt_f24_margin_trajectory_omdrift_252d_jerk_v050_signal,
    f24mt_f24_margin_trajectory_gmmeanz_126d_jerk_v051_signal,
    f24mt_f24_margin_trajectory_nmmeanz_63d_jerk_v052_signal,
    f24mt_f24_margin_trajectory_emmeanz_126d_jerk_v053_signal,
    f24mt_f24_margin_trajectory_ommeanz_63d_jerk_v054_signal,
    f24mt_f24_margin_trajectory_gpmmeanz_63d_jerk_v055_signal,
    f24mt_f24_margin_trajectory_gmslz_126d_jerk_v056_signal,
    f24mt_f24_margin_trajectory_nmslz_126d_jerk_v057_signal,
    f24mt_f24_margin_trajectory_emslz_252d_jerk_v058_signal,
    f24mt_f24_margin_trajectory_omslz_126d_jerk_v059_signal,
    f24mt_f24_margin_trajectory_gpslz_126d_jerk_v060_signal,
    f24mt_f24_margin_trajectory_gnsprz_63d_jerk_v061_signal,
    f24mt_f24_margin_trajectory_gesprz_126d_jerk_v062_signal,
    f24mt_f24_margin_trajectory_ensprz_126d_jerk_v063_signal,
    f24mt_f24_margin_trajectory_omnmsprz_126d_jerk_v064_signal,
    f24mt_f24_margin_trajectory_gmzz_252d_jerk_v065_signal,
    f24mt_f24_margin_trajectory_nmzz_252d_jerk_v066_signal,
    f24mt_f24_margin_trajectory_emzz_252d_jerk_v067_signal,
    f24mt_f24_margin_trajectory_omzz_252d_jerk_v068_signal,
    f24mt_f24_margin_trajectory_gmstabz_252d_jerk_v069_signal,
    f24mt_f24_margin_trajectory_nmstabz_126d_jerk_v070_signal,
    f24mt_f24_margin_trajectory_emudbalz_252d_jerk_v071_signal,
    f24mt_f24_margin_trajectory_gmemadz_63d_jerk_v072_signal,
    f24mt_f24_margin_trajectory_nmemadz_63d_jerk_v073_signal,
    f24mt_f24_margin_trajectory_ememadz_126d_jerk_v074_signal,
    f24mt_f24_margin_trajectory_omemadz_63d_jerk_v075_signal,
    f24mt_f24_margin_trajectory_gmrngz_252d_jerk_v076_signal,
    f24mt_f24_margin_trajectory_nmrngz_252d_jerk_v077_signal,
    f24mt_f24_margin_trajectory_emrngz_252d_jerk_v078_signal,
    f24mt_f24_margin_trajectory_gmdevz_252d_jerk_v079_signal,
    f24mt_f24_margin_trajectory_nmdevz_252d_jerk_v080_signal,
    f24mt_f24_margin_trajectory_emdevz_252d_jerk_v081_signal,
    f24mt_f24_margin_trajectory_omdevz_252d_jerk_v082_signal,
    f24mt_f24_margin_trajectory_passthruz_252d_jerk_v083_signal,
    f24mt_f24_margin_trajectory_egconvz_126d_jerk_v084_signal,
    f24mt_f24_margin_trajectory_omgmconvz_126d_jerk_v085_signal,
    f24mt_f24_margin_trajectory_gmtroughz_252d_jerk_v086_signal,
    f24mt_f24_margin_trajectory_nmpeakz_252d_jerk_v087_signal,
    f24mt_f24_margin_trajectory_omrngz_252d_jerk_v088_signal,
    f24mt_f24_margin_trajectory_nmtroughz_252d_jerk_v089_signal,
    f24mt_f24_margin_trajectory_emhitz_252d_jerk_v090_signal,
    f24mt_f24_margin_trajectory_emcurvz_126d_jerk_v091_signal,
    f24mt_f24_margin_trajectory_emsmoothz_126d_jerk_v092_signal,
    f24mt_f24_margin_trajectory_gmdownvz_252d_jerk_v093_signal,
    f24mt_f24_margin_trajectory_nmudbalz_126d_jerk_v094_signal,
    f24mt_f24_margin_trajectory_ompassz_126d_jerk_v095_signal,
    f24mt_f24_margin_trajectory_gmpeakz_252d_jerk_v096_signal,
    f24mt_f24_margin_trajectory_emtroughz_252d_jerk_v097_signal,
    f24mt_f24_margin_trajectory_nmmedz_252d_jerk_v098_signal,
    f24mt_f24_margin_trajectory_gmdispz_126d_jerk_v099_signal,
    f24mt_f24_margin_trajectory_omdriftz_252d_jerk_v100_signal,
    f24mt_f24_margin_trajectory_gmmeansm_126d_jerk_v101_signal,
    f24mt_f24_margin_trajectory_nmmeansm_63d_jerk_v102_signal,
    f24mt_f24_margin_trajectory_emmeansm_126d_jerk_v103_signal,
    f24mt_f24_margin_trajectory_ommeansm_63d_jerk_v104_signal,
    f24mt_f24_margin_trajectory_gpmmeansm_63d_jerk_v105_signal,
    f24mt_f24_margin_trajectory_gmslsm_126d_jerk_v106_signal,
    f24mt_f24_margin_trajectory_nmslsm_126d_jerk_v107_signal,
    f24mt_f24_margin_trajectory_emslsm_252d_jerk_v108_signal,
    f24mt_f24_margin_trajectory_omslsm_126d_jerk_v109_signal,
    f24mt_f24_margin_trajectory_gpslsm_126d_jerk_v110_signal,
    f24mt_f24_margin_trajectory_gnsprsm_63d_jerk_v111_signal,
    f24mt_f24_margin_trajectory_gesprsm_126d_jerk_v112_signal,
    f24mt_f24_margin_trajectory_ensprsm_126d_jerk_v113_signal,
    f24mt_f24_margin_trajectory_omnmsprsm_126d_jerk_v114_signal,
    f24mt_f24_margin_trajectory_gmzsm_252d_jerk_v115_signal,
    f24mt_f24_margin_trajectory_nmzsm_252d_jerk_v116_signal,
    f24mt_f24_margin_trajectory_emzsm_252d_jerk_v117_signal,
    f24mt_f24_margin_trajectory_omzsm_252d_jerk_v118_signal,
    f24mt_f24_margin_trajectory_gmstabsm_252d_jerk_v119_signal,
    f24mt_f24_margin_trajectory_nmstabsm_126d_jerk_v120_signal,
    f24mt_f24_margin_trajectory_emudbalsm_252d_jerk_v121_signal,
    f24mt_f24_margin_trajectory_gmemadsm_63d_jerk_v122_signal,
    f24mt_f24_margin_trajectory_nmemadsm_63d_jerk_v123_signal,
    f24mt_f24_margin_trajectory_ememadsm_126d_jerk_v124_signal,
    f24mt_f24_margin_trajectory_omemadsm_63d_jerk_v125_signal,
    f24mt_f24_margin_trajectory_gmrngsm_252d_jerk_v126_signal,
    f24mt_f24_margin_trajectory_nmrngsm_252d_jerk_v127_signal,
    f24mt_f24_margin_trajectory_emrngsm_252d_jerk_v128_signal,
    f24mt_f24_margin_trajectory_gmdevsm_252d_jerk_v129_signal,
    f24mt_f24_margin_trajectory_nmdevsm_252d_jerk_v130_signal,
    f24mt_f24_margin_trajectory_emdevsm_252d_jerk_v131_signal,
    f24mt_f24_margin_trajectory_omdevsm_252d_jerk_v132_signal,
    f24mt_f24_margin_trajectory_passthrusm_252d_jerk_v133_signal,
    f24mt_f24_margin_trajectory_egconvsm_126d_jerk_v134_signal,
    f24mt_f24_margin_trajectory_omgmconvsm_126d_jerk_v135_signal,
    f24mt_f24_margin_trajectory_gmtroughsm_252d_jerk_v136_signal,
    f24mt_f24_margin_trajectory_nmpeaksm_252d_jerk_v137_signal,
    f24mt_f24_margin_trajectory_omrngsm_252d_jerk_v138_signal,
    f24mt_f24_margin_trajectory_nmtroughsm_252d_jerk_v139_signal,
    f24mt_f24_margin_trajectory_emhitsm_252d_jerk_v140_signal,
    f24mt_f24_margin_trajectory_emcurvsm_126d_jerk_v141_signal,
    f24mt_f24_margin_trajectory_emsmoothsm_126d_jerk_v142_signal,
    f24mt_f24_margin_trajectory_gmdownvsm_252d_jerk_v143_signal,
    f24mt_f24_margin_trajectory_nmudbalsm_126d_jerk_v144_signal,
    f24mt_f24_margin_trajectory_ompasssm_126d_jerk_v145_signal,
    f24mt_f24_margin_trajectory_gmpeaksm_252d_jerk_v146_signal,
    f24mt_f24_margin_trajectory_emtroughsm_252d_jerk_v147_signal,
    f24mt_f24_margin_trajectory_nmmedsm_252d_jerk_v148_signal,
    f24mt_f24_margin_trajectory_gmdispsm_126d_jerk_v149_signal,
    f24mt_f24_margin_trajectory_omdriftsm_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_MARGIN_TRAJECTORY_REGISTRY_001_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(101, n, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    grossmargin = _fund(102, n, base=0.35, drift=0.005, vol=0.03).clip(0.02, 0.9).rename("grossmargin")
    netmargin = _fund(103, n, base=0.12, drift=0.004, vol=0.04).clip(-0.2, 0.6).rename("netmargin")
    ebitdamargin = _fund(104, n, base=0.20, drift=0.004, vol=0.035).clip(-0.1, 0.7).rename("ebitdamargin")
    opinc = _fund(105, n, base=1.5e8, drift=0.02, vol=0.05, allow_neg=True).rename("opinc")
    gp = (revenue * _fund(106, n, base=0.33, drift=0.005, vol=0.03).clip(0.02, 0.9)).rename("gp")

    cols = {
        "grossmargin": grossmargin, "netmargin": netmargin,
        "ebitdamargin": ebitdamargin, "opinc": opinc,
        "revenue": revenue, "gp": gp,
    }

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

    print("OK f24_margin_trajectory_3rd_derivatives_001_150_claude: %d features pass" % n_features)
