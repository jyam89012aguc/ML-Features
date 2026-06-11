"""failed_breakout_dynamics d2 features 001-075 — Pipeline 1b-technical.

Bull-trap / false-break hypotheses. SEP OHLCV only. PIT-clean.
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

def f05_fbkd_001_false_break_count_21d_resistance_63d(high, close):
    """Count of false breaks of prior 21d high in trailing 63d:"""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    broke = (high > prior_max).astype(float)
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.rolling(QDAYS, min_periods=MDAYS).sum().where(broke.notna(), np.nan)

def f05_fbkd_002_false_break_count_63d_resistance_252d(high, close):
    """Count of false breaks of prior 63d high in trailing 252d"""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_003_false_break_count_252d_resistance_504d(high, close):
    """Count of false breaks of prior 252d high in trailing 504d"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_004_false_break_count_5d_resistance_21d(high, close):
    """Count of false breaks of prior 5d (weekly) high in traili"""
    prior_max = high.shift(1).rolling(WDAYS, min_periods=2).max()
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.rolling(MDAYS, min_periods=WDAYS).sum()

def f05_fbkd_005_false_break_count_504d_resistance_756d(high, close):
    """Count of false breaks of prior 504d (2y) high in trailing"""
    prior_max = high.shift(1).rolling(DDAYS_2Y, min_periods=YDAYS).max()
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.rolling(DDAYS_3Y, min_periods=YDAYS).sum()

def f05_fbkd_006_false_break_count_1260d_resistance_full(high, close):
    """Expanding count of false breaks of prior 1260d (5y) high"""
    prior_max = high.shift(1).rolling(DDAYS_5Y, min_periods=YDAYS).max()
    failed = ((close < prior_max) & (high > prior_max)).astype(float)
    return failed.expanding(min_periods=YDAYS).sum()

def f05_fbkd_007_false_break_count_alltime_high_expanding(high, close):
    """Expanding count of false breaks of expanding all-time hig"""
    prior_ath = high.shift(1).expanding(min_periods=QDAYS).max()
    failed = ((close < prior_ath) & (high > prior_ath)).astype(float)
    return failed.expanding(min_periods=QDAYS).sum()

def f05_fbkd_008_attempt_vs_success_ratio_21d_break_63d(high, close):
    """In trailing 63d: attempts (intraday break of prior 21d hi"""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    attempt = (high > prior_max).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    succ = (close > prior_max).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(attempt, succ)

