"""macd_topping_dynamics base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: core MACD line, signal, histogram + multi-config (5/35, 12/26, 19/39, PPO).
Bucket B: zero-line dynamics (state, cross, persistence).
Bucket C: signal-line cross dynamics (bearish cross, density, failures).
Bucket D: histogram dynamics (peak decay, double-tops, runs).
Bucket E: MACD bearish divergence vs price (multiple horizons).
Bucket F: slope / rollover / decay velocity.
Bucket G: PPO variants (price-normalized MACD).
Bucket H: multi-config MACD ensembles (fast/classical/slow alignment).

Inputs: SEP OHLCV (close primarily, high/low for divergence reference).
PIT-clean: ewm right-anchored, no centered, no shift(-N). Self-contained helpers.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return macd, sig, histo


def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return ppo, sig, histo


def _bars_since_true(mask: pd.Series) -> pd.Series:
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket A — core MACD line, signal, histogram + multi-config (001-010)
# ============================================================

def f27_mcdt_001_macd_line_12_26(close: pd.Series) -> pd.Series:
    """Classical MACD line (EMA12 - EMA26) — level."""
    m, _, _ = _macd(close, 12, 26, 9)
    return m


def f27_mcdt_002_macd_signal_9(close: pd.Series) -> pd.Series:
    """Classical MACD signal line (EMA9 of MACD)."""
    _, s, _ = _macd(close, 12, 26, 9)
    return s


def f27_mcdt_003_macd_histogram_12_26_9(close: pd.Series) -> pd.Series:
    """Classical MACD histogram = MACD - Signal."""
    _, _, h = _macd(close, 12, 26, 9)
    return h


def f27_mcdt_004_macd_line_5_35(close: pd.Series) -> pd.Series:
    """Short-cycle MACD line (EMA5 - EMA35) — distinct concept: faster trend signal."""
    return _ema(close, 5) - _ema(close, 35)


def f27_mcdt_005_macd_histogram_5_35_5(close: pd.Series) -> pd.Series:
    """Short-cycle MACD histogram — fast trend-momentum convergence."""
    m = _ema(close, 5) - _ema(close, 35)
    return m - _ema(m, 5)


def f27_mcdt_006_macd_line_19_39(close: pd.Series) -> pd.Series:
    """Long-cycle MACD line (EMA19 - EMA39) — distinct concept: slow trend signal."""
    return _ema(close, 19) - _ema(close, 39)


def f27_mcdt_007_macd_histogram_19_39_9(close: pd.Series) -> pd.Series:
    """Long-cycle MACD histogram — slow trend-momentum convergence."""
    m = _ema(close, 19) - _ema(close, 39)
    return m - _ema(m, 9)


def f27_mcdt_008_ppo_12_26(close: pd.Series) -> pd.Series:
    """PPO = 100 * (EMA12 - EMA26) / EMA26 — price-normalized MACD (cross-stock comparable)."""
    p, _, _ = _ppo(close, 12, 26, 9)
    return p


def f27_mcdt_009_ppo_signal_9(close: pd.Series) -> pd.Series:
    """PPO signal line (EMA9 of PPO)."""
    _, s, _ = _ppo(close, 12, 26, 9)
    return s


def f27_mcdt_010_ppo_histogram(close: pd.Series) -> pd.Series:
    """PPO histogram = PPO - Signal."""
    _, _, h = _ppo(close, 12, 26, 9)
    return h


# ============================================================
# Bucket B — zero-line dynamics (011-018)
# ============================================================

def f27_mcdt_011_macd_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if MACD line > 0 — bullish trend regime."""
    m, _, _ = _macd(close)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_012_bars_since_macd_above_zero_start(close: pd.Series) -> pd.Series:
    """Bars since MACD most-recently crossed above zero — age of current bullish regime."""
    m, _, _ = _macd(close)
    ev = (m.shift(1) <= 0) & (m > 0)
    return _bars_since_true(ev)


def f27_mcdt_013_bars_since_macd_below_zero_start(close: pd.Series) -> pd.Series:
    """Bars since MACD most-recently crossed below zero — age of current bearish regime
    (stale = long bull run that may be exhausted)."""
    m, _, _ = _macd(close)
    ev = (m.shift(1) >= 0) & (m < 0)
    return _bars_since_true(ev)


def f27_mcdt_014_macd_zero_cross_down_indicator(close: pd.Series) -> pd.Series:
    """1 if MACD crossed below zero this bar — bearish zero-line cross trigger."""
    m, _, _ = _macd(close)
    return ((m.shift(1) >= 0) & (m < 0)).astype(float).where(m.notna(), np.nan)


