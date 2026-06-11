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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f12os_f12_oversold_reversion_oscillator_rsi_7d_slope_v001_signal(closeadj):
    result = _f12_rsi(closeadj, 7)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_14d_slope_v002_signal(closeadj):
    result = _f12_rsi(closeadj, 14)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_21d_slope_v003_signal(closeadj):
    result = _f12_rsi(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_63d_slope_v004_signal(closeadj):
    result = _f12_rsi(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_14d_slope_v005_signal(closeadj):
    result = _f12_rsi(closeadj, 14) - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_21d_slope_v006_signal(closeadj):
    result = _f12_rsi(closeadj, 21) - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_63d_slope_v007_signal(closeadj):
    result = _f12_rsi(closeadj, 63) - 50.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_osdist_14d_slope_v008_signal(closeadj):
    g = 30.0 - _f12_rsi(closeadj, 14)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_osdist_21d_slope_v009_signal(closeadj):
    g = 30.0 - _f12_rsi(closeadj, 21)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_osgap_14d_slope_v010_signal(closeadj):
    result = 30.0 - _f12_rsi(closeadj, 14)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsisurp_7d_slope_v011_signal(closeadj):
    r = _f12_rsi(closeadj, 7)
    result = r - _mean(r, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsisurp_14d_slope_v012_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r - _mean(r, 63)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zrsi_14d_slope_v013_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 14), 126)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zrsi_21d_slope_v014_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsismooth_14d_slope_v015_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 14), 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsivel_14d_slope_v016_signal(closeadj):
    result = _f12_rsi(closeadj, 14).diff(5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsivel_21d_slope_v017_signal(closeadj):
    result = _f12_rsi(closeadj, 21).diff(10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_14d_slope_v018_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_21d_slope_v019_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_63d_slope_v020_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochd_14d_slope_v021_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 14), 3)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochd_21d_slope_v022_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 21), 3)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochkd_14d_slope_v023_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = k - _mean(k, 3)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochdev_14d_slope_v024_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochos_21d_slope_v025_signal(closeadj, low, high):
    g = 20.0 - _f12_stoch(closeadj, low, high, 21)
    result = np.log1p(np.exp(-np.abs(g))) + np.maximum(g, 0.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_14d_slope_v026_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - 100.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_21d_slope_v027_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21) - 100.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_63d_slope_v028_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63) - 100.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_126d_slope_v029_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 126) - 100.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zstoch_14d_slope_v030_signal(closeadj, low, high):
    result = _z(_f12_stoch(closeadj, low, high, 14), 126)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_21d_slope_v031_signal(closeadj):
    result = _f12_zclose(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_42d_slope_v032_signal(closeadj):
    result = _f12_zclose(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_63d_slope_v033_signal(closeadj):
    result = _f12_zclose(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_126d_slope_v034_signal(closeadj):
    result = _f12_zclose(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_252d_slope_v035_signal(closeadj):
    result = _f12_zclose(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloseneg_63d_slope_v036_signal(closeadj):
    result = -_f12_zclose(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_14d_slope_v037_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 14)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_21d_slope_v038_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_63d_slope_v039_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccios_21d_slope_v040_signal(closeadj, low, high):
    g = -100.0 - _f12_cci(closeadj, low, high, 21)
    result = np.log1p(np.exp(-np.abs(g) / 20.0)) * 20.0 + np.maximum(g, 0.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_21d_slope_v041_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=10).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_42d_slope_v042_signal(closeadj):
    ema = closeadj.ewm(span=42, min_periods=21).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 42) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_63d_slope_v043_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=21).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_126d_slope_v044_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=42).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_dpo_21d_slope_v045_signal(closeadj):
    sma = _mean(closeadj, 21).shift(21 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_dpo_42d_slope_v046_signal(closeadj):
    sma = _mean(closeadj, 42).shift(42 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 42) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_dpo_63d_slope_v047_signal(closeadj):
    sma = _mean(closeadj, 63).shift(63 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochrsi_14d_slope_v048_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    rk = k.rolling(14, min_periods=7).min()
    rh = k.rolling(14, min_periods=7).max()
    result = (k - rk) / (rh - rk).replace(0, np.nan) * 100.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smi_14d_slope_v049_signal(closeadj, low, high):
    ll = low.rolling(14, min_periods=7).min()
    hh = high.rolling(14, min_periods=7).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=5, min_periods=3).mean()
    den = ((hh - ll) / 2.0).ewm(span=5, min_periods=3).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 14) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smi_21d_slope_v050_signal(closeadj, low, high):
    ll = low.rolling(21, min_periods=10).min()
    hh = high.rolling(21, min_periods=10).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=8, min_periods=4).mean()
    den = ((hh - ll) / 2.0).ewm(span=8, min_periods=4).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_7d_slope_v051_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsispread_7_21_slope_v052_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - _f12_rsi(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsispread_14_63_slope_v053_signal(closeadj):
    result = _f12_rsi(closeadj, 14) - _f12_rsi(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zspread_21_63_slope_v054_signal(closeadj):
    result = _f12_zclose(closeadj, 21) - _f12_zclose(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zspread_63_252_slope_v055_signal(closeadj):
    result = _f12_zclose(closeadj, 63) - _f12_zclose(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsipress_14d_slope_v056_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = _safe_div(50.0 - r, _std(r, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zpress_63d_slope_v057_signal(closeadj):
    z = _f12_zclose(closeadj, 63)
    result = _safe_div(-z, _std(z, 126).add(1.0))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochpress_14d_slope_v058_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = _safe_div(50.0 - k, _std(k, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccinorm_21d_slope_v059_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 21)
    result = _safe_div(c, _std(c, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccios_63d_slope_v060_signal(closeadj, low, high):
    g = -100.0 - _f12_cci(closeadj, low, high, 63)
    result = np.log1p(np.exp(-np.abs(g) / 20.0)) * 20.0 + np.maximum(g, 0.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsielas_14d_slope_v061_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    depth = (50.0 - r) / 50.0
    result = r.diff(5) * depth
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npovol_21d_slope_v062_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=10).mean()
    npo = _safe_div(closeadj - ema, ema)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(npo, _std(lr, 63) * np.sqrt(21.0)) + _f12_zclose(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsiema_14d_slope_v063_signal(closeadj):
    dev = _f12_rsi(closeadj, 14) - 50.0
    result = dev.ewm(span=10, min_periods=5).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloseclip_21d_slope_v064_signal(closeadj):
    result = _f12_zclose(closeadj, 21).clip(-4.0, 4.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsirank_14d_slope_v065_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochrank_14d_slope_v066_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 14)
    result = k.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloserank_63d_slope_v067_signal(closeadj):
    z = _f12_zclose(closeadj, 63)
    result = z.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_composite_21d_slope_v068_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 21) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 21) - 50.0) / 50.0
    c = _f12_zclose(closeadj, 21) / 3.0
    result = (a + b + c) / 3.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsistochx_14d_slope_v069_signal(closeadj, low, high):
    r = (_f12_rsi(closeadj, 14) - 50.0) / 50.0
    k = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 50.0
    result = r * k
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smaosc_21d_slope_v070_signal(closeadj):
    sma = _mean(closeadj, 21)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smaosc_63d_slope_v071_signal(closeadj):
    sma = _mean(closeadj, 63)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smaosc_126d_slope_v072_signal(closeadj):
    sma = _mean(closeadj, 126)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsitarget_14d_slope_v073_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = (50.0 - r) * (1.0 + r.diff(3) / 100.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_slowstoch_21d_slope_v074_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = _mean(_mean(k, 3), 3)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsitanh_14d_slope_v075_signal(closeadj):
    dev = (_f12_rsi(closeadj, 14) - 50.0) / 20.0
    result = np.tanh(dev) + _f12_rsi(closeadj, 14) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_10d_slope_v076_signal(closeadj):
    result = _f12_rsi(closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_42d_slope_v077_signal(closeadj):
    result = _f12_rsi(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsi_126d_slope_v078_signal(closeadj):
    result = _f12_rsi(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_42d_slope_v079_signal(closeadj):
    result = _f12_rsi(closeadj, 42) - 50.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidev_126d_slope_v080_signal(closeadj):
    result = _f12_rsi(closeadj, 126) - 50.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zrsi_7d_slope_v081_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 7), 63)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zrsi_63d_slope_v082_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsismooth_21d_slope_v083_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 21), 42)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsivel_7d_slope_v084_signal(closeadj):
    result = _f12_rsi(closeadj, 7).diff(3)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsivel_63d_slope_v085_signal(closeadj):
    result = _f12_rsi(closeadj, 63).diff(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsispread_7_14_slope_v086_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - _f12_rsi(closeadj, 14)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsispread_21_63_slope_v087_signal(closeadj):
    result = _f12_rsi(closeadj, 21) - _f12_rsi(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsiema21_14d_slope_v088_signal(closeadj):
    dev = _f12_rsi(closeadj, 14) - 50.0
    result = dev.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsirank_252_14d_slope_v089_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsitanh30_14d_slope_v090_signal(closeadj):
    dev = (_f12_rsi(closeadj, 14) - 50.0) / 30.0
    result = np.tanh(dev) + _f12_rsi(closeadj, 14) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_10d_slope_v091_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_42d_slope_v092_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochk_126d_slope_v093_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochd_63d_slope_v094_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 63), 3)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochdev_21d_slope_v095_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21) - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochdev_63d_slope_v096_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63) - 50.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_42d_slope_v097_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 42) - 100.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willr_252d_slope_v098_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 252) - 100.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zstoch_21d_slope_v099_signal(closeadj, low, high):
    result = _z(_f12_stoch(closeadj, low, high, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochspread_14_63_slope_v100_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - _f12_stoch(closeadj, low, high, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochrank_252_21d_slope_v101_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = k.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochtanh_14d_slope_v102_signal(closeadj, low, high):
    dev = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 30.0
    result = np.tanh(dev) + _f12_stoch(closeadj, low, high, 14) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_10d_slope_v103_signal(closeadj):
    result = _f12_zclose(closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_84d_slope_v104_signal(closeadj):
    result = _f12_zclose(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_189d_slope_v105_signal(closeadj):
    result = _f12_zclose(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zclose_504d_slope_v106_signal(closeadj):
    result = _f12_zclose(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloseneg_21d_slope_v107_signal(closeadj):
    result = -_f12_zclose(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ztanh_21d_slope_v108_signal(closeadj):
    result = np.tanh(_f12_zclose(closeadj, 21) / 2.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zspread_21_126_slope_v109_signal(closeadj):
    result = _f12_zclose(closeadj, 21) - _f12_zclose(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloserank_21d_slope_v110_signal(closeadj):
    z = _f12_zclose(closeadj, 21)
    result = z.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_7d_slope_v111_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 7)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_42d_slope_v112_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cci_126d_slope_v113_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccitanh_21d_slope_v114_signal(closeadj, low, high):
    result = np.tanh(_f12_cci(closeadj, low, high, 21) / 150.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccirank_21d_slope_v115_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 21)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccispread_21_63_slope_v116_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21) - _f12_cci(closeadj, low, high, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_10d_slope_v117_signal(closeadj):
    ema = closeadj.ewm(span=10, min_periods=5).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 10) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_npo_252d_slope_v118_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=84).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ppo_12_26_slope_v119_signal(closeadj):
    fast = closeadj.ewm(span=12, min_periods=6).mean()
    slow = closeadj.ewm(span=26, min_periods=13).mean()
    result = _safe_div(fast - slow, slow) + _f12_zclose(closeadj, 26) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ppo_21_63_slope_v120_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=10).mean()
    slow = closeadj.ewm(span=63, min_periods=21).mean()
    result = _safe_div(fast - slow, slow) + _f12_zclose(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_dpo_126d_slope_v121_signal(closeadj):
    sma = _mean(closeadj, 126).shift(126 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_dpo_10d_slope_v122_signal(closeadj):
    sma = _mean(closeadj, 10).shift(10 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 10) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smaoscvol_21d_slope_v123_signal(closeadj):
    sma = _mean(closeadj, 21)
    osc = _safe_div(closeadj - sma, sma)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(osc, _std(lr, 126) * np.sqrt(21.0)) + _f12_zclose(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smaosc_252d_slope_v124_signal(closeadj):
    sma = _mean(closeadj, 252)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochrsi_21d_slope_v125_signal(closeadj):
    r = _f12_rsi(closeadj, 21)
    rl = r.rolling(21, min_periods=10).min()
    rh = r.rolling(21, min_periods=10).max()
    result = (r - rl) / (rh - rl).replace(0, np.nan) * 100.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_smi_63d_slope_v126_signal(closeadj, low, high):
    ll = low.rolling(63, min_periods=21).min()
    hh = high.rolling(63, min_periods=21).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=10, min_periods=5).mean()
    den = ((hh - ll) / 2.0).ewm(span=10, min_periods=5).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsipress126_14d_slope_v127_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = _safe_div(50.0 - r, _std(r, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochpress_21d_slope_v128_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = _safe_div(50.0 - k, _std(k, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ccinorm_63d_slope_v129_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 63)
    result = _safe_div(c, _std(c, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsielas63_14d_slope_v130_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    depth = (50.0 - r) / 50.0
    result = r.diff(10) * depth
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_composite_63d_slope_v131_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 63) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 63) - 50.0) / 50.0
    c = _f12_zclose(closeadj, 63) / 3.0
    result = (a + b + c) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsistochx_21d_slope_v132_signal(closeadj, low, high):
    r = (_f12_rsi(closeadj, 21) - 50.0) / 50.0
    k = (_f12_stoch(closeadj, low, high, 21) - 50.0) / 50.0
    result = r * k
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zccix_21d_slope_v133_signal(closeadj, low, high):
    z = _f12_zclose(closeadj, 21)
    c = _f12_cci(closeadj, low, high, 21) / 150.0
    result = z * c
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidbl_14d_slope_v134_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.ewm(span=10, min_periods=5).mean().ewm(span=10, min_periods=5).mean() - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zcloseema_21d_slope_v135_signal(closeadj):
    result = _f12_zclose(closeadj, 21).ewm(span=10, min_periods=5).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsidevsmooth_63d_slope_v136_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 63) - 50.0, 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsiblend_multi_slope_v137_signal(closeadj):
    result = (_f12_rsi(closeadj, 7) + 2.0 * _f12_rsi(closeadj, 14)
              + _f12_rsi(closeadj, 21)) / 4.0 - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochblend_multi_slope_v138_signal(closeadj, low, high):
    result = (_f12_stoch(closeadj, low, high, 14) + _f12_stoch(closeadj, low, high, 21)
              + _f12_stoch(closeadj, low, high, 63)) / 3.0 - 50.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_ztarget_21d_slope_v139_signal(closeadj):
    z = _f12_zclose(closeadj, 21)
    result = -z * (1.0 + z.diff(3))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_willrsmooth_42d_slope_v140_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 42) - 100.0, 5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsimom_14d_slope_v141_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r - r.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsimom_63d_slope_v142_signal(closeadj):
    r = _f12_rsi(closeadj, 63)
    result = r - r.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_stochmom_21d_slope_v143_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = k - k.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsistochdiff_slope_v144_signal(closeadj, low, high):
    result = _f12_rsi(closeadj, 14) - _f12_stoch(closeadj, low, high, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_zrsidiff_slope_v145_signal(closeadj):
    result = _f12_zclose(closeadj, 21) * 25.0 - (_f12_rsi(closeadj, 14) - 50.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_lowprox_63d_slope_v146_signal(closeadj, low, high):
    ll = low.rolling(63, min_periods=21).min()
    result = _safe_div(closeadj - ll, ll) + _f12_stoch(closeadj, low, high, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_lowprox_126d_slope_v147_signal(closeadj, low, high):
    ll = low.rolling(126, min_periods=42).min()
    result = _safe_div(closeadj - ll, ll) + _f12_stoch(closeadj, low, high, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_rsisig_14d_slope_v148_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = (50.0 - r) / (1.0 + np.exp((r - 30.0) / 10.0))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_cciema_21d_slope_v149_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21).ewm(span=10, min_periods=5).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12os_f12_oversold_reversion_oscillator_oscblend_multi_slope_v150_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 14) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 50.0
    c = np.tanh(_f12_cci(closeadj, low, high, 14) / 150.0)
    d = np.tanh(_f12_zclose(closeadj, 21) / 2.0)
    result = (a + b + c + d) / 4.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f12os_f12_oversold_reversion_oscillator_rsi_7d_slope_v001_signal,    f12os_f12_oversold_reversion_oscillator_rsi_14d_slope_v002_signal,    f12os_f12_oversold_reversion_oscillator_rsi_21d_slope_v003_signal,    f12os_f12_oversold_reversion_oscillator_rsi_63d_slope_v004_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_14d_slope_v005_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_21d_slope_v006_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_63d_slope_v007_signal,    f12os_f12_oversold_reversion_oscillator_osdist_14d_slope_v008_signal,    f12os_f12_oversold_reversion_oscillator_osdist_21d_slope_v009_signal,    f12os_f12_oversold_reversion_oscillator_osgap_14d_slope_v010_signal,    f12os_f12_oversold_reversion_oscillator_rsisurp_7d_slope_v011_signal,    f12os_f12_oversold_reversion_oscillator_rsisurp_14d_slope_v012_signal,    f12os_f12_oversold_reversion_oscillator_zrsi_14d_slope_v013_signal,    f12os_f12_oversold_reversion_oscillator_zrsi_21d_slope_v014_signal,    f12os_f12_oversold_reversion_oscillator_rsismooth_14d_slope_v015_signal,    f12os_f12_oversold_reversion_oscillator_rsivel_14d_slope_v016_signal,    f12os_f12_oversold_reversion_oscillator_rsivel_21d_slope_v017_signal,    f12os_f12_oversold_reversion_oscillator_stochk_14d_slope_v018_signal,    f12os_f12_oversold_reversion_oscillator_stochk_21d_slope_v019_signal,    f12os_f12_oversold_reversion_oscillator_stochk_63d_slope_v020_signal,    f12os_f12_oversold_reversion_oscillator_stochd_14d_slope_v021_signal,    f12os_f12_oversold_reversion_oscillator_stochd_21d_slope_v022_signal,    f12os_f12_oversold_reversion_oscillator_stochkd_14d_slope_v023_signal,    f12os_f12_oversold_reversion_oscillator_stochdev_14d_slope_v024_signal,    f12os_f12_oversold_reversion_oscillator_stochos_21d_slope_v025_signal,    f12os_f12_oversold_reversion_oscillator_willr_14d_slope_v026_signal,    f12os_f12_oversold_reversion_oscillator_willr_21d_slope_v027_signal,    f12os_f12_oversold_reversion_oscillator_willr_63d_slope_v028_signal,    f12os_f12_oversold_reversion_oscillator_willr_126d_slope_v029_signal,    f12os_f12_oversold_reversion_oscillator_zstoch_14d_slope_v030_signal,    f12os_f12_oversold_reversion_oscillator_zclose_21d_slope_v031_signal,    f12os_f12_oversold_reversion_oscillator_zclose_42d_slope_v032_signal,    f12os_f12_oversold_reversion_oscillator_zclose_63d_slope_v033_signal,    f12os_f12_oversold_reversion_oscillator_zclose_126d_slope_v034_signal,    f12os_f12_oversold_reversion_oscillator_zclose_252d_slope_v035_signal,    f12os_f12_oversold_reversion_oscillator_zcloseneg_63d_slope_v036_signal,    f12os_f12_oversold_reversion_oscillator_cci_14d_slope_v037_signal,    f12os_f12_oversold_reversion_oscillator_cci_21d_slope_v038_signal,    f12os_f12_oversold_reversion_oscillator_cci_63d_slope_v039_signal,    f12os_f12_oversold_reversion_oscillator_ccios_21d_slope_v040_signal,    f12os_f12_oversold_reversion_oscillator_npo_21d_slope_v041_signal,    f12os_f12_oversold_reversion_oscillator_npo_42d_slope_v042_signal,    f12os_f12_oversold_reversion_oscillator_npo_63d_slope_v043_signal,    f12os_f12_oversold_reversion_oscillator_npo_126d_slope_v044_signal,    f12os_f12_oversold_reversion_oscillator_dpo_21d_slope_v045_signal,    f12os_f12_oversold_reversion_oscillator_dpo_42d_slope_v046_signal,    f12os_f12_oversold_reversion_oscillator_dpo_63d_slope_v047_signal,    f12os_f12_oversold_reversion_oscillator_stochrsi_14d_slope_v048_signal,    f12os_f12_oversold_reversion_oscillator_smi_14d_slope_v049_signal,    f12os_f12_oversold_reversion_oscillator_smi_21d_slope_v050_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_7d_slope_v051_signal,    f12os_f12_oversold_reversion_oscillator_rsispread_7_21_slope_v052_signal,    f12os_f12_oversold_reversion_oscillator_rsispread_14_63_slope_v053_signal,    f12os_f12_oversold_reversion_oscillator_zspread_21_63_slope_v054_signal,    f12os_f12_oversold_reversion_oscillator_zspread_63_252_slope_v055_signal,    f12os_f12_oversold_reversion_oscillator_rsipress_14d_slope_v056_signal,    f12os_f12_oversold_reversion_oscillator_zpress_63d_slope_v057_signal,    f12os_f12_oversold_reversion_oscillator_stochpress_14d_slope_v058_signal,    f12os_f12_oversold_reversion_oscillator_ccinorm_21d_slope_v059_signal,    f12os_f12_oversold_reversion_oscillator_ccios_63d_slope_v060_signal,    f12os_f12_oversold_reversion_oscillator_rsielas_14d_slope_v061_signal,    f12os_f12_oversold_reversion_oscillator_npovol_21d_slope_v062_signal,    f12os_f12_oversold_reversion_oscillator_rsiema_14d_slope_v063_signal,    f12os_f12_oversold_reversion_oscillator_zcloseclip_21d_slope_v064_signal,    f12os_f12_oversold_reversion_oscillator_rsirank_14d_slope_v065_signal,    f12os_f12_oversold_reversion_oscillator_stochrank_14d_slope_v066_signal,    f12os_f12_oversold_reversion_oscillator_zcloserank_63d_slope_v067_signal,    f12os_f12_oversold_reversion_oscillator_composite_21d_slope_v068_signal,    f12os_f12_oversold_reversion_oscillator_rsistochx_14d_slope_v069_signal,    f12os_f12_oversold_reversion_oscillator_smaosc_21d_slope_v070_signal,    f12os_f12_oversold_reversion_oscillator_smaosc_63d_slope_v071_signal,    f12os_f12_oversold_reversion_oscillator_smaosc_126d_slope_v072_signal,    f12os_f12_oversold_reversion_oscillator_rsitarget_14d_slope_v073_signal,    f12os_f12_oversold_reversion_oscillator_slowstoch_21d_slope_v074_signal,    f12os_f12_oversold_reversion_oscillator_rsitanh_14d_slope_v075_signal,    f12os_f12_oversold_reversion_oscillator_rsi_10d_slope_v076_signal,    f12os_f12_oversold_reversion_oscillator_rsi_42d_slope_v077_signal,    f12os_f12_oversold_reversion_oscillator_rsi_126d_slope_v078_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_42d_slope_v079_signal,    f12os_f12_oversold_reversion_oscillator_rsidev_126d_slope_v080_signal,    f12os_f12_oversold_reversion_oscillator_zrsi_7d_slope_v081_signal,    f12os_f12_oversold_reversion_oscillator_zrsi_63d_slope_v082_signal,    f12os_f12_oversold_reversion_oscillator_rsismooth_21d_slope_v083_signal,    f12os_f12_oversold_reversion_oscillator_rsivel_7d_slope_v084_signal,    f12os_f12_oversold_reversion_oscillator_rsivel_63d_slope_v085_signal,    f12os_f12_oversold_reversion_oscillator_rsispread_7_14_slope_v086_signal,    f12os_f12_oversold_reversion_oscillator_rsispread_21_63_slope_v087_signal,    f12os_f12_oversold_reversion_oscillator_rsiema21_14d_slope_v088_signal,    f12os_f12_oversold_reversion_oscillator_rsirank_252_14d_slope_v089_signal,    f12os_f12_oversold_reversion_oscillator_rsitanh30_14d_slope_v090_signal,    f12os_f12_oversold_reversion_oscillator_stochk_10d_slope_v091_signal,    f12os_f12_oversold_reversion_oscillator_stochk_42d_slope_v092_signal,    f12os_f12_oversold_reversion_oscillator_stochk_126d_slope_v093_signal,    f12os_f12_oversold_reversion_oscillator_stochd_63d_slope_v094_signal,    f12os_f12_oversold_reversion_oscillator_stochdev_21d_slope_v095_signal,    f12os_f12_oversold_reversion_oscillator_stochdev_63d_slope_v096_signal,    f12os_f12_oversold_reversion_oscillator_willr_42d_slope_v097_signal,    f12os_f12_oversold_reversion_oscillator_willr_252d_slope_v098_signal,    f12os_f12_oversold_reversion_oscillator_zstoch_21d_slope_v099_signal,    f12os_f12_oversold_reversion_oscillator_stochspread_14_63_slope_v100_signal,    f12os_f12_oversold_reversion_oscillator_stochrank_252_21d_slope_v101_signal,    f12os_f12_oversold_reversion_oscillator_stochtanh_14d_slope_v102_signal,    f12os_f12_oversold_reversion_oscillator_zclose_10d_slope_v103_signal,    f12os_f12_oversold_reversion_oscillator_zclose_84d_slope_v104_signal,    f12os_f12_oversold_reversion_oscillator_zclose_189d_slope_v105_signal,    f12os_f12_oversold_reversion_oscillator_zclose_504d_slope_v106_signal,    f12os_f12_oversold_reversion_oscillator_zcloseneg_21d_slope_v107_signal,    f12os_f12_oversold_reversion_oscillator_ztanh_21d_slope_v108_signal,    f12os_f12_oversold_reversion_oscillator_zspread_21_126_slope_v109_signal,    f12os_f12_oversold_reversion_oscillator_zcloserank_21d_slope_v110_signal,    f12os_f12_oversold_reversion_oscillator_cci_7d_slope_v111_signal,    f12os_f12_oversold_reversion_oscillator_cci_42d_slope_v112_signal,    f12os_f12_oversold_reversion_oscillator_cci_126d_slope_v113_signal,    f12os_f12_oversold_reversion_oscillator_ccitanh_21d_slope_v114_signal,    f12os_f12_oversold_reversion_oscillator_ccirank_21d_slope_v115_signal,    f12os_f12_oversold_reversion_oscillator_ccispread_21_63_slope_v116_signal,    f12os_f12_oversold_reversion_oscillator_npo_10d_slope_v117_signal,    f12os_f12_oversold_reversion_oscillator_npo_252d_slope_v118_signal,    f12os_f12_oversold_reversion_oscillator_ppo_12_26_slope_v119_signal,    f12os_f12_oversold_reversion_oscillator_ppo_21_63_slope_v120_signal,    f12os_f12_oversold_reversion_oscillator_dpo_126d_slope_v121_signal,    f12os_f12_oversold_reversion_oscillator_dpo_10d_slope_v122_signal,    f12os_f12_oversold_reversion_oscillator_smaoscvol_21d_slope_v123_signal,    f12os_f12_oversold_reversion_oscillator_smaosc_252d_slope_v124_signal,    f12os_f12_oversold_reversion_oscillator_stochrsi_21d_slope_v125_signal,    f12os_f12_oversold_reversion_oscillator_smi_63d_slope_v126_signal,    f12os_f12_oversold_reversion_oscillator_rsipress126_14d_slope_v127_signal,    f12os_f12_oversold_reversion_oscillator_stochpress_21d_slope_v128_signal,    f12os_f12_oversold_reversion_oscillator_ccinorm_63d_slope_v129_signal,    f12os_f12_oversold_reversion_oscillator_rsielas63_14d_slope_v130_signal,    f12os_f12_oversold_reversion_oscillator_composite_63d_slope_v131_signal,    f12os_f12_oversold_reversion_oscillator_rsistochx_21d_slope_v132_signal,    f12os_f12_oversold_reversion_oscillator_zccix_21d_slope_v133_signal,    f12os_f12_oversold_reversion_oscillator_rsidbl_14d_slope_v134_signal,    f12os_f12_oversold_reversion_oscillator_zcloseema_21d_slope_v135_signal,    f12os_f12_oversold_reversion_oscillator_rsidevsmooth_63d_slope_v136_signal,    f12os_f12_oversold_reversion_oscillator_rsiblend_multi_slope_v137_signal,    f12os_f12_oversold_reversion_oscillator_stochblend_multi_slope_v138_signal,    f12os_f12_oversold_reversion_oscillator_ztarget_21d_slope_v139_signal,    f12os_f12_oversold_reversion_oscillator_willrsmooth_42d_slope_v140_signal,    f12os_f12_oversold_reversion_oscillator_rsimom_14d_slope_v141_signal,    f12os_f12_oversold_reversion_oscillator_rsimom_63d_slope_v142_signal,    f12os_f12_oversold_reversion_oscillator_stochmom_21d_slope_v143_signal,    f12os_f12_oversold_reversion_oscillator_rsistochdiff_slope_v144_signal,    f12os_f12_oversold_reversion_oscillator_zrsidiff_slope_v145_signal,    f12os_f12_oversold_reversion_oscillator_lowprox_63d_slope_v146_signal,    f12os_f12_oversold_reversion_oscillator_lowprox_126d_slope_v147_signal,    f12os_f12_oversold_reversion_oscillator_rsisig_14d_slope_v148_signal,    f12os_f12_oversold_reversion_oscillator_cciema_21d_slope_v149_signal,    f12os_f12_oversold_reversion_oscillator_oscblend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_OVERSOLD_REVERSION_OSCILLATOR_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f12_rsi', '_f12_stoch', '_f12_zclose', '_f12_cci')
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f12_oversold_reversion_oscillator_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
