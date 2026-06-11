"""failed_breakout_dynamics d2 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Theme:
bull traps, false-break counts, breakaway gap failures at multi-year peaks.
This file covers: volume confirmation, dwell duration, downside fakeouts at top,
psychological-level interactions, multi-signal composites, longer-cycle bull-trap
patterns and post-failure trajectory metrics.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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

def f05_fbkd_076_breakout_day_vol_vs_21d_mean_at_252d_fail(high, close, volume):
    """At 252d false-break bars: ratio of volume / 21d-mean-vol"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vr = _safe_div(volume, v21)
    is_fail = (high > prior_max) & (close < prior_max)
    return vr.where(is_fail, np.nan)

def f05_fbkd_077_high_vol_low_progress_false_break_252d(high, low, close, volume):
    """At 252d false-break bars: indicator that volume>2x 21d-me"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vr = _safe_div(volume, v21)
    pos = _safe_div(close - low, high - low)
    cond = (vr > 2.0) & (pos < 0.3)
    is_fail = (high > prior_max) & (close < prior_max)
    return cond.astype(float).where(is_fail & vr.notna() & pos.notna(), np.nan)

def f05_fbkd_078_volume_on_failback_move_vs_breakout(high, close, volume):
    """Post/pre 3d vol ratio at most recent 252d failed-break"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; vv = volume.values; n = len(vv)
    out = np.full(n, np.nan); w = YDAYS
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1); lf = -1
        for j in range(i, lo - 1, -1):
            if fail[j]:
                lf = j; break
        if lf < 0:
            continue
        pre = vv[max(0, lf - 3):lf]; pre = pre[~np.isnan(pre)]
        up = min(min(n - 1, lf + 3), i)
        post = vv[lf + 1:up + 1]; post = post[~np.isnan(post)]
        if pre.size and post.size and pre.mean() > 0:
            out[i] = float(post.mean() / pre.mean())
    return pd.Series(out, index=high.index)

def f05_fbkd_079_volume_zscore_at_252d_fail(high, close, volume):
    """Volume z-score (over 252d) at 252d failed-break bars"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    vz = _rolling_zscore(volume, YDAYS)
    is_fail = (high > prior_max) & (close < prior_max)
    return vz.where(is_fail, np.nan)

def f05_fbkd_080_dollar_volume_fail_severity_252d(high, close, volume):
    """Dollar-volume z-score (252d) at 252d failed-break bars —"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    dv = close * volume
    dvz = _rolling_zscore(dv, YDAYS)
    is_fail = (high > prior_max) & (close < prior_max)
    return dvz.where(is_fail, np.nan)

def f05_fbkd_081_low_volume_252d_break_count_252d(high, close, volume):
    """Count in 252d of 252d successful breaks (close>prior 252d"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    succ = (close > prior_max)
    lowv = volume < v21
    event = (succ & lowv).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_082_vol_ratio_at_intraday_pierce_vs_pre_252d(high, close, volume):
    """At intraday 252d-pierce bars (high>prior 252d max), vol /"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v5 = volume.shift(1).rolling(WDAYS, min_periods=2).mean()
    vr = _safe_div(volume, v5)
    pierce = (high > prior_max)
    return vr.where(pierce, np.nan)

def f05_fbkd_083_obv_divergence_at_252d_fail(close, volume, high):
    """At 252d failed-break bars: 21d-slope of OBV minus 21d-slo"""
    direction = np.sign(close.diff()).fillna(0)
    obv = (direction * volume).cumsum()
    sl_obv = _rolling_slope(obv, MDAYS)
    sl_px = _rolling_slope(close, MDAYS)
    diff = sl_obv - sl_px
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_fail = (high > prior_max) & (close < prior_max)
    return diff.where(is_fail, np.nan)

def f05_fbkd_084_cum_vol_above_broken_252d_pre_fail(high, close, volume):
    """Cumulative pre-fail dwell-above volume (most recent 252d fail)"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; cv = close.values; vv = volume.values; n = len(cv)
    out = np.full(n, np.nan); w = YDAYS
    for i in range(n):
        if np.isnan(pv[i]):
            continue
        lo = max(0, i - w + 1); lf = -1
        for j in range(i, lo - 1, -1):
            if fail[j]:
                lf = j; break
        if lf < 0:
            continue
        lvl = pv[lf]; cum = 0.0; any_a = False
        for k in range(lf - 1, max(-1, lf - 22), -1):
            if not np.isnan(cv[k]) and cv[k] > lvl and not np.isnan(vv[k]):
                cum += vv[k]; any_a = True
            else:
                break
        if any_a:
            out[i] = cum
    return pd.Series(out, index=high.index)

def f05_fbkd_085_vol_weighted_failed_breaks_252d(high, close, volume):
    """Sum over trailing 252d of (volume_zscore_at_fail) for eac"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    vz = _rolling_zscore(volume, YDAYS)
    is_fail = ((high > prior_max) & (close < prior_max)).astype(float)
    contrib = (vz * is_fail).fillna(0)
    return contrib.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_086_vol_climax_into_failed_break_5d_252d(high, close, volume):
    """At 252d failed-break bars: indicator that 5d-pre-break cu"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    pre_vol = volume.shift(1).rolling(WDAYS, min_periods=2).sum()
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size)
    rk = pre_vol.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    is_fail = (high > prior_max) & (close < prior_max)
    return (rk >= 0.9).astype(float).where(is_fail & rk.notna(), np.nan)

def f05_fbkd_087_avg_relative_vol_at_failed_breaks_252d(high, close, volume):
    """Mean of (vol / 21d-mean-vol) across all 252d failed-break"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vr = _safe_div(volume, v21)
    is_fail = (high > prior_max) & (close < prior_max)
    val = vr.where(is_fail, np.nan)
    return val.rolling(YDAYS, min_periods=QDAYS).mean()

def _fbkd_dwell_at_fails(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    pv = pm.values; cv = close.values; n = len(cv)
    dw = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(pv[i]) or not fail[i]:
            continue
        lvl = pv[i]; d = 0
        for k in range(i - 1, max(-1, i - 31), -1):
            if not np.isnan(cv[k]) and cv[k] > lvl:
                d += 1
            else:
                break
        dw[i] = float(d)
    return pd.Series(dw, index=high.index)


def f05_fbkd_088_short_dwell_trap_under_3d_count_252d(high, close):
    """252d count of failed 252d-breaks with pre-fail dwell < 3 bars"""
    dw = _fbkd_dwell_at_fails(high, close)
    ind = (dw < 3).astype(float).where(dw.notna(), 0.0)
    return ind.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_089_extended_dwell_trap_over_10d_count_252d(high, close):
    """252d count of failed 252d-breaks with pre-fail dwell > 10 bars"""
    dw = _fbkd_dwell_at_fails(high, close)
    ind = (dw > 10).astype(float).where(dw.notna(), 0.0)
    return ind.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_090_mean_dwell_above_at_failed_breaks_252d(high, close):
    """Mean pre-fail dwell duration across 252d failed-breaks"""
    return _fbkd_dwell_at_fails(high, close).rolling(YDAYS, min_periods=QDAYS).mean()

def f05_fbkd_091_max_dwell_above_at_failed_breaks_252d(high, close):
    """Max pre-fail dwell duration across 252d failed-breaks"""
    return _fbkd_dwell_at_fails(high, close).rolling(YDAYS, min_periods=QDAYS).max()

def f05_fbkd_092_dwell_duration_variance_failed_252d(high, close):
    """Variance of pre-fail dwell durations across 252d failed-breaks"""
    return _fbkd_dwell_at_fails(high, close).rolling(YDAYS, min_periods=QDAYS).var()

def f05_fbkd_093_bars_between_consecutive_252d_fails_avg_252d(high, close):
    """Mean bar-gap between consecutive 252d failed-break events"""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > prior_max) & (close < prior_max)).astype(float)
    def _mean_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True)