def f27_mcdt_015_macd_zero_cross_down_count_252(close: pd.Series) -> pd.Series:
    """Annual count of bearish MACD zero-line crosses — trend churn frequency."""
    m, _, _ = _macd(close)
    ev = ((m.shift(1) >= 0) & (m < 0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan)


def f27_mcdt_016_fraction_time_macd_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with MACD > 0 — annual bullish-regime dwell."""
    m, _, _ = _macd(close)
    return (m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)


def f27_mcdt_017_macd_current_above_zero_streak(close: pd.Series) -> pd.Series:
    """Current consecutive run of MACD > 0 — live bullish-regime streak."""
    m, _, _ = _macd(close)
    return _streak_true(m > 0).where(m.notna(), np.nan)


def f27_mcdt_018_macd_max_above_zero_streak_252(close: pd.Series) -> pd.Series:
    """Longest above-zero streak in trailing 252 — annual peak streak."""
    m, _, _ = _macd(close)
    return _streak_true(m > 0).rolling(YDAYS, min_periods=QDAYS).max().where(m.notna(), np.nan)


# ============================================================
# Bucket C — signal-line cross dynamics (019-026)
# ============================================================

def f27_mcdt_019_signal_bearish_cross_indicator(close: pd.Series) -> pd.Series:
    """1 if MACD crossed below its signal line — classical bearish MACD cross."""
    m, s, _ = _macd(close)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_020_signal_bearish_cross_count_63(close: pd.Series) -> pd.Series:
    """Count of bearish MACD/signal crosses in 63 bars — quarterly cross frequency."""
    m, s, _ = _macd(close)
    d = m - s
    ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_021_bars_since_last_signal_bearish_cross(close: pd.Series) -> pd.Series:
    """Bars since most-recent bearish MACD/signal cross — recency of bearish trigger."""
    m, s, _ = _macd(close)
    d = m - s
    ev = (d.shift(1) > 0) & (d <= 0)
    return _bars_since_true(ev)


def f27_mcdt_022_signal_bearish_cross_above_zero_indicator(close: pd.Series) -> pd.Series:
    """1 if bearish MACD/signal cross fired while MACD > 0 — premium signal (in bullish regime)."""
    m, s, _ = _macd(close)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0) & (m > 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_023_signal_cross_density_in_above_zero_63(close: pd.Series) -> pd.Series:
    """Count of any MACD/signal crosses (either direction) while MACD > 0, past 63 bars — in-regime churn."""
    m, s, _ = _macd(close)
    d = m - s
    cross = ((d.shift(1) * d) < 0) & (m > 0)
    return cross.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_024_signal_bullish_cross_count_63(close: pd.Series) -> pd.Series:
    """Count of bullish MACD/signal crosses in 63 bars — context for net cross density."""
    m, s, _ = _macd(close)
    d = m - s
    ev = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_025_signal_net_cross_density_63(close: pd.Series) -> pd.Series:
    """Bearish - bullish MACD/signal crosses in 63 — net cross-pressure index."""
    m, s, _ = _macd(close)
    d = m - s
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    return (be - bu).rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_026_signal_bullish_cross_failure_count_252(close: pd.Series) -> pd.Series:
    """Bullish MACD/signal crosses that were followed by a bearish cross within 21 bars, past 252 — failed bullish triggers."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    bu_21_ago = bu.shift(MDAYS)
    be_in_21 = be.rolling(MDAYS, min_periods=1).sum()
    fail = (bu_21_ago > 0) & (be_in_21 > 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan)


# ============================================================
# Bucket D — histogram dynamics (027-035)
# ============================================================

def f27_mcdt_027_histogram_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if MACD histogram > 0 — bullish momentum-of-momentum."""
    _, _, h = _macd(close)
    return (h > 0).astype(float).where(h.notna(), np.nan)


def f27_mcdt_028_histogram_just_crossed_below_zero(close: pd.Series) -> pd.Series:
    """1 if histogram crossed below 0 this bar — same as bearish MACD/signal cross trigger but
    framed as 'momentum-of-momentum sign flip' (distinct framing)."""
    _, _, h = _macd(close)
    return ((h.shift(1) >= 0) & (h < 0)).astype(float).where(h.notna(), np.nan)


def f27_mcdt_029_histogram_peak_decay_21(close: pd.Series) -> pd.Series:
    """Histogram 21d max - histogram from 21 bars ago — short-term histogram peak decay."""
    _, _, h = _macd(close)
    pmax = h.rolling(MDAYS, min_periods=WDAYS).max()
    return pmax - pmax.shift(MDAYS)


def f27_mcdt_030_histogram_peak_decay_63(close: pd.Series) -> pd.Series:
    """Histogram 63d max - histogram from 63 bars ago — quarterly histogram peak decay."""
    _, _, h = _macd(close)
    pmax = h.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f27_mcdt_031_histogram_rolling_max_63(close: pd.Series) -> pd.Series:
    """Histogram rolling 63d max — quarterly histogram peak level (regime intensity)."""
    _, _, h = _macd(close)
    return h.rolling(QDAYS, min_periods=MDAYS).max()


def f27_mcdt_032_histogram_lower_high_count_63(close: pd.Series) -> pd.Series:
    """Count of bars where current 5d histo-max is below the prior 5d histo-max, past 63 — lower-histo-high count."""
    _, _, h = _macd(close)
    rmax = h.rolling(WDAYS, min_periods=2).max()
    lh = (rmax < rmax.shift(WDAYS)).astype(float)
    return lh.rolling(QDAYS, min_periods=MDAYS).sum().where(h.notna(), np.nan)


def f27_mcdt_033_histogram_double_top_indicator_63(close: pd.Series) -> pd.Series:
    """1 if 21d histogram max < 21d histogram max from 21 bars ago AND both are positive — double-top in histo."""
    _, _, h = _macd(close)
    pmax = h.rolling(MDAYS, min_periods=WDAYS).max()
    return ((pmax < pmax.shift(MDAYS)) & (pmax > 0) & (pmax.shift(MDAYS) > 0)).astype(float).where(h.notna(), np.nan)


def f27_mcdt_034_histogram_bars_since_last_252_max(close: pd.Series) -> pd.Series:
    """Bars since histogram hit its 252d max — recency of histogram peak."""
    _, _, h = _macd(close)
    at_max = h == h.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_035_histogram_consecutive_negatives_streak(close: pd.Series) -> pd.Series:
    """Current consecutive run of histo < 0 — live bearish-momentum-of-momentum streak."""
    _, _, h = _macd(close)
    return _streak_true(h < 0).where(h.notna(), np.nan)


# ============================================================
# Bucket E — MACD bearish divergence vs price (036-045)
# ============================================================

def f27_mcdt_036_price_new_63h_macd_below_prior_63_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if price made new 63d high AND MACD is below prior 63d MACD max — classical bearish divergence."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


def f27_mcdt_037_price_new_252h_macd_below_prior_252_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual-horizon bearish divergence — new 252d high but MACD below prior 252d MACD max."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    m_below = m < m.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


def f27_mcdt_038_amplitude_of_macd_div_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bearish-div bars, amplitude = prior 63d MACD max - current MACD (magnitude of divergence)."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_max - m).where(p_new & (m < prior_max), np.nan)
    return amp.ffill(limit=QDAYS)


def f27_mcdt_039_bars_since_last_macd_div_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent quarterly MACD bearish divergence."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = p_new & (m < prior_max)
    return _bars_since_true(ev)


def f27_mcdt_040_rolling_corr_macd_price_63(close: pd.Series) -> pd.Series:
    """Rolling 63d correlation(close, MACD) — drops when momentum decouples from price."""
    m, _, _ = _macd(close)
    return close.rolling(QDAYS, min_periods=MDAYS).corr(m)


def f27_mcdt_041_rolling_corr_macd_price_252(close: pd.Series) -> pd.Series:
    """Rolling 252d correlation(close, MACD) — annual decoupling indicator."""
    m, _, _ = _macd(close)
    return close.rolling(YDAYS, min_periods=QDAYS).corr(m)


def f27_mcdt_042_histo_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using MACD histogram (not the line): price new 63d high but histo below prior max."""
    _, _, h = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    h_below = h < h.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & h_below).astype(float).where(h.notna(), np.nan)


def f27_mcdt_043_count_macd_div_events_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish MACD-line divergence events in past 63 bars."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = (p_new & (m < prior_max)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(m.notna(), np.nan)


def f27_mcdt_044_count_macd_div_events_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of MACD-line bearish divergence events."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_max = m.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = (p_new & (m < prior_max)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan)


