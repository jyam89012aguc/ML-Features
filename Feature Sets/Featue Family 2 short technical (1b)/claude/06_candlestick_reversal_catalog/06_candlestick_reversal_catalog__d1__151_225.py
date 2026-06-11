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



def _near_252d_high_atr(high, low, close, k=1.0):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (rmax - high) <= (k * atr)


def _at_252d_high(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return high >= rmax


def _heikin_ashi(open_, high, low, close):
    ha_close = (open_ + high + low + close) / 4.0
    ha_open = (open_.shift(1) + close.shift(1)) / 2.0
    ha_open = ha_open.fillna((open_.iloc[0] + close.iloc[0]) / 2.0)
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return ha_open, ha_high, ha_low, ha_close



def f06_cscr_151_belt_hold_bearish_indicator(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    body = (open_ - close)
    red = close < open_
    open_at_high = (high - open_) / rng <= 0.05
    big_body = (body / rng) >= 0.7
    flag = (red & open_at_high & big_body).astype(float)
    return flag.where(rng.notna(), np.nan)


def f06_cscr_152_belt_hold_at_252d_high(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    body = (open_ - close)
    red = close < open_
    open_at_high = (high - open_) / rng <= 0.05
    big_body = (body / rng) >= 0.7
    near = _near_252d_high_atr(high, low, close, k=1.0)
    flag = (red & open_at_high & big_body & near).astype(float)
    return flag.where(near.notna(), np.nan)


def f06_cscr_153_bearish_counterattack_line(open_, high, low, close):
    prev_o = open_.shift(1); prev_c = close.shift(1); prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_up = open_ > prev_h
    tol = (close - prev_c).abs() / prev_c.replace(0, np.nan) <= 0.002
    today_red = close < open_
    flag = (prev_green & gap_up & tol & today_red).astype(float)
    return flag.where(prev_c.notna(), np.nan)


def f06_cscr_154_bearish_meeting_line_tolerance_score(open_, high, low, close):
    prev_o = open_.shift(1); prev_c = close.shift(1); prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_up = open_ > prev_h
    today_red = close < open_
    tightness = 1.0 - ((close - prev_c).abs() / prev_c.replace(0, np.nan)).clip(upper=0.05) / 0.05
    return tightness.where(prev_green & gap_up & today_red, np.nan)


def f06_cscr_155_stick_sandwich_bearish(open_, close):
    c2 = close.shift(2); o2 = open_.shift(2)
    c1 = close.shift(1); o1 = open_.shift(1)
    c0 = close;          o0 = open_
    red2 = c2 < o2
    green1 = c1 > o1
    red0 = c0 < o0
    eq_close = (c0 - c2).abs() / c2.abs().replace(0, np.nan) <= 0.003
    flag = (red2 & green1 & red0 & eq_close).astype(float)
    return flag.where(c2.notna(), np.nan)


def f06_cscr_156_identical_three_crows(open_, close):
    o0 = open_; c0 = close
    o1 = open_.shift(1); c1 = close.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2)
    red0 = c0 < o0; red1 = c1 < o1; red2 = c2 < o2
    open_near_prev_close_a = (o0 - c1).abs() / c1.abs().replace(0, np.nan) <= 0.005
    open_near_prev_close_b = (o1 - c2).abs() / c2.abs().replace(0, np.nan) <= 0.005
    b0 = (o0 - c0); b1 = (o1 - c1); b2 = (o2 - c2)
    bmean = (b0 + b1 + b2) / 3.0
    similar = ((b0 - bmean).abs() / bmean.replace(0, np.nan) <= 0.3) & \
              ((b1 - bmean).abs() / bmean.replace(0, np.nan) <= 0.3) & \
              ((b2 - bmean).abs() / bmean.replace(0, np.nan) <= 0.3)
    flag = (red0 & red1 & red2 & open_near_prev_close_a & open_near_prev_close_b & similar).astype(float)
    return flag.where(c2.notna(), np.nan)


def f06_cscr_157_advance_block_indicator(open_, high, low, close):
    o0 = open_; c0 = close; h0 = high
    o1 = open_.shift(1); c1 = close.shift(1); h1 = high.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2); h2 = high.shift(2)
    g0 = c0 > o0; g1 = c1 > o1; g2 = c2 > o2
    b0 = c0 - o0; b1 = c1 - o1; b2 = c2 - o2
    shrinking = (b0 < b1) & (b1 < b2)
    u0 = h0 - c0; u1 = h1 - c1; u2 = h2 - c2
    growing = (u0 > u1) & (u1 > u2)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (g0 & g1 & g2 & shrinking & growing & near).astype(float)
    return flag.where(c2.notna() & near.notna(), np.nan)


def f06_cscr_158_deliberation_pattern(open_, high, low, close):
    o0 = open_; c0 = close
    o1 = open_.shift(1); c1 = close.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2)
    rng0 = (high - low).replace(0, np.nan)
    g0 = c0 > o0; g1 = c1 > o1; g2 = c2 > o2
    b0 = (c0 - o0); b1 = (c1 - o1); b2 = (c2 - o2)
    big1 = b1 / rng0 >= 0.5
    big2 = b2 / rng0 >= 0.5
    small0 = (b0.abs() / rng0) <= 0.25
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (g0 & g1 & g2 & big1 & big2 & small0 & near).astype(float)
    return flag.where(near.notna() & rng0.notna(), np.nan)


