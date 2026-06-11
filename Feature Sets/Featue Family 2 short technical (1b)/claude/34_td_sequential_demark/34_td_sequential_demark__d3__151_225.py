"""td_sequential_demark d3 features 151-225 — Pipeline 1b-technical (gap-fill extension).

Extends 001-150 with additional DeMark indicators not previously covered:
TD Anti-Differential, TD Reverse Differential, TD CLOP, TD CLOPWIN, TD Power of 3,
TD DeMarker 1, TD DeMarker 2, TD REBO (Range Expansion Breakout), TD Range
Projection, TD Termination Count, TD Reference Close, TD Pressure Reverse,
TD Trend Factor, TD Alignment (multi-timeframe proxy), and REI × price divergence.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- standard helpers ----------------------------

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


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ---------------------------- TD setup/countdown helpers ----------------------------

def _td_sell_setup_count(close: pd.Series) -> pd.Series:
    qual = (close > close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    qual = (close < close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_sell_countdown_count_local(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values; hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and cl[i] >= hi[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _td_rei(close: pd.Series, high: pd.Series, low: pd.Series, n: int = 5) -> pd.Series:
    high_mom = high - high.shift(2); low_mom = low - low.shift(2)
    abs_h = high_mom.abs(); abs_l = low_mom.abs()
    cond1 = (high.shift(2) >= close.shift(7)) | (high.shift(2) >= close.shift(8))
    cond2 = (high >= low.shift(5)) | (high >= low.shift(6))
    cond3 = (low.shift(2) <= close.shift(7)) | (low.shift(2) <= close.shift(8))
    cond4 = (low <= high.shift(5)) | (low <= high.shift(6))
    weight = ((cond1 & cond2) | (cond3 & cond4)).astype(float)
    weighted = (high_mom + low_mom) * weight
    abs_sum = abs_h + abs_l
    num = weighted.rolling(n, min_periods=max(n // 3, 2)).sum()
    den = abs_sum.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(num, den)


# ---------------------------- new TD pattern helpers ----------------------------

def _td_anti_differential_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish TD Anti-Differential: 2-bar reversal after up-move.
    prior close > 2-prior close AND current close < prior close
    AND (prior close - prior low) > (2-prior close - 2-prior low)
    AND (current high - close) > (prior high - prior close)."""
    pc = close.shift(1); ppc = close.shift(2)
    plow = low.shift(1); pplow = low.shift(2)
    phigh = high.shift(1)
    a = pc > ppc; b = close < pc
    c = (pc - plow) > (ppc - pplow)
    d = (high - close) > (phigh - pc)
    return (a & b & c & d).astype(float).where(pc.notna() & ppc.notna(), np.nan)


def _td_reverse_differential_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish TD Reverse Differential: current close > prior close (up bar)
    AND (prior close - prior low) > (current close - current low)  (lower-shadow shrinking)
    AND (current high - close) > (prior high - prior close)  (upper-shadow growing — failed thrust)."""
    pc = close.shift(1); plow = low.shift(1); phigh = high.shift(1)
    a = close > pc
    b = (pc - plow) > (close - low)
    c = (high - close) > (phigh - pc)
    return (a & b & c).astype(float).where(pc.notna() & plow.notna() & phigh.notna(), np.nan)


def _td_clop_bearish_event(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Bearish TD CLOP: today's open AND today's close both > prior open AND prior high
    (gap-up continuation that may exhaust at top)."""
    return ((open_ > open_.shift(1)) & (open_ > high.shift(1))
            & (close > high.shift(1))).astype(float).where(open_.shift(1).notna() & high.shift(1).notna(), np.nan)


def _td_clopwin_event(open_: pd.Series, close: pd.Series) -> pd.Series:
    """TD CLOPWIN: current open AND current close both within prior bar's open-close range (indecision)."""
    po = open_.shift(1); pc = close.shift(1)
    lo_bar = pd.concat([po, pc], axis=1).min(axis=1)
    hi_bar = pd.concat([po, pc], axis=1).max(axis=1)
    return ((open_ >= lo_bar) & (open_ <= hi_bar)
            & (close >= lo_bar) & (close <= hi_bar)).astype(float).where(po.notna() & pc.notna(), np.nan)


