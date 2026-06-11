"""td_sequential_demark d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py — built around the
DeMark TD Sequential framework: TD Sell/Buy Setup counts, perfected setups, TD
countdowns (Combo / Aggressive variants), TDST support/resistance, TD Pressure, TD
REI, TD Camouflage / Open / Trap / Differential bar patterns, and topping-pressure
composites.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


# ---------------------------- TD setup helpers ----------------------------

def _td_sell_setup_count(close: pd.Series) -> pd.Series:
    """Running TD sell-setup count: increments on close > close[t-4], resets to 0 otherwise.
    Vectorized via groupby+cumsum — no Python loop."""
    qual = (close > close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    """Running TD buy-setup count: increments on close < close[t-4]."""
    qual = (close < close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_perfected_sell_setup_9_event(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on the bar where a TD sell setup completes (count==9) AND it is 'perfected':
    high of bar 8 OR bar 9 is >= max(high of bar 6, high of bar 7)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    h6 = high.shift(3); h7 = high.shift(2); h8 = high.shift(1); h9 = high
    bar_max = pd.concat([h6, h7], axis=1).max(axis=1)
    perfected = ((h8 >= bar_max) | (h9 >= bar_max)).astype(float)
    return (fires * perfected).where(sc.notna(), np.nan)


def _td_sell_countdown_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD sell-countdown count series. State machine:
    - Inactive until a TD sell setup-9 completes.
    - Increments on bars where close >= high[t-2]; cap at 13.
    - Resets on TD buy setup-9 completion (invalidation).
    - After hitting 13, stays at 13 until invalidation (so 'count==13' is queryable post-event).
    Implemented as O(n) state loop."""
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


def _td_buy_countdown_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD buy-countdown count (symmetric to sell): close <= low[t-2]; reset on sell-setup-9."""
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values; lo = low.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and bc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and sc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and cl[i] <= lo[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _td_aggressive_sell_countdown_count(close: pd.Series, high: pd.Series) -> pd.Series:
    """Aggressive TD sell countdown: uses high (instead of close) ≥ high[t-2]."""
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and hi[i] >= hi[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _td_sell_combo_count(close: pd.Series, high: pd.Series) -> pd.Series:
    """TD Combo (stricter): same as sell countdown but requires CONSECUTIVE qualifying bars after a setup-9."""
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
        if active and i >= 2:
            qual = (cl[i] >= hi[i - 2])
            if qual and cnt < 13:
                cnt += 1
            elif not qual:
                cnt = 0
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _tdst_buy_resistance(close: pd.Series, high: pd.Series) -> pd.Series:
    """TDST Buy Resistance: highest high during the most recent COMPLETED buy setup
    (count went from rising to reset at the bar following count==9)."""
    bc = _td_buy_setup_count(close).values
    hi = high.values
    n = len(close)
    out = np.full(n, np.nan)
    current_setup_max = np.nan; in_setup = False; setup_start = -1
    last_resistance = np.nan
    for i in range(n):
        if bc[i] == 1:
            in_setup = True; setup_start = i; current_setup_max = hi[i]
        elif in_setup and bc[i] > bc[i - 1] if i > 0 else False:
            current_setup_max = max(current_setup_max, hi[i])
        if in_setup and i > 0 and bc[i] == 0:
            # setup just ended; finalize if it reached at least 9
            if bc[i - 1] >= 9:
                last_resistance = current_setup_max
            in_setup = False
        out[i] = last_resistance
    return pd.Series(out, index=close.index)


def _tdst_sell_support(close: pd.Series, low: pd.Series) -> pd.Series:
    """TDST Sell Support: lowest low during the most recent COMPLETED sell setup."""
    sc = _td_sell_setup_count(close).values
    lo = low.values
    n = len(close)
    out = np.full(n, np.nan)
    current_setup_min = np.nan; in_setup = False
    last_support = np.nan
    for i in range(n):
        if sc[i] == 1:
            in_setup = True; current_setup_min = lo[i]
        elif in_setup and i > 0 and sc[i] > sc[i - 1]:
            current_setup_min = min(current_setup_min, lo[i])
        if in_setup and i > 0 and sc[i] == 0:
            if sc[i - 1] >= 9:
                last_support = current_setup_min
            in_setup = False
        out[i] = last_support
    return pd.Series(out, index=close.index)


def _td_pressure(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, n: int = 13) -> pd.Series:
    """TD Pressure: rolling sum of (close - open) / (high - low) over n bars,
    normalized by sum of (high - low) over same window."""
    body = (close - open_)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     rng.rolling(n, min_periods=max(n // 3, 2)).sum())


# ============================================================
# Bucket A — Setup count state (001-015)
# ============================================================

def f34_tdsq_001_td_sell_setup_count_current(close: pd.Series) -> pd.Series:
    """Current running TD sell-setup count (0..N)."""
    return _td_sell_setup_count(close)


def f34_tdsq_002_td_buy_setup_count_current(close: pd.Series) -> pd.Series:
    """Current running TD buy-setup count."""
    return _td_buy_setup_count(close)


def f34_tdsq_003_td_sell_setup_max_in_21d(close: pd.Series) -> pd.Series:
    """Max TD sell-setup count over trailing 21d — recent peak exhaustion intensity."""
    return _td_sell_setup_count(close).rolling(MDAYS, min_periods=WDAYS).max()


def f34_tdsq_004_td_sell_setup_max_in_63d(close: pd.Series) -> pd.Series:
    """Max TD sell-setup count over trailing 63d."""
    return _td_sell_setup_count(close).rolling(QDAYS, min_periods=MDAYS).max()


def f34_tdsq_005_td_sell_setup_max_in_252d(close: pd.Series) -> pd.Series:
    """Max TD sell-setup count over trailing 252d — secular exhaustion intensity."""
    return _td_sell_setup_count(close).rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_006_td_sell_setup_9_fires_today_indicator(close: pd.Series) -> pd.Series:
    """+1 on the bar where TD sell-setup count == 9 (setup completion)."""
    sc = _td_sell_setup_count(close)
    return (sc == 9).astype(float).where(sc.notna(), np.nan)


def f34_tdsq_007_td_perfected_sell_setup_9_fires_today_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on the bar where a *perfected* TD sell-setup-9 fires."""
    return _td_perfected_sell_setup_9_event(close, high)