def f06_cscr_159_tower_top_indicator(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    avg_body = body.rolling(MDAYS, min_periods=WDAYS).mean()
    tall = body > 1.5 * avg_body
    small_body = (body / rng) <= 0.3
    tall_green = tall & (close > open_)
    tall_red = tall & (close < open_)
    has_left_tower = pd.Series(False, index=close.index)
    has_intermediate_small = pd.Series(False, index=close.index)
    for k in range(2, 6):
        has_left_tower |= tall_green.shift(k).fillna(False)
    for k in range(1, 5):
        has_intermediate_small |= small_body.shift(k).fillna(False)
    flag = (tall_red & has_left_tower & has_intermediate_small).astype(float)
    return flag.where(avg_body.notna(), np.nan)


def f06_cscr_160_three_mountains_top(high):
    n = len(high)
    h = high.to_numpy(copy=True)
    out = np.zeros(n, dtype=float)
    pivots = []
    for i in range(WDAYS, n - WDAYS):
        if np.isnan(h[i]):
            continue
        window_l = h[max(0, i - WDAYS):i]
        window_r = h[i + 1:i + WDAYS + 1]
        if window_l.size == 0 or window_r.size == 0:
            continue
        if h[i] >= np.nanmax(window_l) and h[i] >= np.nanmax(window_r):
            pivots.append((i, h[i]))
    pivot_idx = np.array([p[0] for p in pivots], dtype=int)
    pivot_val = np.array([p[1] for p in pivots], dtype=float)
    for i in range(n):
        prior_mask = pivot_idx <= i
        if prior_mask.sum() < 3:
            continue
        recent_mask = prior_mask & (pivot_idx >= i - DDAYS_2Y)
        vals = pivot_val[recent_mask]
        if vals.size < 3:
            continue
        last3 = vals[-3:]
        mn = last3.mean()
        if mn <= 0:
            continue
        if np.all(np.abs(last3 - mn) / mn <= 0.03) and pivot_idx[recent_mask][-1] == i:
            out[i] = 1.0
    return pd.Series(out, index=high.index)


def f06_cscr_161_three_buddha_top(high):
    n = len(high)
    h = high.to_numpy(copy=True)
    out = np.zeros(n, dtype=float)
    pivots = []
    for i in range(WDAYS, n - WDAYS):
        if np.isnan(h[i]):
            continue
        window_l = h[max(0, i - WDAYS):i]
        window_r = h[i + 1:i + WDAYS + 1]
        if window_l.size == 0 or window_r.size == 0:
            continue
        if h[i] >= np.nanmax(window_l) and h[i] >= np.nanmax(window_r):
            pivots.append((i, h[i]))
    pivot_idx = np.array([p[0] for p in pivots], dtype=int)
    pivot_val = np.array([p[1] for p in pivots], dtype=float)
    for i in range(n):
        prior_mask = pivot_idx <= i
        if prior_mask.sum() < 3:
            continue
        recent_mask = prior_mask & (pivot_idx >= i - DDAYS_2Y)
        vals = pivot_val[recent_mask]
        if vals.size < 3:
            continue
        last3 = vals[-3:]
        if last3[1] > last3[0] and last3[1] > last3[2] and pivot_idx[recent_mask][-1] == i:
            out[i] = 1.0
    return pd.Series(out, index=high.index)


def f06_cscr_162_falling_window_confirmation(open_, high, low, close):
    prev_l = low.shift(1)
    gap_down = high < prev_l
    topping = (close < open_) & _near_252d_high_atr(high, low, close, k=2.0)
    confirm = pd.Series(False, index=close.index)
    for k in range(1, WDAYS + 1):
        confirm |= (gap_down.shift(-0).fillna(False) & topping.shift(k).fillna(False))
    return confirm.astype(float).where(prev_l.notna(), np.nan)


def f06_cscr_163_rising_window_failure(open_, high, low, close):
    prev_h = high.shift(1)
    gap_up_lvl = prev_h  # the window-low
    is_gap_up_today = low > prev_h
    near = _near_252d_high_atr(high, low, close, k=2.0)
    out = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        gap_active = is_gap_up_today.shift(k).fillna(False)
        lvl = gap_up_lvl.shift(k)
        near_k = near.shift(k).fillna(False)
        filled = (low < lvl) & gap_active & near_k
        out = out + filled.astype(float)
    return (out > 0).astype(float).where(prev_h.notna(), np.nan)


def f06_cscr_164_downward_tasuki_gap_failed(open_, high, low, close):
    prev_h = high.shift(1); prev_l = low.shift(1); prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_red = prev_c < prev_o
    gap_dn = prev_h < low.shift(2)  # gap-down on bar t-1
    today_green = close > open_
    inside_gap = (open_ < prev_c.shift(0)) & (close < low.shift(2))
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (prev_red & gap_dn & today_green & inside_gap & near).astype(float)
    return flag.where(prev_c.notna() & near.notna(), np.nan)


def f06_cscr_165_upward_tasuki_gap_failure(open_, high, low, close):
    prev_l = low.shift(1); prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    gap_up_yesterday = prev_l > close.shift(2)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    setup = prev_green & gap_up_yesterday & near
    filled = low <= close.shift(2)
    out = pd.Series(0.0, index=close.index)
    for k in range(0, 3):
        out = out + (setup.shift(k).fillna(False) & filled).astype(float)
    return (out > 0).astype(float).where(prev_c.notna(), np.nan)


def f06_cscr_166_side_by_side_white_after_gap_up_failed(open_, high, low, close):
    o0 = open_; c0 = close
    o1 = open_.shift(1); c1 = close.shift(1); h1 = high.shift(1); l1 = low.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2); h2 = high.shift(2); l2 = low.shift(2)
    o3 = open_.shift(3); c3 = close.shift(3); h3 = high.shift(3)
    g1 = c1 > o1; g2 = c2 > o2
    b1 = c1 - o1; b2 = c2 - o2
    sim = (b1 - b2).abs() / b2.replace(0, np.nan) <= 0.3
    gap_up = l2 > h3
    pattern_low = pd.concat([l1, l2], axis=1).min(axis=1)
    failed_today = close < pattern_low
    flag = (g1 & g2 & sim & gap_up & failed_today).astype(float)
    return flag.where(c3.notna(), np.nan)


def f06_cscr_167_mat_hold_failure_at_high(open_, high, low, close):
    o0 = open_; c0 = close
    o4 = open_.shift(4); c4 = close.shift(4)
    o3 = open_.shift(3); c3 = close.shift(3); h3 = high.shift(3); l3 = low.shift(3)
    o2 = open_.shift(2); c2 = close.shift(2)
    o1 = open_.shift(1); c1 = close.shift(1)
    big_green4 = (c4 > o4) & ((c4 - o4) >= 1.5 * _atr(high, low, close, n=MDAYS))
    small_red3 = (c3 < o3)
    small_red2 = (c2 < o2)
    small_red1 = (c1 < o1)
    big_green0 = (c0 > o0) & ((c0 - o0) >= 1.5 * _atr(high, low, close, n=MDAYS))
    pattern_low = pd.concat([l3.shift(0), low.shift(1), low.shift(2)], axis=1).min(axis=1)
    setup = big_green4 & small_red3 & small_red2 & small_red1 & big_green0
    near = _near_252d_high_atr(high, low, close, k=1.0)
    fail = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        active_setup = setup.shift(k).fillna(False)
        pl_k = pattern_low.shift(k)
        near_k = near.shift(k).fillna(False)
        fail = fail + ((close < pl_k) & active_setup & near_k).astype(float)
    return (fail > 0).astype(float).where(c4.notna(), np.nan)


def f06_cscr_168_three_stars_south_inverted(open_, high, low, close):
    g0 = close > open_
    g1 = close.shift(1) > open_.shift(1)
    g2 = close.shift(2) > open_.shift(2)
    r0 = (high - low); r1 = (high - low).shift(1); r2 = (high - low).shift(2)
    shrink = (r0 < r1) & (r1 < r2)
    small = (close - open_).abs() / r0.replace(0, np.nan) <= 0.3
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (g0 & g1 & g2 & shrink & small & near).astype(float)
    return flag.where(r2.notna() & near.notna(), np.nan)


def f06_cscr_169_concealing_baby_swallow_inverse(open_, high, low, close):
    o0 = open_; c0 = close; h0 = high; l0 = low
    o1 = open_.shift(1); c1 = close.shift(1); h1 = high.shift(1); l1 = low.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2); h2 = high.shift(2); l2 = low.shift(2)
    r1 = (h1 - l1).replace(0, np.nan); r2 = (h2 - l2).replace(0, np.nan)
    big_green1 = (c1 > o1) & ((c1 - o1) / r1 >= 0.9)
    big_green2 = (c2 > o2) & ((c2 - o2) / r2 >= 0.9)
    today_opens_above = o0 > h1
    today_closes_inside = (c0 <= h1) & (c0 >= l1)
    flag = (big_green1 & big_green2 & today_opens_above & today_closes_inside).astype(float)
    return flag.where(c2.notna(), np.nan)


def f06_cscr_170_hikkake_bearish_indicator(open_, high, low, close):
    h2 = high.shift(2); l2 = low.shift(2); h3 = high.shift(3); l3 = low.shift(3)
    inside_bar = (h2 < h3) & (l2 > l3)
    h1 = high.shift(1)
    false_brk = h1 > h2
    trigger = close < l2
    flag = (inside_bar & false_brk & trigger).astype(float)
    return flag.where(l3.notna(), np.nan)


def f06_cscr_171_hikkake_bearish_at_252d_high(open_, high, low, close):
    h2 = high.shift(2); l2 = low.shift(2); h3 = high.shift(3); l3 = low.shift(3)
    inside_bar = (h2 < h3) & (l2 > l3)
    h1 = high.shift(1)
    false_brk = h1 > h2
    trigger = close < l2
    near = _near_252d_high_atr(high, low, close, k=1.0)
    flag = (inside_bar & false_brk & trigger & near).astype(float)
    return flag.where(l3.notna() & near.notna(), np.nan)


def f06_cscr_172_modified_hikkake_bearish(open_, high, low, close):
    h2 = high.shift(2); l2 = low.shift(2); h3 = high.shift(3); l3 = low.shift(3)
    inside_bar = (h2 < h3) & (l2 > l3)
    h1 = high.shift(1)
    false_brk = h1 > h2
    trigger = close < l2
    base_flag = (inside_bar & false_brk & trigger)
    today_red = close < open_
    confirm = pd.Series(False, index=close.index)
    for k in range(0, 4):
        confirm |= base_flag.shift(k).fillna(False)
    flag = (confirm & today_red).astype(float)
    return flag.where(l3.notna(), np.nan)


