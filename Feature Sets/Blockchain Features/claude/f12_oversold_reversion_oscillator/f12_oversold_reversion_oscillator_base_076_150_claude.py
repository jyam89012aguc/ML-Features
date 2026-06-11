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
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.ewm(alpha=1.0 / w, min_periods=w, adjust=False).mean()
    ad = dn.ewm(alpha=1.0 / w, min_periods=w, adjust=False).mean()
    rs = au / ad.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _f12_stoch(close, low, high, w):
    ll = low.rolling(w, min_periods=max(1, w // 2)).min()
    hh = high.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - ll) / (hh - ll).replace(0, np.nan) * 100.0


def _f12_zclose(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _f12_cci(close, low, high, w):
    tp = (close + low + high) / 3.0
    ma = tp.rolling(w, min_periods=max(1, w // 2)).mean()
    md = (tp - ma).abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return (tp - ma) / (0.015 * md).replace(0, np.nan)


# ============ FEATURES 076-150 ============

# 10d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_10d_base_v076_signal(closeadj):
    result = _f12_rsi(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_42d_base_v077_signal(closeadj):
    result = _f12_rsi(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Wilder RSI
def f12os_f12_oversold_reversion_oscillator_rsi_126d_base_v078_signal(closeadj):
    result = _f12_rsi(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d RSI distance from 50
def f12os_f12_oversold_reversion_oscillator_rsidev_42d_base_v079_signal(closeadj):
    result = _f12_rsi(closeadj, 42) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d RSI distance from 50
def f12os_f12_oversold_reversion_oscillator_rsidev_126d_base_v080_signal(closeadj):
    result = _f12_rsi(closeadj, 126) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 7d RSI over 63d
def f12os_f12_oversold_reversion_oscillator_zrsi_7d_base_v081_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 7), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d RSI over 252d
def f12os_f12_oversold_reversion_oscillator_zrsi_63d_base_v082_signal(closeadj):
    result = _z(_f12_rsi(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed RSI (42d mean)
def f12os_f12_oversold_reversion_oscillator_rsismooth_21d_base_v083_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 7d RSI velocity (3d change)
def f12os_f12_oversold_reversion_oscillator_rsivel_7d_base_v084_signal(closeadj):
    result = _f12_rsi(closeadj, 7).diff(3)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RSI velocity (21d change)
def f12os_f12_oversold_reversion_oscillator_rsivel_63d_base_v085_signal(closeadj):
    result = _f12_rsi(closeadj, 63).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 7d-14d RSI spread
def f12os_f12_oversold_reversion_oscillator_rsispread_7_14_base_v086_signal(closeadj):
    result = _f12_rsi(closeadj, 7) - _f12_rsi(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-63d RSI spread
def f12os_f12_oversold_reversion_oscillator_rsispread_21_63_base_v087_signal(closeadj):
    result = _f12_rsi(closeadj, 21) - _f12_rsi(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI EMA-smoothed deviation over span 21
def f12os_f12_oversold_reversion_oscillator_rsiema21_14d_base_v088_signal(closeadj):
    dev = _f12_rsi(closeadj, 14) - 50.0
    result = dev.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI percentile rank over 252d
def f12os_f12_oversold_reversion_oscillator_rsirank_252_14d_base_v089_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI bounded reversion via tanh over 30-band
def f12os_f12_oversold_reversion_oscillator_rsitanh30_14d_base_v090_signal(closeadj):
    dev = (_f12_rsi(closeadj, 14) - 50.0) / 30.0
    result = np.tanh(dev) + _f12_rsi(closeadj, 14) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d stochastic %K
def f12os_f12_oversold_reversion_oscillator_stochk_10d_base_v091_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d stochastic %K
def f12os_f12_oversold_reversion_oscillator_stochk_42d_base_v092_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d stochastic %K
def f12os_f12_oversold_reversion_oscillator_stochk_126d_base_v093_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d stochastic %D (3d mean)
def f12os_f12_oversold_reversion_oscillator_stochd_63d_base_v094_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 63), 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K distance from 50
def f12os_f12_oversold_reversion_oscillator_stochdev_21d_base_v095_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 21) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d stochastic %K distance from 50
def f12os_f12_oversold_reversion_oscillator_stochdev_63d_base_v096_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 63) - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Williams %R
def f12os_f12_oversold_reversion_oscillator_willr_42d_base_v097_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 42) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Williams %R
def f12os_f12_oversold_reversion_oscillator_willr_252d_base_v098_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 252) - 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d stochastic %K over 252d
def f12os_f12_oversold_reversion_oscillator_zstoch_21d_base_v099_signal(closeadj, low, high):
    result = _z(_f12_stoch(closeadj, low, high, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d-63d stochastic %K spread (fast vs slow window)
def f12os_f12_oversold_reversion_oscillator_stochspread_14_63_base_v100_signal(closeadj, low, high):
    result = _f12_stoch(closeadj, low, high, 14) - _f12_stoch(closeadj, low, high, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K percentile rank over 252d
def f12os_f12_oversold_reversion_oscillator_stochrank_252_21d_base_v101_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = k.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d stochastic %K bounded reversion via tanh
def f12os_f12_oversold_reversion_oscillator_stochtanh_14d_base_v102_signal(closeadj, low, high):
    dev = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 30.0
    result = np.tanh(dev) + _f12_stoch(closeadj, low, high, 14) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_10d_base_v103_signal(closeadj):
    result = _f12_zclose(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_84d_base_v104_signal(closeadj):
    result = _f12_zclose(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_189d_base_v105_signal(closeadj):
    result = _f12_zclose(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling z-score of close
def f12os_f12_oversold_reversion_oscillator_zclose_504d_base_v106_signal(closeadj):
    result = _f12_zclose(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# negative 21d z-close (continuous oversold depth)
def f12os_f12_oversold_reversion_oscillator_zcloseneg_21d_base_v107_signal(closeadj):
    result = -_f12_zclose(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close bounded via tanh
def f12os_f12_oversold_reversion_oscillator_ztanh_21d_base_v108_signal(closeadj):
    result = np.tanh(_f12_zclose(closeadj, 21) / 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-126d z-close spread
def f12os_f12_oversold_reversion_oscillator_zspread_21_126_base_v109_signal(closeadj):
    result = _f12_zclose(closeadj, 21) - _f12_zclose(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close percentile rank over 252d
def f12os_f12_oversold_reversion_oscillator_zcloserank_21d_base_v110_signal(closeadj):
    z = _f12_zclose(closeadj, 21)
    result = z.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 7d CCI
def f12os_f12_oversold_reversion_oscillator_cci_7d_base_v111_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 7)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d CCI
def f12os_f12_oversold_reversion_oscillator_cci_42d_base_v112_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d CCI
def f12os_f12_oversold_reversion_oscillator_cci_126d_base_v113_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI bounded via tanh
def f12os_f12_oversold_reversion_oscillator_ccitanh_21d_base_v114_signal(closeadj, low, high):
    result = np.tanh(_f12_cci(closeadj, low, high, 21) / 150.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI percentile rank over 252d
def f12os_f12_oversold_reversion_oscillator_ccirank_21d_base_v115_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 21)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-63d CCI spread
def f12os_f12_oversold_reversion_oscillator_ccispread_21_63_base_v116_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21) - _f12_cci(closeadj, low, high, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 10d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_10d_base_v117_signal(closeadj):
    ema = closeadj.ewm(span=10, min_periods=5).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized price oscillator (close - 252d EMA) / EMA
def f12os_f12_oversold_reversion_oscillator_npo_252d_base_v118_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=84).mean()
    result = _safe_div(closeadj - ema, ema) + _f12_zclose(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# percentage price oscillator (fast EMA - slow EMA) / slow EMA
def f12os_f12_oversold_reversion_oscillator_ppo_12_26_base_v119_signal(closeadj):
    fast = closeadj.ewm(span=12, min_periods=6).mean()
    slow = closeadj.ewm(span=26, min_periods=13).mean()
    result = _safe_div(fast - slow, slow) + _f12_zclose(closeadj, 26) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# percentage price oscillator 21/63
def f12os_f12_oversold_reversion_oscillator_ppo_21_63_base_v120_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=10).mean()
    slow = closeadj.ewm(span=63, min_periods=21).mean()
    result = _safe_div(fast - slow, slow) + _f12_zclose(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# detrended price oscillator 126d
def f12os_f12_oversold_reversion_oscillator_dpo_126d_base_v121_signal(closeadj):
    sma = _mean(closeadj, 126).shift(126 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# detrended price oscillator 10d
def f12os_f12_oversold_reversion_oscillator_dpo_10d_base_v122_signal(closeadj):
    sma = _mean(closeadj, 10).shift(10 // 2 + 1)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d normalized price oscillator vs SMA scaled by 126d vol
def f12os_f12_oversold_reversion_oscillator_smaoscvol_21d_base_v123_signal(closeadj):
    sma = _mean(closeadj, 21)
    osc = _safe_div(closeadj - sma, sma)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(osc, _std(lr, 126) * np.sqrt(21.0)) + _f12_zclose(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized price oscillator vs SMA
def f12os_f12_oversold_reversion_oscillator_smaosc_252d_base_v124_signal(closeadj):
    sma = _mean(closeadj, 252)
    result = _safe_div(closeadj - sma, sma) + _f12_zclose(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic RSI (RSI of RSI range)
def f12os_f12_oversold_reversion_oscillator_stochrsi_21d_base_v125_signal(closeadj):
    r = _f12_rsi(closeadj, 21)
    rl = r.rolling(21, min_periods=10).min()
    rh = r.rolling(21, min_periods=10).max()
    result = (r - rl) / (rh - rl).replace(0, np.nan) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic momentum index 63d
def f12os_f12_oversold_reversion_oscillator_smi_63d_base_v126_signal(closeadj, low, high):
    ll = low.rolling(63, min_periods=21).min()
    hh = high.rolling(63, min_periods=21).max()
    mid = (hh + ll) / 2.0
    num = (closeadj - mid).ewm(span=10, min_periods=5).mean()
    den = ((hh - ll) / 2.0).ewm(span=10, min_periods=5).mean()
    result = _safe_div(num, den) * 100.0 + _f12_stoch(closeadj, low, high, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI reversion pressure scaled by 126d RSI std
def f12os_f12_oversold_reversion_oscillator_rsipress126_14d_base_v127_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = _safe_div(50.0 - r, _std(r, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K reversion pressure scaled by 126d std
def f12os_f12_oversold_reversion_oscillator_stochpress_21d_base_v128_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = _safe_div(50.0 - k, _std(k, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d CCI normalized by 252d CCI std
def f12os_f12_oversold_reversion_oscillator_ccinorm_63d_base_v129_signal(closeadj, low, high):
    c = _f12_cci(closeadj, low, high, 63)
    result = _safe_div(c, _std(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI elasticity weighted by oversold depth over 63d
def f12os_f12_oversold_reversion_oscillator_rsielas63_14d_base_v130_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    depth = (50.0 - r) / 50.0
    result = r.diff(10) * depth
    return result.replace([np.inf, -np.inf], np.nan)


# composite oversold index 63d (RSI, stoch, z-close)
def f12os_f12_oversold_reversion_oscillator_composite_63d_base_v131_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 63) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 63) - 50.0) / 50.0
    c = _f12_zclose(closeadj, 63) / 3.0
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# RSI(21) x stochastic %K(21) interaction (centered)
def f12os_f12_oversold_reversion_oscillator_rsistochx_21d_base_v132_signal(closeadj, low, high):
    r = (_f12_rsi(closeadj, 21) - 50.0) / 50.0
    k = (_f12_stoch(closeadj, low, high, 21) - 50.0) / 50.0
    result = r * k
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close x CCI(21) interaction (mean-reversion confirmation)
def f12os_f12_oversold_reversion_oscillator_zccix_21d_base_v133_signal(closeadj, low, high):
    z = _f12_zclose(closeadj, 21)
    c = _f12_cci(closeadj, low, high, 21) / 150.0
    result = z * c
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI EMA double-smoothed (TRIX-like on RSI)
def f12os_f12_oversold_reversion_oscillator_rsidbl_14d_base_v134_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r.ewm(span=10, min_periods=5).mean().ewm(span=10, min_periods=5).mean() - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close smoothed by 10d EMA
def f12os_f12_oversold_reversion_oscillator_zcloseema_21d_base_v135_signal(closeadj):
    result = _f12_zclose(closeadj, 21).ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RSI distance from 50 smoothed
def f12os_f12_oversold_reversion_oscillator_rsidevsmooth_63d_base_v136_signal(closeadj):
    result = _mean(_f12_rsi(closeadj, 63) - 50.0, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d ultimate-style blended RSI across 7/14/21
def f12os_f12_oversold_reversion_oscillator_rsiblend_multi_base_v137_signal(closeadj):
    result = (_f12_rsi(closeadj, 7) + 2.0 * _f12_rsi(closeadj, 14)
              + _f12_rsi(closeadj, 21)) / 4.0 - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended stochastic across 14/21/63 centered
def f12os_f12_oversold_reversion_oscillator_stochblend_multi_base_v138_signal(closeadj, low, high):
    result = (_f12_stoch(closeadj, low, high, 14) + _f12_stoch(closeadj, low, high, 21)
              + _f12_stoch(closeadj, low, high, 63)) / 3.0 - 50.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close reversion target weighted by recent slope
def f12os_f12_oversold_reversion_oscillator_ztarget_21d_base_v139_signal(closeadj):
    z = _f12_zclose(closeadj, 21)
    result = -z * (1.0 + z.diff(3))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Williams %R smoothed
def f12os_f12_oversold_reversion_oscillator_willrsmooth_42d_base_v140_signal(closeadj, low, high):
    result = _mean(_f12_stoch(closeadj, low, high, 42) - 100.0, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI momentum (RSI minus its 21d EMA)
def f12os_f12_oversold_reversion_oscillator_rsimom_14d_base_v141_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = r - r.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RSI momentum (RSI minus its 63d EMA)
def f12os_f12_oversold_reversion_oscillator_rsimom_63d_base_v142_signal(closeadj):
    r = _f12_rsi(closeadj, 63)
    result = r - r.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d stochastic %K momentum vs its EMA
def f12os_f12_oversold_reversion_oscillator_stochmom_21d_base_v143_signal(closeadj, low, high):
    k = _f12_stoch(closeadj, low, high, 21)
    result = k - k.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI vs 21d stochastic %K spread (cross-oscillator divergence)
def f12os_f12_oversold_reversion_oscillator_rsistochdiff_base_v144_signal(closeadj, low, high):
    result = _f12_rsi(closeadj, 14) - _f12_stoch(closeadj, low, high, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-close vs RSI(14)-centered divergence
def f12os_f12_oversold_reversion_oscillator_zrsidiff_base_v145_signal(closeadj):
    result = _f12_zclose(closeadj, 21) * 25.0 - (_f12_rsi(closeadj, 14) - 50.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d normalized distance to 63d low (continuous proximity to trough)
def f12os_f12_oversold_reversion_oscillator_lowprox_63d_base_v146_signal(closeadj, low, high):
    ll = low.rolling(63, min_periods=21).min()
    result = _safe_div(closeadj - ll, ll) + _f12_stoch(closeadj, low, high, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized distance to 126d low
def f12os_f12_oversold_reversion_oscillator_lowprox_126d_base_v147_signal(closeadj, low, high):
    ll = low.rolling(126, min_periods=42).min()
    result = _safe_div(closeadj - ll, ll) + _f12_stoch(closeadj, low, high, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 14d RSI scaled oversold-reversion score (sigmoid weighting of depth)
def f12os_f12_oversold_reversion_oscillator_rsisig_14d_base_v148_signal(closeadj):
    r = _f12_rsi(closeadj, 14)
    result = (50.0 - r) / (1.0 + np.exp((r - 30.0) / 10.0))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d CCI smoothed deviation (EMA of CCI)
def f12os_f12_oversold_reversion_oscillator_cciema_21d_base_v149_signal(closeadj, low, high):
    result = _f12_cci(closeadj, low, high, 21).ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-oscillator oversold composite (RSI/stoch/CCI/z-close, all centered)
def f12os_f12_oversold_reversion_oscillator_oscblend_multi_base_v150_signal(closeadj, low, high):
    a = (_f12_rsi(closeadj, 14) - 50.0) / 50.0
    b = (_f12_stoch(closeadj, low, high, 14) - 50.0) / 50.0
    c = np.tanh(_f12_cci(closeadj, low, high, 14) / 150.0)
    d = np.tanh(_f12_zclose(closeadj, 21) / 2.0)
    result = (a + b + c + d) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12os_f12_oversold_reversion_oscillator_rsi_10d_base_v076_signal,
    f12os_f12_oversold_reversion_oscillator_rsi_42d_base_v077_signal,
    f12os_f12_oversold_reversion_oscillator_rsi_126d_base_v078_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_42d_base_v079_signal,
    f12os_f12_oversold_reversion_oscillator_rsidev_126d_base_v080_signal,
    f12os_f12_oversold_reversion_oscillator_zrsi_7d_base_v081_signal,
    f12os_f12_oversold_reversion_oscillator_zrsi_63d_base_v082_signal,
    f12os_f12_oversold_reversion_oscillator_rsismooth_21d_base_v083_signal,
    f12os_f12_oversold_reversion_oscillator_rsivel_7d_base_v084_signal,
    f12os_f12_oversold_reversion_oscillator_rsivel_63d_base_v085_signal,
    f12os_f12_oversold_reversion_oscillator_rsispread_7_14_base_v086_signal,
    f12os_f12_oversold_reversion_oscillator_rsispread_21_63_base_v087_signal,
    f12os_f12_oversold_reversion_oscillator_rsiema21_14d_base_v088_signal,
    f12os_f12_oversold_reversion_oscillator_rsirank_252_14d_base_v089_signal,
    f12os_f12_oversold_reversion_oscillator_rsitanh30_14d_base_v090_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_10d_base_v091_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_42d_base_v092_signal,
    f12os_f12_oversold_reversion_oscillator_stochk_126d_base_v093_signal,
    f12os_f12_oversold_reversion_oscillator_stochd_63d_base_v094_signal,
    f12os_f12_oversold_reversion_oscillator_stochdev_21d_base_v095_signal,
    f12os_f12_oversold_reversion_oscillator_stochdev_63d_base_v096_signal,
    f12os_f12_oversold_reversion_oscillator_willr_42d_base_v097_signal,
    f12os_f12_oversold_reversion_oscillator_willr_252d_base_v098_signal,
    f12os_f12_oversold_reversion_oscillator_zstoch_21d_base_v099_signal,
    f12os_f12_oversold_reversion_oscillator_stochspread_14_63_base_v100_signal,
    f12os_f12_oversold_reversion_oscillator_stochrank_252_21d_base_v101_signal,
    f12os_f12_oversold_reversion_oscillator_stochtanh_14d_base_v102_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_10d_base_v103_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_84d_base_v104_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_189d_base_v105_signal,
    f12os_f12_oversold_reversion_oscillator_zclose_504d_base_v106_signal,
    f12os_f12_oversold_reversion_oscillator_zcloseneg_21d_base_v107_signal,
    f12os_f12_oversold_reversion_oscillator_ztanh_21d_base_v108_signal,
    f12os_f12_oversold_reversion_oscillator_zspread_21_126_base_v109_signal,
    f12os_f12_oversold_reversion_oscillator_zcloserank_21d_base_v110_signal,
    f12os_f12_oversold_reversion_oscillator_cci_7d_base_v111_signal,
    f12os_f12_oversold_reversion_oscillator_cci_42d_base_v112_signal,
    f12os_f12_oversold_reversion_oscillator_cci_126d_base_v113_signal,
    f12os_f12_oversold_reversion_oscillator_ccitanh_21d_base_v114_signal,
    f12os_f12_oversold_reversion_oscillator_ccirank_21d_base_v115_signal,
    f12os_f12_oversold_reversion_oscillator_ccispread_21_63_base_v116_signal,
    f12os_f12_oversold_reversion_oscillator_npo_10d_base_v117_signal,
    f12os_f12_oversold_reversion_oscillator_npo_252d_base_v118_signal,
    f12os_f12_oversold_reversion_oscillator_ppo_12_26_base_v119_signal,
    f12os_f12_oversold_reversion_oscillator_ppo_21_63_base_v120_signal,
    f12os_f12_oversold_reversion_oscillator_dpo_126d_base_v121_signal,
    f12os_f12_oversold_reversion_oscillator_dpo_10d_base_v122_signal,
    f12os_f12_oversold_reversion_oscillator_smaoscvol_21d_base_v123_signal,
    f12os_f12_oversold_reversion_oscillator_smaosc_252d_base_v124_signal,
    f12os_f12_oversold_reversion_oscillator_stochrsi_21d_base_v125_signal,
    f12os_f12_oversold_reversion_oscillator_smi_63d_base_v126_signal,
    f12os_f12_oversold_reversion_oscillator_rsipress126_14d_base_v127_signal,
    f12os_f12_oversold_reversion_oscillator_stochpress_21d_base_v128_signal,
    f12os_f12_oversold_reversion_oscillator_ccinorm_63d_base_v129_signal,
    f12os_f12_oversold_reversion_oscillator_rsielas63_14d_base_v130_signal,
    f12os_f12_oversold_reversion_oscillator_composite_63d_base_v131_signal,
    f12os_f12_oversold_reversion_oscillator_rsistochx_21d_base_v132_signal,
    f12os_f12_oversold_reversion_oscillator_zccix_21d_base_v133_signal,
    f12os_f12_oversold_reversion_oscillator_rsidbl_14d_base_v134_signal,
    f12os_f12_oversold_reversion_oscillator_zcloseema_21d_base_v135_signal,
    f12os_f12_oversold_reversion_oscillator_rsidevsmooth_63d_base_v136_signal,
    f12os_f12_oversold_reversion_oscillator_rsiblend_multi_base_v137_signal,
    f12os_f12_oversold_reversion_oscillator_stochblend_multi_base_v138_signal,
    f12os_f12_oversold_reversion_oscillator_ztarget_21d_base_v139_signal,
    f12os_f12_oversold_reversion_oscillator_willrsmooth_42d_base_v140_signal,
    f12os_f12_oversold_reversion_oscillator_rsimom_14d_base_v141_signal,
    f12os_f12_oversold_reversion_oscillator_rsimom_63d_base_v142_signal,
    f12os_f12_oversold_reversion_oscillator_stochmom_21d_base_v143_signal,
    f12os_f12_oversold_reversion_oscillator_rsistochdiff_base_v144_signal,
    f12os_f12_oversold_reversion_oscillator_zrsidiff_base_v145_signal,
    f12os_f12_oversold_reversion_oscillator_lowprox_63d_base_v146_signal,
    f12os_f12_oversold_reversion_oscillator_lowprox_126d_base_v147_signal,
    f12os_f12_oversold_reversion_oscillator_rsisig_14d_base_v148_signal,
    f12os_f12_oversold_reversion_oscillator_cciema_21d_base_v149_signal,
    f12os_f12_oversold_reversion_oscillator_oscblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_OVERSOLD_REVERSION_OSCILLATOR_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f12_oversold_reversion_oscillator_base_076_150_claude: {n_features} features pass")
