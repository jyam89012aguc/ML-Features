"""demark_extended_signals d3 features 076-150 - Pipeline 1b-technical.

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


def f56_dems_076_td_power_of_3_bearish_at_252d_high_indicator_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: Power-of-3 bearish AND close = 252d max."""
    ev = _td_power_of_3_bearish(open, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_077_td_open_x_overbought_indicator_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TD Open AND RSI14 > 70."""
    ev = _td_open_bearish(open, high, close)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan)).diff().diff().diff()

def f56_dems_078_td_power_of_3_days_since_last_bearish_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bearish Power-of-3 (capped 252)."""
    ev = _td_power_of_3_bearish(open, close)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff().diff().diff()

def f56_dems_079_td_open_at_252d_high_indicator_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish TD Open AND close = 252d max."""
    ev = _td_open_bearish(open, high, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_080_td_power_of_3_bearish_intensity_zscore_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d Power-of-3 bearish count over 252d."""
    ev = _td_power_of_3_bearish(open, close)
    cnt = ev.rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS)).diff().diff().diff()

def f56_dems_081_td_setup_cancelled_4bar_low_close_event_d3(close: pd.Series) -> pd.Series:
    """Setup cancellation rule: close < close[-4] - cancels in-progress TD Sell Setup."""
    return (_td_setup_cancelled_by_4bar_low_close(close)).diff().diff().diff()

def f56_dems_082_td_setup_cancelled_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of 4-bar-low-close cancellations in 252d."""
    ev = _td_setup_cancelled_by_4bar_low_close(close)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_083_td_countdown_cancelled_by_tdst_break_event_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Countdown cancellation: true high above TDST-buy level breaks down-countdown structure."""
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    cond = (high > tdst_buy.shift(1)) & tdst_buy.notna()
    return (cond.astype(float).where(tdst_buy.notna(), np.nan)).diff().diff().diff()

def f56_dems_084_td_countdown_cancelled_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TDST-break countdown cancellations in 252d."""
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    cond = (high > tdst_buy.shift(1)) & tdst_buy.notna()
    ev = cond.astype(float).where(tdst_buy.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_085_td_setup_cancellation_at_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: Setup cancellation AND close = 252d max - failed setup at top."""
    ev = _td_setup_cancelled_by_4bar_low_close(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_086_td_setup_completion_to_cancellation_ratio_504d_d3(close: pd.Series) -> pd.Series:
    """(Setup-9 completions) / (Setup cancellations) over 504d."""
    ss = _td_setup_count_sell(close, 4)
    comp = (ss == 9).astype(float).where(ss.notna(), np.nan)
    canc = _td_setup_cancelled_by_4bar_low_close(close)
    comp_cnt = comp.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    canc_cnt = canc.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return (_safe_div(comp_cnt, canc_cnt)).diff().diff().diff()

def f56_dems_087_td_sequential_cancellation_density_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Setup cancellations + Countdown cancellations) / 252."""
    ev_s = _td_setup_cancelled_by_4bar_low_close(close)
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    ev_c = ((high > tdst_buy.shift(1)) & tdst_buy.notna()).astype(float).where(tdst_buy.notna(), np.nan)
    tot = ev_s.fillna(0.0) + ev_c.fillna(0.0)
    return (tot.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff().diff().diff()

def f56_dems_088_td_setup_recovery_after_cancellation_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: Setup cancellation AND new Setup count >= 5 within next 13 bars (recovery)."""
    ev = _td_setup_cancelled_by_4bar_low_close(close)
    ss = _td_setup_count_sell(close, 4)
    ss_max13 = ss.rolling(13, min_periods=5).max()
    rec = (ss_max13 >= 5).astype(float)
    return ((ev * rec).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_089_td_countdown_cancellation_at_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: TDST-break cancellation AND close = 252d max."""
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    ev = ((high > tdst_buy.shift(1)) & tdst_buy.notna()).astype(float).where(tdst_buy.notna(), np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float)).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_090_td_sequential_pattern_failure_score_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score over 252d of (setup-cancellation count + countdown-cancellation count) / 21d."""
    ev_s = _td_setup_cancelled_by_4bar_low_close(close)
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    ev_c = ((high > tdst_buy.shift(1)) & tdst_buy.notna()).astype(float).where(tdst_buy.notna(), np.nan)
    tot = (ev_s.fillna(0.0) + ev_c.fillna(0.0)).rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(tot, YDAYS)).diff().diff().diff()

def f56_dems_091_td_rebo_breakout_up_indicator_d3(high: pd.Series) -> pd.Series:
    """TD Range Expansion Breakout up: high > prior 2-bar max."""
    return (_td_rebo_breakout_up(high, 2)).diff().diff().diff()

def f56_dems_092_td_rebo_breakout_down_indicator_d3(low: pd.Series) -> pd.Series:
    """TD REBO down: low < prior 2-bar min."""
    return (_td_rebo_breakout_down(low, 2)).diff().diff().diff()

