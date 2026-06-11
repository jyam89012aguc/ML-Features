"""f19_atr_normalized_price jerk 001-150 (2nd derivative). Each fn computes base
inline (with _tr/_atr/_sma/_ema helpers); returns b - 2*b.shift(k) + b.shift(2k).
NaN policy: only the final replace([inf,-inf],nan). Window > 21d uses closeadj."""
from __future__ import annotations
import numpy as np
import pandas as pd


def _tr(high, low, c):
    pc = c.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, c, n):
    return _tr(high, low, c).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _ds(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def f19an_f19_atr_normalized_price_close_sma8_atr14_8d_jerk_v001_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (close - _sma(close, 8)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_sma50_atr20_50d_jerk_v002_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    b = (closeadj - _sma(closeadj, 50)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sign_close_sma100_atr_100d_jerk_v003_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 50)
    z = (closeadj - _sma(closeadj, 100)) / a.replace(0.0, np.nan)
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.where(z <= 1.0, 1.0)
    out = out.where(z >= -1.0, -1.0)
    b = out.where(~z.isna())
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_sma200_atr100_200d_jerk_v004_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 100)
    b = (closeadj - _sma(closeadj, 200)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ret5_atr5_5d_jerk_v005_signal(high, low, close):
    a = _atr(high, low, close, 5)
    raw = (close - close.shift(5)) / a.replace(0.0, np.nan)
    b = raw * raw
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ret20_atr14_20d_jerk_v006_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (close - close.shift(20)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ret63_atr30_63d_jerk_v007_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    b = (closeadj - closeadj.shift(63)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_high20_atr14_20d_jerk_v008_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (close - high.rolling(20, min_periods=20).max()) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_low20_atr14_20d_jerk_v009_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (close - low.rolling(20, min_periods=20).min()) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_high60_atr30_60d_jerk_v010_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    b = (closeadj - high.rolling(60, min_periods=60).max()) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dayssince_120d_low_120d_jerk_v011_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    prior_low = low.rolling(120, min_periods=120).min().shift(1)
    fresh = ((closeadj - prior_low) / a.replace(0.0, np.nan) < 0.0).astype(float).where(~a.isna() & ~prior_low.isna())
    b = fresh.rolling(120, min_periods=120).apply(_ds, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sma5_sma20_atr14_20d_jerk_v012_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (_sma(close, 5) - _sma(close, 20)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_xover_count_macd_60d_jerk_v013_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (_ema(close, 12) - _ema(close, 26)) / a.replace(0.0, np.nan)
    s = np.sign(z)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(60, min_periods=60).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sma50_sma200_atr50_200d_jerk_v014_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 50)
    b = (_sma(closeadj, 50) - _sma(closeadj, 200)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_hl_atr14_14d_jerk_v015_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (high - low) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_body_atr10_10d_jerk_v016_signal(high, low, close, open):
    a = _atr(high, low, close, 10)
    b = (close - open) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_upwick_atr14_14d_jerk_v017_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    top = pd.concat([open, close], axis=1).max(axis=1)
    b = (high - top) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_lowwick_atr14_14d_jerk_v018_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    bot = pd.concat([open, close], axis=1).min(axis=1)
    b = (bot - low) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_gap_atr14_14d_jerk_v019_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    b = (open - close.shift(1)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_abs_gap_atr14_14d_jerk_v020_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    b = (open - close.shift(1)).abs() / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr5_atr50_50d_jerk_v021_signal(high, low, close):
    a5 = _atr(high, low, close, 5)
    a50 = _atr(high, low, close, 50)
    b = a5 / a50.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr20_atr200_200d_jerk_v022_signal(high, low, closeadj):
    a20 = _atr(high, low, closeadj, 20)
    a200 = _atr(high, low, closeadj, 200)
    b = a20 / a200.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_log_atr10_atr100_100d_jerk_v023_signal(high, low, closeadj):
    a10 = _atr(high, low, closeadj, 10)
    a100 = _atr(high, low, closeadj, 100)
    b = np.log(a10 / a100.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_slope_30d_norm_jerk_v024_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    b = (a - a.shift(30)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_keltner_pos_20d_20d_jerk_v025_signal(high, low, close):
    a = _atr(high, low, close, 20)
    mid = _sma(close, 20)
    lower = mid - 2.0 * a
    width = 4.0 * a
    b = (close - lower) / width.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_since_atr_band_120d_jerk_v026_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    sma = _sma(closeadj, 60)
    flag = ((closeadj > sma + 2.0 * a) | (closeadj < sma - 2.0 * a)).astype(float).where(~a.isna() & ~sma.isna())
    b = flag.rolling(120, min_periods=120).apply(_ds, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_roc10_atr10_10d_jerk_v027_signal(high, low, close):
    a = _atr(high, low, close, 10)
    roc = np.log(close / close.shift(10))
    atr_pct = a / close.replace(0.0, np.nan)
    b = roc / atr_pct.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_cumret_cumatr_30d_jerk_v028_signal(high, low, closeadj):
    tr = _tr(high, low, closeadj)
    csum_tr = tr.rolling(30, min_periods=30).sum()
    csum_ret = closeadj - closeadj.shift(30)
    raw = csum_ret / csum_tr.replace(0.0, np.nan)
    b = np.sign(raw).where(~raw.isna())
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_signed_count_atr_30d_jerk_v029_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - close.shift(1)) / a.replace(0.0, np.nan)
    pos = (z > 0.5).astype(float).where(~z.isna())
    neg = (z < -0.5).astype(float).where(~z.isna())
    b = (pos - neg).rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_residual_acf_80d_jerk_v030_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    z = (closeadj - _sma(closeadj, 20)) / a.replace(0.0, np.nan)
    b = z.rolling(80, min_periods=80).corr(z.shift(5))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dd_severity_60d_jerk_v031_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    peak = closeadj.rolling(60, min_periods=60).max()
    dd = (peak - closeadj) / a.replace(0.0, np.nan)
    flag = (dd > 2.0).astype(float).where(~dd.isna())
    b = flag.rolling(60, min_periods=60).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_rally_strength_atr_120d_jerk_v032_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    direction = np.sign(closeadj - closeadj.shift(120))
    push = ((closeadj - closeadj.shift(20)) / a.replace(0.0, np.nan) > 1.0).astype(float).where(~a.isna())
    b = direction * push.rolling(120, min_periods=120).sum()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_absret1_atr14_jerk_v033_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = (close - close.shift(1)).abs() / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_max_absret_atr_20d_jerk_v034_signal(high, low, close):
    a = _atr(high, low, close, 20)
    ar = (close - close.shift(1)).abs()
    b = ar.rolling(20, min_periods=20).max() / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_min_ret_atr_60d_jerk_v035_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    r = closeadj - closeadj.shift(1)
    b = r.rolling(60, min_periods=60).min() / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_count_1atr_30d_jerk_v036_signal(high, low, close):
    a = _atr(high, low, close, 14)
    pc = close.shift(1)
    flag = ((close - pc).abs() > a).astype(float).where(~a.isna() & ~pc.isna())
    b = flag.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_count_2atr_60d_jerk_v037_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    pc = closeadj.shift(1)
    flag = ((closeadj - pc).abs() > 2.0 * a).astype(float).where(~a.isna() & ~pc.isna())
    b = flag.rolling(60, min_periods=60).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dayssince_2atr_120d_jerk_v038_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    pc = closeadj.shift(1)
    flag = ((closeadj - pc).abs() > 2.0 * a).astype(float).where(~a.isna() & ~pc.isna())
    b = flag.rolling(120, min_periods=120).apply(_ds, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_signed_dist_sma40_atr14_jerk_v039_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    m = _sma(closeadj, 40)
    raw = (closeadj - m) / a.replace(0.0, np.nan)
    direction = np.sign(m - m.shift(10))
    b = raw * direction
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_std_atr_60d_norm_jerk_v040_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    sd = a.rolling(60, min_periods=60).std()
    b = sd / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_diff_pct_50d_jerk_v041_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    b = a.diff(50) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_regime_252d_jerk_v042_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    q25 = a.rolling(252, min_periods=252).quantile(0.25)
    q75 = a.rolling(252, min_periods=252).quantile(0.75)
    out = pd.Series(1.0, index=a.index, dtype=float)
    out = out.where(a <= q75, 2.0)
    out = out.where(a >= q25, 0.0)
    b = out.where(~q25.isna() & ~q75.isna() & ~a.isna())
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_in_high_atr_252d_jerk_v043_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    med = a.rolling(252, min_periods=252).median()
    flag = (a > med).astype(float).where(~a.isna() & ~med.isna())
    b = flag.rolling(60, min_periods=60).mean()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_arctan_absret_60d_jerk_v044_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - close.shift(1)).abs() / a.replace(0.0, np.nan)
    bz = 2.0 / np.pi * np.arctan(z)
    b = bz.rolling(60, min_periods=60).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tanh_ret60_atr80_jerk_v045_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 80)
    z = (closeadj - closeadj.shift(60)) / (3.0 * a).replace(0.0, np.nan)
    b = np.tanh(z)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sigmoid_zatr_30d_jerk_v046_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    z = ((closeadj - _sma(closeadj, 30)) / a.replace(0.0, np.nan)).clip(-50.0, 50.0)
    b = 1.0 / (1.0 + np.exp(-z))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_pct_vs_stdret_30d_jerk_v047_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    r = np.log(closeadj / closeadj.shift(1))
    sd = r.rolling(30, min_periods=30).std()
    atr_pct = a / closeadj.replace(0.0, np.nan)
    b = atr_pct / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_streak_above_atr_band_60d_jerk_v048_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    sma = _sma(closeadj, 30)
    above = (closeadj > sma + 0.5 * a).astype(float).where(~a.isna() & ~sma.isna())
    def _sp(x):
        idx = np.where(x < 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    b = above.rolling(60, min_periods=60).apply(_sp, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_streak_below_atr_band_60d_jerk_v049_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    sma = _sma(closeadj, 30)
    below = (closeadj < sma - 0.5 * a).astype(float).where(~a.isna() & ~sma.isna())
    def _sp(x):
        idx = np.where(x < 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    b = below.rolling(60, min_periods=60).apply(_sp, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_typical_minus_close_atr14_jerk_v050_signal(high, low, close):
    a = _atr(high, low, close, 14)
    tp = (high + low + close) / 3.0
    b = (tp - close) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tr_atr14_jerk_v051_signal(high, low, close):
    a = _atr(high, low, close, 14)
    b = _tr(high, low, close) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tr_atr_max60d_jerk_v052_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    mx = _tr(high, low, closeadj).rolling(60, min_periods=60).max()
    b = mx / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_stdclose_atr_30d_jerk_v053_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    sd = closeadj.rolling(30, min_periods=30).std()
    b = sd / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_above_1atr_sma20_jerk_v054_signal(high, low, close):
    a = _atr(high, low, close, 14)
    sma = _sma(close, 20)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(close <= sma + a, 1.0)
    out = out.where(close >= sma - a, -1.0)
    b = out.where(~a.isna() & ~sma.isna())
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_above_2atr_sma50_jerk_v055_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 50)
    sma = _sma(closeadj, 50)
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.where(closeadj <= sma + 2.0 * a, 1.0)
    out = out.where(closeadj >= sma - 2.0 * a, -1.0)
    b = out.where(~a.isna() & ~sma.isna())
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_skew_retatr_60d_jerk_v056_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(60, min_periods=60).skew()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_kurt_retatr_120d_jerk_v057_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(120, min_periods=120).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_open_close_diff_atr_5d_jerk_v058_signal(high, low, close, open):
    a = _atr(high, low, close, 5)
    body_sum = (close - open).rolling(5, min_periods=5).sum()
    b = body_sum / (5.0 * a).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_rank_close_sma20_60d_jerk_v059_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    z = (closeadj - _sma(closeadj, 20)) / a.replace(0.0, np.nan)
    b = z.rolling(60, min_periods=60).rank(pct=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_frac_above_atr_band_30d_jerk_v060_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    sma = _sma(closeadj, 30)
    flag = (closeadj > sma + 0.5 * a).astype(float).where(~a.isna() & ~sma.isna())
    b = flag.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_range_width_60d_atr_jerk_v061_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    hh = high.rolling(60, min_periods=60).max()
    ll = low.rolling(60, min_periods=60).min()
    b = (hh - ll) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_pos_minus_neg_eventfreq_120d_jerk_v062_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    pos = (z > 1.0).astype(float).where(~z.isna())
    neg = (z < -1.0).astype(float).where(~z.isna())
    b = (pos - neg).rolling(120, min_periods=120).sum()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_neg_ret_count_atr_30d_jerk_v063_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    pc = closeadj.shift(1)
    z = (closeadj - pc) / a.replace(0.0, np.nan)
    flag = (z < -1.0).astype(float).where(~a.isna() & ~pc.isna())
    b = flag.rolling(30, min_periods=30).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_autocorr_retatr_50d_jerk_v064_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(50, min_periods=50).corr(z.shift(1))
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atrband_crosses_40d_jerk_v065_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    sma = _sma(closeadj, 20)
    state = pd.Series(0.0, index=closeadj.index, dtype=float)
    state = state.where(closeadj <= sma + a, 1.0)
    state = state.where(closeadj >= sma - a, -1.0)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    b = flip.rolling(40, min_periods=40).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)




def f19an_f19_atr_normalized_price_ema_ribbon_disp_atr_jerk_v067_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    mat = pd.concat([_ema(closeadj, 10), _ema(closeadj, 20), _ema(closeadj, 40)], axis=1)
    span = mat.max(axis=1) - mat.min(axis=1)
    b = span / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_high_minus_close_atr_5d_jerk_v068_signal(high, low, close):
    a = _atr(high, low, close, 5)
    b = (high - close) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_minus_low_atr_5d_jerk_v069_signal(high, low, close):
    a = _atr(high, low, close, 5)
    b = (close - low) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_q90_q10_120d_jerk_v070_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    q90 = a.rolling(120, min_periods=120).quantile(0.9)
    q10 = a.rolling(120, min_periods=120).quantile(0.1)
    b = np.log(q90 / q10.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_gapfill_atr_5d_jerk_v071_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    pc = close.shift(1)
    gap_sign = np.sign(open - pc)
    b = -1.0 * gap_sign * (close - open) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_underwater_atr_60d_jerk_v072_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    peak = closeadj.rolling(60, min_periods=60).max()
    def _dsp(x):
        idx = int(np.argmax(x))
        return float(len(x) - 1 - idx)
    dsp = closeadj.rolling(60, min_periods=60).apply(_dsp, raw=True)
    b = dsp * (peak - closeadj) / (60.0 * a).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_macd_above_signal_60d_jerk_v073_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    macd = _ema(closeadj, 12) - _ema(closeadj, 26)
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = (macd - sig) / a.replace(0.0, np.nan)
    flag = (hist > 0.0).astype(float).where(~hist.isna())
    b = flag.rolling(60, min_periods=60).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_rank_252d_jerk_v074_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    r = a.rolling(252, min_periods=252).rank(pct=True)
    b = (r - 0.5) ** 2
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_reversion_z_atr_45d_jerk_v075_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    z = (closeadj - _sma(closeadj, 45)) / a.replace(0.0, np.nan)
    b = z - z.rolling(45, min_periods=45).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_minus_high40_atr25_jerk_v076_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 25)
    b = (closeadj - high.rolling(40, min_periods=40).max()) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_minus_low40_atr25_jerk_v077_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 25)
    b = (closeadj - low.rolling(40, min_periods=40).min()) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_chand_exit_long_22d_jerk_v078_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 22)
    hh = high.rolling(22, min_periods=22).max()
    b = (hh - 3.0 * a - closeadj) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_chand_exit_short_22d_jerk_v079_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 22)
    ll = low.rolling(22, min_periods=22).min()
    raw = (closeadj - (ll + 3.0 * a)) / a.replace(0.0, np.nan)
    b = np.arctan(raw)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_supertrend_dist_atr_15d_jerk_v080_signal(high, low, close):
    a = _atr(high, low, close, 15)
    mid = (high + low) / 2.0
    b = (mid - 3.0 * a - close) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_donchian_pos_20d_atr_jerk_v081_signal(high, low, close):
    a = _atr(high, low, close, 20)
    hh = high.rolling(20, min_periods=20).max()
    raw = (close - hh) / a.replace(0.0, np.nan)
    b = -(raw * raw)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_donchian_width_55d_atr_jerk_v082_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 40)
    hh = high.rolling(55, min_periods=55).max()
    ll = low.rolling(55, min_periods=55).min()
    b = (hh - ll) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_weighted_ma_30d_jerk_v083_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 15)
    w = 1.0 / a.replace(0.0, np.nan)
    num = (closeadj * w).rolling(30, min_periods=30).sum()
    den = w.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    mw = num / den
    raw = (closeadj - mw) / a.replace(0.0, np.nan)
    b = np.sign(raw).where(~raw.isna())
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_smooth_diff_25d_jerk_v084_signal(high, low, closeadj):
    tr = _tr(high, low, closeadj)
    sma_tr = tr.rolling(25, min_periods=25).mean()
    wild = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    b = (sma_tr - wild) / wild.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_3bar_move_atr_7d_jerk_v085_signal(high, low, close):
    a = _atr(high, low, close, 7)
    b = (close - close.shift(3)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_10bar_move_atr_25d_jerk_v086_signal(high, low, close):
    a = _atr(high, low, close, 25)
    raw = (close - close.shift(10)) / a.replace(0.0, np.nan)
    b = raw.abs()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_short_long_pct_jerk_v087_signal(high, low, closeadj):
    a7 = _atr(high, low, closeadj, 7)
    a70 = _atr(high, low, closeadj, 70)
    raw = (a7 - a70) / a70.replace(0.0, np.nan)
    b = np.sign(raw) * raw.abs().pow(0.5)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)




def f19an_f19_atr_normalized_price_atr_pct_close_60d_jerk_v089_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    b = a / closeadj.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_count_15atr_45d_jerk_v090_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    pc = closeadj.shift(1)
    flag = ((closeadj - pc).abs() > 1.5 * a).astype(float).where(~a.isna() & ~pc.isna())
    b = flag.rolling(45, min_periods=45).sum()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_max_5d_move_atr_252d_jerk_v091_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 40)
    five = (closeadj - closeadj.shift(5)).abs()
    mx = five.rolling(252, min_periods=252).max()
    b = mx / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_max_signed_ret_atr_180d_jerk_v092_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(180, min_periods=180).max()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_min_signed_ret_atr_180d_jerk_v093_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(180, min_periods=180).min()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_body_atr_30d_jerk_v094_signal(high, low, closeadj, open):
    a = _atr(high, low, closeadj, 20)
    body = (closeadj - open).abs()
    b = body.rolling(30, min_periods=30).mean() / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_range_atr_50d_jerk_v095_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 50)
    rng = (high - low).rolling(50, min_periods=50).mean()
    b = rng / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_williamsR_atr_14d_jerk_v096_signal(high, low, close):
    a = _atr(high, low, close, 14)
    hh = high.rolling(14, min_periods=14).max()
    b = (hh - close) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_30d_move_60d_atr_jerk_v097_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    b = (closeadj - closeadj.shift(30)) / (np.sqrt(30.0) * a).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_upwick_minus_lowwick_15d_jerk_v098_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    top = pd.concat([open, close], axis=1).max(axis=1)
    bot = pd.concat([open, close], axis=1).min(axis=1)
    asym = (high - top) - (bot - low)
    b = asym.rolling(15, min_periods=15).sum() / (15.0 * a).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_zscore_close_atr_15d_jerk_v099_signal(high, low, close):
    a = _atr(high, low, close, 15)
    z = (close - _sma(close, 15)) / a.replace(0.0, np.nan)
    b = z.rolling(15, min_periods=15).max() - z.rolling(15, min_periods=15).min()
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_above_05atr_sma8_jerk_v100_signal(high, low, close):
    a = _atr(high, low, close, 8)
    sma = _sma(close, 8)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(close <= sma + 0.5 * a, 1.0)
    out = out.where(close >= sma - 0.5 * a, -1.0)
    b = out.where(~a.isna() & ~sma.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ema_cross_8_30_atr_jerk_v101_signal(high, low, close):
    a = _atr(high, low, close, 15)
    b = (_ema(close, 8) - _ema(close, 30)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ema_cross_20_80_atr_jerk_v102_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 40)
    b = (_ema(closeadj, 20) - _ema(closeadj, 80)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_slope_5d_short_jerk_v103_signal(high, low, close):
    a = _atr(high, low, close, 7)
    b = (a - a.shift(5)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_slope_90d_long_jerk_v104_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    b = (a - a.shift(90)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_median_tr_atr_45d_jerk_v105_signal(high, low, closeadj):
    tr = _tr(high, low, closeadj)
    med_tr = tr.rolling(45, min_periods=45).median()
    a = tr.ewm(alpha=1.0 / 45.0, adjust=False, min_periods=45).mean()
    b = med_tr / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_close_corr_60d_jerk_v106_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    b = a.rolling(60, min_periods=60).corr(closeadj)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_logret_corr_120d_jerk_v107_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    ar = np.log(closeadj / closeadj.shift(1)).abs()
    b = a.rolling(120, min_periods=120).corr(ar)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_short_long_move_atr_60d_jerk_v108_signal(high, low, closeadj):
    a10 = _atr(high, low, closeadj, 10)
    a60 = _atr(high, low, closeadj, 60)
    z10 = (closeadj - closeadj.shift(10)) / a10.replace(0.0, np.nan)
    z60 = (closeadj - closeadj.shift(60)) / a60.replace(0.0, np.nan)
    b = z10 - z60
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_signed_ret_atr_sum_20d_jerk_v109_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - close.shift(1)) / a.replace(0.0, np.nan)
    s = z.rolling(20, min_periods=20).sum()
    b = np.sign(s) * np.log1p(s.abs())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_signed_ret_atr_sum_80d_jerk_v110_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(80, min_periods=80).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_retatr_lag5_autocorr_100d_jerk_v111_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(100, min_periods=100).corr(z.shift(5))
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_abs_gap_mean_atr_30d_jerk_v112_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    ag = (open - close.shift(1)).abs() / a.replace(0.0, np.nan)
    b = ag.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_gap_std_atr_45d_jerk_v113_signal(high, low, close, open):
    a = _atr(high, low, close, 14)
    gap = (open - close.shift(1)) / a.replace(0.0, np.nan)
    b = gap.rolling(45, min_periods=45).std()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_skew_60d_jerk_v114_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    b = a.rolling(60, min_periods=60).skew()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_kurt_120d_jerk_v115_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    b = a.rolling(120, min_periods=120).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_vw_atr_dispersion_30d_jerk_v116_signal(high, low, closeadj, volume):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    z2 = z * z
    wsum = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    wm = (volume * z).rolling(30, min_periods=30).sum() / wsum
    wm2 = (volume * z2).rolling(30, min_periods=30).sum() / wsum
    vw_var = (wm2 - wm * wm).clip(lower=0.0)
    eq_var = z.rolling(30, min_periods=30).var()
    b = vw_var.pow(0.5) - eq_var.pow(0.5)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_hma_dist_atr_30d_jerk_v117_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    n = 30; half = 15; sqn = 5
    w_half = np.arange(1, half + 1, dtype=float); w_half /= w_half.sum()
    w_n = np.arange(1, n + 1, dtype=float); w_n /= w_n.sum()
    w_sqn = np.arange(1, sqn + 1, dtype=float); w_sqn /= w_sqn.sum()
    wma_half = closeadj.rolling(half, min_periods=half).apply(lambda x: float(np.dot(x, w_half)), raw=True)
    wma_n = closeadj.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w_n)), raw=True)
    raw = 2.0 * wma_half - wma_n
    hma = raw.rolling(sqn, min_periods=sqn).apply(lambda x: float(np.dot(x, w_sqn)), raw=True)
    b = (closeadj - hma) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_state_flips_80d_jerk_v118_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 40)
    sma = _sma(closeadj, 40)
    z = (closeadj - sma) / a.replace(0.0, np.nan)
    state = pd.Series(0.0, index=closeadj.index, dtype=float)
    state = state.where(z <= 0.5, 1.0)
    state = state.where(z >= -0.5, -1.0)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    b = flip.rolling(80, min_periods=80).sum()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_logret_mean_atr_15d_jerk_v119_signal(high, low, close):
    a = _atr(high, low, close, 15)
    r = np.log(close / close.shift(1))
    b = r.rolling(15, min_periods=15).mean() / (a / close.replace(0.0, np.nan)).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_logret_mean_atr_120d_jerk_v120_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 120)
    r = np.log(closeadj / closeadj.shift(1))
    b = r.rolling(120, min_periods=120).mean() / (a / closeadj.replace(0.0, np.nan)).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_rmax_rmin_40d_jerk_v121_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    mx = a.rolling(40, min_periods=40).max()
    mn = a.rolling(40, min_periods=40).min().replace(0.0, np.nan)
    b = mx / mn
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_skew_atr_sq_ret_120d_jerk_v122_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = ((closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)) ** 2
    b = z.rolling(120, min_periods=120).skew()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_z_iqr_90d_jerk_v123_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    q75 = z.rolling(90, min_periods=90).quantile(0.75)
    q25 = z.rolling(90, min_periods=90).quantile(0.25)
    b = q75 - q25
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_since_high_atr_252d_jerk_v124_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    q80 = a.rolling(252, min_periods=252).quantile(0.8)
    flag = (a > q80).astype(float).where(~a.isna() & ~q80.isna())
    b = flag.rolling(252, min_periods=252).apply(_ds, raw=True)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_move_bucket_jerk_v125_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - close.shift(1)) / a.replace(0.0, np.nan)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(z <= 1.0, 1.0)
    out = out.where(z <= 2.0, 2.0)
    out = out.where(z >= -1.0, -1.0)
    out = out.where(z >= -2.0, -2.0)
    b = out.where(~z.isna())
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_path_atr_efficiency_30d_jerk_v126_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    tr = _tr(high, low, closeadj)
    cum_path = (tr / a.replace(0.0, np.nan)).rolling(30, min_periods=30).sum()
    net = (closeadj - closeadj.shift(30)).abs() / a.replace(0.0, np.nan)
    b = net / cum_path.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_high5_atr_short_jerk_v127_signal(high, low, close):
    a = _atr(high, low, close, 7)
    hh = high.rolling(5, min_periods=5).max()
    b = (close - hh) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(10)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_accel_atr_15d_jerk_v128_signal(high, low, close):
    a = _atr(high, low, close, 15)
    b = (close - 2.0 * close.shift(15) + close.shift(30)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_accel_atr_60d_jerk_v129_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    b = (closeadj - 2.0 * closeadj.shift(60) + closeadj.shift(120)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sigmoid_long_atr_z_jerk_v130_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    z = ((closeadj - _sma(closeadj, 120)) / a.replace(0.0, np.nan)).clip(-50.0, 50.0)
    b = (z - 2.0 * z.shift(21) + z.shift(42)).abs()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_underwater_atr_120d_jerk_v131_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    peak = closeadj.rolling(120, min_periods=120).max()
    z = (closeadj - peak) / a.replace(0.0, np.nan)
    flag = (z < -1.0).astype(float).where(~z.isna())
    b = flag.rolling(120, min_periods=120).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_squeeze_60d_jerk_v132_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    mx = a.rolling(60, min_periods=60).max().replace(0.0, np.nan)
    b = a / mx
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_keltner_BB_tightness_jerk_v133_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    sd = closeadj.rolling(20, min_periods=20).std()
    b = a / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ma_consensus_atr_band_jerk_v134_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    m10 = _sma(closeadj, 10); m20 = _sma(closeadj, 20); m40 = _sma(closeadj, 40); m80 = _sma(closeadj, 80)
    band = 0.25 * a
    flags = [(closeadj > m10 + band).astype(float), (closeadj > m20 + band).astype(float),
             (closeadj > m40 + band).astype(float), (closeadj > m80 + band).astype(float)]
    mask = ~m80.isna() & ~a.isna()
    b = sum(flags).where(mask)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_pos_252d_atr_jerk_v135_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    hh = high.rolling(252, min_periods=252).max()
    ll = low.rolling(252, min_periods=252).min()
    raw = (closeadj - 0.5 * (hh + ll)) / a.replace(0.0, np.nan)
    b = raw.rolling(252, min_periods=252).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_close_to_high_atr_30d_jerk_v136_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (high - close) / a.replace(0.0, np.nan)
    b = z.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_close_to_low_atr_30d_jerk_v137_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - low) / a.replace(0.0, np.nan)
    b = z.rolling(30, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_median_signed_ret_atr_60d_jerk_v138_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(60, min_periods=60).median()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_revstrength_atr_15d_jerk_v139_signal(high, low, close):
    a = _atr(high, low, close, 14)
    z = (close - _sma(close, 15)) / a.replace(0.0, np.nan)
    r = np.log(close / close.shift(1))
    b = z.rolling(15, min_periods=15).corr(-r)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_trend_conf_atr_45d_jerk_v140_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    direction = np.sign(_ema(closeadj, 20) - _ema(closeadj, 50))
    move = (closeadj - closeadj.shift(20)) / a.replace(0.0, np.nan)
    b = direction * move
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def _ols_slope(y):
    if not np.all(np.isfinite(y)):
        return np.nan
    x = np.arange(len(y), dtype=float)
    xm = x.mean(); ym = y.mean()
    den = float(((x - xm) ** 2).sum())
    if den == 0.0:
        return np.nan
    return float(((x - xm) * (y - ym)).sum() / den)


def f19an_f19_atr_normalized_price_regslope_atr_30d_jerk_v141_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    slope = closeadj.rolling(30, min_periods=30).apply(_ols_slope, raw=True)
    b = slope / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_chand_spread_15d_jerk_v142_signal(high, low, close):
    a = _atr(high, low, close, 15)
    upper_long = high.rolling(15, min_periods=15).max() - 3.0 * a
    upper_short = low.rolling(15, min_periods=15).min() + 3.0 * a
    b = (upper_short - upper_long) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_pct_above_q70_atr_z_jerk_v143_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    z = (closeadj - _sma(closeadj, 20)) / a.replace(0.0, np.nan)
    q70 = z.rolling(252, min_periods=252).quantile(0.7)
    flag = (z > q70).astype(float).where(~z.isna() & ~q70.isna())
    b = flag.rolling(60, min_periods=60).mean()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tr_expansion_atr_30d_jerk_v144_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 20)
    tr = _tr(high, low, closeadj)
    b = (tr - tr.shift(5)) / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(20)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_frac_extreme_atr_z_120d_jerk_v145_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 30)
    z = ((closeadj - _sma(closeadj, 30)) / a.replace(0.0, np.nan)).abs()
    flag = (z > 2.0).astype(float).where(~z.isna())
    b = flag.rolling(120, min_periods=120).mean()
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_vol_corr_60d_jerk_v146_signal(high, low, closeadj, volume):
    a = _atr(high, low, closeadj, 14)
    lv = np.log(volume.replace(0.0, np.nan))
    b = a.rolling(60, min_periods=60).corr(lv)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_regslope_atr_long_120d_jerk_v147_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 60)
    slope = closeadj.rolling(120, min_periods=120).apply(_ols_slope, raw=True)
    b = slope / a.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(126)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_hl_dist_from_atr_60d_jerk_v148_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = ((high - low) - a) / a.replace(0.0, np.nan)
    b = z.rolling(60, min_periods=60).mean()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_var_retatr_30d_jerk_v149_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    b = z.rolling(30, min_periods=30).var()
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def _max_run(x):
    if not np.all(np.isfinite(x)):
        return np.nan
    m = 0; c = 0
    for v in x:
        if v > 0.5:
            c += 1
            if c > m:
                m = c
        else:
            c = 0
    return float(m)


