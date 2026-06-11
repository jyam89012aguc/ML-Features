"""f01_moving_average_systems slope features 001-150 (1st derivative).
Each function computes its own MA-systems base formula inline, then returns
base.diff(k).replace([inf,-inf],nan). k follows the ROC bracket of the
base's primary window:  <=5d:k=5;  6-21d:k=5 or 10;  22-63d:k=10 or 21;
64-200d:k=21 or 63;  >200d:k=63. NaN policy: only the final replace().
"""
from __future__ import annotations
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (kernel constructors). Each slope feature SPELLS its base inline.
# ---------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _hma(s, n):
    half = max(2, n // 2); sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _dema(s, n):
    e1 = _ema(s, n); e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s, n):
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _zlema(s, n):
    lag = max(1, (n - 1) // 2)
    return _ema(s + (s - s.shift(lag)), n)


def _kama(s, n, fast=2, slow=30):
    direction = (s - s.shift(n)).abs()
    volatility = s.diff().abs().rolling(n, min_periods=n).sum()
    er = direction / volatility.replace(0.0, np.nan)
    sc = (er * (2.0 / (fast + 1) - 2.0 / (slow + 1)) + 2.0 / (slow + 1)) ** 2
    out = pd.Series(np.nan, index=s.index, dtype=float)
    prev = np.nan; sv = s.values; scv = sc.values
    for i in range(len(s)):
        if i < n or not np.isfinite(scv[i]) or not np.isfinite(sv[i]):
            continue
        if not np.isfinite(prev):
            prev = sv[i]
        else:
            prev = prev + scv[i] * (sv[i] - prev)
        out.iat[i] = prev
    return out


def _alma(s, n, offset=0.85, sigma=6.0):
    m = offset * (n - 1); sig = n / sigma
    w = np.exp(-((np.arange(n) - m) ** 2) / (2.0 * sig * sig)); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _vwma(s, v, n):
    num = (s * v).rolling(n, min_periods=n).sum()
    den = v.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return num / den


def _streak(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


# ---------------------------------------------------------------------------
# Features 001-075 (slopes of "new" MA-systems base formulas)
# ---------------------------------------------------------------------------

def f01ms_f01_moving_average_systems_logclose_sma_5d_slope_v001_signal(close):
    return np.log(close / _sma(close, 5)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema_sma_diff_10d_slope_v002_signal(close):
    return np.log(_ema(close, 10) / _sma(close, 10)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_sma_20d_slope_v003_signal(close):
    return np.log(close / _sma(close, 20)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sma_40_120_diff_slope_v004_signal(closeadj):
    return np.log(_sma(closeadj, 40) / _sma(closeadj, 120)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_sma_100d_slope_v005_signal(closeadj):
    return np.log(closeadj / _sma(closeadj, 100)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_ema8_slope_v006_signal(close):
    return np.sign(close - _ema(close, 8)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_ema25_slope_v007_signal(closeadj):
    return np.sign(closeadj - _ema(closeadj, 25)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema80_sma80_diff_slope_v008_signal(closeadj):
    return np.log(_ema(closeadj, 80) / _sma(closeadj, 80)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_close_above_sma_freq_15d_slope_v009_signal(close):
    sgn = (close > _sma(close, 15)).astype(float).where(~_sma(close, 15).isna())
    return sgn.rolling(15, min_periods=15).sum().diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_close_above_ema_freq_45d_slope_v010_signal(closeadj):
    sgn = (closeadj > _ema(closeadj, 45)).astype(float).where(~_ema(closeadj, 45).isna())
    return sgn.rolling(45, min_periods=45).sum().diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_hma_30d_slope_v011_signal(closeadj):
    return np.log(closeadj / _hma(closeadj, 30)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope2_v012_signal(close):
    return np.log(_dema(close, 20) / _ema(close, 20)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_tema_50d_slope_v013_signal(closeadj):
    return np.log(closeadj / _tema(closeadj, 50)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_zlema_25d_slope_v014_signal(closeadj):
    return np.log(closeadj / _zlema(closeadj, 25)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_kama40_ema40_slope_v015_signal(closeadj):
    return np.sign(_kama(closeadj, 40) - _ema(closeadj, 40)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_alma_wma_diff_35d_slope_v016_signal(closeadj):
    return np.log(_alma(closeadj, 35) / _wma(closeadj, 35)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_median_ema_diff_55d_slope_v017_signal(closeadj):
    return np.log(closeadj.rolling(55, min_periods=55).median() / _ema(closeadj, 55)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_vwma_ema_diff_30d_slope_v018_signal(closeadj, volume):
    return np.log(_vwma(closeadj, volume, 30) / _ema(closeadj, 30)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sma3_sma8_slope_v019_signal(close):
    return np.log(_sma(close, 3) / _sma(close, 8)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_streak_sma_5_20_50d_slope_v020_signal(close):
    diff = _sma(close, 5) - _sma(close, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(50, min_periods=50).apply(_streak, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_streak_sma_50100_120d_slope_v021_signal(closeadj):
    diff = _sma(closeadj, 50) - _sma(closeadj, 100)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).apply(_streak, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ribbon_order_short_ema_slope_v022_signal(close):
    sn = [_ema(close, k) for k in (8, 12, 16, 20, 24)]
    cnt = pd.Series(0.0, index=close.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema15_ema60_slope_v023_signal(closeadj):
    return np.log(_ema(closeadj, 15) / _ema(closeadj, 60)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema40_ema120_slope_v024_signal(closeadj):
    return np.log(_ema(closeadj, 40) / _ema(closeadj, 120)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_close_above_wma8_30d_slope_v025_signal(close):
    sgn = (close > _wma(close, 8)).astype(float).where(~_wma(close, 8).isna())
    return sgn.rolling(30, min_periods=30).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_hma15_hma45_slope_v026_signal(closeadj):
    return np.log(_hma(closeadj, 15) / _hma(closeadj, 45)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_dema_10_40_slope_v027_signal(closeadj):
    return np.sign(_dema(closeadj, 10) - _dema(closeadj, 40)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kama20_kama80_slope_v028_signal(closeadj):
    return np.log(_kama(closeadj, 20) / _kama(closeadj, 80)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_alma12_alma36_slope_v029_signal(close):
    return np.log(_alma(close, 12) / _alma(close, 36)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_vwma10_vwma40_slope_v030_signal(closeadj, volume):
    return np.log(_vwma(closeadj, volume, 10) / _vwma(closeadj, volume, 40)).diff(10).replace([np.inf, -np.inf], np.nan)


# === sign-based bases (slope produces integer diffs in {-2,-1,0,1,2}) ======

def f01ms_f01_moving_average_systems_sign_close_sma10_slope_v031_signal(close):
    return np.sign(close - _sma(close, 10)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_sma30_slope_v032_signal(closeadj):
    return np.sign(closeadj - _sma(closeadj, 30)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_sma100_slope_v033_signal(closeadj):
    return np.sign(closeadj - _sma(closeadj, 100)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_ema12_ema26_slope_v034_signal(close):
    return np.sign(_ema(close, 12) - _ema(close, 26)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_sma10_sma40_slope_v035_signal(close):
    return np.sign(_sma(close, 10) - _sma(close, 40)).diff(10).replace([np.inf, -np.inf], np.nan)


# === OHLC-MA based slopes ==================================================

def f01ms_f01_moving_average_systems_hl2_close_sma_diff_15d_slope_v036_signal(high, low, close):
    hl2 = 0.5 * (high + low)
    return np.log(_sma(hl2, 15) / _sma(close, 15)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_typ_close_sma_diff_35d_slope_v037_signal(high, low, closeadj):
    typ = (high + low + closeadj) / 3.0
    return np.log(_sma(typ, 35) / _sma(closeadj, 35)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_ohlc4_close_ema_30d_slope_v038_signal(open_, high, low, closeadj):
    ohlc4 = (open_ + high + low + closeadj) / 4.0
    return np.sign(_ema(ohlc4, 30) - _ema(closeadj, 30)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_highsma_lowsma_diff_22d_slope_v039_signal(high, low):
    return np.log(_sma(high, 22) / _sma(low, 22)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_lowsma_closesma_diff_55d_slope_v040_signal(low, closeadj):
    return np.log(_sma(low, 55) / _sma(closeadj, 55)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_low_ma_25d_slope_v041_signal(high, low):
    return np.log(_sma(high, 25) / _sma(low, 25)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_low_ma_range_70d_slope_v042_signal(high, low, closeadj):
    return ((_sma(high, 70) - _sma(low, 70)) / _sma(closeadj, 70)).diff(63).replace([np.inf, -np.inf], np.nan)


# === Ribbon / kernel dispersion slopes =====================================

def f01ms_f01_moving_average_systems_ribbon_kendall_40d_slope_v043_signal(closeadj):
    """slope of Kendall-monotonicity score across SMA(8,16,24,32,40) ribbon.
    Counts how often ribbon is in strict descending order. Base 40 -> k=10."""
    sn = [_sma(closeadj, k) for k in (8, 16, 24, 32, 40)]
    mat = pd.concat(sn, axis=1)
    is_desc = mat.apply(lambda r: float(np.all(np.diff(r.values) < 0)) if np.all(np.isfinite(r.values)) else np.nan, axis=1)
    return is_desc.rolling(20, min_periods=20).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kernel_disp_40d_slope_v044_signal(closeadj):
    """slope of kernel-dispersion across {SMA,EMA,WMA,HMA,ALMA} all at n=40.
    Base 40 -> k=10."""
    n = 40
    a = _sma(closeadj, n); b = _ema(closeadj, n); c = _wma(closeadj, n)
    d = _hma(closeadj, n); e = _alma(closeadj, n)
    mat = pd.concat([a, b, c, d, e], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kernel_agree_50d_slope_v045_signal(closeadj):
    n = 50
    sigs = [(closeadj > _sma(closeadj, n)).astype(float),
            (closeadj > _ema(closeadj, n)).astype(float),
            (closeadj > _wma(closeadj, n)).astype(float),
            (closeadj > _hma(closeadj, n)).astype(float),
            (closeadj > _dema(closeadj, n)).astype(float)]
    mat = pd.concat(sigs, axis=1)
    mask = ~_sma(closeadj, n).isna() & ~_hma(closeadj, n).isna() & ~_dema(closeadj, n).isna()
    return mat.sum(axis=1).where(mask).diff(21).replace([np.inf, -np.inf], np.nan)


# === Rank / fraction slopes ================================================

def f01ms_f01_moving_average_systems_rank_close_sma15_60d_slope_v046_signal(closeadj):
    d = closeadj - _sma(closeadj, 15)
    return d.rolling(60, min_periods=60).rank(pct=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_rank_logclose_ema40_252d_slope_v047_signal(closeadj):
    d = np.log(closeadj / _ema(closeadj, 40))
    return d.rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_fracabove_sma20_30d_slope_v048_signal(closeadj):
    sgn = (closeadj > _sma(closeadj, 20)).astype(float).where(~_sma(closeadj, 20).isna())
    return sgn.rolling(30, min_periods=30).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_fracabove_sma60_120d_slope_v049_signal(closeadj):
    sgn = (closeadj > _sma(closeadj, 60)).astype(float).where(~_sma(closeadj, 60).isna())
    return sgn.rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)


# === Tanh/arctan transform slopes ==========================================

def f01ms_f01_moving_average_systems_tanh_z_ema20_slope_v050_signal(close):
    e = _ema(close, 20)
    sig = (close - e).rolling(20, min_periods=20).std()
    return np.tanh((close - e) / sig.replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_tanh_z_ema100_slope_v051_signal(closeadj):
    """slope of tanh(z of close-EMA(100)) using SHORT 30d window for std.
    Base 100 -> k=63."""
    e = _ema(closeadj, 100)
    sig = (closeadj - e).rolling(30, min_periods=30).std()
    return np.tanh((closeadj - e) / sig.replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


# === MA curvature slopes ===================================================

def f01ms_f01_moving_average_systems_curv_sma25_slope_v052_signal(closeadj):
    m = _sma(closeadj, 25)
    return ((m - 2.0 * m.shift(5) + m.shift(10)) / m).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_curv_sign_sma60_slope_v053_signal(closeadj):
    m = _sma(closeadj, 60)
    return np.sign(m - 2.0 * m.shift(10) + m.shift(20)).diff(21).replace([np.inf, -np.inf], np.nan)


# === Asymmetric MA slopes ==================================================

def f01ms_f01_moving_average_systems_updnratio_20d_slope_v054_signal(close):
    n = 20
    pc = close.shift(1)
    up_mask = (close > pc).astype(float).where(~pc.isna())
    dn_mask = (close < pc).astype(float).where(~pc.isna())
    upm = (close * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    dnm = (close * dn_mask).rolling(n, min_periods=n).sum() / dn_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / dnm).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_upma_sma_diff_50d_slope_v055_signal(closeadj):
    n = 50
    pc = closeadj.shift(1)
    up_mask = (closeadj > pc).astype(float).where(~pc.isna())
    upm = (closeadj * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / _sma(closeadj, n)).diff(21).replace([np.inf, -np.inf], np.nan)


# === VWMA slopes ===========================================================

def f01ms_f01_moving_average_systems_vwma_sma_diff_20d_slope_v056_signal(close, volume):
    return np.log(_vwma(close, volume, 20) / _sma(close, 20)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_vwma_sma_diff_70d_slope_v057_signal(closeadj, volume):
    return np.log(_vwma(closeadj, volume, 70) / _sma(closeadj, 70)).diff(21).replace([np.inf, -np.inf], np.nan)


# === Median / quantile slopes ==============================================

def f01ms_f01_moving_average_systems_median_sma_diff_50d_slope_v058_signal(closeadj):
    return np.log(closeadj.rolling(50, min_periods=50).median() / _sma(closeadj, 50)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_q75_q25_log_80d_slope_v059_signal(closeadj):
    return np.log(closeadj.rolling(80, min_periods=80).quantile(0.75) / closeadj.rolling(80, min_periods=80).quantile(0.25)).diff(63).replace([np.inf, -np.inf], np.nan)


# === Different-kernel diff slopes ==========================================

def f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope_v060_signal(close):
    return np.log(_dema(close, 20) / _ema(close, 20)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_tema_sma_diff_50d_slope_v061_signal(closeadj):
    return np.log(_tema(closeadj, 50) / _sma(closeadj, 50)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kama_ema_diff_40d_slope_v062_signal(closeadj):
    return np.log(_kama(closeadj, 40) / _ema(closeadj, 40)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossmag_hma_2080_slope_v063_signal(closeadj):
    return ((_hma(closeadj, 20) - _hma(closeadj, 80)).abs() / closeadj).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_alma_ema_diff_45d_slope_v064_signal(closeadj):
    return np.log(_alma(closeadj, 45) / _ema(closeadj, 45)).diff(10).replace([np.inf, -np.inf], np.nan)


# === Crossing-count / streak slopes ========================================

def f01ms_f01_moving_average_systems_crossfreq_close_sma15_25d_slope_v065_signal(closeadj):
    diff = closeadj - _sma(closeadj, 15)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(25, min_periods=25).sum().diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_daysince_ema_close_45d_slope_v066_signal(closeadj):
    diff = closeadj - _ema(closeadj, 35)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(80, min_periods=80).apply(_streak, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


# === Ribbon order slopes ===================================================

def f01ms_f01_moving_average_systems_ribbon_order_50d_slope_v067_signal(closeadj):
    sn = [_sma(closeadj, k) for k in (10, 20, 30, 40, 50)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).diff(21).replace([np.inf, -np.inf], np.nan)


# === MA-slope sign slopes ==================================================

def f01ms_f01_moving_average_systems_slope_sign_ema20_slope_v068_signal(close):
    e = _ema(close, 20)
    return np.sign(e - e.shift(5)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_slope_sign_sma80_slope_v069_signal(closeadj):
    m = _sma(closeadj, 80)
    return np.sign(m - m.shift(21)).diff(63).replace([np.inf, -np.inf], np.nan)


# === Geom / harmonic slopes ================================================

def f01ms_f01_moving_average_systems_geom_arith_diff_30d_slope_v070_signal(closeadj):
    n = 30
    geom = np.exp(np.log(closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(geom / _sma(closeadj, n)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_harm_geom_diff_40d_slope_v071_signal(closeadj):
    n = 40
    harm = n / (1.0 / closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).sum()
    geom = np.exp(np.log(closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(harm / geom).diff(10).replace([np.inf, -np.inf], np.nan)


# === Distance stats slopes =================================================

def f01ms_f01_moving_average_systems_dist_std_sma20_slope_v072_signal(closeadj):
    m = _sma(closeadj, 20)
    return (((closeadj - m).rolling(20, min_periods=20).std()) / closeadj).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_autocorr_60d_slope_v073_signal(closeadj):
    s = _sma(closeadj, 20).diff()
    return s.rolling(60, min_periods=60).corr(s.shift(5)).diff(21).replace([np.inf, -np.inf], np.nan)


# === Slope-of-slope (crossmag) =============================================

def f01ms_f01_moving_average_systems_crossmag_sma_2050_slope_v074_signal(closeadj):
    return ((_sma(closeadj, 20) - _sma(closeadj, 50)).abs() / closeadj).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossmag_ema_30100_slope_v075_signal(closeadj):
    return ((_ema(closeadj, 30) - _ema(closeadj, 100)).abs() / closeadj).diff(63).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Features 076-150 (slopes of the base_076_150 features)
# ---------------------------------------------------------------------------

def f01ms_f01_moving_average_systems_sign_close_sma8d_slope_v076_signal(close):
    return np.sign(close - _sma(close, 8)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_sma50d_slope_v077_signal(closeadj):
    return np.sign(closeadj - _sma(closeadj, 50)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_close_sma200d_slope_v078_signal(closeadj):
    return np.sign(closeadj - _sma(closeadj, 200)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_sma5_sma20_slope_v079_signal(close):
    return np.sign(_sma(close, 5) - _sma(close, 20)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_ema20_ema50_slope_v080_signal(closeadj):
    return np.sign(_ema(closeadj, 20) - _ema(closeadj, 50)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_sma50_sma200_slope_v081_signal(closeadj):
    return np.sign(_sma(closeadj, 50) - _sma(closeadj, 200)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_hma30_hma90_slope_v082_signal(closeadj):
    return np.sign(_hma(closeadj, 30) - _hma(closeadj, 90)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_vwma_sma_30d_slope_v083_signal(closeadj, volume):
    return np.sign(_vwma(closeadj, volume, 30) - _sma(closeadj, 30)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_daysince_close_sma20_slope_v084_signal(closeadj):
    diff = closeadj - _sma(closeadj, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).apply(_streak, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_daysince_close_sma50_slope_v085_signal(closeadj):
    diff = closeadj - _sma(closeadj, 50)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).apply(_streak, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_daysince_ema_2050_slope_v086_signal(closeadj):
    diff = _ema(closeadj, 20) - _ema(closeadj, 50)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(150, min_periods=150).apply(_streak, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_daysince_sma_50200_slope_v087_signal(closeadj):
    diff = _sma(closeadj, 50) - _sma(closeadj, 200)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).apply(_streak, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossfreq_close_sma20_slope_v088_signal(closeadj):
    diff = closeadj - _sma(closeadj, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossfreq_ema_1040_slope_v089_signal(closeadj):
    diff = _ema(closeadj, 10) - _ema(closeadj, 40)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).sum().diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossfreq_sma_50200_slope_v090_signal(closeadj):
    diff = _sma(closeadj, 50) - _sma(closeadj, 200)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).sum().diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_fracabove_sma20_60d_slope_v091_signal(closeadj):
    sgn = (closeadj > _sma(closeadj, 20)).astype(float).where(~_sma(closeadj, 20).isna())
    return sgn.rolling(60, min_periods=60).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_fracabove_sma200_120d_slope_v092_signal(closeadj):
    sgn = (closeadj > _sma(closeadj, 200)).astype(float).where(~_sma(closeadj, 200).isna())
    return sgn.rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_fracabove_ema50_30d_slope_v093_signal(closeadj):
    sgn = (closeadj > _ema(closeadj, 50)).astype(float).where(~_ema(closeadj, 50).isna())
    return sgn.rolling(30, min_periods=30).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ribbon_order_short_slope_v094_signal(closeadj):
    sn = [_sma(closeadj, k) for k in (8, 16, 24, 32, 40)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ribbon_order_long_slope_v095_signal(closeadj):
    sn = [_ema(closeadj, k) for k in (20, 40, 60, 80, 100)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_slope_v096_signal(closeadj):
    e = [_ema(closeadj, k) for k in (10, 20, 30, 40, 50)]
    mat = pd.concat(e, axis=1)
    return ((mat.max(axis=1) - mat.min(axis=1)) / mat.mean(axis=1)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ribbon_cv_80d_slope_v097_signal(closeadj):
    e = [_ema(closeadj, k) for k in (15, 30, 45, 60, 80)]
    mat = pd.concat(e, axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kernel_disp_25d_slope_v098_signal(closeadj):
    n = 25
    a = _sma(closeadj, n); b = _ema(closeadj, n); c = _wma(closeadj, n)
    d = _hma(closeadj, n); e = _alma(closeadj, n)
    mat = pd.concat([a, b, c, d, e], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_kernel_agree_30d_slope_v099_signal(closeadj):
    n = 30
    sigs = [(closeadj > _sma(closeadj, n)).astype(float),
            (closeadj > _ema(closeadj, n)).astype(float),
            (closeadj > _wma(closeadj, n)).astype(float),
            (closeadj > _hma(closeadj, n)).astype(float),
            (closeadj > _dema(closeadj, n)).astype(float)]
    mat = pd.concat(sigs, axis=1)
    mask = ~_sma(closeadj, n).isna() & ~_hma(closeadj, n).isna() & ~_dema(closeadj, n).isna()
    return mat.sum(axis=1).where(mask).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_slope_v100_signal(closeadj):
    d = np.log(closeadj / _sma(closeadj, 20))
    return d.rolling(120, min_periods=120).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_slope_v101_signal(closeadj):
    d = np.log(_ema(closeadj, 20) / _ema(closeadj, 50))
    return d.rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_slope_v102_signal(closeadj):
    d = np.log(_sma(closeadj, 50) / _sma(closeadj, 200))
    return d.rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_rank_dist_sma60_30d_slope_v103_signal(closeadj):
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(30, min_periods=30).rank(pct=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_tanh_z_ema30_slope_v104_signal(closeadj):
    n = 30
    e = _ema(closeadj, n)
    sig = (closeadj - e).rolling(n, min_periods=n).std()
    return np.tanh((closeadj - e) / sig.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_arctan_z_sma60_slope_v105_signal(closeadj):
    n = 60
    m = _sma(closeadj, n)
    sig = (closeadj - m).rolling(n, min_periods=n).std()
    return np.arctan((closeadj - m) / sig.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_slope_sign_sma30_slope_v106_signal(closeadj):
    m = _sma(closeadj, 30)
    return np.sign(m - m.shift(10)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_slope_sign_sma100_slope_v107_signal(closeadj):
    m = _sma(closeadj, 100)
    return np.sign(m - m.shift(21)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_slope_diff_2060_slope_v108_signal(closeadj):
    return (_sma(closeadj, 20).pct_change(10) - _sma(closeadj, 60).pct_change(10)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_slope_streak_30d_slope_v109_signal(closeadj):
    m = _sma(closeadj, 30)
    s = np.sign(m - m.shift(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(50, min_periods=50).apply(_streak, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_curv_sma30_slope_v110_signal(closeadj):
    m = _sma(closeadj, 30)
    return ((m - 2.0 * m.shift(5) + m.shift(10)) / m).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_curv_sign_ema80_slope_v111_signal(closeadj):
    e = _ema(closeadj, 80)
    return np.sign(e - 2.0 * e.shift(10) + e.shift(20)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_curv_sign_hma40_slope_v112_signal(closeadj):
    h = _hma(closeadj, 40)
    return np.sign(h - 2.0 * h.shift(10) + h.shift(20)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_ma_low_ma_30d_slope_v113_signal(high, low):
    return np.log(_sma(high, 30) / _sma(low, 30)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_ma_low_ma_60d_slope_v114_signal(high, low):
    return np.log(_ema(high, 60) / _ema(low, 60)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_typ_close_diff_50d_slope_v115_signal(high, low, closeadj):
    typ = (high + low + closeadj) / 3.0
    return np.log(_sma(typ, 50) / _sma(closeadj, 50)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_hl2_close_diff_25d_slope_v116_signal(high, low, closeadj):
    hl2 = 0.5 * (high + low)
    return np.log(_ema(hl2, 25) / _ema(closeadj, 25)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_slope_v117_signal(open_, high, low, close):
    ohlc4 = (open_ + high + low + close) / 4.0
    return np.log(_wma(ohlc4, 30) / _wma(close, 30)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_slope_v118_signal(high, low):
    n = 45
    sp = np.log(_sma(high, n) / _sma(low, n))
    return ((sp - sp.rolling(60, min_periods=60).mean()) / sp.rolling(60, min_periods=60).std()).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_high_ma_close_ma_70d_slope_v119_signal(high, closeadj):
    return np.log(_sma(high, 70) / _sma(closeadj, 70)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_updnratio_25d_slope_v120_signal(close):
    n = 25
    pc = close.shift(1)
    up_mask = (close > pc).astype(float).where(~pc.isna())
    dn_mask = (close < pc).astype(float).where(~pc.isna())
    upm = (close * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    dnm = (close * dn_mask).rolling(n, min_periods=n).sum() / dn_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / dnm).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_upma_sma_diff_60d_slope_v121_signal(closeadj):
    n = 60
    pc = closeadj.shift(1)
    up_mask = (closeadj > pc).astype(float).where(~pc.isna())
    upm = (closeadj * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / _sma(closeadj, n)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_vwma_sma_diff_25d_slope_v122_signal(close, volume):
    return np.log(_vwma(close, volume, 25) / _sma(close, 25)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_vwma_short_long_diff_slope_v123_signal(closeadj, volume):
    return np.log(_vwma(closeadj, volume, 15) / _vwma(closeadj, volume, 60)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_vwma60_sma60_slope_v124_signal(closeadj, volume):
    return np.sign(_vwma(closeadj, volume, 60) - _sma(closeadj, 60)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_median_sma_diff_40d_slope_v125_signal(closeadj):
    return np.log(closeadj.rolling(40, min_periods=40).median() / _sma(closeadj, 40)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_q75_q25_log_60d_slope_v126_signal(closeadj):
    return np.log(closeadj.rolling(60, min_periods=60).quantile(0.75) / closeadj.rolling(60, min_periods=60).quantile(0.25)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_close_above_median_30d_slope_v127_signal(closeadj):
    med = closeadj.rolling(30, min_periods=30).median()
    sgn = (closeadj > med).astype(float).where(~med.isna())
    return sgn.rolling(30, min_periods=30).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_geom_arith_diff_50d_slope_v128_signal(closeadj):
    n = 50
    geom = np.exp(np.log(closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(geom / _sma(closeadj, n)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_harm_geom_diff_25d_slope_v129_signal(close):
    n = 25
    harm = n / (1.0 / close.replace(0.0, np.nan)).rolling(n, min_periods=n).sum()
    geom = np.exp(np.log(close.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(harm / geom).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_corr_close_sma20_30d_slope_v130_signal(closeadj):
    return closeadj.rolling(30, min_periods=30).corr(_sma(closeadj, 20)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_slope_v131_signal(closeadj):
    return _sma(closeadj, 20).rolling(120, min_periods=120).corr(_sma(closeadj, 60)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_slope_v132_signal(closeadj):
    e = _ema(closeadj, 30)
    return e.rolling(60, min_periods=60).corr(e.shift(10)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_dist_std_sma30_slope_v133_signal(closeadj):
    m = _sma(closeadj, 30)
    return ((closeadj - m).rolling(30, min_periods=30).std() / closeadj).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_dist_std_ema60_slope_v134_signal(closeadj):
    e = _ema(closeadj, 60)
    return ((closeadj - e).rolling(60, min_periods=60).std() / closeadj).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_slope_v135_signal(closeadj):
    n = 60
    d = closeadj - _sma(closeadj, 20)
    def _amax(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(int(np.argmax(x))) / float(n - 1)
    return d.rolling(n, min_periods=n).apply(_amax, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_sign_hma_45_sma_45_slope_v136_signal(closeadj):
    return np.sign(_hma(closeadj, 45) - _sma(closeadj, 45)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_alma_sma_diff_80d_slope_v137_signal(closeadj):
    return np.log(_alma(closeadj, 80) / _sma(closeadj, 80)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_wma_sma_diff_30d_slope_v138_signal(closeadj):
    return np.log(_wma(closeadj, 30) / _sma(closeadj, 30)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema_12_26_diff_slope_v139_signal(close):
    return np.log(_ema(close, 12) / _ema(close, 26)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_hma_20_80_diff_slope_v140_signal(closeadj):
    return np.log(_hma(closeadj, 20) / _hma(closeadj, 80)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_wma_10_30_diff_slope_v141_signal(close):
    return np.log(_wma(close, 10) / _wma(close, 30)).diff(10).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_distance_zscore_30d_slope_v142_signal(closeadj):
    n = 30
    d = closeadj - _sma(closeadj, n)
    return ((d - d.rolling(90, min_periods=90).mean()) / d.rolling(90, min_periods=90).std()).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_crossmag_sma_50200_slope_v143_signal(closeadj):
    return ((_sma(closeadj, 50) - _sma(closeadj, 200)).abs() / closeadj).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_dist_argmin_60d_slope_v144_signal(closeadj):
    n = 60
    d = closeadj - _sma(closeadj, n)
    def _amin(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(int(np.argmin(x))) / float(n - 1)
    return d.rolling(n, min_periods=n).apply(_amin, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_sma_8d_slope_v145_signal(close):
    return np.log(close / _sma(close, 8)).diff(5).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_sma_50d_slope_v146_signal(closeadj):
    return np.log(closeadj / _sma(closeadj, 50)).diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_logclose_sma_252d_slope_v147_signal(closeadj):
    return np.log(closeadj / _sma(closeadj, 252)).diff(63).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_skew_60d_slope_v148_signal(closeadj):
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(60, min_periods=60).skew().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ma_kurt_60d_slope_v149_signal(closeadj):
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(60, min_periods=60).kurt().diff(21).replace([np.inf, -np.inf], np.nan)

def f01ms_f01_moving_average_systems_ema_acceleration_30d_slope_v150_signal(closeadj):
    return _ema(closeadj, 30).pct_change(5).diff(5).diff(10).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f01_moving_average_systems_slope_001_150_REGISTRY = {
    "f01ms_f01_moving_average_systems_logclose_sma_5d_slope_v001_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_logclose_sma_5d_slope_v001_signal},
    "f01ms_f01_moving_average_systems_ema_sma_diff_10d_slope_v002_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_ema_sma_diff_10d_slope_v002_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_20d_slope_v003_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_logclose_sma_20d_slope_v003_signal},
    "f01ms_f01_moving_average_systems_sma_40_120_diff_slope_v004_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sma_40_120_diff_slope_v004_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_100d_slope_v005_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_sma_100d_slope_v005_signal},
    "f01ms_f01_moving_average_systems_sign_close_ema8_slope_v006_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_ema8_slope_v006_signal},
    "f01ms_f01_moving_average_systems_sign_close_ema25_slope_v007_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_ema25_slope_v007_signal},
    "f01ms_f01_moving_average_systems_ema80_sma80_diff_slope_v008_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ema80_sma80_diff_slope_v008_signal},
    "f01ms_f01_moving_average_systems_close_above_sma_freq_15d_slope_v009_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_close_above_sma_freq_15d_slope_v009_signal},
    "f01ms_f01_moving_average_systems_close_above_ema_freq_45d_slope_v010_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_close_above_ema_freq_45d_slope_v010_signal},
    "f01ms_f01_moving_average_systems_logclose_hma_30d_slope_v011_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_hma_30d_slope_v011_signal},
    "f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope2_v012_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope2_v012_signal},
    "f01ms_f01_moving_average_systems_logclose_tema_50d_slope_v013_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_tema_50d_slope_v013_signal},
    "f01ms_f01_moving_average_systems_logclose_zlema_25d_slope_v014_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_zlema_25d_slope_v014_signal},
    "f01ms_f01_moving_average_systems_sign_kama40_ema40_slope_v015_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_kama40_ema40_slope_v015_signal},
    "f01ms_f01_moving_average_systems_alma_wma_diff_35d_slope_v016_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_alma_wma_diff_35d_slope_v016_signal},
    "f01ms_f01_moving_average_systems_median_ema_diff_55d_slope_v017_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_median_ema_diff_55d_slope_v017_signal},
    "f01ms_f01_moving_average_systems_vwma_ema_diff_30d_slope_v018_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_vwma_ema_diff_30d_slope_v018_signal},
    "f01ms_f01_moving_average_systems_sma3_sma8_slope_v019_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sma3_sma8_slope_v019_signal},
    "f01ms_f01_moving_average_systems_streak_sma_5_20_50d_slope_v020_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_streak_sma_5_20_50d_slope_v020_signal},
    "f01ms_f01_moving_average_systems_streak_sma_50100_120d_slope_v021_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_streak_sma_50100_120d_slope_v021_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_short_ema_slope_v022_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_ribbon_order_short_ema_slope_v022_signal},
    "f01ms_f01_moving_average_systems_ema15_ema60_slope_v023_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ema15_ema60_slope_v023_signal},
    "f01ms_f01_moving_average_systems_ema40_ema120_slope_v024_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ema40_ema120_slope_v024_signal},
    "f01ms_f01_moving_average_systems_close_above_wma8_30d_slope_v025_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_close_above_wma8_30d_slope_v025_signal},
    "f01ms_f01_moving_average_systems_hma15_hma45_slope_v026_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hma15_hma45_slope_v026_signal},
    "f01ms_f01_moving_average_systems_sign_dema_10_40_slope_v027_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_dema_10_40_slope_v027_signal},
    "f01ms_f01_moving_average_systems_kama20_kama80_slope_v028_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kama20_kama80_slope_v028_signal},
    "f01ms_f01_moving_average_systems_alma12_alma36_slope_v029_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_alma12_alma36_slope_v029_signal},
    "f01ms_f01_moving_average_systems_vwma10_vwma40_slope_v030_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_vwma10_vwma40_slope_v030_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma10_slope_v031_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_sma10_slope_v031_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma30_slope_v032_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma30_slope_v032_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma100_slope_v033_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma100_slope_v033_signal},
    "f01ms_f01_moving_average_systems_sign_ema12_ema26_slope_v034_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_ema12_ema26_slope_v034_signal},
    "f01ms_f01_moving_average_systems_sign_sma10_sma40_slope_v035_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_sma10_sma40_slope_v035_signal},
    "f01ms_f01_moving_average_systems_hl2_close_sma_diff_15d_slope_v036_signal": {"inputs": ["high", "low", "close"], "func": f01ms_f01_moving_average_systems_hl2_close_sma_diff_15d_slope_v036_signal},
    "f01ms_f01_moving_average_systems_typ_close_sma_diff_35d_slope_v037_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_typ_close_sma_diff_35d_slope_v037_signal},
    "f01ms_f01_moving_average_systems_sign_ohlc4_close_ema_30d_slope_v038_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_sign_ohlc4_close_ema_30d_slope_v038_signal},
    "f01ms_f01_moving_average_systems_highsma_lowsma_diff_22d_slope_v039_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_highsma_lowsma_diff_22d_slope_v039_signal},
    "f01ms_f01_moving_average_systems_lowsma_closesma_diff_55d_slope_v040_signal": {"inputs": ["low", "closeadj"], "func": f01ms_f01_moving_average_systems_lowsma_closesma_diff_55d_slope_v040_signal},
    "f01ms_f01_moving_average_systems_high_low_ma_25d_slope_v041_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_low_ma_25d_slope_v041_signal},
    "f01ms_f01_moving_average_systems_high_low_ma_range_70d_slope_v042_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_high_low_ma_range_70d_slope_v042_signal},
    "f01ms_f01_moving_average_systems_ribbon_kendall_40d_slope_v043_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_kendall_40d_slope_v043_signal},
    "f01ms_f01_moving_average_systems_kernel_disp_40d_slope_v044_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_disp_40d_slope_v044_signal},
    "f01ms_f01_moving_average_systems_kernel_agree_50d_slope_v045_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_agree_50d_slope_v045_signal},
    "f01ms_f01_moving_average_systems_rank_close_sma15_60d_slope_v046_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_close_sma15_60d_slope_v046_signal},
    "f01ms_f01_moving_average_systems_rank_logclose_ema40_252d_slope_v047_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_logclose_ema40_252d_slope_v047_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma20_30d_slope_v048_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma20_30d_slope_v048_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma60_120d_slope_v049_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma60_120d_slope_v049_signal},
    "f01ms_f01_moving_average_systems_tanh_z_ema20_slope_v050_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_tanh_z_ema20_slope_v050_signal},
    "f01ms_f01_moving_average_systems_tanh_z_ema100_slope_v051_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_tanh_z_ema100_slope_v051_signal},
    "f01ms_f01_moving_average_systems_curv_sma25_slope_v052_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sma25_slope_v052_signal},
    "f01ms_f01_moving_average_systems_curv_sign_sma60_slope_v053_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sign_sma60_slope_v053_signal},
    "f01ms_f01_moving_average_systems_updnratio_20d_slope_v054_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_updnratio_20d_slope_v054_signal},
    "f01ms_f01_moving_average_systems_upma_sma_diff_50d_slope_v055_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_upma_sma_diff_50d_slope_v055_signal},
    "f01ms_f01_moving_average_systems_vwma_sma_diff_20d_slope_v056_signal": {"inputs": ["close", "volume"], "func": f01ms_f01_moving_average_systems_vwma_sma_diff_20d_slope_v056_signal},
    "f01ms_f01_moving_average_systems_vwma_sma_diff_70d_slope_v057_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_vwma_sma_diff_70d_slope_v057_signal},
    "f01ms_f01_moving_average_systems_median_sma_diff_50d_slope_v058_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_median_sma_diff_50d_slope_v058_signal},
    "f01ms_f01_moving_average_systems_q75_q25_log_80d_slope_v059_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_q75_q25_log_80d_slope_v059_signal},
    "f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope_v060_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_dema_ema_diff_20d_slope_v060_signal},
    "f01ms_f01_moving_average_systems_tema_sma_diff_50d_slope_v061_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_tema_sma_diff_50d_slope_v061_signal},
    "f01ms_f01_moving_average_systems_kama_ema_diff_40d_slope_v062_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kama_ema_diff_40d_slope_v062_signal},
    "f01ms_f01_moving_average_systems_crossmag_hma_2080_slope_v063_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossmag_hma_2080_slope_v063_signal},
    "f01ms_f01_moving_average_systems_alma_ema_diff_45d_slope_v064_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_alma_ema_diff_45d_slope_v064_signal},
    "f01ms_f01_moving_average_systems_crossfreq_close_sma15_25d_slope_v065_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_close_sma15_25d_slope_v065_signal},
    "f01ms_f01_moving_average_systems_daysince_ema_close_45d_slope_v066_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_ema_close_45d_slope_v066_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_50d_slope_v067_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_order_50d_slope_v067_signal},
    "f01ms_f01_moving_average_systems_slope_sign_ema20_slope_v068_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_slope_sign_ema20_slope_v068_signal},
    "f01ms_f01_moving_average_systems_slope_sign_sma80_slope_v069_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_sign_sma80_slope_v069_signal},
    "f01ms_f01_moving_average_systems_geom_arith_diff_30d_slope_v070_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_geom_arith_diff_30d_slope_v070_signal},
    "f01ms_f01_moving_average_systems_harm_geom_diff_40d_slope_v071_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_harm_geom_diff_40d_slope_v071_signal},
    "f01ms_f01_moving_average_systems_dist_std_sma20_slope_v072_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dist_std_sma20_slope_v072_signal},
    "f01ms_f01_moving_average_systems_ma_autocorr_60d_slope_v073_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_autocorr_60d_slope_v073_signal},
    "f01ms_f01_moving_average_systems_crossmag_sma_2050_slope_v074_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossmag_sma_2050_slope_v074_signal},
    "f01ms_f01_moving_average_systems_crossmag_ema_30100_slope_v075_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossmag_ema_30100_slope_v075_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma8d_slope_v076_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_sma8d_slope_v076_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma50d_slope_v077_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma50d_slope_v077_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma200d_slope_v078_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma200d_slope_v078_signal},
    "f01ms_f01_moving_average_systems_sign_sma5_sma20_slope_v079_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_sma5_sma20_slope_v079_signal},
    "f01ms_f01_moving_average_systems_sign_ema20_ema50_slope_v080_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_ema20_ema50_slope_v080_signal},
    "f01ms_f01_moving_average_systems_sign_sma50_sma200_slope_v081_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_sma50_sma200_slope_v081_signal},
    "f01ms_f01_moving_average_systems_sign_hma30_hma90_slope_v082_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_hma30_hma90_slope_v082_signal},
    "f01ms_f01_moving_average_systems_sign_vwma_sma_30d_slope_v083_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_sign_vwma_sma_30d_slope_v083_signal},
    "f01ms_f01_moving_average_systems_daysince_close_sma20_slope_v084_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_close_sma20_slope_v084_signal},
    "f01ms_f01_moving_average_systems_daysince_close_sma50_slope_v085_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_close_sma50_slope_v085_signal},
    "f01ms_f01_moving_average_systems_daysince_ema_2050_slope_v086_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_ema_2050_slope_v086_signal},
    "f01ms_f01_moving_average_systems_daysince_sma_50200_slope_v087_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_sma_50200_slope_v087_signal},
    "f01ms_f01_moving_average_systems_crossfreq_close_sma20_slope_v088_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_close_sma20_slope_v088_signal},
    "f01ms_f01_moving_average_systems_crossfreq_ema_1040_slope_v089_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_ema_1040_slope_v089_signal},
    "f01ms_f01_moving_average_systems_crossfreq_sma_50200_slope_v090_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_sma_50200_slope_v090_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma20_60d_slope_v091_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma20_60d_slope_v091_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma200_120d_slope_v092_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma200_120d_slope_v092_signal},
    "f01ms_f01_moving_average_systems_fracabove_ema50_30d_slope_v093_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_ema50_30d_slope_v093_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_short_slope_v094_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_order_short_slope_v094_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_long_slope_v095_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_order_long_slope_v095_signal},
    "f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_slope_v096_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_slope_v096_signal},
    "f01ms_f01_moving_average_systems_ribbon_cv_80d_slope_v097_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_cv_80d_slope_v097_signal},
    "f01ms_f01_moving_average_systems_kernel_disp_25d_slope_v098_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_disp_25d_slope_v098_signal},
    "f01ms_f01_moving_average_systems_kernel_agree_30d_slope_v099_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_agree_30d_slope_v099_signal},
    "f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_slope_v100_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_slope_v100_signal},
    "f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_slope_v101_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_slope_v101_signal},
    "f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_slope_v102_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_slope_v102_signal},
    "f01ms_f01_moving_average_systems_rank_dist_sma60_30d_slope_v103_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_dist_sma60_30d_slope_v103_signal},
    "f01ms_f01_moving_average_systems_tanh_z_ema30_slope_v104_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_tanh_z_ema30_slope_v104_signal},
    "f01ms_f01_moving_average_systems_arctan_z_sma60_slope_v105_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_arctan_z_sma60_slope_v105_signal},
    "f01ms_f01_moving_average_systems_slope_sign_sma30_slope_v106_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_sign_sma30_slope_v106_signal},
    "f01ms_f01_moving_average_systems_slope_sign_sma100_slope_v107_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_sign_sma100_slope_v107_signal},
    "f01ms_f01_moving_average_systems_slope_diff_2060_slope_v108_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_diff_2060_slope_v108_signal},
    "f01ms_f01_moving_average_systems_ma_slope_streak_30d_slope_v109_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_slope_streak_30d_slope_v109_signal},
    "f01ms_f01_moving_average_systems_curv_sma30_slope_v110_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sma30_slope_v110_signal},
    "f01ms_f01_moving_average_systems_curv_sign_ema80_slope_v111_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sign_ema80_slope_v111_signal},
    "f01ms_f01_moving_average_systems_curv_sign_hma40_slope_v112_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sign_hma40_slope_v112_signal},
    "f01ms_f01_moving_average_systems_high_ma_low_ma_30d_slope_v113_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_ma_low_ma_30d_slope_v113_signal},
    "f01ms_f01_moving_average_systems_high_ma_low_ma_60d_slope_v114_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_ma_low_ma_60d_slope_v114_signal},
    "f01ms_f01_moving_average_systems_typ_close_diff_50d_slope_v115_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_typ_close_diff_50d_slope_v115_signal},
    "f01ms_f01_moving_average_systems_hl2_close_diff_25d_slope_v116_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_hl2_close_diff_25d_slope_v116_signal},
    "f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_slope_v117_signal": {"inputs": ["open", "high", "low", "close"], "func": f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_slope_v117_signal},
    "f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_slope_v118_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_slope_v118_signal},
    "f01ms_f01_moving_average_systems_high_ma_close_ma_70d_slope_v119_signal": {"inputs": ["high", "closeadj"], "func": f01ms_f01_moving_average_systems_high_ma_close_ma_70d_slope_v119_signal},
    "f01ms_f01_moving_average_systems_updnratio_25d_slope_v120_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_updnratio_25d_slope_v120_signal},
    "f01ms_f01_moving_average_systems_upma_sma_diff_60d_slope_v121_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_upma_sma_diff_60d_slope_v121_signal},
    "f01ms_f01_moving_average_systems_vwma_sma_diff_25d_slope_v122_signal": {"inputs": ["close", "volume"], "func": f01ms_f01_moving_average_systems_vwma_sma_diff_25d_slope_v122_signal},
    "f01ms_f01_moving_average_systems_vwma_short_long_diff_slope_v123_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_vwma_short_long_diff_slope_v123_signal},
    "f01ms_f01_moving_average_systems_sign_vwma60_sma60_slope_v124_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_sign_vwma60_sma60_slope_v124_signal},
    "f01ms_f01_moving_average_systems_median_sma_diff_40d_slope_v125_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_median_sma_diff_40d_slope_v125_signal},
    "f01ms_f01_moving_average_systems_q75_q25_log_60d_slope_v126_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_q75_q25_log_60d_slope_v126_signal},
    "f01ms_f01_moving_average_systems_close_above_median_30d_slope_v127_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_close_above_median_30d_slope_v127_signal},
    "f01ms_f01_moving_average_systems_geom_arith_diff_50d_slope_v128_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_geom_arith_diff_50d_slope_v128_signal},
    "f01ms_f01_moving_average_systems_harm_geom_diff_25d_slope_v129_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_harm_geom_diff_25d_slope_v129_signal},
    "f01ms_f01_moving_average_systems_corr_close_sma20_30d_slope_v130_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_close_sma20_30d_slope_v130_signal},
    "f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_slope_v131_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_slope_v131_signal},
    "f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_slope_v132_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_slope_v132_signal},
    "f01ms_f01_moving_average_systems_dist_std_sma30_slope_v133_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dist_std_sma30_slope_v133_signal},
    "f01ms_f01_moving_average_systems_dist_std_ema60_slope_v134_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dist_std_ema60_slope_v134_signal},
    "f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_slope_v135_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_slope_v135_signal},
    "f01ms_f01_moving_average_systems_sign_hma_45_sma_45_slope_v136_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_hma_45_sma_45_slope_v136_signal},
    "f01ms_f01_moving_average_systems_alma_sma_diff_80d_slope_v137_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_alma_sma_diff_80d_slope_v137_signal},
    "f01ms_f01_moving_average_systems_wma_sma_diff_30d_slope_v138_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_wma_sma_diff_30d_slope_v138_signal},
    "f01ms_f01_moving_average_systems_ema_12_26_diff_slope_v139_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_ema_12_26_diff_slope_v139_signal},
    "f01ms_f01_moving_average_systems_hma_20_80_diff_slope_v140_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hma_20_80_diff_slope_v140_signal},
    "f01ms_f01_moving_average_systems_wma_10_30_diff_slope_v141_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_wma_10_30_diff_slope_v141_signal},
    "f01ms_f01_moving_average_systems_ma_distance_zscore_30d_slope_v142_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_distance_zscore_30d_slope_v142_signal},
    "f01ms_f01_moving_average_systems_crossmag_sma_50200_slope_v143_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossmag_sma_50200_slope_v143_signal},
    "f01ms_f01_moving_average_systems_ma_dist_argmin_60d_slope_v144_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_dist_argmin_60d_slope_v144_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_8d_slope_v145_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_logclose_sma_8d_slope_v145_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_50d_slope_v146_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_sma_50d_slope_v146_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_252d_slope_v147_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_sma_252d_slope_v147_signal},
    "f01ms_f01_moving_average_systems_ma_skew_60d_slope_v148_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_skew_60d_slope_v148_signal},
    "f01ms_f01_moving_average_systems_ma_kurt_60d_slope_v149_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_kurt_60d_slope_v149_signal},
    "f01ms_f01_moving_average_systems_ema_acceleration_30d_slope_v150_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ema_acceleration_30d_slope_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


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
    for name, entry in f01_moving_average_systems_slope_001_150_REGISTRY.items():
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
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