def f56_dems_093_td_rebo_breakout_up_count_252d_d3(high: pd.Series) -> pd.Series:
    """Count of REBO-up breakouts in 252d."""
    ev = _td_rebo_breakout_up(high, 2)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_094_td_rebo_breakout_down_count_252d_d3(low: pd.Series) -> pd.Series:
    """Count of REBO-down breakouts in 252d."""
    ev = _td_rebo_breakout_down(low, 2)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_095_td_rebo_breakout_failure_after_252d_high_indicator_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: REBO-up breakout AND close > 252d max AND next 5-bar high LOWER than current high."""
    ev = _td_rebo_breakout_up(high, 2)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    future_h_5 = high.rolling(WDAYS, min_periods=1).max().shift(WDAYS)
    failure = ((high > future_h_5) & (ev > 0.5) & (close >= rmax - 1e-12)).astype(float).shift(WDAYS)
    return (failure.where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_096_td_rebo_breakout_failure_count_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of failed REBO-up breakouts in 252d."""
    ev = _td_rebo_breakout_up(high, 2)
    future_h_5 = high.rolling(WDAYS, min_periods=1).max().shift(WDAYS)
    failure = ((high > future_h_5) & (ev > 0.5)).astype(float).shift(WDAYS)
    return (failure.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_097_td_rebo_breakout_up_at_overbought_indicator_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """REBO-up breakout AND RSI14 > 70."""
    ev = _td_rebo_breakout_up(high, 2)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan)).diff().diff().diff()

def f56_dems_098_td_rebo_breakout_up_to_down_ratio_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """(REBO-up count) / (REBO-down count) over 252d."""
    u = _td_rebo_breakout_up(high, 2).rolling(YDAYS, min_periods=QDAYS).sum()
    d = _td_rebo_breakout_down(low, 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(u, d)).diff().diff().diff()

