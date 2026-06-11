"""rsi_exhaustion_family d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Focus is on
RSI-based exhaustion at multi-year peaks. Differentiated from family 26
(stochastic_williams_family) and 32 (divergence_detection) by depth across
Wilder/Cutler/Connors variants, RSI-of-RSI, OB-exit dynamics, dwell, and
saturation/peak-decay measures specific to RSI.

Bucket A: Core RSI levels (Wilder & Cutler) at multi-horizons.
Bucket B: OB state at multiple thresholds and horizons.
Bucket C: OB-exit events / triggers / recency.
Bucket D: Dwell / persistence in OB.
Bucket E: Cumulative OB area / saturation / peak decay.
Bucket F: Bearish divergence (price up, RSI down).
Bucket G: RSI dynamics (slope, momentum, range).
Bucket H: Connors RSI components.
Bucket I: RSI-of-RSI (momentum of momentum).

Inputs: SEP close only. Self-contained helpers, PIT-clean.
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


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ---------- RSI variants ----------

def _rsi_wilder(close, n=14):
    """Wilder's RSI — EMA(alpha=1/n) of gains and losses."""
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_cutler(close, n=14):
    """Cutler's RSI — SMA of gains and losses (instead of EMA)."""
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.rolling(n, min_periods=max(n // 3, 2)).mean()
    ad = dn.rolling(n, min_periods=max(n // 3, 2)).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _up_down_streak(close):
    """Signed consecutive-streak length: positive for up-close runs, negative for down."""
    diff = close.diff()
    arr = diff.to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0.0
    for i in range(arr.size):
        x = arr[i]
        if np.isnan(x):
            c = 0.0
        elif x > 0:
            c = c + 1.0 if c >= 0 else 1.0
        elif x < 0:
            c = c - 1.0 if c <= 0 else -1.0
        else:
            c = 0.0
        out[i] = c
    return pd.Series(out, index=close.index)


def _percent_rank_return(close, n_ret=1, n_window=100):
    """Connors PercentRank: rank of (n_ret-bar return) within trailing n_window distribution."""
    r = close.pct_change(n_ret)
    return r.rolling(n_window, min_periods=max(n_window // 3, 5)).rank(pct=True) * 100.0


def _connors_rsi(close, n_rsi=3, n_streak=2, n_pr=100):
    """Connors RSI = average of {RSI(close, n_rsi), RSI(UD-streak, n_streak), PercentRank(100)}."""
    a = _rsi_wilder(close, n_rsi)
    streak = _up_down_streak(close)
    b = _rsi_wilder(streak, n_streak)
    c = _percent_rank_return(close, 1, n_pr)
    return (a + b + c) / 3.0


# ============================================================
# Bucket A — Core RSI levels at multi-horizons (001-008)
# ============================================================


def f25_rsxh_001_rsi_wilder_7_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(7) — short-horizon (distinct concept from RSI14)."""
    return (_rsi_wilder(close, 7)).diff().diff().diff()


def f25_rsxh_002_rsi_wilder_14_d3(close: pd.Series) -> pd.Series:
    """Classical Wilder RSI(14) — baseline."""
    return (_rsi_wilder(close, 14)).diff().diff().diff()


def f25_rsxh_003_rsi_wilder_21_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(21) — monthly horizon (distinct concept)."""
    return (_rsi_wilder(close, MDAYS)).diff().diff().diff()


def f25_rsxh_004_rsi_wilder_63_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(63) — quarterly horizon (distinct concept)."""
    return (_rsi_wilder(close, QDAYS)).diff().diff().diff()


def f25_rsxh_005_rsi_wilder_252_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(252) — annual horizon (distinct concept)."""
    return (_rsi_wilder(close, YDAYS)).diff().diff().diff()


def f25_rsxh_006_rsi_cutler_14_d3(close: pd.Series) -> pd.Series:
    """Cutler RSI(14) — SMA-based RSI (distinct from EMA-based Wilder)."""
    return (_rsi_cutler(close, 14)).diff().diff().diff()


def f25_rsxh_007_rsi_cutler_63_d3(close: pd.Series) -> pd.Series:
    """Cutler RSI(63) — quarterly SMA-RSI."""
    return (_rsi_cutler(close, QDAYS)).diff().diff().diff()


def f25_rsxh_008_rsi_cutler_252_d3(close: pd.Series) -> pd.Series:
    """Cutler RSI(252) — annual SMA-RSI."""
    return (_rsi_cutler(close, YDAYS)).diff().diff().diff()


def f25_rsxh_009_rsi14_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 70 — classical OB state."""
    r = _rsi_wilder(close, 14)
    return ((r > 70.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_010_rsi14_above_80_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 80 — strong OB (distinct severity)."""
    r = _rsi_wilder(close, 14)
    return ((r > 80.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_011_rsi14_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 90 — extreme OB (climax momentum)."""
    r = _rsi_wilder(close, 14)
    return ((r > 90.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_012_rsi63_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(63) > 70 — quarterly OB state."""
    r = _rsi_wilder(close, QDAYS)
    return ((r > 70.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_013_rsi252_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(252) > 70 — annual OB state."""
    r = _rsi_wilder(close, YDAYS)
    return ((r > 70.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_014_rsi14_above_95_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 95 — extreme-exhaustion threshold."""
    r = _rsi_wilder(close, 14)
    return ((r > 95.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_015_rsi14_above_q95_distribution_252_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > trailing 252d 95th-pct of itself — distribution-based OB."""
    r = _rsi_wilder(close, 14)
    q = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return ((r > q).astype(float).where(r.notna() & q.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_016_rsi14_above_q99_distribution_252_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 252d 99th-pct of itself — extreme distribution OB."""
    r = _rsi_wilder(close, 14)
    q = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return ((r > q).astype(float).where(r.notna() & q.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_017_rsi14_at_252d_max_flag_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) equals its 252d max this bar — RSI peak event."""
    r = _rsi_wilder(close, 14)
    return ((r == r.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_018_rsi14_just_exited_ob70_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) was > 70 prior bar and <= 70 this bar — classical OB70 exit trigger."""
    r = _rsi_wilder(close, 14)
    return (((r.shift(1) > 70.0) & (r <= 70.0)).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_019_rsi14_just_exited_ob80_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) just exited OB80 — strong-momentum cooling."""
    r = _rsi_wilder(close, 14)
    return (((r.shift(1) > 80.0) & (r <= 80.0)).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_020_rsi14_just_exited_ob90_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) just exited OB90 — extreme-momentum reset."""
    r = _rsi_wilder(close, 14)
    return (((r.shift(1) > 90.0) & (r <= 90.0)).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_021_bars_since_rsi14_ob70_exit_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent RSI(14) OB70 exit — recency of bearish RSI trigger."""
    r = _rsi_wilder(close, 14)
    ev = (r.shift(1) > 70.0) & (r <= 70.0)
    return (_bars_since_true(ev)).diff().diff().diff()


def f25_rsxh_022_bars_since_rsi14_ob80_exit_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent RSI(14) OB80 exit."""
    r = _rsi_wilder(close, 14)
    ev = (r.shift(1) > 80.0) & (r <= 80.0)
    return (_bars_since_true(ev)).diff().diff().diff()


def f25_rsxh_023_count_rsi14_ob70_exits_63_d3(close: pd.Series) -> pd.Series:
    """Count of RSI(14) OB70 exits past 63 — exit-density (quarterly)."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) > 70.0) & (r <= 70.0)).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_024_count_rsi14_ob70_exits_252_d3(close: pd.Series) -> pd.Series:
    """Annual count of RSI(14) OB70 exits."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) > 70.0) & (r <= 70.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_025_count_rsi14_ob80_exits_252_d3(close: pd.Series) -> pd.Series:
    """Annual count of RSI(14) OB80 exits — strong-OB churn density."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) > 80.0) & (r <= 80.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_026_rsi_exit_velocity_drop_from_peak_21_d3(close: pd.Series) -> pd.Series:
    """At OB70 exit: (21d max RSI) - RSI — magnitude of collapse from peak. NaN elsewhere."""
    r = _rsi_wilder(close, 14)
    ev = (r.shift(1) > 70.0) & (r <= 70.0)
    peak = r.rolling(MDAYS, min_periods=WDAYS).max()
    return ((peak - r).where(ev, np.nan)).diff().diff().diff()


def f25_rsxh_027_rsi_failed_retest_lower_peak_63_d3(close: pd.Series) -> pd.Series:
    """At OB70-exit: 1 if 63d RSI max is lower than 63d-ago RSI max — failed retest (lower OB peak)."""
    r = _rsi_wilder(close, 14)
    rmax = r.rolling(QDAYS, min_periods=MDAYS).max()
    prev_rmax = rmax.shift(MDAYS)
    just_exited = (r.shift(1) > 70.0) & (r <= 70.0)
    failed = (rmax < prev_rmax).astype(float)
    return (failed.where(just_exited & rmax.notna() & prev_rmax.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_028_fraction_rsi14_ob70_past_21_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 21 bars RSI(14) > 70 — monthly OB dwell."""
    r = _rsi_wilder(close, 14)
    return ((r > 70.0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_029_fraction_rsi14_ob70_past_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars RSI(14) > 70 — quarterly OB dwell."""
    r = _rsi_wilder(close, 14)
    return ((r > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_030_fraction_rsi14_ob70_past_252_d3(close: pd.Series) -> pd.Series:
    """Annual fraction of bars RSI(14) > 70 — saturation index."""
    r = _rsi_wilder(close, 14)
    return ((r > 70.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_031_fraction_rsi14_ob80_past_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars RSI(14) > 80 — strong-OB dwell."""
    r = _rsi_wilder(close, 14)
    return ((r > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_032_fraction_rsi14_ob80_past_252_d3(close: pd.Series) -> pd.Series:
    """Annual fraction RSI(14) > 80 — annual strong-OB dwell."""
    r = _rsi_wilder(close, 14)
    return ((r > 80.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_033_longest_rsi14_ob70_run_252_d3(close: pd.Series) -> pd.Series:
    """Longest consecutive run of RSI(14) > 70 in past 252 bars."""
    r = _rsi_wilder(close, 14)
    streak = _streak_true(r > 70.0)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_034_current_rsi14_ob70_streak_d3(close: pd.Series) -> pd.Series:
    """Current consecutive run of RSI(14) > 70 — live OB-streak length."""
    r = _rsi_wilder(close, 14)
    return (_streak_true(r > 70.0).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_035_distinct_ob70_sessions_252_d3(close: pd.Series) -> pd.Series:
    """Count of distinct OB70-session entries past 252 — # separate OB episodes."""
    r = _rsi_wilder(close, 14)
    entered = ((r.shift(1) <= 70.0) & (r > 70.0)).astype(float)
    return (entered.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_036_avg_ob70_session_duration_252_d3(close: pd.Series) -> pd.Series:
    """Avg OB70 session duration past 252 = (time-in-OB) / (#sessions)."""
    r = _rsi_wilder(close, 14)
    in_ob = (r > 70.0).astype(float)
    entered = ((r.shift(1) <= 70.0) & (r > 70.0)).astype(float)
    num = in_ob.rolling(YDAYS, min_periods=QDAYS).sum()
    den = entered.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(num, den).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_037_cumulative_ob70_area_252_d3(close: pd.Series) -> pd.Series:
    """Sum of (RSI - 70) over OB70 bars past 252 — RSI saturation intensity."""
    r = _rsi_wilder(close, 14)
    area = (r - 70.0).clip(lower=0).where(r.notna(), np.nan)
    return (area.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f25_rsxh_038_cumulative_ob80_area_252_d3(close: pd.Series) -> pd.Series:
    """Sum of (RSI - 80) over OB80 bars past 252 — strong-OB saturation."""
    r = _rsi_wilder(close, 14)
    area = (r - 80.0).clip(lower=0).where(r.notna(), np.nan)
    return (area.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f25_rsxh_039_cumulative_ob90_area_252_d3(close: pd.Series) -> pd.Series:
    """Sum of (RSI - 90) over OB90 bars past 252 — extreme-OB saturation."""
    r = _rsi_wilder(close, 14)
    area = (r - 90.0).clip(lower=0).where(r.notna(), np.nan)
    return (area.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f25_rsxh_040_max_rsi_minus_70_past_252_d3(close: pd.Series) -> pd.Series:
    """Max (RSI - 70) in past 252 — peak OB amplitude."""
    r = _rsi_wilder(close, 14)
    return ((r - 70.0).rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f25_rsxh_041_rsi_peak_decay_63_d3(close: pd.Series) -> pd.Series:
    """63d max of RSI minus its value 63 bars ago — quarterly RSI-peak decay."""
    r = _rsi_wilder(close, 14)
    pmax = r.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff().diff()


def f25_rsxh_042_rsi_peak_decay_252_d3(close: pd.Series) -> pd.Series:
    """252d max of RSI minus its value 252 bars ago — annual RSI-peak decay."""
    r = _rsi_wilder(close, 14)
    pmax = r.rolling(YDAYS, min_periods=QDAYS).max()
    return (pmax - pmax.shift(YDAYS)).diff().diff().diff()


def f25_rsxh_043_price_vs_rsi14_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish RSI divergence: new 63d price high while RSI(14) < prior 63d RSI max."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & r_below).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_044_price_vs_rsi14_div_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon bearish RSI divergence (252d)."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r_below = r < r.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return ((p_new & r_below).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_045_count_bearish_rsi_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish RSI-div events in past 63."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = (p_new & r_below).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_046_count_bearish_rsi_div_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of bearish RSI-div events."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r_below = r < r.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = (p_new & r_below).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_047_bars_since_last_bearish_rsi_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent bearish RSI-div event (63d horizon)."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (_bars_since_true(p_new & r_below)).diff().diff().diff()


def f25_rsxh_048_rsi_div_amplitude_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """At RSI-div bars: amplitude = prior 63d RSI-max - RSI; brief ffill."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_max - r).where(p_new & (r < prior_max), np.nan)
    return (amp.ffill(limit=QDAYS)).diff().diff().diff()


def f25_rsxh_049_price_vs_rsi63_div_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using RSI(63) (slow oscillator) over 252d."""
    r = _rsi_wilder(close, QDAYS)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r_below = r < r.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return ((p_new & r_below).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_050_hidden_bearish_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish div: lower 63d price high AND lower 63d RSI high simultaneously — continuation-down signal."""
    r = _rsi_wilder(close, 14)
    p_lh = high < high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    r_lh = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_lh & r_lh).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_051_triple_bearish_div_within_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3+ bearish-RSI-div bars in past 63 — cluster of divergences (recurring weakness)."""
    r = _rsi_wilder(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = (p_new & r_below).astype(float)
    cnt = ev.rolling(QDAYS, min_periods=MDAYS).sum()
    return ((cnt >= 3).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_052_rsi_price_corr_63_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between RSI(14) and close — decoupling indicator."""
    r = _rsi_wilder(close, 14)
    return (close.rolling(QDAYS, min_periods=MDAYS).corr(r)).diff().diff().diff()


def f25_rsxh_053_rsi_slope_21_d3(close: pd.Series) -> pd.Series:
    """Rolling 21d slope of RSI(14) — monthly RSI trend."""
    return (_rolling_slope(_rsi_wilder(close, 14), MDAYS)).diff().diff().diff()


def f25_rsxh_054_rsi_slope_63_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d slope of RSI(14) — quarterly RSI trend."""
    return (_rolling_slope(_rsi_wilder(close, 14), QDAYS)).diff().diff().diff()


def f25_rsxh_055_rsi_slope_252_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d slope of RSI(14) — annual RSI trend."""
    return (_rolling_slope(_rsi_wilder(close, 14), YDAYS)).diff().diff().diff()


def f25_rsxh_056_rsi_cross_50_event_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) crossed below 50 this bar — bullish-to-bearish bias flip."""
    r = _rsi_wilder(close, 14)
    return (((r.shift(1) >= 50.0) & (r < 50.0)).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_057_rsi_below_50_dwell_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars RSI(14) < 50 — bearish-bias dwell."""
    r = _rsi_wilder(close, 14)
    return ((r < 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_058_rsi_cross_above_50_event_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) crossed above 50 this bar — context for cross-density."""
    r = _rsi_wilder(close, 14)
    return (((r.shift(1) <= 50.0) & (r > 50.0)).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_059_rsi_21d_range_d3(close: pd.Series) -> pd.Series:
    """21d max(RSI) - 21d min(RSI) — RSI oscillator range (monthly)."""
    r = _rsi_wilder(close, 14)
    return (r.rolling(MDAYS, min_periods=WDAYS).max() - r.rolling(MDAYS, min_periods=WDAYS).min()).diff().diff().diff()


def f25_rsxh_060_rsi_std_21_d3(close: pd.Series) -> pd.Series:
    """21d standard deviation of RSI — RSI oscillator volatility."""
    return (_rsi_wilder(close, 14).rolling(MDAYS, min_periods=WDAYS).std()).diff().diff().diff()


def f25_rsxh_061_connors_rsi_3_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(3) — used as Connors-RSI's first component."""
    return (_rsi_wilder(close, 3)).diff().diff().diff()


def f25_rsxh_062_connors_rsi_full_d3(close: pd.Series) -> pd.Series:
    """Connors RSI = avg of (RSI(3), RSI-of-UD-streak(2), PercentRank(100))."""
    return (_connors_rsi(close)).diff().diff().diff()


def f25_rsxh_063_ud_streak_signed_d3(close: pd.Series) -> pd.Series:
    """Signed up/down-close consecutive-streak length (positive=up, negative=down)."""
    return (_up_down_streak(close)).diff().diff().diff()


def f25_rsxh_064_up_streak_length_d3(close: pd.Series) -> pd.Series:
    """Current up-close streak length (positive part of UD streak)."""
    return (_up_down_streak(close).clip(lower=0)).diff().diff().diff()


def f25_rsxh_065_down_streak_length_d3(close: pd.Series) -> pd.Series:
    """Current down-close streak length (absolute value of negative UD streak)."""
    return ((-_up_down_streak(close)).clip(lower=0)).diff().diff().diff()


def f25_rsxh_066_percent_rank_return_1_over_100_d3(close: pd.Series) -> pd.Series:
    """PercentRank of 1-bar return over trailing 100 bars (Connors component)."""
    return (_percent_rank_return(close, 1, 100)).diff().diff().diff()


def f25_rsxh_067_connors_rsi_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if Connors RSI > 90 — Connors-strategy short-entry threshold."""
    c = _connors_rsi(close)
    return ((c > 90.0).astype(float).where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_068_bars_since_connors_rsi_ob90_exit_d3(close: pd.Series) -> pd.Series:
    """Bars since Connors RSI just dropped from > 90 to <= 90."""
    c = _connors_rsi(close)
    ev = (c.shift(1) > 90.0) & (c <= 90.0)
    return (_bars_since_true(ev)).diff().diff().diff()


def f25_rsxh_069_rsi_of_rsi_14_d3(close: pd.Series) -> pd.Series:
    """RSI(14) of RSI(14) — momentum-of-momentum oscillator level."""
    return (_rsi_wilder(_rsi_wilder(close, 14), 14)).diff().diff().diff()


def f25_rsxh_070_rsi_of_rsi_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI-of-RSI > 70 — momentum-of-momentum OB state."""
    rr = _rsi_wilder(_rsi_wilder(close, 14), 14)
    return ((rr > 70.0).astype(float).where(rr.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_071_rsi_of_rsi_just_exited_ob70_d3(close: pd.Series) -> pd.Series:
    """1 if RSI-of-RSI just crossed back below 70 — momentum-of-momentum OB-exit."""
    rr = _rsi_wilder(_rsi_wilder(close, 14), 14)
    return (((rr.shift(1) > 70.0) & (rr <= 70.0)).astype(float).where(rr.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_072_rsi_of_rsi_bearish_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using RSI-of-RSI as oscillator."""
    rr = _rsi_wilder(_rsi_wilder(close, 14), 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    rr_below = rr < rr.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & rr_below).astype(float).where(rr.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_073_rsi_of_rsi_dwell_ob70_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars RSI-of-RSI > 70 — momentum-of-momentum OB dwell."""
    rr = _rsi_wilder(_rsi_wilder(close, 14), 14)
    return ((rr > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(rr.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_074_rsi_of_rsi_peak_decay_63_d3(close: pd.Series) -> pd.Series:
    """63d max of RSI-of-RSI minus its value 63 bars ago — momentum-of-momentum peak decay."""
    rr = _rsi_wilder(_rsi_wilder(close, 14), 14)
    pmax = rr.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff().diff()


def f25_rsxh_075_rsi_of_rsi_zscore_252_d3(close: pd.Series) -> pd.Series:
    """Z-score of RSI-of-RSI vs trailing 252d distribution."""
    return (_rolling_zscore(_rsi_wilder(_rsi_wilder(close, 14), 14), YDAYS, min_periods=QDAYS)).diff().diff().diff()


# ============================================================
#                         REGISTRY 001-075 (d3)
# ============================================================

_HC = ["high", "close"]

RSI_EXHAUSTION_FAMILY_D3_REGISTRY_001_075 = {
    "f25_rsxh_001_rsi_wilder_7_d3": {"inputs": ["close"], "func": f25_rsxh_001_rsi_wilder_7_d3},
    "f25_rsxh_002_rsi_wilder_14_d3": {"inputs": ["close"], "func": f25_rsxh_002_rsi_wilder_14_d3},
    "f25_rsxh_003_rsi_wilder_21_d3": {"inputs": ["close"], "func": f25_rsxh_003_rsi_wilder_21_d3},
    "f25_rsxh_004_rsi_wilder_63_d3": {"inputs": ["close"], "func": f25_rsxh_004_rsi_wilder_63_d3},
    "f25_rsxh_005_rsi_wilder_252_d3": {"inputs": ["close"], "func": f25_rsxh_005_rsi_wilder_252_d3},
    "f25_rsxh_006_rsi_cutler_14_d3": {"inputs": ["close"], "func": f25_rsxh_006_rsi_cutler_14_d3},
    "f25_rsxh_007_rsi_cutler_63_d3": {"inputs": ["close"], "func": f25_rsxh_007_rsi_cutler_63_d3},
    "f25_rsxh_008_rsi_cutler_252_d3": {"inputs": ["close"], "func": f25_rsxh_008_rsi_cutler_252_d3},
    "f25_rsxh_009_rsi14_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_009_rsi14_above_70_state_d3},
    "f25_rsxh_010_rsi14_above_80_state_d3": {"inputs": ["close"], "func": f25_rsxh_010_rsi14_above_80_state_d3},
    "f25_rsxh_011_rsi14_above_90_state_d3": {"inputs": ["close"], "func": f25_rsxh_011_rsi14_above_90_state_d3},
    "f25_rsxh_012_rsi63_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_012_rsi63_above_70_state_d3},
    "f25_rsxh_013_rsi252_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_013_rsi252_above_70_state_d3},
    "f25_rsxh_014_rsi14_above_95_state_d3": {"inputs": ["close"], "func": f25_rsxh_014_rsi14_above_95_state_d3},
    "f25_rsxh_015_rsi14_above_q95_distribution_252_d3": {"inputs": ["close"], "func": f25_rsxh_015_rsi14_above_q95_distribution_252_d3},
    "f25_rsxh_016_rsi14_above_q99_distribution_252_d3": {"inputs": ["close"], "func": f25_rsxh_016_rsi14_above_q99_distribution_252_d3},
    "f25_rsxh_017_rsi14_at_252d_max_flag_d3": {"inputs": ["close"], "func": f25_rsxh_017_rsi14_at_252d_max_flag_d3},
    "f25_rsxh_018_rsi14_just_exited_ob70_d3": {"inputs": ["close"], "func": f25_rsxh_018_rsi14_just_exited_ob70_d3},
    "f25_rsxh_019_rsi14_just_exited_ob80_d3": {"inputs": ["close"], "func": f25_rsxh_019_rsi14_just_exited_ob80_d3},
    "f25_rsxh_020_rsi14_just_exited_ob90_d3": {"inputs": ["close"], "func": f25_rsxh_020_rsi14_just_exited_ob90_d3},
    "f25_rsxh_021_bars_since_rsi14_ob70_exit_d3": {"inputs": ["close"], "func": f25_rsxh_021_bars_since_rsi14_ob70_exit_d3},
    "f25_rsxh_022_bars_since_rsi14_ob80_exit_d3": {"inputs": ["close"], "func": f25_rsxh_022_bars_since_rsi14_ob80_exit_d3},
    "f25_rsxh_023_count_rsi14_ob70_exits_63_d3": {"inputs": ["close"], "func": f25_rsxh_023_count_rsi14_ob70_exits_63_d3},
    "f25_rsxh_024_count_rsi14_ob70_exits_252_d3": {"inputs": ["close"], "func": f25_rsxh_024_count_rsi14_ob70_exits_252_d3},
    "f25_rsxh_025_count_rsi14_ob80_exits_252_d3": {"inputs": ["close"], "func": f25_rsxh_025_count_rsi14_ob80_exits_252_d3},
    "f25_rsxh_026_rsi_exit_velocity_drop_from_peak_21_d3": {"inputs": ["close"], "func": f25_rsxh_026_rsi_exit_velocity_drop_from_peak_21_d3},
    "f25_rsxh_027_rsi_failed_retest_lower_peak_63_d3": {"inputs": ["close"], "func": f25_rsxh_027_rsi_failed_retest_lower_peak_63_d3},
    "f25_rsxh_028_fraction_rsi14_ob70_past_21_d3": {"inputs": ["close"], "func": f25_rsxh_028_fraction_rsi14_ob70_past_21_d3},
    "f25_rsxh_029_fraction_rsi14_ob70_past_63_d3": {"inputs": ["close"], "func": f25_rsxh_029_fraction_rsi14_ob70_past_63_d3},
    "f25_rsxh_030_fraction_rsi14_ob70_past_252_d3": {"inputs": ["close"], "func": f25_rsxh_030_fraction_rsi14_ob70_past_252_d3},
    "f25_rsxh_031_fraction_rsi14_ob80_past_63_d3": {"inputs": ["close"], "func": f25_rsxh_031_fraction_rsi14_ob80_past_63_d3},
    "f25_rsxh_032_fraction_rsi14_ob80_past_252_d3": {"inputs": ["close"], "func": f25_rsxh_032_fraction_rsi14_ob80_past_252_d3},
    "f25_rsxh_033_longest_rsi14_ob70_run_252_d3": {"inputs": ["close"], "func": f25_rsxh_033_longest_rsi14_ob70_run_252_d3},
    "f25_rsxh_034_current_rsi14_ob70_streak_d3": {"inputs": ["close"], "func": f25_rsxh_034_current_rsi14_ob70_streak_d3},
    "f25_rsxh_035_distinct_ob70_sessions_252_d3": {"inputs": ["close"], "func": f25_rsxh_035_distinct_ob70_sessions_252_d3},
    "f25_rsxh_036_avg_ob70_session_duration_252_d3": {"inputs": ["close"], "func": f25_rsxh_036_avg_ob70_session_duration_252_d3},
    "f25_rsxh_037_cumulative_ob70_area_252_d3": {"inputs": ["close"], "func": f25_rsxh_037_cumulative_ob70_area_252_d3},
    "f25_rsxh_038_cumulative_ob80_area_252_d3": {"inputs": ["close"], "func": f25_rsxh_038_cumulative_ob80_area_252_d3},
    "f25_rsxh_039_cumulative_ob90_area_252_d3": {"inputs": ["close"], "func": f25_rsxh_039_cumulative_ob90_area_252_d3},
    "f25_rsxh_040_max_rsi_minus_70_past_252_d3": {"inputs": ["close"], "func": f25_rsxh_040_max_rsi_minus_70_past_252_d3},
    "f25_rsxh_041_rsi_peak_decay_63_d3": {"inputs": ["close"], "func": f25_rsxh_041_rsi_peak_decay_63_d3},
    "f25_rsxh_042_rsi_peak_decay_252_d3": {"inputs": ["close"], "func": f25_rsxh_042_rsi_peak_decay_252_d3},
    "f25_rsxh_043_price_vs_rsi14_div_63_d3": {"inputs": _HC, "func": f25_rsxh_043_price_vs_rsi14_div_63_d3},
    "f25_rsxh_044_price_vs_rsi14_div_252_d3": {"inputs": _HC, "func": f25_rsxh_044_price_vs_rsi14_div_252_d3},
    "f25_rsxh_045_count_bearish_rsi_div_63_d3": {"inputs": _HC, "func": f25_rsxh_045_count_bearish_rsi_div_63_d3},
    "f25_rsxh_046_count_bearish_rsi_div_252_d3": {"inputs": _HC, "func": f25_rsxh_046_count_bearish_rsi_div_252_d3},
    "f25_rsxh_047_bars_since_last_bearish_rsi_div_63_d3": {"inputs": _HC, "func": f25_rsxh_047_bars_since_last_bearish_rsi_div_63_d3},
    "f25_rsxh_048_rsi_div_amplitude_63_d3": {"inputs": _HC, "func": f25_rsxh_048_rsi_div_amplitude_63_d3},
    "f25_rsxh_049_price_vs_rsi63_div_252_d3": {"inputs": _HC, "func": f25_rsxh_049_price_vs_rsi63_div_252_d3},
    "f25_rsxh_050_hidden_bearish_div_63_d3": {"inputs": _HC, "func": f25_rsxh_050_hidden_bearish_div_63_d3},
    "f25_rsxh_051_triple_bearish_div_within_63_d3": {"inputs": _HC, "func": f25_rsxh_051_triple_bearish_div_within_63_d3},
    "f25_rsxh_052_rsi_price_corr_63_d3": {"inputs": ["close"], "func": f25_rsxh_052_rsi_price_corr_63_d3},
    "f25_rsxh_053_rsi_slope_21_d3": {"inputs": ["close"], "func": f25_rsxh_053_rsi_slope_21_d3},
    "f25_rsxh_054_rsi_slope_63_d3": {"inputs": ["close"], "func": f25_rsxh_054_rsi_slope_63_d3},
    "f25_rsxh_055_rsi_slope_252_d3": {"inputs": ["close"], "func": f25_rsxh_055_rsi_slope_252_d3},
    "f25_rsxh_056_rsi_cross_50_event_d3": {"inputs": ["close"], "func": f25_rsxh_056_rsi_cross_50_event_d3},
    "f25_rsxh_057_rsi_below_50_dwell_63_d3": {"inputs": ["close"], "func": f25_rsxh_057_rsi_below_50_dwell_63_d3},
    "f25_rsxh_058_rsi_cross_above_50_event_d3": {"inputs": ["close"], "func": f25_rsxh_058_rsi_cross_above_50_event_d3},
    "f25_rsxh_059_rsi_21d_range_d3": {"inputs": ["close"], "func": f25_rsxh_059_rsi_21d_range_d3},
    "f25_rsxh_060_rsi_std_21_d3": {"inputs": ["close"], "func": f25_rsxh_060_rsi_std_21_d3},
    "f25_rsxh_061_connors_rsi_3_d3": {"inputs": ["close"], "func": f25_rsxh_061_connors_rsi_3_d3},
    "f25_rsxh_062_connors_rsi_full_d3": {"inputs": ["close"], "func": f25_rsxh_062_connors_rsi_full_d3},
    "f25_rsxh_063_ud_streak_signed_d3": {"inputs": ["close"], "func": f25_rsxh_063_ud_streak_signed_d3},
    "f25_rsxh_064_up_streak_length_d3": {"inputs": ["close"], "func": f25_rsxh_064_up_streak_length_d3},
    "f25_rsxh_065_down_streak_length_d3": {"inputs": ["close"], "func": f25_rsxh_065_down_streak_length_d3},
    "f25_rsxh_066_percent_rank_return_1_over_100_d3": {"inputs": ["close"], "func": f25_rsxh_066_percent_rank_return_1_over_100_d3},
    "f25_rsxh_067_connors_rsi_above_90_state_d3": {"inputs": ["close"], "func": f25_rsxh_067_connors_rsi_above_90_state_d3},
    "f25_rsxh_068_bars_since_connors_rsi_ob90_exit_d3": {"inputs": ["close"], "func": f25_rsxh_068_bars_since_connors_rsi_ob90_exit_d3},
    "f25_rsxh_069_rsi_of_rsi_14_d3": {"inputs": ["close"], "func": f25_rsxh_069_rsi_of_rsi_14_d3},
    "f25_rsxh_070_rsi_of_rsi_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_070_rsi_of_rsi_above_70_state_d3},
    "f25_rsxh_071_rsi_of_rsi_just_exited_ob70_d3": {"inputs": ["close"], "func": f25_rsxh_071_rsi_of_rsi_just_exited_ob70_d3},
    "f25_rsxh_072_rsi_of_rsi_bearish_div_63_d3": {"inputs": _HC, "func": f25_rsxh_072_rsi_of_rsi_bearish_div_63_d3},
    "f25_rsxh_073_rsi_of_rsi_dwell_ob70_63_d3": {"inputs": ["close"], "func": f25_rsxh_073_rsi_of_rsi_dwell_ob70_63_d3},
    "f25_rsxh_074_rsi_of_rsi_peak_decay_63_d3": {"inputs": ["close"], "func": f25_rsxh_074_rsi_of_rsi_peak_decay_63_d3},
    "f25_rsxh_075_rsi_of_rsi_zscore_252_d3": {"inputs": ["close"], "func": f25_rsxh_075_rsi_of_rsi_zscore_252_d3},
}