def _td_power_of_3_bearish_event(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3 consecutive lower closes with each bar's volume > prior — distribution power."""
    cond = ((close < close.shift(1)) & (close.shift(1) < close.shift(2))
            & (volume > volume.shift(1)) & (volume.shift(1) > volume.shift(2)))
    return cond.astype(float).where(close.shift(2).notna() & volume.shift(2).notna(), np.nan)


def _td_demarker(high: pd.Series, low: pd.Series, n: int = 14) -> pd.Series:
    """TD DeMarker 1 oscillator: SMA(DeMax) / (SMA(DeMax) + SMA(DeMin)). Range [0, 1]."""
    de_max = (high - high.shift(1)).clip(lower=0)
    de_min = (low.shift(1) - low).clip(lower=0)
    sma_max = _sma(de_max, n); sma_min = _sma(de_min, n)
    return _safe_div(sma_max, sma_max + sma_min)


def _td_demarker_2(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 8) -> pd.Series:
    """TD DeMarker 2 (simplified): weighted-ratio variant emphasizing prior-close gaps."""
    pc = close.shift(1)
    num_a = (high - pc).clip(lower=0)
    num_b = (pc - low).clip(lower=0) * 0.5
    num = (num_a + num_b).rolling(n, min_periods=max(n // 3, 2)).sum()
    den_a = (high - low)
    den_b = (close - close.shift(13)).abs()
    den = (den_a + den_b).rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _td_rebo_buy_level(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD REBO long-trigger: open + 0.382 × prior-bar range."""
    return open_ + 0.382 * (high.shift(1) - low.shift(1))


def _td_rebo_sell_level(open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD REBO short-trigger: open - 0.382 × prior-bar range."""
    return open_ - 0.382 * (high.shift(1) - low.shift(1))


def _td_range_projection(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Projected next-bar range: today's TR × (1 + close-position-in-bar)."""
    tr = high - low
    pos = _safe_div(close - low, high - low)
    return tr * (1.0 + pos)


def _td_pressure_reverse(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, n: int = 13) -> pd.Series:
    """Selling-pressure analog of TD Pressure: rolling sum(open-close) / sum(high-low)."""
    body = (open_ - close)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     rng.rolling(n, min_periods=max(n // 3, 2)).sum())


def _td_sell_setup_weekly_proxy(close: pd.Series) -> pd.Series:
    """Weekly-proxy sell setup: 9 consecutive closes > close 20 bars earlier."""
    qual = (close > close.shift(20)).astype(int).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


# ---------------------------- divergence helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    return (bear - bull).where(ps.notna() & osl.notna(), np.nan)


def _shift_div_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


# ============================================================
# Bucket HHH — TD Anti-Differential (151-155)
# ============================================================

def f34_tdsq_151_td_anti_differential_bearish_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD Anti-Differential pattern fires (2-bar reversal after up-move)."""
    return _td_anti_differential_bearish_event(close, high, low)


def f34_tdsq_152_td_anti_differential_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD Anti-Differential events in trailing 252d."""
    return _td_anti_differential_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_153_days_since_td_anti_differential(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Anti-Differential event."""
    return _bars_since_true(_td_anti_differential_bearish_event(close, high, low))


def f34_tdsq_154_td_anti_differential_x_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Anti-Differential fires AND close within 1% of 252d max."""
    f = _td_anti_differential_bearish_event(close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_155_td_anti_differential_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Anti-Differential events in trailing 63d (acute density)."""
    return _td_anti_differential_bearish_event(close, high, low).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket III — TD Reverse Differential (156-160)
# ============================================================

def f34_tdsq_156_td_reverse_differential_bearish_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD Reverse Differential fires."""
    return _td_reverse_differential_bearish_event(close, high, low)


def f34_tdsq_157_td_reverse_differential_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD Reverse Differential events in trailing 252d."""
    return _td_reverse_differential_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_158_days_since_td_reverse_differential(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Reverse Differential event."""
    return _bars_since_true(_td_reverse_differential_bearish_event(close, high, low))


def f34_tdsq_159_td_reverse_differential_x_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Reverse Differential fires AND close within 1% of 252d max."""
    f = _td_reverse_differential_bearish_event(close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_160_td_reverse_differential_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Reverse Differential events in trailing 63d."""
    return _td_reverse_differential_bearish_event(close, high, low).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket JJJ — TD CLOP (161-165)
# ============================================================

def f34_tdsq_161_td_clop_bearish_event_indicator(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD CLOP fires (gap-up continuation that may exhaust)."""
    return _td_clop_bearish_event(open, close, high)


def f34_tdsq_162_td_clop_count_252d(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of TD CLOP events in trailing 252d."""
    return _td_clop_bearish_event(open, close, high).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_163_days_since_td_clop(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since most recent CLOP event."""
    return _bars_since_true(_td_clop_bearish_event(open, close, high))


def f34_tdsq_164_td_clop_followed_by_lower_close_count_252d(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of CLOP events in 252d where next bar's close < CLOP bar's close (CLOP failure / exhaustion)."""
    f = _td_clop_bearish_event(open, close, high).fillna(0)
    next_lower = (close.shift(1) < close).astype(float)
    # PIT issue: shift(-1) peeks; use shift(1) on flag instead — meaning we check yesterday's flag with today's close
    f_prev = f.shift(1).fillna(0)
    return ((f_prev == 1) & (close < close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_165_td_clop_x_at_252d_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when CLOP fires AND close within 1% of 252d max."""
    f = _td_clop_bearish_event(open, close, high)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


# ============================================================
# Bucket KKK — TD CLOPWIN (166-170)
# ============================================================

def f34_tdsq_166_td_clopwin_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where CLOPWIN fires (indecision: current bar contained within prior open-close range)."""
    return _td_clopwin_event(open, close)


def f34_tdsq_167_td_clopwin_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CLOPWIN events in 252d."""
    return _td_clopwin_event(open, close).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_168_days_since_td_clopwin(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent CLOPWIN event."""
    return _bars_since_true(_td_clopwin_event(open, close))


def f34_tdsq_169_td_clopwin_x_at_252d_high_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when CLOPWIN fires AND close within 1% of 252d max (indecision at top)."""
    f = _td_clopwin_event(open, close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_170_td_clopwin_count_at_high_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CLOPWIN-at-252d-high conjunctions in trailing 252d."""
    f = _td_clopwin_event(open, close).fillna(0)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket LLL — TD Power of 3 (171-175)
# ============================================================

def f34_tdsq_171_td_power_of_3_bearish_event_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on bar where TD Power of 3 bearish pattern fires (3 down closes + 3 expanding volumes)."""
    return _td_power_of_3_bearish_event(close, volume)


def f34_tdsq_172_td_power_of_3_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Power of 3 events in 252d."""
    return _td_power_of_3_bearish_event(close, volume).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_173_days_since_td_power_of_3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent Power of 3 event."""
    return _bars_since_true(_td_power_of_3_bearish_event(close, volume))


def f34_tdsq_174_td_power_of_3_x_at_252d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when Power of 3 fires AND close within 1% of 252d max (distribution power at top)."""
    f = _td_power_of_3_bearish_event(close, volume)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_175_td_power_of_3_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Power of 3 events in trailing 63d (acute distribution)."""
    return _td_power_of_3_bearish_event(close, volume).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket MMM — TD DeMarker 1 / DeMarker 2 (176-185)
# ============================================================

def f34_tdsq_176_td_demarker_14_value(high: pd.Series, low: pd.Series) -> pd.Series:
    """TD DeMarker 1 (n=14) value, range [0, 1]."""
    return _td_demarker(high, low, 14)


def f34_tdsq_177_td_demarker_14_overbought_above_70_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when DeMarker > 0.7 (canonical overbought threshold)."""
    d = _td_demarker(high, low, 14)
    return (d > 0.7).astype(float).where(d.notna(), np.nan)


def f34_tdsq_178_td_demarker_14_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of DeMarker(14) in trailing 252d."""
    return _pct_rank(_td_demarker(high, low, 14), YDAYS)


def f34_tdsq_179_td_demarker_14_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of DeMarker(14)."""
    return _rolling_slope(_td_demarker(high, low, 14), MDAYS)


def f34_tdsq_180_td_demarker_14_slope_div_sign_63d_vs_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs DeMarker(14) over 63d."""
    return _slope_div_sign(close, _td_demarker(high, low, 14), QDAYS)


def f34_tdsq_181_td_demarker_2_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD DeMarker 2 (n=8) value — variant emphasizing prior-close gaps."""
    return _td_demarker_2(high, low, close, 8)


def f34_tdsq_182_td_demarker_2_overbought_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when DeMarker 2 > 0.6 (overbought threshold)."""
    d = _td_demarker_2(high, low, close, 8)
    return (d > 0.6).astype(float).where(d.notna(), np.nan)


def f34_tdsq_183_td_demarker_2_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DeMarker 2 in trailing 252d."""
    return _rolling_zscore(_td_demarker_2(high, low, close, 8), YDAYS)


def f34_tdsq_184_td_demarker_14_persistence_above_70_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-21d bars where DeMarker(14) > 0.7."""
    d = _td_demarker(high, low, 14)
    return (d > 0.7).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f34_tdsq_185_td_demarker_14_above_70_x_close_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when DeMarker(14) > 0.7 AND close within 1% of 252d max."""
    d = _td_demarker(high, low, 14)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((d > 0.7) & (near == 1)).astype(float).where(d.notna() & near.notna(), np.nan)


# ============================================================
# Bucket NNN — TD REBO (Range Expansion Breakout) (186-190)
# ============================================================

def f34_tdsq_186_td_rebo_buy_level(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD REBO long-trigger level: open + 0.382 × prior-bar range."""
    return _td_rebo_buy_level(open, high, low)


def f34_tdsq_187_close_above_td_rebo_buy_level_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close crosses above REBO buy level (range-expansion breakout fires)."""
    lvl = _td_rebo_buy_level(open, high, low)
    return (close > lvl).astype(float).where(lvl.notna(), np.nan)


def f34_tdsq_188_close_above_rebo_buy_x_close_at_252d_high_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when REBO buy breakout AND close within 1% of 252d max (potential failed-breakout at top)."""
    above = (close > _td_rebo_buy_level(open, high, low)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (above * near).where(above.notna() & near.notna(), np.nan)


def f34_tdsq_189_close_below_rebo_sell_level_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close crosses below REBO sell level (range-expansion breakdown event)."""
    lvl = _td_rebo_sell_level(open, high, low)
    return (close < lvl).astype(float).where(lvl.notna(), np.nan)


def f34_tdsq_190_rebo_failed_breakout_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 252d where: prior bar closed above REBO buy AND current bar closed below it (failed breakout)."""
    above = (close > _td_rebo_buy_level(open, high, low)).astype(float)
    fail = ((above.shift(1) == 1) & (above == 0)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket OOO — TD Range Projection (191-195)
# ============================================================

def f34_tdsq_191_td_range_projection_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Projected next-bar range based on today's TR × (1 + close-position-in-bar)."""
    return _td_range_projection(high, low, close)


def f34_tdsq_192_td_range_projection_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of range projection in trailing 252d."""
    return _rolling_zscore(_td_range_projection(high, low, close), YDAYS)


def f34_tdsq_193_td_range_projection_x_close_at_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when range-projection z(252) > 1 AND close within 1% of 252d max (volatility-expansion at top)."""
    z = _rolling_zscore(_td_range_projection(high, low, close), YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((z > 1) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


def f34_tdsq_194_td_range_projection_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of range projection in trailing 252d."""
    return _pct_rank(_td_range_projection(high, low, close), YDAYS)


def f34_tdsq_195_td_range_projection_above_atr21_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range projection / ATR(21) — how much larger than typical the projected range is."""
    return _safe_div(_td_range_projection(high, low, close), _atr(high, low, close, MDAYS))


# ============================================================
# Bucket PPP — TD Termination Count (196-200)
# ============================================================

def f34_tdsq_196_td_termination_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where sell-countdown resets from >0 to 0 (termination event — invalidation)."""
    cd = _td_sell_countdown_count_local(close, high, low)
    return ((cd == 0) & (cd.shift(1) > 0)).astype(float).where(cd.notna() & cd.shift(1).notna(), np.nan)


def f34_tdsq_197_td_termination_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of termination events in trailing 252d."""
    cd = _td_sell_countdown_count_local(close, high, low)
    reset = ((cd == 0) & (cd.shift(1) > 0)).astype(float)
    return reset.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_198_days_since_td_termination(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent termination event."""
    cd = _td_sell_countdown_count_local(close, high, low)
    reset = ((cd == 0) & (cd.shift(1) > 0)).astype(float)
    return _bars_since_true(reset)


def f34_tdsq_199_td_termination_count_at_high_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of termination events occurring at near-252d-high bars (terminations 'at top')."""
    cd = _td_sell_countdown_count_local(close, high, low)
    reset = ((cd == 0) & (cd.shift(1) > 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (reset * near).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_200_td_termination_max_progress_before_reset(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """At each termination event, the countdown value at the prior bar (held forward) —
    'how far did countdown get before it terminated'."""
    cd = _td_sell_countdown_count_local(close, high, low)
    reset = ((cd == 0) & (cd.shift(1) > 0))
    return cd.shift(1).where(reset, np.nan).ffill()


# ============================================================
# Bucket QQQ — TD Reference Close (201-205)
# ============================================================

def f34_tdsq_201_td_reference_close_4bars_ago(close: pd.Series) -> pd.Series:
    """TD Reference Close: close 4 bars ago — canonical setup-comparison bar."""
    return close.shift(4)


def f34_tdsq_202_close_vs_td_reference_close_log_diff(close: pd.Series) -> pd.Series:
    """log(close / reference close) — log distance from setup-comparison reference."""
    return _safe_log(close) - _safe_log(close.shift(4))


def f34_tdsq_203_close_vs_td_reference_close_atr_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - reference close) / ATR(21) — distance in vol units."""
    return _safe_div(close - close.shift(4), _atr(high, low, close, MDAYS))


def f34_tdsq_204_consecutive_bars_above_td_reference_close(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where close > reference close (setup-bar streak)."""
    flag = (close > close.shift(4)).astype(int).fillna(0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f34_tdsq_205_close_above_td_reference_close_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where close > reference close."""
    return (close > close.shift(4)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket RRR — TD Pressure Reverse / Supply (206-210)
# ============================================================

def f34_tdsq_206_td_pressure_reverse_value_13d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Pressure Reverse (selling-pressure analog) over 13d window."""
    return _td_pressure_reverse(open, close, high, low, 13)


def f34_tdsq_207_td_pressure_reverse_zscore_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Pressure Reverse in trailing 252d."""
    return _rolling_zscore(_td_pressure_reverse(open, close, high, low, 13), YDAYS)


def f34_tdsq_208_td_pressure_reverse_above_threshold_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Pressure Reverse z-score > 1 (high selling pressure regime)."""
    z = _rolling_zscore(_td_pressure_reverse(open, close, high, low, 13), YDAYS)
    return (z > 1.0).astype(float).where(z.notna(), np.nan)


def f34_tdsq_209_pressure_reverse_x_at_252d_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Pressure Reverse z > 1 AND close within 2% of 252d max (selling-pressure rising at top)."""
    z = _rolling_zscore(_td_pressure_reverse(open, close, high, low, 13), YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.98).astype(float)
    return ((z > 1) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


def f34_tdsq_210_pressure_minus_pressure_reverse_diff(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Buying pressure minus selling pressure (TD Pressure - TD Pressure Reverse) — net pressure."""
    body_buy = (close - open); body_sell = (open - close)
    rng = (high - low).replace(0, np.nan)
    buy = _safe_div(body_buy.rolling(13, min_periods=max(13 // 3, 2)).sum(),
                    rng.rolling(13, min_periods=max(13 // 3, 2)).sum())
    sell = _safe_div(body_sell.rolling(13, min_periods=max(13 // 3, 2)).sum(),
                     rng.rolling(13, min_periods=max(13 // 3, 2)).sum())
    return buy - sell


# ============================================================
# Bucket SSS — TD Trend Factor (211-215)
# ============================================================

def f34_tdsq_211_td_trend_factor_1_target_level(close: pd.Series, low: pd.Series) -> pd.Series:
    """TF1 target: trailing 252d low × 1.0382."""
    return low.rolling(YDAYS, min_periods=QDAYS).min() * 1.0382


def f34_tdsq_212_td_trend_factor_2_target_level(close: pd.Series, low: pd.Series) -> pd.Series:
    """TF2 target: trailing 252d low × 1.0786."""
    return low.rolling(YDAYS, min_periods=QDAYS).min() * 1.0786


def f34_tdsq_213_close_above_td_trend_factor_2_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close > TF2 target (in upside-extension zone — pricing-in continuation)."""
    tf2 = low.rolling(YDAYS, min_periods=QDAYS).min() * 1.0786
    return (close > tf2).astype(float).where(tf2.notna(), np.nan)


def f34_tdsq_214_close_distance_to_td_trend_factor_2_atr_norm(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """(close - TF2 target) / ATR(21) — distance above TF2 in vol units."""
    tf2 = low.rolling(YDAYS, min_periods=QDAYS).min() * 1.0786
    return _safe_div(close - tf2, _atr(high, low, close, MDAYS))


def f34_tdsq_215_close_above_tf2_persistence_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where close > TF2 target."""
    tf2 = low.rolling(YDAYS, min_periods=QDAYS).min() * 1.0786
    return (close > tf2).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket TTT — TD Alignment (multi-timeframe proxy via different setup periods) (216-220)
# ============================================================

def f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator(close: pd.Series) -> pd.Series:
    """+1 when standard daily setup-9 AND weekly-proxy (20-bar-comparison) setup-9 are both active."""
    daily = (_td_sell_setup_count(close) == 9).astype(float)
    weekly = (_td_sell_setup_weekly_proxy(close) == 9).astype(float)
    daily_recent = daily.rolling(WDAYS, min_periods=1).max()
    weekly_recent = weekly.rolling(MDAYS, min_periods=1).max()
    return (daily_recent * weekly_recent).where(daily.notna() & weekly.notna(), np.nan)


def f34_tdsq_217_td_alignment_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where daily setup-9 AND weekly-proxy setup-9 align."""
    daily = (_td_sell_setup_count(close) == 9).astype(float)
    weekly = (_td_sell_setup_weekly_proxy(close) == 9).astype(float)
    daily_recent = daily.rolling(WDAYS, min_periods=1).max()
    weekly_recent = weekly.rolling(MDAYS, min_periods=1).max()
    return (daily_recent * weekly_recent).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_218_td_alignment_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when alignment fires AND close within 1% of 252d max."""
    align = f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (align * near).where(align.notna() & near.notna(), np.nan)


def f34_tdsq_219_td_sell_setup_weekly_proxy_current_count(close: pd.Series) -> pd.Series:
    """Current running weekly-proxy (20-bar-comparison) sell-setup count."""
    return _td_sell_setup_weekly_proxy(close)


def f34_tdsq_220_td_sell_setup_weekly_proxy_9_fires_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where weekly-proxy sell-setup reaches 9."""
    return (_td_sell_setup_weekly_proxy(close) == 9).astype(float)


# ============================================================
# Bucket UUU — REI × price divergence (221-225)
# ============================================================

def f34_tdsq_221_rei_slope_div_sign_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish slope-divergence between close and TD REI over 63d."""
    return _slope_div_sign(close, _td_rei(close, high, low), QDAYS)


def f34_tdsq_222_rei_shift_div_indicator_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Two-point bearish divergence on REI, 63d."""
    return _shift_div_bearish_indicator(close, _td_rei(close, high, low), QDAYS)


def f34_tdsq_223_rei_zscore_gap_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """z(log close,63) - z(REI,63) — extension gap."""
    return _zscore_gap(close, _td_rei(close, high, low), QDAYS)


def f34_tdsq_224_rei_rolling_corr_price_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and REI."""
    return _rolling_corr_pearson(_safe_log(close), _td_rei(close, high, low), QDAYS)


def f34_tdsq_225_rei_bearish_div_at_overbought_x_close_at_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when REI bearish slope-div AND REI > 60 AND close within 1% of 252d max — triple conjunction."""
    r = _td_rei(close, high, low)
    div = (_slope_div_sign(close, r, QDAYS) > 0).astype(float)
    ob = (r > 60).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((div == 1) & (ob == 1) & (near == 1)).astype(float).where(div.notna() & ob.notna() & near.notna(), np.nan)


# ============================================================
# REGISTRY
# ============================================================



def f34_tdsq_151_td_anti_differential_bearish_event_indicator_d3(close, high, low):
    return f34_tdsq_151_td_anti_differential_bearish_event_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_152_td_anti_differential_count_252d_d3(close, high, low):
    return f34_tdsq_152_td_anti_differential_count_252d(close, high, low).diff().diff().diff()


def f34_tdsq_153_days_since_td_anti_differential_d3(close, high, low):
    return f34_tdsq_153_days_since_td_anti_differential(close, high, low).diff().diff().diff()


def f34_tdsq_154_td_anti_differential_x_252d_high_indicator_d3(close, high, low):
    return f34_tdsq_154_td_anti_differential_x_252d_high_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_155_td_anti_differential_count_63d_d3(close, high, low):
    return f34_tdsq_155_td_anti_differential_count_63d(close, high, low).diff().diff().diff()


def f34_tdsq_156_td_reverse_differential_bearish_event_indicator_d3(close, high, low):
    return f34_tdsq_156_td_reverse_differential_bearish_event_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_157_td_reverse_differential_count_252d_d3(close, high, low):
    return f34_tdsq_157_td_reverse_differential_count_252d(close, high, low).diff().diff().diff()


def f34_tdsq_158_days_since_td_reverse_differential_d3(close, high, low):
    return f34_tdsq_158_days_since_td_reverse_differential(close, high, low).diff().diff().diff()


def f34_tdsq_159_td_reverse_differential_x_252d_high_indicator_d3(close, high, low):
    return f34_tdsq_159_td_reverse_differential_x_252d_high_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_160_td_reverse_differential_count_63d_d3(close, high, low):
    return f34_tdsq_160_td_reverse_differential_count_63d(close, high, low).diff().diff().diff()


def f34_tdsq_161_td_clop_bearish_event_indicator_d3(open, close, high):
    return f34_tdsq_161_td_clop_bearish_event_indicator(open, close, high).diff().diff().diff()


def f34_tdsq_162_td_clop_count_252d_d3(open, close, high):
    return f34_tdsq_162_td_clop_count_252d(open, close, high).diff().diff().diff()


def f34_tdsq_163_days_since_td_clop_d3(open, close, high):
    return f34_tdsq_163_days_since_td_clop(open, close, high).diff().diff().diff()


def f34_tdsq_164_td_clop_followed_by_lower_close_count_252d_d3(open, close, high):
    return f34_tdsq_164_td_clop_followed_by_lower_close_count_252d(open, close, high).diff().diff().diff()


def f34_tdsq_165_td_clop_x_at_252d_high_indicator_d3(open, close, high):
    return f34_tdsq_165_td_clop_x_at_252d_high_indicator(open, close, high).diff().diff().diff()


def f34_tdsq_166_td_clopwin_event_indicator_d3(open, close):
    return f34_tdsq_166_td_clopwin_event_indicator(open, close).diff().diff().diff()


def f34_tdsq_167_td_clopwin_count_252d_d3(open, close):
    return f34_tdsq_167_td_clopwin_count_252d(open, close).diff().diff().diff()


def f34_tdsq_168_days_since_td_clopwin_d3(open, close):
    return f34_tdsq_168_days_since_td_clopwin(open, close).diff().diff().diff()


def f34_tdsq_169_td_clopwin_x_at_252d_high_indicator_d3(open, close):
    return f34_tdsq_169_td_clopwin_x_at_252d_high_indicator(open, close).diff().diff().diff()


def f34_tdsq_170_td_clopwin_count_at_high_252d_d3(open, close):
    return f34_tdsq_170_td_clopwin_count_at_high_252d(open, close).diff().diff().diff()


def f34_tdsq_171_td_power_of_3_bearish_event_indicator_d3(close, volume):
    return f34_tdsq_171_td_power_of_3_bearish_event_indicator(close, volume).diff().diff().diff()


def f34_tdsq_172_td_power_of_3_count_252d_d3(close, volume):
    return f34_tdsq_172_td_power_of_3_count_252d(close, volume).diff().diff().diff()


def f34_tdsq_173_days_since_td_power_of_3_d3(close, volume):
    return f34_tdsq_173_days_since_td_power_of_3(close, volume).diff().diff().diff()


def f34_tdsq_174_td_power_of_3_x_at_252d_high_indicator_d3(close, volume):
    return f34_tdsq_174_td_power_of_3_x_at_252d_high_indicator(close, volume).diff().diff().diff()


def f34_tdsq_175_td_power_of_3_count_63d_d3(close, volume):
    return f34_tdsq_175_td_power_of_3_count_63d(close, volume).diff().diff().diff()


def f34_tdsq_176_td_demarker_14_value_d3(high, low):
    return f34_tdsq_176_td_demarker_14_value(high, low).diff().diff().diff()


def f34_tdsq_177_td_demarker_14_overbought_above_70_indicator_d3(high, low):
    return f34_tdsq_177_td_demarker_14_overbought_above_70_indicator(high, low).diff().diff().diff()


def f34_tdsq_178_td_demarker_14_pct_rank_252d_d3(high, low):
    return f34_tdsq_178_td_demarker_14_pct_rank_252d(high, low).diff().diff().diff()


def f34_tdsq_179_td_demarker_14_slope_21d_d3(high, low):
    return f34_tdsq_179_td_demarker_14_slope_21d(high, low).diff().diff().diff()


def f34_tdsq_180_td_demarker_14_slope_div_sign_63d_vs_close_d3(high, low, close):
    return f34_tdsq_180_td_demarker_14_slope_div_sign_63d_vs_close(high, low, close).diff().diff().diff()


def f34_tdsq_181_td_demarker_2_value_d3(high, low, close):
    return f34_tdsq_181_td_demarker_2_value(high, low, close).diff().diff().diff()


def f34_tdsq_182_td_demarker_2_overbought_indicator_d3(high, low, close):
    return f34_tdsq_182_td_demarker_2_overbought_indicator(high, low, close).diff().diff().diff()


def f34_tdsq_183_td_demarker_2_zscore_252d_d3(high, low, close):
    return f34_tdsq_183_td_demarker_2_zscore_252d(high, low, close).diff().diff().diff()


def f34_tdsq_184_td_demarker_14_persistence_above_70_21d_d3(high, low):
    return f34_tdsq_184_td_demarker_14_persistence_above_70_21d(high, low).diff().diff().diff()


def f34_tdsq_185_td_demarker_14_above_70_x_close_at_252d_high_indicator_d3(high, low, close):
    return f34_tdsq_185_td_demarker_14_above_70_x_close_at_252d_high_indicator(high, low, close).diff().diff().diff()


def f34_tdsq_186_td_rebo_buy_level_d3(open, high, low):
    return f34_tdsq_186_td_rebo_buy_level(open, high, low).diff().diff().diff()


def f34_tdsq_187_close_above_td_rebo_buy_level_indicator_d3(open, high, low, close):
    return f34_tdsq_187_close_above_td_rebo_buy_level_indicator(open, high, low, close).diff().diff().diff()


def f34_tdsq_188_close_above_rebo_buy_x_close_at_252d_high_indicator_d3(open, high, low, close):
    return f34_tdsq_188_close_above_rebo_buy_x_close_at_252d_high_indicator(open, high, low, close).diff().diff().diff()


def f34_tdsq_189_close_below_rebo_sell_level_indicator_d3(open, high, low, close):
    return f34_tdsq_189_close_below_rebo_sell_level_indicator(open, high, low, close).diff().diff().diff()


def f34_tdsq_190_rebo_failed_breakout_count_252d_d3(open, high, low, close):
    return f34_tdsq_190_rebo_failed_breakout_count_252d(open, high, low, close).diff().diff().diff()


def f34_tdsq_191_td_range_projection_value_d3(close, high, low):
    return f34_tdsq_191_td_range_projection_value(close, high, low).diff().diff().diff()


def f34_tdsq_192_td_range_projection_zscore_252d_d3(close, high, low):
    return f34_tdsq_192_td_range_projection_zscore_252d(close, high, low).diff().diff().diff()


def f34_tdsq_193_td_range_projection_x_close_at_252d_high_indicator_d3(close, high, low):
    return f34_tdsq_193_td_range_projection_x_close_at_252d_high_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_194_td_range_projection_pct_rank_252d_d3(close, high, low):
    return f34_tdsq_194_td_range_projection_pct_rank_252d(close, high, low).diff().diff().diff()


def f34_tdsq_195_td_range_projection_above_atr21_ratio_d3(close, high, low):
    return f34_tdsq_195_td_range_projection_above_atr21_ratio(close, high, low).diff().diff().diff()


def f34_tdsq_196_td_termination_event_indicator_d3(close, high, low):
    return f34_tdsq_196_td_termination_event_indicator(close, high, low).diff().diff().diff()


def f34_tdsq_197_td_termination_count_252d_d3(close, high, low):
    return f34_tdsq_197_td_termination_count_252d(close, high, low).diff().diff().diff()


def f34_tdsq_198_days_since_td_termination_d3(close, high, low):
    return f34_tdsq_198_days_since_td_termination(close, high, low).diff().diff().diff()


def f34_tdsq_199_td_termination_count_at_high_252d_d3(close, high, low):
    return f34_tdsq_199_td_termination_count_at_high_252d(close, high, low).diff().diff().diff()


def f34_tdsq_200_td_termination_max_progress_before_reset_d3(close, high, low):
    return f34_tdsq_200_td_termination_max_progress_before_reset(close, high, low).diff().diff().diff()


def f34_tdsq_201_td_reference_close_4bars_ago_d3(close):
    return f34_tdsq_201_td_reference_close_4bars_ago(close).diff().diff().diff()


def f34_tdsq_202_close_vs_td_reference_close_log_diff_d3(close):
    return f34_tdsq_202_close_vs_td_reference_close_log_diff(close).diff().diff().diff()


def f34_tdsq_203_close_vs_td_reference_close_atr_norm_d3(close, high, low):
    return f34_tdsq_203_close_vs_td_reference_close_atr_norm(close, high, low).diff().diff().diff()


def f34_tdsq_204_consecutive_bars_above_td_reference_close_d3(close):
    return f34_tdsq_204_consecutive_bars_above_td_reference_close(close).diff().diff().diff()


def f34_tdsq_205_close_above_td_reference_close_persistence_63d_d3(close):
    return f34_tdsq_205_close_above_td_reference_close_persistence_63d(close).diff().diff().diff()


def f34_tdsq_206_td_pressure_reverse_value_13d_d3(open, close, high, low):
    return f34_tdsq_206_td_pressure_reverse_value_13d(open, close, high, low).diff().diff().diff()


def f34_tdsq_207_td_pressure_reverse_zscore_252d_d3(open, close, high, low):
    return f34_tdsq_207_td_pressure_reverse_zscore_252d(open, close, high, low).diff().diff().diff()


def f34_tdsq_208_td_pressure_reverse_above_threshold_indicator_d3(open, close, high, low):
    return f34_tdsq_208_td_pressure_reverse_above_threshold_indicator(open, close, high, low).diff().diff().diff()


def f34_tdsq_209_pressure_reverse_x_at_252d_high_indicator_d3(open, close, high, low):
    return f34_tdsq_209_pressure_reverse_x_at_252d_high_indicator(open, close, high, low).diff().diff().diff()


def f34_tdsq_210_pressure_minus_pressure_reverse_diff_d3(open, close, high, low):
    return f34_tdsq_210_pressure_minus_pressure_reverse_diff(open, close, high, low).diff().diff().diff()


def f34_tdsq_211_td_trend_factor_1_target_level_d3(close, low):
    return f34_tdsq_211_td_trend_factor_1_target_level(close, low).diff().diff().diff()


def f34_tdsq_212_td_trend_factor_2_target_level_d3(close, low):
    return f34_tdsq_212_td_trend_factor_2_target_level(close, low).diff().diff().diff()


def f34_tdsq_213_close_above_td_trend_factor_2_indicator_d3(close, low):
    return f34_tdsq_213_close_above_td_trend_factor_2_indicator(close, low).diff().diff().diff()


def f34_tdsq_214_close_distance_to_td_trend_factor_2_atr_norm_d3(close, low, high):
    return f34_tdsq_214_close_distance_to_td_trend_factor_2_atr_norm(close, low, high).diff().diff().diff()


def f34_tdsq_215_close_above_tf2_persistence_63d_d3(close, low):
    return f34_tdsq_215_close_above_tf2_persistence_63d(close, low).diff().diff().diff()


def f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator_d3(close):
    return f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator(close).diff().diff().diff()


def f34_tdsq_217_td_alignment_count_252d_d3(close):
    return f34_tdsq_217_td_alignment_count_252d(close).diff().diff().diff()


def f34_tdsq_218_td_alignment_at_252d_high_indicator_d3(close):
    return f34_tdsq_218_td_alignment_at_252d_high_indicator(close).diff().diff().diff()


def f34_tdsq_219_td_sell_setup_weekly_proxy_current_count_d3(close):
    return f34_tdsq_219_td_sell_setup_weekly_proxy_current_count(close).diff().diff().diff()


def f34_tdsq_220_td_sell_setup_weekly_proxy_9_fires_indicator_d3(close):
    return f34_tdsq_220_td_sell_setup_weekly_proxy_9_fires_indicator(close).diff().diff().diff()


def f34_tdsq_221_rei_slope_div_sign_63d_d3(close, high, low):
    return f34_tdsq_221_rei_slope_div_sign_63d(close, high, low).diff().diff().diff()


def f34_tdsq_222_rei_shift_div_indicator_63d_d3(close, high, low):
    return f34_tdsq_222_rei_shift_div_indicator_63d(close, high, low).diff().diff().diff()


def f34_tdsq_223_rei_zscore_gap_63d_d3(close, high, low):
    return f34_tdsq_223_rei_zscore_gap_63d(close, high, low).diff().diff().diff()


def f34_tdsq_224_rei_rolling_corr_price_63d_d3(close, high, low):
    return f34_tdsq_224_rei_rolling_corr_price_63d(close, high, low).diff().diff().diff()


def f34_tdsq_225_rei_bearish_div_at_overbought_x_close_at_high_indicator_d3(close, high, low):
    return f34_tdsq_225_rei_bearish_div_at_overbought_x_close_at_high_indicator(close, high, low).diff().diff().diff()


TD_SEQUENTIAL_DEMARK_D3_REGISTRY_151_225 = {
    "f34_tdsq_151_td_anti_differential_bearish_event_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_151_td_anti_differential_bearish_event_indicator_d3},
    "f34_tdsq_152_td_anti_differential_count_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_152_td_anti_differential_count_252d_d3},
    "f34_tdsq_153_days_since_td_anti_differential_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_153_days_since_td_anti_differential_d3},
    "f34_tdsq_154_td_anti_differential_x_252d_high_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_154_td_anti_differential_x_252d_high_indicator_d3},
    "f34_tdsq_155_td_anti_differential_count_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_155_td_anti_differential_count_63d_d3},
    "f34_tdsq_156_td_reverse_differential_bearish_event_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_156_td_reverse_differential_bearish_event_indicator_d3},
    "f34_tdsq_157_td_reverse_differential_count_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_157_td_reverse_differential_count_252d_d3},
    "f34_tdsq_158_days_since_td_reverse_differential_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_158_days_since_td_reverse_differential_d3},
    "f34_tdsq_159_td_reverse_differential_x_252d_high_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_159_td_reverse_differential_x_252d_high_indicator_d3},
    "f34_tdsq_160_td_reverse_differential_count_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_160_td_reverse_differential_count_63d_d3},
    "f34_tdsq_161_td_clop_bearish_event_indicator_d3": {"inputs": ["open", "close", "high"], "func": f34_tdsq_161_td_clop_bearish_event_indicator_d3},
    "f34_tdsq_162_td_clop_count_252d_d3": {"inputs": ["open", "close", "high"], "func": f34_tdsq_162_td_clop_count_252d_d3},
    "f34_tdsq_163_days_since_td_clop_d3": {"inputs": ["open", "close", "high"], "func": f34_tdsq_163_days_since_td_clop_d3},
    "f34_tdsq_164_td_clop_followed_by_lower_close_count_252d_d3": {"inputs": ["open", "close", "high"], "func": f34_tdsq_164_td_clop_followed_by_lower_close_count_252d_d3},
    "f34_tdsq_165_td_clop_x_at_252d_high_indicator_d3": {"inputs": ["open", "close", "high"], "func": f34_tdsq_165_td_clop_x_at_252d_high_indicator_d3},
    "f34_tdsq_166_td_clopwin_event_indicator_d3": {"inputs": ["open", "close"], "func": f34_tdsq_166_td_clopwin_event_indicator_d3},
    "f34_tdsq_167_td_clopwin_count_252d_d3": {"inputs": ["open", "close"], "func": f34_tdsq_167_td_clopwin_count_252d_d3},
    "f34_tdsq_168_days_since_td_clopwin_d3": {"inputs": ["open", "close"], "func": f34_tdsq_168_days_since_td_clopwin_d3},
    "f34_tdsq_169_td_clopwin_x_at_252d_high_indicator_d3": {"inputs": ["open", "close"], "func": f34_tdsq_169_td_clopwin_x_at_252d_high_indicator_d3},
    "f34_tdsq_170_td_clopwin_count_at_high_252d_d3": {"inputs": ["open", "close"], "func": f34_tdsq_170_td_clopwin_count_at_high_252d_d3},
    "f34_tdsq_171_td_power_of_3_bearish_event_indicator_d3": {"inputs": ["close", "volume"], "func": f34_tdsq_171_td_power_of_3_bearish_event_indicator_d3},
    "f34_tdsq_172_td_power_of_3_count_252d_d3": {"inputs": ["close", "volume"], "func": f34_tdsq_172_td_power_of_3_count_252d_d3},
    "f34_tdsq_173_days_since_td_power_of_3_d3": {"inputs": ["close", "volume"], "func": f34_tdsq_173_days_since_td_power_of_3_d3},
    "f34_tdsq_174_td_power_of_3_x_at_252d_high_indicator_d3": {"inputs": ["close", "volume"], "func": f34_tdsq_174_td_power_of_3_x_at_252d_high_indicator_d3},
    "f34_tdsq_175_td_power_of_3_count_63d_d3": {"inputs": ["close", "volume"], "func": f34_tdsq_175_td_power_of_3_count_63d_d3},
    "f34_tdsq_176_td_demarker_14_value_d3": {"inputs": ["high", "low"], "func": f34_tdsq_176_td_demarker_14_value_d3},
    "f34_tdsq_177_td_demarker_14_overbought_above_70_indicator_d3": {"inputs": ["high", "low"], "func": f34_tdsq_177_td_demarker_14_overbought_above_70_indicator_d3},
    "f34_tdsq_178_td_demarker_14_pct_rank_252d_d3": {"inputs": ["high", "low"], "func": f34_tdsq_178_td_demarker_14_pct_rank_252d_d3},
    "f34_tdsq_179_td_demarker_14_slope_21d_d3": {"inputs": ["high", "low"], "func": f34_tdsq_179_td_demarker_14_slope_21d_d3},
    "f34_tdsq_180_td_demarker_14_slope_div_sign_63d_vs_close_d3": {"inputs": ["high", "low", "close"], "func": f34_tdsq_180_td_demarker_14_slope_div_sign_63d_vs_close_d3},
    "f34_tdsq_181_td_demarker_2_value_d3": {"inputs": ["high", "low", "close"], "func": f34_tdsq_181_td_demarker_2_value_d3},
    "f34_tdsq_182_td_demarker_2_overbought_indicator_d3": {"inputs": ["high", "low", "close"], "func": f34_tdsq_182_td_demarker_2_overbought_indicator_d3},
    "f34_tdsq_183_td_demarker_2_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f34_tdsq_183_td_demarker_2_zscore_252d_d3},
    "f34_tdsq_184_td_demarker_14_persistence_above_70_21d_d3": {"inputs": ["high", "low"], "func": f34_tdsq_184_td_demarker_14_persistence_above_70_21d_d3},
    "f34_tdsq_185_td_demarker_14_above_70_x_close_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f34_tdsq_185_td_demarker_14_above_70_x_close_at_252d_high_indicator_d3},
    "f34_tdsq_186_td_rebo_buy_level_d3": {"inputs": ["open", "high", "low"], "func": f34_tdsq_186_td_rebo_buy_level_d3},
    "f34_tdsq_187_close_above_td_rebo_buy_level_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_187_close_above_td_rebo_buy_level_indicator_d3},
    "f34_tdsq_188_close_above_rebo_buy_x_close_at_252d_high_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_188_close_above_rebo_buy_x_close_at_252d_high_indicator_d3},
    "f34_tdsq_189_close_below_rebo_sell_level_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_189_close_below_rebo_sell_level_indicator_d3},
    "f34_tdsq_190_rebo_failed_breakout_count_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_190_rebo_failed_breakout_count_252d_d3},
    "f34_tdsq_191_td_range_projection_value_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_191_td_range_projection_value_d3},
    "f34_tdsq_192_td_range_projection_zscore_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_192_td_range_projection_zscore_252d_d3},
    "f34_tdsq_193_td_range_projection_x_close_at_252d_high_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_193_td_range_projection_x_close_at_252d_high_indicator_d3},
    "f34_tdsq_194_td_range_projection_pct_rank_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_194_td_range_projection_pct_rank_252d_d3},
    "f34_tdsq_195_td_range_projection_above_atr21_ratio_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_195_td_range_projection_above_atr21_ratio_d3},
    "f34_tdsq_196_td_termination_event_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_196_td_termination_event_indicator_d3},
    "f34_tdsq_197_td_termination_count_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_197_td_termination_count_252d_d3},
    "f34_tdsq_198_days_since_td_termination_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_198_days_since_td_termination_d3},
    "f34_tdsq_199_td_termination_count_at_high_252d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_199_td_termination_count_at_high_252d_d3},
    "f34_tdsq_200_td_termination_max_progress_before_reset_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_200_td_termination_max_progress_before_reset_d3},
    "f34_tdsq_201_td_reference_close_4bars_ago_d3": {"inputs": ["close"], "func": f34_tdsq_201_td_reference_close_4bars_ago_d3},
    "f34_tdsq_202_close_vs_td_reference_close_log_diff_d3": {"inputs": ["close"], "func": f34_tdsq_202_close_vs_td_reference_close_log_diff_d3},
    "f34_tdsq_203_close_vs_td_reference_close_atr_norm_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_203_close_vs_td_reference_close_atr_norm_d3},
    "f34_tdsq_204_consecutive_bars_above_td_reference_close_d3": {"inputs": ["close"], "func": f34_tdsq_204_consecutive_bars_above_td_reference_close_d3},
    "f34_tdsq_205_close_above_td_reference_close_persistence_63d_d3": {"inputs": ["close"], "func": f34_tdsq_205_close_above_td_reference_close_persistence_63d_d3},
    "f34_tdsq_206_td_pressure_reverse_value_13d_d3": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_206_td_pressure_reverse_value_13d_d3},
    "f34_tdsq_207_td_pressure_reverse_zscore_252d_d3": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_207_td_pressure_reverse_zscore_252d_d3},
    "f34_tdsq_208_td_pressure_reverse_above_threshold_indicator_d3": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_208_td_pressure_reverse_above_threshold_indicator_d3},
    "f34_tdsq_209_pressure_reverse_x_at_252d_high_indicator_d3": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_209_pressure_reverse_x_at_252d_high_indicator_d3},
    "f34_tdsq_210_pressure_minus_pressure_reverse_diff_d3": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_210_pressure_minus_pressure_reverse_diff_d3},
    "f34_tdsq_211_td_trend_factor_1_target_level_d3": {"inputs": ["close", "low"], "func": f34_tdsq_211_td_trend_factor_1_target_level_d3},
    "f34_tdsq_212_td_trend_factor_2_target_level_d3": {"inputs": ["close", "low"], "func": f34_tdsq_212_td_trend_factor_2_target_level_d3},
    "f34_tdsq_213_close_above_td_trend_factor_2_indicator_d3": {"inputs": ["close", "low"], "func": f34_tdsq_213_close_above_td_trend_factor_2_indicator_d3},
    "f34_tdsq_214_close_distance_to_td_trend_factor_2_atr_norm_d3": {"inputs": ["close", "low", "high"], "func": f34_tdsq_214_close_distance_to_td_trend_factor_2_atr_norm_d3},
    "f34_tdsq_215_close_above_tf2_persistence_63d_d3": {"inputs": ["close", "low"], "func": f34_tdsq_215_close_above_tf2_persistence_63d_d3},
    "f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator_d3": {"inputs": ["close"], "func": f34_tdsq_216_td_sell_setup_daily_x_weekly_proxy_indicator_d3},
    "f34_tdsq_217_td_alignment_count_252d_d3": {"inputs": ["close"], "func": f34_tdsq_217_td_alignment_count_252d_d3},
    "f34_tdsq_218_td_alignment_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f34_tdsq_218_td_alignment_at_252d_high_indicator_d3},
    "f34_tdsq_219_td_sell_setup_weekly_proxy_current_count_d3": {"inputs": ["close"], "func": f34_tdsq_219_td_sell_setup_weekly_proxy_current_count_d3},
    "f34_tdsq_220_td_sell_setup_weekly_proxy_9_fires_indicator_d3": {"inputs": ["close"], "func": f34_tdsq_220_td_sell_setup_weekly_proxy_9_fires_indicator_d3},
    "f34_tdsq_221_rei_slope_div_sign_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_221_rei_slope_div_sign_63d_d3},
    "f34_tdsq_222_rei_shift_div_indicator_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_222_rei_shift_div_indicator_63d_d3},
    "f34_tdsq_223_rei_zscore_gap_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_223_rei_zscore_gap_63d_d3},
    "f34_tdsq_224_rei_rolling_corr_price_63d_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_224_rei_rolling_corr_price_63d_d3},
    "f34_tdsq_225_rei_bearish_div_at_overbought_x_close_at_high_indicator_d3": {"inputs": ["close", "high", "low"], "func": f34_tdsq_225_rei_bearish_div_at_overbought_x_close_at_high_indicator_d3},
}
