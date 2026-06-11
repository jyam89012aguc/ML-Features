# f11_raw_roc_family_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _raw_roc(price, w):
    return (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
def _log_roc(price, w):
    return np.log(price / price.shift(w).replace(0, np.nan))
def _roc_zscore(price, w, lookback):
    roc = (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
    return (roc - roc.rolling(lookback).mean()) / roc.rolling(lookback).std().replace(0, np.nan)

# ROC of 5d Raw ROC (ROC Acceleration)
def f11rf_f11_raw_roc_family_roc_accel_5d_base_v076_signal(close: pd.Series) -> pd.Series:
    roc = _raw_roc(close, 5)
    res = _raw_roc(roc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 10d Raw ROC (ROC Acceleration)
def f11rf_f11_raw_roc_family_roc_accel_10d_base_v077_signal(close: pd.Series) -> pd.Series:
    roc = _raw_roc(close, 10)
    res = _raw_roc(roc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 21d Raw ROC (ROC Acceleration)
def f11rf_f11_raw_roc_family_roc_accel_21d_base_v078_signal(close: pd.Series) -> pd.Series:
    roc = _raw_roc(close, 21)
    res = _raw_roc(roc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 63d Raw ROC (ROC Acceleration, using closeadj)
def f11rf_f11_raw_roc_family_roc_accel_63d_base_v079_signal(closeadj: pd.Series) -> pd.Series:
    roc = _raw_roc(closeadj, 63)
    res = _raw_roc(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 5d Volatility (Standard Deviation)
def f11rf_f11_raw_roc_family_vol_roc_5d_base_v080_signal(close: pd.Series) -> pd.Series:
    vol = close.rolling(5).std()
    res = _raw_roc(vol, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 21d Volatility (Standard Deviation)
def f11rf_f11_raw_roc_family_vol_roc_21d_base_v081_signal(close: pd.Series) -> pd.Series:
    vol = close.rolling(21).std()
    res = _raw_roc(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC of 63d Volatility (Standard Deviation, using closeadj)
def f11rf_f11_raw_roc_family_vol_roc_63d_base_v082_signal(closeadj: pd.Series) -> pd.Series:
    vol = closeadj.rolling(63).std()
    res = _raw_roc(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of High-Low Range
def f11rf_f11_raw_roc_family_range_roc_5d_base_v083_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    rng = high - low
    res = _raw_roc(rng, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of High-Low Range
def f11rf_f11_raw_roc_family_range_roc_21d_base_v084_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    rng = high - low
    res = _raw_roc(rng, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 63d of High-Low Range (using closeadj-adjusted)
def f11rf_f11_raw_roc_family_range_roc_63d_base_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rng = (high * adj) - (low * adj)
    res = _raw_roc(rng, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Close - Low) / (High - Low) - Donchian Position
def f11rf_f11_raw_roc_family_donchian_pos_roc_5d_base_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h5, l5 = high.rolling(5).max(), low.rolling(5).min()
    pos = (close - l5) / (h5 - l5).replace(0, np.nan)
    res = _raw_roc(pos, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Donchian Position
def f11rf_f11_raw_roc_family_donchian_pos_roc_21d_base_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h21, l21 = high.rolling(21).max(), low.rolling(21).min()
    pos = (close - l21) / (h21 - l21).replace(0, np.nan)
    res = _raw_roc(pos, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Volume / 21d SMA Volume
def f11rf_f11_raw_roc_family_vol_rel_roc_5d_base_v088_signal(volume: pd.Series) -> pd.Series:
    vol_rel = volume / _sma(volume, 21).replace(0, np.nan)
    res = _raw_roc(vol_rel, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Volume / 63d SMA Volume
def f11rf_f11_raw_roc_family_vol_rel_roc_21d_base_v089_signal(volume: pd.Series) -> pd.Series:
    vol_rel = volume / _sma(volume, 63).replace(0, np.nan)
    res = _raw_roc(vol_rel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 5d of SMA 5 / SMA 21
def f11rf_f11_raw_roc_family_ma_ratio_log_roc_5d_base_v090_signal(close: pd.Series) -> pd.Series:
    ratio = _sma(close, 5) / _sma(close, 21).replace(0, np.nan)
    res = _log_roc(ratio, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 21d of SMA 21 / SMA 63
def f11rf_f11_raw_roc_family_ma_ratio_log_roc_21d_base_v091_signal(close: pd.Series) -> pd.Series:
    ratio = _sma(close, 21) / _sma(close, 63).replace(0, np.nan)
    res = _log_roc(ratio, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 63d of SMA 63 / SMA 252 (using closeadj)
def f11rf_f11_raw_roc_family_ma_ratio_log_roc_63d_base_v092_signal(closeadj: pd.Series) -> pd.Series:
    ratio = _sma(closeadj, 63) / _sma(closeadj, 252).replace(0, np.nan)
    res = _log_roc(ratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Price minus 252d Low
def f11rf_f11_raw_roc_family_price_dist_low_roc_5d_base_v093_signal(close: pd.Series) -> pd.Series:
    low252 = close.rolling(252).min()
    dist = close - low252
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of 252d High minus Price
def f11rf_f11_raw_roc_family_price_dist_high_roc_5d_base_v094_signal(close: pd.Series) -> pd.Series:
    high252 = close.rolling(252).max()
    dist = high252 - close
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Price / 252d SMA (Distance from SMA)
def f11rf_f11_raw_roc_family_sma_dist_roc_21d_base_v095_signal(closeadj: pd.Series) -> pd.Series:
    dist = closeadj / _sma(closeadj, 252).replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 1d of Log ROC 5d
def f11rf_f11_raw_roc_family_log_roc_5d_roc_1d_base_v096_signal(close: pd.Series) -> pd.Series:
    roc5 = _log_roc(close, 5)
    res = _raw_roc(roc5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Log ROC 21d
def f11rf_f11_raw_roc_family_log_roc_21d_roc_5d_base_v097_signal(close: pd.Series) -> pd.Series:
    roc21 = _log_roc(close, 21)
    res = _raw_roc(roc21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Log ROC 63d (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_63d_roc_21d_base_v098_signal(closeadj: pd.Series) -> pd.Series:
    roc63 = _log_roc(closeadj, 63)
    res = _raw_roc(roc63, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d Raw ROC with 252d lookback

# Z-score of 21d Raw ROC with 252d lookback

# Raw ROC 5d of (EMA 10 - EMA 50) - MACD-like
def f11rf_f11_raw_roc_family_macd_roc_5d_base_v101_signal(close: pd.Series) -> pd.Series:
    macd = _ema(close, 10) - _ema(close, 50)
    res = _raw_roc(macd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (EMA 10 - EMA 50)
def f11rf_f11_raw_roc_family_macd_roc_21d_base_v102_signal(close: pd.Series) -> pd.Series:
    macd = _ema(close, 10) - _ema(close, 50)
    res = _raw_roc(macd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Price - SMA 20) / STD 20 - Bollinger Position
def f11rf_f11_raw_roc_family_bb_pos_roc_5d_base_v103_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 20)
    std = close.rolling(20).std()
    pos = (close - ma) / std.replace(0, np.nan)
    res = _raw_roc(pos, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Bollinger Position
def f11rf_f11_raw_roc_family_bb_pos_roc_21d_base_v104_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 20)
    std = close.rolling(20).std()
    pos = (close - ma) / std.replace(0, np.nan)
    res = _raw_roc(pos, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of RSI 14
def f11rf_f11_raw_roc_family_rsi_roc_5d_base_v105_signal(close: pd.Series) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0).rolling(14).mean()
    down = -delta.clip(upper=0).rolling(14).mean()
    rsi = 100 - (100 / (1 + (up / down.replace(0, np.nan)).replace(np.nan, 0)))
    res = _raw_roc(rsi, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of RSI 14
def f11rf_f11_raw_roc_family_rsi_roc_21d_base_v106_signal(close: pd.Series) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0).rolling(14).mean()
    down = -delta.clip(upper=0).rolling(14).mean()
    rsi = 100 - (100 / (1 + (up / down.replace(0, np.nan)).replace(np.nan, 0)))
    res = _raw_roc(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 5d of typical price (H+L+C)/3
def f11rf_f11_raw_roc_family_typical_price_log_roc_5d_base_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3
    res = _log_roc(tp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 21d of typical price
def f11rf_f11_raw_roc_family_typical_price_log_roc_21d_base_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3
    res = _log_roc(tp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Money Flow Index (approx)
def f11rf_f11_raw_roc_family_mfi_roc_5d_base_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3
    mf = tp * volume
    res = _raw_roc(mf.rolling(14).sum(), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Money Flow Index (approx)
def f11rf_f11_raw_roc_family_mfi_roc_21d_base_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3
    mf = tp * volume
    res = _raw_roc(mf.rolling(14).sum(), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Williams %R 14
def f11rf_f11_raw_roc_family_willr_roc_5d_base_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h14, l14 = high.rolling(14).max(), low.rolling(14).min()
    wr = (h14 - close) / (h14 - l14).replace(0, np.nan) * -100
    res = _raw_roc(wr, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Williams %R 14
def f11rf_f11_raw_roc_family_willr_roc_21d_base_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h14, l14 = high.rolling(14).max(), low.rolling(14).min()
    wr = (h14 - close) / (h14 - l14).replace(0, np.nan) * -100
    res = _raw_roc(wr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of ATR 14 / Price
def f11rf_f11_raw_roc_family_atr_price_roc_5d_base_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr14 = _sma(tr, 14)
    res = _raw_roc(atr14 / close.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of ATR 14 / Price
def f11rf_f11_raw_roc_family_atr_price_roc_21d_base_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr14 = _sma(tr, 14)
    res = _raw_roc(atr14 / close.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of ADX 14 (approx)
def f11rf_f11_raw_roc_family_adx_roc_5d_base_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    up = high.diff(); down = -low.diff()
    plus_dm = up.where((up > down) & (up > 0), 0)
    minus_dm = down.where((down > up) & (down > 0), 0)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr14 = _sma(tr, 14)
    plus_di = 100 * _sma(plus_dm, 14) / atr14.replace(0, np.nan)
    minus_di = 100 * _sma(minus_dm, 14) / atr14.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = _sma(dx, 14)
    res = _raw_roc(adx, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of ADX 14
def f11rf_f11_raw_roc_family_adx_roc_21d_base_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    up = high.diff(); down = -low.diff()
    plus_dm = up.where((up > down) & (up > 0), 0)
    minus_dm = down.where((down > up) & (down > 0), 0)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr14 = _sma(tr, 14)
    plus_di = 100 * _sma(plus_dm, 14) / atr14.replace(0, np.nan)
    minus_di = 100 * _sma(minus_dm, 14) / atr14.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = _sma(dx, 14)
    res = _raw_roc(adx, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of OBV
def f11rf_f11_raw_roc_family_obv_roc_5d_base_v117_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = (np.sign(close.diff()) * volume).fillna(0).cumsum()
    res = _raw_roc(obv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of OBV
def f11rf_f11_raw_roc_family_obv_roc_21d_base_v118_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = (np.sign(close.diff()) * volume).fillna(0).cumsum()
    res = _raw_roc(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Chaikin Volatility
def f11rf_f11_raw_roc_family_chaikin_vol_roc_5d_base_v119_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl_ema = _ema(high - low, 10)
    cvol = (hl_ema - hl_ema.shift(10)) / hl_ema.shift(10).replace(0, np.nan)
    res = _raw_roc(cvol, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Chaikin Volatility
def f11rf_f11_raw_roc_family_chaikin_vol_roc_21d_base_v120_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl_ema = _ema(high - low, 10)
    cvol = (hl_ema - hl_ema.shift(10)) / hl_ema.shift(10).replace(0, np.nan)
    res = _raw_roc(cvol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Price / 52-week High
def f11rf_f11_raw_roc_family_price_52wh_roc_5d_base_v121_signal(closeadj: pd.Series) -> pd.Series:
    h52 = closeadj.rolling(252).max()
    res = _raw_roc(closeadj / h52.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Price / 52-week High
def f11rf_f11_raw_roc_family_price_52wh_roc_21d_base_v122_signal(closeadj: pd.Series) -> pd.Series:
    h52 = closeadj.rolling(252).max()
    res = _raw_roc(closeadj / h52.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Price / 52-week Low
def f11rf_f11_raw_roc_family_price_52wl_roc_5d_base_v123_signal(closeadj: pd.Series) -> pd.Series:
    l52 = closeadj.rolling(252).min()
    res = _raw_roc(closeadj / l52.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Price / 52-week Low
def f11rf_f11_raw_roc_family_price_52wl_roc_21d_base_v124_signal(closeadj: pd.Series) -> pd.Series:
    l52 = closeadj.rolling(252).min()
    res = _raw_roc(closeadj / l52.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Close - Open) / (High - Low)
def f11rf_f11_raw_roc_family_candle_body_roc_5d_base_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open) / (high - low).replace(0, np.nan)
    res = _raw_roc(body, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Candle Body
def f11rf_f11_raw_roc_family_candle_body_roc_21d_base_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open) / (high - low).replace(0, np.nan)
    res = _raw_roc(body, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Volume / SMA(Volume, 5)
def f11rf_f11_raw_roc_family_vol_sma_ratio_roc_5d_base_v127_signal(volume: pd.Series) -> pd.Series:
    ratio = volume / _sma(volume, 5).replace(0, np.nan)
    res = _raw_roc(ratio, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Volume / SMA(Volume, 21)
def f11rf_f11_raw_roc_family_vol_sma_ratio_roc_21d_base_v128_signal(volume: pd.Series) -> pd.Series:
    ratio = volume / _sma(volume, 21).replace(0, np.nan)
    res = _raw_roc(ratio, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (SMA 5 - SMA 20) / SMA 20
def f11rf_f11_raw_roc_family_ma_cross_roc_5d_base_v129_signal(close: pd.Series) -> pd.Series:
    cross = (_sma(close, 5) - _sma(close, 20)) / _sma(close, 20).replace(0, np.nan)
    res = _raw_roc(cross, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (SMA 5 - SMA 20) / SMA 20
def f11rf_f11_raw_roc_family_ma_cross_roc_21d_base_v130_signal(close: pd.Series) -> pd.Series:
    cross = (_sma(close, 5) - _sma(close, 20)) / _sma(close, 20).replace(0, np.nan)
    res = _raw_roc(cross, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Price / EMA 200 (using closeadj)
def f11rf_f11_raw_roc_family_ema200_dist_roc_5d_base_v131_signal(closeadj: pd.Series) -> pd.Series:
    dist = closeadj / _ema(closeadj, 200).replace(0, np.nan)
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Price / EMA 200
def f11rf_f11_raw_roc_family_ema200_dist_roc_21d_base_v132_signal(closeadj: pd.Series) -> pd.Series:
    dist = closeadj / _ema(closeadj, 200).replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (High - Low) / Close
def f11rf_f11_raw_roc_family_volatility_prox_roc_5d_base_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol = (high - low) / close.replace(0, np.nan)
    res = _raw_roc(vol, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (High - Low) / Close
def f11rf_f11_raw_roc_family_volatility_prox_roc_21d_base_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol = (high - low) / close.replace(0, np.nan)
    res = _raw_roc(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of SMA(Close, 5) / EMA(Close, 5)
def f11rf_f11_raw_roc_family_sma_ema_ratio_roc_5d_base_v135_signal(close: pd.Series) -> pd.Series:
    ratio = _sma(close, 5) / _ema(close, 5).replace(0, np.nan)
    res = _raw_roc(ratio, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of SMA(Close, 21) / EMA(Close, 21)
def f11rf_f11_raw_roc_family_sma_ema_ratio_roc_21d_base_v136_signal(close: pd.Series) -> pd.Series:
    ratio = _sma(close, 21) / _ema(close, 21).replace(0, np.nan)
    res = _raw_roc(ratio, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Close - SMA 252) / SMA 252
def f11rf_f11_raw_roc_family_sma252_dist_roc_5d_base_v137_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    dist = (closeadj - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (Close - SMA 252) / SMA 252
def f11rf_f11_raw_roc_family_sma252_dist_roc_21d_base_v138_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    dist = (closeadj - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Close - EMA 100) / EMA 100
def f11rf_f11_raw_roc_family_ema100_dist_roc_5d_base_v139_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 100)
    dist = (closeadj - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (Close - EMA 100) / EMA 100
def f11rf_f11_raw_roc_family_ema100_dist_roc_21d_base_v140_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 100)
    dist = (closeadj - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Standard Deviation of Volume 21d
def f11rf_f11_raw_roc_family_vol_std_roc_5d_base_v141_signal(volume: pd.Series) -> pd.Series:
    res = _raw_roc(volume.rolling(21).std(), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Standard Deviation of Volume 63d
def f11rf_f11_raw_roc_family_vol_std_roc_21d_base_v142_signal(volume: pd.Series) -> pd.Series:
    res = _raw_roc(volume.rolling(63).std(), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (High - EMA 21) / EMA 21
def f11rf_f11_raw_roc_family_high_ema_dist_roc_5d_base_v143_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    dist = (high - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (High - EMA 21) / EMA 21
def f11rf_f11_raw_roc_family_high_ema_dist_roc_21d_base_v144_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    dist = (high - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of (Low - EMA 21) / EMA 21
def f11rf_f11_raw_roc_family_low_ema_dist_roc_5d_base_v145_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    dist = (low - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of (Low - EMA 21) / EMA 21
def f11rf_f11_raw_roc_family_low_ema_dist_roc_21d_base_v146_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    dist = (low - ma) / ma.replace(0, np.nan)
    res = _raw_roc(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of SMA(Volume, 5) / SMA(Volume, 252)
def f11rf_f11_raw_roc_family_vol_ma_ratio_roc_5d_base_v147_signal(volume: pd.Series) -> pd.Series:
    ratio = _sma(volume, 5) / _sma(volume, 252).replace(0, np.nan)
    res = _raw_roc(ratio, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of SMA(Volume, 21) / SMA(Volume, 252)
def f11rf_f11_raw_roc_family_vol_ma_ratio_roc_21d_base_v148_signal(volume: pd.Series) -> pd.Series:
    ratio = _sma(volume, 21) / _sma(volume, 252).replace(0, np.nan)
    res = _raw_roc(ratio, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of ATR 21 / SMA(ATR 21, 252)
def f11rf_f11_raw_roc_family_atr_norm_roc_5d_base_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    norm_atr = atr / _sma(atr, 252).replace(0, np.nan)
    res = _raw_roc(norm_atr, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of ATR 21 / SMA(ATR 21, 252)
def f11rf_f11_raw_roc_family_atr_norm_roc_21d_base_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    norm_atr = atr / _sma(atr, 252).replace(0, np.nan)
    res = _raw_roc(norm_atr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f11rf_") and f.endswith("_signal")]

F11_RAW_ROC_FAMILY_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"open": np.random.randn(sz).cumsum()+100, "close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.randn(sz).cumsum()+1000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F11_RAW_ROC_FAMILY_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
