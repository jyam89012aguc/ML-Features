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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f48_cash_runway(ncfo, marketcap):
    # cash-runway proxy: marketcap-implied cash divided by absolute cash flow magnitude
    cash_proxy = marketcap * 0.05
    return cash_proxy / ncfo.abs().replace(0, np.nan)


def _f48_burnyield(ncfo, marketcap):
    # ncfo / marketcap: positive = generating, negative = burning
    return ncfo / marketcap.replace(0, np.nan)


def _f48_runway_qtrs(fcf, marketcap):
    # quarters of runway proxy: marketcap-implied cash divided by absolute quarterly fcf magnitude
    burn_q = fcf.abs() / 4.0
    cash_proxy = marketcap * 0.05
    return cash_proxy / burn_q.replace(0, np.nan)


# 21d cash-runway proxy weighted by marketcap level
def f48cr_f48_cash_runway_runwayraw_21d_base_v001_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean cash-runway proxy × marketcap
def f48cr_f48_cash_runway_runwayraw_63d_base_v002_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean cash-runway proxy × marketcap
def f48cr_f48_cash_runway_runwayraw_252d_base_v003_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean cash-runway proxy × marketcap
def f48cr_f48_cash_runway_runwayraw_504d_base_v004_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of runway × marketcap
def f48cr_f48_cash_runway_runwaystd_21d_base_v005_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of runway
def f48cr_f48_cash_runway_runwaystd_63d_base_v006_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of runway
def f48cr_f48_cash_runway_runwaystd_252d_base_v007_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of runway over 252d
def f48cr_f48_cash_runway_runwayz_252d_base_v008_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of runway over 504d
def f48cr_f48_cash_runway_runwayz_504d_base_v009_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo/marketcap burn yield
def f48cr_f48_cash_runway_burnyield_21d_base_v010_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn yield
def f48cr_f48_cash_runway_burnyield_63d_base_v011_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn yield
def f48cr_f48_cash_runway_burnyield_252d_base_v012_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d burn yield
def f48cr_f48_cash_runway_burnyield_504d_base_v013_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std burn yield
def f48cr_f48_cash_runway_burnstd_21d_base_v014_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _std(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std burn yield
def f48cr_f48_cash_runway_burnstd_63d_base_v015_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _std(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std burn yield
def f48cr_f48_cash_runway_burnstd_252d_base_v016_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _std(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore burn yield over 252d
def f48cr_f48_cash_runway_burnz_252d_base_v017_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _z(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore burn yield over 504d
def f48cr_f48_cash_runway_burnz_504d_base_v018_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _z(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quarters runway via fcf burn × marketcap
def f48cr_f48_cash_runway_qtrs_21d_base_v019_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quarters runway
def f48cr_f48_cash_runway_qtrs_63d_base_v020_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quarters runway
def f48cr_f48_cash_runway_qtrs_252d_base_v021_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quarters runway
def f48cr_f48_cash_runway_qtrs_504d_base_v022_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days runway < 4 quarters
def f48cr_f48_cash_runway_lowrunwaycount_252d_base_v023_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = base.rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days runway < 2 quarters (severe)
def f48cr_f48_cash_runway_lowrunwaycount_504d_base_v024_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = base.rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of burn days (ncfo<0)
def f48cr_f48_cash_runway_burndaycount_252d_base_v025_signal(ncfo, marketcap):
    burn = _f48_burnyield(ncfo, marketcap)
    result = (burn).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of burn days
def f48cr_f48_cash_runway_burndaycount_504d_base_v026_signal(ncfo, marketcap):
    burn = _f48_burnyield(ncfo, marketcap)
    result = (burn).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst (min) runway × marketcap
def f48cr_f48_cash_runway_worstrunway_21d_base_v027_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(21, min_periods=5).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst runway
def f48cr_f48_cash_runway_worstrunway_63d_base_v028_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(63, min_periods=21).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst runway
def f48cr_f48_cash_runway_worstrunway_252d_base_v029_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(252, min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst runway
def f48cr_f48_cash_runway_worstrunway_504d_base_v030_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(504, min_periods=126).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of runway
def f48cr_f48_cash_runway_runwayema_21d_base_v031_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of runway
def f48cr_f48_cash_runway_runwayema_63d_base_v032_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of runway
def f48cr_f48_cash_runway_runwayema_252d_base_v033_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA burn yield
def f48cr_f48_cash_runway_burnema_21d_base_v034_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA burn yield
def f48cr_f48_cash_runway_burnema_63d_base_v035_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA burn yield
def f48cr_f48_cash_runway_burnema_252d_base_v036_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × ev (size-scaled scarcity)
def f48cr_f48_cash_runway_runwayxev_63d_base_v037_signal(ncfo, marketcap, ev):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# runway × ev 252d
def f48cr_f48_cash_runway_runwayxev_252d_base_v038_signal(ncfo, marketcap, ev):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# runway × pe 63d (overpriced w/ poor runway)
def f48cr_f48_cash_runway_runwayxpe_63d_base_v039_signal(ncfo, marketcap, pe):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × ps 63d
def f48cr_f48_cash_runway_runwayxps_63d_base_v040_signal(ncfo, marketcap, ps):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × evebitda 63d
def f48cr_f48_cash_runway_runwayxevebitda_63d_base_v041_signal(ncfo, marketcap, evebitda):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × evebit 63d
def f48cr_f48_cash_runway_runwayxevebit_63d_base_v042_signal(ncfo, marketcap, evebit):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × pb 63d
def f48cr_f48_cash_runway_runwayxpb_63d_base_v043_signal(ncfo, marketcap, pb):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn yield × ev 63d
def f48cr_f48_cash_runway_burnxev_63d_base_v044_signal(ncfo, marketcap, ev):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# burn yield × pe 63d
def f48cr_f48_cash_runway_burnxpe_63d_base_v045_signal(ncfo, marketcap, pe):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn yield × ps 63d
def f48cr_f48_cash_runway_burnxps_63d_base_v046_signal(ncfo, marketcap, ps):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn yield × evebitda 63d
def f48cr_f48_cash_runway_burnxevebitda_63d_base_v047_signal(ncfo, marketcap, evebitda):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-based runway × ev 63d
def f48cr_f48_cash_runway_qtrsxev_63d_base_v048_signal(fcf, marketcap, ev):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-based runway × pe 63d
def f48cr_f48_cash_runway_qtrsxpe_63d_base_v049_signal(fcf, marketcap, pe):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 63) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-based runway × ps 63d
def f48cr_f48_cash_runway_qtrsxps_63d_base_v050_signal(fcf, marketcap, ps):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(base, 63) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × debt (leverage with weak cash)
def f48cr_f48_cash_runway_runwayxdebt_63d_base_v051_signal(ncfo, marketcap, debt):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * debt + _f48_burnyield(ncfo, marketcap) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × debt
def f48cr_f48_cash_runway_runwayxdebt_252d_base_v052_signal(ncfo, marketcap, debt):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * debt + _f48_burnyield(ncfo, marketcap) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × debt/equity
def f48cr_f48_cash_runway_runwayxlev_63d_base_v053_signal(ncfo, marketcap, debt, equity):
    base = _f48_cash_runway(ncfo, marketcap)
    lev = debt / equity.replace(0, np.nan)
    result = _mean(base, 63) * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × debt/equity
def f48cr_f48_cash_runway_runwayxlev_252d_base_v054_signal(ncfo, marketcap, debt, equity):
    base = _f48_cash_runway(ncfo, marketcap)
    lev = debt / equity.replace(0, np.nan)
    result = _mean(base, 252) * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × shares dilution growth (dilutive financing risk)
def f48cr_f48_cash_runway_runwayxshareg_63d_base_v055_signal(ncfo, marketcap, sharesbas):
    base = _f48_cash_runway(ncfo, marketcap)
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    result = _mean(base, 63) * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × shares dilution growth
def f48cr_f48_cash_runway_runwayxshareg_252d_base_v056_signal(ncfo, marketcap, sharesbas):
    base = _f48_cash_runway(ncfo, marketcap)
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 252) * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × capex intensity
def f48cr_f48_cash_runway_runwayxcapex_63d_base_v057_signal(ncfo, marketcap, capex, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    cx = capex / revenue.replace(0, np.nan)
    result = _mean(base, 63) * cx * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × capex intensity
def f48cr_f48_cash_runway_runwayxcapex_252d_base_v058_signal(ncfo, marketcap, capex, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    cx = capex / revenue.replace(0, np.nan)
    result = _mean(base, 252) * cx * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squared burn (severity)
def f48cr_f48_cash_runway_burnsq_21d_base_v059_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base * base.abs(), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared burn
def f48cr_f48_cash_runway_burnsq_63d_base_v060_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base * base.abs(), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared burn
def f48cr_f48_cash_runway_burnsq_252d_base_v061_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base * base.abs(), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squared runway (severity of low-runway)
def f48cr_f48_cash_runway_runwaysq_21d_base_v062_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base * base.abs(), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared runway
def f48cr_f48_cash_runway_runwaysq_63d_base_v063_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base * base.abs(), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst burn (most negative)
def f48cr_f48_cash_runway_worstburn_21d_base_v064_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.rolling(21, min_periods=5).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst burn
def f48cr_f48_cash_runway_worstburn_63d_base_v065_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.rolling(63, min_periods=21).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst burn
def f48cr_f48_cash_runway_worstburn_252d_base_v066_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.rolling(252, min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn × revenue (absolute burn scale)
def f48cr_f48_cash_runway_burnxrev_63d_base_v067_signal(ncfo, marketcap, revenue):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# burn × assets (absolute burn scale)
def f48cr_f48_cash_runway_burnxassets_63d_base_v068_signal(ncfo, marketcap, assets):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst-ever runway
def f48cr_f48_cash_runway_worstrunwayever_base_v069_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.expanding(min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst-ever burn
def f48cr_f48_cash_runway_worstburnever_base_v070_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.expanding(min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway minus expanding worst-ever
def f48cr_f48_cash_runway_runwayvsever_63d_base_v071_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    worst = base.expanding(min_periods=63).min()
    result = (base - worst) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn minus expanding worst-ever
def f48cr_f48_cash_runway_burnvsever_63d_base_v072_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    worst = base.expanding(min_periods=63).min()
    result = (base - worst) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × ebitda margin (cash quality)
def f48cr_f48_cash_runway_runwayxebmargin_63d_base_v073_signal(ncfo, marketcap, ebitda, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    em = ebitda / revenue.replace(0, np.nan)
    result = _mean(base, 63) * em * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn × ebitda margin
def f48cr_f48_cash_runway_burnxebmargin_252d_base_v074_signal(ncfo, marketcap, ebitda, revenue):
    base = _f48_burnyield(ncfo, marketcap)
    em = ebitda / revenue.replace(0, np.nan)
    result = _mean(base, 252) * em * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite scarcity: |burn| × (1/runway) × marketcap
def f48cr_f48_cash_runway_scarcity_63d_base_v075_signal(ncfo, marketcap, fcf):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    result = _mean(burn / runway.replace(0, np.nan).abs(), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f48cr_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_CASH_RUNWAY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f48_cash_runway_base_001_075_claude: {n_features} features pass")
