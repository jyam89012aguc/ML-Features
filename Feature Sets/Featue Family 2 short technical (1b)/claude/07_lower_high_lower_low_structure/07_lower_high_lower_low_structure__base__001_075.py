"""lower_high_lower_low_structure base features 001-075 — Pipeline 1b-technical.

Dow-theory uptrend-breakdown hypotheses: swing-pivot identification, lower-high /
lower-low formation counts, slopes of pivot-low and pivot-high sequences, broken
higher-high formation, pivot hierarchy degradation, swing-amplitude asymmetry,
swing-leg duration asymmetry, fractal patterns, new-N-day-high vs new-N-day-low
race. SEP OHLCV only. PIT-clean.

Distinct from family 10 (swing_pivot_topology, which handles raw amplitude-decay
/ zigzag-compression / generic pivot counts) — here the emphasis is on the
*structural sequence* and Dow-theory regime degradation.
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
    """Boolean Series, True at time t when bar t-n is confirmed as a pivot-high.
    PIT-safe: uses only data from t-2n..t."""
    window = 2 * n + 1
    rolling_max = high.rolling(window, min_periods=window).max()
    center_val = high.shift(n)
    return (center_val == rolling_max) & rolling_max.notna()


def _pivot_low_event(low, n):
    """Boolean Series, True at time t when bar t-n is confirmed as a pivot-low.
    PIT-safe: uses only data from t-2n..t."""
    window = 2 * n + 1
    rolling_min = low.rolling(window, min_periods=window).min()
    center_val = low.shift(n)
    return (center_val == rolling_min) & rolling_min.notna()


def _pivot_high_value(high, n):
    """Series with the pivot-high price at confirmation time t (else NaN)."""
    evt = _pivot_high_event(high, n)
    val = high.shift(n)
    return val.where(evt, np.nan)


def _pivot_low_value(low, n):
    """Series with the pivot-low price at confirmation time t (else NaN)."""
    evt = _pivot_low_event(low, n)
    val = low.shift(n)
    return val.where(evt, np.nan)


# ============================================================
# Bucket A — Lower-high counts at multi-horizon (001-009)
# Each horizon = a different hypothesis (short / medium / long topping)
# ============================================================

def f07_lhll_001_lower_high_count_pivot5_in_63d(high: pd.Series) -> pd.Series:
    """Count of confirmed pivot5-highs in trailing 63d that are LOWER than the
    immediately prior pivot5-high — short-term topping cadence (n=5)."""
    pv = _pivot_high_value(high, 5)
    prev = pv.shift(1).ffill()  # carry last pivot value forward
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_lh.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_lhll_002_lower_high_count_pivot10_in_252d(high: pd.Series) -> pd.Series:
    """Count of confirmed pivot10-highs in trailing 252d that are LOWER than the
    immediately prior pivot10-high — medium-term topping (n=10)."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_lh.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_003_lower_high_count_pivot21_in_504d(high: pd.Series) -> pd.Series:
    """Count of confirmed pivot21-highs in trailing 504d that are LOWER than the
    immediately prior pivot21-high — long-term regime topping (n=21)."""
    pv = _pivot_high_value(high, 21)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_lh.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_004_lower_high_ratio_pivot10_in_252d(high: pd.Series) -> pd.Series:
    """Ratio of lower-highs to total pivot10-high events in trailing 252d
    (0 = all higher-highs / 1 = all lower-highs)."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = pv.notna().astype(float)
    num = is_lh.rolling(YDAYS, min_periods=QDAYS).sum()
    den = is_evt.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f07_lhll_005_longest_lower_high_streak_pivot5_252d(high: pd.Series) -> pd.Series:
    """Longest run of CONSECUTIVE lower-highs (pivot5) within trailing 252d
    — most extreme topping pulse."""
    pv = _pivot_high_value(high, 5)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_hh = ((pv.notna()) & (prev.notna()) & (pv >= prev)).astype(float)
    # marker: +1 LH, -1 HH, 0 otherwise; then longest run of +1
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
    return mark.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True)


def f07_lhll_006_current_lower_high_streak_pivot10(high: pd.Series) -> pd.Series:
    """Current consecutive-lower-highs streak length (pivot10) ending today."""
    pv = _pivot_high_value(high, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev_val = np.nan
    last_streak = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val):
                if v < prev_val:
                    streak += 1
                else:
                    streak = 0
            last_streak = float(streak)
            prev_val = v
        out[i] = last_streak
    return pd.Series(out, index=high.index)


def f07_lhll_007_lower_high_fraction_expanding_pivot21(high: pd.Series) -> pd.Series:
    """Expanding fraction of pivot21-high events that were lower-highs
    — long-horizon regime measure."""
    pv = _pivot_high_value(high, 21)
    prev = pv.shift(1).ffill()
    is_lh = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = ((pv.notna()) & (prev.notna())).astype(float)
    num = is_lh.expanding(min_periods=1).sum()
    den = is_evt.expanding(min_periods=1).sum()
    return _safe_div(num, den)


def f07_lhll_008_lower_high_severity_log_pivot10_252d(high: pd.Series) -> pd.Series:
    """Mean log shortfall of lower-highs vs their prior pivot10-high in trailing 252d
    — magnitude (not just count) of downside pivot degradation."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    shortfall = (_safe_log(prev) - _safe_log(pv)).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    return shortfall.rolling(YDAYS, min_periods=MDAYS).mean()


def f07_lhll_009_lower_high_severity_atr_pivot10_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR21-normalized shortfall of lower-highs vs prior pivot10-high in 252d."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    short = (prev - pv).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    norm = _safe_div(short, atr)
    return norm.rolling(YDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket B — Lower-low counts at multi-horizon (010-018)
# ============================================================

def f07_lhll_010_lower_low_count_pivot5_in_63d(low: pd.Series) -> pd.Series:
    """Count of confirmed pivot5-lows in trailing 63d that are LOWER than prior
    pivot5-low — short-term breakdown cadence."""
    pv = _pivot_low_value(low, 5)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_ll.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_lhll_011_lower_low_count_pivot10_in_252d(low: pd.Series) -> pd.Series:
    """Count of confirmed pivot10-lows in trailing 252d that are LOWER than prior
    pivot10-low — medium-term breakdown."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_ll.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_012_lower_low_count_pivot21_in_504d(low: pd.Series) -> pd.Series:
    """Count of pivot21-lows in trailing 504d that are LOWER than prior
    pivot21-low — long-term regime breakdown."""
    pv = _pivot_low_value(low, 21)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    return is_ll.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_013_lower_low_ratio_pivot10_in_252d(low: pd.Series) -> pd.Series:
    """Ratio of lower-lows to all pivot10-low events in trailing 252d."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = ((pv.notna()) & (prev.notna())).astype(float)
    num = is_ll.rolling(YDAYS, min_periods=QDAYS).sum()
    den = is_evt.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f07_lhll_014_longest_lower_low_streak_pivot5_252d(low: pd.Series) -> pd.Series:
    """Longest run of consecutive lower-lows (pivot5) in trailing 252d."""
    pv = _pivot_low_value(low, 5)
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
    return mark.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True)


