# f23_on_balance_volume_family_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average"""
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    """Exponential Moving Average"""
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _obv_calc(c, v):
    """On-Balance Volume Calculation"""
    return (v * np.sign(c.diff().fillna(0))).cumsum()

def _obv_zscore(obv, w):
    """OBV Z-Score relative to its rolling window"""
    return (obv - obv.rolling(w).mean()) / obv.rolling(w).std().replace(0, np.nan)

def _obv_rel_dist(obv, w):
    """OBV relative distance to its moving average"""
    ma = obv.rolling(w).mean()
    return (obv - ma) / ma.abs().replace(0, np.nan)

# --- Features 076 - 085: Long Window Z-Scores and Smoothings ---

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_504d_v076_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score using closeadj over a very long 504-day window."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_zscore(obv, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_504d_v077_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (closeadj) smoothed with a 504-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_504d_v078_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (closeadj) smoothed with a 504-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_504d_v079_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (closeadj) relative distance to its 504-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_252d_zscore_v080_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 252-day SMA of OBV."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 252)
    res = _obv_zscore(obv_sma, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_21d_rel_dist_10d_v081_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 21-day EMA of OBV to its 10-day SMA."""
    obv = _ema(_obv_calc(close, volume), 21)
    res = _obv_rel_dist(obv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_rel_dist_21d_v082_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 63-day EMA of OBV (closeadj) to its 21-day SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 63)
    res = _obv_rel_dist(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_126d_rel_dist_63d_v083_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 126-day EMA of OBV (closeadj) to its 63-day SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 126)
    res = _obv_rel_dist(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_252d_rel_dist_126d_v084_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 252-day EMA of OBV (closeadj) to its 126-day SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 252)
    res = _obv_rel_dist(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_504d_rel_dist_252d_v085_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 504-day EMA of OBV (closeadj) to its 252-day SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 504)
    res = _obv_rel_dist(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 086 - 095: Advanced OBV Momentum and Volatility ---

def f23obv_f23_on_balance_volume_family_obv_volatility_21d_v086_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of OBV."""
    obv = _obv_calc(close, volume)
    res = obv.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_volatility_63d_v087_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling standard deviation of OBV (closeadj)."""
    obv = _obv_calc(closeadj, volume)
    res = obv.rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_momentum_5d_v088_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV momentum measured as the 5-day difference."""
    obv = _obv_calc(close, volume)
    res = obv.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_momentum_21d_v089_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV momentum measured as the 21-day difference using closeadj."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_momentum_63d_v090_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV momentum measured as the 63-day difference using closeadj."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_momentum_ratio_v091_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day OBV momentum to 21-day OBV momentum."""
    obv = _obv_calc(close, volume)
    res = obv.diff(5) / obv.diff(21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_momentum_ratio_v092_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day OBV momentum to 63-day OBV momentum (closeadj)."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(21) / obv.diff(63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_momentum_zscore_21d_v093_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day OBV momentum over a 21-day window."""
    obv_mom = _obv_calc(close, volume).diff(5)
    res = (obv_mom - obv_mom.rolling(21).mean()) / obv_mom.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_momentum_zscore_63d_v094_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day OBV momentum over a 63-day window."""
    obv_mom = _obv_calc(closeadj, volume).diff(21)
    res = (obv_mom - obv_mom.rolling(63).mean()) / obv_mom.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_momentum_zscore_252d_v095_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day OBV momentum over a 252-day window."""
    obv_mom = _obv_calc(closeadj, volume).diff(63)
    res = (obv_mom - obv_mom.rolling(252).mean()) / obv_mom.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 096 - 105: OBV Relative to Price Dynamics ---

def f23obv_f23_on_balance_volume_family_obv_price_ratio_5d_v096_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV to Price over 5 days."""
    obv = _obv_calc(close, volume)
    res = obv / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_price_ratio_63d_v097_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV to closeadj over 63 days."""
    obv = _obv_calc(closeadj, volume)
    res = obv / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_price_dist_ratio_21d_v098_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV relative distance to Price relative distance over 21 days."""
    obv = _obv_calc(close, volume)
    obv_d = _obv_rel_dist(obv, 21)
    price_ma = close.rolling(21).mean()
    price_d = (close - price_ma) / price_ma.abs().replace(0, np.nan)
    res = obv_d / price_d.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_price_dist_ratio_63d_v099_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV (closeadj) relative distance to Price relative distance over 63 days."""
    obv = _obv_calc(closeadj, volume)
    obv_d = _obv_rel_dist(obv, 63)
    price_ma = closeadj.rolling(63).mean()
    price_d = (closeadj - price_ma) / price_ma.abs().replace(0, np.nan)
    res = obv_d / price_d.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_price_zscore_ratio_21d_v100_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV Z-score to Price Z-score over 21 days."""
    obv = _obv_calc(close, volume)
    obv_z = _obv_zscore(obv, 21)
    price_z = (close - close.rolling(21).mean()) / close.rolling(21).std().replace(0, np.nan)
    res = obv_z / price_z.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_price_zscore_ratio_63d_v101_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV (closeadj) Z-score to Price Z-score over 63 days."""
    obv = _obv_calc(closeadj, volume)
    obv_z = _obv_zscore(obv, 63)
    price_z = (closeadj - closeadj.rolling(63).mean()) / closeadj.rolling(63).std().replace(0, np.nan)
    res = obv_z / price_z.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_price_corr_diff_v102_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day Price-OBV correlation."""
    obv = _obv_calc(close, volume)
    res = close.rolling(5).corr(obv) - close.rolling(21).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_price_corr_diff_v103_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day Price-OBV correlation using closeadj."""
    obv = _obv_calc(closeadj, volume)
    res = closeadj.rolling(21).corr(obv) - closeadj.rolling(63).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_divergence_proxy_5d_v104_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence proxy: 5-day Price ROC minus 5-day OBV ROC (scaled)."""
    obv = _obv_calc(close, volume)
    price_roc = close.pct_change(5)
    obv_roc = obv.diff(5) / obv.abs().rolling(5).mean().replace(0, np.nan)
    res = price_roc - obv_roc
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_divergence_proxy_21d_v105_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence proxy: 21-day closeadj ROC minus 21-day OBV ROC (scaled)."""
    obv = _obv_calc(closeadj, volume)
    price_roc = closeadj.pct_change(21)
    obv_roc = obv.diff(21) / obv.abs().rolling(21).mean().replace(0, np.nan)
    res = price_roc - obv_roc
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 106 - 115: OBV Smoothed with various spans ---

def f23obv_f23_on_balance_volume_family_obv_ema_50d_v106_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 50-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_100d_v107_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 100-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_200d_v108_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 200-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 200)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_50d_v109_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 50-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_100d_v110_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 100-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 100)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_200d_v111_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV smoothed with a 200-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 200)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_cross_v112_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 12-day and 26-day EMA of OBV (MACD style)."""
    obv = _obv_calc(close, volume)
    res = _ema(obv, 12) - _ema(obv, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_cross_v113_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 50-day and 200-day EMA of OBV (Golden Cross style)."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 50) - _ema(obv, 200)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_cross_v114_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 50-day and 200-day SMA of OBV."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 50) - _sma(obv, 200)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_zscore_diff_v115_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day OBV Z-score."""
    obv = _obv_calc(close, volume)
    res = _obv_zscore(obv, 5) - _obv_zscore(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 116 - 125: Long Range OBV Normalizations ---

def f23obv_f23_on_balance_volume_family_obv_adj_range_norm_126d_v116_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (using closeadj) normalized by its 126-day range."""
    obv = _obv_calc(closeadj, volume)
    r = obv.rolling(126).max() - obv.rolling(126).min()
    res = (obv - obv.rolling(126).min()) / r.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_range_norm_252d_v117_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (using closeadj) normalized by its 252-day range."""
    obv = _obv_calc(closeadj, volume)
    r = obv.rolling(252).max() - obv.rolling(252).min()
    res = (obv - obv.rolling(252).min()) / r.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_range_norm_504d_v118_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (using closeadj) normalized by its 504-day range."""
    obv = _obv_calc(closeadj, volume)
    r = obv.rolling(504).max() - obv.rolling(504).min()
    res = (obv - obv.rolling(504).min()) / r.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_126d_v119_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV normalized by its 126-day volume average."""
    obv = _obv_calc(closeadj, volume)
    res = obv / volume.rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_252d_v120_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV normalized by its 252-day volume average."""
    obv = _obv_calc(closeadj, volume)
    res = obv / volume.rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_504d_v121_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV normalized by its 504-day volume average."""
    obv = _obv_calc(closeadj, volume)
    res = obv / volume.rolling(504).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_std_norm_126d_v122_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change normalized by its 126-day standard deviation."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(21) / obv.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_std_norm_252d_v123_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change normalized by its 252-day standard deviation."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63) / obv.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_std_norm_504d_v124_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change normalized by its 504-day standard deviation."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63) / obv.rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_rel_dist_ratio_v125_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day EMA of OBV relative distance to 126-day SMA of OBV relative distance."""
    obv = _obv_calc(closeadj, volume)
    d63 = _obv_rel_dist(_ema(obv, 63), 63)
    d126 = _obv_rel_dist(_sma(obv, 126), 126)
    res = d63 / d126.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 126 - 150: Combinations and Residuals ---

