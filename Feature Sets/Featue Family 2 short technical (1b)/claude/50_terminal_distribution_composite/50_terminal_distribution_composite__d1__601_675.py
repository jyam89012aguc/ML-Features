"""terminal_distribution_composite d1 features 601-675 — Pipeline 1b-technical.

75 distinct INDIVIDUAL signal hypotheses extending the 600 existing features.
Themes: survival hazard for stuck-specific patterns / post-peak bounce
magnitude+conviction / behavioral anchoring / quantile-regression /
long-horizon memory / asymmetric mean-reversion / conditional moment-shifts /
information-asymmetry.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
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
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _bars_since_true(b: pd.Series) -> pd.Series:
    arr = b.fillna(False).astype(bool).values
    n = arr.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


def f50_tdco_601_frac_time_near_252d_low_5pct_252d_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    near = (close <= rmin * 1.05).astype(float).where(rmin.notna(), np.nan)
    out = near.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_602_rate_distance_from_252d_high_63d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    dist = _safe_log(rmax) - _safe_log(close)
    out = dist - dist.shift(63)
    return out.diff()


def f50_tdco_603_stuck_dd50_no_recover_indicator_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax_all = high.expanding(min_periods=63).max()
    dd = _safe_log(rmax_all) - _safe_log(close)
    big_dd = (dd > 0.69).astype(float)  # log(2) ~= 0.693, i.e. -50% in linear
    out = big_dd.rolling(252, min_periods=84).min()
    return out.diff()


def f50_tdco_604_bars_since_last_252d_high_d1(high: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    ev = (high >= rmax)
    out = _bars_since_true(ev)
    return out.diff()


def f50_tdco_605_expected_time_to_next_peak_252d_d1(high: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    ev = (high >= rmax).astype(float).where(rmax.notna(), np.nan)
    cnt = ev.rolling(252, min_periods=84).sum()
    out = 252.0 / cnt.replace(0, np.nan)
    return out.diff()


def f50_tdco_606_hazard_new_1260d_low_252d_d1(low: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=252).min()
    ev = (low <= rmin).astype(float).where(rmin.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_607_stuck_momentum_no_pos_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close).diff(252)
    r63 = _safe_log(close).diff(63)
    no_pos = (r63.rolling(252, min_periods=84).max() < 0).astype(float)
    big_decl = (r252 < -0.5).astype(float)
    out = (no_pos * big_decl).where(r252.notna(), np.nan)
    return out.diff()


def f50_tdco_608_indicator_504d_cum_decline_50pct_d1(close: pd.Series) -> pd.Series:
    r504 = _safe_log(close).diff(504)
    out = (r504 < -0.69).astype(float).where(r504.notna(), np.nan)
    return out.diff()


def f50_tdco_609_longest_gap_no_new_21d_high_252d_d1(high: pd.Series) -> pd.Series:
    rmax21 = high.rolling(21, min_periods=7).max()
    ev = (high >= rmax21).astype(float).where(rmax21.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        best = 0; cur = 0
        for x in v:
            if x < 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = ev.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f50_tdco_610_cond_5d_ret_given_dd30_from_252d_high_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    dd = _safe_log(rmax) - _safe_log(close)
    cond_dd30 = (dd > 0.35).astype(bool)
    ret5 = _safe_log(close).diff(5)
    out = ret5.where(cond_dd30, np.nan).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_611_hazard_5pct_gap_down_event_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    ev = (g < -0.05).astype(float).where(g.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_612_cond_max_dd_21d_given_at_252d_high_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(bool)
    fut_min = _safe_log(close.shift(21)).rolling(21, min_periods=7).min()
    dd_fwd = _safe_log(close) - fut_min
    out = dd_fwd.where(at_high, np.nan).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_613_sequential_lower_low_count_252d_d1(low: pd.Series) -> pd.Series:
    ll = (low < low.shift(21)).astype(int).where(low.notna() & low.shift(21).notna(), 0)
    seq = ll * ll.shift(21)
    out = seq.rolling(252, min_periods=84).sum()
    return out.diff()


def f50_tdco_614_sequential_lower_high_count_252d_d1(high: pd.Series) -> pd.Series:
    lh = (high < high.shift(21)).astype(int).where(high.notna() & high.shift(21).notna(), 0)
    seq = lh * lh.shift(21)
    out = seq.rolling(252, min_periods=84).sum()
    return out.diff()


def f50_tdco_615_hazard_new_504d_low_252d_d1(low: pd.Series) -> pd.Series:
    rmin = low.rolling(504, min_periods=168).min()
    ev = (low <= rmin).astype(float).where(rmin.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_616_mean_5d_bounce_after_5pct_dd_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    rmax = lh.rolling(21, min_periods=7).max()
    big_dd_5d_ago = ((rmax.shift(5) - lc.shift(5)) > 0.05).astype(bool)
    bounce = (lc - lc.shift(5)).where(big_dd_5d_ago, np.nan)
    out = bounce.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_617_mean_21d_bounce_after_10pct_dd_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    rmax = lh.rolling(63, min_periods=21).max()
    big_dd = ((rmax.shift(21) - lc.shift(21)) > 0.10).astype(bool)
    bounce = (lc - lc.shift(21)).where(big_dd, np.nan)
    out = bounce.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_618_bounce_vol_conviction_ratio_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    up_v = volume.where(r > 0, 0.0).rolling(5, min_periods=2).sum()
    dn_v = volume.where(r < 0, 0.0).shift(5).rolling(5, min_periods=2).sum()
    out = _safe_div(up_v, dn_v).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_619_bounce_fizzle_rate_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    fizzle = ((r5 > 0.05).shift(5) & (r5 < 0)).astype(float).where(r5.notna() & r5.shift(5).notna(), np.nan)
    out = fizzle.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_620_pct_dd_recovered_21d_after_dd10_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    rmax = lh.rolling(63, min_periods=21).max()
    dd_21d_ago = (rmax.shift(21) - lc.shift(21)).where(rmax.shift(21).notna(), np.nan)
    recovery = (lc - lc.shift(21)).where(dd_21d_ago > 0.10, np.nan)
    pct_rec = _safe_div(recovery, dd_21d_ago.where(dd_21d_ago > 0.10, np.nan))
    out = pct_rec.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_621_recovery_success_rate_dd_gt_5pct_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    rmax = lh.rolling(63, min_periods=21).max()
    dd_21d = (rmax.shift(21) - lc.shift(21))
    recov_21d = (lc - lc.shift(21))
    success = ((dd_21d > 0.05) & (recov_21d > 0.5 * dd_21d)).astype(float).where(dd_21d.notna() & recov_21d.notna(), np.nan)
    total_dd = (dd_21d > 0.05).astype(float).where(dd_21d.notna(), np.nan)
    out = _safe_div(success.rolling(252, min_periods=84).sum(), total_dd.rolling(252, min_periods=84).sum())
    return out.diff()


def f50_tdco_622_bounce_vol_vs_252d_median_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r5 = _safe_log(close).diff(5)
    in_bounce = (r5 > 0.03).astype(bool)
    bounce_vol = volume.where(in_bounce, np.nan)
    med_v = volume.rolling(252, min_periods=84).median()
    out = _safe_div(bounce_vol.rolling(252, min_periods=84).mean(), med_v)
    return out.diff()


def f50_tdco_623_reaction_rally_lower_high_rate_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lh = _safe_log(high); lc = _safe_log(close)
    prior_h = lh.shift(5).rolling(5, min_periods=2).max()
    decline = (lc - lc.shift(5)) < -0.05
    post_h = lh.rolling(5, min_periods=2).max()
    lower_h = ((post_h < prior_h.shift(5)) & decline.shift(5)).astype(float).where(decline.shift(5).notna(), np.nan)
    out = lower_h.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_624_bounce_5d_decay_slope_63d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    pos5 = r5.clip(lower=0).rolling(21, min_periods=7).max()
    out = _rolling_slope(pos5, 63, min_periods=21)
    return out.diff()


def f50_tdco_625_up_day_vol_minus_down_day_vol_pct_rank_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    up_v = volume.where(r > 0, np.nan).rolling(63, min_periods=21).mean()
    dn_v = volume.where(r < 0, np.nan).rolling(63, min_periods=21).mean()
    ratio = _safe_div(up_v, dn_v)
    out = _rolling_pct_rank(ratio, 252, min_periods=84)
    return out.diff()


def f50_tdco_626_bounce_rate_acceleration_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    rate = (r5 > 0.05).astype(float).where(r5.notna(), np.nan).rolling(63, min_periods=21).mean()
    out = rate - rate.shift(21)
    return out.diff()


def f50_tdco_627_close_vs_21d_mean_post_decline_252d_d1(close: pd.Series) -> pd.Series:
    r21 = _safe_log(close).diff(21)
    big_decl = (r21.shift(1) < -0.1).astype(bool)
    m21 = close.rolling(21, min_periods=7).mean()
    gap = _safe_div(close - m21, m21).where(big_decl, np.nan)
    out = gap.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_628_actual_vs_expected_recovery_time_ratio_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    rmax21 = lh.rolling(21, min_periods=7).max()
    dd21 = rmax21 - lc
    # actual_recovery_bars: bars-since-last-not-in-dd (proxy for time underwater)
    in_dd = (dd21 > 0.01)
    actual_bars = _bars_since_true(~in_dd)
    # expected ~ 21d on average
    out = _safe_div(actual_bars, 21.0).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_629_bounce_75pct_percentile_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5).clip(lower=0)
    out = r5.rolling(252, min_periods=84).quantile(0.75)
    return out.diff()


def f50_tdco_630_bounce_fail_to_hold_rate_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bounce = (r > 0.03).astype(bool)
    follow_dn = (r.shift(1) < 0).astype(float)
    fail = follow_dn.where(bounce, np.nan)
    out = fail.rolling(63, min_periods=21).mean()
    return out.diff()


def f50_tdco_631_nearest_round_dollar_distance_pct_d1(close: pd.Series) -> pd.Series:
    nearest = close.round(0)
    out = (close - nearest).abs() / close
    return out.diff()


def f50_tdco_632_round_dollar_bear_next_freq_252d_d1(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(float)
    at_r = ((cents % 100) == 0).astype(float)
    bear = (close.shift(1) < close).astype(float)
    out = (at_r * bear).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_633_attention_spike_3sigma_ret_vol2_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)
    ev = ((r.abs() > 3.0 * sd) & (vz > 2.0)).astype(float).where(sd.notna() & vz.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_634_ipo_anchor_pct_distance_504d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(504, min_periods=168).min()
    rmax = high.rolling(504, min_periods=168).max()
    out = _safe_div(close - rmin, rmax - rmin)
    return out.diff()


def f50_tdco_635_magnetism_to_200d_sma_pct_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=84).mean()
    out = _safe_div(close - sma, close)
    return out.diff()


def f50_tdco_636_touch_count_200d_sma_within_2pct_252d_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=84).mean()
    touch = ((close - sma).abs() < 0.02 * close).astype(float).where(sma.notna(), np.nan)
    out = touch.rolling(252, min_periods=84).sum()
    return out.diff()


def f50_tdco_637_bars_since_last_200d_sma_cross_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=84).mean()
    above = (close > sma).astype(float)
    cross = (above != above.shift(1)).fillna(False) & sma.notna() & sma.shift(1).notna()
    out = _bars_since_true(cross)
    return out.diff()


def f50_tdco_638_magnetism_to_50d_sma_pct_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=21).mean()
    out = _safe_div(close - sma, close)
    return out.diff()


def f50_tdco_639_anchor_to_21d_mean_within_1pct_freq_252d_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(21, min_periods=7).mean()
    anc = ((close - sma).abs() < 0.01 * close).astype(float).where(sma.notna(), np.nan)
    out = anc.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_640_round_5dollar_within_5c_freq_252d_d1(close: pd.Series) -> pd.Series:
    nearest = (close / 5.0).round() * 5.0
    near = ((close - nearest).abs() < 0.05).astype(float).where(close.notna(), np.nan)
    out = near.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_641_distance_above_21d_low_pct_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    rmin21 = low.rolling(21, min_periods=7).min()
    out = _safe_div(close - rmin21, close)
    return out.diff()


def f50_tdco_642_attention_decay_post_spike_21d_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)
    spike = (vz > 2.0).astype(float)
    fut_vz = vz.shift(21)
    decay = (vz - fut_vz).where(spike > 0.5, np.nan)
    out = decay.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_643_cond_dist_52w_high_given_high_vol_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    dist = _safe_div(rmax - close, rmax)
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    out = dist.where(rv21 > med_rv, np.nan).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_644_attention_ret_magnitude_normed_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    abs_r = r.abs()
    mean_21 = abs_r.rolling(21, min_periods=7).mean()
    out = _safe_div(abs_r, mean_21).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_645_anchor_break_below_50d_sma_5pct_252d_d1(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=21).mean()
    ev = (close < 0.95 * sma).astype(float).where(sma.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_646_q05_ret_given_prior_5d_up_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r5p = _safe_log(close).diff(5).shift(1)
    cond = r.where(r5p > 0, np.nan)
    out = cond.rolling(252, min_periods=84).quantile(0.05)
    return out.diff()


def f50_tdco_647_q05_ret_given_prior_5d_down_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r5p = _safe_log(close).diff(5).shift(1)
    cond = r.where(r5p < 0, np.nan)
    out = cond.rolling(252, min_periods=84).quantile(0.05)
    return out.diff()


def f50_tdco_648_q01_ret_given_high_vol_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    cond = r.where(rv21 > med_rv, np.nan)
    out = cond.rolling(252, min_periods=84).quantile(0.01)
    return out.diff()


def f50_tdco_649_q95_ret_given_low_vol_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    cond = r.where(rv21 < med_rv, np.nan)
    out = cond.rolling(252, min_periods=84).quantile(0.95)
    return out.diff()


def f50_tdco_650_q99_minus_q01_spread_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q99 = r.rolling(252, min_periods=84).quantile(0.99)
    q01 = r.rolling(252, min_periods=84).quantile(0.01)
    out = q99 + q01
    return out.diff()


def f50_tdco_651_lower_tail_q1_minus_q5_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q1 = r.rolling(252, min_periods=84).quantile(0.01)
    q5 = r.rolling(252, min_periods=84).quantile(0.05)
    out = q1 - q5
    return out.diff()


def f50_tdco_652_upper_tail_q99_minus_q95_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q99 = r.rolling(252, min_periods=84).quantile(0.99)
    q95 = r.rolling(252, min_periods=84).quantile(0.95)
    out = q99 - q95
    return out.diff()


def f50_tdco_653_cond_mean_above_q95_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q95 = r.rolling(252, min_periods=84).quantile(0.95)
    tail = r.where(r >= q95, np.nan)
    out = tail.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_654_cond_mean_below_q05_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q05 = r.rolling(252, min_periods=84).quantile(0.05)
    tail = r.where(r <= q05, np.nan)
    out = tail.rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_655_mean_minus_median_at_252d_high_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax)
    cond_r = r.where(at_high, np.nan)
    m = cond_r.rolling(252, min_periods=84).mean()
    med = cond_r.rolling(252, min_periods=84).median()
    out = m - med
    return out.diff()


def f50_tdco_656_iqr_cond_on_up_trend_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21).shift(1)
    cond = r.where(ret21 > 0, np.nan)
    q75 = cond.rolling(252, min_periods=84).quantile(0.75)
    q25 = cond.rolling(252, min_periods=84).quantile(0.25)
    out = q75 - q25
    return out.diff()


def f50_tdco_657_iqr_cond_on_down_trend_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21).shift(1)
    cond = r.where(ret21 < 0, np.nan)
    q75 = cond.rolling(252, min_periods=84).quantile(0.75)
    q25 = cond.rolling(252, min_periods=84).quantile(0.25)
    out = q75 - q25
    return out.diff()


def f50_tdco_658_iqr_ratio_up_over_down_regime_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21).shift(1)
    up = r.where(ret21 > 0, np.nan)
    dn = r.where(ret21 < 0, np.nan)
    iqr_u = up.rolling(252, min_periods=84).quantile(0.75) - up.rolling(252, min_periods=84).quantile(0.25)
    iqr_d = dn.rolling(252, min_periods=84).quantile(0.75) - dn.rolling(252, min_periods=84).quantile(0.25)
    out = _safe_div(iqr_u, iqr_d)
    return out.diff()


def f50_tdco_659_neg_3sigma_day_vol_share_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r < -3.0 * sd)
    neg_vol = volume.where(ev, 0.0).rolling(252, min_periods=84).sum()
    tot_vol = volume.rolling(252, min_periods=84).sum()
    out = _safe_div(neg_vol, tot_vol)
    return out.diff()


def f50_tdco_660_pos_3sigma_day_vol_share_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r > 3.0 * sd)
    pos_vol = volume.where(ev, 0.0).rolling(252, min_periods=84).sum()
    tot_vol = volume.rolling(252, min_periods=84).sum()
    out = _safe_div(pos_vol, tot_vol)
    return out.diff()


def f50_tdco_661_ret_504d_minus_2x_ret_252d_d1(close: pd.Series) -> pd.Series:
    out = _safe_log(close).diff(504) - 2.0 * _safe_log(close).diff(252)
    return out.diff()


def f50_tdco_662_log_ret_1260d_d1(close: pd.Series) -> pd.Series:
    out = _safe_log(close).diff(1260)
    return out.diff()


def f50_tdco_663_slope_ratio_504d_over_252d_d1(close: pd.Series) -> pd.Series:
    out = _safe_div(_rolling_slope(_safe_log(close), 504, min_periods=168), _rolling_slope(_safe_log(close), 252, min_periods=84))
    return out.diff()


def f50_tdco_664_rv_1260d_over_252d_ratio_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _safe_div(r.rolling(1260, min_periods=252).std(), r.rolling(252, min_periods=84).std())
    return out.diff()


def f50_tdco_665_structural_break_mean_test_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    m1 = r.shift(252).rolling(252, min_periods=84).mean()
    m2 = r.rolling(252, min_periods=84).mean()
    sd = r.rolling(504, min_periods=168).std() / np.sqrt(252.0)
    out = _safe_div((m2 - m1).abs(), sd)
    return out.diff()


def f50_tdco_666_current_vs_1260d_mean_close_distance_pct_d1(close: pd.Series) -> pd.Series:
    m = close.rolling(1260, min_periods=252).mean()
    out = _safe_div(close - m, m)
    return out.diff()


def f50_tdco_667_cond_5d_ret_given_below_200d_sma_252d_d1(close: pd.Series) -> pd.Series:
    sma200 = close.rolling(200, min_periods=84).mean()
    below = (close < sma200).astype(bool)
    ret5 = _safe_log(close).diff(5)
    out = ret5.where(below, np.nan).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_668_cond_5d_ret_given_above_200d_sma_252d_d1(close: pd.Series) -> pd.Series:
    sma200 = close.rolling(200, min_periods=84).mean()
    above = (close > sma200).astype(bool)
    ret5 = _safe_log(close).diff(5)
    out = ret5.where(above, np.nan).rolling(252, min_periods=84).mean()
    return out.diff()


def f50_tdco_669_ar1_504d_minus_ar1_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ar1(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    ar504 = r.rolling(504, min_periods=168).apply(_ar1, raw=True)
    ar252 = r.rolling(252, min_periods=84).apply(_ar1, raw=True)
    out = ar504.abs() - ar252.abs()
    return out.diff()


def f50_tdco_670_new_504d_low_count_in_21d_d1(low: pd.Series) -> pd.Series:
    rmin504 = low.rolling(504, min_periods=168).min()
    ev = (low <= rmin504).astype(float).where(rmin504.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff()


def f50_tdco_671_new_1260d_high_count_in_21d_d1(high: pd.Series) -> pd.Series:
    rmax = high.rolling(1260, min_periods=252).max()
    ev = (high >= rmax).astype(float).where(rmax.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff()


def f50_tdco_672_cond_kurt_given_top_quintile_1260d_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=252).min()
    rmax = high.rolling(1260, min_periods=252).max()
    pos = _safe_div(close - rmin, rmax - rmin)
    top = (pos > 0.8).astype(bool)
    r = _safe_log(close).diff().where(top, np.nan)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 4) - 3.0)
    out = r.rolling(252, min_periods=84).apply(_kt, raw=True)
    return out.diff()


def f50_tdco_673_ret_252d_pct_rank_in_1260d_d1(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close).diff(252)
    out = _rolling_pct_rank(r252, 1260, min_periods=252)
    return out.diff()


def f50_tdco_674_ret_504d_pct_rank_in_1260d_d1(close: pd.Series) -> pd.Series:
    r504 = _safe_log(close).diff(504)
    out = _rolling_pct_rank(r504, 1260, min_periods=252)
    return out.diff()


def f50_tdco_675_max_dd_from_1260d_peak_pct_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(1260, min_periods=252).max()
    out = _safe_div(rmax - close, rmax)
    return out.diff()


# ============================================================
#                         REGISTRY 601_675 (d1)
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_D1_REGISTRY_601_675 = {
    "f50_tdco_601_frac_time_near_252d_low_5pct_252d_d1": {"inputs": ["low", "close"], "func": f50_tdco_601_frac_time_near_252d_low_5pct_252d_d1},
    "f50_tdco_602_rate_distance_from_252d_high_63d_d1": {"inputs": ["high", "close"], "func": f50_tdco_602_rate_distance_from_252d_high_63d_d1},
    "f50_tdco_603_stuck_dd50_no_recover_indicator_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_603_stuck_dd50_no_recover_indicator_252d_d1},
    "f50_tdco_604_bars_since_last_252d_high_d1": {"inputs": ["high"], "func": f50_tdco_604_bars_since_last_252d_high_d1},
    "f50_tdco_605_expected_time_to_next_peak_252d_d1": {"inputs": ["high"], "func": f50_tdco_605_expected_time_to_next_peak_252d_d1},
    "f50_tdco_606_hazard_new_1260d_low_252d_d1": {"inputs": ["low"], "func": f50_tdco_606_hazard_new_1260d_low_252d_d1},
    "f50_tdco_607_stuck_momentum_no_pos_63d_in_252d_d1": {"inputs": ["close"], "func": f50_tdco_607_stuck_momentum_no_pos_63d_in_252d_d1},
    "f50_tdco_608_indicator_504d_cum_decline_50pct_d1": {"inputs": ["close"], "func": f50_tdco_608_indicator_504d_cum_decline_50pct_d1},
    "f50_tdco_609_longest_gap_no_new_21d_high_252d_d1": {"inputs": ["high"], "func": f50_tdco_609_longest_gap_no_new_21d_high_252d_d1},
    "f50_tdco_610_cond_5d_ret_given_dd30_from_252d_high_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_610_cond_5d_ret_given_dd30_from_252d_high_252d_d1},
    "f50_tdco_611_hazard_5pct_gap_down_event_252d_d1": {"inputs": ["open", "close"], "func": f50_tdco_611_hazard_5pct_gap_down_event_252d_d1},
    "f50_tdco_612_cond_max_dd_21d_given_at_252d_high_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_612_cond_max_dd_21d_given_at_252d_high_252d_d1},
    "f50_tdco_613_sequential_lower_low_count_252d_d1": {"inputs": ["low"], "func": f50_tdco_613_sequential_lower_low_count_252d_d1},
    "f50_tdco_614_sequential_lower_high_count_252d_d1": {"inputs": ["high"], "func": f50_tdco_614_sequential_lower_high_count_252d_d1},
    "f50_tdco_615_hazard_new_504d_low_252d_d1": {"inputs": ["low"], "func": f50_tdco_615_hazard_new_504d_low_252d_d1},
    "f50_tdco_616_mean_5d_bounce_after_5pct_dd_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_616_mean_5d_bounce_after_5pct_dd_252d_d1},
    "f50_tdco_617_mean_21d_bounce_after_10pct_dd_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_617_mean_21d_bounce_after_10pct_dd_252d_d1},
    "f50_tdco_618_bounce_vol_conviction_ratio_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_618_bounce_vol_conviction_ratio_252d_d1},
    "f50_tdco_619_bounce_fizzle_rate_252d_d1": {"inputs": ["close"], "func": f50_tdco_619_bounce_fizzle_rate_252d_d1},
    "f50_tdco_620_pct_dd_recovered_21d_after_dd10_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_620_pct_dd_recovered_21d_after_dd10_252d_d1},
    "f50_tdco_621_recovery_success_rate_dd_gt_5pct_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_621_recovery_success_rate_dd_gt_5pct_252d_d1},
    "f50_tdco_622_bounce_vol_vs_252d_median_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_622_bounce_vol_vs_252d_median_252d_d1},
    "f50_tdco_623_reaction_rally_lower_high_rate_252d_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_623_reaction_rally_lower_high_rate_252d_d1},
    "f50_tdco_624_bounce_5d_decay_slope_63d_d1": {"inputs": ["close"], "func": f50_tdco_624_bounce_5d_decay_slope_63d_d1},
    "f50_tdco_625_up_day_vol_minus_down_day_vol_pct_rank_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_625_up_day_vol_minus_down_day_vol_pct_rank_252d_d1},
    "f50_tdco_626_bounce_rate_acceleration_21d_in_252d_d1": {"inputs": ["close"], "func": f50_tdco_626_bounce_rate_acceleration_21d_in_252d_d1},
    "f50_tdco_627_close_vs_21d_mean_post_decline_252d_d1": {"inputs": ["close"], "func": f50_tdco_627_close_vs_21d_mean_post_decline_252d_d1},
    "f50_tdco_628_actual_vs_expected_recovery_time_ratio_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_628_actual_vs_expected_recovery_time_ratio_252d_d1},
    "f50_tdco_629_bounce_75pct_percentile_252d_d1": {"inputs": ["close"], "func": f50_tdco_629_bounce_75pct_percentile_252d_d1},
    "f50_tdco_630_bounce_fail_to_hold_rate_63d_d1": {"inputs": ["close"], "func": f50_tdco_630_bounce_fail_to_hold_rate_63d_d1},
    "f50_tdco_631_nearest_round_dollar_distance_pct_d1": {"inputs": ["close"], "func": f50_tdco_631_nearest_round_dollar_distance_pct_d1},
    "f50_tdco_632_round_dollar_bear_next_freq_252d_d1": {"inputs": ["close"], "func": f50_tdco_632_round_dollar_bear_next_freq_252d_d1},
    "f50_tdco_633_attention_spike_3sigma_ret_vol2_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_633_attention_spike_3sigma_ret_vol2_252d_d1},
    "f50_tdco_634_ipo_anchor_pct_distance_504d_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_634_ipo_anchor_pct_distance_504d_d1},
    "f50_tdco_635_magnetism_to_200d_sma_pct_d1": {"inputs": ["close"], "func": f50_tdco_635_magnetism_to_200d_sma_pct_d1},
    "f50_tdco_636_touch_count_200d_sma_within_2pct_252d_d1": {"inputs": ["close"], "func": f50_tdco_636_touch_count_200d_sma_within_2pct_252d_d1},
    "f50_tdco_637_bars_since_last_200d_sma_cross_d1": {"inputs": ["close"], "func": f50_tdco_637_bars_since_last_200d_sma_cross_d1},
    "f50_tdco_638_magnetism_to_50d_sma_pct_d1": {"inputs": ["close"], "func": f50_tdco_638_magnetism_to_50d_sma_pct_d1},
    "f50_tdco_639_anchor_to_21d_mean_within_1pct_freq_252d_d1": {"inputs": ["close"], "func": f50_tdco_639_anchor_to_21d_mean_within_1pct_freq_252d_d1},
    "f50_tdco_640_round_5dollar_within_5c_freq_252d_d1": {"inputs": ["close"], "func": f50_tdco_640_round_5dollar_within_5c_freq_252d_d1},
    "f50_tdco_641_distance_above_21d_low_pct_d1": {"inputs": ["low", "close"], "func": f50_tdco_641_distance_above_21d_low_pct_d1},
    "f50_tdco_642_attention_decay_post_spike_21d_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_642_attention_decay_post_spike_21d_252d_d1},
    "f50_tdco_643_cond_dist_52w_high_given_high_vol_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_643_cond_dist_52w_high_given_high_vol_252d_d1},
    "f50_tdco_644_attention_ret_magnitude_normed_252d_d1": {"inputs": ["close"], "func": f50_tdco_644_attention_ret_magnitude_normed_252d_d1},
    "f50_tdco_645_anchor_break_below_50d_sma_5pct_252d_d1": {"inputs": ["close"], "func": f50_tdco_645_anchor_break_below_50d_sma_5pct_252d_d1},
    "f50_tdco_646_q05_ret_given_prior_5d_up_252d_d1": {"inputs": ["close"], "func": f50_tdco_646_q05_ret_given_prior_5d_up_252d_d1},
    "f50_tdco_647_q05_ret_given_prior_5d_down_252d_d1": {"inputs": ["close"], "func": f50_tdco_647_q05_ret_given_prior_5d_down_252d_d1},
    "f50_tdco_648_q01_ret_given_high_vol_252d_d1": {"inputs": ["close"], "func": f50_tdco_648_q01_ret_given_high_vol_252d_d1},
    "f50_tdco_649_q95_ret_given_low_vol_252d_d1": {"inputs": ["close"], "func": f50_tdco_649_q95_ret_given_low_vol_252d_d1},
    "f50_tdco_650_q99_minus_q01_spread_252d_d1": {"inputs": ["close"], "func": f50_tdco_650_q99_minus_q01_spread_252d_d1},
    "f50_tdco_651_lower_tail_q1_minus_q5_252d_d1": {"inputs": ["close"], "func": f50_tdco_651_lower_tail_q1_minus_q5_252d_d1},
    "f50_tdco_652_upper_tail_q99_minus_q95_252d_d1": {"inputs": ["close"], "func": f50_tdco_652_upper_tail_q99_minus_q95_252d_d1},
    "f50_tdco_653_cond_mean_above_q95_252d_d1": {"inputs": ["close"], "func": f50_tdco_653_cond_mean_above_q95_252d_d1},
    "f50_tdco_654_cond_mean_below_q05_252d_d1": {"inputs": ["close"], "func": f50_tdco_654_cond_mean_below_q05_252d_d1},
    "f50_tdco_655_mean_minus_median_at_252d_high_252d_d1": {"inputs": ["high", "close"], "func": f50_tdco_655_mean_minus_median_at_252d_high_252d_d1},
    "f50_tdco_656_iqr_cond_on_up_trend_252d_d1": {"inputs": ["close"], "func": f50_tdco_656_iqr_cond_on_up_trend_252d_d1},
    "f50_tdco_657_iqr_cond_on_down_trend_252d_d1": {"inputs": ["close"], "func": f50_tdco_657_iqr_cond_on_down_trend_252d_d1},
    "f50_tdco_658_iqr_ratio_up_over_down_regime_252d_d1": {"inputs": ["close"], "func": f50_tdco_658_iqr_ratio_up_over_down_regime_252d_d1},
    "f50_tdco_659_neg_3sigma_day_vol_share_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_659_neg_3sigma_day_vol_share_252d_d1},
    "f50_tdco_660_pos_3sigma_day_vol_share_252d_d1": {"inputs": ["close", "volume"], "func": f50_tdco_660_pos_3sigma_day_vol_share_252d_d1},
    "f50_tdco_661_ret_504d_minus_2x_ret_252d_d1": {"inputs": ["close"], "func": f50_tdco_661_ret_504d_minus_2x_ret_252d_d1},
    "f50_tdco_662_log_ret_1260d_d1": {"inputs": ["close"], "func": f50_tdco_662_log_ret_1260d_d1},
    "f50_tdco_663_slope_ratio_504d_over_252d_d1": {"inputs": ["close"], "func": f50_tdco_663_slope_ratio_504d_over_252d_d1},
    "f50_tdco_664_rv_1260d_over_252d_ratio_d1": {"inputs": ["close"], "func": f50_tdco_664_rv_1260d_over_252d_ratio_d1},
    "f50_tdco_665_structural_break_mean_test_504d_d1": {"inputs": ["close"], "func": f50_tdco_665_structural_break_mean_test_504d_d1},
    "f50_tdco_666_current_vs_1260d_mean_close_distance_pct_d1": {"inputs": ["close"], "func": f50_tdco_666_current_vs_1260d_mean_close_distance_pct_d1},
    "f50_tdco_667_cond_5d_ret_given_below_200d_sma_252d_d1": {"inputs": ["close"], "func": f50_tdco_667_cond_5d_ret_given_below_200d_sma_252d_d1},
    "f50_tdco_668_cond_5d_ret_given_above_200d_sma_252d_d1": {"inputs": ["close"], "func": f50_tdco_668_cond_5d_ret_given_above_200d_sma_252d_d1},
    "f50_tdco_669_ar1_504d_minus_ar1_252d_d1": {"inputs": ["close"], "func": f50_tdco_669_ar1_504d_minus_ar1_252d_d1},
    "f50_tdco_670_new_504d_low_count_in_21d_d1": {"inputs": ["low"], "func": f50_tdco_670_new_504d_low_count_in_21d_d1},
    "f50_tdco_671_new_1260d_high_count_in_21d_d1": {"inputs": ["high"], "func": f50_tdco_671_new_1260d_high_count_in_21d_d1},
    "f50_tdco_672_cond_kurt_given_top_quintile_1260d_range_252d_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_672_cond_kurt_given_top_quintile_1260d_range_252d_d1},
    "f50_tdco_673_ret_252d_pct_rank_in_1260d_d1": {"inputs": ["close"], "func": f50_tdco_673_ret_252d_pct_rank_in_1260d_d1},
    "f50_tdco_674_ret_504d_pct_rank_in_1260d_d1": {"inputs": ["close"], "func": f50_tdco_674_ret_504d_pct_rank_in_1260d_d1},
    "f50_tdco_675_max_dd_from_1260d_peak_pct_d1": {"inputs": ["high", "close"], "func": f50_tdco_675_max_dd_from_1260d_peak_pct_d1},
}