def f07_lhll_015_current_lower_low_streak_pivot10(low: pd.Series) -> pd.Series:
    """Current consecutive-lower-lows streak length (pivot10) ending today."""
    pv = _pivot_low_value(low, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev_val = np.nan
    last_streak = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val):
                if v < prev_val:
                    streak += 1
                else:
                    streak = 0
            last_streak = float(streak)
            prev_val = v
        out[i] = last_streak
    return pd.Series(out, index=low.index)


def f07_lhll_016_lower_low_fraction_expanding_pivot21(low: pd.Series) -> pd.Series:
    """Expanding fraction of pivot21-low events that were lower-lows."""
    pv = _pivot_low_value(low, 21)
    prev = pv.shift(1).ffill()
    is_ll = ((pv.notna()) & (prev.notna()) & (pv < prev)).astype(float)
    is_evt = ((pv.notna()) & (prev.notna())).astype(float)
    num = is_ll.expanding(min_periods=1).sum()
    den = is_evt.expanding(min_periods=1).sum()
    return _safe_div(num, den)


def f07_lhll_017_lower_low_severity_log_pivot10_252d(low: pd.Series) -> pd.Series:
    """Mean log shortfall of lower-lows vs prior pivot10-low in 252d."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    short = (_safe_log(prev) - _safe_log(pv)).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    return short.rolling(YDAYS, min_periods=MDAYS).mean()


def f07_lhll_018_lower_low_severity_atr_pivot10_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR21-normalized shortfall of lower-lows vs prior pivot10-low in 252d."""
    pv = _pivot_low_value(low, 10)
    prev = pv.shift(1).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    short = (prev - pv).where((pv.notna()) & (prev.notna()) & (pv < prev), np.nan)
    norm = _safe_div(short, atr)
    return norm.rolling(YDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket C — Dow-theory breakdown events (019-027)
# ============================================================

def f07_lhll_019_days_since_last_higher_high_pivot10(high: pd.Series) -> pd.Series:
    """Bars since the last confirmed pivot10 HIGHER-high
    (pivot10 > previous pivot10) — staleness of last bullish-confirmation."""
    pv = _pivot_high_value(high, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    last_hh_idx = -1
    prev_val = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val) and v > prev_val:
                last_hh_idx = i
            prev_val = v
        if last_hh_idx >= 0:
            out[i] = float(i - last_hh_idx)
    return pd.Series(out, index=high.index)


def f07_lhll_020_days_since_last_higher_low_pivot10(low: pd.Series) -> pd.Series:
    """Bars since the last confirmed pivot10 HIGHER-low — staleness of last
    bullish-trend pivot-low confirmation."""
    pv = _pivot_low_value(low, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    last_hl_idx = -1
    prev_val = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val) and v > prev_val:
                last_hl_idx = i
            prev_val = v
        if last_hl_idx >= 0:
            out[i] = float(i - last_hl_idx)
    return pd.Series(out, index=low.index)


def f07_lhll_021_dow_breakdown_event_count_pivot10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Dow-theory breakdown events (a new pivot10 LOWER-LOW formed AFTER
    the most recent pivot10 HIGHER-HIGH) in trailing 252d."""
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    n = len(pvh)
    out_evt = np.zeros(n, dtype=float)
    last_hh_idx = -1
    last_hh_val = np.nan
    prev_h = np.nan
    prev_l = np.nan
    most_recent_ll_after_hh_idx = -1
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if not np.isnan(prev_h) and vh > prev_h:
                last_hh_idx = i
                last_hh_val = vh
                most_recent_ll_after_hh_idx = -1
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l) and vl < prev_l and last_hh_idx >= 0 and i > last_hh_idx:
                if i != most_recent_ll_after_hh_idx:
                    out_evt[i] = 1.0
                    most_recent_ll_after_hh_idx = i
            prev_l = vl
    out_evt_s = pd.Series(out_evt, index=high.index)
    return out_evt_s.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_022_days_since_dow_breakdown_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the most recent Dow-theory breakdown event (LL after HH)."""
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    n = len(pvh)
    out = np.full(n, np.nan, dtype=float)
    last_hh_idx = -1
    last_break_idx = -1
    prev_h = np.nan
    prev_l = np.nan
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if not np.isnan(prev_h) and vh > prev_h:
                last_hh_idx = i
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l) and vl < prev_l and last_hh_idx >= 0 and i > last_hh_idx:
                last_break_idx = i
            prev_l = vl
        if last_break_idx >= 0:
            out[i] = float(i - last_break_idx)
    return pd.Series(out, index=high.index)


def f07_lhll_023_dow_breakdown_severity_atr_pivot10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized severity of the most recent LL-after-HH breakdown:
    (prior_pivot_low - new_lower_pivot_low) / ATR21, carried forward until next breakdown."""
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    atr = _atr(high, low, close, n=MDAYS).values
    n = len(pvh)
    out = np.full(n, np.nan, dtype=float)
    last_hh_idx = -1
    prev_h = np.nan
    prev_l = np.nan
    last_sev = np.nan
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if not np.isnan(prev_h) and vh > prev_h:
                last_hh_idx = i
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l) and vl < prev_l and last_hh_idx >= 0 and i > last_hh_idx:
                a = atr[i]
                if not np.isnan(a) and a > 0:
                    last_sev = (prev_l - vl) / a
            prev_l = vl
        out[i] = last_sev
    return pd.Series(out, index=high.index)


def f07_lhll_024_dow_uptrend_intact_indicator_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when the most recent pivot10 high is the highest pivot10 high to date AND
    the most recent pivot10 low is higher than the prior pivot10 low (Dow-uptrend);
    else 0."""
    pvh = _pivot_high_value(high, 10).values
    pvl = _pivot_low_value(low, 10).values
    n = len(pvh)
    out = np.full(n, np.nan, dtype=float)
    max_hh = -np.inf
    prev_h = np.nan
    prev_l = np.nan
    h_ok = np.nan
    l_ok = np.nan
    for i in range(n):
        vh = pvh[i]
        vl = pvl[i]
        if not np.isnan(vh):
            if vh >= max_hh:
                max_hh = vh
                h_ok = 1.0
            else:
                h_ok = 0.0
            prev_h = vh
        if not np.isnan(vl):
            if not np.isnan(prev_l):
                l_ok = 1.0 if vl > prev_l else 0.0
            prev_l = vl
        if not (np.isnan(h_ok) or np.isnan(l_ok)):
            out[i] = 1.0 if (h_ok > 0.5 and l_ok > 0.5) else 0.0
    return pd.Series(out, index=high.index)