def f56_dems_099_td_rebo_breakout_amplitude_pct_252d_d3(high: pd.Series) -> pd.Series:
    """Avg (high - prior 2-bar max) / prior 2-bar max for REBO-up events in 252d."""
    h_prior = high.shift(1).rolling(2, min_periods=1).max()
    amp = _safe_div(high - h_prior, h_prior).where(high > h_prior, np.nan)
    return (amp.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f56_dems_100_td_rebo_breakout_velocity_count_per_year_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """REBO breakout total count / 252."""
    u = _td_rebo_breakout_up(high, 2); d = _td_rebo_breakout_down(low, 2)
    tot = (u.fillna(0.0) + d.fillna(0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return (tot / float(YDAYS)).diff().diff().diff()

def f56_dems_101_td_d_wave_current_wave_number_proxy_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """D-Wave-like wave number proxy: number of distinct higher-highs since last 252d-low (capped 5)."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    since_low = (close.values - rmin_252.values)
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
        out[i] = float(cnt)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f56_dems_102_td_d_wave_wave_5_indicator_proxy_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: D-Wave proxy at wave count == 5."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
        out[i] = float(cnt)
    wave = pd.Series(out, index=close.index)
    return ((wave >= 5).astype(float).where(wave.notna(), np.nan)).diff().diff().diff()

def f56_dems_103_td_d_wave_wave_5_at_252d_high_indicator_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """D-Wave proxy at wave-5 AND close = 252d max - wave-5-top warning."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    rmax_252 = close.rolling(YDAYS, min_periods=QDAYS).max()
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
        out[i] = float(cnt)
    wave = pd.Series(out, index=close.index)
    return (((wave >= 5) & (close >= rmax_252 - 1e-12)).astype(float).where(wave.notna(), np.nan)).diff().diff().diff()

def f56_dems_104_td_d_wave_wave_c_indicator_proxy_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """D-Wave 'wave C' proxy: 3rd distinct lower-low since last 252d-high."""
    rmax_252 = close.rolling(YDAYS, min_periods=QDAYS).max()
    l_arr = low.values; nb = len(l_arr); out = np.full(nb, np.nan); cnt = 0; last_low = np.inf
    for i in range(nb):
        if not np.isnan(rmax_252.iloc[i]) and close.iloc[i] >= rmax_252.iloc[i] - 1e-9:
            cnt = 0; last_low = np.inf
        if not np.isnan(l_arr[i]) and l_arr[i] < last_low:
            cnt = min(cnt + 1, 3); last_low = l_arr[i]
        out[i] = float(cnt)
    wave = pd.Series(out, index=close.index)
    return ((wave >= 3).astype(float).where(wave.notna(), np.nan)).diff().diff().diff()

def f56_dems_105_td_d_wave_completed_5_count_504d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of distinct wave-5 completions in 504d."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); ev = np.zeros(nb); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
            if cnt == 5:
                ev[i] = 1.0
    evs = pd.Series(ev, index=close.index)
    return (evs.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff().diff()

def f56_dems_106_td_d_wave_bars_since_wave_3_proxy_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since the wave-3 reading (3rd distinct higher-high since last 252d-low)."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf; last3 = -1
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf; last3 = -1
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
            if cnt == 3:
                last3 = i
        if last3 >= 0:
            out[i] = float(i - last3)
    res = pd.Series(out, index=close.index)
    return (res.clip(upper=float(YDAYS))).diff().diff().diff()

def f56_dems_107_td_d_wave_wave_5_extension_pct_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """% extension of close above SMA200 at wave-5 (proxy)."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
        out[i] = float(cnt)
    wave = pd.Series(out, index=close.index)
    sma200 = _sma(close, 200)
    ext = _safe_div(close - sma200, sma200)
    return (ext.where(wave >= 5, np.nan)).diff().diff().diff()

def f56_dems_108_td_d_wave_wave_5_truncated_indicator_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: wave proxy reached 5 but high did not exceed prior wave-3 peak."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); wave = np.zeros(nb); peak3 = np.full(nb, np.nan); cur_peak3 = np.nan; cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf; cur_peak3 = np.nan
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
            if cnt == 3:
                cur_peak3 = h_arr[i]
        wave[i] = float(cnt); peak3[i] = cur_peak3
    wave_s = pd.Series(wave, index=close.index); peak3_s = pd.Series(peak3, index=close.index)
    return (((wave_s >= 5) & (high < peak3_s)).astype(float).where(wave_s.notna(), np.nan)).diff().diff().diff()

def f56_dems_109_td_d_wave_completed_c_count_504d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of completed wave-C readings in 504d."""
    rmax_252 = close.rolling(YDAYS, min_periods=QDAYS).max()
    l_arr = low.values; nb = len(l_arr); ev = np.zeros(nb); cnt = 0; last_low = np.inf
    for i in range(nb):
        if not np.isnan(rmax_252.iloc[i]) and close.iloc[i] >= rmax_252.iloc[i] - 1e-9:
            cnt = 0; last_low = np.inf
        if not np.isnan(l_arr[i]) and l_arr[i] < last_low:
            cnt = min(cnt + 1, 3); last_low = l_arr[i]
            if cnt == 3:
                ev[i] = 1.0
    evs = pd.Series(ev, index=close.index)
    return (evs.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff().diff()

def f56_dems_110_td_d_wave_wave_5_failure_indicator_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: wave-5 proxy AND price drops 3% within 21 bars (wave-5 failure)."""
    rmin_252 = close.rolling(YDAYS, min_periods=QDAYS).min()
    h_arr = high.values; nb = len(h_arr); out = np.full(nb, np.nan); cnt = 0; last_high = -np.inf
    for i in range(nb):
        if not np.isnan(rmin_252.iloc[i]) and close.iloc[i] <= rmin_252.iloc[i] + 1e-9:
            cnt = 0; last_high = -np.inf
        if not np.isnan(h_arr[i]) and h_arr[i] > last_high:
            cnt = min(cnt + 1, 5); last_high = h_arr[i]
        out[i] = float(cnt)
    wave = pd.Series(out, index=close.index)
    fwd_min21 = close.rolling(MDAYS, min_periods=1).min().shift(MDAYS)
    fail = ((wave >= 5) & (fwd_min21 < close * 0.97)).astype(float).shift(MDAYS)
    return (fail.where(wave.notna(), np.nan)).diff().diff().diff()

def f56_dems_111_td_trend_factor_upside_target_d3(close: pd.Series) -> pd.Series:
    """TD Trend Factor upside target: prior 252d peak * 1.0556 (Demark's 5.56% factor)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (rmax * 1.0556).diff().diff().diff()

def f56_dems_112_td_trend_factor_downside_target_d3(close: pd.Series) -> pd.Series:
    """TD Trend Factor downside target: prior 252d trough * 0.9444."""
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    return (rmin * 0.9444).diff().diff().diff()

def f56_dems_113_td_trend_factor_upside_distance_pct_d3(close: pd.Series) -> pd.Series:
    """(Close / upside-target) - 1 - distance to upside Trend Factor target."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    return (_safe_div(close - tgt, tgt)).diff().diff().diff()

def f56_dems_114_td_trend_factor_downside_distance_pct_d3(close: pd.Series) -> pd.Series:
    """(Close / downside-target) - 1."""
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    tgt = rmin * 0.9444
    return (_safe_div(close - tgt, tgt)).diff().diff().diff()

def f56_dems_115_td_trend_factor_breach_upside_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: close >= upside Trend Factor target."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    return ((close >= tgt).astype(float).where(tgt.notna(), np.nan)).diff().diff().diff()

def f56_dems_116_td_trend_factor_breach_downside_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: close <= downside Trend Factor target."""
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    tgt = rmin * 0.9444
    return ((close <= tgt).astype(float).where(tgt.notna(), np.nan)).diff().diff().diff()

def f56_dems_117_td_trend_factor_upside_breach_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of upside Trend Factor breaches in 252d."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    ev = (close >= tgt).astype(float).where(tgt.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_118_td_trend_factor_upside_breach_at_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Upside Trend Factor breach AND close = 252d max."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    ev = (close >= tgt).astype(float).where(tgt.notna(), np.nan)
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff().diff()

def f56_dems_119_td_trend_factor_max_target_minus_current_252d_d3(close: pd.Series) -> pd.Series:
    """Max upside-target seen over 252d minus current close."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    tgt_max = tgt.rolling(YDAYS, min_periods=QDAYS).max()
    return (tgt_max - close).diff().diff().diff()

def f56_dems_120_td_trend_factor_target_failure_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: upside Trend Factor target reached but price falls 5% within 21 bars."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    tgt = rmax * 1.0556
    ev = (close >= tgt).astype(float).where(tgt.notna(), np.nan)
    fwd_min21 = close.rolling(MDAYS, min_periods=1).min().shift(MDAYS)
    fail = ((ev > 0.5) & (fwd_min21 < close * 0.95)).astype(float).shift(MDAYS)
    return (fail.where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_121_td_line_breakout_up_qualified_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Qualified break above a TD-line: close > prior 21d max AND high - close < (high - low)."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    broke = (close > h21.shift(1)).astype(float)
    qual = ((high - close) < (high - low)).astype(float)
    return ((broke * qual).where(h21.notna(), np.nan)).diff().diff().diff()

def f56_dems_122_td_line_breakout_down_qualified_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Qualified break below a TD-line: close < prior 21d min AND close - low < (high - low)."""
    l21 = low.rolling(MDAYS, min_periods=10).min()
    broke = (close < l21.shift(1)).astype(float)
    qual = ((close - low) < (high - low)).astype(float)
    return ((broke * qual).where(l21.notna(), np.nan)).diff().diff().diff()

def f56_dems_123_td_line_breakout_up_failure_indicator_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: qualified up-break AND close falls back below within 5 bars."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    broke = (close > h21.shift(1)).astype(float)
    qual = ((high - close) < (high - low)).astype(float)
    ev = broke * qual
    min5 = close.rolling(WDAYS, min_periods=1).min().shift(WDAYS)
    fail = ((ev > 0.5) & (min5 < h21.shift(1))).astype(float).shift(WDAYS)
    return (fail.where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_124_td_line_breakout_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of qualified TD-line breakouts (either direction) in 252d."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    l21 = low.rolling(MDAYS, min_periods=10).min()
    up = ((close > h21.shift(1)) & ((high - close) < (high - low))).astype(float)
    dn = ((close < l21.shift(1)) & ((close - low) < (high - low))).astype(float)
    return ((up.fillna(0.0) + dn.fillna(0.0)).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_125_td_line_qualified_breakout_at_252d_high_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of qualified up-breakouts in 252d while close = 252d max."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    up = ((close > h21.shift(1)) & ((high - close) < (high - low))).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((up * (close >= rmax - 1e-12).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_126_td_aggressive_setup_9_event_indicator_d3(close: pd.Series) -> pd.Series:
    """Aggressive TD Sell Setup with lookback=3 reaches 9 - event indicator."""
    ss_agg = _td_setup_count_sell(close, 3)
    return ((ss_agg == 9).astype(float).where(ss_agg.notna(), np.nan)).diff().diff().diff()

def f56_dems_127_td_aggressive_setup_9_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of aggressive sell-setup-9 events in 252d."""
    ss_agg = _td_setup_count_sell(close, 3)
    ev = (ss_agg == 9).astype(float).where(ss_agg.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_128_td_aggressive_countdown_13_count_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Aggressive TD Countdown reaches 13 (close >= high[-1], simplified)."""
    ev = (close >= high.shift(1)).astype(float)
    arr = ev.values; nb = len(arr); cd = np.zeros(nb); cnt = 0
    for i in range(nb):
        if np.isnan(arr[i]):
            continue
        if arr[i] > 0.5:
            cnt = min(cnt + 1, 13)
        if cnt == 13:
            cd[i] = 1.0; cnt = 0
    ev13 = pd.Series(cd, index=close.index)
    return (ev13.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_129_td_aggressive_setup_9_at_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Aggressive sell-setup-9 AND close = 252d max."""
    ss_agg = _td_setup_count_sell(close, 3)
    ev = (ss_agg == 9).astype(float).where(ss_agg.notna(), np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff().diff()

def f56_dems_130_td_aggressive_setup_9_vs_standard_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Aggressive setup-9 count / standard setup-9 count over 252d."""
    ss_agg = _td_setup_count_sell(close, 3); ss = _td_setup_count_sell(close, 4)
    ev_a = (ss_agg == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    ev_s = (ss == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(ev_a, ev_s)).diff().diff().diff()

def f56_dems_131_td_termination_count_value_proxy_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Termination Count proxy: bars since last TDST-sell level was created."""
    tdst_sell = _tdst_sell_level(high, low, close, 9)
    ch = (tdst_sell != tdst_sell.shift(1)).astype(float)
    return (_bars_since_last_event(ch).clip(upper=float(YDAYS))).diff().diff().diff()

def f56_dems_132_td_termination_completion_event_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: TDST-sell level was just updated (rare - completed setup boundary)."""
    tdst_sell = _tdst_sell_level(high, low, close, 9)
    return ((tdst_sell != tdst_sell.shift(1)).astype(float).where(tdst_sell.notna(), np.nan)).diff().diff().diff()

def f56_dems_133_td_termination_at_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TDST-sell level update AND close = 252d max."""
    tdst_sell = _tdst_sell_level(high, low, close, 9)
    ev = (tdst_sell != tdst_sell.shift(1)).astype(float).where(tdst_sell.notna(), np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff().diff()

def f56_dems_134_td_termination_to_setup_ratio_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TDST updates / sell-setup-9 count in 252d."""
    tdst_sell = _tdst_sell_level(high, low, close, 9)
    ev_t = (tdst_sell != tdst_sell.shift(1)).astype(float).where(tdst_sell.notna(), np.nan)
    ss = _td_setup_count_sell(close, 4)
    ev_s = (ss == 9).astype(float).where(ss.notna(), np.nan)
    c_t = ev_t.rolling(YDAYS, min_periods=QDAYS).sum()
    c_s = ev_s.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(c_t, c_s)).diff().diff().diff()

def f56_dems_135_td_time_price_intersection_event_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Time-price intersection: setup-count >= 9 AND close near TDST-sell level within 2%."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    return (((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)).diff().diff().diff()

def f56_dems_136_td_time_price_intersection_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of time-price intersection events in 252d."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_137_td_time_price_intersection_at_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Time-price intersection AND close = 252d max."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff().diff()

def f56_dems_138_td_intersection_failure_indicator_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Time-price intersection AND price > intersection level within 5 bars (failed)."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    fwd_max5 = high.rolling(WDAYS, min_periods=1).max().shift(WDAYS)
    fail = ((ev > 0.5) & (fwd_max5 > tdst * 1.02)).astype(float).shift(WDAYS)
    return (fail.where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_139_td_intersection_at_overbought_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Time-price intersection AND RSI14 > 70."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean() / dn.ewm(alpha=1.0/14, adjust=False, min_periods=14).mean().replace(0, np.nan)
    rsi = 100.0 - 100.0 / (1.0 + rs)
    return ((ev * (rsi > 70).astype(float)).where(ev.notna() & rsi.notna(), np.nan)).diff().diff().diff()

def f56_dems_140_td_intersection_with_volume_distribution_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Time-price intersection AND volume > 21d-avg * 1.2."""
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_dist = (volume > 1.2 * v_avg).astype(float)
    return ((ev * vol_dist).where(ev.notna(), np.nan)).diff().diff().diff()

def f56_dems_141_demark_all_bearish_signal_count_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of {Differential, Anti-Differential, CLOP, CLOPWIN, Camouflage, TD Open, Power-of-3} bearish events in 252d."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    tot = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0)
    return (tot.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_142_demark_bearish_signal_breadth_at_252d_high_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 252d where >=2 DeMark bearish signals AND close = 252d max."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ind = ((cnt >= 2) & (close >= rmax - 1e-12)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_143_demark_extended_signal_intensity_zscore_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score over 252d of 21d total bearish DeMark signal count."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    cnt = (e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0)).rolling(MDAYS, min_periods=10).sum()
    return (_rolling_zscore(cnt, YDAYS)).diff().diff().diff()

def f56_dems_144_demark_bearish_signal_clustering_indicator_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 3+ different DeMark bearish signals in last 5 bars."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    any_5 = (e1.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e2.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e3.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e4.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e5.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e6.rolling(WDAYS, min_periods=1).max().fillna(0.0)
             + e7.rolling(WDAYS, min_periods=1).max().fillna(0.0))
    return ((any_5 >= 3).astype(float)).diff().diff().diff()

def f56_dems_145_demark_signal_freshness_min_age_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum bars-since-event across 7 DeMark bearish signals (newest signal age)."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    df = pd.concat([_bars_since_last_event(e).rename(i) for i, e in enumerate([e1, e2, e3, e4, e5, e6, e7])], axis=1)
    return (df.min(axis=1)).diff().diff().diff()

def f56_dems_146_demark_failed_setup_density_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Setup cancellations + Countdown cancellations + TD-line failures) / 252."""
    ev_s = _td_setup_cancelled_by_4bar_low_close(close)
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    ev_c = ((high > tdst_buy.shift(1)) & tdst_buy.notna()).astype(float).where(tdst_buy.notna(), np.nan)
    h21 = high.rolling(MDAYS, min_periods=10).max()
    broke = (close > h21.shift(1)).astype(float)
    qual = ((high - close) < (high - low)).astype(float)
    ev_line = broke * qual
    min5 = close.rolling(WDAYS, min_periods=1).min().shift(WDAYS)
    ev_line_fail = ((ev_line > 0.5) & (min5 < h21.shift(1))).astype(float).shift(WDAYS)
    tot = ev_s.fillna(0.0) + ev_c.fillna(0.0) + ev_line_fail.fillna(0.0)
    return (tot.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff().diff().diff()

def f56_dems_147_demark_master_bearish_score_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-summed: signal-density + breadth-at-high + cancellation-density + ts-price-intersection-count."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    tot = (e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    breadth_at_high = (tot * (close >= rmax - 1e-12).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    ev_s = _td_setup_cancelled_by_4bar_low_close(close)
    tdst_buy = _tdst_buy_level(high, low, close, 9)
    ev_c = ((high > tdst_buy.shift(1)) & tdst_buy.notna()).astype(float).where(tdst_buy.notna(), np.nan)
    canc = (ev_s.fillna(0.0) + ev_c.fillna(0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(tot, YDAYS); z2 = _rolling_zscore(breadth_at_high, YDAYS); z3 = _rolling_zscore(canc, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff().diff()

def f56_dems_148_demark_signal_x_volume_distribution_score_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total DeMark bearish signals with volume > 21d-avg, in 252d."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_above = (volume > v_avg).astype(float)
    tot = (e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0))
    return ((tot * vol_above).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f56_dems_149_demark_blowoff_signature_composite_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Master z-summed score weighted by close-z (close-z > 1 boosts) over 252d."""
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    tot = (e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0)).rolling(MDAYS, min_periods=10).sum()
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    return (tot * (zc > 1.0).astype(float)).diff().diff().diff()

def f56_dems_150_demark_top_completion_composite_score_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Buy-setup-9 at high + bearish-signal-density + TDST-updates + time-price-intersection over 252d."""
    bs = _td_setup_count_buy(close, 4)
    bs_at_high = ((bs == 9) & (close >= close.rolling(YDAYS, min_periods=QDAYS).max() - 1e-12)).astype(float)
    e1 = _td_differential_bearish(high, low, close); e2 = _td_anti_differential_bearish(close)
    e3 = _td_clop_bearish(open, close); e4 = _td_clopwin_bearish(open, close)
    e5 = _td_camouflage_bearish(open, high, low, close); e6 = _td_open_bearish(open, high, close)
    e7 = _td_power_of_3_bearish(open, close)
    tot = (e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0) + e6.fillna(0.0) + e7.fillna(0.0))
    ss = _td_setup_count_sell(close, 4)
    tdst = _tdst_sell_level(high, low, close, 9)
    near = (close >= tdst * 0.98) & (close <= tdst * 1.02)
    ev_int = ((ss >= 9) & near).astype(float).where(ss.notna() & tdst.notna(), np.nan)
    comp = bs_at_high.fillna(0.0) + tot.fillna(0.0) + ev_int.fillna(0.0)
    return (comp.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d3)
# ============================================================

DEMARK_EXTENDED_SIGNALS_D3_REGISTRY_076_150 = {
    "f56_dems_076_td_power_of_3_bearish_at_252d_high_indicator_d3": {"inputs": ["open", "close"], "func": f56_dems_076_td_power_of_3_bearish_at_252d_high_indicator_d3},
    "f56_dems_077_td_open_x_overbought_indicator_d3": {"inputs": ["open", "high", "close"], "func": f56_dems_077_td_open_x_overbought_indicator_d3},
    "f56_dems_078_td_power_of_3_days_since_last_bearish_d3": {"inputs": ["open", "close"], "func": f56_dems_078_td_power_of_3_days_since_last_bearish_d3},
    "f56_dems_079_td_open_at_252d_high_indicator_d3": {"inputs": ["open", "high", "close"], "func": f56_dems_079_td_open_at_252d_high_indicator_d3},
    "f56_dems_080_td_power_of_3_bearish_intensity_zscore_252d_d3": {"inputs": ["open", "close"], "func": f56_dems_080_td_power_of_3_bearish_intensity_zscore_252d_d3},
    "f56_dems_081_td_setup_cancelled_4bar_low_close_event_d3": {"inputs": ["close"], "func": f56_dems_081_td_setup_cancelled_4bar_low_close_event_d3},
    "f56_dems_082_td_setup_cancelled_count_252d_d3": {"inputs": ["close"], "func": f56_dems_082_td_setup_cancelled_count_252d_d3},
    "f56_dems_083_td_countdown_cancelled_by_tdst_break_event_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_083_td_countdown_cancelled_by_tdst_break_event_d3},
    "f56_dems_084_td_countdown_cancelled_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_084_td_countdown_cancelled_count_252d_d3},
    "f56_dems_085_td_setup_cancellation_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f56_dems_085_td_setup_cancellation_at_252d_high_indicator_d3},
    "f56_dems_086_td_setup_completion_to_cancellation_ratio_504d_d3": {"inputs": ["close"], "func": f56_dems_086_td_setup_completion_to_cancellation_ratio_504d_d3},
    "f56_dems_087_td_sequential_cancellation_density_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_087_td_sequential_cancellation_density_252d_d3},
    "f56_dems_088_td_setup_recovery_after_cancellation_indicator_d3": {"inputs": ["close"], "func": f56_dems_088_td_setup_recovery_after_cancellation_indicator_d3},
    "f56_dems_089_td_countdown_cancellation_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_089_td_countdown_cancellation_at_252d_high_indicator_d3},
    "f56_dems_090_td_sequential_pattern_failure_score_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_090_td_sequential_pattern_failure_score_252d_d3},
    "f56_dems_091_td_rebo_breakout_up_indicator_d3": {"inputs": ["high"], "func": f56_dems_091_td_rebo_breakout_up_indicator_d3},
    "f56_dems_092_td_rebo_breakout_down_indicator_d3": {"inputs": ["low"], "func": f56_dems_092_td_rebo_breakout_down_indicator_d3},
    "f56_dems_093_td_rebo_breakout_up_count_252d_d3": {"inputs": ["high"], "func": f56_dems_093_td_rebo_breakout_up_count_252d_d3},
    "f56_dems_094_td_rebo_breakout_down_count_252d_d3": {"inputs": ["low"], "func": f56_dems_094_td_rebo_breakout_down_count_252d_d3},
    "f56_dems_095_td_rebo_breakout_failure_after_252d_high_indicator_d3": {"inputs": ["high", "close"], "func": f56_dems_095_td_rebo_breakout_failure_after_252d_high_indicator_d3},
    "f56_dems_096_td_rebo_breakout_failure_count_252d_d3": {"inputs": ["high", "close"], "func": f56_dems_096_td_rebo_breakout_failure_count_252d_d3},
    "f56_dems_097_td_rebo_breakout_up_at_overbought_indicator_d3": {"inputs": ["high", "close"], "func": f56_dems_097_td_rebo_breakout_up_at_overbought_indicator_d3},
    "f56_dems_098_td_rebo_breakout_up_to_down_ratio_252d_d3": {"inputs": ["high", "low"], "func": f56_dems_098_td_rebo_breakout_up_to_down_ratio_252d_d3},
    "f56_dems_099_td_rebo_breakout_amplitude_pct_252d_d3": {"inputs": ["high"], "func": f56_dems_099_td_rebo_breakout_amplitude_pct_252d_d3},
    "f56_dems_100_td_rebo_breakout_velocity_count_per_year_d3": {"inputs": ["high", "low"], "func": f56_dems_100_td_rebo_breakout_velocity_count_per_year_d3},
    "f56_dems_101_td_d_wave_current_wave_number_proxy_d3": {"inputs": ["close", "high"], "func": f56_dems_101_td_d_wave_current_wave_number_proxy_d3},
    "f56_dems_102_td_d_wave_wave_5_indicator_proxy_d3": {"inputs": ["close", "high"], "func": f56_dems_102_td_d_wave_wave_5_indicator_proxy_d3},
    "f56_dems_103_td_d_wave_wave_5_at_252d_high_indicator_d3": {"inputs": ["close", "high"], "func": f56_dems_103_td_d_wave_wave_5_at_252d_high_indicator_d3},
    "f56_dems_104_td_d_wave_wave_c_indicator_proxy_d3": {"inputs": ["close", "low"], "func": f56_dems_104_td_d_wave_wave_c_indicator_proxy_d3},
    "f56_dems_105_td_d_wave_completed_5_count_504d_d3": {"inputs": ["close", "high"], "func": f56_dems_105_td_d_wave_completed_5_count_504d_d3},
    "f56_dems_106_td_d_wave_bars_since_wave_3_proxy_d3": {"inputs": ["close", "high"], "func": f56_dems_106_td_d_wave_bars_since_wave_3_proxy_d3},
    "f56_dems_107_td_d_wave_wave_5_extension_pct_d3": {"inputs": ["close", "high"], "func": f56_dems_107_td_d_wave_wave_5_extension_pct_d3},
    "f56_dems_108_td_d_wave_wave_5_truncated_indicator_d3": {"inputs": ["close", "high"], "func": f56_dems_108_td_d_wave_wave_5_truncated_indicator_d3},
    "f56_dems_109_td_d_wave_completed_c_count_504d_d3": {"inputs": ["close", "low"], "func": f56_dems_109_td_d_wave_completed_c_count_504d_d3},
    "f56_dems_110_td_d_wave_wave_5_failure_indicator_252d_d3": {"inputs": ["close", "high"], "func": f56_dems_110_td_d_wave_wave_5_failure_indicator_252d_d3},
    "f56_dems_111_td_trend_factor_upside_target_d3": {"inputs": ["close"], "func": f56_dems_111_td_trend_factor_upside_target_d3},
    "f56_dems_112_td_trend_factor_downside_target_d3": {"inputs": ["close"], "func": f56_dems_112_td_trend_factor_downside_target_d3},
    "f56_dems_113_td_trend_factor_upside_distance_pct_d3": {"inputs": ["close"], "func": f56_dems_113_td_trend_factor_upside_distance_pct_d3},
    "f56_dems_114_td_trend_factor_downside_distance_pct_d3": {"inputs": ["close"], "func": f56_dems_114_td_trend_factor_downside_distance_pct_d3},
    "f56_dems_115_td_trend_factor_breach_upside_indicator_d3": {"inputs": ["close"], "func": f56_dems_115_td_trend_factor_breach_upside_indicator_d3},
    "f56_dems_116_td_trend_factor_breach_downside_indicator_d3": {"inputs": ["close"], "func": f56_dems_116_td_trend_factor_breach_downside_indicator_d3},
    "f56_dems_117_td_trend_factor_upside_breach_count_252d_d3": {"inputs": ["close"], "func": f56_dems_117_td_trend_factor_upside_breach_count_252d_d3},
    "f56_dems_118_td_trend_factor_upside_breach_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f56_dems_118_td_trend_factor_upside_breach_at_252d_high_indicator_d3},
    "f56_dems_119_td_trend_factor_max_target_minus_current_252d_d3": {"inputs": ["close"], "func": f56_dems_119_td_trend_factor_max_target_minus_current_252d_d3},
    "f56_dems_120_td_trend_factor_target_failure_indicator_252d_d3": {"inputs": ["close"], "func": f56_dems_120_td_trend_factor_target_failure_indicator_252d_d3},
    "f56_dems_121_td_line_breakout_up_qualified_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_121_td_line_breakout_up_qualified_indicator_d3},
    "f56_dems_122_td_line_breakout_down_qualified_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_122_td_line_breakout_down_qualified_indicator_d3},
    "f56_dems_123_td_line_breakout_up_failure_indicator_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_123_td_line_breakout_up_failure_indicator_252d_d3},
    "f56_dems_124_td_line_breakout_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_124_td_line_breakout_count_252d_d3},
    "f56_dems_125_td_line_qualified_breakout_at_252d_high_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_125_td_line_qualified_breakout_at_252d_high_count_252d_d3},
    "f56_dems_126_td_aggressive_setup_9_event_indicator_d3": {"inputs": ["close"], "func": f56_dems_126_td_aggressive_setup_9_event_indicator_d3},
    "f56_dems_127_td_aggressive_setup_9_count_252d_d3": {"inputs": ["close"], "func": f56_dems_127_td_aggressive_setup_9_count_252d_d3},
    "f56_dems_128_td_aggressive_countdown_13_count_252d_d3": {"inputs": ["close", "high"], "func": f56_dems_128_td_aggressive_countdown_13_count_252d_d3},
    "f56_dems_129_td_aggressive_setup_9_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f56_dems_129_td_aggressive_setup_9_at_252d_high_indicator_d3},
    "f56_dems_130_td_aggressive_setup_9_vs_standard_ratio_252d_d3": {"inputs": ["close"], "func": f56_dems_130_td_aggressive_setup_9_vs_standard_ratio_252d_d3},
    "f56_dems_131_td_termination_count_value_proxy_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_131_td_termination_count_value_proxy_d3},
    "f56_dems_132_td_termination_completion_event_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_132_td_termination_completion_event_indicator_d3},
    "f56_dems_133_td_termination_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_133_td_termination_at_252d_high_indicator_d3},
    "f56_dems_134_td_termination_to_setup_ratio_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_134_td_termination_to_setup_ratio_252d_d3},
    "f56_dems_135_td_time_price_intersection_event_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_135_td_time_price_intersection_event_indicator_d3},
    "f56_dems_136_td_time_price_intersection_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_136_td_time_price_intersection_count_252d_d3},
    "f56_dems_137_td_time_price_intersection_at_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_137_td_time_price_intersection_at_high_indicator_d3},
    "f56_dems_138_td_intersection_failure_indicator_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_138_td_intersection_failure_indicator_252d_d3},
    "f56_dems_139_td_intersection_at_overbought_indicator_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_139_td_intersection_at_overbought_indicator_d3},
    "f56_dems_140_td_intersection_with_volume_distribution_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f56_dems_140_td_intersection_with_volume_distribution_indicator_d3},
    "f56_dems_141_demark_all_bearish_signal_count_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_141_demark_all_bearish_signal_count_252d_d3},
    "f56_dems_142_demark_bearish_signal_breadth_at_252d_high_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_142_demark_bearish_signal_breadth_at_252d_high_252d_d3},
    "f56_dems_143_demark_extended_signal_intensity_zscore_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_143_demark_extended_signal_intensity_zscore_252d_d3},
    "f56_dems_144_demark_bearish_signal_clustering_indicator_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_144_demark_bearish_signal_clustering_indicator_252d_d3},
    "f56_dems_145_demark_signal_freshness_min_age_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_145_demark_signal_freshness_min_age_252d_d3},
    "f56_dems_146_demark_failed_setup_density_252d_d3": {"inputs": ["high", "low", "close"], "func": f56_dems_146_demark_failed_setup_density_252d_d3},
    "f56_dems_147_demark_master_bearish_score_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_147_demark_master_bearish_score_252d_d3},
    "f56_dems_148_demark_signal_x_volume_distribution_score_252d_d3": {"inputs": ["open", "high", "low", "close", "volume"], "func": f56_dems_148_demark_signal_x_volume_distribution_score_252d_d3},
    "f56_dems_149_demark_blowoff_signature_composite_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_149_demark_blowoff_signature_composite_252d_d3},
    "f56_dems_150_demark_top_completion_composite_score_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f56_dems_150_demark_top_completion_composite_score_252d_d3},
}
