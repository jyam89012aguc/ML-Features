"""topping_pattern_classical base 151-225 — Pipeline 1b-technical.

Gap-fill extension of 03_topping_pattern_classical (see __base__001_075.py
and __base__076_150.py for first 150 hypotheses). This file covers themes
that were NOT in the first 150 features and are NOT reserved by other
1b families:

    Bucket A — Tom DeMark indicator family               (151-160)
    Bucket B — Point-and-Figure tops                     (161-168)
    Bucket C — Andrews pitchfork & Gann angles           (169-176)
    Bucket D — Elliott wave heuristic counters           (177-182)
    Bucket E — Wyckoff distribution refinement           (183-190)
    Bucket F — Bulkowski-style pattern statistics        (191-197)
    Bucket G — Specialty / textbook reversal patterns    (198-205)
    Bucket H — Pattern strength / breadth                (206-213)
    Bucket I — Template-matching / signature recognition (214-218)
    Bucket J — Hidden / failed-confirmation patterns     (219-222)
    Bucket K — Narrow tpcl-internal composites           (223-225)

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
No scipy / statsmodels — numpy + pandas only.
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
    """Elementwise safe division returning a Series."""
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
    return pd.concat(
        [high - low, (high - pc).abs(), (low - pc).abs()],
        axis=1,
    ).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(
        n, min_periods=max(n // 3, 2)
    ).mean()


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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan

    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _pivot3_high_mask(high: pd.Series) -> pd.Series:
    """PIT pivot: bar (i-3) is a high if high[i-3] is strictly greater than
    high[i-1], high[i-2], high[i-4], high[i-5], high[i-6]. Output at index i
    flags whether (i-3) was a pivot — all comparisons are against past bars
    relative to i. Returns float 0/1 series."""
    h = high
    p = h.shift(3)
    cond = (
        (p > h.shift(1))
        & (p > h.shift(2))
        & (p > h.shift(4))
        & (p > h.shift(5))
        & (p > h.shift(6))
    )
    return cond.astype(float)


def _pivot3_low_mask(low: pd.Series) -> pd.Series:
    p = low.shift(3)
    cond = (
        (p < low.shift(1))
        & (p < low.shift(2))
        & (p < low.shift(4))
        & (p < low.shift(5))
        & (p < low.shift(6))
    )
    return cond.astype(float)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _rsi(close, n=14):
    diff = close.diff()
    up = diff.clip(lower=0)
    down = (-diff).clip(lower=0)
    au = up.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    ad = down.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    rs = au / ad.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _macd_hist(close, fast=12, slow=26, sig=9):
    macd = _ema(close, fast) - _ema(close, slow)
    signal = _ema(macd, sig)
    return macd - signal


def f03_tpcl_151_td_setup_completion_count_252d_d3(close: pd.Series) -> pd.Series:
    """Tom DeMark Buy/Sell Setup: count of completed 9-bar Sell Setups within
    last 252 bars (price closes > close 4 bars ago for 9 consecutive bars).
    High counts at a top indicate upside exhaustion (sell-setup completions)."""
    flip = (close > close.shift(4)).astype(float)
    # rolling 9-bar window all-true
    completed = flip.rolling(9, min_periods=9).sum() == 9
    return (completed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_152_td_combo_completion_count_252d_d3(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """TD Combo (Sell): 13-bar exhaustion. Bar qualifies if close > close.shift(2)
    AND high > previous high. Count completed 13-bar runs within 252d."""
    qual = ((close > close.shift(2)) & (high > high.shift(1))).astype(float)
    completed = qual.rolling(13, min_periods=13).sum() == 13
    return (completed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_153_td_sequential_exhaustion_bar_count_252d_d3(close: pd.Series) -> pd.Series:
    """TD Sequential count (sell-side exhaustion): rolling consecutive bars
    closing above close.shift(4). Reported as max consecutive run within 252d."""
    flip = (close > close.shift(4)).astype(int)
    # streak length
    grp = (flip != flip.shift(1)).cumsum()
    streak = flip.groupby(grp).cumsum() * flip
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f03_tpcl_154_td_pressure_at_top_63d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Pressure-style: (close - low) / (high - low) averaged over 21d, then
    deviation from its 63d mean. High = aggressive buyers; sudden DROP after
    sustained high = topping pressure release."""
    intrabar = _safe_div(close - low, high - low)
    short_p = intrabar.rolling(MDAYS, min_periods=WDAYS).mean()
    long_p = intrabar.rolling(QDAYS, min_periods=MDAYS).mean()
    return (short_p - long_p).diff().diff().diff()


def f03_tpcl_155_td_range_projection_breach_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Range Projection (next-bar upper projection). Computed as
        upper = high.shift(1) + (high.shift(1) - low.shift(1)).
    Indicator: count within 252d of bars where actual high pierced upper
    projection (over-extension events) MINUS bars where high failed to reach
    median projection. Net positive = upper-projection breach regime."""
    rng_prev = high.shift(1) - low.shift(1)
    upper = high.shift(1) + rng_prev
    median = high.shift(1) + 0.5 * rng_prev
    breached = (high > upper).astype(float)
    failed = (high < median).astype(float)
    return ((breached - failed).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_156_td_differential_at_peak_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Differential: bar qualifies when (close - low) > (close - low).shift(1)
    AND (high - close) < (high - close).shift(1) on a day after a higher close.
    Count qualifying events in last 63d at proximity to 63d high."""
    buy_pressure = close - low
    sell_pressure = high - close
    cond = (
        (close > close.shift(1))
        & (buy_pressure > buy_pressure.shift(1))
        & (sell_pressure < sell_pressure.shift(1))
    )
    raw = cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    near_high = (close >= high.rolling(QDAYS, min_periods=MDAYS).max() * 0.97).astype(float)
    return (raw * near_high).diff().diff().diff()