def f07_lhll_025_consecutive_dow_uptrend_intact_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bars streak where Dow-uptrend indicator (f024) is 1."""
    base = f07_lhll_024_dow_uptrend_intact_indicator_pivot10(high, low).values
    n = len(base)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        v = base[i]
        if np.isnan(v):
            out[i] = np.nan
        else:
            streak = streak + 1 if v > 0.5 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)


def f07_lhll_026_dow_breakdown_event_count_pivot21_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Long-horizon (pivot21) Dow-breakdown event count in trailing 504d."""
    pvh = _pivot_high_value(high, 21).values
    pvl = _pivot_low_value(low, 21).values
    n = len(pvh)
    out_evt = np.zeros(n, dtype=float)
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
                    out_evt[i] = 1.0
                    most_recent_ll_after_hh_idx = i
            prev_l = vl
    out_evt_s = pd.Series(out_evt, index=high.index)
    return out_evt_s.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f07_lhll_027_dow_breakdown_event_count_pivot5_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Short-horizon (pivot5) Dow-breakdown event count in trailing 63d."""
    pvh = _pivot_high_value(high, 5).values
    pvl = _pivot_low_value(low, 5).values
    n = len(pvh)
    out_evt = np.zeros(n, dtype=float)
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
                    out_evt[i] = 1.0
                    most_recent_ll_after_hh_idx = i
            prev_l = vl
    out_evt_s = pd.Series(out_evt, index=high.index)
    return out_evt_s.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket D — Pivot-low slope (028-033)
# ============================================================

def f07_lhll_028_pivot_low_value_slope_pivot10_252d(low: pd.Series) -> pd.Series:
    """Slope of forward-filled pivot10-low-value series over trailing 252d
    — negative slope = degrading support (LL sequence)."""
    pv = _pivot_low_value(low, 10).ffill()
    return _rolling_slope(pv, YDAYS, min_periods=QDAYS)


def f07_lhll_029_pivot_low_value_slope_pivot21_504d(low: pd.Series) -> pd.Series:
    """Long-horizon slope of pivot21-low-value series over 504d."""
    pv = _pivot_low_value(low, 21).ffill()
    return _rolling_slope(pv, DDAYS_2Y, min_periods=YDAYS)


def f07_lhll_030_pivot_low_value_slope_pivot5_63d(low: pd.Series) -> pd.Series:
    """Short-horizon slope of pivot5-low-value series over 63d."""
    pv = _pivot_low_value(low, 5).ffill()
    return _rolling_slope(pv, QDAYS, min_periods=MDAYS)


def f07_lhll_031_pivot_low_log_slope_pivot10_252d(low: pd.Series) -> pd.Series:
    """Slope of log(pivot10-low-value) over 252d — scale-free pivot-low decay rate."""
    pv = _safe_log(_pivot_low_value(low, 10).ffill())
    return _rolling_slope(pv, YDAYS, min_periods=QDAYS)


def f07_lhll_032_pivot_low_slope_sign_negative_indicator_pivot10(low: pd.Series) -> pd.Series:
    """1 when 252d pivot10-low slope is negative (Dow downtrend by support), else 0."""
    sl = f07_lhll_028_pivot_low_value_slope_pivot10_252d(low)
    return (sl < 0).astype(float).where(sl.notna(), np.nan)


def f07_lhll_033_pivot_low_slope_zscore_pivot10_504d(low: pd.Series) -> pd.Series:
    """504d z-score of the 252d pivot10-low slope — anomaly in the decay rate."""
    sl = f07_lhll_028_pivot_low_value_slope_pivot10_252d(low)
    return _rolling_zscore(sl, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket E — Pivot-high slope & sign flip (034-039)
# ============================================================

def f07_lhll_034_pivot_high_value_slope_pivot10_252d(high: pd.Series) -> pd.Series:
    """Slope of forward-filled pivot10-high-value series over 252d
    — negative = LH sequence (Dow downtrend by resistance)."""
    pv = _pivot_high_value(high, 10).ffill()
    return _rolling_slope(pv, YDAYS, min_periods=QDAYS)


def f07_lhll_035_pivot_high_value_slope_pivot21_504d(high: pd.Series) -> pd.Series:
    """Long-horizon slope of pivot21-high-value over 504d."""
    pv = _pivot_high_value(high, 21).ffill()
    return _rolling_slope(pv, DDAYS_2Y, min_periods=YDAYS)


def f07_lhll_036_pivot_high_value_slope_pivot5_63d(high: pd.Series) -> pd.Series:
    """Short-horizon slope of pivot5-high-value over 63d."""
    pv = _pivot_high_value(high, 5).ffill()
    return _rolling_slope(pv, QDAYS, min_periods=MDAYS)


def f07_lhll_037_pivot_high_log_slope_pivot10_252d(high: pd.Series) -> pd.Series:
    """Slope of log(pivot10-high-value) over 252d — scale-free resistance decay rate."""
    pv = _safe_log(_pivot_high_value(high, 10).ffill())
    return _rolling_slope(pv, YDAYS, min_periods=QDAYS)


def f07_lhll_038_pivot_high_slope_sign_flip_pos_to_neg_indicator(high: pd.Series) -> pd.Series:
    """1 when the 252d pivot10-high slope is now negative but was positive 63d ago
    — fresh topping/sign-flip event."""
    sl = f07_lhll_034_pivot_high_value_slope_pivot10_252d(high)
    flip = ((sl < 0) & (sl.shift(QDAYS) > 0)).astype(float)
    return flip.where(sl.notna() & sl.shift(QDAYS).notna(), np.nan)


def f07_lhll_039_pivot_high_slope_change_252d_minus_63d(high: pd.Series) -> pd.Series:
    """Long-minus-short slope difference: (252d pivot10 high slope) - (63d pivot10 high slope)
    — degree to which short-term slope is decelerating relative to long-term."""
    long_sl = f07_lhll_034_pivot_high_value_slope_pivot10_252d(high)
    short_sl = f07_lhll_036_pivot_high_value_slope_pivot5_63d(high)
    return long_sl - short_sl


# ============================================================
# Bucket F — Higher-high formation failure (040-045)
# ============================================================

def f07_lhll_040_most_recent_pivot10_high_shortfall_log(high: pd.Series) -> pd.Series:
    """Log shortfall: log(prior pivot10 high) - log(most-recent pivot10 high).
    > 0 means latest peak failed to exceed the prior one. Forward-filled until next pivot."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    cur = pv.ffill()
    return (_safe_log(prev) - _safe_log(cur))


