"""divergence_detection base features 451-525 — Pipeline 1b-technical (precision extension).

Individual signals: Heikin-Ashi divergences (smoothed bars give distinct signals),
Schaff Trend Cycle (STC), TSV (Time Segmented Volume), Cutler RSI (SMA-smoothed,
distinct from Wilder), Slow Stochastic (3d-smoothed), Connors RSI (3-component
composite as oscillator), per-volume-oscillator dwell-time variants.

Each feature = single discrete signal. PIT-clean. Self-contained.
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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


# ---------------------------- divergence helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    return ((ps > 0) & (osl < 0)).astype(float).where(ps.notna() & osl.notna(), np.nan)


def _shift_div_bearish(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _shift_div_hidden_bearish(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price < pp) & (osc > op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


# ---------------------------- Heikin-Ashi helpers ----------------------------

def _ha_close(open_, high, low, close):
    return (open_ + high + low + close) / 4.0


def _ha_open(open_, close):
    """Heikin-Ashi open = (prior HA open + prior HA close) / 2. Recursive — vectorized via state."""
    n = len(open_)
    ha_o = np.full(n, np.nan)
    cl = close.values; op = open_.values
    if n > 0:
        ha_o[0] = (op[0] + cl[0]) / 2.0
        for i in range(1, n):
            ha_c_prev = (op[i - 1] + cl[i - 1] + cl[i - 1] + cl[i - 1]) / 4.0  # approximate via standard formula on prior
            ha_o[i] = (ha_o[i - 1] + ha_c_prev) / 2.0
    return pd.Series(ha_o, index=open_.index)


def _ha_close_simple(open_, high, low, close):
    return (open_ + high + low + close) / 4.0


def _ha_high(high, open_, close):
    return pd.concat([high, _ha_open(open_, close), _ha_close_simple(open_, high, high, close)], axis=1).max(axis=1)


def _ha_low(low, open_, close):
    return pd.concat([low, _ha_open(open_, close), _ha_close_simple(open_, low, low, close)], axis=1).min(axis=1)


def _ha_body(open_, high, low, close):
    return _ha_close(open_, high, low, close) - _ha_open(open_, close)


# ---------------------------- Schaff Trend Cycle (STC) ----------------------------

def _macd_line_simple(close, fast=23, slow=50):
    return _ema(close, fast) - _ema(close, slow)


def _stc(close, fast=23, slow=50, n_cycle=10):
    """Schaff Trend Cycle: double-stochastic of MACD. Returns 0-100 oscillator."""
    macd = _macd_line_simple(close, fast, slow)
    # First stoch: %K of MACD over n_cycle
    mn = macd.rolling(n_cycle, min_periods=max(n_cycle // 3, 2)).min()
    mx = macd.rolling(n_cycle, min_periods=max(n_cycle // 3, 2)).max()
    k1 = 100.0 * _safe_div(macd - mn, mx - mn)
    d1 = _ema(k1, 3)
    # Second stoch: %K of d1
    mn2 = d1.rolling(n_cycle, min_periods=max(n_cycle // 3, 2)).min()
    mx2 = d1.rolling(n_cycle, min_periods=max(n_cycle // 3, 2)).max()
    k2 = 100.0 * _safe_div(d1 - mn2, mx2 - mn2)
    return _ema(k2, 3)


# ---------------------------- TSV (Time Segmented Volume) ----------------------------

def _tsv(close, volume, n=18):
    """Worden's Time Segmented Volume: cumulative sum of (close.diff() * volume) smoothed."""
    raw = (close.diff() * volume).fillna(0)
    return raw.rolling(n, min_periods=max(n // 3, 2)).sum()


# ---------------------------- Cutler RSI (SMA-smoothed) ----------------------------

def _cutler_rsi(close, n=14):
    """Cutler RSI uses SMA of gains/losses instead of EMA — different smoothing from Wilder."""
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = _sma(gain, n)
    avg_loss = _sma(loss, n)
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


# ---------------------------- Slow Stochastic ----------------------------

def _stoch_k_fast(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _slow_stoch_k(high, low, close, n=14, d=3):
    """Slow Stoch %K: SMA-d-smoothed fast %K (distinct from raw)."""
    return _sma(_stoch_k_fast(high, low, close, n), d)


def _slow_stoch_d(high, low, close, n=14, d=3, dd=3):
    """Slow Stoch %D: SMA-dd of slow %K."""
    return _sma(_slow_stoch_k(high, low, close, n, d), dd)


# ---------------------------- Connors RSI ----------------------------

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0); loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(ag, al))


def _streak_value(close):
    """Days-since-last-direction-change streak (positive for up streaks, negative for down)."""
    direction = np.sign(close.diff()).fillna(0).astype(int)
    n = len(close)
    streak = np.zeros(n, dtype=float)
    for i in range(1, n):
        if direction.iloc[i] == 0:
            streak[i] = 0.0
        elif direction.iloc[i] == direction.iloc[i - 1]:
            streak[i] = streak[i - 1] + direction.iloc[i]
        else:
            streak[i] = direction.iloc[i]
    return pd.Series(streak, index=close.index)


def _streak_rsi(close, n=2):
    """RSI(2) applied to the streak series — Connors RSI component 2."""
    return _rsi_wilder(_streak_value(close), n)


def _percent_rank_3d(close, n=100):
    """Percent-rank of today's 1-day return within trailing n bars (Connors RSI component 3)."""
    ret = close.pct_change()
    return _pct_rank(ret, n) * 100.0


def _connors_rsi(close, rsi_n=3, streak_n=2, rank_n=100):
    """Connors RSI = mean of [RSI(3), streak-RSI(2), percent-rank-3d(100)]."""
    return (_rsi_wilder(close, rsi_n)
            + _streak_rsi(close, streak_n)
            + _percent_rank_3d(close, rank_n)) / 3.0


# ---------------------------- volume oscillator helpers (reused for dwell-time) ----------------------------

def _cmf(high, low, close, volume, n=20):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    mfv = (mfm * volume).fillna(0)
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     volume.rolling(n, min_periods=max(n // 3, 2)).sum())


def _force_index(close, volume, n=13):
    raw = close.diff() * volume
    return _ema(raw, n)


def _eom(high, low, volume, n=14):
    midpoint = (high + low) / 2.0
    distance = midpoint.diff()
    box_ratio = _safe_div(volume / 1e6, high - low)
    return _sma(_safe_div(distance, box_ratio), n)


def _klinger(high, low, close, volume, fast=34, slow=55):
    hlc = (high + low + close) / 3.0
    trend = np.sign(hlc.diff()).fillna(0)
    dm = high - low
    cm = dm.rolling(2, min_periods=1).sum()
    vf = volume * trend * (2.0 * _safe_div(dm, cm) - 1.0).abs() * 100.0
    return _ema(vf, fast) - _ema(vf, slow)


def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    return (mfm * volume).fillna(0).cumsum()


def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    ad = _ad_line(high, low, close, volume)
    return _ema(ad, fast) - _ema(ad, slow)


# ============================================================
# Bucket A — Heikin-Ashi divergences (451-465)
# ============================================================

def f32_divd_451_heikin_ashi_close_slope_div_sign_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and Heikin-Ashi-close over 63d."""
    return _slope_div_sign(close, _ha_close(open, high, low, close), QDAYS)


def f32_divd_452_heikin_ashi_close_slope_div_sign_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on HA-close, 252d."""
    return _slope_div_sign(close, _ha_close(open, high, low, close), YDAYS)


def f32_divd_453_heikin_ashi_close_shift_div_indicator_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs HA-close, 63d."""
    return _shift_div_bearish(close, _ha_close(open, high, low, close), QDAYS)


def f32_divd_454_heikin_ashi_close_zscore_gap_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(HA-close,63) — extension gap on smoothed bars."""
    return _zscore_gap(close, _ha_close(open, high, low, close), QDAYS)


def f32_divd_455_heikin_ashi_close_rolling_corr_price_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and HA-close."""
    return _rolling_corr_pearson(_safe_log(close), _ha_close(open, high, low, close), QDAYS)


def f32_divd_456_heikin_ashi_close_hidden_bearish_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish divergence on HA-close, 63d."""
    return _shift_div_hidden_bearish(close, _ha_close(open, high, low, close), QDAYS)


def f32_divd_457_heikin_ashi_body_pct_value(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Heikin-Ashi body as percentage of HA bar range (signed)."""
    body = _ha_body(open, high, low, close)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body, rng)


def f32_divd_458_heikin_ashi_consecutive_bullish_bar_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bullish-HA-bar streak length (HA close > HA open)."""
    flag = (_ha_close(open, high, low, close) > _ha_open(open, close)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f32_divd_459_heikin_ashi_consecutive_bearish_bar_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bearish-HA-bar streak length."""
    flag = (_ha_close(open, high, low, close) < _ha_open(open, close)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f32_divd_460_heikin_ashi_bullish_to_bearish_flip_event_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where HA bar flipped from bullish (prior) to bearish (today)."""
    ha_c = _ha_close(open, high, low, close); ha_o = _ha_open(open, close)
    cur_bear = (ha_c < ha_o).astype(int)
    prev_bull = (ha_c.shift(1) > ha_o.shift(1)).astype(int)
    return (cur_bear & prev_bull).astype(float)


def f32_divd_461_heikin_ashi_no_lower_wick_bullish_streak(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Streak of consecutive HA bars with no lower wick (HA bar open == HA low) — strong-trend signal."""
    ha_o = _ha_open(open, close)
    ha_l = pd.concat([low, ha_o], axis=1).min(axis=1)
    no_lower = ((ha_o - ha_l).abs() < 1e-9).astype(int)
    grp = (no_lower == 0).cumsum()
    return no_lower.groupby(grp).cumsum().astype(float)


def f32_divd_462_heikin_ashi_close_at_252d_high_x_bearish_bar_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close near 252d max AND current HA bar is bearish (top + smoothed reversal)."""
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    ha_bear = (_ha_close(open, high, low, close) < _ha_open(open, close)).astype(float)
    return (near * ha_bear).where(near.notna() & ha_bear.notna(), np.nan)


def f32_divd_463_heikin_ashi_body_pct_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of HA body% over 252d."""
    body = _ha_body(open, high, low, close)
    rng = (high - low).replace(0, np.nan)
    return _rolling_zscore(_safe_div(body, rng), YDAYS)


def f32_divd_464_heikin_ashi_consecutive_bullish_streak_above_5_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when current HA-bullish streak >= 5 bars."""
    flag = (_ha_close(open, high, low, close) > _ha_open(open, close)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum().astype(float)
    return (streak >= 5).astype(float)


def f32_divd_465_heikin_ashi_flip_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of HA bull-to-bear flip events in trailing 252d (regime instability)."""
    ha_c = _ha_close(open, high, low, close); ha_o = _ha_open(open, close)
    flip = ((ha_c < ha_o) & (ha_c.shift(1) > ha_o.shift(1))).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket B — Schaff Trend Cycle (STC) divergences (466-475)
# ============================================================

def f32_divd_466_stc_value(close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle value (0..100), Fast 23, Slow 50, cycle 10."""
    return _stc(close)


def f32_divd_467_stc_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and STC over 63d."""
    return _slope_div_sign(close, _stc(close), QDAYS)


def f32_divd_468_stc_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs STC, 63d."""
    return _shift_div_bearish(close, _stc(close), QDAYS)


def f32_divd_469_stc_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(STC,63)."""
    return _zscore_gap(close, _stc(close), QDAYS)


def f32_divd_470_stc_above_75_indicator(close: pd.Series) -> pd.Series:
    """+1 when STC > 75 (canonical overbought threshold)."""
    s = _stc(close)
    return (s > 75).astype(float).where(s.notna(), np.nan)


def f32_divd_471_stc_below_25_indicator(close: pd.Series) -> pd.Series:
    """+1 when STC < 25 (canonical oversold)."""
    s = _stc(close)
    return (s < 25).astype(float).where(s.notna(), np.nan)


def f32_divd_472_stc_above_75_persistence_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where STC > 75."""
    s = _stc(close)
    return (s > 75).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_473_days_since_stc_cross_75_down(close: pd.Series) -> pd.Series:
    """Bars since most recent STC bearish cross of 75 (from above to below)."""
    s = _stc(close)
    flag = ((s.shift(1) > 75) & (s <= 75)).astype(float)
    return _bars_since_true(flag)


def f32_divd_474_stc_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of STC."""
    return _rolling_slope(_stc(close), MDAYS)


def f32_divd_475_stc_above_75_x_close_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when STC > 75 AND close within 1% of 252d max."""
    s = _stc(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((s > 75) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


# ============================================================
# Bucket C — TSV (Time Segmented Volume) divergences (476-485)
# ============================================================

def f32_divd_476_tsv_value(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Worden Time Segmented Volume (n=18)."""
    return _tsv(close, volume, 18)


def f32_divd_477_tsv_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on TSV(18), 63d."""
    return _slope_div_sign(close, _tsv(close, volume, 18), QDAYS)


def f32_divd_478_tsv_shift_div_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on TSV, 63d."""
    return _shift_div_bearish(close, _tsv(close, volume, 18), QDAYS)


def f32_divd_479_tsv_zscore_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(TSV,63)."""
    return _zscore_gap(close, _tsv(close, volume, 18), QDAYS)


def f32_divd_480_tsv_rolling_corr_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and TSV."""
    return _rolling_corr_pearson(_safe_log(close), _tsv(close, volume, 18), QDAYS)


def f32_divd_481_tsv_hidden_bearish_div_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + TSV HH, 63d."""
    return _shift_div_hidden_bearish(close, _tsv(close, volume, 18), QDAYS)


def f32_divd_482_tsv_above_zero_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when TSV > 0 (positive money flow regime)."""
    t = _tsv(close, volume, 18)
    return (t > 0).astype(float).where(t.notna(), np.nan)


def f32_divd_483_days_since_tsv_zero_cross_bearish(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent bearish TSV zero-cross."""
    t = _tsv(close, volume, 18)
    flag = ((t.shift(1) > 0) & (t <= 0)).astype(float)
    return _bars_since_true(flag)


def f32_divd_484_tsv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of TSV."""
    return _rolling_slope(_tsv(close, volume, 18), QDAYS)


def f32_divd_485_tsv_div_count_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of TSV 21d bearish-shift divergences in trailing 252d."""
    flag = _shift_div_bearish(close, _tsv(close, volume, 18), MDAYS).fillna(0)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket D — Cutler RSI divergences (486-495)
# ============================================================

def f32_divd_486_cutler_rsi14_value(close: pd.Series) -> pd.Series:
    """Cutler RSI(14) — SMA-smoothed variant, distinct from Wilder."""
    return _cutler_rsi(close, 14)


def f32_divd_487_cutler_rsi14_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Cutler RSI(14), 63d."""
    return _slope_div_sign(close, _cutler_rsi(close, 14), QDAYS)


def f32_divd_488_cutler_rsi14_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Cutler RSI, 63d."""
    return _shift_div_bearish(close, _cutler_rsi(close, 14), QDAYS)


def f32_divd_489_cutler_rsi14_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Cutler RSI,63)."""
    return _zscore_gap(close, _cutler_rsi(close, 14), QDAYS)


def f32_divd_490_cutler_rsi14_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Cutler RSI HH, 63d."""
    return _shift_div_hidden_bearish(close, _cutler_rsi(close, 14), QDAYS)


def f32_divd_491_cutler_rsi14_above_70_indicator(close: pd.Series) -> pd.Series:
    """+1 when Cutler RSI(14) > 70 (overbought)."""
    r = _cutler_rsi(close, 14)
    return (r > 70).astype(float).where(r.notna(), np.nan)


def f32_divd_492_cutler_rsi14_dwell_above_70_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Cutler RSI(14) > 70."""
    r = _cutler_rsi(close, 14)
    return (r > 70).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_493_cutler_rsi14_minus_wilder_rsi14_diff(close: pd.Series) -> pd.Series:
    """Cutler RSI(14) - Wilder RSI(14) — smoothing-method divergence."""
    return _cutler_rsi(close, 14) - _rsi_wilder(close, 14)


def f32_divd_494_cutler_rsi14_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Cutler RSI(14)."""
    return _rolling_corr_pearson(_safe_log(close), _cutler_rsi(close, 14), QDAYS)


def f32_divd_495_cutler_rsi14_div_dwell_time_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Cutler RSI 63d slope-div is bearish."""
    div = _slope_div_sign(close, _cutler_rsi(close, 14), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket E — Slow Stochastic divergences (496-505)
# ============================================================

def f32_divd_496_slow_stoch_k_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stoch %K (14, 3) — SMA-3-smoothed fast %K."""
    return _slow_stoch_k(high, low, close, 14, 3)


def f32_divd_497_slow_stoch_d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stoch %D (14, 3, 3) — SMA-3 of slow %K."""
    return _slow_stoch_d(high, low, close, 14, 3, 3)


def f32_divd_498_slow_stoch_k_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Slow Stoch %K, 63d."""
    return _slope_div_sign(close, _slow_stoch_k(high, low, close, 14, 3), QDAYS)


def f32_divd_499_slow_stoch_k_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Slow Stoch %K, 63d."""
    return _shift_div_bearish(close, _slow_stoch_k(high, low, close, 14, 3), QDAYS)


def f32_divd_500_slow_stoch_k_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Slow Stoch %K,63)."""
    return _zscore_gap(close, _slow_stoch_k(high, low, close, 14, 3), QDAYS)


def f32_divd_501_slow_stoch_k_above_80_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when Slow Stoch %K > 80 (overbought)."""
    k = _slow_stoch_k(high, low, close, 14, 3)
    return (k > 80).astype(float).where(k.notna(), np.nan)


def f32_divd_502_slow_stoch_k_d_bearish_cross_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where Slow Stoch %K crosses below %D (classic bearish cross)."""
    k = _slow_stoch_k(high, low, close, 14, 3); d = _slow_stoch_d(high, low, close, 14, 3, 3)
    return ((k.shift(1) > d.shift(1)) & (k <= d)).astype(float).where(k.notna() & d.notna(), np.nan)


def f32_divd_503_days_since_slow_stoch_bearish_cross(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent Slow Stoch %K bearish cross of %D."""
    k = _slow_stoch_k(high, low, close, 14, 3); d = _slow_stoch_d(high, low, close, 14, 3, 3)
    flag = ((k.shift(1) > d.shift(1)) & (k <= d)).astype(float)
    return _bars_since_true(flag)


def f32_divd_504_slow_stoch_k_minus_d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stoch %K - %D — direction indicator (positive = bullish slope)."""
    return _slow_stoch_k(high, low, close, 14, 3) - _slow_stoch_d(high, low, close, 14, 3, 3)


def f32_divd_505_slow_stoch_k_above_80_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Slow Stoch %K > 80."""
    k = _slow_stoch_k(high, low, close, 14, 3)
    return (k > 80).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket F — Connors RSI components and divergence (506-515)
# ============================================================

def f32_divd_506_connors_rsi_value(close: pd.Series) -> pd.Series:
    """Connors RSI value (mean of RSI(3), streak-RSI(2), pct-rank-3d)."""
    return _connors_rsi(close)


def f32_divd_507_connors_rsi_component_1_rsi3_value(close: pd.Series) -> pd.Series:
    """Connors RSI component 1: RSI(3) standalone."""
    return _rsi_wilder(close, 3)


def f32_divd_508_connors_rsi_component_2_streak_rsi2_value(close: pd.Series) -> pd.Series:
    """Connors RSI component 2: RSI(2) of streak series (up/down day-counter)."""
    return _streak_rsi(close, 2)


def f32_divd_509_connors_rsi_component_3_percent_rank_3d_100(close: pd.Series) -> pd.Series:
    """Connors RSI component 3: percent-rank-of-1d-return within trailing 100d."""
    return _percent_rank_3d(close, 100)


def f32_divd_510_connors_rsi_above_90_indicator(close: pd.Series) -> pd.Series:
    """+1 when Connors RSI > 90 (classic overbought)."""
    c = _connors_rsi(close)
    return (c > 90).astype(float).where(c.notna(), np.nan)


def f32_divd_511_connors_rsi_below_10_indicator(close: pd.Series) -> pd.Series:
    """+1 when Connors RSI < 10 (classic oversold)."""
    c = _connors_rsi(close)
    return (c < 10).astype(float).where(c.notna(), np.nan)


def f32_divd_512_connors_rsi_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Connors RSI, 63d."""
    return _slope_div_sign(close, _connors_rsi(close), QDAYS)


def f32_divd_513_connors_rsi_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Connors RSI,63)."""
    return _zscore_gap(close, _connors_rsi(close), QDAYS)


def f32_divd_514_connors_rsi_above_90_dwell_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars with Connors RSI > 90."""
    c = _connors_rsi(close)
    return (c > 90).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_515_streak_value_current(close: pd.Series) -> pd.Series:
    """Signed streak counter (positive for up streaks, negative for down)."""
    return _streak_value(close)


# ============================================================
# Bucket G — Per-volume-oscillator dwell-time (516-525)
# ============================================================

def f32_divd_516_cmf_div_dwell_time_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where CMF 63d bearish slope-div sign fires."""
    div = _slope_div_sign(close, _cmf(high, low, close, volume, 20), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_517_force_index_div_dwell_time_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Force Index 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _force_index(close, volume, 13), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_518_eom_div_dwell_time_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Ease-of-Movement 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _eom(high, low, volume, 14), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_519_klinger_div_dwell_time_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Klinger 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _klinger(high, low, close, volume), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_520_chaikin_osc_div_dwell_time_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Chaikin Osc 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS).fillna(0)
    return div.rolling(MDAYS, min_periods=WDAYS).sum()


def f32_divd_521_cmf_div_dwell_time_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where CMF 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _cmf(high, low, close, volume, 20), QDAYS).fillna(0)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f32_divd_522_force_index_div_dwell_time_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where Force Index 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _force_index(close, volume, 13), QDAYS).fillna(0)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f32_divd_523_klinger_div_dwell_time_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where Klinger 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _klinger(high, low, close, volume), QDAYS).fillna(0)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f32_divd_524_chaikin_osc_div_dwell_time_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where Chaikin Osc 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS).fillna(0)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f32_divd_525_eom_div_dwell_time_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where EOM 63d bearish slope-div fires."""
    div = _slope_div_sign(close, _eom(high, low, volume, 14), QDAYS).fillna(0)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# REGISTRY
# ============================================================

DIVERGENCE_DETECTION_BASE_REGISTRY_451_525 = {
    "f32_divd_451_heikin_ashi_close_slope_div_sign_63d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_451_heikin_ashi_close_slope_div_sign_63d},
    "f32_divd_452_heikin_ashi_close_slope_div_sign_252d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_452_heikin_ashi_close_slope_div_sign_252d},
    "f32_divd_453_heikin_ashi_close_shift_div_indicator_63d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_453_heikin_ashi_close_shift_div_indicator_63d},
    "f32_divd_454_heikin_ashi_close_zscore_gap_63d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_454_heikin_ashi_close_zscore_gap_63d},
    "f32_divd_455_heikin_ashi_close_rolling_corr_price_63d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_455_heikin_ashi_close_rolling_corr_price_63d},
    "f32_divd_456_heikin_ashi_close_hidden_bearish_63d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_456_heikin_ashi_close_hidden_bearish_63d},
    "f32_divd_457_heikin_ashi_body_pct_value": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_457_heikin_ashi_body_pct_value},
    "f32_divd_458_heikin_ashi_consecutive_bullish_bar_streak": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_458_heikin_ashi_consecutive_bullish_bar_streak},
    "f32_divd_459_heikin_ashi_consecutive_bearish_bar_streak": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_459_heikin_ashi_consecutive_bearish_bar_streak},
    "f32_divd_460_heikin_ashi_bullish_to_bearish_flip_event_indicator": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_460_heikin_ashi_bullish_to_bearish_flip_event_indicator},
    "f32_divd_461_heikin_ashi_no_lower_wick_bullish_streak": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_461_heikin_ashi_no_lower_wick_bullish_streak},
    "f32_divd_462_heikin_ashi_close_at_252d_high_x_bearish_bar_indicator": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_462_heikin_ashi_close_at_252d_high_x_bearish_bar_indicator},
    "f32_divd_463_heikin_ashi_body_pct_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_463_heikin_ashi_body_pct_zscore_252d},
    "f32_divd_464_heikin_ashi_consecutive_bullish_streak_above_5_indicator": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_464_heikin_ashi_consecutive_bullish_streak_above_5_indicator},
    "f32_divd_465_heikin_ashi_flip_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f32_divd_465_heikin_ashi_flip_count_252d},
    "f32_divd_466_stc_value": {"inputs": ["close"], "func": f32_divd_466_stc_value},
    "f32_divd_467_stc_slope_div_sign_63d": {"inputs": ["close"], "func": f32_divd_467_stc_slope_div_sign_63d},
    "f32_divd_468_stc_shift_div_indicator_63d": {"inputs": ["close"], "func": f32_divd_468_stc_shift_div_indicator_63d},
    "f32_divd_469_stc_zscore_gap_63d": {"inputs": ["close"], "func": f32_divd_469_stc_zscore_gap_63d},
    "f32_divd_470_stc_above_75_indicator": {"inputs": ["close"], "func": f32_divd_470_stc_above_75_indicator},
    "f32_divd_471_stc_below_25_indicator": {"inputs": ["close"], "func": f32_divd_471_stc_below_25_indicator},
    "f32_divd_472_stc_above_75_persistence_21d": {"inputs": ["close"], "func": f32_divd_472_stc_above_75_persistence_21d},
    "f32_divd_473_days_since_stc_cross_75_down": {"inputs": ["close"], "func": f32_divd_473_days_since_stc_cross_75_down},
    "f32_divd_474_stc_slope_21d": {"inputs": ["close"], "func": f32_divd_474_stc_slope_21d},
    "f32_divd_475_stc_above_75_x_close_at_252d_high_indicator": {"inputs": ["close"], "func": f32_divd_475_stc_above_75_x_close_at_252d_high_indicator},
    "f32_divd_476_tsv_value": {"inputs": ["close", "volume"], "func": f32_divd_476_tsv_value},
    "f32_divd_477_tsv_slope_div_sign_63d": {"inputs": ["close", "volume"], "func": f32_divd_477_tsv_slope_div_sign_63d},
    "f32_divd_478_tsv_shift_div_indicator_63d": {"inputs": ["close", "volume"], "func": f32_divd_478_tsv_shift_div_indicator_63d},
    "f32_divd_479_tsv_zscore_gap_63d": {"inputs": ["close", "volume"], "func": f32_divd_479_tsv_zscore_gap_63d},
    "f32_divd_480_tsv_rolling_corr_price_63d": {"inputs": ["close", "volume"], "func": f32_divd_480_tsv_rolling_corr_price_63d},
    "f32_divd_481_tsv_hidden_bearish_div_63d": {"inputs": ["close", "volume"], "func": f32_divd_481_tsv_hidden_bearish_div_63d},
    "f32_divd_482_tsv_above_zero_indicator": {"inputs": ["close", "volume"], "func": f32_divd_482_tsv_above_zero_indicator},
    "f32_divd_483_days_since_tsv_zero_cross_bearish": {"inputs": ["close", "volume"], "func": f32_divd_483_days_since_tsv_zero_cross_bearish},
    "f32_divd_484_tsv_slope_63d": {"inputs": ["close", "volume"], "func": f32_divd_484_tsv_slope_63d},
    "f32_divd_485_tsv_div_count_in_252d": {"inputs": ["close", "volume"], "func": f32_divd_485_tsv_div_count_in_252d},
    "f32_divd_486_cutler_rsi14_value": {"inputs": ["close"], "func": f32_divd_486_cutler_rsi14_value},
    "f32_divd_487_cutler_rsi14_slope_div_sign_63d": {"inputs": ["close"], "func": f32_divd_487_cutler_rsi14_slope_div_sign_63d},
    "f32_divd_488_cutler_rsi14_shift_div_indicator_63d": {"inputs": ["close"], "func": f32_divd_488_cutler_rsi14_shift_div_indicator_63d},
    "f32_divd_489_cutler_rsi14_zscore_gap_63d": {"inputs": ["close"], "func": f32_divd_489_cutler_rsi14_zscore_gap_63d},
    "f32_divd_490_cutler_rsi14_hidden_bearish_div_63d": {"inputs": ["close"], "func": f32_divd_490_cutler_rsi14_hidden_bearish_div_63d},
    "f32_divd_491_cutler_rsi14_above_70_indicator": {"inputs": ["close"], "func": f32_divd_491_cutler_rsi14_above_70_indicator},
    "f32_divd_492_cutler_rsi14_dwell_above_70_21d": {"inputs": ["close"], "func": f32_divd_492_cutler_rsi14_dwell_above_70_21d},
    "f32_divd_493_cutler_rsi14_minus_wilder_rsi14_diff": {"inputs": ["close"], "func": f32_divd_493_cutler_rsi14_minus_wilder_rsi14_diff},
    "f32_divd_494_cutler_rsi14_rolling_corr_price_63d": {"inputs": ["close"], "func": f32_divd_494_cutler_rsi14_rolling_corr_price_63d},
    "f32_divd_495_cutler_rsi14_div_dwell_time_21d": {"inputs": ["close"], "func": f32_divd_495_cutler_rsi14_div_dwell_time_21d},
    "f32_divd_496_slow_stoch_k_value": {"inputs": ["high", "low", "close"], "func": f32_divd_496_slow_stoch_k_value},
    "f32_divd_497_slow_stoch_d_value": {"inputs": ["high", "low", "close"], "func": f32_divd_497_slow_stoch_d_value},
    "f32_divd_498_slow_stoch_k_slope_div_sign_63d": {"inputs": ["high", "low", "close"], "func": f32_divd_498_slow_stoch_k_slope_div_sign_63d},
    "f32_divd_499_slow_stoch_k_shift_div_indicator_63d": {"inputs": ["high", "low", "close"], "func": f32_divd_499_slow_stoch_k_shift_div_indicator_63d},
    "f32_divd_500_slow_stoch_k_zscore_gap_63d": {"inputs": ["high", "low", "close"], "func": f32_divd_500_slow_stoch_k_zscore_gap_63d},
    "f32_divd_501_slow_stoch_k_above_80_indicator": {"inputs": ["high", "low", "close"], "func": f32_divd_501_slow_stoch_k_above_80_indicator},
    "f32_divd_502_slow_stoch_k_d_bearish_cross_event_indicator": {"inputs": ["high", "low", "close"], "func": f32_divd_502_slow_stoch_k_d_bearish_cross_event_indicator},
    "f32_divd_503_days_since_slow_stoch_bearish_cross": {"inputs": ["high", "low", "close"], "func": f32_divd_503_days_since_slow_stoch_bearish_cross},
    "f32_divd_504_slow_stoch_k_minus_d_diff": {"inputs": ["high", "low", "close"], "func": f32_divd_504_slow_stoch_k_minus_d_diff},
    "f32_divd_505_slow_stoch_k_above_80_dwell_21d": {"inputs": ["high", "low", "close"], "func": f32_divd_505_slow_stoch_k_above_80_dwell_21d},
    "f32_divd_506_connors_rsi_value": {"inputs": ["close"], "func": f32_divd_506_connors_rsi_value},
    "f32_divd_507_connors_rsi_component_1_rsi3_value": {"inputs": ["close"], "func": f32_divd_507_connors_rsi_component_1_rsi3_value},
    "f32_divd_508_connors_rsi_component_2_streak_rsi2_value": {"inputs": ["close"], "func": f32_divd_508_connors_rsi_component_2_streak_rsi2_value},
    "f32_divd_509_connors_rsi_component_3_percent_rank_3d_100": {"inputs": ["close"], "func": f32_divd_509_connors_rsi_component_3_percent_rank_3d_100},
    "f32_divd_510_connors_rsi_above_90_indicator": {"inputs": ["close"], "func": f32_divd_510_connors_rsi_above_90_indicator},
    "f32_divd_511_connors_rsi_below_10_indicator": {"inputs": ["close"], "func": f32_divd_511_connors_rsi_below_10_indicator},
    "f32_divd_512_connors_rsi_slope_div_sign_63d": {"inputs": ["close"], "func": f32_divd_512_connors_rsi_slope_div_sign_63d},
    "f32_divd_513_connors_rsi_zscore_gap_63d": {"inputs": ["close"], "func": f32_divd_513_connors_rsi_zscore_gap_63d},
    "f32_divd_514_connors_rsi_above_90_dwell_21d": {"inputs": ["close"], "func": f32_divd_514_connors_rsi_above_90_dwell_21d},
    "f32_divd_515_streak_value_current": {"inputs": ["close"], "func": f32_divd_515_streak_value_current},
    "f32_divd_516_cmf_div_dwell_time_21d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_516_cmf_div_dwell_time_21d},
    "f32_divd_517_force_index_div_dwell_time_21d": {"inputs": ["close", "volume"], "func": f32_divd_517_force_index_div_dwell_time_21d},
    "f32_divd_518_eom_div_dwell_time_21d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_518_eom_div_dwell_time_21d},
    "f32_divd_519_klinger_div_dwell_time_21d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_519_klinger_div_dwell_time_21d},
    "f32_divd_520_chaikin_osc_div_dwell_time_21d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_520_chaikin_osc_div_dwell_time_21d},
    "f32_divd_521_cmf_div_dwell_time_63d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_521_cmf_div_dwell_time_63d},
    "f32_divd_522_force_index_div_dwell_time_63d": {"inputs": ["close", "volume"], "func": f32_divd_522_force_index_div_dwell_time_63d},
    "f32_divd_523_klinger_div_dwell_time_63d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_523_klinger_div_dwell_time_63d},
    "f32_divd_524_chaikin_osc_div_dwell_time_63d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_524_chaikin_osc_div_dwell_time_63d},
    "f32_divd_525_eom_div_dwell_time_63d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_525_eom_div_dwell_time_63d},
}
