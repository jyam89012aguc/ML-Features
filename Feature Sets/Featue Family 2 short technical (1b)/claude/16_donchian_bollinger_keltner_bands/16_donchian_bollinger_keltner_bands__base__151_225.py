"""donchian_bollinger_keltner_bands base features 151-225 — Pipeline 1b-technical.

Practitioner gap-fill extension covering Bollinger/Raschke/Faith/Crabel framework:
  * M-top / W-bottom Bollinger band-divergent patterns         (151-159)
  * %B extreme position and divergence (Bollinger)             (160-165)
  * Multi-year BBwidth squeeze regime / release direction      (166-174)
  * Keltner with non-standard ATR multipliers (1, 3)           (175-186)
  * Holy Grail (Raschke)                                       (184-186)
  * Donchian Turtle S1/S2 entry/exit & failure                 (187-199)
  * STARC bands (Stoller)                                      (200-203)
  * TTM Squeeze auxiliary                                      (204-205)
  * Multi-system consensus & divergences                       (206-212)
  * Bandwidth multi-year context & dynamics                    (213-220)
  * Crabel NR4/NR7 inside Keltner / Bollinger setups           (221-225)

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling windows, explicit
min_periods, no centered windows, no .shift(N). Self-contained helpers — no
cross-family imports.
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


def _bars_since(event: pd.Series) -> pd.Series:
    arr = event.fillna(False).astype(bool).to_numpy()
    idx_at = np.where(arr, np.arange(len(arr)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    pos = pd.Series(np.arange(len(arr), dtype=float), index=event.index)
    return pos - last


def _streak(condition: pd.Series) -> pd.Series:
    c = condition.fillna(False)
    grp = (~c).cumsum()
    return c.astype(int).groupby(grp).cumsum().astype(float)


# ---- family-specific helpers ----

def _bbands(close, n=20, mult=2.0):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return mid, mid + mult * sd, mid - mult * sd


def _pct_b(close, n=20, mult=2.0):
    mid, up, lo = _bbands(close, n=n, mult=mult)
    return _safe_div(close - lo, up - lo)


def _bbwidth(close, n=20, mult=2.0):
    mid, up, lo = _bbands(close, n=n, mult=mult)
    return _safe_div(up - lo, mid)


def _keltner(high, low, close, n=20, mult=2.0):
    mid = close.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    atr = _atr(high, low, close, n=n)
    return mid, mid + mult * atr, mid - mult * atr


def _donchian(high, low, n):
    upper = high.rolling(n, min_periods=max(n // 3, 2)).max()
    lower = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return upper, lower


def _starc(high, low, close, n=15, mult=2.0):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n=n)
    return mid, mid + mult * atr, mid - mult * atr


def _adx(high, low, close, n=14):
    up = high.diff()
    dn = -low.diff()
    plus_dm = up.where((up > dn) & (up > 0), 0.0)
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    tr = _true_range(high, low, close)
    atr_n = tr.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    plus_di = 100.0 * _safe_div(plus_dm.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean(), atr_n)
    minus_di = 100.0 * _safe_div(minus_dm.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean(), atr_n)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), (plus_di + minus_di))
    return dx.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()


def _pivot_high_event(high, n=3):
    win = 2 * n + 1
    rmax = high.rolling(win, min_periods=win).max()
    center = high.shift(n)
    return (center == rmax) & rmax.notna()


def _pivot_low_event(low, n=3):
    win = 2 * n + 1
    rmin = low.rolling(win, min_periods=win).min()
    center = low.shift(n)
    return (center == rmin) & rmin.notna()


# ============================================================
# 151-159  M-top / W-bottom Bollinger band-divergent patterns
# ============================================================

def _m_top_event(close: pd.Series, lookback: int = QDAYS, piv_n: int = 3) -> pd.Series:
    """At each bar, did we just confirm a 'Bollinger M-top' — two pivot-highs in
    lookback where 2nd is higher than 1st but %B at 2nd < %B at 1st (negative
    %B divergence)."""
    pctb = _pct_b(close, n=MDAYS, mult=2.0)
    ev = _pivot_high_event(close, n=piv_n)
    # pivot value confirmed at bar t is close.shift(piv_n) at bar t
    pv = close.shift(piv_n).where(ev, np.nan)
    pb_at = pctb.shift(piv_n).where(ev, np.nan)
    # rolling: get the previous pivot value and pctb in lookback prior to this one
    pv_prev = pv.shift(1).ffill(limit=lookback)
    pb_prev = pb_at.shift(1).ffill(limit=lookback)
    cond = ev & (pv > pv_prev) & (pb_at < pb_prev) & pv_prev.notna()
    return cond.fillna(False)


def _m_top_severity(close: pd.Series, lookback: int = QDAYS, piv_n: int = 3) -> pd.Series:
    pctb = _pct_b(close, n=MDAYS, mult=2.0)
    ev = _pivot_high_event(close, n=piv_n)
    pv = close.shift(piv_n).where(ev, np.nan)
    pb_at = pctb.shift(piv_n).where(ev, np.nan)
    pv_prev = pv.shift(1).ffill(limit=lookback)
    pb_prev = pb_at.shift(1).ffill(limit=lookback)
    cond = ev & (pv > pv_prev) & (pb_at < pb_prev) & pv_prev.notna()
    sev = (pb_prev - pb_at).where(cond, 0.0)
    return sev.fillna(0.0)


def f16_dbkb_151_bollinger_m_top_indicator_63d(close: pd.Series) -> pd.Series:
    """Bollinger M-top: two highs in 63d, 2nd higher than 1st but %B at 2nd is
    LOWER (band-divergent double top)."""
    return _m_top_event(close, lookback=QDAYS).astype(float)


def f16_dbkb_152_bollinger_m_top_severity_pct_b_delta(close: pd.Series) -> pd.Series:
    """Magnitude of %B drop between the two highs of the Bollinger M-top pattern."""
    return _m_top_severity(close, lookback=QDAYS)


def f16_dbkb_153_bollinger_m_top_count_252d(close: pd.Series) -> pd.Series:
    """Count of Bollinger M-top events in trailing 252d."""
    ev = _m_top_event(close, lookback=QDAYS).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_154_failed_w_bottom_at_top_zone_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: confirmed W-bottom pivot in 63d that FAILED (didn't make new
    high within next 10d) while close is currently in top quintile of 252d."""
    ev_l = _pivot_low_event(low, n=3)
    # pivot value (low at t-3 confirmed at t)
    pv_l = low.shift(3).where(ev_l, np.nan).ffill(limit=QDAYS)
    # naive W-bottom: latest two pivot lows with 2nd >= 1st
    pv_prev_l = low.shift(3).where(ev_l, np.nan).shift(1).ffill(limit=QDAYS)
    w_event = ev_l & (low.shift(3) >= pv_prev_l) & pv_prev_l.notna()
    # failed: 10d after the W-bottom, max close still below the prior high in 21d
    high_after = close.rolling(10, min_periods=5).max()
    failed = w_event.shift(10).fillna(False) & (close <= high_after.shift(10))
    # in top quintile
    r_max = close.rolling(YDAYS, min_periods=QDAYS).max()
    r_min = close.rolling(YDAYS, min_periods=QDAYS).min()
    pct = _safe_div(close - r_min, r_max - r_min)
    in_top = pct >= 0.8
    return (failed & in_top).astype(float)