def f03_tpcl_157_td_reverse_setup_qualifier_252d_d3(close: pd.Series) -> pd.Series:
    """TD Reverse Setup (post-Sell-Setup): after a 9-count Sell Setup, qualifies
    if 2 bars later close > prior 2 bars (continuation). Indicator returns
    rolling 252d count of reverse-setup qualifiers (failed reversals).
    Lower count = cleaner top."""
    flip = (close > close.shift(4)).astype(float)
    sell_complete = flip.rolling(9, min_periods=9).sum() == 9
    # 2 bars after completion, did close keep ascending?
    rev_qual = sell_complete.shift(2).fillna(False) & (close > close.shift(2))
    return (rev_qual.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_158_td_camouflage_event_count_63d_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Camouflage: bar appears bearish (close < open) yet closes ABOVE
    close.shift(1) (hidden bullish) — at a top this is the inverse: bar
    appears bullish (close > open) yet closes BELOW close.shift(1). Count of
    bearish-camouflage events in last 63d."""
    cond = (close > open_) & (close < close.shift(1))
    return (cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f03_tpcl_159_td_open_downcross_in_setup_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """TD Open-downcross within a 9-bar Sell Setup: count of bars where
    open opened above close.shift(1) but closed below close.shift(1). This
    'gap-up then close-down' pattern undermines setup validity. Count over 252d."""
    cond = (open_ > close.shift(1)) & (close < close.shift(1))
    return (cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_160_td_countdown_completion_event_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Countdown (Sell, simplified): after a 9-bar Setup completion, count bars
    where close >= high.shift(2). When that cumulative count reaches 13, mark
    completion. Reports rolling 252d count of countdown-completion events."""
    flip = (close > close.shift(4)).astype(float)
    setup = flip.rolling(9, min_periods=9).sum() == 9
    # countdown qualifier
    cd_qual = (close >= high.shift(2)).astype(int)
    # cumulative qualifier count since the latest setup
    bars_since_setup = setup.astype(int)
    grp = bars_since_setup.cumsum()
    # within each setup group, rolling sum of cd_qual
    cd_count = cd_qual.groupby(grp).cumsum() * (grp > 0).astype(int)
    completion = (cd_count >= 13) & (cd_count.shift(1) < 13)
    return (completion.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def _pnf_columns(close: pd.Series, atr: pd.Series, box_mult: float = 0.5, reversal: int = 3):
    """Helper: derive an integer column ID per bar of a P&F approximation
    (ATR-scaled boxes). Returns Series of column-IDs aligned to input index.
    Column direction can be recovered from sign of column-end value of close."""
    box = (atr * box_mult).clip(lower=1e-9)
    n = len(close)
    col_id = np.zeros(n, dtype=float)
    direction = 0  # +1 X (up) / -1 O (down)
    col_high = np.nan
    col_low = np.nan
    cid = 0
    for i in range(n):
        c = close.iat[i]
        b = box.iat[i]
        if np.isnan(c) or np.isnan(b) or b <= 0:
            col_id[i] = np.nan
            continue
        if direction == 0:
            col_high = c
            col_low = c
            direction = 1
            col_id[i] = cid
            continue
        if direction == 1:
            if c >= col_high:
                col_high = c
                col_id[i] = cid
            elif (col_high - c) >= reversal * b:
                cid += 1
                direction = -1
                col_low = c
                col_high = c
                col_id[i] = cid
            else:
                col_id[i] = cid
        else:
            if c <= col_low:
                col_low = c
                col_id[i] = cid
            elif (c - col_low) >= reversal * b:
                cid += 1
                direction = 1
                col_high = c
                col_low = c
                col_id[i] = cid
            else:
                col_id[i] = cid
    return pd.Series(col_id, index=close.index)


def f03_tpcl_161_pnf_consecutive_x_columns_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Approximate P&F (ATR-box 0.5x ATR21, 3-box reversal). Within the last 252
    bars, count of consecutive X (up) columns ending at most 21 bars ago.
    High counts mean repeated up-thrusts — classic distribution top pattern."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    # mean close per column → direction = sign of diff
    col_mean = close.groupby(col).transform("mean")
    col_id_change = (col != col.shift(1)).astype(int)
    # rebuild per-column direction by checking close mean at column transitions
    # simpler: direction at bar i = sign(close.iat[i] - column_start_close)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        # find column-ids
        unique = []
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                unique.append(int(x))
                starts.append(k)
                last = int(x)
        # determine direction of each column
        directions = []
        for j, s in enumerate(starts):
            e = starts[j + 1] - 1 if j + 1 < len(starts) else len(seg) - 1
            directions.append(1 if seg_c[e] > seg_c[s] else -1)
        # count consecutive Xs at tail
        cnt = 0
        for d in reversed(directions):
            if d == 1:
                cnt += 1
            else:
                break
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_162_pnf_triple_top_then_fail_event_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F triple-top breakout: 3 X-columns with equal-or-rising tops, then a
    subsequent O-column that breaches the prior O low. Count events in 252d."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        events = 0
        # need at least 7 columns to see 3 X + intervening O + failing O
        for j in range(6, len(starts)):
            e = starts[j] if j == len(starts) else starts[j]
            # last 7 columns: indices j-6..j
            cols = []
            for k in range(j - 6, j + 1):
                s = starts[k]
                e2 = starts[k + 1] - 1 if k + 1 < len(starts) else len(seg) - 1
                cols.append((seg_c[s], seg_c[e2]))
            # X = col[1] > col[0], O = col[1] < col[0]
            dirs = [1 if b > a else -1 for a, b in cols]
            if dirs == [1, -1, 1, -1, 1, -1, -1]:  # 3 X with Os between, then 2 Os
                tops = [cols[0][1], cols[2][1], cols[4][1]]
                if tops[1] >= tops[0] and tops[2] >= tops[1]:
                    if cols[6][1] < cols[5][0]:  # failure
                        events += 1
        out[i] = float(events)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_163_pnf_descending_tops_x_column_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F descending-tops pattern: 3+ X-columns where each successive X-top is
    LOWER than the prior — triangle top. Indicator returns count over 252d."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        # collect X-column tops
        x_tops = []
        for k in range(len(starts)):
            s = starts[k]
            e = starts[k + 1] - 1 if k + 1 < len(starts) else len(seg) - 1
            if seg_c[e] > seg_c[s]:
                x_tops.append(seg_c[e])
        # count descending triplets
        cnt = 0
        for k in range(2, len(x_tops)):
            if x_tops[k] < x_tops[k - 1] < x_tops[k - 2]:
                cnt += 1
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_164_pnf_bull_trap_signal_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F bull-trap: X-column makes a 1-box new high above prior X, then
    immediately reverses 3 boxes (O column) below the prior X top. Count events."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        x_tops = []
        for k in range(len(starts)):
            s = starts[k]
            e = starts[k + 1] - 1 if k + 1 < len(starts) else len(seg) - 1
            if seg_c[e] > seg_c[s]:
                x_tops.append((k, seg_c[e]))
        events = 0
        for j in range(1, len(x_tops)):
            k_curr, top_curr = x_tops[j]
            _, top_prev = x_tops[j - 1]
            if top_curr > top_prev:
                # next column should be O (reverse) — check follow
                if k_curr + 1 < len(starts):
                    s2 = starts[k_curr + 1]
                    e2 = starts[k_curr + 2] - 1 if k_curr + 2 < len(starts) else len(seg) - 1
                    if seg_c[e2] < seg_c[s2] and seg_c[e2] < top_prev:
                        events += 1
        out[i] = float(events)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_165_pnf_box_count_target_projection_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F downward count-target projection from the latest column-cluster:
    target_down = column_top - box_size * boxes_in_pattern * reversal.
    Returns distance from current close to target (normalized by current close).
    Negative = target ABOVE current price (already overshot); positive = below."""
    atr = _atr(high, low, close, n=21)
    box = (atr * 0.5).clip(lower=1e-9)
    col = _pnf_columns(close, atr)
    # most recent X-top within 63d, count active boxes in that column
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    bv = box.values
    for i in range(YDAYS, len(close)):
        lo = max(0, i - QDAYS + 1)
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any() or np.isnan(bv[i]):
            continue
        # last column slice
        last_col = seg[-1]
        col_mask = seg == last_col
        if col_mask.sum() < 2:
            continue
        col_top = seg_c[col_mask].max()
        col_bot = seg_c[col_mask].min()
        boxes = max(int(round((col_top - col_bot) / bv[i])), 1)
        target = col_top - bv[i] * boxes * 3.0
        out[i] = (c[i] - target) / c[i] if c[i] != 0 else np.nan
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_166_pnf_distribution_top_column_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F distribution-top: total number of X-columns within 252d where the
    X-column top is within 5% of the 252d max — congestion at top."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        cmax = seg_c.max()
        thr = cmax * 0.95
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        cnt = 0
        for k in range(len(starts)):
            s = starts[k]
            e = starts[k + 1] - 1 if k + 1 < len(starts) else len(seg) - 1
            if seg_c[e] > seg_c[s]:  # X column
                if seg_c[e] >= thr:
                    cnt += 1
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_167_pnf_box_reversal_frequency_at_top_63d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F reversal frequency in last 63d (number of column changes per 63 bars).
    Higher = choppier / more uncertain = topping behaviour."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    chg = (col != col.shift(1)).astype(float)
    return (chg.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f03_tpcl_168_pnf_column_high_low_symmetry_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """P&F column high-low symmetry: ratio of average X-column height to average
    O-column depth within 252d. Near 1.0 = symmetric (consolidation top);
    >1.5 = upward dominance; <0.5 = downward dominance."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        x_heights = []
        o_depths = []
        for k in range(len(starts)):
            s = starts[k]
            e = starts[k + 1] - 1 if k + 1 < len(starts) else len(seg) - 1
            if seg_c[e] > seg_c[s]:
                x_heights.append(seg_c[e] - seg_c[s])
            else:
                o_depths.append(seg_c[s] - seg_c[e])
        if not x_heights or not o_depths:
            continue
        out[i] = float(np.mean(x_heights) / max(np.mean(o_depths), 1e-12))
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_169_andrews_median_line_distance_at_top_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Andrews pitchfork: anchor at lowest-low ~252 bars ago, then two recent
    pivots at ~168 and ~84 bars ago — median line connects anchor to midpoint
    of the two pivots. Indicator: (close - median_line_value) / median_value.
    Strongly positive = price riding above median = extension / top regime."""
    out = np.full(len(close), np.nan)
    l = low.values
    h = high.values
    c = close.values
    for i in range(YDAYS, len(close)):
        # anchor: lowest-low in [i-251..i-168]
        a_lo = i - YDAYS + 1
        a_hi = i - 167
        if a_lo < 0 or a_hi >= len(close):
            continue
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:a_hi + 1]))
        anchor_val = l[anchor_idx]
        # two pivots: highest-high in [i-167..i-84] and [i-83..i-1]
        p1_lo, p1_hi = i - 167, i - 84
        p2_lo, p2_hi = i - 83, i - 1
        if p1_lo < 0 or p2_lo < 0:
            continue
        p1_idx = p1_lo + int(np.nanargmax(h[p1_lo:p1_hi + 1]))
        p2_idx = p2_lo + int(np.nanargmax(h[p2_lo:p2_hi + 1]))
        p1_val = h[p1_idx]
        p2_val = h[p2_idx]
        mid_idx = (p1_idx + p2_idx) / 2.0
        mid_val = (p1_val + p2_val) / 2.0
        # median-line slope
        if mid_idx == anchor_idx:
            continue
        slope = (mid_val - anchor_val) / (mid_idx - anchor_idx)
        med_now = anchor_val + slope * (i - anchor_idx)
        if med_now <= 0:
            continue
        out[i] = (c[i] - med_now) / med_now
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_170_andrews_upper_channel_touch_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Andrews pitchfork upper-channel-line touch count within 252d. Repeated
    upper-tine touches = strong resistance at top tine."""
    out = np.full(len(close), np.nan)
    l = low.values
    h = high.values
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        a_hi = i - 167
        if a_lo < 0:
            continue
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:a_hi + 1]))
        anchor_val = l[anchor_idx]
        p1_lo, p1_hi = i - 167, i - 84
        p2_lo, p2_hi = i - 83, i - 1
        if p1_lo < 0 or p2_lo < 0:
            continue
        p1_idx = p1_lo + int(np.nanargmax(h[p1_lo:p1_hi + 1]))
        p2_idx = p2_lo + int(np.nanargmax(h[p2_lo:p2_hi + 1]))
        p1_val = h[p1_idx]
        p2_val = h[p2_idx]
        mid_idx = (p1_idx + p2_idx) / 2.0
        mid_val = (p1_val + p2_val) / 2.0
        if mid_idx == anchor_idx:
            continue
        slope = (mid_val - anchor_val) / (mid_idx - anchor_idx)
        # upper tine passes through max(p1_val, p2_val) at corresponding x
        if p1_val >= p2_val:
            base_idx, base_val = p1_idx, p1_val
        else:
            base_idx, base_val = p2_idx, p2_val
        # tine line parallel to median, anchored at base
        cnt = 0
        for k in range(a_lo, i + 1):
            tine = base_val + slope * (k - base_idx)
            if not np.isnan(h[k]) and abs(h[k] - tine) / max(abs(tine), 1e-9) < 0.01:
                cnt += 1
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_171_andrews_lower_channel_break_event_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Andrews pitchfork LOWER tine break (downside-confirmation): 1 if close
    breaks below the lower tine within last 21d, 0 otherwise."""
    out = np.full(len(close), np.nan)
    l = low.values
    h = high.values
    c = close.values
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        a_hi = i - 167
        if a_lo < 0:
            continue
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:a_hi + 1]))
        anchor_val = l[anchor_idx]
        p1_lo, p1_hi = i - 167, i - 84
        p2_lo, p2_hi = i - 83, i - 1
        if p1_lo < 0 or p2_lo < 0:
            continue
        p1_idx = p1_lo + int(np.nanargmax(h[p1_lo:p1_hi + 1]))
        p2_idx = p2_lo + int(np.nanargmax(h[p2_lo:p2_hi + 1]))
        p1_val = h[p1_idx]
        p2_val = h[p2_idx]
        mid_idx = (p1_idx + p2_idx) / 2.0
        mid_val = (p1_val + p2_val) / 2.0
        if mid_idx == anchor_idx:
            continue
        slope = (mid_val - anchor_val) / (mid_idx - anchor_idx)
        if p1_val <= p2_val:
            base_idx, base_val = p1_idx, p1_val
        else:
            base_idx, base_val = p2_idx, p2_val
        # lower tine
        broke = 0
        for k in range(max(a_lo, i - MDAYS + 1), i + 1):
            tine = base_val + slope * (k - base_idx)
            if not np.isnan(c[k]) and c[k] < tine:
                broke = 1
                break
        out[i] = float(broke)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_172_gann_1x1_distance_at_top_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gann 1x1 angle: 1 price unit per 1 time unit (in scale of 252d ATR).
    Anchor at 252d low, slope = ATR21 per bar. Indicator: (close - 1x1) / close.
    Above 1x1 = strong-trend regime (toppy); below = trend break."""
    out = np.full(len(close), np.nan)
    l = low.values
    c = close.values
    atr = _atr(high, low, close, n=21).values
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:i + 1]))
        anchor_val = l[anchor_idx]
        if np.isnan(atr[i]) or anchor_val <= 0:
            continue
        line = anchor_val + atr[i] * (i - anchor_idx)
        out[i] = (c[i] - line) / c[i] if c[i] != 0 else np.nan
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_173_gann_2x1_breakdown_event_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gann 2x1 (steep angle, 2 price units per 1 time unit). Breakdown event:
    close was above 2x1 line in past 63d, now below. 1 = breakdown today."""
    out = np.full(len(close), np.nan)
    l = low.values
    c = close.values
    atr = _atr(high, low, close, n=21).values
    above_prev = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:i + 1]))
        anchor_val = l[anchor_idx]
        if np.isnan(atr[i]) or anchor_val <= 0:
            continue
        line = anchor_val + 2.0 * atr[i] * (i - anchor_idx)
        above_prev[i] = 1.0 if c[i] > line else 0.0
    s = pd.Series(above_prev, index=close.index)
    # breakdown event: was above in [i-QDAYS..i-1] AND below at i
    was_above = s.shift(1).rolling(QDAYS, min_periods=WDAYS).max() > 0
    is_below = s == 0.0
    return ((was_above & is_below).astype(float)).diff().diff().diff()


def f03_tpcl_174_gann_1x2_pierce_event_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gann 1x2 angle (shallow, 1 price per 2 time). Pierce-event: count within
    252d of bars where close crossed from above to below the 1x2 line."""
    out = np.full(len(close), np.nan)
    l = low.values
    c = close.values
    atr = _atr(high, low, close, n=21).values
    above = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:i + 1]))
        anchor_val = l[anchor_idx]
        if np.isnan(atr[i]) or anchor_val <= 0:
            continue
        line = anchor_val + 0.5 * atr[i] * (i - anchor_idx)
        above[i] = 1.0 if c[i] > line else 0.0
    s = pd.Series(above, index=close.index)
    cross = ((s.shift(1) == 1.0) & (s == 0.0)).astype(float)
    return (cross.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_175_gann_square_of_9_cardinal_cross_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gann Square-of-9 cardinal-cross proximity: distance from current close to
    nearest 'cardinal' price level (square or square-plus-half of anchor low's
    square root). Returns normalized (close-distance)/close. Lower abs value =
    sitting on a cardinal level (potential reversal)."""
    out = np.full(len(close), np.nan)
    l = low.values
    c = close.values
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        anchor_val = np.nanmin(l[a_lo:i + 1])
        if anchor_val <= 0 or np.isnan(c[i]):
            continue
        root = np.sqrt(anchor_val)
        cur_root = np.sqrt(max(c[i], 1e-9))
        delta = cur_root - root
        # cardinal levels are at integer + half-integer increments of root delta
        nearest = round(delta * 2.0) / 2.0
        level_root = root + nearest
        level_price = level_root ** 2
        out[i] = (c[i] - level_price) / c[i] if c[i] != 0 else np.nan
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_176_gann_fan_resistance_hits_at_top_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gann fan: 5 angles (1x8, 1x4, 1x2, 1x1, 2x1) anchored at 252d low.
    Count bars within 252d whose high touches any of the 3 steepest angles."""
    out = np.full(len(close), np.nan)
    l = low.values
    h = high.values
    atr = _atr(high, low, close, n=21).values
    mults = [1.0, 2.0, 4.0]  # steeper angles
    for i in range(YDAYS, len(close)):
        a_lo = i - YDAYS + 1
        anchor_idx = a_lo + int(np.nanargmin(l[a_lo:i + 1]))
        anchor_val = l[anchor_idx]
        if anchor_val <= 0:
            continue
        cnt = 0
        for k in range(a_lo, i + 1):
            if np.isnan(atr[k]):
                continue
            for m in mults:
                line = anchor_val + m * atr[k] * (k - anchor_idx)
                if not np.isnan(h[k]) and abs(h[k] - line) / max(line, 1e-9) < 0.005:
                    cnt += 1
                    break
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def _zigzag_pivots(price: np.ndarray, threshold: float):
    """Crude zig-zag pivot finder: returns list of (idx, price, kind) where
    kind = +1 high, -1 low. PIT-internal use only — caller restricts windows."""
    pivots = []
    if len(price) < 3 or np.isnan(price).any():
        return pivots
    direction = 0  # +1 = looking for high, -1 = looking for low
    last_pivot_idx = 0
    last_pivot_val = price[0]
    for i in range(1, len(price)):
        if direction == 0:
            if price[i] >= last_pivot_val * (1 + threshold):
                direction = 1
                last_pivot_idx = 0
                last_pivot_val = price[0]
                pivots.append((0, price[0], -1))
            elif price[i] <= last_pivot_val * (1 - threshold):
                direction = -1
                pivots.append((0, price[0], 1))
            continue
        if direction == 1:
            if price[i] > last_pivot_val:
                last_pivot_idx = i
                last_pivot_val = price[i]
            elif price[i] <= last_pivot_val * (1 - threshold):
                pivots.append((last_pivot_idx, last_pivot_val, 1))
                direction = -1
                last_pivot_idx = i
                last_pivot_val = price[i]
        else:
            if price[i] < last_pivot_val:
                last_pivot_idx = i
                last_pivot_val = price[i]
            elif price[i] >= last_pivot_val * (1 + threshold):
                pivots.append((last_pivot_idx, last_pivot_val, -1))
                direction = 1
                last_pivot_idx = i
                last_pivot_val = price[i]
    return pivots


def f03_tpcl_177_elliott_5_wave_advance_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """Heuristic 5-wave advance: within last 252d, run zigzag (3% threshold),
    require sequence of pivots low-high-low-high-low-high-low-high-low-high
    with each new high higher than the previous and each new low higher than
    the previous low — Elliott-impulse skeleton ending at a high. Returns 1
    if such a sequence ends within the last 21d, else 0."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pv = _zigzag_pivots(seg, 0.03)
        if len(pv) < 10:
            out[i] = 0.0
            continue
        last10 = pv[-10:]
        # impulse pattern: starts low (-1) ends high (+1)
        kinds = [k for _, _, k in last10]
        if kinds != [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]:
            out[i] = 0.0
            continue
        # rising structure
        highs = [last10[j][1] for j in (1, 3, 5, 7, 9)]
        lows = [last10[j][1] for j in (0, 2, 4, 6, 8)]
        ascending = (
            highs[1] > highs[0]
            and highs[2] > highs[1]
            and highs[3] < highs[2]
            and highs[4] > highs[3]  # 5th makes new high
            and lows[1] > lows[0]
            and lows[2] > lows[1]
            and lows[3] > lows[2]
        )
        # 5th pivot end must be within last 21 bars of the 252-window
        end_idx = last10[-1][0]
        recent = (len(seg) - 1 - end_idx) < MDAYS
        out[i] = 1.0 if (ascending and recent) else 0.0
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_178_elliott_wave5_truncation_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """5th-wave truncation: 5th wave fails to exceed wave-3 top. After 5-wave
    structure, returns 1 if final high <= prior (wave-3) high."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pv = _zigzag_pivots(seg, 0.03)
        if len(pv) < 10:
            out[i] = 0.0
            continue
        last10 = pv[-10:]
        kinds = [k for _, _, k in last10]
        if kinds != [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]:
            out[i] = 0.0
            continue
        highs = [last10[j][1] for j in (1, 3, 5, 7, 9)]
        # wave-1=highs[1], wave-3=highs[2], wave-5=highs[4]
        out[i] = 1.0 if highs[4] <= highs[2] else 0.0
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_179_elliott_wave5_extension_excess_252d_d3(close: pd.Series) -> pd.Series:
    """5th-wave extension excess: ratio of wave-5 length to wave-1 length.
    >2.618 = extended fifth (terminal). Returns the ratio (NaN if no structure)."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pv = _zigzag_pivots(seg, 0.03)
        if len(pv) < 10:
            continue
        last10 = pv[-10:]
        kinds = [k for _, _, k in last10]
        if kinds != [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]:
            continue
        vals = [last10[j][1] for j in range(10)]
        wave1 = vals[1] - vals[0]
        wave5 = vals[9] - vals[8]
        if wave1 <= 0:
            continue
        out[i] = wave5 / wave1
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_180_elliott_abc_correction_start_event_63d_d3(close: pd.Series) -> pd.Series:
    """A-B-C corrective onset after a peak: zigzag identifies high-low-high-low
    (3-leg zigzag) sequence in last 63d where the latest pivot is a lower low
    relative to the earlier low. Returns 1 if start within 21d."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(QDAYS, len(close)):
        lo = i - QDAYS + 1
        seg = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pv = _zigzag_pivots(seg, 0.02)
        if len(pv) < 4:
            out[i] = 0.0
            continue
        last4 = pv[-4:]
        kinds = [k for _, _, k in last4]
        if kinds != [1, -1, 1, -1]:
            out[i] = 0.0
            continue
        vals = [v for _, v, _ in last4]
        # B-wave high < A-wave high; C-wave low < A-wave low
        cond = vals[2] < vals[0] and vals[3] < vals[1]
        end_idx = last4[-1][0]
        recent = (len(seg) - 1 - end_idx) < MDAYS
        out[i] = 1.0 if (cond and recent) else 0.0
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_181_elliott_diagonal_triangle_ending_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ending diagonal (terminal wedge with overlapping wave-4): rising slopes
    of highs AND lows, slope of highs < slope of lows (converging), and wave-4
    overlap (a recent local low penetrates the prior wave-1 high)."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        lo = i - QDAYS + 1
        seg = c[lo:i + 1]
        seg_h = high.values[lo:i + 1]
        seg_l = low.values[lo:i + 1]
        if np.isnan(seg).any():
            continue
        x = np.arange(len(seg), dtype=float)
        if seg_h.std() == 0 or seg_l.std() == 0:
            continue
        sh = np.polyfit(x, seg_h, 1)[0]
        sl = np.polyfit(x, seg_l, 1)[0]
        if sh > 0 and sl > 0 and sh < sl:
            pv = _zigzag_pivots(seg, 0.02)
            if len(pv) >= 4:
                # wave-1 high = pv[1], wave-4 low = pv[3]
                if pv[0][2] == -1 and pv[1][2] == 1 and pv[3][2] == -1:
                    if pv[3][1] < pv[1][1]:  # overlap
                        out[i] = 1.0
                        continue
        out[i] = 0.0
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_182_elliott_five_three_density_252d_d3(close: pd.Series) -> pd.Series:
    """Five-three pattern density: count of independent (5-up, 3-down) skeleton
    detections in 252d, using crude zigzag (5% threshold)."""
    c = close.values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = c[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pv = _zigzag_pivots(seg, 0.05)
        cnt = 0
        # slide a window of 13 pivots = (5-up sequence of 10 pivots + 3-correction of 3 pivots beyond)
        # easier: count subsequences of [+1,-1,+1,-1,+1,-1,+1,-1,+1,-1,+1] (5-up ending high)
        # followed by [-1,+1,-1] (3 corrective)
        kinds = [k for _, _, k in pv]
        target_up = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
        for k in range(len(kinds) - 12):
            if kinds[k:k + 10] == target_up and kinds[k + 10:k + 13] == [-1, 1, -1]:
                cnt += 1
        out[i] = float(cnt)
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_183_wyckoff_selling_climax_intensity_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling-climax intensity: vol-weighted (close-low) / range on bars where
    volume is in top 5% of last 252d AND range is in top 5% of last 252d.
    Used here for SC (selling climax) detection within distribution range —
    returns the largest event value within last 21d."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    vol_rank = volume.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    rng_rank = rng.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    climax = (vol_rank > 0.95) & (rng_rank > 0.95)
    intensity = pos.where(climax, 0.0) * volume
    norm = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    score = _safe_div(intensity, norm)
    return (score.rolling(MDAYS, min_periods=WDAYS).max()).diff().diff().diff()


def f03_tpcl_184_wyckoff_automatic_reaction_depth_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Automatic Reaction (AR) depth: after a buying-climax-style spike (top 5%
    range bar), measure the lowest low within the next 21d relative to the
    spike high. Returns the deepest AR pull (as fraction of spike high)."""
    rng = high - low
    rng_rank = rng.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    spike = rng_rank > 0.95
    spike_high = high.where(spike, np.nan)
    spike_high_ff = spike_high.shift(1).ffill(limit=MDAYS)
    bars_since = (spike.shift(1).cumsum() == spike.shift(1).cumsum()).astype(int)
    # depth = (spike_high - rolling-min-low) / spike_high
    rolling_low = low.rolling(MDAYS, min_periods=WDAYS).min()
    depth = _safe_div(spike_high_ff - rolling_low, spike_high_ff)
    return (depth.rolling(MDAYS, min_periods=WDAYS).max()).diff().diff().diff()


def f03_tpcl_185_wyckoff_secondary_test_failure_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Secondary Test (ST) failure: after an AR low, a rally that fails to
    exceed prior climax high on LIGHTER volume. Indicator: rolling 252d count
    of bars where (close is within 2% of prior 21d high) AND (volume is below
    63d median) AND (high < 252d max). Higher = repeated weak retests = top."""
    near_top = close >= high.rolling(MDAYS, min_periods=WDAYS).max() * 0.98
    light_vol = volume < volume.rolling(QDAYS, min_periods=MDAYS).median()
    below_max = high < high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = near_top & light_vol & below_max
    return (cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_186_wyckoff_trading_range_persistence_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Trading-range boundary persistence: count of bars in last 252d where
    high stays within +/- 5% of the rolling 63d max-high — measures the
    duration of sideways congestion / Wyckoff range."""
    cap = high.rolling(QDAYS, min_periods=MDAYS).max()
    floor = cap * 0.90
    inside = (high <= cap) & (low >= floor)
    return (inside.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_187_wyckoff_sign_of_weakness_angle_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign-of-Weakness (SOW): negative slope of close over 21d AFTER price was
    near 252d max in the prior 63d. Returns the slope when condition met."""
    s21 = _rolling_slope(close, MDAYS)
    near_max = (close.shift(MDAYS) >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(MDAYS) * 0.97)
    return (s21.where(near_max & (s21 < 0), np.nan)).diff().diff().diff()


def f03_tpcl_188_wyckoff_last_point_of_supply_event_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Last Point of Supply (LPSY): final lower-high retest after sign-of-weakness
    with declining volume. Event: bar where high is between 95-98% of 252d max,
    21d close-slope < 0, and 21d-volume below 63d median."""
    near = (high >= high.rolling(YDAYS, min_periods=QDAYS).max() * 0.95) & (
        high < high.rolling(YDAYS, min_periods=QDAYS).max() * 0.98
    )
    sl = _rolling_slope(close, MDAYS)
    vol_med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    vol_short = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = near & (sl < 0) & (vol_short < vol_med)
    return (cond.astype(float)).diff().diff().diff()


def f03_tpcl_189_wyckoff_upthrust_intensity_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Upthrust (UT/UTAD): bar makes new 252d high but closes back below prior
    21d high. Intensity = (new_high - close) / (high - low), volume-weighted.
    Returns max intensity within last 21d."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    prior_21_high = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    closes_back_below = close < prior_21_high
    rng = (high - low).replace(0, np.nan)
    intensity = _safe_div(high - close, rng)
    vol_rank = volume.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    weighted = intensity * vol_rank
    event = weighted.where(new_high & closes_back_below, 0.0)
    return (event.rolling(MDAYS, min_periods=WDAYS).max()).diff().diff().diff()


def f03_tpcl_190_wyckoff_spring_vs_upthrust_polarity_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net polarity of UT events MINUS spring events within last 63d. Positive =
    distribution-dominant (top); negative = accumulation-dominant (bottom)."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    prior_21_high = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    ut = new_high & (close < prior_21_high)
    new_low = low <= low.rolling(YDAYS, min_periods=QDAYS).min().shift(1)
    prior_21_low = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    spring = new_low & (close > prior_21_low)
    return ((ut.astype(float) - spring.astype(float)).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f03_tpcl_191_hs_breakdown_move_zscore_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """H&S average breakdown move (post-neckline-break: close drop over next 21d
    expressed as fraction of pattern height), then z-score over 504d. Higher
    z = breakdown stronger than typical for this stock."""
    p3h = _pivot3_high_mask(high)
    pivot_count = p3h.rolling(QDAYS, min_periods=MDAYS).sum()
    # head height proxy = 63d max - 21d trough
    head_h = high.rolling(QDAYS, min_periods=MDAYS).max()
    neckline = low.rolling(MDAYS, min_periods=WDAYS).min()
    pat_h = (head_h - neckline).replace(0, np.nan)
    move_21d = close.shift(MDAYS) - close
    norm_move = _safe_div(move_21d, pat_h)
    # only when h&s-like (>=3 pivots in 63d)
    proxy = norm_move.where(pivot_count >= 3, np.nan)
    return (_rolling_zscore(proxy, DDAYS_2Y, min_periods=YDAYS)).diff().diff().diff()


def f03_tpcl_192_double_top_breakout_failure_rate_504d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Empirical failure rate of double-top breakdowns at this stock: of all
    double-top breakdown events in last 504d, fraction that REVERSED back above
    the trough level within 21d."""
    rh63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    trough = high.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS)
    breakdown = (close < trough) & (close.shift(1) >= trough.shift(1))
    # reversal within 21d: close returns above trough in next 21 bars
    rev = (close > trough.shift(MDAYS)) & breakdown.shift(MDAYS).fillna(False)
    bd_count = breakdown.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    rev_count = rev.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return (_safe_div(rev_count, bd_count)).diff().diff().diff()


def f03_tpcl_193_pattern_volume_profile_bulkowski_match_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bulkowski-style: tops typically show DECLINING volume across the pattern.
    Indicator: correlation of volume series with a linearly-declining template
    over last 63d, weighted by how often close is near rolling max in window."""
    n = QDAYS
    template = np.linspace(1.0, -1.0, n)
    template = (template - template.mean()) / template.std()
    vols = volume.values

    def _corr(w):
        if np.isnan(w).any() or w.std() == 0:
            return np.nan
        wn = (w - w.mean()) / w.std()
        return float(np.dot(wn, template) / n)

    base = volume.rolling(n, min_periods=n).apply(_corr, raw=True)
    near_top = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.97).astype(float)
    return (base * near_top.rolling(n, min_periods=MDAYS).mean()).diff().diff().diff()


def f03_tpcl_194_throwback_frequency_post_breakdown_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Throwback = price retraces back to broken support after breakdown.
    Frequency: count of throwbacks per 504d. A throwback event = breakdown
    below 63d-low, then within 21d close returns within 2% of that support."""
    supp = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    breakdown = close < supp
    # for each breakdown bar, check if next 21d close came within 2% of supp
    bd_idx = breakdown.astype(int)
    # shifted return-near-support within next 21 bars
    near_support_future = (
        ((close - supp).abs() / supp.replace(0, np.nan) < 0.02).rolling(MDAYS).max()
    )
    throwback = bd_idx.shift(MDAYS).fillna(0).astype(bool) & near_support_future.fillna(0).astype(bool)
    return (throwback.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff().diff()


def f03_tpcl_195_failure_rate_weighted_pattern_probability_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: count pattern-completion events in 252d, weighted by 1-failure
    rate (from history). Returns expected-success-weighted pattern count."""
    # pattern completions: count bars where price made 252d high in past 63d AND
    # currently broke below 63d low
    made_high = (high.shift(QDAYS) >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(QDAYS) * 0.99)
    broke_low = close < low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    pat_event = made_high & broke_low
    pat_count_252 = pat_event.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    # historical failure rate: of past pat events in 504d, % where close > 63d low within 21d
    failure_event = pat_event.shift(MDAYS).fillna(False) & (
        close > low.rolling(QDAYS, min_periods=MDAYS).min().shift(MDAYS + 1)
    )
    fail_rate = _safe_div(
        failure_event.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
        pat_event.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
    ).fillna(0.5)
    return (pat_count_252 * (1.0 - fail_rate)).diff().diff().diff()


def f03_tpcl_196_multi_pattern_bulkowski_weighted_score_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multi-pattern Bulkowski-weighted bearish-probability score. Each detected
    pattern contributes its empirical break-even reliability weight (literature
    values: H&S 0.93, double-top 0.83, triple-top 0.79, descending-tri 0.62,
    rising-wedge 0.81). Sum of weights of detected patterns in last 21d."""
    # rough detection proxies on past data only
    head_high = high.shift(MDAYS) >= high.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS) * 0.99
    hs_score = head_high.astype(float) * 0.93
    # double top: two highs within 1% in last 63d
    rh = high.rolling(QDAYS, min_periods=MDAYS).max()
    dt_score = ((high >= rh * 0.99) & (high.shift(MDAYS) >= rh.shift(MDAYS) * 0.99)).astype(float) * 0.83
    # triple top: 3 pivots near max within 63d (proxy via pivot count)
    p3h = _pivot3_high_mask(high)
    tt_score = (p3h.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(float) * 0.79
    # descending triangle: high slope <0, low slope ~0
    sh = _rolling_slope(high, QDAYS)
    sl = _rolling_slope(low, QDAYS)
    dt_tri_score = ((sh < 0) & (sl.abs() < sh.abs() * 0.25)).astype(float) * 0.62
    # rising wedge: both slopes > 0, high < low
    rw_score = ((sh > 0) & (sl > 0) & (sl > sh)).astype(float) * 0.81
    total = hs_score + dt_score + tt_score + dt_tri_score + rw_score
    return (total.rolling(MDAYS, min_periods=WDAYS).max()).diff().diff().diff()


def f03_tpcl_197_pattern_duration_vs_bulkowski_median_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Pattern formation duration vs Bulkowski median (H&S ~ 62 days). Ratio of
    bars from first pivot in current pattern cluster to current bar, divided
    by 62.  >1 = longer than typical; <1 = shorter."""
    p3h = _pivot3_high_mask(high)
    # bars since first pivot in last 252d
    first_pivot_age = np.full(len(high), np.nan)
    pv = p3h.values
    for i in range(YDAYS, len(high)):
        lo = i - YDAYS + 1
        seg = pv[lo:i + 1]
        idxs = np.where(seg == 1.0)[0]
        if len(idxs) == 0:
            continue
        first_pivot_age[i] = float(len(seg) - 1 - idxs[0])
    return (pd.Series(first_pivot_age, index=high.index) / 62.0).diff().diff().diff()


def f03_tpcl_198_roof_pattern_schabacker_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Schabacker 'Roof': sharp peak with two SLOPING shoulders. Detect via
    pivot_max in last 63d with two pivots flanking (within +/-21 bars) lower
    than peak AND descending slopes on both sides (left rises, right falls)."""
    h = high.values
    out = np.full(len(high), np.nan)
    for i in range(QDAYS, len(high)):
        lo = i - QDAYS + 1
        seg = h[lo:i + 1]
        if np.isnan(seg).any():
            continue
        pk = int(np.argmax(seg))
        if pk < MDAYS or pk > len(seg) - MDAYS - 1:
            out[i] = 0.0
            continue
        left = seg[pk - MDAYS:pk]
        right = seg[pk + 1:pk + 1 + MDAYS]
        # left slope > 0, right slope < 0, peak strictly > both
        x_l = np.arange(len(left))
        x_r = np.arange(len(right))
        sl_l = np.polyfit(x_l, left, 1)[0] if left.std() > 0 else 0.0
        sl_r = np.polyfit(x_r, right, 1)[0] if right.std() > 0 else 0.0
        cond = sl_l > 0 and sl_r < 0 and seg[pk] > left.max() and seg[pk] > right.max()
        out[i] = 1.0 if cond else 0.0
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_199_dragon_top_pattern_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """'Dragon' top: two adjacent peaks at slightly DIFFERENT heights with sharp
    pullback between, the second peak forming the 'spine' and falling away —
    detect via two pivots within 21 bars where second is 5-10% higher and the
    trough between is at least 3% below both."""
    h = high.values
    out = np.full(len(high), np.nan)
    for i in range(QDAYS, len(high)):
        lo = i - QDAYS + 1
        seg = h[lo:i + 1]
        if np.isnan(seg).any():
            continue
        # find top 2 peaks in window via argpartition
        if len(seg) < 10:
            out[i] = 0.0
            continue
        # crude: find pivot-3 highs in seg
        cand = []
        for k in range(3, len(seg) - 3):
            s = seg[k - 3:k + 4]
            if seg[k] == s.max() and seg[k] > s[0] and seg[k] > s[-1]:
                cand.append((k, seg[k]))
        if len(cand) < 2:
            out[i] = 0.0
            continue
        # pick top 2 by value
        cand.sort(key=lambda x: -x[1])
        p1, p2 = cand[0], cand[1]
        if abs(p1[0] - p2[0]) > MDAYS:
            out[i] = 0.0
            continue
        higher = max(p1[1], p2[1])
        lower = min(p1[1], p2[1])
        if not (1.05 < higher / lower < 1.10):
            out[i] = 0.0
            continue
        a, b = sorted([p1[0], p2[0]])
        trough = seg[a:b + 1].min()
        if trough < lower * 0.97:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_200_high_pole_reversal_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """High-Pole reversal (P&F variant): a tall X-column (>=8 boxes) immediately
    followed by an O-column that retraces >=50% of the X-column. Returns 1
    if such event ends within last 21d."""
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    out = np.full(len(close), np.nan)
    c = close.values
    cv = col.values
    bv = (atr * 0.5).clip(lower=1e-9).values
    for i in range(YDAYS, len(close)):
        lo = i - YDAYS + 1
        seg = cv[lo:i + 1]
        seg_c = c[lo:i + 1]
        if np.isnan(seg).any() or np.isnan(bv[i]):
            continue
        last = -1
        starts = []
        for k, x in enumerate(seg):
            if x != last:
                starts.append(k)
                last = int(x)
        if len(starts) < 2:
            out[i] = 0.0
            continue
        # last two columns: previous X, current O
        j = len(starts) - 1
        s_cur = starts[j]
        e_cur = len(seg) - 1
        s_prev = starts[j - 1]
        e_prev = starts[j] - 1
        prev_is_X = seg_c[e_prev] > seg_c[s_prev]
        cur_is_O = seg_c[e_cur] < seg_c[s_cur]
        if not (prev_is_X and cur_is_O):
            out[i] = 0.0
            continue
        x_boxes = (seg_c[e_prev] - seg_c[s_prev]) / max(bv[i], 1e-9)
        o_retr = (seg_c[s_cur] - seg_c[e_cur]) / max(seg_c[e_prev] - seg_c[s_prev], 1e-9)
        recent = (len(seg) - 1 - s_cur) < MDAYS
        out[i] = 1.0 if (x_boxes >= 8 and o_retr >= 0.5 and recent) else 0.0
    return (pd.Series(out, index=close.index)).diff().diff().diff()


def f03_tpcl_201_quasimodo_top_pattern_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Quasimodo top (Q-pattern): inverse-asymmetric H&S — left shoulder LOW,
    head HIGH, right shoulder HIGHER than left shoulder but lower than head.
    Detect via 3 pivot-3 highs in last 63d with right-shoulder > left-shoulder."""
    h = high.values
    out = np.full(len(high), np.nan)
    for i in range(QDAYS, len(high)):
        lo = i - QDAYS + 1
        seg = h[lo:i + 1]
        if np.isnan(seg).any():
            continue
        cand = []
        for k in range(3, len(seg) - 3):
            s = seg[k - 3:k + 4]
            if seg[k] == s.max() and seg[k] > s[0] and seg[k] > s[-1]:
                cand.append((k, seg[k]))
        if len(cand) < 3:
            out[i] = 0.0
            continue
        last3 = cand[-3:]
        ls, hd, rs = last3
        if not (hd[1] > ls[1] and hd[1] > rs[1]):
            out[i] = 0.0
            continue
        out[i] = 1.0 if (rs[1] > ls[1]) else 0.0
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_202_five_day_reversal_pattern_63d_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Five-day reversal: 4 consecutive higher closes, then a 5th bar with
    higher high but close < open AND below close.shift(1). Count over 63d."""
    rising = (close > close.shift(1)) & (close.shift(1) > close.shift(2)) & (
        close.shift(2) > close.shift(3)
    ) & (close.shift(3) > close.shift(4))
    reversal_day = (high > high.shift(1)) & (close < open_) & (close < close.shift(1))
    event = rising.shift(1).fillna(False) & reversal_day
    return (event.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f03_tpcl_203_bowtie_ma_reversal_252d_d3(close: pd.Series) -> pd.Series:
    """Bowtie pattern (Don Pendergast): SMA10, SMA20, SMA30 fan out then converge
    and cross — bearish at top. Indicator: 1 when, after a regime of SMA10>SMA20>SMA30
    lasting >=21 bars, the order flips to SMA10<SMA20<SMA30 within next 21d."""
    s10 = close.rolling(10, min_periods=5).mean()
    s20 = close.rolling(20, min_periods=10).mean()
    s30 = close.rolling(30, min_periods=15).mean()
    up_order = (s10 > s20) & (s20 > s30)
    down_order = (s10 < s20) & (s20 < s30)
    sustained_up = up_order.rolling(MDAYS, min_periods=WDAYS).sum() >= MDAYS - 2
    cross = down_order & sustained_up.shift(MDAYS).fillna(False)
    return (cross.astype(float)).diff().diff().diff()


def f03_tpcl_204_boomerang_pattern_v_retrace_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Boomerang: a sharp V-down move followed by a retracement that overshoots
    the prior high. Inverted at top: sharp upmove then collapse below origin.
    Indicator: in last 42d, was close[t-42]<close[t-21]>close[t] AND
    close[t] < close[t-42]. Returns 1 if pattern present."""
    cond = (
        (close.shift(21) > close.shift(42))
        & (close.shift(21) > close)
        & (close < close.shift(42))
    )
    return (cond.astype(float)).diff().diff().diff()


def f03_tpcl_205_last_kiss_retest_then_breakdown_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """'Last-Kiss' pattern: after a breakdown below a 63d support level, price
    retraces to KISS the broken support from below, then resumes drop.
    Indicator: 1 if all three conditions met within last 21d:
       (a) close was below 63d-support sometime in last 21d,
       (b) close came within 2% of that support,
       (c) close then fell back below by >=1 ATR."""
    supp = low.rolling(QDAYS, min_periods=MDAYS).min().shift(MDAYS)
    atr = _atr(high, low, close, n=21)
    was_below = (close.shift(MDAYS) < supp.shift(MDAYS)).astype(float)
    kissed = ((close.shift(WDAYS) - supp.shift(WDAYS)).abs() / supp.shift(WDAYS).replace(0, np.nan) < 0.02).astype(float)
    fell_back = (close < supp - atr).astype(float)
    return (((was_below + kissed + fell_back) >= 3).astype(float)).diff().diff().diff()


def f03_tpcl_206_pattern_detection_breadth_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of DISTINCT pattern types firing within last 21d. Each pattern
    contributes at most 1. Uses simple proxy detectors."""
    rh63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    # H&S proxy
    p3h = _pivot3_high_mask(high)
    hs = (p3h.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(int)
    # double top
    dt = ((high >= rh63 * 0.99) & (high.shift(MDAYS) >= rh63.shift(MDAYS) * 0.99)).astype(int)
    # desc triangle
    sh = _rolling_slope(high, QDAYS)
    sl = _rolling_slope(low, QDAYS)
    desc = ((sh < 0) & (sl.abs() < sh.abs() * 0.5)).astype(int)
    # rising wedge
    rw = ((sh > 0) & (sl > 0) & (sl > sh)).astype(int)
    # broadening
    br = ((sh > 0) & (sl < 0)).astype(int)
    fired = (
        hs.rolling(MDAYS, min_periods=WDAYS).max()
        + dt.rolling(MDAYS, min_periods=WDAYS).max()
        + desc.rolling(MDAYS, min_periods=WDAYS).max()
        + rw.rolling(MDAYS, min_periods=WDAYS).max()
        + br.rolling(MDAYS, min_periods=WDAYS).max()
    )
    return (fired.astype(float)).diff().diff().diff()


def f03_tpcl_207_pattern_detection_density_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Pattern density over 252d: per-bar count of pivot-3 highs / 252."""
    p3h = _pivot3_high_mask(high)
    return (p3h.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS).diff().diff().diff()


def f03_tpcl_208_multi_pattern_simultaneous_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3+ pattern types fire on the same bar (within +/-3 bars), else 0."""
    p3h = _pivot3_high_mask(high)
    rh63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    hs = (p3h.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(int)
    dt = ((high >= rh63 * 0.99) & (high.shift(MDAYS) >= rh63.shift(MDAYS) * 0.99)).astype(int)
    sh = _rolling_slope(high, QDAYS)
    sl = _rolling_slope(low, QDAYS)
    desc = ((sh < 0) & (sl.abs() < sh.abs() * 0.5)).astype(int)
    rw = ((sh > 0) & (sl > 0) & (sl > sh)).astype(int)
    br = ((sh > 0) & (sl < 0)).astype(int)
    total = hs + dt + desc + rw + br
    # treat fire if any of last 3 bars
    fired_count = total.rolling(7, min_periods=3, center=False).max()
    return ((fired_count >= 3).astype(float)).diff().diff().diff()


def f03_tpcl_209_pattern_quality_consensus_score_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Average quality score across patterns. Quality of each pattern: R² of a
    polynomial fit to last 63d high — single number consensus."""
    h = high.values
    out = np.full(len(high), np.nan)
    for i in range(QDAYS, len(high)):
        lo = i - QDAYS + 1
        seg = h[lo:i + 1]
        if np.isnan(seg).any():
            continue
        x = np.arange(len(seg), dtype=float)
        # fit quadratic
        coef = np.polyfit(x, seg, 2)
        yhat = np.polyval(coef, x)
        ss_res = ((seg - yhat) ** 2).sum()
        ss_tot = ((seg - seg.mean()) ** 2).sum()
        r2_q = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
        # fit linear
        coef1 = np.polyfit(x, seg, 1)
        yhat1 = np.polyval(coef1, x)
        ss_res1 = ((seg - yhat1) ** 2).sum()
        r2_l = 1 - ss_res1 / ss_tot if ss_tot > 0 else 0.0
        out[i] = (r2_q + r2_l) / 2.0
    return (pd.Series(out, index=high.index)).diff().diff().diff()


def f03_tpcl_210_pattern_coincidence_with_new_252d_high_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 1 if any pattern fires within +/-5 bars of a new 252d high
    (last 21d). Higher = pattern emerging right at the high."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high >= rh).astype(float)
    p3h = _pivot3_high_mask(high)
    pat = (p3h.rolling(7, min_periods=3).sum() >= 1).astype(float)
    return (((new_high.rolling(MDAYS, min_periods=WDAYS).max() > 0) &
            (pat.rolling(MDAYS, min_periods=WDAYS).max() > 0)).astype(float)).diff().diff().diff()


def f03_tpcl_211_pattern_in_low_vol_regime_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Detects whether the prevailing pattern fires in a LOW-volatility regime
    (realized vol below 30th pct of 252d): tops in quiet markets are typically
    more reliable. Returns 1 if pattern fired in last 21d AND vol is in low
    tercile."""
    ret = close.pct_change()
    rv21 = ret.rolling(MDAYS, min_periods=WDAYS).std()
    rv_rank = rv21.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    p3h = _pivot3_high_mask(high)
    pat = (p3h.rolling(MDAYS, min_periods=WDAYS).sum() >= 1).astype(float)
    return (((rv_rank < 0.30) & (pat > 0)).astype(float)).diff().diff().diff()


def f03_tpcl_212_pattern_completion_probability_composite_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite completion probability: weighted sum of (pattern_density)
    + (proximity to 252d max) + (recent slope reversal sign).  Returns
    0..3 range."""
    p3h = _pivot3_high_mask(high)
    density = (p3h.rolling(QDAYS, min_periods=MDAYS).sum() / QDAYS).clip(0, 1)
    prox = (close / close.rolling(YDAYS, min_periods=QDAYS).max()).clip(0, 1)
    sl_short = _rolling_slope(close, MDAYS)
    sl_long = _rolling_slope(close, QDAYS)
    rev_sign = ((sl_short < 0) & (sl_long > 0)).astype(float)
    return (density + prox + rev_sign).diff().diff().diff()


def f03_tpcl_213_pattern_persistence_index_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern persistence: longest streak (in bars within 252d) of consecutive
    bars where the same pattern continued to fire (proxy: pivot-3 highs within
    a rolling 21d window kept count >= 2)."""
    p3h = _pivot3_high_mask(high)
    active = (p3h.rolling(MDAYS, min_periods=WDAYS).sum() >= 2).astype(int)
    grp = (active != active.shift(1)).cumsum()
    streak = active.groupby(grp).cumsum() * active
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff().diff().diff()


def _ncc_template(close: pd.Series, window: int, template: np.ndarray) -> pd.Series:
    """Normalized cross-correlation of close (rolling window) with template.
    Template length must equal window. Returns Series of NCC values."""
    t = template - template.mean()
    t_norm = np.sqrt((t ** 2).sum())
    if t_norm == 0:
        return pd.Series(np.nan, index=close.index)

    def _ncc(w):
        if np.isnan(w).any():
            return np.nan
        w0 = w - w.mean()
        wn = np.sqrt((w0 ** 2).sum())
        if wn == 0:
            return 0.0
        return float(np.dot(w0, t) / (wn * t_norm))

    return close.rolling(window, min_periods=window).apply(_ncc, raw=True)


def f03_tpcl_214_ncc_with_hs_template_63d_d3(close: pd.Series) -> pd.Series:
    """NCC of last 63d close with idealized H&S template (left-shoulder peak at
    1/6, head peak at 1/2, right-shoulder peak at 5/6, neckline = baseline 0)."""
    n = QDAYS
    x = np.arange(n)
    t = np.zeros(n)
    # left shoulder bell centered at n/6
    sigma = n / 14.0
    t += 0.6 * np.exp(-((x - n / 6.0) ** 2) / (2 * sigma ** 2))
    # head bell at n/2
    t += 1.0 * np.exp(-((x - n / 2.0) ** 2) / (2 * sigma ** 2))
    # right shoulder bell at 5n/6
    t += 0.6 * np.exp(-((x - 5 * n / 6.0) ** 2) / (2 * sigma ** 2))
    return (_ncc_template(close, n, t)).diff().diff().diff()


def f03_tpcl_215_ncc_with_double_top_template_42d_d3(close: pd.Series) -> pd.Series:
    """NCC of last 42d close with idealized double-top template (two peaks at
    1/4 and 3/4)."""
    n = 42
    x = np.arange(n)
    sigma = n / 12.0
    t = np.exp(-((x - n / 4.0) ** 2) / (2 * sigma ** 2)) + np.exp(
        -((x - 3 * n / 4.0) ** 2) / (2 * sigma ** 2)
    )
    return (_ncc_template(close, n, t)).diff().diff().diff()


def f03_tpcl_216_ncc_with_rounding_top_template_126d_d3(close: pd.Series) -> pd.Series:
    """NCC of last 126d close with concave-down quadratic template."""
    n = 126
    x = np.arange(n, dtype=float)
    t = -(x - (n - 1) / 2.0) ** 2  # inverted parabola
    return (_ncc_template(close, n, t)).diff().diff().diff()


def f03_tpcl_217_multi_template_best_fit_label_63d_d3(close: pd.Series) -> pd.Series:
    """Multi-template best-fit label: out of {H&S=3, double-top=2, rounding=1,
    none=0}, returns the integer label corresponding to the highest NCC over
    last 63d (must exceed 0.5 to qualify)."""
    n = QDAYS
    x = np.arange(n)
    sigma = n / 14.0
    hs = (
        0.6 * np.exp(-((x - n / 6.0) ** 2) / (2 * sigma ** 2))
        + 1.0 * np.exp(-((x - n / 2.0) ** 2) / (2 * sigma ** 2))
        + 0.6 * np.exp(-((x - 5 * n / 6.0) ** 2) / (2 * sigma ** 2))
    )
    dt = np.exp(-((x - n / 4.0) ** 2) / (2 * sigma ** 2)) + np.exp(
        -((x - 3 * n / 4.0) ** 2) / (2 * sigma ** 2)
    )
    rd = -(x - (n - 1) / 2.0) ** 2
    ncc_hs = _ncc_template(close, n, hs)
    ncc_dt = _ncc_template(close, n, dt)
    ncc_rd = _ncc_template(close, n, rd)
    df = pd.concat([ncc_rd.rename(1), ncc_dt.rename(2), ncc_hs.rename(3)], axis=1)
    best = df.fillna(-np.inf).idxmax(axis=1)
    best_val = df.max(axis=1)
    out = best.where(best_val > 0.5, 0).astype(float)
    return (out).diff().diff().diff()


def f03_tpcl_218_template_distance_distribution_kurtosis_252d_d3(close: pd.Series) -> pd.Series:
    """Distribution moments of the H&S-template NCC over 252d: returns its
    excess kurtosis. Highly leptokurtic distribution = a few strong matches
    standing out from noise."""
    n = QDAYS
    x = np.arange(n)
    sigma = n / 14.0
    hs = (
        0.6 * np.exp(-((x - n / 6.0) ** 2) / (2 * sigma ** 2))
        + 1.0 * np.exp(-((x - n / 2.0) ** 2) / (2 * sigma ** 2))
        + 0.6 * np.exp(-((x - 5 * n / 6.0) ** 2) / (2 * sigma ** 2))
    )
    ncc = _ncc_template(close, n, hs)

    def _exc_kurt(w):
        if np.isnan(w).any() or w.std() == 0:
            return np.nan
        m = w.mean()
        s = w.std()
        z = (w - m) / s
        return float((z ** 4).mean() - 3.0)

    return (ncc.rolling(YDAYS, min_periods=QDAYS).apply(_exc_kurt, raw=True)).diff().diff().diff()


def f03_tpcl_219_hidden_bearish_divergence_at_pattern_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Hidden bearish divergence: at pattern completion (proxy: pivot-3 high
    within last 21d), price makes a LOWER high vs prior 63d max, BUT RSI(14)
    makes a HIGHER high vs its prior 63d max. Returns 1 if found."""
    rsi = _rsi(close, n=14)
    p3h = _pivot3_high_mask(high)
    pat_recent = p3h.rolling(MDAYS, min_periods=WDAYS).max()
    price_lh = high < high.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS)
    rsi_hh = rsi > rsi.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS)
    return (((pat_recent > 0) & price_lh & rsi_hh).astype(float)).diff().diff().diff()


def f03_tpcl_220_failed_bearish_setup_reversal_count_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count within 252d of failed bearish setups: 9-bar Sell Setup completed
    BUT close 21 bars later is HIGHER than the setup-completion close (failure)."""
    flip = (close > close.shift(4)).astype(float)
    sell_complete = (flip.rolling(9, min_periods=9).sum() == 9).astype(int)
    cmp_close = close.where(sell_complete.astype(bool), np.nan).ffill(limit=MDAYS)
    failed = sell_complete.shift(MDAYS).fillna(0).astype(bool) & (close > cmp_close.shift(MDAYS))
    return (failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_221_pattern_completion_then_immediate_failure_event_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern-then-failure event: pattern completion (proxy: bar breaks below
    63d-low neckline) but within 5 bars close returns above the neckline.
    Count within 252d."""
    neckline = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    completion = (close < neckline) & (close.shift(1) >= neckline.shift(1))
    # within next 5 bars close returns above neckline
    above_next_5 = (close > neckline).rolling(WDAYS).max()
    failure = completion.shift(WDAYS).fillna(False) & (above_next_5 > 0)
    return (failure.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f03_tpcl_222_pre_pattern_compression_breakout_direction_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pre-pattern compression: was 21d range a 252d low BEFORE the pattern?
    Then breakout direction (close vs prior 21d midpoint). Returns -1 (down,
    strong bearish signal), +1 (up), 0 (no compression)."""
    rng21 = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    rng_rank = rng21.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    compressed = (rng_rank < 0.10).astype(float)
    mid21 = (high.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS) +
             low.rolling(MDAYS, min_periods=WDAYS).min().shift(WDAYS)) / 2.0
    direction = np.where(close > mid21, 1.0, np.where(close < mid21, -1.0, 0.0))
    return (pd.Series(direction, index=close.index) * compressed).diff().diff().diff()


def f03_tpcl_223_td_plus_bulkowski_joint_score_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Joint score: TD Setup completions (normalized) + Bulkowski-style
    weighted pattern score (normalized).  Both >0 = double confirmation."""
    flip = (close > close.shift(4)).astype(float)
    completed = (flip.rolling(9, min_periods=9).sum() == 9).astype(float)
    td_count_252 = completed.rolling(YDAYS, min_periods=QDAYS).sum()
    td_norm = td_count_252 / 5.0  # 5 completions = strong
    # Bulkowski proxy
    head_high = high.shift(MDAYS) >= high.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS) * 0.99
    hs = head_high.astype(float) * 0.93
    rh = high.rolling(QDAYS, min_periods=MDAYS).max()
    dt = ((high >= rh * 0.99) & (high.shift(MDAYS) >= rh.shift(MDAYS) * 0.99)).astype(float) * 0.83
    bulk = (hs + dt).rolling(MDAYS, min_periods=WDAYS).max() / 1.76
    return (td_norm + bulk).diff().diff().diff()


def f03_tpcl_224_multi_pattern_weighted_bearish_probability_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted bearish-probability composite. Each detector returns 0/1, mapped
    to literature breakdown probabilities, summed and normalized. Output 0..1."""
    p3h = _pivot3_high_mask(high)
    head_high = high.shift(MDAYS) >= high.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS) * 0.99
    rh = high.rolling(QDAYS, min_periods=MDAYS).max()
    sh = _rolling_slope(high, QDAYS)
    sl = _rolling_slope(low, QDAYS)
    # pattern proxies
    hs_p = head_high.astype(float) * 0.85
    dt_p = ((high >= rh * 0.99) & (high.shift(MDAYS) >= rh.shift(MDAYS) * 0.99)).astype(float) * 0.75
    tt_p = (p3h.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(float) * 0.70
    rw_p = ((sh > 0) & (sl > 0) & (sl > sh)).astype(float) * 0.65
    dtri_p = ((sh < 0) & (sl.abs() < sh.abs() * 0.3)).astype(float) * 0.55
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(1))
    prior_21_high = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    ut_p = (new_high & (close < prior_21_high)).astype(float) * 0.80
    total = hs_p + dt_p + tt_p + rw_p + dtri_p + ut_p
    return ((total / 4.30).clip(0.0, 1.0)).diff().diff().diff()


def f03_tpcl_225_terminal_classical_pattern_aggregate_confidence_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal-pattern aggregate confidence:
       NCC-template-best-fit normalized + Wyckoff polarity normalized +
       PnF-distribution-column-count normalized + Bulkowski-pattern-detect score.
    Output ~0..4 range."""
    # NCC best fit
    n = QDAYS
    x = np.arange(n)
    sigma = n / 14.0
    hs_t = (
        0.6 * np.exp(-((x - n / 6.0) ** 2) / (2 * sigma ** 2))
        + 1.0 * np.exp(-((x - n / 2.0) ** 2) / (2 * sigma ** 2))
        + 0.6 * np.exp(-((x - 5 * n / 6.0) ** 2) / (2 * sigma ** 2))
    )
    dt_t = np.exp(-((x - n / 4.0) ** 2) / (2 * sigma ** 2)) + np.exp(
        -((x - 3 * n / 4.0) ** 2) / (2 * sigma ** 2)
    )
    ncc_hs = _ncc_template(close, n, hs_t)
    ncc_dt = _ncc_template(close, n, dt_t)
    ncc_best = pd.concat([ncc_hs, ncc_dt], axis=1).max(axis=1).clip(0, 1)
    # Wyckoff polarity (UT vs spring) — normalized
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    prior_21_high = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    ut = (new_high & (close < prior_21_high)).astype(float)
    new_low = low <= low.rolling(YDAYS, min_periods=QDAYS).min().shift(1)
    prior_21_low = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    spring = (new_low & (close > prior_21_low)).astype(float)
    polarity = (ut - spring).rolling(QDAYS, min_periods=MDAYS).sum()
    polarity_norm = (polarity / 5.0).clip(-1, 1).clip(lower=0)
    # P&F distribution column count proxy
    atr = _atr(high, low, close, n=21)
    col = _pnf_columns(close, atr)
    chg = (col != col.shift(1)).astype(float)
    cols_252 = chg.rolling(YDAYS, min_periods=QDAYS).sum()
    pnf_norm = (cols_252 / 30.0).clip(0, 1)
    # Bulkowski-weighted score normalized
    head_high = high.shift(MDAYS) >= high.rolling(QDAYS, min_periods=MDAYS).max().shift(MDAYS) * 0.99
    hs_b = head_high.astype(float) * 0.93
    rh = high.rolling(QDAYS, min_periods=MDAYS).max()
    dt_b = ((high >= rh * 0.99) & (high.shift(MDAYS) >= rh.shift(MDAYS) * 0.99)).astype(float) * 0.83
    bulk_norm = ((hs_b + dt_b).rolling(MDAYS, min_periods=WDAYS).max() / 1.76).clip(0, 1)
    return (ncc_best.fillna(0) + polarity_norm.fillna(0) + pnf_norm.fillna(0) + bulk_norm.fillna(0)).diff().diff().diff()


TOPPING_PATTERN_CLASSICAL_D3_REGISTRY_151_225 = {
    "f03_tpcl_151_td_setup_completion_count_252d_d3": {"inputs": ["close"], "func": f03_tpcl_151_td_setup_completion_count_252d_d3},
    "f03_tpcl_152_td_combo_completion_count_252d_d3": {"inputs": ["close", "low", "high"], "func": f03_tpcl_152_td_combo_completion_count_252d_d3},
    "f03_tpcl_153_td_sequential_exhaustion_bar_count_252d_d3": {"inputs": ["close"], "func": f03_tpcl_153_td_sequential_exhaustion_bar_count_252d_d3},
    "f03_tpcl_154_td_pressure_at_top_63d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_154_td_pressure_at_top_63d_d3},
    "f03_tpcl_155_td_range_projection_breach_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_155_td_range_projection_breach_252d_d3},
    "f03_tpcl_156_td_differential_at_peak_63d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_156_td_differential_at_peak_63d_d3},
    "f03_tpcl_157_td_reverse_setup_qualifier_252d_d3": {"inputs": ["close"], "func": f03_tpcl_157_td_reverse_setup_qualifier_252d_d3},
    "f03_tpcl_158_td_camouflage_event_count_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f03_tpcl_158_td_camouflage_event_count_63d_d3},
    "f03_tpcl_159_td_open_downcross_in_setup_252d_d3": {"inputs": ["open", "close"], "func": f03_tpcl_159_td_open_downcross_in_setup_252d_d3},
    "f03_tpcl_160_td_countdown_completion_event_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_160_td_countdown_completion_event_252d_d3},
    "f03_tpcl_161_pnf_consecutive_x_columns_count_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_161_pnf_consecutive_x_columns_count_252d_d3},
    "f03_tpcl_162_pnf_triple_top_then_fail_event_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_162_pnf_triple_top_then_fail_event_252d_d3},
    "f03_tpcl_163_pnf_descending_tops_x_column_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_163_pnf_descending_tops_x_column_252d_d3},
    "f03_tpcl_164_pnf_bull_trap_signal_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_164_pnf_bull_trap_signal_252d_d3},
    "f03_tpcl_165_pnf_box_count_target_projection_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_165_pnf_box_count_target_projection_252d_d3},
    "f03_tpcl_166_pnf_distribution_top_column_count_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_166_pnf_distribution_top_column_count_252d_d3},
    "f03_tpcl_167_pnf_box_reversal_frequency_at_top_63d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_167_pnf_box_reversal_frequency_at_top_63d_d3},
    "f03_tpcl_168_pnf_column_high_low_symmetry_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_168_pnf_column_high_low_symmetry_252d_d3},
    "f03_tpcl_169_andrews_median_line_distance_at_top_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_169_andrews_median_line_distance_at_top_252d_d3},
    "f03_tpcl_170_andrews_upper_channel_touch_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_170_andrews_upper_channel_touch_count_252d_d3},
    "f03_tpcl_171_andrews_lower_channel_break_event_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_171_andrews_lower_channel_break_event_252d_d3},
    "f03_tpcl_172_gann_1x1_distance_at_top_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_172_gann_1x1_distance_at_top_252d_d3},
    "f03_tpcl_173_gann_2x1_breakdown_event_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_173_gann_2x1_breakdown_event_252d_d3},
    "f03_tpcl_174_gann_1x2_pierce_event_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_174_gann_1x2_pierce_event_252d_d3},
    "f03_tpcl_175_gann_square_of_9_cardinal_cross_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_175_gann_square_of_9_cardinal_cross_252d_d3},
    "f03_tpcl_176_gann_fan_resistance_hits_at_top_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_176_gann_fan_resistance_hits_at_top_252d_d3},
    "f03_tpcl_177_elliott_5_wave_advance_proxy_252d_d3": {"inputs": ["close"], "func": f03_tpcl_177_elliott_5_wave_advance_proxy_252d_d3},
    "f03_tpcl_178_elliott_wave5_truncation_indicator_252d_d3": {"inputs": ["close"], "func": f03_tpcl_178_elliott_wave5_truncation_indicator_252d_d3},
    "f03_tpcl_179_elliott_wave5_extension_excess_252d_d3": {"inputs": ["close"], "func": f03_tpcl_179_elliott_wave5_extension_excess_252d_d3},
    "f03_tpcl_180_elliott_abc_correction_start_event_63d_d3": {"inputs": ["close"], "func": f03_tpcl_180_elliott_abc_correction_start_event_63d_d3},
    "f03_tpcl_181_elliott_diagonal_triangle_ending_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_181_elliott_diagonal_triangle_ending_252d_d3},
    "f03_tpcl_182_elliott_five_three_density_252d_d3": {"inputs": ["close"], "func": f03_tpcl_182_elliott_five_three_density_252d_d3},
    "f03_tpcl_183_wyckoff_selling_climax_intensity_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_183_wyckoff_selling_climax_intensity_252d_d3},
    "f03_tpcl_184_wyckoff_automatic_reaction_depth_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_184_wyckoff_automatic_reaction_depth_252d_d3},
    "f03_tpcl_185_wyckoff_secondary_test_failure_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_185_wyckoff_secondary_test_failure_252d_d3},
    "f03_tpcl_186_wyckoff_trading_range_persistence_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_186_wyckoff_trading_range_persistence_252d_d3},
    "f03_tpcl_187_wyckoff_sign_of_weakness_angle_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_187_wyckoff_sign_of_weakness_angle_252d_d3},
    "f03_tpcl_188_wyckoff_last_point_of_supply_event_252d_d3": {"inputs": ["close", "high", "low", "volume"], "func": f03_tpcl_188_wyckoff_last_point_of_supply_event_252d_d3},
    "f03_tpcl_189_wyckoff_upthrust_intensity_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_189_wyckoff_upthrust_intensity_252d_d3},
    "f03_tpcl_190_wyckoff_spring_vs_upthrust_polarity_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_190_wyckoff_spring_vs_upthrust_polarity_252d_d3},
    "f03_tpcl_191_hs_breakdown_move_zscore_504d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_191_hs_breakdown_move_zscore_504d_d3},
    "f03_tpcl_192_double_top_breakout_failure_rate_504d_d3": {"inputs": ["high", "close"], "func": f03_tpcl_192_double_top_breakout_failure_rate_504d_d3},
    "f03_tpcl_193_pattern_volume_profile_bulkowski_match_252d_d3": {"inputs": ["close", "volume"], "func": f03_tpcl_193_pattern_volume_profile_bulkowski_match_252d_d3},
    "f03_tpcl_194_throwback_frequency_post_breakdown_504d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_194_throwback_frequency_post_breakdown_504d_d3},
    "f03_tpcl_195_failure_rate_weighted_pattern_probability_504d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_195_failure_rate_weighted_pattern_probability_504d_d3},
    "f03_tpcl_196_multi_pattern_bulkowski_weighted_score_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_196_multi_pattern_bulkowski_weighted_score_252d_d3},
    "f03_tpcl_197_pattern_duration_vs_bulkowski_median_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_197_pattern_duration_vs_bulkowski_median_252d_d3},
    "f03_tpcl_198_roof_pattern_schabacker_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_198_roof_pattern_schabacker_252d_d3},
    "f03_tpcl_199_dragon_top_pattern_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_199_dragon_top_pattern_252d_d3},
    "f03_tpcl_200_high_pole_reversal_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_200_high_pole_reversal_252d_d3},
    "f03_tpcl_201_quasimodo_top_pattern_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_201_quasimodo_top_pattern_252d_d3},
    "f03_tpcl_202_five_day_reversal_pattern_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f03_tpcl_202_five_day_reversal_pattern_63d_d3},
    "f03_tpcl_203_bowtie_ma_reversal_252d_d3": {"inputs": ["close"], "func": f03_tpcl_203_bowtie_ma_reversal_252d_d3},
    "f03_tpcl_204_boomerang_pattern_v_retrace_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_204_boomerang_pattern_v_retrace_252d_d3},
    "f03_tpcl_205_last_kiss_retest_then_breakdown_63d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_205_last_kiss_retest_then_breakdown_63d_d3},
    "f03_tpcl_206_pattern_detection_breadth_21d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_206_pattern_detection_breadth_21d_d3},
    "f03_tpcl_207_pattern_detection_density_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_207_pattern_detection_density_252d_d3},
    "f03_tpcl_208_multi_pattern_simultaneous_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_208_multi_pattern_simultaneous_252d_d3},
    "f03_tpcl_209_pattern_quality_consensus_score_252d_d3": {"inputs": ["high", "low"], "func": f03_tpcl_209_pattern_quality_consensus_score_252d_d3},
    "f03_tpcl_210_pattern_coincidence_with_new_252d_high_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_210_pattern_coincidence_with_new_252d_high_d3},
    "f03_tpcl_211_pattern_in_low_vol_regime_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_211_pattern_in_low_vol_regime_252d_d3},
    "f03_tpcl_212_pattern_completion_probability_composite_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_212_pattern_completion_probability_composite_252d_d3},
    "f03_tpcl_213_pattern_persistence_index_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_213_pattern_persistence_index_252d_d3},
    "f03_tpcl_214_ncc_with_hs_template_63d_d3": {"inputs": ["close"], "func": f03_tpcl_214_ncc_with_hs_template_63d_d3},
    "f03_tpcl_215_ncc_with_double_top_template_42d_d3": {"inputs": ["close"], "func": f03_tpcl_215_ncc_with_double_top_template_42d_d3},
    "f03_tpcl_216_ncc_with_rounding_top_template_126d_d3": {"inputs": ["close"], "func": f03_tpcl_216_ncc_with_rounding_top_template_126d_d3},
    "f03_tpcl_217_multi_template_best_fit_label_63d_d3": {"inputs": ["close"], "func": f03_tpcl_217_multi_template_best_fit_label_63d_d3},
    "f03_tpcl_218_template_distance_distribution_kurtosis_252d_d3": {"inputs": ["close"], "func": f03_tpcl_218_template_distance_distribution_kurtosis_252d_d3},
    "f03_tpcl_219_hidden_bearish_divergence_at_pattern_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_219_hidden_bearish_divergence_at_pattern_252d_d3},
    "f03_tpcl_220_failed_bearish_setup_reversal_count_252d_d3": {"inputs": ["close", "high"], "func": f03_tpcl_220_failed_bearish_setup_reversal_count_252d_d3},
    "f03_tpcl_221_pattern_completion_then_immediate_failure_event_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_221_pattern_completion_then_immediate_failure_event_252d_d3},
    "f03_tpcl_222_pre_pattern_compression_breakout_direction_252d_d3": {"inputs": ["high", "low", "close"], "func": f03_tpcl_222_pre_pattern_compression_breakout_direction_252d_d3},
    "f03_tpcl_223_td_plus_bulkowski_joint_score_252d_d3": {"inputs": ["close", "high", "low"], "func": f03_tpcl_223_td_plus_bulkowski_joint_score_252d_d3},
    "f03_tpcl_224_multi_pattern_weighted_bearish_probability_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_224_multi_pattern_weighted_bearish_probability_252d_d3},
    "f03_tpcl_225_terminal_classical_pattern_aggregate_confidence_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_225_terminal_classical_pattern_aggregate_confidence_252d_d3},
}
