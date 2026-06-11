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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (options / warrant positioning) =====
def _f46_skew(a, b):
    return (a - b) / (a + b).replace(0, np.nan)


def _f46_share(part, whole):
    return part / whole.replace(0, np.nan)


def _f46_intensity(value, marketcap):
    return value / marketcap.replace(0, np.nan)


def _f46_per_holder(value, holders):
    return value / holders.replace(0, np.nan)


def _f46_accum(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ===== derivative operators =====
def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)



def f46ow_f46_options_warrant_positioning_putintens_z252_21d_slope_v001_signal(putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putintens_rank504_42d_slope_v002_signal(putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putintens_ema63_63d_slope_v003_signal(putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllintens_z252_21d_slope_v004_signal(cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllintens_rank504_42d_slope_v005_signal(cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllintens_ema63_63d_slope_v006_signal(cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntoverhang_z252_21d_slope_v007_signal(wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntoverhang_rank504_42d_slope_v008_signal(wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntoverhang_ema63_63d_slope_v009_signal(wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtoverhang_z252_21d_slope_v010_signal(dbtvalue, marketcap):
    base = _f46_intensity(dbtvalue, marketcap)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtoverhang_rank504_42d_slope_v011_signal(dbtvalue, marketcap):
    base = _f46_intensity(dbtvalue, marketcap)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtoverhang_ema63_63d_slope_v012_signal(dbtvalue, marketcap):
    base = _f46_intensity(dbtvalue, marketcap)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcvalskew_z252_21d_slope_v013_signal(putvalue, cllvalue):
    base = _f46_skew(putvalue, cllvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcvalskew_rank504_42d_slope_v014_signal(putvalue, cllvalue):
    base = _f46_skew(putvalue, cllvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcvalskew_ema63_63d_slope_v015_signal(putvalue, cllvalue):
    base = _f46_skew(putvalue, cllvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pchldskew_z252_21d_slope_v016_signal(putholders, cllholders):
    base = _f46_skew(putholders, cllholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pchldskew_rank504_42d_slope_v017_signal(putholders, cllholders):
    base = _f46_skew(putholders, cllholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pchldskew_ema63_63d_slope_v018_signal(putholders, cllholders):
    base = _f46_skew(putholders, cllholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntshare_z252_21d_slope_v019_signal(wntvalue, totalvalue):
    base = _f46_share(wntvalue, totalvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntshare_rank504_42d_slope_v020_signal(wntvalue, totalvalue):
    base = _f46_share(wntvalue, totalvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntshare_ema63_63d_slope_v021_signal(wntvalue, totalvalue):
    base = _f46_share(wntvalue, totalvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtshare_z252_21d_slope_v022_signal(dbtvalue, totalvalue):
    base = _f46_share(dbtvalue, totalvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtshare_rank504_42d_slope_v023_signal(dbtvalue, totalvalue):
    base = _f46_share(dbtvalue, totalvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtshare_ema63_63d_slope_v024_signal(dbtvalue, totalvalue):
    base = _f46_share(dbtvalue, totalvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putshare_z252_21d_slope_v025_signal(putvalue, totalvalue):
    base = _f46_share(putvalue, totalvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putshare_rank504_42d_slope_v026_signal(putvalue, totalvalue):
    base = _f46_share(putvalue, totalvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putshare_ema63_63d_slope_v027_signal(putvalue, totalvalue):
    base = _f46_share(putvalue, totalvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllshare_z252_21d_slope_v028_signal(cllvalue, totalvalue):
    base = _f46_share(cllvalue, totalvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllshare_rank504_42d_slope_v029_signal(cllvalue, totalvalue):
    base = _f46_share(cllvalue, totalvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllshare_ema63_63d_slope_v030_signal(cllvalue, totalvalue):
    base = _f46_share(cllvalue, totalvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putperhld_z252_21d_slope_v031_signal(putvalue, putholders):
    base = _f46_per_holder(putvalue, putholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putperhld_rank504_42d_slope_v032_signal(putvalue, putholders):
    base = _f46_per_holder(putvalue, putholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putperhld_ema63_63d_slope_v033_signal(putvalue, putholders):
    base = _f46_per_holder(putvalue, putholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllperhld_z252_21d_slope_v034_signal(cllvalue, cllholders):
    base = _f46_per_holder(cllvalue, cllholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllperhld_rank504_42d_slope_v035_signal(cllvalue, cllholders):
    base = _f46_per_holder(cllvalue, cllholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllperhld_ema63_63d_slope_v036_signal(cllvalue, cllholders):
    base = _f46_per_holder(cllvalue, cllholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntperhld_z252_21d_slope_v037_signal(wntvalue, wntholders):
    base = _f46_per_holder(wntvalue, wntholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntperhld_rank504_42d_slope_v038_signal(wntvalue, wntholders):
    base = _f46_per_holder(wntvalue, wntholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntperhld_ema63_63d_slope_v039_signal(wntvalue, wntholders):
    base = _f46_per_holder(wntvalue, wntholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtperhld_z252_21d_slope_v040_signal(dbtvalue, dbtholders):
    base = _f46_per_holder(dbtvalue, dbtholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtperhld_rank504_42d_slope_v041_signal(dbtvalue, dbtholders):
    base = _f46_per_holder(dbtvalue, dbtholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtperhld_ema63_63d_slope_v042_signal(dbtvalue, dbtholders):
    base = _f46_per_holder(dbtvalue, dbtholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optintens_z252_21d_slope_v043_signal(putvalue, cllvalue, marketcap):
    base = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optintens_rank504_42d_slope_v044_signal(putvalue, cllvalue, marketcap):
    base = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optintens_ema63_63d_slope_v045_signal(putvalue, cllvalue, marketcap):
    base = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivhhi_z252_21d_slope_v046_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    tot = (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base = (putvalue / tot) ** 2 + (cllvalue / tot) ** 2 + (wntvalue / tot) ** 2 + (dbtvalue / tot) ** 2
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivhhi_rank504_42d_slope_v047_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    tot = (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base = (putvalue / tot) ** 2 + (cllvalue / tot) ** 2 + (wntvalue / tot) ** 2 + (dbtvalue / tot) ** 2
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivhhi_ema63_63d_slope_v048_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    tot = (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base = (putvalue / tot) ** 2 + (cllvalue / tot) ** 2 + (wntvalue / tot) ** 2 + (dbtvalue / tot) ** 2
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putvsequity_z252_21d_slope_v049_signal(putvalue, shrvalue):
    base = _f46_share(putvalue, shrvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putvsequity_rank504_42d_slope_v050_signal(putvalue, shrvalue):
    base = _f46_share(putvalue, shrvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putvsequity_ema63_63d_slope_v051_signal(putvalue, shrvalue):
    base = _f46_share(putvalue, shrvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllvsequity_z252_21d_slope_v052_signal(cllvalue, shrvalue):
    base = _f46_share(cllvalue, shrvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllvsequity_rank504_42d_slope_v053_signal(cllvalue, shrvalue):
    base = _f46_share(cllvalue, shrvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllvsequity_ema63_63d_slope_v054_signal(cllvalue, shrvalue):
    base = _f46_share(cllvalue, shrvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntvsequity_z252_21d_slope_v055_signal(wntvalue, shrvalue):
    base = _f46_share(wntvalue, shrvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntvsequity_rank504_42d_slope_v056_signal(wntvalue, shrvalue):
    base = _f46_share(wntvalue, shrvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntvsequity_ema63_63d_slope_v057_signal(wntvalue, shrvalue):
    base = _f46_share(wntvalue, shrvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_totalfootprint_z252_21d_slope_v058_signal(totalvalue, marketcap):
    base = _f46_intensity(totalvalue, marketcap)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_totalfootprint_rank504_42d_slope_v059_signal(totalvalue, marketcap):
    base = _f46_intensity(totalvalue, marketcap)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_totalfootprint_ema63_63d_slope_v060_signal(totalvalue, marketcap):
    base = _f46_intensity(totalvalue, marketcap)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_equityshare_z252_21d_slope_v061_signal(shrvalue, totalvalue):
    base = _f46_share(shrvalue, totalvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_equityshare_rank504_42d_slope_v062_signal(shrvalue, totalvalue):
    base = _f46_share(shrvalue, totalvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_equityshare_ema63_63d_slope_v063_signal(shrvalue, totalvalue):
    base = _f46_share(shrvalue, totalvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pctoftotal_z252_21d_slope_v064_signal(percentoftotal):
    base = percentoftotal
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pctoftotal_rank504_42d_slope_v065_signal(percentoftotal):
    base = percentoftotal
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pctoftotal_ema63_63d_slope_v066_signal(percentoftotal):
    base = percentoftotal
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivbreadth_z252_21d_slope_v067_signal(putholders, cllholders, wntholders, dbtholders):
    base = putholders + cllholders + wntholders + dbtholders
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivbreadth_rank504_42d_slope_v068_signal(putholders, cllholders, wntholders, dbtholders):
    base = putholders + cllholders + wntholders + dbtholders
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivbreadth_ema63_63d_slope_v069_signal(putholders, cllholders, wntholders, dbtholders):
    base = putholders + cllholders + wntholders + dbtholders
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optstructshare_z252_21d_slope_v070_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    base = (putvalue + cllvalue) / (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optstructshare_rank504_42d_slope_v071_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    base = (putvalue + cllvalue) / (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optstructshare_ema63_63d_slope_v072_signal(putvalue, cllvalue, wntvalue, dbtvalue):
    base = (putvalue + cllvalue) / (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbthldperval_z252_21d_slope_v073_signal(dbtholders, totalvalue):
    base = dbtholders / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbthldperval_rank504_42d_slope_v074_signal(dbtholders, totalvalue):
    base = dbtholders / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbthldperval_ema63_63d_slope_v075_signal(dbtholders, totalvalue):
    base = dbtholders / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_overhangcomp_z252_21d_slope_v076_signal(wntvalue, dbtvalue, shrvalue):
    base = (wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_overhangcomp_rank504_42d_slope_v077_signal(wntvalue, dbtvalue, shrvalue):
    base = (wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_overhangcomp_ema63_63d_slope_v078_signal(wntvalue, dbtvalue, shrvalue):
    base = (wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntcv_z252_21d_slope_v079_signal(wntvalue):
    base = _std(wntvalue, 126) / _mean(wntvalue, 126).replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntcv_rank504_42d_slope_v080_signal(wntvalue):
    base = _std(wntvalue, 126) / _mean(wntvalue, 126).replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wntcv_ema63_63d_slope_v081_signal(wntvalue):
    base = _std(wntvalue, 126) / _mean(wntvalue, 126).replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hedgedilskew_z252_21d_slope_v082_signal(putvalue, wntvalue):
    base = _f46_skew(putvalue, wntvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hedgedilskew_rank504_42d_slope_v083_signal(putvalue, wntvalue):
    base = _f46_skew(putvalue, wntvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hedgedilskew_ema63_63d_slope_v084_signal(putvalue, wntvalue):
    base = _f46_skew(putvalue, wntvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_specdilskew_z252_21d_slope_v085_signal(cllvalue, wntvalue):
    base = _f46_skew(cllvalue, wntvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_specdilskew_rank504_42d_slope_v086_signal(cllvalue, wntvalue):
    base = _f46_skew(cllvalue, wntvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_specdilskew_ema63_63d_slope_v087_signal(cllvalue, wntvalue):
    base = _f46_skew(cllvalue, wntvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtwntskew_z252_21d_slope_v088_signal(dbtvalue, wntvalue):
    base = _f46_skew(dbtvalue, wntvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtwntskew_rank504_42d_slope_v089_signal(dbtvalue, wntvalue):
    base = _f46_skew(dbtvalue, wntvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_dbtwntskew_ema63_63d_slope_v090_signal(dbtvalue, wntvalue):
    base = _f46_skew(dbtvalue, wntvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthldshare_z252_21d_slope_v091_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = putholders / deriv
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthldshare_rank504_42d_slope_v092_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = putholders / deriv
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthldshare_ema63_63d_slope_v093_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = putholders / deriv
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhldshare_z252_21d_slope_v094_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = cllholders / deriv
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhldshare_rank504_42d_slope_v095_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = cllholders / deriv
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhldshare_ema63_63d_slope_v096_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = cllholders / deriv
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldshare_z252_21d_slope_v097_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = wntholders / deriv
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldshare_rank504_42d_slope_v098_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = wntholders / deriv
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldshare_ema63_63d_slope_v099_signal(putholders, cllholders, wntholders, dbtholders):
    deriv = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = wntholders / deriv
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcconvskew_z252_21d_slope_v100_signal(putvalue, putholders, cllvalue, cllholders):
    base = _f46_skew(_f46_per_holder(putvalue, putholders), _f46_per_holder(cllvalue, cllholders))
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcconvskew_rank504_42d_slope_v101_signal(putvalue, putholders, cllvalue, cllholders):
    base = _f46_skew(_f46_per_holder(putvalue, putholders), _f46_per_holder(cllvalue, cllholders))
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcconvskew_ema63_63d_slope_v102_signal(putvalue, putholders, cllvalue, cllholders):
    base = _f46_skew(_f46_per_holder(putvalue, putholders), _f46_per_holder(cllvalue, cllholders))
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivvalshare_z252_21d_slope_v103_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivvalshare_rank504_42d_slope_v104_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_derivvalshare_ema63_63d_slope_v105_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_fullclaim_z252_21d_slope_v106_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_fullclaim_rank504_42d_slope_v107_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_fullclaim_ema63_63d_slope_v108_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimfootprint_z252_21d_slope_v109_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimfootprint_rank504_42d_slope_v110_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimfootprint_ema63_63d_slope_v111_signal(putvalue, cllvalue, wntvalue, dbtvalue, marketcap):
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optequityskew_z252_21d_slope_v112_signal(putvalue, cllvalue, shrvalue):
    base = _f46_skew(putvalue + cllvalue, shrvalue)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optequityskew_rank504_42d_slope_v113_signal(putvalue, cllvalue, shrvalue):
    base = _f46_skew(putvalue + cllvalue, shrvalue)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_optequityskew_ema63_63d_slope_v114_signal(putvalue, cllvalue, shrvalue):
    base = _f46_skew(putvalue + cllvalue, shrvalue)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcholdprod_z252_21d_slope_v115_signal(putholders, cllholders, totalvalue):
    base = np.sqrt((putholders * cllholders).clip(lower=0)) / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcholdprod_rank504_42d_slope_v116_signal(putholders, cllholders, totalvalue):
    base = np.sqrt((putholders * cllholders).clip(lower=0)) / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_pcholdprod_ema63_63d_slope_v117_signal(putholders, cllholders, totalvalue):
    base = np.sqrt((putholders * cllholders).clip(lower=0)) / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldperval_z252_21d_slope_v118_signal(wntholders, totalvalue):
    base = wntholders / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldperval_rank504_42d_slope_v119_signal(wntholders, totalvalue):
    base = wntholders / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_wnthldperval_ema63_63d_slope_v120_signal(wntholders, totalvalue):
    base = wntholders / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putcv_z252_21d_slope_v121_signal(putvalue):
    base = _std(putvalue, 126) / _mean(putvalue, 126).replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putcv_rank504_42d_slope_v122_signal(putvalue):
    base = _std(putvalue, 126) / _mean(putvalue, 126).replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_putcv_ema63_63d_slope_v123_signal(putvalue):
    base = _std(putvalue, 126) / _mean(putvalue, 126).replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllcv_z252_21d_slope_v124_signal(cllvalue):
    base = _std(cllvalue, 126) / _mean(cllvalue, 126).replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllcv_rank504_42d_slope_v125_signal(cllvalue):
    base = _std(cllvalue, 126) / _mean(cllvalue, 126).replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllcv_ema63_63d_slope_v126_signal(cllvalue):
    base = _std(cllvalue, 126) / _mean(cllvalue, 126).replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covhedge_z252_21d_slope_v127_signal(percentoftotal, putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap) * percentoftotal
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covhedge_rank504_42d_slope_v128_signal(percentoftotal, putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap) * percentoftotal
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covhedge_ema63_63d_slope_v129_signal(percentoftotal, putvalue, marketcap):
    base = _f46_intensity(putvalue, marketcap) * percentoftotal
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covspec_z252_21d_slope_v130_signal(percentoftotal, cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap) * percentoftotal
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covspec_rank504_42d_slope_v131_signal(percentoftotal, cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap) * percentoftotal
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covspec_ema63_63d_slope_v132_signal(percentoftotal, cllvalue, marketcap):
    base = _f46_intensity(cllvalue, marketcap) * percentoftotal
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covdilrisk_z252_21d_slope_v133_signal(percentoftotal, wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap) * percentoftotal
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covdilrisk_rank504_42d_slope_v134_signal(percentoftotal, wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap) * percentoftotal
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_covdilrisk_ema63_63d_slope_v135_signal(percentoftotal, wntvalue, marketcap):
    base = _f46_intensity(wntvalue, marketcap) * percentoftotal
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthlddens_z252_21d_slope_v136_signal(putholders, totalvalue):
    base = putholders / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthlddens_rank504_42d_slope_v137_signal(putholders, totalvalue):
    base = putholders / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_puthlddens_ema63_63d_slope_v138_signal(putholders, totalvalue):
    base = putholders / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhlddens_z252_21d_slope_v139_signal(cllholders, totalvalue):
    base = cllholders / totalvalue.replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhlddens_rank504_42d_slope_v140_signal(cllholders, totalvalue):
    base = cllholders / totalvalue.replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_cllhlddens_ema63_63d_slope_v141_signal(cllholders, totalvalue):
    base = cllholders / totalvalue.replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimperhld_z252_21d_slope_v142_signal(putvalue, cllvalue, wntvalue, dbtvalue, putholders, cllholders, wntholders, dbtholders):
    hld = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / hld
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimperhld_rank504_42d_slope_v143_signal(putvalue, cllvalue, wntvalue, dbtvalue, putholders, cllholders, wntholders, dbtholders):
    hld = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / hld
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_claimperhld_ema63_63d_slope_v144_signal(putvalue, cllvalue, wntvalue, dbtvalue, putholders, cllholders, wntholders, dbtholders):
    hld = (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    base = (putvalue + cllvalue + wntvalue + dbtvalue) / hld
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hldbreadthdisp_z252_21d_slope_v145_signal(putholders, cllholders, wntholders, dbtholders):
    stk = pd.concat([putholders, cllholders, wntholders, dbtholders], axis=1)
    base = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hldbreadthdisp_rank504_42d_slope_v146_signal(putholders, cllholders, wntholders, dbtholders):
    stk = pd.concat([putholders, cllholders, wntholders, dbtholders], axis=1)
    base = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_hldbreadthdisp_ema63_63d_slope_v147_signal(putholders, cllholders, wntholders, dbtholders):
    stk = pd.concat([putholders, cllholders, wntholders, dbtholders], axis=1)
    base = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_structhldskew_z252_21d_slope_v148_signal(wntholders, dbtholders):
    base = _f46_skew(wntholders, dbtholders)
    base2 = _z(base, 252)
    d = _slope(base2, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_structhldskew_rank504_42d_slope_v149_signal(wntholders, dbtholders):
    base = _f46_skew(wntholders, dbtholders)
    base2 = _rank(base, 504)
    d = _slope(base2, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f46ow_f46_options_warrant_positioning_structhldskew_ema63_63d_slope_v150_signal(wntholders, dbtholders):
    base = _f46_skew(wntholders, dbtholders)
    base2 = base.ewm(span=63, min_periods=21).mean()
    d = _slope(base2, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_putintens_z252_21d_slope_v001_signal,
    f46ow_f46_options_warrant_positioning_putintens_rank504_42d_slope_v002_signal,
    f46ow_f46_options_warrant_positioning_putintens_ema63_63d_slope_v003_signal,
    f46ow_f46_options_warrant_positioning_cllintens_z252_21d_slope_v004_signal,
    f46ow_f46_options_warrant_positioning_cllintens_rank504_42d_slope_v005_signal,
    f46ow_f46_options_warrant_positioning_cllintens_ema63_63d_slope_v006_signal,
    f46ow_f46_options_warrant_positioning_wntoverhang_z252_21d_slope_v007_signal,
    f46ow_f46_options_warrant_positioning_wntoverhang_rank504_42d_slope_v008_signal,
    f46ow_f46_options_warrant_positioning_wntoverhang_ema63_63d_slope_v009_signal,
    f46ow_f46_options_warrant_positioning_dbtoverhang_z252_21d_slope_v010_signal,
    f46ow_f46_options_warrant_positioning_dbtoverhang_rank504_42d_slope_v011_signal,
    f46ow_f46_options_warrant_positioning_dbtoverhang_ema63_63d_slope_v012_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_z252_21d_slope_v013_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_rank504_42d_slope_v014_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_ema63_63d_slope_v015_signal,
    f46ow_f46_options_warrant_positioning_pchldskew_z252_21d_slope_v016_signal,
    f46ow_f46_options_warrant_positioning_pchldskew_rank504_42d_slope_v017_signal,
    f46ow_f46_options_warrant_positioning_pchldskew_ema63_63d_slope_v018_signal,
    f46ow_f46_options_warrant_positioning_wntshare_z252_21d_slope_v019_signal,
    f46ow_f46_options_warrant_positioning_wntshare_rank504_42d_slope_v020_signal,
    f46ow_f46_options_warrant_positioning_wntshare_ema63_63d_slope_v021_signal,
    f46ow_f46_options_warrant_positioning_dbtshare_z252_21d_slope_v022_signal,
    f46ow_f46_options_warrant_positioning_dbtshare_rank504_42d_slope_v023_signal,
    f46ow_f46_options_warrant_positioning_dbtshare_ema63_63d_slope_v024_signal,
    f46ow_f46_options_warrant_positioning_putshare_z252_21d_slope_v025_signal,
    f46ow_f46_options_warrant_positioning_putshare_rank504_42d_slope_v026_signal,
    f46ow_f46_options_warrant_positioning_putshare_ema63_63d_slope_v027_signal,
    f46ow_f46_options_warrant_positioning_cllshare_z252_21d_slope_v028_signal,
    f46ow_f46_options_warrant_positioning_cllshare_rank504_42d_slope_v029_signal,
    f46ow_f46_options_warrant_positioning_cllshare_ema63_63d_slope_v030_signal,
    f46ow_f46_options_warrant_positioning_putperhld_z252_21d_slope_v031_signal,
    f46ow_f46_options_warrant_positioning_putperhld_rank504_42d_slope_v032_signal,
    f46ow_f46_options_warrant_positioning_putperhld_ema63_63d_slope_v033_signal,
    f46ow_f46_options_warrant_positioning_cllperhld_z252_21d_slope_v034_signal,
    f46ow_f46_options_warrant_positioning_cllperhld_rank504_42d_slope_v035_signal,
    f46ow_f46_options_warrant_positioning_cllperhld_ema63_63d_slope_v036_signal,
    f46ow_f46_options_warrant_positioning_wntperhld_z252_21d_slope_v037_signal,
    f46ow_f46_options_warrant_positioning_wntperhld_rank504_42d_slope_v038_signal,
    f46ow_f46_options_warrant_positioning_wntperhld_ema63_63d_slope_v039_signal,
    f46ow_f46_options_warrant_positioning_dbtperhld_z252_21d_slope_v040_signal,
    f46ow_f46_options_warrant_positioning_dbtperhld_rank504_42d_slope_v041_signal,
    f46ow_f46_options_warrant_positioning_dbtperhld_ema63_63d_slope_v042_signal,
    f46ow_f46_options_warrant_positioning_optintens_z252_21d_slope_v043_signal,
    f46ow_f46_options_warrant_positioning_optintens_rank504_42d_slope_v044_signal,
    f46ow_f46_options_warrant_positioning_optintens_ema63_63d_slope_v045_signal,
    f46ow_f46_options_warrant_positioning_derivhhi_z252_21d_slope_v046_signal,
    f46ow_f46_options_warrant_positioning_derivhhi_rank504_42d_slope_v047_signal,
    f46ow_f46_options_warrant_positioning_derivhhi_ema63_63d_slope_v048_signal,
    f46ow_f46_options_warrant_positioning_putvsequity_z252_21d_slope_v049_signal,
    f46ow_f46_options_warrant_positioning_putvsequity_rank504_42d_slope_v050_signal,
    f46ow_f46_options_warrant_positioning_putvsequity_ema63_63d_slope_v051_signal,
    f46ow_f46_options_warrant_positioning_cllvsequity_z252_21d_slope_v052_signal,
    f46ow_f46_options_warrant_positioning_cllvsequity_rank504_42d_slope_v053_signal,
    f46ow_f46_options_warrant_positioning_cllvsequity_ema63_63d_slope_v054_signal,
    f46ow_f46_options_warrant_positioning_wntvsequity_z252_21d_slope_v055_signal,
    f46ow_f46_options_warrant_positioning_wntvsequity_rank504_42d_slope_v056_signal,
    f46ow_f46_options_warrant_positioning_wntvsequity_ema63_63d_slope_v057_signal,
    f46ow_f46_options_warrant_positioning_totalfootprint_z252_21d_slope_v058_signal,
    f46ow_f46_options_warrant_positioning_totalfootprint_rank504_42d_slope_v059_signal,
    f46ow_f46_options_warrant_positioning_totalfootprint_ema63_63d_slope_v060_signal,
    f46ow_f46_options_warrant_positioning_equityshare_z252_21d_slope_v061_signal,
    f46ow_f46_options_warrant_positioning_equityshare_rank504_42d_slope_v062_signal,
    f46ow_f46_options_warrant_positioning_equityshare_ema63_63d_slope_v063_signal,
    f46ow_f46_options_warrant_positioning_pctoftotal_z252_21d_slope_v064_signal,
    f46ow_f46_options_warrant_positioning_pctoftotal_rank504_42d_slope_v065_signal,
    f46ow_f46_options_warrant_positioning_pctoftotal_ema63_63d_slope_v066_signal,
    f46ow_f46_options_warrant_positioning_derivbreadth_z252_21d_slope_v067_signal,
    f46ow_f46_options_warrant_positioning_derivbreadth_rank504_42d_slope_v068_signal,
    f46ow_f46_options_warrant_positioning_derivbreadth_ema63_63d_slope_v069_signal,
    f46ow_f46_options_warrant_positioning_optstructshare_z252_21d_slope_v070_signal,
    f46ow_f46_options_warrant_positioning_optstructshare_rank504_42d_slope_v071_signal,
    f46ow_f46_options_warrant_positioning_optstructshare_ema63_63d_slope_v072_signal,
    f46ow_f46_options_warrant_positioning_dbthldperval_z252_21d_slope_v073_signal,
    f46ow_f46_options_warrant_positioning_dbthldperval_rank504_42d_slope_v074_signal,
    f46ow_f46_options_warrant_positioning_dbthldperval_ema63_63d_slope_v075_signal,
    f46ow_f46_options_warrant_positioning_overhangcomp_z252_21d_slope_v076_signal,
    f46ow_f46_options_warrant_positioning_overhangcomp_rank504_42d_slope_v077_signal,
    f46ow_f46_options_warrant_positioning_overhangcomp_ema63_63d_slope_v078_signal,
    f46ow_f46_options_warrant_positioning_wntcv_z252_21d_slope_v079_signal,
    f46ow_f46_options_warrant_positioning_wntcv_rank504_42d_slope_v080_signal,
    f46ow_f46_options_warrant_positioning_wntcv_ema63_63d_slope_v081_signal,
    f46ow_f46_options_warrant_positioning_hedgedilskew_z252_21d_slope_v082_signal,
    f46ow_f46_options_warrant_positioning_hedgedilskew_rank504_42d_slope_v083_signal,
    f46ow_f46_options_warrant_positioning_hedgedilskew_ema63_63d_slope_v084_signal,
    f46ow_f46_options_warrant_positioning_specdilskew_z252_21d_slope_v085_signal,
    f46ow_f46_options_warrant_positioning_specdilskew_rank504_42d_slope_v086_signal,
    f46ow_f46_options_warrant_positioning_specdilskew_ema63_63d_slope_v087_signal,
    f46ow_f46_options_warrant_positioning_dbtwntskew_z252_21d_slope_v088_signal,
    f46ow_f46_options_warrant_positioning_dbtwntskew_rank504_42d_slope_v089_signal,
    f46ow_f46_options_warrant_positioning_dbtwntskew_ema63_63d_slope_v090_signal,
    f46ow_f46_options_warrant_positioning_puthldshare_z252_21d_slope_v091_signal,
    f46ow_f46_options_warrant_positioning_puthldshare_rank504_42d_slope_v092_signal,
    f46ow_f46_options_warrant_positioning_puthldshare_ema63_63d_slope_v093_signal,
    f46ow_f46_options_warrant_positioning_cllhldshare_z252_21d_slope_v094_signal,
    f46ow_f46_options_warrant_positioning_cllhldshare_rank504_42d_slope_v095_signal,
    f46ow_f46_options_warrant_positioning_cllhldshare_ema63_63d_slope_v096_signal,
    f46ow_f46_options_warrant_positioning_wnthldshare_z252_21d_slope_v097_signal,
    f46ow_f46_options_warrant_positioning_wnthldshare_rank504_42d_slope_v098_signal,
    f46ow_f46_options_warrant_positioning_wnthldshare_ema63_63d_slope_v099_signal,
    f46ow_f46_options_warrant_positioning_pcconvskew_z252_21d_slope_v100_signal,
    f46ow_f46_options_warrant_positioning_pcconvskew_rank504_42d_slope_v101_signal,
    f46ow_f46_options_warrant_positioning_pcconvskew_ema63_63d_slope_v102_signal,
    f46ow_f46_options_warrant_positioning_derivvalshare_z252_21d_slope_v103_signal,
    f46ow_f46_options_warrant_positioning_derivvalshare_rank504_42d_slope_v104_signal,
    f46ow_f46_options_warrant_positioning_derivvalshare_ema63_63d_slope_v105_signal,
    f46ow_f46_options_warrant_positioning_fullclaim_z252_21d_slope_v106_signal,
    f46ow_f46_options_warrant_positioning_fullclaim_rank504_42d_slope_v107_signal,
    f46ow_f46_options_warrant_positioning_fullclaim_ema63_63d_slope_v108_signal,
    f46ow_f46_options_warrant_positioning_claimfootprint_z252_21d_slope_v109_signal,
    f46ow_f46_options_warrant_positioning_claimfootprint_rank504_42d_slope_v110_signal,
    f46ow_f46_options_warrant_positioning_claimfootprint_ema63_63d_slope_v111_signal,
    f46ow_f46_options_warrant_positioning_optequityskew_z252_21d_slope_v112_signal,
    f46ow_f46_options_warrant_positioning_optequityskew_rank504_42d_slope_v113_signal,
    f46ow_f46_options_warrant_positioning_optequityskew_ema63_63d_slope_v114_signal,
    f46ow_f46_options_warrant_positioning_pcholdprod_z252_21d_slope_v115_signal,
    f46ow_f46_options_warrant_positioning_pcholdprod_rank504_42d_slope_v116_signal,
    f46ow_f46_options_warrant_positioning_pcholdprod_ema63_63d_slope_v117_signal,
    f46ow_f46_options_warrant_positioning_wnthldperval_z252_21d_slope_v118_signal,
    f46ow_f46_options_warrant_positioning_wnthldperval_rank504_42d_slope_v119_signal,
    f46ow_f46_options_warrant_positioning_wnthldperval_ema63_63d_slope_v120_signal,
    f46ow_f46_options_warrant_positioning_putcv_z252_21d_slope_v121_signal,
    f46ow_f46_options_warrant_positioning_putcv_rank504_42d_slope_v122_signal,
    f46ow_f46_options_warrant_positioning_putcv_ema63_63d_slope_v123_signal,
    f46ow_f46_options_warrant_positioning_cllcv_z252_21d_slope_v124_signal,
    f46ow_f46_options_warrant_positioning_cllcv_rank504_42d_slope_v125_signal,
    f46ow_f46_options_warrant_positioning_cllcv_ema63_63d_slope_v126_signal,
    f46ow_f46_options_warrant_positioning_covhedge_z252_21d_slope_v127_signal,
    f46ow_f46_options_warrant_positioning_covhedge_rank504_42d_slope_v128_signal,
    f46ow_f46_options_warrant_positioning_covhedge_ema63_63d_slope_v129_signal,
    f46ow_f46_options_warrant_positioning_covspec_z252_21d_slope_v130_signal,
    f46ow_f46_options_warrant_positioning_covspec_rank504_42d_slope_v131_signal,
    f46ow_f46_options_warrant_positioning_covspec_ema63_63d_slope_v132_signal,
    f46ow_f46_options_warrant_positioning_covdilrisk_z252_21d_slope_v133_signal,
    f46ow_f46_options_warrant_positioning_covdilrisk_rank504_42d_slope_v134_signal,
    f46ow_f46_options_warrant_positioning_covdilrisk_ema63_63d_slope_v135_signal,
    f46ow_f46_options_warrant_positioning_puthlddens_z252_21d_slope_v136_signal,
    f46ow_f46_options_warrant_positioning_puthlddens_rank504_42d_slope_v137_signal,
    f46ow_f46_options_warrant_positioning_puthlddens_ema63_63d_slope_v138_signal,
    f46ow_f46_options_warrant_positioning_cllhlddens_z252_21d_slope_v139_signal,
    f46ow_f46_options_warrant_positioning_cllhlddens_rank504_42d_slope_v140_signal,
    f46ow_f46_options_warrant_positioning_cllhlddens_ema63_63d_slope_v141_signal,
    f46ow_f46_options_warrant_positioning_claimperhld_z252_21d_slope_v142_signal,
    f46ow_f46_options_warrant_positioning_claimperhld_rank504_42d_slope_v143_signal,
    f46ow_f46_options_warrant_positioning_claimperhld_ema63_63d_slope_v144_signal,
    f46ow_f46_options_warrant_positioning_hldbreadthdisp_z252_21d_slope_v145_signal,
    f46ow_f46_options_warrant_positioning_hldbreadthdisp_rank504_42d_slope_v146_signal,
    f46ow_f46_options_warrant_positioning_hldbreadthdisp_ema63_63d_slope_v147_signal,
    f46ow_f46_options_warrant_positioning_structhldskew_z252_21d_slope_v148_signal,
    f46ow_f46_options_warrant_positioning_structhldskew_rank504_42d_slope_v149_signal,
    f46ow_f46_options_warrant_positioning_structhldskew_ema63_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_001_150 = REGISTRY


ALLOW = {
    "putholders", "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
    "dbtholders", "dbtvalue", "totalvalue", "shrvalue", "percentoftotal", "marketcap",
}


def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.6
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    putholders = _fund(101, base=120.0, drift=0.02, vol=0.06).rename("putholders")
    putvalue = _fund(102, base=4.0e7, drift=0.025, vol=0.09).rename("putvalue")
    cllholders = _fund(103, base=140.0, drift=0.02, vol=0.06).rename("cllholders")
    cllvalue = _fund(104, base=5.0e7, drift=0.03, vol=0.09).rename("cllvalue")
    wntholders = _fund(105, base=40.0, drift=0.015, vol=0.07).rename("wntholders")
    wntvalue = _fund(106, base=2.0e7, drift=0.02, vol=0.10).rename("wntvalue")
    dbtholders = _fund(107, base=55.0, drift=0.015, vol=0.06).rename("dbtholders")
    dbtvalue = _fund(108, base=3.0e7, drift=0.02, vol=0.08).rename("dbtvalue")
    totalvalue = _fund(109, base=6.0e8, drift=0.03, vol=0.05).rename("totalvalue")
    shrvalue = _fund(110, base=4.5e8, drift=0.03, vol=0.05).rename("shrvalue")
    marketcap = _fund(111, base=1.0e9, drift=0.025, vol=0.06).rename("marketcap")
    percentoftotal = (_fund(112, base=0.4, drift=0.005, vol=0.04).clip(0.01, 0.99)).rename("percentoftotal")

    cols = {
        "putholders": putholders, "putvalue": putvalue, "cllholders": cllholders,
        "cllvalue": cllvalue, "wntholders": wntholders, "wntvalue": wntvalue,
        "dbtholders": dbtholders, "dbtvalue": dbtvalue, "totalvalue": totalvalue,
        "shrvalue": shrvalue, "percentoftotal": percentoftotal, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset" % (name, meta["inputs"])
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

    print("OK f46_options_warrant_positioning_2nd_derivatives_001_150_claude: %d features pass" % n_features)