def f06_cscr_173_heikin_ashi_red_after_green_streak(open_, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open_, high, low, close)
    ha_green = ha_c > ha_o
    ha_red = ha_c < ha_o
    streak = ha_green.astype(int).groupby((ha_green != ha_green.shift()).cumsum()).cumcount() + 1
    streak = streak.where(ha_green, 0)
    prior_streak = streak.shift(1).fillna(0)
    flag = (ha_red & (prior_streak >= 3)).astype(float)
    return flag.where(ha_o.notna(), np.nan)


def f06_cscr_174_heikin_ashi_flip_no_upper_shadow(open_, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open_, high, low, close)
    ha_red = ha_c < ha_o
    body_top = pd.concat([ha_o, ha_c], axis=1).max(axis=1)
    no_upper = (ha_h - body_top) <= 1e-9
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (ha_red & no_upper & near).astype(float)
    return flag.where(near.notna(), np.nan)


def f06_cscr_175_heikin_ashi_body_size_zscore(open_, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open_, high, low, close)
    body = (ha_o - ha_c).where(ha_c < ha_o, np.nan)
    z = _rolling_zscore(body, QDAYS)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    return z.where(near, np.nan)


def f06_cscr_176_heikin_ashi_streak_length_at_flip(open_, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open_, high, low, close)
    ha_green = ha_c > ha_o
    ha_red = ha_c < ha_o
    streak = ha_green.astype(int).groupby((ha_green != ha_green.shift()).cumsum()).cumcount() + 1
    streak = streak.where(ha_green, 0)
    prior_streak = streak.shift(1).fillna(0)
    return prior_streak.where(ha_red, np.nan).astype(float)