def f23obv_f23_on_balance_volume_family_obv_sma_resid_v126_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of OBV from its 21-day SMA."""
    obv = _obv_calc(close, volume)
    res = obv - _sma(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_resid_v127_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of OBV (closeadj) from its 63-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = obv - _ema(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_resid_126d_v128_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of OBV (closeadj) from its 126-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = obv - _sma(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_vol_weighted_change_5d_v129_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change over 5 days weighted by relative volume."""
    obv = _obv_calc(close, volume)
    rel_vol = volume / volume.rolling(21).mean().replace(0, np.nan)
    res = obv.diff(5) * rel_vol
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_weighted_change_21d_v130_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change over 21 days weighted by relative volume (using closeadj)."""
    obv = _obv_calc(closeadj, volume)
    rel_vol = volume / volume.rolling(63).mean().replace(0, np.nan)
    res = obv.diff(21) * rel_vol
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_vol_weighted_zscore_21d_v131_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV weighted by 21-day relative volume."""
    obv = _obv_calc(close, volume)
    rel_vol = volume / volume.rolling(21).mean().replace(0, np.nan)
    weighted_obv = obv * rel_vol
    res = _obv_zscore(weighted_obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_weighted_zscore_63d_v132_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV (closeadj) weighted by 63-day relative volume."""
    obv = _obv_calc(closeadj, volume)
    rel_vol = volume / volume.rolling(63).mean().replace(0, np.nan)
    weighted_obv = obv * rel_vol
    res = _obv_zscore(weighted_obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_126d_vol_norm_v133_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day EMA of OBV normalized by volume average."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    res = obv_ema / volume.rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_252d_vol_norm_v134_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day EMA of OBV normalized by volume average."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 252)
    res = obv_ema / volume.rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_504d_vol_norm_v135_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """504-day SMA of OBV normalized by volume average."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 504)
    res = obv_sma / volume.rolling(504).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_accel_ratio_v136_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day OBV acceleration to 21-day OBV acceleration."""
    obv = _obv_calc(close, volume)
    accel5 = obv.diff(5).diff(5)
    accel21 = obv.diff(21).diff(21)
    res = accel5 / accel21.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_accel_ratio_v137_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day OBV acceleration to 63-day OBV acceleration."""
    obv = _obv_calc(closeadj, volume)
    accel21 = obv.diff(21).diff(21)
    accel63 = obv.diff(63).diff(63)
    res = accel21 / accel63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_zscore_resid_v138_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of 63-day OBV Z-score from its SMA."""
    obv = _obv_calc(closeadj, volume)
    z = _obv_zscore(obv, 63)
    res = z - _sma(z, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_126d_zscore_resid_v139_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of 126-day OBV Z-score from its SMA."""
    obv = _obv_calc(closeadj, volume)
    z = _obv_zscore(obv, 126)
    res = z - _sma(z, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_252d_zscore_resid_v140_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Residual of 252-day OBV Z-score from its SMA."""
    obv = _obv_calc(closeadj, volume)
    z = _obv_zscore(obv, 252)
    res = z - _sma(z, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_sma_diff_v141_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 63-day and 126-day relative distance of OBV."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 63) - _obv_rel_dist(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_sma_diff_long_v142_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 126-day and 252-day relative distance of OBV."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 126) - _obv_rel_dist(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_sma_diff_vlong_v143_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 252-day and 504-day relative distance of OBV."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 252) - _obv_rel_dist(obv, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_vol_norm_zscore_21d_v144_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV normalized by volume over 21 days."""
    obv = _obv_calc(close, volume)
    norm_obv = obv / volume.rolling(21).mean().replace(0, np.nan)
    res = _obv_zscore(norm_obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_zscore_63d_v145_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV normalized by volume over 63 days."""
    obv = _obv_calc(closeadj, volume)
    norm_obv = obv / volume.rolling(63).mean().replace(0, np.nan)
    res = _obv_zscore(norm_obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_zscore_126d_v146_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV normalized by volume over 126 days."""
    obv = _obv_calc(closeadj, volume)
    norm_obv = obv / volume.rolling(126).mean().replace(0, np.nan)
    res = _obv_zscore(norm_obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_zscore_252d_v147_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV normalized by volume over 252 days."""
    obv = _obv_calc(closeadj, volume)
    norm_obv = obv / volume.rolling(252).mean().replace(0, np.nan)
    res = _obv_zscore(norm_obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_slope_v148_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of 21-day EMA of OBV."""
    obv_ema = _ema(_obv_calc(close, volume), 21)
    res = obv_ema.diff(5) / 5
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_slope_63d_v149_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of 63-day EMA of OBV (closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 63)
    res = obv_ema.diff(21) / 21
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_slope_126d_v150_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of 126-day EMA of OBV (closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    res = obv_ema.diff(21) / 21
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f23obv_") and f.endswith("_signal")]

F23_ON_BALANCE_VOLUME_FAMILY_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 1000
    d = pd.DataFrame({
        "close": np.linspace(100, 200, sz) + np.sin(np.linspace(0, 10, sz)),
        "closeadj": np.linspace(100, 200, sz) + np.sin(np.linspace(0, 10, sz)),
        "volume": np.abs(np.cos(np.linspace(0, 10, sz))) * 1000 + 100,
        "ticker": ["T"]*sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F23_ON_BALANCE_VOLUME_FAMILY_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
