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
def _f48_cash_runway(ncfo, marketcap):
    cash_proxy = marketcap * 0.05
    return cash_proxy / ncfo.abs().replace(0, np.nan)


def _f48_burnyield(ncfo, marketcap):
    return ncfo / marketcap.replace(0, np.nan)


def _f48_runway_qtrs(fcf, marketcap):
    burn_q = fcf.abs() / 4.0
    cash_proxy = marketcap * 0.05
    return cash_proxy / burn_q.replace(0, np.nan)


# Programmatically build 150 unique slope feature definitions
def _make_slope_feature(idx, base_kind, win_a, win_b, slope_w, has_extra=None):
    """Generates a single slope feature. Used at module-load time."""
    pass


# 5d slope of 21d runway × marketcap
def f48cr_f48_cash_runway_runway_21d_slope_v001_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d runway × marketcap
def f48cr_f48_cash_runway_runway_21d_slope_v002_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d runway × marketcap
def f48cr_f48_cash_runway_runway_63d_slope_v003_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d runway × marketcap
def f48cr_f48_cash_runway_runway_63d_slope_v004_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d runway
def f48cr_f48_cash_runway_runway_63d_slope_v005_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d runway
def f48cr_f48_cash_runway_runway_252d_slope_v006_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d runway
def f48cr_f48_cash_runway_runway_252d_slope_v007_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d runway
def f48cr_f48_cash_runway_runway_504d_slope_v008_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d runway
def f48cr_f48_cash_runway_runway_504d_slope_v009_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d runway
def f48cr_f48_cash_runway_runway_504d_slope_v010_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d burn yield × marketcap
def f48cr_f48_cash_runway_burn_21d_slope_v011_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d burn yield × marketcap
def f48cr_f48_cash_runway_burn_21d_slope_v012_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d burn yield
def f48cr_f48_cash_runway_burn_63d_slope_v013_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d burn yield
def f48cr_f48_cash_runway_burn_63d_slope_v014_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d burn yield
def f48cr_f48_cash_runway_burn_63d_slope_v015_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d burn yield
def f48cr_f48_cash_runway_burn_252d_slope_v016_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d burn yield
def f48cr_f48_cash_runway_burn_252d_slope_v017_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d burn yield
def f48cr_f48_cash_runway_burn_504d_slope_v018_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d burn yield
def f48cr_f48_cash_runway_burn_504d_slope_v019_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d quarters runway
def f48cr_f48_cash_runway_qtrs_21d_slope_v020_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d quarters runway
def f48cr_f48_cash_runway_qtrs_63d_slope_v021_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d quarters runway
def f48cr_f48_cash_runway_qtrs_63d_slope_v022_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d quarters runway
def f48cr_f48_cash_runway_qtrs_252d_slope_v023_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d quarters runway
def f48cr_f48_cash_runway_qtrs_252d_slope_v024_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d quarters runway
def f48cr_f48_cash_runway_qtrs_504d_slope_v025_signal(fcf, marketcap):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway std 21d
def f48cr_f48_cash_runway_runwaystd_21d_slope_v026_signal(ncfo, marketcap):
    base = _std(_f48_cash_runway(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway std 63d
def f48cr_f48_cash_runway_runwaystd_63d_slope_v027_signal(ncfo, marketcap):
    base = _std(_f48_cash_runway(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway std 252d
def f48cr_f48_cash_runway_runwaystd_252d_slope_v028_signal(ncfo, marketcap):
    base = _std(_f48_cash_runway(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn std 21d
def f48cr_f48_cash_runway_burnstd_21d_slope_v029_signal(ncfo, marketcap):
    base = _std(_f48_burnyield(ncfo, marketcap), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn std 63d
def f48cr_f48_cash_runway_burnstd_63d_slope_v030_signal(ncfo, marketcap):
    base = _std(_f48_burnyield(ncfo, marketcap), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn std 252d
def f48cr_f48_cash_runway_burnstd_252d_slope_v031_signal(ncfo, marketcap):
    base = _std(_f48_burnyield(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway zscore 252d
def f48cr_f48_cash_runway_runwayz_252d_slope_v032_signal(ncfo, marketcap):
    base = _z(_f48_cash_runway(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway zscore 504d
def f48cr_f48_cash_runway_runwayz_504d_slope_v033_signal(ncfo, marketcap):
    base = _z(_f48_cash_runway(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn zscore 252d
def f48cr_f48_cash_runway_burnz_252d_slope_v034_signal(ncfo, marketcap):
    base = _z(_f48_burnyield(ncfo, marketcap), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn zscore 504d
def f48cr_f48_cash_runway_burnz_504d_slope_v035_signal(ncfo, marketcap):
    base = _z(_f48_burnyield(ncfo, marketcap), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d runway mean × marketcap
def f48cr_f48_cash_runway_lowrunwaycount_252d_slope_v036_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    base = base.rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of severe low-runway count 504d
def f48cr_f48_cash_runway_lowrunwaycount_504d_slope_v037_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn day count 252d
def f48cr_f48_cash_runway_burndaycount_252d_slope_v038_signal(ncfo, marketcap):
    burn = _f48_burnyield(ncfo, marketcap)
    base = (burn).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of burn day count 504d
def f48cr_f48_cash_runway_burndaycount_504d_slope_v039_signal(ncfo, marketcap):
    burn = _f48_burnyield(ncfo, marketcap)
    base = (burn).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst-runway 21d
def f48cr_f48_cash_runway_worstrunway_21d_slope_v040_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(21, min_periods=5).min() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst-runway 63d
def f48cr_f48_cash_runway_worstrunway_63d_slope_v041_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(63, min_periods=21).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst-runway 252d
def f48cr_f48_cash_runway_worstrunway_252d_slope_v042_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(252, min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worst-runway 504d
def f48cr_f48_cash_runway_worstrunway_504d_slope_v043_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(504, min_periods=126).min() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway EMA 21d
def f48cr_f48_cash_runway_runwayema_21d_slope_v044_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway EMA 63d
def f48cr_f48_cash_runway_runwayema_63d_slope_v045_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway EMA 252d
def f48cr_f48_cash_runway_runwayema_252d_slope_v046_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn EMA 21d
def f48cr_f48_cash_runway_burnema_21d_slope_v047_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn EMA 63d
def f48cr_f48_cash_runway_burnema_63d_slope_v048_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn EMA 252d
def f48cr_f48_cash_runway_burnema_252d_slope_v049_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × ev 63d
def f48cr_f48_cash_runway_runwayxev_63d_slope_v050_signal(ncfo, marketcap, ev):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × ev 252d
def f48cr_f48_cash_runway_runwayxev_252d_slope_v051_signal(ncfo, marketcap, ev):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × pe 63d
def f48cr_f48_cash_runway_runwayxpe_63d_slope_v052_signal(ncfo, marketcap, pe):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × ps 63d
def f48cr_f48_cash_runway_runwayxps_63d_slope_v053_signal(ncfo, marketcap, ps):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × evebitda 63d
def f48cr_f48_cash_runway_runwayxevebitda_63d_slope_v054_signal(ncfo, marketcap, evebitda):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × evebit 63d
def f48cr_f48_cash_runway_runwayxevebit_63d_slope_v055_signal(ncfo, marketcap, evebit):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * evebit * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × pb 63d
def f48cr_f48_cash_runway_runwayxpb_63d_slope_v056_signal(ncfo, marketcap, pb):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * pb * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × ev 63d
def f48cr_f48_cash_runway_burnxev_63d_slope_v057_signal(ncfo, marketcap, ev):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × pe 63d
def f48cr_f48_cash_runway_burnxpe_63d_slope_v058_signal(ncfo, marketcap, pe):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × ps 63d
def f48cr_f48_cash_runway_burnxps_63d_slope_v059_signal(ncfo, marketcap, ps):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × evebitda 63d
def f48cr_f48_cash_runway_burnxevebitda_63d_slope_v060_signal(ncfo, marketcap, evebitda):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of qtrs × ev 63d
def f48cr_f48_cash_runway_qtrsxev_63d_slope_v061_signal(fcf, marketcap, ev):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 63) * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of qtrs × pe 63d
def f48cr_f48_cash_runway_qtrsxpe_63d_slope_v062_signal(fcf, marketcap, pe):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 63) * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of qtrs × ps 63d
def f48cr_f48_cash_runway_qtrsxps_63d_slope_v063_signal(fcf, marketcap, ps):
    base = _mean(_f48_runway_qtrs(fcf, marketcap), 63) * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × debt 63d
def f48cr_f48_cash_runway_runwayxdebt_63d_slope_v064_signal(ncfo, marketcap, debt):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * debt + _f48_burnyield(ncfo, marketcap) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × debt 252d
def f48cr_f48_cash_runway_runwayxdebt_252d_slope_v065_signal(ncfo, marketcap, debt):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * debt + _f48_burnyield(ncfo, marketcap) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × leverage 63d
def f48cr_f48_cash_runway_runwayxlev_63d_slope_v066_signal(ncfo, marketcap, debt, equity):
    lev = debt / equity.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * lev * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × leverage 252d
def f48cr_f48_cash_runway_runwayxlev_252d_slope_v067_signal(ncfo, marketcap, debt, equity):
    lev = debt / equity.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * lev * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × shares growth 63d
def f48cr_f48_cash_runway_runwayxshareg_63d_slope_v068_signal(ncfo, marketcap, sharesbas):
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × shares growth 252d
def f48cr_f48_cash_runway_runwayxshareg_252d_slope_v069_signal(ncfo, marketcap, sharesbas):
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × capex intensity 63d
def f48cr_f48_cash_runway_runwayxcapex_63d_slope_v070_signal(ncfo, marketcap, capex, revenue):
    cx = capex / revenue.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * cx * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn squared 21d
def f48cr_f48_cash_runway_burnsq_21d_slope_v071_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(b * b.abs(), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn squared 63d
def f48cr_f48_cash_runway_burnsq_63d_slope_v072_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(b * b.abs(), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn squared 252d
def f48cr_f48_cash_runway_burnsq_252d_slope_v073_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(b * b.abs(), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway squared 21d
def f48cr_f48_cash_runway_runwaysq_21d_slope_v074_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = _mean(r * r.abs(), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worst-burn 21d
def f48cr_f48_cash_runway_worstburn_21d_slope_v075_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).rolling(21, min_periods=5).min() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst-burn 63d
def f48cr_f48_cash_runway_worstburn_63d_slope_v076_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).rolling(63, min_periods=21).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worst-burn 252d
def f48cr_f48_cash_runway_worstburn_252d_slope_v077_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).rolling(252, min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × revenue 63d
def f48cr_f48_cash_runway_burnxrev_63d_slope_v078_signal(ncfo, marketcap, revenue):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * revenue
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × assets 63d
def f48cr_f48_cash_runway_burnxassets_63d_slope_v079_signal(ncfo, marketcap, assets):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * assets
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst-runway
def f48cr_f48_cash_runway_worstrunwayever_slope_v080_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).expanding(min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst-burn
def f48cr_f48_cash_runway_worstburnever_slope_v081_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).expanding(min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway-vs-ever 63d
def f48cr_f48_cash_runway_runwayvsever_63d_slope_v082_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    worst = r.expanding(min_periods=63).min()
    base = (r - worst) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn-vs-ever 63d
def f48cr_f48_cash_runway_burnvsever_63d_slope_v083_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    worst = b.expanding(min_periods=63).min()
    base = (b - worst) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × ebitda margin 63d
def f48cr_f48_cash_runway_runwayxebmargin_63d_slope_v084_signal(ncfo, marketcap, ebitda, revenue):
    em = ebitda / revenue.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * em * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × ebitda margin 252d
def f48cr_f48_cash_runway_burnxebmargin_252d_slope_v085_signal(ncfo, marketcap, ebitda, revenue):
    em = ebitda / revenue.replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * em * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of composite scarcity 63d
def f48cr_f48_cash_runway_scarcity_63d_slope_v086_signal(ncfo, marketcap, fcf):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    base = _mean(burn / runway.replace(0, np.nan).abs(), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway diff 21d
def f48cr_f48_cash_runway_runwaydiff_21d_slope_v087_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = _mean(_diff(r, 21), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway diff 63d
def f48cr_f48_cash_runway_runwaydiff_63d_slope_v088_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = _mean(_diff(r, 63), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway diff 252d
def f48cr_f48_cash_runway_runwaydiff_252d_slope_v089_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = _mean(_diff(r, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn diff 21d
def f48cr_f48_cash_runway_burndiff_21d_slope_v090_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(_diff(b, 21), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn diff 63d
def f48cr_f48_cash_runway_burndiff_63d_slope_v091_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(_diff(b, 63), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn diff 252d
def f48cr_f48_cash_runway_burndiff_252d_slope_v092_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = _mean(_diff(b, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × marketcap squared 63d
def f48cr_f48_cash_runway_runwayxmcapsq_63d_slope_v093_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * marketcap * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × marketcap squared 252d
def f48cr_f48_cash_runway_runwayxmcapsq_252d_slope_v094_signal(ncfo, marketcap):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * marketcap * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × marketcap squared 63d
def f48cr_f48_cash_runway_burnxmcapsq_63d_slope_v095_signal(ncfo, marketcap):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * marketcap * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway ratio 21v63
def f48cr_f48_cash_runway_runwayratio_21v63_slope_v096_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    a = _mean(r, 21)
    b = _mean(r, 63).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway ratio 63v252
def f48cr_f48_cash_runway_runwayratio_63v252_slope_v097_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    a = _mean(r, 63)
    b = _mean(r, 252).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway ratio 252v504
def f48cr_f48_cash_runway_runwayratio_252v504_slope_v098_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    a = _mean(r, 252)
    b = _mean(r, 504).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn ratio 21v63
def f48cr_f48_cash_runway_burnratio_21v63_slope_v099_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    a = _mean(b, 21)
    bb = _mean(b, 63).replace(0, np.nan)
    base = (a / bb) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn ratio 63v252
def f48cr_f48_cash_runway_burnratio_63v252_slope_v100_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    a = _mean(b, 63)
    bb = _mean(b, 252).replace(0, np.nan)
    base = (a / bb) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway gap 21m63
def f48cr_f48_cash_runway_runwaygapdiff_21m63_slope_v101_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = (_mean(r, 21) - _mean(r, 63)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway gap 63m252
def f48cr_f48_cash_runway_runwaygapdiff_63m252_slope_v102_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = (_mean(r, 63) - _mean(r, 252)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway gap 252m504
def f48cr_f48_cash_runway_runwaygapdiff_252m504_slope_v103_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = (_mean(r, 252) - _mean(r, 504)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of low-runway count 8 252d
def f48cr_f48_cash_runway_lowrunwaycount8_252d_slope_v104_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    base = (base).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of crit-runway count 504d
def f48cr_f48_cash_runway_critrunwaycount_504d_slope_v105_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    base = (base).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of severe burn count 10 252d
def f48cr_f48_cash_runway_severeburncount10_252d_slope_v106_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = (b).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of severe burn count 25 504d
def f48cr_f48_cash_runway_severeburncount25_504d_slope_v107_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = (b).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × debt growth 21d
def f48cr_f48_cash_runway_burnxdebtg_21d_slope_v108_signal(ncfo, marketcap, debt):
    dg = debt.diff(63) / debt.shift(63).abs().replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 21) * dg * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × debt growth 63d
def f48cr_f48_cash_runway_burnxdebtg_63d_slope_v109_signal(ncfo, marketcap, debt):
    dg = debt.diff(63) / debt.shift(63).abs().replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * dg * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × debt growth 252d
def f48cr_f48_cash_runway_burnxdebtg_252d_slope_v110_signal(ncfo, marketcap, debt):
    dg = debt.diff(252) / debt.shift(252).abs().replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * dg * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × revenue growth 21d
def f48cr_f48_cash_runway_runwayxrevg_21d_slope_v111_signal(ncfo, marketcap, revenue):
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 21) * rg * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × revenue growth 252d
def f48cr_f48_cash_runway_runwayxrevg_252d_slope_v112_signal(ncfo, marketcap, revenue):
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * rg * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × log marketcap 21d
def f48cr_f48_cash_runway_runwayxlogmcap_21d_slope_v113_signal(ncfo, marketcap):
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = _mean(_f48_cash_runway(ncfo, marketcap), 21) * lm * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × log marketcap 252d
def f48cr_f48_cash_runway_runwayxlogmcap_252d_slope_v114_signal(ncfo, marketcap):
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * lm * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × close 63d
def f48cr_f48_cash_runway_burnxclose_63d_slope_v115_signal(ncfo, marketcap, closeadj):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * closeadj * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × close 252d
def f48cr_f48_cash_runway_runwayxclose_252d_slope_v116_signal(ncfo, marketcap, closeadj):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * closeadj * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway-area 63d
def f48cr_f48_cash_runway_runwayarea_63d_slope_v117_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(63, min_periods=21).sum() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway-area 252d
def f48cr_f48_cash_runway_runwayarea_252d_slope_v118_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(252, min_periods=63).sum() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of runway-area 504d
def f48cr_f48_cash_runway_runwayarea_504d_slope_v119_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap).rolling(504, min_periods=126).sum() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn-area 63d
def f48cr_f48_cash_runway_burnarea_63d_slope_v120_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).abs().rolling(63, min_periods=21).sum() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn-area 252d
def f48cr_f48_cash_runway_burnarea_252d_slope_v121_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).abs().rolling(252, min_periods=63).sum() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway volvol 63d
def f48cr_f48_cash_runway_runwayvolvol_63d_slope_v122_signal(ncfo, marketcap):
    sd = _std(_f48_cash_runway(ncfo, marketcap), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway volvol 252d
def f48cr_f48_cash_runway_runwayvolvol_252d_slope_v123_signal(ncfo, marketcap):
    sd = _std(_f48_cash_runway(ncfo, marketcap), 252)
    base = _std(sd, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn volvol 63d
def f48cr_f48_cash_runway_burnvolvol_63d_slope_v124_signal(ncfo, marketcap):
    sd = _std(_f48_burnyield(ncfo, marketcap), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway anomaly 63d
def f48cr_f48_cash_runway_runwayanomaly_63d_slope_v125_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = (_mean(r, 63) - _mean(r, 252)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway anomaly 252d
def f48cr_f48_cash_runway_runwayanomaly_252d_slope_v126_signal(ncfo, marketcap):
    r = _f48_cash_runway(ncfo, marketcap)
    base = (_mean(r, 252) - _mean(r, 504)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn anomaly 63d
def f48cr_f48_cash_runway_burnanomaly_63d_slope_v127_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = (_mean(b, 63) - _mean(b, 252)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn anomaly 252d
def f48cr_f48_cash_runway_burnanomaly_252d_slope_v128_signal(ncfo, marketcap):
    b = _f48_burnyield(ncfo, marketcap)
    base = (_mean(b, 252) - _mean(b, 504)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × shares 63d
def f48cr_f48_cash_runway_burnxshares_63d_slope_v129_signal(ncfo, marketcap, sharesbas):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * sharesbas + _f48_runway_qtrs(ncfo, marketcap) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × shares 252d
def f48cr_f48_cash_runway_runwayxshares_252d_slope_v130_signal(ncfo, marketcap, sharesbas):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * sharesbas + _f48_burnyield(ncfo, marketcap) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × shares growth 252d
def f48cr_f48_cash_runway_burnxshareg_252d_slope_v131_signal(ncfo, marketcap, sharesbas):
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × evrev 63d
def f48cr_f48_cash_runway_runwayxevrev_63d_slope_v132_signal(ncfo, marketcap, ev, revenue):
    er = ev / revenue.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * er * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × evrev 252d
def f48cr_f48_cash_runway_runwayxevrev_252d_slope_v133_signal(ncfo, marketcap, ev, revenue):
    er = ev / revenue.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * er * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × inverse-equity 63d
def f48cr_f48_cash_runway_runwayxinveq_63d_slope_v134_signal(ncfo, marketcap, equity):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * inveq * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × inverse-equity 252d
def f48cr_f48_cash_runway_runwayxinveq_252d_slope_v135_signal(ncfo, marketcap, equity):
    inveq = marketcap / equity.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * inveq * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × inverse-assets 63d
def f48cr_f48_cash_runway_runwayxinvassets_63d_slope_v136_signal(ncfo, marketcap, assets):
    inva = marketcap / assets.replace(0, np.nan)
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * inva * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × inverse-assets 252d
def f48cr_f48_cash_runway_burnxinvassets_252d_slope_v137_signal(ncfo, marketcap, assets):
    inva = marketcap / assets.replace(0, np.nan)
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * inva * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × evebit 63d
def f48cr_f48_cash_runway_burnxevebit_63d_slope_v138_signal(ncfo, marketcap, evebit):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * evebit * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × evebit 252d
def f48cr_f48_cash_runway_burnxevebit_252d_slope_v139_signal(ncfo, marketcap, evebit):
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * evebit * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of burn × pb 63d
def f48cr_f48_cash_runway_burnxpb_63d_slope_v140_signal(ncfo, marketcap, pb):
    base = _mean(_f48_burnyield(ncfo, marketcap), 63) * pb * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × pb 252d
def f48cr_f48_cash_runway_burnxpb_252d_slope_v141_signal(ncfo, marketcap, pb):
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * pb * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multifactor 63d
def f48cr_f48_cash_runway_multifactor_63d_slope_v142_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 63) + _mean(b, 63) + _mean(c, 63)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of multifactor 252d
def f48cr_f48_cash_runway_multifactor_252d_slope_v143_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 252) + _mean(b, 252) + _mean(c, 252)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of multifactor 504d
def f48cr_f48_cash_runway_multifactor_504d_slope_v144_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 504) + _mean(b, 504) + _mean(c, 504)) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × revenue 63d
def f48cr_f48_cash_runway_runwayxrev_63d_slope_v145_signal(ncfo, marketcap, revenue):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * revenue
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of runway × revenue 252d
def f48cr_f48_cash_runway_runwayxrev_252d_slope_v146_signal(ncfo, marketcap, revenue):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 252) * revenue
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of burn × revenue 252d
def f48cr_f48_cash_runway_burnxrev_252d_slope_v147_signal(ncfo, marketcap, revenue):
    base = _mean(_f48_burnyield(ncfo, marketcap), 252) * revenue
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of runway × ebitda 63d
def f48cr_f48_cash_runway_runwayxebitda_63d_slope_v148_signal(ncfo, marketcap, ebitda):
    base = _mean(_f48_cash_runway(ncfo, marketcap), 63) * ebitda + _f48_runway_qtrs(ncfo, marketcap) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite scarcity × ev 252d
def f48cr_f48_cash_runway_compositescarcity_252d_slope_v149_signal(ncfo, marketcap, fcf, ev):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    base = _mean(burn / runway.replace(0, np.nan).abs(), 252) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of composite scarcity × ev 504d
def f48cr_f48_cash_runway_compositescarcity_504d_slope_v150_signal(ncfo, marketcap, fcf, ev):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    base = _mean(burn / runway.replace(0, np.nan).abs(), 504) * ev
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f48cr_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_CASH_RUNWAY_REGISTRY_SLOPE = REGISTRY


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
    domain_primitives = ("_f48_cash_runway", "_f48_burnyield", "_f48_runway_qtrs")
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
    print(f"OK f48_cash_runway_2nd_derivatives_001_150_claude: {n_features} features pass")
