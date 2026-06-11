"""momentum_exhaustion base features 001_075 — short blowup pipeline 1a-inverse.

Momentum exhaustion signatures at multi-year peaks: oscillator overextension, divergence, thrust decay, and acceleration loss.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _rsi_wilder(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    ru = _wilder_rma(up, n)
    rd = _wilder_rma(dn, n)
    rs = ru / rd.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _rsi_cutler(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    ru = up.rolling(n, min_periods=max(n // 3, 2)).mean()
    rd = dn.rolling(n, min_periods=max(n // 3, 2)).mean()
    rs = ru / rd.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _stoch_k(close, high, low, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _stoch_d(close, high, low, n=14, d=3):
    k = _stoch_k(close, high, low, n)
    return k.rolling(d, min_periods=1).mean()


def _macd(close, fast=12, slow=26, signal=9):
    line = _ema(close, fast) - _ema(close, slow)
    sig = _ema(line, signal)
    hist = line - sig
    return line, sig, hist


def _trix(close, n):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return e3.pct_change() * 1000.0


def _tsi(close, r=25, s=13):
    m = close.diff()
    em1 = _ema(m, r); em2 = _ema(em1, s)
    am1 = _ema(m.abs(), r); am2 = _ema(am1, s)
    return 100.0 * _safe_div(em2, am2)


def _dmi(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    up = high.diff()
    dn = -low.diff()
    plus_dm = ((up > dn) & (up > 0)).astype(float) * up
    minus_dm = ((dn > up) & (dn > 0)).astype(float) * dn
    atr = _wilder_rma(tr, n)
    plus_di = 100.0 * _wilder_rma(plus_dm, n) / atr.replace(0, np.nan)
    minus_di = 100.0 * _wilder_rma(minus_dm, n) / atr.replace(0, np.nan)
    dx = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = _wilder_rma(dx, n)
    return plus_di, minus_di, adx


def _aroon(high, low, n=25):
    def _idx_max(w):
        return (len(w) - 1) - int(np.argmax(w))
    def _idx_min(w):
        return (len(w) - 1) - int(np.argmin(w))
    bsm_h = high.rolling(n, min_periods=max(n // 3, 2)).apply(_idx_max, raw=True)
    bsm_l = low.rolling(n, min_periods=max(n // 3, 2)).apply(_idx_min, raw=True)
    up = 100.0 * (n - bsm_h) / n
    dn = 100.0 * (n - bsm_l) / n
    return up, dn


def _vortex(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    vmp = (high - low.shift(1)).abs()
    vmm = (low - high.shift(1)).abs()
    vip = vmp.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum().replace(0, np.nan)
    vim = vmm.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum().replace(0, np.nan)
    return vip, vim


def _mass_index(high, low, n_ema=9, n_sum=25):
    rng = high - low
    e1 = _ema(rng, n_ema)
    e2 = _ema(e1, n_ema)
    ratio = e1 / e2.replace(0, np.nan)
    return ratio.rolling(n_sum, min_periods=max(n_sum // 3, 2)).sum()


def _choppiness(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr_sum = tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    rng = hh - ll
    return 100.0 * np.log10(_safe_div(atr_sum, rng).replace(0, np.nan)) / np.log10(n)


def _ultimate(close, high, low, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    avg = lambda w: bp.rolling(w, min_periods=max(w // 3, 2)).sum() / tr.rolling(w, min_periods=max(w // 3, 2)).sum().replace(0, np.nan)
    return 100.0 * (4 * avg(n1) + 2 * avg(n2) + avg(n3)) / 7.0


def _awesome(high, low, fast=5, slow=34):
    mp = (high + low) / 2.0
    return mp.rolling(fast, min_periods=max(fast // 3, 2)).mean() - mp.rolling(slow, min_periods=max(slow // 3, 2)).mean()


def _kst(close, r1=10, r2=15, r3=20, r4=30, s1=10, s2=10, s3=10, s4=15):
    roc = lambda n: close.pct_change(n)
    return (
        roc(r1).rolling(s1, min_periods=max(s1 // 3, 2)).mean() * 1
        + roc(r2).rolling(s2, min_periods=max(s2 // 3, 2)).mean() * 2
        + roc(r3).rolling(s3, min_periods=max(s3 // 3, 2)).mean() * 3
        + roc(r4).rolling(s4, min_periods=max(s4 // 3, 2)).mean() * 4
    )


def _dpo(close, n=21):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)


def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    dn = (-d).clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(up - dn, up + dn)


def _kvo(high, low, close, volume, fast=34, slow=55):
    hlc3 = (high + low + close) / 3.0
    trend = np.sign(hlc3.diff().fillna(0))
    sv = volume * trend
    return _ema(sv, fast) - _ema(sv, slow)


def _stc(close, fast=23, slow=50, cyc=10):
    macd = _ema(close, fast) - _ema(close, slow)
    lo = macd.rolling(cyc, min_periods=max(cyc // 3, 2)).min()
    hi = macd.rolling(cyc, min_periods=max(cyc // 3, 2)).max()
    k = 100.0 * _safe_div(macd - lo, hi - lo)
    return k.ewm(span=cyc, adjust=False, min_periods=max(cyc // 3, 2)).mean()


def _coppock(close, r1=14, r2=11, smooth=10):
    return (close.pct_change(r1) + close.pct_change(r2)).rolling(smooth, min_periods=max(smooth // 3, 2)).mean()


def _obv(close, volume):
    sign = np.sign(close.diff().fillna(0))
    return (sign * volume).cumsum()

# ============================================================
#                    BASE FEATURES 001-075
# ============================================================

def f09_mexh_001_rsi_wilder_25_overbought_intensity_63d(close: pd.Series) -> pd.Series:
    """Mean of (RSI_w(25) - 75)+ over trailing 63d — long-horizon overbought intensity."""
    r = _rsi_wilder(close, 25)
    return (r - 75).clip(lower=0).rolling(QDAYS, min_periods=MDAYS).mean()


def f09_mexh_002_rsi_wilder_50_overbought_intensity_63d(close: pd.Series) -> pd.Series:
    """Long-window (50d) Wilder RSI overbought intensity."""
    r = _rsi_wilder(close, 50)
    return (r - 75).clip(lower=0).rolling(QDAYS, min_periods=MDAYS).mean()


def f09_mexh_003_rsi_cutler_25_value(close: pd.Series) -> pd.Series:
    """Cutler's RSI(25) (SMA-smoothed) — long-horizon RSI variant."""
    return _rsi_cutler(close, 25)


