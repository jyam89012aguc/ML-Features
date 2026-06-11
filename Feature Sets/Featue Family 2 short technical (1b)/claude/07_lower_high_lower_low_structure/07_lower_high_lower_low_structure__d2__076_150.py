"""lower_high_lower_low_structure d2 features 076-150 — Pipeline 1b-technical.

Continuation of the Dow-theory uptrend-breakdown family. Buckets here:
  L. Pivot-low break events (close below recent pivot-low, severity)
  M. Dow-theory composites (combined HH/HL/LL/LH state metrics)
  N. Swing fan / channel breakdown
  O. Fractal patterns (Bill Williams 5-bar fractals; bullish vs bearish; ratio)
  P. New-N-day-high vs new-N-day-low race
  Q. Cross-horizon HH/LL transitions and regime-change indicators

SEP OHLCV only. PIT-clean.
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


def _pivot_high_event(high, n):
    window = 2 * n + 1
    rolling_max = high.rolling(window, min_periods=window).max()
    center_val = high.shift(n)
    return (center_val == rolling_max) & rolling_max.notna()


def _pivot_low_event(low, n):
    window = 2 * n + 1
    rolling_min = low.rolling(window, min_periods=window).min()
    center_val = low.shift(n)
    return (center_val == rolling_min) & rolling_min.notna()


def _pivot_high_value(high, n):
    evt = _pivot_high_event(high, n)
    val = high.shift(n)
    return val.where(evt, np.nan)


def _pivot_low_value(low, n):
    evt = _pivot_low_event(low, n)
    val = low.shift(n)
    return val.where(evt, np.nan)


# ============================================================
# Bucket L — Pivot-low break events (076-084)
# ============================================================

def f07_lhll_076_close_below_recent_pivot10_low_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when today's close < most-recent confirmed pivot10-low (support break)."""
    pv = _pivot_low_value(low, 10).ffill()
    return (close < pv).astype(float).where(pv.notna(), np.nan)


def f07_lhll_077_close_below_recent_pivot21_low_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when close < most-recent pivot21-low (long-base support break)."""
    pv = _pivot_low_value(low, 21).ffill()
    return (close < pv).astype(float).where(pv.notna(), np.nan)


def f07_lhll_078_pivot_low_break_event_count_pivot10_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of NEW pivot10-low-break events in trailing 252d (transitions from 0 -> 1
    of the indicator). Captures discrete breakdown events not just persistent state."""
    pv = _pivot_low_value(low, 10).ffill()
    ind = (close < pv).astype(float)
    ind_prev = ind.shift(1)
    evt = ((ind > 0.5) & (ind_prev < 0.5)).astype(float)
    return evt.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_079_pivot_low_break_event_count_pivot21_504d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of pivot21-low-break events in trailing 504d."""
    pv = _pivot_low_value(low, 21).ffill()
    ind = (close < pv).astype(float)
    evt = ((ind > 0.5) & (ind.shift(1) < 0.5)).astype(float)
    return evt.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_080_pivot_low_break_severity_atr_pivot10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized severity of pivot10-low break: (pivot10-low - close) / ATR21
    when close < pivot10-low; else NaN. Carries forward last severity."""
    pv = _pivot_low_value(low, 10).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    sev = _safe_div(pv - close, atr)
    return sev.where(close < pv, np.nan)


def f07_lhll_081_pivot_low_break_severity_log_pivot10(low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance below most-recent pivot10-low (when broken)."""
    pv = _pivot_low_value(low, 10).ffill()
    diff = _safe_log(pv) - _safe_log(close)
    return diff.where(close < pv, np.nan)


def f07_lhll_082_bars_below_pivot10_low_streak(low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bars streak with close < most-recent pivot10-low."""
    pv = _pivot_low_value(low, 10).ffill().values
    cl = close.values
    n = len(cl)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(pv[i]) or np.isnan(cl[i]):
            out[i] = np.nan
        else:
            streak = streak + 1 if cl[i] < pv[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=low.index)


def f07_lhll_083_count_pivot10_lows_broken_in_504d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of DISTINCT pivot10-low levels that have been violated by close in the
    trailing 504d window (each unique pivot-low broken counts once)."""
    pv = _pivot_low_value(low, 10).values
    cl = close.values
    n = len(cl)
    out = np.full(n, np.nan, dtype=float)
    win = DDAYS_2Y
    for i in range(n):
        if i < YDAYS:
            continue
        lo = max(0, i - win + 1)
        # find pivot-lows in this window
        pivs = []
        for j in range(lo, i + 1):
            v = pv[j]
            if not np.isnan(v):
                pivs.append((j, v))
        if not pivs:
            out[i] = 0.0
            continue
        max_close_after = -np.inf
        # for each pivot, check whether any subsequent close in window broke it
        broken = 0
        for (j, v) in pivs:
            broken_flag = False
            for k in range(j + 1, i + 1):
                cv = cl[k]
                if not np.isnan(cv) and cv < v:
                    broken_flag = True
                    break
            if broken_flag:
                broken += 1
        out[i] = float(broken)
    return pd.Series(out, index=low.index)


def f07_lhll_084_pivot_low_break_max_severity_atr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ATR-normalized severity of pivot10-low break observed in trailing 252d."""
    sev = f07_lhll_080_pivot_low_break_severity_atr_pivot10(high, low, close)
    return sev.rolling(YDAYS, min_periods=MDAYS).max()


# ============================================================
# Bucket M — Dow-theory composites (085-093)
# ============================================================

def f07_lhll_085_dow_state_score_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Score in [-2, +2]: +1 if most-recent pivot10-high made HH (else -1), +1 if
    most-recent pivot10-low made HL (else -1). Sum: +2 healthy uptrend, -2 broken."""
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    prev_h = pvh.shift(1).ffill()
    cur_h = pvh.ffill()
    prev_l = pvl.shift(1).ffill()
    cur_l = pvl.ffill()
    h_score = np.where(cur_h > prev_h, 1.0, -1.0)
    l_score = np.where(cur_l > prev_l, 1.0, -1.0)
    out = pd.Series(h_score + l_score, index=high.index)
    valid = cur_h.notna() & prev_h.notna() & cur_l.notna() & prev_l.notna()
    return out.where(valid, np.nan)


def f07_lhll_086_dow_state_score_negative_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars with Dow state score < 0 (degraded uptrend)."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low).values
    n = len(base)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        v = base[i]
        if np.isnan(v):
            out[i] = np.nan
        else:
            streak = streak + 1 if v < 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)


def f07_lhll_087_dow_state_score_mean_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean Dow state score over trailing 252d — regime-strength metric."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    return base.rolling(YDAYS, min_periods=QDAYS).mean()


def f07_lhll_088_dow_uptrend_to_downtrend_transition_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when Dow state score = -2 today AND was = +2 within the last 63 bars
    (rapid trend reversal)."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    was_pos = (base.shift(1).rolling(QDAYS, min_periods=2).max() >= 2.0)
    is_neg = (base <= -2.0)
    return (was_pos & is_neg).astype(float).where(base.notna(), np.nan)


def f07_lhll_089_hh_to_ll_transition_count_pivot10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of HH-then-LL transitions: at each bar count whether the prior pivot
    event-pair (one high, one low) showed HH then the next pair showed LL,
    summed over trailing 252d."""
    # Implementation: walk pivots; mark each LL whose nearest preceding HH was strict.
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    n = len(pvh)
    out_evt = np.zeros(n, dtype=float)
    prev_h = np.nan
    prev_l = np.nan
    last_was_hh = False
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if not np.isnan(prev_h):
                last_was_hh = vh > prev_h
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l) and vl < prev_l and last_was_hh:
                out_evt[i] = 1.0
                last_was_hh = False
            prev_l = vl
    out_evt_s = pd.Series(out_evt, index=high.index)
    return out_evt_s.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_090_dow_breakdown_after_long_uptrend_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when current bar has Dow score = -2 AND the trailing-504d mean of Dow score was > +1
    (breakdown out of a sustained healthy uptrend)."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    long_mean = base.shift(1).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return ((base <= -2.0) & (long_mean > 1.0)).astype(float).where(long_mean.notna(), np.nan)