def f16_dbkb_155_walking_upper_band_streak_length(close: pd.Series) -> pd.Series:
    """Current consecutive bars closing above Bollinger upper(20, 2σ)."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    return _streak(close > up)


def f16_dbkb_156_walking_upper_band_streak_count_252d(close: pd.Series) -> pd.Series:
    """Distinct walking-upper episodes (streaks of len>=2) in trailing 252d."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    above = (close > up).fillna(False)
    # An episode start: above today and not-above yesterday, streak will be >=2 if also above tomorrow — count starts that lead to streak>=2
    # PIT-safe approximation: count starts that ALREADY had len>=2 by streak series
    streak = _streak(above)
    # Episode start indicator where streak == 2 (first time it reaches 2)
    starts = (streak == 2)
    return starts.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_157_walking_upper_band_streak_avg_length_252d(close: pd.Series) -> pd.Series:
    """Average length of completed walking-upper streaks in trailing 252d."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    above = (close > up).fillna(False)
    streak = _streak(above)
    # streak length on the LAST bar of each episode = streak at last bar before reset
    end = above & (~above.shift(1).fillna(False))  # uses shift(-1) — but only for grouping at PIT we approximate using diff over the streak series
    # PIT-safe alternative: take streak values where streak.shift(1) is 0 — forbidden — use streak.diff()<0
    streak_drop = streak.diff() < 0
    # bar k drop means k-1 was end-of-streak
    ends_pit = streak_drop.shift(0).fillna(False)
    # at bar k where drop, the prior bar's streak length is the previous value
    prior_len = streak.shift(1).where(ends_pit, np.nan)
    sum_len = prior_len.fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    count = ends_pit.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(sum_len, count)


def f16_dbkb_158_first_close_inside_after_walking_streak_indicator(close: pd.Series) -> pd.Series:
    """Indicator: first close back inside Bollinger Bands after a walking-upper
    streak of length >= 3."""
    _, up, lo = _bbands(close, n=20, mult=2.0)
    above = (close > up).fillna(False)
    streak = _streak(above)
    prior_streak = streak.shift(1).fillna(0)
    inside_today = (close <= up) & (close >= lo)
    return ((prior_streak >= 3) & inside_today).astype(float)


def f16_dbkb_159_walking_band_failure_streak_priorlen(close: pd.Series) -> pd.Series:
    """Length of the walking-upper streak that JUST failed (severity)."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    above = (close > up).fillna(False)
    streak = _streak(above)
    drop = (streak.diff() < 0) & (~above)
    return streak.shift(1).where(drop, 0.0).fillna(0.0)


# ============================================================
# 160-165  %B extreme position and divergence
# ============================================================

def f16_dbkb_160_pct_b_extreme_above_1p2_indicator(close: pd.Series) -> pd.Series:
    """Indicator: Bollinger %B > 1.2 — extreme extension above upper band."""
    return (_pct_b(close, n=MDAYS, mult=2.0) > 1.2).astype(float)