def f07_lhll_041_most_recent_pivot10_high_shortfall_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized shortfall: (prior pivot10 high - latest pivot10 high) / ATR21."""
    pv = _pivot_high_value(high, 10)
    prev = pv.shift(1).ffill()
    cur = pv.ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(prev - cur, atr)


def f07_lhll_042_consecutive_failed_higher_highs_count_pivot10(high: pd.Series) -> pd.Series:
    """Count of consecutive most-recent pivot10-highs that failed to exceed their prior peak
    — running 'failed HH attempt' streak (resets on a true HH)."""
    pv = _pivot_high_value(high, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev_val = np.nan
    last_streak = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val):
                if v <= prev_val:
                    streak += 1
                else:
                    streak = 0
            last_streak = float(streak)
            prev_val = v
        out[i] = last_streak
    return pd.Series(out, index=high.index)


def f07_lhll_043_failed_higher_high_attempts_count_pivot10_252d(high: pd.Series) -> pd.Series:
    """Count of pivot10-high events in trailing 252d that failed to reach a new
    all-time-window-high (i.e., pivot value <= 252d running pivot max)."""
    pv = _pivot_high_value(high, 10)
    running_max = pv.expanding(min_periods=1).max()
    failed = ((pv.notna()) & (pv < running_max)).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_044_higher_high_formation_failure_severity_504d(high: pd.Series) -> pd.Series:
    """Mean log shortfall (relative to running expanding pivot-max) of failed HH attempts
    in trailing 504d — magnitude of failure, not just count."""
    pv = _pivot_high_value(high, 10)
    running_max = pv.expanding(min_periods=1).max()
    short = (_safe_log(running_max) - _safe_log(pv)).where(pv.notna(), np.nan)
    return short.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f07_lhll_045_post_hh_failure_decline_severity_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At each bar following a failed HH attempt, the ATR21-normalized fall of close
    from the prior pivot10 high. Forward-filled until next pivot. Encodes 'rejection depth'."""
    pv = _pivot_high_value(high, 10)
    prev_top = pv.shift(1).ffill()
    cur_pv = pv.ffill()
    failed_mask = (cur_pv.notna()) & (prev_top.notna()) & (cur_pv < prev_top)
    atr = _atr(high, low, close, n=MDAYS)
    fall = _safe_div(prev_top - close, atr)
    return fall.where(failed_mask, np.nan).ffill()


# ============================================================
# Bucket G — Swing-amplitude asymmetry (046-052)
# (distinct from family 10 which handles raw decay/zigzag-compression)
# ============================================================

def f07_lhll_046_downswing_to_upswing_amplitude_ratio_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Most-recent downswing amplitude / most-recent upswing amplitude (pivot10).
    A downswing = drop from a pivot-high to the next pivot-low; upswing the reverse.
    > 1 means downswings are now larger than upswings (topping)."""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    # Use most recent pivot-high and pivot-low values; ratio of (last_pvh - last_pvl) / (last_pvh - prev_pvl)
    prev_pvl = _pivot_low_value(low, 10).shift(1).ffill()
    up_amp = (pvh - prev_pvl).abs()
    down_amp = (pvh - pvl).abs()
    return _safe_div(down_amp, up_amp)


def f07_lhll_047_log_downswing_to_upswing_ratio_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log of downswing/upswing amplitude ratio — symmetric scale around 0."""
    r = f07_lhll_046_downswing_to_upswing_amplitude_ratio_pivot10(high, low)
    return _safe_log(r)


def f07_lhll_048_downswing_growth_rate_pivot10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope over 252d of |last pivot10-high - last pivot10-low| forward-filled series
    — are downswings getting larger over time (degradation)?"""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    down_amp = (pvh - pvl).abs()
    return _rolling_slope(down_amp, YDAYS, min_periods=QDAYS)


def f07_lhll_049_upswing_decay_rate_pivot10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope over 252d of |last pivot10-high - prior pivot10-low| forward-filled
    — declining upswing amplitudes = weakening demand."""
    pvh = _pivot_high_value(high, 10).ffill()
    prev_pvl = _pivot_low_value(low, 10).shift(1).ffill()
    up_amp = (pvh - prev_pvl).abs()
    return _rolling_slope(up_amp, YDAYS, min_periods=QDAYS)


def f07_lhll_050_swing_amplitude_asymmetry_zscore_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """504d z-score of log(downswing/upswing) ratio — anomalous swing asymmetry."""
    r = f07_lhll_047_log_downswing_to_upswing_ratio_pivot10(high, low)
    return _rolling_zscore(r, DDAYS_2Y, min_periods=YDAYS)


def f07_lhll_051_downswing_amplitude_atr_normalized_pivot10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current downswing amplitude (last pivot10 high - last pivot10 low), ATR21-normalized."""
    pvh = _pivot_high_value(high, 10).ffill()
    pvl = _pivot_low_value(low, 10).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div((pvh - pvl).abs(), atr)


def f07_lhll_052_upswing_amplitude_atr_normalized_pivot10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current upswing amplitude (last pivot10 high - prior pivot10 low), ATR21-normalized."""
    pvh = _pivot_high_value(high, 10).ffill()
    prev_pvl = _pivot_low_value(low, 10).shift(1).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div((pvh - prev_pvl).abs(), atr)


# ============================================================
# Bucket H — Swing-leg duration asymmetry (053-057)
# ============================================================

