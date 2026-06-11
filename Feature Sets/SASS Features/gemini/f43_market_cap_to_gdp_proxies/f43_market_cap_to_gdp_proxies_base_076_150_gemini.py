
import numpy as np
import pandas as pd
import inspect

def _safe_div(a, b):
    return a / b.replace(0, np.nan)

def _z(x, w):
    return (x - x.rolling(w, min_periods=w//2).mean()) / x.rolling(w, min_periods=w//2).std().replace(0, np.nan)

def _rank(x, w):
    return x.rolling(w, min_periods=w//2).rank(pct=True) - 0.5

def _slope(x, w):
    return x.diff(w) / x.shift(w).abs().replace(0, np.nan)

def _jerk(x, w):
    s = _slope(x, w)
    return _slope(s, w)

def _f43_mcap_gdp(mcap, gdp):
    return _safe_div(mcap, gdp)

def _f43_norm_rev(mcap, rev):
    return _safe_div(mcap, rev)

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v076_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v076_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v077_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v077_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v078_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v078_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v079_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v079_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v080_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v080_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v081_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v081_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v082_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v082_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v083_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v083_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v084_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v084_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v085_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v085_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v086_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v086_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v087_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v087_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v088_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v088_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v089_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v089_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v090_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v090_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v091_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v091_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v092_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v092_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v093_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v093_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v094_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v094_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v095_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v095_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v096_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v096_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v097_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v097_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v098_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v098_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v099_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v099_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v100_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v100_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v101_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v101_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v102_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v102_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v103_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v103_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v104_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v104_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v105_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v105_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v106_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v106_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v107_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v107_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v108_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v108_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v109_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v109_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v110_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v110_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v111_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v111_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v112_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v112_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v113_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v113_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v114_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v114_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v115_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v115_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v116_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v116_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v117_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v117_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v118_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v118_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v119_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v119_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v120_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v120_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v121_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v121_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v122_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v122_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v123_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v123_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v124_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v124_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v125_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v125_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v126_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v126_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v127_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v127_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v128_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v128_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v129_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v129_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v130_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v130_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v131_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v131_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v132_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v132_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v133_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v133_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v134_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v134_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v135_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v135_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v136_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v136_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v137_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v137_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v138_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v138_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v139_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v139_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v140_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v140_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v141_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v141_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v142_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v142_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v143_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v143_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v144_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v144_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v145_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v145_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v146_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v146_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v147_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v147_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v148_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v148_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v149_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v149_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v150_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v150_signal')

_FEATURES = [f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v076_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v077_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v078_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v079_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v080_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v081_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v082_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v083_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v084_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v085_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v086_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v087_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v088_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v089_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v090_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v091_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v092_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v093_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v094_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v095_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v096_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v097_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v098_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v099_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v100_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v101_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v102_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v103_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v104_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v105_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v106_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v107_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v108_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v109_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v110_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v111_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v112_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v113_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v114_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v115_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_base_v116_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_base_v117_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_base_v118_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_base_v119_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_base_v120_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v121_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v122_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v123_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v124_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v125_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v126_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v127_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v128_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v129_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v130_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v131_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v132_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v133_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v134_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v135_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v136_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v137_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v138_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v139_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v140_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v141_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v142_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v143_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v144_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v145_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_base_v146_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_base_v147_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_base_v148_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_base_v149_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_base_v150_signal]
def _inputs_for(fn): return [p.name for p in inspect.signature(fn).parameters.values()]
REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F43MG_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    import numpy as np, pandas as pd
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0*np.exp(np.cumsum(rets)), name="closeadj")
    close    = pd.Series(closeadj.values, name="close")
    openp    = pd.Series(close.shift(1).fillna(close.iloc[0]).values*(1+np.random.normal(0,0.005,n)), name="open")
    high     = pd.Series(np.maximum(close, openp)*(1+np.abs(np.random.normal(0,0.01,n))), name="high")
    low      = pd.Series(np.minimum(close, openp)*(1-np.abs(np.random.normal(0,0.01,n))), name="low")
    volume   = pd.Series(np.abs(np.random.normal(1e6,3e5,n))+1e5, name="volume")      
    
    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n//63 + 1), 63)[:n]
        s = base*np.exp(np.cumsum(steps/63))
        if allow_neg: s = s - base*0.3
        return pd.Series(s, name=None)
    
    equity = _fund(np.random.randint(0, 10000), allow_neg=True).rename("equity")
    assets = _fund(np.random.randint(0, 10000), allow_neg=True).rename("assets")
    marketcap = _fund(np.random.randint(0, 10000), allow_neg=True).rename("marketcap")
    gdp_proxy = _fund(np.random.randint(0, 10000), allow_neg=True).rename("gdp_proxy")

    
    _FEATURES = [v for k, v in globals().items() if k.endswith("_signal") and callable(v)]
    for fn in _FEATURES:
        res = fn(**{k: v for k, v in locals().items() if k in inspect.signature(fn).parameters})
        assert res.name.endswith("_signal")
        assert len(res) == n
    print(f"OK: {len(_FEATURES)} features passed")