def f16_dbkb_161_pct_b_extreme_above_1p2_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where %B > 1.2."""
    return (_pct_b(close, n=MDAYS, mult=2.0) > 1.2).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_162_pct_b_above_1_bars_in_21d(close: pd.Series) -> pd.Series:
    """Count of bars in 21d where %B > 1 (close above upper band)."""
    return (_pct_b(close, n=MDAYS, mult=2.0) > 1).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f16_dbkb_163_pct_b_divergence_price_hh_pct_b_lh_63d(close: pd.Series) -> pd.Series:
    """Bollinger negative divergence: price new 63d high but %B lower than %B at
    prior 63d-max date."""
    pctb = _pct_b(close, n=MDAYS, mult=2.0)
    p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
    at_high = close >= p_max
    # %B at prior 63d high — value of pctb where prior bar reached the running max
    pb_prev_max = pctb.where(close >= close.rolling(QDAYS, min_periods=MDAYS).max(),
                             np.nan).shift(1).ffill(limit=QDAYS)
    return (at_high & (pctb < pb_prev_max)).astype(float)


def f16_dbkb_164_pct_b_divergence_severity_63d(close: pd.Series) -> pd.Series:
    """Magnitude of %B drop in Bollinger negative divergence."""
    pctb = _pct_b(close, n=MDAYS, mult=2.0)
    p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
    at_high = close >= p_max
    pb_prev_max = pctb.where(close >= close.rolling(QDAYS, min_periods=MDAYS).max(),
                             np.nan).shift(1).ffill(limit=QDAYS)
    sev = (pb_prev_max - pctb).where(at_high & (pctb < pb_prev_max), 0.0)
    return sev.fillna(0.0)


def f16_dbkb_165_pct_b_divergence_count_252d(close: pd.Series) -> pd.Series:
    """Count of Bollinger negative-divergence events in trailing 252d."""
    return f16_dbkb_163_pct_b_divergence_price_hh_pct_b_lh_63d(close).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# 166-174  Multi-year BBwidth squeeze / release direction
# ============================================================

def f16_dbkb_166_bbwidth_percentile_in_1260d_low(close: pd.Series) -> pd.Series:
    """Indicator: BBwidth (20,2) in bottom decile of trailing 1260d (multi-year squeeze)."""
    w = _bbwidth(close, n=20, mult=2.0)
    q10 = w.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.1)
    return (w <= q10).astype(float)


def f16_dbkb_167_bbwidth_squeeze_release_direction_bearish_count_252d(close: pd.Series) -> pd.Series:
    """Count in 252d of post-squeeze BEARISH releases: prior 21d had BBwidth in
    bottom decile vs 252d and today close < BB lower."""
    w = _bbwidth(close, n=20, mult=2.0)
    q10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    was_squeeze = (w <= q10).shift(1).rolling(MDAYS, min_periods=WDAYS).max().fillna(0).astype(bool)
    _, _, lo = _bbands(close, n=20, mult=2.0)
    release_bear = was_squeeze & (close < lo)
    return release_bear.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_168_bbwidth_squeeze_release_to_upper_then_fail_count_252d(close: pd.Series) -> pd.Series:
    """Bull-trap squeeze: prior 21d squeeze, broke above upper, then closed back
    below upper within 5d. Count in 252d."""
    w = _bbwidth(close, n=20, mult=2.0)
    q10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    was_squeeze = (w <= q10).shift(1).rolling(MDAYS, min_periods=WDAYS).max().fillna(0).astype(bool)
    _, up, _ = _bbands(close, n=20, mult=2.0)
    broke_up = was_squeeze & (close > up)
    failed = broke_up.shift(5).fillna(False) & (close < up)
    return failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_169_bb_upper_slope_flat_then_down_indicator(close: pd.Series) -> pd.Series:
    """Bollinger stalling-top regime change: upper-band slope over 21d is ~flat
    (|slope|<small) and over 5d is negative."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    s21 = _rolling_slope(up, 21)
    s5 = _rolling_slope(up, 5)
    atr = _atr_safe = close.rolling(MDAYS, min_periods=WDAYS).std()
    return ((s21.abs() < 0.1 * atr) & (s5 < 0)).astype(float)


