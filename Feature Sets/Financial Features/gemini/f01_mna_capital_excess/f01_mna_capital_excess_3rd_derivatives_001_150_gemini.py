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

def f01_mna_capital_excess_capital_buffer_jerk_1260d_v151_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 1260d window."""
    res = _jerk(_ratio(equity, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_1260d_v152_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 1260d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_1260d_v153_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 1260d window."""
    res = _jerk(_ratio(marketcap, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_1260d_v154_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 1260d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_5d_v155_signal(equity):
    """Normalized slope change for Raw level of equity over 5d window."""
    res = (_slope_pct(equity, 5).diff(5) / _sma(equity.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_5d_v156_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_5d_v157_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_5d_v158_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 5d window."""
    res = (_slope_pct(_ratio(equity, assets), 5).diff(5) / _sma(_ratio(equity, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_5d_v159_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 5d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 5).diff(5) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_5d_v160_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 5d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 5).diff(5) / _sma(_ratio(marketcap, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_5d_v161_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 5d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 5).diff(5) / _sma(_ratio(assets - equity, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_10d_v162_signal(equity):
    """Normalized slope change for Raw level of equity over 10d window."""
    res = (_slope_pct(equity, 10).diff(10) / _sma(equity.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_10d_v163_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_10d_v164_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_10d_v165_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 10d window."""
    res = (_slope_pct(_ratio(equity, assets), 10).diff(10) / _sma(_ratio(equity, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_10d_v166_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 10d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 10).diff(10) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_10d_v167_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 10d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 10).diff(10) / _sma(_ratio(marketcap, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_10d_v168_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 10d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 10).diff(10) / _sma(_ratio(assets - equity, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_21d_v169_signal(equity):
    """Normalized slope change for Raw level of equity over 21d window."""
    res = (_slope_pct(equity, 21).diff(21) / _sma(equity.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_21d_v170_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_21d_v171_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_21d_v172_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 21d window."""
    res = (_slope_pct(_ratio(equity, assets), 21).diff(21) / _sma(_ratio(equity, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_21d_v173_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 21d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 21).diff(21) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_21d_v174_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 21d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 21).diff(21) / _sma(_ratio(marketcap, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_21d_v175_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 21d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 21).diff(21) / _sma(_ratio(assets - equity, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_42d_v176_signal(equity):
    """Normalized slope change for Raw level of equity over 42d window."""
    res = (_slope_pct(equity, 42).diff(42) / _sma(equity.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_42d_v177_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_42d_v178_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_42d_v179_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 42d window."""
    res = (_slope_pct(_ratio(equity, assets), 42).diff(42) / _sma(_ratio(equity, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_42d_v180_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 42d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 42).diff(42) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_42d_v181_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 42d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 42).diff(42) / _sma(_ratio(marketcap, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_42d_v182_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 42d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 42).diff(42) / _sma(_ratio(assets - equity, marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_63d_v183_signal(equity):
    """Normalized slope change for Raw level of equity over 63d window."""
    res = (_slope_pct(equity, 63).diff(63) / _sma(equity.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_63d_v184_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_63d_v185_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_63d_v186_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 63d window."""
    res = (_slope_pct(_ratio(equity, assets), 63).diff(63) / _sma(_ratio(equity, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_63d_v187_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 63d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 63).diff(63) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_63d_v188_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 63d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 63).diff(63) / _sma(_ratio(marketcap, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_63d_v189_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 63d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 63).diff(63) / _sma(_ratio(assets - equity, marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_126d_v190_signal(equity):
    """Normalized slope change for Raw level of equity over 126d window."""
    res = (_slope_pct(equity, 126).diff(126) / _sma(equity.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_126d_v191_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_126d_v192_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_126d_v193_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 126d window."""
    res = (_slope_pct(_ratio(equity, assets), 126).diff(126) / _sma(_ratio(equity, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_126d_v194_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 126d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 126).diff(126) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_126d_v195_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 126d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 126).diff(126) / _sma(_ratio(marketcap, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_126d_v196_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 126d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 126).diff(126) / _sma(_ratio(assets - equity, marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_252d_v197_signal(equity):
    """Normalized slope change for Raw level of equity over 252d window."""
    res = (_slope_pct(equity, 252).diff(252) / _sma(equity.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_252d_v198_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_252d_v199_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_252d_v200_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 252d window."""
    res = (_slope_pct(_ratio(equity, assets), 252).diff(252) / _sma(_ratio(equity, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_252d_v201_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 252d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 252).diff(252) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_252d_v202_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 252d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 252).diff(252) / _sma(_ratio(marketcap, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_252d_v203_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 252d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 252).diff(252) / _sma(_ratio(assets - equity, marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_504d_v204_signal(equity):
    """Normalized slope change for Raw level of equity over 504d window."""
    res = (_slope_pct(equity, 504).diff(504) / _sma(equity.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_504d_v205_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_504d_v206_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_504d_v207_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 504d window."""
    res = (_slope_pct(_ratio(equity, assets), 504).diff(504) / _sma(_ratio(equity, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_504d_v208_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 504d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 504).diff(504) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_504d_v209_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 504d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 504).diff(504) / _sma(_ratio(marketcap, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_504d_v210_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 504d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 504).diff(504) / _sma(_ratio(assets - equity, marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_756d_v211_signal(equity):
    """Normalized slope change for Raw level of equity over 756d window."""
    res = (_slope_pct(equity, 756).diff(756) / _sma(equity.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_756d_v212_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_756d_v213_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_756d_v214_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 756d window."""
    res = (_slope_pct(_ratio(equity, assets), 756).diff(756) / _sma(_ratio(equity, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_756d_v215_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 756d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 756).diff(756) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_756d_v216_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 756d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 756).diff(756) / _sma(_ratio(marketcap, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_756d_v217_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 756d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 756).diff(756) / _sma(_ratio(assets - equity, marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_1008d_v218_signal(equity):
    """Normalized slope change for Raw level of equity over 1008d window."""
    res = (_slope_pct(equity, 1008).diff(1008) / _sma(equity.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_1008d_v219_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_1008d_v220_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_1008d_v221_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 1008d window."""
    res = (_slope_pct(_ratio(equity, assets), 1008).diff(1008) / _sma(_ratio(equity, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_1008d_v222_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 1008d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 1008).diff(1008) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1008d_v223_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 1008d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 1008).diff(1008) / _sma(_ratio(marketcap, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_1008d_v224_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 1008d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 1008).diff(1008) / _sma(_ratio(assets - equity, marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_diff_norm_1260d_v225_signal(equity):
    """Normalized slope change for Raw level of equity over 1260d window."""
    res = (_slope_pct(equity, 1260).diff(1260) / _sma(equity.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_diff_norm_1260d_v226_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_diff_norm_1260d_v227_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_diff_norm_1260d_v228_signal(equity, assets):
    """Normalized slope change for Equity-to-assets buffer over 1260d window."""
    res = (_slope_pct(_ratio(equity, assets), 1260).diff(1260) / _sma(_ratio(equity, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_diff_norm_1260d_v229_signal(equity, assets, marketcap):
    """Normalized slope change for True excess capital relative to valuation over 1260d window."""
    res = (_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 1260).diff(1260) / _sma(_ratio(equity - (0.08 * assets), marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1260d_v230_signal(marketcap, assets):
    """Normalized slope change for Market valuation per unit of asset over 1260d window."""
    res = (_slope_pct(_ratio(marketcap, assets), 1260).diff(1260) / _sma(_ratio(marketcap, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_diff_norm_1260d_v231_signal(assets, equity, marketcap):
    """Normalized slope change for Non-equity funding relative to valuation over 1260d window."""
    res = (_slope_pct(_ratio(assets - equity, marketcap), 1260).diff(1260) / _sma(_ratio(assets - equity, marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_5d_v232_signal(equity):
    """Relative momentum strength for Raw level of equity over 5d window."""
    res = _z(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_5d_v233_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_5d_v234_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_5d_v235_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 5d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_5d_v236_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 5d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_5d_v237_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 5d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_5d_v238_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 5d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_10d_v239_signal(equity):
    """Relative momentum strength for Raw level of equity over 10d window."""
    res = _z(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_10d_v240_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_10d_v241_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_10d_v242_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 10d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_10d_v243_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 10d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_10d_v244_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 10d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_10d_v245_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 10d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_21d_v246_signal(equity):
    """Relative momentum strength for Raw level of equity over 21d window."""
    res = _z(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_21d_v247_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_21d_v248_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_21d_v249_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 21d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_21d_v250_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 21d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_21d_v251_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 21d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_21d_v252_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 21d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_42d_v253_signal(equity):
    """Relative momentum strength for Raw level of equity over 42d window."""
    res = _z(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_42d_v254_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_42d_v255_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_42d_v256_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 42d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_42d_v257_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 42d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_42d_v258_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 42d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_42d_v259_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 42d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_63d_v260_signal(equity):
    """Relative momentum strength for Raw level of equity over 63d window."""
    res = _z(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_63d_v261_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_63d_v262_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_63d_v263_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 63d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_63d_v264_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 63d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_63d_v265_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 63d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_63d_v266_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 63d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_126d_v267_signal(equity):
    """Relative momentum strength for Raw level of equity over 126d window."""
    res = _z(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_126d_v268_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_126d_v269_signal(pb):
    """Relative momentum strength for Raw level of pb over 126d window."""
    res = _z(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_126d_v270_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 126d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_126d_v271_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 126d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_126d_v272_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 126d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_126d_v273_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 126d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_252d_v274_signal(equity):
    """Relative momentum strength for Raw level of equity over 252d window."""
    res = _z(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_252d_v275_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_252d_v276_signal(pb):
    """Relative momentum strength for Raw level of pb over 252d window."""
    res = _z(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_252d_v277_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 252d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_252d_v278_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 252d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_252d_v279_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 252d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_252d_v280_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 252d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_504d_v281_signal(equity):
    """Relative momentum strength for Raw level of equity over 504d window."""
    res = _z(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_504d_v282_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_504d_v283_signal(pb):
    """Relative momentum strength for Raw level of pb over 504d window."""
    res = _z(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_504d_v284_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 504d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_504d_v285_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 504d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_504d_v286_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 504d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_504d_v287_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 504d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_756d_v288_signal(equity):
    """Relative momentum strength for Raw level of equity over 756d window."""
    res = _z(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_756d_v289_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_756d_v290_signal(pb):
    """Relative momentum strength for Raw level of pb over 756d window."""
    res = _z(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_756d_v291_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 756d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_756d_v292_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 756d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_756d_v293_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 756d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_mom_z_756d_v294_signal(assets, equity, marketcap):
    """Relative momentum strength for Non-equity funding relative to valuation over 756d window."""
    res = _z(_slope_pct(_ratio(assets - equity, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_mom_z_1008d_v295_signal(equity):
    """Relative momentum strength for Raw level of equity over 1008d window."""
    res = _z(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_mom_z_1008d_v296_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_mom_z_1008d_v297_signal(pb):
    """Relative momentum strength for Raw level of pb over 1008d window."""
    res = _z(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_mom_z_1008d_v298_signal(equity, assets):
    """Relative momentum strength for Equity-to-assets buffer over 1008d window."""
    res = _z(_slope_pct(_ratio(equity, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_mom_z_1008d_v299_signal(equity, assets, marketcap):
    """Relative momentum strength for True excess capital relative to valuation over 1008d window."""
    res = _z(_slope_pct(_ratio(equity - (0.08 * assets), marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_mom_z_1008d_v300_signal(marketcap, assets):
    """Relative momentum strength for Market valuation per unit of asset over 1008d window."""
    res = _z(_slope_pct(_ratio(marketcap, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_mna_capital_excess_capital_buffer_jerk_1260d_v151_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_1260d_v151_signal},
    "f01_mna_capital_excess_excess_capital_jerk_1260d_v152_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_1260d_v152_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_1260d_v153_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_1260d_v153_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_1260d_v154_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_1260d_v154_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_5d_v155_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_5d_v155_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_5d_v156_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_5d_v156_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_5d_v157_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_5d_v157_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_5d_v158_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_5d_v158_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_5d_v159_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_5d_v159_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_5d_v160_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_5d_v160_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_5d_v161_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_5d_v161_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_10d_v162_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_10d_v162_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_10d_v163_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_10d_v163_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_10d_v164_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_10d_v164_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_10d_v165_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_10d_v165_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_10d_v166_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_10d_v166_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_10d_v167_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_10d_v167_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_10d_v168_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_10d_v168_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_21d_v169_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_21d_v169_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_21d_v170_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_21d_v170_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_21d_v171_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_21d_v171_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_21d_v172_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_21d_v172_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_21d_v173_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_21d_v173_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_21d_v174_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_21d_v174_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_21d_v175_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_21d_v175_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_42d_v176_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_42d_v176_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_42d_v177_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_42d_v177_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_42d_v178_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_42d_v178_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_42d_v179_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_42d_v179_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_42d_v180_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_42d_v180_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_42d_v181_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_42d_v181_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_42d_v182_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_42d_v182_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_63d_v183_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_63d_v183_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_63d_v184_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_63d_v184_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_63d_v185_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_63d_v185_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_63d_v186_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_63d_v186_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_63d_v187_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_63d_v187_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_63d_v188_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_63d_v188_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_63d_v189_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_63d_v189_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_126d_v190_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_126d_v190_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_126d_v191_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_126d_v191_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_126d_v192_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_126d_v192_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_126d_v193_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_126d_v193_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_126d_v194_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_126d_v194_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_126d_v195_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_126d_v195_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_126d_v196_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_126d_v196_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_252d_v197_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_252d_v197_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_252d_v198_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_252d_v198_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_252d_v199_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_252d_v199_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_252d_v200_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_252d_v200_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_252d_v201_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_252d_v201_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_252d_v202_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_252d_v202_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_252d_v203_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_252d_v203_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_504d_v204_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_504d_v204_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_504d_v205_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_504d_v205_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_504d_v206_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_504d_v206_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_504d_v207_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_504d_v207_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_504d_v208_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_504d_v208_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_504d_v209_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_504d_v209_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_504d_v210_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_504d_v210_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_756d_v211_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_756d_v211_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_756d_v212_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_756d_v212_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_756d_v213_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_756d_v213_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_756d_v214_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_756d_v214_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_756d_v215_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_756d_v215_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_756d_v216_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_756d_v216_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_756d_v217_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_756d_v217_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_1008d_v218_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_1008d_v218_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_1008d_v219_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_1008d_v219_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_1008d_v220_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_1008d_v220_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_1008d_v221_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_1008d_v221_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_1008d_v222_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_1008d_v222_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1008d_v223_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1008d_v223_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_1008d_v224_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_1008d_v224_signal},
    "f01_mna_capital_excess_equity_slope_diff_norm_1260d_v225_signal": {"func": f01_mna_capital_excess_equity_slope_diff_norm_1260d_v225_signal},
    "f01_mna_capital_excess_assets_slope_diff_norm_1260d_v226_signal": {"func": f01_mna_capital_excess_assets_slope_diff_norm_1260d_v226_signal},
    "f01_mna_capital_excess_pb_slope_diff_norm_1260d_v227_signal": {"func": f01_mna_capital_excess_pb_slope_diff_norm_1260d_v227_signal},
    "f01_mna_capital_excess_capital_buffer_slope_diff_norm_1260d_v228_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_diff_norm_1260d_v228_signal},
    "f01_mna_capital_excess_excess_capital_slope_diff_norm_1260d_v229_signal": {"func": f01_mna_capital_excess_excess_capital_slope_diff_norm_1260d_v229_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1260d_v230_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_diff_norm_1260d_v230_signal},
    "f01_mna_capital_excess_leverage_moat_slope_diff_norm_1260d_v231_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_diff_norm_1260d_v231_signal},
    "f01_mna_capital_excess_equity_mom_z_5d_v232_signal": {"func": f01_mna_capital_excess_equity_mom_z_5d_v232_signal},
    "f01_mna_capital_excess_assets_mom_z_5d_v233_signal": {"func": f01_mna_capital_excess_assets_mom_z_5d_v233_signal},
    "f01_mna_capital_excess_pb_mom_z_5d_v234_signal": {"func": f01_mna_capital_excess_pb_mom_z_5d_v234_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_5d_v235_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_5d_v235_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_5d_v236_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_5d_v236_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_5d_v237_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_5d_v237_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_5d_v238_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_5d_v238_signal},
    "f01_mna_capital_excess_equity_mom_z_10d_v239_signal": {"func": f01_mna_capital_excess_equity_mom_z_10d_v239_signal},
    "f01_mna_capital_excess_assets_mom_z_10d_v240_signal": {"func": f01_mna_capital_excess_assets_mom_z_10d_v240_signal},
    "f01_mna_capital_excess_pb_mom_z_10d_v241_signal": {"func": f01_mna_capital_excess_pb_mom_z_10d_v241_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_10d_v242_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_10d_v242_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_10d_v243_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_10d_v243_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_10d_v244_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_10d_v244_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_10d_v245_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_10d_v245_signal},
    "f01_mna_capital_excess_equity_mom_z_21d_v246_signal": {"func": f01_mna_capital_excess_equity_mom_z_21d_v246_signal},
    "f01_mna_capital_excess_assets_mom_z_21d_v247_signal": {"func": f01_mna_capital_excess_assets_mom_z_21d_v247_signal},
    "f01_mna_capital_excess_pb_mom_z_21d_v248_signal": {"func": f01_mna_capital_excess_pb_mom_z_21d_v248_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_21d_v249_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_21d_v249_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_21d_v250_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_21d_v250_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_21d_v251_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_21d_v251_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_21d_v252_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_21d_v252_signal},
    "f01_mna_capital_excess_equity_mom_z_42d_v253_signal": {"func": f01_mna_capital_excess_equity_mom_z_42d_v253_signal},
    "f01_mna_capital_excess_assets_mom_z_42d_v254_signal": {"func": f01_mna_capital_excess_assets_mom_z_42d_v254_signal},
    "f01_mna_capital_excess_pb_mom_z_42d_v255_signal": {"func": f01_mna_capital_excess_pb_mom_z_42d_v255_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_42d_v256_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_42d_v256_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_42d_v257_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_42d_v257_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_42d_v258_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_42d_v258_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_42d_v259_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_42d_v259_signal},
    "f01_mna_capital_excess_equity_mom_z_63d_v260_signal": {"func": f01_mna_capital_excess_equity_mom_z_63d_v260_signal},
    "f01_mna_capital_excess_assets_mom_z_63d_v261_signal": {"func": f01_mna_capital_excess_assets_mom_z_63d_v261_signal},
    "f01_mna_capital_excess_pb_mom_z_63d_v262_signal": {"func": f01_mna_capital_excess_pb_mom_z_63d_v262_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_63d_v263_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_63d_v263_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_63d_v264_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_63d_v264_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_63d_v265_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_63d_v265_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_63d_v266_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_63d_v266_signal},
    "f01_mna_capital_excess_equity_mom_z_126d_v267_signal": {"func": f01_mna_capital_excess_equity_mom_z_126d_v267_signal},
    "f01_mna_capital_excess_assets_mom_z_126d_v268_signal": {"func": f01_mna_capital_excess_assets_mom_z_126d_v268_signal},
    "f01_mna_capital_excess_pb_mom_z_126d_v269_signal": {"func": f01_mna_capital_excess_pb_mom_z_126d_v269_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_126d_v270_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_126d_v270_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_126d_v271_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_126d_v271_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_126d_v272_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_126d_v272_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_126d_v273_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_126d_v273_signal},
    "f01_mna_capital_excess_equity_mom_z_252d_v274_signal": {"func": f01_mna_capital_excess_equity_mom_z_252d_v274_signal},
    "f01_mna_capital_excess_assets_mom_z_252d_v275_signal": {"func": f01_mna_capital_excess_assets_mom_z_252d_v275_signal},
    "f01_mna_capital_excess_pb_mom_z_252d_v276_signal": {"func": f01_mna_capital_excess_pb_mom_z_252d_v276_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_252d_v277_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_252d_v277_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_252d_v278_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_252d_v278_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_252d_v279_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_252d_v279_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_252d_v280_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_252d_v280_signal},
    "f01_mna_capital_excess_equity_mom_z_504d_v281_signal": {"func": f01_mna_capital_excess_equity_mom_z_504d_v281_signal},
    "f01_mna_capital_excess_assets_mom_z_504d_v282_signal": {"func": f01_mna_capital_excess_assets_mom_z_504d_v282_signal},
    "f01_mna_capital_excess_pb_mom_z_504d_v283_signal": {"func": f01_mna_capital_excess_pb_mom_z_504d_v283_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_504d_v284_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_504d_v284_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_504d_v285_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_504d_v285_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_504d_v286_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_504d_v286_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_504d_v287_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_504d_v287_signal},
    "f01_mna_capital_excess_equity_mom_z_756d_v288_signal": {"func": f01_mna_capital_excess_equity_mom_z_756d_v288_signal},
    "f01_mna_capital_excess_assets_mom_z_756d_v289_signal": {"func": f01_mna_capital_excess_assets_mom_z_756d_v289_signal},
    "f01_mna_capital_excess_pb_mom_z_756d_v290_signal": {"func": f01_mna_capital_excess_pb_mom_z_756d_v290_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_756d_v291_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_756d_v291_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_756d_v292_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_756d_v292_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_756d_v293_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_756d_v293_signal},
    "f01_mna_capital_excess_leverage_moat_mom_z_756d_v294_signal": {"func": f01_mna_capital_excess_leverage_moat_mom_z_756d_v294_signal},
    "f01_mna_capital_excess_equity_mom_z_1008d_v295_signal": {"func": f01_mna_capital_excess_equity_mom_z_1008d_v295_signal},
    "f01_mna_capital_excess_assets_mom_z_1008d_v296_signal": {"func": f01_mna_capital_excess_assets_mom_z_1008d_v296_signal},
    "f01_mna_capital_excess_pb_mom_z_1008d_v297_signal": {"func": f01_mna_capital_excess_pb_mom_z_1008d_v297_signal},
    "f01_mna_capital_excess_capital_buffer_mom_z_1008d_v298_signal": {"func": f01_mna_capital_excess_capital_buffer_mom_z_1008d_v298_signal},
    "f01_mna_capital_excess_excess_capital_mom_z_1008d_v299_signal": {"func": f01_mna_capital_excess_excess_capital_mom_z_1008d_v299_signal},
    "f01_mna_capital_excess_valuation_per_asset_mom_z_1008d_v300_signal": {"func": f01_mna_capital_excess_valuation_per_asset_mom_z_1008d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 01...")
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
