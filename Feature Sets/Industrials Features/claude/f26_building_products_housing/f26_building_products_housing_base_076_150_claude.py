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
    growth = revenue.pct_change(periods=w)
    long_growth = growth.rolling(max(2 * w, 21), min_periods=max(1, w // 2)).mean()
    return growth - long_growth


def _f26_demand_seasonality(revenue, w):
    annual = revenue.rolling(252, min_periods=63).mean()
    dev = (revenue - annual) / annual.replace(0, np.nan).abs()
    return dev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_housing_growth_signal(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) / 2.0


# v076 cycle 10d × close
def f26bph_f26_building_products_housing_cycle_10d_base_v076_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077 cycle 189d × close
def f26bph_f26_building_products_housing_cycle_189d_base_v077_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078 cycle 378d × close
def f26bph_f26_building_products_housing_cycle_378d_base_v078_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079 cycle 504d × close
def f26bph_f26_building_products_housing_cycle_504d_base_v079_signal(revenue, closeadj):
    result = _f26_housing_cycle_proxy(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080 seasonality 10d × close
def f26bph_f26_building_products_housing_season_10d_base_v080_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081 seasonality 42d × close
def f26bph_f26_building_products_housing_season_42d_base_v081_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082 seasonality 189d × close
def f26bph_f26_building_products_housing_season_189d_base_v082_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083 seasonality 378d × close
def f26bph_f26_building_products_housing_season_378d_base_v083_signal(revenue, closeadj):
    result = _f26_demand_seasonality(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084 growth 10d × close
def f26bph_f26_building_products_housing_growth_10d_base_v084_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085 growth 42d × close
def f26bph_f26_building_products_housing_growth_42d_base_v085_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086 growth 189d × close
def f26bph_f26_building_products_housing_growth_189d_base_v086_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087 growth 378d × close
def f26bph_f26_building_products_housing_growth_378d_base_v087_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088 growth 504d × close
def f26bph_f26_building_products_housing_growth_504d_base_v088_signal(revenue, ebitda, closeadj):
    result = _f26_housing_growth_signal(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089 cycle EMA 126 × close
def f26bph_f26_building_products_housing_cyclema_ema126_base_v089_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090 cycle EMA 252 × close
def f26bph_f26_building_products_housing_cyclema_ema252_base_v090_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091 seasonality EMA 63
def f26bph_f26_building_products_housing_seasonema_63d_base_v091_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092 seasonality EMA 126
def f26bph_f26_building_products_housing_seasonema_126d_base_v092_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 126)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093 growth EMA 63
def f26bph_f26_building_products_housing_growthema_63d_base_v093_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094 growth EMA 126
def f26bph_f26_building_products_housing_growthema_126d_base_v094_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 126)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095 cycle / volatility scaled
def f26bph_f26_building_products_housing_cyclevsstd_63d_base_v095_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    sd = _std(closeadj, 63)
    result = base * closeadj / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v096 cycle / volatility scaled 252
def f26bph_f26_building_products_housing_cyclevsstd_252d_base_v096_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    sd = _std(closeadj, 252)
    result = base * closeadj / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v097 cycle * dollar volume mean 21d
def f26bph_f26_building_products_housing_cyclexdv_63d_base_v097_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v098 cycle * dollar volume mean 63d
def f26bph_f26_building_products_housing_cyclexdv_252d_base_v098_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v099 seasonality * dollar volume mean
def f26bph_f26_building_products_housing_seasonxdv_63d_base_v099_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_demand_seasonality(revenue, 63)
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v100 growth * dollar volume mean
def f26bph_f26_building_products_housing_growthxdv_252d_base_v100_signal(revenue, ebitda, volume, closeadj):
    dv = closeadj * volume
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v101 cycle × close minus mean (centered)
def f26bph_f26_building_products_housing_cyclexpxgap_252d_base_v101_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    px_gap = closeadj - _mean(closeadj, 252)
    result = base * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


# v102 seasonality × close gap 63d
def f26bph_f26_building_products_housing_seasonxpxgap_63d_base_v102_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    px_gap = closeadj - _mean(closeadj, 63)
    result = base * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


# v103 growth × close gap 252d
def f26bph_f26_building_products_housing_growthxpxgap_252d_base_v103_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    px_gap = closeadj - _mean(closeadj, 252)
    result = base * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


# v104 cycle × capex per revenue z 63d
def f26bph_f26_building_products_housing_cyclexcaprev_63d_base_v104_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    capr = _safe_div(capex, revenue)
    result = base * _z(capr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105 seasonality × capex per revenue z 252d
def f26bph_f26_building_products_housing_seasonxcaprev_252d_base_v105_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    capr = _safe_div(capex, revenue)
    result = base * _z(capr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106 growth × capex per revenue z 63d
def f26bph_f26_building_products_housing_growthxcaprev_63d_base_v106_signal(revenue, ebitda, capex, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    capr = _safe_div(capex, revenue)
    result = base * _z(capr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107 cycle minus 1y mean × close
def f26bph_f26_building_products_housing_cycledev_252d_base_v107_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108 seasonality minus 1y mean × close
def f26bph_f26_building_products_housing_seasondev_252d_base_v108_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109 growth minus 1y mean × close
def f26bph_f26_building_products_housing_growthdev_252d_base_v109_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110 cycle sign × close × volume z
def f26bph_f26_building_products_housing_cyclesignxvol_63d_base_v110_signal(revenue, volume, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    sg = np.sign(base)
    result = sg * closeadj * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v111 cycle × close × capex sign
def f26bph_f26_building_products_housing_cyclexcapsign_63d_base_v111_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    cap_sign = np.sign(capex.diff(63))
    result = base * cap_sign * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112 cycle * (1 + revenue growth)
def f26bph_f26_building_products_housing_cyclexrevg_63d_base_v112_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    rg = revenue.pct_change(63)
    result = base * (1.0 + rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113 seasonality * (1+revenue growth)
def f26bph_f26_building_products_housing_seasonxrevg_252d_base_v113_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    rg = revenue.pct_change(252)
    result = base * (1.0 + rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114 growth × revenue/ebitda mix
def f26bph_f26_building_products_housing_growthxratio_63d_base_v114_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    rat = _safe_div(ebitda, revenue)
    result = base * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115 cycle × revenue/ebitda mix
def f26bph_f26_building_products_housing_cyclexratio_252d_base_v115_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    rat = _safe_div(ebitda, revenue)
    result = base * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116 cycle squared × close
def f26bph_f26_building_products_housing_cyclesq_63d_base_v116_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117 cycle squared × close 252d
def f26bph_f26_building_products_housing_cyclesq_252d_base_v117_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118 seasonality squared × close
def f26bph_f26_building_products_housing_seasonsq_63d_base_v118_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119 seasonality squared 252
def f26bph_f26_building_products_housing_seasonsq_252d_base_v119_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120 growth squared 252
def f26bph_f26_building_products_housing_growthsq_252d_base_v120_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121 cycle × seasonality × close 252d
def f26bph_f26_building_products_housing_cyclexseason_252d_base_v121_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    result = c * s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122 cycle × growth × close 252d
def f26bph_f26_building_products_housing_cyclexgrowth_252d_base_v122_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = c * g * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123 seasonality × growth × close 252d
def f26bph_f26_building_products_housing_seasonxgrowth_252d_base_v123_signal(revenue, ebitda, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = s * g * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124 cycle quantile rank 504
def f26bph_f26_building_products_housing_cyclerank_504d_base_v124_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125 seasonality quantile rank 504
def f26bph_f26_building_products_housing_seasonrank_504d_base_v125_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126 growth quantile rank 504
def f26bph_f26_building_products_housing_growthrank_504d_base_v126_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127 cycle * close drawdown (peak gap)
def f26bph_f26_building_products_housing_cyclexpkgap_252d_base_v127_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = base * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128 seasonality * close drawdown
def f26bph_f26_building_products_housing_seasonxpkgap_252d_base_v128_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = base * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129 growth × peak gap
def f26bph_f26_building_products_housing_growthxpkgap_252d_base_v129_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = base * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130 cycle × ebitda 63
def f26bph_f26_building_products_housing_cyclexebitval_63d_base_v130_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131 cycle × log ebitda 252
def f26bph_f26_building_products_housing_cyclexebitval_252d_base_v131_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132 seasonality × log ebitda
def f26bph_f26_building_products_housing_seasonxebitval_63d_base_v132_signal(revenue, ebitda, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133 growth × log capex
def f26bph_f26_building_products_housing_growthxlogcap_63d_base_v133_signal(revenue, ebitda, capex, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    result = base * np.log(capex.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134 cycle × log capex
def f26bph_f26_building_products_housing_cyclexlogcap_252d_base_v134_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * np.log(capex.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135 seasonality × log capex
def f26bph_f26_building_products_housing_seasonxlogcap_252d_base_v135_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = base * np.log(capex.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136 cycle × ebitda growth 63
def f26bph_f26_building_products_housing_cyclexebitg_63d_base_v136_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    eg = ebitda.pct_change(63)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137 cycle × ebitda growth 252
def f26bph_f26_building_products_housing_cyclexebitg_252d_base_v137_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    eg = ebitda.pct_change(252)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138 seasonality × ebitda growth
def f26bph_f26_building_products_housing_seasonxebitg_252d_base_v138_signal(revenue, ebitda, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    eg = ebitda.pct_change(252)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139 growth × revenue growth
def f26bph_f26_building_products_housing_growthxrevg_63d_base_v139_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63)
    rg = revenue.pct_change(63)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140 cycle * vol z 252
def f26bph_f26_building_products_housing_cyclexvolz_252d_base_v140_signal(revenue, volume, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141 seasonality * vol z 252
def f26bph_f26_building_products_housing_seasonxvolz_252d_base_v141_signal(revenue, volume, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142 cycle × close std × close (volatility amplification)
def f26bph_f26_building_products_housing_cyclexvolclose_63d_base_v142_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63)
    result = base * _std(closeadj, 63) * np.sign(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# v143 cycle * close detrended
def f26bph_f26_building_products_housing_cyclexpxdet_252d_base_v143_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = base * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144 seasonality * close detrended
def f26bph_f26_building_products_housing_seasonxpxdet_252d_base_v144_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252)
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = base * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145 growth * close detrended
def f26bph_f26_building_products_housing_growthxpxdet_252d_base_v145_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252)
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = base * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146 cycle × close range
def f26bph_f26_building_products_housing_cyclexrange_252d_base_v146_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = base * rng
    return result.replace([np.inf, -np.inf], np.nan)


# v147 seasonality × close range 63
def f26bph_f26_building_products_housing_seasonxrange_63d_base_v147_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63)
    rng = closeadj.rolling(63, min_periods=21).max() - closeadj.rolling(63, min_periods=21).min()
    result = base * rng
    return result.replace([np.inf, -np.inf], np.nan)


# v148 cycle × cum revenue trend
def f26bph_f26_building_products_housing_cyclexlogrev_252d_base_v148_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149 composite cycle/seasonality/growth × close
def f26bph_f26_building_products_housing_compo3_252d_base_v149_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = (c + s + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150 composite weighted × close
def f26bph_f26_building_products_housing_compow_252d_base_v150_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    result = (0.5 * c + 0.3 * s + 0.2 * g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26bph_f26_building_products_housing_cycle_10d_base_v076_signal,
    f26bph_f26_building_products_housing_cycle_189d_base_v077_signal,
    f26bph_f26_building_products_housing_cycle_378d_base_v078_signal,
    f26bph_f26_building_products_housing_cycle_504d_base_v079_signal,
    f26bph_f26_building_products_housing_season_10d_base_v080_signal,
    f26bph_f26_building_products_housing_season_42d_base_v081_signal,
    f26bph_f26_building_products_housing_season_189d_base_v082_signal,
    f26bph_f26_building_products_housing_season_378d_base_v083_signal,
    f26bph_f26_building_products_housing_growth_10d_base_v084_signal,
    f26bph_f26_building_products_housing_growth_42d_base_v085_signal,
    f26bph_f26_building_products_housing_growth_189d_base_v086_signal,
    f26bph_f26_building_products_housing_growth_378d_base_v087_signal,
    f26bph_f26_building_products_housing_growth_504d_base_v088_signal,
    f26bph_f26_building_products_housing_cyclema_ema126_base_v089_signal,
    f26bph_f26_building_products_housing_cyclema_ema252_base_v090_signal,
    f26bph_f26_building_products_housing_seasonema_63d_base_v091_signal,
    f26bph_f26_building_products_housing_seasonema_126d_base_v092_signal,
    f26bph_f26_building_products_housing_growthema_63d_base_v093_signal,
    f26bph_f26_building_products_housing_growthema_126d_base_v094_signal,
    f26bph_f26_building_products_housing_cyclevsstd_63d_base_v095_signal,
    f26bph_f26_building_products_housing_cyclevsstd_252d_base_v096_signal,
    f26bph_f26_building_products_housing_cyclexdv_63d_base_v097_signal,
    f26bph_f26_building_products_housing_cyclexdv_252d_base_v098_signal,
    f26bph_f26_building_products_housing_seasonxdv_63d_base_v099_signal,
    f26bph_f26_building_products_housing_growthxdv_252d_base_v100_signal,
    f26bph_f26_building_products_housing_cyclexpxgap_252d_base_v101_signal,
    f26bph_f26_building_products_housing_seasonxpxgap_63d_base_v102_signal,
    f26bph_f26_building_products_housing_growthxpxgap_252d_base_v103_signal,
    f26bph_f26_building_products_housing_cyclexcaprev_63d_base_v104_signal,
    f26bph_f26_building_products_housing_seasonxcaprev_252d_base_v105_signal,
    f26bph_f26_building_products_housing_growthxcaprev_63d_base_v106_signal,
    f26bph_f26_building_products_housing_cycledev_252d_base_v107_signal,
    f26bph_f26_building_products_housing_seasondev_252d_base_v108_signal,
    f26bph_f26_building_products_housing_growthdev_252d_base_v109_signal,
    f26bph_f26_building_products_housing_cyclesignxvol_63d_base_v110_signal,
    f26bph_f26_building_products_housing_cyclexcapsign_63d_base_v111_signal,
    f26bph_f26_building_products_housing_cyclexrevg_63d_base_v112_signal,
    f26bph_f26_building_products_housing_seasonxrevg_252d_base_v113_signal,
    f26bph_f26_building_products_housing_growthxratio_63d_base_v114_signal,
    f26bph_f26_building_products_housing_cyclexratio_252d_base_v115_signal,
    f26bph_f26_building_products_housing_cyclesq_63d_base_v116_signal,
    f26bph_f26_building_products_housing_cyclesq_252d_base_v117_signal,
    f26bph_f26_building_products_housing_seasonsq_63d_base_v118_signal,
    f26bph_f26_building_products_housing_seasonsq_252d_base_v119_signal,
    f26bph_f26_building_products_housing_growthsq_252d_base_v120_signal,
    f26bph_f26_building_products_housing_cyclexseason_252d_base_v121_signal,
    f26bph_f26_building_products_housing_cyclexgrowth_252d_base_v122_signal,
    f26bph_f26_building_products_housing_seasonxgrowth_252d_base_v123_signal,
    f26bph_f26_building_products_housing_cyclerank_504d_base_v124_signal,
    f26bph_f26_building_products_housing_seasonrank_504d_base_v125_signal,
    f26bph_f26_building_products_housing_growthrank_504d_base_v126_signal,
    f26bph_f26_building_products_housing_cyclexpkgap_252d_base_v127_signal,
    f26bph_f26_building_products_housing_seasonxpkgap_252d_base_v128_signal,
    f26bph_f26_building_products_housing_growthxpkgap_252d_base_v129_signal,
    f26bph_f26_building_products_housing_cyclexebitval_63d_base_v130_signal,
    f26bph_f26_building_products_housing_cyclexebitval_252d_base_v131_signal,
    f26bph_f26_building_products_housing_seasonxebitval_63d_base_v132_signal,
    f26bph_f26_building_products_housing_growthxlogcap_63d_base_v133_signal,
    f26bph_f26_building_products_housing_cyclexlogcap_252d_base_v134_signal,
    f26bph_f26_building_products_housing_seasonxlogcap_252d_base_v135_signal,
    f26bph_f26_building_products_housing_cyclexebitg_63d_base_v136_signal,
    f26bph_f26_building_products_housing_cyclexebitg_252d_base_v137_signal,
    f26bph_f26_building_products_housing_seasonxebitg_252d_base_v138_signal,
    f26bph_f26_building_products_housing_growthxrevg_63d_base_v139_signal,
    f26bph_f26_building_products_housing_cyclexvolz_252d_base_v140_signal,
    f26bph_f26_building_products_housing_seasonxvolz_252d_base_v141_signal,
    f26bph_f26_building_products_housing_cyclexvolclose_63d_base_v142_signal,
    f26bph_f26_building_products_housing_cyclexpxdet_252d_base_v143_signal,
    f26bph_f26_building_products_housing_seasonxpxdet_252d_base_v144_signal,
    f26bph_f26_building_products_housing_growthxpxdet_252d_base_v145_signal,
    f26bph_f26_building_products_housing_cyclexrange_252d_base_v146_signal,
    f26bph_f26_building_products_housing_seasonxrange_63d_base_v147_signal,
    f26bph_f26_building_products_housing_cyclexlogrev_252d_base_v148_signal,
    f26bph_f26_building_products_housing_compo3_252d_base_v149_signal,
    f26bph_f26_building_products_housing_compow_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_BUILDING_PRODUCTS_HOUSING_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f26_building_products_housing_base_076_150_claude: {n_features} features pass")