def f27_mcdt_045_div_amplitude_zscore_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of most-recent divergence amplitude vs trailing 252d distribution of amplitudes."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_max - m).where(p_new & (m < prior_max), np.nan).ffill(limit=QDAYS)
    return _rolling_zscore(amp, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket F — slope / rollover / decay velocity (046-055)
# ============================================================

def f27_mcdt_046_macd_line_slope_5(close: pd.Series) -> pd.Series:
    """5-bar linear slope of MACD line — short-term momentum-direction rate."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, WDAYS)


def f27_mcdt_047_macd_line_slope_21(close: pd.Series) -> pd.Series:
    """21-bar linear slope of MACD line — monthly momentum-direction rate."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, MDAYS)


def f27_mcdt_048_macd_line_slope_63(close: pd.Series) -> pd.Series:
    """63-bar linear slope of MACD line — quarterly momentum-direction rate."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, QDAYS)


def f27_mcdt_049_macd_slope_just_turned_negative(close: pd.Series) -> pd.Series:
    """1 if 5d-slope of MACD was positive last bar and is negative this bar — rollover trigger."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, WDAYS)
    return ((sl.shift(1) > 0) & (sl <= 0)).astype(float).where(sl.notna(), np.nan)


def f27_mcdt_050_bars_since_macd_slope_turned_negative(close: pd.Series) -> pd.Series:
    """Bars since the most-recent slope-turn-negative event — recency of MACD rollover."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, WDAYS)
    ev = (sl.shift(1) > 0) & (sl <= 0)
    return _bars_since_true(ev)


def f27_mcdt_051_macd_max_then_decay_indicator(close: pd.Series) -> pd.Series:
    """1 if MACD was at its 63d max within last 21 bars AND is now declining (sl<0) — post-peak decay state."""
    m, _, _ = _macd(close)
    rmax63 = m.rolling(QDAYS, min_periods=MDAYS).max()
    was_at_max = (m == rmax63).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    sl = _rolling_slope(m, WDAYS)
    return (was_at_max & (sl < 0)).astype(float).where(m.notna() & sl.notna(), np.nan)


def f27_mcdt_052_macd_decay_velocity_from_peak_21(close: pd.Series) -> pd.Series:
    """(21d MACD max) - (current MACD) — magnitude of decay since recent peak."""
    m, _, _ = _macd(close)
    return m.rolling(MDAYS, min_periods=WDAYS).max() - m


def f27_mcdt_053_macd_slope_acceleration_5(close: pd.Series) -> pd.Series:
    """First difference of 5d-slope-of-MACD — slope acceleration (jerk-of-line)."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, WDAYS).diff()


def f27_mcdt_054_histo_slope_5(close: pd.Series) -> pd.Series:
    """5-bar slope of MACD histogram — short-term histogram trend rate."""
    _, _, h = _macd(close)
    return _rolling_slope(h, WDAYS)


def f27_mcdt_055_histo_slope_turned_negative_indicator(close: pd.Series) -> pd.Series:
    """1 if histogram slope just turned negative — momentum-of-momentum rollover."""
    _, _, h = _macd(close)
    sl = _rolling_slope(h, WDAYS)
    return ((sl.shift(1) > 0) & (sl <= 0)).astype(float).where(sl.notna(), np.nan)


# ============================================================
# Bucket G — PPO variants (056-065)
# ============================================================

def f27_mcdt_056_ppo_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if PPO > 0 — bullish trend regime (price-normalized version of MACD>0)."""
    p, _, _ = _ppo(close)
    return (p > 0).astype(float).where(p.notna(), np.nan)


def f27_mcdt_057_ppo_bearish_cross_signal_indicator(close: pd.Series) -> pd.Series:
    """1 if PPO crossed below its signal line — bearish PPO cross (cross-stock comparable)."""
    p, s, _ = _ppo(close)
    d = p - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_058_ppo_histogram_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if PPO histogram > 0 — bullish momentum-of-momentum (normalized)."""
    _, _, h = _ppo(close)
    return (h > 0).astype(float).where(h.notna(), np.nan)


def f27_mcdt_059_ppo_above_q90_distribution_252(close: pd.Series) -> pd.Series:
    """1 if PPO above its trailing 252d 90th percentile — distribution-based PPO OB."""
    p, _, _ = _ppo(close)
    q = p.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (p > q).astype(float).where(p.notna() & q.notna(), np.nan)


def f27_mcdt_060_ppo_persistence_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with PPO > 0 — annual normalized-bullish dwell."""
    p, _, _ = _ppo(close)
    return (p > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(p.notna(), np.nan)


def f27_mcdt_061_ppo_peak_decay_63(close: pd.Series) -> pd.Series:
    """PPO 63d max - PPO from 63 bars ago — quarterly normalized peak decay."""
    p, _, _ = _ppo(close)
    pmax = p.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f27_mcdt_062_ppo_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of PPO over 252d — distribution-normalized normalized-momentum extreme."""
    p, _, _ = _ppo(close)
    return _rolling_zscore(p, YDAYS, min_periods=QDAYS)


def f27_mcdt_063_ppo_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using PPO (price-normalized momentum) instead of MACD."""
    p, _, _ = _ppo(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    p_below = p < p.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & p_below).astype(float).where(p.notna(), np.nan)


def f27_mcdt_064_ppo_signal_cross_density_63(close: pd.Series) -> pd.Series:
    """Count of PPO/signal crosses (either direction) in past 63 — normalized cross-churn."""
    p, s, _ = _ppo(close)
    d = p - s
    cross = (d.shift(1) * d) < 0
    return cross.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_065_ppo_histogram_lower_high_count_63(close: pd.Series) -> pd.Series:
    """Count of lower 5d-histogram-max events in past 63 — normalized momentum-of-momentum cooling count."""
    _, _, h = _ppo(close)
    rmax = h.rolling(WDAYS, min_periods=2).max()
    lh = (rmax < rmax.shift(WDAYS)).astype(float)
    return lh.rolling(QDAYS, min_periods=MDAYS).sum().where(h.notna(), np.nan)


# ============================================================
# Bucket H — multi-config MACD ensembles (066-075)
# ============================================================

def f27_mcdt_066_fast_macd_minus_classical_macd(close: pd.Series) -> pd.Series:
    """MACD(5,35) - MACD(12,26) — fast-cycle minus classical-cycle MACD (cycle gap)."""
    fast = _ema(close, 5) - _ema(close, 35)
    classical, _, _ = _macd(close, 12, 26, 9)
    return fast - classical


def f27_mcdt_067_slow_macd_minus_classical_macd(close: pd.Series) -> pd.Series:
    """MACD(19,39) - MACD(12,26) — slow-cycle minus classical-cycle MACD (cycle gap)."""
    slow = _ema(close, 19) - _ema(close, 39)
    classical, _, _ = _macd(close, 12, 26, 9)
    return slow - classical


def f27_mcdt_068_all_three_macd_above_zero_indicator(close: pd.Series) -> pd.Series:
    """1 if MACD(5,35), MACD(12,26), MACD(19,39) all > 0 — confirmed multi-cycle bullish regime."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, _ = _macd(close, 12, 26, 9)
    s = _ema(close, 19) - _ema(close, 39)
    return ((f > 0) & (c > 0) & (s > 0)).astype(float).where(
        f.notna() & c.notna() & s.notna(), np.nan)


def f27_mcdt_069_count_configs_with_bearish_cross_in_21d(close: pd.Series) -> pd.Series:
    """Count of MACD configs in {5/35/5, 12/26/9, 19/39/9} that had a bearish cross in past 21 — multi-cycle bearish."""
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9)]:
        m, s, _ = _macd(close, f, sl, sg)
        d = m - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        in_21 = ev.rolling(MDAYS, min_periods=1).sum() > 0
        cnt = cnt + in_21.astype(float)
    return cnt.where(close.notna(), np.nan)


def f27_mcdt_070_macd_ensemble_avg_zscore_252(close: pd.Series) -> pd.Series:
    """Average z-score (over 252d) of MACD line across {5/35, 12/26, 19/39} — ensemble extension."""
    z1 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    c, _, _ = _macd(close, 12, 26, 9)
    z2 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    return (z1 + z2 + z3) / 3.0


def f27_mcdt_071_macd_ensemble_dispersion(close: pd.Series) -> pd.Series:
    """Std across z-scored {fast, classical, slow} MACD — multi-cycle dispersion (regime disagreement)."""
    z1 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    c, _, _ = _macd(close, 12, 26, 9)
    z2 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    return pd.concat([z1.rename("z1"), z2.rename("z2"), z3.rename("z3")], axis=1).std(axis=1)


