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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f46_revenue_housing_proxy(revenue, w):
    # housing cycle proxy = revenue level vs long-horizon mean; positive => above-trend housing demand
    long_mean = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (revenue - long_mean) / long_mean.replace(0, np.nan).abs()


def _f46_demand_seasonality(revenue, w):
    # demand seasonality = std of revenue relative to its rolling mean
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / mn.replace(0, np.nan).abs()


def _f46_housing_signal(revenue, ebitda, w):
    # combine revenue proxy with ebitda momentum to detect housing-cycle health
    long_mean_r = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    rev_proxy = (revenue - long_mean_r) / long_mean_r.replace(0, np.nan).abs()
    long_mean_e = ebitda.rolling(w, min_periods=max(1, w // 2)).mean()
    eb_proxy = (ebitda - long_mean_e) / long_mean_e.replace(0, np.nan).abs()
    return rev_proxy + eb_proxy


# v001: 63d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_63d_base_v001_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 126d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_126d_base_v002_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 252d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_252d_base_v003_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 504d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_504d_base_v004_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 21d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_21d_base_v005_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 42d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_42d_base_v006_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 189d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_189d_base_v007_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 378d revenue housing proxy scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_378d_base_v008_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 63d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_63d_base_v009_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 126d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_126d_base_v010_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 252d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_252d_base_v011_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 504d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_504d_base_v012_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 21d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_21d_base_v013_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 42d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_42d_base_v014_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 189d demand seasonality scaled by closeadj
def f46fhc_f46_furniture_housing_cycle_seas_189d_base_v015_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 63d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_63d_base_v016_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 126d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_126d_base_v017_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 252d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_252d_base_v018_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 504d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_504d_base_v019_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 21d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_21d_base_v020_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 42d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_42d_base_v021_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 189d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_189d_base_v022_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 378d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_378d_base_v023_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: revenue proxy 63d × capex
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_63d_base_v024_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: revenue proxy 126d × capex
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_126d_base_v025_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 126)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: revenue proxy 252d × capex
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_252d_base_v026_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: revenue proxy 504d × capex
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_504d_base_v027_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 504)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 63d z-score of revenue housing proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_63d_base_v028_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 126d z-score of revenue housing proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_126d_base_v029_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 252d z-score of revenue housing proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_252d_base_v030_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 504d z-score of revenue housing proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_504d_base_v031_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 63d rolling mean of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalmean_63d_base_v032_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 126d rolling mean of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalmean_126d_base_v033_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 252d rolling mean of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalmean_252d_base_v034_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 504d rolling mean of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalmean_504d_base_v035_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 63d std of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalstd_63d_base_v036_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 126d std of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalstd_126d_base_v037_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 252d std of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalstd_252d_base_v038_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 504d std of housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalstd_504d_base_v039_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: 63d demand seasonality × ebitda growth × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxebgrow_63d_base_v040_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 63)
    eb_g = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = seas * eb_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 126d demand seasonality × ebitda growth × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxebgrow_126d_base_v041_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 126)
    eb_g = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = seas * eb_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 252d demand seasonality × ebitda growth × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxebgrow_252d_base_v042_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 252)
    eb_g = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = seas * eb_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 504d demand seasonality × ebitda growth × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxebgrow_504d_base_v043_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 504)
    eb_g = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = seas * eb_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 63d housing signal z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_63d_base_v044_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 126d housing signal z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_126d_base_v045_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 252d housing signal z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_252d_base_v046_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 504d housing signal z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_504d_base_v047_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: revenue proxy × seasonality × closeadj (63d)
def f46fhc_f46_furniture_housing_cycle_revxseas_63d_base_v048_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 63)
    seas = _f46_demand_seasonality(revenue, 63)
    result = rp * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: revenue proxy × seasonality × closeadj (126d)
def f46fhc_f46_furniture_housing_cycle_revxseas_126d_base_v049_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 126)
    seas = _f46_demand_seasonality(revenue, 126)
    result = rp * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: revenue proxy × seasonality × closeadj (252d)
def f46fhc_f46_furniture_housing_cycle_revxseas_252d_base_v050_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 252)
    seas = _f46_demand_seasonality(revenue, 252)
    result = rp * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: revenue proxy × seasonality × closeadj (504d)