def f07_lhll_091_dow_state_zero_crossings_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of zero-crossings of the Dow state score in trailing 252d
    (regime indecision)."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    sgn = np.sign(base)
    crosses = (sgn != sgn.shift(1)).astype(float)
    return crosses.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_092_dow_state_minimum_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Minimum Dow state score in trailing 252d — worst regime state hit."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    return base.rolling(YDAYS, min_periods=QDAYS).min()


def f07_lhll_093_dow_state_slope_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of the Dow state score over 504d — directional regime change."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    return _rolling_slope(base, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket N — Swing fan / channel breakdown (094-100)
# ============================================================

def f07_lhll_094_pivot_low_channel_break_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when close is below the linear-extrapolated channel of pivot10-lows
    (fitted over the trailing 252d window). Encodes 'fan-line break'."""
    pv = _pivot_low_value(low, 10).ffill()
    # rolling-slope and rolling-mean give us y = m*x + b at the window's centroid.
    sl = _rolling_slope(pv, YDAYS, min_periods=QDAYS)
    mean_pv = pv.rolling(YDAYS, min_periods=QDAYS).mean()
    # at the last bar of the window, x - xmean = (n - 1)/2
    offset = (YDAYS - 1) / 2.0
    line = mean_pv + sl * offset
    return (close < line).astype(float).where(line.notna() & close.notna(), np.nan)


def f07_lhll_095_pivot_high_channel_extension_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - fitted pivot10-high line) / ATR21. Negative = close has fallen below
    the resistance channel line drawn by pivot-highs (channel-collapse)."""
    pv = _pivot_high_value(high, 10).ffill()
    sl = _rolling_slope(pv, YDAYS, min_periods=QDAYS)
    mean_pv = pv.rolling(YDAYS, min_periods=QDAYS).mean()
    offset = (YDAYS - 1) / 2.0
    line = mean_pv + sl * offset
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - line, atr)


def f07_lhll_096_pivot_low_channel_break_count_504d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of pivot10-low channel breakdown events (0->1 transitions of f094) in 504d."""
    ind = f07_lhll_094_pivot_low_channel_break_indicator(low, close)
    evt = ((ind > 0.5) & (ind.shift(1) < 0.5)).astype(float)
    return evt.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_097_pivot_channel_widening_at_top_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when pivot-high channel slope > 0 (still rising) BUT pivot-low channel slope < 0
    (already falling) over 252d — broadening top / channel widening."""
    sh = _rolling_slope(_pivot_high_value(high, 10).ffill(), YDAYS, min_periods=QDAYS)
    sl = _rolling_slope(_pivot_low_value(low, 10).ffill(), YDAYS, min_periods=QDAYS)
    return ((sh > 0) & (sl < 0)).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f07_lhll_098_swing_fan_break_severity_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized severity of swing-low channel break: (line - close) / ATR21 when broken."""
    pv = _pivot_low_value(low, 10).ffill()
    sl = _rolling_slope(pv, YDAYS, min_periods=QDAYS)
    mean_pv = pv.rolling(YDAYS, min_periods=QDAYS).mean()
    offset = (YDAYS - 1) / 2.0
    line = mean_pv + sl * offset
    atr = _atr(high, low, close, n=MDAYS)
    sev = _safe_div(line - close, atr)
    return sev.where(close < line, np.nan)


def f07_lhll_099_pivot_channel_width_log_change_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log-change of channel width (mean pivot10-high minus mean pivot10-low over 63d)
    today vs 252d ago. Positive = widening / broadening top."""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    width = pvh.rolling(QDAYS, min_periods=MDAYS).mean() - pvl.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_log(width) - _safe_log(width.shift(YDAYS))


def f07_lhll_100_pivot_channel_inversion_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when most-recent pivot10-low > most-recent pivot10-high (degenerate / inverted
    swing structure suggesting chaotic regime). Else 0."""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    return (pvl > pvh).astype(float).where(pvh.notna() & pvl.notna(), np.nan)


# ============================================================
# Bucket O — Fractal patterns (Bill Williams 5-bar) (101-108)
# ============================================================

def _bw_fractal_up(high: pd.Series) -> pd.Series:
    """Bill Williams 5-bar bullish-fractal: high[t-2] is the max of {t-4..t}, confirmed at t."""
    rmax = high.rolling(5, min_periods=5).max()
    return (high.shift(2) == rmax) & rmax.notna()


def _bw_fractal_down(low: pd.Series) -> pd.Series:
    """Bill Williams 5-bar bearish-fractal: low[t-2] is the min of {t-4..t}, confirmed at t."""
    rmin = low.rolling(5, min_periods=5).min()
    return (low.shift(2) == rmin) & rmin.notna()


def f07_lhll_101_bw_up_fractal_count_252d(high: pd.Series) -> pd.Series:
    """Count of Bill-Williams 5-bar up-fractals (potential resistance pivots) in 252d."""
    fr = _bw_fractal_up(high).astype(float)
    return fr.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_102_bw_down_fractal_count_252d(low: pd.Series) -> pd.Series:
    """Count of Bill-Williams 5-bar down-fractals (potential support pivots) in 252d."""
    fr = _bw_fractal_down(low).astype(float)
    return fr.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_103_bw_down_to_up_fractal_ratio_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Down-fractals / up-fractals in trailing 252d. > 1 = more support-test events than
    resistance-test events (consistent with distribution / topping)."""
    up_cnt = f07_lhll_101_bw_up_fractal_count_252d(high)
    dn_cnt = f07_lhll_102_bw_down_fractal_count_252d(low)
    return _safe_div(dn_cnt, up_cnt)


