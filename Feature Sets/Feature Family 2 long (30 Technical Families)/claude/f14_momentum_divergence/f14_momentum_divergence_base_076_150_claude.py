"""f14_momentum_divergence base features 076-150.

Second 75 momentum-divergence features. Every feature explicitly compares
PRICE behaviour to MOMENTUM-INDICATOR behaviour (RSI, MACD, ROC, Stoch,
TSI, CMO, MFI, Awesome, Williams %R, PPO). No structural duplicates of
file-1 features.

Window > 21d -> closeadj. NaN policy: only replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# --- Helpers ----------------------------------------------------------------


def _rsi(s: pd.Series, n: int) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    a = 1.0 / float(n)
    au = up.ewm(alpha=a, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=a, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + au / ad.replace(0.0, np.nan))


def _macd(s: pd.Series, fast: int, slow: int) -> pd.Series:
    return s.ewm(span=fast, adjust=False, min_periods=fast).mean() - s.ewm(span=slow, adjust=False, min_periods=slow).mean()


def _roc(s: pd.Series, n: int) -> pd.Series:
    return 100.0 * (s / s.shift(n) - 1.0)


def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)


def _wpr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return -100.0 * (hh - close) / (hh - ll).replace(0.0, np.nan)


def _cmo(s: pd.Series, n: int) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0).rolling(n, min_periods=n).sum()
    dn = (-d).clip(lower=0.0).rolling(n, min_periods=n).sum()
    return 100.0 * (up - dn) / (up + dn).replace(0.0, np.nan)


def _ao(high: pd.Series, low: pd.Series) -> pd.Series:
    mp = (high + low) / 2.0
    return mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()


def _ppo(s: pd.Series, fast: int, slow: int) -> pd.Series:
    ef = s.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = s.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return 100.0 * (ef - es) / es.replace(0.0, np.nan)


def _tsi(s: pd.Series, slow: int, fast: int) -> pd.Series:
    m = s.diff()
    e1 = m.ewm(span=slow, adjust=False, min_periods=slow).mean()
    e2 = e1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    a1 = m.abs().ewm(span=slow, adjust=False, min_periods=slow).mean()
    a2 = a1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    return 100.0 * e2 / a2.replace(0.0, np.nan)


# --- Features 076-150 ------------------------------------------------------


def f14md_f14_momentum_divergence_pslp_minus_rocslp_45d_base_v076_signal(closeadj):
    """Price slope - ROC(20) slope, 45 bars, normalised by close."""
    n = 45
    rc = _roc(closeadj, 20)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (rc - rc.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_minus_ppoSlp_30d_base_v077_signal(closeadj):
    """Price slope - PPO(12,26) slope, 30 bars."""
    n = 30
    pp = _ppo(closeadj, 12, 26)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (pp - pp.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_minus_wprSlp_22d_base_v078_signal(high, low, closeadj):
    """Price slope - Williams %R(14) slope, 22 bars."""
    n = 22
    w = _wpr(high, low, closeadj, 14)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (w - w.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_minus_aoSlp_35d_base_v079_signal(high, low):
    """Mid-price slope - Awesome Oscillator slope, 35 bars (HL only)."""
    n = 35
    a = _ao(high, low)
    mp = (high + low) / 2.0
    pslp = (mp - mp.shift(n)) / mp.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (a - a.shift(n)) / mp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_tsi_20d_base_v080_signal(close):
    """1 if sign(close.diff(20)) disagrees with sign(TSI(25,13).diff(20))."""
    n = 20
    t = _tsi(close, 25, 13)
    sp = np.sign(close.diff(n))
    st = np.sign(t.diff(n))
    return ((sp * st) < 0).astype(float).where(~sp.isna() & ~st.isna()).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_cmo_25d_base_v081_signal(closeadj):
    """Sign disagreement: 25d price change vs CMO(14) change."""
    n = 25
    c = _cmo(closeadj, 14)
    sp = np.sign(closeadj.diff(n))
    sc = np.sign(c.diff(n))
    return ((sp * sc) < 0).astype(float).where(~sp.isna() & ~sc.isna()).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_mfi_18d_base_v082_signal(high, low, close, volume):
    """Sign disagreement: 18d price change vs MFI(14) change."""
    n = 18
    from_volume = _stoch_k  # noqa: F841  (no-op, retains structural reference)
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    dn = tp.diff()
    pos = rmf.where(dn > 0, 0.0).rolling(14, min_periods=14).sum()
    neg = rmf.where(dn < 0, 0.0).rolling(14, min_periods=14).sum()
    mfi = 100.0 - 100.0 / (1.0 + pos / neg.replace(0.0, np.nan))
    sp = np.sign(close.diff(n))
    sm = np.sign(mfi.diff(n))
    return ((sp * sm) < 0).astype(float).where(~sp.isna() & ~sm.isna()).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_roc_30d_base_v083_signal(closeadj):
    """30d corr between log-price and ROC(10)."""
    n = 30
    rc = _roc(closeadj, 10)
    return np.log(closeadj).rolling(n, min_periods=n).corr(rc).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_stoch_45d_base_v084_signal(high, low, closeadj):
    """45d corr between price and Stochastic-K(14)."""
    n = 45
    k = _stoch_k(high, low, closeadj, 14)
    return closeadj.rolling(n, min_periods=n).corr(k).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_wpr_55d_base_v085_signal(high, low, closeadj):
    """55d corr between log-price and Williams %R(14)."""
    n = 55
    w = _wpr(high, low, closeadj, 14)
    return np.log(closeadj).rolling(n, min_periods=n).corr(w).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_ao_70d_base_v086_signal(high, low):
    """70d corr between mid-price and Awesome Oscillator."""
    n = 70
    a = _ao(high, low)
    mp = (high + low) / 2.0
    return mp.rolling(n, min_periods=n).corr(a).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_ppo_60d_base_v087_signal(closeadj):
    """60d corr between log-price and PPO(12,26)."""
    n = 60
    pp = _ppo(closeadj, 12, 26)
    return np.log(closeadj).rolling(n, min_periods=n).corr(pp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_phigh_macd_40d_base_v088_signal(closeadj):
    """Days-since-event count: bars since last 'price 40d-high WITHOUT MACD
    40d-high', up to 80 bars."""
    n = 40
    m = _macd(closeadj, 12, 26)
    phi = closeadj.rolling(n, min_periods=n).max()
    mhi = m.rolling(n, min_periods=n).max()
    ev = ((closeadj >= phi * 0.999) & (m < mhi - mhi.abs().rolling(n, min_periods=n).mean() * 0.1)).astype(float).where(~phi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return float(len(x)) if idx.size == 0 else float(len(x) - 1 - idx[-1])
    return ev.rolling(80, min_periods=80).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_plow_macd_50d_base_v089_signal(closeadj):
    """Bullish: price at 50d-low while MACD above 50d-MACD-low. Continuous gap."""
    n = 50
    m = _macd(closeadj, 12, 26)
    plo = closeadj.rolling(n, min_periods=n).min()
    mlo = m.rolling(n, min_periods=n).min()
    at_low = (closeadj <= plo * 1.001).astype(float).where(~plo.isna())
    return (at_low * (m - mlo)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_phigh_cmo_30d_base_v090_signal(closeadj):
    """Bearish: price at 30d-high while CMO(14) below 30d-CMO-high."""
    n = 30
    c = _cmo(closeadj, 14)
    phi = closeadj.rolling(n, min_periods=n).max()
    chi = c.rolling(n, min_periods=n).max()
    at_high = (closeadj >= phi * 0.999).astype(float).where(~phi.isna())
    return (at_high * (chi - c)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_phigh_tsi_70d_base_v091_signal(closeadj):
    """Bearish: price at 70d-high while TSI(25,13) below 70d-TSI-high."""
    n = 70
    t = _tsi(closeadj, 25, 13)
    phi = closeadj.rolling(n, min_periods=n).max()
    thi = t.rolling(n, min_periods=n).max()
    at_high = (closeadj >= phi * 0.999).astype(float).where(~phi.isna())
    return (at_high * (thi - t)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_dslph_macd_100d_base_v092_signal(closeadj):
    """Days since price-high-without-MACD-high event, looking back 100 bars."""
    n = 100
    m = _macd(closeadj, 12, 26)
    phi = closeadj.rolling(25, min_periods=25).max()
    mhi = m.rolling(25, min_periods=25).max()
    ev = ((closeadj >= phi * 0.999) & (m < mhi)).astype(float).where(~phi.isna() & ~mhi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return float(len(x)) if idx.size == 0 else float(len(x) - 1 - idx[-1])
    return ev.rolling(n, min_periods=n).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_rsi_minus_cmo_40d_base_v093_signal(closeadj):
    """Z-score over 40d of RSI(14) - CMO(14). Two related-but-distinct
    momentum oscillators -> their gap captures divergence between them."""
    n = 40
    r = _rsi(closeadj, 14)
    c = _cmo(closeadj, 14)
    d = r - (c + 100.0) / 2.0
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_macd_minus_ppo_50d_base_v094_signal(closeadj):
    """Rolling Pearson corr (50d) between MACD and PPO -> when they disagree
    (corr low) momentum picture is fractured."""
    n = 50
    m = _macd(closeadj, 12, 26)
    p = _ppo(closeadj, 12, 26)
    return m.rolling(n, min_periods=n).corr(p).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_tsi_minus_rsi_60d_base_v095_signal(closeadj):
    """TSI(25,13) - normalised RSI(14) Z-scored over 60d."""
    n = 60
    t = _tsi(closeadj, 25, 13)
    r = _rsi(closeadj, 14) * 2.0 - 100.0
    d = t - r
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_compxor_macd_50d_base_v096_signal(closeadj):
    """Sum of bars in 50d where sign(price.diff(5)) != sign(MACD.diff(5))."""
    n = 50
    m = _macd(closeadj, 12, 26)
    sp = np.sign(closeadj.diff(5))
    sm = np.sign(m.diff(5))
    flag = ((sp * sm) < 0).astype(float).where(~sp.isna() & ~sm.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_compxor_stoch_30d_base_v097_signal(high, low, close):
    """Number of 5d windows where sign(close.diff(5)) disagrees with sign(Stoch.diff(5)), 30d total."""
    n = 30
    k = _stoch_k(high, low, close, 14)
    sp = np.sign(close.diff(5))
    sk = np.sign(k.diff(5))
    flag = ((sp * sk) < 0).astype(float).where(~sp.isna() & ~sk.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_arctan_macdiv_30d_base_v098_signal(closeadj):
    """arctan(20 * (price-3d-pct - MACD-3d-norm-change)) -> bounded high-freq
    divergence."""
    m = _macd(closeadj, 12, 26) / closeadj
    return np.arctan(20.0 * (closeadj.pct_change(3) - m.diff(3))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_tanh_corr_macd_40d_base_v099_signal(closeadj):
    """tanh(corr(price, MACD) * 2) over 40d."""
    n = 40
    m = _macd(closeadj, 12, 26)
    return np.tanh(2.0 * closeadj.rolling(n, min_periods=n).corr(m)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_sigmoid_rocdiv_40d_base_v100_signal(closeadj):
    """Sigmoid of (price-pct - ROC(10)/100) at 20d horizon -> bounded slope diff."""
    n = 20
    rc = _roc(closeadj, 10) / 100.0
    x = 15.0 * (closeadj.pct_change(n) - rc.diff(n))
    return (1.0 / (1.0 + np.exp(-x)) - 0.5).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_flipcount_macd_60d_base_v101_signal(closeadj):
    """Count of sign-flips in (close.diff - MACD.diff*scale) series over 60d."""
    n = 60
    m = _macd(closeadj, 12, 26)
    scale = closeadj.abs().rolling(20, min_periods=20).mean() / m.abs().rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    d = closeadj.diff() - m.diff() * scale
    s = np.sign(d)
    fl = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return fl.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_cumabs_macd_45d_base_v102_signal(closeadj):
    """Cumulative |price.pct - MACD-normalised-pct| over 45d."""
    n = 45
    m = _macd(closeadj, 12, 26) / closeadj
    d = (closeadj.pct_change() - m.diff()).abs()
    return d.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_convrate_macd_50d_base_v103_signal(closeadj):
    """Convergence: 15d corr - 60d corr of price vs MACD."""
    m = _macd(closeadj, 12, 26)
    c_s = closeadj.rolling(15, min_periods=15).corr(m)
    c_l = closeadj.rolling(60, min_periods=60).corr(m)
    return (c_s - c_l).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_bullintens_macd_60d_base_v104_signal(closeadj):
    """Bullish intensity using MACD: max over 60d of (MACD-MACDlow when price at 20d-low)."""
    n = 60
    m = _macd(closeadj, 12, 26)
    plo = closeadj.rolling(20, min_periods=20).min()
    mlo = m.rolling(20, min_periods=20).min()
    at_low = (closeadj <= plo * 1.001).astype(float).where(~plo.isna())
    return (at_low * (m - mlo)).rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_bearintens_macd_60d_base_v105_signal(closeadj):
    """Bearish intensity using MACD: max over 60d of (MACDhigh-MACD when price at 20d-high)."""
    n = 60
    m = _macd(closeadj, 12, 26)
    phi = closeadj.rolling(20, min_periods=20).max()
    mhi = m.rolling(20, min_periods=20).max()
    at_high = (closeadj >= phi * 0.999).astype(float).where(~phi.isna())
    return (at_high * (mhi - m)).rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_regresid_macd_40d_base_v106_signal(closeadj):
    """Last residual of regressing MACD on log-price over 40d."""
    n = 40
    m = _macd(closeadj, 12, 26)
    lp = np.log(closeadj)
    def _r(idx):
        i = int(idx[-1])
        a = lp.iloc[i - n + 1 : i + 1].values
        b = m.iloc[i - n + 1 : i + 1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(b)):
            return np.nan
        va = ((a - a.mean()) ** 2).sum()
        if va <= 0:
            return np.nan
        beta = ((a - a.mean()) * (b - b.mean())).sum() / va
        alpha = b.mean() - beta * a.mean()
        return float(b[-1] - (alpha + beta * a[-1]))
    idx_s = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    return idx_s.rolling(n, min_periods=n).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_beta_macd_70d_base_v107_signal(closeadj):
    """Beta of MACD on log-price over 70d."""
    n = 70
    m = _macd(closeadj, 12, 26)
    lp = np.log(closeadj)
    cov = lp.rolling(n, min_periods=n).cov(m)
    var = lp.rolling(n, min_periods=n).var(ddof=1)
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_r2_macd_60d_base_v108_signal(closeadj):
    """R^2 of MACD vs price fit over 60d (low -> divergent)."""
    n = 60
    m = _macd(closeadj, 12, 26)
    c = np.log(closeadj).rolling(n, min_periods=n).corr(m)
    return (c * c).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_curv_macd_35d_base_v109_signal(closeadj):
    """Price 2nd diff (normalised) - MACD 2nd diff over 35d."""
    n = 35
    m = _macd(closeadj, 12, 26) / closeadj
    pc = (closeadj - 2 * closeadj.shift(n) + closeadj.shift(2 * n)) / closeadj.shift(n).replace(0.0, np.nan)
    mc = m - 2 * m.shift(n) + m.shift(2 * n)
    return (pc - mc).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_accel_rsi_50d_base_v110_signal(closeadj):
    """Price acceleration - RSI acceleration over 50d."""
    n = 50
    r = _rsi(closeadj, 14)
    pa = closeadj.pct_change(n) - closeadj.pct_change(n).shift(n)
    ra = (r.diff(n) - r.diff(n).shift(n)) / 100.0
    return (pa - ra).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_lag_macd_50d_base_v111_signal(closeadj):
    """Best-lag (in -3..3) at which return and MACD-change maximally correlate, 50d."""
    n = 50
    m = _macd(closeadj, 12, 26)
    ret = closeadj.pct_change()
    md = m.diff()
    def _bl(idx):
        i = int(idx[-1])
        if i < 2 * n:
            return np.nan
        a = ret.iloc[i - n + 1 : i + 1].values
        best = 0.0; bl = 0
        for L in range(-3, 4):
            b = md.shift(L).iloc[i - n + 1 : i + 1].values
            if np.any(~np.isfinite(a)) or np.any(~np.isfinite(b)):
                continue
            sa = a.std(); sb = b.std()
            if sa <= 0 or sb <= 0:
                continue
            c = float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
            if abs(c) > abs(best):
                best = c; bl = L
        return float(bl)
    idx_s = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    return idx_s.rolling(n, min_periods=n).apply(_bl, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_veldiff_cmo_12d_base_v112_signal(close):
    """close.pct_change(12) - CMO(14)/100 change(12). Velocity diff."""
    n = 12
    c = _cmo(close, 14)
    return (close.pct_change(n) - c.diff(n) / 100.0).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_veldiff_tsi_30d_base_v113_signal(closeadj):
    """close.pct_change(30) - TSI(25,13).diff(30)/100."""
    n = 30
    t = _tsi(closeadj, 25, 13)
    return (closeadj.pct_change(n) - t.diff(n) / 100.0).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_veldiff_wpr_15d_base_v114_signal(high, low, close):
    """Williams%R(14) Z-score (40d) AT TIMES OF PRICE 15d-HIGH minus same at
    PRICE 15d-LOW -> asymmetric Williams%R divergence profile."""
    n = 15
    w = _wpr(high, low, close, 14)
    mu = w.rolling(40, min_periods=40).mean(); sd = w.rolling(40, min_periods=40).std(ddof=1)
    zw = (w - mu) / sd.replace(0.0, np.nan)
    phi = close.rolling(n, min_periods=n).max(); plo = close.rolling(n, min_periods=n).min()
    at_high = (close >= phi * 0.999).astype(float).where(~phi.isna())
    at_low = (close <= plo * 1.001).astype(float).where(~plo.isna())
    return (at_high * zw - at_low * zw).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_zslp_macd_50d_base_v115_signal(closeadj):
    """Z-score (50d) of 15d (price-pct - normalised-MACD slope)."""
    n = 50
    m = _macd(closeadj, 12, 26) / closeadj
    d = closeadj.pct_change(15) - m.diff(15)
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corrrank_macd_120d_base_v116_signal(closeadj):
    """Percentile rank (120d) of 30d corr(close, MACD)."""
    m = _macd(closeadj, 12, 26)
    c = closeadj.rolling(30, min_periods=30).corr(m)
    return c.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pjerk_mjerk_40d_base_v117_signal(closeadj):
    """Price 3rd-diff minus MACD 3rd-diff over 40d."""
    n = 40
    m = _macd(closeadj, 12, 26) / closeadj
    pj = closeadj.pct_change(n).diff(n).diff(n)
    mj = m.diff(n).diff(n).diff(n)
    return (pj - mj).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signdir_macd_30d_base_v118_signal(closeadj):
    """sign(price.diff(30)) - sign(MACD.diff(30)) -> values in {-2..2}."""
    n = 30
    m = _macd(closeadj, 12, 26)
    return (np.sign(closeadj.diff(n)) - np.sign(m.diff(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_mad_macd_45d_base_v119_signal(closeadj):
    """Median of |5d-price-pct - normalised 5d MACD-pct| over 45d -> robust
    median divergence (structurally distinct from sum/mean variants)."""
    n = 45
    m = _macd(closeadj, 12, 26) / closeadj
    d = (closeadj.pct_change(5) - m.diff(5)).abs()
    return d.rolling(n, min_periods=n).median().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_hfdiv_macd_5d_base_v120_signal(close):
    """5d price-return - 5d normalised MACD change."""
    n = 5
    m = _macd(close, 12, 26) / close
    return (np.log(close / close.shift(n)) - m.diff(n)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_msd_macd_60d_base_v121_signal(closeadj):
    """MSE between Z-log-price and Z-MACD over 60d."""
    n = 60
    lp = np.log(closeadj)
    m = _macd(closeadj, 12, 26)
    zp = (lp - lp.rolling(n, min_periods=n).mean()) / lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm = (m - m.rolling(n, min_periods=n).mean()) / m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    return ((zp - zm) ** 2).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_hidden_macd_40d_base_v122_signal(closeadj):
    """Hidden bullish divergence: price higher-low while MACD lower-low. Mean
    over 40d of binary flag."""
    n = 40
    m = _macd(closeadj, 12, 26)
    plo_now = closeadj.rolling(20, min_periods=20).min()
    plo_then = plo_now.shift(20)
    mlo_now = m.rolling(20, min_periods=20).min()
    mlo_then = mlo_now.shift(20)
    cond = ((plo_now > plo_then) & (mlo_now < mlo_then)).astype(float).where(~plo_then.isna() & ~mlo_then.isna())
    return cond.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_slpratio_macd_45d_base_v123_signal(closeadj):
    """arctan( price-slope / normalised-MACD-slope ) over 45d."""
    n = 45
    m = _macd(closeadj, 12, 26) / closeadj
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan)
    mslp = m - m.shift(n)
    return np.arctan(pslp / mslp.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pmstoch_avg_50d_base_v124_signal(high, low, closeadj):
    """Avg over 50d of (5d-price-return - Stoch-K(14)/100 change(5))."""
    n = 50
    k = _stoch_k(high, low, closeadj, 14)
    d = closeadj.pct_change(5) - k.diff(5) / 100.0
    return d.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_obvmom_60d_base_v125_signal(close, volume):
    """60d Z-difference between volume-momentum flow and price-momentum flow."""
    n = 60
    sp = np.sign(close.diff())
    obv = (volume * sp).rolling(n, min_periods=n).sum()
    pflow = (close.diff().abs() * sp).rolling(n, min_periods=n).sum()
    zo = (obv - obv.rolling(120, min_periods=120).mean()) / obv.rolling(120, min_periods=120).std(ddof=1).replace(0.0, np.nan)
    zp = (pflow - pflow.rolling(120, min_periods=120).mean()) / pflow.rolling(120, min_periods=120).std(ddof=1).replace(0.0, np.nan)
    return (zp - zo).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_adapt_macd_80d_base_v126_signal(closeadj):
    """Count over 80d where |price-pct(5) - MACD-norm-diff(5)| > 100d median."""
    m = _macd(closeadj, 12, 26) / closeadj
    d = (closeadj.pct_change(5) - m.diff(5)).abs()
    med = d.rolling(150, min_periods=150).median()
    fl = (d > med).astype(float).where(~med.isna())
    return fl.rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_persist_macd_60d_base_v127_signal(closeadj):
    """Mean over 60d of sign(price-pct(5) - MACD-norm-diff(5))."""
    n = 60
    m = _macd(closeadj, 12, 26) / closeadj
    s = np.sign(closeadj.pct_change(5) - m.diff(5))
    return s.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_skew_macd_80d_base_v128_signal(closeadj):
    """Skew over 80d of (price.pct - normalised-MACD-pct) series."""
    n = 80
    m = _macd(closeadj, 12, 26) / closeadj
    d = closeadj.pct_change() - m.diff()
    return d.rolling(n, min_periods=n).skew().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_kurt_div_rsi_80d_base_v129_signal(closeadj):
    """Kurtosis over 80d of daily (price-pct - RSI/100 diff)."""
    n = 80
    r = _rsi(closeadj, 14)
    d = closeadj.pct_change() - r.diff() / 100.0
    return d.rolling(n, min_periods=n).kurt().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_acfr1_div_60d_base_v130_signal(closeadj):
    """Lag-1 autocorrelation of (price-pct - RSI/100 diff) over 60d."""
    n = 60
    r = _rsi(closeadj, 14)
    d = closeadj.pct_change() - r.diff() / 100.0
    return d.rolling(n, min_periods=n).corr(d.shift(1)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_atrnorm_pslp_40d_base_v131_signal(high, low, closeadj):
    """(price-pct(40)) - (RSI(14).diff(40)/100), then divided by ATR/close to
    volatility-normalise the divergence."""
    n = 40
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(n, min_periods=n).mean() / closeadj
    r = _rsi(closeadj, 14)
    d = closeadj.pct_change(n) - r.diff(n) / 100.0
    return (d / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_argextr_rsi_25d_base_v132_signal(closeadj):
    """Distance in bars between argmax(price) and argmax(RSI) over 25d window.
    Nonzero = the two highs occur on different days -> classic divergence."""
    n = 25
    r = _rsi(closeadj, 14)
    def _arg(arr):
        return float(np.argmax(arr))
    pa = closeadj.rolling(n, min_periods=n).apply(_arg, raw=True)
    ra = r.rolling(n, min_periods=n).apply(_arg, raw=True)
    return (pa - ra).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_argextr_macd_45d_base_v133_signal(closeadj):
    """argmin(price) - argmin(MACD) over 45d (timing of lows divergence)."""
    n = 45
    m = _macd(closeadj, 12, 26)
    def _arg(arr):
        return float(np.argmin(arr))
    pa = closeadj.rolling(n, min_periods=n).apply(_arg, raw=True)
    ma = m.rolling(n, min_periods=n).apply(_arg, raw=True)
    return (pa - ma).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pctile_div_rsi_60d_base_v134_signal(closeadj):
    """Percentile rank of price within 60d MINUS percentile rank of RSI(14)
    within 60d. Positive -> price relatively higher than RSI's relative level."""
    n = 60
    r = _rsi(closeadj, 14)
    pp = closeadj.rolling(n, min_periods=n).rank(pct=True)
    rp = r.rolling(n, min_periods=n).rank(pct=True)
    return (pp - rp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pctile_div_macd_80d_base_v135_signal(closeadj):
    """rank(price,80d) - rank(MACD,80d)."""
    n = 80
    m = _macd(closeadj, 12, 26)
    pp = closeadj.rolling(n, min_periods=n).rank(pct=True)
    mp = m.rolling(n, min_periods=n).rank(pct=True)
    return (pp - mp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_zspread_rsi_45d_base_v136_signal(closeadj):
    """Z-score(45d) of log-price MINUS Z-score(45d) of RSI(14). The Z-spread
    captures how far apart the two have moved relative to their typical scale."""
    n = 45
    lp = np.log(closeadj)
    r = _rsi(closeadj, 14)
    zp = (lp - lp.rolling(n, min_periods=n).mean()) / lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zr = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    return (zp - zr).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_zspread_macd_70d_base_v137_signal(closeadj):
    """Z-score(70d) of log-price MINUS Z-score(70d) of MACD."""
    n = 70
    lp = np.log(closeadj)
    m = _macd(closeadj, 12, 26)
    zp = (lp - lp.rolling(n, min_periods=n).mean()) / lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm = (m - m.rolling(n, min_periods=n).mean()) / m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    return (zp - zm).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_volprice_rsi_50d_base_v138_signal(close, volume):
    """50d corr between volume-weighted log-return and RSI(14) change. Captures
    whether volume agrees with price-momentum vs RSI-momentum direction."""
    n = 50
    vwret = np.log(close / close.shift(1)) * np.log1p(volume)
    r = _rsi(close, 14).diff()
    return vwret.rolling(n, min_periods=n).corr(r).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_oscslp_diff_25d_base_v139_signal(closeadj):
    """RSI(14) 25d slope MINUS CMO(14) 25d slope -> divergence between two
    momentum oscillators, both derived from price."""
    n = 25
    r = _rsi(closeadj, 14)
    c = _cmo(closeadj, 14)
    return (r.diff(n) - c.diff(n)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_oscslp_diff_long_60d_base_v140_signal(closeadj):
    """MACD 60d-slope MINUS PPO(12,26) 60d-slope*scale -> long-horizon
    discrepancy between unscaled and percentage MACD."""
    n = 60
    m = _macd(closeadj, 12, 26)
    p = _ppo(closeadj, 12, 26)
    scale = m.abs().rolling(60, min_periods=60).mean() / p.abs().rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    return (m.diff(n) - p.diff(n) * scale).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_intrabar_diff_5d_base_v141_signal(high, low, close, open):
    """Intra-bar momentum disagreement: (close - open) - (high - low)/2 sign
    cumulative count over 5d window where this disagrees with daily close.diff."""
    n = 5
    bar_mom = (close - open) / (high - low).replace(0.0, np.nan)
    s1 = np.sign(close.diff())
    s2 = np.sign(bar_mom)
    flag = ((s1 * s2) < 0).astype(float).where(~s1.isna() & ~s2.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_runrocdiff_40d_base_v142_signal(closeadj):
    """Cumulative running sign of (ROC(10) - ROC(20)) reset every 40d when
    sum exceeds 5 -> tracks regime of short vs long momentum divergence."""
    rc1 = _roc(closeadj, 10)
    rc2 = _roc(closeadj, 20)
    s = np.sign(rc1 - rc2)
    csum = s.rolling(40, min_periods=40).sum()
    return csum.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pricerocstd_40d_base_v143_signal(closeadj):
    """40d std of (log-price - ROC(10)*scale) -> structural divergence volatility."""
    n = 40
    rc = _roc(closeadj, 10)
    lp = np.log(closeadj) * 100.0
    d = lp - rc
    return d.rolling(n, min_periods=n).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_topqdiv_macd_60d_base_v144_signal(closeadj):
    """Mean of top-quartile |price-pct(5) - MACD-norm-pct(5)| over 60d.
    Captures tail-divergence magnitude."""
    n = 60
    m = _macd(closeadj, 12, 26) / closeadj
    d = (closeadj.pct_change(5) - m.diff(5)).abs()
    q = d.rolling(n, min_periods=n).quantile(0.75)
    return q.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_pcurv_rsi_50d_base_v145_signal(closeadj):
    """50d corr between price-curvature (2nd diff over 5d) and RSI-curvature."""
    n = 50
    r = _rsi(closeadj, 14)
    pc = closeadj - 2 * closeadj.shift(5) + closeadj.shift(10)
    rc = r - 2 * r.shift(5) + r.shift(10)
    return pc.rolling(n, min_periods=n).corr(rc).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_lag2_pr_rsi_55d_base_v146_signal(closeadj):
    """corr(price, RSI.shift(2)) over 55d. Captures RSI-leads-price coherence."""
    n = 55
    r = _rsi(closeadj, 14)
    return closeadj.rolling(n, min_periods=n).corr(r.shift(2)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_lag_neg2_pr_macd_45d_base_v147_signal(closeadj):
    """corr(price.shift(2), MACD) over 45d -> price-leads-MACD coherence."""
    n = 45
    m = _macd(closeadj, 12, 26)
    return closeadj.shift(2).rolling(n, min_periods=n).corr(m).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_zwedge_rsi_macd_60d_base_v148_signal(closeadj):
    """Wedge: Z(RSI,60) - Z(MACD,60). Two momentum oscillators on a single
    Z-scale -> their gap is cross-indicator divergence."""
    n = 60
    r = _rsi(closeadj, 14)
    m = _macd(closeadj, 12, 26)
    zr = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm = (m - m.rolling(n, min_periods=n).mean()) / m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    return (zr - zm).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_emadiv_rsi_45d_base_v149_signal(closeadj):
    """EMA(20) of (price.pct - RSI.diff/100) -> smoothed running divergence,
    structurally different from rolling-sum cumulative versions."""
    r = _rsi(closeadj, 14)
    d = closeadj.pct_change() - r.diff() / 100.0
    return d.ewm(span=20, adjust=False, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_atrnorm_macd_60d_base_v150_signal(high, low, closeadj):
    """ATR-normalised price-vs-MACD slope diff (60d). Captures unit-free
    divergence after stripping volatility regime."""
    n = 60
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(n, min_periods=n).mean() / closeadj
    m = _macd(closeadj, 12, 26) / closeadj
    d = closeadj.pct_change(n) - m.diff(n)
    return (d / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f14_momentum_divergence_base_076_150_REGISTRY = dict([
    _e(f14md_f14_momentum_divergence_pslp_minus_rocslp_45d_base_v076_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_ppoSlp_30d_base_v077_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_wprSlp_22d_base_v078_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_aoSlp_35d_base_v079_signal, "high", "low"),
    _e(f14md_f14_momentum_divergence_signxor_tsi_20d_base_v080_signal, "close"),
    _e(f14md_f14_momentum_divergence_signxor_cmo_25d_base_v081_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signxor_mfi_18d_base_v082_signal, "high", "low", "close", "volume"),
    _e(f14md_f14_momentum_divergence_corr_roc_30d_base_v083_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_stoch_45d_base_v084_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_wpr_55d_base_v085_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_ao_70d_base_v086_signal, "high", "low"),
    _e(f14md_f14_momentum_divergence_corr_ppo_60d_base_v087_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_macd_40d_base_v088_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_plow_macd_50d_base_v089_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_cmo_30d_base_v090_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_tsi_70d_base_v091_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_dslph_macd_100d_base_v092_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_rsi_minus_cmo_40d_base_v093_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_macd_minus_ppo_50d_base_v094_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_tsi_minus_rsi_60d_base_v095_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_macd_50d_base_v096_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_stoch_30d_base_v097_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_arctan_macdiv_30d_base_v098_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_tanh_corr_macd_40d_base_v099_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_sigmoid_rocdiv_40d_base_v100_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_flipcount_macd_60d_base_v101_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_cumabs_macd_45d_base_v102_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_convrate_macd_50d_base_v103_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bullintens_macd_60d_base_v104_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bearintens_macd_60d_base_v105_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_regresid_macd_40d_base_v106_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_beta_macd_70d_base_v107_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_r2_macd_60d_base_v108_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_curv_macd_35d_base_v109_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_accel_rsi_50d_base_v110_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag_macd_50d_base_v111_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_veldiff_cmo_12d_base_v112_signal, "close"),
    _e(f14md_f14_momentum_divergence_veldiff_tsi_30d_base_v113_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_veldiff_wpr_15d_base_v114_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_zslp_macd_50d_base_v115_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corrrank_macd_120d_base_v116_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pjerk_mjerk_40d_base_v117_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signdir_macd_30d_base_v118_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_mad_macd_45d_base_v119_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hfdiv_macd_5d_base_v120_signal, "close"),
    _e(f14md_f14_momentum_divergence_msd_macd_60d_base_v121_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hidden_macd_40d_base_v122_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_slpratio_macd_45d_base_v123_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pmstoch_avg_50d_base_v124_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_obvmom_60d_base_v125_signal, "close", "volume"),
    _e(f14md_f14_momentum_divergence_adapt_macd_80d_base_v126_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_persist_macd_60d_base_v127_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_skew_macd_80d_base_v128_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_kurt_div_rsi_80d_base_v129_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_acfr1_div_60d_base_v130_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_atrnorm_pslp_40d_base_v131_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_argextr_rsi_25d_base_v132_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_argextr_macd_45d_base_v133_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pctile_div_rsi_60d_base_v134_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pctile_div_macd_80d_base_v135_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zspread_rsi_45d_base_v136_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zspread_macd_70d_base_v137_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_volprice_rsi_50d_base_v138_signal, "close", "volume"),
    _e(f14md_f14_momentum_divergence_oscslp_diff_25d_base_v139_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_oscslp_diff_long_60d_base_v140_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_intrabar_diff_5d_base_v141_signal, "high", "low", "close", "open"),
    _e(f14md_f14_momentum_divergence_runrocdiff_40d_base_v142_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pricerocstd_40d_base_v143_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_topqdiv_macd_60d_base_v144_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_pcurv_rsi_50d_base_v145_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag2_pr_rsi_55d_base_v146_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag_neg2_pr_macd_45d_base_v147_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zwedge_rsi_macd_60d_base_v148_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_emadiv_rsi_45d_base_v149_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_atrnorm_macd_60d_base_v150_signal, "high", "low", "closeadj"),
])


# ---------------------------------------------------------------------------
# Self-test (copied verbatim pattern)
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
    for name, entry in f14_momentum_divergence_base_076_150_REGISTRY.items():
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
