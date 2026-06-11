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
def _f26_housing_cycle_proxy(revenue, w):
    # cyclic proxy: rolling growth minus longer-window mean growth -> cycle position
    growth = revenue.pct_change(periods=w)
    long_growth = growth.rolling(max(2 * w, 21), min_periods=max(1, w // 2)).mean()
    return growth - long_growth


def _f26_demand_seasonality(revenue, w):
    # seasonality proxy: deviation of revenue from its trailing-year mean, normalized
    annual = revenue.rolling(252, min_periods=63).mean()
    dev = (revenue - annual) / annual.replace(0, np.nan).abs()
    return dev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_housing_growth_signal(revenue, ebitda, w):
    # combined revenue & ebitda growth amplitude, housing-driven
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) / 2.0


# v001 21d housing cycle proxy × close
def f26bph_f26_building_products_housing_cycle_21d_base_v001_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002 63d cycle proxy × close
def f26bph_f26_building_products_housing_cycle_63d_base_v002_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003 126d cycle proxy × close
def f26bph_f26_building_products_housing_cycle_126d_base_v003_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004 252d cycle proxy × close
def f26bph_f26_building_products_housing_cycle_252d_base_v004_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005 5d cycle proxy × close
def f26bph_f26_building_products_housing_cycle_5d_base_v005_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006 42d cycle proxy × close
def f26bph_f26_building_products_housing_cycle_42d_base_v006_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007 cycle proxy × closeadj squared
def f26bph_f26_building_products_housing_cycle_63d_sq_base_v007_signal(revenue, closeadj):
    p = _f26_housing_cycle_proxy(revenue, 63)
    result = p * closeadj * closeadj.abs().pow(0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008 21d seasonality × close
def f26bph_f26_building_products_housing_season_21d_base_v008_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009 63d seasonality × close
def f26bph_f26_building_products_housing_season_63d_base_v009_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010 126d seasonality × close
def f26bph_f26_building_products_housing_season_126d_base_v010_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011 252d seasonality × close
def f26bph_f26_building_products_housing_season_252d_base_v011_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012 5d seasonality × close
def f26bph_f26_building_products_housing_season_5d_base_v012_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013 21d housing growth signal × close
def f26bph_f26_building_products_housing_growth_21d_base_v013_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014 63d housing growth signal × close
def f26bph_f26_building_products_housing_growth_63d_base_v014_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015 126d housing growth signal × close
def f26bph_f26_building_products_housing_growth_126d_base_v015_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016 252d housing growth signal × close
def f26bph_f26_building_products_housing_growth_252d_base_v016_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017 5d housing growth signal × close
def f26bph_f26_building_products_housing_growth_5d_base_v017_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018 housing growth - cycle composite
def f26bph_f26_building_products_housing_compo_63d_base_v018_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = (c + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019 composite 252d
def f26bph_f26_building_products_housing_compo_252d_base_v019_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = (c + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020 cycle - season composite
def f26bph_f26_building_products_housing_cyseason_63d_base_v020_signal(revenue, closeadj):
    a = _f26_housing_cycle_proxy(revenue, 63)
    b = _f26_demand_seasonality(revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021 cycle × season
def f26bph_f26_building_products_housing_cyseason_252d_base_v021_signal(revenue, closeadj):
    a = _f26_housing_cycle_proxy(revenue, 252)
    b = _f26_demand_seasonality(revenue, 252)
    result = a * b * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022 rolling mean of cycle proxy 63d over 21d × close
def f26bph_f26_building_products_housing_cyclema_63d_base_v022_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023 rolling mean of cycle proxy 252d over 63d × close
def f26bph_f26_building_products_housing_cyclema_252d_base_v023_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024 rolling std of cycle proxy 63d × close
def f26bph_f26_building_products_housing_cyclestd_63d_base_v024_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025 rolling std of cycle proxy 252d × close
def f26bph_f26_building_products_housing_cyclestd_252d_base_v025_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026 z-score cycle 63d/252d
def f26bph_f26_building_products_housing_cyclez_63d_base_v026_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027 z-score cycle 252d/504d
def f26bph_f26_building_products_housing_cyclez_252d_base_v027_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028 rolling mean of seasonality 21d × close
def f26bph_f26_building_products_housing_seasonma_21d_base_v028_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029 rolling mean of seasonality 126d × close
def f26bph_f26_building_products_housing_seasonma_126d_base_v029_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030 rolling std seasonality 252d × close
def f26bph_f26_building_products_housing_seasonstd_252d_base_v030_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031 z-score seasonality 63d/252d
def f26bph_f26_building_products_housing_seasonz_63d_base_v031_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032 z-score seasonality 252d/504d
def f26bph_f26_building_products_housing_seasonz_252d_base_v032_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033 housing growth mean 63d × close
def f26bph_f26_building_products_housing_growthma_63d_base_v033_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034 housing growth std 252d × close
def f26bph_f26_building_products_housing_growthstd_252d_base_v034_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035 housing growth z 63d
def f26bph_f26_building_products_housing_growthz_63d_base_v035_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036 housing growth z 252d
def f26bph_f26_building_products_housing_growthz_252d_base_v036_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037 cycle × capex (sensitivity)
def f26bph_f26_building_products_housing_cyclexcapex_63d_base_v037_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * capex / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038 cycle × capex 252d
def f26bph_f26_building_products_housing_cyclexcapex_252d_base_v038_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * capex / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039 cycle × ebitda margin
def f26bph_f26_building_products_housing_cyclexebitda_63d_base_v039_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * (ebitda / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040 cycle × ebitda margin 252d
def f26bph_f26_building_products_housing_cyclexebitda_252d_base_v040_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * (ebitda / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041 seasonality × capex
def f26bph_f26_building_products_housing_seasonxcapex_63d_base_v041_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base * capex / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042 seasonality × capex 252d
def f26bph_f26_building_products_housing_seasonxcapex_252d_base_v042_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = base * capex / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043 cycle x close growth proxy
def f26bph_f26_building_products_housing_cyclexpx_63d_base_v043_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    px_chg = closeadj.pct_change(63)
    result = base * px_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044 cycle x px 252d
def f26bph_f26_building_products_housing_cyclexpx_252d_base_v044_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    px_chg = closeadj.pct_change(252)
    result = base * px_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045 cycle × log close
def f26bph_f26_building_products_housing_cyclelogpx_63d_base_v045_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046 cycle × log close 252d
def f26bph_f26_building_products_housing_cyclelogpx_252d_base_v046_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047 seasonality × log close
def f26bph_f26_building_products_housing_seasonlogpx_63d_base_v047_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048 housing growth × log close
def f26bph_f26_building_products_housing_growthlogpx_63d_base_v048_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049 cycle magnitude (abs) × close
def f26bph_f26_building_products_housing_cycleabs_63d_base_v049_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050 cycle magnitude × close 252d
def f26bph_f26_building_products_housing_cycleabs_252d_base_v050_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051 seasonality abs × close
def f26bph_f26_building_products_housing_seasonabs_63d_base_v051_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052 housing growth sq × close
def f26bph_f26_building_products_housing_growthsq_63d_base_v052_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053 cycle quantile rank × close
def f26bph_f26_building_products_housing_cyclerank_252d_base_v053_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054 seasonality quantile rank × close
def f26bph_f26_building_products_housing_seasonrank_252d_base_v054_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055 housing growth quantile rank × close
def f26bph_f26_building_products_housing_growthrank_252d_base_v055_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056 housing growth × capex z
def f26bph_f26_building_products_housing_growthxcapexz_63d_base_v056_signal(revenue, ebitda, capex, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base * _z(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057 cycle × capex zscore 252d
def f26bph_f26_building_products_housing_cyclexcapexz_252d_base_v057_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * _z(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058 seasonality × ebitda margin × close
def f26bph_f26_building_products_housing_seasonxebmgn_63d_base_v058_signal(revenue, ebitda, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    em = ebitda / revenue.replace(0, np.nan)
    result = base * em * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059 cycle ratio close 252d
def f26bph_f26_building_products_housing_cyclexclose_5d_base_v059_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 5)
    result = base * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v060 cycle × capex level
def f26bph_f26_building_products_housing_cyclexcapexlvl_63d_base_v060_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * _mean(capex, 63) / _mean(revenue, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061 cycle minus seasonality × close
def f26bph_f26_building_products_housing_cyminussns_21d_base_v061_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 21)
    s = _f26_demand_seasonality(revenue, 21)
    result = (c - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062 cycle minus seasonality 126d × close
def f26bph_f26_building_products_housing_cyminussns_126d_base_v062_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 126)
    s = _f26_demand_seasonality(revenue, 126)
    result = (c - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063 cycle + growth weighted
def f26bph_f26_building_products_housing_cycplusg_63d_base_v063_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = (0.6 * c + 0.4 * g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064 cycle + growth weighted 252d
def f26bph_f26_building_products_housing_cycplusg_252d_base_v064_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = (0.6 * c + 0.4 * g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065 cycle EMA × close
def f26bph_f26_building_products_housing_cyclema_ema21_base_v065_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066 cycle EMA 63 × close
def f26bph_f26_building_products_housing_cyclema_ema63_base_v066_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067 seasonality EMA × close
def f26bph_f26_building_products_housing_seasonema_21d_base_v067_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068 housing growth EMA × close
def f26bph_f26_building_products_housing_growthema_21d_base_v068_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069 cycle scaled by ebitda / close
def f26bph_f26_building_products_housing_cyclevsebitda_63d_base_v069_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base / (ebitda / revenue.replace(0, np.nan)).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070 cycle × revenue level / close
def f26bph_f26_building_products_housing_cyclexrev_63d_base_v070_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071 seasonality × revenue change × close
def f26bph_f26_building_products_housing_seasonxrev_63d_base_v071_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    rev_chg = revenue.pct_change(21)
    result = base * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072 cycle slope-like (diff(63))
def f26bph_f26_building_products_housing_cyclediff_63d_base_v072_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073 cycle diff 252d
def f26bph_f26_building_products_housing_cyclediff_252d_base_v073_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074 cycle x volume z scaled
def f26bph_f26_building_products_housing_cyclexvol_63d_base_v074_signal(revenue, volume, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075 housing growth × volume z 252d
def f26bph_f26_building_products_housing_growthxvol_252d_base_v075_signal(revenue, ebitda, volume, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26bph_f26_building_products_housing_cycle_21d_base_v001_signal,
    f26bph_f26_building_products_housing_cycle_63d_base_v002_signal,
    f26bph_f26_building_products_housing_cycle_126d_base_v003_signal,
    f26bph_f26_building_products_housing_cycle_252d_base_v004_signal,
    f26bph_f26_building_products_housing_cycle_5d_base_v005_signal,
    f26bph_f26_building_products_housing_cycle_42d_base_v006_signal,
    f26bph_f26_building_products_housing_cycle_63d_sq_base_v007_signal,
    f26bph_f26_building_products_housing_season_21d_base_v008_signal,
    f26bph_f26_building_products_housing_season_63d_base_v009_signal,
    f26bph_f26_building_products_housing_season_126d_base_v010_signal,
    f26bph_f26_building_products_housing_season_252d_base_v011_signal,
    f26bph_f26_building_products_housing_season_5d_base_v012_signal,
    f26bph_f26_building_products_housing_growth_21d_base_v013_signal,
    f26bph_f26_building_products_housing_growth_63d_base_v014_signal,
    f26bph_f26_building_products_housing_growth_126d_base_v015_signal,
    f26bph_f26_building_products_housing_growth_252d_base_v016_signal,
    f26bph_f26_building_products_housing_growth_5d_base_v017_signal,
    f26bph_f26_building_products_housing_compo_63d_base_v018_signal,
    f26bph_f26_building_products_housing_compo_252d_base_v019_signal,
    f26bph_f26_building_products_housing_cyseason_63d_base_v020_signal,
    f26bph_f26_building_products_housing_cyseason_252d_base_v021_signal,
    f26bph_f26_building_products_housing_cyclema_63d_base_v022_signal,
    f26bph_f26_building_products_housing_cyclema_252d_base_v023_signal,
    f26bph_f26_building_products_housing_cyclestd_63d_base_v024_signal,
    f26bph_f26_building_products_housing_cyclestd_252d_base_v025_signal,
    f26bph_f26_building_products_housing_cyclez_63d_base_v026_signal,
    f26bph_f26_building_products_housing_cyclez_252d_base_v027_signal,
    f26bph_f26_building_products_housing_seasonma_21d_base_v028_signal,
    f26bph_f26_building_products_housing_seasonma_126d_base_v029_signal,
    f26bph_f26_building_products_housing_seasonstd_252d_base_v030_signal,
    f26bph_f26_building_products_housing_seasonz_63d_base_v031_signal,
    f26bph_f26_building_products_housing_seasonz_252d_base_v032_signal,
    f26bph_f26_building_products_housing_growthma_63d_base_v033_signal,
    f26bph_f26_building_products_housing_growthstd_252d_base_v034_signal,
    f26bph_f26_building_products_housing_growthz_63d_base_v035_signal,
    f26bph_f26_building_products_housing_growthz_252d_base_v036_signal,
    f26bph_f26_building_products_housing_cyclexcapex_63d_base_v037_signal,
    f26bph_f26_building_products_housing_cyclexcapex_252d_base_v038_signal,
    f26bph_f26_building_products_housing_cyclexebitda_63d_base_v039_signal,
    f26bph_f26_building_products_housing_cyclexebitda_252d_base_v040_signal,
    f26bph_f26_building_products_housing_seasonxcapex_63d_base_v041_signal,
    f26bph_f26_building_products_housing_seasonxcapex_252d_base_v042_signal,
    f26bph_f26_building_products_housing_cyclexpx_63d_base_v043_signal,
    f26bph_f26_building_products_housing_cyclexpx_252d_base_v044_signal,
    f26bph_f26_building_products_housing_cyclelogpx_63d_base_v045_signal,
    f26bph_f26_building_products_housing_cyclelogpx_252d_base_v046_signal,
    f26bph_f26_building_products_housing_seasonlogpx_63d_base_v047_signal,
    f26bph_f26_building_products_housing_growthlogpx_63d_base_v048_signal,
    f26bph_f26_building_products_housing_cycleabs_63d_base_v049_signal,
    f26bph_f26_building_products_housing_cycleabs_252d_base_v050_signal,
    f26bph_f26_building_products_housing_seasonabs_63d_base_v051_signal,
    f26bph_f26_building_products_housing_growthsq_63d_base_v052_signal,
    f26bph_f26_building_products_housing_cyclerank_252d_base_v053_signal,
    f26bph_f26_building_products_housing_seasonrank_252d_base_v054_signal,
    f26bph_f26_building_products_housing_growthrank_252d_base_v055_signal,
    f26bph_f26_building_products_housing_growthxcapexz_63d_base_v056_signal,
    f26bph_f26_building_products_housing_cyclexcapexz_252d_base_v057_signal,
    f26bph_f26_building_products_housing_seasonxebmgn_63d_base_v058_signal,
    f26bph_f26_building_products_housing_cyclexclose_5d_base_v059_signal,
    f26bph_f26_building_products_housing_cyclexcapexlvl_63d_base_v060_signal,
    f26bph_f26_building_products_housing_cyminussns_21d_base_v061_signal,
    f26bph_f26_building_products_housing_cyminussns_126d_base_v062_signal,
    f26bph_f26_building_products_housing_cycplusg_63d_base_v063_signal,
    f26bph_f26_building_products_housing_cycplusg_252d_base_v064_signal,
    f26bph_f26_building_products_housing_cyclema_ema21_base_v065_signal,
    f26bph_f26_building_products_housing_cyclema_ema63_base_v066_signal,
    f26bph_f26_building_products_housing_seasonema_21d_base_v067_signal,
    f26bph_f26_building_products_housing_growthema_21d_base_v068_signal,
    f26bph_f26_building_products_housing_cyclevsebitda_63d_base_v069_signal,
    f26bph_f26_building_products_housing_cyclexrev_63d_base_v070_signal,
    f26bph_f26_building_products_housing_seasonxrev_63d_base_v071_signal,
    f26bph_f26_building_products_housing_cyclediff_63d_base_v072_signal,
    f26bph_f26_building_products_housing_cyclediff_252d_base_v073_signal,
    f26bph_f26_building_products_housing_cyclexvol_63d_base_v074_signal,
    f26bph_f26_building_products_housing_growthxvol_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_BUILDING_PRODUCTS_HOUSING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "capex": capex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_housing_cycle_proxy", "_f26_demand_seasonality", "_f26_housing_growth_signal")
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
    print(f"OK f26_building_products_housing_base_001_075_claude: {n_features} features pass")
