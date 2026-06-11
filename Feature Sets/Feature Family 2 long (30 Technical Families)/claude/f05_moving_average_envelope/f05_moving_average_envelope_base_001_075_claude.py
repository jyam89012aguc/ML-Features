"""f05_moving_average_envelope base features 001-075.

Domain: MOVING AVERAGE ENVELOPES — features about the band/channel
that surrounds a moving average. An envelope is MA +/- k*width, where
width is a volatility/deviation/percent measure. This file covers
Bollinger Bands (%B, width, squeeze, touches, walks), Keltner Channels
(ATR-anchored), fixed-percent envelopes, asymmetric envelopes built
from positive/negative deviations, multi-scale envelope differentials,
volatility-anchored envelopes (Parkinson, Garman-Klass, range-quantile)
and TTM-squeeze (BB inside KC) signals.

Every feature references BOTH a moving average AND a band-width.
None is a pure close-vs-MA distance (that is f01's domain) nor a
pure rolling high-low position (f02's domain).

NaN policy: never fillna(0); only replace([inf,-inf], nan) at return.
Windows > 21d use closeadj; windows <= 21d use close (or unadjusted
OHLC inside-bar where applicable).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Envelope helpers. Each builds a named band component. Features below
# spell their formula inline; helpers only construct the band pieces.
# ---------------------------------------------------------------------------


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


def _parkinson(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    r = np.log(high / low.replace(0.0, np.nan))
    var = (r ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var)


def _garman_klass(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    hl = np.log(high / low.replace(0.0, np.nan)) ** 2
    co = np.log(close / open_.replace(0.0, np.nan)) ** 2
    daily = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    var = daily.rolling(n, min_periods=n).mean()
    return np.sqrt(var.clip(lower=0.0))


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: Bollinger %B at varied N and k (4) ---------------------------


def f05me_f05_moving_average_envelope_bbpctb_10d_base_v001_signal(close: pd.Series) -> pd.Series:
    """%B over BB(10, 2): (close - (SMA10 - 2*std10)) / (4*std10). Bounded."""
    sma = close.rolling(10, min_periods=10).mean()
    sd = close.rolling(10, min_periods=10).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    out = (close - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbcross_50d_base_v002_signal(closeadj: pd.Series) -> pd.Series:
    """Number of BB(50,2) median crossings in trailing 50 bars: count of
    sign-flips of (close - SMA50). Crossing frequency is a regime feature
    — bounded integer, structurally distinct from band-position."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sign = np.sign(closeadj - sma)
    flip = (sign * sign.shift(1) < 0).astype(float)
    out = flip.rolling(50, min_periods=25).sum()
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbpctb_200d_base_v003_signal(closeadj: pd.Series) -> pd.Series:
    """%B over BB(200, 2): long-horizon band position, regime feature."""
    sma = closeadj.rolling(200, min_periods=200).mean()
    sd = closeadj.rolling(200, min_periods=200).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    out = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbpctb1_20d_base_v004_signal(close: pd.Series) -> pd.Series:
    """%B with INNER 1-sigma band (k=1) at N=20. Same MA, narrower band ->
    structurally distinct sensitivity vs the 2-sigma variant."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 1.0 * sd
    lower = sma - 1.0 * sd
    out = (close - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: BB width and width dynamics (5) ------------------------------


def f05me_f05_moving_average_envelope_bbwid_20d_base_v005_signal(close: pd.Series) -> pd.Series:
    """BB(20, 2) width / SMA: (4*std)/SMA. Volatility relative to level."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    out = (4.0 * sd) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbwidrnk_120d_base_v006_signal(closeadj: pd.Series) -> pd.Series:
    """Rank of BB(20,2) width within trailing 120 bars. 0..1, regime-style."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.rolling(120, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbwslp_30d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of BB(20,2) width over 10 bars, normalized: diff(10)/level.
    Captures band expansion vs contraction."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.diff(10) / width.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbsqz_120d_base_v008_signal(closeadj: pd.Series) -> pd.Series:
    """Bollinger squeeze flag: 1.0 when current BB(20,2) width is in the
    bottom decile of the trailing 120-bar distribution, else 0."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    rk = width.rolling(120, min_periods=60).rank(pct=True)
    out = (rk <= 0.10).astype(float)
    out[rk.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbwcurv_40d_base_v009_signal(closeadj: pd.Series) -> pd.Series:
    """Curvature of BB(20,2) width: w - 2*w.shift(10) + w.shift(20)
    normalized by w. Width acceleration."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = (width - 2.0 * width.shift(10) + width.shift(20)) / width.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: Band-touch / band-walk / days-since (8) ----------------------


def f05me_f05_moving_average_envelope_dsupper_60d_base_v010_signal(close: pd.Series) -> pd.Series:
    """Days since last close >= BB(20,2) upper. 0..N. Decays with time."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    touch = (close >= upper).astype(int)
    # days-since via cummax of index*touch
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dslower_60d_base_v011_signal(close: pd.Series) -> pd.Series:
    """Days since last close <= BB(20,2) lower."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    touch = (close <= lower).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_walkup_20d_base_v012_signal(close: pd.Series) -> pd.Series:
    """Streak of consecutive bars closing above BB(20,2) upper band
    ("walking the band" — strong-trend signature)."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    above = (close > upper).astype(int)
    grp = (above == 0).cumsum()
    cnt = above.groupby(grp).cumcount() + 1
    out = cnt.where(above == 1, 0).astype(float)
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_walkdn_20d_base_v013_signal(close: pd.Series) -> pd.Series:
    """Streak of consecutive bars closing below BB(20,2) lower band."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    below = (close < lower).astype(int)
    grp = (below == 0).cumsum()
    cnt = below.groupby(grp).cumcount() + 1
    out = cnt.where(below == 1, 0).astype(float)
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_touchcnt_50d_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    """Number of BB(20,2) upper-band touches in trailing 50 bars."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    touch = (closeadj >= upper).astype(float)
    out = touch.rolling(50, min_periods=50).sum()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_touchasy_50d_base_v015_signal(closeadj: pd.Series) -> pd.Series:
    """Touch asymmetry: (upper touches - lower touches) / 50 over BB(20,2)
    in trailing 50 bars. -1..+1."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    up = (closeadj >= upper).astype(float).rolling(50, min_periods=50).sum()
    dn = (closeadj <= lower).astype(float).rolling(50, min_periods=50).sum()
    out = (up - dn) / 50.0
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_rejtop_30d_base_v016_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Rejection at top: bar where high touched BB(20,2) upper but close
    finished inside the band, count over 30 bars."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    flag = ((high >= upper) & (close < upper)).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_rejbot_30d_base_v017_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """Rejection at bottom: bar where low touched BB(20,2) lower but close
    finished inside the band, count over 30 bars."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    flag = ((low <= lower) & (close > lower)).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: Keltner Channels (5) -----------------------------------------


def f05me_f05_moving_average_envelope_kcbreak_20d_base_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Discrete Keltner-channel breakout state at 2*ATR14 around EMA(20):
    +1 if close > upper, -1 if close < lower, 0 inside. Three-state
    KC-state feature — structurally distinct from continuous %K position."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr
    lower = ema - 2.0 * atr
    out = (close > upper).astype(float) - (close < lower).astype(float)
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwid_30d_base_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner width in EMA units: (upper - lower)/EMA = 4*ATR/EMA."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    out = (4.0 * atr) / ema.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_ttmsqz_120d_base_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM squeeze: 1 when BB(20,2) is fully INSIDE KC(20, 2*ATR14):
    upper_bb < upper_kc AND lower_bb > lower_kc."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    atr = _atr(high, low, close, 14)
    up_bb = sma + 2.0 * sd
    lo_bb = sma - 2.0 * sd
    up_kc = ema + 2.0 * atr
    lo_kc = ema - 2.0 * atr
    flag = ((up_bb < up_kc) & (lo_bb > lo_kc)).astype(float)
    flag[up_bb.isna() | up_kc.isna()] = np.nan
    return flag.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwidrnk_120d_base_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Rank of Keltner width in trailing 120 bars (regime feature)."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    width = (4.0 * atr) / ema.replace(0.0, np.nan)
    out = width.rolling(120, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcdsup_60d_base_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since last close >= Keltner upper band."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr
    touch = (close >= upper).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: Fixed-percent envelopes (5) ----------------------------------


def f05me_f05_moving_average_envelope_pctstreak_20d_base_v023_signal(close: pd.Series) -> pd.Series:
    """Streak of consecutive bars closing above +1.5% SMA(20) envelope —
    persistent upside-breach run length. Integer streak, structurally
    distinct from continuous distance to the band."""
    sma = close.rolling(20, min_periods=20).mean()
    upper = 1.015 * sma
    above = (close > upper).astype(int)
    grp = (above == 0).cumsum()
    cnt = above.groupby(grp).cumcount() + 1
    out = cnt.where(above == 1, 0).astype(float)
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctenvstate_50d_base_v024_signal(closeadj: pd.Series) -> pd.Series:
    """Discrete pct-envelope state on SMA(50) with ±3% band: +1 above
    upper, -1 below lower, 0 inside band. Three-state regime feature
    — structurally distinct from continuous distance."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    upper = 1.03 * sma
    lower = 0.97 * sma
    out = (closeadj > upper).astype(float) - (closeadj < lower).astype(float)
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctenvbrk_60d_base_v025_signal(closeadj: pd.Series) -> pd.Series:
    """Pct envelope break count: in 60 bars, count of (close > 1.02*SMA20)
    plus count of (close < 0.98*SMA20). Both-side breach intensity."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    up = (closeadj > 1.02 * sma).astype(float)
    dn = (closeadj < 0.98 * sma).astype(float)
    out = (up + dn).rolling(60, min_periods=60).sum()
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctenvst_30d_base_v026_signal(close: pd.Series) -> pd.Series:
    """Streak of consecutive bars outside the ±2% SMA(30) envelope (either
    side). Persistent breakout intensity."""
    sma = close.rolling(30, min_periods=30).mean()
    out_flag = ((close > 1.02 * sma) | (close < 0.98 * sma)).astype(int)
    grp = (out_flag == 0).cumsum()
    cnt = out_flag.groupby(grp).cumcount() + 1
    out = cnt.where(out_flag == 1, 0).astype(float)
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctenvfrac_60d_base_v027_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 60d where close is OUTSIDE the ±3%
    SMA(60) envelope. 0..1 — a band-occupancy rate, structurally distinct
    from any band-position feature."""
    sma = closeadj.rolling(60, min_periods=60).mean()
    upper = 1.03 * sma
    lower = 0.97 * sma
    outflag = ((closeadj > upper) | (closeadj < lower)).astype(float)
    out = outflag.rolling(60, min_periods=60).mean()
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: Asymmetric envelopes from up/down deviations (5) ------------


def f05me_f05_moving_average_envelope_asyp_20d_base_v028_signal(close: pd.Series) -> pd.Series:
    """Asymmetric envelope position. Upper = SMA + 2*EMA(positive dev, 20).
    Lower = SMA - 2*EMA(negative dev, 20). %B-style position."""
    sma = close.rolling(20, min_periods=20).mean()
    dev = close - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev
    lower = sma - 2.0 * dn_dev
    out = (close - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_asyskew_30d_base_v029_signal(closeadj: pd.Series) -> pd.Series:
    """Skewness of band: (upper_dev - lower_dev)/(upper_dev + lower_dev),
    -1..+1. Captures whether positive deviations dominate."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).rolling(30, min_periods=30).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).rolling(30, min_periods=30).mean()
    out = (up_dev - dn_dev) / (up_dev + dn_dev).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_asywdrnk_30d_base_v030_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of the asymmetric-envelope upside fraction
    up_dev / (up_dev + dn_dev) within trailing 80 bars. Bounded 0..1.
    Captures whether the upside-dev contribution to the band is
    historically high — distinct from any continuous width feature."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=30, adjust=False, min_periods=30).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=30, adjust=False, min_periods=30).mean()
    frac = up_dev / (up_dev + dn_dev).replace(0.0, np.nan)
    out = frac.rolling(80, min_periods=40).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_asybrk_50d_base_v031_signal(closeadj: pd.Series) -> pd.Series:
    """Asymmetric upper-band break count over 50 bars, where the upper
    band uses positive-deviation EMA(20). Distinct from BB upper-touch
    (which is symmetric and std-based)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev
    flag = (closeadj > upper).astype(float)
    out = flag.rolling(50, min_periods=50).sum()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_asylobrk_50d_base_v032_signal(closeadj: pd.Series) -> pd.Series:
    """Asymmetric lower-band break count over 50 bars (negative-dev EMA)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    dev = closeadj - sma
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    lower = sma - 2.0 * dn_dev
    flag = (closeadj < lower).astype(float)
    out = flag.rolling(50, min_periods=50).sum()
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: Volatility-anchored envelopes (Parkinson, GK) (4) -----------


def f05me_f05_moving_average_envelope_parkrnk_120d_base_v033_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile-rank of Parkinson(20) envelope half-width within trailing
    120 bars. Width-regime signal using range-based vol (orthogonal to BB
    width which is std-based). Bounded 0..1."""
    pk = _parkinson(high, low, 20)
    out = pk.rolling(120, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_parkwid_30d_base_v034_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Parkinson envelope width: (4*Parkinson(30)*closeadj)/SMA(30)."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    pk = _parkinson(high, low, 30)
    out = (4.0 * pk * closeadj) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_gkwidrat_20d_base_v035_signal(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of Garman-Klass envelope half-width to BB(20,2) half-width.
    Compares OHLC-vol envelope sizing vs close-std envelope sizing —
    orthogonal to either width alone, and not a position feature."""
    gk = _garman_klass(open_, high, low, close, 20)
    sd = close.rolling(20, min_periods=20).std()
    gk_half = gk * close
    bb_half = 2.0 * sd
    out = gk_half / bb_half.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pkdays_60d_base_v036_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Days since last close >= Parkinson-anchored upper band:
    SMA(30) + 2*Parkinson(30)*close. Time-since signal — structurally
    distinct from any width ratio or %B feature."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    pk = _parkinson(high, low, 30)
    upper = sma + 2.0 * pk * closeadj
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: Range-quantile / MAD envelopes (3) --------------------------


def f05me_f05_moving_average_envelope_madenv_30d_base_v037_signal(closeadj: pd.Series) -> pd.Series:
    """%B over MAD envelope: SMA(30) ± 2*MAD(30). MAD is robust to outliers
    vs std-based BB — different shape under fat tails."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    mad = (closeadj - sma).abs().rolling(30, min_periods=30).mean()
    upper = sma + 2.0 * mad
    lower = sma - 2.0 * mad
    out = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_iqrasy_40d_base_v038_signal(closeadj: pd.Series) -> pd.Series:
    """Quantile-band asymmetry on 40d window: (Q3 - median) - (median - Q1)
    normalized by IQR. Sign + magnitude of distributional skew within the
    envelope — distinct from any %B feature."""
    q1 = closeadj.rolling(40, min_periods=40).quantile(0.25)
    med = closeadj.rolling(40, min_periods=40).median()
    q3 = closeadj.rolling(40, min_periods=40).quantile(0.75)
    iqr = q3 - q1
    out = ((q3 - med) - (med - q1)) / iqr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_qbnd_60d_base_v039_signal(closeadj: pd.Series) -> pd.Series:
    """Quantile-band signature: distance from SMA(30) to 95th-percentile
    of closeadj in 60 bars, normalized by SMA. Width-style feature using
    extreme quantile rather than std."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    q95 = closeadj.rolling(60, min_periods=60).quantile(0.95)
    out = (q95 - sma) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: Envelope dynamics (slopes/curvatures of bands themselves) (4)


def f05me_f05_moving_average_envelope_upslp_30d_base_v040_signal(closeadj: pd.Series) -> pd.Series:
    """Normalized slope of BB(20,2) UPPER band: upper.diff(10)/upper.
    Captures upper-band direction (distinct from price slope or MA slope)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    out = upper.diff(10) / upper.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_loslp_30d_base_v041_signal(closeadj: pd.Series) -> pd.Series:
    """Normalized slope of BB(20,2) LOWER band: lower.diff(10)/lower."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    out = lower.diff(10) / lower.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bndsdif_30d_base_v042_signal(closeadj: pd.Series) -> pd.Series:
    """Difference of upper-band slope minus lower-band slope (BB 20,2).
    Positive = bands diverging, negative = converging."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    out = upper.diff(10) / sma.replace(0.0, np.nan) - lower.diff(10) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_upcurv_60d_base_v043_signal(closeadj: pd.Series) -> pd.Series:
    """Curvature of BB(20,2) upper band: u - 2*u.shift(10) + u.shift(20),
    normalized by u. Acceleration of the upper-band path."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    out = (upper - 2.0 * upper.shift(10) + upper.shift(20)) / upper.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: Multi-scale band differentials (4) --------------------------


def f05me_f05_moving_average_envelope_innband_20d_base_v044_signal(close: pd.Series) -> pd.Series:
    """Fraction of close-bars inside the INNER 1-sigma SMA(20) band over a
    trailing 20-bar window. 0..1. A persistence-style 'middle band'
    occupancy that is structurally distinct from raw %B."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 1.0 * sd
    lower = sma - 1.0 * sd
    inside = ((close <= upper) & (close >= lower)).astype(float)
    out = inside.rolling(20, min_periods=20).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widrat_50d_base_v045_signal(closeadj: pd.Series) -> pd.Series:
    """Width ratio: BB(20,2) width / BB(50,2) width. Short vs long
    vol regime — independent of price level."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    w20 = (4.0 * sd20) / sma20.replace(0.0, np.nan)
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    w50 = (4.0 * sd50) / sma50.replace(0.0, np.nan)
    out = w20 / w50.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbdiff_50d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    """%B(20,2) - %B(50,2). Differential band position across scales."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    pb20 = (closeadj - (sma20 - 2.0 * sd20)) / (4.0 * sd20).replace(0.0, np.nan)
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    pb50 = (closeadj - (sma50 - 2.0 * sd50)) / (4.0 * sd50).replace(0.0, np.nan)
    out = pb20 - pb50
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widdiff_100d_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    """BB(50,2) width minus BB(100,2) width, normalized by long width.
    Captures contraction/expansion across two long scales."""
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    w50 = (4.0 * sd50) / sma50.replace(0.0, np.nan)
    sma100 = closeadj.rolling(100, min_periods=100).mean()
    sd100 = closeadj.rolling(100, min_periods=100).std()
    w100 = (4.0 * sd100) / sma100.replace(0.0, np.nan)
    out = (w50 - w100) / w100.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: Sign / discrete state on bands (5) --------------------------


def f05me_f05_moving_average_envelope_signupper_20d_base_v048_signal(close: pd.Series) -> pd.Series:
    """sign(close - BB(20,2) upper). +1 above, 0 at, -1 below."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    out = np.sign(close - upper)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_signlower_50d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    """sign(close - BB(50,2) lower). Long-band lower-side state."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    lower = sma - 2.0 * sd
    out = np.sign(closeadj - lower)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_quad_30d_base_v050_signal(close: pd.Series) -> pd.Series:
    """BB position quadrant: 2*sign(close - SMA20) + sign(BB-width.diff(5)).
    4-state regime: above-band-expanding, above-contracting, below-expanding,
    below-contracting."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = 2.0 * np.sign(close - sma) + np.sign(width.diff(5))
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_breakdir_60d_base_v051_signal(closeadj: pd.Series) -> pd.Series:
    """Recent BB(20,2) breakout direction: +1 if last 5d had upper touch
    with no lower touch, -1 reverse, 0 otherwise."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    upn = (closeadj >= upper).astype(float).rolling(5, min_periods=5).sum()
    dnn = (closeadj <= lower).astype(float).rolling(5, min_periods=5).sum()
    out = (upn > 0).astype(float) * (dnn == 0).astype(float) - (dnn > 0).astype(float) * (upn == 0).astype(float)
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_sqzbrk_60d_base_v052_signal(closeadj: pd.Series) -> pd.Series:
    """Squeeze-and-break signal: 1 if BB-width was in bottom decile 5 bars
    ago AND price now outside the band. Volatility expansion alert."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    rk = width.rolling(60, min_periods=30).rank(pct=True)
    sqz_then = (rk.shift(5) <= 0.10).astype(float)
    outside = ((closeadj > sma + 2.0 * sd) | (closeadj < sma - 2.0 * sd)).astype(float)
    out = sqz_then * outside
    out[rk.shift(5).isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: Envelope vs price normalized stats (5) ----------------------


def f05me_f05_moving_average_envelope_madwid_30d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of MAD(30) to std(30) — a width-style quality of fit metric
    for the band. For Gaussian noise this is ~0.798; deviations from that
    indicate fat tails. Distinct from any %B or width-level feature."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    mad = (closeadj - sma).abs().rolling(30, min_periods=30).mean()
    out = mad / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbpath_60d_base_v054_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 60 where close was OUTSIDE BB(20,2).
    0..1. Distinct from raw touch count: this is a fraction-based shape."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    flag = ((closeadj > upper) | (closeadj < lower)).astype(float)
    out = flag.rolling(60, min_periods=60).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbex_30d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    """Excursion outside BB(20,2): rolling sum of max(0, close-upper)+
    max(0, lower-close) over 30 bars, normalized by SMA. Magnitude not count."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    out = excess.rolling(30, min_periods=30).sum() / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbrank_60d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of %B(20,2) within trailing 60 bars. Persistence/
    extremity of band position vs its own recent distribution."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = pb.rolling(60, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widdrawd_120d_base_v057_signal(closeadj: pd.Series) -> pd.Series:
    """BB(20,2) width drawdown: 1 - (current_width / max_width_120d).
    0 at fresh-high width, ~1 deep contraction. Bounded; structurally
    distinct from rank — drawdown shape is non-linear and asymmetric."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    peak = width.rolling(120, min_periods=60).max()
    out = 1.0 - (width / peak.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: Combined band & MA-slope (3) --------------------------------


def f05me_f05_moving_average_envelope_walknet_60d_base_v058_signal(closeadj: pd.Series) -> pd.Series:
    """Net band-walk: (#bars at upper - #bars at lower) over 60d on BB(20,2).
    Signed walking-the-band intensity."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    up = (closeadj > upper).astype(float).rolling(60, min_periods=60).sum()
    dn = (closeadj < lower).astype(float).rolling(60, min_periods=60).sum()
    out = (up - dn) / 60.0
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widnorm_30d_base_v059_signal(closeadj: pd.Series) -> pd.Series:
    """BB(30,2) width divided by current ATR(14) — measures whether the
    close-std band is wider/narrower than the range-based ATR band."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    width_abs = 4.0 * sd
    atr = closeadj.diff().abs().ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    out = width_abs / (atr * 4.0).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widslp_50d_base_v060_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of BB(50,2) width-slope (diff(10)) in 50d.
    Captures whether vol is expanding more than usual."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    slp = width.diff(10)
    out = slp.rolling(50, min_periods=25).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: Multi-MA ensemble bands (3) ---------------------------------


def f05me_f05_moving_average_envelope_kcbbwrat_30d_base_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """KC-vs-BB width ratio at 30d. Compares ATR-based KC half-width to
    std-based BB half-width at the same SMA(30) anchor. < 1 -> ATR is
    narrower (TTM-squeeze conditions). Pure width-shape feature, not a
    position feature."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    atr = _atr(high, low, close, 20)
    out = atr / sd.replace(0.0, np.nan)
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_donchma_50d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    """Donchian-on-MA position: where the SMA(20) sits inside its own
    rolling 50-bar high/low range. Bounded 0..1; the MA's regime within
    a Donchian-style envelope of itself."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    hi = sma.rolling(50, min_periods=50).max()
    lo = sma.rolling(50, min_periods=50).min()
    out = (sma - lo) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_donchmawid_50d_base_v063_signal(closeadj: pd.Series) -> pd.Series:
    """Width of the Donchian envelope around SMA(20) over 50 bars,
    normalized: (max-min)/SMA. The MA's own travel-range."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    hi = sma.rolling(50, min_periods=50).max()
    lo = sma.rolling(50, min_periods=50).min()
    out = (hi - lo) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: Envelope-conditional statistical features (4) ---------------


def f05me_f05_moving_average_envelope_pbskew_60d_base_v064_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling skewness of %B(20,2) over 60 bars. Distribution shape of
    band-position — orthogonal to band level."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = pb.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widac_60d_base_v065_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of BB(20,2) width across 60 bars. Persistence
    of volatility regimes."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widkurt_60d_base_v066_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling kurtosis of BB(20,2) width over 60 bars. High = sporadic
    width spikes; low = smooth width evolution."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.rolling(60, min_periods=60).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbvar_30d_base_v067_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling std of %B(20,2) in 30 bars. Volatility of band position —
    captures how quickly price swings inside the envelope."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = pb.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: Cross-kernel envelope features (3) --------------------------


def f05me_f05_moving_average_envelope_emasmadif_20d_base_v068_signal(close: pd.Series) -> pd.Series:
    """Normalized gap between EMA(20) and SMA(20) centers expressed in
    BB(20,2) half-widths: (EMA - SMA)/(2*std). Captures center-skew of
    the envelope — small for symmetric data, large in strong trends.
    Distinct from any %B or width feature."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    out = (ema - sma) / (2.0 * sd).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widema_30d_base_v069_signal(closeadj: pd.Series) -> pd.Series:
    """Width of EMA(30) Bollinger band normalized: 4*EMAstd / EMA. Where
    the std itself is exponentially-weighted (sqrt of EWM-variance)."""
    ema = closeadj.ewm(span=30, adjust=False, min_periods=30).mean()
    var = (closeadj - ema).pow(2).ewm(span=30, adjust=False, min_periods=30).mean()
    sd = np.sqrt(var)
    out = (4.0 * sd) / ema.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_walkbeyond_30d_base_v070_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 30 where close > BB(20,2.5) upper —
    a TIGHTER outside-walk definition (k=2.5 cuts touches sharply)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.5 * sd
    flag = (closeadj > upper).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: Range-distance and volatility-of-volatility (5) -------------


def f05me_f05_moving_average_envelope_widmad_50d_base_v071_signal(closeadj: pd.Series) -> pd.Series:
    """Width measured via MAD/SMA at N=50. Robust envelope-width proxy."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    mad = (closeadj - sma).abs().rolling(50, min_periods=50).mean()
    out = (4.0 * mad) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_envtilt_30d_base_v072_signal(closeadj: pd.Series) -> pd.Series:
    """Envelope tilt: ratio of upper-band slope to lower-band slope for
    asymmetric envelope (upper from +dev, lower from -dev). Signed."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    dev = closeadj - sma
    up_dev = dev.where(dev > 0, 0.0).ewm(span=20, adjust=False, min_periods=20).mean()
    dn_dev = (-dev.where(dev < 0, 0.0)).ewm(span=20, adjust=False, min_periods=20).mean()
    upper = sma + 2.0 * up_dev
    lower = sma - 2.0 * dn_dev
    out = upper.diff(10) / lower.diff(10).abs().replace(0.0, np.nan)
    out = np.sign(lower.diff(10)) * out
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widvol_60d_base_v073_signal(closeadj: pd.Series) -> pd.Series:
    """Vol-of-vol: rolling std of BB(20,2) width over 60 bars normalized
    by the mean width. Coefficient of variation of the band width."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    m = width.rolling(60, min_periods=60).mean()
    s = width.rolling(60, min_periods=60).std()
    out = s / m.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_distup_30d_base_v074_signal(closeadj: pd.Series) -> pd.Series:
    """Normalized distance from close to BB(20,2) upper: (upper-close)/upper.
    Always >0 inside the band; <0 above. Inverted band-room metric."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    out = (upper - closeadj) / upper.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_distlo_50d_base_v075_signal(closeadj: pd.Series) -> pd.Series:
    """Normalized distance from close to BB(50,2) lower: (close-lower)/lower.
    Always >0 above the lower band; <0 below."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    lower = sma - 2.0 * sd
    out = (closeadj - lower) / lower.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f05_moving_average_envelope_base_001_075_REGISTRY = {
    "f05me_f05_moving_average_envelope_bbpctb_10d_base_v001_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_bbpctb_10d_base_v001_signal},
    "f05me_f05_moving_average_envelope_bbcross_50d_base_v002_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbcross_50d_base_v002_signal},
    "f05me_f05_moving_average_envelope_bbpctb_200d_base_v003_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbpctb_200d_base_v003_signal},
    "f05me_f05_moving_average_envelope_bbpctb1_20d_base_v004_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_bbpctb1_20d_base_v004_signal},
    "f05me_f05_moving_average_envelope_bbwid_20d_base_v005_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_bbwid_20d_base_v005_signal},
    "f05me_f05_moving_average_envelope_bbwidrnk_120d_base_v006_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbwidrnk_120d_base_v006_signal},
    "f05me_f05_moving_average_envelope_bbwslp_30d_base_v007_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbwslp_30d_base_v007_signal},
    "f05me_f05_moving_average_envelope_bbsqz_120d_base_v008_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbsqz_120d_base_v008_signal},
    "f05me_f05_moving_average_envelope_bbwcurv_40d_base_v009_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbwcurv_40d_base_v009_signal},
    "f05me_f05_moving_average_envelope_dsupper_60d_base_v010_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_dsupper_60d_base_v010_signal},
    "f05me_f05_moving_average_envelope_dslower_60d_base_v011_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_dslower_60d_base_v011_signal},
    "f05me_f05_moving_average_envelope_walkup_20d_base_v012_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_walkup_20d_base_v012_signal},
    "f05me_f05_moving_average_envelope_walkdn_20d_base_v013_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_walkdn_20d_base_v013_signal},
    "f05me_f05_moving_average_envelope_touchcnt_50d_base_v014_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_touchcnt_50d_base_v014_signal},
    "f05me_f05_moving_average_envelope_touchasy_50d_base_v015_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_touchasy_50d_base_v015_signal},
    "f05me_f05_moving_average_envelope_rejtop_30d_base_v016_signal": {"inputs": ["high", "close"], "func": f05me_f05_moving_average_envelope_rejtop_30d_base_v016_signal},
    "f05me_f05_moving_average_envelope_rejbot_30d_base_v017_signal": {"inputs": ["low", "close"], "func": f05me_f05_moving_average_envelope_rejbot_30d_base_v017_signal},
    "f05me_f05_moving_average_envelope_kcbreak_20d_base_v018_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcbreak_20d_base_v018_signal},
    "f05me_f05_moving_average_envelope_kcwid_30d_base_v019_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcwid_30d_base_v019_signal},
    "f05me_f05_moving_average_envelope_ttmsqz_120d_base_v020_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_ttmsqz_120d_base_v020_signal},
    "f05me_f05_moving_average_envelope_kcwidrnk_120d_base_v021_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcwidrnk_120d_base_v021_signal},
    "f05me_f05_moving_average_envelope_kcdsup_60d_base_v022_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcdsup_60d_base_v022_signal},
    "f05me_f05_moving_average_envelope_pctstreak_20d_base_v023_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_pctstreak_20d_base_v023_signal},
    "f05me_f05_moving_average_envelope_pctenvstate_50d_base_v024_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pctenvstate_50d_base_v024_signal},
    "f05me_f05_moving_average_envelope_pctenvbrk_60d_base_v025_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pctenvbrk_60d_base_v025_signal},
    "f05me_f05_moving_average_envelope_pctenvst_30d_base_v026_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_pctenvst_30d_base_v026_signal},
    "f05me_f05_moving_average_envelope_pctenvfrac_60d_base_v027_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pctenvfrac_60d_base_v027_signal},
    "f05me_f05_moving_average_envelope_asyp_20d_base_v028_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_asyp_20d_base_v028_signal},
    "f05me_f05_moving_average_envelope_asyskew_30d_base_v029_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_asyskew_30d_base_v029_signal},
    "f05me_f05_moving_average_envelope_asywdrnk_30d_base_v030_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_asywdrnk_30d_base_v030_signal},
    "f05me_f05_moving_average_envelope_asybrk_50d_base_v031_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_asybrk_50d_base_v031_signal},
    "f05me_f05_moving_average_envelope_asylobrk_50d_base_v032_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_asylobrk_50d_base_v032_signal},
    "f05me_f05_moving_average_envelope_parkrnk_120d_base_v033_signal": {"inputs": ["high", "low"], "func": f05me_f05_moving_average_envelope_parkrnk_120d_base_v033_signal},
    "f05me_f05_moving_average_envelope_parkwid_30d_base_v034_signal": {"inputs": ["high", "low", "closeadj"], "func": f05me_f05_moving_average_envelope_parkwid_30d_base_v034_signal},
    "f05me_f05_moving_average_envelope_gkwidrat_20d_base_v035_signal": {"inputs": ["open", "high", "low", "close"], "func": f05me_f05_moving_average_envelope_gkwidrat_20d_base_v035_signal},
    "f05me_f05_moving_average_envelope_pkdays_60d_base_v036_signal": {"inputs": ["high", "low", "closeadj"], "func": f05me_f05_moving_average_envelope_pkdays_60d_base_v036_signal},
    "f05me_f05_moving_average_envelope_madenv_30d_base_v037_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_madenv_30d_base_v037_signal},
    "f05me_f05_moving_average_envelope_iqrasy_40d_base_v038_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_iqrasy_40d_base_v038_signal},
    "f05me_f05_moving_average_envelope_qbnd_60d_base_v039_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_qbnd_60d_base_v039_signal},
    "f05me_f05_moving_average_envelope_upslp_30d_base_v040_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_upslp_30d_base_v040_signal},
    "f05me_f05_moving_average_envelope_loslp_30d_base_v041_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_loslp_30d_base_v041_signal},
    "f05me_f05_moving_average_envelope_bndsdif_30d_base_v042_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bndsdif_30d_base_v042_signal},
    "f05me_f05_moving_average_envelope_upcurv_60d_base_v043_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_upcurv_60d_base_v043_signal},
    "f05me_f05_moving_average_envelope_innband_20d_base_v044_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_innband_20d_base_v044_signal},
    "f05me_f05_moving_average_envelope_widrat_50d_base_v045_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widrat_50d_base_v045_signal},
    "f05me_f05_moving_average_envelope_pbdiff_50d_base_v046_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbdiff_50d_base_v046_signal},
    "f05me_f05_moving_average_envelope_widdiff_100d_base_v047_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widdiff_100d_base_v047_signal},
    "f05me_f05_moving_average_envelope_signupper_20d_base_v048_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_signupper_20d_base_v048_signal},
    "f05me_f05_moving_average_envelope_signlower_50d_base_v049_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_signlower_50d_base_v049_signal},
    "f05me_f05_moving_average_envelope_quad_30d_base_v050_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_quad_30d_base_v050_signal},
    "f05me_f05_moving_average_envelope_breakdir_60d_base_v051_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_breakdir_60d_base_v051_signal},
    "f05me_f05_moving_average_envelope_sqzbrk_60d_base_v052_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_sqzbrk_60d_base_v052_signal},
    "f05me_f05_moving_average_envelope_madwid_30d_base_v053_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_madwid_30d_base_v053_signal},
    "f05me_f05_moving_average_envelope_bbpath_60d_base_v054_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbpath_60d_base_v054_signal},
    "f05me_f05_moving_average_envelope_bbex_30d_base_v055_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbex_30d_base_v055_signal},
    "f05me_f05_moving_average_envelope_pbrank_60d_base_v056_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbrank_60d_base_v056_signal},
    "f05me_f05_moving_average_envelope_widdrawd_120d_base_v057_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widdrawd_120d_base_v057_signal},
    "f05me_f05_moving_average_envelope_walknet_60d_base_v058_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_walknet_60d_base_v058_signal},
    "f05me_f05_moving_average_envelope_widnorm_30d_base_v059_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widnorm_30d_base_v059_signal},
    "f05me_f05_moving_average_envelope_widslp_50d_base_v060_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widslp_50d_base_v060_signal},
    "f05me_f05_moving_average_envelope_kcbbwrat_30d_base_v061_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcbbwrat_30d_base_v061_signal},
    "f05me_f05_moving_average_envelope_donchma_50d_base_v062_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_donchma_50d_base_v062_signal},
    "f05me_f05_moving_average_envelope_donchmawid_50d_base_v063_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_donchmawid_50d_base_v063_signal},
    "f05me_f05_moving_average_envelope_pbskew_60d_base_v064_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbskew_60d_base_v064_signal},
    "f05me_f05_moving_average_envelope_widac_60d_base_v065_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widac_60d_base_v065_signal},
    "f05me_f05_moving_average_envelope_widkurt_60d_base_v066_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widkurt_60d_base_v066_signal},
    "f05me_f05_moving_average_envelope_pbvar_30d_base_v067_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbvar_30d_base_v067_signal},
    "f05me_f05_moving_average_envelope_emasmadif_20d_base_v068_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_emasmadif_20d_base_v068_signal},
    "f05me_f05_moving_average_envelope_widema_30d_base_v069_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widema_30d_base_v069_signal},
    "f05me_f05_moving_average_envelope_walkbeyond_30d_base_v070_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_walkbeyond_30d_base_v070_signal},
    "f05me_f05_moving_average_envelope_widmad_50d_base_v071_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widmad_50d_base_v071_signal},
    "f05me_f05_moving_average_envelope_envtilt_30d_base_v072_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_envtilt_30d_base_v072_signal},
    "f05me_f05_moving_average_envelope_widvol_60d_base_v073_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widvol_60d_base_v073_signal},
    "f05me_f05_moving_average_envelope_distup_30d_base_v074_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_distup_30d_base_v074_signal},
    "f05me_f05_moving_average_envelope_distlo_50d_base_v075_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_distlo_50d_base_v075_signal},
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
    for name, entry in f05_moving_average_envelope_base_001_075_REGISTRY.items():
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
