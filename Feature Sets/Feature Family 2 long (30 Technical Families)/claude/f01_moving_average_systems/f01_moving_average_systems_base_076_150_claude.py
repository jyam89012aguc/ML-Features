"""f01_moving_average_systems base features 076-150.

Domain: moving-average SYSTEMS — kernels (SMA/EMA/WMA/HMA/DEMA/TEMA/ZLEMA
/KAMA/T3/ALMA/McGinley/Wilder/median/quantile/trimmed/winsorized/geometric
/harmonic), OHLC-flavored MAs (HL2/HLC3/OHLC4/typical), asymmetric/up-down
MAs, volume-weighted MAs. Features lean heavily on discrete/count/rank
classes (signs, streaks, crossing-counts, ribbon-ordering, rank transforms,
percentiles) to decorrelate from continuous MA-distance lookalikes.

Each function inlines its formula. No fillna(0). Windows > 21d use
closeadj. NaN policy: replace([inf,-inf], nan) at the final return only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float)
    w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _hma(s: pd.Series, n: int) -> pd.Series:
    half = max(2, n // 2)
    sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _dema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _alma(s: pd.Series, n: int, offset: float = 0.85, sigma: float = 6.0) -> pd.Series:
    m = offset * (n - 1)
    sig = n / sigma
    w = np.exp(-((np.arange(n) - m) ** 2) / (2.0 * sig * sig))
    w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _streak(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def _vwma(s: pd.Series, v: pd.Series, n: int) -> pd.Series:
    num = (s * v).rolling(n, min_periods=n).sum()
    den = v.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return num / den


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === SIGN family (8) =======================================================


def f01ms_f01_moving_average_systems_sign_close_sma8d_base_v076_signal(close):
    """sign(close - SMA(8)). Very short-term trend filter."""
    return np.sign(close - _sma(close, 8)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_close_sma50d_base_v077_signal(closeadj):
    """sign(close - SMA(50)). Mid-term trend filter."""
    return np.sign(closeadj - _sma(closeadj, 50)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_close_sma200d_base_v078_signal(closeadj):
    """sign(close - SMA(200)). Classic 200d trend filter."""
    return np.sign(closeadj - _sma(closeadj, 200)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_sma5_sma20_base_v079_signal(close):
    """sign(SMA(5) - SMA(20)). Fast SMA crossover sign."""
    return np.sign(_sma(close, 5) - _sma(close, 20)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_ema20_ema50_base_v080_signal(closeadj):
    """sign(EMA(20) - EMA(50)). Short-vs-long EMA crossover sign."""
    return np.sign(_ema(closeadj, 20) - _ema(closeadj, 50)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_sma50_sma200_base_v081_signal(closeadj):
    """sign(SMA(50) - SMA(200)). Golden/death-cross sign."""
    return np.sign(_sma(closeadj, 50) - _sma(closeadj, 200)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_hma30_hma90_base_v082_signal(closeadj):
    """sign(HMA(30) - HMA(90)). Hull-MA fast/slow crossover sign."""
    return np.sign(_hma(closeadj, 30) - _hma(closeadj, 90)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_vwma_sma_30d_base_v083_signal(closeadj, volume):
    """sign(VWMA(30) - SMA(30)). Volume vs equal-weighted MA divergence sign."""
    return np.sign(_vwma(closeadj, volume, 30) - _sma(closeadj, 30)).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE-CROSS streak counts (4) ====================================


def f01ms_f01_moving_average_systems_daysince_close_sma20_30d_base_v084_signal(closeadj):
    """Bars since last (close vs SMA(20)) sign-change, capped 30."""
    diff = closeadj - _sma(closeadj, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_daysince_close_sma50_100d_base_v085_signal(closeadj):
    """Bars since last (close vs SMA(50)) sign-change, capped 100."""
    diff = closeadj - _sma(closeadj, 50)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_daysince_ema_2050_150d_base_v086_signal(closeadj):
    """Bars since last (EMA(20)-EMA(50)) sign-change, capped 150."""
    diff = _ema(closeadj, 20) - _ema(closeadj, 50)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(150, min_periods=150).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_daysince_sma_50200_252d_base_v087_signal(closeadj):
    """Bars since last (SMA(50)-SMA(200)) sign-change, capped 252."""
    diff = _sma(closeadj, 50) - _sma(closeadj, 200)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === CROSSING-FREQUENCY counts (3) =========================================


def f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_base_v088_signal(closeadj):
    """Count of (close vs SMA(20)) sign-changes in last 30 bars."""
    diff = closeadj - _sma(closeadj, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_base_v089_signal(closeadj):
    """Count of (EMA(10) vs EMA(40)) sign-changes in last 120 bars."""
    diff = _ema(closeadj, 10) - _ema(closeadj, 40)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_base_v090_signal(closeadj):
    """Count of (SMA(50) vs SMA(200)) sign-changes in last 252 bars."""
    diff = _sma(closeadj, 50) - _sma(closeadj, 200)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).sum().replace([np.inf, -np.inf], np.nan)


# === FRACTION-ABOVE-MA (rolling mean of bull-bar indicator, 3) =============


def f01ms_f01_moving_average_systems_fracabove_sma20_60d_base_v091_signal(closeadj):
    """Fraction of last 60 bars where close > SMA(20)."""
    diff = closeadj - _sma(closeadj, 20)
    sgn = (diff > 0).astype(float).where(~diff.isna())
    return sgn.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_fracabove_sma200_120d_base_v092_signal(closeadj):
    """Fraction of last 120 bars where close > SMA(200)."""
    diff = closeadj - _sma(closeadj, 200)
    sgn = (diff > 0).astype(float).where(~diff.isna())
    return sgn.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_fracabove_ema50_30d_base_v093_signal(closeadj):
    """Fraction of last 30 bars where close > EMA(50). Mid-MA regime."""
    diff = closeadj - _ema(closeadj, 50)
    sgn = (diff > 0).astype(float).where(~diff.isna())
    return sgn.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === RIBBON / KERNEL DISPERSION ============================================


def f01ms_f01_moving_average_systems_ribbon_order_short_base_v094_signal(closeadj):
    """Count of properly-ordered (short>long) pairs in SMA ribbon n=8,16,24,32,40.
    Range 0-10."""
    sn = [_sma(closeadj, k) for k in (8, 16, 24, 32, 40)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ribbon_order_long_base_v095_signal(closeadj):
    """Ribbon order count over EMA(20,40,60,80,100). Long-horizon ordering."""
    sn = [_ema(closeadj, k) for k in (20, 40, 60, 80, 100)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_base_v096_signal(closeadj):
    """(max-min)/mean of EMA ribbon n=10,20,30,40,50. Normalized fan."""
    e = [_ema(closeadj, k) for k in (10, 20, 30, 40, 50)]
    mat = pd.concat(e, axis=1)
    return ((mat.max(axis=1) - mat.min(axis=1)) / mat.mean(axis=1)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ribbon_cv_80d_base_v097_signal(closeadj):
    """std/mean of EMA ribbon n=15,30,45,60,80. CV-fan."""
    e = [_ema(closeadj, k) for k in (15, 30, 45, 60, 80)]
    mat = pd.concat(e, axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_kernel_disp_25d_base_v098_signal(closeadj):
    """std/mean across {SMA, EMA, WMA, HMA, ALMA} all at n=25."""
    n = 25
    a = _sma(closeadj, n); b = _ema(closeadj, n); c = _wma(closeadj, n)
    d = _hma(closeadj, n); e = _alma(closeadj, n)
    mat = pd.concat([a, b, c, d, e], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_kernel_agree_30d_base_v099_signal(closeadj):
    """Count of MAs (SMA, EMA, WMA, HMA, DEMA at n=30) above which close trades.
    Range 0-5. Discrete kernel agreement."""
    n = 30
    sigs = [(closeadj > _sma(closeadj, n)).astype(float),
            (closeadj > _ema(closeadj, n)).astype(float),
            (closeadj > _wma(closeadj, n)).astype(float),
            (closeadj > _hma(closeadj, n)).astype(float),
            (closeadj > _dema(closeadj, n)).astype(float)]
    mat = pd.concat(sigs, axis=1)
    mask = ~_sma(closeadj, n).isna() & ~_hma(closeadj, n).isna() & ~_dema(closeadj, n).isna()
    return mat.sum(axis=1).where(mask).replace([np.inf, -np.inf], np.nan)


# === RANK transforms (4) ===================================================




def f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_base_v101_signal(closeadj):
    """252d percentile rank of log(EMA(20)/EMA(50))."""
    d = np.log(_ema(closeadj, 20) / _ema(closeadj, 50))
    return d.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_base_v102_signal(closeadj):
    """252d rank of log(SMA(50)/SMA(200)). Long cross-rank regime."""
    d = np.log(_sma(closeadj, 50) / _sma(closeadj, 200))
    return d.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_rank_dist_sma60_30d_base_v103_signal(closeadj):
    """30d percentile rank of (close - SMA(60)). Local distance rank."""
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(30, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === TANH / ARCTAN bounded (2) =============================================


def f01ms_f01_moving_average_systems_tanh_z_ema30_base_v104_signal(closeadj):
    """tanh of z-scored (close - EMA(30)) / rolling-std."""
    n = 30
    e = _ema(closeadj, n)
    sig = (closeadj - e).rolling(n, min_periods=n).std()
    return np.tanh((closeadj - e) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_arctan_z_sma60_base_v105_signal(closeadj):
    """arctan of z-scored (close - SMA(60)) / rolling-std."""
    n = 60
    m = _sma(closeadj, n)
    sig = (closeadj - m).rolling(n, min_periods=n).std()
    return np.arctan((closeadj - m) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MA SLOPE discrete + diff (4) ==========================================


def f01ms_f01_moving_average_systems_slope_sign_sma30_base_v106_signal(closeadj):
    """sign(SMA(30) - SMA(30).shift(10)). Discrete mid-MA slope direction."""
    m = _sma(closeadj, 30)
    return np.sign(m - m.shift(10)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_slope_sign_sma100_base_v107_signal(closeadj):
    """sign(SMA(100) - SMA(100).shift(21)). Discrete long MA-slope direction."""
    m = _sma(closeadj, 100)
    return np.sign(m - m.shift(21)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_slope_diff_2060_base_v108_signal(closeadj):
    """SMA(20).pct_change(10) - SMA(60).pct_change(10). Slope spread."""
    return (_sma(closeadj, 20).pct_change(10) - _sma(closeadj, 60).pct_change(10)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_slope_streak_30d_base_v109_signal(closeadj):
    """Bars-since-last-sign-change of (SMA(30) slope sign), capped 50.
    Persistence of MA-slope direction."""
    m = _sma(closeadj, 30)
    s = np.sign(m - m.shift(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(50, min_periods=50).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === MA CURVATURE (3) ======================================================


def f01ms_f01_moving_average_systems_curv_sma30_base_v110_signal(closeadj):
    """(SMA(30) - 2*SMA(30).shift(5) + SMA(30).shift(10)) / SMA(30)."""
    m = _sma(closeadj, 30)
    return ((m - 2.0 * m.shift(5) + m.shift(10)) / m).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_curv_ema80_base_v111_signal(closeadj):
    """Long-MA 2nd-diff normalized: 2nd-diff of EMA(80) / EMA(80)."""
    e = _ema(closeadj, 80)
    return ((e - 2.0 * e.shift(10) + e.shift(20)) / e).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_curv_sign_hma40_base_v112_signal(closeadj):
    """sign(2nd-diff of HMA(40)). Discrete Hull-MA concavity sign."""
    h = _hma(closeadj, 40)
    return np.sign(h - 2.0 * h.shift(10) + h.shift(20)).replace([np.inf, -np.inf], np.nan)


# === OHLC-flavored MAs (uses high/low/open) (7) ============================


def f01ms_f01_moving_average_systems_high_ma_low_ma_30d_base_v113_signal(high, low):
    """log(SMA(high,30) / SMA(low,30)). High-low MA log-spread."""
    return np.log(_sma(high, 30) / _sma(low, 30)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_high_ma_low_ma_60d_base_v114_signal(high, low):
    """log(EMA(high,60) / EMA(low,60)). Long high-low EMA spread."""
    return np.log(_ema(high, 60) / _ema(low, 60)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_typ_close_diff_50d_base_v115_signal(high, low, closeadj):
    """log(SMA(typical,50) / SMA(closeadj,50))."""
    typ = (high + low + closeadj) / 3.0
    return np.log(_sma(typ, 50) / _sma(closeadj, 50)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_hl2_close_diff_25d_base_v116_signal(high, low, closeadj):
    """log(EMA(HL2,25) / EMA(closeadj,25))."""
    hl2 = 0.5 * (high + low)
    return np.log(_ema(hl2, 25) / _ema(closeadj, 25)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_base_v117_signal(open_, high, low, close):
    """log(WMA(OHLC4,30) / WMA(close,30))."""
    ohlc4 = (open_ + high + low + close) / 4.0
    return np.log(_wma(ohlc4, 30) / _wma(close, 30)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_base_v118_signal(high, low):
    """z-score of log(SMA(high,45)/SMA(low,45)). Standardized high-low MA spread.
    Decorrelated from raw log-spread by per-window z-normalization."""
    n = 45
    sp = np.log(_sma(high, n) / _sma(low, n))
    return ((sp - sp.rolling(60, min_periods=60).mean()) / sp.rolling(60, min_periods=60).std()).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_high_ma_close_ma_70d_base_v119_signal(high, closeadj):
    """log(SMA(high,70) / SMA(closeadj,70)). Long high-MA vs close-MA spread."""
    return np.log(_sma(high, 70) / _sma(closeadj, 70)).replace([np.inf, -np.inf], np.nan)


# === ASYMMETRIC up/down MAs (2) ============================================


def f01ms_f01_moving_average_systems_updnratio_25d_base_v120_signal(close):
    """log(up-only-mean / down-only-mean) at N=25."""
    n = 25
    pc = close.shift(1)
    up_mask = (close > pc).astype(float).where(~pc.isna())
    dn_mask = (close < pc).astype(float).where(~pc.isna())
    upm = (close * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    dnm = (close * dn_mask).rolling(n, min_periods=n).sum() / dn_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / dnm).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_upma_sma_diff_60d_base_v121_signal(closeadj):
    """log(up-only-mean(60) / SMA(60))."""
    n = 60
    pc = closeadj.shift(1)
    up_mask = (closeadj > pc).astype(float).where(~pc.isna())
    upm = (closeadj * up_mask).rolling(n, min_periods=n).sum() / up_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(upm / _sma(closeadj, n)).replace([np.inf, -np.inf], np.nan)


# === VWMA family (3) =======================================================


def f01ms_f01_moving_average_systems_vwma_sma_diff_25d_base_v122_signal(close, volume):
    """log(VWMA(25) / SMA(25))."""
    return np.log(_vwma(close, volume, 25) / _sma(close, 25)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_vwma_short_long_diff_base_v123_signal(closeadj, volume):
    """log(VWMA(15) / VWMA(60)). Short/long VWMA cross."""
    return np.log(_vwma(closeadj, volume, 15) / _vwma(closeadj, volume, 60)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_vwma60_sma60_base_v124_signal(closeadj, volume):
    """sign(VWMA(60) - SMA(60)). Volume vs equal-weighted MA sign at 60d."""
    return np.sign(_vwma(closeadj, volume, 60) - _sma(closeadj, 60)).replace([np.inf, -np.inf], np.nan)


# === MEDIAN / QUANTILE MAs (3) =============================================


def f01ms_f01_moving_average_systems_median_sma_diff_40d_base_v125_signal(closeadj):
    """log(rolling-median(40) / SMA(40))."""
    return np.log(closeadj.rolling(40, min_periods=40).median() / _sma(closeadj, 40)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_q75_q25_log_60d_base_v126_signal(closeadj):
    """log(rolling-Q75(60) / Q25(60)). Interquartile log-spread."""
    return np.log(closeadj.rolling(60, min_periods=60).quantile(0.75) / closeadj.rolling(60, min_periods=60).quantile(0.25)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_close_above_median_30d_base_v127_signal(closeadj):
    """Fraction of last 30 bars where close > rolling-median(30) — robust trend."""
    med = closeadj.rolling(30, min_periods=30).median()
    sgn = (closeadj > med).astype(float).where(~med.isna())
    return sgn.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === GEOMETRIC / HARMONIC means (2) ========================================


def f01ms_f01_moving_average_systems_geom_arith_diff_50d_base_v128_signal(closeadj):
    """log(geomean(50) / SMA(50)). AM-GM inequality measure."""
    n = 50
    geom = np.exp(np.log(closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(geom / _sma(closeadj, n)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_harm_geom_diff_25d_base_v129_signal(close):
    """log(harm-mean(25) / geomean(25)). HM-GM inequality measure."""
    n = 25
    harm = n / (1.0 / close.replace(0.0, np.nan)).rolling(n, min_periods=n).sum()
    geom = np.exp(np.log(close.replace(0.0, np.nan)).rolling(n, min_periods=n).mean())
    return np.log(harm / geom).replace([np.inf, -np.inf], np.nan)


# === ROLLING corr(close, MA-shifted) (3) ===================================


def f01ms_f01_moving_average_systems_corr_close_sma20_30d_base_v130_signal(closeadj):
    """30d rolling Pearson correlation of close vs SMA(20). Tracking quality."""
    return closeadj.rolling(30, min_periods=30).corr(_sma(closeadj, 20)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_base_v131_signal(closeadj):
    """120d rolling Pearson correlation of SMA(20) vs SMA(60)."""
    return _sma(closeadj, 20).rolling(120, min_periods=120).corr(_sma(closeadj, 60)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_base_v132_signal(closeadj):
    """60d rolling corr between EMA(30) and its 10d-shifted self. Self-similarity."""
    e = _ema(closeadj, 30)
    return e.rolling(60, min_periods=60).corr(e.shift(10)).replace([np.inf, -np.inf], np.nan)


# === MA distance VOLATILITY (std of close-MA) (2) ==========================


def f01ms_f01_moving_average_systems_dist_std_sma30_base_v133_signal(closeadj):
    """30d std of (close - SMA(30)) / close. MA-distance volatility."""
    m = _sma(closeadj, 30)
    return ((closeadj - m).rolling(30, min_periods=30).std() / closeadj).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_dist_std_ema60_base_v134_signal(closeadj):
    """60d std of (close - EMA(60)) / close. Long MA-distance volatility."""
    e = _ema(closeadj, 60)
    return ((closeadj - e).rolling(60, min_periods=60).std() / closeadj).replace([np.inf, -np.inf], np.nan)


# === SAME-N kernel diffs (only 4, varied n) ================================


def f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_base_v135_signal(closeadj):
    """Bar-index of maximum (close - SMA(20)) in last 60 bars / 60.
    Position of largest above-MA distance in window."""
    n = 60
    d = closeadj - _sma(closeadj, 20)
    def _amax(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(int(np.argmax(x))) / float(n - 1)
    return d.rolling(n, min_periods=n).apply(_amax, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_hma_sma_diff_45d_base_v136_signal(closeadj):
    """log(HMA(45) / SMA(45)). Hull vs SMA same-n."""
    return np.log(_hma(closeadj, 45) / _sma(closeadj, 45)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_alma_sma_diff_80d_base_v137_signal(closeadj):
    """log(ALMA(80) / SMA(80)). Gaussian-w vs equal-w at long horizon."""
    return np.log(_alma(closeadj, 80) / _sma(closeadj, 80)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_wma_sma_diff_30d_base_v138_signal(closeadj):
    """log(WMA(30) / SMA(30)). Linear-w vs equal-w."""
    return np.log(_wma(closeadj, 30) / _sma(closeadj, 30)).replace([np.inf, -np.inf], np.nan)


# === SHORT/LONG-same-kernel diffs (only 3) =================================


def f01ms_f01_moving_average_systems_ema_12_26_diff_base_v139_signal(close):
    """log(EMA(12) / EMA(26)). MACD-style cross."""
    return np.log(_ema(close, 12) / _ema(close, 26)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_hma_20_80_diff_base_v140_signal(closeadj):
    """log(HMA(20) / HMA(80)). Hull short/long cross."""
    return np.log(_hma(closeadj, 20) / _hma(closeadj, 80)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_wma_10_30_diff_base_v141_signal(close):
    """log(WMA(10) / WMA(30)). WMA short/long cross."""
    return np.log(_wma(close, 10) / _wma(close, 30)).replace([np.inf, -np.inf], np.nan)


# === CROSSMAG (|short - long| / close) (2) =================================


def f01ms_f01_moving_average_systems_ma_distance_zscore_30d_base_v142_signal(closeadj):
    """z-score of (close - SMA(30)) using 90-day mean/std. Long-window
    normalization of short-window MA distance."""
    n = 30
    d = closeadj - _sma(closeadj, n)
    return ((d - d.rolling(90, min_periods=90).mean()) / d.rolling(90, min_periods=90).std()).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_crossmag_sma_50200_base_v143_signal(closeadj):
    """|SMA(50)-SMA(200)| / close. Long-horizon cross magnitude."""
    return ((_sma(closeadj, 50) - _sma(closeadj, 200)).abs() / closeadj).replace([np.inf, -np.inf], np.nan)


# === MA self-momentum (1) ==================================================


def f01ms_f01_moving_average_systems_ma_dist_argmin_60d_base_v144_signal(closeadj):
    """Bar-index of minimum (close - SMA(60)) in last 60 bars / 60. Position
    of largest below-MA distance in the window — structural feature."""
    n = 60
    d = closeadj - _sma(closeadj, n)
    def _amin(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(int(np.argmin(x))) / float(n - 1)
    return d.rolling(n, min_periods=n).apply(_amin, raw=True).replace([np.inf, -np.inf], np.nan)


# === Wide-spaced level-distance features (only 3, spaced) ==================


def f01ms_f01_moving_average_systems_logclose_sma_8d_base_v145_signal(close):
    """log(close / SMA(8))."""
    return np.log(close / _sma(close, 8)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_logclose_sma_50d_base_v146_signal(closeadj):
    """log(closeadj / SMA(50))."""
    return np.log(closeadj / _sma(closeadj, 50)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_logclose_sma_252d_base_v147_signal(closeadj):
    """log(closeadj / SMA(252))."""
    return np.log(closeadj / _sma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)


# === MA dispersion / second-order stats (3) ================================


def f01ms_f01_moving_average_systems_ma_skew_60d_base_v148_signal(closeadj):
    """Rolling skew of (close - SMA(60)) over 60 bars."""
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_kurt_60d_base_v149_signal(closeadj):
    """Rolling kurtosis of (close - SMA(60)) over 60 bars."""
    d = closeadj - _sma(closeadj, 60)
    return d.rolling(60, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ema_acceleration_30d_base_v150_signal(closeadj):
    """ema(30).pct_change(5).diff(5) — EMA-pct-change acceleration."""
    return _ema(closeadj, 30).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f01_moving_average_systems_base_076_150_REGISTRY = {
    "f01ms_f01_moving_average_systems_sign_close_sma8d_base_v076_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_sma8d_base_v076_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma50d_base_v077_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma50d_base_v077_signal},
    "f01ms_f01_moving_average_systems_sign_close_sma200d_base_v078_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_sma200d_base_v078_signal},
    "f01ms_f01_moving_average_systems_sign_sma5_sma20_base_v079_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_sma5_sma20_base_v079_signal},
    "f01ms_f01_moving_average_systems_sign_ema20_ema50_base_v080_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_ema20_ema50_base_v080_signal},
    "f01ms_f01_moving_average_systems_sign_sma50_sma200_base_v081_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_sma50_sma200_base_v081_signal},
    "f01ms_f01_moving_average_systems_sign_hma30_hma90_base_v082_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_hma30_hma90_base_v082_signal},
    "f01ms_f01_moving_average_systems_sign_vwma_sma_30d_base_v083_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_sign_vwma_sma_30d_base_v083_signal},
    "f01ms_f01_moving_average_systems_daysince_close_sma20_30d_base_v084_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_close_sma20_30d_base_v084_signal},
    "f01ms_f01_moving_average_systems_daysince_close_sma50_100d_base_v085_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_close_sma50_100d_base_v085_signal},
    "f01ms_f01_moving_average_systems_daysince_ema_2050_150d_base_v086_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_ema_2050_150d_base_v086_signal},
    "f01ms_f01_moving_average_systems_daysince_sma_50200_252d_base_v087_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_sma_50200_252d_base_v087_signal},
    "f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_base_v088_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_base_v088_signal},
    "f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_base_v089_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_base_v089_signal},
    "f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_base_v090_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_base_v090_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma20_60d_base_v091_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma20_60d_base_v091_signal},
    "f01ms_f01_moving_average_systems_fracabove_sma200_120d_base_v092_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_sma200_120d_base_v092_signal},
    "f01ms_f01_moving_average_systems_fracabove_ema50_30d_base_v093_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_fracabove_ema50_30d_base_v093_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_short_base_v094_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_order_short_base_v094_signal},
    "f01ms_f01_moving_average_systems_ribbon_order_long_base_v095_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_order_long_base_v095_signal},
    "f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_base_v096_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_base_v096_signal},
    "f01ms_f01_moving_average_systems_ribbon_cv_80d_base_v097_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_cv_80d_base_v097_signal},
    "f01ms_f01_moving_average_systems_kernel_disp_25d_base_v098_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_disp_25d_base_v098_signal},
    "f01ms_f01_moving_average_systems_kernel_agree_30d_base_v099_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kernel_agree_30d_base_v099_signal},
    "f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_base_v101_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_base_v101_signal},
    "f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_base_v102_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_base_v102_signal},
    "f01ms_f01_moving_average_systems_rank_dist_sma60_30d_base_v103_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_dist_sma60_30d_base_v103_signal},
    "f01ms_f01_moving_average_systems_tanh_z_ema30_base_v104_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_tanh_z_ema30_base_v104_signal},
    "f01ms_f01_moving_average_systems_arctan_z_sma60_base_v105_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_arctan_z_sma60_base_v105_signal},
    "f01ms_f01_moving_average_systems_slope_sign_sma30_base_v106_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_sign_sma30_base_v106_signal},
    "f01ms_f01_moving_average_systems_slope_sign_sma100_base_v107_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_sign_sma100_base_v107_signal},
    "f01ms_f01_moving_average_systems_slope_diff_2060_base_v108_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_diff_2060_base_v108_signal},
    "f01ms_f01_moving_average_systems_ma_slope_streak_30d_base_v109_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_slope_streak_30d_base_v109_signal},
    "f01ms_f01_moving_average_systems_curv_sma30_base_v110_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sma30_base_v110_signal},
    "f01ms_f01_moving_average_systems_curv_ema80_base_v111_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_ema80_base_v111_signal},
    "f01ms_f01_moving_average_systems_curv_sign_hma40_base_v112_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_sign_hma40_base_v112_signal},
    "f01ms_f01_moving_average_systems_high_ma_low_ma_30d_base_v113_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_ma_low_ma_30d_base_v113_signal},
    "f01ms_f01_moving_average_systems_high_ma_low_ma_60d_base_v114_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_ma_low_ma_60d_base_v114_signal},
    "f01ms_f01_moving_average_systems_typ_close_diff_50d_base_v115_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_typ_close_diff_50d_base_v115_signal},
    "f01ms_f01_moving_average_systems_hl2_close_diff_25d_base_v116_signal": {"inputs": ["high", "low", "closeadj"], "func": f01ms_f01_moving_average_systems_hl2_close_diff_25d_base_v116_signal},
    "f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_base_v117_signal": {"inputs": ["open", "high", "low", "close"], "func": f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_base_v117_signal},
    "f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_base_v118_signal": {"inputs": ["high", "low"], "func": f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_base_v118_signal},
    "f01ms_f01_moving_average_systems_high_ma_close_ma_70d_base_v119_signal": {"inputs": ["high", "closeadj"], "func": f01ms_f01_moving_average_systems_high_ma_close_ma_70d_base_v119_signal},
    "f01ms_f01_moving_average_systems_updnratio_25d_base_v120_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_updnratio_25d_base_v120_signal},
    "f01ms_f01_moving_average_systems_upma_sma_diff_60d_base_v121_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_upma_sma_diff_60d_base_v121_signal},
    "f01ms_f01_moving_average_systems_vwma_sma_diff_25d_base_v122_signal": {"inputs": ["close", "volume"], "func": f01ms_f01_moving_average_systems_vwma_sma_diff_25d_base_v122_signal},
    "f01ms_f01_moving_average_systems_vwma_short_long_diff_base_v123_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_vwma_short_long_diff_base_v123_signal},
    "f01ms_f01_moving_average_systems_sign_vwma60_sma60_base_v124_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_sign_vwma60_sma60_base_v124_signal},
    "f01ms_f01_moving_average_systems_median_sma_diff_40d_base_v125_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_median_sma_diff_40d_base_v125_signal},
    "f01ms_f01_moving_average_systems_q75_q25_log_60d_base_v126_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_q75_q25_log_60d_base_v126_signal},
    "f01ms_f01_moving_average_systems_close_above_median_30d_base_v127_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_close_above_median_30d_base_v127_signal},
    "f01ms_f01_moving_average_systems_geom_arith_diff_50d_base_v128_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_geom_arith_diff_50d_base_v128_signal},
    "f01ms_f01_moving_average_systems_harm_geom_diff_25d_base_v129_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_harm_geom_diff_25d_base_v129_signal},
    "f01ms_f01_moving_average_systems_corr_close_sma20_30d_base_v130_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_close_sma20_30d_base_v130_signal},
    "f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_base_v131_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_base_v131_signal},
    "f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_base_v132_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_base_v132_signal},
    "f01ms_f01_moving_average_systems_dist_std_sma30_base_v133_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dist_std_sma30_base_v133_signal},
    "f01ms_f01_moving_average_systems_dist_std_ema60_base_v134_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dist_std_ema60_base_v134_signal},
    "f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_base_v135_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_base_v135_signal},
    "f01ms_f01_moving_average_systems_hma_sma_diff_45d_base_v136_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hma_sma_diff_45d_base_v136_signal},
    "f01ms_f01_moving_average_systems_alma_sma_diff_80d_base_v137_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_alma_sma_diff_80d_base_v137_signal},
    "f01ms_f01_moving_average_systems_wma_sma_diff_30d_base_v138_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_wma_sma_diff_30d_base_v138_signal},
    "f01ms_f01_moving_average_systems_ema_12_26_diff_base_v139_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_ema_12_26_diff_base_v139_signal},
    "f01ms_f01_moving_average_systems_hma_20_80_diff_base_v140_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hma_20_80_diff_base_v140_signal},
    "f01ms_f01_moving_average_systems_wma_10_30_diff_base_v141_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_wma_10_30_diff_base_v141_signal},
    "f01ms_f01_moving_average_systems_ma_distance_zscore_30d_base_v142_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_distance_zscore_30d_base_v142_signal},
    "f01ms_f01_moving_average_systems_crossmag_sma_50200_base_v143_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_crossmag_sma_50200_base_v143_signal},
    "f01ms_f01_moving_average_systems_ma_dist_argmin_60d_base_v144_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_dist_argmin_60d_base_v144_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_8d_base_v145_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_logclose_sma_8d_base_v145_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_50d_base_v146_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_sma_50d_base_v146_signal},
    "f01ms_f01_moving_average_systems_logclose_sma_252d_base_v147_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_sma_252d_base_v147_signal},
    "f01ms_f01_moving_average_systems_ma_skew_60d_base_v148_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_skew_60d_base_v148_signal},
    "f01ms_f01_moving_average_systems_ma_kurt_60d_base_v149_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_kurt_60d_base_v149_signal},
    "f01ms_f01_moving_average_systems_ema_acceleration_30d_base_v150_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ema_acceleration_30d_base_v150_signal},
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
    for name, entry in f01_moving_average_systems_base_076_150_REGISTRY.items():
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
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
