import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
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

def f10_tier1_leverage_equity_slope_diff_norm_756d_v151_signal(equity):
    """Normalized slope change for Raw level of equity over 756d window."""
    res = (_slope_pct(equity, 756).diff(756) / _sma(equity.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_756d_v152_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_756d_v153_signal(debt):
    """Normalized slope change for Raw level of debt over 756d window."""
    res = (_slope_pct(debt, 756).diff(756) / _sma(debt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_756d_v154_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 756d window."""
    res = (_slope_pct(_ratio(equity, assets), 756).diff(756) / _sma(_ratio(equity, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_756d_v155_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 756d window."""
    res = (_slope_pct(_ratio(debt, equity), 756).diff(756) / _sma(_ratio(debt, equity).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_1008d_v156_signal(equity):
    """Normalized slope change for Raw level of equity over 1008d window."""
    res = (_slope_pct(equity, 1008).diff(1008) / _sma(equity.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_1008d_v157_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_1008d_v158_signal(debt):
    """Normalized slope change for Raw level of debt over 1008d window."""
    res = (_slope_pct(debt, 1008).diff(1008) / _sma(debt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_1008d_v159_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 1008d window."""
    res = (_slope_pct(_ratio(equity, assets), 1008).diff(1008) / _sma(_ratio(equity, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_1008d_v160_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 1008d window."""
    res = (_slope_pct(_ratio(debt, equity), 1008).diff(1008) / _sma(_ratio(debt, equity).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_1260d_v161_signal(equity):
    """Normalized slope change for Raw level of equity over 1260d window."""
    res = (_slope_pct(equity, 1260).diff(1260) / _sma(equity.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_1260d_v162_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_1260d_v163_signal(debt):
    """Normalized slope change for Raw level of debt over 1260d window."""
    res = (_slope_pct(debt, 1260).diff(1260) / _sma(debt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_1260d_v164_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 1260d window."""
    res = (_slope_pct(_ratio(equity, assets), 1260).diff(1260) / _sma(_ratio(equity, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_1260d_v165_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 1260d window."""
    res = (_slope_pct(_ratio(debt, equity), 1260).diff(1260) / _sma(_ratio(debt, equity).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_5d_v166_signal(equity):
    """Relative momentum strength for Raw level of equity over 5d window."""
    res = _z(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_5d_v167_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_5d_v168_signal(debt):
    """Relative momentum strength for Raw level of debt over 5d window."""
    res = _z(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_5d_v169_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 5d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_5d_v170_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 5d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_10d_v171_signal(equity):
    """Relative momentum strength for Raw level of equity over 10d window."""
    res = _z(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_10d_v172_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_10d_v173_signal(debt):
    """Relative momentum strength for Raw level of debt over 10d window."""
    res = _z(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_10d_v174_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 10d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_10d_v175_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 10d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_21d_v176_signal(equity):
    """Relative momentum strength for Raw level of equity over 21d window."""
    res = _z(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_21d_v177_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_21d_v178_signal(debt):
    """Relative momentum strength for Raw level of debt over 21d window."""
    res = _z(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_21d_v179_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 21d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_21d_v180_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 21d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_42d_v181_signal(equity):
    """Relative momentum strength for Raw level of equity over 42d window."""
    res = _z(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_42d_v182_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_42d_v183_signal(debt):
    """Relative momentum strength for Raw level of debt over 42d window."""
    res = _z(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_42d_v184_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 42d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_42d_v185_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 42d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_63d_v186_signal(equity):
    """Relative momentum strength for Raw level of equity over 63d window."""
    res = _z(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_63d_v187_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_63d_v188_signal(debt):
    """Relative momentum strength for Raw level of debt over 63d window."""
    res = _z(_slope_pct(debt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_63d_v189_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 63d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_63d_v190_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 63d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_126d_v191_signal(equity):
    """Relative momentum strength for Raw level of equity over 126d window."""
    res = _z(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_126d_v192_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_126d_v193_signal(debt):
    """Relative momentum strength for Raw level of debt over 126d window."""
    res = _z(_slope_pct(debt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_126d_v194_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 126d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_126d_v195_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 126d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_252d_v196_signal(equity):
    """Relative momentum strength for Raw level of equity over 252d window."""
    res = _z(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_252d_v197_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_252d_v198_signal(debt):
    """Relative momentum strength for Raw level of debt over 252d window."""
    res = _z(_slope_pct(debt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_252d_v199_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 252d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_252d_v200_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 252d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_504d_v201_signal(equity):
    """Relative momentum strength for Raw level of equity over 504d window."""
    res = _z(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_504d_v202_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_504d_v203_signal(debt):
    """Relative momentum strength for Raw level of debt over 504d window."""
    res = _z(_slope_pct(debt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_504d_v204_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 504d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_504d_v205_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 504d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_756d_v206_signal(equity):
    """Relative momentum strength for Raw level of equity over 756d window."""
    res = _z(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_756d_v207_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_756d_v208_signal(debt):
    """Relative momentum strength for Raw level of debt over 756d window."""
    res = _z(_slope_pct(debt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_756d_v209_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 756d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_756d_v210_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 756d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_1008d_v211_signal(equity):
    """Relative momentum strength for Raw level of equity over 1008d window."""
    res = _z(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_1008d_v212_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_1008d_v213_signal(debt):
    """Relative momentum strength for Raw level of debt over 1008d window."""
    res = _z(_slope_pct(debt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_1008d_v214_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 1008d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_1008d_v215_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 1008d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_mom_z_1260d_v216_signal(equity):
    """Relative momentum strength for Raw level of equity over 1260d window."""
    res = _z(_slope_pct(equity, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_mom_z_1260d_v217_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_mom_z_1260d_v218_signal(debt):
    """Relative momentum strength for Raw level of debt over 1260d window."""
    res = _z(_slope_pct(debt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_mom_z_1260d_v219_signal(equity, assets):
    """Relative momentum strength for Capital adequacy proxy over 1260d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_mom_z_1260d_v220_signal(debt, equity):
    """Relative momentum strength for Total debt to equity ratio over 1260d window."""
    res = _z(_slope_pct(_ratio(debt, equity), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_5d_v221_signal(equity):
    """Volatility of momentum for Raw level of equity over 5d window."""
    res = _std(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_5d_v222_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_5d_v223_signal(debt):
    """Volatility of momentum for Raw level of debt over 5d window."""
    res = _std(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_5d_v224_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 5d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_5d_v225_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 5d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_10d_v226_signal(equity):
    """Volatility of momentum for Raw level of equity over 10d window."""
    res = _std(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_10d_v227_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_10d_v228_signal(debt):
    """Volatility of momentum for Raw level of debt over 10d window."""
    res = _std(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_10d_v229_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 10d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_10d_v230_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 10d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_21d_v231_signal(equity):
    """Volatility of momentum for Raw level of equity over 21d window."""
    res = _std(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_21d_v232_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_21d_v233_signal(debt):
    """Volatility of momentum for Raw level of debt over 21d window."""
    res = _std(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_21d_v234_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 21d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_21d_v235_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 21d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_42d_v236_signal(equity):
    """Volatility of momentum for Raw level of equity over 42d window."""
    res = _std(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_42d_v237_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_42d_v238_signal(debt):
    """Volatility of momentum for Raw level of debt over 42d window."""
    res = _std(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_42d_v239_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 42d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_42d_v240_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 42d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_63d_v241_signal(equity):
    """Volatility of momentum for Raw level of equity over 63d window."""
    res = _std(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_63d_v242_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_63d_v243_signal(debt):
    """Volatility of momentum for Raw level of debt over 63d window."""
    res = _std(_slope_pct(debt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_63d_v244_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 63d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_63d_v245_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 63d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_126d_v246_signal(equity):
    """Volatility of momentum for Raw level of equity over 126d window."""
    res = _std(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_126d_v247_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_126d_v248_signal(debt):
    """Volatility of momentum for Raw level of debt over 126d window."""
    res = _std(_slope_pct(debt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_126d_v249_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 126d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_126d_v250_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 126d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_252d_v251_signal(equity):
    """Volatility of momentum for Raw level of equity over 252d window."""
    res = _std(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_252d_v252_signal(assets):
    """Volatility of momentum for Raw level of assets over 252d window."""
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_252d_v253_signal(debt):
    """Volatility of momentum for Raw level of debt over 252d window."""
    res = _std(_slope_pct(debt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_252d_v254_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 252d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_252d_v255_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 252d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_504d_v256_signal(equity):
    """Volatility of momentum for Raw level of equity over 504d window."""
    res = _std(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_504d_v257_signal(assets):
    """Volatility of momentum for Raw level of assets over 504d window."""
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_504d_v258_signal(debt):
    """Volatility of momentum for Raw level of debt over 504d window."""
    res = _std(_slope_pct(debt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_504d_v259_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 504d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_504d_v260_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 504d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_756d_v261_signal(equity):
    """Volatility of momentum for Raw level of equity over 756d window."""
    res = _std(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_756d_v262_signal(assets):
    """Volatility of momentum for Raw level of assets over 756d window."""
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_756d_v263_signal(debt):
    """Volatility of momentum for Raw level of debt over 756d window."""
    res = _std(_slope_pct(debt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_756d_v264_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 756d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_756d_v265_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 756d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_1008d_v266_signal(equity):
    """Volatility of momentum for Raw level of equity over 1008d window."""
    res = _std(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_1008d_v267_signal(assets):
    """Volatility of momentum for Raw level of assets over 1008d window."""
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_1008d_v268_signal(debt):
    """Volatility of momentum for Raw level of debt over 1008d window."""
    res = _std(_slope_pct(debt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_1008d_v269_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 1008d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_1008d_v270_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 1008d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_vol_slope_1260d_v271_signal(equity):
    """Volatility of momentum for Raw level of equity over 1260d window."""
    res = _std(_slope_pct(equity, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_vol_slope_1260d_v272_signal(assets):
    """Volatility of momentum for Raw level of assets over 1260d window."""
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_vol_slope_1260d_v273_signal(debt):
    """Volatility of momentum for Raw level of debt over 1260d window."""
    res = _std(_slope_pct(debt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_vol_slope_1260d_v274_signal(equity, assets):
    """Volatility of momentum for Capital adequacy proxy over 1260d window."""
    res = _std(_slope_pct(_ratio(equity, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_vol_slope_1260d_v275_signal(debt, equity):
    """Volatility of momentum for Total debt to equity ratio over 1260d window."""
    res = _std(_slope_pct(_ratio(debt, equity), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_slope_5d_v276_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 5d window."""
    res = _ewma(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_slope_5d_v277_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 5d window."""
    res = _ewma(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_slope_5d_v278_signal(debt):
    """Exponential momentum smoothing for Raw level of debt over 5d window."""
    res = _ewma(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_slope_5d_v279_signal(equity, assets):
    """Exponential momentum smoothing for Capital adequacy proxy over 5d window."""
    res = _ewma(_slope_pct(_ratio(equity, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_slope_5d_v280_signal(debt, equity):
    """Exponential momentum smoothing for Total debt to equity ratio over 5d window."""
    res = _ewma(_slope_pct(_ratio(debt, equity), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_slope_10d_v281_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 10d window."""
    res = _ewma(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_slope_10d_v282_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 10d window."""
    res = _ewma(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_slope_10d_v283_signal(debt):
    """Exponential momentum smoothing for Raw level of debt over 10d window."""
    res = _ewma(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_slope_10d_v284_signal(equity, assets):
    """Exponential momentum smoothing for Capital adequacy proxy over 10d window."""
    res = _ewma(_slope_pct(_ratio(equity, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_slope_10d_v285_signal(debt, equity):
    """Exponential momentum smoothing for Total debt to equity ratio over 10d window."""
    res = _ewma(_slope_pct(_ratio(debt, equity), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_slope_21d_v286_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 21d window."""
    res = _ewma(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_slope_21d_v287_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 21d window."""
    res = _ewma(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_slope_21d_v288_signal(debt):
    """Exponential momentum smoothing for Raw level of debt over 21d window."""
    res = _ewma(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_slope_21d_v289_signal(equity, assets):
    """Exponential momentum smoothing for Capital adequacy proxy over 21d window."""
    res = _ewma(_slope_pct(_ratio(equity, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_slope_21d_v290_signal(debt, equity):
    """Exponential momentum smoothing for Total debt to equity ratio over 21d window."""
    res = _ewma(_slope_pct(_ratio(debt, equity), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_slope_42d_v291_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 42d window."""
    res = _ewma(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_slope_42d_v292_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 42d window."""
    res = _ewma(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_slope_42d_v293_signal(debt):
    """Exponential momentum smoothing for Raw level of debt over 42d window."""
    res = _ewma(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_slope_42d_v294_signal(equity, assets):
    """Exponential momentum smoothing for Capital adequacy proxy over 42d window."""
    res = _ewma(_slope_pct(_ratio(equity, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_slope_42d_v295_signal(debt, equity):
    """Exponential momentum smoothing for Total debt to equity ratio over 42d window."""
    res = _ewma(_slope_pct(_ratio(debt, equity), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_slope_63d_v296_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 63d window."""
    res = _ewma(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_slope_63d_v297_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 63d window."""
    res = _ewma(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_slope_63d_v298_signal(debt):
    """Exponential momentum smoothing for Raw level of debt over 63d window."""
    res = _ewma(_slope_pct(debt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_slope_63d_v299_signal(equity, assets):
    """Exponential momentum smoothing for Capital adequacy proxy over 63d window."""
    res = _ewma(_slope_pct(_ratio(equity, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_slope_63d_v300_signal(debt, equity):
    """Exponential momentum smoothing for Total debt to equity ratio over 63d window."""
    res = _ewma(_slope_pct(_ratio(debt, equity), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_tier1_leverage_equity_slope_diff_norm_756d_v151_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_756d_v151_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_756d_v152_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_756d_v152_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_756d_v153_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_756d_v153_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_756d_v154_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_756d_v154_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_756d_v155_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_756d_v155_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_1008d_v156_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_1008d_v156_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_1008d_v157_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_1008d_v157_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_1008d_v158_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_1008d_v158_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_1008d_v159_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_1008d_v159_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_1008d_v160_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_1008d_v160_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_1260d_v161_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_1260d_v161_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_1260d_v162_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_1260d_v162_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_1260d_v163_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_1260d_v163_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_1260d_v164_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_1260d_v164_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_1260d_v165_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_1260d_v165_signal},
    "f10_tier1_leverage_equity_mom_z_5d_v166_signal": {"func": f10_tier1_leverage_equity_mom_z_5d_v166_signal},
    "f10_tier1_leverage_assets_mom_z_5d_v167_signal": {"func": f10_tier1_leverage_assets_mom_z_5d_v167_signal},
    "f10_tier1_leverage_debt_mom_z_5d_v168_signal": {"func": f10_tier1_leverage_debt_mom_z_5d_v168_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_5d_v169_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_5d_v169_signal},
    "f10_tier1_leverage_total_leverage_mom_z_5d_v170_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_5d_v170_signal},
    "f10_tier1_leverage_equity_mom_z_10d_v171_signal": {"func": f10_tier1_leverage_equity_mom_z_10d_v171_signal},
    "f10_tier1_leverage_assets_mom_z_10d_v172_signal": {"func": f10_tier1_leverage_assets_mom_z_10d_v172_signal},
    "f10_tier1_leverage_debt_mom_z_10d_v173_signal": {"func": f10_tier1_leverage_debt_mom_z_10d_v173_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_10d_v174_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_10d_v174_signal},
    "f10_tier1_leverage_total_leverage_mom_z_10d_v175_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_10d_v175_signal},
    "f10_tier1_leverage_equity_mom_z_21d_v176_signal": {"func": f10_tier1_leverage_equity_mom_z_21d_v176_signal},
    "f10_tier1_leverage_assets_mom_z_21d_v177_signal": {"func": f10_tier1_leverage_assets_mom_z_21d_v177_signal},
    "f10_tier1_leverage_debt_mom_z_21d_v178_signal": {"func": f10_tier1_leverage_debt_mom_z_21d_v178_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_21d_v179_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_21d_v179_signal},
    "f10_tier1_leverage_total_leverage_mom_z_21d_v180_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_21d_v180_signal},
    "f10_tier1_leverage_equity_mom_z_42d_v181_signal": {"func": f10_tier1_leverage_equity_mom_z_42d_v181_signal},
    "f10_tier1_leverage_assets_mom_z_42d_v182_signal": {"func": f10_tier1_leverage_assets_mom_z_42d_v182_signal},
    "f10_tier1_leverage_debt_mom_z_42d_v183_signal": {"func": f10_tier1_leverage_debt_mom_z_42d_v183_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_42d_v184_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_42d_v184_signal},
    "f10_tier1_leverage_total_leverage_mom_z_42d_v185_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_42d_v185_signal},
    "f10_tier1_leverage_equity_mom_z_63d_v186_signal": {"func": f10_tier1_leverage_equity_mom_z_63d_v186_signal},
    "f10_tier1_leverage_assets_mom_z_63d_v187_signal": {"func": f10_tier1_leverage_assets_mom_z_63d_v187_signal},
    "f10_tier1_leverage_debt_mom_z_63d_v188_signal": {"func": f10_tier1_leverage_debt_mom_z_63d_v188_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_63d_v189_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_63d_v189_signal},
    "f10_tier1_leverage_total_leverage_mom_z_63d_v190_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_63d_v190_signal},
    "f10_tier1_leverage_equity_mom_z_126d_v191_signal": {"func": f10_tier1_leverage_equity_mom_z_126d_v191_signal},
    "f10_tier1_leverage_assets_mom_z_126d_v192_signal": {"func": f10_tier1_leverage_assets_mom_z_126d_v192_signal},
    "f10_tier1_leverage_debt_mom_z_126d_v193_signal": {"func": f10_tier1_leverage_debt_mom_z_126d_v193_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_126d_v194_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_126d_v194_signal},
    "f10_tier1_leverage_total_leverage_mom_z_126d_v195_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_126d_v195_signal},
    "f10_tier1_leverage_equity_mom_z_252d_v196_signal": {"func": f10_tier1_leverage_equity_mom_z_252d_v196_signal},
    "f10_tier1_leverage_assets_mom_z_252d_v197_signal": {"func": f10_tier1_leverage_assets_mom_z_252d_v197_signal},
    "f10_tier1_leverage_debt_mom_z_252d_v198_signal": {"func": f10_tier1_leverage_debt_mom_z_252d_v198_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_252d_v199_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_252d_v199_signal},
    "f10_tier1_leverage_total_leverage_mom_z_252d_v200_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_252d_v200_signal},
    "f10_tier1_leverage_equity_mom_z_504d_v201_signal": {"func": f10_tier1_leverage_equity_mom_z_504d_v201_signal},
    "f10_tier1_leverage_assets_mom_z_504d_v202_signal": {"func": f10_tier1_leverage_assets_mom_z_504d_v202_signal},
    "f10_tier1_leverage_debt_mom_z_504d_v203_signal": {"func": f10_tier1_leverage_debt_mom_z_504d_v203_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_504d_v204_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_504d_v204_signal},
    "f10_tier1_leverage_total_leverage_mom_z_504d_v205_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_504d_v205_signal},
    "f10_tier1_leverage_equity_mom_z_756d_v206_signal": {"func": f10_tier1_leverage_equity_mom_z_756d_v206_signal},
    "f10_tier1_leverage_assets_mom_z_756d_v207_signal": {"func": f10_tier1_leverage_assets_mom_z_756d_v207_signal},
    "f10_tier1_leverage_debt_mom_z_756d_v208_signal": {"func": f10_tier1_leverage_debt_mom_z_756d_v208_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_756d_v209_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_756d_v209_signal},
    "f10_tier1_leverage_total_leverage_mom_z_756d_v210_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_756d_v210_signal},
    "f10_tier1_leverage_equity_mom_z_1008d_v211_signal": {"func": f10_tier1_leverage_equity_mom_z_1008d_v211_signal},
    "f10_tier1_leverage_assets_mom_z_1008d_v212_signal": {"func": f10_tier1_leverage_assets_mom_z_1008d_v212_signal},
    "f10_tier1_leverage_debt_mom_z_1008d_v213_signal": {"func": f10_tier1_leverage_debt_mom_z_1008d_v213_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_1008d_v214_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_1008d_v214_signal},
    "f10_tier1_leverage_total_leverage_mom_z_1008d_v215_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_1008d_v215_signal},
    "f10_tier1_leverage_equity_mom_z_1260d_v216_signal": {"func": f10_tier1_leverage_equity_mom_z_1260d_v216_signal},
    "f10_tier1_leverage_assets_mom_z_1260d_v217_signal": {"func": f10_tier1_leverage_assets_mom_z_1260d_v217_signal},
    "f10_tier1_leverage_debt_mom_z_1260d_v218_signal": {"func": f10_tier1_leverage_debt_mom_z_1260d_v218_signal},
    "f10_tier1_leverage_tier1_proxy_mom_z_1260d_v219_signal": {"func": f10_tier1_leverage_tier1_proxy_mom_z_1260d_v219_signal},
    "f10_tier1_leverage_total_leverage_mom_z_1260d_v220_signal": {"func": f10_tier1_leverage_total_leverage_mom_z_1260d_v220_signal},
    "f10_tier1_leverage_equity_vol_slope_5d_v221_signal": {"func": f10_tier1_leverage_equity_vol_slope_5d_v221_signal},
    "f10_tier1_leverage_assets_vol_slope_5d_v222_signal": {"func": f10_tier1_leverage_assets_vol_slope_5d_v222_signal},
    "f10_tier1_leverage_debt_vol_slope_5d_v223_signal": {"func": f10_tier1_leverage_debt_vol_slope_5d_v223_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_5d_v224_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_5d_v224_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_5d_v225_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_5d_v225_signal},
    "f10_tier1_leverage_equity_vol_slope_10d_v226_signal": {"func": f10_tier1_leverage_equity_vol_slope_10d_v226_signal},
    "f10_tier1_leverage_assets_vol_slope_10d_v227_signal": {"func": f10_tier1_leverage_assets_vol_slope_10d_v227_signal},
    "f10_tier1_leverage_debt_vol_slope_10d_v228_signal": {"func": f10_tier1_leverage_debt_vol_slope_10d_v228_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_10d_v229_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_10d_v229_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_10d_v230_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_10d_v230_signal},
    "f10_tier1_leverage_equity_vol_slope_21d_v231_signal": {"func": f10_tier1_leverage_equity_vol_slope_21d_v231_signal},
    "f10_tier1_leverage_assets_vol_slope_21d_v232_signal": {"func": f10_tier1_leverage_assets_vol_slope_21d_v232_signal},
    "f10_tier1_leverage_debt_vol_slope_21d_v233_signal": {"func": f10_tier1_leverage_debt_vol_slope_21d_v233_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_21d_v234_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_21d_v234_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_21d_v235_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_21d_v235_signal},
    "f10_tier1_leverage_equity_vol_slope_42d_v236_signal": {"func": f10_tier1_leverage_equity_vol_slope_42d_v236_signal},
    "f10_tier1_leverage_assets_vol_slope_42d_v237_signal": {"func": f10_tier1_leverage_assets_vol_slope_42d_v237_signal},
    "f10_tier1_leverage_debt_vol_slope_42d_v238_signal": {"func": f10_tier1_leverage_debt_vol_slope_42d_v238_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_42d_v239_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_42d_v239_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_42d_v240_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_42d_v240_signal},
    "f10_tier1_leverage_equity_vol_slope_63d_v241_signal": {"func": f10_tier1_leverage_equity_vol_slope_63d_v241_signal},
    "f10_tier1_leverage_assets_vol_slope_63d_v242_signal": {"func": f10_tier1_leverage_assets_vol_slope_63d_v242_signal},
    "f10_tier1_leverage_debt_vol_slope_63d_v243_signal": {"func": f10_tier1_leverage_debt_vol_slope_63d_v243_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_63d_v244_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_63d_v244_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_63d_v245_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_63d_v245_signal},
    "f10_tier1_leverage_equity_vol_slope_126d_v246_signal": {"func": f10_tier1_leverage_equity_vol_slope_126d_v246_signal},
    "f10_tier1_leverage_assets_vol_slope_126d_v247_signal": {"func": f10_tier1_leverage_assets_vol_slope_126d_v247_signal},
    "f10_tier1_leverage_debt_vol_slope_126d_v248_signal": {"func": f10_tier1_leverage_debt_vol_slope_126d_v248_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_126d_v249_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_126d_v249_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_126d_v250_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_126d_v250_signal},
    "f10_tier1_leverage_equity_vol_slope_252d_v251_signal": {"func": f10_tier1_leverage_equity_vol_slope_252d_v251_signal},
    "f10_tier1_leverage_assets_vol_slope_252d_v252_signal": {"func": f10_tier1_leverage_assets_vol_slope_252d_v252_signal},
    "f10_tier1_leverage_debt_vol_slope_252d_v253_signal": {"func": f10_tier1_leverage_debt_vol_slope_252d_v253_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_252d_v254_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_252d_v254_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_252d_v255_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_252d_v255_signal},
    "f10_tier1_leverage_equity_vol_slope_504d_v256_signal": {"func": f10_tier1_leverage_equity_vol_slope_504d_v256_signal},
    "f10_tier1_leverage_assets_vol_slope_504d_v257_signal": {"func": f10_tier1_leverage_assets_vol_slope_504d_v257_signal},
    "f10_tier1_leverage_debt_vol_slope_504d_v258_signal": {"func": f10_tier1_leverage_debt_vol_slope_504d_v258_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_504d_v259_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_504d_v259_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_504d_v260_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_504d_v260_signal},
    "f10_tier1_leverage_equity_vol_slope_756d_v261_signal": {"func": f10_tier1_leverage_equity_vol_slope_756d_v261_signal},
    "f10_tier1_leverage_assets_vol_slope_756d_v262_signal": {"func": f10_tier1_leverage_assets_vol_slope_756d_v262_signal},
    "f10_tier1_leverage_debt_vol_slope_756d_v263_signal": {"func": f10_tier1_leverage_debt_vol_slope_756d_v263_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_756d_v264_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_756d_v264_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_756d_v265_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_756d_v265_signal},
    "f10_tier1_leverage_equity_vol_slope_1008d_v266_signal": {"func": f10_tier1_leverage_equity_vol_slope_1008d_v266_signal},
    "f10_tier1_leverage_assets_vol_slope_1008d_v267_signal": {"func": f10_tier1_leverage_assets_vol_slope_1008d_v267_signal},
    "f10_tier1_leverage_debt_vol_slope_1008d_v268_signal": {"func": f10_tier1_leverage_debt_vol_slope_1008d_v268_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_1008d_v269_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_1008d_v269_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_1008d_v270_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_1008d_v270_signal},
    "f10_tier1_leverage_equity_vol_slope_1260d_v271_signal": {"func": f10_tier1_leverage_equity_vol_slope_1260d_v271_signal},
    "f10_tier1_leverage_assets_vol_slope_1260d_v272_signal": {"func": f10_tier1_leverage_assets_vol_slope_1260d_v272_signal},
    "f10_tier1_leverage_debt_vol_slope_1260d_v273_signal": {"func": f10_tier1_leverage_debt_vol_slope_1260d_v273_signal},
    "f10_tier1_leverage_tier1_proxy_vol_slope_1260d_v274_signal": {"func": f10_tier1_leverage_tier1_proxy_vol_slope_1260d_v274_signal},
    "f10_tier1_leverage_total_leverage_vol_slope_1260d_v275_signal": {"func": f10_tier1_leverage_total_leverage_vol_slope_1260d_v275_signal},
    "f10_tier1_leverage_equity_ewma_slope_5d_v276_signal": {"func": f10_tier1_leverage_equity_ewma_slope_5d_v276_signal},
    "f10_tier1_leverage_assets_ewma_slope_5d_v277_signal": {"func": f10_tier1_leverage_assets_ewma_slope_5d_v277_signal},
    "f10_tier1_leverage_debt_ewma_slope_5d_v278_signal": {"func": f10_tier1_leverage_debt_ewma_slope_5d_v278_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_slope_5d_v279_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_slope_5d_v279_signal},
    "f10_tier1_leverage_total_leverage_ewma_slope_5d_v280_signal": {"func": f10_tier1_leverage_total_leverage_ewma_slope_5d_v280_signal},
    "f10_tier1_leverage_equity_ewma_slope_10d_v281_signal": {"func": f10_tier1_leverage_equity_ewma_slope_10d_v281_signal},
    "f10_tier1_leverage_assets_ewma_slope_10d_v282_signal": {"func": f10_tier1_leverage_assets_ewma_slope_10d_v282_signal},
    "f10_tier1_leverage_debt_ewma_slope_10d_v283_signal": {"func": f10_tier1_leverage_debt_ewma_slope_10d_v283_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_slope_10d_v284_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_slope_10d_v284_signal},
    "f10_tier1_leverage_total_leverage_ewma_slope_10d_v285_signal": {"func": f10_tier1_leverage_total_leverage_ewma_slope_10d_v285_signal},
    "f10_tier1_leverage_equity_ewma_slope_21d_v286_signal": {"func": f10_tier1_leverage_equity_ewma_slope_21d_v286_signal},
    "f10_tier1_leverage_assets_ewma_slope_21d_v287_signal": {"func": f10_tier1_leverage_assets_ewma_slope_21d_v287_signal},
    "f10_tier1_leverage_debt_ewma_slope_21d_v288_signal": {"func": f10_tier1_leverage_debt_ewma_slope_21d_v288_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_slope_21d_v289_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_slope_21d_v289_signal},
    "f10_tier1_leverage_total_leverage_ewma_slope_21d_v290_signal": {"func": f10_tier1_leverage_total_leverage_ewma_slope_21d_v290_signal},
    "f10_tier1_leverage_equity_ewma_slope_42d_v291_signal": {"func": f10_tier1_leverage_equity_ewma_slope_42d_v291_signal},
    "f10_tier1_leverage_assets_ewma_slope_42d_v292_signal": {"func": f10_tier1_leverage_assets_ewma_slope_42d_v292_signal},
    "f10_tier1_leverage_debt_ewma_slope_42d_v293_signal": {"func": f10_tier1_leverage_debt_ewma_slope_42d_v293_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_slope_42d_v294_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_slope_42d_v294_signal},
    "f10_tier1_leverage_total_leverage_ewma_slope_42d_v295_signal": {"func": f10_tier1_leverage_total_leverage_ewma_slope_42d_v295_signal},
    "f10_tier1_leverage_equity_ewma_slope_63d_v296_signal": {"func": f10_tier1_leverage_equity_ewma_slope_63d_v296_signal},
    "f10_tier1_leverage_assets_ewma_slope_63d_v297_signal": {"func": f10_tier1_leverage_assets_ewma_slope_63d_v297_signal},
    "f10_tier1_leverage_debt_ewma_slope_63d_v298_signal": {"func": f10_tier1_leverage_debt_ewma_slope_63d_v298_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_slope_63d_v299_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_slope_63d_v299_signal},
    "f10_tier1_leverage_total_leverage_ewma_slope_63d_v300_signal": {"func": f10_tier1_leverage_total_leverage_ewma_slope_63d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 10...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