def f27_mcdt_072_multi_horizon_macd_div_count(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {63, 126, 252} where a MACD bearish-div currently fires — multi-horizon div breadth."""
    m, _, _ = _macd(close)
    cnt = pd.Series(0.0, index=close.index)
    for n in (QDAYS, 126, YDAYS):
        p_new = high >= high.rolling(n, min_periods=max(n // 3, MDAYS)).max()
        m_below = m < m.shift(1).rolling(n, min_periods=max(n // 3, MDAYS)).max()
        cnt = cnt + (p_new & m_below).astype(float).fillna(0)
    return cnt.where(m.notna(), np.nan)


def f27_mcdt_073_fast_macd_minus_slow_macd_at_top(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d max: (fast MACD - slow MACD). Else NaN.
    Sign of fast-vs-slow at the peak."""
    fast = _ema(close, 5) - _ema(close, 35)
    slow = _ema(close, 19) - _ema(close, 39)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return (fast - slow).where(at_max, np.nan)


def f27_mcdt_074_count_macd_horizons_in_decline_63(close: pd.Series) -> pd.Series:
    """Count of MACD configs in {5/35, 12/26, 19/39} with 63d slope < 0 — multi-cycle decline breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9)]:
        m, _, _ = _macd(close, f, sl, sg)
        slope = _rolling_slope(m, QDAYS)
        cnt = cnt + (slope < 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f27_mcdt_075_macd_horizon_lead_lag_diff_21(close: pd.Series) -> pd.Series:
    """21d slope of fast MACD minus 21d slope of slow MACD — fast leads / lags slow indicator."""
    fast = _ema(close, 5) - _ema(close, 35)
    slow = _ema(close, 19) - _ema(close, 39)
    return _rolling_slope(fast, MDAYS) - _rolling_slope(slow, MDAYS)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

MACD_TOPPING_DYNAMICS_BASE_REGISTRY_001_075 = {
    "f27_mcdt_001_macd_line_12_26": {"inputs": ["close"], "func": f27_mcdt_001_macd_line_12_26},
    "f27_mcdt_002_macd_signal_9": {"inputs": ["close"], "func": f27_mcdt_002_macd_signal_9},
    "f27_mcdt_003_macd_histogram_12_26_9": {"inputs": ["close"], "func": f27_mcdt_003_macd_histogram_12_26_9},
    "f27_mcdt_004_macd_line_5_35": {"inputs": ["close"], "func": f27_mcdt_004_macd_line_5_35},
    "f27_mcdt_005_macd_histogram_5_35_5": {"inputs": ["close"], "func": f27_mcdt_005_macd_histogram_5_35_5},
    "f27_mcdt_006_macd_line_19_39": {"inputs": ["close"], "func": f27_mcdt_006_macd_line_19_39},
    "f27_mcdt_007_macd_histogram_19_39_9": {"inputs": ["close"], "func": f27_mcdt_007_macd_histogram_19_39_9},
    "f27_mcdt_008_ppo_12_26": {"inputs": ["close"], "func": f27_mcdt_008_ppo_12_26},
    "f27_mcdt_009_ppo_signal_9": {"inputs": ["close"], "func": f27_mcdt_009_ppo_signal_9},
    "f27_mcdt_010_ppo_histogram": {"inputs": ["close"], "func": f27_mcdt_010_ppo_histogram},
    "f27_mcdt_011_macd_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_011_macd_above_zero_state},
    "f27_mcdt_012_bars_since_macd_above_zero_start": {"inputs": ["close"], "func": f27_mcdt_012_bars_since_macd_above_zero_start},
    "f27_mcdt_013_bars_since_macd_below_zero_start": {"inputs": ["close"], "func": f27_mcdt_013_bars_since_macd_below_zero_start},
    "f27_mcdt_014_macd_zero_cross_down_indicator": {"inputs": ["close"], "func": f27_mcdt_014_macd_zero_cross_down_indicator},
    "f27_mcdt_015_macd_zero_cross_down_count_252": {"inputs": ["close"], "func": f27_mcdt_015_macd_zero_cross_down_count_252},
    "f27_mcdt_016_fraction_time_macd_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_016_fraction_time_macd_above_zero_252},
    "f27_mcdt_017_macd_current_above_zero_streak": {"inputs": ["close"], "func": f27_mcdt_017_macd_current_above_zero_streak},
    "f27_mcdt_018_macd_max_above_zero_streak_252": {"inputs": ["close"], "func": f27_mcdt_018_macd_max_above_zero_streak_252},
    "f27_mcdt_019_signal_bearish_cross_indicator": {"inputs": ["close"], "func": f27_mcdt_019_signal_bearish_cross_indicator},
    "f27_mcdt_020_signal_bearish_cross_count_63": {"inputs": ["close"], "func": f27_mcdt_020_signal_bearish_cross_count_63},
    "f27_mcdt_021_bars_since_last_signal_bearish_cross": {"inputs": ["close"], "func": f27_mcdt_021_bars_since_last_signal_bearish_cross},
    "f27_mcdt_022_signal_bearish_cross_above_zero_indicator": {"inputs": ["close"], "func": f27_mcdt_022_signal_bearish_cross_above_zero_indicator},
    "f27_mcdt_023_signal_cross_density_in_above_zero_63": {"inputs": ["close"], "func": f27_mcdt_023_signal_cross_density_in_above_zero_63},
    "f27_mcdt_024_signal_bullish_cross_count_63": {"inputs": ["close"], "func": f27_mcdt_024_signal_bullish_cross_count_63},
    "f27_mcdt_025_signal_net_cross_density_63": {"inputs": ["close"], "func": f27_mcdt_025_signal_net_cross_density_63},
    "f27_mcdt_026_signal_bullish_cross_failure_count_252": {"inputs": ["close"], "func": f27_mcdt_026_signal_bullish_cross_failure_count_252},
    "f27_mcdt_027_histogram_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_027_histogram_above_zero_state},
    "f27_mcdt_028_histogram_just_crossed_below_zero": {"inputs": ["close"], "func": f27_mcdt_028_histogram_just_crossed_below_zero},
    "f27_mcdt_029_histogram_peak_decay_21": {"inputs": ["close"], "func": f27_mcdt_029_histogram_peak_decay_21},
    "f27_mcdt_030_histogram_peak_decay_63": {"inputs": ["close"], "func": f27_mcdt_030_histogram_peak_decay_63},
    "f27_mcdt_031_histogram_rolling_max_63": {"inputs": ["close"], "func": f27_mcdt_031_histogram_rolling_max_63},
    "f27_mcdt_032_histogram_lower_high_count_63": {"inputs": ["close"], "func": f27_mcdt_032_histogram_lower_high_count_63},
    "f27_mcdt_033_histogram_double_top_indicator_63": {"inputs": ["close"], "func": f27_mcdt_033_histogram_double_top_indicator_63},
    "f27_mcdt_034_histogram_bars_since_last_252_max": {"inputs": ["close"], "func": f27_mcdt_034_histogram_bars_since_last_252_max},
    "f27_mcdt_035_histogram_consecutive_negatives_streak": {"inputs": ["close"], "func": f27_mcdt_035_histogram_consecutive_negatives_streak},
    "f27_mcdt_036_price_new_63h_macd_below_prior_63_max": {"inputs": ["high", "close"], "func": f27_mcdt_036_price_new_63h_macd_below_prior_63_max},
    "f27_mcdt_037_price_new_252h_macd_below_prior_252_max": {"inputs": ["high", "close"], "func": f27_mcdt_037_price_new_252h_macd_below_prior_252_max},
    "f27_mcdt_038_amplitude_of_macd_div_63": {"inputs": ["high", "close"], "func": f27_mcdt_038_amplitude_of_macd_div_63},
    "f27_mcdt_039_bars_since_last_macd_div_63": {"inputs": ["high", "close"], "func": f27_mcdt_039_bars_since_last_macd_div_63},
    "f27_mcdt_040_rolling_corr_macd_price_63": {"inputs": ["close"], "func": f27_mcdt_040_rolling_corr_macd_price_63},
    "f27_mcdt_041_rolling_corr_macd_price_252": {"inputs": ["close"], "func": f27_mcdt_041_rolling_corr_macd_price_252},
    "f27_mcdt_042_histo_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_042_histo_div_vs_price_63},
    "f27_mcdt_043_count_macd_div_events_63": {"inputs": ["high", "close"], "func": f27_mcdt_043_count_macd_div_events_63},
    "f27_mcdt_044_count_macd_div_events_252": {"inputs": ["high", "close"], "func": f27_mcdt_044_count_macd_div_events_252},
    "f27_mcdt_045_div_amplitude_zscore_252": {"inputs": ["high", "close"], "func": f27_mcdt_045_div_amplitude_zscore_252},
    "f27_mcdt_046_macd_line_slope_5": {"inputs": ["close"], "func": f27_mcdt_046_macd_line_slope_5},
    "f27_mcdt_047_macd_line_slope_21": {"inputs": ["close"], "func": f27_mcdt_047_macd_line_slope_21},
    "f27_mcdt_048_macd_line_slope_63": {"inputs": ["close"], "func": f27_mcdt_048_macd_line_slope_63},
    "f27_mcdt_049_macd_slope_just_turned_negative": {"inputs": ["close"], "func": f27_mcdt_049_macd_slope_just_turned_negative},
    "f27_mcdt_050_bars_since_macd_slope_turned_negative": {"inputs": ["close"], "func": f27_mcdt_050_bars_since_macd_slope_turned_negative},
    "f27_mcdt_051_macd_max_then_decay_indicator": {"inputs": ["close"], "func": f27_mcdt_051_macd_max_then_decay_indicator},
    "f27_mcdt_052_macd_decay_velocity_from_peak_21": {"inputs": ["close"], "func": f27_mcdt_052_macd_decay_velocity_from_peak_21},
    "f27_mcdt_053_macd_slope_acceleration_5": {"inputs": ["close"], "func": f27_mcdt_053_macd_slope_acceleration_5},
    "f27_mcdt_054_histo_slope_5": {"inputs": ["close"], "func": f27_mcdt_054_histo_slope_5},
    "f27_mcdt_055_histo_slope_turned_negative_indicator": {"inputs": ["close"], "func": f27_mcdt_055_histo_slope_turned_negative_indicator},
    "f27_mcdt_056_ppo_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_056_ppo_above_zero_state},
    "f27_mcdt_057_ppo_bearish_cross_signal_indicator": {"inputs": ["close"], "func": f27_mcdt_057_ppo_bearish_cross_signal_indicator},
    "f27_mcdt_058_ppo_histogram_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_058_ppo_histogram_above_zero_state},
    "f27_mcdt_059_ppo_above_q90_distribution_252": {"inputs": ["close"], "func": f27_mcdt_059_ppo_above_q90_distribution_252},
    "f27_mcdt_060_ppo_persistence_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_060_ppo_persistence_above_zero_252},
    "f27_mcdt_061_ppo_peak_decay_63": {"inputs": ["close"], "func": f27_mcdt_061_ppo_peak_decay_63},
    "f27_mcdt_062_ppo_zscore_252": {"inputs": ["close"], "func": f27_mcdt_062_ppo_zscore_252},
    "f27_mcdt_063_ppo_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_063_ppo_div_vs_price_63},
    "f27_mcdt_064_ppo_signal_cross_density_63": {"inputs": ["close"], "func": f27_mcdt_064_ppo_signal_cross_density_63},
    "f27_mcdt_065_ppo_histogram_lower_high_count_63": {"inputs": ["close"], "func": f27_mcdt_065_ppo_histogram_lower_high_count_63},
    "f27_mcdt_066_fast_macd_minus_classical_macd": {"inputs": ["close"], "func": f27_mcdt_066_fast_macd_minus_classical_macd},
    "f27_mcdt_067_slow_macd_minus_classical_macd": {"inputs": ["close"], "func": f27_mcdt_067_slow_macd_minus_classical_macd},
    "f27_mcdt_068_all_three_macd_above_zero_indicator": {"inputs": ["close"], "func": f27_mcdt_068_all_three_macd_above_zero_indicator},
    "f27_mcdt_069_count_configs_with_bearish_cross_in_21d": {"inputs": ["close"], "func": f27_mcdt_069_count_configs_with_bearish_cross_in_21d},
    "f27_mcdt_070_macd_ensemble_avg_zscore_252": {"inputs": ["close"], "func": f27_mcdt_070_macd_ensemble_avg_zscore_252},
    "f27_mcdt_071_macd_ensemble_dispersion": {"inputs": ["close"], "func": f27_mcdt_071_macd_ensemble_dispersion},
    "f27_mcdt_072_multi_horizon_macd_div_count": {"inputs": ["high", "close"], "func": f27_mcdt_072_multi_horizon_macd_div_count},
    "f27_mcdt_073_fast_macd_minus_slow_macd_at_top": {"inputs": ["high", "close"], "func": f27_mcdt_073_fast_macd_minus_slow_macd_at_top},
    "f27_mcdt_074_count_macd_horizons_in_decline_63": {"inputs": ["close"], "func": f27_mcdt_074_count_macd_horizons_in_decline_63},
    "f27_mcdt_075_macd_horizon_lead_lag_diff_21": {"inputs": ["close"], "func": f27_mcdt_075_macd_horizon_lead_lag_diff_21},
}


# === D2 wrappers + registry (001_075) ===
def f27_mcdt_001_macd_line_12_26_d2(close): return f27_mcdt_001_macd_line_12_26(close).diff().diff()
def f27_mcdt_002_macd_signal_9_d2(close): return f27_mcdt_002_macd_signal_9(close).diff().diff()
def f27_mcdt_003_macd_histogram_12_26_9_d2(close): return f27_mcdt_003_macd_histogram_12_26_9(close).diff().diff()
def f27_mcdt_004_macd_line_5_35_d2(close): return f27_mcdt_004_macd_line_5_35(close).diff().diff()
def f27_mcdt_005_macd_histogram_5_35_5_d2(close): return f27_mcdt_005_macd_histogram_5_35_5(close).diff().diff()
def f27_mcdt_006_macd_line_19_39_d2(close): return f27_mcdt_006_macd_line_19_39(close).diff().diff()
def f27_mcdt_007_macd_histogram_19_39_9_d2(close): return f27_mcdt_007_macd_histogram_19_39_9(close).diff().diff()
def f27_mcdt_008_ppo_12_26_d2(close): return f27_mcdt_008_ppo_12_26(close).diff().diff()
def f27_mcdt_009_ppo_signal_9_d2(close): return f27_mcdt_009_ppo_signal_9(close).diff().diff()
def f27_mcdt_010_ppo_histogram_d2(close): return f27_mcdt_010_ppo_histogram(close).diff().diff()
def f27_mcdt_011_macd_above_zero_state_d2(close): return f27_mcdt_011_macd_above_zero_state(close).diff().diff()
def f27_mcdt_012_bars_since_macd_above_zero_start_d2(close): return f27_mcdt_012_bars_since_macd_above_zero_start(close).diff().diff()
def f27_mcdt_013_bars_since_macd_below_zero_start_d2(close): return f27_mcdt_013_bars_since_macd_below_zero_start(close).diff().diff()
def f27_mcdt_014_macd_zero_cross_down_indicator_d2(close): return f27_mcdt_014_macd_zero_cross_down_indicator(close).diff().diff()
def f27_mcdt_015_macd_zero_cross_down_count_252_d2(close): return f27_mcdt_015_macd_zero_cross_down_count_252(close).diff().diff()
def f27_mcdt_016_fraction_time_macd_above_zero_252_d2(close): return f27_mcdt_016_fraction_time_macd_above_zero_252(close).diff().diff()
def f27_mcdt_017_macd_current_above_zero_streak_d2(close): return f27_mcdt_017_macd_current_above_zero_streak(close).diff().diff()
def f27_mcdt_018_macd_max_above_zero_streak_252_d2(close): return f27_mcdt_018_macd_max_above_zero_streak_252(close).diff().diff()
def f27_mcdt_019_signal_bearish_cross_indicator_d2(close): return f27_mcdt_019_signal_bearish_cross_indicator(close).diff().diff()
def f27_mcdt_020_signal_bearish_cross_count_63_d2(close): return f27_mcdt_020_signal_bearish_cross_count_63(close).diff().diff()
def f27_mcdt_021_bars_since_last_signal_bearish_cross_d2(close): return f27_mcdt_021_bars_since_last_signal_bearish_cross(close).diff().diff()
def f27_mcdt_022_signal_bearish_cross_above_zero_indicator_d2(close): return f27_mcdt_022_signal_bearish_cross_above_zero_indicator(close).diff().diff()
def f27_mcdt_023_signal_cross_density_in_above_zero_63_d2(close): return f27_mcdt_023_signal_cross_density_in_above_zero_63(close).diff().diff()
def f27_mcdt_024_signal_bullish_cross_count_63_d2(close): return f27_mcdt_024_signal_bullish_cross_count_63(close).diff().diff()
def f27_mcdt_025_signal_net_cross_density_63_d2(close): return f27_mcdt_025_signal_net_cross_density_63(close).diff().diff()
def f27_mcdt_026_signal_bullish_cross_failure_count_252_d2(close): return f27_mcdt_026_signal_bullish_cross_failure_count_252(close).diff().diff()
def f27_mcdt_027_histogram_above_zero_state_d2(close): return f27_mcdt_027_histogram_above_zero_state(close).diff().diff()
def f27_mcdt_028_histogram_just_crossed_below_zero_d2(close): return f27_mcdt_028_histogram_just_crossed_below_zero(close).diff().diff()
def f27_mcdt_029_histogram_peak_decay_21_d2(close): return f27_mcdt_029_histogram_peak_decay_21(close).diff().diff()
def f27_mcdt_030_histogram_peak_decay_63_d2(close): return f27_mcdt_030_histogram_peak_decay_63(close).diff().diff()
def f27_mcdt_031_histogram_rolling_max_63_d2(close): return f27_mcdt_031_histogram_rolling_max_63(close).diff().diff()
def f27_mcdt_032_histogram_lower_high_count_63_d2(close): return f27_mcdt_032_histogram_lower_high_count_63(close).diff().diff()
def f27_mcdt_033_histogram_double_top_indicator_63_d2(close): return f27_mcdt_033_histogram_double_top_indicator_63(close).diff().diff()
def f27_mcdt_034_histogram_bars_since_last_252_max_d2(close): return f27_mcdt_034_histogram_bars_since_last_252_max(close).diff().diff()
def f27_mcdt_035_histogram_consecutive_negatives_streak_d2(close): return f27_mcdt_035_histogram_consecutive_negatives_streak(close).diff().diff()
def f27_mcdt_036_price_new_63h_macd_below_prior_63_max_d2(high, close): return f27_mcdt_036_price_new_63h_macd_below_prior_63_max(high, close).diff().diff()
def f27_mcdt_037_price_new_252h_macd_below_prior_252_max_d2(high, close): return f27_mcdt_037_price_new_252h_macd_below_prior_252_max(high, close).diff().diff()
def f27_mcdt_038_amplitude_of_macd_div_63_d2(high, close): return f27_mcdt_038_amplitude_of_macd_div_63(high, close).diff().diff()
def f27_mcdt_039_bars_since_last_macd_div_63_d2(high, close): return f27_mcdt_039_bars_since_last_macd_div_63(high, close).diff().diff()
def f27_mcdt_040_rolling_corr_macd_price_63_d2(close): return f27_mcdt_040_rolling_corr_macd_price_63(close).diff().diff()
def f27_mcdt_041_rolling_corr_macd_price_252_d2(close): return f27_mcdt_041_rolling_corr_macd_price_252(close).diff().diff()
def f27_mcdt_042_histo_div_vs_price_63_d2(high, close): return f27_mcdt_042_histo_div_vs_price_63(high, close).diff().diff()
def f27_mcdt_043_count_macd_div_events_63_d2(high, close): return f27_mcdt_043_count_macd_div_events_63(high, close).diff().diff()
def f27_mcdt_044_count_macd_div_events_252_d2(high, close): return f27_mcdt_044_count_macd_div_events_252(high, close).diff().diff()
def f27_mcdt_045_div_amplitude_zscore_252_d2(high, close): return f27_mcdt_045_div_amplitude_zscore_252(high, close).diff().diff()
def f27_mcdt_046_macd_line_slope_5_d2(close): return f27_mcdt_046_macd_line_slope_5(close).diff().diff()
def f27_mcdt_047_macd_line_slope_21_d2(close): return f27_mcdt_047_macd_line_slope_21(close).diff().diff()
def f27_mcdt_048_macd_line_slope_63_d2(close): return f27_mcdt_048_macd_line_slope_63(close).diff().diff()
def f27_mcdt_049_macd_slope_just_turned_negative_d2(close): return f27_mcdt_049_macd_slope_just_turned_negative(close).diff().diff()
def f27_mcdt_050_bars_since_macd_slope_turned_negative_d2(close): return f27_mcdt_050_bars_since_macd_slope_turned_negative(close).diff().diff()
def f27_mcdt_051_macd_max_then_decay_indicator_d2(close): return f27_mcdt_051_macd_max_then_decay_indicator(close).diff().diff()
def f27_mcdt_052_macd_decay_velocity_from_peak_21_d2(close): return f27_mcdt_052_macd_decay_velocity_from_peak_21(close).diff().diff()
def f27_mcdt_053_macd_slope_acceleration_5_d2(close): return f27_mcdt_053_macd_slope_acceleration_5(close).diff().diff()
def f27_mcdt_054_histo_slope_5_d2(close): return f27_mcdt_054_histo_slope_5(close).diff().diff()
def f27_mcdt_055_histo_slope_turned_negative_indicator_d2(close): return f27_mcdt_055_histo_slope_turned_negative_indicator(close).diff().diff()
def f27_mcdt_056_ppo_above_zero_state_d2(close): return f27_mcdt_056_ppo_above_zero_state(close).diff().diff()
def f27_mcdt_057_ppo_bearish_cross_signal_indicator_d2(close): return f27_mcdt_057_ppo_bearish_cross_signal_indicator(close).diff().diff()
def f27_mcdt_058_ppo_histogram_above_zero_state_d2(close): return f27_mcdt_058_ppo_histogram_above_zero_state(close).diff().diff()
def f27_mcdt_059_ppo_above_q90_distribution_252_d2(close): return f27_mcdt_059_ppo_above_q90_distribution_252(close).diff().diff()
def f27_mcdt_060_ppo_persistence_above_zero_252_d2(close): return f27_mcdt_060_ppo_persistence_above_zero_252(close).diff().diff()
def f27_mcdt_061_ppo_peak_decay_63_d2(close): return f27_mcdt_061_ppo_peak_decay_63(close).diff().diff()
def f27_mcdt_062_ppo_zscore_252_d2(close): return f27_mcdt_062_ppo_zscore_252(close).diff().diff()
def f27_mcdt_063_ppo_div_vs_price_63_d2(high, close): return f27_mcdt_063_ppo_div_vs_price_63(high, close).diff().diff()
def f27_mcdt_064_ppo_signal_cross_density_63_d2(close): return f27_mcdt_064_ppo_signal_cross_density_63(close).diff().diff()
def f27_mcdt_065_ppo_histogram_lower_high_count_63_d2(close): return f27_mcdt_065_ppo_histogram_lower_high_count_63(close).diff().diff()
def f27_mcdt_066_fast_macd_minus_classical_macd_d2(close): return f27_mcdt_066_fast_macd_minus_classical_macd(close).diff().diff()
def f27_mcdt_067_slow_macd_minus_classical_macd_d2(close): return f27_mcdt_067_slow_macd_minus_classical_macd(close).diff().diff()
def f27_mcdt_068_all_three_macd_above_zero_indicator_d2(close): return f27_mcdt_068_all_three_macd_above_zero_indicator(close).diff().diff()
def f27_mcdt_069_count_configs_with_bearish_cross_in_21d_d2(close): return f27_mcdt_069_count_configs_with_bearish_cross_in_21d(close).diff().diff()
def f27_mcdt_070_macd_ensemble_avg_zscore_252_d2(close): return f27_mcdt_070_macd_ensemble_avg_zscore_252(close).diff().diff()
def f27_mcdt_071_macd_ensemble_dispersion_d2(close): return f27_mcdt_071_macd_ensemble_dispersion(close).diff().diff()
def f27_mcdt_072_multi_horizon_macd_div_count_d2(high, close): return f27_mcdt_072_multi_horizon_macd_div_count(high, close).diff().diff()
def f27_mcdt_073_fast_macd_minus_slow_macd_at_top_d2(high, close): return f27_mcdt_073_fast_macd_minus_slow_macd_at_top(high, close).diff().diff()
def f27_mcdt_074_count_macd_horizons_in_decline_63_d2(close): return f27_mcdt_074_count_macd_horizons_in_decline_63(close).diff().diff()
def f27_mcdt_075_macd_horizon_lead_lag_diff_21_d2(close): return f27_mcdt_075_macd_horizon_lead_lag_diff_21(close).diff().diff()

MACD_TOPPING_DYNAMICS_D2_REGISTRY_001_075 = {
    "f27_mcdt_001_macd_line_12_26_d2": {"inputs": ["close"], "func": f27_mcdt_001_macd_line_12_26_d2},
    "f27_mcdt_002_macd_signal_9_d2": {"inputs": ["close"], "func": f27_mcdt_002_macd_signal_9_d2},
    "f27_mcdt_003_macd_histogram_12_26_9_d2": {"inputs": ["close"], "func": f27_mcdt_003_macd_histogram_12_26_9_d2},
    "f27_mcdt_004_macd_line_5_35_d2": {"inputs": ["close"], "func": f27_mcdt_004_macd_line_5_35_d2},
    "f27_mcdt_005_macd_histogram_5_35_5_d2": {"inputs": ["close"], "func": f27_mcdt_005_macd_histogram_5_35_5_d2},
    "f27_mcdt_006_macd_line_19_39_d2": {"inputs": ["close"], "func": f27_mcdt_006_macd_line_19_39_d2},
    "f27_mcdt_007_macd_histogram_19_39_9_d2": {"inputs": ["close"], "func": f27_mcdt_007_macd_histogram_19_39_9_d2},
    "f27_mcdt_008_ppo_12_26_d2": {"inputs": ["close"], "func": f27_mcdt_008_ppo_12_26_d2},
    "f27_mcdt_009_ppo_signal_9_d2": {"inputs": ["close"], "func": f27_mcdt_009_ppo_signal_9_d2},
    "f27_mcdt_010_ppo_histogram_d2": {"inputs": ["close"], "func": f27_mcdt_010_ppo_histogram_d2},
    "f27_mcdt_011_macd_above_zero_state_d2": {"inputs": ["close"], "func": f27_mcdt_011_macd_above_zero_state_d2},
    "f27_mcdt_012_bars_since_macd_above_zero_start_d2": {"inputs": ["close"], "func": f27_mcdt_012_bars_since_macd_above_zero_start_d2},
    "f27_mcdt_013_bars_since_macd_below_zero_start_d2": {"inputs": ["close"], "func": f27_mcdt_013_bars_since_macd_below_zero_start_d2},
    "f27_mcdt_014_macd_zero_cross_down_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_014_macd_zero_cross_down_indicator_d2},
    "f27_mcdt_015_macd_zero_cross_down_count_252_d2": {"inputs": ["close"], "func": f27_mcdt_015_macd_zero_cross_down_count_252_d2},
    "f27_mcdt_016_fraction_time_macd_above_zero_252_d2": {"inputs": ["close"], "func": f27_mcdt_016_fraction_time_macd_above_zero_252_d2},
    "f27_mcdt_017_macd_current_above_zero_streak_d2": {"inputs": ["close"], "func": f27_mcdt_017_macd_current_above_zero_streak_d2},
    "f27_mcdt_018_macd_max_above_zero_streak_252_d2": {"inputs": ["close"], "func": f27_mcdt_018_macd_max_above_zero_streak_252_d2},
    "f27_mcdt_019_signal_bearish_cross_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_019_signal_bearish_cross_indicator_d2},
    "f27_mcdt_020_signal_bearish_cross_count_63_d2": {"inputs": ["close"], "func": f27_mcdt_020_signal_bearish_cross_count_63_d2},
    "f27_mcdt_021_bars_since_last_signal_bearish_cross_d2": {"inputs": ["close"], "func": f27_mcdt_021_bars_since_last_signal_bearish_cross_d2},
    "f27_mcdt_022_signal_bearish_cross_above_zero_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_022_signal_bearish_cross_above_zero_indicator_d2},
    "f27_mcdt_023_signal_cross_density_in_above_zero_63_d2": {"inputs": ["close"], "func": f27_mcdt_023_signal_cross_density_in_above_zero_63_d2},
    "f27_mcdt_024_signal_bullish_cross_count_63_d2": {"inputs": ["close"], "func": f27_mcdt_024_signal_bullish_cross_count_63_d2},
    "f27_mcdt_025_signal_net_cross_density_63_d2": {"inputs": ["close"], "func": f27_mcdt_025_signal_net_cross_density_63_d2},
    "f27_mcdt_026_signal_bullish_cross_failure_count_252_d2": {"inputs": ["close"], "func": f27_mcdt_026_signal_bullish_cross_failure_count_252_d2},
    "f27_mcdt_027_histogram_above_zero_state_d2": {"inputs": ["close"], "func": f27_mcdt_027_histogram_above_zero_state_d2},
    "f27_mcdt_028_histogram_just_crossed_below_zero_d2": {"inputs": ["close"], "func": f27_mcdt_028_histogram_just_crossed_below_zero_d2},
    "f27_mcdt_029_histogram_peak_decay_21_d2": {"inputs": ["close"], "func": f27_mcdt_029_histogram_peak_decay_21_d2},
    "f27_mcdt_030_histogram_peak_decay_63_d2": {"inputs": ["close"], "func": f27_mcdt_030_histogram_peak_decay_63_d2},
    "f27_mcdt_031_histogram_rolling_max_63_d2": {"inputs": ["close"], "func": f27_mcdt_031_histogram_rolling_max_63_d2},
    "f27_mcdt_032_histogram_lower_high_count_63_d2": {"inputs": ["close"], "func": f27_mcdt_032_histogram_lower_high_count_63_d2},
    "f27_mcdt_033_histogram_double_top_indicator_63_d2": {"inputs": ["close"], "func": f27_mcdt_033_histogram_double_top_indicator_63_d2},
    "f27_mcdt_034_histogram_bars_since_last_252_max_d2": {"inputs": ["close"], "func": f27_mcdt_034_histogram_bars_since_last_252_max_d2},
    "f27_mcdt_035_histogram_consecutive_negatives_streak_d2": {"inputs": ["close"], "func": f27_mcdt_035_histogram_consecutive_negatives_streak_d2},
    "f27_mcdt_036_price_new_63h_macd_below_prior_63_max_d2": {"inputs": ["high", "close"], "func": f27_mcdt_036_price_new_63h_macd_below_prior_63_max_d2},
    "f27_mcdt_037_price_new_252h_macd_below_prior_252_max_d2": {"inputs": ["high", "close"], "func": f27_mcdt_037_price_new_252h_macd_below_prior_252_max_d2},
    "f27_mcdt_038_amplitude_of_macd_div_63_d2": {"inputs": ["high", "close"], "func": f27_mcdt_038_amplitude_of_macd_div_63_d2},
    "f27_mcdt_039_bars_since_last_macd_div_63_d2": {"inputs": ["high", "close"], "func": f27_mcdt_039_bars_since_last_macd_div_63_d2},
    "f27_mcdt_040_rolling_corr_macd_price_63_d2": {"inputs": ["close"], "func": f27_mcdt_040_rolling_corr_macd_price_63_d2},
    "f27_mcdt_041_rolling_corr_macd_price_252_d2": {"inputs": ["close"], "func": f27_mcdt_041_rolling_corr_macd_price_252_d2},
    "f27_mcdt_042_histo_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f27_mcdt_042_histo_div_vs_price_63_d2},
    "f27_mcdt_043_count_macd_div_events_63_d2": {"inputs": ["high", "close"], "func": f27_mcdt_043_count_macd_div_events_63_d2},
    "f27_mcdt_044_count_macd_div_events_252_d2": {"inputs": ["high", "close"], "func": f27_mcdt_044_count_macd_div_events_252_d2},
    "f27_mcdt_045_div_amplitude_zscore_252_d2": {"inputs": ["high", "close"], "func": f27_mcdt_045_div_amplitude_zscore_252_d2},
    "f27_mcdt_046_macd_line_slope_5_d2": {"inputs": ["close"], "func": f27_mcdt_046_macd_line_slope_5_d2},
    "f27_mcdt_047_macd_line_slope_21_d2": {"inputs": ["close"], "func": f27_mcdt_047_macd_line_slope_21_d2},
    "f27_mcdt_048_macd_line_slope_63_d2": {"inputs": ["close"], "func": f27_mcdt_048_macd_line_slope_63_d2},
    "f27_mcdt_049_macd_slope_just_turned_negative_d2": {"inputs": ["close"], "func": f27_mcdt_049_macd_slope_just_turned_negative_d2},
    "f27_mcdt_050_bars_since_macd_slope_turned_negative_d2": {"inputs": ["close"], "func": f27_mcdt_050_bars_since_macd_slope_turned_negative_d2},
    "f27_mcdt_051_macd_max_then_decay_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_051_macd_max_then_decay_indicator_d2},
    "f27_mcdt_052_macd_decay_velocity_from_peak_21_d2": {"inputs": ["close"], "func": f27_mcdt_052_macd_decay_velocity_from_peak_21_d2},
    "f27_mcdt_053_macd_slope_acceleration_5_d2": {"inputs": ["close"], "func": f27_mcdt_053_macd_slope_acceleration_5_d2},
    "f27_mcdt_054_histo_slope_5_d2": {"inputs": ["close"], "func": f27_mcdt_054_histo_slope_5_d2},
    "f27_mcdt_055_histo_slope_turned_negative_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_055_histo_slope_turned_negative_indicator_d2},
    "f27_mcdt_056_ppo_above_zero_state_d2": {"inputs": ["close"], "func": f27_mcdt_056_ppo_above_zero_state_d2},
    "f27_mcdt_057_ppo_bearish_cross_signal_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_057_ppo_bearish_cross_signal_indicator_d2},
    "f27_mcdt_058_ppo_histogram_above_zero_state_d2": {"inputs": ["close"], "func": f27_mcdt_058_ppo_histogram_above_zero_state_d2},
    "f27_mcdt_059_ppo_above_q90_distribution_252_d2": {"inputs": ["close"], "func": f27_mcdt_059_ppo_above_q90_distribution_252_d2},
    "f27_mcdt_060_ppo_persistence_above_zero_252_d2": {"inputs": ["close"], "func": f27_mcdt_060_ppo_persistence_above_zero_252_d2},
    "f27_mcdt_061_ppo_peak_decay_63_d2": {"inputs": ["close"], "func": f27_mcdt_061_ppo_peak_decay_63_d2},
    "f27_mcdt_062_ppo_zscore_252_d2": {"inputs": ["close"], "func": f27_mcdt_062_ppo_zscore_252_d2},
    "f27_mcdt_063_ppo_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f27_mcdt_063_ppo_div_vs_price_63_d2},
    "f27_mcdt_064_ppo_signal_cross_density_63_d2": {"inputs": ["close"], "func": f27_mcdt_064_ppo_signal_cross_density_63_d2},
    "f27_mcdt_065_ppo_histogram_lower_high_count_63_d2": {"inputs": ["close"], "func": f27_mcdt_065_ppo_histogram_lower_high_count_63_d2},
    "f27_mcdt_066_fast_macd_minus_classical_macd_d2": {"inputs": ["close"], "func": f27_mcdt_066_fast_macd_minus_classical_macd_d2},
    "f27_mcdt_067_slow_macd_minus_classical_macd_d2": {"inputs": ["close"], "func": f27_mcdt_067_slow_macd_minus_classical_macd_d2},
    "f27_mcdt_068_all_three_macd_above_zero_indicator_d2": {"inputs": ["close"], "func": f27_mcdt_068_all_three_macd_above_zero_indicator_d2},
    "f27_mcdt_069_count_configs_with_bearish_cross_in_21d_d2": {"inputs": ["close"], "func": f27_mcdt_069_count_configs_with_bearish_cross_in_21d_d2},
    "f27_mcdt_070_macd_ensemble_avg_zscore_252_d2": {"inputs": ["close"], "func": f27_mcdt_070_macd_ensemble_avg_zscore_252_d2},
    "f27_mcdt_071_macd_ensemble_dispersion_d2": {"inputs": ["close"], "func": f27_mcdt_071_macd_ensemble_dispersion_d2},
    "f27_mcdt_072_multi_horizon_macd_div_count_d2": {"inputs": ["high", "close"], "func": f27_mcdt_072_multi_horizon_macd_div_count_d2},
    "f27_mcdt_073_fast_macd_minus_slow_macd_at_top_d2": {"inputs": ["high", "close"], "func": f27_mcdt_073_fast_macd_minus_slow_macd_at_top_d2},
    "f27_mcdt_074_count_macd_horizons_in_decline_63_d2": {"inputs": ["close"], "func": f27_mcdt_074_count_macd_horizons_in_decline_63_d2},
    "f27_mcdt_075_macd_horizon_lead_lag_diff_21_d2": {"inputs": ["close"], "func": f27_mcdt_075_macd_horizon_lead_lag_diff_21_d2},
}
