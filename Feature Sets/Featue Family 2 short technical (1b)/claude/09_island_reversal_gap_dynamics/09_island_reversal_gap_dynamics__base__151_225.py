"""island_reversal_gap_dynamics base features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. Each feature here encodes a DISTINCT
concept NOT covered by 001-150:

- PARTIAL gaps (open > prior close but range overlaps) — 001-150 only
  covered FULL gaps (entire range gap-cleared from prior range)
- Inside-day / outside-day patterns AFTER a gap day
- Pre-gap setup metrics (compression, low-volume coil, range tightening)
- Gap-and-go rate vs gap-and-fade rate (post-gap directional bias)
- Isolated catalyst gaps (gap after long quiet period — earnings/news proxy)
- Successive-gap stacking (each gap larger / smaller than prior)
- Gap into new 52w / 5y highs (regime context)
- Gap-down warning during uptrend
- Gap retest within N days (price returns to gap zone but doesn't fill)
- Exhaustion down-gaps (down-gap at lows during downtrend)
- Inside-bar followthrough after gap
- Composite top/bottom gap signatures

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


# ---- family-specific helpers (PIT-clean) ----

def _full_up_gap(high, low):
    return low > high.shift(1)


def _full_down_gap(high, low):
    return high < low.shift(1)


def _partial_up_gap(open_, high, low, close):
    """Partial up-gap: open > prior_close AND low <= prior_high (range overlaps prior bar)."""
    return (open_ > close.shift(1)) & (low <= high.shift(1))


def _partial_down_gap(open_, high, low, close):
    """Partial down-gap: open < prior_close AND high >= prior_low."""
    return (open_ < close.shift(1)) & (high >= low.shift(1))


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


def _streak(condition):
    grp = (~condition).cumsum()
    return condition.astype(int).groupby(grp).cumsum().astype(float)


def _inside_bar(high, low):
    """Inside bar: today's high < prior high AND today's low > prior low."""
    return (high < high.shift(1)) & (low > low.shift(1))


def _outside_bar(high, low):
    """Outside bar: today's high > prior high AND today's low < prior low — engulfs prior range."""
    return (high > high.shift(1)) & (low < low.shift(1))


# ============================================================
# Bucket A — Partial gaps (151-160)
# ============================================================

def f09_irgd_151_partial_up_gap_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: open > prior close AND range overlaps prior bar (partial up gap)."""
    return _partial_up_gap(open_, high, low, close).astype(float)


def f09_irgd_152_partial_down_gap_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: open < prior close AND range overlaps prior bar (partial down gap)."""
    return _partial_down_gap(open_, high, low, close).astype(float)


def f09_irgd_153_log_size_most_recent_partial_up_gap_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-size of most-recent partial up-gap (log(open/prior_close)) in last 21d. 0 if none."""
    pug = _partial_up_gap(open_, high, low, close)
    log_g = (_safe_log(open_) - _safe_log(close.shift(1))).where(pug, np.nan)
    return log_g.rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_154_atr_size_most_recent_partial_up_gap_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized size of most-recent partial up-gap in 21d."""
    pug = _partial_up_gap(open_, high, low, close)
    g = (open_ - close.shift(1)).where(pug, np.nan)
    return _safe_div(g, _atr(high, low, close, n=MDAYS)).rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_155_count_partial_up_gaps_in_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of partial up-gap days in trailing 252 bars."""
    return _partial_up_gap(open_, high, low, close).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_156_count_partial_down_gaps_in_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of partial down-gap days in trailing 252 bars."""
    return _partial_down_gap(open_, high, low, close).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_157_partial_to_full_up_gap_ratio_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: partial up-gap count / full up-gap count in trailing 252d (regime indicator)."""
    pug = _partial_up_gap(open_, high, low, close).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    fug = _full_up_gap(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pug, fug)


def f09_irgd_158_partial_up_gap_followthrough_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of partial up-gap days in last 252d that closed above open (bullish followthrough)."""
    pug = _partial_up_gap(open_, high, low, close)
    ft = (pug & (close > open_)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = pug.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(ft, tot)


def f09_irgd_159_partial_up_gap_fade_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of partial up-gap days that faded (close < open)."""
    pug = _partial_up_gap(open_, high, low, close)
    fade = (pug & (close < open_)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = pug.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fade, tot)