def f46fhc_f46_furniture_housing_cycle_revxseas_504d_base_v051_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 504)
    seas = _f46_demand_seasonality(revenue, 504)
    result = rp * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 5d revenue proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_5d_base_v052_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 10d revenue proxy × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy_10d_base_v053_signal(revenue, closeadj):
    result = _f46_revenue_housing_proxy(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 5d demand seasonality × closeadj
def f46fhc_f46_furniture_housing_cycle_seas_5d_base_v054_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 10d demand seasonality × closeadj
def f46fhc_f46_furniture_housing_cycle_seas_10d_base_v055_signal(revenue, closeadj):
    result = _f46_demand_seasonality(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 5d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_5d_base_v056_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 10d housing signal × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal_10d_base_v057_signal(revenue, ebitda, closeadj):
    result = _f46_housing_signal(revenue, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: revenue proxy 63d × log closeadj
def f46fhc_f46_furniture_housing_cycle_revproxylogp_63d_base_v058_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v059: revenue proxy 252d × log closeadj
def f46fhc_f46_furniture_housing_cycle_revproxylogp_252d_base_v059_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 63d housing signal × log closeadj
def f46fhc_f46_furniture_housing_cycle_hsignallogp_63d_base_v060_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 252d housing signal × log closeadj
def f46fhc_f46_furniture_housing_cycle_hsignallogp_252d_base_v061_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v062: revenue proxy 21d × capex ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_21d_base_v062_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 21)
    result = base * capex / _mean(capex, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: revenue proxy 42d × capex ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_42d_base_v063_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 42)
    result = base * capex / _mean(capex, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: revenue proxy 189d × capex ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_189d_base_v064_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 189)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: revenue proxy 378d × capex ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcapex_378d_base_v065_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 378)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: housing signal × capex / mean capex 63d
def f46fhc_f46_furniture_housing_cycle_hsxcapex_63d_base_v066_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: housing signal × capex 126d
def f46fhc_f46_furniture_housing_cycle_hsxcapex_126d_base_v067_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 126)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: housing signal × capex 252d
def f46fhc_f46_furniture_housing_cycle_hsxcapex_252d_base_v068_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: housing signal × capex 504d
def f46fhc_f46_furniture_housing_cycle_hsxcapex_504d_base_v069_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    result = base * capex / _mean(capex, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d seasonality × closeadj squared
def f46fhc_f46_furniture_housing_cycle_seasxp2_63d_base_v070_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 252d seasonality × closeadj squared
def f46fhc_f46_furniture_housing_cycle_seasxp2_252d_base_v071_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 252)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v072: revenue proxy 63d × ebitda / revenue
def f46fhc_f46_furniture_housing_cycle_revproxyxebmar_63d_base_v072_signal(revenue, ebitda, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: revenue proxy 252d × ebitda / revenue
def f46fhc_f46_furniture_housing_cycle_revproxyxebmar_252d_base_v073_signal(revenue, ebitda, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: revenue proxy 504d × ebitda / revenue
def f46fhc_f46_furniture_housing_cycle_revproxyxebmar_504d_base_v074_signal(revenue, ebitda, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 504)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: housing signal 63d × ebitda / revenue × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxebmar_63d_base_v075_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46fhc_f46_furniture_housing_cycle_revproxy_63d_base_v001_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_126d_base_v002_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_252d_base_v003_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_504d_base_v004_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_21d_base_v005_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_42d_base_v006_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_189d_base_v007_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_378d_base_v008_signal,
    f46fhc_f46_furniture_housing_cycle_seas_63d_base_v009_signal,
    f46fhc_f46_furniture_housing_cycle_seas_126d_base_v010_signal,
    f46fhc_f46_furniture_housing_cycle_seas_252d_base_v011_signal,
    f46fhc_f46_furniture_housing_cycle_seas_504d_base_v012_signal,
    f46fhc_f46_furniture_housing_cycle_seas_21d_base_v013_signal,
    f46fhc_f46_furniture_housing_cycle_seas_42d_base_v014_signal,
    f46fhc_f46_furniture_housing_cycle_seas_189d_base_v015_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_63d_base_v016_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_126d_base_v017_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_252d_base_v018_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_504d_base_v019_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_21d_base_v020_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_42d_base_v021_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_189d_base_v022_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_378d_base_v023_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_63d_base_v024_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_126d_base_v025_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_252d_base_v026_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_504d_base_v027_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_63d_base_v028_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_126d_base_v029_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_252d_base_v030_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_504d_base_v031_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalmean_63d_base_v032_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalmean_126d_base_v033_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalmean_252d_base_v034_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalmean_504d_base_v035_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalstd_63d_base_v036_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalstd_126d_base_v037_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalstd_252d_base_v038_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalstd_504d_base_v039_signal,
    f46fhc_f46_furniture_housing_cycle_seasxebgrow_63d_base_v040_signal,
    f46fhc_f46_furniture_housing_cycle_seasxebgrow_126d_base_v041_signal,
    f46fhc_f46_furniture_housing_cycle_seasxebgrow_252d_base_v042_signal,
    f46fhc_f46_furniture_housing_cycle_seasxebgrow_504d_base_v043_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_63d_base_v044_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_126d_base_v045_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_252d_base_v046_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_504d_base_v047_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas_63d_base_v048_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas_126d_base_v049_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas_252d_base_v050_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas_504d_base_v051_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_5d_base_v052_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy_10d_base_v053_signal,
    f46fhc_f46_furniture_housing_cycle_seas_5d_base_v054_signal,
    f46fhc_f46_furniture_housing_cycle_seas_10d_base_v055_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_5d_base_v056_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal_10d_base_v057_signal,
    f46fhc_f46_furniture_housing_cycle_revproxylogp_63d_base_v058_signal,
    f46fhc_f46_furniture_housing_cycle_revproxylogp_252d_base_v059_signal,
    f46fhc_f46_furniture_housing_cycle_hsignallogp_63d_base_v060_signal,
    f46fhc_f46_furniture_housing_cycle_hsignallogp_252d_base_v061_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_21d_base_v062_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_42d_base_v063_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_189d_base_v064_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapex_378d_base_v065_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapex_63d_base_v066_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapex_126d_base_v067_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapex_252d_base_v068_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapex_504d_base_v069_signal,
    f46fhc_f46_furniture_housing_cycle_seasxp2_63d_base_v070_signal,
    f46fhc_f46_furniture_housing_cycle_seasxp2_252d_base_v071_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxebmar_63d_base_v072_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxebmar_252d_base_v073_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxebmar_504d_base_v074_signal,
    f46fhc_f46_furniture_housing_cycle_hsxebmar_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_FURNITURE_HOUSING_CYCLE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_revenue_housing_proxy", "_f46_demand_seasonality", "_f46_housing_signal")
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
    print(f"OK f46_furniture_housing_cycle_base_001_075_claude: {n_features} features pass")
