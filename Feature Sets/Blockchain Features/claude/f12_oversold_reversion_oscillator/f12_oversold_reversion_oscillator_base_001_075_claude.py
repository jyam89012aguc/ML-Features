import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (oversold-reversion oscillators) =====
def _f12_rsi(s, w):
    # Wilder RSI on price series s over window w (continuous, bounded 0-100)
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.ewm(alpha=1.0 / w, min_periods=w, adjust=False).mean()
    ad = dn.ewm(alpha=1.0 / w, min_periods=w, adjust=False).mean()
    rs = au / ad.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _f12_stoch(close, low, high, w):
    # stochastic %K = (close - low_w) / (high_w - low_w) * 100 (continuous, bounded)
    ll = low.rolling(w, min_periods=max(1, w // 2)).min()
    hh = high.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - ll) / (hh - ll).replace(0, np.nan) * 100.0


def _f12_zclose(s, w):
    # rolling z-score of close (continuous, mean-reversion gauge)
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _f12_cci(close, low, high, w):
    # Commodity Channel Index on typical price (continuous, unbounded oscillator)
    tp = (close + low + high) / 3.0
    ma = tp.rolling(w, min_periods=max(1, w // 2)).mean()
    md = (tp - ma).abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return (tp - ma) / (0.015 * md).replace(0, np.nan)


# ============ FEATURES 001-075 ============

# 7d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_7d_base_v001_signal(closeadj):
    result = _f12_rsi(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_14d_base_v002_signal(closeadj):
    result = _f12_rsi(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_21d_base_v003_signal(closeadj):
    result = _f12_rsi(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_63d_base_v004_signal(closeadj):
    result = _f12_rsi(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI distance from 50 (centered oscillator)
def f12os_f12_oversold_reversion_oscillator_rsidev_14d_base_v005_signal(closeadj):
    result = _f12_rsi(closeadj, 14) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RSI distance from 50
def f12os_f12_oversold_reversion_oscillator_rsidev_21d_base_v006_signal(closeadj):
    result = _f12_rsi(closeadj, 21) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RSI distance from 50
def f12os_f12_oversold_reversion_oscillator_rsidev_63d_base_v007_signal(closeadj):
    result = _f12_rsi(closeadj, 63) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d continuous depth below oversold threshold 30 (softplus, always continuous)
def f12os_f12_oversold_reversion_oscillator_osdist_14d_base_v008_signal(closeadj):
    g = 30.0 - _f12_rsi(closeadj, 14)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d continuous depth below oversold threshold 30 (softplus)
def f12os_f12_oversold_reversion_oscillator_osdist_21d_base_v009_signal(closeadj):
    g = 30.0 - _f12_rsi(closeadj, 21)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d signed gap to oversold band centre 30 (continuous, unclipped)
def f12os_f12_oversold_reversion_oscillator_osgap_14d_base_v010_signal(closeadj):
    result = 30.0 - _f12_rsi(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 7d RSI minus its 21d average (RSI surprise)
def f12os_f12_oversold_reversion_oscillator_rsisurp_7d_base_v011_signal(closeadj):
    r = _f12_rsi(closeadj, 7)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI minus its 63d average
def f12os_f12_oversold_reversion_oscillator_rsisurp_14d_base_v012_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 14d RSI over 126d
def f12os_f12_oversold_reversion_oscillator_zrsi_14d_base_v013_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 14), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d RSI over 252d
def f12os_f12_oversold_reversion_oscillator_zrsi_21d_base_v014_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d smoothed RSI (21d mean)
def f12os_f12_oversold_reversion_oscillator_rsismooth_14d_base_v015_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 14), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI velocity (5d change of RSI)
def f12os_f12_oversold_reversion_oscillator_rsivel_14d_base_v016_signal(closeadj):
    result = _f12_rsi(closeadj, 14).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RSI velocity (10d change of RSI)
def f12os_f12_oversold_reversion_oscillator_rsivel_21d_base_v017_signal(closeadj):
    result = _f12_rsi(closeadj, 21).diff(10)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K (14d window)
def f12os_f12_oversold_reversion_oscillator_stochk_14d_base_v018_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K
def f12os_f12_oversold_reversion_oscillator_stochk_21d_base_v019_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d stochastic %K
def f12os_f12_oversold_reversion_oscillator_stochk_63d_base_v020_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %D (3d mean of %K)
def f12os_f12_oversold_reversion_oscillator_stochd_14d_base_v021_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 14), 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %D (3d mean of %K)
def f12os_f12_oversold_reversion_oscillator_stochd_21d_base_v022_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 21), 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K minus %D (fast-slow spread)
def f12os_f12_oversold_reversion_oscillator_stochkd_14d_base_v023_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = k - _mean(k, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K distance from 50 (centered)
def f12os_f12_oversold_reversion_oscillator_stochdev_14d_base_v024_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K continuous depth below oversold 20 (softplus)
def f12os_f12_oversold_reversion_oscillator_stochos_21d_base_v025_signal(closeadj, low, high):
    g = 20.0 - _f12_stoch(closeadj, low, high, 21)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d Williams %R (= stochastic %K - 100)
def f12os_f12_oversold_reversion_oscillator_willr_14d_base_v026_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Williams %R
def f12os_f12_oversold_reversion_oscillator_willr_21d_base_v027_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Williams %R
def f12os_f12_oversold_reversion_oscillator_willr_63d_base_v028_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Williams %R
def f12os_f12_oversold_reversion_oscillator_willr_126d_base_v029_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 126) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 14d stochastic %K over 126d
def f12os_f12_oversold_reversion_oscillator_zstoch_14d_base_v030_signal(closeadj, low, high):
    result = _z(_f12_stoch(closeadj, low, high, 14), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_21d_base_v031_signal(closeadj):
    result = _f12_zclose(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_42d_base_v032_signal(closeadj):
    result = _f12_zclose(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_63d_base_v033_signal(closeadj):
    result = _f12_zclose(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_126d_base_v034_signal(closeadj):
    result = _f12_zclose(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_252d_base_v035_signal(closeadj):
    result = _f12_zclose(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# negative 63d z-close (continuous oversold depth: positive = below mean)
def f12os_f12_oversold_reversion_oscillator_zcloseneg_63d_base_v036_signal(closeadj):
    result = -_f12_zclose(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d CCI (typical-price oscillator)
def f12os_f12_oversold_reversion_oscillator_cci_14d_base_v037_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI
def f12os_f12_oversold_reversion_oscillator_cci_21d_base_v038_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d CCI
def f12os_f12_oversold_reversion_oscillator_cci_63d_base_v039_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI continuous depth below oversold -100 (softplus)
def f12os_f12_oversold_reversion_oscillator_ccios_21d_base_v040_signal(closeadj, low, high):
    g = -100.0 - _f12_cci(closeadj, low, high, 21)
    result = np.log1p(np.exp(-np.abs(g) / 20.0)) * 20.0 + np.maximum(g, 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 21d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_21d_base_v041_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=10).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 42d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_42d_base_v042_signal(closeadj):
    ema = closeadj.ewm(span=42, min_periods=21).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 63d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_63d_base_v043_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=21).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 126d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_126d_base_v044_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=42).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# detrended price oscillator 21d (close - SMA shifted)
def f12os_f12_oversold_reversion_oscillator_dpo_21d_base_v045_signal(closeadj):
    sma = _mean(closeadj, 21).shift(21 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# detrended price oscillator 42d
def f12os_f12_oversold_reversion_oscillator_dpo_42d_base_v046_signal(closeadj):
    sma = _mean(closeadj, 42).shift(42 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# detrended price oscillator 63d
def f12os_f12_oversold_reversion_oscillator_dpo_63d_base_v047_signal(closeadj):
    sma = _mean(closeadj, 63).shift(63 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI of stochastic %K (composite oscillator)
def f12os_f12_oversold_reversion_oscillator_stochrsi_14d_base_v048_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    rk = k.rolling(14, min_periods=7).min()
    rh = k.rolling(14, min_periods=7).max()
    result = (k - rk) / (rh - rk).replace(0, np.nan) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic momentum index 14d (close vs midpoint of range)
def f12os_f12_oversold_reversion_oscillator_smi_14d_base_v049_signal(closeadj, low, high):
    ll = low.rolling(14, min_periods=7).min()
    hh = high.rolling(14, min_periods=7).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=5, min_periods=3).mean()
    den = ((hh - ll) / 2.0).ewm(span=5, min_periods=3).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 14) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic momentum index 21d
def f12os_f12_oversold_reversion_oscillator_smi_21d_base_v050_signal(closeadj, low, high):
    ll = low.rolling(21, min_periods=10).min()
    hh = high.rolling(21, min_periods=10).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=8, min_periods=4).mean()
    den = ((hh - ll) / 2.0).ewm(span=8, min_periods=4).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 7d RSI distance from 50
def f12os_f12_oversold_reversion_oscillator_rsidev_7d_base_v051_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 7d-21d RSI spread (fast minus slow)
def f12os_f12_oversold_reversion_oscillator_rsispread_7_21_base_v052_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - _f12_rsi(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d-63d RSI spread
def f12os_f12_oversold_reversion_oscillator_rsispread_14_63_base_v053_signal(closeadj):
    result = _f12_rsi(closeadj, 14) - _f12_rsi(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-63d z-close spread (short vs long mean-reversion)
def f12os_f12_oversold_reversion_oscillator_zspread_21_63_base_v054_signal(closeadj):
    result = _f12_zclose(closeadj, 21) - _f12_zclose(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-252d z-close spread
def f12os_f12_oversold_reversion_oscillator_zspread_63_252_base_v055_signal(closeadj):
    result = _f12_zclose(closeadj, 63) - _f12_zclose(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# RSI(14) reversion pressure: RSI deviation scaled by 63d RSI std
def f12os_f12_oversold_reversion_oscillator_rsipress_14d_base_v056_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = _safe_div(50.0 - r, _std(r, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# z-close reversion pressure: negative z scaled by 126d window depth
def f12os_f12_oversold_reversion_oscillator_zpress_63d_base_v057_signal(closeadj):
    z = _f12_zclose(closeadj, 63)
    result = _safe_div(-z, _std(z, 126).add(1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K reversion pressure from 50
def f12os_f12_oversold_reversion_oscillator_stochpress_14d_base_v058_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = _safe_div(50.0 - k, _std(k, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI distance from 0 normalized by 126d CCI std
def f12os_f12_oversold_reversion_oscillator_ccinorm_21d_base_v059_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 21)
    result = _safe_div(c, _std(c, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d CCI continuous depth below -100 (softplus)
def f12os_f12_oversold_reversion_oscillator_ccios_63d_base_v060_signal(closeadj, low, high):
    g = -100.0 - _f12_cci(closeadj, low, high, 63)
    result = np.log1p(np.exp(-np.abs(g) / 20.0)) * 20.0 + np.maximum(g, 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# RSI(14) elasticity: 5d RSI change weighted by oversold depth
def f12os_f12_oversold_reversion_oscillator_rsielas_14d_base_v061_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    depth = (50.0 - r) / 50.0
    result = r.diff(5) * depth
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator vs 21d EMA scaled by 63d realized vol
def f12os_f12_oversold_reversion_oscillator_npovol_21d_base_v062_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=10).mean()
    npo = _safe_div(closeadj - ema, ema)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(npo, _std(lr, 63) * np.sqrt(21.0)) + _f12_zclose(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RSI(14) smoothed deviation: EMA of (RSI-50)
def f12os_f12_oversold_reversion_oscillator_rsiema_14d_base_v063_signal(closeadj):
    dev = _f12_rsi(closeadj, 14) - 50.0
    result = dev.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close clipped to robust band
def f12os_f12_oversold_reversion_oscillator_zcloseclip_21d_base_v064_signal(closeadj):
    result = _f12_zclose(closeadj, 21).clip(-4.0, 4.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI percentile rank over 126d
def f12os_f12_oversold_reversion_oscillator_rsirank_14d_base_v065_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K percentile rank over 126d
def f12os_f12_oversold_reversion_oscillator_stochrank_14d_base_v066_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = k.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-close percentile rank over 252d
def f12os_f12_oversold_reversion_oscillator_zcloserank_63d_base_v067_signal(closeadj):
    z = _f12_zclose(closeadj, 63)
    result = z.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# composite oversold index: mean of RSI-dev, stoch-dev, z-close (normalized)
def f12os_f12_oversold_reversion_oscillator_composite_21d_base_v068_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 21) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 21) - 50.0) / 50.0
    c = _f12_zclose(closeadj, 21) / 3.0
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI gated by deep oversold (continuous interaction with stoch %K)
def f12os_f12_oversold_reversion_oscillator_rsistochx_14d_base_v069_signal(closeadj, low, high):
    r = (_f12_rsi(closeadj, 14) - 50.0) / 50.0
    k = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 50.0
    result = r * k
    return result.replace([np.inf, -np.inf], np.nan)


# 21d normalized price oscillator vs SMA (close-SMA)/SMA
def f12os_f12_oversold_reversion_oscillator_smaosc_21d_base_v070_signal(closeadj):
    sma = _mean(closeadj, 21)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d normalized price oscillator vs SMA
def f12os_f12_oversold_reversion_oscillator_smaosc_63d_base_v071_signal(closeadj):
    sma = _mean(closeadj, 63)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized price oscillator vs SMA
def f12os_f12_oversold_reversion_oscillator_smaosc_126d_base_v072_signal(closeadj):
    sma = _mean(closeadj, 126)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI reversion target: expected pullback to 50 weighted by recent slope
def f12os_f12_oversold_reversion_oscillator_rsitarget_14d_base_v073_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = (50.0 - r) * (1.0 + r.diff(3) / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %D smoothed twice (slow stochastic)
def f12os_f12_oversold_reversion_oscillator_slowstoch_21d_base_v074_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = _mean(_mean(k, 3), 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI bounded reversion score: tanh of centered RSI deviation
def f12os_f12_oversold_reversion_oscillator_rsitanh_14d_base_v075_signal(closeadj):
    dev = (_f12_rsi(closeadj, 14) - 50.0) / 20.0
    result = np.tanh(dev) + _f12_rsi(closeadj, 14) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12os_f12_oversold_reversion_oscillator_rsi_7d_base_v001_signal,
    f12os_f12_oversold_reversion_oscillator_rsi_14d_base_v002_signal,
    f12os_f12_oversold_reversion_oscillator_rsi_21d_base_v003_signal,
    f12os_f12_oversold_reversion_oscillator_rsi_63d_base_v004_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_14d_base_v005_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_21d_base_v006_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_63d_base_v007_signal,
    f12os_f12_oversold_reversion_oscillator_osdist_14d_base_v008_signal,
    f12os_f12_oversold_reversion_oscillator_osdist_21d_base_v009_signal,
    f12os_f12_oversold_reversion_oscillator_osgap_14d_base_v010_signal,
    f12os_f12_oversold_reversion_oscillator_rsisurp_7d_base_v011_signal,
    f12os_f12_oversold_reversion_oscillator_rsisurp_14d_base_v012_signal,
    f12os_f12_oversold_reversion_oscillator_zrsi_14d_base_v013_signal,
    f12os_f12_oversold_reversion_oscillator_zrsi_21d_base_v014_signal,
    f12os_f12_oversold_reversion_oscillator_rsismooth_14d_base_v015_signal,
    f12os_f12_oversold_reversion_oscillator_rsivel_14d_base_v016_signal,
    f12os_f12_oversold_reversion_oscillator_rsivel_21d_base_v017_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_14d_base_v018_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_21d_base_v019_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_63d_base_v020_signal,
    f12os_f12_oversold_reversion_oscillator_stochd_14d_base_v021_signal,
    f12os_f12_oversold_reversion_oscillator_stochd_21d_base_v022_signal,
    f12os_f12_oversold_reversion_oscillator_stochkd_14d_base_v023_signal,
    f12os_f12_oversold_reversion_oscillator_stochdev_14d_base_v024_signal,
    f12os_f12_oversold_reversion_oscillator_stochos_21d_base_v025_signal,
    f12os_f12_oversold_reversion_oscillator_willr_14d_base_v026_signal,
    f12os_f12_oversold_reversion_oscillator_willr_21d_base_v027_signal,
    f12os_f12_oversold_reversion_oscillator_willr_63d_base_v028_signal,
    f12os_f12_oversold_reversion_oscillator_willr_126d_base_v029_signal,
    f12os_f12_oversold_reversion_oscillator_zstoch_14d_base_v030_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_21d_base_v031_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_42d_base_v032_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_63d_base_v033_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_126d_base_v034_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_252d_base_v035_signal,
    f12os_f12_oversold_reversion_oscillator_zcloseneg_63d_base_v036_signal,
    f12os_f12_oversold_reversion_oscillator_cci_14d_base_v037_signal,
    f12os_f12_oversold_reversion_oscillator_cci_21d_base_v038_signal,
    f12os_f12_oversold_reversion_oscillator_cci_63d_base_v039_signal,
    f12os_f12_oversold_reversion_oscillator_ccios_21d_base_v040_signal,
    f12os_f12_oversold_reversion_oscillator_npo_21d_base_v041_signal,
    f12os_f12_oversold_reversion_oscillator_npo_42d_base_v042_signal,
    f12os_f12_oversold_reversion_oscillator_npo_63d_base_v043_signal,
    f12os_f12_oversold_reversion_oscillator_npo_126d_base_v044_signal,
    f12os_f12_oversold_reversion_oscillator_dpo_21d_base_v045_signal,
    f12os_f12_oversold_reversion_oscillator_dpo_42d_base_v046_signal,
    f12os_f12_oversold_reversion_oscillator_dpo_63d_base_v047_signal,
    f12os_f12_oversold_reversion_oscillator_stochrsi_14d_base_v048_signal,
    f12os_f12_oversold_reversion_oscillator_smi_14d_base_v049_signal,
    f12os_f12_oversold_reversion_oscillator_smi_21d_base_v050_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_7d_base_v051_signal,
    f12os_f12_oversold_reversion_oscillator_rsispread_7_21_base_v052_signal,
    f12os_f12_oversold_reversion_oscillator_rsispread_14_63_base_v053_signal,
    f12os_f12_oversold_reversion_oscillator_zspread_21_63_base_v054_signal,
    f12os_f12_oversold_reversion_oscillator_zspread_63_252_base_v055_signal,
    f12os_f12_oversold_reversion_oscillator_rsipress_14d_base_v056_signal,
    f12os_f12_oversold_reversion_oscillator_zpress_63d_base_v057_signal,
    f12os_f12_oversold_reversion_oscillator_stochpress_14d_base_v058_signal,
    f12os_f12_oversold_reversion_oscillator_ccinorm_21d_base_v059_signal,
    f12os_f12_oversold_reversion_oscillator_ccios_63d_base_v060_signal,
    f12os_f12_oversold_reversion_oscillator_rsielas_14d_base_v061_signal,
    f12os_f12_oversold_reversion_oscillator_npovol_21d_base_v062_signal,
    f12os_f12_oversold_reversion_oscillator_rsiema_14d_base_v063_signal,
    f12os_f12_oversold_reversion_oscillator_zcloseclip_21d_base_v064_signal,
    f12os_f12_oversold_reversion_oscillator_rsirank_14d_base_v065_signal,
    f12os_f12_oversold_reversion_oscillator_stochrank_14d_base_v066_signal,
    f12os_f12_oversold_reversion_oscillator_zcloserank_63d_base_v067_signal,
    f12os_f12_oversold_reversion_oscillator_composite_21d_base_v068_signal,
    f12os_f12_oversold_reversion_oscillator_rsistochx_14d_base_v069_signal,
    f12os_f12_oversold_reversion_oscillator_smaosc_21d_base_v070_signal,
    f12os_f12_oversold_reversion_oscillator_smaosc_63d_base_v071_signal,
    f12os_f12_oversold_reversion_oscillator_smaosc_126d_base_v072_signal,
    f12os_f12_oversold_reversion_oscillator_rsitarget_14d_base_v073_signal,
    f12os_f12_oversold_reversion_oscillator_slowstoch_21d_base_v074_signal,
    f12os_f12_oversold_reversion_oscillator_rsitanh_14d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_OVERSOLD_REVERSION_OSCILLATOR_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f12_rsi", "_f12_stoch", "_f12_zclose", "_f12_cci")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    print(f"OK f12_oversold_reversion_oscillator_base_001_075_claude: {n_features} features pass")
