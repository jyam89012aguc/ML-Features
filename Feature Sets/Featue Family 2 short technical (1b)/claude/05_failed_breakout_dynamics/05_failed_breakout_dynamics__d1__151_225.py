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


def _failed_break_mask(high, close, win, min_periods):
    pm = high.shift(1).rolling(win, min_periods=min_periods).max()
    return (high > pm) & (close < pm) & pm.notna(), pm



def f05_fbkd_151_wyckoff_utad_signature_252d(high, low, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > pm
    rng = high - low
    rng_mean = rng.rolling(50, min_periods=MDAYS).mean()
    rng_std = rng.rolling(50, min_periods=MDAYS).std()
    wide = rng > (rng_mean + 2.0 * rng_std)
    pos = _safe_div(close - low, high - low)
    weak_close = pos <= 0.25
    vol_mean = volume.rolling(50, min_periods=MDAYS).mean()
    big_vol = volume > 2.0 * vol_mean
    sig = (new_high & wide & weak_close & big_vol).astype(float)
    return sig.where(pm.notna() & rng_std.notna() & vol_mean.notna(), np.nan)


def f05_fbkd_152_wyckoff_spring_then_utad_within_63d(high, low, close, volume):
    pm_low = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    spring = ((low < pm_low) & (close > pm_low)).astype(float)
    pm_hi = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    pos = _safe_div(close - low, high - low)
    utad = ((high > pm_hi) & (pos <= 0.30)).astype(float)
    had_spring = spring.rolling(QDAYS, min_periods=MDAYS).sum() > 0
    return (utad.where(had_spring, 0.0)).where(pm_low.notna() & pm_hi.notna(), np.nan)


def f05_fbkd_153_wyckoff_sow_after_buying_climax_21d(high, low, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    rng = high - low
    rng_z = _rolling_zscore(rng, 50)
    vol_z = _rolling_zscore(volume, 50)
    bc = ((high > pm) & (rng_z > 2.0) & (vol_z > 2.0)).astype(float)
    had_bc = bc.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    down_wide = ((close < close.shift(1)) & (rng_z > 1.5)).astype(float)
    return down_wide.where(had_bc, 0.0).where(pm.notna() & rng_z.notna(), np.nan)


def f05_fbkd_154_cup_handle_failure_oneill_proxy(high, low, close):
    win = 60
    rmax_base = high.shift(11).rolling(win, min_periods=20).max()
    rmin_base = low.shift(11).rolling(win, min_periods=20).min()
    base_depth = _safe_div(rmax_base - rmin_base, rmax_base)
    handle_max = high.shift(1).rolling(10, min_periods=3).max()
    handle_min = low.shift(1).rolling(10, min_periods=3).min()
    handle_depth = _safe_div(handle_max - handle_min, handle_max)
    valid_handle = (handle_depth <= 0.12 * base_depth.clip(lower=0.05)) & (base_depth > 0.10)
    broke_past = ((close.shift(10) > handle_max.shift(10)) & valid_handle.shift(10)).fillna(False)
    failed_now = broke_past & (close < handle_min.shift(10))
    return failed_now.astype(float).where(base_depth.notna() & handle_max.notna(), np.nan)


def f05_fbkd_155_high_tight_flag_failure_oneill(high, low, close):
    gain_8wk = _safe_div(close.shift(25) - close.shift(65), close.shift(65))
    base_max = high.shift(11).rolling(20, min_periods=10).max()
    base_min = low.shift(11).rolling(20, min_periods=10).min()
    cons_depth = _safe_div(base_max - base_min, base_max)
    valid = (gain_8wk > 1.0) & (cons_depth < 0.25)
    broke_past = ((close.shift(10) > base_max.shift(10)) & valid.shift(10)).fillna(False)
    failed = broke_past & (close < base_max.shift(10))
    return failed.astype(float).where(gain_8wk.notna() & base_max.notna(), np.nan)


def f05_fbkd_156_ascending_triangle_apex_failure_63d(high, low, close):
    flat_top = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    flat_std = high.shift(1).rolling(QDAYS, min_periods=MDAYS).std()
    flat = _safe_div(flat_std, flat_top) < 0.02
    low_slope = _rolling_slope(low, QDAYS)
    rising = low_slope > 0
    broke_past = ((close.shift(5) > flat_top.shift(5)) & flat.shift(5) & rising.shift(5)).fillna(False)
    failed = broke_past & (close < flat_top.shift(5))
    return failed.astype(float).where(flat_top.notna() & low_slope.notna(), np.nan)


def f05_fbkd_157_rising_wedge_failure_252d(high, low, close):
    hs = _rolling_slope(high, QDAYS)
    ls = _rolling_slope(low, QDAYS)
    wedge = (hs > 0) & (ls > 0) & (hs < ls)
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    broke_past = ((high.shift(WDAYS) > pm.shift(WDAYS)) & wedge.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < pm.shift(WDAYS))
    return failed.astype(float).where(pm.notna() & hs.notna(), np.nan)


def f05_fbkd_158_bear_pennant_breakout_failure_post_rally(high, low, close):
    rally = _safe_div(close - close.shift(21), close.shift(21)) > 0.20
    near_high = close >= 0.95 * high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    rng_recent = (high - low).rolling(10, min_periods=3).mean()
    rng_prior = (high - low).shift(10).rolling(10, min_periods=3).mean()
    pennant = (rng_recent < 0.6 * rng_prior) & rally & near_high
    pm = high.shift(1).rolling(10, min_periods=3).max()
    broke_past = ((high.shift(WDAYS) > pm.shift(WDAYS)) & pennant.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < pm.shift(WDAYS))
    return failed.astype(float).where(pm.notna() & pennant.notna(), np.nan)


def f05_fbkd_159_bollinger_squeeze_release_failure_20d(high, close):
    n = 20
    m = close.rolling(n, min_periods=10).mean()
    sd = close.rolling(n, min_periods=10).std()
    upper = m + 2.0 * sd
    width = _safe_div(4.0 * sd, m)
    width_pctl = width.rolling(126, min_periods=QDAYS).rank(pct=True)
    squeeze = width_pctl <= 0.10
    broke_past = ((close.shift(WDAYS) > upper.shift(WDAYS)) & squeeze.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < upper.shift(WDAYS))
    return failed.astype(float).where(upper.notna() & width_pctl.notna(), np.nan)


def f05_fbkd_160_keltner_squeeze_failure_20d(high, low, close):
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    bb_upper = m + 2.0 * sd
    bb_lower = m - 2.0 * sd
    atr21 = _atr(high, low, close, n=MDAYS)
    kc_upper = m + 1.5 * atr21
    kc_lower = m - 1.5 * atr21
    squeeze = (kc_upper < bb_upper) & (kc_lower > bb_lower)
    broke_past = ((close.shift(3) > bb_upper.shift(3)) & squeeze.shift(3)).fillna(False)
    failed = broke_past & (close < bb_upper.shift(3))
    return failed.astype(float).where(bb_upper.notna() & kc_upper.notna(), np.nan)



def _rolling_anchored_vwap_from_low(high, low, close, volume, win):
    typ = (high + low + close) / 3.0
    pv = typ * volume
    lo_arr = low.values
    pv_arr = pv.values
    v_arr = volume.values
    n = len(lo_arr)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - win + 1)
        seg = lo_arr[lo:i + 1]
        if np.isnan(seg).all():
            continue
        j_local = int(np.nanargmin(seg))
        anchor = lo + j_local
        pv_sum = np.nansum(pv_arr[anchor:i + 1])
        v_sum = np.nansum(v_arr[anchor:i + 1])
        if v_sum > 0:
            out[i] = pv_sum / v_sum
    return pd.Series(out, index=close.index)


def f05_fbkd_161_anchored_vwap_from_252d_low_failure(high, low, close, volume):
    avwap = _rolling_anchored_vwap_from_low(high, low, close, volume, YDAYS)
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    near_top = close >= 0.95 * pm
    broke_past = ((close.shift(WDAYS) > avwap.shift(WDAYS)) & near_top.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < avwap.shift(WDAYS))
    return failed.astype(float).where(avwap.notna() & pm.notna(), np.nan)


def f05_fbkd_162_anchored_vwap_from_prior_ath_rejection(high, low, close, volume):
    typ = (high + low + close) / 3.0
    pv = typ * volume
    hi_arr = high.values
    pv_arr = pv.values
    v_arr = volume.values
    n = len(hi_arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_idx = -1
    pv_sum = 0.0
    v_sum = 0.0
    for i in range(n):
        v = hi_arr[i]
        if not np.isnan(v) and v >= cur_max:
            cur_max = v
            cur_idx = i
            pv_sum = pv_arr[i] if not np.isnan(pv_arr[i]) else 0.0
            v_sum = v_arr[i] if not np.isnan(v_arr[i]) else 0.0
        else:
            if cur_idx >= 0:
                if not np.isnan(pv_arr[i]):
                    pv_sum += pv_arr[i]
                if not np.isnan(v_arr[i]):
                    v_sum += v_arr[i]
        if v_sum > 0 and cur_idx >= 0:
            out[i] = pv_sum / v_sum
    avwap = pd.Series(out, index=close.index)
    broke_past = (close.shift(WDAYS) > avwap.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < avwap.shift(WDAYS))
    return failed.astype(float).where(avwap.notna(), np.nan)


def f05_fbkd_163_hl2_pierce_only_252d_high_count(high, low):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    hl2 = (high + low) / 2.0
    weak = ((high > pm) & (hl2 < pm)).astype(float)
    return weak.rolling(YDAYS, min_periods=QDAYS).sum().where(pm.notna(), np.nan)


def f05_fbkd_164_typical_price_pierce_252d_failure(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    typ = (high + low + close) / 3.0
    broke_past = (typ.shift(3) > pm.shift(3)).fillna(False)
    failed = broke_past & (typ < pm.shift(3))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_165_consecutive_close_above_then_below_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    above = close > pm
    two_above = above & above.shift(1)
    confirm_past = two_above.shift(3).fillna(False)
    failed = confirm_past & (close < pm.shift(3))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_166_three_close_confirmation_failure_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    above = close > pm
    three_above = above & above.shift(1) & above.shift(2)
    confirm_past = three_above.shift(WDAYS).fillna(False)
    failed = confirm_past & (close < pm.shift(WDAYS))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_167_failure_rate_by_full_gap_breakout(open_, high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    full_gap = (open_ > pm) & (high > pm)
    full_gap_past = full_gap.shift(10).fillna(False)
    failed = full_gap_past & (close < pm.shift(10))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_168_failure_rate_by_partial_gap_breakout(open_, high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    partial_gap = (open_ <= pm) & (open_ > close.shift(1)) & (high > pm)
    pg_past = partial_gap.shift(10).fillna(False)
    failed = pg_past & (close < pm.shift(10))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_169_failure_rate_by_no_gap_breakout(open_, high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    no_gap = (open_ < pm) & (high > pm)
    ng_past = no_gap.shift(10).fillna(False)
    failed = ng_past & (close < pm.shift(10))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_170_atr_expansion_at_failed_breakout_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    failed = (high > pm) & (close < pm)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    expand = failed & (tr > 2.0 * atr)
    return expand.astype(float).where(pm.notna() & atr.notna(), np.nan)



def f05_fbkd_171_slow_grind_failed_breakout_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    failed = (high > pm) & (close < pm)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    quiet = failed & (tr < 0.75 * atr)
    return quiet.astype(float).where(pm.notna() & atr.notna(), np.nan)


def _touch_count_at_resistance(high, win, tol_frac):
    rmax = high.rolling(win, min_periods=max(win // 4, 5)).max()
    near = (high >= (1.0 - tol_frac) * rmax).astype(float)
    return near.rolling(win, min_periods=max(win // 4, 5)).sum()


def f05_fbkd_172_second_touch_failure_at_252d_resistance(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * pm)
    touch_cum = near.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    failed = (high > pm) & (close < pm) & (touch_cum == 2)
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_173_third_touch_failure_at_252d_resistance(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * pm)
    touch_cum = near.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    failed = (high > pm) & (close < pm) & (touch_cum == 3)
    return failed.astype(float).where(pm.notna(), np.nan)


def _three_pushes_to_high_fail(high, close, win):
    arr_h = high.values
    arr_c = close.values
    n = len(arr_h)
    out = np.full(n, np.nan, dtype=float)
    for i in range(win, n):
        seg_h = arr_h[i - win + 1:i + 1]
        pushes = []
        for k in range(2, len(seg_h) - 2):
            if (seg_h[k] > seg_h[k - 1] and seg_h[k] > seg_h[k + 1]
                    and seg_h[k] > seg_h[k - 2] and seg_h[k] > seg_h[k + 2]):
                pushes.append((k, seg_h[k]))
        if len(pushes) >= 3:
            last3 = pushes[-3:]
            hh = last3[0][1] < last3[1][1] < last3[2][1]
            d1 = last3[1][1] - last3[0][1]
            d2 = last3[2][1] - last3[1][1]
            diminishing = d2 < d1
            failed = arr_c[i] < last3[2][1]
            if hh and diminishing and failed:
                out[i] = 1.0
            else:
                out[i] = 0.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def f05_fbkd_174_three_pushes_to_high_failure_252d(high, close):
    return _three_pushes_to_high_fail(high, close, YDAYS)


def f05_fbkd_175_upper_wick_volume_weighted_absorption_252d(high, low, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    upper_wick = (high - close.clip(lower=low)).clip(lower=0)
    failed = (high > pm) & (close < pm)
    vol_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    score = _safe_div(upper_wick * volume, vol_mean)
    return score.where(failed & pm.notna(), np.nan)


def f05_fbkd_176_coiling_time_within_half_atr_of_252d_pre_break(high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    near = (rmax - high).abs() <= 0.5 * atr
    return near.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(rmax.notna() & atr.notna(), np.nan)


def f05_fbkd_177_failed_break_inter_arrival_dispersion_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    def _cv(w):
        idx = np.where(w > 0)[0]
        if idx.size < 3:
            return np.nan
        g = np.diff(idx).astype(float)
        m = g.mean()
        if m == 0:
            return np.nan
        return float(g.std(ddof=1) / m)
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_cv, raw=True)


def f05_fbkd_178_failed_break_inter_arrival_min_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    def _min_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).min())
    return fail.rolling(YDAYS, min_periods=QDAYS).apply(_min_gap, raw=True)


def f05_fbkd_179_failure_then_confirmed_breakdown_below_63d_low_within_21d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    had_fail = fail.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    pl = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    breakdown = close < pl
    return (had_fail & breakdown).astype(float).where(pm.notna() & pl.notna(), np.nan)


def f05_fbkd_180_failure_then_range_no_breakdown_63d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    had_fail = fail.rolling(QDAYS, min_periods=MDAYS).sum() > 0
    rel = _safe_div(close - pm, pm)
    in_range = (rel >= -0.15) & (rel <= -0.02)
    stay = in_range.rolling(QDAYS, min_periods=MDAYS).mean() > 0.80
    return (had_fail & stay).astype(float).where(pm.notna(), np.nan)



def f05_fbkd_181_lppl_log_periodic_acceleration_pre_failure_252d(high, close):
    lp = _safe_log(close)
    sm = lp.rolling(WDAYS, min_periods=2).mean()
    accel = sm.diff().diff()
    detrend = lp - lp.rolling(QDAYS, min_periods=MDAYS).mean()
    amp_recent = detrend.abs().rolling(MDAYS, min_periods=WDAYS).mean()
    amp_prior = detrend.abs().shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).mean()
    diminishing = amp_recent < amp_prior
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail_recent = ((high > pm) & (close < pm)).rolling(QDAYS, min_periods=MDAYS).sum() > 0
    proxy = accel.where(diminishing & fail_recent, np.nan)
    return proxy


def f05_fbkd_182_parabolic_blowoff_then_failed_252d(high, close):
    r21 = _safe_div(close - close.shift(MDAYS), close.shift(MDAYS))
    q90 = r21.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    blowoff = r21 > 2.0 * q90
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    return (blowoff & fail).astype(float).where(pm.notna() & q90.notna(), np.nan)


def f05_fbkd_183_nr7_breakout_failure_252d(high, low, close):
    rng = high - low
    nr7 = rng == rng.rolling(7, min_periods=7).min()
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    return (fail & nr7.shift(1)).astype(float).where(pm.notna(), np.nan)


def f05_fbkd_184_inside_bar_after_break_then_breakdown_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    inside_after_fail = inside & fail.shift(1)
    inside_low_past = low.where(inside_after_fail).ffill(limit=WDAYS)
    breakdown = close < inside_low_past
    return (inside_after_fail.shift(1).fillna(False) & breakdown).astype(float).where(pm.notna(), np.nan)


def f05_fbkd_185_outside_bar_reversal_at_252d_high(high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    outside = (high > high.shift(1)) & (low < low.shift(1)) & (close < low.shift(1))
    at_high = high >= rmax
    return (outside & at_high).astype(float).where(rmax.notna(), np.nan)


def f05_fbkd_186_pocket_pivot_inversion_at_252d_high(high, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    down_day = close < close.shift(1)
    back_below = (close < pm) & (high.shift(1) > pm.shift(1))
    up_day = close > close.shift(1)
    up_vol = volume.where(up_day, 0.0)
    max_up_vol_10 = up_vol.shift(1).rolling(10, min_periods=3).max()
    inv = back_below & down_day & (volume > max_up_vol_10)
    return inv.astype(float).where(pm.notna() & max_up_vol_10.notna(), np.nan)


def f05_fbkd_187_stop_run_overshoot_percentile_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    fail = (high > pm) & (close < pm)
    overshoot = _safe_div(high - pm, atr).where(fail, np.nan)
    return overshoot.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f05_fbkd_188_failed_break_at_fib_extension_127_of_prior_swing(high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = rmin + 1.272 * (rmax - rmin)
    near = (high - fib).abs() / fib.replace(0, np.nan) <= 0.01
    failed = (high > fib) & (close < fib) & near
    return failed.astype(float).where(fib.notna(), np.nan)


def f05_fbkd_189_failed_break_at_fib_extension_162_of_prior_swing(high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = rmin + 1.618 * (rmax - rmin)
    near = (high - fib).abs() / fib.replace(0, np.nan) <= 0.01
    failed = (high > fib) & (close < fib) & near
    return failed.astype(float).where(fib.notna(), np.nan)


def f05_fbkd_190_no_demand_pre_breakout_then_failure(high, close, volume):
    v5 = volume.rolling(WDAYS, min_periods=2).mean()
    v50 = volume.rolling(50, min_periods=MDAYS).mean()
    no_demand = v5 < 0.7 * v50
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    broke_past = ((high.shift(10) > pm.shift(10)) & no_demand.shift(10)).fillna(False)
    failed = broke_past & (close < pm.shift(10))
    return failed.astype(float).where(pm.notna() & v50.notna(), np.nan)



def f05_fbkd_191_failed_break_followed_by_gap_down_breakaway_5d(open_, high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    had_fail = fail.rolling(WDAYS, min_periods=2).sum() > 0
    gap_dn = open_ < low.shift(1)
    return (had_fail & gap_dn).astype(float).where(pm.notna(), np.nan)


def f05_fbkd_192_failed_break_in_low_vol_regime_atr_pctile_bottom_25(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    atr = _atr(high, low, close, n=MDAYS)
    atr_pctl = atr.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    low_regime = atr_pctl <= 0.25
    return (fail & low_regime).astype(float).where(pm.notna() & atr_pctl.notna(), np.nan)


def f05_fbkd_193_failed_break_in_high_vol_of_vol_regime_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    atr = _atr(high, low, close, n=MDAYS)
    vov = atr.rolling(MDAYS, min_periods=WDAYS).std()
    vov_pctl = vov.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    high_regime = vov_pctl >= 0.75
    return (fail & high_regime).astype(float).where(pm.notna() & vov_pctl.notna(), np.nan)


def f05_fbkd_194_truncated_swing_failed_5th_push_252d(high, close):
    arr_h = high.values
    arr_c = close.values
    n = len(arr_h)
    out = np.full(n, np.nan, dtype=float)
    for i in range(20, n):
        seg = arr_h[i - 20:i + 1]
        pushes = []
        for k in range(2, len(seg) - 2):
            if (seg[k] > seg[k - 1] and seg[k] > seg[k + 1]
                    and seg[k] > seg[k - 2] and seg[k] > seg[k + 2]):
                pushes.append(seg[k])
        if len(pushes) >= 5:
            last5 = pushes[-5:]
            hh = all(last5[j + 1] > last5[j] for j in range(4))
            diffs = [last5[j + 1] - last5[j] for j in range(4)]
            shrinking = all(diffs[j + 1] < diffs[j] for j in range(3))
            failed = arr_c[i] < last5[-1]
            out[i] = 1.0 if (hh and shrinking and failed) else 0.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def f05_fbkd_195_failed_break_with_two_bar_reversal_at_252d(high, low, close, open_):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    strong = (high >= rmax) & (close > open_)
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1)) & (close < open_)
    sig = strong.shift(1) & engulf
    return sig.astype(float).where(rmax.notna(), np.nan)


def f05_fbkd_196_climax_thrust_then_reversal_williams_proxy(high, low, close):
    atr50 = _atr(high, low, close, n=50)
    rng = high - low
    pos = _safe_div(close - low, high - low)
    climax = (rng > 2.5 * atr50) & (pos >= 0.90)
    nxt = pos <= 0.25
    return (climax.shift(1) & nxt).astype(float).where(atr50.notna(), np.nan)


def f05_fbkd_197_failed_break_at_round_number_clinginess_5pct_severity(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    atr = _atr(high, low, close, n=MDAYS)
    rounds = [10.0, 25.0, 50.0, 100.0]
    pm_arr = pm.values
    overshoot = high - pm
    near_round = pd.Series(False, index=high.index)
    for r in rounds:
        nearest_r = (np.round(pm_arr / r) * r)
        nr = pd.Series(nearest_r, index=high.index)
        near_round = near_round | ((pm - nr).abs() / pm.replace(0, np.nan) <= 0.005)
    sev = _safe_div(overshoot, atr).where(fail & near_round, np.nan)
    return sev.rolling(QDAYS, min_periods=MDAYS).max()


def f05_fbkd_198_double_top_failure_with_diverging_volume_252d(high, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm))
    arr_pm = pm.values
    arr_fail = fail.values
    arr_vol = volume.values
    n = len(arr_pm)
    out = np.full(n, np.nan, dtype=float)
    for i in range(QDAYS, n):
        lo = max(0, i - QDAYS + 1)
        idxs = [j for j in range(lo, i + 1) if arr_fail[j]]
        if len(idxs) >= 2:
            j1 = idxs[-2]
            j2 = idxs[-1]
            gap = j2 - j1
            same_level = (not np.isnan(arr_pm[j1]) and not np.isnan(arr_pm[j2])
                          and abs(arr_pm[j1] - arr_pm[j2]) / max(arr_pm[j1], 1e-9) <= 0.01)
            vol_div = arr_vol[j2] < arr_vol[j1]
            if MDAYS <= gap <= QDAYS and same_level and vol_div:
                out[i] = 1.0
            else:
                out[i] = 0.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def f05_fbkd_199_failed_break_pre_close_intraday_pierce_only_count(high, close, open_):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    pierce = high > pm
    min_prev5 = close.shift(1).rolling(WDAYS, min_periods=2).min()
    weak = (close < open_) & (close < min_prev5)
    sig = (pierce & weak).astype(float)
    return sig.rolling(YDAYS, min_periods=QDAYS).sum().where(pm.notna() & min_prev5.notna(), np.nan)


def f05_fbkd_200_failure_amplification_index_hawkes_proxy(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    fail = (high > pm) & (close < pm)
    sev = _safe_div(high - pm, atr).where(fail, 0.0)
    decay = np.exp(-np.log(2.0) * np.arange(QDAYS)[::-1] / MDAYS)
    def _hawkes(w):
        if w.size < 2:
            return np.nan
        d = decay[-w.size:]
        return float(np.nansum(w * d))
    return sev.rolling(QDAYS, min_periods=MDAYS).apply(_hawkes, raw=True).where(pm.notna() & atr.notna(), np.nan)



def _triple_barrier_speed(close, level_series, fail_event, threshold_pct, horizon):
    cv = close.values
    lv = level_series.values
    ev = fail_event.values
    n = len(cv)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not ev[i] or np.isnan(lv[i]):
            continue
        anchor = lv[i]
        target = anchor * (1.0 + threshold_pct)
        for k in range(i + 1, min(n, i + 1 + horizon)):
            if not np.isnan(cv[k]) and cv[k] <= target:
                out[k] = float(k - i)
                break
    return pd.Series(out, index=close.index)


def f05_fbkd_201_triple_barrier_speed_to_minus_5pct_after_break_21d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    return _triple_barrier_speed(close, pm, fail, -0.05, MDAYS)


def f05_fbkd_202_triple_barrier_speed_to_minus_10pct_after_break_63d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    return _triple_barrier_speed(close, pm, fail, -0.10, QDAYS)


def f05_fbkd_203_triple_barrier_speed_to_minus_20pct_after_break_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    return _triple_barrier_speed(close, pm, fail, -0.20, YDAYS)


def f05_fbkd_204_triple_barrier_which_first_after_break_indicator(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    cv = close.values
    lv = pm.values
    n = len(cv)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not fail[i] or np.isnan(lv[i]):
            continue
        anchor = lv[i]
        upper = anchor * 1.05
        lower = anchor * 0.95
        result = 0.0
        for k in range(i + 1, min(n, i + 1 + MDAYS)):
            if np.isnan(cv[k]):
                continue
            if cv[k] >= upper:
                result = 1.0
                break
            if cv[k] <= lower:
                result = -1.0
                break
        out[i] = result
    return pd.Series(out, index=close.index)


def f05_fbkd_205_volume_spike_4x_threshold_at_failed_break_252d(high, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    v_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    spike = volume > 4.0 * v_mean
    return (fail & spike).astype(float).where(pm.notna() & v_mean.notna(), np.nan)


def f05_fbkd_206_volume_spike_6x_threshold_at_failed_break_252d(high, close, volume):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = (high > pm) & (close < pm)
    v_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    spike = volume > 6.0 * v_mean
    return (fail & spike).astype(float).where(pm.notna() & v_mean.notna(), np.nan)


def f05_fbkd_207_visible_reversal_zone_failed_count_252d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    fail = (high > pm) & (close < pm)
    zone = (pm - pm.shift(1)).abs() <= 0.5 * atr
    in_zone_fail = (fail & zone).astype(float)
    return in_zone_fail.rolling(YDAYS, min_periods=QDAYS).sum().where(pm.notna() & atr.notna(), np.nan)


def f05_fbkd_208_visible_reversal_zone_strength_atr(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    fail = (high > pm) & (close < pm)
    upper_wick = (high - close).clip(lower=0)
    wick_per_atr = _safe_div(upper_wick, atr).where(fail, 0.0)
    return wick_per_atr.rolling(YDAYS, min_periods=QDAYS).sum().where(pm.notna() & atr.notna(), np.nan)


def f05_fbkd_209_anchored_vwap_from_21d_low_failure(high, low, close, volume):
    avwap = _rolling_anchored_vwap_from_low(high, low, close, volume, MDAYS)
    broke_past = (close.shift(WDAYS) > avwap.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < avwap.shift(WDAYS))
    return failed.astype(float).where(avwap.notna(), np.nan)


def f05_fbkd_210_anchored_vwap_from_504d_low_failure(high, low, close, volume):
    avwap = _rolling_anchored_vwap_from_low(high, low, close, volume, DDAYS_2Y)
    broke_past = (close.shift(WDAYS) > avwap.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < avwap.shift(WDAYS))
    return failed.astype(float).where(avwap.notna(), np.nan)



def f05_fbkd_211_anchored_vwap_from_max_volume_bar_failure_252d(high, low, close, volume):
    typ = (high + low + close) / 3.0
    pv = typ * volume
    v_arr = volume.values
    pv_arr = pv.values
    n = len(v_arr)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - YDAYS + 1)
        seg_v = v_arr[lo:i + 1]
        if np.isnan(seg_v).all():
            continue
        j_local = int(np.nanargmax(seg_v))
        anchor = lo + j_local
        pv_sum = np.nansum(pv_arr[anchor:i + 1])
        v_sum = np.nansum(v_arr[anchor:i + 1])
        if v_sum > 0:
            out[i] = pv_sum / v_sum
    avwap = pd.Series(out, index=close.index)
    broke_past = (close.shift(WDAYS) > avwap.shift(WDAYS)).fillna(False)
    failed = broke_past & (close < avwap.shift(WDAYS))
    return failed.astype(float).where(avwap.notna(), np.nan)


def f05_fbkd_212_wyckoff_utad_signature_63d(high, low, close, volume):
    pm = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    new_high = high > pm
    rng = high - low
    rng_mean = rng.rolling(50, min_periods=MDAYS).mean()
    rng_std = rng.rolling(50, min_periods=MDAYS).std()
    wide = rng > (rng_mean + 2.0 * rng_std)
    pos = _safe_div(close - low, high - low)
    weak_close = pos <= 0.25
    vol_mean = volume.rolling(50, min_periods=MDAYS).mean()
    big_vol = volume > 2.0 * vol_mean
    sig = (new_high & wide & weak_close & big_vol).astype(float)
    return sig.where(pm.notna() & rng_std.notna() & vol_mean.notna(), np.nan)


def f05_fbkd_213_wyckoff_utad_signature_504d(high, low, close, volume):
    pm = high.shift(1).rolling(DDAYS_2Y, min_periods=YDAYS).max()
    new_high = high > pm
    rng = high - low
    rng_mean = rng.rolling(50, min_periods=MDAYS).mean()
    rng_std = rng.rolling(50, min_periods=MDAYS).std()
    wide = rng > (rng_mean + 2.0 * rng_std)
    pos = _safe_div(close - low, high - low)
    weak_close = pos <= 0.25
    vol_mean = volume.rolling(50, min_periods=MDAYS).mean()
    big_vol = volume > 2.0 * vol_mean
    sig = (new_high & wide & weak_close & big_vol).astype(float)
    return sig.where(pm.notna() & rng_std.notna() & vol_mean.notna(), np.nan)


def f05_fbkd_214_four_close_confirmation_failure_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    above = close > pm
    four_above = above & above.shift(1) & above.shift(2) & above.shift(3)
    confirm_past = four_above.shift(7).fillna(False)
    failed = confirm_past & (close < pm.shift(7))
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_215_fourth_touch_failure_at_252d_resistance(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * pm)
    touch_cum = near.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    failed = (high > pm) & (close < pm) & (touch_cum >= 4)
    return failed.astype(float).where(pm.notna(), np.nan)


def f05_fbkd_216_three_pushes_to_high_failure_63d(high, close):
    return _three_pushes_to_high_fail(high, close, QDAYS)


def f05_fbkd_217_three_pushes_to_high_failure_504d(high, close):
    return _three_pushes_to_high_fail(high, close, DDAYS_2Y)


def f05_fbkd_218_lppl_acceleration_pre_failure_252d_window(high, close):
    lp = _safe_log(close)
    sm = lp.rolling(MDAYS, min_periods=WDAYS).mean()
    accel = sm.diff().diff()
    detrend = lp - lp.rolling(YDAYS, min_periods=QDAYS).mean()
    amp_recent = detrend.abs().rolling(QDAYS, min_periods=MDAYS).mean()
    amp_prior = detrend.abs().shift(QDAYS).rolling(QDAYS, min_periods=MDAYS).mean()
    diminishing = amp_recent < amp_prior
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail_recent = ((high > pm) & (close < pm)).rolling(YDAYS, min_periods=QDAYS).sum() > 0
    return accel.where(diminishing & fail_recent, np.nan)


def f05_fbkd_219_lppl_acceleration_pre_failure_21d_short_term(high, close):
    lp = _safe_log(close)
    sm = lp.rolling(3, min_periods=2).mean()
    accel = sm.diff().diff()
    detrend = lp - lp.rolling(MDAYS, min_periods=WDAYS).mean()
    amp_recent = detrend.abs().rolling(WDAYS, min_periods=2).mean()
    amp_prior = detrend.abs().shift(WDAYS).rolling(WDAYS, min_periods=2).mean()
    diminishing = amp_recent < amp_prior
    pm = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    fail_recent = ((high > pm) & (close < pm)).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return accel.where(diminishing & fail_recent, np.nan)


def f05_fbkd_220_cup_handle_failure_handle_in_lower_third_of_base_oneill(high, low, close):
    base_max = high.shift(11).rolling(60, min_periods=20).max()
    base_min = low.shift(11).rolling(60, min_periods=20).min()
    base_third = base_min + (base_max - base_min) / 3.0
    handle_max = high.shift(1).rolling(10, min_periods=3).max()
    handle_min = low.shift(1).rolling(10, min_periods=3).min()
    handle_in_lower = (handle_max < base_third)
    broke_past = ((close.shift(10) > handle_max.shift(10)) & handle_in_lower.shift(10)).fillna(False)
    failed = broke_past & (close < handle_min.shift(10))
    return failed.astype(float).where(base_max.notna() & handle_max.notna(), np.nan)


def f05_fbkd_221_high_tight_flag_failure_extended_consolidation_oneill(high, low, close):
    gain_8wk = _safe_div(close.shift(25) - close.shift(65), close.shift(65))
    base_max = high.shift(11).rolling(30, min_periods=25).max()
    base_min = low.shift(11).rolling(30, min_periods=25).min()
    cons_depth = _safe_div(base_max - base_min, base_max)
    valid = (gain_8wk > 1.0) & (cons_depth < 0.25)
    broke_past = ((close.shift(10) > base_max.shift(10)) & valid.shift(10)).fillna(False)
    failed = broke_past & (close < base_max.shift(10))
    return failed.astype(float).where(gain_8wk.notna() & base_max.notna(), np.nan)


def f05_fbkd_222_failed_break_then_inside_bar_streak_3d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).astype(float)
    had_fail = fail.shift(3).rolling(3, min_periods=2).sum() > 0
    inside = (high < high.shift(1)) & (low > low.shift(1))
    three_inside = inside & inside.shift(1) & inside.shift(2)
    return (had_fail & three_inside).astype(float).where(pm.notna(), np.nan)


def f05_fbkd_223_failed_break_run_length_wald_wolfowitz_252d(high, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    attempts = high > pm
    failed = attempts & (close < pm)
    succ = attempts & (close >= pm)
    label = pd.Series(np.where(failed, 1, np.where(succ, 0, np.nan)), index=high.index)
    def _ww(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        n1 = float((v == 1).sum())
        n2 = float((v == 0).sum())
        if n1 == 0 or n2 == 0:
            return np.nan
        runs = 1 + int((np.diff(v) != 0).sum())
        n = n1 + n2
        mu = 1.0 + 2.0 * n1 * n2 / n
        var = (2.0 * n1 * n2 * (2.0 * n1 * n2 - n)) / (n * n * (n - 1.0))
        if var <= 0:
            return np.nan
        return float((runs - mu) / np.sqrt(var))
    return label.rolling(YDAYS, min_periods=QDAYS).apply(_ww, raw=True)


def f05_fbkd_224_max_adverse_excursion_post_failed_break_21d_atr(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    fail = ((high > pm) & (close < pm)).values
    lv = low.values
    pv = pm.values
    av = atr.values
    n = len(lv)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not fail[i] or np.isnan(pv[i]) or np.isnan(av[i]) or av[i] == 0:
            continue
        anchor = pv[i]
        seg = lv[i + 1:i + 1 + MDAYS]
        if seg.size == 0 or np.isnan(seg).all():
            continue
        mae = anchor - np.nanmin(seg)
        out[i + min(MDAYS, seg.size)] = float(mae / av[i])
    return pd.Series(out, index=high.index)


def f05_fbkd_225_drawdown_speed_post_failed_break_21d(high, low, close):
    pm = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    fail = ((high > pm) & (close < pm)).values
    lv = low.values
    pv = pm.values
    n = len(lv)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if not fail[i] or np.isnan(pv[i]):
            continue
        anchor = pv[i]
        seg = lv[i + 1:i + 1 + MDAYS]
        if seg.size == 0 or np.isnan(seg).all():
            continue
        j = int(np.nanargmin(seg))
        dd = (anchor - seg[j]) / max(anchor, 1e-9)
        days = j + 1
        out[i + min(MDAYS, seg.size)] = float(dd / days)
    return pd.Series(out, index=high.index)




def f05_fbkd_151_wyckoff_utad_signature_252d_d1(high, low, close, volume): return f05_fbkd_151_wyckoff_utad_signature_252d(high, low, close, volume).diff()

def f05_fbkd_152_wyckoff_spring_then_utad_within_63d_d1(high, low, close, volume): return f05_fbkd_152_wyckoff_spring_then_utad_within_63d(high, low, close, volume).diff()

def f05_fbkd_153_wyckoff_sow_after_buying_climax_21d_d1(high, low, close, volume): return f05_fbkd_153_wyckoff_sow_after_buying_climax_21d(high, low, close, volume).diff()

def f05_fbkd_154_cup_handle_failure_oneill_proxy_d1(high, low, close): return f05_fbkd_154_cup_handle_failure_oneill_proxy(high, low, close).diff()

def f05_fbkd_155_high_tight_flag_failure_oneill_d1(high, low, close): return f05_fbkd_155_high_tight_flag_failure_oneill(high, low, close).diff()

def f05_fbkd_156_ascending_triangle_apex_failure_63d_d1(high, low, close): return f05_fbkd_156_ascending_triangle_apex_failure_63d(high, low, close).diff()

def f05_fbkd_157_rising_wedge_failure_252d_d1(high, low, close): return f05_fbkd_157_rising_wedge_failure_252d(high, low, close).diff()

def f05_fbkd_158_bear_pennant_breakout_failure_post_rally_d1(high, low, close): return f05_fbkd_158_bear_pennant_breakout_failure_post_rally(high, low, close).diff()

def f05_fbkd_159_bollinger_squeeze_release_failure_20d_d1(high, close): return f05_fbkd_159_bollinger_squeeze_release_failure_20d(high, close).diff()

def f05_fbkd_160_keltner_squeeze_failure_20d_d1(high, low, close): return f05_fbkd_160_keltner_squeeze_failure_20d(high, low, close).diff()

def f05_fbkd_161_anchored_vwap_from_252d_low_failure_d1(high, low, close, volume): return f05_fbkd_161_anchored_vwap_from_252d_low_failure(high, low, close, volume).diff()

def f05_fbkd_162_anchored_vwap_from_prior_ath_rejection_d1(high, low, close, volume): return f05_fbkd_162_anchored_vwap_from_prior_ath_rejection(high, low, close, volume).diff()

def f05_fbkd_163_hl2_pierce_only_252d_high_count_d1(high, low): return f05_fbkd_163_hl2_pierce_only_252d_high_count(high, low).diff()

def f05_fbkd_164_typical_price_pierce_252d_failure_d1(high, low, close): return f05_fbkd_164_typical_price_pierce_252d_failure(high, low, close).diff()

def f05_fbkd_165_consecutive_close_above_then_below_252d_d1(high, close): return f05_fbkd_165_consecutive_close_above_then_below_252d(high, close).diff()

def f05_fbkd_166_three_close_confirmation_failure_252d_d1(high, close): return f05_fbkd_166_three_close_confirmation_failure_252d(high, close).diff()

def f05_fbkd_167_failure_rate_by_full_gap_breakout_d1(open_, high, close): return f05_fbkd_167_failure_rate_by_full_gap_breakout(open_, high, close).diff()

def f05_fbkd_168_failure_rate_by_partial_gap_breakout_d1(open_, high, close): return f05_fbkd_168_failure_rate_by_partial_gap_breakout(open_, high, close).diff()

def f05_fbkd_169_failure_rate_by_no_gap_breakout_d1(open_, high, close): return f05_fbkd_169_failure_rate_by_no_gap_breakout(open_, high, close).diff()

def f05_fbkd_170_atr_expansion_at_failed_breakout_252d_d1(high, low, close): return f05_fbkd_170_atr_expansion_at_failed_breakout_252d(high, low, close).diff()

def f05_fbkd_171_slow_grind_failed_breakout_252d_d1(high, low, close): return f05_fbkd_171_slow_grind_failed_breakout_252d(high, low, close).diff()

def f05_fbkd_172_second_touch_failure_at_252d_resistance_d1(high, close): return f05_fbkd_172_second_touch_failure_at_252d_resistance(high, close).diff()

def f05_fbkd_173_third_touch_failure_at_252d_resistance_d1(high, close): return f05_fbkd_173_third_touch_failure_at_252d_resistance(high, close).diff()

def f05_fbkd_174_three_pushes_to_high_failure_252d_d1(high, close): return f05_fbkd_174_three_pushes_to_high_failure_252d(high, close).diff()

def f05_fbkd_175_upper_wick_volume_weighted_absorption_252d_d1(high, low, close, volume): return f05_fbkd_175_upper_wick_volume_weighted_absorption_252d(high, low, close, volume).diff()

def f05_fbkd_176_coiling_time_within_half_atr_of_252d_pre_break_d1(high, low, close): return f05_fbkd_176_coiling_time_within_half_atr_of_252d_pre_break(high, low, close).diff()

def f05_fbkd_177_failed_break_inter_arrival_dispersion_252d_d1(high, close): return f05_fbkd_177_failed_break_inter_arrival_dispersion_252d(high, close).diff()

def f05_fbkd_178_failed_break_inter_arrival_min_252d_d1(high, close): return f05_fbkd_178_failed_break_inter_arrival_min_252d(high, close).diff()

def f05_fbkd_179_failure_then_confirmed_breakdown_below_63d_low_within_21d_d1(high, low, close): return f05_fbkd_179_failure_then_confirmed_breakdown_below_63d_low_within_21d(high, low, close).diff()

def f05_fbkd_180_failure_then_range_no_breakdown_63d_d1(high, close): return f05_fbkd_180_failure_then_range_no_breakdown_63d(high, close).diff()

def f05_fbkd_181_lppl_log_periodic_acceleration_pre_failure_252d_d1(high, close): return f05_fbkd_181_lppl_log_periodic_acceleration_pre_failure_252d(high, close).diff()

def f05_fbkd_182_parabolic_blowoff_then_failed_252d_d1(high, close): return f05_fbkd_182_parabolic_blowoff_then_failed_252d(high, close).diff()

def f05_fbkd_183_nr7_breakout_failure_252d_d1(high, low, close): return f05_fbkd_183_nr7_breakout_failure_252d(high, low, close).diff()

def f05_fbkd_184_inside_bar_after_break_then_breakdown_252d_d1(high, low, close): return f05_fbkd_184_inside_bar_after_break_then_breakdown_252d(high, low, close).diff()

def f05_fbkd_185_outside_bar_reversal_at_252d_high_d1(high, low, close): return f05_fbkd_185_outside_bar_reversal_at_252d_high(high, low, close).diff()

def f05_fbkd_186_pocket_pivot_inversion_at_252d_high_d1(high, close, volume): return f05_fbkd_186_pocket_pivot_inversion_at_252d_high(high, close, volume).diff()

def f05_fbkd_187_stop_run_overshoot_percentile_252d_d1(high, low, close): return f05_fbkd_187_stop_run_overshoot_percentile_252d(high, low, close).diff()

def f05_fbkd_188_failed_break_at_fib_extension_127_of_prior_swing_d1(high, low, close): return f05_fbkd_188_failed_break_at_fib_extension_127_of_prior_swing(high, low, close).diff()

def f05_fbkd_189_failed_break_at_fib_extension_162_of_prior_swing_d1(high, low, close): return f05_fbkd_189_failed_break_at_fib_extension_162_of_prior_swing(high, low, close).diff()

def f05_fbkd_190_no_demand_pre_breakout_then_failure_d1(high, close, volume): return f05_fbkd_190_no_demand_pre_breakout_then_failure(high, close, volume).diff()

def f05_fbkd_191_failed_break_followed_by_gap_down_breakaway_5d_d1(open_, high, low, close): return f05_fbkd_191_failed_break_followed_by_gap_down_breakaway_5d(open_, high, low, close).diff()

def f05_fbkd_192_failed_break_in_low_vol_regime_atr_pctile_bottom_25_d1(high, low, close): return f05_fbkd_192_failed_break_in_low_vol_regime_atr_pctile_bottom_25(high, low, close).diff()

def f05_fbkd_193_failed_break_in_high_vol_of_vol_regime_252d_d1(high, low, close): return f05_fbkd_193_failed_break_in_high_vol_of_vol_regime_252d(high, low, close).diff()

def f05_fbkd_194_truncated_swing_failed_5th_push_252d_d1(high, close): return f05_fbkd_194_truncated_swing_failed_5th_push_252d(high, close).diff()

def f05_fbkd_195_failed_break_with_two_bar_reversal_at_252d_d1(high, low, close, open_): return f05_fbkd_195_failed_break_with_two_bar_reversal_at_252d(high, low, close, open_).diff()

def f05_fbkd_196_climax_thrust_then_reversal_williams_proxy_d1(high, low, close): return f05_fbkd_196_climax_thrust_then_reversal_williams_proxy(high, low, close).diff()

def f05_fbkd_197_failed_break_at_round_number_clinginess_5pct_severity_d1(high, low, close): return f05_fbkd_197_failed_break_at_round_number_clinginess_5pct_severity(high, low, close).diff()

def f05_fbkd_198_double_top_failure_with_diverging_volume_252d_d1(high, close, volume): return f05_fbkd_198_double_top_failure_with_diverging_volume_252d(high, close, volume).diff()

def f05_fbkd_199_failed_break_pre_close_intraday_pierce_only_count_d1(high, close, open_): return f05_fbkd_199_failed_break_pre_close_intraday_pierce_only_count(high, close, open_).diff()

def f05_fbkd_200_failure_amplification_index_hawkes_proxy_d1(high, low, close): return f05_fbkd_200_failure_amplification_index_hawkes_proxy(high, low, close).diff()

def f05_fbkd_201_triple_barrier_speed_to_minus_5pct_after_break_21d_d1(high, close): return f05_fbkd_201_triple_barrier_speed_to_minus_5pct_after_break_21d(high, close).diff()

def f05_fbkd_202_triple_barrier_speed_to_minus_10pct_after_break_63d_d1(high, close): return f05_fbkd_202_triple_barrier_speed_to_minus_10pct_after_break_63d(high, close).diff()

def f05_fbkd_203_triple_barrier_speed_to_minus_20pct_after_break_252d_d1(high, close): return f05_fbkd_203_triple_barrier_speed_to_minus_20pct_after_break_252d(high, close).diff()

def f05_fbkd_204_triple_barrier_which_first_after_break_indicator_d1(high, close): return f05_fbkd_204_triple_barrier_which_first_after_break_indicator(high, close).diff()

def f05_fbkd_205_volume_spike_4x_threshold_at_failed_break_252d_d1(high, close, volume): return f05_fbkd_205_volume_spike_4x_threshold_at_failed_break_252d(high, close, volume).diff()

def f05_fbkd_206_volume_spike_6x_threshold_at_failed_break_252d_d1(high, close, volume): return f05_fbkd_206_volume_spike_6x_threshold_at_failed_break_252d(high, close, volume).diff()

def f05_fbkd_207_visible_reversal_zone_failed_count_252d_d1(high, low, close): return f05_fbkd_207_visible_reversal_zone_failed_count_252d(high, low, close).diff()

def f05_fbkd_208_visible_reversal_zone_strength_atr_d1(high, low, close): return f05_fbkd_208_visible_reversal_zone_strength_atr(high, low, close).diff()

def f05_fbkd_209_anchored_vwap_from_21d_low_failure_d1(high, low, close, volume): return f05_fbkd_209_anchored_vwap_from_21d_low_failure(high, low, close, volume).diff()

def f05_fbkd_210_anchored_vwap_from_504d_low_failure_d1(high, low, close, volume): return f05_fbkd_210_anchored_vwap_from_504d_low_failure(high, low, close, volume).diff()

def f05_fbkd_211_anchored_vwap_from_max_volume_bar_failure_252d_d1(high, low, close, volume): return f05_fbkd_211_anchored_vwap_from_max_volume_bar_failure_252d(high, low, close, volume).diff()

def f05_fbkd_212_wyckoff_utad_signature_63d_d1(high, low, close, volume): return f05_fbkd_212_wyckoff_utad_signature_63d(high, low, close, volume).diff()

def f05_fbkd_213_wyckoff_utad_signature_504d_d1(high, low, close, volume): return f05_fbkd_213_wyckoff_utad_signature_504d(high, low, close, volume).diff()

def f05_fbkd_214_four_close_confirmation_failure_252d_d1(high, close): return f05_fbkd_214_four_close_confirmation_failure_252d(high, close).diff()

def f05_fbkd_215_fourth_touch_failure_at_252d_resistance_d1(high, close): return f05_fbkd_215_fourth_touch_failure_at_252d_resistance(high, close).diff()

def f05_fbkd_216_three_pushes_to_high_failure_63d_d1(high, close): return f05_fbkd_216_three_pushes_to_high_failure_63d(high, close).diff()

def f05_fbkd_217_three_pushes_to_high_failure_504d_d1(high, close): return f05_fbkd_217_three_pushes_to_high_failure_504d(high, close).diff()

def f05_fbkd_218_lppl_acceleration_pre_failure_252d_window_d1(high, close): return f05_fbkd_218_lppl_acceleration_pre_failure_252d_window(high, close).diff()

def f05_fbkd_219_lppl_acceleration_pre_failure_21d_short_term_d1(high, close): return f05_fbkd_219_lppl_acceleration_pre_failure_21d_short_term(high, close).diff()

def f05_fbkd_220_cup_handle_failure_handle_in_lower_third_of_base_oneill_d1(high, low, close): return f05_fbkd_220_cup_handle_failure_handle_in_lower_third_of_base_oneill(high, low, close).diff()

def f05_fbkd_221_high_tight_flag_failure_extended_consolidation_oneill_d1(high, low, close): return f05_fbkd_221_high_tight_flag_failure_extended_consolidation_oneill(high, low, close).diff()

def f05_fbkd_222_failed_break_then_inside_bar_streak_3d_d1(high, low, close): return f05_fbkd_222_failed_break_then_inside_bar_streak_3d(high, low, close).diff()

def f05_fbkd_223_failed_break_run_length_wald_wolfowitz_252d_d1(high, close): return f05_fbkd_223_failed_break_run_length_wald_wolfowitz_252d(high, close).diff()

def f05_fbkd_224_max_adverse_excursion_post_failed_break_21d_atr_d1(high, low, close): return f05_fbkd_224_max_adverse_excursion_post_failed_break_21d_atr(high, low, close).diff()

def f05_fbkd_225_drawdown_speed_post_failed_break_21d_d1(high, low, close): return f05_fbkd_225_drawdown_speed_post_failed_break_21d(high, low, close).diff()


FAILED_BREAKOUT_DYNAMICS_D1_REGISTRY_151_225 = {
    "f05_fbkd_151_wyckoff_utad_signature_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_151_wyckoff_utad_signature_252d_d1},
    "f05_fbkd_152_wyckoff_spring_then_utad_within_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_152_wyckoff_spring_then_utad_within_63d_d1},
    "f05_fbkd_153_wyckoff_sow_after_buying_climax_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_153_wyckoff_sow_after_buying_climax_21d_d1},
    "f05_fbkd_154_cup_handle_failure_oneill_proxy_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_154_cup_handle_failure_oneill_proxy_d1},
    "f05_fbkd_155_high_tight_flag_failure_oneill_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_155_high_tight_flag_failure_oneill_d1},
    "f05_fbkd_156_ascending_triangle_apex_failure_63d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_156_ascending_triangle_apex_failure_63d_d1},
    "f05_fbkd_157_rising_wedge_failure_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_157_rising_wedge_failure_252d_d1},
    "f05_fbkd_158_bear_pennant_breakout_failure_post_rally_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_158_bear_pennant_breakout_failure_post_rally_d1},
    "f05_fbkd_159_bollinger_squeeze_release_failure_20d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_159_bollinger_squeeze_release_failure_20d_d1},
    "f05_fbkd_160_keltner_squeeze_failure_20d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_160_keltner_squeeze_failure_20d_d1},
    "f05_fbkd_161_anchored_vwap_from_252d_low_failure_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_161_anchored_vwap_from_252d_low_failure_d1},
    "f05_fbkd_162_anchored_vwap_from_prior_ath_rejection_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_162_anchored_vwap_from_prior_ath_rejection_d1},
    "f05_fbkd_163_hl2_pierce_only_252d_high_count_d1": {"inputs": ["high", "low"], "func": f05_fbkd_163_hl2_pierce_only_252d_high_count_d1},
    "f05_fbkd_164_typical_price_pierce_252d_failure_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_164_typical_price_pierce_252d_failure_d1},
    "f05_fbkd_165_consecutive_close_above_then_below_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_165_consecutive_close_above_then_below_252d_d1},
    "f05_fbkd_166_three_close_confirmation_failure_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_166_three_close_confirmation_failure_252d_d1},
    "f05_fbkd_167_failure_rate_by_full_gap_breakout_d1": {"inputs": ["open", "high", "close"], "func": f05_fbkd_167_failure_rate_by_full_gap_breakout_d1},
    "f05_fbkd_168_failure_rate_by_partial_gap_breakout_d1": {"inputs": ["open", "high", "close"], "func": f05_fbkd_168_failure_rate_by_partial_gap_breakout_d1},
    "f05_fbkd_169_failure_rate_by_no_gap_breakout_d1": {"inputs": ["open", "high", "close"], "func": f05_fbkd_169_failure_rate_by_no_gap_breakout_d1},
    "f05_fbkd_170_atr_expansion_at_failed_breakout_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_170_atr_expansion_at_failed_breakout_252d_d1},
    "f05_fbkd_171_slow_grind_failed_breakout_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_171_slow_grind_failed_breakout_252d_d1},
    "f05_fbkd_172_second_touch_failure_at_252d_resistance_d1": {"inputs": ["high", "close"], "func": f05_fbkd_172_second_touch_failure_at_252d_resistance_d1},
    "f05_fbkd_173_third_touch_failure_at_252d_resistance_d1": {"inputs": ["high", "close"], "func": f05_fbkd_173_third_touch_failure_at_252d_resistance_d1},
    "f05_fbkd_174_three_pushes_to_high_failure_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_174_three_pushes_to_high_failure_252d_d1},
    "f05_fbkd_175_upper_wick_volume_weighted_absorption_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_175_upper_wick_volume_weighted_absorption_252d_d1},
    "f05_fbkd_176_coiling_time_within_half_atr_of_252d_pre_break_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_176_coiling_time_within_half_atr_of_252d_pre_break_d1},
    "f05_fbkd_177_failed_break_inter_arrival_dispersion_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_177_failed_break_inter_arrival_dispersion_252d_d1},
    "f05_fbkd_178_failed_break_inter_arrival_min_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_178_failed_break_inter_arrival_min_252d_d1},
    "f05_fbkd_179_failure_then_confirmed_breakdown_below_63d_low_within_21d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_179_failure_then_confirmed_breakdown_below_63d_low_within_21d_d1},
    "f05_fbkd_180_failure_then_range_no_breakdown_63d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_180_failure_then_range_no_breakdown_63d_d1},
    "f05_fbkd_181_lppl_log_periodic_acceleration_pre_failure_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_181_lppl_log_periodic_acceleration_pre_failure_252d_d1},
    "f05_fbkd_182_parabolic_blowoff_then_failed_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_182_parabolic_blowoff_then_failed_252d_d1},
    "f05_fbkd_183_nr7_breakout_failure_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_183_nr7_breakout_failure_252d_d1},
    "f05_fbkd_184_inside_bar_after_break_then_breakdown_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_184_inside_bar_after_break_then_breakdown_252d_d1},
    "f05_fbkd_185_outside_bar_reversal_at_252d_high_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_185_outside_bar_reversal_at_252d_high_d1},
    "f05_fbkd_186_pocket_pivot_inversion_at_252d_high_d1": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_186_pocket_pivot_inversion_at_252d_high_d1},
    "f05_fbkd_187_stop_run_overshoot_percentile_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_187_stop_run_overshoot_percentile_252d_d1},
    "f05_fbkd_188_failed_break_at_fib_extension_127_of_prior_swing_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_188_failed_break_at_fib_extension_127_of_prior_swing_d1},
    "f05_fbkd_189_failed_break_at_fib_extension_162_of_prior_swing_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_189_failed_break_at_fib_extension_162_of_prior_swing_d1},
    "f05_fbkd_190_no_demand_pre_breakout_then_failure_d1": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_190_no_demand_pre_breakout_then_failure_d1},
    "f05_fbkd_191_failed_break_followed_by_gap_down_breakaway_5d_d1": {"inputs": ["open", "high", "low", "close"], "func": f05_fbkd_191_failed_break_followed_by_gap_down_breakaway_5d_d1},
    "f05_fbkd_192_failed_break_in_low_vol_regime_atr_pctile_bottom_25_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_192_failed_break_in_low_vol_regime_atr_pctile_bottom_25_d1},
    "f05_fbkd_193_failed_break_in_high_vol_of_vol_regime_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_193_failed_break_in_high_vol_of_vol_regime_252d_d1},
    "f05_fbkd_194_truncated_swing_failed_5th_push_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_194_truncated_swing_failed_5th_push_252d_d1},
    "f05_fbkd_195_failed_break_with_two_bar_reversal_at_252d_d1": {"inputs": ["high", "low", "close", "open"], "func": f05_fbkd_195_failed_break_with_two_bar_reversal_at_252d_d1},
    "f05_fbkd_196_climax_thrust_then_reversal_williams_proxy_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_196_climax_thrust_then_reversal_williams_proxy_d1},
    "f05_fbkd_197_failed_break_at_round_number_clinginess_5pct_severity_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_197_failed_break_at_round_number_clinginess_5pct_severity_d1},
    "f05_fbkd_198_double_top_failure_with_diverging_volume_252d_d1": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_198_double_top_failure_with_diverging_volume_252d_d1},
    "f05_fbkd_199_failed_break_pre_close_intraday_pierce_only_count_d1": {"inputs": ["high", "close", "open"], "func": f05_fbkd_199_failed_break_pre_close_intraday_pierce_only_count_d1},
    "f05_fbkd_200_failure_amplification_index_hawkes_proxy_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_200_failure_amplification_index_hawkes_proxy_d1},
    "f05_fbkd_201_triple_barrier_speed_to_minus_5pct_after_break_21d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_201_triple_barrier_speed_to_minus_5pct_after_break_21d_d1},
    "f05_fbkd_202_triple_barrier_speed_to_minus_10pct_after_break_63d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_202_triple_barrier_speed_to_minus_10pct_after_break_63d_d1},
    "f05_fbkd_203_triple_barrier_speed_to_minus_20pct_after_break_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_203_triple_barrier_speed_to_minus_20pct_after_break_252d_d1},
    "f05_fbkd_204_triple_barrier_which_first_after_break_indicator_d1": {"inputs": ["high", "close"], "func": f05_fbkd_204_triple_barrier_which_first_after_break_indicator_d1},
    "f05_fbkd_205_volume_spike_4x_threshold_at_failed_break_252d_d1": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_205_volume_spike_4x_threshold_at_failed_break_252d_d1},
    "f05_fbkd_206_volume_spike_6x_threshold_at_failed_break_252d_d1": {"inputs": ["high", "close", "volume"], "func": f05_fbkd_206_volume_spike_6x_threshold_at_failed_break_252d_d1},
    "f05_fbkd_207_visible_reversal_zone_failed_count_252d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_207_visible_reversal_zone_failed_count_252d_d1},
    "f05_fbkd_208_visible_reversal_zone_strength_atr_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_208_visible_reversal_zone_strength_atr_d1},
    "f05_fbkd_209_anchored_vwap_from_21d_low_failure_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_209_anchored_vwap_from_21d_low_failure_d1},
    "f05_fbkd_210_anchored_vwap_from_504d_low_failure_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_210_anchored_vwap_from_504d_low_failure_d1},
    "f05_fbkd_211_anchored_vwap_from_max_volume_bar_failure_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_211_anchored_vwap_from_max_volume_bar_failure_252d_d1},
    "f05_fbkd_212_wyckoff_utad_signature_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_212_wyckoff_utad_signature_63d_d1},
    "f05_fbkd_213_wyckoff_utad_signature_504d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f05_fbkd_213_wyckoff_utad_signature_504d_d1},
    "f05_fbkd_214_four_close_confirmation_failure_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_214_four_close_confirmation_failure_252d_d1},
    "f05_fbkd_215_fourth_touch_failure_at_252d_resistance_d1": {"inputs": ["high", "close"], "func": f05_fbkd_215_fourth_touch_failure_at_252d_resistance_d1},
    "f05_fbkd_216_three_pushes_to_high_failure_63d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_216_three_pushes_to_high_failure_63d_d1},
    "f05_fbkd_217_three_pushes_to_high_failure_504d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_217_three_pushes_to_high_failure_504d_d1},
    "f05_fbkd_218_lppl_acceleration_pre_failure_252d_window_d1": {"inputs": ["high", "close"], "func": f05_fbkd_218_lppl_acceleration_pre_failure_252d_window_d1},
    "f05_fbkd_219_lppl_acceleration_pre_failure_21d_short_term_d1": {"inputs": ["high", "close"], "func": f05_fbkd_219_lppl_acceleration_pre_failure_21d_short_term_d1},
    "f05_fbkd_220_cup_handle_failure_handle_in_lower_third_of_base_oneill_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_220_cup_handle_failure_handle_in_lower_third_of_base_oneill_d1},
    "f05_fbkd_221_high_tight_flag_failure_extended_consolidation_oneill_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_221_high_tight_flag_failure_extended_consolidation_oneill_d1},
    "f05_fbkd_222_failed_break_then_inside_bar_streak_3d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_222_failed_break_then_inside_bar_streak_3d_d1},
    "f05_fbkd_223_failed_break_run_length_wald_wolfowitz_252d_d1": {"inputs": ["high", "close"], "func": f05_fbkd_223_failed_break_run_length_wald_wolfowitz_252d_d1},
    "f05_fbkd_224_max_adverse_excursion_post_failed_break_21d_atr_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_224_max_adverse_excursion_post_failed_break_21d_atr_d1},
    "f05_fbkd_225_drawdown_speed_post_failed_break_21d_d1": {"inputs": ["high", "low", "close"], "func": f05_fbkd_225_drawdown_speed_post_failed_break_21d_d1},
}
