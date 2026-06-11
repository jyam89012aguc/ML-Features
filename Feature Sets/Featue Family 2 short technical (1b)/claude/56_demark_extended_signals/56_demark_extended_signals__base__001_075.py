"""demark_extended_signals base features 001-075 - Pipeline 1b-technical.

150 distinct hypotheses across __base__001_075.py and __base__076_150.py.
Each feature encodes a *different concept*.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers - no cross-family imports.
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
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float)
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _rolling_corr(a, b, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return a.rolling(n, min_periods=min_periods).corr(b)

def _td_setup_count_sell(close, lookback=4):
    """TD Sell Setup count: bars where close > close[t-lookback]. Resets when broken."""
    cmp_ = (close > close.shift(lookback)).astype(float)
    arr = cmp_.values
    out = np.full(len(arr), 0.0, dtype=float)
    run = 0
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            run = 0
        elif arr[i] > 0.5:
            run = min(run + 1, 13)
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=close.index)


def _td_setup_count_buy(close, lookback=4):
    """TD Buy Setup count: bars where close < close[t-lookback]."""
    cmp_ = (close < close.shift(lookback)).astype(float)
    arr = cmp_.values
    out = np.full(len(arr), 0.0, dtype=float)
    run = 0
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            run = 0
        elif arr[i] > 0.5:
            run = min(run + 1, 13)
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=close.index)


def _bars_since_last_event(ind):
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan, dtype=float)
    last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _td_differential_bearish(high, low, close):
    """Bearish TD Differential: close>close[-1], buying-pressure decreases, selling-pressure increases."""
    bp_t = close - low
    bp_p = close.shift(1) - low.shift(1)
    sp_t = high - close
    sp_p = high.shift(1) - close.shift(1)
    cond = (close > close.shift(1)) & (bp_t < bp_p) & (sp_t > sp_p)
    return cond.astype(float).where(close.notna() & low.notna() & high.notna(), np.nan)


def _td_differential_bullish(high, low, close):
    """Bullish TD Differential mirror: close<close[-1], buying-pressure increases, selling-pressure decreases."""
    bp_t = close - low; bp_p = close.shift(1) - low.shift(1)
    sp_t = high - close; sp_p = high.shift(1) - close.shift(1)
    cond = (close < close.shift(1)) & (bp_t > bp_p) & (sp_t < sp_p)
    return cond.astype(float).where(close.notna() & low.notna() & high.notna(), np.nan)


def _td_reverse_differential_bearish(high, low, close):
    """Bearish TD Reverse Differential: close<close[-1], BP increases, SP decreases (paradoxical sell)."""
    bp_t = close - low; bp_p = close.shift(1) - low.shift(1)
    sp_t = high - close; sp_p = high.shift(1) - close.shift(1)
    cond = (close < close.shift(1)) & (bp_t > bp_p) & (sp_t < sp_p)
    return cond.astype(float).where(close.notna() & low.notna() & high.notna(), np.nan)


def _td_anti_differential_bearish(close):
    """Anti-Differential bearish 5-bar pattern: close down/up/down/up/down."""
    c0 = close; c1 = close.shift(1); c2 = close.shift(2); c3 = close.shift(3); c4 = close.shift(4)
    # t-4 down, t-3 up, t-2 down, t-1 up, t down
    cond = ((c4 < close.shift(5)) & (c3 > c4) & (c2 < c3) & (c1 > c2) & (c0 < c1))
    return cond.astype(float).where(close.notna(), np.nan)


def _td_anti_differential_bullish(close):
    """Anti-Differential bullish 5-bar pattern: close up/down/up/down/up."""
    c0 = close; c1 = close.shift(1); c2 = close.shift(2); c3 = close.shift(3); c4 = close.shift(4)
    cond = ((c4 > close.shift(5)) & (c3 < c4) & (c2 > c3) & (c1 < c2) & (c0 > c1))
    return cond.astype(float).where(close.notna(), np.nan)


def _td_clop_bearish(open_, close):
    """Bearish CLOP: open > prior close AND open > prior open AND close < open."""
    cond = (open_ > close.shift(1)) & (open_ > open_.shift(1)) & (close < open_)
    return cond.astype(float).where(open_.notna() & close.notna(), np.nan)


def _td_clop_bullish(open_, close):
    """Bullish CLOP mirror."""
    cond = (open_ < close.shift(1)) & (open_ < open_.shift(1)) & (close > open_)
    return cond.astype(float).where(open_.notna() & close.notna(), np.nan)


def _td_clopwin_bearish(open_, close):
    """Bearish CLOPWIN: open AND close BOTH within prior open-close range, prior bar UP, current bar DOWN."""
    prior_up = close.shift(1) > open_.shift(1)
    prior_hi = pd.concat([open_.shift(1), close.shift(1)], axis=1).max(axis=1)
    prior_lo = pd.concat([open_.shift(1), close.shift(1)], axis=1).min(axis=1)
    inside = (open_ >= prior_lo) & (open_ <= prior_hi) & (close >= prior_lo) & (close <= prior_hi)
    cur_down = close < open_
    cond = prior_up & inside & cur_down
    return cond.astype(float).where(open_.notna() & close.notna(), np.nan)


def _td_clopwin_bullish(open_, close):
    prior_dn = close.shift(1) < open_.shift(1)
    prior_hi = pd.concat([open_.shift(1), close.shift(1)], axis=1).max(axis=1)
    prior_lo = pd.concat([open_.shift(1), close.shift(1)], axis=1).min(axis=1)
    inside = (open_ >= prior_lo) & (open_ <= prior_hi) & (close >= prior_lo) & (close <= prior_hi)
    cur_up = close > open_
    cond = prior_dn & inside & cur_up
    return cond.astype(float).where(open_.notna() & close.notna(), np.nan)


def _td_camouflage_bearish(open_, high, low, close):
    """Bearish Camouflage: close > prior close (apparent strength) BUT close < open AND low < prior low (true distribution)."""
    cond = (close > close.shift(1)) & (close < open_) & (low < low.shift(1))
    return cond.astype(float).where(close.notna() & open_.notna() & low.notna(), np.nan)


def _td_camouflage_bullish(open_, high, low, close):
    cond = (close < close.shift(1)) & (close > open_) & (high > high.shift(1))
    return cond.astype(float).where(close.notna() & open_.notna() & high.notna(), np.nan)


def _td_open_bearish(open_, high, close):
    """Bearish TD Open: open > prior high AND close < prior high (gap up, fail to hold)."""
    cond = (open_ > high.shift(1)) & (close < high.shift(1))
    return cond.astype(float).where(open_.notna() & high.notna() & close.notna(), np.nan)


def _td_open_bullish(open_, low, close):
    cond = (open_ < low.shift(1)) & (close > low.shift(1))
    return cond.astype(float).where(open_.notna() & low.notna() & close.notna(), np.nan)


def _td_power_of_3_bearish(open_, close):
    """Bearish Power of 3: two consecutive up bars then bar with close < open of bar 2 (engulf+1)."""
    bar1_up = close.shift(2) > open_.shift(2)
    bar2_up = close.shift(1) > open_.shift(1)
    bar3_below = close < open_.shift(1)
    cond = bar1_up & bar2_up & bar3_below
    return cond.astype(float).where(close.notna() & open_.notna(), np.nan)


def _td_setup_cancelled_by_4bar_low_close(close):
    """Setup cancellation rule: close lower than close[-4]. Returns 1 at the bar of cancellation."""
    cond = close < close.shift(4)
    return cond.astype(float).where(close.notna(), np.nan)


def _tdst_sell_level(high, low, close, lookback=9):
    """TDST sell-line: the highest TRUE high during the last completed sell setup (carries forward)."""
    sell_count = _td_setup_count_sell(close, 4)
    # When sell_count == 9, record high during the setup as TDST sell level
    arr_cnt = sell_count.values
    arr_h = high.values
    nb = len(arr_h)
    out = np.full(nb, np.nan, dtype=float)
    cur = np.nan
    for i in range(nb):
        if arr_cnt[i] == 9 and i >= lookback:
            # Highest high over the setup's 9 bars
            segment = arr_h[i - lookback + 1:i + 1]
            segment = segment[~np.isnan(segment)]
            if segment.size > 0:
                cur = float(segment.max())
        out[i] = cur
    return pd.Series(out, index=high.index)


def _tdst_buy_level(high, low, close, lookback=9):
    buy_count = _td_setup_count_buy(close, 4)
    arr_cnt = buy_count.values
    arr_l = low.values
    nb = len(arr_l)
    out = np.full(nb, np.nan, dtype=float)
    cur = np.nan
    for i in range(nb):
        if arr_cnt[i] == 9 and i >= lookback:
            segment = arr_l[i - lookback + 1:i + 1]
            segment = segment[~np.isnan(segment)]
            if segment.size > 0:
                cur = float(segment.min())
        out[i] = cur
    return pd.Series(out, index=low.index)


def _td_rebo_breakout_up(high, n=2):
    """TD Range Expansion Breakout (REBO): high > prior n-bar max."""
    return (high > high.shift(1).rolling(n, min_periods=1).max()).astype(float).where(high.notna(), np.nan)


def _td_rebo_breakout_down(low, n=2):
    return (low < low.shift(1).rolling(n, min_periods=1).min()).astype(float).where(low.notna(), np.nan)


def _td_rei_value(high, low, close, n=5):
    """TD Range Expansion Index simplified: oscillates +/- around 0."""
    # Following Demark's REI: numerator = sum over n bars of conditional (high-high[-2] + low-low[-2])
    # Denominator = sum over n bars of (high - low)
    h2 = high.shift(2); l2 = low.shift(2)
    h_diff = high - h2; l_diff = low - l2
    cond_h_high = (high >= low.shift(5)) | (high >= low.shift(6))
    cond_h_low = (high.shift(2) >= close.shift(7)) | (high.shift(2) >= close.shift(8))
    valid = (cond_h_high & cond_h_low).astype(float)
    num = (h_diff + l_diff) * valid
    den = (high - low).abs()
    num_sum = num.rolling(n, min_periods=max(n // 2, 2)).sum()
    den_sum = den.rolling(n, min_periods=max(n // 2, 2)).sum().replace(0, np.nan)
    return 100.0 * num_sum / den_sum


def f56_dems_001_td_buy_setup_count_current(close: pd.Series) -> pd.Series:
    """Current TD Buy Setup count (consecutive bars where close < close[-4])."""
    return (_td_setup_count_buy(close, 4))

def f56_dems_002_td_buy_setup_9_completion_event_indicator(close: pd.Series) -> pd.Series:
    """Indicator: Buy Setup just reached 9 bars (rare exhaustion-of-demand signal)."""
    bs = _td_setup_count_buy(close, 4)
    return ((bs == 9).astype(float).where(bs.notna(), np.nan))

def f56_dems_003_td_buy_setup_9_count_252d(close: pd.Series) -> pd.Series:
    """Count of completed TD Buy Setups (count = 9) in last 252d."""
    bs = _td_setup_count_buy(close, 4)
    ev = (bs == 9).astype(float).where(bs.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_004_td_buy_setup_9_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """RARE: Buy setup completion AND close = 252d max (demand exhaustion at top)."""
    bs = _td_setup_count_buy(close, 4)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((bs == 9) & (close >= rmax - 1e-12)).astype(float).where(bs.notna(), np.nan))

def f56_dems_005_td_buy_setup_density_at_252d_high_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where (close = 252d max) AND buy-setup-count >= 5."""
    bs = _td_setup_count_buy(close, 4)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ind = ((bs >= 5) & (close >= rmax - 1e-12)).astype(float).where(bs.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_006_td_buy_setup_bars_since_completion(close: pd.Series) -> pd.Series:
    """Bars since last Buy Setup completion (capped 252)."""
    bs = _td_setup_count_buy(close, 4)
    ev = (bs == 9).astype(float).where(bs.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_007_td_buy_setup_failure_indicator(close: pd.Series) -> pd.Series:
    """Indicator: Buy Setup count goes to 0 after reaching >=5 - in-progress failure."""
    bs = _td_setup_count_buy(close, 4)
    return (((bs < 1) & (bs.shift(1) >= 5)).astype(float).where(bs.notna(), np.nan))

def f56_dems_008_td_buy_setup_perfection_count_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of completed buy setups where bars 8 or 9 had low < min(low[bar6], low[bar7]) in last 252d."""
    bs = _td_setup_count_buy(close, 4)
    comp = (bs == 9).astype(float)
    low_min_67 = pd.concat([low.shift(2), low.shift(3)], axis=1).min(axis=1)
    low_at_89 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    perfect = ((comp > 0.5) & (low_at_89 < low_min_67)).astype(float).where(bs.notna(), np.nan)
    return (perfect.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_009_td_buy_setup_aggressive_count_252d(close: pd.Series) -> pd.Series:
    """Aggressive Buy Setup uses 3-bar lookback (close < close[-3]); count in 252d."""
    bs_agg = _td_setup_count_buy(close, 3)
    ev = (bs_agg == 9).astype(float).where(bs_agg.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_010_td_buy_setup_vs_sell_setup_breadth_difference_252d(close: pd.Series) -> pd.Series:
    """Buy setup count - Sell setup count in 252d - demand-vs-supply exhaustion balance."""
    bs = _td_setup_count_buy(close, 4); ss = _td_setup_count_sell(close, 4)
    b_ev = (bs == 9).astype(float).where(bs.notna(), np.nan)
    s_ev = (ss == 9).astype(float).where(ss.notna(), np.nan)
    b_cnt = b_ev.rolling(YDAYS, min_periods=QDAYS).sum()
    s_cnt = s_ev.rolling(YDAYS, min_periods=QDAYS).sum()
    return (b_cnt - s_cnt)

def f56_dems_011_td_differential_bearish_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Differential indicator (close higher but buying pressure declines, selling pressure increases)."""
    return (_td_differential_bearish(high, low, close))

def f56_dems_012_td_differential_bearish_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish TD Differential events in 252d."""
    ev = _td_differential_bearish(high, low, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_013_td_differential_bearish_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish TD Differential AND close = 252d max."""
    ev = _td_differential_bearish(high, low, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_014_td_differential_bullish_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish TD Differential mirror."""
    return (_td_differential_bullish(high, low, close))

def f56_dems_015_td_differential_days_since_last_bearish(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish TD Differential (capped 252)."""
    ev = _td_differential_bearish(high, low, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_016_td_differential_bearish_at_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish TD Differential events where close = 252d max in 252d."""
    ev = _td_differential_bearish(high, low, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    joint = (ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan)
    return (joint.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_017_td_differential_bearish_at_overbought_rsi_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Differential AND RSI14 > 70."""
    ev = _td_differential_bearish(high, low, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_018_td_differential_bearish_at_sma200_proximity_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Differential AND close within 2% above SMA200."""
    ev = _td_differential_bearish(high, low, close)
    sma200 = _sma(close, 200)
    rel = _safe_div(close - sma200, sma200)
    return ((ev * ((rel > 0) & (rel < 0.02)).astype(float)).where(ev.notna(), np.nan))

def f56_dems_019_td_differential_persistence_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with bearish TD Differential event."""
    ev = _td_differential_bearish(high, low, close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_020_td_differential_bearish_x_volume_above_avg_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish TD Differential AND volume > 21d-avg."""
    ev = _td_differential_bearish(high, low, close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_above = (volume > v_avg).astype(float)
    return ((ev * vol_above).where(ev.notna(), np.nan))

def f56_dems_021_td_anti_differential_bearish_event_indicator(close: pd.Series) -> pd.Series:
    """Bearish TD Anti-Differential (5-bar down/up/down/up/down close pattern)."""
    return (_td_anti_differential_bearish(close))

def f56_dems_022_td_anti_differential_bearish_count_252d(close: pd.Series) -> pd.Series:
    """Count of bearish TD Anti-Differential events in 252d."""
    ev = _td_anti_differential_bearish(close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_023_td_anti_differential_bearish_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """Indicator: Bearish Anti-Differential AND close = 252d max."""
    ev = _td_anti_differential_bearish(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_024_td_anti_differential_bullish_event_indicator(close: pd.Series) -> pd.Series:
    """Bullish TD Anti-Differential mirror."""
    return (_td_anti_differential_bullish(close))

def f56_dems_025_td_anti_differential_days_since_last_bearish(close: pd.Series) -> pd.Series:
    """Bars since last bearish Anti-Differential (capped 252)."""
    ev = _td_anti_differential_bearish(close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_026_td_anti_differential_bearish_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with bearish Anti-Differential event."""
    ev = _td_anti_differential_bearish(close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_027_td_anti_differential_bearish_intensity_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score over 252d of 21d Anti-Differential count."""
    ev = _td_anti_differential_bearish(close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS))

def f56_dems_028_td_anti_differential_x_overbought_indicator(close: pd.Series) -> pd.Series:
    """Bearish Anti-Differential AND RSI14 > 70."""
    ev = _td_anti_differential_bearish(close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_029_td_anti_differential_bearish_x_volume_above_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish Anti-Differential AND volume > 21d-avg."""
    ev = _td_anti_differential_bearish(close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_above = (volume > v_avg).astype(float)
    return ((ev * vol_above).where(ev.notna(), np.nan))

def f56_dems_030_td_anti_differential_failure_indicator_252d(close: pd.Series) -> pd.Series:
    """Indicator: bearish Anti-Differential AND close MAKES NEW 252d-high within next 5 bars (failure)."""
    ev = _td_anti_differential_bearish(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_max_next5 = (close >= rmax - 1e-12).shift(WDAYS, fill_value=False).astype(float)
    # PIT-clean: use prior-evt logic
    ev_5 = ev.shift(WDAYS).rolling(WDAYS, min_periods=1).max()
    at_max_now = (close >= rmax - 1e-12).astype(float)
    return ((ev_5 * at_max_now).where(ev.notna(), np.nan))

def f56_dems_031_td_reverse_differential_bearish_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Reverse-Differential: close down with buying-pressure rising (paradox sell)."""
    return (_td_reverse_differential_bearish(high, low, close))

def f56_dems_032_td_reverse_differential_bearish_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of Reverse-Differential bearish events in 252d."""
    ev = _td_reverse_differential_bearish(high, low, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_033_td_reverse_differential_bearish_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Reverse-Diff bearish AND close near 252d max (within 2%)."""
    ev = _td_reverse_differential_bearish(high, low, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rel = _safe_div(close, rmax)
    return ((ev * (rel > 0.98).astype(float)).where(ev.notna(), np.nan))

def f56_dems_034_td_reverse_differential_days_since_last_bearish(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last Reverse-Differential bearish (capped 252)."""
    ev = _td_reverse_differential_bearish(high, low, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_035_td_reverse_differential_persistence_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with Reverse-Differential event."""
    ev = _td_reverse_differential_bearish(high, low, close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_036_td_reverse_differential_intensity_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score over 252d of 21d Reverse-Differential count."""
    ev = _td_reverse_differential_bearish(high, low, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS))

def f56_dems_037_td_reverse_differential_in_top_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Reverse-Diff count in top decile across 252d."""
    ev = _td_reverse_differential_bearish(high, low, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    p90 = cnt.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((cnt > p90).astype(float).where(p90.notna(), np.nan))

def f56_dems_038_td_reverse_differential_x_overbought_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reverse-Diff bearish AND RSI14 > 70."""
    ev = _td_reverse_differential_bearish(high, low, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_039_td_reverse_differential_with_atr_compression_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reverse-Diff bearish AND ATR21/close < 252d-q25."""
    ev = _td_reverse_differential_bearish(high, low, close)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    q25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return ((ev * (atr_n < q25).astype(float)).where(ev.notna() & q25.notna(), np.nan))

def f56_dems_040_td_reverse_differential_bearish_count_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reverse-Differential count in 504d."""
    ev = _td_reverse_differential_bearish(high, low, close)
    return (ev.rolling(DDAYS_2Y, min_periods=YDAYS).sum())

def f56_dems_041_td_clop_bearish_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD CLOP: open above prior open AND prior close, current close below open."""
    return (_td_clop_bearish(open, close))

def f56_dems_042_td_clop_bearish_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish CLOP events in 252d."""
    ev = _td_clop_bearish(open, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_043_td_clop_bearish_at_252d_high_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish CLOP AND close = 252d max."""
    ev = _td_clop_bearish(open, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_044_td_clop_bullish_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish CLOP mirror."""
    return (_td_clop_bullish(open, close))

def f56_dems_045_td_clop_days_since_last_bearish(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish CLOP (capped 252)."""
    ev = _td_clop_bearish(open, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_046_td_clop_persistence_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with bearish CLOP."""
    ev = _td_clop_bearish(open, close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_047_td_clop_intensity_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d bearish-CLOP count over 252d."""
    ev = _td_clop_bearish(open, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS))

def f56_dems_048_td_clop_x_overbought_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOP AND RSI14 > 70."""
    ev = _td_clop_bearish(open, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_049_td_clop_bearish_x_volume_indicator(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish CLOP AND volume > 21d-avg."""
    ev = _td_clop_bearish(open, close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_above = (volume > v_avg).astype(float)
    return ((ev * vol_above).where(ev.notna(), np.nan))

def f56_dems_050_td_clop_failure_indicator_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOP within last 5 bars AND close MAKES new 252d-high (CLOP failed)."""
    ev = _td_clop_bearish(open, close)
    ev_5 = ev.shift(WDAYS).rolling(WDAYS, min_periods=1).max()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev_5 * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_051_td_clopwin_bearish_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOPWIN: prior bar up, current bar inside prior open-close range, current closes down."""
    return (_td_clopwin_bearish(open, close))

def f56_dems_052_td_clopwin_bearish_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish CLOPWIN events in 252d."""
    ev = _td_clopwin_bearish(open, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_053_td_clopwin_bearish_at_252d_high_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish CLOPWIN AND close = 252d max."""
    ev = _td_clopwin_bearish(open, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_054_td_clopwin_bullish_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish CLOPWIN mirror."""
    return (_td_clopwin_bullish(open, close))

def f56_dems_055_td_clopwin_days_since_last_bearish(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish CLOPWIN (capped 252)."""
    ev = _td_clopwin_bearish(open, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_056_td_clopwin_persistence_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with bearish CLOPWIN."""
    ev = _td_clopwin_bearish(open, close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_057_td_clopwin_intensity_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d bearish-CLOPWIN count over 252d."""
    ev = _td_clopwin_bearish(open, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS))

def f56_dems_058_td_clopwin_x_overbought_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOPWIN AND RSI14 > 70."""
    ev = _td_clopwin_bearish(open, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_059_td_clopwin_in_top_quintile_close_in_range(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOPWIN AND close-position within day-range > 0.8 (high close)."""
    ev = _td_clopwin_bearish(open, close)
    pos = (close - low) / (high - low).replace(0, np.nan)
    return ((ev * (pos > 0.8).astype(float)).where(ev.notna() & pos.notna(), np.nan))

def f56_dems_060_td_clopwin_x_failed_breakout_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CLOPWIN AND high made new 21d high but close < open."""
    ev = _td_clopwin_bearish(open, close)
    h21 = high.rolling(MDAYS, min_periods=10).max()
    ind = ((high >= h21 - 1e-12) & (close < open)).astype(float)
    return ((ev * ind).where(ev.notna(), np.nan))

def f56_dems_061_td_camouflage_bearish_event_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Camouflage: close > prior close AND close < open AND low < prior low."""
    return (_td_camouflage_bearish(open, high, low, close))

def f56_dems_062_td_camouflage_bearish_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish Camouflage events in 252d."""
    ev = _td_camouflage_bearish(open, high, low, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_063_td_camouflage_bearish_at_252d_high_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish Camouflage AND close = 252d max - hidden distribution at top."""
    ev = _td_camouflage_bearish(open, high, low, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_064_td_camouflage_bullish_event_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish Camouflage mirror."""
    return (_td_camouflage_bullish(open, high, low, close))

def f56_dems_065_td_camouflage_days_since_last_bearish(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish Camouflage (capped 252)."""
    ev = _td_camouflage_bearish(open, high, low, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_066_td_camouflage_persistence_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with bearish Camouflage."""
    ev = _td_camouflage_bearish(open, high, low, close)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean())

def f56_dems_067_td_camouflage_intensity_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d bearish-Camouflage count over 252d."""
    ev = _td_camouflage_bearish(open, high, low, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS))

def f56_dems_068_td_camouflage_x_overbought_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Camouflage AND RSI14 > 70."""
    ev = _td_camouflage_bearish(open, high, low, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan))

def f56_dems_069_td_camouflage_with_distribution_volume_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish Camouflage AND volume > 21d-avg * 1.2."""
    ev = _td_camouflage_bearish(open, high, low, close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_dist = (volume > 1.2 * v_avg).astype(float)
    return ((ev * vol_dist).where(ev.notna(), np.nan))

def f56_dems_070_td_camouflage_failure_signal_at_high_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Camouflage within last 5 bars AND price makes new 252d-high (Camouflage failed)."""
    ev = _td_camouflage_bearish(open, high, low, close)
    ev_5 = ev.shift(WDAYS).rolling(WDAYS, min_periods=1).max()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev_5 * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan))

def f56_dems_071_td_open_bearish_event_indicator(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Open: open above prior high AND close back below prior high."""
    return (_td_open_bearish(open, high, close))

def f56_dems_072_td_open_bearish_count_252d(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish TD Open events in 252d."""
    ev = _td_open_bearish(open, high, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f56_dems_073_td_open_days_since_last_bearish(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish TD Open (capped 252)."""
    ev = _td_open_bearish(open, high, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS)))

def f56_dems_074_td_power_of_3_bearish_event_indicator(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Power-of-3: two up bars then bar closes below 2nd-bar open."""
    return (_td_power_of_3_bearish(open, close))

def f56_dems_075_td_power_of_3_bearish_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish Power-of-3 in 252d."""
    ev = _td_power_of_3_bearish(open, close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
#                         REGISTRY 001_075 (base)
# ============================================================

DEMARK_EXTENDED_SIGNALS_BASE_REGISTRY_001_075 = {
    "f56_dems_001_td_buy_setup_count_current": {"inputs": ["close"], "func": f56_dems_001_td_buy_setup_count_current},
    "f56_dems_002_td_buy_setup_9_completion_event_indicator": {"inputs": ["close"], "func": f56_dems_002_td_buy_setup_9_completion_event_indicator},
    "f56_dems_003_td_buy_setup_9_count_252d": {"inputs": ["close"], "func": f56_dems_003_td_buy_setup_9_count_252d},
    "f56_dems_004_td_buy_setup_9_at_252d_high_indicator": {"inputs": ["close"], "func": f56_dems_004_td_buy_setup_9_at_252d_high_indicator},
    "f56_dems_005_td_buy_setup_density_at_252d_high_fraction_63d": {"inputs": ["close"], "func": f56_dems_005_td_buy_setup_density_at_252d_high_fraction_63d},
    "f56_dems_006_td_buy_setup_bars_since_completion": {"inputs": ["close"], "func": f56_dems_006_td_buy_setup_bars_since_completion},
    "f56_dems_007_td_buy_setup_failure_indicator": {"inputs": ["close"], "func": f56_dems_007_td_buy_setup_failure_indicator},
    "f56_dems_008_td_buy_setup_perfection_count_252d": {"inputs": ["close", "low"], "func": f56_dems_008_td_buy_setup_perfection_count_252d},
    "f56_dems_009_td_buy_setup_aggressive_count_252d": {"inputs": ["close"], "func": f56_dems_009_td_buy_setup_aggressive_count_252d},
    "f56_dems_010_td_buy_setup_vs_sell_setup_breadth_difference_252d": {"inputs": ["close"], "func": f56_dems_010_td_buy_setup_vs_sell_setup_breadth_difference_252d},
    "f56_dems_011_td_differential_bearish_event_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_011_td_differential_bearish_event_indicator},
    "f56_dems_012_td_differential_bearish_count_252d": {"inputs": ["high", "low", "close"], "func": f56_dems_012_td_differential_bearish_count_252d},
    "f56_dems_013_td_differential_bearish_at_252d_high_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_013_td_differential_bearish_at_252d_high_indicator},
    "f56_dems_014_td_differential_bullish_event_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_014_td_differential_bullish_event_indicator},
    "f56_dems_015_td_differential_days_since_last_bearish": {"inputs": ["high", "low", "close"], "func": f56_dems_015_td_differential_days_since_last_bearish},
    "f56_dems_016_td_differential_bearish_at_high_count_252d": {"inputs": ["high", "low", "close"], "func": f56_dems_016_td_differential_bearish_at_high_count_252d},
    "f56_dems_017_td_differential_bearish_at_overbought_rsi_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_017_td_differential_bearish_at_overbought_rsi_indicator},
    "f56_dems_018_td_differential_bearish_at_sma200_proximity_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_018_td_differential_bearish_at_sma200_proximity_indicator},
    "f56_dems_019_td_differential_persistence_63d": {"inputs": ["high", "low", "close"], "func": f56_dems_019_td_differential_persistence_63d},
    "f56_dems_020_td_differential_bearish_x_volume_above_avg_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f56_dems_020_td_differential_bearish_x_volume_above_avg_indicator},
    "f56_dems_021_td_anti_differential_bearish_event_indicator": {"inputs": ["close"], "func": f56_dems_021_td_anti_differential_bearish_event_indicator},
    "f56_dems_022_td_anti_differential_bearish_count_252d": {"inputs": ["close"], "func": f56_dems_022_td_anti_differential_bearish_count_252d},
    "f56_dems_023_td_anti_differential_bearish_at_252d_high_indicator": {"inputs": ["close"], "func": f56_dems_023_td_anti_differential_bearish_at_252d_high_indicator},
    "f56_dems_024_td_anti_differential_bullish_event_indicator": {"inputs": ["close"], "func": f56_dems_024_td_anti_differential_bullish_event_indicator},
    "f56_dems_025_td_anti_differential_days_since_last_bearish": {"inputs": ["close"], "func": f56_dems_025_td_anti_differential_days_since_last_bearish},
    "f56_dems_026_td_anti_differential_bearish_persistence_63d": {"inputs": ["close"], "func": f56_dems_026_td_anti_differential_bearish_persistence_63d},
    "f56_dems_027_td_anti_differential_bearish_intensity_zscore_252d": {"inputs": ["close"], "func": f56_dems_027_td_anti_differential_bearish_intensity_zscore_252d},
    "f56_dems_028_td_anti_differential_x_overbought_indicator": {"inputs": ["close"], "func": f56_dems_028_td_anti_differential_x_overbought_indicator},
    "f56_dems_029_td_anti_differential_bearish_x_volume_above_avg": {"inputs": ["close", "volume"], "func": f56_dems_029_td_anti_differential_bearish_x_volume_above_avg},
    "f56_dems_030_td_anti_differential_failure_indicator_252d": {"inputs": ["close"], "func": f56_dems_030_td_anti_differential_failure_indicator_252d},
    "f56_dems_031_td_reverse_differential_bearish_event_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_031_td_reverse_differential_bearish_event_indicator},
    "f56_dems_032_td_reverse_differential_bearish_count_252d": {"inputs": ["high", "low", "close"], "func": f56_dems_032_td_reverse_differential_bearish_count_252d},
    "f56_dems_033_td_reverse_differential_bearish_at_252d_high_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_033_td_reverse_differential_bearish_at_252d_high_indicator},
    "f56_dems_034_td_reverse_differential_days_since_last_bearish": {"inputs": ["high", "low", "close"], "func": f56_dems_034_td_reverse_differential_days_since_last_bearish},
    "f56_dems_035_td_reverse_differential_persistence_63d": {"inputs": ["high", "low", "close"], "func": f56_dems_035_td_reverse_differential_persistence_63d},
    "f56_dems_036_td_reverse_differential_intensity_zscore_252d": {"inputs": ["high", "low", "close"], "func": f56_dems_036_td_reverse_differential_intensity_zscore_252d},
    "f56_dems_037_td_reverse_differential_in_top_decile_252d": {"inputs": ["high", "low", "close"], "func": f56_dems_037_td_reverse_differential_in_top_decile_252d},
    "f56_dems_038_td_reverse_differential_x_overbought_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_038_td_reverse_differential_x_overbought_indicator},
    "f56_dems_039_td_reverse_differential_with_atr_compression_indicator": {"inputs": ["high", "low", "close"], "func": f56_dems_039_td_reverse_differential_with_atr_compression_indicator},
    "f56_dems_040_td_reverse_differential_bearish_count_504d": {"inputs": ["high", "low", "close"], "func": f56_dems_040_td_reverse_differential_bearish_count_504d},
    "f56_dems_041_td_clop_bearish_event_indicator": {"inputs": ["open", "close"], "func": f56_dems_041_td_clop_bearish_event_indicator},
    "f56_dems_042_td_clop_bearish_count_252d": {"inputs": ["open", "close"], "func": f56_dems_042_td_clop_bearish_count_252d},
    "f56_dems_043_td_clop_bearish_at_252d_high_indicator": {"inputs": ["open", "close"], "func": f56_dems_043_td_clop_bearish_at_252d_high_indicator},
    "f56_dems_044_td_clop_bullish_event_indicator": {"inputs": ["open", "close"], "func": f56_dems_044_td_clop_bullish_event_indicator},
    "f56_dems_045_td_clop_days_since_last_bearish": {"inputs": ["open", "close"], "func": f56_dems_045_td_clop_days_since_last_bearish},
    "f56_dems_046_td_clop_persistence_63d": {"inputs": ["open", "close"], "func": f56_dems_046_td_clop_persistence_63d},
    "f56_dems_047_td_clop_intensity_zscore_252d": {"inputs": ["open", "close"], "func": f56_dems_047_td_clop_intensity_zscore_252d},
    "f56_dems_048_td_clop_x_overbought_indicator": {"inputs": ["open", "close"], "func": f56_dems_048_td_clop_x_overbought_indicator},
    "f56_dems_049_td_clop_bearish_x_volume_indicator": {"inputs": ["open", "close", "volume"], "func": f56_dems_049_td_clop_bearish_x_volume_indicator},
    "f56_dems_050_td_clop_failure_indicator_252d": {"inputs": ["open", "close"], "func": f56_dems_050_td_clop_failure_indicator_252d},
    "f56_dems_051_td_clopwin_bearish_event_indicator": {"inputs": ["open", "close"], "func": f56_dems_051_td_clopwin_bearish_event_indicator},
    "f56_dems_052_td_clopwin_bearish_count_252d": {"inputs": ["open", "close"], "func": f56_dems_052_td_clopwin_bearish_count_252d},
    "f56_dems_053_td_clopwin_bearish_at_252d_high_indicator": {"inputs": ["open", "close"], "func": f56_dems_053_td_clopwin_bearish_at_252d_high_indicator},
    "f56_dems_054_td_clopwin_bullish_event_indicator": {"inputs": ["open", "close"], "func": f56_dems_054_td_clopwin_bullish_event_indicator},
    "f56_dems_055_td_clopwin_days_since_last_bearish": {"inputs": ["open", "close"], "func": f56_dems_055_td_clopwin_days_since_last_bearish},
    "f56_dems_056_td_clopwin_persistence_63d": {"inputs": ["open", "close"], "func": f56_dems_056_td_clopwin_persistence_63d},
    "f56_dems_057_td_clopwin_intensity_zscore_252d": {"inputs": ["open", "close"], "func": f56_dems_057_td_clopwin_intensity_zscore_252d},
    "f56_dems_058_td_clopwin_x_overbought_indicator": {"inputs": ["open", "close"], "func": f56_dems_058_td_clopwin_x_overbought_indicator},
    "f56_dems_059_td_clopwin_in_top_quintile_close_in_range": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_059_td_clopwin_in_top_quintile_close_in_range},
    "f56_dems_060_td_clopwin_x_failed_breakout_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_060_td_clopwin_x_failed_breakout_indicator},
    "f56_dems_061_td_camouflage_bearish_event_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_061_td_camouflage_bearish_event_indicator},
    "f56_dems_062_td_camouflage_bearish_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_062_td_camouflage_bearish_count_252d},
    "f56_dems_063_td_camouflage_bearish_at_252d_high_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_063_td_camouflage_bearish_at_252d_high_indicator},
    "f56_dems_064_td_camouflage_bullish_event_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_064_td_camouflage_bullish_event_indicator},
    "f56_dems_065_td_camouflage_days_since_last_bearish": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_065_td_camouflage_days_since_last_bearish},
    "f56_dems_066_td_camouflage_persistence_63d": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_066_td_camouflage_persistence_63d},
    "f56_dems_067_td_camouflage_intensity_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_067_td_camouflage_intensity_zscore_252d},
    "f56_dems_068_td_camouflage_x_overbought_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_068_td_camouflage_x_overbought_indicator},
    "f56_dems_069_td_camouflage_with_distribution_volume_indicator": {"inputs": ["open", "high", "low", "close", "volume"], "func": f56_dems_069_td_camouflage_with_distribution_volume_indicator},
    "f56_dems_070_td_camouflage_failure_signal_at_high_indicator": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_070_td_camouflage_failure_signal_at_high_indicator},
    "f56_dems_071_td_open_bearish_event_indicator": {"inputs": ["open", "high", "close"], "func": f56_dems_071_td_open_bearish_event_indicator},
    "f56_dems_072_td_open_bearish_count_252d": {"inputs": ["open", "high", "close"], "func": f56_dems_072_td_open_bearish_count_252d},
    "f56_dems_073_td_open_days_since_last_bearish": {"inputs": ["open", "high", "close"], "func": f56_dems_073_td_open_days_since_last_bearish},
    "f56_dems_074_td_power_of_3_bearish_event_indicator": {"inputs": ["open", "close"], "func": f56_dems_074_td_power_of_3_bearish_event_indicator},
    "f56_dems_075_td_power_of_3_bearish_count_252d": {"inputs": ["open", "close"], "func": f56_dems_075_td_power_of_3_bearish_count_252d},
}