def f07_lhll_053_downswing_duration_bars_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Duration (in bars) between the most recent pivot10-high confirmation and the
    most recent pivot10-low confirmation, when the low is more recent than the high.
    Forward-filled. NaN otherwise."""
    pvh_evt = _pivot_high_event(high, 10).values
    pvl_evt = _pivot_low_event(low, 10).values
    n = len(pvh_evt)
    out = np.full(n, np.nan, dtype=float)
    last_h_idx = -1
    last_l_idx = -1
    last_val = np.nan
    for i in range(n):
        if pvh_evt[i]:
            last_h_idx = i
        if pvl_evt[i]:
            last_l_idx = i
        if last_h_idx >= 0 and last_l_idx >= 0 and last_l_idx > last_h_idx:
            last_val = float(last_l_idx - last_h_idx)
        out[i] = last_val
    return pd.Series(out, index=high.index)


def f07_lhll_054_upswing_duration_bars_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Duration in bars between the most recent pivot10-low and the most recent
    pivot10-high (when high is more recent than low). Forward-filled."""
    pvh_evt = _pivot_high_event(high, 10).values
    pvl_evt = _pivot_low_event(low, 10).values
    n = len(pvh_evt)
    out = np.full(n, np.nan, dtype=float)
    last_h_idx = -1
    last_l_idx = -1
    last_val = np.nan
    for i in range(n):
        if pvh_evt[i]:
            last_h_idx = i
        if pvl_evt[i]:
            last_l_idx = i
        if last_h_idx >= 0 and last_l_idx >= 0 and last_h_idx > last_l_idx:
            last_val = float(last_h_idx - last_l_idx)
        out[i] = last_val
    return pd.Series(out, index=high.index)


def f07_lhll_055_swing_duration_asymmetry_ratio_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Downswing duration / upswing duration ratio (pivot10), forward-filled.
    > 1 = down legs take longer than up legs (capitulation drift)."""
    dd = f07_lhll_053_downswing_duration_bars_pivot10(high, low)
    uu = f07_lhll_054_upswing_duration_bars_pivot10(high, low)
    return _safe_div(dd, uu)


def f07_lhll_056_downswing_duration_slope_pivot10_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """504d slope of the downswing duration series — are downswings getting longer?"""
    dd = f07_lhll_053_downswing_duration_bars_pivot10(high, low)
    return _rolling_slope(dd, DDAYS_2Y, min_periods=YDAYS)


def f07_lhll_057_upswing_duration_slope_pivot10_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """504d slope of the upswing duration series — are upswings shrinking in time?"""
    uu = f07_lhll_054_upswing_duration_bars_pivot10(high, low)
    return _rolling_slope(uu, DDAYS_2Y, min_periods=YDAYS)


# ============================================================
# Bucket I — Pivot hierarchy degradation (058-063)
# ============================================================

def f07_lhll_058_pivot_high_hierarchy_crack_5_below_21(high: pd.Series) -> pd.Series:
    """Indicator: most-recent pivot5-high is BELOW most-recent pivot21-high
    (small-scale topping below large-scale resistance)."""
    pv5 = _pivot_high_value(high, 5).ffill()
    pv21 = _pivot_high_value(high, 21).ffill()
    return (pv5 < pv21).astype(float).where(pv5.notna() & pv21.notna(), np.nan)


def f07_lhll_059_pivot_low_hierarchy_crack_5_below_21(low: pd.Series) -> pd.Series:
    """Indicator: most-recent pivot5-low is BELOW most-recent pivot21-low
    (short-term break of long-term support floor)."""
    pv5 = _pivot_low_value(low, 5).ffill()
    pv21 = _pivot_low_value(low, 21).ffill()
    return (pv5 < pv21).astype(float).where(pv5.notna() & pv21.notna(), np.nan)


def f07_lhll_060_pivot_high_hierarchy_atr_distance(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance: (pivot21-high - pivot5-high) / ATR21.
    Positive = pivot5 is below pivot21 (cracked hierarchy)."""
    pv5 = _pivot_high_value(high, 5).ffill()
    pv21 = _pivot_high_value(high, 21).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(pv21 - pv5, atr)