def f09_irgd_160_any_gap_indicator_full_or_partial(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: any kind of gap (full up, full down, partial up, partial down) today."""
    return (_full_up_gap(high, low) | _full_down_gap(high, low) |
            _partial_up_gap(open_, high, low, close) | _partial_down_gap(open_, high, low, close)).astype(float)


# ============================================================
# Bucket B — Inside-day / outside-day after gap (161-167)
# ============================================================

def f09_irgd_161_inside_day_after_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today is an inside bar AND yesterday was a full up-gap day — consolidation after gap."""
    yesterday_was_gap = _full_up_gap(high, low).shift(1).fillna(False)
    return (_inside_bar(high, low) & yesterday_was_gap).astype(float)


def f09_irgd_162_count_inside_days_after_up_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of inside-bar-after-up-gap events in last 252 bars."""
    ev = _inside_bar(high, low) & _full_up_gap(high, low).shift(1).fillna(False)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_163_outside_day_after_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today is an outside bar AND yesterday was a full up-gap day — engulf reversal."""
    yesterday_was_gap = _full_up_gap(high, low).shift(1).fillna(False)
    return (_outside_bar(high, low) & yesterday_was_gap).astype(float)


def f09_irgd_164_count_outside_days_after_up_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of outside-bar-after-up-gap events in last 252 bars."""
    ev = _outside_bar(high, low) & _full_up_gap(high, low).shift(1).fillna(False)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_165_inside_day_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """General inside-bar count in trailing 252d — consolidation density."""
    return _inside_bar(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_166_max_consecutive_inside_days_after_up_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of consecutive inside bars following any up-gap in last 252d."""
    streak = _streak(_inside_bar(high, low).fillna(False))
    after_gap = _full_up_gap(high, low).shift(1).fillna(False).rolling(MDAYS, min_periods=1).max()
    return streak.where(after_gap == 1, 0).rolling(YDAYS, min_periods=QDAYS).max()


def f09_irgd_167_outside_day_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """General outside-bar count in trailing 252d — expansion density."""
    return _outside_bar(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Pre-gap setup (compression / coiling) (168-174)
# ============================================================

def f09_irgd_168_atr_compression_5d_before_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap today AND 5d ATR going into gap was < 70% of 21d ATR — coiled spring."""
    atr5 = _atr(high, low, close, n=WDAYS)
    atr21 = _atr(high, low, close, n=MDAYS)
    compressed = (atr5.shift(1) < 0.7 * atr21.shift(1))
    return (_full_up_gap(high, low) & compressed).astype(float)


def f09_irgd_169_atr_compression_zscore_before_up_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5d ATR / 21d ATR ratio at most-recent up-gap day (negative = compressed) vs 252d distribution."""
    atr5 = _atr(high, low, close, n=WDAYS)
    atr21 = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(atr5, atr21)
    z = _rolling_zscore(ratio, YDAYS, min_periods=QDAYS)
    z_at_gap = z.shift(1).where(_full_up_gap(high, low), np.nan).ffill()
    return z_at_gap


def f09_irgd_170_range_compression_5d_before_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of (5d range) / (21d avg true range) at the day BEFORE most-recent up-gap. Smaller = tighter pre-gap coil."""
    rng5 = (high.rolling(WDAYS, min_periods=WDAYS).max() - low.rolling(WDAYS, min_periods=WDAYS).min()).shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    ratio = _safe_div(rng5, atr21 * MDAYS)
    return ratio.where(_full_up_gap(high, low), np.nan).ffill()


def f09_irgd_171_low_volume_before_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: 5d avg volume going into gap < 50% of 21d avg volume — quiet-before-the-storm pre-gap."""
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean().shift(1)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    low_vol = v5 < 0.5 * v21
    return (_full_up_gap(high, low) & low_vol).astype(float)


def f09_irgd_172_close_tight_band_before_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 5d (max close - min close) / mean close < 2% before today's full up-gap."""
    cmax = close.rolling(WDAYS, min_periods=WDAYS).max().shift(1)
    cmin = close.rolling(WDAYS, min_periods=WDAYS).min().shift(1)
    cmean = close.rolling(WDAYS, min_periods=WDAYS).mean().shift(1)
    tight = _safe_div(cmax - cmin, cmean) < 0.02
    return (_full_up_gap(high, low) & tight).astype(float)


def f09_irgd_173_count_consolidation_then_gap_events_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (gap-up day where 5d ATR < 70% of 21d ATR going in) events in trailing 252d."""
    atr5 = _atr(high, low, close, n=WDAYS); atr21 = _atr(high, low, close, n=MDAYS)
    compressed = (atr5.shift(1) < 0.7 * atr21.shift(1))
    ev = _full_up_gap(high, low) & compressed
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_174_volume_buildup_5d_before_up_gap_zscore(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of mean volume over 5 bars before up-gap (vs 252d volume distribution)."""
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean().shift(1)
    z = _rolling_zscore(v5, YDAYS, min_periods=QDAYS)
    return z.where(_full_up_gap(high, low), np.nan).ffill()


# ============================================================
# Bucket D — Gap-and-go vs gap-and-fade rates (175-181)
# ============================================================

def f09_irgd_175_gap_and_go_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap AND close > open AND close > prior_high — bullish gap-and-go."""
    return (_full_up_gap(high, low) & (close > open_) & (close > high.shift(1))).astype(float)


def f09_irgd_176_gap_and_fade_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap AND close < prior_close — full bearish reversal of gap."""
    return (_full_up_gap(high, low) & (close < close.shift(1))).astype(float)


def f09_irgd_177_gap_and_go_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of up-gap days in last 252d that were gap-and-go."""
    go = (_full_up_gap(high, low) & (close > open_) & (close > high.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = _full_up_gap(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(go, tot)


def f09_irgd_178_gap_and_fade_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of up-gap days in last 252d that faded fully (close < prior close)."""
    fade = (_full_up_gap(high, low) & (close < close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = _full_up_gap(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fade, tot)


def f09_irgd_179_gap_and_go_minus_fade_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Net regime: gap_and_go rate minus gap_and_fade rate in last 252d."""
    return f09_irgd_177_gap_and_go_rate_252d(open_, high, low, close) - f09_irgd_178_gap_and_fade_rate_252d(open_, high, low, close)


def f09_irgd_180_consecutive_gap_and_go_days_streak(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak of consecutive gap-and-go days (gap-and-go indicator true)."""
    cond = (_full_up_gap(high, low) & (close > open_) & (close > high.shift(1))).fillna(False)
    return _streak(cond)


def f09_irgd_181_count_successful_gap_followthrough_5d_after_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gap days (in last 252d) where close was higher 5 bars later than gap-day close. PIT-safe via lag."""
    gap_lag = _full_up_gap(high, low).shift(WDAYS).fillna(False)
    close_at_gap_lag = close.shift(WDAYS)
    followthrough = (close > close_at_gap_lag) & gap_lag
    return followthrough.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket E — Isolated catalyst-style gaps (182-186)
# ============================================================

def f09_irgd_182_isolated_up_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap today AND no full up-gap in prior 21d (isolated catalyst-style)."""
    upg = _full_up_gap(high, low)
    no_prior = (upg.shift(1).rolling(MDAYS, min_periods=1).sum() == 0)
    return (upg & no_prior).astype(float)


def f09_irgd_183_isolated_down_gap_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full down-gap today AND no down-gap in prior 21d."""
    dng = _full_down_gap(high, low)
    no_prior = (dng.shift(1).rolling(MDAYS, min_periods=1).sum() == 0)
    return (dng & no_prior).astype(float)


def f09_irgd_184_count_isolated_up_gaps_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of isolated up-gap events in last 252d."""
    upg = _full_up_gap(high, low)
    no_prior = (upg.shift(1).rolling(MDAYS, min_periods=1).sum() == 0)
    return (upg & no_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_185_count_isolated_down_gaps_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of isolated down-gap events in last 252d."""
    dng = _full_down_gap(high, low)
    no_prior = (dng.shift(1).rolling(MDAYS, min_periods=1).sum() == 0)
    return (dng & no_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_186_bars_since_last_isolated_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most-recent isolated up-gap event."""
    upg = _full_up_gap(high, low)
    no_prior = (upg.shift(1).rolling(MDAYS, min_periods=1).sum() == 0)
    return _bars_since((upg & no_prior).fillna(False))


# ============================================================
# Bucket F — Successive-gap stacking (187-190)
# ============================================================

def f09_irgd_187_successive_larger_up_gaps_count_in_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of consecutive up-gap days in last 5 bars where each gap was larger than the prior up-gap."""
    g = (low - high.shift(1)).where(_full_up_gap(high, low), np.nan)
    g_prior = g.ffill().shift(1)
    larger = (g > g_prior).fillna(False) & _full_up_gap(high, low)
    return larger.astype(float).rolling(WDAYS, min_periods=1).sum()


def f09_irgd_188_successive_larger_up_gaps_count_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of larger-than-prior up-gaps in last 21d."""
    g = (low - high.shift(1)).where(_full_up_gap(high, low), np.nan)
    g_prior = g.ffill().shift(1)
    larger = (g > g_prior).fillna(False) & _full_up_gap(high, low)
    return larger.astype(float).rolling(MDAYS, min_periods=1).sum()


def f09_irgd_189_successive_smaller_up_gaps_count_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of smaller-than-prior up-gaps in last 21d — decaying gap pattern."""
    g = (low - high.shift(1)).where(_full_up_gap(high, low), np.nan)
    g_prior = g.ffill().shift(1)
    smaller = (g < g_prior).fillna(False) & _full_up_gap(high, low)
    return smaller.astype(float).rolling(MDAYS, min_periods=1).sum()


def f09_irgd_190_gap_size_slope_last_5_up_gaps(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of the last 5 up-gap log sizes — accelerating vs decelerating gaps."""
    log_g = (_safe_log(low) - _safe_log(high.shift(1))).where(_full_up_gap(high, low), np.nan).fillna(0)
    return _rolling_slope(log_g, MDAYS * 3, min_periods=WDAYS)


# ============================================================
# Bucket G — Gap into new 52w / 5y highs (191-196)
# ============================================================

def f09_irgd_191_gap_up_into_new_52w_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap AND today's high > trailing 252d max excluding today."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (_full_up_gap(high, low) & (high > rmax_excl)).astype(float)


def f09_irgd_192_count_gap_up_into_new_52w_high_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap-up-into-new-52w-high events in last 252d."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = _full_up_gap(high, low) & (high > rmax_excl)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_193_gap_up_into_new_5y_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full up-gap AND high > trailing 1260d max excluding today."""
    rmax_excl = high.shift(1).rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_full_up_gap(high, low) & (high > rmax_excl)).astype(float)


def f09_irgd_194_bars_since_last_gap_up_into_new_52w_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent gap-up into new 52w high."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since((_full_up_gap(high, low) & (high > rmax_excl)).fillna(False))


def f09_irgd_195_gap_down_into_new_52w_low_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full down-gap AND today's low < trailing 252d min excluding today — capitulation-style."""
    rmin_excl = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    return (_full_down_gap(high, low) & (low < rmin_excl)).astype(float)


def f09_irgd_196_count_gap_down_into_new_52w_low_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap-down-into-new-52w-low events in last 252d."""
    rmin_excl = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    ev = _full_down_gap(high, low) & (low < rmin_excl)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket H — Gap-down warning during uptrend (197-200)
# ============================================================

def f09_irgd_197_gap_down_during_uptrend_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full down-gap on a bar where close > 252d SMA AND 21d SMA > 21d SMA from 21d ago — uptrend down-gap."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    sma21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    in_uptrend = (close > sma252) & (sma21 > sma21.shift(MDAYS))
    return (_full_down_gap(high, low) & in_uptrend).astype(float)


def f09_irgd_198_count_gap_down_during_uptrend_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of down-gap-during-uptrend events in last 252d — early warning count."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    sma21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    in_uptrend = (close > sma252) & (sma21 > sma21.shift(MDAYS))
    ev = _full_down_gap(high, low) & in_uptrend
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_199_gap_down_after_new_high_within_5d_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full down-gap today AND a new 52w high was set within last 5 bars — classic top warning."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high_recent = (high.shift(1) >= rmax_excl.shift(1)).rolling(WDAYS, min_periods=1).max().fillna(0)
    return (_full_down_gap(high, low) & (new_high_recent == 1)).astype(float)


def f09_irgd_200_count_gap_down_after_new_high_within_5d_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap-down-after-recent-new-high events in last 252d."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high_recent = (high.shift(1) >= rmax_excl.shift(1)).rolling(WDAYS, min_periods=1).max().fillna(0)
    ev = _full_down_gap(high, low) & (new_high_recent == 1)
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket I — Gap retest / quick-fill / peak-day metrics (201-207)
# ============================================================

def f09_irgd_201_gap_retest_within_5d_not_filled_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: most-recent up-gap is 1-5 bars old AND today's low touched gap zone (within 1% of prior_high)
    but did NOT close it (low > prior_high)."""
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(close)
    bsu_arr = bsu.to_numpy(); low_arr = low.to_numpy(); high_arr = high.to_numpy()
    out = np.full(n, 0.0)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < 1 or b > WDAYS: continue
        j = int(i - int(b))
        if j < 1: continue
        prior_high = high_arr[j - 1]
        l_today = low_arr[i]
        if np.isnan(prior_high) or np.isnan(l_today): continue
        if (l_today <= prior_high * 1.01) and (l_today > prior_high):
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f09_irgd_202_count_gap_retests_not_filled_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap retest events (touched but didn't fill) in last 252d."""
    return f09_irgd_201_gap_retest_within_5d_not_filled_indicator(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_203_quick_fill_up_gap_within_2d_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: an up-gap occurred 1-2 bars ago AND today's low <= gap floor (filled within 2 bars)."""
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(close)
    bsu_arr = bsu.to_numpy(); low_arr = low.to_numpy(); high_arr = high.to_numpy()
    out = np.full(n, 0.0)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < 1 or b > 2: continue
        j = int(i - int(b))
        if j < 1: continue
        prior_high = high_arr[j - 1]
        if np.isnan(prior_high) or np.isnan(low_arr[i]): continue
        if low_arr[i] <= prior_high:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f09_irgd_204_count_quick_fill_up_gaps_within_2d_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gap-quickly-filled events in last 252d — fragile-gap regime."""
    return f09_irgd_203_quick_fill_up_gap_within_2d_indicator(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_205_gap_day_was_5d_peak_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: most-recent up-gap day's high is the 5-day-forward max — gap day was the peak."""
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(close)
    bsu_arr = bsu.to_numpy(); high_arr = high.to_numpy()
    out = np.full(n, 0.0)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        gap_high = high_arr[j]
        post = high_arr[j + 1:j + 1 + WDAYS]
        if np.isnan(gap_high) or post.size == 0: continue
        post_max = np.nanmax(post)
        if np.isnan(post_max): continue
        out[i] = float(gap_high >= post_max)
    return pd.Series(out, index=close.index)


def f09_irgd_206_count_gap_day_peak_events_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap-day-was-5d-peak events in last 252d — gap-as-peak regime."""
    return f09_irgd_205_gap_day_was_5d_peak_indicator(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_207_gap_fill_velocity_atr_per_bar_most_recent_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent FILLED up-gap in last 252d: gap size (ATR-normalized) / bars-to-fill."""
    atr_s = _atr(high, low, close, n=MDAYS)
    n = len(high)
    high_arr = high.to_numpy(); low_arr = low.to_numpy(); atr_arr = atr_s.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        # scan back to find most recent filled up-gap
        for k in range(i, start, -1):
            if k < 1: break
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i >= k + 1:
                window_low = low_arr[k + 1:i + 1]
                hits = np.where(window_low <= gap_floor)[0]
                if hits.size > 0:
                    bars_to_fill = float(hits[0] + 1)
                    gap_size = low_arr[k] - high_arr[k - 1]
                    if not np.isnan(atr_arr[k]) and atr_arr[k] > 0 and bars_to_fill > 0:
                        out[i] = (gap_size / atr_arr[k]) / bars_to_fill
                    break
    return pd.Series(out, index=high.index)


# ============================================================
# Bucket J — Exhaustion down-gaps (208-211)
# ============================================================

def f09_irgd_208_exhaustion_down_gap_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: full down-gap on a bar where close < 252d SMA for last 60d AND close in bottom decile of 252d range — capitulation."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below60 = (close < sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_bot = pos <= 0.1
    return (_full_down_gap(high, low) & below60 & in_bot).astype(float)


def f09_irgd_209_count_exhaustion_down_gaps_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of exhaustion down-gap events in last 252d."""
    return f09_irgd_208_exhaustion_down_gap_indicator(open_, high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_210_exhaustion_down_gap_size_atr_most_recent_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-size of most-recent exhaustion down-gap in last 252d."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below60 = (close < sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_bot = pos <= 0.1
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(low.shift(1) - high, atr).where(_full_down_gap(high, low) & below60 & in_bot, np.nan)
    return sz.rolling(YDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_211_exhaustion_down_gap_with_strong_close_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: exhaustion down-gap day where close in TOP 20% of intraday range (reversal candle bullish bottom)."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below60 = (close < sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos252 = _safe_div(close - lo252, hi252 - lo252)
    in_bot = pos252 <= 0.1
    pos_intra = _safe_div(close - low, high - low)
    return (_full_down_gap(high, low) & below60 & in_bot & (pos_intra >= 0.8)).astype(float)


# ============================================================
# Bucket K — Half-gap / inside-bar followthrough / continuation (212-217)
# ============================================================

def f09_irgd_212_half_gap_up_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-gap up: open is exactly at prior high (within 0.1%) — borderline between full and partial gap."""
    diff = (open_ - high.shift(1)).abs()
    return (diff <= 0.001 * close.shift(1)).astype(float)


def f09_irgd_213_inside_bar_break_above_after_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (inside bar after up-gap → next bar high > inside-bar high) events in last 252d — continuation followthrough."""
    inside_after_gap = (_inside_bar(high, low) & _full_up_gap(high, low).shift(1).fillna(False))
    next_break = (high > high.shift(1)).fillna(False) & inside_after_gap.shift(1).fillna(False)
    return next_break.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_214_inside_bar_break_below_after_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (inside bar after up-gap → next bar low < inside-bar low) events — failed-continuation count."""
    inside_after_gap = (_inside_bar(high, low) & _full_up_gap(high, low).shift(1).fillna(False))
    next_break_down = (low < low.shift(1)).fillna(False) & inside_after_gap.shift(1).fillna(False)
    return next_break_down.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_215_consecutive_higher_highs_after_up_gap_5d_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap (last 63d): count of consecutive higher highs in 5 bars after."""
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy(); high_arr = high.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        post = high_arr[j + 1:j + 1 + WDAYS]
        if post.size == 0 or np.all(np.isnan(post)): continue
        streak = 0
        prev = high_arr[j]
        for v in post:
            if not np.isnan(v) and not np.isnan(prev) and v > prev:
                streak += 1; prev = v
            else:
                break
        out[i] = float(streak)
    return pd.Series(out, index=high.index)


def f09_irgd_216_consecutive_higher_lows_after_up_gap_5d_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap: count of consecutive higher lows in 5 bars after."""
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy(); low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        post = low_arr[j + 1:j + 1 + WDAYS]
        if post.size == 0 or np.all(np.isnan(post)): continue
        streak = 0
        prev = low_arr[j]
        for v in post:
            if not np.isnan(v) and not np.isnan(prev) and v > prev:
                streak += 1; prev = v
            else:
                break
        out[i] = float(streak)
    return pd.Series(out, index=high.index)


def f09_irgd_217_gap_into_consolidation_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap day was followed by 3+ inside bars in the next 5 bars (immediate consolidation post-gap)."""
    inside_bar = _inside_bar(high, low).astype(float)
    bsu = _bars_since(_full_up_gap(high, low).fillna(False))
    n = len(close)
    bsu_arr = bsu.to_numpy(); inside_arr = inside_bar.to_numpy()
    out = np.full(n, 0.0)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b != WDAYS: continue
        j = int(i - int(b))
        if j < 0: continue
        post = inside_arr[j + 1:j + 1 + WDAYS]
        if np.sum(post) >= 3:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket L — Composite top / bottom gap signatures (218-225)
# ============================================================

def f09_irgd_218_terminal_gap_top_composite_weighted_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite top: 3 × gap-up-into-new-52w-high + 2 × gap-and-fade-rate + 1 × gap-day-peak rate + 1 × inside-day-after-gap."""
    a = f09_irgd_192_count_gap_up_into_new_52w_high_252d(high, low, close).fillna(0)
    b = f09_irgd_178_gap_and_fade_rate_252d(open_, high, low, close).fillna(0)
    c = f09_irgd_206_count_gap_day_peak_events_252d(high, low, close).fillna(0)
    d = f09_irgd_162_count_inside_days_after_up_gap_252d(high, low, close).fillna(0)
    return 3.0 * a + 2.0 * b + c + d


def f09_irgd_219_capitulation_bottom_gap_composite_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite bottom: exhaustion-down-gaps + gap-down-into-new-low + exhaustion-with-strong-close."""
    a = f09_irgd_209_count_exhaustion_down_gaps_252d(open_, high, low, close).fillna(0)
    b = f09_irgd_196_count_gap_down_into_new_52w_low_252d(high, low, close).fillna(0)
    c = f09_irgd_211_exhaustion_down_gap_with_strong_close_indicator(open_, high, low, close).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    return a + b + c


def f09_irgd_220_post_gap_distribution_top_indicator_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: in last 21d there was a gap-up-into-new-52w-high AND gap-and-fade today AND inside-day-after-gap in last 5d."""
    rmax_excl = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    recent_new_high_gap = (_full_up_gap(high, low) & (high > rmax_excl)).rolling(MDAYS, min_periods=1).max().fillna(0)
    fade_today = (_full_up_gap(high, low) & (close < close.shift(1)))
    inside_after_gap_recent = (_inside_bar(high, low) & _full_up_gap(high, low).shift(1).fillna(False)).rolling(WDAYS, min_periods=1).max().fillna(0)
    return (recent_new_high_gap.astype(bool) & fade_today & inside_after_gap_recent.astype(bool)).astype(float)


def f09_irgd_221_breakaway_then_exhaustion_pattern_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: breakaway gap-up occurred 30-90 bars ago AND exhaustion gap-up today (price now in top decile)."""
    atr5 = _atr(high, low, close, n=WDAYS); atr21 = _atr(high, low, close, n=MDAYS)
    compress = atr5 < 0.7 * atr21
    breakaway_old = (_full_up_gap(high, low) & compress).shift(QDAYS).rolling(QDAYS - MDAYS, min_periods=1).max().fillna(0)
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    exh_today = _full_up_gap(high, low) & above60 & in_top
    return (breakaway_old.astype(bool) & exh_today).astype(float)


def f09_irgd_222_gap_regime_stability_score_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: |gap_and_go_rate - gap_and_fade_rate| × total_gap_count_252d — strong directional gap regime."""
    go = f09_irgd_177_gap_and_go_rate_252d(open_, high, low, close).fillna(0)
    fade = f09_irgd_178_gap_and_fade_rate_252d(open_, high, low, close).fillna(0)
    cnt = _full_up_gap(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (go - fade).abs() * cnt


def f09_irgd_223_pre_gap_compression_signal_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score: count of compression-then-gap events × mean volume-buildup zscore — preparation quality."""
    atr5 = _atr(high, low, close, n=WDAYS); atr21 = _atr(high, low, close, n=MDAYS)
    compressed = atr5.shift(1) < 0.7 * atr21.shift(1)
    ev = _full_up_gap(high, low) & compressed
    cnt = ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean().shift(1)
    z = _rolling_zscore(v5, YDAYS, min_periods=QDAYS).where(ev, np.nan)
    mean_z = z.rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    return cnt * mean_z.clip(lower=0)


def f09_irgd_224_gap_top_intensity_zscore_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (number of up-gaps in last 21d × mean gap size) vs 252d distribution of same metric."""
    cnt_21 = _full_up_gap(high, low).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    sizes = (low - high.shift(1)).where(_full_up_gap(high, low), 0)
    sum_size_21 = sizes.rolling(MDAYS, min_periods=WDAYS).sum()
    intensity = cnt_21 * sum_size_21
    return _rolling_zscore(intensity, YDAYS, min_periods=QDAYS)


def f09_irgd_225_full_top_gap_signature_weighted(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final weighted top: 3 × terminal_gap_top + 2 × gap_intensity_zscore + 1 × distribution_top_indicator + 1 × post-gap-peak count."""
    a = f09_irgd_218_terminal_gap_top_composite_weighted_252d(open_, high, low, close).fillna(0)
    b = f09_irgd_224_gap_top_intensity_zscore_252d(open_, high, low, close).fillna(0)
    c = f09_irgd_220_post_gap_distribution_top_indicator_252d(open_, high, low, close).fillna(0)
    d = f09_irgd_206_count_gap_day_peak_events_252d(high, low, close).fillna(0)
    return 3.0 * a + 2.0 * b + c + d


# ============================================================
#                         REGISTRY 151-225
# ============================================================

ISLAND_REVERSAL_GAP_DYNAMICS_BASE_REGISTRY_151_225 = {
    "f09_irgd_151_partial_up_gap_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_151_partial_up_gap_indicator},
    "f09_irgd_152_partial_down_gap_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_152_partial_down_gap_indicator},
    "f09_irgd_153_log_size_most_recent_partial_up_gap_21d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_153_log_size_most_recent_partial_up_gap_21d},
    "f09_irgd_154_atr_size_most_recent_partial_up_gap_21d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_154_atr_size_most_recent_partial_up_gap_21d},
    "f09_irgd_155_count_partial_up_gaps_in_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_155_count_partial_up_gaps_in_252d},
    "f09_irgd_156_count_partial_down_gaps_in_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_156_count_partial_down_gaps_in_252d},
    "f09_irgd_157_partial_to_full_up_gap_ratio_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_157_partial_to_full_up_gap_ratio_252d},
    "f09_irgd_158_partial_up_gap_followthrough_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_158_partial_up_gap_followthrough_rate_252d},
    "f09_irgd_159_partial_up_gap_fade_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_159_partial_up_gap_fade_rate_252d},
    "f09_irgd_160_any_gap_indicator_full_or_partial": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_160_any_gap_indicator_full_or_partial},
    "f09_irgd_161_inside_day_after_up_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_161_inside_day_after_up_gap_indicator},
    "f09_irgd_162_count_inside_days_after_up_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_162_count_inside_days_after_up_gap_252d},
    "f09_irgd_163_outside_day_after_up_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_163_outside_day_after_up_gap_indicator},
    "f09_irgd_164_count_outside_days_after_up_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_164_count_outside_days_after_up_gap_252d},
    "f09_irgd_165_inside_day_count_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_165_inside_day_count_252d},
    "f09_irgd_166_max_consecutive_inside_days_after_up_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_166_max_consecutive_inside_days_after_up_gap_252d},
    "f09_irgd_167_outside_day_count_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_167_outside_day_count_252d},
    "f09_irgd_168_atr_compression_5d_before_up_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_168_atr_compression_5d_before_up_gap_indicator},
    "f09_irgd_169_atr_compression_zscore_before_up_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_169_atr_compression_zscore_before_up_gap_252d},
    "f09_irgd_170_range_compression_5d_before_up_gap": {"inputs": ["high", "low", "close"], "func": f09_irgd_170_range_compression_5d_before_up_gap},
    "f09_irgd_171_low_volume_before_up_gap_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_171_low_volume_before_up_gap_indicator},
    "f09_irgd_172_close_tight_band_before_up_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_172_close_tight_band_before_up_gap_indicator},
    "f09_irgd_173_count_consolidation_then_gap_events_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_173_count_consolidation_then_gap_events_252d},
    "f09_irgd_174_volume_buildup_5d_before_up_gap_zscore": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_174_volume_buildup_5d_before_up_gap_zscore},
    "f09_irgd_175_gap_and_go_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_175_gap_and_go_indicator},
    "f09_irgd_176_gap_and_fade_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_176_gap_and_fade_indicator},
    "f09_irgd_177_gap_and_go_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_177_gap_and_go_rate_252d},
    "f09_irgd_178_gap_and_fade_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_178_gap_and_fade_rate_252d},
    "f09_irgd_179_gap_and_go_minus_fade_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_179_gap_and_go_minus_fade_rate_252d},
    "f09_irgd_180_consecutive_gap_and_go_days_streak": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_180_consecutive_gap_and_go_days_streak},
    "f09_irgd_181_count_successful_gap_followthrough_5d_after_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_181_count_successful_gap_followthrough_5d_after_252d},
    "f09_irgd_182_isolated_up_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_182_isolated_up_gap_indicator},
    "f09_irgd_183_isolated_down_gap_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_183_isolated_down_gap_indicator},
    "f09_irgd_184_count_isolated_up_gaps_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_184_count_isolated_up_gaps_252d},
    "f09_irgd_185_count_isolated_down_gaps_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_185_count_isolated_down_gaps_252d},
    "f09_irgd_186_bars_since_last_isolated_up_gap": {"inputs": ["high", "low", "close"], "func": f09_irgd_186_bars_since_last_isolated_up_gap},
    "f09_irgd_187_successive_larger_up_gaps_count_in_5d": {"inputs": ["high", "low", "close"], "func": f09_irgd_187_successive_larger_up_gaps_count_in_5d},
    "f09_irgd_188_successive_larger_up_gaps_count_in_21d": {"inputs": ["high", "low", "close"], "func": f09_irgd_188_successive_larger_up_gaps_count_in_21d},
    "f09_irgd_189_successive_smaller_up_gaps_count_in_21d": {"inputs": ["high", "low", "close"], "func": f09_irgd_189_successive_smaller_up_gaps_count_in_21d},
    "f09_irgd_190_gap_size_slope_last_5_up_gaps": {"inputs": ["high", "low", "close"], "func": f09_irgd_190_gap_size_slope_last_5_up_gaps},
    "f09_irgd_191_gap_up_into_new_52w_high_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_191_gap_up_into_new_52w_high_indicator},
    "f09_irgd_192_count_gap_up_into_new_52w_high_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_192_count_gap_up_into_new_52w_high_252d},
    "f09_irgd_193_gap_up_into_new_5y_high_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_193_gap_up_into_new_5y_high_indicator},
    "f09_irgd_194_bars_since_last_gap_up_into_new_52w_high": {"inputs": ["high", "low", "close"], "func": f09_irgd_194_bars_since_last_gap_up_into_new_52w_high},
    "f09_irgd_195_gap_down_into_new_52w_low_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_195_gap_down_into_new_52w_low_indicator},
    "f09_irgd_196_count_gap_down_into_new_52w_low_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_196_count_gap_down_into_new_52w_low_252d},
    "f09_irgd_197_gap_down_during_uptrend_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_197_gap_down_during_uptrend_indicator},
    "f09_irgd_198_count_gap_down_during_uptrend_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_198_count_gap_down_during_uptrend_252d},
    "f09_irgd_199_gap_down_after_new_high_within_5d_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_199_gap_down_after_new_high_within_5d_indicator},
    "f09_irgd_200_count_gap_down_after_new_high_within_5d_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_200_count_gap_down_after_new_high_within_5d_252d},
    "f09_irgd_201_gap_retest_within_5d_not_filled_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_201_gap_retest_within_5d_not_filled_indicator},
    "f09_irgd_202_count_gap_retests_not_filled_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_202_count_gap_retests_not_filled_in_252d},
    "f09_irgd_203_quick_fill_up_gap_within_2d_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_203_quick_fill_up_gap_within_2d_indicator},
    "f09_irgd_204_count_quick_fill_up_gaps_within_2d_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_204_count_quick_fill_up_gaps_within_2d_252d},
    "f09_irgd_205_gap_day_was_5d_peak_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_205_gap_day_was_5d_peak_indicator},
    "f09_irgd_206_count_gap_day_peak_events_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_206_count_gap_day_peak_events_252d},
    "f09_irgd_207_gap_fill_velocity_atr_per_bar_most_recent_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_207_gap_fill_velocity_atr_per_bar_most_recent_252d},
    "f09_irgd_208_exhaustion_down_gap_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_208_exhaustion_down_gap_indicator},
    "f09_irgd_209_count_exhaustion_down_gaps_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_209_count_exhaustion_down_gaps_252d},
    "f09_irgd_210_exhaustion_down_gap_size_atr_most_recent_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_210_exhaustion_down_gap_size_atr_most_recent_252d},
    "f09_irgd_211_exhaustion_down_gap_with_strong_close_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_211_exhaustion_down_gap_with_strong_close_indicator},
    "f09_irgd_212_half_gap_up_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_212_half_gap_up_indicator},
    "f09_irgd_213_inside_bar_break_above_after_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_213_inside_bar_break_above_after_gap_252d},
    "f09_irgd_214_inside_bar_break_below_after_gap_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_214_inside_bar_break_below_after_gap_252d},
    "f09_irgd_215_consecutive_higher_highs_after_up_gap_5d_streak": {"inputs": ["high", "low", "close"], "func": f09_irgd_215_consecutive_higher_highs_after_up_gap_5d_streak},
    "f09_irgd_216_consecutive_higher_lows_after_up_gap_5d_streak": {"inputs": ["high", "low", "close"], "func": f09_irgd_216_consecutive_higher_lows_after_up_gap_5d_streak},
    "f09_irgd_217_gap_into_consolidation_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_217_gap_into_consolidation_indicator},
    "f09_irgd_218_terminal_gap_top_composite_weighted_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_218_terminal_gap_top_composite_weighted_252d},
    "f09_irgd_219_capitulation_bottom_gap_composite_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_219_capitulation_bottom_gap_composite_252d},
    "f09_irgd_220_post_gap_distribution_top_indicator_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_220_post_gap_distribution_top_indicator_252d},
    "f09_irgd_221_breakaway_then_exhaustion_pattern_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_221_breakaway_then_exhaustion_pattern_252d},
    "f09_irgd_222_gap_regime_stability_score_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_222_gap_regime_stability_score_252d},
    "f09_irgd_223_pre_gap_compression_signal_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_223_pre_gap_compression_signal_score_252d},
    "f09_irgd_224_gap_top_intensity_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_224_gap_top_intensity_zscore_252d},
    "f09_irgd_225_full_top_gap_signature_weighted": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_225_full_top_gap_signature_weighted},
}