def f34_tdsq_008_td_buy_setup_9_fires_today_indicator(close: pd.Series) -> pd.Series:
    """+1 on the bar where TD buy-setup count == 9."""
    bc = _td_buy_setup_count(close)
    return (bc == 9).astype(float).where(bc.notna(), np.nan)


def f34_tdsq_009_days_since_last_td_sell_setup_9(close: pd.Series) -> pd.Series:
    """Bars since the most recent TD sell-setup-9."""
    return _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))


def f34_tdsq_010_days_since_last_perfected_td_sell_setup_9(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since the most recent *perfected* TD sell-setup-9."""
    return _bars_since_true(_td_perfected_sell_setup_9_event(close, high))


def f34_tdsq_011_count_td_sell_setup_9_in_252d(close: pd.Series) -> pd.Series:
    """Count of TD sell-setup-9 fires within trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return fires.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_012_count_td_sell_setup_9_in_504d(close: pd.Series) -> pd.Series:
    """Count of TD sell-setup-9 fires within trailing 504d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return fires.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f34_tdsq_013_ratio_td_sell_to_buy_setup_count_252d(close: pd.Series) -> pd.Series:
    """Asymmetry: count of sell-setup-9 / count of buy-setup-9, trailing 252d (NaN-safe)."""
    s = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    b = (_td_buy_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(s, b)


def f34_tdsq_014_td_sell_setup_active_indicator(close: pd.Series) -> pd.Series:
    """+1 when the current TD sell-setup count > 0 (mid-setup state)."""
    sc = _td_sell_setup_count(close)
    return (sc > 0).astype(float).where(sc.notna(), np.nan)


def f34_tdsq_015_td_sell_setup_progress_pct(close: pd.Series) -> pd.Series:
    """Current TD sell-setup count divided by 9 (progress fraction; values > 1 = post-9 streak)."""
    return _td_sell_setup_count(close) / 9.0


# ============================================================
# Bucket B — Setup-at-stretch composites (016-025)
# ============================================================

def f34_tdsq_016_td_sell_setup_9_x_252d_high_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 if sell-setup-9 fires AND close within 1% of trailing 252d max."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fires * near).where(fires.notna(), np.nan)


def f34_tdsq_017_td_sell_setup_9_x_504d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 if sell-setup-9 fires AND close within 1.5% of trailing 504d max."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(DDAYS_2Y, min_periods=YDAYS).max() * 0.985).astype(float)
    return (fires * near).where(fires.notna(), np.nan)


def f34_tdsq_018_td_sell_setup_9_x_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 if sell-setup-9 fires AND close within 2% of trailing 1260d (5y) max."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fires * near).where(fires.notna(), np.nan)


def f34_tdsq_019_perfected_td_sell_setup_x_252d_high_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 if perfected sell-setup-9 fires AND close within 1% of 252d max."""
    pf = _td_perfected_sell_setup_9_event(close, high)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (pf * near).where(pf.notna(), np.nan)


def f34_tdsq_020_td_sell_setup_count_max_at_252d_high(close: pd.Series) -> pd.Series:
    """Max TD sell-setup count restricted to bars at/near trailing 252d high (else NaN, ffilled)."""
    sc = _td_sell_setup_count(close)
    near = close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99
    return sc.where(near, np.nan).ffill().rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_021_setup_9_density_at_252d_high_fraction(close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d setup-9 fires that occurred WHILE close near 252d high."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    total = fires.rolling(YDAYS, min_periods=QDAYS).sum()
    at_high = (fires * near).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(at_high, total)


def f34_tdsq_022_days_since_setup_9_x_at_high(close: pd.Series) -> pd.Series:
    """Bars since last (sell-setup-9 AND near-252d-high) conjunction."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return _bars_since_true(fires * near)


def f34_tdsq_023_setup_9_fires_within_5d_of_252d_high(close: pd.Series) -> pd.Series:
    """+1 if a sell-setup-9 fired within last 5 bars AND close near 252d high today."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    recent = fires.rolling(WDAYS, min_periods=1).max()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (recent * near).where(fires.notna() & near.notna(), np.nan)


def f34_tdsq_024_setup_9_in_21d_x_in_5pct_of_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 if sell-setup-9 fired in last 21 bars AND close within 5% of 252d max."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    recent = (fires.rolling(MDAYS, min_periods=1).sum() > 0).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.95).astype(float)
    return (recent * near).where(fires.notna() & near.notna(), np.nan)


def f34_tdsq_025_setup_9_at_log_dist_from_252d_max(close: pd.Series) -> pd.Series:
    """Log-distance close-to-252d-max at the bar of the most recent sell-setup-9 (held forward).
    Negative or zero — magnitude indicates how far below max the setup-9 fired."""
    sc = _td_sell_setup_count(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_log(close) - _safe_log(rmax)
    return dist.where(sc == 9, np.nan).ffill()


# ============================================================
# Bucket C — Setup persistence / streak (026-035)
# ============================================================

def f34_tdsq_026_td_sell_setup_streak_length_above_5(close: pd.Series) -> pd.Series:
    """Number of consecutive bars in current setup where count > 5 (post-mid-setup persistence)."""
    sc = _td_sell_setup_count(close)
    flag = (sc > 5).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f34_tdsq_027_setup_9_velocity_per_day_21d(close: pd.Series) -> pd.Series:
    """Setup-9 fires per day over trailing 21d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return fires.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS


def f34_tdsq_028_setup_9_velocity_per_day_63d(close: pd.Series) -> pd.Series:
    """Setup-9 fires per day over trailing 63d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return fires.rolling(QDAYS, min_periods=MDAYS).sum() / QDAYS


def f34_tdsq_029_setup_9_velocity_per_day_252d(close: pd.Series) -> pd.Series:
    """Setup-9 fires per day over trailing 252d — annual baseline rate."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return fires.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS


def f34_tdsq_030_setup_9_velocity_acceleration_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Velocity-21d minus velocity-63d — acute acceleration of setup-9 frequency."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    v21 = fires.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS
    v63 = fires.rolling(QDAYS, min_periods=MDAYS).sum() / QDAYS
    return v21 - v63


def f34_tdsq_031_time_in_setup_state_above_5_in_63d(close: pd.Series) -> pd.Series:
    """Count of trailing-63d bars where TD sell-setup count >= 5."""
    sc = _td_sell_setup_count(close)
    flag = (sc >= 5).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f34_tdsq_032_time_in_setup_completion_state_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where TD sell-setup count == 9."""
    sc = _td_sell_setup_count(close)
    flag = (sc == 9).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_033_longest_consecutive_setup_active_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-bar streak (in trailing 252d) where setup-count > 0."""
    sc = _td_sell_setup_count(close)
    flag = (sc > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_034_median_setup_9_event_gap_252d(close: pd.Series) -> pd.Series:
    """Median bar-gap between consecutive setup-9 events in trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(int)
    idx = pd.Series(np.arange(len(fires)), index=fires.index)
    last_fire_idx = idx.where(fires == 1, np.nan).ffill()
    gap = idx - last_fire_idx
    return gap.where(fires == 1, np.nan).rolling(YDAYS, min_periods=QDAYS).median()


def f34_tdsq_035_std_setup_9_event_gap_252d(close: pd.Series) -> pd.Series:
    """Std deviation of inter-setup-9 gap lengths over trailing 252d (irregularity)."""
    fires = (_td_sell_setup_count(close) == 9).astype(int)
    idx = pd.Series(np.arange(len(fires)), index=fires.index)
    last_fire_idx = idx.where(fires == 1, np.nan).ffill()
    gap = idx - last_fire_idx
    return gap.where(fires == 1, np.nan).rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket D — Countdown state (036-050)
# ============================================================

def f34_tdsq_036_td_sell_countdown_count_current(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current running TD sell-countdown count (0..13)."""
    return _td_sell_countdown_count(close, high, low)


def f34_tdsq_037_td_buy_countdown_count_current(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current running TD buy-countdown count (0..13)."""
    return _td_buy_countdown_count(close, high, low)


def f34_tdsq_038_td_sell_countdown_active_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD sell-countdown is in active state (count > 0 and not yet capped at 13)."""
    cd = _td_sell_countdown_count(close, high, low)
    return ((cd > 0) & (cd < 13)).astype(float).where(cd.notna(), np.nan)


def f34_tdsq_039_td_sell_countdown_13_fires_today_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on the bar where TD sell-countdown transitions from <13 to 13 (signal completion)."""
    cd = _td_sell_countdown_count(close, high, low)
    return ((cd == 13) & (cd.shift(1) < 13)).astype(float).where(cd.notna() & cd.shift(1).notna(), np.nan)


def f34_tdsq_040_days_since_last_td_sell_countdown_13(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the most recent TD sell-countdown-13 completion."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _bars_since_true(fire)


def f34_tdsq_041_count_sell_countdown_13_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD sell-countdown-13 events within trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return fire.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_042_count_sell_countdown_13_in_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD sell-countdown-13 events within trailing 504d."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return fire.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f34_tdsq_043_aggressive_sell_countdown_count_current(close: pd.Series, high: pd.Series) -> pd.Series:
    """Current Aggressive TD sell-countdown count (high ≥ high[t-2])."""
    return _td_aggressive_sell_countdown_count(close, high)


def f34_tdsq_044_aggressive_sell_countdown_13_fires_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where Aggressive countdown hits 13 (completes)."""
    cd = _td_aggressive_sell_countdown_count(close, high)
    return ((cd == 13) & (cd.shift(1) < 13)).astype(float).where(cd.notna() & cd.shift(1).notna(), np.nan)


def f34_tdsq_045_countdown_progress_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current sell-countdown count divided by 13 (progress fraction)."""
    return _td_sell_countdown_count(close, high, low) / 13.0


def f34_tdsq_046_countdown_max_in_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max sell-countdown count over trailing 63d."""
    return _td_sell_countdown_count(close, high, low).rolling(QDAYS, min_periods=MDAYS).max()


def f34_tdsq_047_countdown_max_in_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max sell-countdown count over trailing 252d."""
    return _td_sell_countdown_count(close, high, low).rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_048_countdown_recycled_indicator_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where countdown reset from >0 to 0 (recycle/invalidation events)."""
    cd = _td_sell_countdown_count(close, high, low)
    reset = ((cd == 0) & (cd.shift(1) > 0)).astype(float)
    return reset.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_049_ratio_completed_to_started_countdowns_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: completed-13 events / countdown-starts within trailing 504d."""
    cd = _td_sell_countdown_count(close, high, low)
    completed = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    started = ((cd > 0) & (cd.shift(1) == 0)).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(completed, started)


def f34_tdsq_050_countdown_event_density_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Total countdown events (any state-change) in trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    changes = (cd != cd.shift(1)).astype(float)
    return changes.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket E — Setup + Countdown plurality (051-055)
# ============================================================

def f34_tdsq_051_td_signal_plurality_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of (setup-9 events + perfected-9 events + countdown-13 events) in trailing 252d."""
    s9 = (_td_sell_setup_count(close) == 9).astype(float)
    p9 = _td_perfected_sell_setup_9_event(close, high)
    cd = _td_sell_countdown_count(close, high, low)
    c13 = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return (s9.fillna(0) + p9.fillna(0) + c13.fillna(0)).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_052_td_topping_pressure_setup_x_countdown(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Weighted: 0.5*max_setup_count_in_21d / 9 + 0.5*current_countdown_count / 13."""
    sc_max = _td_sell_setup_count(close).rolling(MDAYS, min_periods=WDAYS).max() / 9.0
    cd = _td_sell_countdown_count(close, high, low) / 13.0
    return 0.5 * sc_max + 0.5 * cd


def f34_tdsq_053_setup_9_AND_countdown_active_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 if a setup-9 has fired AND the countdown is currently active simultaneously."""
    sc = (_td_sell_setup_count(close) == 9).astype(float)
    cd_active = ((_td_sell_countdown_count(close, high, low) > 0)).astype(float)
    return (sc * cd_active).where(sc.notna() & cd_active.notna(), np.nan)


def f34_tdsq_054_setup_active_AND_high_pressure_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-setup count > 5 AND TD pressure > 0.5 (overbought + high buying pressure)."""
    sc_active = (_td_sell_setup_count(close) > 5).astype(float)
    pr = _td_pressure(open, close, high, low, 13)
    return (sc_active * (pr > 0.5).astype(float)).where(pr.notna() & sc_active.notna(), np.nan)


def f34_tdsq_055_bars_since_either_setup_9_or_countdown_13(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the most recent setup-9 OR countdown-13 (whichever was more recent)."""
    s9 = (_td_sell_setup_count(close) == 9).astype(float)
    cd = _td_sell_countdown_count(close, high, low)
    c13 = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    either = ((s9 + c13) > 0).astype(float)
    return _bars_since_true(either)


# ============================================================
# Bucket F — TDST levels and breaks (056-065)
# ============================================================

def f34_tdsq_056_tdst_buy_setup_resistance_level(close: pd.Series, high: pd.Series) -> pd.Series:
    """TDST Buy Resistance level (highest high during the most recent completed buy setup)."""
    return _tdst_buy_resistance(close, high)


def f34_tdsq_057_tdst_sell_setup_support_level(close: pd.Series, low: pd.Series) -> pd.Series:
    """TDST Sell Support level (lowest low during the most recent completed sell setup)."""
    return _tdst_sell_support(close, low)


def f34_tdsq_058_close_above_tdst_buy_resistance_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when close > TDST buy-resistance level (resistance broken)."""
    r = _tdst_buy_resistance(close, high)
    return (close > r).astype(float).where(r.notna(), np.nan)


def f34_tdsq_059_close_below_tdst_sell_support_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close < TDST sell-support level (support broken)."""
    s = _tdst_sell_support(close, low)
    return (close < s).astype(float).where(s.notna(), np.nan)


def f34_tdsq_060_tdst_buy_break_event_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where close newly crosses above TDST buy-resistance (event, not state)."""
    r = _tdst_buy_resistance(close, high)
    return ((close > r) & (close.shift(1) <= r.shift(1))).astype(float).where(r.notna() & r.shift(1).notna(), np.nan)


def f34_tdsq_061_tdst_sell_break_event_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where close newly crosses below TDST sell-support."""
    s = _tdst_sell_support(close, low)
    return ((close < s) & (close.shift(1) >= s.shift(1))).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f34_tdsq_062_days_since_tdst_buy_break(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since most recent TDST buy-resistance break event."""
    r = _tdst_buy_resistance(close, high)
    fire = ((close > r) & (close.shift(1) <= r.shift(1))).astype(float)
    return _bars_since_true(fire)


def f34_tdsq_063_days_since_tdst_sell_break(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent TDST sell-support break event."""
    s = _tdst_sell_support(close, low)
    fire = ((close < s) & (close.shift(1) >= s.shift(1))).astype(float)
    return _bars_since_true(fire)


def f34_tdsq_064_distance_close_to_tdst_buy_resistance_atr_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - TDST_buy_resistance) / ATR21 — signed distance in ATR units."""
    r = _tdst_buy_resistance(close, high)
    return _safe_div(close - r, _atr(high, low, close, MDAYS))


def f34_tdsq_065_distance_close_to_tdst_sell_support_atr_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - TDST_sell_support) / ATR21 — positive = above support."""
    s = _tdst_sell_support(close, low)
    return _safe_div(close - s, _atr(high, low, close, MDAYS))


# ============================================================
# Bucket G — TD Pressure (066-075)
# ============================================================

def f34_tdsq_066_td_pressure_value_13d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Pressure (13d): rolling sum(close-open) / sum(high-low)."""
    return _td_pressure(open, close, high, low, 13)


def f34_tdsq_067_td_pressure_zscore_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 13d TD pressure over trailing 252d."""
    return _rolling_zscore(_td_pressure(open, close, high, low, 13), YDAYS)


def f34_tdsq_068_td_pressure_pct_rank_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 13d TD pressure in trailing 252d."""
    return _pct_rank(_td_pressure(open, close, high, low, 13), YDAYS)


def f34_tdsq_069_td_pressure_above_threshold_80pct_rank_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD pressure 252d-percentile rank > 0.80 (high buying pressure regime)."""
    pr = _pct_rank(_td_pressure(open, close, high, low, 13), YDAYS)
    return (pr > 0.80).astype(float).where(pr.notna(), np.nan)


def f34_tdsq_070_td_pressure_slope_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of TD pressure — directional change."""
    return _rolling_slope(_td_pressure(open, close, high, low, 13), MDAYS)


def f34_tdsq_071_td_pressure_overbought_persistence_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-21d bars where TD-pressure 252d-rank > 0.80."""
    pr = _pct_rank(_td_pressure(open, close, high, low, 13), YDAYS)
    flag = (pr > 0.80).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f34_tdsq_072_days_since_td_pressure_peak_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since TD pressure last printed its trailing-252d maximum."""
    pr = _td_pressure(open, close, high, low, 13)
    flag = (pr == pr.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag)


def f34_tdsq_073_td_pressure_at_252d_high_x_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD pressure z(252d) > 1.5 AND close within 1% of 252d max."""
    z = _rolling_zscore(_td_pressure(open, close, high, low, 13), YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((z > 1.5) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


def f34_tdsq_074_td_pressure_falling_at_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD pressure 21d-slope < 0 AND close within 2% of 252d max — pressure waning at high."""
    s = _rolling_slope(_td_pressure(open, close, high, low, 13), MDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.98).astype(float)
    return ((s < 0) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f34_tdsq_075_td_pressure_dispersion_zscore_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of rolling 21d std of TD pressure over 252d — pressure-volatility regime gauge."""
    pr = _td_pressure(open, close, high, low, 13)
    return _rolling_zscore(pr.rolling(MDAYS, min_periods=WDAYS).std(), YDAYS)


# ============================================================
# REGISTRY
# ============================================================



def f34_tdsq_001_td_sell_setup_count_current_d1(close):
    return f34_tdsq_001_td_sell_setup_count_current(close).diff()


def f34_tdsq_002_td_buy_setup_count_current_d1(close):
    return f34_tdsq_002_td_buy_setup_count_current(close).diff()


def f34_tdsq_003_td_sell_setup_max_in_21d_d1(close):
    return f34_tdsq_003_td_sell_setup_max_in_21d(close).diff()


def f34_tdsq_004_td_sell_setup_max_in_63d_d1(close):
    return f34_tdsq_004_td_sell_setup_max_in_63d(close).diff()


def f34_tdsq_005_td_sell_setup_max_in_252d_d1(close):
    return f34_tdsq_005_td_sell_setup_max_in_252d(close).diff()


def f34_tdsq_006_td_sell_setup_9_fires_today_indicator_d1(close):
    return f34_tdsq_006_td_sell_setup_9_fires_today_indicator(close).diff()


def f34_tdsq_007_td_perfected_sell_setup_9_fires_today_indicator_d1(close, high):
    return f34_tdsq_007_td_perfected_sell_setup_9_fires_today_indicator(close, high).diff()


def f34_tdsq_008_td_buy_setup_9_fires_today_indicator_d1(close):
    return f34_tdsq_008_td_buy_setup_9_fires_today_indicator(close).diff()


def f34_tdsq_009_days_since_last_td_sell_setup_9_d1(close):
    return f34_tdsq_009_days_since_last_td_sell_setup_9(close).diff()


def f34_tdsq_010_days_since_last_perfected_td_sell_setup_9_d1(close, high):
    return f34_tdsq_010_days_since_last_perfected_td_sell_setup_9(close, high).diff()


def f34_tdsq_011_count_td_sell_setup_9_in_252d_d1(close):
    return f34_tdsq_011_count_td_sell_setup_9_in_252d(close).diff()


def f34_tdsq_012_count_td_sell_setup_9_in_504d_d1(close):
    return f34_tdsq_012_count_td_sell_setup_9_in_504d(close).diff()


def f34_tdsq_013_ratio_td_sell_to_buy_setup_count_252d_d1(close):
    return f34_tdsq_013_ratio_td_sell_to_buy_setup_count_252d(close).diff()


def f34_tdsq_014_td_sell_setup_active_indicator_d1(close):
    return f34_tdsq_014_td_sell_setup_active_indicator(close).diff()


def f34_tdsq_015_td_sell_setup_progress_pct_d1(close):
    return f34_tdsq_015_td_sell_setup_progress_pct(close).diff()


def f34_tdsq_016_td_sell_setup_9_x_252d_high_indicator_d1(close, high):
    return f34_tdsq_016_td_sell_setup_9_x_252d_high_indicator(close, high).diff()


def f34_tdsq_017_td_sell_setup_9_x_504d_high_indicator_d1(close):
    return f34_tdsq_017_td_sell_setup_9_x_504d_high_indicator(close).diff()


def f34_tdsq_018_td_sell_setup_9_x_1260d_high_indicator_d1(close):
    return f34_tdsq_018_td_sell_setup_9_x_1260d_high_indicator(close).diff()


def f34_tdsq_019_perfected_td_sell_setup_x_252d_high_indicator_d1(close, high):
    return f34_tdsq_019_perfected_td_sell_setup_x_252d_high_indicator(close, high).diff()


def f34_tdsq_020_td_sell_setup_count_max_at_252d_high_d1(close):
    return f34_tdsq_020_td_sell_setup_count_max_at_252d_high(close).diff()


def f34_tdsq_021_setup_9_density_at_252d_high_fraction_d1(close):
    return f34_tdsq_021_setup_9_density_at_252d_high_fraction(close).diff()


def f34_tdsq_022_days_since_setup_9_x_at_high_d1(close):
    return f34_tdsq_022_days_since_setup_9_x_at_high(close).diff()


def f34_tdsq_023_setup_9_fires_within_5d_of_252d_high_d1(close):
    return f34_tdsq_023_setup_9_fires_within_5d_of_252d_high(close).diff()


def f34_tdsq_024_setup_9_in_21d_x_in_5pct_of_252d_high_indicator_d1(close):
    return f34_tdsq_024_setup_9_in_21d_x_in_5pct_of_252d_high_indicator(close).diff()


def f34_tdsq_025_setup_9_at_log_dist_from_252d_max_d1(close):
    return f34_tdsq_025_setup_9_at_log_dist_from_252d_max(close).diff()


def f34_tdsq_026_td_sell_setup_streak_length_above_5_d1(close):
    return f34_tdsq_026_td_sell_setup_streak_length_above_5(close).diff()


def f34_tdsq_027_setup_9_velocity_per_day_21d_d1(close):
    return f34_tdsq_027_setup_9_velocity_per_day_21d(close).diff()


def f34_tdsq_028_setup_9_velocity_per_day_63d_d1(close):
    return f34_tdsq_028_setup_9_velocity_per_day_63d(close).diff()


def f34_tdsq_029_setup_9_velocity_per_day_252d_d1(close):
    return f34_tdsq_029_setup_9_velocity_per_day_252d(close).diff()


def f34_tdsq_030_setup_9_velocity_acceleration_21d_vs_63d_d1(close):
    return f34_tdsq_030_setup_9_velocity_acceleration_21d_vs_63d(close).diff()


def f34_tdsq_031_time_in_setup_state_above_5_in_63d_d1(close):
    return f34_tdsq_031_time_in_setup_state_above_5_in_63d(close).diff()


def f34_tdsq_032_time_in_setup_completion_state_252d_d1(close):
    return f34_tdsq_032_time_in_setup_completion_state_252d(close).diff()


def f34_tdsq_033_longest_consecutive_setup_active_streak_252d_d1(close):
    return f34_tdsq_033_longest_consecutive_setup_active_streak_252d(close).diff()


def f34_tdsq_034_median_setup_9_event_gap_252d_d1(close):
    return f34_tdsq_034_median_setup_9_event_gap_252d(close).diff()


def f34_tdsq_035_std_setup_9_event_gap_252d_d1(close):
    return f34_tdsq_035_std_setup_9_event_gap_252d(close).diff()


def f34_tdsq_036_td_sell_countdown_count_current_d1(close, high, low):
    return f34_tdsq_036_td_sell_countdown_count_current(close, high, low).diff()


def f34_tdsq_037_td_buy_countdown_count_current_d1(close, high, low):
    return f34_tdsq_037_td_buy_countdown_count_current(close, high, low).diff()


def f34_tdsq_038_td_sell_countdown_active_indicator_d1(close, high, low):
    return f34_tdsq_038_td_sell_countdown_active_indicator(close, high, low).diff()


def f34_tdsq_039_td_sell_countdown_13_fires_today_indicator_d1(close, high, low):
    return f34_tdsq_039_td_sell_countdown_13_fires_today_indicator(close, high, low).diff()


def f34_tdsq_040_days_since_last_td_sell_countdown_13_d1(close, high, low):
    return f34_tdsq_040_days_since_last_td_sell_countdown_13(close, high, low).diff()


def f34_tdsq_041_count_sell_countdown_13_in_252d_d1(close, high, low):
    return f34_tdsq_041_count_sell_countdown_13_in_252d(close, high, low).diff()


def f34_tdsq_042_count_sell_countdown_13_in_504d_d1(close, high, low):
    return f34_tdsq_042_count_sell_countdown_13_in_504d(close, high, low).diff()


def f34_tdsq_043_aggressive_sell_countdown_count_current_d1(close, high):
    return f34_tdsq_043_aggressive_sell_countdown_count_current(close, high).diff()


def f34_tdsq_044_aggressive_sell_countdown_13_fires_indicator_d1(close, high):
    return f34_tdsq_044_aggressive_sell_countdown_13_fires_indicator(close, high).diff()


def f34_tdsq_045_countdown_progress_pct_d1(close, high, low):
    return f34_tdsq_045_countdown_progress_pct(close, high, low).diff()


def f34_tdsq_046_countdown_max_in_63d_d1(close, high, low):
    return f34_tdsq_046_countdown_max_in_63d(close, high, low).diff()


def f34_tdsq_047_countdown_max_in_252d_d1(close, high, low):
    return f34_tdsq_047_countdown_max_in_252d(close, high, low).diff()


def f34_tdsq_048_countdown_recycled_indicator_252d_d1(close, high, low):
    return f34_tdsq_048_countdown_recycled_indicator_252d(close, high, low).diff()


def f34_tdsq_049_ratio_completed_to_started_countdowns_504d_d1(close, high, low):
    return f34_tdsq_049_ratio_completed_to_started_countdowns_504d(close, high, low).diff()


def f34_tdsq_050_countdown_event_density_252d_d1(close, high, low):
    return f34_tdsq_050_countdown_event_density_252d(close, high, low).diff()


def f34_tdsq_051_td_signal_plurality_count_252d_d1(close, high, low):
    return f34_tdsq_051_td_signal_plurality_count_252d(close, high, low).diff()


def f34_tdsq_052_td_topping_pressure_setup_x_countdown_d1(close, high, low):
    return f34_tdsq_052_td_topping_pressure_setup_x_countdown(close, high, low).diff()


def f34_tdsq_053_setup_9_AND_countdown_active_indicator_d1(close, high, low):
    return f34_tdsq_053_setup_9_AND_countdown_active_indicator(close, high, low).diff()


def f34_tdsq_054_setup_active_AND_high_pressure_indicator_d1(open, close, high, low):
    return f34_tdsq_054_setup_active_AND_high_pressure_indicator(open, close, high, low).diff()


def f34_tdsq_055_bars_since_either_setup_9_or_countdown_13_d1(close, high, low):
    return f34_tdsq_055_bars_since_either_setup_9_or_countdown_13(close, high, low).diff()


def f34_tdsq_056_tdst_buy_setup_resistance_level_d1(close, high):
    return f34_tdsq_056_tdst_buy_setup_resistance_level(close, high).diff()


def f34_tdsq_057_tdst_sell_setup_support_level_d1(close, low):
    return f34_tdsq_057_tdst_sell_setup_support_level(close, low).diff()


def f34_tdsq_058_close_above_tdst_buy_resistance_indicator_d1(close, high):
    return f34_tdsq_058_close_above_tdst_buy_resistance_indicator(close, high).diff()


def f34_tdsq_059_close_below_tdst_sell_support_indicator_d1(close, low):
    return f34_tdsq_059_close_below_tdst_sell_support_indicator(close, low).diff()


def f34_tdsq_060_tdst_buy_break_event_indicator_d1(close, high):
    return f34_tdsq_060_tdst_buy_break_event_indicator(close, high).diff()


def f34_tdsq_061_tdst_sell_break_event_indicator_d1(close, low):
    return f34_tdsq_061_tdst_sell_break_event_indicator(close, low).diff()


def f34_tdsq_062_days_since_tdst_buy_break_d1(close, high):
    return f34_tdsq_062_days_since_tdst_buy_break(close, high).diff()


def f34_tdsq_063_days_since_tdst_sell_break_d1(close, low):
    return f34_tdsq_063_days_since_tdst_sell_break(close, low).diff()


def f34_tdsq_064_distance_close_to_tdst_buy_resistance_atr_norm_d1(close, high, low):
    return f34_tdsq_064_distance_close_to_tdst_buy_resistance_atr_norm(close, high, low).diff()


def f34_tdsq_065_distance_close_to_tdst_sell_support_atr_norm_d1(close, high, low):
    return f34_tdsq_065_distance_close_to_tdst_sell_support_atr_norm(close, high, low).diff()


def f34_tdsq_066_td_pressure_value_13d_d1(open, close, high, low):
    return f34_tdsq_066_td_pressure_value_13d(open, close, high, low).diff()


def f34_tdsq_067_td_pressure_zscore_252d_d1(open, close, high, low):
    return f34_tdsq_067_td_pressure_zscore_252d(open, close, high, low).diff()


def f34_tdsq_068_td_pressure_pct_rank_252d_d1(open, close, high, low):
    return f34_tdsq_068_td_pressure_pct_rank_252d(open, close, high, low).diff()


def f34_tdsq_069_td_pressure_above_threshold_80pct_rank_indicator_d1(open, close, high, low):
    return f34_tdsq_069_td_pressure_above_threshold_80pct_rank_indicator(open, close, high, low).diff()


def f34_tdsq_070_td_pressure_slope_21d_d1(open, close, high, low):
    return f34_tdsq_070_td_pressure_slope_21d(open, close, high, low).diff()


def f34_tdsq_071_td_pressure_overbought_persistence_21d_d1(open, close, high, low):
    return f34_tdsq_071_td_pressure_overbought_persistence_21d(open, close, high, low).diff()


def f34_tdsq_072_days_since_td_pressure_peak_252d_d1(open, close, high, low):
    return f34_tdsq_072_days_since_td_pressure_peak_252d(open, close, high, low).diff()


def f34_tdsq_073_td_pressure_at_252d_high_x_indicator_d1(open, close, high, low):
    return f34_tdsq_073_td_pressure_at_252d_high_x_indicator(open, close, high, low).diff()


def f34_tdsq_074_td_pressure_falling_at_high_indicator_d1(open, close, high, low):
    return f34_tdsq_074_td_pressure_falling_at_high_indicator(open, close, high, low).diff()


def f34_tdsq_075_td_pressure_dispersion_zscore_252d_d1(open, close, high, low):
    return f34_tdsq_075_td_pressure_dispersion_zscore_252d(open, close, high, low).diff()


TD_SEQUENTIAL_DEMARK_D1_REGISTRY_001_075 = {
    "f34_tdsq_001_td_sell_setup_count_current_d1": {"inputs": ["close"], "func": f34_tdsq_001_td_sell_setup_count_current_d1},
    "f34_tdsq_002_td_buy_setup_count_current_d1": {"inputs": ["close"], "func": f34_tdsq_002_td_buy_setup_count_current_d1},
    "f34_tdsq_003_td_sell_setup_max_in_21d_d1": {"inputs": ["close"], "func": f34_tdsq_003_td_sell_setup_max_in_21d_d1},
    "f34_tdsq_004_td_sell_setup_max_in_63d_d1": {"inputs": ["close"], "func": f34_tdsq_004_td_sell_setup_max_in_63d_d1},
    "f34_tdsq_005_td_sell_setup_max_in_252d_d1": {"inputs": ["close"], "func": f34_tdsq_005_td_sell_setup_max_in_252d_d1},
    "f34_tdsq_006_td_sell_setup_9_fires_today_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_006_td_sell_setup_9_fires_today_indicator_d1},
    "f34_tdsq_007_td_perfected_sell_setup_9_fires_today_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_007_td_perfected_sell_setup_9_fires_today_indicator_d1},
    "f34_tdsq_008_td_buy_setup_9_fires_today_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_008_td_buy_setup_9_fires_today_indicator_d1},
    "f34_tdsq_009_days_since_last_td_sell_setup_9_d1": {"inputs": ["close"], "func": f34_tdsq_009_days_since_last_td_sell_setup_9_d1},
    "f34_tdsq_010_days_since_last_perfected_td_sell_setup_9_d1": {"inputs": ["close", "high"], "func": f34_tdsq_010_days_since_last_perfected_td_sell_setup_9_d1},
    "f34_tdsq_011_count_td_sell_setup_9_in_252d_d1": {"inputs": ["close"], "func": f34_tdsq_011_count_td_sell_setup_9_in_252d_d1},
    "f34_tdsq_012_count_td_sell_setup_9_in_504d_d1": {"inputs": ["close"], "func": f34_tdsq_012_count_td_sell_setup_9_in_504d_d1},
    "f34_tdsq_013_ratio_td_sell_to_buy_setup_count_252d_d1": {"inputs": ["close"], "func": f34_tdsq_013_ratio_td_sell_to_buy_setup_count_252d_d1},
    "f34_tdsq_014_td_sell_setup_active_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_014_td_sell_setup_active_indicator_d1},
    "f34_tdsq_015_td_sell_setup_progress_pct_d1": {"inputs": ["close"], "func": f34_tdsq_015_td_sell_setup_progress_pct_d1},
    "f34_tdsq_016_td_sell_setup_9_x_252d_high_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_016_td_sell_setup_9_x_252d_high_indicator_d1},
    "f34_tdsq_017_td_sell_setup_9_x_504d_high_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_017_td_sell_setup_9_x_504d_high_indicator_d1},
    "f34_tdsq_018_td_sell_setup_9_x_1260d_high_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_018_td_sell_setup_9_x_1260d_high_indicator_d1},
    "f34_tdsq_019_perfected_td_sell_setup_x_252d_high_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_019_perfected_td_sell_setup_x_252d_high_indicator_d1},
    "f34_tdsq_020_td_sell_setup_count_max_at_252d_high_d1": {"inputs": ["close"], "func": f34_tdsq_020_td_sell_setup_count_max_at_252d_high_d1},
    "f34_tdsq_021_setup_9_density_at_252d_high_fraction_d1": {"inputs": ["close"], "func": f34_tdsq_021_setup_9_density_at_252d_high_fraction_d1},
    "f34_tdsq_022_days_since_setup_9_x_at_high_d1": {"inputs": ["close"], "func": f34_tdsq_022_days_since_setup_9_x_at_high_d1},
    "f34_tdsq_023_setup_9_fires_within_5d_of_252d_high_d1": {"inputs": ["close"], "func": f34_tdsq_023_setup_9_fires_within_5d_of_252d_high_d1},
    "f34_tdsq_024_setup_9_in_21d_x_in_5pct_of_252d_high_indicator_d1": {"inputs": ["close"], "func": f34_tdsq_024_setup_9_in_21d_x_in_5pct_of_252d_high_indicator_d1},
    "f34_tdsq_025_setup_9_at_log_dist_from_252d_max_d1": {"inputs": ["close"], "func": f34_tdsq_025_setup_9_at_log_dist_from_252d_max_d1},
    "f34_tdsq_026_td_sell_setup_streak_length_above_5_d1": {"inputs": ["close"], "func": f34_tdsq_026_td_sell_setup_streak_length_above_5_d1},
    "f34_tdsq_027_setup_9_velocity_per_day_21d_d1": {"inputs": ["close"], "func": f34_tdsq_027_setup_9_velocity_per_day_21d_d1},
    "f34_tdsq_028_setup_9_velocity_per_day_63d_d1": {"inputs": ["close"], "func": f34_tdsq_028_setup_9_velocity_per_day_63d_d1},
    "f34_tdsq_029_setup_9_velocity_per_day_252d_d1": {"inputs": ["close"], "func": f34_tdsq_029_setup_9_velocity_per_day_252d_d1},
    "f34_tdsq_030_setup_9_velocity_acceleration_21d_vs_63d_d1": {"inputs": ["close"], "func": f34_tdsq_030_setup_9_velocity_acceleration_21d_vs_63d_d1},
    "f34_tdsq_031_time_in_setup_state_above_5_in_63d_d1": {"inputs": ["close"], "func": f34_tdsq_031_time_in_setup_state_above_5_in_63d_d1},
    "f34_tdsq_032_time_in_setup_completion_state_252d_d1": {"inputs": ["close"], "func": f34_tdsq_032_time_in_setup_completion_state_252d_d1},
    "f34_tdsq_033_longest_consecutive_setup_active_streak_252d_d1": {"inputs": ["close"], "func": f34_tdsq_033_longest_consecutive_setup_active_streak_252d_d1},
    "f34_tdsq_034_median_setup_9_event_gap_252d_d1": {"inputs": ["close"], "func": f34_tdsq_034_median_setup_9_event_gap_252d_d1},
    "f34_tdsq_035_std_setup_9_event_gap_252d_d1": {"inputs": ["close"], "func": f34_tdsq_035_std_setup_9_event_gap_252d_d1},
    "f34_tdsq_036_td_sell_countdown_count_current_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_036_td_sell_countdown_count_current_d1},
    "f34_tdsq_037_td_buy_countdown_count_current_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_037_td_buy_countdown_count_current_d1},
    "f34_tdsq_038_td_sell_countdown_active_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_038_td_sell_countdown_active_indicator_d1},
    "f34_tdsq_039_td_sell_countdown_13_fires_today_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_039_td_sell_countdown_13_fires_today_indicator_d1},
    "f34_tdsq_040_days_since_last_td_sell_countdown_13_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_040_days_since_last_td_sell_countdown_13_d1},
    "f34_tdsq_041_count_sell_countdown_13_in_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_041_count_sell_countdown_13_in_252d_d1},
    "f34_tdsq_042_count_sell_countdown_13_in_504d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_042_count_sell_countdown_13_in_504d_d1},
    "f34_tdsq_043_aggressive_sell_countdown_count_current_d1": {"inputs": ["close", "high"], "func": f34_tdsq_043_aggressive_sell_countdown_count_current_d1},
    "f34_tdsq_044_aggressive_sell_countdown_13_fires_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_044_aggressive_sell_countdown_13_fires_indicator_d1},
    "f34_tdsq_045_countdown_progress_pct_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_045_countdown_progress_pct_d1},
    "f34_tdsq_046_countdown_max_in_63d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_046_countdown_max_in_63d_d1},
    "f34_tdsq_047_countdown_max_in_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_047_countdown_max_in_252d_d1},
    "f34_tdsq_048_countdown_recycled_indicator_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_048_countdown_recycled_indicator_252d_d1},
    "f34_tdsq_049_ratio_completed_to_started_countdowns_504d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_049_ratio_completed_to_started_countdowns_504d_d1},
    "f34_tdsq_050_countdown_event_density_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_050_countdown_event_density_252d_d1},
    "f34_tdsq_051_td_signal_plurality_count_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_051_td_signal_plurality_count_252d_d1},
    "f34_tdsq_052_td_topping_pressure_setup_x_countdown_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_052_td_topping_pressure_setup_x_countdown_d1},
    "f34_tdsq_053_setup_9_AND_countdown_active_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_053_setup_9_AND_countdown_active_indicator_d1},
    "f34_tdsq_054_setup_active_AND_high_pressure_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_054_setup_active_AND_high_pressure_indicator_d1},
    "f34_tdsq_055_bars_since_either_setup_9_or_countdown_13_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_055_bars_since_either_setup_9_or_countdown_13_d1},
    "f34_tdsq_056_tdst_buy_setup_resistance_level_d1": {"inputs": ["close", "high"], "func": f34_tdsq_056_tdst_buy_setup_resistance_level_d1},
    "f34_tdsq_057_tdst_sell_setup_support_level_d1": {"inputs": ["close", "low"], "func": f34_tdsq_057_tdst_sell_setup_support_level_d1},
    "f34_tdsq_058_close_above_tdst_buy_resistance_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_058_close_above_tdst_buy_resistance_indicator_d1},
    "f34_tdsq_059_close_below_tdst_sell_support_indicator_d1": {"inputs": ["close", "low"], "func": f34_tdsq_059_close_below_tdst_sell_support_indicator_d1},
    "f34_tdsq_060_tdst_buy_break_event_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_060_tdst_buy_break_event_indicator_d1},
    "f34_tdsq_061_tdst_sell_break_event_indicator_d1": {"inputs": ["close", "low"], "func": f34_tdsq_061_tdst_sell_break_event_indicator_d1},
    "f34_tdsq_062_days_since_tdst_buy_break_d1": {"inputs": ["close", "high"], "func": f34_tdsq_062_days_since_tdst_buy_break_d1},
    "f34_tdsq_063_days_since_tdst_sell_break_d1": {"inputs": ["close", "low"], "func": f34_tdsq_063_days_since_tdst_sell_break_d1},
    "f34_tdsq_064_distance_close_to_tdst_buy_resistance_atr_norm_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_064_distance_close_to_tdst_buy_resistance_atr_norm_d1},
    "f34_tdsq_065_distance_close_to_tdst_sell_support_atr_norm_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_065_distance_close_to_tdst_sell_support_atr_norm_d1},
    "f34_tdsq_066_td_pressure_value_13d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_066_td_pressure_value_13d_d1},
    "f34_tdsq_067_td_pressure_zscore_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_067_td_pressure_zscore_252d_d1},
    "f34_tdsq_068_td_pressure_pct_rank_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_068_td_pressure_pct_rank_252d_d1},
    "f34_tdsq_069_td_pressure_above_threshold_80pct_rank_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_069_td_pressure_above_threshold_80pct_rank_indicator_d1},
    "f34_tdsq_070_td_pressure_slope_21d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_070_td_pressure_slope_21d_d1},
    "f34_tdsq_071_td_pressure_overbought_persistence_21d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_071_td_pressure_overbought_persistence_21d_d1},
    "f34_tdsq_072_days_since_td_pressure_peak_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_072_days_since_td_pressure_peak_252d_d1},
    "f34_tdsq_073_td_pressure_at_252d_high_x_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_073_td_pressure_at_252d_high_x_indicator_d1},
    "f34_tdsq_074_td_pressure_falling_at_high_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_074_td_pressure_falling_at_high_indicator_d1},
    "f34_tdsq_075_td_pressure_dispersion_zscore_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_075_td_pressure_dispersion_zscore_252d_d1},
}
