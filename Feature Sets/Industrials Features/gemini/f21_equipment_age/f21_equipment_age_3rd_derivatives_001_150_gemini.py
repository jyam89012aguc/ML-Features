import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f21_equipment_age_capex_slope_diff_norm_756d_v151_signal(capex):
    res = (_slope_pct(capex, 756).diff(756) / _sma(capex.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_756d_v152_signal(assets):
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_756d_v153_signal(depamor):
    res = (_slope_pct(depamor, 756).diff(756) / _sma(depamor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_756d_v154_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 756).diff(756) / _sma(_ratio(capex, depamor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_756d_v155_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 756).diff(756) / _sma(_ratio(assets, depamor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_1008d_v156_signal(capex):
    res = (_slope_pct(capex, 1008).diff(1008) / _sma(capex.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_1008d_v157_signal(assets):
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_1008d_v158_signal(depamor):
    res = (_slope_pct(depamor, 1008).diff(1008) / _sma(depamor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_1008d_v159_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 1008).diff(1008) / _sma(_ratio(capex, depamor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_1008d_v160_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 1008).diff(1008) / _sma(_ratio(assets, depamor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_1260d_v161_signal(capex):
    res = (_slope_pct(capex, 1260).diff(1260) / _sma(capex.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_1260d_v162_signal(assets):
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_1260d_v163_signal(depamor):
    res = (_slope_pct(depamor, 1260).diff(1260) / _sma(depamor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_1260d_v164_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 1260).diff(1260) / _sma(_ratio(capex, depamor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_1260d_v165_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 1260).diff(1260) / _sma(_ratio(assets, depamor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_5d_v166_signal(capex):
    res = _z(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_5d_v167_signal(assets):
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_5d_v168_signal(depamor):
    res = _z(_slope_pct(depamor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_5d_v169_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_5d_v170_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_10d_v171_signal(capex):
    res = _z(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_10d_v172_signal(assets):
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_10d_v173_signal(depamor):
    res = _z(_slope_pct(depamor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_10d_v174_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_10d_v175_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_21d_v176_signal(capex):
    res = _z(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_21d_v177_signal(assets):
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_21d_v178_signal(depamor):
    res = _z(_slope_pct(depamor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_21d_v179_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_21d_v180_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_42d_v181_signal(capex):
    res = _z(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_42d_v182_signal(assets):
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_42d_v183_signal(depamor):
    res = _z(_slope_pct(depamor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_42d_v184_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_42d_v185_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_63d_v186_signal(capex):
    res = _z(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_63d_v187_signal(assets):
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_63d_v188_signal(depamor):
    res = _z(_slope_pct(depamor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_63d_v189_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_63d_v190_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_126d_v191_signal(capex):
    res = _z(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_126d_v192_signal(assets):
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_126d_v193_signal(depamor):
    res = _z(_slope_pct(depamor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_126d_v194_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_126d_v195_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_252d_v196_signal(capex):
    res = _z(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_252d_v197_signal(assets):
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_252d_v198_signal(depamor):
    res = _z(_slope_pct(depamor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_252d_v199_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_252d_v200_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_504d_v201_signal(capex):
    res = _z(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_504d_v202_signal(assets):
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_504d_v203_signal(depamor):
    res = _z(_slope_pct(depamor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_504d_v204_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_504d_v205_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_756d_v206_signal(capex):
    res = _z(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_756d_v207_signal(assets):
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_756d_v208_signal(depamor):
    res = _z(_slope_pct(depamor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_756d_v209_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_756d_v210_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_1008d_v211_signal(capex):
    res = _z(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_1008d_v212_signal(assets):
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_1008d_v213_signal(depamor):
    res = _z(_slope_pct(depamor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_1008d_v214_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_1008d_v215_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_mom_z_1260d_v216_signal(capex):
    res = _z(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_mom_z_1260d_v217_signal(assets):
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_mom_z_1260d_v218_signal(depamor):
    res = _z(_slope_pct(depamor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_mom_z_1260d_v219_signal(capex, depamor):
    res = _z(_slope_pct(_ratio(capex, depamor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_mom_z_1260d_v220_signal(assets, depamor):
    res = _z(_slope_pct(_ratio(assets, depamor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_5d_v221_signal(capex):
    res = _std(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_5d_v222_signal(assets):
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_5d_v223_signal(depamor):
    res = _std(_slope_pct(depamor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_5d_v224_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_5d_v225_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_10d_v226_signal(capex):
    res = _std(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_10d_v227_signal(assets):
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_10d_v228_signal(depamor):
    res = _std(_slope_pct(depamor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_10d_v229_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_10d_v230_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_21d_v231_signal(capex):
    res = _std(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_21d_v232_signal(assets):
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_21d_v233_signal(depamor):
    res = _std(_slope_pct(depamor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_21d_v234_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_21d_v235_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_42d_v236_signal(capex):
    res = _std(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_42d_v237_signal(assets):
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_42d_v238_signal(depamor):
    res = _std(_slope_pct(depamor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_42d_v239_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_42d_v240_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_63d_v241_signal(capex):
    res = _std(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_63d_v242_signal(assets):
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_63d_v243_signal(depamor):
    res = _std(_slope_pct(depamor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_63d_v244_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_63d_v245_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_126d_v246_signal(capex):
    res = _std(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_126d_v247_signal(assets):
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_126d_v248_signal(depamor):
    res = _std(_slope_pct(depamor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_126d_v249_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_126d_v250_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_252d_v251_signal(capex):
    res = _std(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_252d_v252_signal(assets):
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_252d_v253_signal(depamor):
    res = _std(_slope_pct(depamor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_252d_v254_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_252d_v255_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_504d_v256_signal(capex):
    res = _std(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_504d_v257_signal(assets):
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_504d_v258_signal(depamor):
    res = _std(_slope_pct(depamor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_504d_v259_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_504d_v260_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_756d_v261_signal(capex):
    res = _std(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_756d_v262_signal(assets):
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_756d_v263_signal(depamor):
    res = _std(_slope_pct(depamor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_756d_v264_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_756d_v265_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_1008d_v266_signal(capex):
    res = _std(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_1008d_v267_signal(assets):
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_1008d_v268_signal(depamor):
    res = _std(_slope_pct(depamor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_1008d_v269_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_1008d_v270_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_vol_slope_1260d_v271_signal(capex):
    res = _std(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_vol_slope_1260d_v272_signal(assets):
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_vol_slope_1260d_v273_signal(depamor):
    res = _std(_slope_pct(depamor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_vol_slope_1260d_v274_signal(capex, depamor):
    res = _std(_slope_pct(_ratio(capex, depamor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_vol_slope_1260d_v275_signal(assets, depamor):
    res = _std(_slope_pct(_ratio(assets, depamor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 21...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        try:
            res = func(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            break
    print("Success.")