def f05_fbkd_094_dwell_above_persistence_streak_above_252d(high, close):
    """Current consecutive bars close has been above prior 252d-"""
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

def f05_fbkd_095_failed_downside_break_21d_low_count_252d(low, close):
    """Count in 252d of bars where low pierces prior 21d low (in"""
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    fail = ((low < prior_min) & (close > prior_min)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_096_failed_downside_break_63d_low_count_252d(low, close):
    """Count in 252d of failed bear-fakeouts of prior 63d low —"""
    prior_min = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    fail = ((low < prior_min) & (close > prior_min)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_097_failed_downside_break_252d_low_count_504d(low, close):
    """Count in 504d of failed bear-fakeouts of prior 252d low —"""
    prior_min = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    fail = ((low < prior_min) & (close > prior_min)).astype(float)
    return fail.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_098_failed_downside_break_at_252d_high_indicator(high, low, close):
    """Indicator: today is a failed 21d-low break AND price is w"""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    failed_bear = (low < prior_min) & (close > prior_min)
    near_top = close >= 0.95 * rmax
    return (failed_bear & near_top).astype(float).where(rmax.notna() & prior_min.notna(), np.nan)

def f05_fbkd_099_squeeze_recovery_after_failed_down_break_5d(low, close):
    """For failed 21d-low breaks, max close-recovery (close/even"""
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    fail = ((low < prior_min) & (close > prior_min)).astype(float).values
    arr_c = close.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not np.isnan(fail[i]) and fail[i] > 0:
            bc = arr_c[i]
            if np.isnan(bc) or bc <= 0:
                continue
            upper = min(n - 1, i + WDAYS)
            seg = arr_c[i + 1:upper + 1]
            seg_v = seg[~np.isnan(seg)]
            if seg_v.size == 0:
                continue
            out[i] = float(seg_v.max() / bc - 1.0)
    return pd.Series(out, index=low.index).shift(WDAYS)

def f05_fbkd_100_attempt_vs_success_ratio_21d_low_break_252d(low, close):
    """In 252d: attempt (intraday 21d-low break) / success (clos"""
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    attempt = (low < prior_min).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    succ = (close < prior_min).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(attempt, succ)

def f05_fbkd_101_bear_trap_severity_lower_wick_atr(low, high, close, open_):
    """At failed 21d-low-break bars: lower-wick = min(open,close"""
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    wick = body_bot - low
    atr = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(wick, atr)
    is_fail = (low < prior_min) & (close > prior_min)
    return ratio.where(is_fail, np.nan)

def f05_fbkd_102_bear_trap_then_failed_top_within_21d(high, low, close):
    """Indicator: a failed 21d-low (bear trap) at bar i-21"""
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    bear_trap = ((low < prior_min) & (close > prior_min)).astype(float)
    bull_trap = ((high > prior_max) & (close < prior_max)).astype(float)
    bear_recent = bear_trap.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    bull_recent = bull_trap.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return (bear_recent & bull_recent).astype(float).where(prior_min.notna() & prior_max.notna(), np.nan)

def f05_fbkd_103_composite_trap_density_index_252d(high, close):
    """Trap density = (failed 21d breaks + failed 63d breaks + f"""
    pm21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pm63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    pm252 = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    f21 = ((high > pm21) & (close < pm21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    f63 = ((high > pm63) & (close < pm63)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    f252 = ((high > pm252) & (close < pm252)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (f21 + f63 + f252) / float(YDAYS)

def f05_fbkd_104_weighted_severity_sum_failed_252d_atr(high, low, close):
    """Sum over 252d of (overshoot/ATR + below-depth/ATR) at eac"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    depth = _safe_div(pm - close, atr)
    is_fail = ((high > pm) & (close < pm)).astype(float)
    sev = (over.fillna(0) + depth.fillna(0)) * is_fail
    return sev.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_105_trap_breadth_top_quintile_indicator(high, close):
    """Indicator: trap-density-index is in TOP QUINTILE of 252d"""
    pm21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pm63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    pm252 = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    f21 = ((high > pm21) & (close < pm21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    f63 = ((high > pm63) & (close < pm63)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    f252 = ((high > pm252) & (close < pm252)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    density = (f21 + f63 + f252)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size)
    rk = density.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rk >= 0.8).astype(float).where(rk.notna(), np.nan)

def f05_fbkd_106_simultaneous_multi_anchor_fail_count_5d(high, close):
    """Count in 5d of bars that failed AT LEAST 2 of {63d, 252d,"""
    pm63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    pm252 = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    pm504 = high.shift(1).rolling(DDAYS_2Y, min_periods=YDAYS).max()
    f63 = ((high > pm63) & (close < pm63)).astype(float)
    f252 = ((high > pm252) & (close < pm252)).astype(float)
    f504 = ((high > pm504) & (close < pm504)).astype(float)
    multi = (f63 + f252 + f504) >= 2.0
    return multi.astype(float).rolling(WDAYS, min_periods=2).sum()

def f05_fbkd_107_recency_weighted_trap_count_252d(high, close):
    """252d failed-break count weighted by exponential decay (ha"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    decay = np.exp(-np.log(2.0) * np.arange(YDAYS) / float(QDAYS))[::-1]
    def _wt(w):
        if np.isnan(w).all():
            return np.nan
        ww = np.where(np.isnan(w), 0.0, w)
        return float((ww * decay[-len(ww):]).sum())
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_wt, raw=True)

def f05_fbkd_108_trap_count_acceleration_recent_minus_prior(high, close):
    """Change in trap rate: failed-252d-breaks in last 63d minus"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    recent = fail.rolling(QDAYS, min_periods=MDAYS).sum()
    prior = fail.shift(QDAYS).rolling(QDAYS, min_periods=MDAYS).sum()
    return recent - prior

def f05_fbkd_109_avg_overshoot_atr_at_252d_fails_252d(high, low, close):
    """Mean overshoot/ATR magnitude across all 252d failed-break"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    is_fail = (high > pm) & (close < pm)
    val = over.where(is_fail, np.nan)
    return val.rolling(YDAYS, min_periods=QDAYS).mean()

def f05_fbkd_110_max_severity_trap_252d_atr(high, low, close):
    """Max severity (overshoot/ATR + close-below-depth/ATR) acro"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    depth = _safe_div(pm - close, atr)
    is_fail = (high > pm) & (close < pm)
    sev = (over.fillna(0) + depth.fillna(0)).where(is_fail, np.nan)
    return sev.rolling(YDAYS, min_periods=QDAYS).max()

def f05_fbkd_111_min_time_to_fail_252d_breaks_252d(high, close):
    """Min pre-fail dwell duration across 252d failed-breaks"""
    return _fbkd_dwell_at_fails(high, close).rolling(YDAYS, min_periods=QDAYS).min()

def f05_fbkd_112_dispersion_severity_failed_252d(high, low, close):
    """Std dev of severity (overshoot/ATR) across 252d trailing"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    is_fail = (high > pm) & (close < pm)
    val = over.where(is_fail, np.nan)
    return val.rolling(YDAYS, min_periods=QDAYS).std()

def f05_fbkd_113_proportion_failed_vs_total_breaks_252d(high, close):
    """Proportion of all 252d intraday-break attempts that close"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    attempt = (high > pm).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    fail = ((high > pm) & (close < pm)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fail, attempt)

def f05_fbkd_114_normalized_trap_pressure_score_252d(high, low, close, volume):
    """Composite z-score: 0"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    is_fail = ((high > pm) & (close < pm)).astype(float)
    cnt = is_fail.rolling(YDAYS, min_periods=QDAYS).sum()
    sev = over.where(is_fail > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    vz = _rolling_zscore(volume, YDAYS)
    vw = (vz * is_fail).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(cnt, DDAYS_2Y, min_periods=YDAYS)
    z2 = _rolling_zscore(sev, DDAYS_2Y, min_periods=YDAYS)
    z3 = _rolling_zscore(vw, DDAYS_2Y, min_periods=YDAYS)
    return 0.4 * z1.fillna(0) + 0.3 * z2.fillna(0) + 0.3 * z3.fillna(0)

def f05_fbkd_115_trap_pressure_top_decile_indicator_504d(high, low, close, volume):
    """Indicator: composite trap-pressure score (114) is in TOP"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    is_fail = ((high > pm) & (close < pm)).astype(float)
    cnt = is_fail.rolling(YDAYS, min_periods=QDAYS).sum()
    sev = over.where(is_fail > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    vz = _rolling_zscore(volume, YDAYS)
    vw = (vz * is_fail).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(cnt, DDAYS_2Y, min_periods=YDAYS)
    z2 = _rolling_zscore(sev, DDAYS_2Y, min_periods=YDAYS)
    z3 = _rolling_zscore(vw, DDAYS_2Y, min_periods=YDAYS)
    score = 0.4 * z1.fillna(0) + 0.3 * z2.fillna(0) + 0.3 * z3.fillna(0)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size)
    rk = score.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    return (rk >= 0.9).astype(float).where(rk.notna(), np.nan)

def f05_fbkd_116_alltime_high_break_then_failure_within_21d(high, close):
    """Indicator: in last 21d, expanding ATH was made AND a clos"""
    ath = high.expanding(min_periods=QDAYS).max()
    new_ath = (high >= ath).astype(float)
    prior_ath = high.shift(1).expanding(min_periods=QDAYS).max()
    fail_at_ath = ((close < prior_ath) & (high.shift(1).expanding(min_periods=QDAYS).max() > 0)).astype(float)
    nh_recent = new_ath.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    fb_recent = fail_at_ath.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return (nh_recent & fb_recent).astype(float).where(ath.notna(), np.nan)

def f05_fbkd_117_failed_break_round_25_pct_severity_252d(high, close):
    """At failed-25-round-number-breaks: overshoot pct of high a"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 25.0) * 25.0)
    target = target.where(target > prev_c, target + 25.0)
    fail = (high > target) & (close < target)
    overshoot = _safe_div(high - target, target)
    return overshoot.where(fail, np.nan)

def f05_fbkd_118_round_number_density_repeated_failure_252d(high, close):
    """Count in 252d of bars where high pierces ANY of {nearest"""
    prev_c = close.shift(1)
    cnt = pd.Series(0.0, index=high.index)
    for unit in [1.0, 5.0, 10.0, 25.0, 50.0, 100.0]:
        target = (np.ceil(prev_c / unit) * unit)
        target = target.where(target > prev_c, target + unit)
        fail = ((high > target) & (close < target)).astype(float)
        cnt = cnt + fail.fillna(0)
    cnt = cnt.where(prev_c.notna(), np.nan)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_119_approach_to_round_100_within_2pct_count_63d(high, close):
    """Count in 63d of bars where high comes within 2% of neares"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 100.0) * 100.0)
    target = target.where(target > prev_c, target + 100.0)
    near = (high >= 0.98 * target) & (high < target)
    return near.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()

def f05_fbkd_120_approach_to_round_50_within_2pct_count_63d(high, close):
    """Count in 63d of bars where high comes within 2% of neares"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 50.0) * 50.0)
    target = target.where(target > prev_c, target + 50.0)
    near = (high >= 0.98 * target) & (high < target)
    return near.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()

def f05_fbkd_121_failed_break_round_5_pct_252d(high, close):
    """252d count of failed breaks of nearest $5 round number —"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 5.0) * 5.0)
    target = target.where(target > prev_c, target + 5.0)
    fail = ((high > target) & (close < target)).astype(float)
    return fail.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_122_distance_to_next_round_100_close(close):
    """Pct distance from today's close to nearest $100 round abo"""
    target = (np.ceil(close / 100.0) * 100.0)
    target = target.where(target > close, target + 100.0)
    return _safe_div(target - close, close)

def f05_fbkd_123_distance_to_next_round_25_close(close):
    """Pct distance from close to nearest $25 round above"""
    target = (np.ceil(close / 25.0) * 25.0)
    target = target.where(target > close, target + 25.0)
    return _safe_div(target - close, close)

def f05_fbkd_124_distance_to_next_round_10_close(close):
    """Pct distance from close to nearest $10 round above"""
    target = (np.ceil(close / 10.0) * 10.0)
    target = target.where(target > close, target + 10.0)
    return _safe_div(target - close, close)

def f05_fbkd_125_round_100_clinginess_5d(close):
    """Trailing 5d count of bars within 1% (above OR below) of n"""
    nearest = np.round(close / 100.0) * 100.0
    near = (((close / nearest) - 1.0).abs() <= 0.01).astype(float)
    near = near.where(nearest > 0, np.nan)
    return near.rolling(WDAYS, min_periods=2).sum()

def f05_fbkd_126_failed_break_round_high_then_collapse_5d_pct(open_, high, low, close):
    """At failed $25-round-number breaks, max drop (low/event_cl"""
    prev_c = close.shift(1)
    target = (np.ceil(prev_c / 25.0) * 25.0)
    target = target.where(target > prev_c, target + 25.0)
    fail = ((high > target) & (close < target)).astype(float).values
    arr_c = close.values
    arr_l = low.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not np.isnan(fail[i]) and fail[i] > 0:
            bc = arr_c[i]
            if np.isnan(bc) or bc <= 0:
                continue
            upper = min(n - 1, i + WDAYS)
            seg = arr_l[i + 1:upper + 1]
            seg_v = seg[~np.isnan(seg)]
            if seg_v.size == 0:
                continue
            out[i] = float(seg_v.min() / bc - 1.0)
    return pd.Series(out, index=high.index).shift(WDAYS)

def f05_fbkd_127_failed_secular_high_3y_756d(high, close):
    """Count in 756d of failed breaks of prior 756d (3y) high —"""
    pm = high.shift(1).rolling(DDAYS_3Y, min_periods=YDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    return fail.rolling(DDAYS_3Y, min_periods=YDAYS).sum()

def f05_fbkd_128_lifetime_ath_overshoot_failed_count(high, close):
    """Expanding count of bars whose high exceeded prior ATH by"""
    prior_ath = high.shift(1).expanding(min_periods=QDAYS).max()
    overshoot = (high >= 1.02 * prior_ath)
    fail = (close < prior_ath)
    event = (overshoot & fail).astype(float)
    return event.expanding(min_periods=QDAYS).sum()

def f05_fbkd_129_bars_in_failed_break_state_252d(high, close):
    """Count of bars in trailing 252d in 'failed-break state' ="""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high_recent = (high > pm).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    below_now = close < pm
    state = (new_high_recent & below_now).astype(float)
    return state.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_130_breakout_then_fail_event_504d_distinct_levels(high, close):
    """Distinct levels where a successful close-break-then-fail-"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = DDAYS_2Y
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        lo = max(0, i - win + 1)
        levels = []
        for j in range(lo, i + 1):
            if np.isnan(arr_p[j]) or np.isnan(arr_c[j]):
                continue
            if arr_c[j] > arr_p[j]:
                lvl = arr_p[j]
                upper = min(n - 1, j + 10)
                upper = min(upper, i)
                for k in range(j + 1, upper + 1):
                    if not np.isnan(arr_c[k]) and arr_c[k] < lvl:
                        levels.append(lvl)
                        break
        if not levels:
            out[i] = 0.0
            continue
        levels.sort()
        distinct = 1
        last = levels[0]
        for v in levels[1:]:
            if v > last * 1.01:
                distinct += 1
                last = v
        out[i] = float(distinct)
    return pd.Series(out, index=high.index)

def f05_fbkd_131_max_close_above_then_drop_below_252d(high, close):
    """For most recent 252d-break in 252d: max close achieved ab"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_c[i]):
            continue
        lo = max(0, i - win + 1)
        last_brk = -1
        for j in range(i, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_brk = j
                break
        if last_brk < 0:
            continue
        lvl = arr_p[last_brk]
        if arr_c[i] >= lvl:
            out[i] = 0.0
            continue
        seg = arr_c[last_brk:i + 1]
        seg = seg[~np.isnan(seg)]
        if seg.size == 0:
            continue
        mx = float(seg.max())
        if mx <= 0:
            continue
        out[i] = float((mx - arr_c[i]) / mx)
    return pd.Series(out, index=high.index)

def f05_fbkd_132_first_fail_after_lifetime_high_within_21d(high, close):
    """Indicator: lifetime ATH set within last 21 bars AND close"""
    ath = high.expanding(min_periods=QDAYS).max()
    new_ath = (high >= ath).astype(float)
    nh_recent = new_ath.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    drawdown = _safe_div(close - ath, ath)
    cond = drawdown <= -0.05
    return (nh_recent & cond).astype(float).where(ath.notna(), np.nan)

def f05_fbkd_133_fraction_252d_above_then_below_breakout_level(high, close):
    """Fraction of trailing 252d bars in 'distribution overhang'"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    state = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_c[i]):
            continue
        lo = max(0, i - win + 1)
        last_lvl = np.nan
        for j in range(i, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_lvl = arr_p[j]
                break
        if not np.isnan(last_lvl):
            state[i] = 1.0 if arr_c[i] < last_lvl else 0.0
        else:
            state[i] = 0.0
    s = pd.Series(state, index=high.index)
    return s.rolling(YDAYS, min_periods=QDAYS).mean()

def f05_fbkd_134_cycle_break_failure_ratio_3y(high, close):
    """In 756d window: count of 252d failed-break events / count"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float).rolling(DDAYS_3Y, min_periods=YDAYS).sum()
    succ = (close > pm).astype(float).rolling(DDAYS_3Y, min_periods=YDAYS).sum()
    return _safe_div(fail, succ)

def f05_fbkd_135_terminal_failed_break_no_recovery_63d(high, close):
    """Indicator: a 252d failed-break occurred 63 bars ago AND p"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if i - QDAYS < 0:
            continue
        evt_idx = i - QDAYS
        if (not np.isnan(arr_p[evt_idx]) and not np.isnan(arr_h[evt_idx]) and not np.isnan(arr_c[evt_idx])
                and arr_h[evt_idx] > arr_p[evt_idx] and arr_c[evt_idx] < arr_p[evt_idx]):
            lvl = arr_p[evt_idx]
            seg = arr_c[evt_idx + 1:i + 1]
            seg = seg[~np.isnan(seg)]
            if seg.size > 0 and seg.max() < lvl:
                out[i] = 1.0
            else:
                out[i] = 0.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)

def f05_fbkd_136_post_failure_trajectory_slope_21d(high, close):
    """Most recent 252d-fail event was within trailing 21d, AND"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    fail_recent = fail.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    slp = _rolling_slope(close, MDAYS)
    return slp.where(fail_recent, np.nan)

def f05_fbkd_137_breakout_then_within_atr_of_level_after_5d(high, low, close):
    """5 bars after most recent 252d-break: distance of close to"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    arr_c = close.values
    arr_p = pm.values
    arr_atr = atr.values
    n = len(arr_c)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        if i < WDAYS:
            continue
        lo = max(0, i - win + 1)
        last_brk = -1
        for j in range(i - WDAYS, lo - 1, -1):
            if not np.isnan(arr_p[j]) and not np.isnan(arr_c[j]) and arr_c[j] > arr_p[j]:
                last_brk = j
                break
        if last_brk < 0:
            continue
        lvl = arr_p[last_brk]
        a = arr_atr[i]
        if np.isnan(a) or a <= 0 or np.isnan(arr_c[i]):
            continue
        out[i] = float((arr_c[i] - lvl) / a)
    return pd.Series(out, index=high.index)

def f05_fbkd_138_failed_break_to_below_50sma_within_10d(high, close):
    """Indicator: in trailing 10d a 252d fail event occurred AND"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    fail_recent = fail.rolling(10, min_periods=3).sum() > 0
    sma50 = close.rolling(50, min_periods=20).mean()
    below = close < sma50
    return (fail_recent & below).astype(float).where(sma50.notna(), np.nan)

def f05_fbkd_139_failed_break_to_below_200sma_within_21d(high, close):
    """Indicator: in trailing 21d a 252d fail occurred AND close"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    fail_recent = fail.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    sma200 = close.rolling(200, min_periods=63).mean()
    below = close < sma200
    return (fail_recent & below).astype(float).where(sma200.notna(), np.nan)

def f05_fbkd_140_trap_cascade_count_252d(high, close):
    """Count in 252d of 'cascade' bars: a 252d fail-event AND si"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    is_fail = ((high > pm) & (close < pm)).astype(float).values
    cascade = np.zeros(n, dtype=float)
    cascade[:] = np.nan
    for i in range(n):
        if np.isnan(arr_p[i]) or np.isnan(arr_h[i]) or np.isnan(arr_c[i]):
            continue
        if is_fail[i] > 0:
            lvl_now = arr_p[i]
            lb = max(0, i - MDAYS)
            seen_diff_level_fail = False
            for j in range(i - 1, lb - 1, -1):
                if (not np.isnan(arr_p[j]) and not np.isnan(arr_h[j]) and not np.isnan(arr_c[j])
                        and arr_h[j] > arr_p[j] and arr_c[j] < arr_p[j]
                        and abs(arr_p[j] - lvl_now) > 0.01 * lvl_now):
                    seen_diff_level_fail = True
                    break
            cascade[i] = 1.0 if seen_diff_level_fail else 0.0
        else:
            cascade[i] = 0.0
    s = pd.Series(cascade, index=high.index)
    return s.rolling(YDAYS, min_periods=QDAYS).sum()

def f05_fbkd_141_failed_break_bar_severity_composite(open_, high, low, close, volume):
    """Single-bar trap severity composite: (overshoot/ATR) + (cl"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div((high - pm).clip(lower=0), atr)
    depth = _safe_div((pm - close).clip(lower=0), atr)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    wick = _safe_div((high - body_top).clip(lower=0), atr)
    vol21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vlog = _safe_log(_safe_div(volume, vol21))
    return over.fillna(0) + depth.fillna(0) + wick.fillna(0) + vlog.fillna(0)

def f05_fbkd_142_failed_break_recency_decay_score_252d(high, close):
    """Sum of exp(-(i-event_idx)/21) over all 252d fail events i"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    decay = np.exp(-np.arange(YDAYS) / float(MDAYS))[::-1]
    def _wt(w):
        if np.isnan(w).all():
            return np.nan
        ww = np.where(np.isnan(w), 0.0, w)
        return float((ww * decay[-len(ww):]).sum())
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_wt, raw=True)

def f05_fbkd_143_avg_fail_severity_pct_252d(high, close):
    """Average pct overshoot above broken level across 252d trai"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    over = _safe_div(high - pm, pm)
    is_fail = (high > pm) & (close < pm)
    val = over.where(is_fail, np.nan)
    return val.rolling(YDAYS, min_periods=QDAYS).mean()

def f05_fbkd_144_post_trap_recovery_failure_count_63d(high, close):
    """In trailing 63d, count of failed-break events that did NO"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = high.values
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    is_fail = ((high > pm) & (close < pm)).astype(float).values
    nonrecov = np.zeros(n, dtype=float)
    nonrecov[:] = np.nan
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        if is_fail[i] > 0:
            lvl = arr_p[i]
            upper = min(n - 1, i + MDAYS)
            seg = arr_c[i + 1:upper + 1]
            seg = seg[~np.isnan(seg)]
            if seg.size == 0:
                nonrecov[i] = 0.0
            else:
                nonrecov[i] = 1.0 if seg.max() < lvl else 0.0
        else:
            nonrecov[i] = 0.0
    s = pd.Series(nonrecov, index=high.index).shift(MDAYS)
    return s.rolling(QDAYS, min_periods=MDAYS).sum()

def f05_fbkd_145_no_recovery_trap_severity_atr_63d(high, low, close):
    """For non-recovering trap events in trailing 63d (no-recove"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    arr_h = high.values
    arr_c = close.values
    arr_p = pm.values
    arr_atr = atr.values
    n = len(arr_c)
    is_fail = ((high > pm) & (close < pm)).astype(float).values
    val = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        if is_fail[i] > 0:
            lvl = arr_p[i]
            upper = min(n - 1, i + MDAYS)
            if upper - i < MDAYS:
                continue
            cv = arr_c[upper]
            av = arr_atr[upper]
            if np.isnan(cv) or np.isnan(av) or av <= 0:
                continue
            seg = arr_c[i + 1:upper + 1]
            seg = seg[~np.isnan(seg)]
            if seg.size > 0 and seg.max() < lvl:
                val[i] = float((cv - lvl) / av)
    s = pd.Series(val, index=high.index).shift(MDAYS)
    return s.rolling(QDAYS, min_periods=MDAYS).mean()

def f05_fbkd_146_top_trap_episode_indicator_5y(high, low, close, volume):
    """Indicator: today's composite single-bar trap severity (14"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div((high - pm).clip(lower=0), atr)
    depth = _safe_div((pm - close).clip(lower=0), atr)
    body_top = pd.concat([close], axis=1).max(axis=1)
    wick = _safe_div((high - body_top).clip(lower=0), atr)
    vol21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vlog = _safe_log(_safe_div(volume, vol21))
    score = over.fillna(0) + depth.fillna(0) + wick.fillna(0) + vlog.fillna(0)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size)
    rk = score.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)
    return (rk >= 0.99).astype(float).where(rk.notna(), np.nan)

def f05_fbkd_147_failed_break_vs_succeed_volume_ratio_252d(high, close, volume):
    """In 252d: mean vol on 252d failed-break bars / mean vol on"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_fail = ((high > pm) & (close < pm)).astype(float)
    is_succ = ((close > pm)).astype(float)
    fail_v = (volume * is_fail).replace(0, np.nan)
    succ_v = (volume * is_succ).replace(0, np.nan)
    fm = fail_v.rolling(YDAYS, min_periods=QDAYS).mean()
    sm = succ_v.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(fm, sm)

def f05_fbkd_148_clustering_index_failed_breaks_252d(high, close):
    """Variance / mean of inter-arrival gaps between 252d failed"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    def _idx_disp(w):
        idx = np.where(w > 0)[0]
        if idx.size < 3:
            return np.nan
        g = np.diff(idx).astype(float)
        m = g.mean()
        if m == 0:
            return np.nan
        return float(g.var(ddof=1) / m)
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_idx_disp, raw=True)

def f05_fbkd_149_extreme_failed_break_count_top_1pct_severity_504d(high, low, close):
    """Count in 504d of 252d failed-breaks whose severity (overs"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div((high - pm).clip(lower=0), atr)
    depth = _safe_div((pm - close).clip(lower=0), atr)
    sev = over.fillna(0) + depth.fillna(0)
    is_fail = ((high > pm) & (close < pm)).astype(float)
    sev_at_fail = sev.where(is_fail > 0, np.nan)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = sev_at_fail.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    extreme = (rk >= 0.99).astype(float)
    return extreme.rolling(DDAYS_2Y, min_periods=YDAYS).sum()

def f05_fbkd_150_composite_terminal_trap_state_indicator(high, low, close, volume):
    """Composite terminal-trap state: 1 if (≥2 failed 252d-break"""
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    fcnt63 = fail.rolling(QDAYS, min_periods=MDAYS).sum()
    cond1 = fcnt63 >= 2
    arr_h = high.values
    arr_c = close.values
    arr_p = pm.values
    n = len(arr_c)
    is_fail_v = fail.values
    nonrecov_evt = np.zeros(n, dtype=float)
    nonrecov_evt[:] = np.nan
    for i in range(n):
        if np.isnan(arr_p[i]):
            continue
        if is_fail_v[i] > 0:
            lvl = arr_p[i]
            upper = min(n - 1, i + MDAYS)
            seg = arr_c[i + 1:upper + 1]
            seg = seg[~np.isnan(seg)]
            if seg.size == 0:
                nonrecov_evt[i] = 0.0
            else:
                nonrecov_evt[i] = 1.0 if seg.max() < lvl else 0.0
        else:
            nonrecov_evt[i] = 0.0
    nonrec_recent = pd.Series(nonrecov_evt, index=high.index).shift(MDAYS).rolling(QDAYS, min_periods=MDAYS).max() > 0
    atr = _atr(high, low, close, n=MDAYS)
    over = _safe_div(high - pm, atr)
    sev_mean = over.where(fail > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    vz = _rolling_zscore(volume, YDAYS)
    vw_sum = (vz * fail).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(fcnt63, DDAYS_2Y, min_periods=YDAYS).fillna(0)
    z2 = _rolling_zscore(sev_mean, DDAYS_2Y, min_periods=YDAYS).fillna(0)
    z3 = _rolling_zscore(vw_sum, DDAYS_2Y, min_periods=YDAYS).fillna(0)
    score = 0.4 * z1 + 0.3 * z2 + 0.3 * z3
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size)
    rk = score.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    cond3 = rk >= 0.9
    out = (cond1.fillna(False) & nonrec_recent.fillna(False) & cond3.fillna(False)).astype(float)
    return out.where(pm.notna() & rk.notna(), np.nan)



def f05_fbkd_076_breakout_day_vol_vs_21d_mean_at_252d_fail_d2(high, close, volume):
    return f05_fbkd_076_breakout_day_vol_vs_21d_mean_at_252d_fail(high, close, volume).diff().diff()


def f05_fbkd_077_high_vol_low_progress_false_break_252d_d2(high, low, close, volume):
    return f05_fbkd_077_high_vol_low_progress_false_break_252d(high, low, close, volume).diff().diff()


def f05_fbkd_078_volume_on_failback_move_vs_breakout_d2(high, close, volume):
    return f05_fbkd_078_volume_on_failback_move_vs_breakout(high, close, volume).diff().diff()


def f05_fbkd_079_volume_zscore_at_252d_fail_d2(high, close, volume):
    return f05_fbkd_079_volume_zscore_at_252d_fail(high, close, volume).diff().diff()


def f05_fbkd_080_dollar_volume_fail_severity_252d_d2(high, close, volume):
    return f05_fbkd_080_dollar_volume_fail_severity_252d(high, close, volume).diff().diff()


def f05_fbkd_081_low_volume_252d_break_count_252d_d2(high, close, volume):
    return f05_fbkd_081_low_volume_252d_break_count_252d(high, close, volume).diff().diff()


def f05_fbkd_082_vol_ratio_at_intraday_pierce_vs_pre_252d_d2(high, close, volume):
    return f05_fbkd_082_vol_ratio_at_intraday_pierce_vs_pre_252d(high, close, volume).diff().diff()


def f05_fbkd_083_obv_divergence_at_252d_fail_d2(close, volume, high):
    return f05_fbkd_083_obv_divergence_at_252d_fail(close, volume, high).diff().diff()


def f05_fbkd_084_cum_vol_above_broken_252d_pre_fail_d2(high, close, volume):
    return f05_fbkd_084_cum_vol_above_broken_252d_pre_fail(high, close, volume).diff().diff()


def f05_fbkd_085_vol_weighted_failed_breaks_252d_d2(high, close, volume):
    return f05_fbkd_085_vol_weighted_failed_breaks_252d(high, close, volume).diff().diff()


def f05_fbkd_086_vol_climax_into_failed_break_5d_252d_d2(high, close, volume):
    return f05_fbkd_086_vol_climax_into_failed_break_5d_252d(high, close, volume).diff().diff()


def f05_fbkd_087_avg_relative_vol_at_failed_breaks_252d_d2(high, close, volume):
    return f05_fbkd_087_avg_relative_vol_at_failed_breaks_252d(high, close, volume).diff().diff()


def f05_fbkd_088_short_dwell_trap_under_3d_count_252d_d2(high, close):
    return f05_fbkd_088_short_dwell_trap_under_3d_count_252d(high, close).diff().diff()


def f05_fbkd_089_extended_dwell_trap_over_10d_count_252d_d2(high, close):
    return f05_fbkd_089_extended_dwell_trap_over_10d_count_252d(high, close).diff().diff()


def f05_fbkd_090_mean_dwell_above_at_failed_breaks_252d_d2(high, close):
    return f05_fbkd_090_mean_dwell_above_at_failed_breaks_252d(high, close).diff().diff()


def f05_fbkd_091_max_dwell_above_at_failed_breaks_252d_d2(high, close):
    return f05_fbkd_091_max_dwell_above_at_failed_breaks_252d(high, close).diff().diff()


def f05_fbkd_092_dwell_duration_variance_failed_252d_d2(high, close):
    return f05_fbkd_092_dwell_duration_variance_failed_252d(high, close).diff().diff()


def f05_fbkd_093_bars_between_consecutive_252d_fails_avg_252d_d2(high, close):
    return f05_fbkd_093_bars_between_consecutive_252d_fails_avg_252d(high, close).diff().diff()


def f05_fbkd_094_dwell_above_persistence_streak_above_252d_d2(high, close):
    return f05_fbkd_094_dwell_above_persistence_streak_above_252d(high, close).diff().diff()


def f05_fbkd_095_failed_downside_break_21d_low_count_252d_d2(low, close):
    return f05_fbkd_095_failed_downside_break_21d_low_count_252d(low, close).diff().diff()


def f05_fbkd_096_failed_downside_break_63d_low_count_252d_d2(low, close):
    return f05_fbkd_096_failed_downside_break_63d_low_count_252d(low, close).diff().diff()


def f05_fbkd_097_failed_downside_break_252d_low_count_504d_d2(low, close):
    return f05_fbkd_097_failed_downside_break_252d_low_count_504d(low, close).diff().diff()


def f05_fbkd_098_failed_downside_break_at_252d_high_indicator_d2(high, low, close):
    return f05_fbkd_098_failed_downside_break_at_252d_high_indicator(high, low, close).diff().diff()


def f05_fbkd_099_squeeze_recovery_after_failed_down_break_5d_d2(low, close):
    return f05_fbkd_099_squeeze_recovery_after_failed_down_break_5d(low, close).diff().diff()


def f05_fbkd_100_attempt_vs_success_ratio_21d_low_break_252d_d2(low, close):
    return f05_fbkd_100_attempt_vs_success_ratio_21d_low_break_252d(low, close).diff().diff()


def f05_fbkd_101_bear_trap_severity_lower_wick_atr_d2(low, high, close, open_):
    return f05_fbkd_101_bear_trap_severity_lower_wick_atr(low, high, close, open_).diff().diff()


def f05_fbkd_102_bear_trap_then_failed_top_within_21d_d2(high, low, close):
    return f05_fbkd_102_bear_trap_then_failed_top_within_21d(high, low, close).diff().diff()


def f05_fbkd_103_composite_trap_density_index_252d_d2(high, close):
    return f05_fbkd_103_composite_trap_density_index_252d(high, close).diff().diff()


def f05_fbkd_104_weighted_severity_sum_failed_252d_atr_d2(high, low, close):
    return f05_fbkd_104_weighted_severity_sum_failed_252d_atr(high, low, close).diff().diff()


def f05_fbkd_105_trap_breadth_top_quintile_indicator_d2(high, close):
    return f05_fbkd_105_trap_breadth_top_quintile_indicator(high, close).diff().diff()


def f05_fbkd_106_simultaneous_multi_anchor_fail_count_5d_d2(high, close):
    return f05_fbkd_106_simultaneous_multi_anchor_fail_count_5d(high, close).diff().diff()


def f05_fbkd_107_recency_weighted_trap_count_252d_d2(high, close):
    return f05_fbkd_107_recency_weighted_trap_count_252d(high, close).diff().diff()


def f05_fbkd_108_trap_count_acceleration_recent_minus_prior_d2(high, close):
    return f05_fbkd_108_trap_count_acceleration_recent_minus_prior(high, close).diff().diff()


def f05_fbkd_109_avg_overshoot_atr_at_252d_fails_252d_d2(high, low, close):
    return f05_fbkd_109_avg_overshoot_atr_at_252d_fails_252d(high, low, close).diff().diff()


def f05_fbkd_110_max_severity_trap_252d_atr_d2(high, low, close):
    return f05_fbkd_110_max_severity_trap_252d_atr(high, low, close).diff().diff()


def f05_fbkd_111_min_time_to_fail_252d_breaks_252d_d2(high, close):
    return f05_fbkd_111_min_time_to_fail_252d_breaks_252d(high, close).diff().diff()


def f05_fbkd_112_dispersion_severity_failed_252d_d2(high, low, close):
    return f05_fbkd_112_dispersion_severity_failed_252d(high, low, close).diff().diff()


def f05_fbkd_113_proportion_failed_vs_total_breaks_252d_d2(high, close):
    return f05_fbkd_113_proportion_failed_vs_total_breaks_252d(high, close).diff().diff()


def f05_fbkd_114_normalized_trap_pressure_score_252d_d2(high, low, close, volume):
    return f05_fbkd_114_normalized_trap_pressure_score_252d(high, low, close, volume).diff().diff()


def f05_fbkd_115_trap_pressure_top_decile_indicator_504d_d2(high, low, close, volume):
    return f05_fbkd_115_trap_pressure_top_decile_indicator_504d(high, low, close, volume).diff().diff()


def f05_fbkd_116_alltime_high_break_then_failure_within_21d_d2(high, close):
    return f05_fbkd_116_alltime_high_break_then_failure_within_21d(high, close).diff().diff()


def f05_fbkd_117_failed_break_round_25_pct_severity_252d_d2(high, close):
    return f05_fbkd_117_failed_break_round_25_pct_severity_252d(high, close).diff().diff()


def f05_fbkd_118_round_number_density_repeated_failure_252d_d2(high, close):
    return f05_fbkd_118_round_number_density_repeated_failure_252d(high, close).diff().diff()


def f05_fbkd_119_approach_to_round_100_within_2pct_count_63d_d2(high, close):
    return f05_fbkd_119_approach_to_round_100_within_2pct_count_63d(high, close).diff().diff()


def f05_fbkd_120_approach_to_round_50_within_2pct_count_63d_d2(high, close):
    return f05_fbkd_120_approach_to_round_50_within_2pct_count_63d(high, close).diff().diff()


def f05_fbkd_121_failed_break_round_5_pct_252d_d2(high, close):
    return f05_fbkd_121_failed_break_round_5_pct_252d(high, close).diff().diff()


def f05_fbkd_122_distance_to_next_round_100_close_d2(close):
    return f05_fbkd_122_distance_to_next_round_100_close(close).diff().diff()


def f05_fbkd_123_distance_to_next_round_25_close_d2(close):
    return f05_fbkd_123_distance_to_next_round_25_close(close).diff().diff()


def f05_fbkd_124_distance_to_next_round_10_close_d2(close):
    return f05_fbkd_124_distance_to_next_round_10_close(close).diff().diff()


def f05_fbkd_125_round_100_clinginess_5d_d2(close):
    return f05_fbkd_125_round_100_clinginess_5d(close).diff().diff()


def f05_fbkd_126_failed_break_round_high_then_collapse_5d_pct_d2(open_, high, low, close):
    return f05_fbkd_126_failed_break_round_high_then_collapse_5d_pct(open_, high, low, close).diff().diff()


def f05_fbkd_127_failed_secular_high_3y_756d_d2(high, close):
    return f05_fbkd_127_failed_secular_high_3y_756d(high, close).diff().diff()


def f05_fbkd_128_lifetime_ath_overshoot_failed_count_d2(high, close):
    return f05_fbkd_128_lifetime_ath_overshoot_failed_count(high, close).diff().diff()


def f05_fbkd_129_bars_in_failed_break_state_252d_d2(high, close):
    return f05_fbkd_129_bars_in_failed_break_state_252d(high, close).diff().diff()


def f05_fbkd_130_breakout_then_fail_event_504d_distinct_levels_d2(high, close):
    return f05_fbkd_130_breakout_then_fail_event_504d_distinct_levels(high, close).diff().diff()


def f05_fbkd_131_max_close_above_then_drop_below_252d_d2(high, close):
    return f05_fbkd_131_max_close_above_then_drop_below_252d(high, close).diff().diff()


def f05_fbkd_132_first_fail_after_lifetime_high_within_21d_d2(high, close):
    return f05_fbkd_132_first_fail_after_lifetime_high_within_21d(high, close).diff().diff()


def f05_fbkd_133_fraction_252d_above_then_below_breakout_level_d2(high, close):
    return f05_fbkd_133_fraction_252d_above_then_below_breakout_level(high, close).diff().diff()


def f05_fbkd_134_cycle_break_failure_ratio_3y_d2(high, close):
    return f05_fbkd_134_cycle_break_failure_ratio_3y(high, close).diff().diff()


def f05_fbkd_135_terminal_failed_break_no_recovery_63d_d2(high, close):
    return f05_fbkd_135_terminal_failed_break_no_recovery_63d(high, close).diff().diff()


def f05_fbkd_136_post_failure_trajectory_slope_21d_d2(high, close):
    return f05_fbkd_136_post_failure_trajectory_slope_21d(high, close).diff().diff()


def f05_fbkd_137_breakout_then_within_atr_of_level_after_5d_d2(high, low, close):
    return f05_fbkd_137_breakout_then_within_atr_of_level_after_5d(high, low, close).diff().diff()


def f05_fbkd_138_failed_break_to_below_50sma_within_10d_d2(high, close):
    return f05_fbkd_138_failed_break_to_below_50sma_within_10d(high, close).diff().diff()


def f05_fbkd_139_failed_break_to_below_200sma_within_21d_d2(high, close):
    return f05_fbkd_139_failed_break_to_below_200sma_within_21d(high, close).diff().diff()


def f05_fbkd_140_trap_cascade_count_252d_d2(high, close):
    return f05_fbkd_140_trap_cascade_count_252d(high, close).diff().diff()


def f05_fbkd_141_failed_break_bar_severity_composite_d2(open_, high, low, close, volume):
    return f05_fbkd_141_failed_break_bar_severity_composite(open_, high, low, close, volume).diff().diff()


def f05_fbkd_142_failed_break_recency_decay_score_252d_d2(high, close):
    return f05_fbkd_142_failed_break_recency_decay_score_252d(high, close).diff().diff()


def f05_fbkd_143_avg_fail_severity_pct_252d_d2(high, close):
    return f05_fbkd_143_avg_fail_severity_pct_252d(high, close).diff().diff()


def f05_fbkd_144_post_trap_recovery_failure_count_63d_d2(high, close):
    return f05_fbkd_144_post_trap_recovery_failure_count_63d(high, close).diff().diff()


def f05_fbkd_145_no_recovery_trap_severity_atr_63d_d2(high, low, close):
    return f05_fbkd_145_no_recovery_trap_severity_atr_63d(high, low, close).diff().diff()


def f05_fbkd_146_top_trap_episode_indicator_5y_d2(high, low, close, volume):
    return f05_fbkd_146_top_trap_episode_indicator_5y(high, low, close, volume).diff().diff()


def f05_fbkd_147_failed_break_vs_succeed_volume_ratio_252d_d2(high, close, volume):
    return f05_fbkd_147_failed_break_vs_succeed_volume_ratio_252d(high, close, volume).diff().diff()


def f05_fbkd_148_clustering_index_failed_breaks_252d_d2(high, close):
    return f05_fbkd_148_clustering_index_failed_breaks_252d(high, close).diff().diff()


def f05_fbkd_149_extreme_failed_break_count_top_1pct_severity_504d_d2(high, low, close):
    return f05_fbkd_149_extreme_failed_break_count_top_1pct_severity_504d(high, low, close).diff().diff()


def f05_fbkd_150_composite_terminal_trap_state_indicator_d2(high, low, close, volume):
    return f05_fbkd_150_composite_terminal_trap_state_indicator(high, low, close, volume).diff().diff()


FAILED_BREAKOUT_DYNAMICS_D2_REGISTRY_076_150 = {
    "f05_fbkd_076_breakout_day_vol_vs_21d_mean_at_252d_fail_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_076_breakout_day_vol_vs_21d_mean_at_252d_fail_d2},
    "f05_fbkd_077_high_vol_low_progress_false_break_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_077_high_vol_low_progress_false_break_252d_d2},
    "f05_fbkd_078_volume_on_failback_move_vs_breakout_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_078_volume_on_failback_move_vs_breakout_d2},
    "f05_fbkd_079_volume_zscore_at_252d_fail_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_079_volume_zscore_at_252d_fail_d2},
    "f05_fbkd_080_dollar_volume_fail_severity_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_080_dollar_volume_fail_severity_252d_d2},
    "f05_fbkd_081_low_volume_252d_break_count_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_081_low_volume_252d_break_count_252d_d2},
    "f05_fbkd_082_vol_ratio_at_intraday_pierce_vs_pre_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_082_vol_ratio_at_intraday_pierce_vs_pre_252d_d2},
    "f05_fbkd_083_obv_divergence_at_252d_fail_d2": {"inputs": ["close", "volume", "high"], "func": f05_fbkd_083_obv_divergence_at_252d_fail_d2},
    "f05_fbkd_084_cum_vol_above_broken_252d_pre_fail_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_084_cum_vol_above_broken_252d_pre_fail_d2},
    "f05_fbkd_085_vol_weighted_failed_breaks_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_085_vol_weighted_failed_breaks_252d_d2},
    "f05_fbkd_086_vol_climax_into_failed_break_5d_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_086_vol_climax_into_failed_break_5d_252d_d2},
    "f05_fbkd_087_avg_relative_vol_at_failed_breaks_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_087_avg_relative_vol_at_failed_breaks_252d_d2},
    "f05_fbkd_088_short_dwell_trap_under_3d_count_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_088_short_dwell_trap_under_3d_count_252d_d2},
    "f05_fbkd_089_extended_dwell_trap_over_10d_count_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_089_extended_dwell_trap_over_10d_count_252d_d2},
    "f05_fbkd_090_mean_dwell_above_at_failed_breaks_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_090_mean_dwell_above_at_failed_breaks_252d_d2},
    "f05_fbkd_091_max_dwell_above_at_failed_breaks_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_091_max_dwell_above_at_failed_breaks_252d_d2},
    "f05_fbkd_092_dwell_duration_variance_failed_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_092_dwell_duration_variance_failed_252d_d2},
    "f05_fbkd_093_bars_between_consecutive_252d_fails_avg_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_093_bars_between_consecutive_252d_fails_avg_252d_d2},
    "f05_fbkd_094_dwell_above_persistence_streak_above_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_094_dwell_above_persistence_streak_above_252d_d2},
    "f05_fbkd_095_failed_downside_break_21d_low_count_252d_d2": {"inputs": ["low", "close"], "func": f05_fbkd_095_failed_downside_break_21d_low_count_252d_d2},
    "f05_fbkd_096_failed_downside_break_63d_low_count_252d_d2": {"inputs": ["low", "close"], "func": f05_fbkd_096_failed_downside_break_63d_low_count_252d_d2},
    "f05_fbkd_097_failed_downside_break_252d_low_count_504d_d2": {"inputs": ["low", "close"], "func": f05_fbkd_097_failed_downside_break_252d_low_count_504d_d2},
    "f05_fbkd_098_failed_downside_break_at_252d_high_indicator_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_098_failed_downside_break_at_252d_high_indicator_d2},
    "f05_fbkd_099_squeeze_recovery_after_failed_down_break_5d_d2": {"inputs": ["low", "close"], "func": f05_fbkd_099_squeeze_recovery_after_failed_down_break_5d_d2},
    "f05_fbkd_100_attempt_vs_success_ratio_21d_low_break_252d_d2": {"inputs": ["low", "close"], "func": f05_fbkd_100_attempt_vs_success_ratio_21d_low_break_252d_d2},
    "f05_fbkd_101_bear_trap_severity_lower_wick_atr_d2": {"inputs": ["low", "high", "close", "open"], "func": f05_fbkd_101_bear_trap_severity_lower_wick_atr_d2},
    "f05_fbkd_102_bear_trap_then_failed_top_within_21d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_102_bear_trap_then_failed_top_within_21d_d2},
    "f05_fbkd_103_composite_trap_density_index_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_103_composite_trap_density_index_252d_d2},
    "f05_fbkd_104_weighted_severity_sum_failed_252d_atr_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_104_weighted_severity_sum_failed_252d_atr_d2},
    "f05_fbkd_105_trap_breadth_top_quintile_indicator_d2": {"inputs": ["high", "close"], "func": f05_fbkd_105_trap_breadth_top_quintile_indicator_d2},
    "f05_fbkd_106_simultaneous_multi_anchor_fail_count_5d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_106_simultaneous_multi_anchor_fail_count_5d_d2},
    "f05_fbkd_107_recency_weighted_trap_count_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_107_recency_weighted_trap_count_252d_d2},
    "f05_fbkd_108_trap_count_acceleration_recent_minus_prior_d2": {"inputs": ["high", "close"], "func": f05_fbkd_108_trap_count_acceleration_recent_minus_prior_d2},
    "f05_fbkd_109_avg_overshoot_atr_at_252d_fails_252d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_109_avg_overshoot_atr_at_252d_fails_252d_d2},
    "f05_fbkd_110_max_severity_trap_252d_atr_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_110_max_severity_trap_252d_atr_d2},
    "f05_fbkd_111_min_time_to_fail_252d_breaks_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_111_min_time_to_fail_252d_breaks_252d_d2},
    "f05_fbkd_112_dispersion_severity_failed_252d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_112_dispersion_severity_failed_252d_d2},
    "f05_fbkd_113_proportion_failed_vs_total_breaks_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_113_proportion_failed_vs_total_breaks_252d_d2},
    "f05_fbkd_114_normalized_trap_pressure_score_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_114_normalized_trap_pressure_score_252d_d2},
    "f05_fbkd_115_trap_pressure_top_decile_indicator_504d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_115_trap_pressure_top_decile_indicator_504d_d2},
    "f05_fbkd_116_alltime_high_break_then_failure_within_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_116_alltime_high_break_then_failure_within_21d_d2},
    "f05_fbkd_117_failed_break_round_25_pct_severity_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_117_failed_break_round_25_pct_severity_252d_d2},
    "f05_fbkd_118_round_number_density_repeated_failure_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_118_round_number_density_repeated_failure_252d_d2},
    "f05_fbkd_119_approach_to_round_100_within_2pct_count_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_119_approach_to_round_100_within_2pct_count_63d_d2},
    "f05_fbkd_120_approach_to_round_50_within_2pct_count_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_120_approach_to_round_50_within_2pct_count_63d_d2},
    "f05_fbkd_121_failed_break_round_5_pct_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_121_failed_break_round_5_pct_252d_d2},
    "f05_fbkd_122_distance_to_next_round_100_close_d2": {"inputs": ["close"], "func": f05_fbkd_122_distance_to_next_round_100_close_d2},
    "f05_fbkd_123_distance_to_next_round_25_close_d2": {"inputs": ["close"], "func": f05_fbkd_123_distance_to_next_round_25_close_d2},
    "f05_fbkd_124_distance_to_next_round_10_close_d2": {"inputs": ["close"], "func": f05_fbkd_124_distance_to_next_round_10_close_d2},
    "f05_fbkd_125_round_100_clinginess_5d_d2": {"inputs": ["close"], "func": f05_fbkd_125_round_100_clinginess_5d_d2},
    "f05_fbkd_126_failed_break_round_high_then_collapse_5d_pct_d2": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_126_failed_break_round_high_then_collapse_5d_pct_d2},
    "f05_fbkd_127_failed_secular_high_3y_756d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_127_failed_secular_high_3y_756d_d2},
    "f05_fbkd_128_lifetime_ath_overshoot_failed_count_d2": {"inputs": ["high", "close"], "func": f05_fbkd_128_lifetime_ath_overshoot_failed_count_d2},
    "f05_fbkd_129_bars_in_failed_break_state_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_129_bars_in_failed_break_state_252d_d2},
    "f05_fbkd_130_breakout_then_fail_event_504d_distinct_levels_d2": {"inputs": ["high", "close"], "func": f05_fbkd_130_breakout_then_fail_event_504d_distinct_levels_d2},
    "f05_fbkd_131_max_close_above_then_drop_below_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_131_max_close_above_then_drop_below_252d_d2},
    "f05_fbkd_132_first_fail_after_lifetime_high_within_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_132_first_fail_after_lifetime_high_within_21d_d2},
    "f05_fbkd_133_fraction_252d_above_then_below_breakout_level_d2": {"inputs": ["high", "close"], "func": f05_fbkd_133_fraction_252d_above_then_below_breakout_level_d2},
    "f05_fbkd_134_cycle_break_failure_ratio_3y_d2": {"inputs": ["high", "close"], "func": f05_fbkd_134_cycle_break_failure_ratio_3y_d2},
    "f05_fbkd_135_terminal_failed_break_no_recovery_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_135_terminal_failed_break_no_recovery_63d_d2},
    "f05_fbkd_136_post_failure_trajectory_slope_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_136_post_failure_trajectory_slope_21d_d2},
    "f05_fbkd_137_breakout_then_within_atr_of_level_after_5d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_137_breakout_then_within_atr_of_level_after_5d_d2},
    "f05_fbkd_138_failed_break_to_below_50sma_within_10d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_138_failed_break_to_below_50sma_within_10d_d2},
    "f05_fbkd_139_failed_break_to_below_200sma_within_21d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_139_failed_break_to_below_200sma_within_21d_d2},
    "f05_fbkd_140_trap_cascade_count_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_140_trap_cascade_count_252d_d2},
    "f05_fbkd_141_failed_break_bar_severity_composite_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_fbkd_141_failed_break_bar_severity_composite_d2},
    "f05_fbkd_142_failed_break_recency_decay_score_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_142_failed_break_recency_decay_score_252d_d2},
    "f05_fbkd_143_avg_fail_severity_pct_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_143_avg_fail_severity_pct_252d_d2},
    "f05_fbkd_144_post_trap_recovery_failure_count_63d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_144_post_trap_recovery_failure_count_63d_d2},
    "f05_fbkd_145_no_recovery_trap_severity_atr_63d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_145_no_recovery_trap_severity_atr_63d_d2},
    "f05_fbkd_146_top_trap_episode_indicator_5y_d2": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_146_top_trap_episode_indicator_5y_d2},
    "f05_fbkd_147_failed_break_vs_succeed_volume_ratio_252d_d2": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_147_failed_break_vs_succeed_volume_ratio_252d_d2},
    "f05_fbkd_148_clustering_index_failed_breaks_252d_d2": {"inputs": ["high", "close"], "func": f05_fbkd_148_clustering_index_failed_breaks_252d_d2},
    "f05_fbkd_149_extreme_failed_break_count_top_1pct_severity_504d_d2": {"inputs": ["high", "low", "close"], "func": f05_fbkd_149_extreme_failed_break_count_top_1pct_severity_504d_d2},
    "f05_fbkd_150_composite_terminal_trap_state_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_150_composite_terminal_trap_state_indicator_d2},
}
