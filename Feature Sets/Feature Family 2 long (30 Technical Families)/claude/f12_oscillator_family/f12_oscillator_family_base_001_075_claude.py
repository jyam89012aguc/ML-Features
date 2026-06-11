"""f12_oscillator_family base features 001-075.

Domain: bounded oscillating momentum indicators that map price action
to a fixed range. Classic oscillators: RSI, Stochastic %K/%D, Williams
%R, CCI, MFI, Ultimate Oscillator, Awesome Oscillator, Detrended Price
Oscillator (causal), Stochastic RSI, Klinger Oscillator, Chaikin
Oscillator. Plus derived/transformed bounded variants: arctan, tanh,
z-score, percentile rank, overbought/oversold streak counts and
days-since signals.

Each function spells its formula inline. Window > 21d uses closeadj.
NaN policy: only replace([inf,-inf],nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (small primitives; each feature still spells its full formula)
# ---------------------------------------------------------------------------


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _rsi(s: pd.Series, n: int) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- RSI core family (varied N) -----------------------------------------


def f12os_f12_oscillator_family_rsi_7d_base_v001_signal(close):
    """RSI(7). Classic Wilder relative strength index, short window. Bounded 0..100."""
    n = 7
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsi_14d_base_v002_signal(close):
    """RSI(14). Canonical Wilder RSI, the standard oscillator. Bounded 0..100."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsi_50d_base_v003_signal(closeadj):
    """RSI(50). Long-horizon Wilder RSI on adjusted close. Bounded 0..100."""
    n = 50
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsidsmid_21d_base_v004_signal(close):
    """Days-since RSI(21) last crossed midline (50), capped 100. Persistence proxy."""
    n = 21
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    sgn = np.sign(rsi - 50.0)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 100.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(100, min_periods=100).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsidiff21_30d_base_v005_signal(closeadj):
    """RSI(30) - SMA(RSI(30), 21). De-trended RSI; isolates RSI fast deviation from its local mean."""
    n = 30
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (rsi - rsi.rolling(21, min_periods=21).mean()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsisma_60d_base_v006_signal(closeadj):
    """SMA(RSI(14), 30) on closeadj. Smoothed RSI — oscillator-of-oscillator."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsisign_14d_base_v007_signal(close):
    """sign(RSI(14) - 50). Discrete bull/bear midline state."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return np.sign((100.0 - 100.0 / (1.0 + rs)) - 50.0).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiob_20d_base_v008_signal(close):
    """Bars in last 20 with RSI(14) > 70. Overbought density."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    flag = (rsi > 70.0).astype(float).where(~rsi.isna())
    return flag.rolling(20, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsios_30d_base_v009_signal(closeadj):
    """Bars in last 30 with RSI(14) < 30. Oversold density."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    flag = (rsi < 30.0).astype(float).where(~rsi.isna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsidsob_60d_base_v010_signal(closeadj):
    """Days-since-last RSI(14) > 70, capped at 60. Recency of overbought event."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    cond = (rsi > 70.0).astype(float).where(~rsi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsidsos_80d_base_v011_signal(closeadj):
    """Days-since-last RSI(14) < 30, capped at 80. Recency of oversold event."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    cond = (rsi < 30.0).astype(float).where(~rsi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 80.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(80, min_periods=80).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsirank_120d_base_v012_signal(closeadj):
    """120d percentile rank of RSI(14). Where current RSI sits in its trailing distribution."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsivar_80d_base_v013_signal(closeadj):
    """Rolling 80d standard deviation of RSI(14). Local oscillator volatility."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(80, min_periods=80).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsixmid_60d_base_v014_signal(close):
    """Count of RSI(14) midline crossings in last 60 bars. Reversal frequency."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    sgn = np.sign(rsi - 50.0)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsifloor_120d_base_v015_signal(closeadj):
    """120d rolling min of RSI(14). Trailing oversold-floor envelope."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(120, min_periods=120).min().replace([np.inf, -np.inf], np.nan)


# --- Stochastic %K / %D family ----------------------------------------


def f12os_f12_oscillator_family_stochk_5d_base_v016_signal(high, low, close):
    """Stochastic %K, N=5. (close - low_N)/(high_N - low_N) * 100. Bounded 0..100."""
    n = 5
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochk_14d_base_v017_signal(high, low, close):
    """Stochastic %K, N=14. Canonical fast stochastic oscillator. Bounded 0..100."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochk_50d_base_v018_signal(high, low, closeadj):
    """Stochastic %K, N=50. Long-horizon stochastic on adjusted close. Bounded 0..100."""
    n = 50
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochd_14d_base_v019_signal(high, low, close):
    """Stochastic %D = SMA(%K, 3) at N=14. Slow stochastic. Bounded 0..100."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)
    return k.rolling(3, min_periods=3).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkd_14d_base_v020_signal(high, low, close):
    """%K - %D crossover differential, N=14. Crossing zero = oscillator crossover."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)
    d = k.rolling(3, min_periods=3).mean()
    return (k - d).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkdxover_50d_base_v021_signal(high, low, closeadj):
    """Count of %K/%D crossovers in last 50 (N=14). Frequency of cross-flips."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    d = k.rolling(3, min_periods=3).mean()
    s = np.sign(k - d)
    xo = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return xo.rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochob_50d_base_v022_signal(high, low, closeadj):
    """Fraction of last 50 bars with %K(14) > 80 (overbought zone) on closeadj."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    flag = (k > 80.0).astype(float).where(~k.isna())
    return flag.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochstreakob_30d_base_v023_signal(high, low, closeadj):
    """Current consecutive-bar streak of %K(14) > 80, capped at 30."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    cond = (k > 80.0).astype(float).where(~k.isna())
    def _streak(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochcent_30d_base_v024_signal(high, low, closeadj):
    """%K(30) centered: %K - 50, bounded -50..+50."""
    n = 30
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return (k - 50.0).replace([np.inf, -np.inf], np.nan)


# --- Williams %R family ------------------------------------------------


def f12os_f12_oscillator_family_willr_7d_base_v025_signal(high, low, close):
    """Williams %R, N=7. (high_N - close)/(high_N - low_N) * -100. Bounded -100..0.
    Short window distinct from %K(14)."""
    n = 7
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (-100.0 * (hh - close) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_willrxlow_100d_base_v026_signal(high, low, closeadj):
    """Fraction of last 100 bars with Williams %R(21) < -80 (oversold density)."""
    n = 21
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    wr = -100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan)
    flag = (wr < -80.0).astype(float).where(~wr.isna())
    return flag.rolling(100, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_willrdsmid_21d_base_v027_signal(high, low, close):
    """Days-since-last Williams %R(21) crossed midline (-50), capped 80. Persistence."""
    n = 21
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    wr = -100.0 * (hh - close) / (hh - ll).replace(0.0, np.nan)
    sgn = np.sign(wr + 50.0)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 80.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(80, min_periods=80).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- CCI family -------------------------------------------------------


def f12os_f12_oscillator_family_cci_14d_base_v028_signal(high, low, close):
    """CCI(14). (TP - SMA(TP))/(0.015*MAD(TP)). Typical price commodity channel index."""
    n = 14
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    return ((tp - sma) / (0.015 * mad.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cci_50d_base_v029_signal(high, low, closeadj):
    """CCI(50) using closeadj in typical price. Long-horizon CCI."""
    n = 50
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    return ((tp - sma) / (0.015 * mad.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccitanh_20d_base_v030_signal(high, low, close):
    """tanh(CCI(20)/100). Squashes CCI to bounded -1..+1."""
    n = 20
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return np.tanh(cci / 100.0).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cciob_40d_base_v031_signal(high, low, closeadj):
    """Fraction of last 40 bars with CCI(20) > 100 (overbought)."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    flag = (cci > 100.0).astype(float).where(~cci.isna())
    return flag.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cciextrm_120d_base_v032_signal(high, low, closeadj):
    """120d rolling max of |CCI(20)|. Recent extreme magnitude of CCI."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return cci.abs().rolling(120, min_periods=120).max().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccisign_30d_base_v033_signal(high, low, closeadj):
    """sign(CCI(30)). Discrete CCI directional state."""
    n = 30
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return np.sign(cci).replace([np.inf, -np.inf], np.nan)


# --- MFI (Money Flow Index, volume-aware) -----------------------------


def f12os_f12_oscillator_family_mfi_14d_base_v034_signal(high, low, close, volume):
    """MFI(14): RSI applied to typical-price * volume. Money flow index. Bounded 0..100."""
    n = 14
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    posn = pos.rolling(n, min_periods=n).sum()
    negn = neg.rolling(n, min_periods=n).sum()
    mr = posn / negn.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + mr)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfi_30d_base_v035_signal(high, low, closeadj, volume):
    """MFI(30) on closeadj typical price. Mid-horizon money flow index."""
    n = 30
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    posn = pos.rolling(n, min_periods=n).sum()
    negn = neg.rolling(n, min_periods=n).sum()
    mr = posn / negn.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + mr)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfinorm_21d_base_v036_signal(high, low, close, volume):
    """MFI(21) normalized to -1..+1: (MFI - 50)/50."""
    n = 21
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    posn = pos.rolling(n, min_periods=n).sum()
    negn = neg.rolling(n, min_periods=n).sum()
    mr = posn / negn.replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return ((mfi - 50.0) / 50.0).replace([np.inf, -np.inf], np.nan)


# --- Ultimate Oscillator ----------------------------------------------


def f12os_f12_oscillator_family_uo_7_14_28_base_v037_signal(high, low, close):
    """Ultimate Oscillator(7,14,28). Weighted combo of three buying-pressure ratios."""
    pc = close.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = close - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    return (100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uolong_14_28_56_base_v038_signal(high, low, closeadj):
    """Ultimate Oscillator with doubled windows (14,28,56). Long-horizon variant."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a1 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a2 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    a3 = bp.rolling(56, min_periods=56).sum() / trv.rolling(56, min_periods=56).sum().replace(0.0, np.nan)
    return (100.0 * (4.0 * a1 + 2.0 * a2 + a3) / 7.0).replace([np.inf, -np.inf], np.nan)


# --- Awesome Oscillator (AO) ------------------------------------------


def f12os_f12_oscillator_family_aopct_5_34_base_v039_signal(high, low):
    """Awesome Oscillator as % of long MA: (SMA(MP,5)-SMA(MP,34))/SMA(MP,34)*100. Bounded scale."""
    mp = 0.5 * (high + low)
    s = mp.rolling(5, min_periods=5).mean()
    l = mp.rolling(34, min_periods=34).mean()
    return (100.0 * (s - l) / l.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aoz_60d_base_v040_signal(high, low):
    """Z-score of Awesome Oscillator over 60d window. Standardized AO anomaly."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    mu = ao.rolling(60, min_periods=60).mean()
    sd = ao.rolling(60, min_periods=60).std(ddof=1)
    return ((ao - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Detrended Price Oscillator (causal) ------------------------------


def f12os_f12_oscillator_family_dpo_20d_base_v041_signal(close):
    """Causal DPO(20): close - SMA(close, 20).shift(N/2+1). No look-ahead."""
    n = 20
    s = close - close.rolling(n, min_periods=n).mean().shift(n // 2 + 1)
    return s.replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_dpoxsign_60d_base_v042_signal(closeadj):
    """Count of causal DPO(20) sign flips in last 60 bars. Detrended-oscillator
    zero-cross frequency — bounded by 60."""
    n = 20
    dpo = closeadj - closeadj.rolling(n, min_periods=n).mean().shift(n // 2 + 1)
    sgn = np.sign(dpo)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# --- Stochastic RSI ---------------------------------------------------


def f12os_f12_oscillator_family_stochrsi_14d_base_v043_signal(close):
    """Stochastic RSI(14, 14): stochastic applied to RSI(14). Bounded 0..1."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    return ((rsi - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochrsi_50d_base_v044_signal(closeadj):
    """Stochastic RSI(50, 50) on closeadj. Long-horizon stoch-RSI."""
    n = 50
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    return ((rsi - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Chaikin Oscillator (volume) --------------------------------------


def f12os_f12_oscillator_family_chaikin_3_10_base_v045_signal(high, low, close, volume):
    """Chaikin Oscillator: EMA(ADL,3)-EMA(ADL,10) where ADL is accumulation/distribution line."""
    clv = ((close - low) - (high - close)) / (high - low).replace(0.0, np.nan)
    adl = (clv * volume).cumsum()
    return (adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_chaikinrank_120d_base_v046_signal(high, low, close, volume):
    """120d percentile rank of Chaikin Oscillator(6,20). Slower variant. Bounded 0..1."""
    clv = ((close - low) - (high - close)) / (high - low).replace(0.0, np.nan)
    adl = (clv * volume).cumsum()
    co = adl.ewm(span=6, adjust=False, min_periods=6).mean() - adl.ewm(span=20, adjust=False, min_periods=20).mean()
    return co.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Klinger Oscillator (volume) --------------------------------------


def f12os_f12_oscillator_family_klinger_34_55_base_v047_signal(high, low, close, volume):
    """Klinger Volume Oscillator: EMA(VF,34) - EMA(VF,55), VF = sign of trend * volume * |trend|."""
    tp = (high + low + close) / 3.0
    trend = np.sign(tp - tp.shift(1))
    dm = (high - low)
    cm = dm.copy()
    same = (trend == trend.shift(1)) & trend.notna() & trend.shift(1).notna()
    cm = cm.where(~same, cm.shift(1) + dm)
    vf = volume * trend * (2.0 * (dm / cm.replace(0.0, np.nan)) - 1.0) * 100.0
    return (vf.ewm(span=34, adjust=False, min_periods=34).mean() - vf.ewm(span=55, adjust=False, min_periods=55).mean()).replace([np.inf, -np.inf], np.nan)


# --- BIAS oscillator ---------------------------------------------------


def f12os_f12_oscillator_family_bias_10d_base_v048_signal(close):
    """BIAS oscillator: (close - SMA(close,10))/SMA * 100. Short-horizon bounded."""
    n = 10
    s = close.rolling(n, min_periods=n).mean()
    return (100.0 * (close - s) / s.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_bias_60d_base_v049_signal(closeadj):
    """BIAS oscillator(60) on closeadj. Long-horizon BIAS in %."""
    n = 60
    s = closeadj.rolling(n, min_periods=n).mean()
    return (100.0 * (closeadj - s) / s.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Cross-oscillator combinations -----------------------------------


def f12os_f12_oscillator_family_rsistochzdiff_30d_base_v050_signal(high, low, closeadj):
    """Z-score(RSI(14),60) - Z-score(%K(14),60). Cross-oscillator standardized divergence."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    zr = (rsi - rsi.rolling(60, min_periods=60).mean()) / rsi.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    zk = (k - k.rolling(60, min_periods=60).mean()) / k.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    return (zr - zk).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsicciagree_50d_base_v051_signal(high, low, closeadj):
    """Mean over 50 bars of sign(RSI(14)-50) * sign(CCI(20)). Oscillator-sign agreement."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    m = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(m, min_periods=m).mean()
    mad = (tp - sma).abs().rolling(m, min_periods=m).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    prod = np.sign(rsi - 50.0) * np.sign(cci)
    return prod.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscobcnt_30d_base_v052_signal(high, low, closeadj):
    """Count over 30 bars of overbought-triple-confirm: RSI>70 AND %K>80 AND CCI>100."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    m = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(m, min_periods=m).mean()
    mad = (tp - sma).abs().rolling(m, min_periods=m).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    flag = ((rsi > 70.0) & (k > 80.0) & (cci > 100.0)).astype(float).where(~rsi.isna() & ~k.isna() & ~cci.isna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscdisp_30d_base_v053_signal(high, low, closeadj):
    """Dispersion (std) of {RSI(14), %K(14), %R+100}. Oscillator panel disagreement."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    wr_norm = 100.0 + (-100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan))
    panel = pd.concat([rsi, k, wr_norm], axis=1)
    return panel.std(axis=1, ddof=1).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscbullcnt_30d_base_v054_signal(high, low, closeadj):
    """Count of oscillators above midline: {RSI>50, %K>50, %R>-50}. Range 0..3."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    wr = -100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan)
    cnt = ((rsi > 50.0).astype(float).where(~rsi.isna())
           + (k > 50.0).astype(float).where(~k.isna())
           + (wr > -50.0).astype(float).where(~wr.isna()))
    return cnt.replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochzkurt_60d_base_v055_signal(high, low, closeadj):
    """Rolling 60d kurtosis of %K(14). Tail-fatness of stochastic oscillator distribution."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return k.rolling(60, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


# --- Double-smoothed oscillators ---------------------------------------


def f12os_f12_oscillator_family_rsidouble_30d_base_v056_signal(closeadj):
    """SMA(SMA(RSI(14), 5), 10) on closeadj. Double-smoothed RSI."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(5, min_periods=5).mean().rolling(10, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochskew_60d_base_v057_signal(high, low, closeadj):
    """Rolling 60d skewness of %K(14). Distribution asymmetry of stochastic oscillator."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return k.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


# --- Various structural oscillator transforms --------------------------


def f12os_f12_oscillator_family_rsiabs50_25d_base_v058_signal(close):
    """|RSI(25) - 50|. Distance from midline, direction-agnostic momentum extent."""
    n = 25
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (rsi - 50.0).abs().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochrange_50d_base_v059_signal(high, low, closeadj):
    """%K(14) range = max(%K, 50) - min(%K, 50) over 50d. Oscillator excursion span."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return (k.rolling(50, min_periods=50).max() - k.rolling(50, min_periods=50).min()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccixsign_60d_base_v060_signal(high, low, closeadj):
    """Count of CCI(20) sign flips in last 60 bars. Oscillator zero-cross frequency."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    sgn = np.sign(cci)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsistreaktop_30d_base_v061_signal(close):
    """Current streak of consecutive bars with RSI(14) > 50, capped at 30."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    cond = (rsi > 50.0).astype(float).where(~rsi.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aoabs_50d_base_v062_signal(high, low):
    """|Awesome Oscillator| — magnitude of median-price momentum."""
    mp = 0.5 * (high + low)
    return (mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()).abs().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfi_rsidiff_30d_base_v063_signal(high, low, closeadj, volume):
    """MFI(14) - RSI(14). Volume-weighted minus price-only momentum oscillator divergence."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (mfi - rsi).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkdpath_50d_base_v064_signal(high, low, closeadj):
    """Sum of |%K - %D| over last 50 bars (N=14). Oscillator path-length divergence."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    d = k.rolling(3, min_periods=3).mean()
    return (k - d).abs().rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uoslp_30d_base_v065_signal(high, low, closeadj):
    """10-bar diff of Ultimate Oscillator. Rate-of-change of UO."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    return uo.diff(10).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_dpostreak_30d_base_v066_signal(closeadj):
    """Current consecutive-bar streak of DPO(40) > 0, capped at 30."""
    n = 40
    s = closeadj - closeadj.rolling(n, min_periods=n).mean().shift(n // 2 + 1)
    cond = (s > 0.0).astype(float).where(~s.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochrsisma_21d_base_v067_signal(close):
    """SMA(StochRSI(14), 7). Smoothed stochastic-RSI."""
    n = 14
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    srsi = (rsi - lo) / (hi - lo).replace(0.0, np.nan)
    return srsi.rolling(7, min_periods=7).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aobullbear_50d_base_v068_signal(high, low):
    """Fraction of last 50 bars with Awesome Oscillator > 0 (bull-momentum density)."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    flag = (ao > 0.0).astype(float).where(~ao.isna())
    return flag.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_biaspct_30d_base_v069_signal(closeadj):
    """30d percentile rank of BIAS(20). Where current BIAS lies in trailing distribution."""
    n = 20
    s = closeadj.rolling(n, min_periods=n).mean()
    b = 100.0 * (closeadj - s) / s.replace(0.0, np.nan)
    return b.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccinegrun_30d_base_v070_signal(high, low, closeadj):
    """Current streak of consecutive bars with CCI(14) < -100 (oversold), capped at 30."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    cond = (cci < -100.0).astype(float).where(~cci.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsimedian_60d_base_v071_signal(closeadj):
    """Rolling 60d median of RSI(14). Robust central tendency of RSI."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(60, min_periods=60).median().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfivlog_50d_base_v072_signal(high, low, closeadj, volume):
    """log(MFI/(100-MFI)) at N=50. Logit transform of MFI, unbounded but smooth and centered."""
    n = 50
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return np.log(mfi.replace(0.0, np.nan) / (100.0 - mfi).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_chaikinsign_40d_base_v073_signal(high, low, close, volume):
    """sign(Chaikin Oscillator). Discrete A/D divergence direction."""
    clv = ((close - low) - (high - close)) / (high - low).replace(0.0, np.nan)
    adl = (clv * volume).cumsum()
    co = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    return np.sign(co).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkrng_50d_base_v074_signal(high, low, close):
    """Stochastic %K(50) range expansion: %K - rolling-50d mean(%K). De-meaned stochastic."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)
    return (k - k.rolling(50, min_periods=50).mean()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsivolratio_30d_base_v075_signal(closeadj):
    """(RSI(7) - RSI(50))/(|RSI(7) - 50| + |RSI(50) - 50| + 1). Normalized fast/slow RSI gap."""
    n1 = 7
    d = closeadj.diff()
    au1 = d.clip(lower=0.0).ewm(alpha=1.0 / float(n1), adjust=False, min_periods=n1).mean()
    ad1 = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n1), adjust=False, min_periods=n1).mean()
    rs1 = au1 / ad1.replace(0.0, np.nan)
    r1 = 100.0 - 100.0 / (1.0 + rs1)
    n2 = 50
    au2 = d.clip(lower=0.0).ewm(alpha=1.0 / float(n2), adjust=False, min_periods=n2).mean()
    ad2 = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n2), adjust=False, min_periods=n2).mean()
    rs2 = au2 / ad2.replace(0.0, np.nan)
    r2 = 100.0 - 100.0 / (1.0 + rs2)
    return ((r1 - r2) / ((r1 - 50.0).abs() + (r2 - 50.0).abs() + 1.0)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f12_oscillator_family_base_001_075_REGISTRY = {
    "f12os_f12_oscillator_family_rsi_7d_base_v001_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsi_7d_base_v001_signal},
    "f12os_f12_oscillator_family_rsi_14d_base_v002_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsi_14d_base_v002_signal},
    "f12os_f12_oscillator_family_rsi_50d_base_v003_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsi_50d_base_v003_signal},
    "f12os_f12_oscillator_family_rsidsmid_21d_base_v004_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsidsmid_21d_base_v004_signal},
    "f12os_f12_oscillator_family_rsidiff21_30d_base_v005_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsidiff21_30d_base_v005_signal},
    "f12os_f12_oscillator_family_rsisma_60d_base_v006_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsisma_60d_base_v006_signal},
    "f12os_f12_oscillator_family_rsisign_14d_base_v007_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsisign_14d_base_v007_signal},
    "f12os_f12_oscillator_family_rsiob_20d_base_v008_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsiob_20d_base_v008_signal},
    "f12os_f12_oscillator_family_rsios_30d_base_v009_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsios_30d_base_v009_signal},
    "f12os_f12_oscillator_family_rsidsob_60d_base_v010_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsidsob_60d_base_v010_signal},
    "f12os_f12_oscillator_family_rsidsos_80d_base_v011_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsidsos_80d_base_v011_signal},
    "f12os_f12_oscillator_family_rsirank_120d_base_v012_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsirank_120d_base_v012_signal},
    "f12os_f12_oscillator_family_rsivar_80d_base_v013_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsivar_80d_base_v013_signal},
    "f12os_f12_oscillator_family_rsixmid_60d_base_v014_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsixmid_60d_base_v014_signal},
    "f12os_f12_oscillator_family_rsifloor_120d_base_v015_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsifloor_120d_base_v015_signal},
    "f12os_f12_oscillator_family_stochk_5d_base_v016_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochk_5d_base_v016_signal},
    "f12os_f12_oscillator_family_stochk_14d_base_v017_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochk_14d_base_v017_signal},
    "f12os_f12_oscillator_family_stochk_50d_base_v018_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochk_50d_base_v018_signal},
    "f12os_f12_oscillator_family_stochd_14d_base_v019_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochd_14d_base_v019_signal},
    "f12os_f12_oscillator_family_stochkd_14d_base_v020_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochkd_14d_base_v020_signal},
    "f12os_f12_oscillator_family_stochkdxover_50d_base_v021_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochkdxover_50d_base_v021_signal},
    "f12os_f12_oscillator_family_stochob_50d_base_v022_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochob_50d_base_v022_signal},
    "f12os_f12_oscillator_family_stochstreakob_30d_base_v023_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochstreakob_30d_base_v023_signal},
    "f12os_f12_oscillator_family_stochcent_30d_base_v024_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochcent_30d_base_v024_signal},
    "f12os_f12_oscillator_family_willr_7d_base_v025_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_willr_7d_base_v025_signal},
    "f12os_f12_oscillator_family_willrxlow_100d_base_v026_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_willrxlow_100d_base_v026_signal},
    "f12os_f12_oscillator_family_willrdsmid_21d_base_v027_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_willrdsmid_21d_base_v027_signal},
    "f12os_f12_oscillator_family_cci_14d_base_v028_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_cci_14d_base_v028_signal},
    "f12os_f12_oscillator_family_cci_50d_base_v029_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cci_50d_base_v029_signal},
    "f12os_f12_oscillator_family_ccitanh_20d_base_v030_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_ccitanh_20d_base_v030_signal},
    "f12os_f12_oscillator_family_cciob_40d_base_v031_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cciob_40d_base_v031_signal},
    "f12os_f12_oscillator_family_cciextrm_120d_base_v032_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cciextrm_120d_base_v032_signal},
    "f12os_f12_oscillator_family_ccisign_30d_base_v033_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccisign_30d_base_v033_signal},
    "f12os_f12_oscillator_family_mfi_14d_base_v034_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_mfi_14d_base_v034_signal},
    "f12os_f12_oscillator_family_mfi_30d_base_v035_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfi_30d_base_v035_signal},
    "f12os_f12_oscillator_family_mfinorm_21d_base_v036_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_mfinorm_21d_base_v036_signal},
    "f12os_f12_oscillator_family_uo_7_14_28_base_v037_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_uo_7_14_28_base_v037_signal},
    "f12os_f12_oscillator_family_uolong_14_28_56_base_v038_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uolong_14_28_56_base_v038_signal},
    "f12os_f12_oscillator_family_aopct_5_34_base_v039_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aopct_5_34_base_v039_signal},
    "f12os_f12_oscillator_family_aoz_60d_base_v040_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aoz_60d_base_v040_signal},
    "f12os_f12_oscillator_family_dpo_20d_base_v041_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_dpo_20d_base_v041_signal},
    "f12os_f12_oscillator_family_dpoxsign_60d_base_v042_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_dpoxsign_60d_base_v042_signal},
    "f12os_f12_oscillator_family_stochrsi_14d_base_v043_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_stochrsi_14d_base_v043_signal},
    "f12os_f12_oscillator_family_stochrsi_50d_base_v044_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_stochrsi_50d_base_v044_signal},
    "f12os_f12_oscillator_family_chaikin_3_10_base_v045_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_chaikin_3_10_base_v045_signal},
    "f12os_f12_oscillator_family_chaikinrank_120d_base_v046_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_chaikinrank_120d_base_v046_signal},
    "f12os_f12_oscillator_family_klinger_34_55_base_v047_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_klinger_34_55_base_v047_signal},
    "f12os_f12_oscillator_family_bias_10d_base_v048_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_bias_10d_base_v048_signal},
    "f12os_f12_oscillator_family_bias_60d_base_v049_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_bias_60d_base_v049_signal},
    "f12os_f12_oscillator_family_rsistochzdiff_30d_base_v050_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_rsistochzdiff_30d_base_v050_signal},
    "f12os_f12_oscillator_family_rsicciagree_50d_base_v051_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_rsicciagree_50d_base_v051_signal},
    "f12os_f12_oscillator_family_oscobcnt_30d_base_v052_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscobcnt_30d_base_v052_signal},
    "f12os_f12_oscillator_family_oscdisp_30d_base_v053_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscdisp_30d_base_v053_signal},
    "f12os_f12_oscillator_family_oscbullcnt_30d_base_v054_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscbullcnt_30d_base_v054_signal},
    "f12os_f12_oscillator_family_stochzkurt_60d_base_v055_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochzkurt_60d_base_v055_signal},
    "f12os_f12_oscillator_family_rsidouble_30d_base_v056_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsidouble_30d_base_v056_signal},
    "f12os_f12_oscillator_family_stochskew_60d_base_v057_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochskew_60d_base_v057_signal},
    "f12os_f12_oscillator_family_rsiabs50_25d_base_v058_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsiabs50_25d_base_v058_signal},
    "f12os_f12_oscillator_family_stochrange_50d_base_v059_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochrange_50d_base_v059_signal},
    "f12os_f12_oscillator_family_ccixsign_60d_base_v060_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccixsign_60d_base_v060_signal},
    "f12os_f12_oscillator_family_rsistreaktop_30d_base_v061_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsistreaktop_30d_base_v061_signal},
    "f12os_f12_oscillator_family_aoabs_50d_base_v062_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aoabs_50d_base_v062_signal},
    "f12os_f12_oscillator_family_mfi_rsidiff_30d_base_v063_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfi_rsidiff_30d_base_v063_signal},
    "f12os_f12_oscillator_family_stochkdpath_50d_base_v064_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochkdpath_50d_base_v064_signal},
    "f12os_f12_oscillator_family_uoslp_30d_base_v065_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uoslp_30d_base_v065_signal},
    "f12os_f12_oscillator_family_dpostreak_30d_base_v066_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_dpostreak_30d_base_v066_signal},
    "f12os_f12_oscillator_family_stochrsisma_21d_base_v067_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_stochrsisma_21d_base_v067_signal},
    "f12os_f12_oscillator_family_aobullbear_50d_base_v068_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aobullbear_50d_base_v068_signal},
    "f12os_f12_oscillator_family_biaspct_30d_base_v069_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_biaspct_30d_base_v069_signal},
    "f12os_f12_oscillator_family_ccinegrun_30d_base_v070_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccinegrun_30d_base_v070_signal},
    "f12os_f12_oscillator_family_rsimedian_60d_base_v071_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsimedian_60d_base_v071_signal},
    "f12os_f12_oscillator_family_mfivlog_50d_base_v072_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfivlog_50d_base_v072_signal},
    "f12os_f12_oscillator_family_chaikinsign_40d_base_v073_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_chaikinsign_40d_base_v073_signal},
    "f12os_f12_oscillator_family_stochkrng_50d_base_v074_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochkrng_50d_base_v074_signal},
    "f12os_f12_oscillator_family_rsivolratio_30d_base_v075_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsivolratio_30d_base_v075_signal},
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
    for name, entry in f12_oscillator_family_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