def f06_cscr_177_renko_reversal_atr_brick(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    c = close.to_numpy(copy=True)
    a = atr.to_numpy(copy=True)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    last_brick_close = np.nan
    last_color = 0  # 1 green, -1 red
    green_streak = 0
    for i in range(n):
        if np.isnan(c[i]) or np.isnan(a[i]) or a[i] <= 0:
            out[i] = 0.0
            continue
        if np.isnan(last_brick_close):
            last_brick_close = c[i]
            out[i] = 0.0
            continue
        moves_up = int((c[i] - last_brick_close) / a[i])
        moves_dn = int((last_brick_close - c[i]) / a[i])
        flip = 0.0
        if moves_up >= 1:
            if last_color == 1:
                green_streak += moves_up
            else:
                green_streak = moves_up
            last_color = 1
            last_brick_close = last_brick_close + moves_up * a[i]
        elif moves_dn >= 1:
            if last_color == 1 and green_streak >= 3:
                flip = 1.0
            green_streak = 0
            last_color = -1
            last_brick_close = last_brick_close - moves_dn * a[i]
        out[i] = flip
    return pd.Series(out, index=close.index)


def f06_cscr_178_renko_reversal_percent_brick_2pct(open_, high, low, close):
    c = close.to_numpy(copy=True)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    last_brick_close = np.nan
    last_color = 0
    green_streak = 0
    for i in range(n):
        if np.isnan(c[i]) or c[i] <= 0:
            out[i] = 0.0
            continue
        if np.isnan(last_brick_close):
            last_brick_close = c[i]
            out[i] = 0.0
            continue
        brick = 0.02 * last_brick_close
        if brick <= 0:
            out[i] = 0.0
            continue
        moves_up = int((c[i] - last_brick_close) / brick)
        moves_dn = int((last_brick_close - c[i]) / brick)
        flip = 0.0
        if moves_up >= 1:
            if last_color == 1:
                green_streak += moves_up
            else:
                green_streak = moves_up
            last_color = 1
            last_brick_close = last_brick_close + moves_up * brick
        elif moves_dn >= 1:
            if last_color == 1 and green_streak >= 3:
                flip = 1.0
            green_streak = 0
            last_color = -1
            last_brick_close = last_brick_close - moves_dn * brick
        out[i] = flip
    return pd.Series(out, index=close.index)


def f06_cscr_179_renko_brick_count_to_reversal(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    c = close.to_numpy(copy=True); a = atr.to_numpy(copy=True)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    last_brick_close = np.nan
    last_color = 0
    green_streak = 0
    last_streak_at_flip = np.nan
    for i in range(n):
        if np.isnan(c[i]) or np.isnan(a[i]) or a[i] <= 0:
            out[i] = last_streak_at_flip
            continue
        if np.isnan(last_brick_close):
            last_brick_close = c[i]
            out[i] = last_streak_at_flip
            continue
        moves_up = int((c[i] - last_brick_close) / a[i])
        moves_dn = int((last_brick_close - c[i]) / a[i])
        if moves_up >= 1:
            if last_color == 1:
                green_streak += moves_up
            else:
                green_streak = moves_up
            last_color = 1
            last_brick_close = last_brick_close + moves_up * a[i]
        elif moves_dn >= 1:
            if last_color == 1:
                last_streak_at_flip = float(green_streak)
            green_streak = 0
            last_color = -1
            last_brick_close = last_brick_close - moves_dn * a[i]
        out[i] = last_streak_at_flip
    return pd.Series(out, index=close.index)


def f06_cscr_180_engulfing_quality_score(open_, close, volume):
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    cov = _safe_div(today_top - today_bot, prev_top - prev_bot)
    prior_bull = _safe_div(prev_c - prev_o, prev_o)
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ratio = _safe_div(volume, vavg)
    qual = cov * prior_bull.clip(lower=0) * vol_ratio
    return qual.where(today_red & prev_green, np.nan)


def f06_cscr_181_doji_quality_score(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_ratio = body / rng
    proximity = 1.0 - (body / close.replace(0, np.nan).abs()).clip(upper=0.01) / 0.01
    smallness = 1.0 - body_ratio.clip(upper=0.2) / 0.2
    atr = _atr(high, low, close, n=MDAYS)
    atr_factor = 1.0 - (atr / close.replace(0, np.nan)).clip(upper=0.05) / 0.05
    return (proximity * smallness * atr_factor).where(rng.notna(), np.nan)


def f06_cscr_182_hammer_quality_inverse(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    lower_ratio = (body_bot - low) / rng
    small_body = 1.0 - (body / rng).clip(upper=0.4) / 0.4
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    trend_pos = _safe_div(high, rmax)
    return (lower_ratio * small_body * near * trend_pos).where(rng.notna(), np.nan)


def f06_cscr_183_shooting_star_quality_score(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper_ratio = (high - body_top) / rng
    small_body = 1.0 - (body / rng).clip(upper=0.4) / 0.4
    prior_trend = (close.shift(1) - close.shift(WDAYS + 1)) / close.shift(WDAYS + 1).replace(0, np.nan)
    return (upper_ratio * small_body * prior_trend.clip(lower=0)).where(rng.notna(), np.nan)


def f06_cscr_184_pattern_sequence_doji_then_engulf(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    is_doji = (body / rng) <= 0.10
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot) & today_red & prev_green
    prior_doji = pd.Series(False, index=close.index)
    for k in range(1, WDAYS + 1):
        prior_doji |= is_doji.shift(k).fillna(False)
    return (prior_doji & engulf).astype(float).where(rng.notna(), np.nan)


def f06_cscr_185_pattern_sequence_star_then_marubozu(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    star = ((body / rng) <= 0.3) & (upper >= 0.25) & (lower >= 0.25)
    red = close < open_
    bear_maru = red & ((body / rng) >= 0.9)
    prior_star = pd.Series(False, index=close.index)
    for k in range(1, 4):
        prior_star |= star.shift(k).fillna(False)
    return (prior_star & bear_maru).astype(float).where(rng.notna(), np.nan)


def f06_cscr_186_pattern_sequence_engulf_then_gap_down(open_, high, low, close):
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red0 = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot) & today_red0 & prev_green
    gap_down_today = high < low.shift(1)
    prior_engulf = pd.Series(False, index=close.index)
    for k in range(1, WDAYS + 1):
        prior_engulf |= engulf.shift(k).fillna(False)
    return (prior_engulf & gap_down_today).astype(float).where(prev_c.notna(), np.nan)


def f06_cscr_187_consecutive_same_pattern_mean_spacing_63d(open_, close):
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot) & today_red & prev_green
    f = engulf.astype(float).to_numpy(copy=True)
    n = len(f)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        win = f[lo:i + 1]
        idxs = np.where(win > 0)[0]
        if idxs.size >= 2:
            out[i] = float(np.diff(idxs).mean())
    return pd.Series(out, index=close.index)


def f06_cscr_188_pattern_diversity_entropy_63d(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    today_top = body_top; today_bot = body_bot
    upper = (high - body_top); lower = (body_bot - low)
    doji = ((body / rng) <= 0.10).astype(float)
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = ((today_top >= prev_top) & (today_bot <= prev_bot) & today_red & prev_green).astype(float)
    star = (((body / rng) <= 0.3) & (upper >= 2 * body) & ((lower / rng) <= 0.1)).astype(float)
    hang = (((body / rng) <= 0.3) & (lower >= 2 * body) & ((upper / rng) <= 0.1)).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    d = (doji * near).rolling(QDAYS, min_periods=MDAYS).sum()
    e = (engulf * near).rolling(QDAYS, min_periods=MDAYS).sum()
    s = (star * near).rolling(QDAYS, min_periods=MDAYS).sum()
    h = (hang * near).rolling(QDAYS, min_periods=MDAYS).sum()
    total = d + e + s + h
    def _h(x, t):
        p = _safe_div(x, t).replace(0, np.nan)
        return -(p * np.log(p)).fillna(0.0)
    ent = _h(d, total) + _h(e, total) + _h(s, total) + _h(h, total)
    return ent.where(total > 0, np.nan)


def f06_cscr_189_red_bar_streak_in_upper_bband(open_, high, low, close):
    ma = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    upper_bb = ma + 2 * sd
    in_upper = close >= upper_bb
    red = close < open_
    cond = (red & in_upper).astype(int)
    streak = cond.groupby((cond != cond.shift()).cumsum()).cumcount() + 1
    streak = streak.where(cond.astype(bool), 0)
    return streak.astype(float).where(upper_bb.notna(), np.nan)


def f06_cscr_190_nr4_at_252d_high(high, low, close):
    rng = (high - low)
    rmin = rng.rolling(4, min_periods=4).min()
    is_nr4 = rng <= rmin
    at_peak = _at_252d_high(high)
    return (is_nr4 & at_peak).astype(float).where(rmin.notna(), np.nan)


def f06_cscr_191_nr7_at_252d_high(high, low, close):
    rng = (high - low)
    rmin = rng.rolling(7, min_periods=7).min()
    is_nr7 = rng <= rmin
    at_peak = _at_252d_high(high)
    return (is_nr7 & at_peak).astype(float).where(rmin.notna(), np.nan)


def f06_cscr_192_nr7_then_red_break_at_high(open_, high, low, close):
    rng = (high - low)
    rmin = rng.shift(1).rolling(7, min_periods=7).min()
    nr7_yesterday = (rng.shift(1) <= rmin)
    red = close < open_
    break_lo = close < low.shift(1)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (nr7_yesterday & red & break_lo & near).astype(float)
    return flag.where(rmin.notna() & near.notna(), np.nan)


def f06_cscr_193_wide_range_then_narrow_at_high(open_, high, low, close):
    rng = (high - low)
    rmax21 = rng.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    widest_yesterday = rng.shift(1) >= rmax21
    nr4_today = rng <= rng.rolling(4, min_periods=4).min()
    near = _near_252d_high_atr(high, low, close, k=2.0)
    return (widest_yesterday & nr4_today & near).astype(float).where(rmax21.notna(), np.nan)


def f06_cscr_194_outside_red_bar_specifically(open_, high, low, close):
    prev_h = high.shift(1); prev_l = low.shift(1)
    outside = (high > prev_h) & (low < prev_l)
    red = close < open_
    return (outside & red).astype(float).where(prev_h.notna(), np.nan)


def f06_cscr_195_outside_red_at_252d_high_count_63d(open_, high, low, close):
    prev_h = high.shift(1); prev_l = low.shift(1)
    outside = (high > prev_h) & (low < prev_l)
    red = close < open_
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (outside & red & near).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_196_pin_bar_bearish_indicator(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top)
    body = (close - open_).abs()
    upper_ratio = upper / rng
    body_in_lower = ((body_top - low) / rng) <= (1.0 / 3.0)
    small = (body / rng) <= 0.25
    flag = ((upper_ratio >= (2.0 / 3.0)) & body_in_lower & small).astype(float)
    return flag.where(rng.notna(), np.nan)


def f06_cscr_197_pin_bar_atr_normalized_size(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top)
    upper_ratio = upper / rng
    is_pin = upper_ratio >= (2.0 / 3.0)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(upper, atr).where(is_pin, np.nan)


def f06_cscr_198_pin_bar_at_252d_high(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top)
    body = (close - open_).abs()
    body_in_lower = ((body_top - low) / rng) <= (1.0 / 3.0)
    small = (body / rng) <= 0.25
    is_pin = ((upper / rng) >= (2.0 / 3.0)) & body_in_lower & small
    near = _near_252d_high_atr(high, low, close, k=1.0)
    return (is_pin & near).astype(float).where(near.notna() & rng.notna(), np.nan)


def f06_cscr_199_inside_bar_after_climax_push(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    rng = (high - low)
    rng_y = rng.shift(1); atr_y = atr.shift(1)
    climax_y = (rng_y > 2 * atr_y) & ((close.shift(1) - low.shift(1)) / rng_y.replace(0, np.nan) >= 2.0 / 3.0)
    inside_today = (high < high.shift(1)) & (low > low.shift(1))
    return (climax_y & inside_today).astype(float).where(atr_y.notna(), np.nan)


def f06_cscr_200_climax_bar_reversal_close_lower_half(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    rng = (high - low).replace(0, np.nan)
    big = rng > 2.5 * atr
    close_pos = (close - low) / rng
    in_lower_half = close_pos < 0.5
    near = _near_252d_high_atr(high, low, close, k=2.0)
    return (big & in_lower_half & near).astype(float).where(atr.notna() & near.notna(), np.nan)


def f06_cscr_201_climax_bar_then_red_followthrough(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    rng = (high - low)
    climax = rng > 2.5 * atr
    mid = (high + low) / 2.0
    red = close < open_
    out = pd.Series(0.0, index=close.index)
    for k in range(1, 3):
        cl_k = climax.shift(k).fillna(False)
        mid_k = mid.shift(k)
        cond = cl_k & red & (close < mid_k)
        out = out + cond.astype(float)
    return (out > 0).astype(float).where(atr.notna(), np.nan)


def f06_cscr_202_close_below_prior_open_severity(open_, high, low, close):
    prev_o = open_.shift(1)
    atr = _atr(high, low, close, n=MDAYS)
    sev = _safe_div(prev_o - close, atr)
    return sev.where(close < prev_o, np.nan)


def f06_cscr_203_three_bar_thrust_failure(open_, high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs()
    big_green2 = (close.shift(2) > open_.shift(2)) & ((close.shift(2) - open_.shift(2)) > atr.shift(2))
    body_ratio_y = body.shift(1) / rng.shift(1)
    doji_y = body_ratio_y <= 0.1
    red0 = close < open_
    return (big_green2 & doji_y & red0).astype(float).where(atr.notna(), np.nan)


def f06_cscr_204_failed_breakout_red_bar(high, low, close):
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    broke = high > h21
    failed = close < h21
    return (broke & failed).astype(float).where(h21.notna(), np.nan)


def f06_cscr_205_failed_breakout_atr_distance(high, low, close):
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    broke = high > h21
    failed = close < h21
    dist_above = (high - h21).clip(lower=0)
    dist_below = (h21 - close).clip(lower=0)
    sev = _safe_div(dist_above + dist_below, atr)
    return sev.where(broke & failed, np.nan)


def f06_cscr_206_two_legged_pullback_failure_top(open_, high, low, close):
    near = _near_252d_high_atr(high, low, close, k=1.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high >= rmax
    pullback_a = ((close.shift(3) < open_.shift(3)) & near.shift(3).fillna(False))
    pullback_b = ((close.shift(2) < open_.shift(2)) & near.shift(2).fillna(False))
    no_new_high = ~new_high.shift(1).fillna(False)
    gap_dn_today = high < low.shift(1)
    return (pullback_a & pullback_b & no_new_high & gap_dn_today).astype(float).where(rmax.notna(), np.nan)


def f06_cscr_207_doji_at_upper_bband(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    is_doji = (body / rng) <= 0.10
    ma = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    upper_bb = ma + 2 * sd
    return (is_doji & (close >= upper_bb)).astype(float).where(upper_bb.notna(), np.nan)


def f06_cscr_208_engulf_at_upper_bband(open_, close):
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    ma = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    upper_bb = ma + 2 * sd
    return (engulf & today_red & prev_green & (prev_c >= upper_bb.shift(1))).astype(float).where(upper_bb.notna(), np.nan)


def f06_cscr_209_friday_reversal_indicator(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    today_top = body_top; today_bot = body_bot
    upper = (high - body_top); lower = (body_bot - low)
    star = ((body / rng) <= 0.3) & (upper >= 2 * body) & ((lower / rng) <= 0.1)
    hang = ((body / rng) <= 0.3) & (lower >= 2 * body) & ((upper / rng) <= 0.1)
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot) & today_red & prev_green
    any_rev = (star | hang | engulf)
    idx = close.index
    is_friday = pd.Series(False, index=idx)
    if isinstance(idx, pd.DatetimeIndex):
        is_friday = pd.Series(idx.weekday == 4, index=idx)
    return (any_rev & is_friday).astype(float).where(rng.notna(), np.nan)


def f06_cscr_210_monday_gap_down_after_friday_high(open_, high, low, close):
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    prev_close_at_h21 = close.shift(1) >= h21
    gap_down = open_ < low.shift(1)
    idx = close.index
    is_monday = pd.Series(False, index=idx)
    if isinstance(idx, pd.DatetimeIndex):
        is_monday = pd.Series(idx.weekday == 0, index=idx)
    return (is_monday & prev_close_at_h21 & gap_down).astype(float).where(h21.notna(), np.nan)


def f06_cscr_211_end_of_week_doji_at_high(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    is_doji = (body / rng) <= 0.10
    at_peak = _at_252d_high(high)
    idx = close.index
    is_friday = pd.Series(False, index=idx)
    if isinstance(idx, pd.DatetimeIndex):
        is_friday = pd.Series(idx.weekday == 4, index=idx)
    return (is_doji & at_peak & is_friday).astype(float).where(rng.notna(), np.nan)


def f06_cscr_212_dark_pool_signature_proxy(high, low, close, volume):
    atr = _atr(high, low, close, n=MDAYS)
    rng = (high - low)
    tight = rng < 0.5 * atr
    vmed = volume.rolling(20, min_periods=10).median()
    high_vol = volume > 1.5 * vmed
    near = _near_252d_high_atr(high, low, close, k=2.0)
    return (tight & high_vol & near).astype(float).where(vmed.notna() & atr.notna(), np.nan)


def f06_cscr_213_no_demand_bar_at_high(open_, high, low, close, volume):
    rng = (high - low)
    atr = _atr(high, low, close, n=MDAYS)
    narrow = rng < 0.7 * atr
    up_bar = close > open_
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    low_vol = volume < 0.8 * vavg
    near = _near_252d_high_atr(high, low, close, k=2.0)
    return (up_bar & narrow & low_vol & near).astype(float).where(vavg.notna() & atr.notna(), np.nan)


def f06_cscr_214_upthrust_bar_vsa(open_, high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    atr = _atr(high, low, close, n=MDAYS)
    wide = rng > 1.3 * atr
    close_pos = (close - low) / rng
    low_close = close_pos < 0.33
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    high_vol = volume > 1.5 * vavg
    new_high = high > high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (wide & low_close & high_vol & new_high).astype(float).where(vavg.notna() & atr.notna(), np.nan)


def f06_cscr_215_no_supply_reversal_proxy(open_, high, low, close, volume):
    rng = (high - low)
    atr = _atr(high, low, close, n=MDAYS)
    wide_y = rng.shift(1) > 1.3 * atr.shift(1)
    low_close_y = ((close.shift(1) - low.shift(1)) / rng.shift(1).replace(0, np.nan)) < 0.33
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    high_vol_y = volume.shift(1) > 1.5 * vavg.shift(1)
    new_high_y = high.shift(1) > high.shift(2).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust_y = wide_y & low_close_y & high_vol_y & new_high_y
    narrow_today = (high - low) < 0.7 * atr
    low_vol_today = volume < 0.8 * vavg
    down_today = close < open_
    return (upthrust_y & narrow_today & low_vol_today & down_today).astype(float).where(vavg.notna() & atr.notna(), np.nan)


def f06_cscr_216_open_top_quartile_close_bottom_quartile_extreme_reversal(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    open_pos = (open_ - low) / rng
    close_pos = (close - low) / rng
    return ((open_pos >= 0.75) & (close_pos <= 0.25)).astype(float).where(rng.notna(), np.nan)


def f06_cscr_217_consecutive_lower_closes_at_252d_high(high, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * rmax
    lower = close < close.shift(1)
    cond = (near & lower).astype(int)
    streak = cond.groupby((cond != cond.shift()).cumsum()).cumcount() + 1
    streak = streak.where(cond.astype(bool), 0)
    return streak.astype(float).where(rmax.notna(), np.nan)


def f06_cscr_218_lower_close_streak_break_event(close):
    higher = close > close.shift(1)
    lower = close < close.shift(1)
    higher_yesterday = higher.shift(1).fillna(False)
    higher_2 = higher.shift(2).fillna(False)
    prior_run = higher_yesterday & higher_2
    return (lower & prior_run).astype(float).where(close.notna(), np.nan)


def f06_cscr_219_doji_then_two_red_confirmation(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji_2 = ((body.shift(2) / rng.shift(2)) <= 0.10)
    red_1 = (close.shift(1) < open_.shift(1))
    red_0 = (close < open_)
    return (doji_2 & red_1 & red_0).astype(float).where(rng.notna(), np.nan)


def f06_cscr_220_engulf_followed_by_lower_close_5d(open_, high, low, close):
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot) & today_red & prev_green
    engulf_low = low.where(engulf)
    out = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        el_k = engulf_low.shift(k)
        out = out + ((close < el_k)).astype(float)
    return (out > 0).astype(float).where(prev_c.notna(), np.nan)


def f06_cscr_221_tweezer_top_volume_confirmed(open_, high, low, close, volume):
    prev_h = high.shift(1); prev_o = open_.shift(1); prev_c = close.shift(1)
    near_eq = (high - prev_h).abs() / prev_h.replace(0, np.nan) <= 0.001
    prev_green = prev_c > prev_o
    today_red = close < open_
    vol_ok = volume > 1.3 * volume.shift(1)
    return (near_eq & prev_green & today_red & vol_ok).astype(float).where(prev_h.notna(), np.nan)


def f06_cscr_222_high_wave_after_strong_advance(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.15
    long_shadows = (upper >= 0.4) & (lower >= 0.4)
    ret5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    advance = ret5 > 0.05
    return (small_body & long_shadows & advance).astype(float).where(rng.notna(), np.nan)


def f06_cscr_223_long_legged_doji_at_atr_extreme(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    is_doji = (body / rng) <= 0.05
    atr = _atr(high, low, close, n=MDAYS)
    big_range = rng > 2.0 * atr
    at_peak = _at_252d_high(high)
    return (is_doji & big_range & at_peak).astype(float).where(atr.notna(), np.nan)


def f06_cscr_224_dragonfly_failure_within_3d(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top); lower = (body_bot - low)
    is_doji = (body / rng) <= 0.05
    dragonfly = is_doji & (lower / rng >= 0.6) & ((upper / rng) <= 0.1)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    setup = dragonfly & near
    out = pd.Series(0.0, index=close.index)
    for k in range(1, 4):
        setup_k = setup.shift(k).fillna(False)
        out = out + (setup_k & (close < open_)).astype(float)
    return (out > 0).astype(float).where(rng.notna(), np.nan)


def f06_cscr_225_marubozu_then_immediate_reversal(open_, high, low, close):
    body_y = (close.shift(1) - open_.shift(1))
    rng_y = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    bull_maru_y = (close.shift(1) > open_.shift(1)) & ((body_y / rng_y) >= 0.9)
    kicker = (open_ < open_.shift(1)) & (close < open_)
    gap_dn_red = (high < low.shift(1)) & (close < open_)
    return (bull_maru_y & (kicker | gap_dn_red)).astype(float).where(rng_y.notna(), np.nan)



def f06_cscr_151_belt_hold_bearish_indicator_d1(open_, high, low, close): return f06_cscr_151_belt_hold_bearish_indicator(open_, high, low, close).diff()

def f06_cscr_152_belt_hold_at_252d_high_d1(open_, high, low, close): return f06_cscr_152_belt_hold_at_252d_high(open_, high, low, close).diff()

def f06_cscr_153_bearish_counterattack_line_d1(open_, high, low, close): return f06_cscr_153_bearish_counterattack_line(open_, high, low, close).diff()

def f06_cscr_154_bearish_meeting_line_tolerance_score_d1(open_, high, low, close): return f06_cscr_154_bearish_meeting_line_tolerance_score(open_, high, low, close).diff()

def f06_cscr_155_stick_sandwich_bearish_d1(open_, close): return f06_cscr_155_stick_sandwich_bearish(open_, close).diff()

def f06_cscr_156_identical_three_crows_d1(open_, close): return f06_cscr_156_identical_three_crows(open_, close).diff()

def f06_cscr_157_advance_block_indicator_d1(open_, high, low, close): return f06_cscr_157_advance_block_indicator(open_, high, low, close).diff()

def f06_cscr_158_deliberation_pattern_d1(open_, high, low, close): return f06_cscr_158_deliberation_pattern(open_, high, low, close).diff()

def f06_cscr_159_tower_top_indicator_d1(open_, high, low, close): return f06_cscr_159_tower_top_indicator(open_, high, low, close).diff()

def f06_cscr_160_three_mountains_top_d1(high): return f06_cscr_160_three_mountains_top(high).diff()

def f06_cscr_161_three_buddha_top_d1(high): return f06_cscr_161_three_buddha_top(high).diff()

def f06_cscr_162_falling_window_confirmation_d1(open_, high, low, close): return f06_cscr_162_falling_window_confirmation(open_, high, low, close).diff()

def f06_cscr_163_rising_window_failure_d1(open_, high, low, close): return f06_cscr_163_rising_window_failure(open_, high, low, close).diff()

def f06_cscr_164_downward_tasuki_gap_failed_d1(open_, high, low, close): return f06_cscr_164_downward_tasuki_gap_failed(open_, high, low, close).diff()

def f06_cscr_165_upward_tasuki_gap_failure_d1(open_, high, low, close): return f06_cscr_165_upward_tasuki_gap_failure(open_, high, low, close).diff()

def f06_cscr_166_side_by_side_white_after_gap_up_failed_d1(open_, high, low, close): return f06_cscr_166_side_by_side_white_after_gap_up_failed(open_, high, low, close).diff()

def f06_cscr_167_mat_hold_failure_at_high_d1(open_, high, low, close): return f06_cscr_167_mat_hold_failure_at_high(open_, high, low, close).diff()

def f06_cscr_168_three_stars_south_inverted_d1(open_, high, low, close): return f06_cscr_168_three_stars_south_inverted(open_, high, low, close).diff()

def f06_cscr_169_concealing_baby_swallow_inverse_d1(open_, high, low, close): return f06_cscr_169_concealing_baby_swallow_inverse(open_, high, low, close).diff()

def f06_cscr_170_hikkake_bearish_indicator_d1(open_, high, low, close): return f06_cscr_170_hikkake_bearish_indicator(open_, high, low, close).diff()

def f06_cscr_171_hikkake_bearish_at_252d_high_d1(open_, high, low, close): return f06_cscr_171_hikkake_bearish_at_252d_high(open_, high, low, close).diff()

def f06_cscr_172_modified_hikkake_bearish_d1(open_, high, low, close): return f06_cscr_172_modified_hikkake_bearish(open_, high, low, close).diff()

def f06_cscr_173_heikin_ashi_red_after_green_streak_d1(open_, high, low, close): return f06_cscr_173_heikin_ashi_red_after_green_streak(open_, high, low, close).diff()

def f06_cscr_174_heikin_ashi_flip_no_upper_shadow_d1(open_, high, low, close): return f06_cscr_174_heikin_ashi_flip_no_upper_shadow(open_, high, low, close).diff()

def f06_cscr_175_heikin_ashi_body_size_zscore_d1(open_, high, low, close): return f06_cscr_175_heikin_ashi_body_size_zscore(open_, high, low, close).diff()

def f06_cscr_176_heikin_ashi_streak_length_at_flip_d1(open_, high, low, close): return f06_cscr_176_heikin_ashi_streak_length_at_flip(open_, high, low, close).diff()

def f06_cscr_177_renko_reversal_atr_brick_d1(open_, high, low, close): return f06_cscr_177_renko_reversal_atr_brick(open_, high, low, close).diff()

def f06_cscr_178_renko_reversal_percent_brick_2pct_d1(open_, high, low, close): return f06_cscr_178_renko_reversal_percent_brick_2pct(open_, high, low, close).diff()

def f06_cscr_179_renko_brick_count_to_reversal_d1(open_, high, low, close): return f06_cscr_179_renko_brick_count_to_reversal(open_, high, low, close).diff()

def f06_cscr_180_engulfing_quality_score_d1(open_, close, volume): return f06_cscr_180_engulfing_quality_score(open_, close, volume).diff()

def f06_cscr_181_doji_quality_score_d1(open_, high, low, close): return f06_cscr_181_doji_quality_score(open_, high, low, close).diff()

def f06_cscr_182_hammer_quality_inverse_d1(open_, high, low, close): return f06_cscr_182_hammer_quality_inverse(open_, high, low, close).diff()

def f06_cscr_183_shooting_star_quality_score_d1(open_, high, low, close): return f06_cscr_183_shooting_star_quality_score(open_, high, low, close).diff()

def f06_cscr_184_pattern_sequence_doji_then_engulf_d1(open_, high, low, close): return f06_cscr_184_pattern_sequence_doji_then_engulf(open_, high, low, close).diff()

def f06_cscr_185_pattern_sequence_star_then_marubozu_d1(open_, high, low, close): return f06_cscr_185_pattern_sequence_star_then_marubozu(open_, high, low, close).diff()

def f06_cscr_186_pattern_sequence_engulf_then_gap_down_d1(open_, high, low, close): return f06_cscr_186_pattern_sequence_engulf_then_gap_down(open_, high, low, close).diff()

def f06_cscr_187_consecutive_same_pattern_mean_spacing_63d_d1(open_, close): return f06_cscr_187_consecutive_same_pattern_mean_spacing_63d(open_, close).diff()

def f06_cscr_188_pattern_diversity_entropy_63d_d1(open_, high, low, close): return f06_cscr_188_pattern_diversity_entropy_63d(open_, high, low, close).diff()

def f06_cscr_189_red_bar_streak_in_upper_bband_d1(open_, high, low, close): return f06_cscr_189_red_bar_streak_in_upper_bband(open_, high, low, close).diff()

def f06_cscr_190_nr4_at_252d_high_d1(high, low, close): return f06_cscr_190_nr4_at_252d_high(high, low, close).diff()

def f06_cscr_191_nr7_at_252d_high_d1(high, low, close): return f06_cscr_191_nr7_at_252d_high(high, low, close).diff()

def f06_cscr_192_nr7_then_red_break_at_high_d1(open_, high, low, close): return f06_cscr_192_nr7_then_red_break_at_high(open_, high, low, close).diff()

def f06_cscr_193_wide_range_then_narrow_at_high_d1(open_, high, low, close): return f06_cscr_193_wide_range_then_narrow_at_high(open_, high, low, close).diff()

def f06_cscr_194_outside_red_bar_specifically_d1(open_, high, low, close): return f06_cscr_194_outside_red_bar_specifically(open_, high, low, close).diff()

def f06_cscr_195_outside_red_at_252d_high_count_63d_d1(open_, high, low, close): return f06_cscr_195_outside_red_at_252d_high_count_63d(open_, high, low, close).diff()

def f06_cscr_196_pin_bar_bearish_indicator_d1(open_, high, low, close): return f06_cscr_196_pin_bar_bearish_indicator(open_, high, low, close).diff()

def f06_cscr_197_pin_bar_atr_normalized_size_d1(open_, high, low, close): return f06_cscr_197_pin_bar_atr_normalized_size(open_, high, low, close).diff()

def f06_cscr_198_pin_bar_at_252d_high_d1(open_, high, low, close): return f06_cscr_198_pin_bar_at_252d_high(open_, high, low, close).diff()

def f06_cscr_199_inside_bar_after_climax_push_d1(open_, high, low, close): return f06_cscr_199_inside_bar_after_climax_push(open_, high, low, close).diff()

def f06_cscr_200_climax_bar_reversal_close_lower_half_d1(open_, high, low, close): return f06_cscr_200_climax_bar_reversal_close_lower_half(open_, high, low, close).diff()

def f06_cscr_201_climax_bar_then_red_followthrough_d1(open_, high, low, close): return f06_cscr_201_climax_bar_then_red_followthrough(open_, high, low, close).diff()

def f06_cscr_202_close_below_prior_open_severity_d1(open_, high, low, close): return f06_cscr_202_close_below_prior_open_severity(open_, high, low, close).diff()

def f06_cscr_203_three_bar_thrust_failure_d1(open_, high, low, close): return f06_cscr_203_three_bar_thrust_failure(open_, high, low, close).diff()

def f06_cscr_204_failed_breakout_red_bar_d1(high, low, close): return f06_cscr_204_failed_breakout_red_bar(high, low, close).diff()

def f06_cscr_205_failed_breakout_atr_distance_d1(high, low, close): return f06_cscr_205_failed_breakout_atr_distance(high, low, close).diff()

def f06_cscr_206_two_legged_pullback_failure_top_d1(open_, high, low, close): return f06_cscr_206_two_legged_pullback_failure_top(open_, high, low, close).diff()

def f06_cscr_207_doji_at_upper_bband_d1(open_, high, low, close): return f06_cscr_207_doji_at_upper_bband(open_, high, low, close).diff()

def f06_cscr_208_engulf_at_upper_bband_d1(open_, close): return f06_cscr_208_engulf_at_upper_bband(open_, close).diff()

def f06_cscr_209_friday_reversal_indicator_d1(open_, high, low, close): return f06_cscr_209_friday_reversal_indicator(open_, high, low, close).diff()

def f06_cscr_210_monday_gap_down_after_friday_high_d1(open_, high, low, close): return f06_cscr_210_monday_gap_down_after_friday_high(open_, high, low, close).diff()

def f06_cscr_211_end_of_week_doji_at_high_d1(open_, high, low, close): return f06_cscr_211_end_of_week_doji_at_high(open_, high, low, close).diff()

def f06_cscr_212_dark_pool_signature_proxy_d1(high, low, close, volume): return f06_cscr_212_dark_pool_signature_proxy(high, low, close, volume).diff()

def f06_cscr_213_no_demand_bar_at_high_d1(open_, high, low, close, volume): return f06_cscr_213_no_demand_bar_at_high(open_, high, low, close, volume).diff()

def f06_cscr_214_upthrust_bar_vsa_d1(open_, high, low, close, volume): return f06_cscr_214_upthrust_bar_vsa(open_, high, low, close, volume).diff()

def f06_cscr_215_no_supply_reversal_proxy_d1(open_, high, low, close, volume): return f06_cscr_215_no_supply_reversal_proxy(open_, high, low, close, volume).diff()

def f06_cscr_216_open_top_quartile_close_bottom_quartile_extreme_reversal_d1(open_, high, low, close): return f06_cscr_216_open_top_quartile_close_bottom_quartile_extreme_reversal(open_, high, low, close).diff()

def f06_cscr_217_consecutive_lower_closes_at_252d_high_d1(high, close): return f06_cscr_217_consecutive_lower_closes_at_252d_high(high, close).diff()

def f06_cscr_218_lower_close_streak_break_event_d1(close): return f06_cscr_218_lower_close_streak_break_event(close).diff()

def f06_cscr_219_doji_then_two_red_confirmation_d1(open_, high, low, close): return f06_cscr_219_doji_then_two_red_confirmation(open_, high, low, close).diff()

def f06_cscr_220_engulf_followed_by_lower_close_5d_d1(open_, high, low, close): return f06_cscr_220_engulf_followed_by_lower_close_5d(open_, high, low, close).diff()

def f06_cscr_221_tweezer_top_volume_confirmed_d1(open_, high, low, close, volume): return f06_cscr_221_tweezer_top_volume_confirmed(open_, high, low, close, volume).diff()

def f06_cscr_222_high_wave_after_strong_advance_d1(open_, high, low, close): return f06_cscr_222_high_wave_after_strong_advance(open_, high, low, close).diff()

def f06_cscr_223_long_legged_doji_at_atr_extreme_d1(open_, high, low, close): return f06_cscr_223_long_legged_doji_at_atr_extreme(open_, high, low, close).diff()

def f06_cscr_224_dragonfly_failure_within_3d_d1(open_, high, low, close): return f06_cscr_224_dragonfly_failure_within_3d(open_, high, low, close).diff()

def f06_cscr_225_marubozu_then_immediate_reversal_d1(open_, high, low, close): return f06_cscr_225_marubozu_then_immediate_reversal(open_, high, low, close).diff()


CANDLESTICK_REVERSAL_CATALOG_D1_REGISTRY_151_225 = {
    "f06_cscr_151_belt_hold_bearish_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_151_belt_hold_bearish_indicator_d1},
    "f06_cscr_152_belt_hold_at_252d_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_152_belt_hold_at_252d_high_d1},
    "f06_cscr_153_bearish_counterattack_line_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_153_bearish_counterattack_line_d1},
    "f06_cscr_154_bearish_meeting_line_tolerance_score_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_154_bearish_meeting_line_tolerance_score_d1},
    "f06_cscr_155_stick_sandwich_bearish_d1": {"inputs": ["open", "close"], "func": f06_cscr_155_stick_sandwich_bearish_d1},
    "f06_cscr_156_identical_three_crows_d1": {"inputs": ["open", "close"], "func": f06_cscr_156_identical_three_crows_d1},
    "f06_cscr_157_advance_block_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_157_advance_block_indicator_d1},
    "f06_cscr_158_deliberation_pattern_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_158_deliberation_pattern_d1},
    "f06_cscr_159_tower_top_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_159_tower_top_indicator_d1},
    "f06_cscr_160_three_mountains_top_d1": {"inputs": ["high"], "func": f06_cscr_160_three_mountains_top_d1},
    "f06_cscr_161_three_buddha_top_d1": {"inputs": ["high"], "func": f06_cscr_161_three_buddha_top_d1},
    "f06_cscr_162_falling_window_confirmation_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_162_falling_window_confirmation_d1},
    "f06_cscr_163_rising_window_failure_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_163_rising_window_failure_d1},
    "f06_cscr_164_downward_tasuki_gap_failed_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_164_downward_tasuki_gap_failed_d1},
    "f06_cscr_165_upward_tasuki_gap_failure_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_165_upward_tasuki_gap_failure_d1},
    "f06_cscr_166_side_by_side_white_after_gap_up_failed_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_166_side_by_side_white_after_gap_up_failed_d1},
    "f06_cscr_167_mat_hold_failure_at_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_167_mat_hold_failure_at_high_d1},
    "f06_cscr_168_three_stars_south_inverted_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_168_three_stars_south_inverted_d1},
    "f06_cscr_169_concealing_baby_swallow_inverse_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_169_concealing_baby_swallow_inverse_d1},
    "f06_cscr_170_hikkake_bearish_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_170_hikkake_bearish_indicator_d1},
    "f06_cscr_171_hikkake_bearish_at_252d_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_171_hikkake_bearish_at_252d_high_d1},
    "f06_cscr_172_modified_hikkake_bearish_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_172_modified_hikkake_bearish_d1},
    "f06_cscr_173_heikin_ashi_red_after_green_streak_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_173_heikin_ashi_red_after_green_streak_d1},
    "f06_cscr_174_heikin_ashi_flip_no_upper_shadow_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_174_heikin_ashi_flip_no_upper_shadow_d1},
    "f06_cscr_175_heikin_ashi_body_size_zscore_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_175_heikin_ashi_body_size_zscore_d1},
    "f06_cscr_176_heikin_ashi_streak_length_at_flip_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_176_heikin_ashi_streak_length_at_flip_d1},
    "f06_cscr_177_renko_reversal_atr_brick_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_177_renko_reversal_atr_brick_d1},
    "f06_cscr_178_renko_reversal_percent_brick_2pct_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_178_renko_reversal_percent_brick_2pct_d1},
    "f06_cscr_179_renko_brick_count_to_reversal_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_179_renko_brick_count_to_reversal_d1},
    "f06_cscr_180_engulfing_quality_score_d1": {"inputs": ["open", "close", "volume"], "func": f06_cscr_180_engulfing_quality_score_d1},
    "f06_cscr_181_doji_quality_score_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_181_doji_quality_score_d1},
    "f06_cscr_182_hammer_quality_inverse_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_182_hammer_quality_inverse_d1},
    "f06_cscr_183_shooting_star_quality_score_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_183_shooting_star_quality_score_d1},
    "f06_cscr_184_pattern_sequence_doji_then_engulf_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_184_pattern_sequence_doji_then_engulf_d1},
    "f06_cscr_185_pattern_sequence_star_then_marubozu_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_185_pattern_sequence_star_then_marubozu_d1},
    "f06_cscr_186_pattern_sequence_engulf_then_gap_down_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_186_pattern_sequence_engulf_then_gap_down_d1},
    "f06_cscr_187_consecutive_same_pattern_mean_spacing_63d_d1": {"inputs": ["open", "close"], "func": f06_cscr_187_consecutive_same_pattern_mean_spacing_63d_d1},
    "f06_cscr_188_pattern_diversity_entropy_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_188_pattern_diversity_entropy_63d_d1},
    "f06_cscr_189_red_bar_streak_in_upper_bband_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_189_red_bar_streak_in_upper_bband_d1},
    "f06_cscr_190_nr4_at_252d_high_d1": {"inputs": ["high", "low", "close"], "func": f06_cscr_190_nr4_at_252d_high_d1},
    "f06_cscr_191_nr7_at_252d_high_d1": {"inputs": ["high", "low", "close"], "func": f06_cscr_191_nr7_at_252d_high_d1},
    "f06_cscr_192_nr7_then_red_break_at_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_192_nr7_then_red_break_at_high_d1},
    "f06_cscr_193_wide_range_then_narrow_at_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_193_wide_range_then_narrow_at_high_d1},
    "f06_cscr_194_outside_red_bar_specifically_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_194_outside_red_bar_specifically_d1},
    "f06_cscr_195_outside_red_at_252d_high_count_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_195_outside_red_at_252d_high_count_63d_d1},
    "f06_cscr_196_pin_bar_bearish_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_196_pin_bar_bearish_indicator_d1},
    "f06_cscr_197_pin_bar_atr_normalized_size_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_197_pin_bar_atr_normalized_size_d1},
    "f06_cscr_198_pin_bar_at_252d_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_198_pin_bar_at_252d_high_d1},
    "f06_cscr_199_inside_bar_after_climax_push_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_199_inside_bar_after_climax_push_d1},
    "f06_cscr_200_climax_bar_reversal_close_lower_half_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_200_climax_bar_reversal_close_lower_half_d1},
    "f06_cscr_201_climax_bar_then_red_followthrough_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_201_climax_bar_then_red_followthrough_d1},
    "f06_cscr_202_close_below_prior_open_severity_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_202_close_below_prior_open_severity_d1},
    "f06_cscr_203_three_bar_thrust_failure_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_203_three_bar_thrust_failure_d1},
    "f06_cscr_204_failed_breakout_red_bar_d1": {"inputs": ["high", "low", "close"], "func": f06_cscr_204_failed_breakout_red_bar_d1},
    "f06_cscr_205_failed_breakout_atr_distance_d1": {"inputs": ["high", "low", "close"], "func": f06_cscr_205_failed_breakout_atr_distance_d1},
    "f06_cscr_206_two_legged_pullback_failure_top_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_206_two_legged_pullback_failure_top_d1},
    "f06_cscr_207_doji_at_upper_bband_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_207_doji_at_upper_bband_d1},
    "f06_cscr_208_engulf_at_upper_bband_d1": {"inputs": ["open", "close"], "func": f06_cscr_208_engulf_at_upper_bband_d1},
    "f06_cscr_209_friday_reversal_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_209_friday_reversal_indicator_d1},
    "f06_cscr_210_monday_gap_down_after_friday_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_210_monday_gap_down_after_friday_high_d1},
    "f06_cscr_211_end_of_week_doji_at_high_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_211_end_of_week_doji_at_high_d1},
    "f06_cscr_212_dark_pool_signature_proxy_d1": {"inputs": ["high", "low", "close", "volume"], "func": f06_cscr_212_dark_pool_signature_proxy_d1},
    "f06_cscr_213_no_demand_bar_at_high_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_213_no_demand_bar_at_high_d1},
    "f06_cscr_214_upthrust_bar_vsa_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_214_upthrust_bar_vsa_d1},
    "f06_cscr_215_no_supply_reversal_proxy_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_215_no_supply_reversal_proxy_d1},
    "f06_cscr_216_open_top_quartile_close_bottom_quartile_extreme_reversal_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_216_open_top_quartile_close_bottom_quartile_extreme_reversal_d1},
    "f06_cscr_217_consecutive_lower_closes_at_252d_high_d1": {"inputs": ["high", "close"], "func": f06_cscr_217_consecutive_lower_closes_at_252d_high_d1},
    "f06_cscr_218_lower_close_streak_break_event_d1": {"inputs": ["close"], "func": f06_cscr_218_lower_close_streak_break_event_d1},
    "f06_cscr_219_doji_then_two_red_confirmation_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_219_doji_then_two_red_confirmation_d1},
    "f06_cscr_220_engulf_followed_by_lower_close_5d_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_220_engulf_followed_by_lower_close_5d_d1},
    "f06_cscr_221_tweezer_top_volume_confirmed_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_221_tweezer_top_volume_confirmed_d1},
    "f06_cscr_222_high_wave_after_strong_advance_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_222_high_wave_after_strong_advance_d1},
    "f06_cscr_223_long_legged_doji_at_atr_extreme_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_223_long_legged_doji_at_atr_extreme_d1},
    "f06_cscr_224_dragonfly_failure_within_3d_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_224_dragonfly_failure_within_3d_d1},
    "f06_cscr_225_marubozu_then_immediate_reversal_d1": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_225_marubozu_then_immediate_reversal_d1},
}
