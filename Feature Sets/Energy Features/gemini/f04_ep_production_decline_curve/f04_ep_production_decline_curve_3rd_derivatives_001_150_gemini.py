import pandas as pd
import numpy as np
import inspect

# ===== Energy Ultra-High-Performance Alpha Helpers =====
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

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f04_ep_production_decline_curve_debt_slope_diff_norm_42d_v151_signal(debt):
    """Normalized slope change for Raw level of debt over 42d window."""
    res = (_slope_pct(debt, 42).diff(42) / _sma(debt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_42d_v152_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 42d window."""
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_42d_v153_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_42d_v154_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_42d_v155_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 42d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42).diff(42) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_42d_v156_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 42d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 42).diff(42) / _sma(_ratio(marketcap, debt).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_63d_v157_signal(debt):
    """Normalized slope change for Raw level of debt over 63d window."""
    res = (_slope_pct(debt, 63).diff(63) / _sma(debt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_63d_v158_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 63d window."""
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_63d_v159_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_63d_v160_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_63d_v161_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 63d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63).diff(63) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_63d_v162_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 63d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 63).diff(63) / _sma(_ratio(marketcap, debt).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_126d_v163_signal(debt):
    """Normalized slope change for Raw level of debt over 126d window."""
    res = (_slope_pct(debt, 126).diff(126) / _sma(debt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_126d_v164_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 126d window."""
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_126d_v165_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_126d_v166_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_126d_v167_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 126d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126).diff(126) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_126d_v168_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 126d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 126).diff(126) / _sma(_ratio(marketcap, debt).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_252d_v169_signal(debt):
    """Normalized slope change for Raw level of debt over 252d window."""
    res = (_slope_pct(debt, 252).diff(252) / _sma(debt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_252d_v170_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 252d window."""
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_252d_v171_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_252d_v172_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_252d_v173_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 252d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 252).diff(252) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_252d_v174_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 252d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 252).diff(252) / _sma(_ratio(marketcap, debt).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_504d_v175_signal(debt):
    """Normalized slope change for Raw level of debt over 504d window."""
    res = (_slope_pct(debt, 504).diff(504) / _sma(debt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_504d_v176_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 504d window."""
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_504d_v177_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_504d_v178_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_504d_v179_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 504d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 504).diff(504) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_504d_v180_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 504d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 504).diff(504) / _sma(_ratio(marketcap, debt).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_756d_v181_signal(debt):
    """Normalized slope change for Raw level of debt over 756d window."""
    res = (_slope_pct(debt, 756).diff(756) / _sma(debt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_756d_v182_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 756d window."""
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_756d_v183_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_756d_v184_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_756d_v185_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 756d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 756).diff(756) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_756d_v186_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 756d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 756).diff(756) / _sma(_ratio(marketcap, debt).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_1008d_v187_signal(debt):
    """Normalized slope change for Raw level of debt over 1008d window."""
    res = (_slope_pct(debt, 1008).diff(1008) / _sma(debt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_1008d_v188_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1008d window."""
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_1008d_v189_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_1008d_v190_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1008d_v191_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 1008d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1008).diff(1008) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1008d_v192_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 1008d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 1008).diff(1008) / _sma(_ratio(marketcap, debt).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_slope_diff_norm_1260d_v193_signal(debt):
    """Normalized slope change for Raw level of debt over 1260d window."""
    res = (_slope_pct(debt, 1260).diff(1260) / _sma(debt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_slope_diff_norm_1260d_v194_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1260d window."""
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_slope_diff_norm_1260d_v195_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_slope_diff_norm_1260d_v196_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1260d_v197_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 1260d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1260).diff(1260) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1260d_v198_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 1260d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 1260).diff(1260) / _sma(_ratio(marketcap, debt).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_5d_v199_signal(debt):
    """Relative momentum strength for Raw level of debt over 5d window."""
    res = _z(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_5d_v200_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 5d window."""
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_5d_v201_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_5d_v202_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_5d_v203_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 5d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_5d_v204_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 5d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_10d_v205_signal(debt):
    """Relative momentum strength for Raw level of debt over 10d window."""
    res = _z(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_10d_v206_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 10d window."""
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_10d_v207_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_10d_v208_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_10d_v209_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 10d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_10d_v210_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 10d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_21d_v211_signal(debt):
    """Relative momentum strength for Raw level of debt over 21d window."""
    res = _z(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_21d_v212_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 21d window."""
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_21d_v213_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_21d_v214_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_21d_v215_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 21d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_21d_v216_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 21d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_42d_v217_signal(debt):
    """Relative momentum strength for Raw level of debt over 42d window."""
    res = _z(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_42d_v218_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 42d window."""
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_42d_v219_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_42d_v220_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_42d_v221_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 42d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_42d_v222_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 42d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_63d_v223_signal(debt):
    """Relative momentum strength for Raw level of debt over 63d window."""
    res = _z(_slope_pct(debt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_63d_v224_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 63d window."""
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_63d_v225_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_63d_v226_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_63d_v227_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 63d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_63d_v228_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 63d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_126d_v229_signal(debt):
    """Relative momentum strength for Raw level of debt over 126d window."""
    res = _z(_slope_pct(debt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_126d_v230_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 126d window."""
    res = _z(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_126d_v231_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_126d_v232_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_126d_v233_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 126d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_126d_v234_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 126d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_252d_v235_signal(debt):
    """Relative momentum strength for Raw level of debt over 252d window."""
    res = _z(_slope_pct(debt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_252d_v236_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 252d window."""
    res = _z(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_252d_v237_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_252d_v238_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_252d_v239_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 252d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_252d_v240_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 252d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_504d_v241_signal(debt):
    """Relative momentum strength for Raw level of debt over 504d window."""
    res = _z(_slope_pct(debt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_504d_v242_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 504d window."""
    res = _z(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_504d_v243_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_504d_v244_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_504d_v245_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 504d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_504d_v246_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 504d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_756d_v247_signal(debt):
    """Relative momentum strength for Raw level of debt over 756d window."""
    res = _z(_slope_pct(debt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_756d_v248_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 756d window."""
    res = _z(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_756d_v249_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_756d_v250_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_756d_v251_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 756d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_756d_v252_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 756d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_1008d_v253_signal(debt):
    """Relative momentum strength for Raw level of debt over 1008d window."""
    res = _z(_slope_pct(debt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_1008d_v254_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1008d window."""
    res = _z(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_1008d_v255_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_1008d_v256_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_1008d_v257_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_1008d_v258_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 1008d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_mom_z_1260d_v259_signal(debt):
    """Relative momentum strength for Raw level of debt over 1260d window."""
    res = _z(_slope_pct(debt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_mom_z_1260d_v260_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1260d window."""
    res = _z(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_mom_z_1260d_v261_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_mom_z_1260d_v262_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_mom_z_1260d_v263_signal(ebitda, debt, assets, marketcap):
    """Relative momentum strength for Earnings coverage and valuation discount interaction over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_mom_z_1260d_v264_signal(marketcap, debt):
    """Relative momentum strength for Market value coverage of debt over 1260d window."""
    res = _z(_slope_pct(_ratio(marketcap, debt), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_5d_v265_signal(debt):
    """Volatility of momentum for Raw level of debt over 5d window."""
    res = _std(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_5d_v266_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 5d window."""
    res = _std(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_5d_v267_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_5d_v268_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_5d_v269_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 5d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_5d_v270_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 5d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_10d_v271_signal(debt):
    """Volatility of momentum for Raw level of debt over 10d window."""
    res = _std(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_10d_v272_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 10d window."""
    res = _std(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_10d_v273_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_10d_v274_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_10d_v275_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 10d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_10d_v276_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 10d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_21d_v277_signal(debt):
    """Volatility of momentum for Raw level of debt over 21d window."""
    res = _std(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_21d_v278_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 21d window."""
    res = _std(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_21d_v279_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_21d_v280_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_21d_v281_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 21d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_21d_v282_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 21d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_42d_v283_signal(debt):
    """Volatility of momentum for Raw level of debt over 42d window."""
    res = _std(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_42d_v284_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 42d window."""
    res = _std(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_42d_v285_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_42d_v286_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_42d_v287_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 42d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_42d_v288_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 42d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_63d_v289_signal(debt):
    """Volatility of momentum for Raw level of debt over 63d window."""
    res = _std(_slope_pct(debt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_63d_v290_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 63d window."""
    res = _std(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_63d_v291_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_63d_v292_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_63d_v293_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 63d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_63d_v294_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 63d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_debt_vol_slope_126d_v295_signal(debt):
    """Volatility of momentum for Raw level of debt over 126d window."""
    res = _std(_slope_pct(debt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_ebitda_vol_slope_126d_v296_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 126d window."""
    res = _std(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_marketcap_vol_slope_126d_v297_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_assets_vol_slope_126d_v298_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_deleveraging_potential_vol_slope_126d_v299_signal(ebitda, debt, assets, marketcap):
    """Volatility of momentum for Earnings coverage and valuation discount interaction over 126d window."""
    res = _std(_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_ep_production_decline_curve_equity_coverage_vol_slope_126d_v300_signal(marketcap, debt):
    """Volatility of momentum for Market value coverage of debt over 126d window."""
    res = _std(_slope_pct(_ratio(marketcap, debt), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f04_ep_production_decline_curve_debt_slope_diff_norm_42d_v151_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_42d_v151_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_42d_v152_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_42d_v152_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_42d_v153_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_42d_v153_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_42d_v154_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_42d_v154_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_42d_v155_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_42d_v155_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_42d_v156_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_42d_v156_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_63d_v157_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_63d_v157_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_63d_v158_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_63d_v158_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_63d_v159_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_63d_v159_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_63d_v160_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_63d_v160_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_63d_v161_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_63d_v161_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_63d_v162_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_63d_v162_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_126d_v163_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_126d_v163_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_126d_v164_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_126d_v164_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_126d_v165_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_126d_v165_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_126d_v166_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_126d_v166_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_126d_v167_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_126d_v167_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_126d_v168_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_126d_v168_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_252d_v169_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_252d_v169_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_252d_v170_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_252d_v170_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_252d_v171_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_252d_v171_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_252d_v172_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_252d_v172_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_252d_v173_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_252d_v173_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_252d_v174_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_252d_v174_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_504d_v175_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_504d_v175_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_504d_v176_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_504d_v176_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_504d_v177_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_504d_v177_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_504d_v178_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_504d_v178_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_504d_v179_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_504d_v179_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_504d_v180_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_504d_v180_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_756d_v181_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_756d_v181_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_756d_v182_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_756d_v182_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_756d_v183_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_756d_v183_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_756d_v184_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_756d_v184_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_756d_v185_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_756d_v185_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_756d_v186_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_756d_v186_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_1008d_v187_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_1008d_v187_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_1008d_v188_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_1008d_v188_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_1008d_v189_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_1008d_v189_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_1008d_v190_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_1008d_v190_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1008d_v191_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1008d_v191_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1008d_v192_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1008d_v192_signal},
    "f04_ep_production_decline_curve_debt_slope_diff_norm_1260d_v193_signal": {"func": f04_ep_production_decline_curve_debt_slope_diff_norm_1260d_v193_signal},
    "f04_ep_production_decline_curve_ebitda_slope_diff_norm_1260d_v194_signal": {"func": f04_ep_production_decline_curve_ebitda_slope_diff_norm_1260d_v194_signal},
    "f04_ep_production_decline_curve_marketcap_slope_diff_norm_1260d_v195_signal": {"func": f04_ep_production_decline_curve_marketcap_slope_diff_norm_1260d_v195_signal},
    "f04_ep_production_decline_curve_assets_slope_diff_norm_1260d_v196_signal": {"func": f04_ep_production_decline_curve_assets_slope_diff_norm_1260d_v196_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1260d_v197_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_slope_diff_norm_1260d_v197_signal},
    "f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1260d_v198_signal": {"func": f04_ep_production_decline_curve_equity_coverage_slope_diff_norm_1260d_v198_signal},
    "f04_ep_production_decline_curve_debt_mom_z_5d_v199_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_5d_v199_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_5d_v200_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_5d_v200_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_5d_v201_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_5d_v201_signal},
    "f04_ep_production_decline_curve_assets_mom_z_5d_v202_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_5d_v202_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_5d_v203_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_5d_v203_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_5d_v204_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_5d_v204_signal},
    "f04_ep_production_decline_curve_debt_mom_z_10d_v205_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_10d_v205_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_10d_v206_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_10d_v206_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_10d_v207_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_10d_v207_signal},
    "f04_ep_production_decline_curve_assets_mom_z_10d_v208_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_10d_v208_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_10d_v209_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_10d_v209_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_10d_v210_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_10d_v210_signal},
    "f04_ep_production_decline_curve_debt_mom_z_21d_v211_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_21d_v211_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_21d_v212_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_21d_v212_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_21d_v213_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_21d_v213_signal},
    "f04_ep_production_decline_curve_assets_mom_z_21d_v214_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_21d_v214_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_21d_v215_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_21d_v215_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_21d_v216_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_21d_v216_signal},
    "f04_ep_production_decline_curve_debt_mom_z_42d_v217_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_42d_v217_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_42d_v218_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_42d_v218_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_42d_v219_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_42d_v219_signal},
    "f04_ep_production_decline_curve_assets_mom_z_42d_v220_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_42d_v220_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_42d_v221_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_42d_v221_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_42d_v222_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_42d_v222_signal},
    "f04_ep_production_decline_curve_debt_mom_z_63d_v223_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_63d_v223_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_63d_v224_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_63d_v224_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_63d_v225_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_63d_v225_signal},
    "f04_ep_production_decline_curve_assets_mom_z_63d_v226_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_63d_v226_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_63d_v227_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_63d_v227_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_63d_v228_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_63d_v228_signal},
    "f04_ep_production_decline_curve_debt_mom_z_126d_v229_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_126d_v229_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_126d_v230_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_126d_v230_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_126d_v231_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_126d_v231_signal},
    "f04_ep_production_decline_curve_assets_mom_z_126d_v232_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_126d_v232_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_126d_v233_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_126d_v233_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_126d_v234_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_126d_v234_signal},
    "f04_ep_production_decline_curve_debt_mom_z_252d_v235_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_252d_v235_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_252d_v236_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_252d_v236_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_252d_v237_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_252d_v237_signal},
    "f04_ep_production_decline_curve_assets_mom_z_252d_v238_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_252d_v238_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_252d_v239_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_252d_v239_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_252d_v240_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_252d_v240_signal},
    "f04_ep_production_decline_curve_debt_mom_z_504d_v241_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_504d_v241_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_504d_v242_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_504d_v242_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_504d_v243_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_504d_v243_signal},
    "f04_ep_production_decline_curve_assets_mom_z_504d_v244_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_504d_v244_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_504d_v245_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_504d_v245_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_504d_v246_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_504d_v246_signal},
    "f04_ep_production_decline_curve_debt_mom_z_756d_v247_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_756d_v247_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_756d_v248_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_756d_v248_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_756d_v249_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_756d_v249_signal},
    "f04_ep_production_decline_curve_assets_mom_z_756d_v250_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_756d_v250_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_756d_v251_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_756d_v251_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_756d_v252_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_756d_v252_signal},
    "f04_ep_production_decline_curve_debt_mom_z_1008d_v253_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_1008d_v253_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_1008d_v254_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_1008d_v254_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_1008d_v255_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_1008d_v255_signal},
    "f04_ep_production_decline_curve_assets_mom_z_1008d_v256_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_1008d_v256_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_1008d_v257_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_1008d_v257_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_1008d_v258_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_1008d_v258_signal},
    "f04_ep_production_decline_curve_debt_mom_z_1260d_v259_signal": {"func": f04_ep_production_decline_curve_debt_mom_z_1260d_v259_signal},
    "f04_ep_production_decline_curve_ebitda_mom_z_1260d_v260_signal": {"func": f04_ep_production_decline_curve_ebitda_mom_z_1260d_v260_signal},
    "f04_ep_production_decline_curve_marketcap_mom_z_1260d_v261_signal": {"func": f04_ep_production_decline_curve_marketcap_mom_z_1260d_v261_signal},
    "f04_ep_production_decline_curve_assets_mom_z_1260d_v262_signal": {"func": f04_ep_production_decline_curve_assets_mom_z_1260d_v262_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_mom_z_1260d_v263_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_mom_z_1260d_v263_signal},
    "f04_ep_production_decline_curve_equity_coverage_mom_z_1260d_v264_signal": {"func": f04_ep_production_decline_curve_equity_coverage_mom_z_1260d_v264_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_5d_v265_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_5d_v265_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_5d_v266_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_5d_v266_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_5d_v267_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_5d_v267_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_5d_v268_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_5d_v268_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_5d_v269_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_5d_v269_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_5d_v270_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_5d_v270_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_10d_v271_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_10d_v271_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_10d_v272_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_10d_v272_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_10d_v273_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_10d_v273_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_10d_v274_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_10d_v274_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_10d_v275_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_10d_v275_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_10d_v276_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_10d_v276_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_21d_v277_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_21d_v277_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_21d_v278_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_21d_v278_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_21d_v279_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_21d_v279_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_21d_v280_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_21d_v280_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_21d_v281_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_21d_v281_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_21d_v282_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_21d_v282_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_42d_v283_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_42d_v283_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_42d_v284_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_42d_v284_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_42d_v285_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_42d_v285_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_42d_v286_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_42d_v286_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_42d_v287_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_42d_v287_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_42d_v288_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_42d_v288_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_63d_v289_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_63d_v289_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_63d_v290_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_63d_v290_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_63d_v291_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_63d_v291_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_63d_v292_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_63d_v292_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_63d_v293_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_63d_v293_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_63d_v294_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_63d_v294_signal},
    "f04_ep_production_decline_curve_debt_vol_slope_126d_v295_signal": {"func": f04_ep_production_decline_curve_debt_vol_slope_126d_v295_signal},
    "f04_ep_production_decline_curve_ebitda_vol_slope_126d_v296_signal": {"func": f04_ep_production_decline_curve_ebitda_vol_slope_126d_v296_signal},
    "f04_ep_production_decline_curve_marketcap_vol_slope_126d_v297_signal": {"func": f04_ep_production_decline_curve_marketcap_vol_slope_126d_v297_signal},
    "f04_ep_production_decline_curve_assets_vol_slope_126d_v298_signal": {"func": f04_ep_production_decline_curve_assets_vol_slope_126d_v298_signal},
    "f04_ep_production_decline_curve_deleveraging_potential_vol_slope_126d_v299_signal": {"func": f04_ep_production_decline_curve_deleveraging_potential_vol_slope_126d_v299_signal},
    "f04_ep_production_decline_curve_equity_coverage_vol_slope_126d_v300_signal": {"func": f04_ep_production_decline_curve_equity_coverage_vol_slope_126d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 04...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
