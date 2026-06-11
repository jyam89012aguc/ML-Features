"""f12_oscillator_family base features 076-150.

Continuation of bounded momentum oscillators: more RSI/Stoch/CCI/MFI/UO
variants, additional smoothings, alternative bounded transforms, more
overbought/oversold sentinels at fresh windows distinct from 001-075.

Each function spells its formula inline. Window > 21d uses closeadj.
NaN policy: only replace([inf,-inf],nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


def f12os_f12_oscillator_family_rsi_21d_base_v076_signal(close):
    """RSI(21). Mid-horizon Wilder RSI."""
    n = 21
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsi_100d_base_v077_signal(closeadj):
    """RSI(100). Very long-horizon RSI — secular trend bound."""
    n = 100
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiema_30d_base_v078_signal(closeadj):
    """EMA(RSI(14), span=10) on closeadj. Exponentially smoothed RSI."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.ewm(span=10, adjust=False, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiceil_120d_base_v079_signal(closeadj):
    """120d rolling max of RSI(14). Trailing overbought-ceiling envelope."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return rsi.rolling(120, min_periods=120).max().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsispan_80d_base_v080_signal(closeadj):
    """80d (max RSI(14) - min RSI(14)). Oscillator excursion span."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (rsi.rolling(80, min_periods=80).max() - rsi.rolling(80, min_periods=80).min()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsistreakbot_30d_base_v081_signal(closeadj):
    """Current streak of consecutive bars with RSI(14) < 50, capped at 30."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    cond = (rsi < 50.0).astype(float).where(~rsi.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiextrm_80d_base_v082_signal(closeadj):
    """80d count of bars with RSI(14) in extreme zones (>70 or <30). Total
    overbought/oversold incidences."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    flag = ((rsi > 70.0) | (rsi < 30.0)).astype(float).where(~rsi.isna())
    return flag.rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiiqr_60d_base_v083_signal(closeadj):
    """60d interquartile range of RSI(14) (Q75 - Q25). Robust RSI dispersion."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (rsi.rolling(60, min_periods=60).quantile(0.75)
            - rsi.rolling(60, min_periods=60).quantile(0.25)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsigap_30d_base_v084_signal(closeadj):
    """RSI(14) - rolling 30d median of RSI(14). De-centered RSI vs robust local center."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return (rsi - rsi.rolling(30, min_periods=30).median()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsisig_15d_base_v085_signal(close):
    """Connor's RSI-2 (super-short RSI). RSI(2) on close. Bounded 0..100."""
    n = 2
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


# --- Stochastic variants -----------------------------------------------


def f12os_f12_oscillator_family_stochk_21d_base_v086_signal(high, low, close):
    """Stochastic %K, N=21. Mid-horizon stochastic. Bounded 0..100."""
    n = 21
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkpos_50d_base_v087_signal(high, low, closeadj):
    """50d count of bars where %K(14) > 50 (bull-stoch density)."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return (k > 50.0).astype(float).where(~k.isna()).rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochds_80d_base_v088_signal(high, low, closeadj):
    """Days-since-last %K(14) > 80, capped at 80. Recency of stochastic OB."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    cond = (k > 80.0).astype(float).where(~k.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 80.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(80, min_periods=80).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkmed_120d_base_v089_signal(high, low, closeadj):
    """120d rolling median of %K(14). Robust central tendency of stochastic."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return k.rolling(120, min_periods=120).median().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochkdslp_30d_base_v090_signal(high, low, closeadj):
    """5-bar diff of (%K - %D). Acceleration of fast-vs-slow stochastic gap."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    d = k.rolling(3, min_periods=3).mean()
    return (k - d).diff(5).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochwidemar_100d_base_v091_signal(high, low, closeadj):
    """Margin to 100d range edge: min(high_100d-closeadj, closeadj-low_100d)/(high_100d-low_100d).
    Bounded 0..0.5 oscillator of how close to either extreme price sits."""
    n = 100
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    rng = (hh - ll).replace(0.0, np.nan)
    top = (hh - closeadj) / rng
    bot = (closeadj - ll) / rng
    return pd.concat([top, bot], axis=1).min(axis=1).replace([np.inf, -np.inf], np.nan)


