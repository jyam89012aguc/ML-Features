"""f14_momentum_divergence base features 001-075.

Domain: PRICE vs MOMENTUM-INDICATOR divergence. Every feature compares
price slope/peak/trough/sign/correlation to the corresponding behaviour
of a classic momentum oscillator (RSI, MACD, ROC, Stochastic, MFI, TSI,
CMO, momentum). A bullish divergence occurs when price prints a lower
low but the oscillator does not; bearish when price prints a higher
high but the oscillator does not. Continuous magnitudes, sign tests,
correlations, regressions, peak/trough mismatches and asymmetric scores
are all included.

Window > 21d -> closeadj. Window <= 21d -> close. No fillna(<value>).
Only replace([inf,-inf], nan) at function return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Momentum-indicator helpers. Each base feature spells its formula inline,
# but helpers compute the underlying oscillator inputs.
# ---------------------------------------------------------------------------


def _rsi(s: pd.Series, n: int) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    a = 1.0 / float(n)
    au = up.ewm(alpha=a, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=a, adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0.0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _macd(s: pd.Series, fast: int, slow: int) -> pd.Series:
    ef = s.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = s.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return ef - es


def _roc(s: pd.Series, n: int) -> pd.Series:
    return 100.0 * (s / s.shift(n) - 1.0)


def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    ll = low.rolling(n, min_periods=n).min()
    hh = high.rolling(n, min_periods=n).max()
    return 100.0 * (close - ll) / (hh - ll).replace(0.0, np.nan)


def _cmo(s: pd.Series, n: int) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0).rolling(n, min_periods=n).sum()
    dn = (-d).clip(lower=0.0).rolling(n, min_periods=n).sum()
    return 100.0 * (up - dn) / (up + dn).replace(0.0, np.nan)


def _mfi(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, n: int) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    dn = tp.diff()
    pos = rmf.where(dn > 0, 0.0).rolling(n, min_periods=n).sum()
    neg = rmf.where(dn < 0, 0.0).rolling(n, min_periods=n).sum()
    return 100.0 - 100.0 / (1.0 + pos / neg.replace(0.0, np.nan))


def _tsi(s: pd.Series, slow: int, fast: int) -> pd.Series:
    m = s.diff()
    e1 = m.ewm(span=slow, adjust=False, min_periods=slow).mean()
    e2 = e1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    a1 = m.abs().ewm(span=slow, adjust=False, min_periods=slow).mean()
    a2 = a1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    return 100.0 * e2 / a2.replace(0.0, np.nan)


def _zsc(s: pd.Series, n: int) -> pd.Series:
    mu = s.rolling(n, min_periods=n).mean()
    sd = s.rolling(n, min_periods=n).std(ddof=1)
    return (s - mu) / sd.replace(0.0, np.nan)


# ---------------------------------------------------------------------------
# Features 001-075. Every function references both PRICE and an oscillator.
# ---------------------------------------------------------------------------


# --- Slope-difference family (price slope minus oscillator slope) -----------


def f14md_f14_momentum_divergence_pslp_rsi_14d_base_v001_signal(close):
    """Price slope minus RSI(14) slope over 14 bars. Bearish divergence > 0
    when price rising but RSI lagging."""
    n = 14
    r = _rsi(close, n)
    pslp = (close - close.shift(n)) / close.shift(n).replace(0.0, np.nan) * 100.0
    rslp = r - r.shift(n)
    return (pslp - rslp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_rsi_30d_base_v002_signal(closeadj):
    """Price slope minus RSI(14) slope over 30 bars on closeadj."""
    n = 30
    r = _rsi(closeadj, 14)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    rslp = r - r.shift(n)
    return (pslp - rslp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_macd_20d_base_v003_signal(close):
    """Price log-return minus normalized MACD(12,26) slope, window 20."""
    n = 20
    m = _macd(close, 12, 26) / close
    pslp = np.log(close / close.shift(n))
    mslp = m - m.shift(n)
    return (pslp - mslp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_roc_25d_base_v004_signal(closeadj):
    """Diff between scaled price slope and ROC(10) slope, 25 bars."""
    n = 25
    r10 = _roc(closeadj, 10)
    pslp = _roc(closeadj, n)
    rslp = r10 - r10.shift(n)
    return (pslp - rslp).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_stoch_15d_base_v005_signal(high, low, close):
    """Price slope minus Stochastic-K(14) slope over 15d."""
    n = 15
    k = _stoch_k(high, low, close, 14)
    pslp = (close - close.shift(n)) / close.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (k - k.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_cmo_30d_base_v006_signal(closeadj):
    """Price slope minus CMO(14) slope over 30d on closeadj."""
    n = 30
    c = _cmo(closeadj, 14)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (c - c.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_tsi_40d_base_v007_signal(closeadj):
    """Price slope minus TSI(25,13) slope over 40d."""
    n = 40
    t = _tsi(closeadj, 25, 13)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (t - t.shift(n))).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_pslp_mfi_18d_base_v008_signal(high, low, close, volume):
    """Price slope minus MFI(14) slope over 18d. Uses OHLCV."""
    n = 18
    m = _mfi(high, low, close, volume, 14)
    pslp = (close - close.shift(n)) / close.shift(n).replace(0.0, np.nan) * 100.0
    return (pslp - (m - m.shift(n))).replace([np.inf, -np.inf], np.nan)


# --- Sign-disagreement / XOR family (binary divergence flag) ---------------


def f14md_f14_momentum_divergence_signxor_rsi_10d_base_v009_signal(close):
    """Sign(price.diff(10)) XOR sign(RSI(14).diff(10)). 1 = disagree."""
    n = 10
    r = _rsi(close, 14)
    sp = np.sign(close.diff(n))
    sr = np.sign(r.diff(n))
    flag = (sp * sr < 0).astype(float).where(~sp.isna() & ~sr.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_macd_15d_base_v010_signal(close):
    """Sign(price.diff(15)) XOR sign(MACD.diff(15))."""
    n = 15
    m = _macd(close, 12, 26)
    sp = np.sign(close.diff(n))
    sm = np.sign(m.diff(n))
    flag = (sp * sm < 0).astype(float).where(~sp.isna() & ~sm.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_roc_30d_base_v011_signal(closeadj):
    """Sign(price.diff(30)) XOR sign(ROC(10).diff(30))."""
    n = 30
    r = _roc(closeadj, 10)
    sp = np.sign(closeadj.diff(n))
    sr = np.sign(r.diff(n))
    flag = (sp * sr < 0).astype(float).where(~sp.isna() & ~sr.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_signxor_stoch_8d_base_v012_signal(high, low, close):
    """Sign of 8d price change XOR sign of 8d Stochastic-K(14) change."""
    n = 8
    k = _stoch_k(high, low, close, 14)
    sp = np.sign(close.diff(n))
    sk = np.sign(k.diff(n))
    flag = (sp * sk < 0).astype(float).where(~sp.isna() & ~sk.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


# --- Correlation between price and indicator (negative = divergence) -------


def f14md_f14_momentum_divergence_corr_rsi_20d_base_v013_signal(close):
    """20-bar rolling corr between close and RSI(14). Negative -> divergent."""
    n = 20
    r = _rsi(close, 14)
    return close.rolling(n, min_periods=n).corr(r).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_rsi_60d_base_v014_signal(closeadj):
    """60-bar corr between closeadj and RSI(14)."""
    n = 60
    r = _rsi(closeadj, 14)
    return closeadj.rolling(n, min_periods=n).corr(r).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_macd_40d_base_v015_signal(closeadj):
    """40-bar corr between price and MACD(12,26)."""
    n = 40
    m = _macd(closeadj, 12, 26)
    return closeadj.rolling(n, min_periods=n).corr(m).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_mom_30d_base_v016_signal(closeadj):
    """30-bar corr between price and close.diff (raw momentum)."""
    n = 30
    mom = closeadj.diff()
    return closeadj.rolling(n, min_periods=n).corr(mom).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_tsi_50d_base_v017_signal(closeadj):
    """50-bar corr between log-price and TSI(25,13)."""
    n = 50
    lp = np.log(closeadj)
    t = _tsi(closeadj, 25, 13)
    return lp.rolling(n, min_periods=n).corr(t).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_corr_cmo_45d_base_v018_signal(closeadj):
    """45-bar corr between price log-return and CMO(20)."""
    n = 45
    ret = np.log(closeadj / closeadj.shift(1))
    c = _cmo(closeadj, 20)
    return ret.rolling(n, min_periods=n).corr(c).replace([np.inf, -np.inf], np.nan)


# --- Peak/trough divergence: price-high without indicator-high -------------


def f14md_f14_momentum_divergence_phigh_rsi_low_20d_base_v019_signal(close):
    """1 if price is at 20d-high but RSI(14) is below its own 20d-high
    by more than 5 pts -> bearish divergence flag (continuous magnitude)."""
    n = 20
    r = _rsi(close, 14)
    phi = close.rolling(n, min_periods=n).max()
    rhi = r.rolling(n, min_periods=n).max()
    at_high = (close >= phi * 0.999).astype(float).where(~phi.isna())
    rsi_gap = rhi - r
    return (at_high * rsi_gap).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_plow_rsi_high_30d_base_v020_signal(closeadj):
    """Bullish divergence magnitude: 1 if price at 30d-low while RSI(14)
    is above its own 30d-low by some gap."""
    n = 30
    r = _rsi(closeadj, 14)
    plo = closeadj.rolling(n, min_periods=n).min()
    rlo = r.rolling(n, min_periods=n).min()
    at_low = (closeadj <= plo * 1.001).astype(float).where(~plo.isna())
    rsi_gap = r - rlo
    return (at_low * rsi_gap).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_phigh_macd_low_40d_base_v021_signal(closeadj):
    """Bearish: price at 40d max, MACD(12,26) below its 40d max."""
    n = 40
    m = _macd(closeadj, 12, 26)
    phi = closeadj.rolling(n, min_periods=n).max()
    mhi = m.rolling(n, min_periods=n).max()
    at_high = (closeadj >= phi * 0.999).astype(float).where(~phi.isna())
    gap = (mhi - m) / m.abs().rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return (at_high * gap).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_phigh_stoch_low_15d_base_v022_signal(high, low, close):
    """Bearish: price at 15d max, Stochastic-K(14) below its 15d max."""
    n = 15
    k = _stoch_k(high, low, close, 14)
    phi = close.rolling(n, min_periods=n).max()
    khi = k.rolling(n, min_periods=n).max()
    at_high = (close >= phi * 0.999).astype(float).where(~phi.isna())
    return (at_high * (khi - k)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_plow_mfi_high_25d_base_v023_signal(high, low, close, volume):
    """Bullish: price at 25d min, MFI(14) above its 25d min."""
    n = 25
    m = _mfi(high, low, close, volume, 14)
    plo = close.rolling(n, min_periods=n).min()
    mlo = m.rolling(n, min_periods=n).min()
    at_low = (close <= plo * 1.001).astype(float).where(~plo.isna())
    return (at_low * (m - mlo)).replace([np.inf, -np.inf], np.nan)


# --- Days-since-last divergence event ---------------------------------------


def f14md_f14_momentum_divergence_dslph_rsi_60d_base_v024_signal(closeadj):
    """Days since last price-high-without-RSI(14)-high event, 60d window."""
    n = 60
    r = _rsi(closeadj, 14)
    phi = closeadj.rolling(n, min_periods=n).max()
    rhi = r.rolling(n, min_periods=n).max()
    event = ((closeadj >= phi * 0.999) & (r < rhi - 5.0)).astype(float).where(~phi.isna() & ~rhi.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return event.rolling(n, min_periods=n).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_dsplh_rsi_80d_base_v025_signal(closeadj):
    """Days since last price-low-without-RSI(14)-low event, 80d window."""
    n = 80
    r = _rsi(closeadj, 14)
    plo = closeadj.rolling(n, min_periods=n).min()
    rlo = r.rolling(n, min_periods=n).min()
    event = ((closeadj <= plo * 1.001) & (r > rlo + 5.0)).astype(float).where(~plo.isna() & ~rlo.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return event.rolling(n, min_periods=n).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Cross-indicator divergence (oscillator vs oscillator) ------------------


def f14md_f14_momentum_divergence_rsi_minus_mfi_30d_base_v026_signal(high, low, close, volume):
    """RSI(14) - MFI(14) Z-score over 30d. Captures volume-vs-price-momentum disagreement."""
    n = 30
    r = _rsi(close, 14)
    m = _mfi(high, low, close, volume, 14)
    d = r - m
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_rsi_minus_stoch_40d_base_v027_signal(high, low, closeadj):
    """RSI(14) - Stochastic-K(14) Z-score over 40d. Two momentum measures of price."""
    n = 40
    r = _rsi(closeadj, 14)
    k = _stoch_k(high, low, closeadj, 14)
    d = r - k
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_macd_minus_rocsign_30d_base_v028_signal(closeadj):
    """Sign-of-MACD minus sign-of-ROC(10) averaged over 30 bars (sign disagreement
    score between MACD trend and ROC trend, both price-based momentum)."""
    n = 30
    m = _macd(closeadj, 12, 26)
    rc = _roc(closeadj, 10)
    sm = np.sign(m)
    sr = np.sign(rc)
    diff = (sm - sr).abs()
    return diff.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- Composite divergence score (sum of disagreements over N) ---------------


def f14md_f14_momentum_divergence_compxor_rsi_30d_base_v029_signal(closeadj):
    """Sum of multi-shift sign disagreements between price.diff(5) and
    RSI(14).diff(5) over 30d."""
    n = 30
    r = _rsi(closeadj, 14)
    sp = np.sign(closeadj.diff(5))
    sr = np.sign(r.diff(5))
    diff = ((sp * sr) < 0).astype(float).where(~sp.isna() & ~sr.isna())
    return diff.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_compxor_macd_25d_base_v030_signal(close):
    """Count of price-MACD daily sign disagreements over 25d."""
    n = 25
    m = _macd(close, 12, 26)
    sp = np.sign(close.diff())
    sm = np.sign(m.diff())
    diff = ((sp * sm) < 0).astype(float).where(~sp.isna() & ~sm.isna())
    return diff.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_compabs_roc_45d_base_v031_signal(closeadj):
    """Average |normalised price slope - ROC(10) slope| over 45 bars."""
    n = 45
    rc = _roc(closeadj, 10)
    pslp = closeadj.pct_change(5)
    rslp = rc.diff(5) / 100.0
    d = (pslp - rslp).abs()
    return d.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- Bounded transforms (arctan / tanh / sigmoid of slope diff) -------------


def f14md_f14_momentum_divergence_arctan_rsidiv_15d_base_v032_signal(close):
    """arctan of (price-vol-normalised slope - RSI slope) - very different
    scaling from raw slope diff. 15d window."""
    n = 15
    r = _rsi(close, 14)
    vol = close.pct_change().rolling(20, min_periods=20).std(ddof=1)
    pslp = (close.pct_change(n)) / (vol * np.sqrt(n)).replace(0.0, np.nan)
    rslp = r.diff(n) / 100.0
    return np.arctan(2.0 * (pslp - 10.0 * rslp)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_tanh_corrrsi_30d_base_v033_signal(closeadj):
    """tanh(2 * corr(price, RSI)) over 30d. Maps near-perfect-corr to ~+/-1."""
    n = 30
    r = _rsi(closeadj, 14)
    c = closeadj.rolling(n, min_periods=n).corr(r)
    return np.tanh(2.0 * c).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_sigmoid_macdiv_25d_base_v034_signal(closeadj):
    """Sigmoid of (price log-return - normalised MACD slope) over 25d."""
    n = 25
    m = _macd(closeadj, 12, 26) / closeadj
    pslp = np.log(closeadj / closeadj.shift(n))
    mslp = m - m.shift(n)
    x = 10.0 * (pslp - mslp)
    return (1.0 / (1.0 + np.exp(-x)) - 0.5).replace([np.inf, -np.inf], np.nan)


# --- Sign-flip count of disagreement series --------------------------------


def f14md_f14_momentum_divergence_flipcount_pr_40d_base_v035_signal(closeadj):
    """Count of sign-flips in (price.diff - RSI.diff/2) series over 40d."""
    n = 40
    r = _rsi(closeadj, 14)
    d = closeadj.diff() - r.diff() / 2.0
    s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Cumulative-sum / running divergence accumulator ------------------------


def f14md_f14_momentum_divergence_cumdiv_rsi_30d_base_v036_signal(closeadj):
    """Cumulative absolute divergence (energy) of (price.pct_change - RSI.diff/100)
    over 30d - non-directional cumulative magnitude rather than signed slope-diff."""
    n = 30
    r = _rsi(closeadj, 14)
    d = (closeadj.pct_change() - r.diff() / 100.0).abs()
    return d.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_cumdiv_macd_50d_base_v037_signal(closeadj):
    """Rolling sum of (price.pct_change - normalised MACD.diff) over 50d."""
    n = 50
    m = _macd(closeadj, 12, 26) / closeadj
    d = closeadj.pct_change() - m.diff()
    return d.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Convergence rate: how fast price and indicator re-align ---------------


def f14md_f14_momentum_divergence_convrate_rsi_40d_base_v038_signal(closeadj):
    """Convergence rate = corr at 40d minus corr at 10d. Positive -> recently
    coming back together; negative -> recently diverging."""
    r = _rsi(closeadj, 14)
    c_long = closeadj.rolling(40, min_periods=40).corr(r)
    c_short = closeadj.rolling(10, min_periods=10).corr(r)
    return (c_short - c_long).replace([np.inf, -np.inf], np.nan)


# --- Asymmetric divergence (bullish / bearish / net) ------------------------


def f14md_f14_momentum_divergence_bullintens_rsi_40d_base_v039_signal(closeadj):
    """Bullish divergence intensity: max over 40d of (RSI gap when price at
    new low). Captures persistent bullish setup."""
    n = 40
    r = _rsi(closeadj, 14)
    plo = closeadj.rolling(20, min_periods=20).min()
    rlo = r.rolling(20, min_periods=20).min()
    at_low = (closeadj <= plo * 1.001).astype(float).where(~plo.isna())
    raw = at_low * (r - rlo)
    return raw.rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_bearintens_rsi_50d_base_v040_signal(closeadj):
    """Bearish intensity: max over 50d of (RSI-high - current RSI when price
    at new high)."""
    n = 50
    r = _rsi(closeadj, 14)
    phi = closeadj.rolling(25, min_periods=25).max()
    rhi = r.rolling(25, min_periods=25).max()
    at_high = (closeadj >= phi * 0.999).astype(float).where(~phi.isna())
    raw = at_high * (rhi - r)
    return raw.rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_netdiv_rsi_40d_base_v041_signal(closeadj):
    """Net divergence: bullish intensity minus bearish intensity over 40d."""
    n = 40
    r = _rsi(closeadj, 14)
    phi = closeadj.rolling(20, min_periods=20).max()
    plo = closeadj.rolling(20, min_periods=20).min()
    rhi = r.rolling(20, min_periods=20).max()
    rlo = r.rolling(20, min_periods=20).min()
    bull = ((closeadj <= plo * 1.001).astype(float) * (r - rlo)).rolling(n, min_periods=n).mean()
    bear = ((closeadj >= phi * 0.999).astype(float) * (rhi - r)).rolling(n, min_periods=n).mean()
    return (bull - bear).replace([np.inf, -np.inf], np.nan)


# --- Regression-based: residual of RSI on price ----------------------------


def f14md_f14_momentum_divergence_regresid_rsi_30d_base_v042_signal(closeadj):
    """Residual of regressing RSI on log-price over 30d (final residual). Big
    |residual| -> RSI deviates from its expected co-movement with price."""
    n = 30
    r = _rsi(closeadj, 14)
    lp = np.log(closeadj)
    def _resid(idx):
        i = int(idx[-1])
        a = lp.iloc[i - n + 1 : i + 1].values
        b = r.iloc[i - n + 1 : i + 1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(b)):
            return np.nan
        am = a.mean(); bm = b.mean()
        va = ((a - am) ** 2).sum()
        if va <= 0.0:
            return np.nan
        beta = ((a - am) * (b - bm)).sum() / va
        alpha = bm - beta * am
        return float(b[-1] - (alpha + beta * a[-1]))
    idx_s = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    return idx_s.rolling(n, min_periods=n).apply(_resid, raw=True).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_beta_rsi_60d_base_v043_signal(closeadj):
    """Beta of RSI on log-price over 60d. Low / negative beta -> RSI uncoupled
    from price drift."""
    n = 60
    r = _rsi(closeadj, 14)
    lp = np.log(closeadj)
    cov = lp.rolling(n, min_periods=n).cov(r)
    var = lp.rolling(n, min_periods=n).var(ddof=1)
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_r2_pm_50d_base_v044_signal(closeadj):
    """R^2 of price-vs-momentum(close.diff) fit over 50d. Low R^2 -> divergent."""
    n = 50
    mom = closeadj.diff()
    c = closeadj.rolling(n, min_periods=n).corr(mom)
    return (c * c).replace([np.inf, -np.inf], np.nan)


# --- Higher-order: curvature / jerk divergence -----------------------------


def f14md_f14_momentum_divergence_curv_rsi_25d_base_v045_signal(closeadj):
    """Price 2nd diff minus RSI 2nd diff over 25d. Curvature divergence."""
    n = 25
    r = _rsi(closeadj, 14)
    pcurv = (closeadj - 2 * closeadj.shift(n) + closeadj.shift(2 * n)) / closeadj.shift(n).replace(0.0, np.nan)
    rcurv = (r - 2 * r.shift(n) + r.shift(2 * n)) / 100.0
    return (pcurv - rcurv).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_accel_macd_30d_base_v046_signal(closeadj):
    """Price acceleration minus MACD acceleration over 30d."""
    n = 30
    m = _macd(closeadj, 12, 26) / closeadj
    pa = closeadj.pct_change(n) - closeadj.pct_change(n).shift(n)
    ma = m.diff(n) - m.diff(n).shift(n)
    return (pa - ma).replace([np.inf, -np.inf], np.nan)


# --- Time-domain: lag of max correlation -----------------------------------


def f14md_f14_momentum_divergence_lag_pr_rsi_30d_base_v047_signal(closeadj):
    """Lag (in {-3..3}) at which price.pct_change and RSI(14) maximally
    correlate over 30 bars. Non-zero lag = leading/lagging divergence."""
    n = 30
    r = _rsi(closeadj, 14)
    ret = closeadj.pct_change()
    def _bestlag(idx):
        i = int(idx[-1])
        if i < 2 * n:
            return np.nan
        a = ret.iloc[i - n + 1 : i + 1].values
        best = 0.0
        bl = 0
        for L in range(-3, 4):
            b = r.shift(L).iloc[i - n + 1 : i + 1].values
            if np.any(~np.isfinite(a)) or np.any(~np.isfinite(b)):
                continue
            sa = a.std(); sb = b.std()
            if sa <= 0 or sb <= 0:
                continue
            c = float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
            if abs(c) > abs(best):
                best = c
                bl = L
        return float(bl)
    idx_s = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    return idx_s.rolling(n, min_periods=n).apply(_bestlag, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Velocity differential -------------------------------------------------


def f14md_f14_momentum_divergence_veldiff_rsi_8d_base_v048_signal(close):
    """(close.pct_change(8)) - (RSI(14).pct_change(8))."""
    n = 8
    r = _rsi(close, 14)
    return (close.pct_change(n) - r.pct_change(n)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_veldiff_macd_12d_base_v049_signal(close):
    """(close.pct_change(12)) - (normalised MACD pct change). Velocity diff."""
    n = 12
    m = _macd(close, 12, 26)
    mn = m / close
    return (close.pct_change(n) - mn.diff(n)).replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_veldiff_stoch_18d_base_v050_signal(high, low, close):
    """(close.pct_change(18)) - (Stochastic-K(14) change / 100), 18d."""
    n = 18
    k = _stoch_k(high, low, close, 14)
    return (close.pct_change(n) - k.diff(n) / 100.0).replace([np.inf, -np.inf], np.nan)


# --- Z-score of slope difference -------------------------------------------


def f14md_f14_momentum_divergence_zslp_rsi_40d_base_v051_signal(closeadj):
    """Z-score (60d window) of 10d price-slope minus RSI(14)-slope."""
    n = 40
    r = _rsi(closeadj, 14)
    d = (closeadj - closeadj.shift(10)) / closeadj.shift(10).replace(0.0, np.nan) * 100.0 - (r - r.shift(10))
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Rank of corr (percentile) ---------------------------------------------


def f14md_f14_momentum_divergence_corrrank_rsi_100d_base_v052_signal(closeadj):
    """Percentile rank (100d) of 20d corr(close, RSI). Low rank -> divergent regime."""
    n = 100
    r = _rsi(closeadj, 14)
    c = closeadj.rolling(20, min_periods=20).corr(r)
    return c.rolling(n, min_periods=n).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Higher-order indicators -----------------------------------------------


def f14md_f14_momentum_divergence_pjerk_rjerk_30d_base_v053_signal(closeadj):
    """Price jerk minus RSI jerk over 30d. Third-order divergence."""
    n = 30
    r = _rsi(closeadj, 14)
    pj = closeadj.pct_change(n).diff(n).diff(n)
    rj = (r.diff(n) / 100.0).diff(n).diff(n)
    return (pj - rj).replace([np.inf, -np.inf], np.nan)


# --- Stochastic vs RSI: cross-oscillator price-momentum divergence ---------


def f14md_f14_momentum_divergence_stochrsi_div_30d_base_v054_signal(high, low, closeadj):
    """tanh of (Stochastic-K(14) - RSI(14)) / 20 - bounded transform of two
    distinct momentum measures of the same price."""
    k = _stoch_k(high, low, closeadj, 14)
    r = _rsi(closeadj, 14)
    return np.tanh((k - r) / 20.0).replace([np.inf, -np.inf], np.nan)


# --- Coherence at fixed lag ------------------------------------------------


def f14md_f14_momentum_divergence_lag1_pr_corr_40d_base_v055_signal(closeadj):
    """Corr(close, RSI.shift(1)) over 40d. Lag-1 coherence: nonzero -> RSI leads."""
    n = 40
    r = _rsi(closeadj, 14)
    return closeadj.rolling(n, min_periods=n).corr(r.shift(1)).replace([np.inf, -np.inf], np.nan)


# --- Magnitude divergence (absolute value comparison) ----------------------


def f14md_f14_momentum_divergence_magdiv_rsi_25d_base_v056_signal(close):
    """|price 25d log-return| minus |normalised RSI 25d change|. Magnitude
    divergence: how much of the move did momentum register."""
    n = 25
    r = _rsi(close, 14)
    pm = np.log(close / close.shift(n)).abs()
    rm = (r.diff(n) / 100.0).abs()
    return (pm - rm).replace([np.inf, -np.inf], np.nan)


# --- Days at-high-without-osc-high counter ---------------------------------


def f14md_f14_momentum_divergence_days_div_rsi_60d_base_v057_signal(closeadj):
    """Count over 60d of bars where price >= 20d-high but RSI < 20d-RSI-high - 5."""
    n = 60
    r = _rsi(closeadj, 14)
    phi = closeadj.rolling(20, min_periods=20).max()
    rhi = r.rolling(20, min_periods=20).max()
    event = ((closeadj >= phi * 0.999) & (r < rhi - 5.0)).astype(float).where(~phi.isna() & ~rhi.isna())
    return event.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Multi-window divergence signal (composite of two windows) -------------


def f14md_f14_momentum_divergence_multi_macd_60d_base_v058_signal(closeadj):
    """Average of price-MACD log-slope-diff at 20d and 60d (multi-window
    composite divergence)."""
    m = _macd(closeadj, 12, 26) / closeadj
    p1 = np.log(closeadj / closeadj.shift(20))
    m1 = m - m.shift(20)
    p2 = np.log(closeadj / closeadj.shift(60))
    m2 = m - m.shift(60)
    return ((p1 - m1) * 0.5 + (p2 - m2) * 0.5).replace([np.inf, -np.inf], np.nan)


# --- Streak of consecutive divergent bars ----------------------------------


def f14md_f14_momentum_divergence_streak_xor_50d_base_v059_signal(closeadj):
    """Current length of consecutive bars where sign(price.diff(5)) !=
    sign(MACD.diff(5)). Capped at 50."""
    m = _macd(closeadj, 12, 26)
    sp = np.sign(closeadj.diff(5))
    sm = np.sign(m.diff(5))
    disagree = ((sp * sm) < 0).astype(float).where(~sp.isna() & ~sm.isna())
    def _streak(x):
        s = 0
        for v in x[::-1]:
            if v > 0.5:
                s += 1
            else:
                break
        return float(s)
    return disagree.rolling(50, min_periods=50).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Spearman rank corr (robust) -------------------------------------------


def f14md_f14_momentum_divergence_rankcorr_macd_40d_base_v060_signal(closeadj):
    """Spearman corr (40d) between price LOG-RETURNS and MACD CHANGES. Differs
    structurally from level-corr because both inputs are differenced first."""
    n = 40
    m = _macd(closeadj, 12, 26)
    ret = np.log(closeadj / closeadj.shift(1))
    md = m.diff()
    def _sp(idx):
        i = int(idx[-1])
        a = ret.iloc[i - n + 1 : i + 1].values
        b = md.iloc[i - n + 1 : i + 1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(b)):
            return np.nan
        ra = pd.Series(a).rank().values
        rb = pd.Series(b).rank().values
        sa = ra.std(); sb = rb.std()
        if sa <= 0 or sb <= 0:
            return np.nan
        return float(((ra - ra.mean()) * (rb - rb.mean())).mean() / (sa * sb))
    idx_s = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    return idx_s.rolling(n, min_periods=n).apply(_sp, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Divergence-direction sign --------------------------------------------


def f14md_f14_momentum_divergence_signdir_rsi_20d_base_v061_signal(close):
    """Sign(price.diff(20)) MINUS sign(RSI.diff(20)). Values in {-2,-1,0,1,2}."""
    n = 20
    r = _rsi(close, 14)
    return (np.sign(close.diff(n)) - np.sign(r.diff(n))).replace([np.inf, -np.inf], np.nan)


# --- Mean-absolute slope-diff (non-directional divergence) -----------------


def f14md_f14_momentum_divergence_mad_slope_pr_30d_base_v062_signal(closeadj):
    """Mean-abs daily (price-pct - RSI-pct) over 30d -> non-directional
    divergence magnitude."""
    n = 30
    r = _rsi(closeadj, 14)
    d = (closeadj.pct_change() - r.pct_change()).abs()
    return d.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- High-frequency divergence proxy ---------------------------------------


def f14md_f14_momentum_divergence_hfdiv_rsi_5d_base_v063_signal(close):
    """5-day price log-return MINUS 5-day RSI change / 50. Short-term
    momentum-vs-price disagreement."""
    n = 5
    r = _rsi(close, 14)
    return (np.log(close / close.shift(n)) - r.diff(n) / 50.0).replace([np.inf, -np.inf], np.nan)


# --- TSI vs price divergence (long horizon) --------------------------------


def f14md_f14_momentum_divergence_tsi_div_80d_base_v064_signal(closeadj):
    """Z-score (80d window) of (log-price-return - TSI(25,13)/100 change)."""
    n = 80
    t = _tsi(closeadj, 25, 13)
    d = np.log(closeadj / closeadj.shift(20)) - t.diff(20) / 100.0
    mu = d.rolling(n, min_periods=n).mean()
    sd = d.rolling(n, min_periods=n).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Net momentum divergence using both bull / bear sides ------------------


def f14md_f14_momentum_divergence_netasym_macd_50d_base_v065_signal(closeadj):
    """Asymmetric divergence: count(bullish-macd-div) - count(bearish-macd-div)
    over 50d window."""
    n = 50
    m = _macd(closeadj, 12, 26)
    phi = closeadj.rolling(20, min_periods=20).max()
    plo = closeadj.rolling(20, min_periods=20).min()
    mhi = m.rolling(20, min_periods=20).max()
    mlo = m.rolling(20, min_periods=20).min()
    bull = ((closeadj <= plo * 1.001) & (m > mlo)).astype(float).where(~plo.isna() & ~mlo.isna())
    bear = ((closeadj >= phi * 0.999) & (m < mhi)).astype(float).where(~phi.isna() & ~mhi.isna())
    return (bull.rolling(n, min_periods=n).sum() - bear.rolling(n, min_periods=n).sum()).replace([np.inf, -np.inf], np.nan)


# --- Mean-square deviation: price-vs-indicator dispersion ------------------


def f14md_f14_momentum_divergence_msd_norm_pr_50d_base_v066_signal(closeadj):
    """MSE between Z-scored log-price and Z-scored RSI over 50d."""
    n = 50
    lp = np.log(closeadj)
    r = _rsi(closeadj, 14)
    zlp = (lp - lp.rolling(n, min_periods=n).mean()) / lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zr = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    return ((zlp - zr) ** 2).replace([np.inf, -np.inf], np.nan)


# --- Hidden divergence: price LH but RSI HH (continuation) -----------------


def f14md_f14_momentum_divergence_hidden_rsi_30d_base_v067_signal(closeadj):
    """Hidden bearish divergence: price made lower-high but RSI made higher-high
    over 30d. Binary 1 if so."""
    n = 30
    r = _rsi(closeadj, 14)
    plo_now = closeadj.rolling(15, min_periods=15).max()
    plo_then = plo_now.shift(15)
    rhi_now = r.rolling(15, min_periods=15).max()
    rhi_then = rhi_now.shift(15)
    cond = ((plo_now < plo_then) & (rhi_now > rhi_then)).astype(float).where(~plo_then.isna() & ~rhi_then.isna())
    return cond.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- Ratio of slopes ------------------------------------------------------


def f14md_f14_momentum_divergence_slpratio_rsi_30d_base_v068_signal(closeadj):
    """arctan of (price-slope / RSI-slope) over 30d. Captures
    proportional disagreement (1 = aligned, near 0 = momentum lags)."""
    n = 30
    r = _rsi(closeadj, 14)
    pslp = (closeadj - closeadj.shift(n)) / closeadj.shift(n).replace(0.0, np.nan)
    rslp = (r - r.shift(n)) / 100.0
    return np.arctan(pslp / rslp.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Vortex-style: price vs ROC oscillator delta --------------------------


def f14md_f14_momentum_divergence_pmroc_avg_60d_base_v069_signal(closeadj):
    """Avg over 60d of (price 5d-return - ROC(5)/100)."""
    n = 60
    r5 = _roc(closeadj, 5) / 100.0
    d = closeadj.pct_change(5) - r5
    return d.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- OBV-style price-vs-momentum vol-weighted divergence ------------------


def f14md_f14_momentum_divergence_obvmom_30d_base_v070_signal(close, volume):
    """Avg of (volume*sign(close.diff))-(close.diff*sign(close.diff)) sign
    divergence over 30d (volume-momentum vs price-momentum)."""
    n = 30
    sp = np.sign(close.diff())
    obvflow = (volume * sp).rolling(n, min_periods=n).sum()
    pflow = (close.diff().abs() * sp).rolling(n, min_periods=n).sum()
    zo = (obvflow - obvflow.rolling(60, min_periods=60).mean()) / obvflow.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    zp = (pflow - pflow.rolling(60, min_periods=60).mean()) / pflow.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    return (zp - zo).replace([np.inf, -np.inf], np.nan)


# --- Adaptive divergence threshold count -----------------------------------


def f14md_f14_momentum_divergence_adaptdiv_rsi_60d_base_v071_signal(closeadj):
    """Number of 5d windows in last 60d where |price-slope - RSI-slope| > rolling
    50th-pctile of |price-slope - RSI-slope| over 100d."""
    r = _rsi(closeadj, 14)
    d = (closeadj.pct_change(5) * 100.0 - r.diff(5)).abs()
    med = d.rolling(100, min_periods=100).median()
    flag = (d > med).astype(float).where(~med.isna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# --- Coherence over the full lag spectrum --------------------------------


def f14md_f14_momentum_divergence_avgcoh_macd_50d_base_v072_signal(closeadj):
    """Difference between |corr(price, MACD)| at lag 0 vs at lag +/-2 over 50d.
    Captures lag-dispersion of coherence rather than level."""
    n = 50
    m = _macd(closeadj, 12, 26)
    c0 = closeadj.rolling(n, min_periods=n).corr(m).abs()
    cp2 = closeadj.rolling(n, min_periods=n).corr(m.shift(2)).abs()
    cn2 = closeadj.rolling(n, min_periods=n).corr(m.shift(-2)).abs()
    return (c0 - (cp2 + cn2) * 0.5).replace([np.inf, -np.inf], np.nan)


# --- Sign-of-divergence persistence ---------------------------------------


def f14md_f14_momentum_divergence_persistdiv_rsi_40d_base_v073_signal(closeadj):
    """Mean over 40d of sign(price.diff(5) - RSI.diff(5)/20). Persistent
    one-sided divergence."""
    n = 40
    r = _rsi(closeadj, 14)
    s = np.sign(closeadj.pct_change(5) * 100.0 - r.diff(5) / 20.0)
    return s.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- Quintile bucket of divergence strength -------------------------------


def f14md_f14_momentum_divergence_quintdiv_rsi_120d_base_v074_signal(closeadj):
    """Quintile (1..5) of 10d slope-of-corr(price,RSI) -> rate-of-change of
    coupling, ranked within 120d. Differs from raw corr rank."""
    r = _rsi(closeadj, 14)
    c = closeadj.rolling(20, min_periods=20).corr(r)
    dc = c.diff(10)
    pct = dc.rolling(120, min_periods=120).rank(pct=True)
    return (np.ceil(pct * 5.0)).replace([np.inf, -np.inf], np.nan)


# --- Skew of divergence series --------------------------------------------


def f14md_f14_momentum_divergence_skew_diff_rsi_60d_base_v075_signal(closeadj):
    """Skewness over 60d of (price.pct_change - RSI.diff/100) series."""
    n = 60
    r = _rsi(closeadj, 14)
    d = closeadj.pct_change() - r.diff() / 100.0
    return d.rolling(n, min_periods=n).skew().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f14_momentum_divergence_base_001_075_REGISTRY = {
    "f14md_f14_momentum_divergence_pslp_rsi_14d_base_v001_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_pslp_rsi_14d_base_v001_signal},
    "f14md_f14_momentum_divergence_pslp_rsi_30d_base_v002_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pslp_rsi_30d_base_v002_signal},
    "f14md_f14_momentum_divergence_pslp_macd_20d_base_v003_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_pslp_macd_20d_base_v003_signal},
    "f14md_f14_momentum_divergence_pslp_roc_25d_base_v004_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pslp_roc_25d_base_v004_signal},
    "f14md_f14_momentum_divergence_pslp_stoch_15d_base_v005_signal": {"inputs": ["high", "low", "close"], "func": f14md_f14_momentum_divergence_pslp_stoch_15d_base_v005_signal},
    "f14md_f14_momentum_divergence_pslp_cmo_30d_base_v006_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pslp_cmo_30d_base_v006_signal},
    "f14md_f14_momentum_divergence_pslp_tsi_40d_base_v007_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pslp_tsi_40d_base_v007_signal},
    "f14md_f14_momentum_divergence_pslp_mfi_18d_base_v008_signal": {"inputs": ["high", "low", "close", "volume"], "func": f14md_f14_momentum_divergence_pslp_mfi_18d_base_v008_signal},
    "f14md_f14_momentum_divergence_signxor_rsi_10d_base_v009_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_signxor_rsi_10d_base_v009_signal},
    "f14md_f14_momentum_divergence_signxor_macd_15d_base_v010_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_signxor_macd_15d_base_v010_signal},
    "f14md_f14_momentum_divergence_signxor_roc_30d_base_v011_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_signxor_roc_30d_base_v011_signal},
    "f14md_f14_momentum_divergence_signxor_stoch_8d_base_v012_signal": {"inputs": ["high", "low", "close"], "func": f14md_f14_momentum_divergence_signxor_stoch_8d_base_v012_signal},
    "f14md_f14_momentum_divergence_corr_rsi_20d_base_v013_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_corr_rsi_20d_base_v013_signal},
    "f14md_f14_momentum_divergence_corr_rsi_60d_base_v014_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corr_rsi_60d_base_v014_signal},
    "f14md_f14_momentum_divergence_corr_macd_40d_base_v015_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corr_macd_40d_base_v015_signal},
    "f14md_f14_momentum_divergence_corr_mom_30d_base_v016_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corr_mom_30d_base_v016_signal},
    "f14md_f14_momentum_divergence_corr_tsi_50d_base_v017_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corr_tsi_50d_base_v017_signal},
    "f14md_f14_momentum_divergence_corr_cmo_45d_base_v018_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corr_cmo_45d_base_v018_signal},
    "f14md_f14_momentum_divergence_phigh_rsi_low_20d_base_v019_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_phigh_rsi_low_20d_base_v019_signal},
    "f14md_f14_momentum_divergence_plow_rsi_high_30d_base_v020_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_plow_rsi_high_30d_base_v020_signal},
    "f14md_f14_momentum_divergence_phigh_macd_low_40d_base_v021_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_phigh_macd_low_40d_base_v021_signal},
    "f14md_f14_momentum_divergence_phigh_stoch_low_15d_base_v022_signal": {"inputs": ["high", "low", "close"], "func": f14md_f14_momentum_divergence_phigh_stoch_low_15d_base_v022_signal},
    "f14md_f14_momentum_divergence_plow_mfi_high_25d_base_v023_signal": {"inputs": ["high", "low", "close", "volume"], "func": f14md_f14_momentum_divergence_plow_mfi_high_25d_base_v023_signal},
    "f14md_f14_momentum_divergence_dslph_rsi_60d_base_v024_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_dslph_rsi_60d_base_v024_signal},
    "f14md_f14_momentum_divergence_dsplh_rsi_80d_base_v025_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_dsplh_rsi_80d_base_v025_signal},
    "f14md_f14_momentum_divergence_rsi_minus_mfi_30d_base_v026_signal": {"inputs": ["high", "low", "close", "volume"], "func": f14md_f14_momentum_divergence_rsi_minus_mfi_30d_base_v026_signal},
    "f14md_f14_momentum_divergence_rsi_minus_stoch_40d_base_v027_signal": {"inputs": ["high", "low", "closeadj"], "func": f14md_f14_momentum_divergence_rsi_minus_stoch_40d_base_v027_signal},
    "f14md_f14_momentum_divergence_macd_minus_rocsign_30d_base_v028_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_macd_minus_rocsign_30d_base_v028_signal},
    "f14md_f14_momentum_divergence_compxor_rsi_30d_base_v029_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_compxor_rsi_30d_base_v029_signal},
    "f14md_f14_momentum_divergence_compxor_macd_25d_base_v030_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_compxor_macd_25d_base_v030_signal},
    "f14md_f14_momentum_divergence_compabs_roc_45d_base_v031_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_compabs_roc_45d_base_v031_signal},
    "f14md_f14_momentum_divergence_arctan_rsidiv_15d_base_v032_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_arctan_rsidiv_15d_base_v032_signal},
    "f14md_f14_momentum_divergence_tanh_corrrsi_30d_base_v033_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_tanh_corrrsi_30d_base_v033_signal},
    "f14md_f14_momentum_divergence_sigmoid_macdiv_25d_base_v034_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_sigmoid_macdiv_25d_base_v034_signal},
    "f14md_f14_momentum_divergence_flipcount_pr_40d_base_v035_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_flipcount_pr_40d_base_v035_signal},
    "f14md_f14_momentum_divergence_cumdiv_rsi_30d_base_v036_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_cumdiv_rsi_30d_base_v036_signal},
    "f14md_f14_momentum_divergence_cumdiv_macd_50d_base_v037_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_cumdiv_macd_50d_base_v037_signal},
    "f14md_f14_momentum_divergence_convrate_rsi_40d_base_v038_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_convrate_rsi_40d_base_v038_signal},
    "f14md_f14_momentum_divergence_bullintens_rsi_40d_base_v039_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_bullintens_rsi_40d_base_v039_signal},
    "f14md_f14_momentum_divergence_bearintens_rsi_50d_base_v040_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_bearintens_rsi_50d_base_v040_signal},
    "f14md_f14_momentum_divergence_netdiv_rsi_40d_base_v041_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_netdiv_rsi_40d_base_v041_signal},
    "f14md_f14_momentum_divergence_regresid_rsi_30d_base_v042_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_regresid_rsi_30d_base_v042_signal},
    "f14md_f14_momentum_divergence_beta_rsi_60d_base_v043_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_beta_rsi_60d_base_v043_signal},
    "f14md_f14_momentum_divergence_r2_pm_50d_base_v044_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_r2_pm_50d_base_v044_signal},
    "f14md_f14_momentum_divergence_curv_rsi_25d_base_v045_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_curv_rsi_25d_base_v045_signal},
    "f14md_f14_momentum_divergence_accel_macd_30d_base_v046_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_accel_macd_30d_base_v046_signal},
    "f14md_f14_momentum_divergence_lag_pr_rsi_30d_base_v047_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_lag_pr_rsi_30d_base_v047_signal},
    "f14md_f14_momentum_divergence_veldiff_rsi_8d_base_v048_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_veldiff_rsi_8d_base_v048_signal},
    "f14md_f14_momentum_divergence_veldiff_macd_12d_base_v049_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_veldiff_macd_12d_base_v049_signal},
    "f14md_f14_momentum_divergence_veldiff_stoch_18d_base_v050_signal": {"inputs": ["high", "low", "close"], "func": f14md_f14_momentum_divergence_veldiff_stoch_18d_base_v050_signal},
    "f14md_f14_momentum_divergence_zslp_rsi_40d_base_v051_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_zslp_rsi_40d_base_v051_signal},
    "f14md_f14_momentum_divergence_corrrank_rsi_100d_base_v052_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_corrrank_rsi_100d_base_v052_signal},
    "f14md_f14_momentum_divergence_pjerk_rjerk_30d_base_v053_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pjerk_rjerk_30d_base_v053_signal},
    "f14md_f14_momentum_divergence_stochrsi_div_30d_base_v054_signal": {"inputs": ["high", "low", "closeadj"], "func": f14md_f14_momentum_divergence_stochrsi_div_30d_base_v054_signal},
    "f14md_f14_momentum_divergence_lag1_pr_corr_40d_base_v055_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_lag1_pr_corr_40d_base_v055_signal},
    "f14md_f14_momentum_divergence_magdiv_rsi_25d_base_v056_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_magdiv_rsi_25d_base_v056_signal},
    "f14md_f14_momentum_divergence_days_div_rsi_60d_base_v057_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_days_div_rsi_60d_base_v057_signal},
    "f14md_f14_momentum_divergence_multi_macd_60d_base_v058_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_multi_macd_60d_base_v058_signal},
    "f14md_f14_momentum_divergence_streak_xor_50d_base_v059_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_streak_xor_50d_base_v059_signal},
    "f14md_f14_momentum_divergence_rankcorr_macd_40d_base_v060_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_rankcorr_macd_40d_base_v060_signal},
    "f14md_f14_momentum_divergence_signdir_rsi_20d_base_v061_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_signdir_rsi_20d_base_v061_signal},
    "f14md_f14_momentum_divergence_mad_slope_pr_30d_base_v062_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_mad_slope_pr_30d_base_v062_signal},
    "f14md_f14_momentum_divergence_hfdiv_rsi_5d_base_v063_signal": {"inputs": ["close"], "func": f14md_f14_momentum_divergence_hfdiv_rsi_5d_base_v063_signal},
    "f14md_f14_momentum_divergence_tsi_div_80d_base_v064_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_tsi_div_80d_base_v064_signal},
    "f14md_f14_momentum_divergence_netasym_macd_50d_base_v065_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_netasym_macd_50d_base_v065_signal},
    "f14md_f14_momentum_divergence_msd_norm_pr_50d_base_v066_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_msd_norm_pr_50d_base_v066_signal},
    "f14md_f14_momentum_divergence_hidden_rsi_30d_base_v067_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_hidden_rsi_30d_base_v067_signal},
    "f14md_f14_momentum_divergence_slpratio_rsi_30d_base_v068_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_slpratio_rsi_30d_base_v068_signal},
    "f14md_f14_momentum_divergence_pmroc_avg_60d_base_v069_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_pmroc_avg_60d_base_v069_signal},
    "f14md_f14_momentum_divergence_obvmom_30d_base_v070_signal": {"inputs": ["close", "volume"], "func": f14md_f14_momentum_divergence_obvmom_30d_base_v070_signal},
    "f14md_f14_momentum_divergence_adaptdiv_rsi_60d_base_v071_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_adaptdiv_rsi_60d_base_v071_signal},
    "f14md_f14_momentum_divergence_avgcoh_macd_50d_base_v072_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_avgcoh_macd_50d_base_v072_signal},
    "f14md_f14_momentum_divergence_persistdiv_rsi_40d_base_v073_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_persistdiv_rsi_40d_base_v073_signal},
    "f14md_f14_momentum_divergence_quintdiv_rsi_120d_base_v074_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_quintdiv_rsi_120d_base_v074_signal},
    "f14md_f14_momentum_divergence_skew_diff_rsi_60d_base_v075_signal": {"inputs": ["closeadj"], "func": f14md_f14_momentum_divergence_skew_diff_rsi_60d_base_v075_signal},
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
    for name, entry in f14_momentum_divergence_base_001_075_REGISTRY.items():
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
