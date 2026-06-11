"""f19_atr_normalized_price base features 001-075.

Domain: ATR-normalized price -- every feature divides a price-derived
signal by Wilder's ATR(N) (or otherwise references ATR units) so that
the result is volatility-scaled. Includes ATR-units distances, body in
ATR units, gaps in ATR units, ATR ratios (vol-of-vol via ATR), ATR
Keltner channel position, ATR-normalized momentum, ATR-Sharpe-like,
drawdown / ATR, extreme-move detection in ATR units, ATR-units states
and bounded transforms (arctan/tanh/sigmoid) of |move|/ATR.

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at
the function's final return. Window > 21d uses closeadj; <=21d uses
close. Each feature spells its full formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers -- True Range / Wilder ATR / a couple of light primitives.
# Every feature still spells out its full formula inline.
# ---------------------------------------------------------------------------


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    """Wilder's ATR(N) = ewm(alpha=1/N) of TR with min_periods=N."""
    return _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === ATR-normalized level distances (close - MA) / ATR =====================

def f19an_f19_atr_normalized_price_close_sma8_atr14_base_v001_signal(high, low, close):
    """(close - SMA(close,8)) / ATR(14). Short level distance in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    sma = close.rolling(8, min_periods=8).mean()
    return ((close - sma) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_sma50_atr20_base_v002_signal(high, low, closeadj):
    """(closeadj - SMA(50)) / ATR(20). Mid-horizon level distance in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(50, min_periods=50).mean()
    return ((closeadj - sma) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sign_close_sma100_atr_base_v003_signal(high, low, closeadj):
    """sign((closeadj - SMA(100)) / ATR(50)) > 1 -> 1; < -1 -> -1; else 0. Discrete state."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    sma = closeadj.rolling(100, min_periods=100).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.where(z <= 1.0, 1.0)
    out = out.where(z >= -1.0, -1.0)
    return out.where(~z.isna()).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_sma200_atr100_base_v004_signal(high, low, closeadj):
    """(closeadj - SMA(200)) / ATR(100). Very long level distance in long-ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 100.0, adjust=False, min_periods=100).mean()
    sma = closeadj.rolling(200, min_periods=200).mean()
    return ((closeadj - sma) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized N-day returns (close - close.shift(N)) / ATR(N) =========

def f19an_f19_atr_normalized_price_ret5_atr5_base_v005_signal(high, low, close):
    """5-day price change in ATR(5) units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    return ((close - close.shift(5)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ret20_atr14_base_v006_signal(high, low, close):
    """20-day price change in ATR(14) units. Classic Schaff-style normalized momentum."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((close - close.shift(20)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ret63_atr30_base_v007_signal(high, low, closeadj):
    """63-day return in ATR(30) units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    return ((closeadj - closeadj.shift(63)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized distance to recent high / low ==========================

def f19an_f19_atr_normalized_price_dist_high20_atr14_base_v008_signal(high, low, close):
    """(close - rolling_max(high,20)) / ATR(14). Distance to 20d high in ATR units (<=0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    hh = high.rolling(20, min_periods=20).max()
    return ((close - hh) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_low20_atr14_base_v009_signal(high, low, close):
    """(close - rolling_min(low,20)) / ATR(14). Distance to 20d low in ATR units (>=0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    ll = low.rolling(20, min_periods=20).min()
    return ((close - ll) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dist_high60_atr30_base_v010_signal(high, low, closeadj):
    """(closeadj - rolling_max(high,60)) / ATR(30)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    hh = high.rolling(60, min_periods=60).max()
    return ((closeadj - hh) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dayssince_120d_low_base_v011_signal(high, low, closeadj):
    """Days since the 120d low. Counts position-in-cycle rather than distance.
    ATR-domain via: capped by ATR-units-distance band: cap at 120 if no fresh low.
    Domain: ATR-units context -- bar is considered 'fresh low' if (close - prior_low)/ATR(20) drops below 0."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    prior_low = low.rolling(120, min_periods=120).min().shift(1)
    fresh = ((closeadj - prior_low) / atr.replace(0.0, np.nan) < 0.0).astype(float).where(~atr.isna() & ~prior_low.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return fresh.rolling(120, min_periods=120).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized differentials (MA - MA') / ATR =========================

def f19an_f19_atr_normalized_price_sma5_sma20_atr14_base_v012_signal(high, low, close):
    """(SMA(5) - SMA(20)) / ATR(14). Fast-slow MA spread in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    s5 = close.rolling(5, min_periods=5).mean()
    s20 = close.rolling(20, min_periods=20).mean()
    return ((s5 - s20) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_xover_count_macd_atr_60d_base_v013_signal(high, low, close):
    """Number of sign-changes of (EMA12-EMA26)/ATR14 over 60d. Crossing frequency, discrete."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    e12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    e26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    z = (e12 - e26) / atr.replace(0.0, np.nan)
    s = np.sign(z)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sma50_sma200_atr50_base_v014_signal(high, low, closeadj):
    """(SMA(50) - SMA(200)) / ATR(50). Golden/death cross magnitude in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    s50 = closeadj.rolling(50, min_periods=50).mean()
    s200 = closeadj.rolling(200, min_periods=200).mean()
    return ((s50 - s200) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized intra-bar quantities ===================================

def f19an_f19_atr_normalized_price_hl_atr14_base_v015_signal(high, low, close):
    """(high - low) / ATR(14). Today's range as fraction of typical ATR."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((high - low) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_body_atr10_base_v016_signal(high, low, close, open):
    """(close - open) / ATR(10). Body in ATR units (signed)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 10.0, adjust=False, min_periods=10).mean()
    return ((close - open) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_upwick_atr14_base_v017_signal(high, low, close, open):
    """(high - max(open, close)) / ATR(14). Upper wick in ATR units (>=0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    top = pd.concat([open, close], axis=1).max(axis=1)
    return ((high - top) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_lowwick_atr14_base_v018_signal(high, low, close, open):
    """(min(open,close) - low) / ATR(14). Lower wick in ATR units (>=0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    bot = pd.concat([open, close], axis=1).min(axis=1)
    return ((bot - low) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized gap =====================================================

def f19an_f19_atr_normalized_price_gap_atr14_base_v019_signal(high, low, close, open):
    """(open - prev_close) / ATR(14). Overnight gap in ATR units (signed)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((open - pc) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_abs_gap_atr14_base_v020_signal(high, low, close, open):
    """|open - prev_close| / ATR(14). Unsigned overnight gap magnitude in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((open - pc).abs() / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR ratios (vol regime via ATR) =======================================

def f19an_f19_atr_normalized_price_atr5_atr50_base_v021_signal(high, low, close):
    """ATR(5) / ATR(50). Short-vs-long ATR vol regime ratio."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a5 = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a50 = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    return (a5 / a50.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr20_atr200_base_v022_signal(high, low, closeadj):
    """ATR(20) / ATR(200). Medium-vs-very-long ATR regime ratio."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a20 = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    a200 = tr.ewm(alpha=1.0 / 200.0, adjust=False, min_periods=200).mean()
    return (a20 / a200.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_log_atr10_atr100_base_v023_signal(high, low, closeadj):
    """log(ATR(10) / ATR(100)). Log ATR regime ratio (~ symmetric around 0)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a10 = tr.ewm(alpha=1.0 / 10.0, adjust=False, min_periods=10).mean()
    a100 = tr.ewm(alpha=1.0 / 100.0, adjust=False, min_periods=100).mean()
    return np.log(a10 / a100.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_slope_norm_30d_base_v024_signal(high, low, closeadj):
    """(ATR(14) - ATR(14).shift(30)) / ATR(14). ATR slope normalized by ATR."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((a - a.shift(30)) / a.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Keltner channel position (close - midpoint) / (width * ATR) ===========

def f19an_f19_atr_normalized_price_keltner_pos_20d_base_v025_signal(high, low, close):
    """%K position in Keltner band: (close - (SMA(20) - 2*ATR(20))) / (4*ATR(20)).
    0 at lower band, 1 at upper band."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    mid = close.rolling(20, min_periods=20).mean()
    lower = mid - 2.0 * atr
    width = 4.0 * atr
    return ((close - lower) / width.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_since_atr_band_break_120d_base_v026_signal(high, low, closeadj):
    """Days since close last broke SMA(60) +/- 2*ATR(30) band, capped at 120."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(60, min_periods=60).mean()
    flag = ((closeadj > sma + 2.0 * atr) | (closeadj < sma - 2.0 * atr)).astype(float).where(~atr.isna() & ~sma.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(120, min_periods=120).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized momentum (ROC / ATR) ===================================

def f19an_f19_atr_normalized_price_roc10_atr10_base_v027_signal(high, low, close):
    """log return over 10d divided by (ATR(10)/close). Volatility-scaled momentum."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 10.0, adjust=False, min_periods=10).mean()
    roc = np.log(close / close.shift(10))
    atr_pct = atr / close.replace(0.0, np.nan)
    return (roc / atr_pct.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_cumret_cumatr_30d_base_v028_signal(high, low, closeadj):
    """cumulative-return-over-30d / cumulative-TR-over-30d  -- moves vs typical moves."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    csum_tr = tr.rolling(30, min_periods=30).sum()
    csum_ret = (closeadj - closeadj.shift(30))
    return (csum_ret / csum_tr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sharpe-like (return / ATR) ============================================

def f19an_f19_atr_normalized_price_signed_count_atr_30d_base_v029_signal(high, low, close):
    """Sum of sign((ret/ATR14) > 0.5) - sign((ret/ATR14) < -0.5) over 30d. Bias of ATR moves."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (close - pc) / atr.replace(0.0, np.nan)
    pos = (z > 0.5).astype(float).where(~z.isna())
    neg = (z < -0.5).astype(float).where(~z.isna())
    return (pos - neg).rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_residual_acf_80d_base_v030_signal(high, low, closeadj):
    """Lag-5 autocorr of (closeadj - SMA(20))/ATR(20) over 80d. Mean-reversion vs. trend in ATR."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(20, min_periods=20).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    return z.rolling(80, min_periods=80).corr(z.shift(5)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized drawdown ===============================================

def f19an_f19_atr_normalized_price_dd_severity_count_atr_60d_base_v031_signal(high, low, closeadj):
    """Count of bars in last 60d where drawdown-from-60d-peak exceeded 2*ATR(30). Stress count."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    peak = closeadj.rolling(60, min_periods=60).max()
    dd = (peak - closeadj) / atr.replace(0.0, np.nan)
    flag = (dd > 2.0).astype(float).where(~dd.isna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_rally_strength_atr_120d_base_v032_signal(high, low, closeadj):
    """sign(close - close.shift(120)) * count_bars(120d) where (close - close.shift(20))/ATR(20) > 1.
    Combines direction over 120d with frequency of 1-ATR up-pushes."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    direction = np.sign(closeadj - closeadj.shift(120))
    push = ((closeadj - closeadj.shift(20)) / atr.replace(0.0, np.nan) > 1.0).astype(float).where(~atr.isna())
    return (direction * push.rolling(120, min_periods=120).sum()).replace([np.inf, -np.inf], np.nan)


# === Extreme-move detection (|move| / ATR) =================================

def f19an_f19_atr_normalized_price_absret1_atr14_base_v033_signal(high, low, close):
    """|close - close.shift(1)| / ATR(14). One-day move magnitude in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return ((close - pc).abs() / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_max_absret_atr_20d_base_v034_signal(high, low, close):
    """max(|daily ret|) over 20d / ATR(20). Worst single-day shock in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    ar = (close - pc).abs()
    mx = ar.rolling(20, min_periods=20).max()
    return (mx / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_min_ret_atr_60d_base_v035_signal(high, low, closeadj):
    """min(daily return) over 60d / ATR(30). Signed worst-down shock in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    r = closeadj - pc
    mn = r.rolling(60, min_periods=60).min()
    return (mn / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Counts of ATR-extreme events ==========================================

def f19an_f19_atr_normalized_price_count_1atr_30d_base_v036_signal(high, low, close):
    """count of bars (out of 30) where |daily ret| > ATR(14). 1-sigma-ATR event count."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    flag = ((close - pc).abs() > atr).astype(float).where(~atr.isna() & ~pc.isna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_count_2atr_60d_base_v037_signal(high, low, closeadj):
    """count of bars (out of 60) where |daily ret| > 2*ATR(20). Tail-event count."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    flag = ((closeadj - pc).abs() > 2.0 * atr).astype(float).where(~atr.isna() & ~pc.isna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_dayssince_2atr_120d_base_v038_signal(high, low, closeadj):
    """Days since last bar where |daily ret| > 2*ATR(14)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    flag = ((closeadj - pc).abs() > 2.0 * atr).astype(float).where(~atr.isna() & ~pc.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(120, min_periods=120).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# === Signed ATR-units (close vs MA with slope sign) =========================

def f19an_f19_atr_normalized_price_signed_dist_sma40_atr14_base_v039_signal(high, low, closeadj):
    """((closeadj - SMA(40)) / ATR(14)) * sign(SMA(40) - SMA(40).shift(10)).
    Distance signed by trend direction."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    m = closeadj.rolling(40, min_periods=40).mean()
    raw = (closeadj - m) / atr.replace(0.0, np.nan)
    direction = np.sign(m - m.shift(10))
    return (raw * direction).replace([np.inf, -np.inf], np.nan)


# === ATR vol-of-vol ========================================================

def f19an_f19_atr_normalized_price_std_atr_60d_norm_base_v040_signal(high, low, closeadj):
    """std(ATR(14), 60) / ATR(14). Vol-of-vol from ATR."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    sd = atr.rolling(60, min_periods=60).std()
    return (sd / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_diff_pct_50d_base_v041_signal(high, low, closeadj):
    """ATR(20).diff(50) / ATR(20). Long-horizon ATR change ratio."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    return (atr.diff(50) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Discrete ATR regime states ============================================

def f19an_f19_atr_normalized_price_atr_regime_252d_base_v042_signal(high, low, closeadj):
    """ATR regime: 0 = ATR(14) in low quartile vs 252d, 2 = high quartile, else 1."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    q25 = atr.rolling(252, min_periods=252).quantile(0.25)
    q75 = atr.rolling(252, min_periods=252).quantile(0.75)
    out = pd.Series(1.0, index=atr.index, dtype=float)
    out = out.where(atr <= q75, 2.0)
    out = out.where(atr >= q25, 0.0)
    return out.where(~q25.isna() & ~q75.isna() & ~atr.isna()).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_days_in_high_atr_252d_base_v043_signal(high, low, closeadj):
    """Fraction of last 60 bars where ATR(14) > median(ATR(14), 252) (elevated ATR)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    med = atr.rolling(252, min_periods=252).median()
    flag = (atr > med).astype(float).where(~atr.isna() & ~med.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Bounded transforms of move/ATR ========================================

def f19an_f19_atr_normalized_price_arctan_absret1_atr_60d_avg_base_v044_signal(high, low, close):
    """Rolling 60d mean of (2/pi)*arctan(|daily ret| / ATR(14)). Average bounded shock magnitude."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (close - pc).abs() / atr.replace(0.0, np.nan)
    bz = 2.0 / np.pi * np.arctan(z)
    return bz.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tanh_ret60_atr80_base_v045_signal(high, low, closeadj):
    """tanh((closeadj - closeadj.shift(60)) / (3*ATR(80))). Bounded long-horizon ATR-momentum."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 80.0, adjust=False, min_periods=80).mean()
    z = (closeadj - closeadj.shift(60)) / (3.0 * atr).replace(0.0, np.nan)
    return np.tanh(z).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_sigmoid_zatr_30d_base_v046_signal(high, low, closeadj):
    """1/(1+exp(-z)) where z = ((closeadj - SMA(30)) / ATR(30)) - 0. Sigmoid of ATR-z."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(30, min_periods=30).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    z = z.clip(-50.0, 50.0)
    return (1.0 / (1.0 + np.exp(-z))).replace([np.inf, -np.inf], np.nan)


# === Cross-vol-estimator (ATR vs std-returns / Parkinson) ==================

def f19an_f19_atr_normalized_price_atr_pct_vs_stdret_30d_base_v047_signal(high, low, closeadj):
    """(ATR(20)/closeadj) / std(daily log return, 30). ATR vs realized vol estimator."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    r = np.log(closeadj / pc)
    sd = r.rolling(30, min_periods=30).std()
    atr_pct = atr / closeadj.replace(0.0, np.nan)
    return (atr_pct / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units distance to median/quantile of close =======================

def f19an_f19_atr_normalized_price_streak_above_sma_atr_band_60d_base_v048_signal(high, low, closeadj):
    """Current run length (in bars) of closeadj above SMA(30) + 0.5*ATR(30). Capped 60."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(30, min_periods=30).mean()
    above = (closeadj > sma + 0.5 * atr).astype(float).where(~atr.isna() & ~sma.isna())
    def _streak_pos(x):
        idx = np.where(x < 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return above.rolling(60, min_periods=60).apply(_streak_pos, raw=True).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_streak_below_atr_band_60d_base_v049_signal(high, low, closeadj):
    """Current run length (in bars) of closeadj below SMA(30) - 0.5*ATR(30). Capped 60."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(30, min_periods=30).mean()
    below = (closeadj < sma - 0.5 * atr).astype(float).where(~atr.isna() & ~sma.isna())
    def _streak_pos(x):
        idx = np.where(x < 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return below.rolling(60, min_periods=60).apply(_streak_pos, raw=True).replace([np.inf, -np.inf], np.nan)


# === Rolling typical-price normalization ==================================

def f19an_f19_atr_normalized_price_typical_minus_close_atr14_base_v050_signal(high, low, close):
    """((high+low+close)/3 - close) / ATR(14). Today's typical-price displacement vs close."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    tp = (high + low + close) / 3.0
    return ((tp - close) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized cumulative TR vs cumulative range =====================

def f19an_f19_atr_normalized_price_tr_atr14_base_v051_signal(high, low, close):
    """TR / ATR(14). Today's TR in typical ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return (tr / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_tr_atr_max60d_base_v052_signal(high, low, closeadj):
    """max(TR, 60) / ATR(60). Worst single TR over 60d in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    mx = tr.rolling(60, min_periods=60).max()
    return (mx / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized rolling standard deviation of close ====================

def f19an_f19_atr_normalized_price_stdclose_atr_30d_base_v053_signal(high, low, closeadj):
    """std(closeadj, 30) / ATR(30). Price dispersion in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    return (sd / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sign features in ATR thresholds =======================================

def f19an_f19_atr_normalized_price_above_1atr_sma20_base_v054_signal(high, low, close):
    """1 if close > SMA(20) + ATR(14), -1 if close < SMA(20) - ATR(14), else 0.
    Discrete trend confirmation in ATR-band."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    sma = close.rolling(20, min_periods=20).mean()
    upper = sma + atr
    lower = sma - atr
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(close <= upper, 1.0)
    out = out.where(close >= lower, -1.0)
    return out.where(~atr.isna() & ~sma.isna()).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_above_2atr_sma50_base_v055_signal(high, low, closeadj):
    """1 if closeadj > SMA(50) + 2*ATR(50), -1 if < SMA(50) - 2*ATR(50), else 0."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    sma = closeadj.rolling(50, min_periods=50).mean()
    upper = sma + 2.0 * atr
    lower = sma - 2.0 * atr
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.where(closeadj <= upper, 1.0)
    out = out.where(closeadj >= lower, -1.0)
    return out.where(~atr.isna() & ~sma.isna()).replace([np.inf, -np.inf], np.nan)


# === Skew / kurt of return/ATR ============================================

def f19an_f19_atr_normalized_price_skew_retatr_60d_base_v056_signal(high, low, closeadj):
    """Skewness of (daily return / ATR(14)) over 60d. Tail asymmetry in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_kurt_retatr_120d_base_v057_signal(high, low, closeadj):
    """Kurtosis of (daily return / ATR(14)) over 120d. Tail fatness in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# === ATR-normalized open-close-vs-range ===================================

def f19an_f19_atr_normalized_price_open_close_diff_atr_5d_base_v058_signal(high, low, close, open):
    """(close - open).rolling(5).sum() / (5 * ATR(5)). Body persistence in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    body_sum = (close - open).rolling(5, min_periods=5).sum()
    return (body_sum / (5.0 * atr).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-normalized rank ==================================================

def f19an_f19_atr_normalized_price_rank_close_sma20_atr_60d_base_v059_signal(high, low, closeadj):
    """Rolling 60d rank (pct) of (closeadj - SMA(20)) / ATR(20). Bounded [0,1]."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(20, min_periods=20).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    return z.rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === ATR-units fraction of bars positive ===================================

def f19an_f19_atr_normalized_price_frac_above_atr_band_30d_base_v060_signal(high, low, closeadj):
    """Fraction of last 30 bars with closeadj > SMA(30) + 0.5*ATR(30)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(30, min_periods=30).mean()
    flag = (closeadj > sma + 0.5 * atr).astype(float).where(~atr.isna() & ~sma.isna())
    return flag.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Signed extremes / position-from-mid ===================================

def f19an_f19_atr_normalized_price_range_width_60d_in_atr_base_v061_signal(high, low, closeadj):
    """(high.rolling(60).max() - low.rolling(60).min()) / ATR(30). 60d span in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    hh = high.rolling(60, min_periods=60).max()
    ll = low.rolling(60, min_periods=60).min()
    return ((hh - ll) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Multi-window ATR-units feature ========================================

def f19an_f19_atr_normalized_price_pos_minus_neg_atr_eventfreq_120d_base_v062_signal(high, low, closeadj):
    """(count of bars with ret/ATR14>1 minus count with ret/ATR14<-1) over 120d.
    Net up-shock count in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    pos = (z > 1.0).astype(float).where(~z.isna())
    neg = (z < -1.0).astype(float).where(~z.isna())
    return (pos - neg).rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Sharpe-like (down-side ATR) ===========================================

def f19an_f19_atr_normalized_price_neg_ret_count_atr_30d_base_v063_signal(high, low, closeadj):
    """count of bars over 30d with (closeadj - pc)/ATR(14) < -1. Down-side ATR-event count."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    flag = (z < -1.0).astype(float).where(~atr.isna() & ~pc.isna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === ATR-Z autocorrelation ================================================

def f19an_f19_atr_normalized_price_autocorr_retatr_50d_base_v064_signal(high, low, closeadj):
    """Rolling 50d autocorr (lag 1) of (return / ATR(14))."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(50, min_periods=50).corr(z.shift(1)).replace([np.inf, -np.inf], np.nan)


# === ATR-units crossing frequency ==========================================

def f19an_f19_atr_normalized_price_atrband_crosses_40d_base_v065_signal(high, low, closeadj):
    """Number of bars in last 40d where close crossed the SMA(20)+/-ATR(20) band edges."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(20, min_periods=20).mean()
    upper = sma + atr
    lower = sma - atr
    state = pd.Series(0.0, index=closeadj.index, dtype=float)
    state = state.where(closeadj <= upper, 1.0)
    state = state.where(closeadj >= lower, -1.0)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    return flip.rolling(40, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)




# === ATR-units displacement of EMA ribbon ==================================

def f19an_f19_atr_normalized_price_ema_ribbon_disp_atr_50d_base_v067_signal(high, low, closeadj):
    """(max(EMA10,EMA20,EMA40) - min(...)) / ATR(30). Ribbon dispersion in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    e10 = closeadj.ewm(span=10, adjust=False, min_periods=10).mean()
    e20 = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    e40 = closeadj.ewm(span=40, adjust=False, min_periods=40).mean()
    mat = pd.concat([e10, e20, e40], axis=1)
    span = mat.max(axis=1) - mat.min(axis=1)
    return (span / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Distance to high-ATR / low-ATR ========================================

def f19an_f19_atr_normalized_price_high_minus_close_atr_5d_base_v068_signal(high, low, close):
    """(high - close) / ATR(5). Today's pullback from high in short-ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    return ((high - close) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_minus_low_atr_5d_base_v069_signal(high, low, close):
    """(close - low) / ATR(5). Today's bounce from low in short-ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    return ((close - low) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR slope quartile ratio =============================================

def f19an_f19_atr_normalized_price_atr_q90_q10_120d_base_v070_signal(high, low, closeadj):
    """log( q90(ATR(20),120) / q10(ATR(20),120) ). ATR distribution width over 120d."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    q90 = atr.rolling(120, min_periods=120).quantile(0.9)
    q10 = atr.rolling(120, min_periods=120).quantile(0.1)
    return np.log(q90 / q10.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units gap-fill measure ===========================================

def f19an_f19_atr_normalized_price_gapfill_atr_5d_base_v071_signal(high, low, close, open):
    """(close - open) / ATR(14)  --  intraday recovery / shock in ATR units, but distinct
    structure from body via SMA filter: sign((open - prev_close)) * (close - open) / ATR(14).
    """
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    gap_sign = np.sign(open - pc)
    return (-1.0 * gap_sign * (close - open) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Underwater-time x ATR ================================================

def f19an_f19_atr_normalized_price_underwater_atr_60d_base_v072_signal(high, low, closeadj):
    """(days_since_60d_peak) * (peak - closeadj)/ATR(30)/60. Time-weighted DD in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    peak = closeadj.rolling(60, min_periods=60).max()
    def _dsp(x):
        idx = int(np.argmax(x))
        return float(len(x) - 1 - idx)
    dsp = closeadj.rolling(60, min_periods=60).apply(_dsp, raw=True)
    return (dsp * (peak - closeadj) / (60.0 * atr).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === EMA distance ratio with widely-spaced ATR ============================

def f19an_f19_atr_normalized_price_macd_above_signal_atr_60d_base_v073_signal(high, low, closeadj):
    """Fraction of last 60d that ((EMA12-EMA26) - EMA9(EMA12-EMA26))/ATR(14) > 0.
    Histogram-positive rate, an ATR-units MACD-histogram regime."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    e12 = closeadj.ewm(span=12, adjust=False, min_periods=12).mean()
    e26 = closeadj.ewm(span=26, adjust=False, min_periods=26).mean()
    macd = e12 - e26
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = (macd - sig) / atr.replace(0.0, np.nan)
    flag = (hist > 0.0).astype(float).where(~hist.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Bounded transform of ATR ratio =======================================

def f19an_f19_atr_normalized_price_atr_rank_252d_base_v074_signal(high, low, closeadj):
    """Rolling 252d rank (pct) of ATR(14). Where current ATR sits in its 1-year history."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return a.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === ATR-units mean reversion z-score =====================================

def f19an_f19_atr_normalized_price_reversion_z_atr_45d_base_v075_signal(high, low, closeadj):
    """Mean of (closeadj - SMA(45))/ATR(20) - last value of same. Mean-reversion residual."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(45, min_periods=45).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    return (z - z.rolling(45, min_periods=45).mean()).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f19_atr_normalized_price_base_001_075_REGISTRY = {
    "f19an_f19_atr_normalized_price_close_sma8_atr14_base_v001_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_close_sma8_atr14_base_v001_signal},
    "f19an_f19_atr_normalized_price_close_sma50_atr20_base_v002_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_close_sma50_atr20_base_v002_signal},
    "f19an_f19_atr_normalized_price_sign_close_sma100_atr_base_v003_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_sign_close_sma100_atr_base_v003_signal},
    "f19an_f19_atr_normalized_price_close_sma200_atr100_base_v004_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_close_sma200_atr100_base_v004_signal},
    "f19an_f19_atr_normalized_price_ret5_atr5_base_v005_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_ret5_atr5_base_v005_signal},
    "f19an_f19_atr_normalized_price_ret20_atr14_base_v006_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_ret20_atr14_base_v006_signal},
    "f19an_f19_atr_normalized_price_ret63_atr30_base_v007_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_ret63_atr30_base_v007_signal},
    "f19an_f19_atr_normalized_price_dist_high20_atr14_base_v008_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_dist_high20_atr14_base_v008_signal},
    "f19an_f19_atr_normalized_price_dist_low20_atr14_base_v009_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_dist_low20_atr14_base_v009_signal},
    "f19an_f19_atr_normalized_price_dist_high60_atr30_base_v010_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_dist_high60_atr30_base_v010_signal},
    "f19an_f19_atr_normalized_price_dayssince_120d_low_base_v011_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_dayssince_120d_low_base_v011_signal},
    "f19an_f19_atr_normalized_price_sma5_sma20_atr14_base_v012_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_sma5_sma20_atr14_base_v012_signal},
    "f19an_f19_atr_normalized_price_xover_count_macd_atr_60d_base_v013_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_xover_count_macd_atr_60d_base_v013_signal},
    "f19an_f19_atr_normalized_price_sma50_sma200_atr50_base_v014_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_sma50_sma200_atr50_base_v014_signal},
    "f19an_f19_atr_normalized_price_hl_atr14_base_v015_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_hl_atr14_base_v015_signal},
    "f19an_f19_atr_normalized_price_body_atr10_base_v016_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_body_atr10_base_v016_signal},
    "f19an_f19_atr_normalized_price_upwick_atr14_base_v017_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_upwick_atr14_base_v017_signal},
    "f19an_f19_atr_normalized_price_lowwick_atr14_base_v018_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_lowwick_atr14_base_v018_signal},
    "f19an_f19_atr_normalized_price_gap_atr14_base_v019_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_gap_atr14_base_v019_signal},
    "f19an_f19_atr_normalized_price_abs_gap_atr14_base_v020_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_abs_gap_atr14_base_v020_signal},
    "f19an_f19_atr_normalized_price_atr5_atr50_base_v021_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_atr5_atr50_base_v021_signal},
    "f19an_f19_atr_normalized_price_atr20_atr200_base_v022_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr20_atr200_base_v022_signal},
    "f19an_f19_atr_normalized_price_log_atr10_atr100_base_v023_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_log_atr10_atr100_base_v023_signal},
    "f19an_f19_atr_normalized_price_atr_slope_norm_30d_base_v024_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_slope_norm_30d_base_v024_signal},
    "f19an_f19_atr_normalized_price_keltner_pos_20d_base_v025_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_keltner_pos_20d_base_v025_signal},
    "f19an_f19_atr_normalized_price_days_since_atr_band_break_120d_base_v026_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_days_since_atr_band_break_120d_base_v026_signal},
    "f19an_f19_atr_normalized_price_roc10_atr10_base_v027_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_roc10_atr10_base_v027_signal},
    "f19an_f19_atr_normalized_price_cumret_cumatr_30d_base_v028_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_cumret_cumatr_30d_base_v028_signal},
    "f19an_f19_atr_normalized_price_signed_count_atr_30d_base_v029_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_signed_count_atr_30d_base_v029_signal},
    "f19an_f19_atr_normalized_price_atr_residual_acf_80d_base_v030_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_residual_acf_80d_base_v030_signal},
    "f19an_f19_atr_normalized_price_dd_severity_count_atr_60d_base_v031_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_dd_severity_count_atr_60d_base_v031_signal},
    "f19an_f19_atr_normalized_price_rally_strength_atr_120d_base_v032_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_rally_strength_atr_120d_base_v032_signal},
    "f19an_f19_atr_normalized_price_absret1_atr14_base_v033_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_absret1_atr14_base_v033_signal},
    "f19an_f19_atr_normalized_price_max_absret_atr_20d_base_v034_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_max_absret_atr_20d_base_v034_signal},
    "f19an_f19_atr_normalized_price_min_ret_atr_60d_base_v035_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_min_ret_atr_60d_base_v035_signal},
    "f19an_f19_atr_normalized_price_count_1atr_30d_base_v036_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_count_1atr_30d_base_v036_signal},
    "f19an_f19_atr_normalized_price_count_2atr_60d_base_v037_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_count_2atr_60d_base_v037_signal},
    "f19an_f19_atr_normalized_price_dayssince_2atr_120d_base_v038_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_dayssince_2atr_120d_base_v038_signal},
    "f19an_f19_atr_normalized_price_signed_dist_sma40_atr14_base_v039_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_signed_dist_sma40_atr14_base_v039_signal},
    "f19an_f19_atr_normalized_price_std_atr_60d_norm_base_v040_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_std_atr_60d_norm_base_v040_signal},
    "f19an_f19_atr_normalized_price_atr_diff_pct_50d_base_v041_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_diff_pct_50d_base_v041_signal},
    "f19an_f19_atr_normalized_price_atr_regime_252d_base_v042_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_regime_252d_base_v042_signal},
    "f19an_f19_atr_normalized_price_days_in_high_atr_252d_base_v043_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_days_in_high_atr_252d_base_v043_signal},
    "f19an_f19_atr_normalized_price_arctan_absret1_atr_60d_avg_base_v044_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_arctan_absret1_atr_60d_avg_base_v044_signal},
    "f19an_f19_atr_normalized_price_tanh_ret60_atr80_base_v045_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_tanh_ret60_atr80_base_v045_signal},
    "f19an_f19_atr_normalized_price_sigmoid_zatr_30d_base_v046_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_sigmoid_zatr_30d_base_v046_signal},
    "f19an_f19_atr_normalized_price_atr_pct_vs_stdret_30d_base_v047_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_pct_vs_stdret_30d_base_v047_signal},
    "f19an_f19_atr_normalized_price_streak_above_sma_atr_band_60d_base_v048_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_streak_above_sma_atr_band_60d_base_v048_signal},
    "f19an_f19_atr_normalized_price_streak_below_atr_band_60d_base_v049_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_streak_below_atr_band_60d_base_v049_signal},
    "f19an_f19_atr_normalized_price_typical_minus_close_atr14_base_v050_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_typical_minus_close_atr14_base_v050_signal},
    "f19an_f19_atr_normalized_price_tr_atr14_base_v051_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_tr_atr14_base_v051_signal},
    "f19an_f19_atr_normalized_price_tr_atr_max60d_base_v052_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_tr_atr_max60d_base_v052_signal},
    "f19an_f19_atr_normalized_price_stdclose_atr_30d_base_v053_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_stdclose_atr_30d_base_v053_signal},
    "f19an_f19_atr_normalized_price_above_1atr_sma20_base_v054_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_above_1atr_sma20_base_v054_signal},
    "f19an_f19_atr_normalized_price_above_2atr_sma50_base_v055_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_above_2atr_sma50_base_v055_signal},
    "f19an_f19_atr_normalized_price_skew_retatr_60d_base_v056_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_skew_retatr_60d_base_v056_signal},
    "f19an_f19_atr_normalized_price_kurt_retatr_120d_base_v057_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_kurt_retatr_120d_base_v057_signal},
    "f19an_f19_atr_normalized_price_open_close_diff_atr_5d_base_v058_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_open_close_diff_atr_5d_base_v058_signal},
    "f19an_f19_atr_normalized_price_rank_close_sma20_atr_60d_base_v059_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_rank_close_sma20_atr_60d_base_v059_signal},
    "f19an_f19_atr_normalized_price_frac_above_atr_band_30d_base_v060_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_frac_above_atr_band_30d_base_v060_signal},
    "f19an_f19_atr_normalized_price_range_width_60d_in_atr_base_v061_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_range_width_60d_in_atr_base_v061_signal},
    "f19an_f19_atr_normalized_price_pos_minus_neg_atr_eventfreq_120d_base_v062_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_pos_minus_neg_atr_eventfreq_120d_base_v062_signal},
    "f19an_f19_atr_normalized_price_neg_ret_count_atr_30d_base_v063_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_neg_ret_count_atr_30d_base_v063_signal},
    "f19an_f19_atr_normalized_price_autocorr_retatr_50d_base_v064_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_autocorr_retatr_50d_base_v064_signal},
    "f19an_f19_atr_normalized_price_atrband_crosses_40d_base_v065_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atrband_crosses_40d_base_v065_signal},
    "f19an_f19_atr_normalized_price_ema_ribbon_disp_atr_50d_base_v067_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_ema_ribbon_disp_atr_50d_base_v067_signal},
    "f19an_f19_atr_normalized_price_high_minus_close_atr_5d_base_v068_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_high_minus_close_atr_5d_base_v068_signal},
    "f19an_f19_atr_normalized_price_close_minus_low_atr_5d_base_v069_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_close_minus_low_atr_5d_base_v069_signal},
    "f19an_f19_atr_normalized_price_atr_q90_q10_120d_base_v070_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_q90_q10_120d_base_v070_signal},
    "f19an_f19_atr_normalized_price_gapfill_atr_5d_base_v071_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_gapfill_atr_5d_base_v071_signal},
    "f19an_f19_atr_normalized_price_underwater_atr_60d_base_v072_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_underwater_atr_60d_base_v072_signal},
    "f19an_f19_atr_normalized_price_macd_above_signal_atr_60d_base_v073_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_macd_above_signal_atr_60d_base_v073_signal},
    "f19an_f19_atr_normalized_price_atr_rank_252d_base_v074_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_rank_252d_base_v074_signal},
    "f19an_f19_atr_normalized_price_reversion_z_atr_45d_base_v075_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_reversion_z_atr_45d_base_v075_signal},
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
    for name, entry in f19_atr_normalized_price_base_001_075_REGISTRY.items():
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
