"""f05_moving_average_envelope base features 076-150.

Second batch of envelope features. Every feature references a moving
average AND a band/width measure. None duplicates a file-1 feature
(file-1 covers BB %B at 10/20/200, KC break, MAD, IQR, Parkinson, GK,
asymmetric envelopes, walk/touch/streak/days-since at the canonical 20d
BB and Keltner, plus width-of-width).

This file emphasises:
- different MA kernels as the envelope center (EMA, WMA, HMA-style,
  median) with their own width construction
- different vol kernels for the half-width (TR, range-quantile,
  EWM-std on returns, residual-MAD, downside dev, ATR variants)
- different time-aggregations: rolling-low-anchored bands, time-fraction,
  excursion-magnitude, body-fraction outside band
- discrete envelope state transitions (touch sequences, regime flips)
- cross-envelope differentials (KC vs BB, MAD vs std, Parkinson vs GK)
- envelope features keyed on high/low/open rather than close

NaN policy: never fillna(0); only replace([inf,-inf], nan) at return.
Windows > 21d use closeadj; windows <= 21d use close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float)
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w) / w.sum()), raw=True)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


def f05me_f05_moving_average_envelope_bbpctb_30d_base_v076_signal(closeadj: pd.Series) -> pd.Series:
    """%B over BB(30, 2): mid-window band position, fills 20d/50d gap."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    out = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbpctb3_20d_base_v077_signal(close: pd.Series) -> pd.Series:
    """%B over BB(20, 3): 3-sigma outer band — sensitivity at tail."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 3.0 * sd
    lower = sma - 3.0 * sd
    out = (close - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_emabbwid_50d_base_v078_signal(closeadj: pd.Series) -> pd.Series:
    """EMA(50) Bollinger width with EWM std denominator. Continuous,
    distinct from SMA-anchored width."""
    ema = closeadj.ewm(span=50, adjust=False, min_periods=50).mean()
    var = (closeadj - ema).pow(2).ewm(span=50, adjust=False, min_periods=50).mean()
    sd = np.sqrt(var)
    out = (4.0 * sd) / ema.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_wmasmadif_30d_base_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Normalised gap between WMA(30) and SMA(30) centers, expressed as
    fraction of BB(30,2) half-width: (WMA - SMA)/(2*std). Captures
    center-of-mass skew of the envelope, distinct from any position
    feature."""
    wma = _wma(closeadj, 30)
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    out = (wma - sma) / (2.0 * sd).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_medsmadif_30d_base_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Difference between MEDIAN(30) and SMA(30) center expressed in
    IQR(30) units: (median - SMA)/IQR. Center-skew between robust and
    non-robust MA — distinct from any %B."""
    med = closeadj.rolling(30, min_periods=30).median()
    sma = closeadj.rolling(30, min_periods=30).mean()
    q1 = closeadj.rolling(30, min_periods=30).quantile(0.25)
    q3 = closeadj.rolling(30, min_periods=30).quantile(0.75)
    iqr = q3 - q1
    out = (med - sma) / iqr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcpctk_40d_base_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """%K position over Keltner(40, 1.5*ATR(20)). Long-window Keltner —
    different scale than the 20d KC in file 1."""
    ema = closeadj.ewm(span=40, adjust=False, min_periods=40).mean()
    atr = _atr(high, low, close, 20)
    upper = ema + 1.5 * atr
    lower = ema - 1.5 * atr
    out = (closeadj - lower) / (upper - lower).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwid_50d_base_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Keltner(50, 2*ATR(30)) width as fraction of EMA — longer scale."""
    ema = closeadj.ewm(span=50, adjust=False, min_periods=50).mean()
    atr = _atr(high, low, close, 30)
    out = (4.0 * atr) / ema.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwslp_60d_base_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Normalised slope of Keltner(20, 2*ATR14) width over 21 bars."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    width = (4.0 * atr) / ema.replace(0.0, np.nan)
    out = width.diff(21) / width.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcdslo_60d_base_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since last close <= Keltner(20) lower band."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    lower = ema - 2.0 * atr
    touch = (close <= lower).astype(int)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwalkup_30d_base_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars with close > Keltner(20) upper band."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr
    flag = (close > upper).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwalkdn_30d_base_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars with close < Keltner(20) lower band."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    lower = ema - 2.0 * atr
    flag = (close < lower).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbtouchint_60d_base_v087_signal(close: pd.Series) -> pd.Series:
    """Mean inter-arrival days between BB(20,2) upper touches over 60d:
    60 / max(1, touch_count). Persistence-style metric."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    touch = (close >= upper).astype(float)
    cnt = touch.rolling(60, min_periods=60).sum()
    out = 60.0 / cnt.where(cnt > 0, 1.0)
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbdsmid_60d_base_v088_signal(closeadj: pd.Series) -> pd.Series:
    """Days since last MA-midline crossing of BB(20) — flipping sign of
    (close - SMA20). Time-since regime feature."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sign = np.sign(closeadj - sma)
    flip = (sign * sign.shift(1) < 0).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(flip == 1).ffill()
    out = idx - last
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbinside_60d_base_v089_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 60 INSIDE BB(50, 2). 0..1.
    Long-band occupancy regime."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    inside = ((closeadj <= upper) & (closeadj >= lower)).astype(float)
    out = inside.rolling(60, min_periods=60).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbwidroc_60d_base_v090_signal(closeadj: pd.Series) -> pd.Series:
    """ROC of BB(20,2) width over 21 bars: width(t)/width(t-21) - 1.
    Multiplicative change in width, distinct from diff(10)/width form."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width / width.shift(21).replace(0.0, np.nan) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbwjerk_60d_base_v091_signal(closeadj: pd.Series) -> pd.Series:
    """Three-point jerk of BB(50,2) width with k=15: w - 2*w.shift(15) +
    w.shift(30). Long-band width acceleration."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = (width - 2.0 * width.shift(15) + width.shift(30)) / width.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbpathsgn_60d_base_v092_signal(closeadj: pd.Series) -> pd.Series:
    """Signed band-walk fraction: (#bars > upper - #bars < lower)/N for
    BB(50,2) over 60. -1..+1 signed bias."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    up = (closeadj > upper).astype(float).rolling(60, min_periods=60).sum()
    dn = (closeadj < lower).astype(float).rolling(60, min_periods=60).sum()
    out = (up - dn) / 60.0
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbnewlow_60d_base_v093_signal(closeadj: pd.Series) -> pd.Series:
    """Indicator: BB(20,2) width is at a fresh 60d low (squeeze onset).
    Differentiated from rank-based squeeze: uses strict min over 60d."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    mn = width.rolling(60, min_periods=60).min()
    out = (width <= mn + 1e-12).astype(float)
    out[width.isna() | mn.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbnewhigh_60d_base_v094_signal(closeadj: pd.Series) -> pd.Series:
    """Indicator: BB(20,2) width at a fresh 60d high (vol expansion peak)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    mx = width.rolling(60, min_periods=60).max()
    out = (width >= mx - 1e-12).astype(float)
    out[width.isna() | mx.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dnsdev_40d_base_v095_signal(closeadj: pd.Series) -> pd.Series:
    """Downside-deviation half-width: rolling RMS of negative residuals
    from SMA(40) at 40d, normalized by SMA. Half-width using only
    downside variance — distinct from std-based widths."""
    sma = closeadj.rolling(40, min_periods=40).mean()
    dev = closeadj - sma
    dn = dev.where(dev < 0, 0.0)
    rms = (dn.pow(2).rolling(40, min_periods=40).mean()).pow(0.5)
    out = (2.0 * rms) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_upsdev_40d_base_v096_signal(closeadj: pd.Series) -> pd.Series:
    """Upside-deviation half-width: RMS of positive residuals from SMA(40)
    at 40d, normalized by SMA. Distinct from downside variant."""
    sma = closeadj.rolling(40, min_periods=40).mean()
    dev = closeadj - sma
    up = dev.where(dev > 0, 0.0)
    rms = (up.pow(2).rolling(40, min_periods=40).mean()).pow(0.5)
    out = (2.0 * rms) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dnsfrac_60d_base_v097_signal(closeadj: pd.Series) -> pd.Series:
    """Downside-deviation share: dn_dev / (dn_dev + up_dev) at 60d.
    Bounded [0,1]; 0.5 = symmetric, > 0.5 = downside-dominant width."""
    sma = closeadj.rolling(60, min_periods=60).mean()
    dev = closeadj - sma
    up = (dev.where(dev > 0, 0.0).pow(2).rolling(60, min_periods=60).mean()).pow(0.5)
    dn = ((-dev.where(dev < 0, 0.0)).pow(2).rolling(60, min_periods=60).mean()).pow(0.5)
    out = dn / (up + dn).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_atrenvdays_40d_base_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Days since close last >= SMA(40) + 1*ATR(20) (ATR-anchored upper
    around an SMA center, not EMA). Time-since regime feature using the
    SMA+ATR envelope — structurally distinct from %B-style positions."""
    sma = closeadj.rolling(40, min_periods=40).mean()
    atr = _atr(high, low, close, 20)
    upper = sma + 1.0 * atr
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_atrwid_80d_base_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """ATR-anchored band width at SMA(80): 2*ATR(50)/SMA(80). Long ATR
    width — distinct from any 14d or 20d ATR width."""
    sma = closeadj.rolling(80, min_periods=80).mean()
    atr = _atr(high, low, close, 50)
    out = (2.0 * atr) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_trbbwrat_40d_base_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """TR-anchored width vs BB-anchored width at 40d: (ATR40 / std40).
    Cross-vol kernel ratio — orthogonal to either width alone."""
    atr = _atr(high, low, close, 40)
    sd = closeadj.rolling(40, min_periods=40).std()
    out = atr / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_lowanchor_50d_base_v101_signal(closeadj: pd.Series) -> pd.Series:
    """Anchored band: distance from close to rolling-50-low + 2% of SMA(50),
    normalized by SMA. Captures band sitting above the recent low."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    lo = closeadj.rolling(50, min_periods=50).min()
    anch = lo + 0.02 * sma
    out = (closeadj - anch) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_highanchor_50d_base_v102_signal(closeadj: pd.Series) -> pd.Series:
    """Anchored band from rolling-50-high: (high - close) / SMA(50)
    where high is the 50d max. Distance to recent peak normalized."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    hi = closeadj.rolling(50, min_periods=50).max()
    out = (hi - closeadj) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bandsep_50d_base_v103_signal(closeadj: pd.Series) -> pd.Series:
    """Separation between BB(20) upper and BB(50) upper, normalized by
    SMA(50). Captures whether short band is above or below long band."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    up20 = sma20 + 2.0 * sd20
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    up50 = sma50 + 2.0 * sd50
    out = (up20 - up50) / sma50.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bandsep_lo_50d_base_v104_signal(closeadj: pd.Series) -> pd.Series:
    """Separation of BB(20) lower vs BB(50) lower, normalized by SMA(50)."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    lo20 = sma20 - 2.0 * sd20
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    lo50 = sma50 - 2.0 * sd50
    out = (lo20 - lo50) / sma50.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_exrange_30d_base_v105_signal(closeadj: pd.Series) -> pd.Series:
    """Max excursion outside BB(20,2) within trailing 30 bars, normalized:
    max over window of max(close-upper, 0) + max(lower-close, 0), divided
    by SMA. A single biggest-breach metric distinct from sum/excursion."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    out = excess.rolling(30, min_periods=30).max() / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bodyabove_30d_base_v106_signal(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars whose ENTIRE BODY (min(open,close)) is
    above BB(20,2) upper band. Open/close based outside-band signature —
    distinct from close-only walk."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    body_min = pd.concat([open_, close], axis=1).min(axis=1)
    flag = (body_min > upper).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bodybelow_30d_base_v107_signal(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars whose entire body (max(open,close)) is
    below BB(20,2) lower band."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    body_max = pd.concat([open_, close], axis=1).max(axis=1)
    flag = (body_max < lower).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widskew_60d_base_v108_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling skewness of BB(20,2) width over 60 bars — distribution of
    width values themselves; orthogonal to width level or rank."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbac_50d_base_v109_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of %B(20,2) over trailing 50 bars."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = pb.rolling(50, min_periods=50).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbquadcnt_50d_base_v110_signal(closeadj: pd.Series) -> pd.Series:
    """Count of bars in trailing 50 where %B(20,2) is in extreme quartiles
    (<= 0.2 or >= 0.8). Extreme-band-position frequency."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    flag = ((pb <= 0.2) | (pb >= 0.8)).astype(float)
    out = flag.rolling(50, min_periods=50).sum()
    out[pb.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_meanrev_60d_base_v111_signal(closeadj: pd.Series) -> pd.Series:
    """Mean reversion strength: corr(%B(t-1), %B-change(t)) over trailing
    60 bars. Negative -> mean reversion to MA; positive -> trending band."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    dpb = pb.diff()
    out = pb.shift(1).rolling(60, min_periods=60).corr(dpb)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_hlrange_30d_base_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar HL range divided by BB(20,2) total width. Captures whether the
    intraday range is large or small relative to the band size."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    width = 4.0 * sd
    rng = high - low
    out = rng / width.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_highbreach_30d_base_v113_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 30 with HIGH > BB(20,2) upper. Uses high not close
    so it captures intra-bar breaches missed by close-only counts."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    flag = (high > upper).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_lowbreach_30d_base_v114_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 30 with LOW < BB(20,2) lower. Intra-bar downside
    breach intensity."""
    sma = close.rolling(20, min_periods=20).mean()
    sd = close.rolling(20, min_periods=20).std()
    lower = sma - 2.0 * sd
    flag = (low < lower).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_donchemwid_60d_base_v115_signal(closeadj: pd.Series) -> pd.Series:
    """Donchian envelope on EMA(20): (max(EMA20, 60d) - min(EMA20, 60d))/EMA.
    EMA-Donchian width — distinct from the SMA-Donchian on a-MA in file 1."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    hi = ema.rolling(60, min_periods=60).max()
    lo = ema.rolling(60, min_periods=60).min()
    out = (hi - lo) / ema.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_donchempos_60d_base_v116_signal(closeadj: pd.Series) -> pd.Series:
    """Position of EMA(20) inside its 60-bar Donchian-on-EMA range. 0..1."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    hi = ema.rolling(60, min_periods=60).max()
    lo = ema.rolling(60, min_periods=60).min()
    out = (ema - lo) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widatrrat_40d_base_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of BB(40,2) width to KC(40) width: (4*std40/SMA)/(4*ATR20/SMA)
    = std40/ATR20. Long-band BB-vs-KC width ratio."""
    sd = closeadj.rolling(40, min_periods=40).std()
    atr = _atr(high, low, close, 20)
    out = sd / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widasymrat_40d_base_v118_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of upside-RMS half-width to downside-RMS half-width at 40d.
    > 1 -> positive deviations dominate band; < 1 -> negative dominate.
    Distinct from asy_skew (file 1) which used EWM-mean of dev."""
    sma = closeadj.rolling(40, min_periods=40).mean()
    dev = closeadj - sma
    up = (dev.where(dev > 0, 0.0).pow(2).rolling(40, min_periods=40).mean()).pow(0.5)
    dn = ((-dev.where(dev < 0, 0.0)).pow(2).rolling(40, min_periods=40).mean()).pow(0.5)
    out = up / dn.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_envcurv_60d_base_v119_signal(closeadj: pd.Series) -> pd.Series:
    """Curvature of BB(50,2) LOWER band with k=15: lo - 2*lo.shift(15) +
    lo.shift(30), normalised. Lower-band acceleration."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    lo = sma - 2.0 * sd
    out = (lo - 2.0 * lo.shift(15) + lo.shift(30)) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widmean_120d_base_v120_signal(closeadj: pd.Series) -> pd.Series:
    """Mean of BB(20,2) width over trailing 120 bars, normalised by current
    SMA(20). Long-horizon average width."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = width.rolling(120, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcpathfrac_60d_base_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 60 where close is OUTSIDE Keltner(20).
    Counterpart of bb_path in file 1 but using KC band."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr
    lower = ema - 2.0 * atr
    flag = ((close > upper) | (close < lower)).astype(float)
    out = flag.rolling(60, min_periods=60).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctwidrnk_60d_base_v122_signal(closeadj: pd.Series) -> pd.Series:
    """Rank of (max(close-1.02*SMA20, 0) + max(0.98*SMA20-close, 0))/SMA in
    trailing 60. Excursion-magnitude regime in fixed-percent envelope."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    upper = 1.02 * sma
    lower = 0.98 * sma
    excess = (closeadj - upper).clip(lower=0.0) + (lower - closeadj).clip(lower=0.0)
    mag = excess / sma.replace(0.0, np.nan)
    out = mag.rolling(60, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widpbcorr_60d_base_v123_signal(closeadj: pd.Series) -> pd.Series:
    """Trailing 60-bar correlation between BB(20,2) width and |%B - 0.5|.
    Captures whether extreme band positions coincide with band expansion."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    pb_extr = (pb - 0.5).abs()
    out = width.rolling(60, min_periods=60).corr(pb_extr)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widmonot_30d_base_v124_signal(closeadj: pd.Series) -> pd.Series:
    """Monotonicity of BB(20,2) width over 30 bars: fraction of positive
    daily diffs minus negative diffs. -1..+1. Width-direction persistence."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    d = width.diff()
    pos = (d > 0).astype(float).rolling(30, min_periods=30).sum()
    neg = (d < 0).astype(float).rolling(30, min_periods=30).sum()
    out = (pos - neg) / 30.0
    out[width.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widmrev_60d_base_v125_signal(closeadj: pd.Series) -> pd.Series:
    """Mean-reversion of width: corr(width(t-1), width-change(t)) over 60 bars."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    dw = width.diff()
    out = width.shift(1).rolling(60, min_periods=60).corr(dw)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_signmid_20d_base_v126_signal(close: pd.Series) -> pd.Series:
    """sign(close - SMA20) — discrete state of which half of the
    envelope the bar sits in. +1 upper half, -1 lower half. Discrete
    midpoint indicator."""
    sma = close.rolling(20, min_periods=20).mean()
    out = np.sign(close - sma).astype(float)
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widthsign_30d_base_v127_signal(closeadj: pd.Series) -> pd.Series:
    """sign of BB(20,2) width change over 21 bars — +1 expanding,
    -1 contracting. Discrete width-direction state."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    out = np.sign(width.diff(21)).astype(float)
    out[width.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pkgkwid_30d_base_v128_signal(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of Parkinson-vol to Garman-Klass-vol at 30d. Compares two
    range-based vol estimators directly — orthogonal cross-vol shape."""
    r = np.log(high / low.replace(0.0, np.nan))
    pk_var = (r ** 2).rolling(30, min_periods=30).mean() / (4.0 * np.log(2.0))
    pk = np.sqrt(pk_var)
    hl = np.log(high / low.replace(0.0, np.nan)) ** 2
    co = np.log(close / open_.replace(0.0, np.nan)) ** 2
    daily = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    gk = np.sqrt(daily.rolling(30, min_periods=30).mean().clip(lower=0.0))
    out = pk / gk.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcsqz_60d_base_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Keltner squeeze: 1 when KC(20,2*ATR14) width is in the bottom decile
    of trailing 60 bars. Distinct from BB squeeze (file 1) — uses ATR not std."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    width = (4.0 * atr) / ema.replace(0.0, np.nan)
    rk = width.rolling(60, min_periods=30).rank(pct=True)
    out = (rk <= 0.10).astype(float)
    out[rk.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbdiff_200d_base_v130_signal(closeadj: pd.Series) -> pd.Series:
    """%B(50,2) minus %B(200,2). Long-horizon band-position differential."""
    sma50 = closeadj.rolling(50, min_periods=50).mean()
    sd50 = closeadj.rolling(50, min_periods=50).std()
    pb50 = (closeadj - (sma50 - 2.0 * sd50)) / (4.0 * sd50).replace(0.0, np.nan)
    sma200 = closeadj.rolling(200, min_periods=200).mean()
    sd200 = closeadj.rolling(200, min_periods=200).std()
    pb200 = (closeadj - (sma200 - 2.0 * sd200)) / (4.0 * sd200).replace(0.0, np.nan)
    out = pb50 - pb200
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dsupper_120d_base_v131_signal(closeadj: pd.Series) -> pd.Series:
    """Days since close >= BB(50,2) upper — long-window 'days since' on
    the upper band. Distinct from 20d days-since."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    upper = sma + 2.0 * sd
    touch = (closeadj >= upper).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dslower_120d_base_v132_signal(closeadj: pd.Series) -> pd.Series:
    """Days since close <= BB(50,2) lower."""
    sma = closeadj.rolling(50, min_periods=50).mean()
    sd = closeadj.rolling(50, min_periods=50).std()
    lower = sma - 2.0 * sd
    touch = (closeadj <= lower).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(touch == 1).ffill()
    out = idx - last
    out[lower.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbexcsign_30d_base_v133_signal(closeadj: pd.Series) -> pd.Series:
    """Signed BB(30,2) excursion magnitude: + if above upper, - if below
    lower, 0 if inside, normalised by SMA. Captures direction-aware
    breach magnitude — distinct from positional %B (which never returns 0
    inside band)."""
    sma = closeadj.rolling(30, min_periods=30).mean()
    sd = closeadj.rolling(30, min_periods=30).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    pos = (closeadj - upper).clip(lower=0.0)
    neg = (lower - closeadj).clip(lower=0.0)
    out = (pos - neg) / sma.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcoutfrac_30d_base_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars where the FULL BAR RANGE (low to high)
    is outside Keltner(20). 1 = bar entirely outside band, 0 = always
    intersecting. Distinct from close-based KC walk."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    upper = ema + 2.0 * atr
    lower = ema - 2.0 * atr
    flag = ((low > upper) | (high < lower)).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bandgap_100d_base_v135_signal(closeadj: pd.Series) -> pd.Series:
    """Gap between BB(20,2) upper and BB(100,2) upper, both normalized by
    SMA(100). Two-scale upper-band convergence."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    up20 = sma20 + 2.0 * sd20
    sma100 = closeadj.rolling(100, min_periods=100).mean()
    sd100 = closeadj.rolling(100, min_periods=100).std()
    up100 = sma100 + 2.0 * sd100
    out = (up20 - up100) / sma100.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bandgap_lo_100d_base_v136_signal(closeadj: pd.Series) -> pd.Series:
    """Gap between BB(20,2) lower and BB(100,2) lower, normalized."""
    sma20 = closeadj.rolling(20, min_periods=20).mean()
    sd20 = closeadj.rolling(20, min_periods=20).std()
    lo20 = sma20 - 2.0 * sd20
    sma100 = closeadj.rolling(100, min_periods=100).mean()
    sd100 = closeadj.rolling(100, min_periods=100).std()
    lo100 = sma100 - 2.0 * sd100
    out = (lo20 - lo100) / sma100.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbweight_60d_base_v137_signal(closeadj: pd.Series) -> pd.Series:
    """Exponentially-decayed average %B(20,2) over 60 bars (half-life=20).
    Smoothed band position with memory — distinct from raw %B."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = pb.ewm(halflife=20, adjust=False, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widewmrat_60d_base_v138_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of EWM-std(span=20) to rolling-std(20). Compares exponential
    vs equal-weighted vol estimators — orthogonal to either width alone."""
    ewm_var = closeadj.diff().pow(2).ewm(span=20, adjust=False, min_periods=20).mean()
    ewm_sd = np.sqrt(ewm_var)
    sd = closeadj.diff().rolling(20, min_periods=20).std()
    out = ewm_sd / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbsamesign_30d_base_v139_signal(closeadj: pd.Series) -> pd.Series:
    """Fraction of trailing 30 bars where %B(20,2) > 0.5 (above MA-mid).
    Discrete-aggregate balance feature."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    flag = (closeadj > sma).astype(float)
    out = flag.rolling(30, min_periods=30).mean()
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbpeakgap_60d_base_v140_signal(closeadj: pd.Series) -> pd.Series:
    """Distance from current %B(20,2) to its 60-bar max: pb_max - pb.
    Captures how far the band position has fallen from recent extreme."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    mx = pb.rolling(60, min_periods=60).max()
    out = mx - pb
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pbrange_60d_base_v141_signal(closeadj: pd.Series) -> pd.Series:
    """60-bar range of %B(20,2): (pb_max - pb_min). Bounded, but
    structurally orthogonal to the level of %B — measures swing breadth
    of band position rather than position itself."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    mn = pb.rolling(60, min_periods=60).min()
    mx = pb.rolling(60, min_periods=60).max()
    out = mx - mn
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwidskew_60d_base_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Rolling skewness of Keltner(20, 2*ATR14) width over 60 bars —
    distributional shape of the ATR-anchored width."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    width = (4.0 * atr) / ema.replace(0.0, np.nan)
    out = width.rolling(60, min_periods=60).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcwidkurt_60d_base_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Rolling kurtosis of Keltner(20, 2*ATR14) width over 60 bars.
    Captures how spiky/peaked the ATR-anchored width history is."""
    ema = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    atr = _atr(high, low, close, 14)
    width = (4.0 * atr) / ema.replace(0.0, np.nan)
    out = width.rolling(60, min_periods=60).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_bbslprat_30d_base_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of upper-band slope to lower-band slope (signed) for BB(20,2).
    diff(10)/sma denom. Captures whether upper is rising faster than
    lower is falling — distinct from band-slope diff."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    upper = sma + 2.0 * sd
    lower = sma - 2.0 * sd
    us = upper.diff(10) / sma.replace(0.0, np.nan)
    ls = lower.diff(10) / sma.replace(0.0, np.nan)
    out = us / ls.abs().replace(0.0, np.nan) * np.sign(ls)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dsmidup_60d_base_v145_signal(closeadj: pd.Series) -> pd.Series:
    """Days since close last crossed UP through SMA(20): from below to
    above. Directional crossover days-since signal."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sign = np.sign(closeadj - sma)
    flip = ((sign > 0) & (sign.shift(1) <= 0)).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(flip == 1).ffill()
    out = idx - last
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_dsmidwn_60d_base_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Days since close last crossed DOWN through SMA(20)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sign = np.sign(closeadj - sma)
    flip = ((sign < 0) & (sign.shift(1) >= 0)).astype(int)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last = idx.where(flip == 1).ffill()
    out = idx - last
    out[sma.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widmedrat_60d_base_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of current BB(20,2) width to its 60-bar MEDIAN width.
    1 = typical, >1 expansion, <1 contraction. Median anchor differs
    structurally from mean/rank anchors."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    med = width.rolling(60, min_periods=30).median()
    out = width / med.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_pctcombo_60d_base_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Time-weighted combo: %B(20,2) - 0.5 averaged over trailing 60 bars
    (mean signed deviation from band midpoint)."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    pb = (closeadj - (sma - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    out = (pb - 0.5).rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_widlongshort_120d_base_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Difference of trailing 120d mean BB-width vs trailing 60d mean
    BB-width. Captures slow-vs-fast width regime contrast — distinct
    from drawdown (v057), which uses max not mean as the anchor."""
    sma = closeadj.rolling(20, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    width = (4.0 * sd) / sma.replace(0.0, np.nan)
    m120 = width.rolling(120, min_periods=60).mean()
    m60 = width.rolling(60, min_periods=60).mean()
    out = m120 - m60
    return out.replace([np.inf, -np.inf], np.nan)


def f05me_f05_moving_average_envelope_kcrejtop_30d_base_v150_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count over 30d of bars where intraday HIGH exceeded Keltner(20)
    upper but the close finished BELOW the upper — i.e. upper-band
    rejection on KC. Distinct from BB rejection (file 1) by anchor."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    pc = close.shift(1)
    tr = pd.concat([(high - close).abs(), (high - pc).abs(), (close - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    upper = ema + 2.0 * atr
    flag = ((high >= upper) & (close < upper)).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[upper.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f05_moving_average_envelope_base_076_150_REGISTRY = {
    "f05me_f05_moving_average_envelope_bbpctb_30d_base_v076_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbpctb_30d_base_v076_signal},
    "f05me_f05_moving_average_envelope_bbpctb3_20d_base_v077_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_bbpctb3_20d_base_v077_signal},
    "f05me_f05_moving_average_envelope_emabbwid_50d_base_v078_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_emabbwid_50d_base_v078_signal},
    "f05me_f05_moving_average_envelope_wmasmadif_30d_base_v079_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_wmasmadif_30d_base_v079_signal},
    "f05me_f05_moving_average_envelope_medsmadif_30d_base_v080_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_medsmadif_30d_base_v080_signal},
    "f05me_f05_moving_average_envelope_kcpctk_40d_base_v081_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcpctk_40d_base_v081_signal},
    "f05me_f05_moving_average_envelope_kcwid_50d_base_v082_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcwid_50d_base_v082_signal},
    "f05me_f05_moving_average_envelope_kcwslp_60d_base_v083_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcwslp_60d_base_v083_signal},
    "f05me_f05_moving_average_envelope_kcdslo_60d_base_v084_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcdslo_60d_base_v084_signal},
    "f05me_f05_moving_average_envelope_kcwalkup_30d_base_v085_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcwalkup_30d_base_v085_signal},
    "f05me_f05_moving_average_envelope_kcwalkdn_30d_base_v086_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcwalkdn_30d_base_v086_signal},
    "f05me_f05_moving_average_envelope_bbtouchint_60d_base_v087_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_bbtouchint_60d_base_v087_signal},
    "f05me_f05_moving_average_envelope_bbdsmid_60d_base_v088_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbdsmid_60d_base_v088_signal},
    "f05me_f05_moving_average_envelope_bbinside_60d_base_v089_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbinside_60d_base_v089_signal},
    "f05me_f05_moving_average_envelope_bbwidroc_60d_base_v090_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbwidroc_60d_base_v090_signal},
    "f05me_f05_moving_average_envelope_bbwjerk_60d_base_v091_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbwjerk_60d_base_v091_signal},
    "f05me_f05_moving_average_envelope_bbpathsgn_60d_base_v092_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbpathsgn_60d_base_v092_signal},
    "f05me_f05_moving_average_envelope_bbnewlow_60d_base_v093_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbnewlow_60d_base_v093_signal},
    "f05me_f05_moving_average_envelope_bbnewhigh_60d_base_v094_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbnewhigh_60d_base_v094_signal},
    "f05me_f05_moving_average_envelope_dnsdev_40d_base_v095_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dnsdev_40d_base_v095_signal},
    "f05me_f05_moving_average_envelope_upsdev_40d_base_v096_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_upsdev_40d_base_v096_signal},
    "f05me_f05_moving_average_envelope_dnsfrac_60d_base_v097_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dnsfrac_60d_base_v097_signal},
    "f05me_f05_moving_average_envelope_atrenvdays_40d_base_v098_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_atrenvdays_40d_base_v098_signal},
    "f05me_f05_moving_average_envelope_atrwid_80d_base_v099_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_atrwid_80d_base_v099_signal},
    "f05me_f05_moving_average_envelope_trbbwrat_40d_base_v100_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_trbbwrat_40d_base_v100_signal},
    "f05me_f05_moving_average_envelope_lowanchor_50d_base_v101_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_lowanchor_50d_base_v101_signal},
    "f05me_f05_moving_average_envelope_highanchor_50d_base_v102_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_highanchor_50d_base_v102_signal},
    "f05me_f05_moving_average_envelope_bandsep_50d_base_v103_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bandsep_50d_base_v103_signal},
    "f05me_f05_moving_average_envelope_bandsep_lo_50d_base_v104_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bandsep_lo_50d_base_v104_signal},
    "f05me_f05_moving_average_envelope_exrange_30d_base_v105_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_exrange_30d_base_v105_signal},
    "f05me_f05_moving_average_envelope_bodyabove_30d_base_v106_signal": {"inputs": ["open", "close"], "func": f05me_f05_moving_average_envelope_bodyabove_30d_base_v106_signal},
    "f05me_f05_moving_average_envelope_bodybelow_30d_base_v107_signal": {"inputs": ["open", "close"], "func": f05me_f05_moving_average_envelope_bodybelow_30d_base_v107_signal},
    "f05me_f05_moving_average_envelope_widskew_60d_base_v108_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widskew_60d_base_v108_signal},
    "f05me_f05_moving_average_envelope_pbac_50d_base_v109_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbac_50d_base_v109_signal},
    "f05me_f05_moving_average_envelope_pbquadcnt_50d_base_v110_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbquadcnt_50d_base_v110_signal},
    "f05me_f05_moving_average_envelope_meanrev_60d_base_v111_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_meanrev_60d_base_v111_signal},
    "f05me_f05_moving_average_envelope_hlrange_30d_base_v112_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_hlrange_30d_base_v112_signal},
    "f05me_f05_moving_average_envelope_highbreach_30d_base_v113_signal": {"inputs": ["high", "close"], "func": f05me_f05_moving_average_envelope_highbreach_30d_base_v113_signal},
    "f05me_f05_moving_average_envelope_lowbreach_30d_base_v114_signal": {"inputs": ["low", "close"], "func": f05me_f05_moving_average_envelope_lowbreach_30d_base_v114_signal},
    "f05me_f05_moving_average_envelope_donchemwid_60d_base_v115_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_donchemwid_60d_base_v115_signal},
    "f05me_f05_moving_average_envelope_donchempos_60d_base_v116_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_donchempos_60d_base_v116_signal},
    "f05me_f05_moving_average_envelope_widatrrat_40d_base_v117_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_widatrrat_40d_base_v117_signal},
    "f05me_f05_moving_average_envelope_widasymrat_40d_base_v118_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widasymrat_40d_base_v118_signal},
    "f05me_f05_moving_average_envelope_envcurv_60d_base_v119_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_envcurv_60d_base_v119_signal},
    "f05me_f05_moving_average_envelope_widmean_120d_base_v120_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widmean_120d_base_v120_signal},
    "f05me_f05_moving_average_envelope_kcpathfrac_60d_base_v121_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcpathfrac_60d_base_v121_signal},
    "f05me_f05_moving_average_envelope_pctwidrnk_60d_base_v122_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pctwidrnk_60d_base_v122_signal},
    "f05me_f05_moving_average_envelope_widpbcorr_60d_base_v123_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widpbcorr_60d_base_v123_signal},
    "f05me_f05_moving_average_envelope_widmonot_30d_base_v124_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widmonot_30d_base_v124_signal},
    "f05me_f05_moving_average_envelope_widmrev_60d_base_v125_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widmrev_60d_base_v125_signal},
    "f05me_f05_moving_average_envelope_signmid_20d_base_v126_signal": {"inputs": ["close"], "func": f05me_f05_moving_average_envelope_signmid_20d_base_v126_signal},
    "f05me_f05_moving_average_envelope_widthsign_30d_base_v127_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widthsign_30d_base_v127_signal},
    "f05me_f05_moving_average_envelope_pkgkwid_30d_base_v128_signal": {"inputs": ["open", "high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_pkgkwid_30d_base_v128_signal},
    "f05me_f05_moving_average_envelope_kcsqz_60d_base_v129_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcsqz_60d_base_v129_signal},
    "f05me_f05_moving_average_envelope_pbdiff_200d_base_v130_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbdiff_200d_base_v130_signal},
    "f05me_f05_moving_average_envelope_dsupper_120d_base_v131_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dsupper_120d_base_v131_signal},
    "f05me_f05_moving_average_envelope_dslower_120d_base_v132_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dslower_120d_base_v132_signal},
    "f05me_f05_moving_average_envelope_bbexcsign_30d_base_v133_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbexcsign_30d_base_v133_signal},
    "f05me_f05_moving_average_envelope_kcoutfrac_30d_base_v134_signal": {"inputs": ["high", "low", "close"], "func": f05me_f05_moving_average_envelope_kcoutfrac_30d_base_v134_signal},
    "f05me_f05_moving_average_envelope_bandgap_100d_base_v135_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bandgap_100d_base_v135_signal},
    "f05me_f05_moving_average_envelope_bandgap_lo_100d_base_v136_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bandgap_lo_100d_base_v136_signal},
    "f05me_f05_moving_average_envelope_pbweight_60d_base_v137_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbweight_60d_base_v137_signal},
    "f05me_f05_moving_average_envelope_widewmrat_60d_base_v138_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widewmrat_60d_base_v138_signal},
    "f05me_f05_moving_average_envelope_bbsamesign_30d_base_v139_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbsamesign_30d_base_v139_signal},
    "f05me_f05_moving_average_envelope_pbpeakgap_60d_base_v140_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbpeakgap_60d_base_v140_signal},
    "f05me_f05_moving_average_envelope_pbrange_60d_base_v141_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pbrange_60d_base_v141_signal},
    "f05me_f05_moving_average_envelope_kcwidskew_60d_base_v142_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcwidskew_60d_base_v142_signal},
    "f05me_f05_moving_average_envelope_kcwidkurt_60d_base_v143_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f05me_f05_moving_average_envelope_kcwidkurt_60d_base_v143_signal},
    "f05me_f05_moving_average_envelope_bbslprat_30d_base_v144_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_bbslprat_30d_base_v144_signal},
    "f05me_f05_moving_average_envelope_dsmidup_60d_base_v145_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dsmidup_60d_base_v145_signal},
    "f05me_f05_moving_average_envelope_dsmidwn_60d_base_v146_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_dsmidwn_60d_base_v146_signal},
    "f05me_f05_moving_average_envelope_widmedrat_60d_base_v147_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widmedrat_60d_base_v147_signal},
    "f05me_f05_moving_average_envelope_pctcombo_60d_base_v148_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_pctcombo_60d_base_v148_signal},
    "f05me_f05_moving_average_envelope_widlongshort_120d_base_v149_signal": {"inputs": ["closeadj"], "func": f05me_f05_moving_average_envelope_widlongshort_120d_base_v149_signal},
    "f05me_f05_moving_average_envelope_kcrejtop_30d_base_v150_signal": {"inputs": ["high", "close"], "func": f05me_f05_moving_average_envelope_kcrejtop_30d_base_v150_signal},
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
    for name, entry in f05_moving_average_envelope_base_076_150_REGISTRY.items():
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