def f09_mexh_004_rsi_cutler_50_value(close: pd.Series) -> pd.Series:
    """Cutler's RSI(50)."""
    return _rsi_cutler(close, 50)


def f09_mexh_005_rsi_connors_3(close: pd.Series) -> pd.Series:
    """Connors RSI proxy: average of RSI(3) + RSI of streak + 100*percentrank ROC."""
    r3 = _rsi_wilder(close, 3)
    streak = np.sign(close.diff().fillna(0))
    rstreak = _rsi_wilder(streak, 2)
    roc1 = close.pct_change()
    pr = _rolling_pctrank(roc1, 100) * 100
    return (r3 + rstreak + pr) / 3.0


def f09_mexh_006_rsi_smoothed_14_ema_5(close: pd.Series) -> pd.Series:
    """EMA(5) of RSI(14) — smoothed RSI for less-noisy exhaustion read."""
    r = _rsi_wilder(close, 14)
    return _ema(r, 5)


def f09_mexh_007_rsi_25_days_above_70_252d(close: pd.Series) -> pd.Series:
    """Count days RSI(25) > 70 in trailing 252d."""
    r = _rsi_wilder(close, 25)
    return (r > 70).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_008_rsi_25_days_above_80_252d(close: pd.Series) -> pd.Series:
    """Count days RSI(25) > 80 in trailing 252d."""
    r = _rsi_wilder(close, 25)
    return (r > 80).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_009_rsi_50_days_above_60_252d(close: pd.Series) -> pd.Series:
    """Count days RSI(50) > 60 in trailing 252d — long-horizon overheat."""
    r = _rsi_wilder(close, 50)
    return (r > 60).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_010_days_since_rsi14_crossed_50(close: pd.Series) -> pd.Series:
    """Bars since RSI(14) last crossed 50."""
    r = _rsi_wilder(close, 14)
    sign = np.sign((r - 50).fillna(0))
    cross = (sign != sign.shift(1)) & sign.shift(1).ne(0)
    idx = np.arange(len(close))
    last = pd.Series(np.where(cross.values, idx, np.nan), index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f09_mexh_011_days_since_rsi25_crossed_70(close: pd.Series) -> pd.Series:
    """Bars since RSI(25) last crossed 70."""
    r = _rsi_wilder(close, 25)
    sign = np.sign((r - 70).fillna(0))
    cross = (sign != sign.shift(1)) & sign.shift(1).ne(0)
    idx = np.arange(len(close))
    last = pd.Series(np.where(cross.values, idx, np.nan), index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f09_mexh_012_rsi14_bear_div_count_252d(close: pd.Series) -> pd.Series:
    """Higher-high in price with lower RSI(14) count over 252d (long-horizon)."""
    r = _rsi_wilder(close, 14)
    hh_p = (close > close.rolling(63, min_periods=21).max().shift(1)).astype(int)
    rsi_lower = (r < r.rolling(63, min_periods=21).max().shift(1)).astype(int)
    div = (hh_p & rsi_lower).astype(float)
    return div.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_013_rsi25_bear_div_count_252d(close: pd.Series) -> pd.Series:
    """Higher-high in price with lower RSI(25) count over 252d."""
    r = _rsi_wilder(close, 25)
    hh_p = (close > close.rolling(63, min_periods=21).max().shift(1)).astype(int)
    rsi_lower = (r < r.rolling(63, min_periods=21).max().shift(1)).astype(int)
    div = (hh_p & rsi_lower).astype(float)
    return div.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_014_rsi14_max_minus_current_63d(close: pd.Series) -> pd.Series:
    """RSI(14) 63d rolling max minus current — fadeoff from peak RSI."""
    r = _rsi_wilder(close, 14)
    return r.rolling(QDAYS, min_periods=MDAYS).max() - r


def f09_mexh_015_rsi25_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI(25) within 252d."""
    r = _rsi_wilder(close, 25)
    return _rolling_pctrank(r, YDAYS)


def f09_mexh_016_rsi_cutler_25_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Cutler RSI(25) within 252d."""
    return _rolling_zscore(_rsi_cutler(close, 25), YDAYS)


def f09_mexh_017_rsi14_min_since_peak_63d(close: pd.Series) -> pd.Series:
    """Difference RSI(14) - rolling 63d min — distance off the floor."""
    r = _rsi_wilder(close, 14)
    return r - r.rolling(QDAYS, min_periods=MDAYS).min()


def f09_mexh_018_rsi_50_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of RSI(50)."""
    r = _rsi_wilder(close, 50)
    return _rolling_slope(r, MDAYS)


def f09_mexh_019_rsi14_above_70_streak_max_63d(close: pd.Series) -> pd.Series:
    """Max consecutive bars RSI(14)>70 over trailing 63d."""
    r = _rsi_wilder(close, 14)
    above = (r > 70).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)


def f09_mexh_020_rsi14_failed_overbought_breakout_count_252d(close: pd.Series) -> pd.Series:
    """Causal count over 252d: entries to RSI(14)>70 that within the next 5 bars saw RSI back <= 70 (observed at t=entry+5)."""
    r = _rsi_wilder(close, 14)
    enter = (r > 70) & (r.shift(1) <= 70)
    enter_lag5 = enter.shift(5).fillna(False)
    fell_below = (r <= 70).rolling(5, min_periods=1).max().astype(bool)
    failed = (enter_lag5 & fell_below).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_021_stoch_d_slow_21_3_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Slow %D (3-bar SMA of %K) on 21-period stoch."""
    return _stoch_d(close, high, low, 21, 3)


def f09_mexh_022_stoch_k_21_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic %K over 21 bars — medium-horizon stoch."""
    return _stoch_k(close, high, low, 21)


def f09_mexh_023_stoch_k_63_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic %K over 63 bars — quarterly stoch position."""
    return _stoch_k(close, high, low, 63)


def f09_mexh_024_stoch_k_252_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic %K over 252 bars — annual stoch position."""
    return _stoch_k(close, high, low, 252)


def f09_mexh_025_stoch_21_overbought_intensity_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (Stoch%K(21) - 80)+ over 63d."""
    k = _stoch_k(close, high, low, 21)
    return (k - 80).clip(lower=0).rolling(QDAYS, min_periods=MDAYS).mean()


def f09_mexh_026_stoch_63_overbought_intensity_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (Stoch%K(63) - 80)+ over 252d."""
    k = _stoch_k(close, high, low, 63)
    return (k - 80).clip(lower=0).rolling(YDAYS, min_periods=QDAYS).mean()


def f09_mexh_027_stoch_k_d_cross_count_252d_14_3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of %K/%D crossovers on (14,3) over 252d."""
    k = _stoch_k(close, high, low, 14)
    d = k.rolling(3, min_periods=1).mean()
    sign = np.sign((k - d).fillna(0))
    crosses = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return crosses.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_mexh_028_williams_r_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Williams %R over 50 bars."""
    hh = high.rolling(50, min_periods=max(50 // 3, 2)).max()
    ll = low.rolling(50, min_periods=max(50 // 3, 2)).min()
    return -100.0 * _safe_div(hh - close, hh - ll)


def f09_mexh_029_williams_r_252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Williams %R over 252 bars — annual position."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    return -100.0 * _safe_div(hh - close, hh - ll)


def f09_mexh_030_stoch_k_d_gap_63d_mean_14_3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63d mean of %K - %D gap on (14,3) — sustained divergence."""
    k = _stoch_k(close, high, low, 14)
    d = k.rolling(3, min_periods=1).mean()
    return (k - d).rolling(QDAYS, min_periods=MDAYS).mean()


def f09_mexh_031_stochrsi_14_value(close: pd.Series) -> pd.Series:
    """StochRSI on RSI(14) over 14-bar lookback."""
    r = _rsi_wilder(close, 14)
    return _safe_div(r - r.rolling(14, min_periods=5).min(), r.rolling(14, min_periods=5).max() - r.rolling(14, min_periods=5).min())


def f09_mexh_032_stochrsi_50_value(close: pd.Series) -> pd.Series:
    """StochRSI on RSI(50) over 50-bar lookback."""
    r = _rsi_wilder(close, 50)
    return _safe_div(r - r.rolling(50, min_periods=16).min(), r.rolling(50, min_periods=16).max() - r.rolling(50, min_periods=16).min())


def f09_mexh_033_stoch_21_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of Stoch%K(21) within 252d."""
    k = _stoch_k(close, high, low, 21)
    return _rolling_pctrank(k, YDAYS)


def f09_mexh_034_stoch_252_max_minus_current_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63d rolling max of Stoch%K(252) minus current — long-horizon fadeoff."""
    k = _stoch_k(close, high, low, 252)
    return k.rolling(QDAYS, min_periods=MDAYS).max() - k


def f09_mexh_035_williams_r_50_overbought_streak_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive bars %R(50) > -20 over trailing 63d."""
    hh = high.rolling(50, min_periods=max(50 // 3, 2)).max()
    ll = low.rolling(50, min_periods=max(50 // 3, 2)).min()
    wr = -100.0 * _safe_div(hh - close, hh - ll)
    above = (wr > -20).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)


def f09_mexh_036_stoch_div_count_63d_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Higher-high in price with lower Stoch%K(14) — 63d count."""
    k = _stoch_k(close, high, low, 14)
    hh_p = (close > close.rolling(21, min_periods=7).max().shift(1)).astype(int)
    lo_k = (k < k.rolling(21, min_periods=7).max().shift(1)).astype(int)
    div = (hh_p & lo_k).astype(float)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_mexh_037_full_stoch_5_3_3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Full stochastic %D over (5,3,3) — fastest version."""
    k = _stoch_k(close, high, low, 5)
    sk = k.rolling(3, min_periods=1).mean()
    return sk.rolling(3, min_periods=1).mean()


def f09_mexh_038_full_stoch_14_5_5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Full stochastic %D over (14,5,5)."""
    k = _stoch_k(close, high, low, 14)
    sk = k.rolling(5, min_periods=1).mean()
    return sk.rolling(5, min_periods=1).mean()


def f09_mexh_039_stoch_252_above_80_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63d Stoch%K(252) > 80."""
    k = _stoch_k(close, high, low, 252)
    return (k > 80).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f09_mexh_040_days_since_stoch_k14_crossed_d14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since Stoch%K(14)/%D(3) last crossed."""
    k = _stoch_k(close, high, low, 14)
    d = k.rolling(3, min_periods=1).mean()
    sign = np.sign((k - d).fillna(0))
    cross = (sign != sign.shift(1)) & sign.shift(1).ne(0)
    idx = np.arange(len(close))
    last = pd.Series(np.where(cross.values, idx, np.nan), index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f09_mexh_041_trix_15(close: pd.Series) -> pd.Series:
    """TRIX with 15-period triple EMA."""
    return _trix(close, 15)


def f09_mexh_042_trix_30(close: pd.Series) -> pd.Series:
    """TRIX with 30-period triple EMA — medium-horizon TRIX."""
    return _trix(close, 30)


def f09_mexh_043_trix_50(close: pd.Series) -> pd.Series:
    """TRIX with 50-period triple EMA — long-horizon TRIX."""
    return _trix(close, 50)


def f09_mexh_044_tsi_25_13(close: pd.Series) -> pd.Series:
    """True Strength Index (25,13)."""
    return _tsi(close, 25, 13)


def f09_mexh_045_tsi_50_25(close: pd.Series) -> pd.Series:
    """TSI(50,25) — slower TSI variant."""
    return _tsi(close, 50, 25)


def f09_mexh_046_ultimate_oscillator_7_14_28(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ultimate Oscillator (7,14,28)."""
    return _ultimate(close, high, low, 7, 14, 28)


def f09_mexh_047_ultimate_oscillator_14_28_56(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ultimate Oscillator (14,28,56) — longer horizon UO."""
    return _ultimate(close, high, low, 14, 28, 56)


def f09_mexh_048_awesome_oscillator_5_34(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Awesome Oscillator (5,34) on (H+L)/2."""
    return _awesome(high, low, 5, 34)


def f09_mexh_049_awesome_oscillator_21_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Awesome Oscillator (21,50) — slower."""
    return _awesome(high, low, 21, 50)


def f09_mexh_050_kst_classical(close: pd.Series) -> pd.Series:
    """Pring KST with classical params (10,15,20,30 / smoothed)."""
    return _kst(close)


def f09_mexh_051_dpo_21(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator with 21-period MA (causal-shifted)."""
    return _dpo(close, 21)


def f09_mexh_052_dpo_63(close: pd.Series) -> pd.Series:
    """DPO with 63-period MA."""
    return _dpo(close, 63)


def f09_mexh_053_dpo_126(close: pd.Series) -> pd.Series:
    """DPO with 126-period MA."""
    return _dpo(close, 126)


def f09_mexh_054_cmo_14(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (14)."""
    return _cmo(close, 14)


def f09_mexh_055_cmo_25(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (25)."""
    return _cmo(close, 25)


def f09_mexh_056_cmo_63(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (63) — long-horizon."""
    return _cmo(close, 63)


def f09_mexh_057_kvo_34_55(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator (34,55)."""
    return _kvo(high, low, close, volume, 34, 55)


def f09_mexh_058_stc_23_50_10(close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle (23,50,10)."""
    return _stc(close, 23, 50, 10)


def f09_mexh_059_coppock_curve(close: pd.Series) -> pd.Series:
    """Coppock Curve (ROC14+ROC11 smoothed 10)."""
    return _coppock(close, 14, 11, 10)


def f09_mexh_060_macd_50_100_signal_9(close: pd.Series) -> pd.Series:
    """MACD line (50,100) for long-horizon thrust."""
    return _ema(close, 50) - _ema(close, 100)


def f09_mexh_061_adx_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADX(14) — trend strength."""
    _p, _m, adx = _dmi(high, low, close, 14)
    return adx


def f09_mexh_062_adx_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADX(50) — long-horizon trend strength."""
    _p, _m, adx = _dmi(high, low, close, 50)
    return adx


def f09_mexh_063_plus_di_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+DI(14)."""
    p, _m, _a = _dmi(high, low, close, 14)
    return p


def f09_mexh_064_minus_di_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """-DI(14)."""
    _p, m, _a = _dmi(high, low, close, 14)
    return m


def f09_mexh_065_plus_minus_di_gap_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(+DI - -DI) on (14)."""
    p, m, _a = _dmi(high, low, close, 14)
    return p - m


def f09_mexh_066_plus_minus_di_gap_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(+DI - -DI) on (50) — long-horizon directional pressure."""
    p, m, _a = _dmi(high, low, close, 50)
    return p - m


def f09_mexh_067_adx_14_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of ADX(14) — trend-strength change."""
    _p, _m, adx = _dmi(high, low, close, 14)
    return _rolling_slope(adx, MDAYS)


def f09_mexh_068_vortex_vip_minus_vim_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Vortex VI+ - VI- (14)."""
    p, m = _vortex(high, low, close, 14)
    return p - m


def f09_mexh_069_vortex_vip_minus_vim_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Vortex VI+ - VI- (50)."""
    p, m = _vortex(high, low, close, 50)
    return p - m


def f09_mexh_070_mass_index_9_25(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index (9,25) — range expansion through ema ratio."""
    return _mass_index(high, low, 9, 25)


def f09_mexh_071_choppiness_14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Choppiness Index (14)."""
    return _choppiness(high, low, close, 14)


def f09_mexh_072_choppiness_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Choppiness Index (50) — long-horizon chop vs trend."""
    return _choppiness(high, low, close, 50)


def f09_mexh_073_aroon_up_25(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Up (25)."""
    up, _d = _aroon(high, low, 25)
    return up


def f09_mexh_074_aroon_down_25(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Down (25)."""
    _u, dn = _aroon(high, low, 25)
    return dn


def f09_mexh_075_aroon_oscillator_25(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator = AroonUp - AroonDown (25)."""
    up, dn = _aroon(high, low, 25)
    return up - dn


MOMENTUM_EXHAUSTION_BASE_REGISTRY_001_075 = {
    "f09_mexh_001_rsi_wilder_25_overbought_intensity_63d": {"inputs": ["close"], "func": f09_mexh_001_rsi_wilder_25_overbought_intensity_63d},
    "f09_mexh_002_rsi_wilder_50_overbought_intensity_63d": {"inputs": ["close"], "func": f09_mexh_002_rsi_wilder_50_overbought_intensity_63d},
    "f09_mexh_003_rsi_cutler_25_value": {"inputs": ["close"], "func": f09_mexh_003_rsi_cutler_25_value},
    "f09_mexh_004_rsi_cutler_50_value": {"inputs": ["close"], "func": f09_mexh_004_rsi_cutler_50_value},
    "f09_mexh_005_rsi_connors_3": {"inputs": ["close"], "func": f09_mexh_005_rsi_connors_3},
    "f09_mexh_006_rsi_smoothed_14_ema_5": {"inputs": ["close"], "func": f09_mexh_006_rsi_smoothed_14_ema_5},
    "f09_mexh_007_rsi_25_days_above_70_252d": {"inputs": ["close"], "func": f09_mexh_007_rsi_25_days_above_70_252d},
    "f09_mexh_008_rsi_25_days_above_80_252d": {"inputs": ["close"], "func": f09_mexh_008_rsi_25_days_above_80_252d},
    "f09_mexh_009_rsi_50_days_above_60_252d": {"inputs": ["close"], "func": f09_mexh_009_rsi_50_days_above_60_252d},
    "f09_mexh_010_days_since_rsi14_crossed_50": {"inputs": ["close"], "func": f09_mexh_010_days_since_rsi14_crossed_50},
    "f09_mexh_011_days_since_rsi25_crossed_70": {"inputs": ["close"], "func": f09_mexh_011_days_since_rsi25_crossed_70},
    "f09_mexh_012_rsi14_bear_div_count_252d": {"inputs": ["close"], "func": f09_mexh_012_rsi14_bear_div_count_252d},
    "f09_mexh_013_rsi25_bear_div_count_252d": {"inputs": ["close"], "func": f09_mexh_013_rsi25_bear_div_count_252d},
    "f09_mexh_014_rsi14_max_minus_current_63d": {"inputs": ["close"], "func": f09_mexh_014_rsi14_max_minus_current_63d},
    "f09_mexh_015_rsi25_pctrank_252d": {"inputs": ["close"], "func": f09_mexh_015_rsi25_pctrank_252d},
    "f09_mexh_016_rsi_cutler_25_zscore_252d": {"inputs": ["close"], "func": f09_mexh_016_rsi_cutler_25_zscore_252d},
    "f09_mexh_017_rsi14_min_since_peak_63d": {"inputs": ["close"], "func": f09_mexh_017_rsi14_min_since_peak_63d},
    "f09_mexh_018_rsi_50_slope_21d": {"inputs": ["close"], "func": f09_mexh_018_rsi_50_slope_21d},
    "f09_mexh_019_rsi14_above_70_streak_max_63d": {"inputs": ["close"], "func": f09_mexh_019_rsi14_above_70_streak_max_63d},
    "f09_mexh_020_rsi14_failed_overbought_breakout_count_252d": {"inputs": ["close"], "func": f09_mexh_020_rsi14_failed_overbought_breakout_count_252d},
    "f09_mexh_021_stoch_d_slow_21_3_value": {"inputs": ["close", "high", "low"], "func": f09_mexh_021_stoch_d_slow_21_3_value},
    "f09_mexh_022_stoch_k_21_value": {"inputs": ["close", "high", "low"], "func": f09_mexh_022_stoch_k_21_value},
    "f09_mexh_023_stoch_k_63_value": {"inputs": ["close", "high", "low"], "func": f09_mexh_023_stoch_k_63_value},
    "f09_mexh_024_stoch_k_252_value": {"inputs": ["close", "high", "low"], "func": f09_mexh_024_stoch_k_252_value},
    "f09_mexh_025_stoch_21_overbought_intensity_63d": {"inputs": ["close", "high", "low"], "func": f09_mexh_025_stoch_21_overbought_intensity_63d},
    "f09_mexh_026_stoch_63_overbought_intensity_252d": {"inputs": ["close", "high", "low"], "func": f09_mexh_026_stoch_63_overbought_intensity_252d},
    "f09_mexh_027_stoch_k_d_cross_count_252d_14_3": {"inputs": ["close", "high", "low"], "func": f09_mexh_027_stoch_k_d_cross_count_252d_14_3},
    "f09_mexh_028_williams_r_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_028_williams_r_50},
    "f09_mexh_029_williams_r_252": {"inputs": ["close", "high", "low"], "func": f09_mexh_029_williams_r_252},
    "f09_mexh_030_stoch_k_d_gap_63d_mean_14_3": {"inputs": ["close", "high", "low"], "func": f09_mexh_030_stoch_k_d_gap_63d_mean_14_3},
    "f09_mexh_031_stochrsi_14_value": {"inputs": ["close"], "func": f09_mexh_031_stochrsi_14_value},
    "f09_mexh_032_stochrsi_50_value": {"inputs": ["close"], "func": f09_mexh_032_stochrsi_50_value},
    "f09_mexh_033_stoch_21_pctrank_252d": {"inputs": ["close", "high", "low"], "func": f09_mexh_033_stoch_21_pctrank_252d},
    "f09_mexh_034_stoch_252_max_minus_current_63d": {"inputs": ["close", "high", "low"], "func": f09_mexh_034_stoch_252_max_minus_current_63d},
    "f09_mexh_035_williams_r_50_overbought_streak_max_63d": {"inputs": ["close", "high", "low"], "func": f09_mexh_035_williams_r_50_overbought_streak_max_63d},
    "f09_mexh_036_stoch_div_count_63d_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_036_stoch_div_count_63d_14},
    "f09_mexh_037_full_stoch_5_3_3": {"inputs": ["close", "high", "low"], "func": f09_mexh_037_full_stoch_5_3_3},
    "f09_mexh_038_full_stoch_14_5_5": {"inputs": ["close", "high", "low"], "func": f09_mexh_038_full_stoch_14_5_5},
    "f09_mexh_039_stoch_252_above_80_fraction_63d": {"inputs": ["close", "high", "low"], "func": f09_mexh_039_stoch_252_above_80_fraction_63d},
    "f09_mexh_040_days_since_stoch_k14_crossed_d14": {"inputs": ["close", "high", "low"], "func": f09_mexh_040_days_since_stoch_k14_crossed_d14},
    "f09_mexh_041_trix_15": {"inputs": ["close"], "func": f09_mexh_041_trix_15},
    "f09_mexh_042_trix_30": {"inputs": ["close"], "func": f09_mexh_042_trix_30},
    "f09_mexh_043_trix_50": {"inputs": ["close"], "func": f09_mexh_043_trix_50},
    "f09_mexh_044_tsi_25_13": {"inputs": ["close"], "func": f09_mexh_044_tsi_25_13},
    "f09_mexh_045_tsi_50_25": {"inputs": ["close"], "func": f09_mexh_045_tsi_50_25},
    "f09_mexh_046_ultimate_oscillator_7_14_28": {"inputs": ["close", "high", "low"], "func": f09_mexh_046_ultimate_oscillator_7_14_28},
    "f09_mexh_047_ultimate_oscillator_14_28_56": {"inputs": ["close", "high", "low"], "func": f09_mexh_047_ultimate_oscillator_14_28_56},
    "f09_mexh_048_awesome_oscillator_5_34": {"inputs": ["close", "high", "low"], "func": f09_mexh_048_awesome_oscillator_5_34},
    "f09_mexh_049_awesome_oscillator_21_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_049_awesome_oscillator_21_50},
    "f09_mexh_050_kst_classical": {"inputs": ["close"], "func": f09_mexh_050_kst_classical},
    "f09_mexh_051_dpo_21": {"inputs": ["close"], "func": f09_mexh_051_dpo_21},
    "f09_mexh_052_dpo_63": {"inputs": ["close"], "func": f09_mexh_052_dpo_63},
    "f09_mexh_053_dpo_126": {"inputs": ["close"], "func": f09_mexh_053_dpo_126},
    "f09_mexh_054_cmo_14": {"inputs": ["close"], "func": f09_mexh_054_cmo_14},
    "f09_mexh_055_cmo_25": {"inputs": ["close"], "func": f09_mexh_055_cmo_25},
    "f09_mexh_056_cmo_63": {"inputs": ["close"], "func": f09_mexh_056_cmo_63},
    "f09_mexh_057_kvo_34_55": {"inputs": ["close", "high", "low", "volume"], "func": f09_mexh_057_kvo_34_55},
    "f09_mexh_058_stc_23_50_10": {"inputs": ["close"], "func": f09_mexh_058_stc_23_50_10},
    "f09_mexh_059_coppock_curve": {"inputs": ["close"], "func": f09_mexh_059_coppock_curve},
    "f09_mexh_060_macd_50_100_signal_9": {"inputs": ["close"], "func": f09_mexh_060_macd_50_100_signal_9},
    "f09_mexh_061_adx_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_061_adx_14},
    "f09_mexh_062_adx_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_062_adx_50},
    "f09_mexh_063_plus_di_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_063_plus_di_14},
    "f09_mexh_064_minus_di_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_064_minus_di_14},
    "f09_mexh_065_plus_minus_di_gap_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_065_plus_minus_di_gap_14},
    "f09_mexh_066_plus_minus_di_gap_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_066_plus_minus_di_gap_50},
    "f09_mexh_067_adx_14_slope_21d": {"inputs": ["close", "high", "low"], "func": f09_mexh_067_adx_14_slope_21d},
    "f09_mexh_068_vortex_vip_minus_vim_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_068_vortex_vip_minus_vim_14},
    "f09_mexh_069_vortex_vip_minus_vim_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_069_vortex_vip_minus_vim_50},
    "f09_mexh_070_mass_index_9_25": {"inputs": ["high", "low"], "func": f09_mexh_070_mass_index_9_25},
    "f09_mexh_071_choppiness_14": {"inputs": ["close", "high", "low"], "func": f09_mexh_071_choppiness_14},
    "f09_mexh_072_choppiness_50": {"inputs": ["close", "high", "low"], "func": f09_mexh_072_choppiness_50},
    "f09_mexh_073_aroon_up_25": {"inputs": ["high", "low"], "func": f09_mexh_073_aroon_up_25},
    "f09_mexh_074_aroon_down_25": {"inputs": ["high", "low"], "func": f09_mexh_074_aroon_down_25},
    "f09_mexh_075_aroon_oscillator_25": {"inputs": ["high", "low"], "func": f09_mexh_075_aroon_oscillator_25},
}