# --- Williams %R variants ---------------------------------------------


def f12os_f12_oscillator_family_willr_28d_base_v092_signal(high, low, closeadj):
    """Williams %R, N=28. Mid-horizon inverted stochastic."""
    n = 28
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return (-100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_willrslp_50d_base_v093_signal(high, low, closeadj):
    """10-bar slope of Williams %R(28). Rate-of-change of %R."""
    n = 28
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    wr = -100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan)
    return wr.diff(10).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_willrxhi_50d_base_v094_signal(high, low, closeadj):
    """Fraction of last 50 bars with Williams %R(21) > -20 (overbought zone)."""
    n = 21
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    wr = -100.0 * (hh - closeadj) / (hh - ll).replace(0.0, np.nan)
    return (wr > -20.0).astype(float).where(~wr.isna()).rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# --- CCI variants ------------------------------------------------------


def f12os_f12_oscillator_family_cci_30d_base_v095_signal(high, low, closeadj):
    """CCI(30). Mid-horizon commodity channel index."""
    n = 30
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    return ((tp - sma) / (0.015 * mad.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccislope_50d_base_v096_signal(high, low, closeadj):
    """10-bar diff of CCI(20). CCI rate-of-change."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return cci.diff(10).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccipos_60d_base_v097_signal(high, low, closeadj):
    """Fraction of last 60 bars with CCI(14) > 0 (bull-CCI density)."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return (cci > 0.0).astype(float).where(~cci.isna()).rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cciskew_60d_base_v098_signal(high, low, closeadj):
    """60d rolling skewness of CCI(30). Distribution asymmetry."""
    n = 30
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return cci.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cciosmin_60d_base_v099_signal(high, low, closeadj):
    """60d rolling min of CCI(20). Trailing oversold floor."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return cci.rolling(60, min_periods=60).min().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccids_60d_base_v100_signal(high, low, closeadj):
    """Days-since-last CCI(20) > 100 (overbought), capped 60."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    cond = (cci > 100.0).astype(float).where(~cci.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- MFI variants ------------------------------------------------------


def f12os_f12_oscillator_family_mfi_50d_base_v101_signal(high, low, closeadj, volume):
    """MFI(50). Long-horizon money flow index."""
    n = 50
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + mr)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfiob_50d_base_v102_signal(high, low, closeadj, volume):
    """Fraction of last 50 bars with MFI(14) > 80 (volume OB density)."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return (mfi > 80.0).astype(float).where(~mfi.isna()).rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfislp_30d_base_v103_signal(high, low, closeadj, volume):
    """5-bar diff of MFI(14). MFI rate-of-change."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return mfi.diff(5).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfidsos_80d_base_v104_signal(high, low, closeadj, volume):
    """Days-since-last MFI(14) < 20 (oversold), capped 80."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    cond = (mfi < 20.0).astype(float).where(~mfi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 80.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(80, min_periods=80).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Ultimate Oscillator variants -------------------------------------


def f12os_f12_oscillator_family_uodefault_base_v105_signal(high, low, closeadj):
    """UO(7,14,28) on closeadj. Variation 2 of UO using adjusted close as reference."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    return (100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uoob_50d_base_v106_signal(high, low, closeadj):
    """Fraction of last 50 bars with UO(7,14,28) > 70 (overbought zone)."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    return (uo > 70.0).astype(float).where(~uo.isna()).rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uorng_80d_base_v107_signal(high, low, closeadj):
    """80d (max UO - min UO) excursion range — long-horizon UO span."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    return (uo.rolling(80, min_periods=80).max() - uo.rolling(80, min_periods=80).min()).replace([np.inf, -np.inf], np.nan)


# --- Awesome Oscillator variants ---------------------------------------


def f12os_f12_oscillator_family_aoxsign_60d_base_v108_signal(high, low):
    """Count of Awesome Oscillator zero crossings in last 60 bars."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    sgn = np.sign(ao)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aosig_30d_base_v109_signal(high, low):
    """Awesome Oscillator divided by 80d std of AO. Self-normalized AO."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    sd = ao.rolling(80, min_periods=80).std(ddof=1)
    return (ao / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aoslp_50d_base_v110_signal(high, low):
    """5-bar diff of Awesome Oscillator. AO rate-of-change."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    return ao.diff(5).replace([np.inf, -np.inf], np.nan)


# --- DPO variants ------------------------------------------------------


def f12os_f12_oscillator_family_dpo_30d_base_v111_signal(closeadj):
    """Causal DPO(30): close - SMA(close, 30).shift(N/2+1) on closeadj."""
    n = 30
    return (closeadj - closeadj.rolling(n, min_periods=n).mean().shift(n // 2 + 1)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_dpoabs_50d_base_v112_signal(closeadj):
    """|Causal DPO(50)|. Magnitude of detrended deviation."""
    n = 50
    return (closeadj - closeadj.rolling(n, min_periods=n).mean().shift(n // 2 + 1)).abs().replace([np.inf, -np.inf], np.nan)


# --- StochRSI variants -------------------------------------------------


def f12os_f12_oscillator_family_stochrsi_7d_base_v113_signal(close):
    """Stochastic RSI(7,7). Short-window stoch-RSI. Bounded 0..1."""
    n = 7
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    return ((rsi - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochrsiob_30d_base_v114_signal(closeadj):
    """30d count of StochRSI(14) > 0.8 (extreme overbought stoch-RSI density)."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    srsi = (rsi - lo) / (hi - lo).replace(0.0, np.nan)
    return (srsi > 0.8).astype(float).where(~srsi.isna()).rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# --- Chaikin variants -------------------------------------------------


def f12os_f12_oscillator_family_chaikin_10_30_base_v115_signal(high, low, closeadj, volume):
    """Chaikin Oscillator with slower spans (10,30). Long-horizon A/D divergence."""
    clv = ((closeadj - low) - (high - closeadj)) / (high - low).replace(0.0, np.nan)
    adl = (clv * volume).cumsum()
    return (adl.ewm(span=10, adjust=False, min_periods=10).mean() - adl.ewm(span=30, adjust=False, min_periods=30).mean()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_chaikinxs_60d_base_v116_signal(high, low, close, volume):
    """Count of Chaikin Oscillator(3,10) sign flips in last 60 bars."""
    clv = ((close - low) - (high - close)) / (high - low).replace(0.0, np.nan)
    adl = (clv * volume).cumsum()
    co = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    sgn = np.sign(co)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# --- Klinger variants -------------------------------------------------


def f12os_f12_oscillator_family_klingertanh_30d_base_v117_signal(high, low, closeadj, volume):
    """tanh(Klinger VO / its 60d std). Bounded -1..+1 KVO signal."""
    tp = (high + low + closeadj) / 3.0
    trend = np.sign(tp - tp.shift(1))
    dm = (high - low)
    cm = dm.copy()
    same = (trend == trend.shift(1)) & trend.notna() & trend.shift(1).notna()
    cm = cm.where(~same, cm.shift(1) + dm)
    vf = volume * trend * (2.0 * (dm / cm.replace(0.0, np.nan)) - 1.0) * 100.0
    kvo = vf.ewm(span=34, adjust=False, min_periods=34).mean() - vf.ewm(span=55, adjust=False, min_periods=55).mean()
    sd = kvo.rolling(60, min_periods=60).std(ddof=1)
    return np.tanh(kvo / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- BIAS variants -----------------------------------------------------


def f12os_f12_oscillator_family_bias_20d_base_v118_signal(close):
    """BIAS oscillator(20): (close - SMA(close,20))/SMA * 100."""
    n = 20
    s = close.rolling(n, min_periods=n).mean()
    return (100.0 * (close - s) / s.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_biasxsign_40d_base_v119_signal(closeadj):
    """Count of BIAS(20) sign flips in last 40 bars. Mean-reversion frequency."""
    n = 20
    s = closeadj.rolling(n, min_periods=n).mean()
    b = 100.0 * (closeadj - s) / s.replace(0.0, np.nan)
    sgn = np.sign(b)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(40, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


# --- Cross-oscillator combinations ------------------------------------


def f12os_f12_oscillator_family_rsimficorr_60d_base_v120_signal(high, low, closeadj, volume):
    """60d Pearson correlation between RSI(14) and MFI(14). Convergence/divergence
    of price-only vs volume-weighted momentum oscillators."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return rsi.rolling(60, min_periods=60).corr(mfi).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiccixdcorr_50d_base_v121_signal(high, low, closeadj):
    """50d Pearson correlation between RSI(14) and CCI(20). Momentum-oscillator coherence."""
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
    return rsi.rolling(50, min_periods=50).corr(cci).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscbearcnt_30d_base_v122_signal(high, low, closeadj):
    """Count over 30 bars where ALL of {RSI<30, %K<20, CCI<-100}. Triple-oversold confirm."""
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
    flag = ((rsi < 30.0) & (k < 20.0) & (cci < -100.0)).astype(float).where(~rsi.isna() & ~k.isna() & ~cci.isna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscavgcent_30d_base_v123_signal(high, low, closeadj):
    """Centered composite: average of {RSI-50, %K-50, %R+50, normalized CCI/2}. Bounded ~-50..+50."""
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
    m = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(m, min_periods=m).mean()
    mad = (tp - sma).abs().rolling(m, min_periods=m).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    cci_b = 25.0 * np.tanh(cci / 100.0)
    return ((rsi - 50.0) + (k - 50.0) + (wr + 50.0) + cci_b).replace([np.inf, -np.inf], np.nan) / 4.0


# --- Misc bounded transforms ------------------------------------------


def f12os_f12_oscillator_family_rsicvar_50d_base_v124_signal(closeadj):
    """std(RSI(50), 80) / (|mean(RSI(50)) - 50| + 1). Stability ratio of long RSI."""
    n = 50
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    mu = rsi.rolling(80, min_periods=80).mean()
    sd = rsi.rolling(80, min_periods=80).std(ddof=1)
    return (sd / ((mu - 50.0).abs() + 1.0)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochstd_60d_base_v125_signal(high, low, closeadj):
    """60d std of %K(30). Mid-horizon stochastic local volatility."""
    n = 30
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return k.rolling(60, min_periods=60).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_cciarctan_60d_base_v126_signal(high, low, closeadj):
    """arctan(CCI(60)/200). Long-horizon CCI smoothly bounded."""
    n = 60
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return np.arctan(cci / 200.0).replace([np.inf, -np.inf], np.nan)


# --- Streak / persistence ----------------------------------------------


def f12os_f12_oscillator_family_ccistreaktop_30d_base_v127_signal(high, low, closeadj):
    """Current streak of consecutive bars with CCI(14) > 100, capped 30."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    cond = (cci > 100.0).astype(float).where(~cci.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfistreakob_30d_base_v128_signal(high, low, closeadj, volume):
    """Current streak of consecutive bars with MFI(14) > 80 (volume OB), capped 30."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    cond = (mfi > 80.0).astype(float).where(~mfi.isna())
    def _st(x):
        c = 0.0
        for v in x[::-1]:
            if v > 0.5:
                c += 1.0
            else:
                break
        return c
    return cond.rolling(30, min_periods=30).apply(_st, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiparity_50d_base_v129_signal(closeadj):
    """50d count of bars where sign(RSI(14)-50) == sign(RSI(50)-50). Fast/slow RSI agreement count."""
    n1 = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n1), adjust=False, min_periods=n1).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n1), adjust=False, min_periods=n1).mean()
    rs = au / ad.replace(0.0, np.nan)
    r1 = 100.0 - 100.0 / (1.0 + rs)
    n2 = 50
    au2 = d.clip(lower=0.0).ewm(alpha=1.0 / float(n2), adjust=False, min_periods=n2).mean()
    ad2 = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n2), adjust=False, min_periods=n2).mean()
    rs2 = au2 / ad2.replace(0.0, np.nan)
    r2 = 100.0 - 100.0 / (1.0 + rs2)
    agr = (np.sign(r1 - 50.0) == np.sign(r2 - 50.0)).astype(float).where(~r1.isna() & ~r2.isna())
    return agr.rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_oscobds_60d_base_v130_signal(high, low, closeadj):
    """Days-since-last triple-OB event (RSI>70 AND %K>80 AND CCI>100), cap 60."""
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
    cond = ((rsi > 70.0) & (k > 80.0) & (cci > 100.0)).astype(float).where(~rsi.isna() & ~k.isna() & ~cci.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- TRIX (triple-smoothed oscillator) -------------------------------


def f12os_f12_oscillator_family_trix_15d_base_v131_signal(closeadj):
    """TRIX(15): 1-bar % change of triple-smoothed EMA(log(close), 15). Bounded oscillator."""
    n = 15
    e1 = np.log(closeadj).ewm(span=n, adjust=False, min_periods=n).mean()
    e2 = e1.ewm(span=n, adjust=False, min_periods=n).mean()
    e3 = e2.ewm(span=n, adjust=False, min_periods=n).mean()
    return (10000.0 * e3.diff()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_trix_30d_base_v132_signal(closeadj):
    """TRIX(30): longer triple-smoothing. Slower bounded oscillator."""
    n = 30
    e1 = np.log(closeadj).ewm(span=n, adjust=False, min_periods=n).mean()
    e2 = e1.ewm(span=n, adjust=False, min_periods=n).mean()
    e3 = e2.ewm(span=n, adjust=False, min_periods=n).mean()
    return (10000.0 * e3.diff()).replace([np.inf, -np.inf], np.nan)


# --- Fisher transform / kernels ---------------------------------------


def f12os_f12_oscillator_family_fisherwr_10d_base_v133_signal(high, low, close):
    """Fisher transform of Williams %R(10), normalized to ±0.999. Bounded ±2.6 typical."""
    n = 10
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    wr = -100.0 * (hh - close) / (hh - ll).replace(0.0, np.nan)
    x = (wr + 50.0) / 50.0  # in ~[-1,1]
    x = x.clip(-0.999, 0.999)
    return (0.5 * np.log((1.0 + x) / (1.0 - x))).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_kvarstd_50d_base_v134_signal(high, low, close):
    """Coefficient-of-variation: std(%K(14),50) / |mean(%K(14),50) - 50|.
    Local stability ratio of stochastic. Distinct from raw %K."""
    n = 14
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    k = 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)
    mu = k.rolling(50, min_periods=50).mean()
    sd = k.rolling(50, min_periods=50).std(ddof=1)
    return (sd / ((mu - 50.0).abs() + 1.0)).replace([np.inf, -np.inf], np.nan)


# --- Stochastic-of-RSI on long window ---------------------------------


def f12os_f12_oscillator_family_stochrsi_30d_base_v135_signal(closeadj):
    """StochRSI(30,30) — mid-horizon stoch-RSI on closeadj."""
    n = 30
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    return ((rsi - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_stochrsixs_50d_base_v136_signal(closeadj):
    """Count of StochRSI(14) crossings of 0.5 in last 50 bars. Mid-cross frequency."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lo = rsi.rolling(n, min_periods=n).min()
    hi = rsi.rolling(n, min_periods=n).max()
    srsi = (rsi - lo) / (hi - lo).replace(0.0, np.nan)
    sgn = np.sign(srsi - 0.5)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


# --- Misc novel oscillators / rank features --------------------------


def f12os_f12_oscillator_family_pctrnk_clmid_50d_base_v137_signal(closeadj):
    """|0.5 - 50d percentile rank of closeadj|. Distance from middle — direction-agnostic."""
    return (closeadj.rolling(50, min_periods=50).rank(pct=True) - 0.5).abs().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_pctrnk_hldiff_120d_base_v138_signal(high, low):
    """120d percentile rank of (high - low) — bounded volatility oscillator on bar-range."""
    return (high - low).rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uovariation_30d_base_v139_signal(high, low, closeadj):
    """80d std of UO(7,14,28). Local volatility of the Ultimate Oscillator."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    return uo.rolling(80, min_periods=80).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccixdmu_60d_base_v140_signal(high, low, closeadj):
    """CCI(60) - rolling 30d mean(CCI). Local CCI deviation from short-trail center."""
    n = 60
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return (cci - cci.rolling(30, min_periods=30).mean()).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_ccislpsign_60d_base_v141_signal(high, low, closeadj):
    """sign(CCI(20).diff(10)). Discrete trend of CCI: up / flat / down."""
    n = 20
    tp = (high + low + closeadj) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    cci = (tp - sma) / (0.015 * mad.replace(0.0, np.nan))
    return np.sign(cci.diff(10)).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_klingersign_30d_base_v142_signal(high, low, closeadj, volume):
    """sign(Klinger Volume Oscillator). Discrete KVO directional state."""
    tp = (high + low + closeadj) / 3.0
    trend = np.sign(tp - tp.shift(1))
    dm = (high - low)
    cm = dm.copy()
    same = (trend == trend.shift(1)) & trend.notna() & trend.shift(1).notna()
    cm = cm.where(~same, cm.shift(1) + dm)
    vf = volume * trend * (2.0 * (dm / cm.replace(0.0, np.nan)) - 1.0) * 100.0
    kvo = vf.ewm(span=34, adjust=False, min_periods=34).mean() - vf.ewm(span=55, adjust=False, min_periods=55).mean()
    return np.sign(kvo).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uords_60d_base_v143_signal(high, low, closeadj):
    """Days-since-last UO(7,14,28) < 30 (oversold), capped 60."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    cond = (uo < 30.0).astype(float).where(~uo.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_mfirank_120d_base_v144_signal(high, low, closeadj, volume):
    """120d percentile rank of MFI(14)."""
    n = 14
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return mfi.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_uoxsign_60d_base_v145_signal(high, low, closeadj):
    """Count of UO(7,14,28) midline (50) crossings in last 60 bars."""
    pc = closeadj.shift(1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    bp = closeadj - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    uo = 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0
    sgn = np.sign(uo - 50.0)
    fl = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return fl.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aotop_120d_base_v146_signal(high, low):
    """120d rolling max of Awesome Oscillator. Recent bull-momentum ceiling."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    return ao.rolling(120, min_periods=120).max().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_aobot_120d_base_v147_signal(high, low):
    """120d rolling min of Awesome Oscillator. Recent bear-momentum floor."""
    mp = 0.5 * (high + low)
    ao = mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()
    return ao.rolling(120, min_periods=120).min().replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_pctrnk_tr_60d_base_v148_signal(high, low, close):
    """60d percentile rank of True Range — bounded volatility position (oscillator-of-vol)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsivol_match_40d_base_v149_signal(closeadj, volume):
    """40d Pearson corr between RSI(14) and log(volume). Volume-confirmation of RSI."""
    n = 14
    d = closeadj.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    lv = np.log(volume.replace(0.0, np.nan))
    return rsi.rolling(40, min_periods=40).corr(lv).replace([np.inf, -np.inf], np.nan)


def f12os_f12_oscillator_family_rsiwlder_5d_base_v150_signal(close):
    """RSI(5). Ultra-short Wilder RSI for high-frequency momentum."""
    n = 5
    d = close.diff()
    au = d.clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    ad = (-d).clip(lower=0.0).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f12_oscillator_family_base_076_150_REGISTRY = {
    "f12os_f12_oscillator_family_rsi_21d_base_v076_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsi_21d_base_v076_signal},
    "f12os_f12_oscillator_family_rsi_100d_base_v077_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsi_100d_base_v077_signal},
    "f12os_f12_oscillator_family_rsiema_30d_base_v078_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsiema_30d_base_v078_signal},
    "f12os_f12_oscillator_family_rsiceil_120d_base_v079_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsiceil_120d_base_v079_signal},
    "f12os_f12_oscillator_family_rsispan_80d_base_v080_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsispan_80d_base_v080_signal},
    "f12os_f12_oscillator_family_rsistreakbot_30d_base_v081_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsistreakbot_30d_base_v081_signal},
    "f12os_f12_oscillator_family_rsiextrm_80d_base_v082_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsiextrm_80d_base_v082_signal},
    "f12os_f12_oscillator_family_rsiiqr_60d_base_v083_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsiiqr_60d_base_v083_signal},
    "f12os_f12_oscillator_family_rsigap_30d_base_v084_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsigap_30d_base_v084_signal},
    "f12os_f12_oscillator_family_rsisig_15d_base_v085_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsisig_15d_base_v085_signal},
    "f12os_f12_oscillator_family_stochk_21d_base_v086_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_stochk_21d_base_v086_signal},
    "f12os_f12_oscillator_family_stochkpos_50d_base_v087_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochkpos_50d_base_v087_signal},
    "f12os_f12_oscillator_family_stochds_80d_base_v088_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochds_80d_base_v088_signal},
    "f12os_f12_oscillator_family_stochkmed_120d_base_v089_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochkmed_120d_base_v089_signal},
    "f12os_f12_oscillator_family_stochkdslp_30d_base_v090_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochkdslp_30d_base_v090_signal},
    "f12os_f12_oscillator_family_stochwidemar_100d_base_v091_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochwidemar_100d_base_v091_signal},
    "f12os_f12_oscillator_family_willr_28d_base_v092_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_willr_28d_base_v092_signal},
    "f12os_f12_oscillator_family_willrslp_50d_base_v093_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_willrslp_50d_base_v093_signal},
    "f12os_f12_oscillator_family_willrxhi_50d_base_v094_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_willrxhi_50d_base_v094_signal},
    "f12os_f12_oscillator_family_cci_30d_base_v095_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cci_30d_base_v095_signal},
    "f12os_f12_oscillator_family_ccislope_50d_base_v096_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccislope_50d_base_v096_signal},
    "f12os_f12_oscillator_family_ccipos_60d_base_v097_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccipos_60d_base_v097_signal},
    "f12os_f12_oscillator_family_cciskew_60d_base_v098_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cciskew_60d_base_v098_signal},
    "f12os_f12_oscillator_family_cciosmin_60d_base_v099_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cciosmin_60d_base_v099_signal},
    "f12os_f12_oscillator_family_ccids_60d_base_v100_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccids_60d_base_v100_signal},
    "f12os_f12_oscillator_family_mfi_50d_base_v101_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfi_50d_base_v101_signal},
    "f12os_f12_oscillator_family_mfiob_50d_base_v102_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfiob_50d_base_v102_signal},
    "f12os_f12_oscillator_family_mfislp_30d_base_v103_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfislp_30d_base_v103_signal},
    "f12os_f12_oscillator_family_mfidsos_80d_base_v104_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfidsos_80d_base_v104_signal},
    "f12os_f12_oscillator_family_uodefault_base_v105_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uodefault_base_v105_signal},
    "f12os_f12_oscillator_family_uoob_50d_base_v106_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uoob_50d_base_v106_signal},
    "f12os_f12_oscillator_family_uorng_80d_base_v107_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uorng_80d_base_v107_signal},
    "f12os_f12_oscillator_family_aoxsign_60d_base_v108_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aoxsign_60d_base_v108_signal},
    "f12os_f12_oscillator_family_aosig_30d_base_v109_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aosig_30d_base_v109_signal},
    "f12os_f12_oscillator_family_aoslp_50d_base_v110_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aoslp_50d_base_v110_signal},
    "f12os_f12_oscillator_family_dpo_30d_base_v111_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_dpo_30d_base_v111_signal},
    "f12os_f12_oscillator_family_dpoabs_50d_base_v112_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_dpoabs_50d_base_v112_signal},
    "f12os_f12_oscillator_family_stochrsi_7d_base_v113_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_stochrsi_7d_base_v113_signal},
    "f12os_f12_oscillator_family_stochrsiob_30d_base_v114_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_stochrsiob_30d_base_v114_signal},
    "f12os_f12_oscillator_family_chaikin_10_30_base_v115_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_chaikin_10_30_base_v115_signal},
    "f12os_f12_oscillator_family_chaikinxs_60d_base_v116_signal": {"inputs": ["high", "low", "close", "volume"], "func": f12os_f12_oscillator_family_chaikinxs_60d_base_v116_signal},
    "f12os_f12_oscillator_family_klingertanh_30d_base_v117_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_klingertanh_30d_base_v117_signal},
    "f12os_f12_oscillator_family_bias_20d_base_v118_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_bias_20d_base_v118_signal},
    "f12os_f12_oscillator_family_biasxsign_40d_base_v119_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_biasxsign_40d_base_v119_signal},
    "f12os_f12_oscillator_family_rsimficorr_60d_base_v120_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_rsimficorr_60d_base_v120_signal},
    "f12os_f12_oscillator_family_rsiccixdcorr_50d_base_v121_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_rsiccixdcorr_50d_base_v121_signal},
    "f12os_f12_oscillator_family_oscbearcnt_30d_base_v122_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscbearcnt_30d_base_v122_signal},
    "f12os_f12_oscillator_family_oscavgcent_30d_base_v123_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscavgcent_30d_base_v123_signal},
    "f12os_f12_oscillator_family_rsicvar_50d_base_v124_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsicvar_50d_base_v124_signal},
    "f12os_f12_oscillator_family_stochstd_60d_base_v125_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_stochstd_60d_base_v125_signal},
    "f12os_f12_oscillator_family_cciarctan_60d_base_v126_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_cciarctan_60d_base_v126_signal},
    "f12os_f12_oscillator_family_ccistreaktop_30d_base_v127_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccistreaktop_30d_base_v127_signal},
    "f12os_f12_oscillator_family_mfistreakob_30d_base_v128_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfistreakob_30d_base_v128_signal},
    "f12os_f12_oscillator_family_rsiparity_50d_base_v129_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_rsiparity_50d_base_v129_signal},
    "f12os_f12_oscillator_family_oscobds_60d_base_v130_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_oscobds_60d_base_v130_signal},
    "f12os_f12_oscillator_family_trix_15d_base_v131_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_trix_15d_base_v131_signal},
    "f12os_f12_oscillator_family_trix_30d_base_v132_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_trix_30d_base_v132_signal},
    "f12os_f12_oscillator_family_fisherwr_10d_base_v133_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_fisherwr_10d_base_v133_signal},
    "f12os_f12_oscillator_family_kvarstd_50d_base_v134_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_kvarstd_50d_base_v134_signal},
    "f12os_f12_oscillator_family_stochrsi_30d_base_v135_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_stochrsi_30d_base_v135_signal},
    "f12os_f12_oscillator_family_stochrsixs_50d_base_v136_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_stochrsixs_50d_base_v136_signal},
    "f12os_f12_oscillator_family_pctrnk_clmid_50d_base_v137_signal": {"inputs": ["closeadj"], "func": f12os_f12_oscillator_family_pctrnk_clmid_50d_base_v137_signal},
    "f12os_f12_oscillator_family_pctrnk_hldiff_120d_base_v138_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_pctrnk_hldiff_120d_base_v138_signal},
    "f12os_f12_oscillator_family_uovariation_30d_base_v139_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uovariation_30d_base_v139_signal},
    "f12os_f12_oscillator_family_ccixdmu_60d_base_v140_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccixdmu_60d_base_v140_signal},
    "f12os_f12_oscillator_family_ccislpsign_60d_base_v141_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_ccislpsign_60d_base_v141_signal},
    "f12os_f12_oscillator_family_klingersign_30d_base_v142_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_klingersign_30d_base_v142_signal},
    "f12os_f12_oscillator_family_uords_60d_base_v143_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uords_60d_base_v143_signal},
    "f12os_f12_oscillator_family_mfirank_120d_base_v144_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f12os_f12_oscillator_family_mfirank_120d_base_v144_signal},
    "f12os_f12_oscillator_family_uoxsign_60d_base_v145_signal": {"inputs": ["high", "low", "closeadj"], "func": f12os_f12_oscillator_family_uoxsign_60d_base_v145_signal},
    "f12os_f12_oscillator_family_aotop_120d_base_v146_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aotop_120d_base_v146_signal},
    "f12os_f12_oscillator_family_aobot_120d_base_v147_signal": {"inputs": ["high", "low"], "func": f12os_f12_oscillator_family_aobot_120d_base_v147_signal},
    "f12os_f12_oscillator_family_pctrnk_tr_60d_base_v148_signal": {"inputs": ["high", "low", "close"], "func": f12os_f12_oscillator_family_pctrnk_tr_60d_base_v148_signal},
    "f12os_f12_oscillator_family_rsivol_match_40d_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f12os_f12_oscillator_family_rsivol_match_40d_base_v149_signal},
    "f12os_f12_oscillator_family_rsiwlder_5d_base_v150_signal": {"inputs": ["close"], "func": f12os_f12_oscillator_family_rsiwlder_5d_base_v150_signal},
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
    for name, entry in f12_oscillator_family_base_076_150_REGISTRY.items():
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