def f16_dbkb_170_bb_upper_slope_negative_while_close_in_top_decile(close: pd.Series) -> pd.Series:
    """Indicator: BB upper slope (21d) < 0 AND close is in top decile of 252d
    range."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    s = _rolling_slope(up, 21)
    r_max = close.rolling(YDAYS, min_periods=QDAYS).max()
    r_min = close.rolling(YDAYS, min_periods=QDAYS).min()
    pct = _safe_div(close - r_min, r_max - r_min)
    return ((s < 0) & (pct >= 0.9)).astype(float)


def f16_dbkb_171_bb_lower_rising_while_close_at_upper(close: pd.Series) -> pd.Series:
    """Asymmetric contraction at top: BB lower slope (21d) > 0 and close > BB upper."""
    _, up, lo = _bbands(close, n=20, mult=2.0)
    s_lo = _rolling_slope(lo, 21)
    return ((s_lo > 0) & (close > up)).astype(float)


def f16_dbkb_172_bb_band_convergence_at_top_indicator(close: pd.Series) -> pd.Series:
    """BBwidth declining (21d slope < 0) while close in top quintile of 252d range."""
    w = _bbwidth(close, n=20, mult=2.0)
    s = _rolling_slope(w, 21)
    r_max = close.rolling(YDAYS, min_periods=QDAYS).max()
    r_min = close.rolling(YDAYS, min_periods=QDAYS).min()
    pct = _safe_div(close - r_min, r_max - r_min)
    return ((s < 0) & (pct >= 0.8)).astype(float)


def f16_dbkb_173_bollinger_band_of_band_pctile(close: pd.Series) -> pd.Series:
    """BB on BBwidth — percentile of BBwidth in 252d (vol-of-vol regime)."""
    w = _bbwidth(close, n=20, mult=2.0)
    return w.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f16_dbkb_174_band_of_band_upper_break_count_252d(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where BBwidth > (mean + 2 stdev of BBwidth) — vol-of-vol breakouts."""
    w = _bbwidth(close, n=20, mult=2.0)
    m = w.rolling(MDAYS, min_periods=WDAYS).mean()
    s = w.rolling(MDAYS, min_periods=WDAYS).std()
    return (w > m + 2 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# 175-186  Keltner with non-standard multipliers (1, 3) / Holy Grail
# ============================================================

def f16_dbkb_175_keltner_width_1atr_norm_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner channel width (mult 1 ATR — Raschke scalp) normalized by mid."""
    mid, up, lo = _keltner(high, low, close, n=20, mult=1.0)
    return _safe_div(up - lo, mid)


def f16_dbkb_176_keltner_width_3atr_norm_mid(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner channel width (mult 3 ATR — position trade) normalized by mid."""
    mid, up, lo = _keltner(high, low, close, n=20, mult=3.0)
    return _safe_div(up - lo, mid)


def f16_dbkb_177_keltner_1atr_upper_break_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 63d where close > Keltner upper (mult 1 ATR)."""
    _, up, _ = _keltner(high, low, close, n=20, mult=1.0)
    return (close > up).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_178_keltner_3atr_upper_break_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 252d where close > Keltner upper (mult 3 ATR — rare deep stretch)."""
    _, up, _ = _keltner(high, low, close, n=20, mult=3.0)
    return (close > up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_179_keltner_upper_gt_bollinger_upper_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in 63d where Keltner upper (20,2) > Bollinger upper (20,2) — ATR-vol > stdev-vol asymmetry."""
    _, k_up, _ = _keltner(high, low, close, n=20, mult=2.0)
    _, b_up, _ = _bbands(close, n=20, mult=2.0)
    return (k_up > b_up).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_180_keltner_minus_bollinger_upper_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed continuous asymmetry: (Keltner upper - Bollinger upper) / ATR(21)."""
    _, k_up, _ = _keltner(high, low, close, n=20, mult=2.0)
    _, b_up, _ = _bbands(close, n=20, mult=2.0)
    return _safe_div(k_up - b_up, _atr(high, low, close, n=MDAYS))


def f16_dbkb_181_keltner_mid_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of Keltner mid (EMA20) over 252d — long-horizon channel trend."""
    mid, _, _ = _keltner(high, low, close, n=20, mult=2.0)
    return _rolling_slope(mid, YDAYS)


def f16_dbkb_182_walking_keltner_upper_streak_length(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive bars closing above Keltner upper (20, 2 ATR)."""
    _, up, _ = _keltner(high, low, close, n=20, mult=2.0)
    return _streak(close > up)


def f16_dbkb_183_walking_keltner_upper_streak_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distinct walking-upper-Keltner episodes (streak hit 2) in 252d."""
    _, up, _ = _keltner(high, low, close, n=20, mult=2.0)
    streak = _streak((close > up).fillna(False))
    return (streak == 2).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_184_holy_grail_setup_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raschke Holy Grail: ADX(14) > 30 + pullback to Keltner mid (low <= mid) +
    bounce (close > prior close). Count in 252d."""
    adx = _adx(high, low, close, n=14)
    mid, _, _ = _keltner(high, low, close, n=20, mult=2.0)
    setup = (adx > 30) & (low <= mid) & (close > close.shift(1))
    return setup.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_185_holy_grail_failure_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Holy Grail setups that did NOT make a new high within 5 bars. Count in 252d."""
    adx = _adx(high, low, close, n=14)
    mid, _, _ = _keltner(high, low, close, n=20, mult=2.0)
    setup = (adx > 30) & (low <= mid) & (close > close.shift(1))
    fwd_max = high.rolling(5, min_periods=2).max()
    # PIT: at bar t, check that 5 bars BEFORE we had a setup and we did not exceed setup's high in the 5 bars after
    setup5 = setup.shift(5).fillna(False)
    high_at_setup = high.shift(5)
    failed = setup5 & (fwd_max <= high_at_setup)
    return failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_186_bars_since_last_holy_grail(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the last Holy Grail setup confirmed."""
    adx = _adx(high, low, close, n=14)
    mid, _, _ = _keltner(high, low, close, n=20, mult=2.0)
    setup = (adx > 30) & (low <= mid) & (close > close.shift(1))
    return _bars_since(setup.fillna(False))


# ============================================================
# 187-199  Donchian / Turtle setups
# ============================================================

def f16_dbkb_187_donchian_20_break_today_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Turtle S1: close > prior-20 Donchian upper (entry today)."""
    up, _ = _donchian(high, low, 20)
    return (close > up.shift(1)).astype(float)


def f16_dbkb_188_donchian_20_break_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of Donchian-20 breakouts (close > prior-20 high) in 63d."""
    up, _ = _donchian(high, low, 20)
    return (close > up.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_189_donchian_55_break_today_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Turtle S2 trigger: close > prior-55 Donchian upper."""
    up, _ = _donchian(high, low, 55)
    return (close > up.shift(1)).astype(float)


def f16_dbkb_190_donchian_55_break_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of Donchian-55 breakouts in 252d."""
    up, _ = _donchian(high, low, 55)
    return (close > up.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_191_donchian_10_breakdown_today_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Turtle S1 long-exit: close < prior-10 Donchian lower."""
    _, lo = _donchian(high, low, 10)
    return (close < lo.shift(1)).astype(float)


def f16_dbkb_192_donchian_20_breakdown_today_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Turtle S2 exit: close < prior-20 Donchian lower."""
    _, lo = _donchian(high, low, 20)
    return (close < lo.shift(1)).astype(float)


def f16_dbkb_193_donchian_20_break_then_close_below_5d_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Turtle whipsaw: D20 break then close back below the broken level within 5d.
    Count in 252d."""
    up, _ = _donchian(high, low, 20)
    prior_up = up.shift(1)
    break_ev = close > prior_up
    # within next 5 bars (PIT: at bar t check if any 1..5 bars back had break AND today close < that bar's prior_up)
    fail_today = pd.Series(False, index=close.index)
    for k in range(1, 6):
        be_k = break_ev.shift(k).fillna(False)
        lvl_k = prior_up.shift(k)
        fail_today = fail_today | (be_k & (close < lvl_k))
    return fail_today.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_194_donchian_55_break_then_fail_within_10d_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """D55 break then close back below the broken level within 10d. Count in 252d."""
    up, _ = _donchian(high, low, 55)
    prior_up = up.shift(1)
    break_ev = close > prior_up
    fail_today = pd.Series(False, index=close.index)
    for k in range(1, 11):
        be_k = break_ev.shift(k).fillna(False)
        lvl_k = prior_up.shift(k)
        fail_today = fail_today | (be_k & (close < lvl_k))
    return fail_today.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_195_donchian_narrow_channel_p10_indicator(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Donchian-20 width in bottom decile of trailing 252d."""
    up, lo = _donchian(high, low, 20)
    w = up - lo
    q10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (w <= q10).astype(float)


def f16_dbkb_196_donchian_channel_asymmetry_upper_vs_lower(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Asymmetry: (upper - close) - (close - lower), normalized by channel width."""
    up, lo = _donchian(high, low, 20)
    w = up - lo
    return _safe_div((up - close) - (close - lo), w)


def f16_dbkb_197_bars_since_last_donchian_20_breakout(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last close > prior-20 Donchian upper."""
    up, _ = _donchian(high, low, 20)
    ev = (close > up.shift(1)).fillna(False)
    return _bars_since(ev)


def f16_dbkb_198_bars_since_last_donchian_55_breakout(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last close > prior-55 Donchian upper."""
    up, _ = _donchian(high, low, 55)
    ev = (close > up.shift(1)).fillna(False)
    return _bars_since(ev)


def f16_dbkb_199_donchian_breakout_extension_atr_since_break(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized extension above the most-recent D20 breakout-level."""
    up, _ = _donchian(high, low, 20)
    prior_up = up.shift(1)
    ev = (close > prior_up).fillna(False)
    # last breakout level: prior_up at the bar of the break, then ffill
    lvl = prior_up.where(ev, np.nan).ffill()
    return _safe_div(close - lvl, _atr(high, low, close, n=MDAYS))


# ============================================================
# 200-203  STARC (Stoller)
# ============================================================

def f16_dbkb_200_starc_width_pctile_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """STARC (15, 2 ATR) width as percentile in trailing 252d."""
    _, up, lo = _starc(high, low, close, n=15, mult=2.0)
    w = up - lo
    return w.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f16_dbkb_201_starc_upper_break_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in 63d where close > STARC upper (15, 2 ATR)."""
    _, up, _ = _starc(high, low, close, n=15, mult=2.0)
    return (close > up).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_202_starc_upper_break_then_fail_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """STARC upper break then close below STARC mid within 5d. Count in 252d."""
    mid, up, _ = _starc(high, low, close, n=15, mult=2.0)
    ev = (close > up).fillna(False)
    failed = pd.Series(False, index=close.index)
    for k in range(1, 6):
        failed = failed | (ev.shift(k).fillna(False) & (close < mid))
    return failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_203_starc_minus_bb_upper_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Alternative band asymmetry: (STARC upper - BB upper) / ATR(21)."""
    _, s_up, _ = _starc(high, low, close, n=15, mult=2.0)
    _, b_up, _ = _bbands(close, n=20, mult=2.0)
    return _safe_div(s_up - b_up, _atr(high, low, close, n=MDAYS))


# ============================================================
# 204-205  TTM Squeeze auxiliary
# ============================================================

def f16_dbkb_204_ttm_squeeze_duration_active(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive bars in TTM squeeze (BB inside KC at 1.5 ATR)."""
    _, b_up, b_lo = _bbands(close, n=MDAYS, mult=2.0)
    _, k_up, k_lo = _keltner(high, low, close, n=MDAYS, mult=1.5)
    in_sq = (b_up < k_up) & (b_lo > k_lo)
    return _streak(in_sq.fillna(False))


def f16_dbkb_205_ttm_squeeze_release_was_bearish_recency(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recency-weighted indicator: was the LAST TTM squeeze release bearish (close < BB lower at release)?
    Returns 1 / (1 + bars_since_bearish_release), 0 if no bearish release yet."""
    _, b_up, b_lo = _bbands(close, n=MDAYS, mult=2.0)
    _, k_up, k_lo = _keltner(high, low, close, n=MDAYS, mult=1.5)
    in_sq = ((b_up < k_up) & (b_lo > k_lo)).fillna(False)
    release = in_sq.shift(1).fillna(False) & ~in_sq
    bear_release = release & (close < b_lo)
    bs = _bars_since(bear_release)
    return _safe_div(1.0, 1.0 + bs).fillna(0.0)


# ============================================================
# 206-212  Multi-system consensus & divergences
# ============================================================

def f16_dbkb_206_bb_donchian_upper_agreement_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in 63d where BOTH BB upper AND Donchian upper were broken on the same day."""
    _, b_up, _ = _bbands(close, n=20, mult=2.0)
    d_up, _ = _donchian(high, low, 20)
    both = (close > b_up) & (close > d_up.shift(1))
    return both.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_207_bb_keltner_divergence_bbsqueeze_kcwiden(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: BBwidth in bottom quintile of 252d AND Keltner width in top
    quintile of 252d (unusual quiet stdev with high ATR)."""
    bbw = _bbwidth(close, n=20, mult=2.0)
    _, k_up, k_lo = _keltner(high, low, close, n=20, mult=2.0)
    kcw = _safe_div(k_up - k_lo, ((k_up + k_lo) / 2.0))
    bb_lo_q = bbw.rolling(YDAYS, min_periods=QDAYS).quantile(0.2)
    kc_hi_q = kcw.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((bbw <= bb_lo_q) & (kcw >= kc_hi_q)).astype(float)


def f16_dbkb_208_triple_band_upper_break_consensus_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in 252d where BB + Keltner + Donchian uppers all broken on the same day."""
    _, b_up, _ = _bbands(close, n=20, mult=2.0)
    _, k_up, _ = _keltner(high, low, close, n=20, mult=2.0)
    d_up, _ = _donchian(high, low, 20)
    triple = (close > b_up) & (close > k_up) & (close > d_up.shift(1))
    return triple.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_209_triple_band_consensus_then_fail_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Triple-break days that closed below BB mid within 5d. Count in 252d."""
    mid, b_up, _ = _bbands(close, n=20, mult=2.0)
    _, k_up, _ = _keltner(high, low, close, n=20, mult=2.0)
    d_up, _ = _donchian(high, low, 20)
    triple = ((close > b_up) & (close > k_up) & (close > d_up.shift(1))).fillna(False)
    failed = pd.Series(False, index=close.index)
    for k in range(1, 6):
        failed = failed | (triple.shift(k).fillna(False) & (close < mid))
    return failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_210_bb_short_break_long_mid_channel_indicator(close: pd.Series) -> pd.Series:
    """BB(10) upper broken AND BB(50) %position in [0.4, 0.6] (short break inside long mid)."""
    _, up10, _ = _bbands(close, n=10, mult=2.0)
    pb50 = _pct_b(close, n=50, mult=2.0)
    return ((close > up10) & (pb50 >= 0.4) & (pb50 <= 0.6)).astype(float)


def f16_dbkb_211_bb_10_vs_50_pct_b_divergence(close: pd.Series) -> pd.Series:
    """Indicator: %B(10) > 1 while %B(50) declining over 21d."""
    pb10 = _pct_b(close, n=10, mult=2.0)
    pb50 = _pct_b(close, n=50, mult=2.0)
    declining = pb50 < pb50.shift(MDAYS)
    return ((pb10 > 1.0) & declining).astype(float)


def f16_dbkb_212_bb_horizon_inconsistency_index(close: pd.Series) -> pd.Series:
    """Std of %B across horizons {10, 20, 50}."""
    pb10 = _pct_b(close, n=10, mult=2.0)
    pb20 = _pct_b(close, n=20, mult=2.0)
    pb50 = _pct_b(close, n=50, mult=2.0)
    df = pd.concat([pb10.rename("a"), pb20.rename("b"), pb50.rename("c")], axis=1)
    return df.std(axis=1)


# ============================================================
# 213-220  Bandwidth multi-year context & dynamics
# ============================================================

def f16_dbkb_213_bbwidth_zscore_in_1260d(close: pd.Series) -> pd.Series:
    """Z-score of BBwidth (20,2) in trailing 1260d (multi-year vol regime)."""
    w = _bbwidth(close, n=20, mult=2.0)
    return _rolling_zscore(w, DDAYS_5Y, min_periods=YDAYS)


def f16_dbkb_214_bbwidth_trend_rising_21d_indicator(close: pd.Series) -> pd.Series:
    """Indicator: BBwidth slope > 0 over BOTH 21d AND 63d windows."""
    w = _bbwidth(close, n=20, mult=2.0)
    s21 = _rolling_slope(w, 21)
    s63 = _rolling_slope(w, 63)
    return ((s21 > 0) & (s63 > 0)).astype(float)


def f16_dbkb_215_bbwidth_vol_of_vol_21d(close: pd.Series) -> pd.Series:
    """Std of BBwidth's 5d log-changes over 21d (vol-of-vol)."""
    w = _bbwidth(close, n=20, mult=2.0)
    lc = _safe_log(w).diff(WDAYS)
    return lc.rolling(MDAYS, min_periods=WDAYS).std()


def f16_dbkb_216_bbwidth_max_to_min_ratio_63d(close: pd.Series) -> pd.Series:
    """Expansion amplitude: max(BBwidth, 63d) / min(BBwidth, 63d)."""
    w = _bbwidth(close, n=20, mult=2.0)
    wmax = w.rolling(QDAYS, min_periods=MDAYS).max()
    wmin = w.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(wmax, wmin)


def f16_dbkb_217_bb_squeeze_release_max_excursion_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Energy released post-squeeze: max ATR-units excursion in 21d AFTER a
    squeeze (bottom-decile BBwidth was within prior 21d)."""
    bbw = _bbwidth(close, n=20, mult=2.0)
    q10 = bbw.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    was_sq_21d = (bbw <= q10).shift(1).rolling(MDAYS, min_periods=WDAYS).max().fillna(0).astype(bool)
    atr = _atr(high, low, close, n=MDAYS)
    # max |close - mid| in 21d after — PIT-safe: use 21d rolling max of |close-mid| with right-anchor
    mid = close.rolling(20, min_periods=10).mean()
    excursion = (close - mid).abs()
    max_exc_21 = excursion.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(max_exc_21, atr).where(was_sq_21d, np.nan)


def f16_dbkb_218_consec_squeeze_release_no_new_high_count(close: pd.Series) -> pd.Series:
    """Count of consecutive squeeze releases that failed to make new 21d high.
    A 'failure': release event AND price 21d later did not exceed price at release."""
    bbw = _bbwidth(close, n=20, mult=2.0)
    q10 = bbw.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    in_sq = bbw <= q10
    release = (in_sq.shift(1).fillna(False) & ~in_sq).fillna(False)
    # check 21d after release: PIT — at bar t, was there a release at t-21 and close at t <= close at t-21
    release_21_ago = release.shift(MDAYS).fillna(False)
    close_21_ago = close.shift(MDAYS)
    failure = release_21_ago & (close <= close_21_ago)
    # count consecutive failures (streak) of failure events themselves
    return failure.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_219_bb_upper_touch_with_lower_volume_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weak-touch tops: bars in 21d where close > BB upper AND volume < volume's 21d SMA."""
    _, up, _ = _bbands(close, n=20, mult=2.0)
    v_sma = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (close > up) & (volume < v_sma)
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f16_dbkb_220_keltner_upper_touch_volume_zscore_avg_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume z-score on bars where high >= Keltner upper, over 63d."""
    _, up, _ = _keltner(high, low, close, n=MDAYS, mult=2.0)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return vz.where(high >= up, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# 221-225  Crabel NR4/NR7 inside Keltner / Bollinger setups
# ============================================================

def _nrk(high, low, k):
    rng = high - low
    rmin = rng.rolling(k, min_periods=k).min()
    return rng == rmin


def f16_dbkb_221_nr4_inside_keltner_upper_zone_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Crabel NR4 (today's range is the narrowest of last 4 bars) while close
    in upper zone of Keltner (close >= mid + 0.5 × (upper-mid)). Count in 63d."""
    nr4 = _nrk(high, low, 4)
    mid, up, _ = _keltner(high, low, close, n=MDAYS, mult=2.0)
    in_zone = close >= mid + 0.5 * (up - mid)
    return (nr4 & in_zone).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_222_nr7_inside_keltner_upper_zone_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Crabel NR7 (narrowest of last 7 bars) inside upper Keltner zone. Count in 63d."""
    nr7 = _nrk(high, low, 7)
    mid, up, _ = _keltner(high, low, close, n=MDAYS, mult=2.0)
    in_zone = close >= mid + 0.5 * (up - mid)
    return (nr7 & in_zone).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_223_nr7_in_bb_squeeze_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7 today AND BBwidth in bottom decile of 252d (compressed coil)."""
    nr7 = _nrk(high, low, 7)
    bbw = _bbwidth(close, n=20, mult=2.0)
    q10 = bbw.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (nr7 & (bbw <= q10)).astype(float)


def f16_dbkb_224_id_nr4_at_bb_upper_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Crabel ID-NR4: inside-day (high<prior high AND low>prior low) + NR4 + close > BB upper."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    nr4 = _nrk(high, low, 4)
    _, up, _ = _bbands(close, n=20, mult=2.0)
    return (inside & nr4 & (close > up)).astype(float)


def f16_dbkb_225_bb_pct_b_max_minus_min_21d(close: pd.Series) -> pd.Series:
    """Band-position range cycle amplitude: max(%B,21d) - min(%B,21d)."""
    pb = _pct_b(close, n=MDAYS, mult=2.0)
    return pb.rolling(MDAYS, min_periods=WDAYS).max() - pb.rolling(MDAYS, min_periods=WDAYS).min()


# ============================================================
#                         REGISTRY 151-225
# ============================================================

DONCHIAN_BOLLINGER_KELTNER_BANDS_BASE_REGISTRY_151_225 = {
    "f16_dbkb_151_bollinger_m_top_indicator_63d": {"inputs": ["close"], "func": f16_dbkb_151_bollinger_m_top_indicator_63d},
    "f16_dbkb_152_bollinger_m_top_severity_pct_b_delta": {"inputs": ["close"], "func": f16_dbkb_152_bollinger_m_top_severity_pct_b_delta},
    "f16_dbkb_153_bollinger_m_top_count_252d": {"inputs": ["close"], "func": f16_dbkb_153_bollinger_m_top_count_252d},
    "f16_dbkb_154_failed_w_bottom_at_top_zone_indicator": {"inputs": ["close", "low"], "func": f16_dbkb_154_failed_w_bottom_at_top_zone_indicator},
    "f16_dbkb_155_walking_upper_band_streak_length": {"inputs": ["close"], "func": f16_dbkb_155_walking_upper_band_streak_length},
    "f16_dbkb_156_walking_upper_band_streak_count_252d": {"inputs": ["close"], "func": f16_dbkb_156_walking_upper_band_streak_count_252d},
    "f16_dbkb_157_walking_upper_band_streak_avg_length_252d": {"inputs": ["close"], "func": f16_dbkb_157_walking_upper_band_streak_avg_length_252d},
    "f16_dbkb_158_first_close_inside_after_walking_streak_indicator": {"inputs": ["close"], "func": f16_dbkb_158_first_close_inside_after_walking_streak_indicator},
    "f16_dbkb_159_walking_band_failure_streak_priorlen": {"inputs": ["close"], "func": f16_dbkb_159_walking_band_failure_streak_priorlen},
    "f16_dbkb_160_pct_b_extreme_above_1p2_indicator": {"inputs": ["close"], "func": f16_dbkb_160_pct_b_extreme_above_1p2_indicator},
    "f16_dbkb_161_pct_b_extreme_above_1p2_count_63d": {"inputs": ["close"], "func": f16_dbkb_161_pct_b_extreme_above_1p2_count_63d},
    "f16_dbkb_162_pct_b_above_1_bars_in_21d": {"inputs": ["close"], "func": f16_dbkb_162_pct_b_above_1_bars_in_21d},
    "f16_dbkb_163_pct_b_divergence_price_hh_pct_b_lh_63d": {"inputs": ["close"], "func": f16_dbkb_163_pct_b_divergence_price_hh_pct_b_lh_63d},
    "f16_dbkb_164_pct_b_divergence_severity_63d": {"inputs": ["close"], "func": f16_dbkb_164_pct_b_divergence_severity_63d},
    "f16_dbkb_165_pct_b_divergence_count_252d": {"inputs": ["close"], "func": f16_dbkb_165_pct_b_divergence_count_252d},
    "f16_dbkb_166_bbwidth_percentile_in_1260d_low": {"inputs": ["close"], "func": f16_dbkb_166_bbwidth_percentile_in_1260d_low},
    "f16_dbkb_167_bbwidth_squeeze_release_direction_bearish_count_252d": {"inputs": ["close"], "func": f16_dbkb_167_bbwidth_squeeze_release_direction_bearish_count_252d},
    "f16_dbkb_168_bbwidth_squeeze_release_to_upper_then_fail_count_252d": {"inputs": ["close"], "func": f16_dbkb_168_bbwidth_squeeze_release_to_upper_then_fail_count_252d},
    "f16_dbkb_169_bb_upper_slope_flat_then_down_indicator": {"inputs": ["close"], "func": f16_dbkb_169_bb_upper_slope_flat_then_down_indicator},
    "f16_dbkb_170_bb_upper_slope_negative_while_close_in_top_decile": {"inputs": ["close"], "func": f16_dbkb_170_bb_upper_slope_negative_while_close_in_top_decile},
    "f16_dbkb_171_bb_lower_rising_while_close_at_upper": {"inputs": ["close"], "func": f16_dbkb_171_bb_lower_rising_while_close_at_upper},
    "f16_dbkb_172_bb_band_convergence_at_top_indicator": {"inputs": ["close"], "func": f16_dbkb_172_bb_band_convergence_at_top_indicator},
    "f16_dbkb_173_bollinger_band_of_band_pctile": {"inputs": ["close"], "func": f16_dbkb_173_bollinger_band_of_band_pctile},
    "f16_dbkb_174_band_of_band_upper_break_count_252d": {"inputs": ["close"], "func": f16_dbkb_174_band_of_band_upper_break_count_252d},
    "f16_dbkb_175_keltner_width_1atr_norm_mid": {"inputs": ["high", "low", "close"], "func": f16_dbkb_175_keltner_width_1atr_norm_mid},
    "f16_dbkb_176_keltner_width_3atr_norm_mid": {"inputs": ["high", "low", "close"], "func": f16_dbkb_176_keltner_width_3atr_norm_mid},
    "f16_dbkb_177_keltner_1atr_upper_break_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_177_keltner_1atr_upper_break_count_63d},
    "f16_dbkb_178_keltner_3atr_upper_break_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_178_keltner_3atr_upper_break_count_252d},
    "f16_dbkb_179_keltner_upper_gt_bollinger_upper_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_179_keltner_upper_gt_bollinger_upper_count_63d},
    "f16_dbkb_180_keltner_minus_bollinger_upper_atr_norm": {"inputs": ["high", "low", "close"], "func": f16_dbkb_180_keltner_minus_bollinger_upper_atr_norm},
    "f16_dbkb_181_keltner_mid_slope_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_181_keltner_mid_slope_252d},
    "f16_dbkb_182_walking_keltner_upper_streak_length": {"inputs": ["high", "low", "close"], "func": f16_dbkb_182_walking_keltner_upper_streak_length},
    "f16_dbkb_183_walking_keltner_upper_streak_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_183_walking_keltner_upper_streak_count_252d},
    "f16_dbkb_184_holy_grail_setup_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_184_holy_grail_setup_count_252d},
    "f16_dbkb_185_holy_grail_failure_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_185_holy_grail_failure_count_252d},
    "f16_dbkb_186_bars_since_last_holy_grail": {"inputs": ["high", "low", "close"], "func": f16_dbkb_186_bars_since_last_holy_grail},
    "f16_dbkb_187_donchian_20_break_today_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_187_donchian_20_break_today_indicator},
    "f16_dbkb_188_donchian_20_break_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_188_donchian_20_break_count_63d},
    "f16_dbkb_189_donchian_55_break_today_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_189_donchian_55_break_today_indicator},
    "f16_dbkb_190_donchian_55_break_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_190_donchian_55_break_count_252d},
    "f16_dbkb_191_donchian_10_breakdown_today_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_191_donchian_10_breakdown_today_indicator},
    "f16_dbkb_192_donchian_20_breakdown_today_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_192_donchian_20_breakdown_today_indicator},
    "f16_dbkb_193_donchian_20_break_then_close_below_5d_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_193_donchian_20_break_then_close_below_5d_count_252d},
    "f16_dbkb_194_donchian_55_break_then_fail_within_10d_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_194_donchian_55_break_then_fail_within_10d_count_252d},
    "f16_dbkb_195_donchian_narrow_channel_p10_indicator": {"inputs": ["high", "low"], "func": f16_dbkb_195_donchian_narrow_channel_p10_indicator},
    "f16_dbkb_196_donchian_channel_asymmetry_upper_vs_lower": {"inputs": ["high", "low", "close"], "func": f16_dbkb_196_donchian_channel_asymmetry_upper_vs_lower},
    "f16_dbkb_197_bars_since_last_donchian_20_breakout": {"inputs": ["high", "low", "close"], "func": f16_dbkb_197_bars_since_last_donchian_20_breakout},
    "f16_dbkb_198_bars_since_last_donchian_55_breakout": {"inputs": ["high", "low", "close"], "func": f16_dbkb_198_bars_since_last_donchian_55_breakout},
    "f16_dbkb_199_donchian_breakout_extension_atr_since_break": {"inputs": ["high", "low", "close"], "func": f16_dbkb_199_donchian_breakout_extension_atr_since_break},
    "f16_dbkb_200_starc_width_pctile_in_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_200_starc_width_pctile_in_252d},
    "f16_dbkb_201_starc_upper_break_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_201_starc_upper_break_count_63d},
    "f16_dbkb_202_starc_upper_break_then_fail_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_202_starc_upper_break_then_fail_count_252d},
    "f16_dbkb_203_starc_minus_bb_upper_atr_norm": {"inputs": ["high", "low", "close"], "func": f16_dbkb_203_starc_minus_bb_upper_atr_norm},
    "f16_dbkb_204_ttm_squeeze_duration_active": {"inputs": ["high", "low", "close"], "func": f16_dbkb_204_ttm_squeeze_duration_active},
    "f16_dbkb_205_ttm_squeeze_release_was_bearish_recency": {"inputs": ["high", "low", "close"], "func": f16_dbkb_205_ttm_squeeze_release_was_bearish_recency},
    "f16_dbkb_206_bb_donchian_upper_agreement_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_206_bb_donchian_upper_agreement_count_63d},
    "f16_dbkb_207_bb_keltner_divergence_bbsqueeze_kcwiden": {"inputs": ["close", "high", "low"], "func": f16_dbkb_207_bb_keltner_divergence_bbsqueeze_kcwiden},
    "f16_dbkb_208_triple_band_upper_break_consensus_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_208_triple_band_upper_break_consensus_count_252d},
    "f16_dbkb_209_triple_band_consensus_then_fail_count_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_209_triple_band_consensus_then_fail_count_252d},
    "f16_dbkb_210_bb_short_break_long_mid_channel_indicator": {"inputs": ["close"], "func": f16_dbkb_210_bb_short_break_long_mid_channel_indicator},
    "f16_dbkb_211_bb_10_vs_50_pct_b_divergence": {"inputs": ["close"], "func": f16_dbkb_211_bb_10_vs_50_pct_b_divergence},
    "f16_dbkb_212_bb_horizon_inconsistency_index": {"inputs": ["close"], "func": f16_dbkb_212_bb_horizon_inconsistency_index},
    "f16_dbkb_213_bbwidth_zscore_in_1260d": {"inputs": ["close"], "func": f16_dbkb_213_bbwidth_zscore_in_1260d},
    "f16_dbkb_214_bbwidth_trend_rising_21d_indicator": {"inputs": ["close"], "func": f16_dbkb_214_bbwidth_trend_rising_21d_indicator},
    "f16_dbkb_215_bbwidth_vol_of_vol_21d": {"inputs": ["close"], "func": f16_dbkb_215_bbwidth_vol_of_vol_21d},
    "f16_dbkb_216_bbwidth_max_to_min_ratio_63d": {"inputs": ["close"], "func": f16_dbkb_216_bbwidth_max_to_min_ratio_63d},
    "f16_dbkb_217_bb_squeeze_release_max_excursion_atr_21d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_217_bb_squeeze_release_max_excursion_atr_21d},
    "f16_dbkb_218_consec_squeeze_release_no_new_high_count": {"inputs": ["close"], "func": f16_dbkb_218_consec_squeeze_release_no_new_high_count},
    "f16_dbkb_219_bb_upper_touch_with_lower_volume_count_21d": {"inputs": ["close", "volume"], "func": f16_dbkb_219_bb_upper_touch_with_lower_volume_count_21d},
    "f16_dbkb_220_keltner_upper_touch_volume_zscore_avg_63d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_220_keltner_upper_touch_volume_zscore_avg_63d},
    "f16_dbkb_221_nr4_inside_keltner_upper_zone_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_221_nr4_inside_keltner_upper_zone_count_63d},
    "f16_dbkb_222_nr7_inside_keltner_upper_zone_count_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_222_nr7_inside_keltner_upper_zone_count_63d},
    "f16_dbkb_223_nr7_in_bb_squeeze_indicator": {"inputs": ["close", "high", "low"], "func": f16_dbkb_223_nr7_in_bb_squeeze_indicator},
    "f16_dbkb_224_id_nr4_at_bb_upper_indicator": {"inputs": ["close", "high", "low"], "func": f16_dbkb_224_id_nr4_at_bb_upper_indicator},
    "f16_dbkb_225_bb_pct_b_max_minus_min_21d": {"inputs": ["close"], "func": f16_dbkb_225_bb_pct_b_max_minus_min_21d},
}