def f07_lhll_061_pivot_low_hierarchy_atr_distance(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance: (pivot21-low - pivot5-low) / ATR21.
    Positive = pivot5 low is below pivot21 low (cracked support floor)."""
    pv5 = _pivot_low_value(low, 5).ffill()
    pv21 = _pivot_low_value(low, 21).ffill()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(pv21 - pv5, atr)


def f07_lhll_062_hierarchy_pivot_high_below_count_252d(high: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where pivot5-high < pivot21-high (cracked hierarchy)."""
    ind = f07_lhll_058_pivot_high_hierarchy_crack_5_below_21(high)
    return ind.rolling(YDAYS, min_periods=QDAYS).sum()


def f07_lhll_063_hierarchy_pivot_low_below_count_252d(low: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where pivot5-low < pivot21-low (cracked support)."""
    ind = f07_lhll_059_pivot_low_hierarchy_crack_5_below_21(low)
    return ind.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket J — Most-recent swing-direction state (064-069)
# ============================================================

def f07_lhll_064_bars_since_last_new_alltime_high(high: pd.Series) -> pd.Series:
    """Bars since the last expanding-all-time-high was set — staleness of the bull case."""
    arr = high.values
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_idx = i
            if cur_idx >= 0:
                out[i] = float(i - cur_idx)
    return pd.Series(out, index=high.index)


def f07_lhll_065_bars_since_last_higher_low_pivot21(low: pd.Series) -> pd.Series:
    """Bars since the last pivot21 higher-low — long-horizon Dow-trend staleness."""
    pv = _pivot_low_value(low, 21).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    last_hl_idx = -1
    prev_val = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val) and v > prev_val:
                last_hl_idx = i
            prev_val = v
        if last_hl_idx >= 0:
            out[i] = float(i - last_hl_idx)
    return pd.Series(out, index=low.index)


def f07_lhll_066_consecutive_down_swings_count_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of consecutive most-recent pivot10 swing-legs whose net direction is down
    (pivot-high then pivot-low pair where the pivot-low < prior pivot-low)."""
    pvl = _pivot_low_value(low, 10).values
    n = len(pvl)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev_val = np.nan
    last_streak = np.nan
    for i in range(n):
        v = pvl[i]
        if not np.isnan(v):
            if not np.isnan(prev_val):
                if v < prev_val:
                    streak += 1
                else:
                    streak = 0
            last_streak = float(streak)
            prev_val = v
        out[i] = last_streak
    return pd.Series(out, index=low.index)


def f07_lhll_067_most_recent_swing_direction_indicator_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 if the last confirmed pivot was a pivot10-high (next leg presumably down);
    -1 if the last confirmed pivot was a pivot10-low; 0 / NaN otherwise.
    Equivalent to: latest pivot is a peak (bearish setup)."""
    pvh_evt = _pivot_high_event(high, 10).values
    pvl_evt = _pivot_low_event(low, 10).values
    n = len(pvh_evt)
    out = np.full(n, np.nan, dtype=float)
    last_kind = 0  # +1 = high, -1 = low
    last_val = np.nan
    for i in range(n):
        if pvh_evt[i]:
            last_kind = 1
        if pvl_evt[i]:
            last_kind = -1
        if last_kind != 0:
            last_val = float(last_kind)
        out[i] = last_val
    return pd.Series(out, index=high.index)


def f07_lhll_068_time_since_pivot10_high_minus_time_since_pivot10_low(high: pd.Series, low: pd.Series) -> pd.Series:
    """(bars since last pivot10-high) - (bars since last pivot10-low).
    < 0 means the most recent pivot was a HIGH (bearish setup)."""
    pvh_evt = _pivot_high_event(high, 10).values
    pvl_evt = _pivot_low_event(low, 10).values
    n = len(pvh_evt)
    out = np.full(n, np.nan, dtype=float)
    last_h_idx = -1
    last_l_idx = -1
    for i in range(n):
        if pvh_evt[i]:
            last_h_idx = i
        if pvl_evt[i]:
            last_l_idx = i
        if last_h_idx >= 0 and last_l_idx >= 0:
            out[i] = float((i - last_h_idx) - (i - last_l_idx))
    return pd.Series(out, index=high.index)


def f07_lhll_069_consecutive_higher_lows_count_pivot10(low: pd.Series) -> pd.Series:
    """Current consecutive HIGHER-lows streak length (pivot10). Resets to 0 on lower-low.
    Inverse measure of Bucket B — higher value = strong uptrend support."""
    pv = _pivot_low_value(low, 10).values
    n = len(pv)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    prev_val = np.nan
    last_streak = np.nan
    for i in range(n):
        v = pv[i]
        if not np.isnan(v):
            if not np.isnan(prev_val):
                if v > prev_val:
                    streak += 1
                else:
                    streak = 0
            last_streak = float(streak)
            prev_val = v
        out[i] = last_streak
    return pd.Series(out, index=low.index)


# ============================================================
# Bucket K — Multi-scale pivot agreement (070-075)
# ============================================================

def f07_lhll_070_pivot_low_slope_sign_agreement_5_vs_21(low: pd.Series) -> pd.Series:
    """Sign-agreement indicator: +1 if both pivot5 and pivot21 low-slopes (252d window) are
    same sign; -1 if opposite signs; 0 if either is exactly zero."""
    sl5 = _rolling_slope(_pivot_low_value(low, 5).ffill(), YDAYS, min_periods=QDAYS)
    sl21 = _rolling_slope(_pivot_low_value(low, 21).ffill(), YDAYS, min_periods=QDAYS)
    sign_match = np.sign(sl5) * np.sign(sl21)
    return sign_match.where(sl5.notna() & sl21.notna(), np.nan)


def f07_lhll_071_pivot_high_slope_sign_agreement_5_vs_21(high: pd.Series) -> pd.Series:
    """Sign-agreement of pivot5 and pivot21 high-slopes over 252d window."""
    sl5 = _rolling_slope(_pivot_high_value(high, 5).ffill(), YDAYS, min_periods=QDAYS)
    sl21 = _rolling_slope(_pivot_high_value(high, 21).ffill(), YDAYS, min_periods=QDAYS)
    sign_match = np.sign(sl5) * np.sign(sl21)
    return sign_match.where(sl5.notna() & sl21.notna(), np.nan)


def f07_lhll_072_pivot_slope_cross_axis_agreement_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 if both pivot10 high-slope and low-slope are negative (Dow downtrend by both axes);
    -1 if both positive; 0 if mixed."""
    sh = _rolling_slope(_pivot_high_value(high, 10).ffill(), YDAYS, min_periods=QDAYS)
    sl = _rolling_slope(_pivot_low_value(low, 10).ffill(), YDAYS, min_periods=QDAYS)
    both_neg = ((sh < 0) & (sl < 0)).astype(float)
    both_pos = ((sh > 0) & (sl > 0)).astype(float)
    return (both_neg - both_pos).where(sh.notna() & sl.notna(), np.nan)


def f07_lhll_073_pivot_low_slope_diff_5_minus_21(low: pd.Series) -> pd.Series:
    """Difference: pivot5-low slope (252d) - pivot21-low slope (252d).
    Negative = short-term low-slope worse than long-term (acceleration)."""
    sl5 = _rolling_slope(_pivot_low_value(low, 5).ffill(), YDAYS, min_periods=QDAYS)
    sl21 = _rolling_slope(_pivot_low_value(low, 21).ffill(), YDAYS, min_periods=QDAYS)
    return sl5 - sl21


def f07_lhll_074_pivot_high_slope_diff_5_minus_21(high: pd.Series) -> pd.Series:
    """Difference: pivot5-high slope (252d) - pivot21-high slope (252d)."""
    sl5 = _rolling_slope(_pivot_high_value(high, 5).ffill(), YDAYS, min_periods=QDAYS)
    sl21 = _rolling_slope(_pivot_high_value(high, 21).ffill(), YDAYS, min_periods=QDAYS)
    return sl5 - sl21


def f07_lhll_075_dow_full_breakdown_composite_pivot10(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when ALL of: pivot10 high-slope (252d) < 0, pivot10 low-slope (252d) < 0,
    most-recent pivot10 high failed to make a HH, most-recent pivot10 low made a LL.
    Else 0. Cross-confirmation Dow-breakdown composite."""
    sh = _rolling_slope(_pivot_high_value(high, 10).ffill(), YDAYS, min_periods=QDAYS)
    sl = _rolling_slope(_pivot_low_value(low, 10).ffill(), YDAYS, min_periods=QDAYS)
    pvh = _pivot_high_value(high, 10)
    pvl = _pivot_low_value(low, 10)
    prev_h = pvh.shift(1).ffill()
    cur_h = pvh.ffill()
    prev_l = pvl.shift(1).ffill()
    cur_l = pvl.ffill()
    hh_fail = (cur_h < prev_h)
    ll_made = (cur_l < prev_l)
    composite = ((sh < 0) & (sl < 0) & hh_fail & ll_made).astype(float)
    valid = sh.notna() & sl.notna() & cur_h.notna() & prev_h.notna() & cur_l.notna() & prev_l.notna()
    return composite.where(valid, np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

LOWER_HIGH_LOWER_LOW_STRUCTURE_BASE_REGISTRY_001_075 = {
    "f07_lhll_001_lower_high_count_pivot5_in_63d": {"inputs": ["high"], "func": f07_lhll_001_lower_high_count_pivot5_in_63d},
    "f07_lhll_002_lower_high_count_pivot10_in_252d": {"inputs": ["high"], "func": f07_lhll_002_lower_high_count_pivot10_in_252d},
    "f07_lhll_003_lower_high_count_pivot21_in_504d": {"inputs": ["high"], "func": f07_lhll_003_lower_high_count_pivot21_in_504d},
    "f07_lhll_004_lower_high_ratio_pivot10_in_252d": {"inputs": ["high"], "func": f07_lhll_004_lower_high_ratio_pivot10_in_252d},
    "f07_lhll_005_longest_lower_high_streak_pivot5_252d": {"inputs": ["high"], "func": f07_lhll_005_longest_lower_high_streak_pivot5_252d},
    "f07_lhll_006_current_lower_high_streak_pivot10": {"inputs": ["high"], "func": f07_lhll_006_current_lower_high_streak_pivot10},
    "f07_lhll_007_lower_high_fraction_expanding_pivot21": {"inputs": ["high"], "func": f07_lhll_007_lower_high_fraction_expanding_pivot21},
    "f07_lhll_008_lower_high_severity_log_pivot10_252d": {"inputs": ["high"], "func": f07_lhll_008_lower_high_severity_log_pivot10_252d},
    "f07_lhll_009_lower_high_severity_atr_pivot10_252d": {"inputs": ["high", "low", "close"], "func": f07_lhll_009_lower_high_severity_atr_pivot10_252d},
    "f07_lhll_010_lower_low_count_pivot5_in_63d": {"inputs": ["low"], "func": f07_lhll_010_lower_low_count_pivot5_in_63d},
    "f07_lhll_011_lower_low_count_pivot10_in_252d": {"inputs": ["low"], "func": f07_lhll_011_lower_low_count_pivot10_in_252d},
    "f07_lhll_012_lower_low_count_pivot21_in_504d": {"inputs": ["low"], "func": f07_lhll_012_lower_low_count_pivot21_in_504d},
    "f07_lhll_013_lower_low_ratio_pivot10_in_252d": {"inputs": ["low"], "func": f07_lhll_013_lower_low_ratio_pivot10_in_252d},
    "f07_lhll_014_longest_lower_low_streak_pivot5_252d": {"inputs": ["low"], "func": f07_lhll_014_longest_lower_low_streak_pivot5_252d},
    "f07_lhll_015_current_lower_low_streak_pivot10": {"inputs": ["low"], "func": f07_lhll_015_current_lower_low_streak_pivot10},
    "f07_lhll_016_lower_low_fraction_expanding_pivot21": {"inputs": ["low"], "func": f07_lhll_016_lower_low_fraction_expanding_pivot21},
    "f07_lhll_017_lower_low_severity_log_pivot10_252d": {"inputs": ["low"], "func": f07_lhll_017_lower_low_severity_log_pivot10_252d},
    "f07_lhll_018_lower_low_severity_atr_pivot10_252d": {"inputs": ["high", "low", "close"], "func": f07_lhll_018_lower_low_severity_atr_pivot10_252d},
    "f07_lhll_019_days_since_last_higher_high_pivot10": {"inputs": ["high"], "func": f07_lhll_019_days_since_last_higher_high_pivot10},
    "f07_lhll_020_days_since_last_higher_low_pivot10": {"inputs": ["low"], "func": f07_lhll_020_days_since_last_higher_low_pivot10},
    "f07_lhll_021_dow_breakdown_event_count_pivot10_252d": {"inputs": ["high", "low"], "func": f07_lhll_021_dow_breakdown_event_count_pivot10_252d},
    "f07_lhll_022_days_since_dow_breakdown_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_022_days_since_dow_breakdown_pivot10},
    "f07_lhll_023_dow_breakdown_severity_atr_pivot10": {"inputs": ["high", "low", "close"], "func": f07_lhll_023_dow_breakdown_severity_atr_pivot10},
    "f07_lhll_024_dow_uptrend_intact_indicator_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_024_dow_uptrend_intact_indicator_pivot10},
    "f07_lhll_025_consecutive_dow_uptrend_intact_streak": {"inputs": ["high", "low"], "func": f07_lhll_025_consecutive_dow_uptrend_intact_streak},
    "f07_lhll_026_dow_breakdown_event_count_pivot21_504d": {"inputs": ["high", "low"], "func": f07_lhll_026_dow_breakdown_event_count_pivot21_504d},
    "f07_lhll_027_dow_breakdown_event_count_pivot5_63d": {"inputs": ["high", "low"], "func": f07_lhll_027_dow_breakdown_event_count_pivot5_63d},
    "f07_lhll_028_pivot_low_value_slope_pivot10_252d": {"inputs": ["low"], "func": f07_lhll_028_pivot_low_value_slope_pivot10_252d},
    "f07_lhll_029_pivot_low_value_slope_pivot21_504d": {"inputs": ["low"], "func": f07_lhll_029_pivot_low_value_slope_pivot21_504d},
    "f07_lhll_030_pivot_low_value_slope_pivot5_63d": {"inputs": ["low"], "func": f07_lhll_030_pivot_low_value_slope_pivot5_63d},
    "f07_lhll_031_pivot_low_log_slope_pivot10_252d": {"inputs": ["low"], "func": f07_lhll_031_pivot_low_log_slope_pivot10_252d},
    "f07_lhll_032_pivot_low_slope_sign_negative_indicator_pivot10": {"inputs": ["low"], "func": f07_lhll_032_pivot_low_slope_sign_negative_indicator_pivot10},
    "f07_lhll_033_pivot_low_slope_zscore_pivot10_504d": {"inputs": ["low"], "func": f07_lhll_033_pivot_low_slope_zscore_pivot10_504d},
    "f07_lhll_034_pivot_high_value_slope_pivot10_252d": {"inputs": ["high"], "func": f07_lhll_034_pivot_high_value_slope_pivot10_252d},
    "f07_lhll_035_pivot_high_value_slope_pivot21_504d": {"inputs": ["high"], "func": f07_lhll_035_pivot_high_value_slope_pivot21_504d},
    "f07_lhll_036_pivot_high_value_slope_pivot5_63d": {"inputs": ["high"], "func": f07_lhll_036_pivot_high_value_slope_pivot5_63d},
    "f07_lhll_037_pivot_high_log_slope_pivot10_252d": {"inputs": ["high"], "func": f07_lhll_037_pivot_high_log_slope_pivot10_252d},
    "f07_lhll_038_pivot_high_slope_sign_flip_pos_to_neg_indicator": {"inputs": ["high"], "func": f07_lhll_038_pivot_high_slope_sign_flip_pos_to_neg_indicator},
    "f07_lhll_039_pivot_high_slope_change_252d_minus_63d": {"inputs": ["high"], "func": f07_lhll_039_pivot_high_slope_change_252d_minus_63d},
    "f07_lhll_040_most_recent_pivot10_high_shortfall_log": {"inputs": ["high"], "func": f07_lhll_040_most_recent_pivot10_high_shortfall_log},
    "f07_lhll_041_most_recent_pivot10_high_shortfall_atr": {"inputs": ["high", "low", "close"], "func": f07_lhll_041_most_recent_pivot10_high_shortfall_atr},
    "f07_lhll_042_consecutive_failed_higher_highs_count_pivot10": {"inputs": ["high"], "func": f07_lhll_042_consecutive_failed_higher_highs_count_pivot10},
    "f07_lhll_043_failed_higher_high_attempts_count_pivot10_252d": {"inputs": ["high"], "func": f07_lhll_043_failed_higher_high_attempts_count_pivot10_252d},
    "f07_lhll_044_higher_high_formation_failure_severity_504d": {"inputs": ["high"], "func": f07_lhll_044_higher_high_formation_failure_severity_504d},
    "f07_lhll_045_post_hh_failure_decline_severity_atr": {"inputs": ["high", "low", "close"], "func": f07_lhll_045_post_hh_failure_decline_severity_atr},
    "f07_lhll_046_downswing_to_upswing_amplitude_ratio_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_046_downswing_to_upswing_amplitude_ratio_pivot10},
    "f07_lhll_047_log_downswing_to_upswing_ratio_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_047_log_downswing_to_upswing_ratio_pivot10},
    "f07_lhll_048_downswing_growth_rate_pivot10_252d": {"inputs": ["high", "low"], "func": f07_lhll_048_downswing_growth_rate_pivot10_252d},
    "f07_lhll_049_upswing_decay_rate_pivot10_252d": {"inputs": ["high", "low"], "func": f07_lhll_049_upswing_decay_rate_pivot10_252d},
    "f07_lhll_050_swing_amplitude_asymmetry_zscore_504d": {"inputs": ["high", "low"], "func": f07_lhll_050_swing_amplitude_asymmetry_zscore_504d},
    "f07_lhll_051_downswing_amplitude_atr_normalized_pivot10": {"inputs": ["high", "low", "close"], "func": f07_lhll_051_downswing_amplitude_atr_normalized_pivot10},
    "f07_lhll_052_upswing_amplitude_atr_normalized_pivot10": {"inputs": ["high", "low", "close"], "func": f07_lhll_052_upswing_amplitude_atr_normalized_pivot10},
    "f07_lhll_053_downswing_duration_bars_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_053_downswing_duration_bars_pivot10},
    "f07_lhll_054_upswing_duration_bars_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_054_upswing_duration_bars_pivot10},
    "f07_lhll_055_swing_duration_asymmetry_ratio_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_055_swing_duration_asymmetry_ratio_pivot10},
    "f07_lhll_056_downswing_duration_slope_pivot10_504d": {"inputs": ["high", "low"], "func": f07_lhll_056_downswing_duration_slope_pivot10_504d},
    "f07_lhll_057_upswing_duration_slope_pivot10_504d": {"inputs": ["high", "low"], "func": f07_lhll_057_upswing_duration_slope_pivot10_504d},
    "f07_lhll_058_pivot_high_hierarchy_crack_5_below_21": {"inputs": ["high"], "func": f07_lhll_058_pivot_high_hierarchy_crack_5_below_21},
    "f07_lhll_059_pivot_low_hierarchy_crack_5_below_21": {"inputs": ["low"], "func": f07_lhll_059_pivot_low_hierarchy_crack_5_below_21},
    "f07_lhll_060_pivot_high_hierarchy_atr_distance": {"inputs": ["high", "low", "close"], "func": f07_lhll_060_pivot_high_hierarchy_atr_distance},
    "f07_lhll_061_pivot_low_hierarchy_atr_distance": {"inputs": ["high", "low", "close"], "func": f07_lhll_061_pivot_low_hierarchy_atr_distance},
    "f07_lhll_062_hierarchy_pivot_high_below_count_252d": {"inputs": ["high"], "func": f07_lhll_062_hierarchy_pivot_high_below_count_252d},
    "f07_lhll_063_hierarchy_pivot_low_below_count_252d": {"inputs": ["low"], "func": f07_lhll_063_hierarchy_pivot_low_below_count_252d},
    "f07_lhll_064_bars_since_last_new_alltime_high": {"inputs": ["high"], "func": f07_lhll_064_bars_since_last_new_alltime_high},
    "f07_lhll_065_bars_since_last_higher_low_pivot21": {"inputs": ["low"], "func": f07_lhll_065_bars_since_last_higher_low_pivot21},
    "f07_lhll_066_consecutive_down_swings_count_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_066_consecutive_down_swings_count_pivot10},
    "f07_lhll_067_most_recent_swing_direction_indicator_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_067_most_recent_swing_direction_indicator_pivot10},
    "f07_lhll_068_time_since_pivot10_high_minus_time_since_pivot10_low": {"inputs": ["high", "low"], "func": f07_lhll_068_time_since_pivot10_high_minus_time_since_pivot10_low},
    "f07_lhll_069_consecutive_higher_lows_count_pivot10": {"inputs": ["low"], "func": f07_lhll_069_consecutive_higher_lows_count_pivot10},
    "f07_lhll_070_pivot_low_slope_sign_agreement_5_vs_21": {"inputs": ["low"], "func": f07_lhll_070_pivot_low_slope_sign_agreement_5_vs_21},
    "f07_lhll_071_pivot_high_slope_sign_agreement_5_vs_21": {"inputs": ["high"], "func": f07_lhll_071_pivot_high_slope_sign_agreement_5_vs_21},
    "f07_lhll_072_pivot_slope_cross_axis_agreement_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_072_pivot_slope_cross_axis_agreement_pivot10},
    "f07_lhll_073_pivot_low_slope_diff_5_minus_21": {"inputs": ["low"], "func": f07_lhll_073_pivot_low_slope_diff_5_minus_21},
    "f07_lhll_074_pivot_high_slope_diff_5_minus_21": {"inputs": ["high"], "func": f07_lhll_074_pivot_high_slope_diff_5_minus_21},
    "f07_lhll_075_dow_full_breakdown_composite_pivot10": {"inputs": ["high", "low"], "func": f07_lhll_075_dow_full_breakdown_composite_pivot10},
}