def f19an_f19_atr_normalized_price_max_consec_atr_up_60d_jerk_v150_signal(high, low, closeadj):
    a = _atr(high, low, closeadj, 14)
    z = (closeadj - closeadj.shift(1)) / a.replace(0.0, np.nan)
    flag = (z > 0.5).astype(float).where(~z.isna())
    b = flag.rolling(60, min_periods=60).apply(_max_run, raw=True)
    return (b - 2.0 * b.shift(21) + b.shift(42)).replace([np.inf, -np.inf], np.nan)


def _R(f, inputs):
    return f.__name__, {"inputs": inputs, "func": f}


_FNS = [
    (f19an_f19_atr_normalized_price_close_sma8_atr14_8d_jerk_v001_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_close_sma50_atr20_50d_jerk_v002_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_sign_close_sma100_atr_100d_jerk_v003_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_close_sma200_atr100_200d_jerk_v004_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_ret5_atr5_5d_jerk_v005_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_ret20_atr14_20d_jerk_v006_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_ret63_atr30_63d_jerk_v007_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_dist_high20_atr14_20d_jerk_v008_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_dist_low20_atr14_20d_jerk_v009_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_dist_high60_atr30_60d_jerk_v010_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_dayssince_120d_low_120d_jerk_v011_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_sma5_sma20_atr14_20d_jerk_v012_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_xover_count_macd_60d_jerk_v013_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_sma50_sma200_atr50_200d_jerk_v014_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_hl_atr14_14d_jerk_v015_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_body_atr10_10d_jerk_v016_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_upwick_atr14_14d_jerk_v017_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_lowwick_atr14_14d_jerk_v018_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_gap_atr14_14d_jerk_v019_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_abs_gap_atr14_14d_jerk_v020_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_atr5_atr50_50d_jerk_v021_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_atr20_atr200_200d_jerk_v022_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_log_atr10_atr100_100d_jerk_v023_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_slope_30d_norm_jerk_v024_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_keltner_pos_20d_20d_jerk_v025_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_days_since_atr_band_120d_jerk_v026_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_roc10_atr10_10d_jerk_v027_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_cumret_cumatr_30d_jerk_v028_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_signed_count_atr_30d_jerk_v029_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_atr_residual_acf_80d_jerk_v030_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_dd_severity_60d_jerk_v031_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_rally_strength_atr_120d_jerk_v032_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_absret1_atr14_jerk_v033_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_max_absret_atr_20d_jerk_v034_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_min_ret_atr_60d_jerk_v035_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_count_1atr_30d_jerk_v036_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_count_2atr_60d_jerk_v037_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_dayssince_2atr_120d_jerk_v038_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_signed_dist_sma40_atr14_jerk_v039_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_std_atr_60d_norm_jerk_v040_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_diff_pct_50d_jerk_v041_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_regime_252d_jerk_v042_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_days_in_high_atr_252d_jerk_v043_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_arctan_absret_60d_jerk_v044_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_tanh_ret60_atr80_jerk_v045_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_sigmoid_zatr_30d_jerk_v046_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_pct_vs_stdret_30d_jerk_v047_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_streak_above_atr_band_60d_jerk_v048_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_streak_below_atr_band_60d_jerk_v049_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_typical_minus_close_atr14_jerk_v050_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_tr_atr14_jerk_v051_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_tr_atr_max60d_jerk_v052_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_stdclose_atr_30d_jerk_v053_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_above_1atr_sma20_jerk_v054_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_above_2atr_sma50_jerk_v055_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_skew_retatr_60d_jerk_v056_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_kurt_retatr_120d_jerk_v057_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_open_close_diff_atr_5d_jerk_v058_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_rank_close_sma20_60d_jerk_v059_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_frac_above_atr_band_30d_jerk_v060_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_range_width_60d_atr_jerk_v061_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_pos_minus_neg_eventfreq_120d_jerk_v062_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_neg_ret_count_atr_30d_jerk_v063_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_autocorr_retatr_50d_jerk_v064_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atrband_crosses_40d_jerk_v065_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_ema_ribbon_disp_atr_jerk_v067_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_high_minus_close_atr_5d_jerk_v068_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_close_minus_low_atr_5d_jerk_v069_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_atr_q90_q10_120d_jerk_v070_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_gapfill_atr_5d_jerk_v071_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_underwater_atr_60d_jerk_v072_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_macd_above_signal_60d_jerk_v073_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_rank_252d_jerk_v074_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_reversion_z_atr_45d_jerk_v075_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_close_minus_high40_atr25_jerk_v076_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_close_minus_low40_atr25_jerk_v077_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_chand_exit_long_22d_jerk_v078_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_chand_exit_short_22d_jerk_v079_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_supertrend_dist_atr_15d_jerk_v080_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_donchian_pos_20d_atr_jerk_v081_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_donchian_width_55d_atr_jerk_v082_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_weighted_ma_30d_jerk_v083_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_smooth_diff_25d_jerk_v084_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_3bar_move_atr_7d_jerk_v085_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_10bar_move_atr_25d_jerk_v086_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_atr_short_long_pct_jerk_v087_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_pct_close_60d_jerk_v089_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_count_15atr_45d_jerk_v090_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_max_5d_move_atr_252d_jerk_v091_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_max_signed_ret_atr_180d_jerk_v092_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_min_signed_ret_atr_180d_jerk_v093_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_avg_body_atr_30d_jerk_v094_signal, ["high","low","closeadj","open"]),
    (f19an_f19_atr_normalized_price_avg_range_atr_50d_jerk_v095_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_williamsR_atr_14d_jerk_v096_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_30d_move_60d_atr_jerk_v097_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_upwick_minus_lowwick_15d_jerk_v098_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_zscore_close_atr_15d_jerk_v099_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_above_05atr_sma8_jerk_v100_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_ema_cross_8_30_atr_jerk_v101_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_ema_cross_20_80_atr_jerk_v102_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_slope_5d_short_jerk_v103_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_atr_slope_90d_long_jerk_v104_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_median_tr_atr_45d_jerk_v105_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_close_corr_60d_jerk_v106_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_logret_corr_120d_jerk_v107_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_short_long_move_atr_60d_jerk_v108_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_signed_ret_atr_sum_20d_jerk_v109_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_signed_ret_atr_sum_80d_jerk_v110_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_retatr_lag5_autocorr_100d_jerk_v111_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_abs_gap_mean_atr_30d_jerk_v112_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_gap_std_atr_45d_jerk_v113_signal, ["high","low","close","open"]),
    (f19an_f19_atr_normalized_price_atr_skew_60d_jerk_v114_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_kurt_120d_jerk_v115_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_vw_atr_dispersion_30d_jerk_v116_signal, ["high","low","closeadj","volume"]),
    (f19an_f19_atr_normalized_price_hma_dist_atr_30d_jerk_v117_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_state_flips_80d_jerk_v118_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_logret_mean_atr_15d_jerk_v119_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_logret_mean_atr_120d_jerk_v120_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_rmax_rmin_40d_jerk_v121_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_skew_atr_sq_ret_120d_jerk_v122_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_z_iqr_90d_jerk_v123_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_days_since_high_atr_252d_jerk_v124_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_move_bucket_jerk_v125_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_path_atr_efficiency_30d_jerk_v126_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_dist_high5_atr_short_jerk_v127_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_accel_atr_15d_jerk_v128_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_accel_atr_60d_jerk_v129_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_sigmoid_long_atr_z_jerk_v130_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_days_underwater_atr_120d_jerk_v131_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_squeeze_60d_jerk_v132_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_keltner_BB_tightness_jerk_v133_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_ma_consensus_atr_band_jerk_v134_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_close_pos_252d_atr_jerk_v135_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_avg_close_to_high_atr_30d_jerk_v136_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_avg_close_to_low_atr_30d_jerk_v137_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_median_signed_ret_atr_60d_jerk_v138_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_revstrength_atr_15d_jerk_v139_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_trend_conf_atr_45d_jerk_v140_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_regslope_atr_30d_jerk_v141_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_chand_spread_15d_jerk_v142_signal, ["high","low","close"]),
    (f19an_f19_atr_normalized_price_pct_above_q70_atr_z_jerk_v143_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_tr_expansion_atr_30d_jerk_v144_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_frac_extreme_atr_z_120d_jerk_v145_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_atr_vol_corr_60d_jerk_v146_signal, ["high","low","closeadj","volume"]),
    (f19an_f19_atr_normalized_price_regslope_atr_long_120d_jerk_v147_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_hl_dist_from_atr_60d_jerk_v148_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_var_retatr_30d_jerk_v149_signal, ["high","low","closeadj"]),
    (f19an_f19_atr_normalized_price_max_consec_atr_up_60d_jerk_v150_signal, ["high","low","closeadj"]),
]
f19_atr_normalized_price_jerk_001_150_REGISTRY = dict(_R(f, i) for f, i in _FNS)


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f19_atr_normalized_price_jerk_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