def f05_fbkd_009_attempt_vs_success_ratio_252d_break_504d(high, close):
    """In trailing 504d: intraday 252d-break attempts / closes a"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    attempt = (high > prior_max).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    succ = (close > prior_max).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(attempt, succ)

def f05_fbkd_010_false_break_severity_atr_21d(high, low, close):
    """At false-break bars (pierce prior 21d high but close belo"""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    overshoot = _safe_div(high - prior_max, atr)
    is_fail = (high > prior_max) & (close < prior_max)
    return overshoot.where(is_fail, np.nan)

def f05_fbkd_011_false_break_severity_pct_252d(high, close):
    """At false-break bars (pierce prior 252d high but close bel"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    overshoot = _safe_div(high - prior_max, prior_max)
    is_fail = (high > prior_max) & (close < prior_max)
    return overshoot.where(is_fail, np.nan)

def f05_fbkd_012_false_break_close_below_depth_atr_63d(high, low, close):
    """At false-break bars of prior 63d high, how deep close fin"""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    depth_below = _safe_div(prior_max - close, atr)
    is_fail = (high > prior_max) & (close < prior_max)
    return depth_below.where(is_fail, np.nan)

def f05_fbkd_013_bars_above_prior_252d_high_before_fail(high, close):
    """Current streak length: consecutive bars where close has b"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    above = (close > prior_max).astype(float).values
    n = len(above)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(above[i]) or np.isnan(prior_max.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if above[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)

def f05_fbkd_014_bars_above_prior_63d_high_before_fail(high, close):
    """Consecutive bars close above prior 63d-high anchor — shor"""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    above = (close > prior_max).astype(float).values
    n = len(above)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(above[i]) or np.isnan(prior_max.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if above[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)

def f05_fbkd_015_time_to_fail_after_most_recent_252d_break(high, close):
    """For most recent intraday 252d break, days until close<level"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    brk = ((high > pm) & pm.notna()).values
    pv = pm.values; cv = close.values; n = len(cv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if not pm.notna().iat[i]:
            continue
        lo = max(0, i - w + 1); lb = -1
        for j in range(i, lo - 1, -1):
            if brk[j]:
                lb = j; break
        if lb < 0:
            continue
        lvl = pv[lb]
        for k in range(lb + 1, i + 1):
            if not np.isnan(cv[k]) and cv[k] < lvl:
                out[i] = float(k - lb); break
    return pd.Series(out, index=high.index)

def f05_fbkd_016_post_break_max_drawdown_63d_after_252d_break(high, low, close):
    """Max drawdown 63d post most recent 252d intraday break"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    brk = ((high > pm) & pm.notna()).values
    lv = low.values; cv = close.values; n = len(cv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if not pm.notna().iat[i]:
            continue
        lo = max(0, i - w + 1); lb = -1
        for j in range(i, lo - 1, -1):
            if brk[j]:
                lb = j; break
        if lb < 0:
            continue
        bc = cv[lb]
        if np.isnan(bc) or bc <= 0:
            continue
        up = min(min(n - 1, lb + QDAYS), i)
        if up <= lb:
            continue
        seg = lv[lb + 1:up + 1]; sv = seg[~np.isnan(seg)]
        if sv.size:
            out[i] = float(sv.min() / bc - 1.0)
    return pd.Series(out, index=high.index)

def f05_fbkd_017_repeat_fail_count_same_252d_level_504d(high, close):
    """Distinct failed-break episodes at same 252d level (504d)"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; n = len(pv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1); tgt = pv[i]; cnt = 0
        for j in range(lo, i + 1):
            if fail[j] and abs(pv[j] - tgt) <= 0.01 * tgt:
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)

def f05_fbkd_018_distinct_failed_levels_252d_horizon_504d(high, close):
    """Number of DISTINCT failed-break levels in 504d"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; n = len(pv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1)
        fails = sorted(pv[j] for j in range(lo, i + 1) if fail[j])
        if not fails:
            out[i] = 0.0; continue
        d = 1; last = fails[0]
        for v in fails[1:]:
            if v > last * 1.01:
                d += 1; last = v
        out[i] = float(d)
    return pd.Series(out, index=high.index)

def f05_fbkd_019_bars_since_last_252d_false_break(high, close):
    """Bars since the most recent failed break of prior 252d hig"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float).values
    n = len(fail)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if not np.isnan(fail[i]) and fail[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=high.index)

def f05_fbkd_020_post_fail_red_bar_count_5d(high, close):
    """In the 5 bars FOLLOWING each prior 252d-high failed-break"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    red = (close.diff() < 0).astype(float)
    fail_recent = fail.shift(1).rolling(WDAYS, min_periods=2).sum()
    red5 = red.rolling(WDAYS, min_periods=2).sum()
    return red5.where(fail_recent > 0, np.nan)

def f05_fbkd_021_post_fail_lower_high_count_10d(high, close):
    """Count of lower-highs (high < prior high) in 10 bars follo"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    lh = (high.diff() < 0).astype(float)
    fail_recent = fail.shift(1).rolling(10, min_periods=3).sum()
    lh10 = lh.rolling(10, min_periods=3).sum()
    return lh10.where(fail_recent > 0, np.nan)

def f05_fbkd_022_max_high_vs_close_at_252d_fail(high, close):
    """At 252d false-break bars: (high - close) / close — closin"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_fail = (high > prior_max) & (close < prior_max)
    weakness = _safe_div(high - close, close)
    return weakness.where(is_fail, np.nan)

def f05_fbkd_023_time_to_first_fail_after_new_252d_high(high, close):
    """Days from most recent close-break of 252d high to close<lvl"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    brk = ((close > pm) & pm.notna()).values
    pv = pm.values; cv = close.values; n = len(cv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1); lb = -1
        for j in range(i, lo - 1, -1):
            if brk[j]:
                lb = j; break
        if lb < 0:
            continue
        lvl = pv[lb]
        for k in range(lb + 1, i + 1):
            if not np.isnan(cv[k]) and cv[k] < lvl:
                out[i] = float(k - lb); break
    return pd.Series(out, index=high.index)

def f05_fbkd_024_dwell_above_252d_pre_break_post_fail_ratio(high, close):
    """Pre-fail dwell-above vs 5d post-fail dwell-below"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; cv = close.values; n = len(cv)
    out = np.full(n, np.nan); w = DDAYS_2Y
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1); lf = -1
        for j in range(i, lo - 1, -1):
            if fail[j]:
                lf = j; break
        if lf < 0:
            continue
        lvl = pv[lf]; above = 0
        for k in range(lf - 1, max(-1, lf - 22), -1):
            if not np.isnan(cv[k]) and cv[k] > lvl:
                above += 1
            else:
                break
        up = min(min(n - 1, lf + WDAYS), i); below = 0
        for k in range(lf + 1, up + 1):
            if not np.isnan(cv[k]) and cv[k] < lvl:
                below += 1
        out[i] = float(above) / float(below) if below > 0 else np.nan
    return pd.Series(out, index=high.index)

def f05_fbkd_025_failed_break_prior_year_high_ytd(high, close):
    """YTD count of bars where high pierces prior-calendar-year"""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    yr_max_map = high.groupby(year_id).max()
    unique_yrs = year_id.drop_duplicates().tolist()
    prior_map = {y: (unique_yrs[i - 1] if i > 0 else np.nan) for i, y in enumerate(unique_yrs)}
    prior_y = year_id.map(prior_map)
    prior_y_max = prior_y.map(yr_max_map)
    fail = ((high > prior_y_max) & (close < prior_y_max)).astype(float)
    return fail.groupby(year_id).cumsum()

def f05_fbkd_026_failed_break_prior_quarter_high_qtd(high, close):
    """QTD count of failed breaks of prior-calendar-quarter high"""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    q_id = pd.Series(high.index.to_period("Q").astype(str), index=high.index)
    qmax = high.groupby(q_id).max()
    uniqs = q_id.drop_duplicates().tolist()
    prior_map = {q: (uniqs[i - 1] if i > 0 else np.nan) for i, q in enumerate(uniqs)}
    prior_q = q_id.map(prior_map)
    prior_q_max = prior_q.map(qmax)
    fail = ((high > prior_q_max) & (close < prior_q_max)).astype(float)
    return fail.groupby(q_id).cumsum()

def f05_fbkd_027_failed_break_prior_month_high_mtd(high, close):
    """MTD count of failed breaks of prior-calendar-month high"""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    m_id = pd.Series(high.index.to_period("M").astype(str), index=high.index)
    mmax = high.groupby(m_id).max()
    uniqs = m_id.drop_duplicates().tolist()
    prior_map = {m: (uniqs[i - 1] if i > 0 else np.nan) for i, m in enumerate(uniqs)}
    prior_m = m_id.map(prior_map)
    prior_m_max = prior_m.map(mmax)
    fail = ((high > prior_m_max) & (close < prior_m_max)).astype(float)
    return fail.groupby(m_id).cumsum()

def f05_fbkd_028_failed_break_round_number_10dollar_252d(high, close):
    """252d count of bars where high pierces nearest $10 round n"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 10.0) * 10.0)
    target = target.where(target > prev_c, target + 10.0)
    fail = ((high > target) & (close < target)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_029_failed_break_round_number_25dollar_252d(high, close):
    """252d count of failed breaks of nearest $25 round number a"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 25.0) * 25.0)
    target = target.where(target > prev_c, target + 25.0)
    fail = ((high > target) & (close < target)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_030_failed_break_round_number_50dollar_252d(high, close):
    """252d count of failed breaks of nearest $50 round number —"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 50.0) * 50.0)
    target = target.where(target > prev_c, target + 50.0)
    fail = ((high > target) & (close < target)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_031_failed_break_round_number_100dollar_504d(high, close):
    """504d count of failed breaks of $100 century mark — extrem"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 100.0) * 100.0)
    target = target.where(target > prev_c, target + 100.0)
    fail = ((high > target) & (close < target)).astype(float)
    return fail.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_032_failed_break_2y_high_504d(high, close):
    """504d count of failed breaks of prior 2y high anchor — bie"""
    prior_max = high.shift(1).rolling(DDAYS_2Y, min_periods=YDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    return fail.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_033_failed_break_5y_high_756d(high, close):
    """756d count of failed breaks of prior 5y high anchor — sec"""
    prior_max = high.shift(1).rolling(DDAYS_5Y, min_periods=YDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    return fail.rolling(DDAYS_3Y, min_periods=YDAYS).sum()

def f05_fbkd_034_failed_break_consolidation_top_63d(high, low, close):
    """Failed break of a 63d narrow-range consolidation top (top"""
    rmax = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    atr = _atr(high, low, close, n=MDAYS)
    tightness = _safe_div(rmax - rmin, atr)
    in_tight = (tightness < 4.0)
    fail = ((high > rmax) & (close < rmax) & in_tight).astype(float)
    return fail.where(rmax.notna(), np.nan)

def f05_fbkd_035_failed_break_pivot_r1_classical(high, low, close):
    """Indicator: today's high pierces classical pivot R1 = 2*P"""
    ph = high.shift(1); pl = low.shift(1); pc = close.shift(1)
    P = (ph + pl + pc) / 3.0
    R1 = 2.0 * P - pl
    fail = ((high > R1) & (close < R1)).astype(float)
    return fail.where(R1.notna(), np.nan)

def f05_fbkd_036_failed_break_pivot_r2_classical(high, low, close):
    """Indicator: today's high pierces classical pivot R2 = P +"""
    ph = high.shift(1); pl = low.shift(1); pc = close.shift(1)
    P = (ph + pl + pc) / 3.0
    R2 = P + (ph - pl)
    fail = ((high > R2) & (close < R2)).astype(float)
    return fail.where(R2.notna(), np.nan)

def f05_fbkd_037_failed_break_double_top_neckline_proxy_63d(high, low, close):
    """Double-top neckline failure proxy in 63d window"""
    hv = high.values; cv = close.values; n = len(hv)
    out = np.full(n, np.nan); w = QDAYS
    for i in range(w - 1, n):
        seg = hv[i - w + 1:i]; sv = seg[~np.isnan(seg)]
        if sv.size < 10:
            continue
        sd = np.sort(sv)[::-1]; p1 = sd[0]; p2 = np.nan
        for v in sd[1:]:
            if abs(v - p1) <= 0.015 * p1:
                p2 = v; break
        if np.isnan(p2):
            out[i] = 0.0; continue
        lvl = max(p1, p2)
        out[i] = 1.0 if (not np.isnan(hv[i]) and not np.isnan(cv[i]) and hv[i] > lvl and cv[i] < lvl) else 0.0
    return pd.Series(out, index=high.index)

def f05_fbkd_038_failed_break_donchian_upper_20d(high, close):
    """Failed break of Donchian 20-day upper channel (Turtle set"""
    upper = high.shift(1).rolling(20, min_periods=10).max()
    fail = ((high > upper) & (close < upper)).astype(float)
    return fail.where(upper.notna(), np.nan)

def f05_fbkd_039_gap_up_at_new_252d_high_then_filled_252d(open_, high, low, close):
    """Count in trailing 252d of gap-up bars (open > prior_high)"""
    prev_h = high.shift(1)
    prev_c = close.shift(1)
    prev_252_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    gap_up = open_ > prev_h
    new_high = high > prev_252_max
    filled = low <= prev_c
    event = (gap_up & new_high & filled).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_040_gap_up_at_new_high_close_bottom_third_252d(open_, high, low, close):
    """Count in 252d of gap-up bars at new 252d-high that close"""
    prev_h = high.shift(1)
    prev_252_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    gap_up = open_ > prev_h
    new_high = high > prev_252_max
    pos = _safe_div(close - low, high - low)
    bottom_third = pos <= (1.0 / 3.0)
    event = (gap_up & new_high & bottom_third).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_041_breakaway_gap_failure_time_to_fill_63d(open_, high, low, close):
    """Days until most recent breakaway gap was filled"""
    ph = high.shift(1); pc = close.shift(1)
    p63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    gap = ((open_ > ph) & (open_ > p63) & p63.notna()).values
    pcv = pc.values; lv = low.values; n = len(lv)
    out = np.full(n, np.nan); w = YDAYS
    for i in range(n):
        if not p63.notna().iat[i]:
            continue
        lo = max(0, i - w + 1); lg = -1
        for j in range(i, lo - 1, -1):
            if gap[j]:
                lg = j; break
        if lg < 0:
            continue
        gf = pcv[lg]
        if np.isnan(gf):
            continue
        for k in range(lg + 1, i + 1):
            if not np.isnan(lv[k]) and lv[k] <= gf:
                out[i] = float(k - lg); break
    return pd.Series(out, index=high.index)

def f05_fbkd_042_post_breakaway_gap_max_dd_21d(open_, high, low, close):
    """Max DD 21d after most recent breakaway gap"""
    ph = high.shift(1)
    p63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    gap = ((open_ > ph) & (open_ > p63) & p63.notna()).values
    ov = open_.values; lv = low.values; n = len(lv)
    out = np.full(n, np.nan); w = YDAYS
    for i in range(n):
        if not p63.notna().iat[i]:
            continue
        lo = max(0, i - w + 1); lg = -1
        for j in range(i, lo - 1, -1):
            if gap[j]:
                lg = j; break
        if lg < 0:
            continue
        b = ov[lg]
        if np.isnan(b) or b <= 0:
            continue
        up = min(min(n - 1, lg + MDAYS), i)
        if up <= lg:
            continue
        seg = lv[lg + 1:up + 1]; sv = seg[~np.isnan(seg)]
        if sv.size == 0:
            continue
        out[i] = float(sv.min() / b - 1.0)
    return pd.Series(out, index=high.index)

def f05_fbkd_043_low_volume_gap_up_new_high_252d(open_, high, close, volume):
    """Count in 252d of gap-up bars at new 252d-high WHERE volum"""
    prev_h = high.shift(1)
    prev_252_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    gap_up = open_ > prev_h
    new_high = high > prev_252_max
    low_vol = volume < v21
    event = (gap_up & new_high & low_vol).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_044_runaway_gap_failure_504d(open_, high, low, close):
    """Count in 504d of 'runaway' (mid-trend) gap failures: gap-"""
    sma50 = close.rolling(50, min_periods=20).mean()
    sma200 = close.rolling(200, min_periods=63).mean()
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    in_trend = (close > sma50) & (sma50 > sma200)
    red = close < open_
    event = (gap_up & in_trend & red).astype(float)
    return event.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_045_exhaustion_gap_island_top_252d(open_, high, low):
    """Count in 252d of island-top setups: a bar with both a gap"""
    prev_h = high.shift(1)
    next_o = open_.shift(-0)  # placeholder; we cannot use future. Instead use today's open vs next bar - so use PIT logic.
    gap_up_prev = open_.shift(0) > high.shift(1)  # gap-up at today
    gap_down_today = open_ < low.shift(1)
    gap_up_prior_bar = (open_.shift(1) > high.shift(2)).fillna(False)
    event = (gap_up_prior_bar & gap_down_today).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_046_post_gap_up_close_below_open_count_63d(open_, high, close):
    """In trailing 63d: count of gap-up bars (open > prior_high)"""
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    red = close < open_
    event = (gap_up & red).astype(float)
    return event.rolling(QDAYS, min_periods=MDAYS).sum()

def f05_fbkd_047_avg_gap_severity_failed_gaps_252d(open_, high, close):
    """For failed gap-ups (gap_up & close < open) in trailing 25"""
    prev_h = high.shift(1)
    prev_c = close.shift(1)
    gap_up = open_ > prev_h
    red = close < open_
    gap_sz = _safe_div(open_ - prev_c, prev_c)
    failed_sz = gap_sz.where(gap_up & red, np.nan)
    return failed_sz.rolling(YDAYS, min_periods=QDAYS).mean()

def f05_fbkd_048_gap_fill_rate_within_5d_252d(open_, high, low, close):
    """Fraction of all gap-up events in trailing 252d that got f"""
    prev_h = high.shift(1)
    prev_c = close.shift(1)
    gap_up = (open_ > prev_h).astype(float)
    low_min_5 = low.rolling(WDAYS, min_periods=2).min()
    gap_floor = prev_c.shift(4)
    filled = (low_min_5 <= gap_floor).astype(float).where(gap_up.shift(4) > 0, np.nan)
    gap_evts = gap_up.shift(4).rolling(YDAYS, min_periods=QDAYS).sum()
    fill_cnt = filled.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fill_cnt, gap_evts)

def f05_fbkd_049_close_below_gap_open_within_3d_count_252d(open_, high, close):
    """In trailing 252d, count of gap-up bars that had a CLOSE b"""
    prev_h = high.shift(1)
    gap_up = (open_ > prev_h).astype(float)
    gap_open = open_.where(gap_up > 0, np.nan)
    fail_indicator = pd.Series(np.nan, index=open_.index)
    for k in range(0, 4):
        c_k = close.shift(k) if k > 0 else close
    gap_open_lag3 = gap_up.shift(3)
    open_lag3 = open_.where(gap_up > 0, np.nan).shift(3)
    close_min_4 = close.rolling(4, min_periods=2).min()
    fail = (close_min_4 < open_lag3).astype(float).where(gap_open_lag3 > 0, np.nan)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_050_gap_up_at_252d_high_followed_by_red_close_63d(open_, high, close):
    """Count in 63d of bars where: gap up AND new 252d-high AND"""
    prev_h = high.shift(1)
    prev_252_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    gap_up = open_ > prev_h
    new_high = high > prev_252_max
    red = close < open_
    event = (gap_up & new_high & red).astype(float)
    return event.rolling(QDAYS, min_periods=MDAYS).sum()

def f05_fbkd_051_gap_size_zscore_failed_252d(open_, high, close):
    """Z-score (over 252d) of failed-gap sizes — extreme failed-"""
    prev_h = high.shift(1)
    prev_c = close.shift(1)
    gap_up = open_ > prev_h
    red = close < open_
    gap_sz = _safe_div(open_ - prev_c, prev_c)
    failed_sz = gap_sz.where(gap_up & red, np.nan)
    return _rolling_zscore(failed_sz, YDAYS, min_periods=QDAYS)

def f05_fbkd_052_consecutive_failed_gap_ups_streak(open_, high, close):
    """Current streak: consecutive gap-up events that ended red"""
    prev_h = high.shift(1)
    gap_up = (open_ > prev_h)
    red = (close < open_)
    failed = (gap_up & red).astype(float).values
    successful_gap = (gap_up & ~red).astype(float).values
    n = len(failed)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(failed[i]):
            streak = 0
            out[i] = np.nan
        else:
            if failed[i] > 0:
                streak += 1
            elif successful_gap[i] > 0:
                streak = 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)

def f05_fbkd_053_close_back_below_broken_252d_within_3d(high, close):
    """Indicator: a successful close>prior-252d-high event was f"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    succ_break_3d_ago = ((close.shift(3) > prior_max.shift(3))).astype(float)
    lvl_3d_ago = prior_max.shift(3)
    cmin3 = close.rolling(3, min_periods=2).min()
    failed = (cmin3 < lvl_3d_ago).astype(float)
    return failed.where(succ_break_3d_ago > 0, np.nan)

def f05_fbkd_054_close_back_below_broken_252d_within_5d(high, close):
    """Same as 053 but 5-day window — distinct trap horizon"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    succ_break_5d_ago = ((close.shift(5) > prior_max.shift(5))).astype(float)
    lvl_5d_ago = prior_max.shift(5)
    cmin5 = close.rolling(5, min_periods=2).min()
    failed = (cmin5 < lvl_5d_ago).astype(float)
    return failed.where(succ_break_5d_ago > 0, np.nan)

def f05_fbkd_055_close_back_below_broken_252d_within_10d(high, close):
    """Same but 10-day window — slower failure horizon"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    succ_break_ago = ((close.shift(10) > prior_max.shift(10))).astype(float)
    lvl_ago = prior_max.shift(10)
    cmin = close.rolling(10, min_periods=3).min()
    failed = (cmin < lvl_ago).astype(float)
    return failed.where(succ_break_ago > 0, np.nan)

def f05_fbkd_056_post_break_vol_decay_5d_vs_break_vol(high, close, volume):
    """For the most recent 252d successful break (close>prior 25"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_p = prior_max.values
    arr_v = volume.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = QDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        last_brk = -1
        for j in range(i, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_brk = j
                break
        if last_brk < 0:
            continue
        bv = arr_v[last_brk]
        if np.isnan(bv) or bv <= 0:
            continue
        upper = min(n - 1, last_brk + WDAYS)
        upper = min(upper, i)
        if upper <= last_brk:
            continue
        seg = arr_v[last_brk + 1:upper + 1]
        seg_v = seg[~np.isnan(seg)]
        if seg_v.size == 0:
            continue
        out[i] = float(seg_v.mean() / bv)
    return pd.Series(out, index=high.index)

def f05_fbkd_057_post_break_lower_high_within_5d_indicator(high, close):
    """For most recent 252d-break in trailing 21d, indicator tha"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_p = prior_max.values
    arr_h = high.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = MDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        last_brk = -1
        for j in range(i, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_brk = j
                break
        if last_brk < 0:
            continue
        bh = arr_h[last_brk]
        if np.isnan(bh):
            continue
        upper = min(n - 1, last_brk + WDAYS)
        upper = min(upper, i)
        if upper <= last_brk:
            continue
        seg = arr_h[last_brk + 1:upper + 1]
        seg_v = seg[~np.isnan(seg)]
        if seg_v.size == 0:
            continue
        out[i] = 1.0 if seg_v.max() < bh else 0.0
    return pd.Series(out, index=high.index)

def f05_fbkd_058_bull_trap_dwell_below_after_fail_252d(high, close):
    """For most recent 252d failed-break in trailing 252d, curre"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        last_fail = -1
        for j in range(i, lo - 1, -1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                last_fail = j
                break
        if last_fail < 0:
            continue
        lvl = arr_p[last_fail]
        cnt = 0
        for k in range(last_fail, i + 1):
            if not np.isnan(arr_c[k]) and arr_c[k] < lvl:
                cnt += 1
            else:
                cnt = 0
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)

def f05_fbkd_059_post_fail_volume_surge_5d_252d(high, close, volume):
    """In trailing 252d, count of 252d-fail events whose subsequ"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    arr_v = volume.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    is_fail = ((high > prior_max) & (close < prior_max)).astype(float).values
    surge_evt = np.zeros(n, dtype=float)
    surge_evt[:] = np.nan
    for i in range(n):
        if is_fail[i] > 0:
            bv = arr_v[i]
            if np.isnan(bv) or bv <= 0:
                surge_evt[i] = 0.0
                continue
            upper = min(n - 1, i + WDAYS)
            if upper <= i:
                surge_evt[i] = 0.0
                continue
            seg = arr_v[i + 1:upper + 1]
            seg_v = seg[~np.isnan(seg)]
            if seg_v.size == 0:
                surge_evt[i] = 0.0
                continue
            surge_evt[i] = 1.0 if seg_v.mean() > 1.5 * bv else 0.0
        else:
            surge_evt[i] = 0.0
    surge_lag = pd.Series(surge_evt, index=high.index).shift(WDAYS)
    return surge_lag.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_060_max_post_break_drawdown_pct_21d_252d(high, low, close):
    """For the most recent 252d successful close-break in traili"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_l = low.values
    arr_p = prior_max.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        last_brk = -1
        for j in range(i, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_brk = j
                break
        if last_brk < 0:
            continue
        bc = arr_c[last_brk]
        if np.isnan(bc) or bc <= 0:
            continue
        upper = min(n - 1, last_brk + MDAYS)
        upper = min(upper, i)
        if upper <= last_brk:
            continue
        seg = arr_l[last_brk + 1:upper + 1]
        seg_v = seg[~np.isnan(seg)]
        if seg_v.size == 0:
            continue
        out[i] = float(seg_v.min() / bc - 1.0)
    return pd.Series(out, index=high.index)

def f05_fbkd_061_failed_breakout_to_lower_low_within_10d(high, low, close):
    """Indicator at bar i: a 252d failed-break occurred at bar i"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    pre_low = low.rolling(MDAYS, min_periods=WDAYS).min()
    fail_10ago = ((high.shift(10) > prior_max.shift(10)) & (close.shift(10) < prior_max.shift(10))).astype(float)
    pre_low_10ago = pre_low.shift(10)
    cur_low_min_10 = low.rolling(10, min_periods=3).min()
    lower_low = (cur_low_min_10 < pre_low_10ago).astype(float)
    return lower_low.where(fail_10ago > 0, np.nan)

def f05_fbkd_062_post_fail_red_volume_dominance_5d(high, close, volume):
    """For 252d failed-break events, share of next-5d volume on"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_fail = ((high > prior_max) & (close < prior_max)).astype(float)
    red = (close.diff() < 0).astype(float)
    red_vol = volume * red
    red_vol_5 = red_vol.rolling(WDAYS, min_periods=2).sum()
    tot_vol_5 = volume.rolling(WDAYS, min_periods=2).sum()
    share = _safe_div(red_vol_5, tot_vol_5)
    return share.where(is_fail.shift(WDAYS) > 0, np.nan)

def f05_fbkd_063_failed_break_close_in_lower_third_of_bar(high, low, close):
    """At 252d failed-break bars: indicator that close is in the"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    pos = _safe_div(close - low, high - low)
    is_fail = (high > prior_max) & (close < prior_max)
    return (pos <= 1.0 / 3.0).astype(float).where(is_fail & pos.notna(), np.nan)

def f05_fbkd_064_failed_break_with_upper_wick_atr_ratio(high, low, close, open_):
    """At 252d failed-break bars: upper-wick = high - max(open,c"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    wick = high - body_top
    atr = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(wick, atr)
    is_fail = (high > prior_max) & (close < prior_max)
    return ratio.where(is_fail, np.nan)

def f05_fbkd_065_consecutive_failed_breaks_streak_21d(high, close):
    """Count of failed 21d-high breaks in trailing 21 bars — clu"""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    return fail.rolling(MDAYS, min_periods=WDAYS).sum()

def f05_fbkd_066_failed_retest_count_252d_504d(high, low, close):
    """Count in trailing 504d of failed RETESTS: after a 252d-fa"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_l = low.values
    arr_c = close.values
    arr_p = prior_max.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win_back = DDAYS_2Y
    fail_lookback = QDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_h[i]):
            continue
        lo = max(0, i - win_back + 1)
        cnt = 0
        for k in range(lo, i + 1):
            if np.isnan(arr_h[k]) or np.isnan(arr_c[k]):
                continue
            kk_lo = max(0, k - fail_lookback)
            for j in range(k - 1, kk_lo - 1, -1):
                if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                        and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                    lvl = arr_p[j]
                    if abs(arr_h[k] - lvl) <= 0.01 * lvl and arr_c[k] < lvl:
                        cnt += 1
                        break
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)

def f05_fbkd_067_failed_retest_severity_atr_252d(high, low, close):
    """At failed-retest bars (defined as in 066), magnitude (bro"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    arr_atr = atr.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    fail_lookback = QDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_h[i]) or np.isnan(arr_c[i]) or np.isnan(arr_atr[i]) or arr_atr[i] <= 0:
            continue
        kk_lo = max(0, i - fail_lookback)
        for j in range(i - 1, kk_lo - 1, -1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                lvl = arr_p[j]
                if abs(arr_h[i] - lvl) <= 0.01 * lvl and arr_c[i] < lvl:
                    out[i] = float((lvl - arr_c[i]) / arr_atr[i])
                    break
    return pd.Series(out, index=high.index)

def f05_fbkd_068_distance_to_nearest_failed_break_level_atr(high, low, close):
    """Distance of today's close BELOW the nearest failed-break"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    arr_c = close.values
    arr_p = prior_max.values
    arr_h = high.values
    arr_atr = atr.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    lb = QDAYS
    for i in range(n):
        if np.isnan(arr_c[i]) or np.isnan(arr_atr[i]) or arr_atr[i] <= 0:
            continue
        kk_lo = max(0, i - lb)
        nearest = np.inf
        for j in range(i - 1, kk_lo - 1, -1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                lvl = arr_p[j]
                if lvl > arr_c[i]:
                    dist = (lvl - arr_c[i]) / arr_atr[i]
                    if dist < nearest:
                        nearest = dist
        if np.isfinite(nearest):
            out[i] = nearest
    return pd.Series(out, index=high.index)

def f05_fbkd_069_failed_break_then_failed_retest_within_21d(high, close):
    """Indicator at bar i: in trailing 21d, occurred BOTH a 252d"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = MDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        found = False
        for j in range(lo, i + 1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                lvl = arr_p[j]
                for k in range(j + 1, i + 1):
                    if (not np.isnan(arr_h[k]) and not np.isnan(arr_c[k])
                            and abs(arr_h[k] - lvl) <= 0.01 * lvl and arr_c[k] < lvl):
                        found = True
                        break
            if found:
                break
        out[i] = 1.0 if found else 0.0
    return pd.Series(out, index=high.index)

def f05_fbkd_070_volume_on_failed_retest_vs_initial_fail(high, close, volume):
    """At a failed-retest bar (within 63d of a fail event at sam"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    arr_v = volume.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    lb = QDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_h[i]) or np.isnan(arr_c[i]):
            continue
        kk_lo = max(0, i - lb)
        for j in range(i - 1, kk_lo - 1, -1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                lvl = arr_p[j]
                if abs(arr_h[i] - lvl) <= 0.01 * lvl and arr_c[i] < lvl:
                    iv = arr_v[j]
                    rv = arr_v[i]
                    if not np.isnan(iv) and iv > 0 and not np.isnan(rv):
                        out[i] = float(rv / iv)
                    break
    return pd.Series(out, index=high.index)

def f05_fbkd_071_failed_retest_count_63d_window(high, close):
    """Count of failed retests in trailing 63d — short-window re"""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = QDAYS
    fail_lb = MDAYS
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        cnt = 0
        for k in range(lo, i + 1):
            if np.isnan(arr_h[k]) or np.isnan(arr_c[k]):
                continue
            kk_lo = max(0, k - fail_lb)
            for j in range(k - 1, kk_lo - 1, -1):
                if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                        and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                    lvl = arr_p[j]
                    if abs(arr_h[k] - lvl) <= 0.01 * lvl and arr_c[k] < lvl:
                        cnt += 1
                        break
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)

def f05_fbkd_072_bars_since_last_failed_retest(high, close):
    """Bars since the most recent failed retest of a recent fail"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = prior_max.values
    n = len(arr_c)
    last_evt = -1
    out = np.full(n, np.nan, dtype=float)
    fail_lb = QDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_h[i]) or np.isnan(arr_c[i]):
            if last_evt >= 0:
                out[i] = float(i - last_evt)
            continue
        kk_lo = max(0, i - fail_lb)
        for j in range(i - 1, kk_lo - 1, -1):
            if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                    and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]):
                lvl = arr_p[j]
                if abs(arr_h[i] - lvl) <= 0.01 * lvl and arr_c[i] < lvl:
                    last_evt = i
                    break
        if last_evt >= 0:
            out[i] = float(i - last_evt)
    return pd.Series(out, index=high.index)

def f05_fbkd_073_composite_false_break_severity_score(open_, high, low, close, volume):
    """At 252d failed-break bars: composite severity = zscore(in"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    overshoot = _safe_div(high - prior_max, atr)
    depth = _safe_div(prior_max - close, atr)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    wick = _safe_div(high - body_top, atr)
    vol21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vratio = _safe_div(volume, vol21)
    z_os = _rolling_zscore(overshoot, YDAYS)
    z_dp = _rolling_zscore(depth, YDAYS)
    z_wk = _rolling_zscore(wick, YDAYS)
    z_vr = _rolling_zscore(vratio, YDAYS)
    score = z_os.fillna(0) + z_dp.fillna(0) + z_wk.fillna(0) + z_vr.fillna(0)
    is_fail = (high > prior_max) & (close < prior_max)
    return score.where(is_fail, np.nan)

def f05_fbkd_074_weighted_false_break_count_63d_decay(high, close):
    """Exponentially-decay-weighted count of 252d false-break ev"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    decay = np.exp(-np.log(2.0) * np.arange(QDAYS) / float(MDAYS))[::-1]
    def _wt_sum(w):
        if np.isnan(w).all():
            return np.nan
        ww = np.where(np.isnan(w), 0.0, w)
        return float((ww * decay[-len(ww):]).sum())
    return fail.rolling(QDAYS, min_periods=MDAYS).apply(_wt_sum, raw=True)

def f05_fbkd_075_multi_horizon_false_break_breadth_count(high, close):
    """Today's bar is a false-break at HOW MANY of {5d, 21d, 63d"""
    horizons = [(WDAYS, 2), (MDAYS, WDAYS), (QDAYS, MDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS)]
    pieces = []
    for hz, mp in horizons:
        pm = high.shift(1).rolling(hz, min_periods=mp).max()
        fail = ((high > pm) & (close < pm)).astype(float)
        pieces.append(fail.rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return df.sum(axis=1)



def f05_fbkd_001_false_break_count_21d_resistance_63d_d2(high, close):
    return f05_fbkd_001_false_break_count_21d_resistance_63d(high, close).diff().diff()


def f05_fbkd_002_false_break_count_63d_resistance_252d_d2(high, close):
    return f05_fbkd_002_false_break_count_63d_resistance_252d(high, close).diff().diff()


def f05_fbkd_003_false_break_count_252d_resistance_504d_d2(high, close):
    return f05_fbkd_003_false_break_count_252d_resistance_504d(high, close).diff().diff()


def f05_fbkd_004_false_break_count_5d_resistance_21d_d2(high, close):
    return f05_fbkd_004_false_break_count_5d_resistance_21d(high, close).diff().diff()


def f05_fbkd_005_false_break_count_504d_resistance_756d_d2(high, close):
    return f05_fbkd_005_false_break_count_504d_resistance_756d(high, close).diff().diff()


def f05_fbkd_006_false_break_count_1260d_resistance_full_d2(high, close):
    return f05_fbkd_006_false_break_count_1260d_resistance_full(high, close).diff().diff()


def f05_fbkd_007_false_break_count_alltime_high_expanding_d2(high, close):
    return f05_fbkd_007_false_break_count_alltime_high_expanding(high, close).diff().diff()


def f05_fbkd_008_attempt_vs_success_ratio_21d_break_63d_d2(high, close):
    return f05_fbkd_008_attempt_vs_success_ratio_21d_break_63d(high, close).diff().diff()


def f05_fbkd_009_attempt_vs_success_ratio_252d_break_504d_d2(high, close):
    return f05_fbkd_009_attempt_vs_success_ratio_252d_break_504d(high, close).diff().diff()


def f05_fbkd_010_false_break_severity_atr_21d_d2(high, low, close):
    return f05_fbkd_010_false_break_severity_atr_21d(high, low, close).diff().diff()


def f05_fbkd_011_false_break_severity_pct_252d_d2(high, close):
    return f05_fbkd_011_false_break_severity_pct_252d(high, close).diff().diff()


def f05_fbkd_012_false_break_close_below_depth_atr_63d_d2(high, low, close):
    return f05_fbkd_012_false_break_close_below_depth_atr_63d(high, low, close).diff().diff()


def f05_fbkd_013_bars_above_prior_252d_high_before_fail_d2(high, close):
    return f05_fbkd_013_bars_above_prior_252d_high_before_fail(high, close).diff().diff()


def f05_fbkd_014_bars_above_prior_63d_high_before_fail_d2(high, close):
    return f05_fbkd_014_bars_above_prior_63d_high_before_fail(high, close).diff().diff()


def f05_fbkd_015_time_to_fail_after_most_recent_252d_break_d2(high, close):
    return f05_fbkd_015_time_to_fail_after_most_recent_252d_break(high, close).diff().diff()


def f05_fbkd_016_post_break_max_drawdown_63d_after_252d_break_d2(high, low, close):
    return f05_fbkd_016_post_break_max_drawdown_63d_after_252d_break(high, low, close).diff().diff()


def f05_fbkd_017_repeat_fail_count_same_252d_level_504d_d2(high, close):
    return f05_fbkd_017_repeat_fail_count_same_252d_level_504d(high, close).diff().diff()


def f05_fbkd_018_distinct_failed_levels_252d_horizon_504d_d2(high, close):
    return f05_fbkd_018_distinct_failed_levels_252d_horizon_504d(high, close).diff().diff()


def f05_fbkd_019_bars_since_last_252d_false_break_d2(high, close):
    return f05_fbkd_019_bars_since_last_252d_false_break(high, close).diff().diff()


def f05_fbkd_020_post_fail_red_bar_count_5d_d2(high, close):
    return f05_fbkd_020_post_fail_red_bar_count_5d(high, close).diff().diff()


def f05_fbkd_021_post_fail_lower_high_count_10d_d2(high, close):
    return f05_fbkd_021_post_fail_lower_high_count_10d(high, close).diff().diff()


def f05_fbkd_022_max_high_vs_close_at_252d_fail_d2(high, close):
    return f05_fbkd_022_max_high_vs_close_at_252d_fail(high, close).diff().diff()


def f05_fbkd_023_time_to_first_fail_after_new_252d_high_d2(high, close):
    return f05_fbkd_023_time_to_first_fail_after_new_252d_high(high, close).diff().diff()


def f05_fbkd_024_dwell_above_252d_pre_break_post_fail_ratio_d2(high, close):
    return f05_fbkd_024_dwell_above_252d_pre_break_post_fail_ratio(high, close).diff().diff()


def f05_fbkd_025_failed_break_prior_year_high_ytd_d2(high, close):
    return f05_fbkd_025_failed_break_prior_year_high_ytd(high, close).diff().diff()


def f05_fbkd_026_failed_break_prior_quarter_high_qtd_d2(high, close):
    return f05_fbkd_026_failed_break_prior_quarter_high_qtd(high, close).diff().diff()


def f05_fbkd_027_failed_break_prior_month_high_mtd_d2(high, close):
    return f05_fbkd_027_failed_break_prior_month_high_mtd(high, close).diff().diff()


def f05_fbkd_028_failed_break_round_number_10dollar_252d_d2(high, close):
    return f05_fbkd_028_failed_break_round_number_10dollar_252d(high, close).diff().diff()


def f05_fbkd_029_failed_break_round_number_25dollar_252d_d2(high, close):
    return f05_fbkd_029_failed_break_round_number_25dollar_252d(high, close).diff().diff()


def f05_fbkd_030_failed_break_round_number_50dollar_252d_d2(high, close):
    return f05_fbkd_030_failed_break_round_number_50dollar_252d(high, close).diff().diff()


def f05_fbkd_031_failed_break_round_number_100dollar_504d_d2(high, close):
    return f05_fbkd_031_failed_break_round_number_100dollar_504d(high, close).diff().diff()


def f05_fbkd_032_failed_break_2y_high_504d_d2(high, close):
    return f05_fbkd_032_failed_break_2y_high_504d(high, close).diff().diff()


def f05_fbkd_033_failed_break_5y_high_756d_d2(high, close):
    return f05_fbkd_033_failed_break_5y_high_756d(high, close).diff().diff()


def f05_fbkd_034_failed_break_consolidation_top_63d_d2(high, low, close):
    return f05_fbkd_034_failed_break_consolidation_top_63d(high, low, close).diff().diff()


def f05_fbkd_035_failed_break_pivot_r1_classical_d2(high, low, close):
    return f05_fbkd_035_failed_break_pivot_r1_classical(high, low, close).diff().diff()


def f05_fbkd_036_failed_break_pivot_r2_classical_d2(high, low, close):
    return f05_fbkd_036_failed_break_pivot_r2_classical(high, low, close).diff().diff()


def f05_fbkd_037_failed_break_double_top_neckline_proxy_63d_d2(high, low, close):
    return f05_fbkd_037_failed_break_double_top_neckline_proxy_63d(high, low, close).diff().diff()


def f05_fbkd_038_failed_break_donchian_upper_20d_d2(high, close):
    return f05_fbkd_038_failed_break_donchian_upper_20d(high, close).diff().diff()


def f05_fbkd_039_gap_up_at_new_252d_high_then_filled_252d_d2(open_, high, low, close):
    return f05_fbkd_039_gap_up_at_new_252d_high_then_filled_252d(open_, high, low, close).diff().diff()


def f05_fbkd_040_gap_up_at_new_high_close_bottom_third_252d_d2(open_, high, low, close):
    return f05_fbkd_040_gap_up_at_new_high_close_bottom_third_252d(open_, high, low, close).diff().diff()


def f05_fbkd_041_breakaway_gap_failure_time_to_fill_63d_d2(open_, high, low, close):
    return f05_fbkd_041_breakaway_gap_failure_time_to_fill_63d(open_, high, low, close).diff().diff()


def f05_fbkd_042_post_breakaway_gap_max_dd_21d_d2(open_, high, low, close):
    return f05_fbkd_042_post_breakaway_gap_max_dd_21d(open_, high, low, close).diff().diff()


def f05_fbkd_043_low_volume_gap_up_new_high_252d_d2(open_, high, close, volume):
    return f05_fbkd_043_low_volume_gap_up_new_high_252d(open_, high, close, volume).diff().diff()


def f05_fbkd_044_runaway_gap_failure_504d_d2(open_, high, low, close):
    return f05_fbkd_044_runaway_gap_failure_504d(open_, high, low, close).diff().diff()


def f05_fbkd_045_exhaustion_gap_island_top_252d_d2(open_, high, low):
    return f05_fbkd_045_exhaustion_gap_island_top_252d(open_, high, low).diff().diff()


def f05_fbkd_046_post_gap_up_close_below_open_count_63d_d2(open_, high, close):
    return f05_fbkd_046_post_gap_up_close_below_open_count_63d(open_, high, close).diff().diff()


def f05_fbkd_047_avg_gap_severity_failed_gaps_252d_d2(open_, high, close):
    return f05_fbkd_047_avg_gap_severity_failed_gaps_252d(open_, high, close).diff().diff()


def f05_fbkd_048_gap_fill_rate_within_5d_252d_d2(open_, high, low, close):
    return f05_fbkd_048_gap_fill_rate_within_5d_252d(open_, high, low, close).diff().diff()


def f05_fbkd_049_close_below_gap_open_within_3d_count_252d_d2(open_, high, close):
    return f05_fbkd_049_close_below_gap_open_within_3d_count_252d(open_, high, close).diff().diff()


def f05_fbkd_050_gap_up_at_252d_high_followed_by_red_close_63d_d2(open_, high, close):
    return f05_fbkd_050_gap_up_at_252d_high_followed_by_red_close_63d(open_, high, close).diff().diff()


def f05_fbkd_051_gap_size_zscore_failed_252d_d2(open_, high, close):
    return f05_fbkd_051_gap_size_zscore_failed_252d(open_, high, close).diff().diff()


def f05_fbkd_052_consecutive_failed_gap_ups_streak_d2(open_, high, close):
    return f05_fbkd_052_consecutive_failed_gap_ups_streak(open_, high, close).diff().diff()


def f05_fbkd_053_close_back_below_broken_252d_within_3d_d2(high, close):
    return f05_fbkd_053_close_back_below_broken_252d_within_3d(high, close).diff().diff()


def f05_fbkd_054_close_back_below_broken_252d_within_5d_d2(high, close):
    return f05_fbkd_054_close_back_below_broken_252d_within_5d(high, close).diff().diff()


def f05_fbkd_055_close_back_below_broken_252d_within_10d_d2(high, close):
    return f05_fbkd_055_close_back_below_broken_252d_within_10d(high, close).diff().diff()


def f05_fbkd_056_post_break_vol_decay_5d_vs_break_vol_d2(high, close, volume):
    return f05_fbkd_056_post_break_vol_decay_5d_vs_break_vol(high, close, volume).diff().diff()


def f05_fbkd_057_post_break_lower_high_within_5d_indicator_d2(high, close):
    return f05_fbkd_057_post_break_lower_high_within_5d_indicator(high, close).diff().diff()


def f05_fbkd_058_bull_trap_dwell_below_after_fail_252d_d2(high, close):
    return f05_fbkd_058_bull_trap_dwell_below_after_fail_252d(high, close).diff().diff()


def f05_fbkd_059_post_fail_volume_surge_5d_252d_d2(high, close, volume):
    return f05_fbkd_059_post_fail_volume_surge_5d_252d(high, close, volume).diff().diff()


def f05_fbkd_060_max_post_break_drawdown_pct_21d_252d_d2(high, low, close):
    return f05_fbkd_060_max_post_break_drawdown_pct_21d_252d(high, low, close).diff().diff()


def f05_fbkd_061_failed_breakout_to_lower_low_within_10d_d2(high, low, close):
    return f05_fbkd_061_failed_breakout_to_lower_low_within_10d(high, low, close).diff().diff()


def f05_fbkd_062_post_fail_red_volume_dominance_5d_d2(high, close, volume):
    return f05_fbkd_062_post_fail_red_volume_dominance_5d(high, close, volume).diff().diff()


def f05_fbkd_063_failed_break_close_in_lower_third_of_bar_d2(high, low, close):
    return f05_fbkd_063_failed_break_close_in_lower_third_of_bar(high, low, close).diff().diff()


def f05_fbkd_064_failed_break_with_upper_wick_atr_ratio_d2(high, low, close, open_):
    return f05_fbkd_064_failed_break_with_upper_wick_atr_ratio(high, low, close, open_).diff().diff()


def f05_fbkd_065_consecutive_failed_breaks_streak_21d_d2(high, close):
    return f05_fbkd_065_consecutive_failed_breaks_streak_21d(high, close).diff().diff()


def f05_fbkd_066_failed_retest_count_252d_504d_d2(high, low, close):
    return f05_fbkd_066_failed_retest_count_252d_504d(high, low, close).diff().diff()


def f05_fbkd_067_failed_retest_severity_atr_252d_d2(high, low, close):
    return f05_fbkd_067_failed_retest_severity_atr_252d(high, low, close).diff().diff()


def f05_fbkd_068_distance_to_nearest_failed_break_level_atr_d2(high, low, close):
    return f05_fbkd_068_distance_to_nearest_failed_break_level_atr(high, low, close).diff().diff()


def f05_fbkd_069_failed_break_then_failed_retest_within_21d_d2(high, close):
    return f05_fbkd_069_failed_break_then_failed_retest_within_21d(high, close).diff().diff()


def f05_fbkd_070_volume_on_failed_retest_vs_initial_fail_d2(high, close, volume):
    return f05_fbkd_070_volume_on_failed_retest_vs_initial_fail(high, close, volume).diff().diff()


def f05_fbkd_071_failed_retest_count_63d_window_d2(high, close):
    return f05_fbkd_071_failed_retest_count_63d_window(high, close).diff().diff()


def f05_fbkd_072_bars_since_last_failed_retest_d2(high, close):
    return f05_fbkd_072_bars_since_last_failed_retest(high, close).diff().diff()


def f05_fbkd_073_composite_false_break_severity_score_d2(open_, high, low, close, volume):
    return f05_fbkd_073_composite_false_break_severity_score(open_, high, low, close, volume).diff().diff()


def f05_fbkd_074_weighted_false_break_count_63d_decay_d2(high, close):
    return f05_fbkd_074_weighted_false_break_count_63d_decay(high, close).diff().diff()


def f05_fbkd_075_multi_horizon_false_break_breadth_count_d2(high, close):
    return f05_fbkd_075_multi_horizon_false_break_breadth_count(high, close).diff().diff()


FAILED_BREAKOUT_DYNAMICS_D2_REGISTRY_001_075 = {
    "f05_fbkd_001_false_break_count_21d_resistance_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_001_false_break_count_21d_resistance_63d_d2},
    "f05_fbkd_002_false_break_count_63d_resistance_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_002_false_break_count_63d_resistance_252d_d2},
    "f05_fbkd_003_false_break_count_252d_resistance_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_003_false_break_count_252d_resistance_504d_d2},
    "f05_fbkd_004_false_break_count_5d_resistance_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_004_false_break_count_5d_resistance_21d_d2},
    "f05_fbkd_005_false_break_count_504d_resistance_756d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_005_false_break_count_504d_resistance_756d_d2},
    "f05_fbkd_006_false_break_count_1260d_resistance_full_d2": {"inputs": ["high", "close"], "func": f05_fbkd_006_false_break_count_1260d_resistance_full_d2},
    "f05_fbkd_007_false_break_count_alltime_high_expanding_d2": {"inputs": ["high", "close"], "func": f05_fbkd_007_false_break_count_alltime_high_expanding_d2},
    "f05_fbkd_008_attempt_vs_success_ratio_21d_break_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_008_attempt_vs_success_ratio_21d_break_63d_d2},
    "f05_fbkd_009_attempt_vs_success_ratio_252d_break_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_009_attempt_vs_success_ratio_252d_break_504d_d2},
    "f05_fbkd_010_false_break_severity_atr_21d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_010_false_break_severity_atr_21d_d2},
    "f05_fbkd_011_false_break_severity_pct_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_011_false_break_severity_pct_252d_d2},
    "f05_fbkd_012_false_break_close_below_depth_atr_63d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_012_false_break_close_below_depth_atr_63d_d2},
    "f05_fbkd_013_bars_above_prior_252d_high_before_fail_d2": {"inputs": ["high", "close"], "func": f05_fbkd_013_bars_above_prior_252d_high_before_fail_d2},
    "f05_fbkd_014_bars_above_prior_63d_high_before_fail_d2": {"inputs": ["high", "close"], "func": f05_fbkd_014_bars_above_prior_63d_high_before_fail_d2},
    "f05_fbkd_015_time_to_fail_after_most_recent_252d_break_d2": {"inputs": ["high", "close"], "func": f05_fbkd_015_time_to_fail_after_most_recent_252d_break_d2},
    "f05_fbkd_016_post_break_max_drawdown_63d_after_252d_break_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_016_post_break_max_drawdown_63d_after_252d_break_d2},
    "f05_fbkd_017_repeat_fail_count_same_252d_level_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_017_repeat_fail_count_same_252d_level_504d_d2},
    "f05_fbkd_018_distinct_failed_levels_252d_horizon_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_018_distinct_failed_levels_252d_horizon_504d_d2},
    "f05_fbkd_019_bars_since_last_252d_false_break_d2": {"inputs": ["high", "close"], "func": f05_fbkd_019_bars_since_last_252d_false_break_d2},
    "f05_fbkd_020_post_fail_red_bar_count_5d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_020_post_fail_red_bar_count_5d_d2},
    "f05_fbkd_021_post_fail_lower_high_count_10d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_021_post_fail_lower_high_count_10d_d2},
    "f05_fbkd_022_max_high_vs_close_at_252d_fail_d2": {"inputs": ["high", "close"], "func": f05_fbkd_022_max_high_vs_close_at_252d_fail_d2},
    "f05_fbkd_023_time_to_first_fail_after_new_252d_high_d2": {"inputs": ["high", "close"], "func": f05_fbkd_023_time_to_first_fail_after_new_252d_high_d2},
    "f05_fbkd_024_dwell_above_252d_pre_break_post_fail_ratio_d2": {"inputs": ["high", "close"], "func": f05_fbkd_024_dwell_above_252d_pre_break_post_fail_ratio_d2},
    "f05_fbkd_025_failed_break_prior_year_high_ytd_d2": {"inputs": ["high", "close"], "func": f05_fbkd_025_failed_break_prior_year_high_ytd_d2},
    "f05_fbkd_026_failed_break_prior_quarter_high_qtd_d2": {"inputs": ["high", "close"], "func": f05_fbkd_026_failed_break_prior_quarter_high_qtd_d2},
    "f05_fbkd_027_failed_break_prior_month_high_mtd_d2": {"inputs": ["high", "close"], "func": f05_fbkd_027_failed_break_prior_month_high_mtd_d2},
    "f05_fbkd_028_failed_break_round_number_10dollar_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_028_failed_break_round_number_10dollar_252d_d2},
    "f05_fbkd_029_failed_break_round_number_25dollar_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_029_failed_break_round_number_25dollar_252d_d2},
    "f05_fbkd_030_failed_break_round_number_50dollar_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_030_failed_break_round_number_50dollar_252d_d2},
    "f05_fbkd_031_failed_break_round_number_100dollar_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_031_failed_break_round_number_100dollar_504d_d2},
    "f05_fbkd_032_failed_break_2y_high_504d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_032_failed_break_2y_high_504d_d2},
    "f05_fbkd_033_failed_break_5y_high_756d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_033_failed_break_5y_high_756d_d2},
    "f05_fbkd_034_failed_break_consolidation_top_63d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_034_failed_break_consolidation_top_63d_d2},
    "f05_fbkd_035_failed_break_pivot_r1_classical_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_035_failed_break_pivot_r1_classical_d2},
    "f05_fbkd_036_failed_break_pivot_r2_classical_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_036_failed_break_pivot_r2_classical_d2},
    "f05_fbkd_037_failed_break_double_top_neckline_proxy_63d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_037_failed_break_double_top_neckline_proxy_63d_d2},
    "f05_fbkd_038_failed_break_donchian_upper_20d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_038_failed_break_donchian_upper_20d_d2},
    "f05_fbkd_039_gap_up_at_new_252d_high_then_filled_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_039_gap_up_at_new_252d_high_then_filled_252d_d2},
    "f05_fbkd_040_gap_up_at_new_high_close_bottom_third_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_040_gap_up_at_new_high_close_bottom_third_252d_d2},
    "f05_fbkd_041_breakaway_gap_failure_time_to_fill_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_041_breakaway_gap_failure_time_to_fill_63d_d2},
    "f05_fbkd_042_post_breakaway_gap_max_dd_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_042_post_breakaway_gap_max_dd_21d_d2},
    "f05_fbkd_043_low_volume_gap_up_new_high_252d_d2": {"inputs": ["open", "high", "close", "volume"], "func": f05_fbkd_043_low_volume_gap_up_new_high_252d_d2},
    "f05_fbkd_044_runaway_gap_failure_504d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_044_runaway_gap_failure_504d_d2},
    "f05_fbkd_045_exhaustion_gap_island_top_252d_d2": {"inputs": ["open", "high", "low"], "func": f05_fbkd_045_exhaustion_gap_island_top_252d_d2},
    "f05_fbkd_046_post_gap_up_close_below_open_count_63d_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_046_post_gap_up_close_below_open_count_63d_d2},
    "f05_fbkd_047_avg_gap_severity_failed_gaps_252d_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_047_avg_gap_severity_failed_gaps_252d_d2},
    "f05_fbkd_048_gap_fill_rate_within_5d_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_048_gap_fill_rate_within_5d_252d_d2},
    "f05_fbkd_049_close_below_gap_open_within_3d_count_252d_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_049_close_below_gap_open_within_3d_count_252d_d2},
    "f05_fbkd_050_gap_up_at_252d_high_followed_by_red_close_63d_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_050_gap_up_at_252d_high_followed_by_red_close_63d_d2},
    "f05_fbkd_051_gap_size_zscore_failed_252d_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_051_gap_size_zscore_failed_252d_d2},
    "f05_fbkd_052_consecutive_failed_gap_ups_streak_d2": {"inputs": ["open", "high", "close"], "func": f05_fbkd_052_consecutive_failed_gap_ups_streak_d2},
    "f05_fbkd_053_close_back_below_broken_252d_within_3d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_053_close_back_below_broken_252d_within_3d_d2},
    "f05_fbkd_054_close_back_below_broken_252d_within_5d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_054_close_back_below_broken_252d_within_5d_d2},
    "f05_fbkd_055_close_back_below_broken_252d_within_10d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_055_close_back_below_broken_252d_within_10d_d2},
    "f05_fbkd_056_post_break_vol_decay_5d_vs_break_vol_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_056_post_break_vol_decay_5d_vs_break_vol_d2},
    "f05_fbkd_057_post_break_lower_high_within_5d_indicator_d2": {"inputs": ["high", "close"], "func": f05_fbkd_057_post_break_lower_high_within_5d_indicator_d2},
    "f05_fbkd_058_bull_trap_dwell_below_after_fail_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_058_bull_trap_dwell_below_after_fail_252d_d2},
    "f05_fbkd_059_post_fail_volume_surge_5d_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_059_post_fail_volume_surge_5d_252d_d2},
    "f05_fbkd_060_max_post_break_drawdown_pct_21d_252d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_060_max_post_break_drawdown_pct_21d_252d_d2},
    "f05_fbkd_061_failed_breakout_to_lower_low_within_10d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_061_failed_breakout_to_lower_low_within_10d_d2},
    "f05_fbkd_062_post_fail_red_volume_dominance_5d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_062_post_fail_red_volume_dominance_5d_d2},
    "f05_fbkd_063_failed_break_close_in_lower_third_of_bar_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_063_failed_break_close_in_lower_third_of_bar_d2},
    "f05_fbkd_064_failed_break_with_upper_wick_atr_ratio_d2": {"inputs": ["high", "low", "close", "open"], "func": f05_fbkd_064_failed_break_with_upper_wick_atr_ratio_d2},
    "f05_fbkd_065_consecutive_failed_breaks_streak_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_065_consecutive_failed_breaks_streak_21d_d2},
    "f05_fbkd_066_failed_retest_count_252d_504d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_066_failed_retest_count_252d_504d_d2},
    "f05_fbkd_067_failed_retest_severity_atr_252d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_067_failed_retest_severity_atr_252d_d2},
    "f05_fbkd_068_distance_to_nearest_failed_break_level_atr_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_068_distance_to_nearest_failed_break_level_atr_d2},
    "f05_fbkd_069_failed_break_then_failed_retest_within_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_069_failed_break_then_failed_retest_within_21d_d2},
    "f05_fbkd_070_volume_on_failed_retest_vs_initial_fail_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_070_volume_on_failed_retest_vs_initial_fail_d2},
    "f05_fbkd_071_failed_retest_count_63d_window_d2": {"inputs": ["high", "close"], "func": f05_fbkd_071_failed_retest_count_63d_window_d2},
    "f05_fbkd_072_bars_since_last_failed_retest_d2": {"inputs": ["high", "close"], "func": f05_fbkd_072_bars_since_last_failed_retest_d2},
    "f05_fbkd_073_composite_false_break_severity_score_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_fbkd_073_composite_false_break_severity_score_d2},
    "f05_fbkd_074_weighted_false_break_count_63d_decay_d2": {"inputs": ["high", "close"], "func": f05_fbkd_074_weighted_false_break_count_63d_decay_d2},
    "f05_fbkd_075_multi_horizon_false_break_breadth_count_d2": {"inputs": ["high", "close"], "func": f05_fbkd_075_multi_horizon_false_break_breadth_count_d2},
}