def f07_lhll_104_bw_lower_up_fractal_count_252d(high: pd.Series) -> pd.Series:
    """Count of bullish 5-bar fractals whose pivot value is LOWER than the prior bullish
    fractal's value (LH cadence at the fractal scale) in 252d."""
    fr = _bw_fractal_up(high)
    val = high.shift(2).where(fr, np.nan)
    prev = val.shift(1).ffill()
    is_lower = ((val.notna()) & (prev.notna()) & (val < prev)).astype(float)
    return is_lower.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_105_bw_lower_down_fractal_count_252d(low: pd.Series) -> pd.Series:
    """Count of bearish 5-bar fractals whose pivot value is LOWER than prior bearish
    fractal value (LL cadence at the fractal scale) in 252d."""
    fr = _bw_fractal_down(low)
    val = low.shift(2).where(fr, np.nan)
    prev = val.shift(1).ffill()
    is_lower = ((val.notna()) & (prev.notna()) & (val < prev)).astype(float)
    return is_lower.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_106_bw_fractal_lh_minus_hh_count_252d(high: pd.Series) -> pd.Series:
    """(lower-fractal-highs) - (higher-fractal-highs) in trailing 252d. > 0 = net LH cadence."""
    fr = _bw_fractal_up(high)
    val = high.shift(2).where(fr, np.nan)
    prev = val.shift(1).ffill()
    lh = ((val.notna()) & (prev.notna()) & (val < prev)).astype(float)
    hh = ((val.notna()) & (prev.notna()) & (val > prev)).astype(float)
    return (lh - hh).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_107_bw_fractal_ll_minus_hl_count_252d(low: pd.Series) -> pd.Series:
    """(lower-fractal-lows) - (higher-fractal-lows) in trailing 252d. > 0 = net LL cadence."""
    fr = _bw_fractal_down(low)
    val = low.shift(2).where(fr, np.nan)
    prev = val.shift(1).ffill()
    ll = ((val.notna()) & (prev.notna()) & (val < prev)).astype(float)
    hl = ((val.notna()) & (prev.notna()) & (val > prev)).astype(float)
    return (ll - hl).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_108_bw_fractal_slope_high_252d(high: pd.Series) -> pd.Series:
    """Slope of the forward-filled bullish-fractal-value series in 252d
    — fractal-scale resistance trajectory."""
    fr = _bw_fractal_up(high)
    val = high.shift(2).where(fr, np.nan).ffill()
    return _rolling_slope(val, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket P — New-N-day-high vs new-N-day-low race (109-117)
# ============================================================

def f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(count new-21d-highs - count new-21d-lows) in trailing 63d. < 0 = lows dominating."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    nh = (high >= rh).astype(float)
    nl = (low <= rl).astype(float)
    return (nh - nl).rolling(QDAYS, min_periods=MDAYS).sum()


def f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Net new-63d-high vs new-63d-low count in trailing 252d (medium-horizon)."""
    rh = high.rolling(QDAYS, min_periods=MDAYS).max()
    rl = low.rolling(QDAYS, min_periods=MDAYS).min()
    nh = (high >= rh).astype(float)
    nl = (low <= rl).astype(float)
    return (nh - nl).rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_111_new_252d_high_minus_new_252d_low_count_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Long-horizon: net new-252d-high vs new-252d-low count in trailing 504d."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    nh = (high >= rh).astype(float)
    nl = (low <= rl).astype(float)
    return (nh - nl).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_112_new_low_dominance_indicator_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when in the trailing 63d more 21d-lows were printed than 21d-highs (regime flip)."""
    diff = f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d(high, low)
    return (diff < 0).astype(float).where(diff.notna(), np.nan)


def f07_lhll_113_new_low_dominance_indicator_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when in the trailing 252d more 63d-lows than 63d-highs (medium-term regime flip)."""
    diff = f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d(high, low)
    return (diff < 0).astype(float).where(diff.notna(), np.nan)


def f07_lhll_114_high_low_race_sign_change_to_negative_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when the high-low-race count over 63d crosses from >= 0 to < 0 today
    (fresh regime flip event)."""
    diff = f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d(high, low)
    return ((diff < 0) & (diff.shift(1) >= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f07_lhll_115_bars_since_high_low_race_went_negative_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the high-low race (63d window of 21d events) last turned negative
    (i.e., bars since regime flipped from highs-dominant to lows-dominant)."""
    diff = f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d(high, low).values
    n = len(diff)
    out = np.full(n, np.nan, dtype=float)
    last_flip_idx = -1
    prev_sign = np.nan
    for i in range(n):
        v = diff[i]
        if not np.isnan(v):
            cur_sign = 1.0 if v >= 0 else -1.0
            if not np.isnan(prev_sign) and prev_sign > 0 and cur_sign < 0:
                last_flip_idx = i
            prev_sign = cur_sign
        if last_flip_idx >= 0:
            out[i] = float(i - last_flip_idx)
    return pd.Series(out, index=high.index)


def f07_lhll_116_high_low_race_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252d z-score of the daily (new-21d-high minus new-21d-low) signal — anomalous bias."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    nh = (high >= rh).astype(float)
    nl = (low <= rl).astype(float)
    daily_diff = nh - nl
    return _rolling_zscore(daily_diff, YDAYS, min_periods=QDAYS)


def f07_lhll_117_cum_new_252d_lows_minus_252d_highs_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative (new 252d-lows minus new 252d-highs) in trailing 504d
    — long-horizon directional bias of yearly extremes."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    nh = (high >= rh).astype(float)
    nl = (low <= rl).astype(float)
    return (nl - nh).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


# ============================================================
# Bucket Q — Cross-horizon HH/LL transitions & regime change (118-126)
# ============================================================

def f07_lhll_118_pivot10_high_below_running_max_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance: (expanding pivot10-high max - current pivot10-high) / ATR21
    — how far the most recent peak sits below the all-time pivot peak."""
    pv = _pivot_high_value(high, 10)
    running_max = pv.expanding(min_periods=1).max()
    cur = pv.ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(running_max - cur, atr)


def f07_lhll_119_pivot10_high_below_running_max_log(high: pd.Series) -> pd.Series:
    """Log shortfall: log(expanding max pivot10-high) - log(current pivot10-high)."""
    pv = _pivot_high_value(high, 10)
    running_max = pv.expanding(min_periods=1).max()
    cur = pv.ffill()
    return _safe_log(running_max) - _safe_log(cur)


def f07_lhll_120_consecutive_lower_pivot10_highs_since_alltime(high: pd.Series) -> pd.Series:
    """Number of pivot10-highs since the all-time pivot10-high that have been lower."""
    pv = _pivot_high_value(high, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    pivots_since = 0
    last_val = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if v > cur_max:
                cur_max = v
                cur_max_idx = i
                pivots_since = 0
            else:
                pivots_since += 1
            last_val = float(pivots_since)
        out[i] = last_val
    return pd.Series(out, index=high.index)


def f07_lhll_121_bars_since_alltime_pivot10_high(high: pd.Series) -> pd.Series:
    """Bars since the highest confirmed pivot10-high in history (PIT-clean)."""
    pv = _pivot_high_value(high, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = pv[i]
        if not np.isnan(v) and v >= cur_max:
            cur_max = v
            cur_max_idx = i
        if cur_max_idx >= 0:
            out[i] = float(i - cur_max_idx)
    return pd.Series(out, index=high.index)


def f07_lhll_122_lh_to_total_pivots_ratio_504d(high: pd.Series) -> pd.Series:
    """Ratio of lower-high pivot10 events to TOTAL pivot10 events in trailing 504d
    — long-horizon proportion measure."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = pv.notna().astype(float)
    return _safe_div(is_lh.rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
                     is_evt.rolling(DDAYS_2Y, min_periods=YDAYS).sum())


def f07_lhll_123_ll_to_total_pivots_ratio_504d(low: pd.Series) -> pd.Series:
    """Ratio of lower-low pivot10 events to total pivot10 events in trailing 504d."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = pv.notna().astype(float)
    return _safe_div(is_ll.rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
                     is_evt.rolling(DDAYS_2Y, min_periods=YDAYS).sum())


def f07_lhll_124_combined_lh_ll_ratio_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of f122 + f123 — combined LH/LL proportion (Dow-theory decay metric)."""
    a = f07_lhll_122_lh_to_total_pivots_ratio_504d(high)
    b = f07_lhll_123_ll_to_total_pivots_ratio_504d(low)
    return (a + b) / 2.0


def f07_lhll_125_pivot10_high_makes_new_252d_low_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when the most-recent pivot10-low value itself is a new 252d low
    (i.e., the lower-low broke below the 252d support floor — long-horizon
    Dow-breakdown confirmation)."""
    pv = _pivot_low_value(low, 10).ffill()
    running_min_252d = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (pv <= running_min_252d).astype(float).where(pv.notna() & running_min_252d.notna(), np.nan)


def f07_lhll_126_recent_pivot10_high_below_252d_max_indicator(high: pd.Series) -> pd.Series:
    """1 when the most-recent pivot10-high is below the trailing 252d high
    (peak failed to make a new 252d high — distribution signal)."""
    pv = _pivot_high_value(high, 10).ffill()
    running_max_252d = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (pv < running_max_252d).astype(float).where(pv.notna() & running_max_252d.notna(), np.nan)


# ============================================================
# Bucket R — Additional Dow / structural metrics (127-150)
# ============================================================

def f07_lhll_127_swing_count_ratio_down_vs_up_pivot10_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Down-swing count / up-swing count over 504d (pivot10).
    A down-swing = pivot-low strictly lower than previous pivot-low (LL).
    > 1 = down-swings outnumber up-swings."""
    pvl = _pivot_low_value(low, 10)
    prev_l = pvl.shift(1).ffill()
    dn = ((pvl.notna()) & (prev_l.notna()) & (pvl < prev_l)).astype(float)
    up = ((pvl.notna()) & (prev_l.notna()) & (pvl > prev_l)).astype(float)
    return _safe_div(dn.rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
                     up.rolling(DDAYS_2Y, min_periods=YDAYS).sum())


def f07_lhll_128_pivot10_swing_amplitude_decay_log_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log-change of mean swing amplitude (high-low value pairs) today vs 252d ago
    — distinct from family 10's raw decay: here uses *paired* pivot amplitudes."""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    amp = (pvh - pvl).abs()
    cur = amp.rolling(QDAYS, min_periods=MDAYS).mean()
    prior = cur.shift(YDAYS)
    return _safe_log(cur) - _safe_log(prior)


def f07_lhll_129_pivot10_average_log_return_per_swing_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Average log return per pivot10 swing-leg in trailing 252d.
    Negative = legs on average lose ground (degraded uptrend)."""
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    # Combine into a single "pivot value" series (whichever was last)
    combined = pvh.combine_first(pvl)
    log_ret = (_safe_log(combined.ffill()) - _safe_log(combined.ffill().shift(1)))
    only_at_pivot = log_ret.where(combined.notna(), np.nan)
    return only_at_pivot.rolling(YDAYS, min_periods=MDAYS).mean()


def f07_lhll_130_pivot10_signed_swing_return_sum_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of signed log-returns between consecutive pivot10 events in trailing 252d.
    Negative cumulative = net downward swing trajectory."""
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    combined = pvh.combine_first(pvl).ffill()
    log_ret = _safe_log(combined) - _safe_log(combined.shift(1))
    only_at_pivot = log_ret.where(pvh.combine_first(pvl).notna(), np.nan)
    return only_at_pivot.rolling(YDAYS, min_periods=MDAYS).sum()


def f07_lhll_131_pivot10_low_below_prev_two_indicator(low: pd.Series) -> pd.Series:
    """1 when current pivot10-low < previous TWO pivot10-lows (deeper-than-deep LL)."""
    pv = _pivot_low_value(low, 10)
    p1 = pv.shift(1).ffill()
    p2 = pv.shift(2).ffill()
    # We need previous two pivot values, not previous two bars - so we use the pivot-value
    # series compressed: walk and track.
    pv_arr = pv.values
    n = len(pv_arr)
    out = np.full(n, np.nan, dtype=float)
    stack = []  # most recent pivot values
    last_state = np.nan
    for i in range(n):
        v = pv_arr[i]
        if not np.isnan(v):
            if len(stack) >= 2:
                if v < stack[-1] and v < stack[-2]:
                    last_state = 1.0
                else:
                    last_state = 0.0
            stack.append(v)
        out[i] = last_state
    return pd.Series(out, index=low.index)


def f07_lhll_132_pivot10_high_below_prev_two_indicator(high: pd.Series) -> pd.Series:
    """1 when current pivot10-high < previous TWO pivot10-highs (deeper-than-deep LH)."""
    pv_arr = _pivot_high_value(high, 10).values
    n = len(pv_arr)
    out = np.full(n, np.nan, dtype=float)
    stack = []
    last_state = np.nan
    for i in range(n):
        v = pv_arr[i]
        if not np.isnan(v):
            if len(stack) >= 2:
                if v < stack[-1] and v < stack[-2]:
                    last_state = 1.0
                else:
                    last_state = 0.0
            stack.append(v)
        out[i] = last_state
    return pd.Series(out, index=high.index)


def f07_lhll_133_three_consecutive_lower_pivot10_highs_indicator(high: pd.Series) -> pd.Series:
    """1 when the last THREE pivot10-highs are strictly monotonically descending."""
    pv_arr = _pivot_high_value(high, 10).values
    n = len(pv_arr)
    out = np.full(n, np.nan, dtype=float)
    stack = []
    last_state = np.nan
    for i in range(n):
        v = pv_arr[i]
        if not np.isnan(v):
            stack.append(v)
            if len(stack) >= 3:
                a, b, c = stack[-3], stack[-2], stack[-1]
                last_state = 1.0 if (a > b and b > c) else 0.0
        out[i] = last_state
    return pd.Series(out, index=high.index)


def f07_lhll_134_three_consecutive_lower_pivot10_lows_indicator(low: pd.Series) -> pd.Series:
    """1 when the last THREE pivot10-lows are strictly monotonically descending."""
    pv_arr = _pivot_low_value(low, 10).values
    n = len(pv_arr)
    out = np.full(n, np.nan, dtype=float)
    stack = []
    last_state = np.nan
    for i in range(n):
        v = pv_arr[i]
        if not np.isnan(v):
            stack.append(v)
            if len(stack) >= 3:
                a, b, c = stack[-3], stack[-2], stack[-1]
                last_state = 1.0 if (a > b and b > c) else 0.0
        out[i] = last_state
    return pd.Series(out, index=low.index)


def f07_lhll_135_pivot10_low_below_252d_low_indicator(low: pd.Series) -> pd.Series:
    """1 when the most-recent pivot10-low is below the trailing 252d low
    (note: this is the pivot's own value being a fresh annual low, not whether
    today's low broke it — distinct from f125)."""
    pv = _pivot_low_value(low, 10)
    running_min_252d = low.shift(11).rolling(YDAYS - 10, min_periods=QDAYS).min()
    fresh_low = ((pv.notna()) & (pv < running_min_252d)).astype(float)
    return fresh_low.ffill()


def f07_lhll_136_pivot10_high_log_distance_to_alltime(high: pd.Series) -> pd.Series:
    """log(all-time-pivot10-high) - log(current close-proxy=high). Forward-filled.
    Distinct from f119 which uses the pivot value — here we measure HOW FAR price
    today sits below the all-time pivot peak."""
    pv = _pivot_high_value(high, 10)
    running_max = pv.expanding(min_periods=1).max()
    return _safe_log(running_max) - _safe_log(high)


def f07_lhll_137_pivot_high_max_streak_lh_in_504d(high: pd.Series) -> pd.Series:
    """Longest LH streak among pivot10-highs within trailing 504d (long-horizon variant of f005)."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_hh = ((pv.notna()) & (prev.notna()) & (pv >= prev)).astype(float)
    mark = is_lh - is_hh
    def _longest(w):
        best = 0
        cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            elif v < -0.5:
                cur = 0
        return float(best) if not np.isnan(w).all() else np.nan
    return mark.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_longest, raw=True)


def f07_lhll_138_pivot_low_max_streak_ll_in_504d(low: pd.Series) -> pd.Series:
    """Longest LL streak among pivot10-lows within trailing 504d."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_hl = ((pv.notna()) & (prev.notna()) & (pv >= prev)).astype(float)
    mark = is_ll - is_hl
    def _longest(w):
        best = 0
        cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            elif v < -0.5:
                cur = 0
        return float(best) if not np.isnan(w).all() else np.nan
    return mark.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_longest, raw=True)


def f07_lhll_139_pivot10_low_below_2y_low_indicator(low: pd.Series) -> pd.Series:
    """1 when the most-recent pivot10-low IS the trailing 504d low — fresh 2y support break."""
    pv = _pivot_low_value(low, 10).ffill()
    running_min_2y = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (pv <= running_min_2y).astype(float).where(pv.notna() & running_min_2y.notna(), np.nan)


def f07_lhll_140_pivot10_low_below_5y_low_indicator(low: pd.Series) -> pd.Series:
    """1 when most-recent pivot10-low is the trailing 1260d low — fresh 5y support break."""
    pv = _pivot_low_value(low, 10).ffill()
    running_min_5y = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return (pv <= running_min_5y).astype(float).where(pv.notna() & running_min_5y.notna(), np.nan)


def f07_lhll_141_dow_score_negative_fraction_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where Dow state score < 0 — proportion of time in
    degraded regime."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    neg = (base < 0).astype(float).where(base.notna(), np.nan)
    return neg.rolling(YDAYS, min_periods=QDAYS).mean()


def f07_lhll_142_dow_score_minus_two_fraction_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 504d bars where Dow state score == -2 (fully degraded)."""
    base = f07_lhll_085_dow_state_score_pivot10(high, low)
    full_neg = (base <= -2.0).astype(float).where(base.notna(), np.nan)
    return full_neg.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f07_lhll_143_pivot10_high_count_in_top_decile_of_pv_dist_252d(high: pd.Series) -> pd.Series:
    """Count of pivot10-highs in trailing 252d whose value lies in the top decile
    of the trailing-504d distribution of close. Low count at top = few near-peak pivots."""
    pv = _pivot_high_value(high, 10)
    thresh = high.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    in_top = (pv >= thresh).astype(float).where(pv.notna() & thresh.notna(), 0.0)
    return in_top.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_144_pivot10_low_count_in_bottom_decile_of_pv_dist_252d(low: pd.Series) -> pd.Series:
    """Count of pivot10-lows in trailing 252d whose value lies in the bottom decile
    of the trailing 504d low distribution (low-floor degradation)."""
    pv = _pivot_low_value(low, 10)
    thresh = low.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.1)
    in_bot = (pv <= thresh).astype(float).where(pv.notna() & thresh.notna(), 0.0)
    return in_bot.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_145_pivot10_swing_signed_drift_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum over trailing 252d of (last_pivot_low - prev_pivot_low) signed differences
    — cumulative low-pivot drift; negative = falling support floor."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    diff = (pv - prev).where(pv.notna() & prev.notna(), np.nan)
    return diff.rolling(YDAYS, min_periods=MDAYS).sum()


def f07_lhll_146_pivot10_high_signed_drift_252d(high: pd.Series) -> pd.Series:
    """Sum over trailing 252d of (last_pivot_high - prev_pivot_high) signed differences
    — cumulative high-pivot drift; negative = falling resistance ceiling."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    diff = (pv - prev).where(pv.notna() & prev.notna(), np.nan)
    return diff.rolling(YDAYS, min_periods=MDAYS).sum()


def f07_lhll_147_pivot_combined_drift_zscore_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """504d z-score of (high signed drift + low signed drift) — anomalous combined drift."""
    a = f07_lhll_146_pivot10_high_signed_drift_252d(high)
    b = f07_lhll_145_pivot10_swing_signed_drift_252d(high, low)
    combined = a + b
    return _rolling_zscore(combined, DDAYS_2Y, min_periods=YDAYS)


def f07_lhll_148_max_log_lower_high_gap_in_252d(high: pd.Series) -> pd.Series:
    """Max log shortfall (prev pivot-high minus current pivot-high) among LH events
    in trailing 252d — worst single LH event in the year."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    short = (_safe_log(prev) - _safe_log(pv)).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    return short.rolling(YDAYS, min_periods=MDAYS).max()


def f07_lhll_149_max_log_lower_low_gap_in_252d(low: pd.Series) -> pd.Series:
    """Max log shortfall (prev pivot-low minus current pivot-low) among LL events
    in trailing 252d — worst single LL event in the year."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    short = (_safe_log(prev) - _safe_log(pv)).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    return short.rolling(YDAYS, min_periods=MDAYS).max()


def f07_lhll_150_dow_breakdown_pivot10_with_close_confirm_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when a Dow-breakdown (LL after HH at pivot10) occurred in the last 21 bars
    AND today's close < the most-recent pivot10-low (close-confirmed breakdown).
    Stronger composite distribution signal."""
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    n = len(pvh)
    break_evt = np.zeros(n, dtype=float)
    last_hh_idx = -1
    prev_h = np.nan
    prev_l = np.nan
    most_recent_ll_after_hh_idx = -1
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if not np.isnan(prev_h) and vh > prev_h:
                last_hh_idx = i
                most_recent_ll_after_hh_idx = -1
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l) and vl < prev_l and last_hh_idx >= 0 and i > last_hh_idx:
                if i != most_recent_ll_after_hh_idx:
                    break_evt[i] = 1.0
                    most_recent_ll_after_hh_idx = i
            prev_l = vl
    break_s = pd.Series(break_evt, index=high.index)
    break_recent = break_s.rolling(MDAYS, min_periods=1).sum() > 0
    pv_low_recent = _pivot_low_value(low, 10).ffill()
    close_below = close < pv_low_recent
    return (break_recent & close_below).astype(float).where(pv_low_recent.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f07_lhll_076_close_below_recent_pivot10_low_indicator_d2(low, close):
    return f07_lhll_076_close_below_recent_pivot10_low_indicator(low, close).diff().diff()


def f07_lhll_077_close_below_recent_pivot21_low_indicator_d2(low, close):
    return f07_lhll_077_close_below_recent_pivot21_low_indicator(low, close).diff().diff()


def f07_lhll_078_pivot_low_break_event_count_pivot10_252d_d2(low, close):
    return f07_lhll_078_pivot_low_break_event_count_pivot10_252d(low, close).diff().diff()


def f07_lhll_079_pivot_low_break_event_count_pivot21_504d_d2(low, close):
    return f07_lhll_079_pivot_low_break_event_count_pivot21_504d(low, close).diff().diff()


def f07_lhll_080_pivot_low_break_severity_atr_pivot10_d2(high, low, close):
    return f07_lhll_080_pivot_low_break_severity_atr_pivot10(high, low, close).diff().diff()


def f07_lhll_081_pivot_low_break_severity_log_pivot10_d2(low, close):
    return f07_lhll_081_pivot_low_break_severity_log_pivot10(low, close).diff().diff()


def f07_lhll_082_bars_below_pivot10_low_streak_d2(low, close):
    return f07_lhll_082_bars_below_pivot10_low_streak(low, close).diff().diff()


def f07_lhll_083_count_pivot10_lows_broken_in_504d_d2(low, close):
    return f07_lhll_083_count_pivot10_lows_broken_in_504d(low, close).diff().diff()


def f07_lhll_084_pivot_low_break_max_severity_atr_252d_d2(high, low, close):
    return f07_lhll_084_pivot_low_break_max_severity_atr_252d(high, low, close).diff().diff()


def f07_lhll_085_dow_state_score_pivot10_d2(high, low):
    return f07_lhll_085_dow_state_score_pivot10(high, low).diff().diff()


def f07_lhll_086_dow_state_score_negative_streak_d2(high, low):
    return f07_lhll_086_dow_state_score_negative_streak(high, low).diff().diff()


def f07_lhll_087_dow_state_score_mean_252d_d2(high, low):
    return f07_lhll_087_dow_state_score_mean_252d(high, low).diff().diff()


def f07_lhll_088_dow_uptrend_to_downtrend_transition_indicator_d2(high, low):
    return f07_lhll_088_dow_uptrend_to_downtrend_transition_indicator(high, low).diff().diff()


def f07_lhll_089_hh_to_ll_transition_count_pivot10_252d_d2(high, low):
    return f07_lhll_089_hh_to_ll_transition_count_pivot10_252d(high, low).diff().diff()


def f07_lhll_090_dow_breakdown_after_long_uptrend_indicator_d2(high, low):
    return f07_lhll_090_dow_breakdown_after_long_uptrend_indicator(high, low).diff().diff()


def f07_lhll_091_dow_state_zero_crossings_count_252d_d2(high, low):
    return f07_lhll_091_dow_state_zero_crossings_count_252d(high, low).diff().diff()


def f07_lhll_092_dow_state_minimum_252d_d2(high, low):
    return f07_lhll_092_dow_state_minimum_252d(high, low).diff().diff()


def f07_lhll_093_dow_state_slope_504d_d2(high, low):
    return f07_lhll_093_dow_state_slope_504d(high, low).diff().diff()


def f07_lhll_094_pivot_low_channel_break_indicator_d2(low, close):
    return f07_lhll_094_pivot_low_channel_break_indicator(low, close).diff().diff()


def f07_lhll_095_pivot_high_channel_extension_atr_d2(high, low, close):
    return f07_lhll_095_pivot_high_channel_extension_atr(high, low, close).diff().diff()


def f07_lhll_096_pivot_low_channel_break_count_504d_d2(low, close):
    return f07_lhll_096_pivot_low_channel_break_count_504d(low, close).diff().diff()


def f07_lhll_097_pivot_channel_widening_at_top_indicator_d2(high, low):
    return f07_lhll_097_pivot_channel_widening_at_top_indicator(high, low).diff().diff()


def f07_lhll_098_swing_fan_break_severity_atr_d2(high, low, close):
    return f07_lhll_098_swing_fan_break_severity_atr(high, low, close).diff().diff()


def f07_lhll_099_pivot_channel_width_log_change_252d_d2(high, low):
    return f07_lhll_099_pivot_channel_width_log_change_252d(high, low).diff().diff()


def f07_lhll_100_pivot_channel_inversion_indicator_d2(high, low):
    return f07_lhll_100_pivot_channel_inversion_indicator(high, low).diff().diff()


def f07_lhll_101_bw_up_fractal_count_252d_d2(high):
    return f07_lhll_101_bw_up_fractal_count_252d(high).diff().diff()


def f07_lhll_102_bw_down_fractal_count_252d_d2(low):
    return f07_lhll_102_bw_down_fractal_count_252d(low).diff().diff()


def f07_lhll_103_bw_down_to_up_fractal_ratio_252d_d2(high, low):
    return f07_lhll_103_bw_down_to_up_fractal_ratio_252d(high, low).diff().diff()


def f07_lhll_104_bw_lower_up_fractal_count_252d_d2(high):
    return f07_lhll_104_bw_lower_up_fractal_count_252d(high).diff().diff()


def f07_lhll_105_bw_lower_down_fractal_count_252d_d2(low):
    return f07_lhll_105_bw_lower_down_fractal_count_252d(low).diff().diff()


def f07_lhll_106_bw_fractal_lh_minus_hh_count_252d_d2(high):
    return f07_lhll_106_bw_fractal_lh_minus_hh_count_252d(high).diff().diff()


def f07_lhll_107_bw_fractal_ll_minus_hl_count_252d_d2(low):
    return f07_lhll_107_bw_fractal_ll_minus_hl_count_252d(low).diff().diff()


def f07_lhll_108_bw_fractal_slope_high_252d_d2(high):
    return f07_lhll_108_bw_fractal_slope_high_252d(high).diff().diff()


def f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d_d2(high, low):
    return f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d(high, low).diff().diff()


def f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d_d2(high, low):
    return f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d(high, low).diff().diff()


def f07_lhll_111_new_252d_high_minus_new_252d_low_count_504d_d2(high, low):
    return f07_lhll_111_new_252d_high_minus_new_252d_low_count_504d(high, low).diff().diff()


def f07_lhll_112_new_low_dominance_indicator_63d_d2(high, low):
    return f07_lhll_112_new_low_dominance_indicator_63d(high, low).diff().diff()


def f07_lhll_113_new_low_dominance_indicator_252d_d2(high, low):
    return f07_lhll_113_new_low_dominance_indicator_252d(high, low).diff().diff()


def f07_lhll_114_high_low_race_sign_change_to_negative_indicator_d2(high, low):
    return f07_lhll_114_high_low_race_sign_change_to_negative_indicator(high, low).diff().diff()


def f07_lhll_115_bars_since_high_low_race_went_negative_63d_d2(high, low):
    return f07_lhll_115_bars_since_high_low_race_went_negative_63d(high, low).diff().diff()


def f07_lhll_116_high_low_race_zscore_252d_d2(high, low):
    return f07_lhll_116_high_low_race_zscore_252d(high, low).diff().diff()


def f07_lhll_117_cum_new_252d_lows_minus_252d_highs_504d_d2(high, low):
    return f07_lhll_117_cum_new_252d_lows_minus_252d_highs_504d(high, low).diff().diff()


def f07_lhll_118_pivot10_high_below_running_max_atr_d2(high, low, close):
    return f07_lhll_118_pivot10_high_below_running_max_atr(high, low, close).diff().diff()


def f07_lhll_119_pivot10_high_below_running_max_log_d2(high):
    return f07_lhll_119_pivot10_high_below_running_max_log(high).diff().diff()


def f07_lhll_120_consecutive_lower_pivot10_highs_since_alltime_d2(high):
    return f07_lhll_120_consecutive_lower_pivot10_highs_since_alltime(high).diff().diff()


def f07_lhll_121_bars_since_alltime_pivot10_high_d2(high):
    return f07_lhll_121_bars_since_alltime_pivot10_high(high).diff().diff()


def f07_lhll_122_lh_to_total_pivots_ratio_504d_d2(high):
    return f07_lhll_122_lh_to_total_pivots_ratio_504d(high).diff().diff()


def f07_lhll_123_ll_to_total_pivots_ratio_504d_d2(low):
    return f07_lhll_123_ll_to_total_pivots_ratio_504d(low).diff().diff()


def f07_lhll_124_combined_lh_ll_ratio_504d_d2(high, low):
    return f07_lhll_124_combined_lh_ll_ratio_504d(high, low).diff().diff()


def f07_lhll_125_pivot10_high_makes_new_252d_low_indicator_d2(high, low):
    return f07_lhll_125_pivot10_high_makes_new_252d_low_indicator(high, low).diff().diff()


def f07_lhll_126_recent_pivot10_high_below_252d_max_indicator_d2(high):
    return f07_lhll_126_recent_pivot10_high_below_252d_max_indicator(high).diff().diff()


def f07_lhll_127_swing_count_ratio_down_vs_up_pivot10_504d_d2(high, low):
    return f07_lhll_127_swing_count_ratio_down_vs_up_pivot10_504d(high, low).diff().diff()


def f07_lhll_128_pivot10_swing_amplitude_decay_log_252d_d2(high, low):
    return f07_lhll_128_pivot10_swing_amplitude_decay_log_252d(high, low).diff().diff()


def f07_lhll_129_pivot10_average_log_return_per_swing_252d_d2(high, low):
    return f07_lhll_129_pivot10_average_log_return_per_swing_252d(high, low).diff().diff()


def f07_lhll_130_pivot10_signed_swing_return_sum_252d_d2(high, low):
    return f07_lhll_130_pivot10_signed_swing_return_sum_252d(high, low).diff().diff()


def f07_lhll_131_pivot10_low_below_prev_two_indicator_d2(low):
    return f07_lhll_131_pivot10_low_below_prev_two_indicator(low).diff().diff()


def f07_lhll_132_pivot10_high_below_prev_two_indicator_d2(high):
    return f07_lhll_132_pivot10_high_below_prev_two_indicator(high).diff().diff()


def f07_lhll_133_three_consecutive_lower_pivot10_highs_indicator_d2(high):
    return f07_lhll_133_three_consecutive_lower_pivot10_highs_indicator(high).diff().diff()


def f07_lhll_134_three_consecutive_lower_pivot10_lows_indicator_d2(low):
    return f07_lhll_134_three_consecutive_lower_pivot10_lows_indicator(low).diff().diff()


def f07_lhll_135_pivot10_low_below_252d_low_indicator_d2(low):
    return f07_lhll_135_pivot10_low_below_252d_low_indicator(low).diff().diff()


def f07_lhll_136_pivot10_high_log_distance_to_alltime_d2(high):
    return f07_lhll_136_pivot10_high_log_distance_to_alltime(high).diff().diff()


def f07_lhll_137_pivot_high_max_streak_lh_in_504d_d2(high):
    return f07_lhll_137_pivot_high_max_streak_lh_in_504d(high).diff().diff()


def f07_lhll_138_pivot_low_max_streak_ll_in_504d_d2(low):
    return f07_lhll_138_pivot_low_max_streak_ll_in_504d(low).diff().diff()


def f07_lhll_139_pivot10_low_below_2y_low_indicator_d2(low):
    return f07_lhll_139_pivot10_low_below_2y_low_indicator(low).diff().diff()


def f07_lhll_140_pivot10_low_below_5y_low_indicator_d2(low):
    return f07_lhll_140_pivot10_low_below_5y_low_indicator(low).diff().diff()


def f07_lhll_141_dow_score_negative_fraction_252d_d2(high, low):
    return f07_lhll_141_dow_score_negative_fraction_252d(high, low).diff().diff()


def f07_lhll_142_dow_score_minus_two_fraction_504d_d2(high, low):
    return f07_lhll_142_dow_score_minus_two_fraction_504d(high, low).diff().diff()


def f07_lhll_143_pivot10_high_count_in_top_decile_of_pv_dist_252d_d2(high):
    return f07_lhll_143_pivot10_high_count_in_top_decile_of_pv_dist_252d(high).diff().diff()


def f07_lhll_144_pivot10_low_count_in_bottom_decile_of_pv_dist_252d_d2(low):
    return f07_lhll_144_pivot10_low_count_in_bottom_decile_of_pv_dist_252d(low).diff().diff()


def f07_lhll_145_pivot10_swing_signed_drift_252d_d2(high, low):
    return f07_lhll_145_pivot10_swing_signed_drift_252d(high, low).diff().diff()


def f07_lhll_146_pivot10_high_signed_drift_252d_d2(high):
    return f07_lhll_146_pivot10_high_signed_drift_252d(high).diff().diff()


def f07_lhll_147_pivot_combined_drift_zscore_504d_d2(high, low):
    return f07_lhll_147_pivot_combined_drift_zscore_504d(high, low).diff().diff()


def f07_lhll_148_max_log_lower_high_gap_in_252d_d2(high):
    return f07_lhll_148_max_log_lower_high_gap_in_252d(high).diff().diff()


def f07_lhll_149_max_log_lower_low_gap_in_252d_d2(low):
    return f07_lhll_149_max_log_lower_low_gap_in_252d(low).diff().diff()


def f07_lhll_150_dow_breakdown_pivot10_with_close_confirm_indicator_d2(high, low, close):
    return f07_lhll_150_dow_breakdown_pivot10_with_close_confirm_indicator(high, low, close).diff().diff()


LOWER_HIGH_LOWER_LOW_STRUCTURE_D2_REGISTRY_076_150 = {
    "f07_lhll_076_close_below_recent_pivot10_low_indicator_d2": {"inputs": ["low", "close"], "func": f07_lhll_076_close_below_recent_pivot10_low_indicator_d2},
    "f07_lhll_077_close_below_recent_pivot21_low_indicator_d2": {"inputs": ["low", "close"], "func": f07_lhll_077_close_below_recent_pivot21_low_indicator_d2},
    "f07_lhll_078_pivot_low_break_event_count_pivot10_252d_d2": {"inputs": ["low", "close"], "func": f07_lhll_078_pivot_low_break_event_count_pivot10_252d_d2},
    "f07_lhll_079_pivot_low_break_event_count_pivot21_504d_d2": {"inputs": ["low", "close"], "func": f07_lhll_079_pivot_low_break_event_count_pivot21_504d_d2},
    "f07_lhll_080_pivot_low_break_severity_atr_pivot10_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_080_pivot_low_break_severity_atr_pivot10_d2},
    "f07_lhll_081_pivot_low_break_severity_log_pivot10_d2": {"inputs": ["low", "close"], "func": f07_lhll_081_pivot_low_break_severity_log_pivot10_d2},
    "f07_lhll_082_bars_below_pivot10_low_streak_d2": {"inputs": ["low", "close"], "func": f07_lhll_082_bars_below_pivot10_low_streak_d2},
    "f07_lhll_083_count_pivot10_lows_broken_in_504d_d2": {"inputs": ["low", "close"], "func": f07_lhll_083_count_pivot10_lows_broken_in_504d_d2},
    "f07_lhll_084_pivot_low_break_max_severity_atr_252d_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_084_pivot_low_break_max_severity_atr_252d_d2},
    "f07_lhll_085_dow_state_score_pivot10_d2": {"inputs": ["high", "low"], "func": f07_lhll_085_dow_state_score_pivot10_d2},
    "f07_lhll_086_dow_state_score_negative_streak_d2": {"inputs": ["high", "low"], "func": f07_lhll_086_dow_state_score_negative_streak_d2},
    "f07_lhll_087_dow_state_score_mean_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_087_dow_state_score_mean_252d_d2},
    "f07_lhll_088_dow_uptrend_to_downtrend_transition_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_088_dow_uptrend_to_downtrend_transition_indicator_d2},
    "f07_lhll_089_hh_to_ll_transition_count_pivot10_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_089_hh_to_ll_transition_count_pivot10_252d_d2},
    "f07_lhll_090_dow_breakdown_after_long_uptrend_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_090_dow_breakdown_after_long_uptrend_indicator_d2},
    "f07_lhll_091_dow_state_zero_crossings_count_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_091_dow_state_zero_crossings_count_252d_d2},
    "f07_lhll_092_dow_state_minimum_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_092_dow_state_minimum_252d_d2},
    "f07_lhll_093_dow_state_slope_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_093_dow_state_slope_504d_d2},
    "f07_lhll_094_pivot_low_channel_break_indicator_d2": {"inputs": ["low", "close"], "func": f07_lhll_094_pivot_low_channel_break_indicator_d2},
    "f07_lhll_095_pivot_high_channel_extension_atr_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_095_pivot_high_channel_extension_atr_d2},
    "f07_lhll_096_pivot_low_channel_break_count_504d_d2": {"inputs": ["low", "close"], "func": f07_lhll_096_pivot_low_channel_break_count_504d_d2},
    "f07_lhll_097_pivot_channel_widening_at_top_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_097_pivot_channel_widening_at_top_indicator_d2},
    "f07_lhll_098_swing_fan_break_severity_atr_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_098_swing_fan_break_severity_atr_d2},
    "f07_lhll_099_pivot_channel_width_log_change_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_099_pivot_channel_width_log_change_252d_d2},
    "f07_lhll_100_pivot_channel_inversion_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_100_pivot_channel_inversion_indicator_d2},
    "f07_lhll_101_bw_up_fractal_count_252d_d2": {"inputs": ["high"], "func": f07_lhll_101_bw_up_fractal_count_252d_d2},
    "f07_lhll_102_bw_down_fractal_count_252d_d2": {"inputs": ["low"], "func": f07_lhll_102_bw_down_fractal_count_252d_d2},
    "f07_lhll_103_bw_down_to_up_fractal_ratio_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_103_bw_down_to_up_fractal_ratio_252d_d2},
    "f07_lhll_104_bw_lower_up_fractal_count_252d_d2": {"inputs": ["high"], "func": f07_lhll_104_bw_lower_up_fractal_count_252d_d2},
    "f07_lhll_105_bw_lower_down_fractal_count_252d_d2": {"inputs": ["low"], "func": f07_lhll_105_bw_lower_down_fractal_count_252d_d2},
    "f07_lhll_106_bw_fractal_lh_minus_hh_count_252d_d2": {"inputs": ["high"], "func": f07_lhll_106_bw_fractal_lh_minus_hh_count_252d_d2},
    "f07_lhll_107_bw_fractal_ll_minus_hl_count_252d_d2": {"inputs": ["low"], "func": f07_lhll_107_bw_fractal_ll_minus_hl_count_252d_d2},
    "f07_lhll_108_bw_fractal_slope_high_252d_d2": {"inputs": ["high"], "func": f07_lhll_108_bw_fractal_slope_high_252d_d2},
    "f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d_d2": {"inputs": ["high", "low"], "func": f07_lhll_109_new_21d_high_minus_new_21d_low_count_63d_d2},
    "f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_110_new_63d_high_minus_new_63d_low_count_252d_d2},
    "f07_lhll_111_new_252d_high_minus_new_252d_low_count_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_111_new_252d_high_minus_new_252d_low_count_504d_d2},
    "f07_lhll_112_new_low_dominance_indicator_63d_d2": {"inputs": ["high", "low"], "func": f07_lhll_112_new_low_dominance_indicator_63d_d2},
    "f07_lhll_113_new_low_dominance_indicator_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_113_new_low_dominance_indicator_252d_d2},
    "f07_lhll_114_high_low_race_sign_change_to_negative_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_114_high_low_race_sign_change_to_negative_indicator_d2},
    "f07_lhll_115_bars_since_high_low_race_went_negative_63d_d2": {"inputs": ["high", "low"], "func": f07_lhll_115_bars_since_high_low_race_went_negative_63d_d2},
    "f07_lhll_116_high_low_race_zscore_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_116_high_low_race_zscore_252d_d2},
    "f07_lhll_117_cum_new_252d_lows_minus_252d_highs_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_117_cum_new_252d_lows_minus_252d_highs_504d_d2},
    "f07_lhll_118_pivot10_high_below_running_max_atr_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_118_pivot10_high_below_running_max_atr_d2},
    "f07_lhll_119_pivot10_high_below_running_max_log_d2": {"inputs": ["high"], "func": f07_lhll_119_pivot10_high_below_running_max_log_d2},
    "f07_lhll_120_consecutive_lower_pivot10_highs_since_alltime_d2": {"inputs": ["high"], "func": f07_lhll_120_consecutive_lower_pivot10_highs_since_alltime_d2},
    "f07_lhll_121_bars_since_alltime_pivot10_high_d2": {"inputs": ["high"], "func": f07_lhll_121_bars_since_alltime_pivot10_high_d2},
    "f07_lhll_122_lh_to_total_pivots_ratio_504d_d2": {"inputs": ["high"], "func": f07_lhll_122_lh_to_total_pivots_ratio_504d_d2},
    "f07_lhll_123_ll_to_total_pivots_ratio_504d_d2": {"inputs": ["low"], "func": f07_lhll_123_ll_to_total_pivots_ratio_504d_d2},
    "f07_lhll_124_combined_lh_ll_ratio_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_124_combined_lh_ll_ratio_504d_d2},
    "f07_lhll_125_pivot10_high_makes_new_252d_low_indicator_d2": {"inputs": ["high", "low"], "func": f07_lhll_125_pivot10_high_makes_new_252d_low_indicator_d2},
    "f07_lhll_126_recent_pivot10_high_below_252d_max_indicator_d2": {"inputs": ["high"], "func": f07_lhll_126_recent_pivot10_high_below_252d_max_indicator_d2},
    "f07_lhll_127_swing_count_ratio_down_vs_up_pivot10_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_127_swing_count_ratio_down_vs_up_pivot10_504d_d2},
    "f07_lhll_128_pivot10_swing_amplitude_decay_log_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_128_pivot10_swing_amplitude_decay_log_252d_d2},
    "f07_lhll_129_pivot10_average_log_return_per_swing_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_129_pivot10_average_log_return_per_swing_252d_d2},
    "f07_lhll_130_pivot10_signed_swing_return_sum_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_130_pivot10_signed_swing_return_sum_252d_d2},
    "f07_lhll_131_pivot10_low_below_prev_two_indicator_d2": {"inputs": ["low"], "func": f07_lhll_131_pivot10_low_below_prev_two_indicator_d2},
    "f07_lhll_132_pivot10_high_below_prev_two_indicator_d2": {"inputs": ["high"], "func": f07_lhll_132_pivot10_high_below_prev_two_indicator_d2},
    "f07_lhll_133_three_consecutive_lower_pivot10_highs_indicator_d2": {"inputs": ["high"], "func": f07_lhll_133_three_consecutive_lower_pivot10_highs_indicator_d2},
    "f07_lhll_134_three_consecutive_lower_pivot10_lows_indicator_d2": {"inputs": ["low"], "func": f07_lhll_134_three_consecutive_lower_pivot10_lows_indicator_d2},
    "f07_lhll_135_pivot10_low_below_252d_low_indicator_d2": {"inputs": ["low"], "func": f07_lhll_135_pivot10_low_below_252d_low_indicator_d2},
    "f07_lhll_136_pivot10_high_log_distance_to_alltime_d2": {"inputs": ["high"], "func": f07_lhll_136_pivot10_high_log_distance_to_alltime_d2},
    "f07_lhll_137_pivot_high_max_streak_lh_in_504d_d2": {"inputs": ["high"], "func": f07_lhll_137_pivot_high_max_streak_lh_in_504d_d2},
    "f07_lhll_138_pivot_low_max_streak_ll_in_504d_d2": {"inputs": ["low"], "func": f07_lhll_138_pivot_low_max_streak_ll_in_504d_d2},
    "f07_lhll_139_pivot10_low_below_2y_low_indicator_d2": {"inputs": ["low"], "func": f07_lhll_139_pivot10_low_below_2y_low_indicator_d2},
    "f07_lhll_140_pivot10_low_below_5y_low_indicator_d2": {"inputs": ["low"], "func": f07_lhll_140_pivot10_low_below_5y_low_indicator_d2},
    "f07_lhll_141_dow_score_negative_fraction_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_141_dow_score_negative_fraction_252d_d2},
    "f07_lhll_142_dow_score_minus_two_fraction_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_142_dow_score_minus_two_fraction_504d_d2},
    "f07_lhll_143_pivot10_high_count_in_top_decile_of_pv_dist_252d_d2": {"inputs": ["high"], "func": f07_lhll_143_pivot10_high_count_in_top_decile_of_pv_dist_252d_d2},
    "f07_lhll_144_pivot10_low_count_in_bottom_decile_of_pv_dist_252d_d2": {"inputs": ["low"], "func": f07_lhll_144_pivot10_low_count_in_bottom_decile_of_pv_dist_252d_d2},
    "f07_lhll_145_pivot10_swing_signed_drift_252d_d2": {"inputs": ["high", "low"], "func": f07_lhll_145_pivot10_swing_signed_drift_252d_d2},
    "f07_lhll_146_pivot10_high_signed_drift_252d_d2": {"inputs": ["high"], "func": f07_lhll_146_pivot10_high_signed_drift_252d_d2},
    "f07_lhll_147_pivot_combined_drift_zscore_504d_d2": {"inputs": ["high", "low"], "func": f07_lhll_147_pivot_combined_drift_zscore_504d_d2},
    "f07_lhll_148_max_log_lower_high_gap_in_252d_d2": {"inputs": ["high"], "func": f07_lhll_148_max_log_lower_high_gap_in_252d_d2},
    "f07_lhll_149_max_log_lower_low_gap_in_252d_d2": {"inputs": ["low"], "func": f07_lhll_149_max_log_lower_low_gap_in_252d_d2},
    "f07_lhll_150_dow_breakdown_pivot10_with_close_confirm_indicator_d2": {"inputs": ["high", "low", "close"], "func": f07_lhll_150_dow_breakdown_pivot10_with_close_confirm_indicator_d2},
}
