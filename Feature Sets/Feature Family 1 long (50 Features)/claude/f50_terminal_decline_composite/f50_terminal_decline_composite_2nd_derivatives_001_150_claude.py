import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w)


# ===== folder domain primitives =====
def _f50_terminal_decline(revenue, opinc, marketcap, w):
    rev_decline = -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    margin = opinc / revenue.replace(0, np.nan)
    margin_compression = -margin.diff(w)
    val_collapse = -marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return rev_decline + margin_compression + val_collapse


def _f50_revdecline(revenue, w):
    return -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)


def _f50_margincompress(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return -margin.diff(w)


# 5d slope of 21d decline × marketcap
def f50tdc_f50_terminal_decline_composite_decline_21d_slope_v001_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d decline
def f50tdc_f50_terminal_decline_composite_decline_21d_slope_v002_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d decline
def f50tdc_f50_terminal_decline_composite_decline_63d_slope_v003_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d decline
def f50tdc_f50_terminal_decline_composite_decline_63d_slope_v004_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d decline
def f50tdc_f50_terminal_decline_composite_decline_63d_slope_v005_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d decline
def f50tdc_f50_terminal_decline_composite_decline_126d_slope_v006_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 126) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d decline
def f50tdc_f50_terminal_decline_composite_decline_126d_slope_v007_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d decline
def f50tdc_f50_terminal_decline_composite_decline_252d_slope_v008_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d decline
def f50tdc_f50_terminal_decline_composite_decline_252d_slope_v009_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d decline
def f50tdc_f50_terminal_decline_composite_decline_504d_slope_v010_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d decline
def f50tdc_f50_terminal_decline_composite_decline_504d_slope_v011_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d decline
def f50tdc_f50_terminal_decline_composite_decline_504d_slope_v012_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline mean 21d
def f50tdc_f50_terminal_decline_composite_declinemean_21d_slope_v013_signal(revenue, opinc, marketcap):
    base = _mean(_f50_terminal_decline(revenue, opinc, marketcap, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline mean 63d
def f50tdc_f50_terminal_decline_composite_declinemean_63d_slope_v014_signal(revenue, opinc, marketcap):
    base = _mean(_f50_terminal_decline(revenue, opinc, marketcap, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline std 21d
def f50tdc_f50_terminal_decline_composite_declinestd_21d_slope_v015_signal(revenue, opinc, marketcap):
    base = _std(_f50_terminal_decline(revenue, opinc, marketcap, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline std 63d
def f50tdc_f50_terminal_decline_composite_declinestd_63d_slope_v016_signal(revenue, opinc, marketcap):
    base = _std(_f50_terminal_decline(revenue, opinc, marketcap, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline std 252d
def f50tdc_f50_terminal_decline_composite_declinestd_252d_slope_v017_signal(revenue, opinc, marketcap):
    base = _std(_f50_terminal_decline(revenue, opinc, marketcap, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline z 252d
def f50tdc_f50_terminal_decline_composite_declinez_252d_slope_v018_signal(revenue, opinc, marketcap):
    base = _z(_f50_terminal_decline(revenue, opinc, marketcap, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline z 504d
def f50tdc_f50_terminal_decline_composite_declinez_504d_slope_v019_signal(revenue, opinc, marketcap):
    base = _z(_f50_terminal_decline(revenue, opinc, marketcap, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_21d_slope_v020_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_63d_slope_v021_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_63d_slope_v022_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_252d_slope_v023_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_252d_slope_v024_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d revdecline
def f50tdc_f50_terminal_decline_composite_revdecline_504d_slope_v025_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline std 21d
def f50tdc_f50_terminal_decline_composite_revdeclinestd_21d_slope_v026_signal(revenue, marketcap):
    base = _std(_f50_revdecline(revenue, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline std 63d
def f50tdc_f50_terminal_decline_composite_revdeclinestd_63d_slope_v027_signal(revenue, marketcap):
    base = _std(_f50_revdecline(revenue, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline z 252d
def f50tdc_f50_terminal_decline_composite_revdeclinez_252d_slope_v028_signal(revenue, marketcap):
    base = _z(_f50_revdecline(revenue, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline z 504d
def f50tdc_f50_terminal_decline_composite_revdeclinez_504d_slope_v029_signal(revenue, marketcap):
    base = _z(_f50_revdecline(revenue, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_21d_slope_v030_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_63d_slope_v031_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_63d_slope_v032_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_252d_slope_v033_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_252d_slope_v034_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margcomp
def f50tdc_f50_terminal_decline_composite_margcomp_504d_slope_v035_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp std 63d
def f50tdc_f50_terminal_decline_composite_margcompstd_63d_slope_v036_signal(opinc, revenue, marketcap):
    base = _std(_f50_margincompress(opinc, revenue, 252), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcomp std 252d
def f50tdc_f50_terminal_decline_composite_margcompstd_252d_slope_v037_signal(opinc, revenue, marketcap):
    base = _std(_f50_margincompress(opinc, revenue, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp z 252d
def f50tdc_f50_terminal_decline_composite_margcompz_252d_slope_v038_signal(opinc, revenue, marketcap):
    base = _z(_f50_margincompress(opinc, revenue, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcomp z 504d
def f50tdc_f50_terminal_decline_composite_margcompz_504d_slope_v039_signal(opinc, revenue, marketcap):
    base = _z(_f50_margincompress(opinc, revenue, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline 10cnt 252d
def f50tdc_f50_terminal_decline_composite_decline10cnt_252d_slope_v040_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of decline 30cnt 504d
def f50tdc_f50_terminal_decline_composite_decline30cnt_504d_slope_v041_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline 5cnt 252d
def f50tdc_f50_terminal_decline_composite_revdecline5cnt_252d_slope_v042_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of revdecline 15cnt 504d
def f50tdc_f50_terminal_decline_composite_revdecline15cnt_504d_slope_v043_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcomp 2cnt 252d
def f50tdc_f50_terminal_decline_composite_margcomp2cnt_252d_slope_v044_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of margcomp 5cnt 504d
def f50tdc_f50_terminal_decline_composite_margcomp5cnt_504d_slope_v045_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst decline 21d
def f50tdc_f50_terminal_decline_composite_worstdecline_21d_slope_v046_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).rolling(21, min_periods=5).max() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst decline 63d
def f50tdc_f50_terminal_decline_composite_worstdecline_63d_slope_v047_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst decline 252d
def f50tdc_f50_terminal_decline_composite_worstdecline_252d_slope_v048_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst decline 504d
def f50tdc_f50_terminal_decline_composite_worstdecline_504d_slope_v049_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline EMA 21d
def f50tdc_f50_terminal_decline_composite_declineema_21d_slope_v050_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline EMA 63d
def f50tdc_f50_terminal_decline_composite_declineema_63d_slope_v051_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline EMA 252d
def f50tdc_f50_terminal_decline_composite_declineema_252d_slope_v052_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline sq 21d
def f50tdc_f50_terminal_decline_composite_declinesq_21d_slope_v053_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    base = s * s.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline sq 63d
def f50tdc_f50_terminal_decline_composite_declinesq_63d_slope_v054_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    base = s * s.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline sq 252d
def f50tdc_f50_terminal_decline_composite_declinesq_252d_slope_v055_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    base = s * s.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × ev 63d
def f50tdc_f50_terminal_decline_composite_declinexev_63d_slope_v056_signal(revenue, opinc, marketcap, ev):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline × ev 252d
def f50tdc_f50_terminal_decline_composite_declinexev_252d_slope_v057_signal(revenue, opinc, marketcap, ev):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × pe 63d
def f50tdc_f50_terminal_decline_composite_declinexpe_63d_slope_v058_signal(revenue, opinc, marketcap, pe):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × ps 63d
def f50tdc_f50_terminal_decline_composite_declinexps_63d_slope_v059_signal(revenue, opinc, marketcap, ps):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × evebitda 63d
def f50tdc_f50_terminal_decline_composite_declinexevebitda_63d_slope_v060_signal(revenue, opinc, marketcap, evebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × evebit 63d
def f50tdc_f50_terminal_decline_composite_declinexevebit_63d_slope_v061_signal(revenue, opinc, marketcap, evebit):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * evebit * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × pb 63d
def f50tdc_f50_terminal_decline_composite_declinexpb_63d_slope_v062_signal(revenue, opinc, marketcap, pb):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * pb * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline × ev 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexev_63d_slope_v063_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 63) * ev + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline × pe 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexpe_63d_slope_v064_signal(revenue, marketcap, pe):
    base = _f50_revdecline(revenue, 63) * pe * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline × ps 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexps_252d_slope_v065_signal(revenue, marketcap, ps):
    base = _f50_revdecline(revenue, 252) * ps * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp × ev 63d
def f50tdc_f50_terminal_decline_composite_margcompxev_63d_slope_v066_signal(opinc, revenue, marketcap, ev):
    base = _f50_margincompress(opinc, revenue, 63) * ev + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp × pe 63d
def f50tdc_f50_terminal_decline_composite_margcompxpe_63d_slope_v067_signal(opinc, revenue, marketcap, pe):
    base = _f50_margincompress(opinc, revenue, 63) * pe * marketcap + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline gap 63m252
def f50tdc_f50_terminal_decline_composite_declinegap_63m252_slope_v068_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    base = (a - b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of decline gap 21m63
def f50tdc_f50_terminal_decline_composite_declinegap_21m63_slope_v069_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    base = (a - b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline gap 252m504
def f50tdc_f50_terminal_decline_composite_declinegap_252m504_slope_v070_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    base = (a - b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline ratio 63v252
def f50tdc_f50_terminal_decline_composite_declineratio_63v252_slope_v071_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of decline ratio 21v63
def f50tdc_f50_terminal_decline_composite_declineratio_21v63_slope_v072_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 63).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline worst-ever
def f50tdc_f50_terminal_decline_composite_declineworstever_slope_v073_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).expanding(min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline vs ever 63d
def f50tdc_f50_terminal_decline_composite_declinevsever_63d_slope_v074_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    worst = s.expanding(min_periods=63).max()
    base = (worst - s) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline vs ever 252d
def f50tdc_f50_terminal_decline_composite_declinevsever_252d_slope_v075_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    worst = s.expanding(min_periods=63).max()
    base = (worst - s) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × marketcap squared 63d
def f50tdc_f50_terminal_decline_composite_declinexmcapsq_63d_slope_v076_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * marketcap * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline × marketcap squared 252d
def f50tdc_f50_terminal_decline_composite_declinexmcapsq_252d_slope_v077_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * marketcap * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × log marketcap 63d
def f50tdc_f50_terminal_decline_composite_declinexlogmcap_63d_slope_v078_signal(revenue, opinc, marketcap):
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * lm * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × revenue 63d
def f50tdc_f50_terminal_decline_composite_declinexrev_63d_slope_v079_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * revenue
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline × assets 63d
def f50tdc_f50_terminal_decline_composite_declinexassets_63d_slope_v080_signal(revenue, opinc, marketcap, assets):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * assets + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline × debt 252d
def f50tdc_f50_terminal_decline_composite_declinexdebt_252d_slope_v081_signal(revenue, opinc, marketcap, debt):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * debt + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline area 63d
def f50tdc_f50_terminal_decline_composite_declinearea_63d_slope_v082_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63).abs().rolling(63, min_periods=21).sum() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline area 252d
def f50tdc_f50_terminal_decline_composite_declinearea_252d_slope_v083_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs().rolling(252, min_periods=63).sum() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of decline area 504d
def f50tdc_f50_terminal_decline_composite_declinearea_504d_slope_v084_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504).abs().rolling(504, min_periods=126).sum() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revxmargcomp 63d
def f50tdc_f50_terminal_decline_composite_revxmargcomp_63d_slope_v085_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 63)
    b = _f50_margincompress(opinc, revenue, 63)
    base = a * b * marketcap + _f50_terminal_decline(revenue, opinc, marketcap, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositesev 252d × ev
def f50tdc_f50_terminal_decline_composite_compositesev_252d_slope_v086_signal(revenue, opinc, marketcap, ev):
    a = _f50_revdecline(revenue, 252).abs()
    b = _f50_margincompress(opinc, revenue, 252).abs()
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    base = (a + b + c) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline EMA 21d
def f50tdc_f50_terminal_decline_composite_revdeclineema_21d_slope_v087_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline EMA 63d
def f50tdc_f50_terminal_decline_composite_revdeclineema_63d_slope_v088_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline EMA 252d
def f50tdc_f50_terminal_decline_composite_revdeclineema_252d_slope_v089_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp EMA 21d
def f50tdc_f50_terminal_decline_composite_margcompema_21d_slope_v090_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp EMA 63d
def f50tdc_f50_terminal_decline_composite_margcompema_63d_slope_v091_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcomp EMA 252d
def f50tdc_f50_terminal_decline_composite_margcompema_252d_slope_v092_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst revdecline 21d
def f50tdc_f50_terminal_decline_composite_worstrevdecline_21d_slope_v093_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63).rolling(21, min_periods=5).max() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst revdecline 63d
def f50tdc_f50_terminal_decline_composite_worstrevdecline_63d_slope_v094_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst revdecline 252d
def f50tdc_f50_terminal_decline_composite_worstrevdecline_252d_slope_v095_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst revdecline 504d
def f50tdc_f50_terminal_decline_composite_worstrevdecline_504d_slope_v096_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst margcomp 63d
def f50tdc_f50_terminal_decline_composite_worstmargcomp_63d_slope_v097_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63).rolling(63, min_periods=21).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst margcomp 252d
def f50tdc_f50_terminal_decline_composite_worstmargcomp_252d_slope_v098_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252).rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst margcomp 504d
def f50tdc_f50_terminal_decline_composite_worstmargcomp_504d_slope_v099_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 504).rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdecline sq 63d
def f50tdc_f50_terminal_decline_composite_revdeclinesq_63d_slope_v100_signal(revenue, marketcap):
    d = _f50_revdecline(revenue, 63)
    base = d * d.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdecline sq 252d
def f50tdc_f50_terminal_decline_composite_revdeclinesq_252d_slope_v101_signal(revenue, marketcap):
    d = _f50_revdecline(revenue, 252)
    base = d * d.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcomp sq 63d
def f50tdc_f50_terminal_decline_composite_margcompsq_63d_slope_v102_signal(opinc, revenue, marketcap):
    m = _f50_margincompress(opinc, revenue, 63)
    base = m * m.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcomp sq 252d
def f50tdc_f50_terminal_decline_composite_margcompsq_252d_slope_v103_signal(opinc, revenue, marketcap):
    m = _f50_margincompress(opinc, revenue, 252)
    base = m * m.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdeclinexev 21d
def f50tdc_f50_terminal_decline_composite_revdeclinexev_21d_slope_v104_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 21) * ev + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdeclinexev 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexev_252d_slope_v105_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 252) * ev + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcompxev 252d
def f50tdc_f50_terminal_decline_composite_margcompxev_252d_slope_v106_signal(opinc, revenue, marketcap, ev):
    base = _f50_margincompress(opinc, revenue, 252) * ev + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdeclinexevebitda 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexevebitda_63d_slope_v107_signal(revenue, marketcap, evebitda):
    base = _f50_revdecline(revenue, 63) * evebitda * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdeclinexevebit 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexevebit_252d_slope_v108_signal(revenue, marketcap, evebit):
    base = _f50_revdecline(revenue, 252) * evebit * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdeclinexpb 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexpb_63d_slope_v109_signal(revenue, marketcap, pb):
    base = _f50_revdecline(revenue, 63) * pb * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdeclinexps 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexps_63d_slope_v110_signal(revenue, marketcap, ps):
    base = _f50_revdecline(revenue, 63) * ps * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcompxevebitda 63d
def f50tdc_f50_terminal_decline_composite_margcompxevebitda_63d_slope_v111_signal(opinc, revenue, marketcap, evebitda):
    base = _f50_margincompress(opinc, revenue, 63) * evebitda * marketcap + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margcompxevebit 252d
def f50tdc_f50_terminal_decline_composite_margcompxevebit_252d_slope_v112_signal(opinc, revenue, marketcap, evebit):
    base = _f50_margincompress(opinc, revenue, 252) * evebit * marketcap + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcompxpb 63d
def f50tdc_f50_terminal_decline_composite_margcompxpb_63d_slope_v113_signal(opinc, revenue, marketcap, pb):
    base = _f50_margincompress(opinc, revenue, 63) * pb * marketcap + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcompxps 63d
def f50tdc_f50_terminal_decline_composite_margcompxps_63d_slope_v114_signal(opinc, revenue, marketcap, ps):
    base = _f50_margincompress(opinc, revenue, 63) * ps * marketcap + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revdeclinexdebt 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexdebt_252d_slope_v115_signal(revenue, marketcap, debt):
    base = _f50_revdecline(revenue, 252) * debt + _f50_margincompress(revenue, revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexdilution 63d
def f50tdc_f50_terminal_decline_composite_declinexdilution_63d_slope_v116_signal(revenue, opinc, marketcap, sharesbas):
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexdilution 252d
def f50tdc_f50_terminal_decline_composite_declinexdilution_252d_slope_v117_signal(revenue, opinc, marketcap, sharesbas):
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexlev 63d
def f50tdc_f50_terminal_decline_composite_declinexlev_63d_slope_v118_signal(revenue, opinc, marketcap, debt, equity):
    lev = debt / equity.replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * lev * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexlev 252d
def f50tdc_f50_terminal_decline_composite_declinexlev_252d_slope_v119_signal(revenue, opinc, marketcap, debt, equity):
    lev = debt / equity.replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * lev * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexinveq 63d
def f50tdc_f50_terminal_decline_composite_declinexinveq_63d_slope_v120_signal(revenue, opinc, marketcap, equity):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * inveq * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexinveq 252d
def f50tdc_f50_terminal_decline_composite_declinexinveq_252d_slope_v121_signal(revenue, opinc, marketcap, equity):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * inveq * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of decline anomaly 63d
def f50tdc_f50_terminal_decline_composite_declineanomaly_63d_slope_v122_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    base = (a - b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of decline anomaly 252d
def f50tdc_f50_terminal_decline_composite_declineanomaly_252d_slope_v123_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    base = (a - b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexevebitda 252d
def f50tdc_f50_terminal_decline_composite_declinexevebitda_252d_slope_v124_signal(revenue, opinc, marketcap, evebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * evebitda * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexevebit 252d
def f50tdc_f50_terminal_decline_composite_declinexevebit_252d_slope_v125_signal(revenue, opinc, marketcap, evebit):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * evebit * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexpb 252d
def f50tdc_f50_terminal_decline_composite_declinexpb_252d_slope_v126_signal(revenue, opinc, marketcap, pb):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * pb * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexpe 252d
def f50tdc_f50_terminal_decline_composite_declinexpe_252d_slope_v127_signal(revenue, opinc, marketcap, pe):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * pe * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexps 252d
def f50tdc_f50_terminal_decline_composite_declinexps_252d_slope_v128_signal(revenue, opinc, marketcap, ps):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * ps * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexlogmcap 252d
def f50tdc_f50_terminal_decline_composite_declinexlogmcap_252d_slope_v129_signal(revenue, opinc, marketcap):
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * lm * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexrev 252d
def f50tdc_f50_terminal_decline_composite_declinexrev_252d_slope_v130_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * revenue
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexassets 252d
def f50tdc_f50_terminal_decline_composite_declinexassets_252d_slope_v131_signal(revenue, opinc, marketcap, assets):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * assets + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexdebt 63d
def f50tdc_f50_terminal_decline_composite_declinexdebt_63d_slope_v132_signal(revenue, opinc, marketcap, debt):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * debt + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexequity 63d
def f50tdc_f50_terminal_decline_composite_declinexequity_63d_slope_v133_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * equity.abs() + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexequity 252d
def f50tdc_f50_terminal_decline_composite_declinexequity_252d_slope_v134_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * equity.abs() + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexebitda 63d
def f50tdc_f50_terminal_decline_composite_declinexebitda_63d_slope_v135_signal(revenue, opinc, marketcap, ebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * ebitda + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexebitda 252d
def f50tdc_f50_terminal_decline_composite_declinexebitda_252d_slope_v136_signal(revenue, opinc, marketcap, ebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * ebitda + _f50_revdecline(revenue, 21) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declineareafrac 63v252
def f50tdc_f50_terminal_decline_composite_declineareafrac_63v252_slope_v137_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    a = s.rolling(63, min_periods=21).sum()
    b = s.rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declineareafrac 252v504
def f50tdc_f50_terminal_decline_composite_declineareafrac_252v504_slope_v138_signal(revenue, opinc, marketcap):
    s = _f50_terminal_decline(revenue, opinc, marketcap, 504).abs()
    a = s.rolling(252, min_periods=63).sum()
    b = s.rolling(504, min_periods=126).sum().replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinevolvol 63d
def f50tdc_f50_terminal_decline_composite_declinevolvol_63d_slope_v139_signal(revenue, opinc, marketcap):
    sd = _std(_f50_terminal_decline(revenue, opinc, marketcap, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinevolvol 252d
def f50tdc_f50_terminal_decline_composite_declinevolvol_252d_slope_v140_signal(revenue, opinc, marketcap):
    sd = _std(_f50_terminal_decline(revenue, opinc, marketcap, 504), 252)
    base = _std(sd, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revdeclinevolvol 63d
def f50tdc_f50_terminal_decline_composite_revdeclinevolvol_63d_slope_v141_signal(revenue, marketcap):
    sd = _std(_f50_revdecline(revenue, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margcompvolvol 63d
def f50tdc_f50_terminal_decline_composite_margcompvolvol_63d_slope_v142_signal(opinc, revenue, marketcap):
    sd = _std(_f50_margincompress(opinc, revenue, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexclose 63d
def f50tdc_f50_terminal_decline_composite_declinexclose_63d_slope_v143_signal(revenue, opinc, marketcap, closeadj):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63) * closeadj * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexclose 252d
def f50tdc_f50_terminal_decline_composite_declinexclose_252d_slope_v144_signal(revenue, opinc, marketcap, closeadj):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * closeadj * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of declinexrevg 21d
def f50tdc_f50_terminal_decline_composite_declinexrevg_21d_slope_v145_signal(revenue, opinc, marketcap):
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21) * rg * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of declinexrevg 252d
def f50tdc_f50_terminal_decline_composite_declinexrevg_252d_slope_v146_signal(revenue, opinc, marketcap):
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252) * rg * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multifactor 63d
def f50tdc_f50_terminal_decline_composite_multifactor_63d_slope_v147_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 63)
    b = _f50_margincompress(opinc, revenue, 63)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    base = (a + b + c) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of multifactor 252d
def f50tdc_f50_terminal_decline_composite_multifactor_252d_slope_v148_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 252)
    b = _f50_margincompress(opinc, revenue, 252)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    base = (a + b + c) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of multifactor 504d
def f50tdc_f50_terminal_decline_composite_multifactor_504d_slope_v149_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 504)
    b = _f50_margincompress(opinc, revenue, 504)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    base = (a + b + c) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of compositesev 252d × ev (extra)
def f50tdc_f50_terminal_decline_composite_compositesev_252d_extra_slope_v150_signal(revenue, opinc, marketcap, ev):
    a = _f50_revdecline(revenue, 252).abs()
    b = _f50_margincompress(opinc, revenue, 252).abs()
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    base = (a + b + c) * ev
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f50tdc_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_TERMINAL_DECLINE_COMPOSITE_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_terminal_decline", "_f50_revdecline", "_f50_margincompress")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f50_terminal_decline_composite_2nd_derivatives_001_150_claude: {n_features} features pass")
