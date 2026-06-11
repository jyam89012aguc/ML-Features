import pandas as pd
import numpy as np

# Helpers
def _sma(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=w//2 if w>1 else 1, adjust=False).mean()
def _z(s, w):
    rolling = s.rolling(w, min_periods=w//2 if w>1 else 1)
    return (s - rolling.mean()) / rolling.std().replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).min()
def _max(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).max()
def _skew(s, w): return s.rolling(w, min_periods=w//2 if w>2 else 3).skew()

# Domain Primitives
def _vol_regime_rank(v, w):
    return v.rolling(w, min_periods=w//2 if w>1 else 1).rank(pct=True)

def _vol_stability(v, w):
    return v.rolling(w, min_periods=w//2 if w>1 else 1).mean() / v.rolling(w, min_periods=w//2 if w>1 else 1).std().replace(0, np.nan)

def _vol_shock_score(v, w):
    return v / v.rolling(w, min_periods=w//2 if w>1 else 1).max().replace(0, np.nan)

# Features 076-090: Volume Volatility Regime
# Stability of volume changes over 21-day window
def f27vr_f27_volume_regime_vol_change_stability_21d_base_v076_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    return _vol_stability(v_diff, 21).replace([np.inf, -np.inf], np.nan)

# Rank of volume changes over 63-day window
def f27vr_f27_volume_regime_vol_change_rank_63d_base_v077_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    return _vol_regime_rank(v_diff, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of volume changes over 21-day window
def f27vr_f27_volume_regime_vol_change_shock_21d_base_v078_signal(volume: pd.Series) -> pd.Series:
    v_diff = volume.diff().abs()
    return _vol_shock_score(v_diff, 21).replace([np.inf, -np.inf], np.nan)

# Stability of volume log returns over 21-day window
def f27vr_f27_volume_regime_vol_logret_stability_21d_base_v079_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_stability(v_logret, 21).replace([np.inf, -np.inf], np.nan)

# Rank of volume log returns over 63-day window
def f27vr_f27_volume_regime_vol_logret_rank_63d_base_v080_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_regime_rank(v_logret, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of volume log returns over 21-day window
def f27vr_f27_volume_regime_vol_logret_shock_21d_base_v081_signal(volume: pd.Series) -> pd.Series:
    v_logret = np.log(volume / volume.shift(1).replace(0, np.nan)).abs()
    return _vol_shock_score(v_logret, 21).replace([np.inf, -np.inf], np.nan)

# Stability of 5-day volume moving average over 42-day window
def f27vr_f27_volume_regime_sma5_stability_42d_base_v082_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 5)
    return _vol_stability(v_sma, 42).replace([np.inf, -np.inf], np.nan)

# Rank of 10-day volume moving average over 63-day window
def f27vr_f27_volume_regime_sma10_rank_63d_base_v083_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 10)
    return _vol_regime_rank(v_sma, 63).replace([np.inf, -np.inf], np.nan)

# Shock score of 21-day volume moving average over 126-day window
def f27vr_f27_volume_regime_sma21_shock_126d_base_v084_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 21)
    return _vol_shock_score(v_sma, 126).replace([np.inf, -np.inf], np.nan)

# Stability of volume z-score (5d) over 63-day window
def f27vr_f27_volume_regime_zscore5_stability_63d_base_v085_signal(volume: pd.Series) -> pd.Series:
    v_z = _z(volume, 5)
    return _vol_stability(v_z, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume z-score (10d) over 126-day window
def f27vr_f27_volume_regime_zscore10_rank_126d_base_v086_signal(volume: pd.Series) -> pd.Series:
    v_z = _z(volume, 10)
    return _vol_regime_rank(v_z, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume z-score (21d) over 252-day window
def f27vr_f27_volume_regime_zscore21_shock_252d_base_v087_signal(volume: pd.Series) -> pd.Series:
    v_z = _z(volume, 21)
    return _vol_shock_score(v_z, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume/closeadj ratio over 63-day window (window > 21)
def f27vr_f27_volume_regime_vol_price_stability_63d_base_v088_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    return _vol_stability(ratio, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume/closeadj ratio over 126-day window (window > 21)
def f27vr_f27_volume_regime_vol_price_rank_126d_base_v089_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    return _vol_regime_rank(ratio, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume/closeadj ratio over 252-day window (window > 21)
def f27vr_f27_volume_regime_vol_price_shock_252d_base_v090_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    ratio = volume / closeadj.replace(0, np.nan)
    return _vol_shock_score(ratio, 252).replace([np.inf, -np.inf], np.nan)

# Features 091-105: Absolute Price-Volume Interactions
# Stability of absolute-dollar-volume (vol * closeadj) over 63d
def f27vr_f27_volume_regime_dollar_vol_stability_63d_base_v091_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    return _vol_stability(dv, 63).replace([np.inf, -np.inf], np.nan)

# Rank of absolute-dollar-volume (vol * closeadj) over 126d
def f27vr_f27_volume_regime_dollar_vol_rank_126d_base_v092_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    return _vol_regime_rank(dv, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of absolute-dollar-volume (vol * closeadj) over 252d
def f27vr_f27_volume_regime_dollar_vol_shock_252d_base_v093_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    dv = volume * closeadj
    return _vol_shock_score(dv, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume during up-days over 63-day window
def f27vr_f27_volume_regime_up_vol_stability_63d_base_v094_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    return _vol_stability(up_vol, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume during up-days over 126-day window
def f27vr_f27_volume_regime_up_vol_rank_126d_base_v095_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    return _vol_regime_rank(up_vol, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume during up-days over 252-day window
def f27vr_f27_volume_regime_up_vol_shock_252d_base_v096_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0)
    return _vol_shock_score(up_vol, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume during down-days over 63-day window
def f27vr_f27_volume_regime_down_vol_stability_63d_base_v097_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    return _vol_stability(dn_vol, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume during down-days over 126-day window
def f27vr_f27_volume_regime_down_vol_rank_126d_base_v098_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    return _vol_regime_rank(dn_vol, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume during down-days over 252-day window
def f27vr_f27_volume_regime_down_vol_shock_252d_base_v099_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    dn_vol = volume.where(close < close.shift(1), 0)
    return _vol_shock_score(dn_vol, 252).replace([np.inf, -np.inf], np.nan)

# Stability of up-vol/down-vol ratio over 63-day window
def f27vr_f27_volume_regime_up_dn_ratio_stability_63d_base_v100_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0).rolling(21).sum()
    dn_vol = volume.where(close < close.shift(1), 0).rolling(21).sum()
    ratio = up_vol / dn_vol.replace(0, np.nan)
    return _vol_stability(ratio, 63).replace([np.inf, -np.inf], np.nan)

# Rank of up-vol/down-vol ratio over 126-day window
def f27vr_f27_volume_regime_up_dn_ratio_rank_126d_base_v101_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0).rolling(21).sum()
    dn_vol = volume.where(close < close.shift(1), 0).rolling(21).sum()
    ratio = up_vol / dn_vol.replace(0, np.nan)
    return _vol_regime_rank(ratio, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of up-vol/down-vol ratio over 252-day window
def f27vr_f27_volume_regime_up_dn_ratio_shock_252d_base_v102_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    up_vol = volume.where(close > close.shift(1), 0).rolling(21).sum()
    dn_vol = volume.where(close < close.shift(1), 0).rolling(21).sum()
    ratio = up_vol / dn_vol.replace(0, np.nan)
    return _vol_shock_score(ratio, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume-weighted-price (VWAP approx) over 63d
def f27vr_f27_volume_regime_vwap_stability_63d_base_v103_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_stability(vwap, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume-weighted-price over 126d
def f27vr_f27_volume_regime_vwap_rank_126d_base_v104_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_regime_rank(vwap, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume-weighted-price over 252d
def f27vr_f27_volume_regime_vwap_shock_252d_base_v105_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwap = (volume * closeadj).rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_shock_score(vwap, 252).replace([np.inf, -np.inf], np.nan)

# Features 106-120: Tail Volume Regimes
# Stability of top 5% volume days over 126-day window
def f27vr_f27_volume_regime_top5_vol_stability_126d_base_v106_signal(volume: pd.Series) -> pd.Series:
    top5 = volume.where(volume > volume.rolling(252).quantile(0.95), 0)
    return _vol_stability(top5, 126).replace([np.inf, -np.inf], np.nan)

# Rank of top 5% volume days over 252-day window
def f27vr_f27_volume_regime_top5_vol_rank_252d_base_v107_signal(volume: pd.Series) -> pd.Series:
    top5 = volume.where(volume > volume.rolling(252).quantile(0.95), 0)
    return _vol_regime_rank(top5, 252).replace([np.inf, -np.inf], np.nan)

# Shock score of top 5% volume days over 63-day window
def f27vr_f27_volume_regime_top5_vol_shock_63d_base_v108_signal(volume: pd.Series) -> pd.Series:
    top5 = volume.where(volume > volume.rolling(252).quantile(0.95), 0)
    return _vol_shock_score(top5, 63).replace([np.inf, -np.inf], np.nan)

# Stability of bottom 5% volume days over 126-day window
def f27vr_f27_volume_regime_bot5_vol_stability_126d_base_v109_signal(volume: pd.Series) -> pd.Series:
    bot5 = volume.where(volume < volume.rolling(252).quantile(0.05), 0)
    return _vol_stability(bot5, 126).replace([np.inf, -np.inf], np.nan)

# Rank of bottom 5% volume days over 252-day window
def f27vr_f27_volume_regime_bot5_vol_rank_252d_base_v110_signal(volume: pd.Series) -> pd.Series:
    bot5 = volume.where(volume < volume.rolling(252).quantile(0.05), 0)
    return _vol_regime_rank(bot5, 252).replace([np.inf, -np.inf], np.nan)

# Shock score of bottom 5% volume days over 63-day window
def f27vr_f27_volume_regime_bot5_vol_shock_63d_base_v111_signal(volume: pd.Series) -> pd.Series:
    bot5 = volume.where(volume < volume.rolling(252).quantile(0.05), 0)
    return _vol_shock_score(bot5, 63).replace([np.inf, -np.inf], np.nan)

# Stability of volume kurtosis over 126-day window
def f27vr_f27_volume_regime_kurt_stability_126d_base_v112_signal(volume: pd.Series) -> pd.Series:
    kurt = volume.rolling(63).kurt()
    return _vol_stability(kurt, 126).replace([np.inf, -np.inf], np.nan)

# Rank of volume kurtosis over 252-day window
def f27vr_f27_volume_regime_kurt_rank_252d_base_v113_signal(volume: pd.Series) -> pd.Series:
    kurt = volume.rolling(63).kurt()
    return _vol_regime_rank(kurt, 252).replace([np.inf, -np.inf], np.nan)

# Shock score of volume kurtosis over 63-day window
def f27vr_f27_volume_regime_kurt_shock_63d_base_v114_signal(volume: pd.Series) -> pd.Series:
    kurt = volume.rolling(63).kurt()
    return _vol_shock_score(kurt, 63).replace([np.inf, -np.inf], np.nan)

# Stability of volume skewness (short-term 21d) over 63d
def f27vr_f27_volume_regime_skew21_stability_63d_base_v115_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 21)
    return _vol_stability(sk, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume skewness (short-term 21d) over 126d
def f27vr_f27_volume_regime_skew21_rank_126d_base_v116_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 21)
    return _vol_regime_rank(sk, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume skewness (short-term 21d) over 42d
def f27vr_f27_volume_regime_skew21_shock_42d_base_v117_signal(volume: pd.Series) -> pd.Series:
    sk = _skew(volume, 21)
    return _vol_shock_score(sk, 42).replace([np.inf, -np.inf], np.nan)

# Stability of volume range (max-min) over 63-day window
def f27vr_f27_volume_regime_vol_range_maxmin_stability_63d_base_v118_signal(volume: pd.Series) -> pd.Series:
    v_range = _max(volume, 21) - _min(volume, 21)
    return _vol_stability(v_range, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume range (max-min) over 126-day window
def f27vr_f27_volume_regime_vol_range_maxmin_rank_126d_base_v119_signal(volume: pd.Series) -> pd.Series:
    v_range = _max(volume, 21) - _min(volume, 21)
    return _vol_regime_rank(v_range, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume range (max-min) over 252-day window
def f27vr_f27_volume_regime_vol_range_maxmin_shock_252d_base_v120_signal(volume: pd.Series) -> pd.Series:
    v_range = _max(volume, 21) - _min(volume, 21)
    return _vol_shock_score(v_range, 252).replace([np.inf, -np.inf], np.nan)

# Features 121-135: Relative Volume Regimes
# Stability of volume relative to sector (proxy: SMA252) over 63d
def f27vr_f27_volume_regime_rel_vol_stability_63d_base_v121_signal(volume: pd.Series) -> pd.Series:
    rel_vol = volume / _sma(volume, 252).replace(0, np.nan)
    return _vol_stability(rel_vol, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume relative to sector (proxy: SMA252) over 126d
def f27vr_f27_volume_regime_rel_vol_rank_126d_base_v122_signal(volume: pd.Series) -> pd.Series:
    rel_vol = volume / _sma(volume, 252).replace(0, np.nan)
    return _vol_regime_rank(rel_vol, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume relative to sector (proxy: SMA252) over 252d
def f27vr_f27_volume_regime_rel_vol_shock_252d_base_v123_signal(volume: pd.Series) -> pd.Series:
    rel_vol = volume / _sma(volume, 252).replace(0, np.nan)
    return _vol_shock_score(rel_vol, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume decay (current / sma21) over 63d
def f27vr_f27_volume_regime_vol_decay_stability_63d_base_v124_signal(volume: pd.Series) -> pd.Series:
    decay = volume / _sma(volume, 21).replace(0, np.nan)
    return _vol_stability(decay, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume decay (current / sma21) over 126d
def f27vr_f27_volume_regime_vol_decay_rank_126d_base_v125_signal(volume: pd.Series) -> pd.Series:
    decay = volume / _sma(volume, 21).replace(0, np.nan)
    return _vol_regime_rank(decay, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume decay (current / sma21) over 252d
def f27vr_f27_volume_regime_vol_decay_shock_252d_base_v126_signal(volume: pd.Series) -> pd.Series:
    decay = volume / _sma(volume, 21).replace(0, np.nan)
    return _vol_shock_score(decay, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume thrust (sum 5d / sum 63d) over 63d
def f27vr_f27_volume_regime_vol_thrust_stability_63d_base_v127_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(5).sum() / volume.rolling(63).sum().replace(0, np.nan)
    return _vol_stability(thrust, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume thrust (sum 5d / sum 63d) over 126d
def f27vr_f27_volume_regime_vol_thrust_rank_126d_base_v128_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(5).sum() / volume.rolling(63).sum().replace(0, np.nan)
    return _vol_regime_rank(thrust, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume thrust (sum 5d / sum 63d) over 252d
def f27vr_f27_volume_regime_vol_thrust_shock_252d_base_v129_signal(volume: pd.Series) -> pd.Series:
    thrust = volume.rolling(5).sum() / volume.rolling(63).sum().replace(0, np.nan)
    return _vol_shock_score(thrust, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume acceleration (slope of sma21) over 63d
def f27vr_f27_volume_regime_vol_accel_stability_63d_base_v130_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 21)
    v_accel = v_sma.diff(5)
    return _vol_stability(v_accel, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume acceleration over 126d
def f27vr_f27_volume_regime_vol_accel_rank_126d_base_v131_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 21)
    v_accel = v_sma.diff(5)
    return _vol_regime_rank(v_accel, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume acceleration over 252d
def f27vr_f27_volume_regime_vol_accel_shock_252d_base_v132_signal(volume: pd.Series) -> pd.Series:
    v_sma = _sma(volume, 21)
    v_accel = v_sma.diff(5)
    return _vol_shock_score(v_accel, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume/ATR ratio over 63-day window
def f27vr_f27_volume_regime_vol_atr_stability_63d_base_v133_signal(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    ratio = volume / atr.replace(0, np.nan)
    return _vol_stability(ratio, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume/ATR ratio over 126-day window
def f27vr_f27_volume_regime_vol_atr_rank_126d_base_v134_signal(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    ratio = volume / atr.replace(0, np.nan)
    return _vol_regime_rank(ratio, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume/ATR ratio over 252-day window
def f27vr_f27_volume_regime_vol_atr_shock_252d_base_v135_signal(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    ratio = volume / atr.replace(0, np.nan)
    return _vol_shock_score(ratio, 252).replace([np.inf, -np.inf], np.nan)

# Features 136-150: Volume-Price Momentum Regimes
# Stability of volume-momentum (vol * ROC5) over 63d
def f27vr_f27_volume_regime_vol_mom_stability_63d_base_v136_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    vm = volume * close.pct_change(5)
    return _vol_stability(vm, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume-momentum (vol * ROC21) over 126d
def f27vr_f27_volume_regime_vol_mom_rank_126d_base_v137_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    vm = volume * close.pct_change(21)
    return _vol_regime_rank(vm, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume-momentum (vol * ROC63) over 252d
def f27vr_f27_volume_regime_vol_mom_shock_252d_base_v138_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vm = volume * closeadj.pct_change(63)
    return _vol_shock_score(vm, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume-weighted-ROC (approx OBV-like) over 63d
def f27vr_f27_volume_regime_vwroc_stability_63d_base_v139_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    vwroc = (volume * np.sign(close.diff())).rolling(21).sum()
    return _vol_stability(vwroc, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume-weighted-ROC over 126d
def f27vr_f27_volume_regime_vwroc_rank_126d_base_v140_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    vwroc = (volume * np.sign(close.diff())).rolling(21).sum()
    return _vol_regime_rank(vwroc, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume-weighted-ROC over 252d
def f27vr_f27_volume_regime_vwroc_shock_252d_base_v141_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    vwroc = (volume * np.sign(closeadj.diff())).rolling(63).sum()
    return _vol_shock_score(vwroc, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume efficiency (abs ROC / sum vol) over 63d
def f27vr_f27_volume_regime_vol_eff_stability_63d_base_v142_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    eff = close.pct_change(21).abs() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_stability(eff, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume efficiency (abs ROC / sum vol) over 126d
def f27vr_f27_volume_regime_vol_eff_rank_126d_base_v143_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    eff = close.pct_change(21).abs() / volume.rolling(21).sum().replace(0, np.nan)
    return _vol_regime_rank(eff, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume efficiency (abs ROC / sum vol) over 252d
def f27vr_f27_volume_regime_vol_eff_shock_252d_base_v144_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    eff = closeadj.pct_change(63).abs() / volume.rolling(63).sum().replace(0, np.nan)
    return _vol_shock_score(eff, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume-price-divergence (vol rank - price rank) over 63d
def f27vr_f27_volume_regime_vp_divergence_stability_63d_base_v145_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    v_rank = _vol_regime_rank(volume, 63)
    p_rank = _vol_regime_rank(closeadj, 63)
    div = v_rank - p_rank
    return _vol_stability(div, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume-price-divergence over 126d
def f27vr_f27_volume_regime_vp_divergence_rank_126d_base_v146_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    v_rank = _vol_regime_rank(volume, 63)
    p_rank = _vol_regime_rank(closeadj, 63)
    div = v_rank - p_rank
    return _vol_regime_rank(div, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume-price-divergence over 252d
def f27vr_f27_volume_regime_vp_divergence_shock_252d_base_v147_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    v_rank = _vol_regime_rank(volume, 252)
    p_rank = _vol_regime_rank(closeadj, 252)
    div = v_rank - p_rank
    return _vol_shock_score(div, 252).replace([np.inf, -np.inf], np.nan)

# Stability of volume-weighted-std (vol * volatility) over 63d
def f27vr_f27_volume_regime_vol_std_stability_63d_base_v148_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    v_std = volume * close.rolling(21).std()
    return _vol_stability(v_std, 63).replace([np.inf, -np.inf], np.nan)

# Rank of volume-weighted-std over 126d
def f27vr_f27_volume_regime_vol_std_rank_126d_base_v149_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    v_std = volume * close.rolling(21).std()
    return _vol_regime_rank(v_std, 126).replace([np.inf, -np.inf], np.nan)

# Shock score of volume-weighted-std over 252d
def f27vr_f27_volume_regime_vol_std_shock_252d_base_v150_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    v_std = volume * closeadj.rolling(63).std()
    return _vol_shock_score(v_std, 252).replace([np.inf, -np.inf], np.nan)

F27_VOLUME_REGIME_BASE_REGISTRY_076_150 = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["volume", "high", "low", "close", "closeadj"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f27vr_f27_volume_regime_")
}

if __name__ == "__main__":
    import numpy as np
    np.random.seed(42)
    n = 1000
    volume = pd.Series(np.random.lognormal(10, 1, n), name="volume")
    close = pd.Series(np.random.normal(100, 5, n), name="close")
    closeadj = close * 1.05
    high = close + np.random.uniform(0, 2, n)
    low = close - np.random.uniform(0, 2, n)
    
    input_map = {"volume": volume, "high": high, "low": low, "close": close, "closeadj": closeadj}
    
    for name, info in F27_VOLUME_REGIME_BASE_REGISTRY_076_150.items():
        func = info["func"]
        inputs = [input_map[arg] for arg in info["inputs"]]
        
        # Determinism check
        y1 = func(*inputs)
        y2 = func(*inputs)
        pd.testing.assert_series_equal(y1, y2)
        
        # Non-trivial output check
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, f"Feature {name} returned all NaNs after warmup"
        print(f"Feature {name}: OK")
