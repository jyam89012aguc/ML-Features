"""short_squeeze_aftermath_technical d1 features 451-525 — Pipeline 1b-technical.

75 distinct INDIVIDUAL signal hypotheses extending the 450 existing features.
Themes: Hawkes self-excitation / survival hazard / reaction-rally failure /
volume-return lead-lag / microstructure clustering / squeeze-decay /
first-passage time / cross-bar coherence.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def f48_ssat_451_interevent_gap_std_3sigma_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        idx = np.where(v > 0.5)[0]
        if idx.size < 3:
            return np.nan
        return float(np.std(np.diff(idx), ddof=1))
    out = ev.astype(float).rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f48_ssat_452_hawkes_branching_ratio_3sigma_5d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    follow = ev * ev.shift(5).rolling(5, min_periods=1).max()
    out = follow.rolling(252, min_periods=84).sum() / ev.rolling(252, min_periods=84).sum().replace(0, np.nan)
    return out.diff()


def f48_ssat_453_hawkes_branching_neg_3sigma_10d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r < -3.0 * sd).astype(float)
    follow = ev * ev.shift(10).rolling(10, min_periods=1).max()
    out = follow.rolling(252, min_periods=84).sum() / ev.rolling(252, min_periods=84).sum().replace(0, np.nan)
    return out.diff()


def f48_ssat_454_interevent_3sigma_cv_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        idx = np.where(v > 0.5)[0]
        if idx.size < 3:
            return np.nan
        gaps = np.diff(idx)
        if np.mean(gaps) == 0:
            return np.nan
        return float(np.std(gaps, ddof=1) / np.mean(gaps))
    out = ev.astype(float).rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f48_ssat_455_cond_hazard_3sigma_given_recent_5d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    has_recent = ev.shift(1).rolling(5, min_periods=1).max()
    cond_ev = ev.where(has_recent > 0.5, np.nan)
    out = cond_ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_456_bars_since_last_3sigma_event_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd)
    out = _bars_since_true(ev)
    return out.diff()


def f48_ssat_457_bars_since_last_neg_3sigma_event_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r < -3.0 * sd)
    out = _bars_since_true(ev)
    return out.diff()


def f48_ssat_458_max_event_free_gap_3sigma_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
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


def f48_ssat_459_fano_factor_3sigma_events_21d_bins_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    bin_ct = ev.rolling(21, min_periods=7).sum()
    m = bin_ct.rolling(252, min_periods=84).mean()
    v = bin_ct.rolling(252, min_periods=84).var()
    out = _safe_div(v, m)
    return out.diff()


def f48_ssat_460_clustered_vs_isolated_3sigma_ratio_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    clustered = ev * (ev.shift(1).rolling(5, min_periods=1).max() + ev.shift(5).rolling(5, min_periods=1).max() > 0).astype(float)
    isolated = ev - clustered
    out = clustered.rolling(252, min_periods=84).sum() / isolated.rolling(252, min_periods=84).sum().replace(0, np.nan)
    return out.diff()


def f48_ssat_461_hawkes_self_excite_rate_prior_21d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    rate = ev.shift(1).rolling(21, min_periods=7).sum()
    # average rate AT event bars
    rate_at_ev = rate.where(ev > 0.5, np.nan)
    out = rate_at_ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_462_pos_to_neg_3sigma_event_ratio_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    pos_ev = (r > 3.0 * sd).astype(float).rolling(252, min_periods=84).sum()
    neg_ev = (r < -3.0 * sd).astype(float).rolling(252, min_periods=84).sum()
    out = _safe_div(pos_ev, neg_ev)
    return out.diff()


def f48_ssat_463_event_3sigma_21d_count_minus_63d_rate_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    out = ev.rolling(21, min_periods=7).sum() - ev.rolling(63, min_periods=21).sum() * 21.0 / 63.0
    return out.diff()


def f48_ssat_464_max_3sigma_5d_count_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    rolling5 = ev.rolling(5, min_periods=1).sum()
    out = rolling5.rolling(252, min_periods=84).max()
    return out.diff()


def f48_ssat_465_poisson_deviance_3sigma_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 3.0 * sd).astype(float)
    bin_ct = ev.rolling(21, min_periods=7).sum()
    m = bin_ct.rolling(252, min_periods=84).mean()
    v = bin_ct.rolling(252, min_periods=84).var()
    out = (v - m).abs() / m.replace(0, np.nan)
    return out.diff()


def f48_ssat_466_hazard_5pct_dd_from_21d_peak_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    peak21 = lc.rolling(21, min_periods=7).max()
    dd = peak21 - lc
    ev = (dd > 0.05).astype(float)
    out = ev.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_467_hazard_10pct_dd_from_21d_peak_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    peak21 = lc.rolling(21, min_periods=7).max()
    dd = peak21 - lc
    ev = (dd > 0.10).astype(float)
    out = ev.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_468_hazard_20pct_dd_from_63d_peak_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    peak = lc.rolling(63, min_periods=21).max()
    dd = peak - lc
    ev = (dd > 0.20).astype(float)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_469_fpt_5pct_below_21d_peak_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    peak21 = lc.rolling(21, min_periods=7).max()
    dd = peak21 - lc
    ev = (dd > 0.05)
    out = _bars_since_true(ev)
    return out.diff()


def f48_ssat_470_fpt_10pct_below_63d_peak_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    peak = lc.rolling(63, min_periods=21).max()
    dd = peak - lc
    ev = (dd > 0.10)
    out = _bars_since_true(ev)
    return out.diff()


def f48_ssat_471_cond_hazard_new_21d_low_given_5d_up_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    min21 = lc.rolling(21, min_periods=7).min()
    new_low = (lc <= min21).astype(float)
    up_prior = (lc.shift(1) - lc.shift(6) > 0).astype(float)
    ev = new_low * up_prior
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_472_bars_since_21d_peak_vs_252d_avg_d1(close: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        return float(w.size - 1 - int(np.nanargmax(w)))
    bars_since = close.rolling(21, min_periods=7).apply(_f_idx, raw=True)
    out = bars_since - bars_since.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_473_current_streak_above_252d_peak_90pct_d1(close: pd.Series) -> pd.Series:
    rmax = close.rolling(252, min_periods=84).max()
    above = (close >= 0.9 * rmax).astype(int).where(rmax.notna(), 0)
    block = (above != above.shift(1)).fillna(False).cumsum()
    st = above.groupby(block).cumcount().astype(float)
    out = (st * (above > 0)).where(rmax.notna(), np.nan)
    return out.diff()


def f48_ssat_474_hazard_3sigma_down_no_bounce_5d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r < -3.0 * sd).astype(float)
    no_bounce = (r.shift(5).rolling(5, min_periods=1).max() < sd * 0.5).astype(float)
    out = (ev * no_bounce).rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_475_mean_underwater_spell_length_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        peak = np.maximum.accumulate(v)
        under = (peak - v) > 0
        spells = []; cur = 0
        for u in under:
            if u: cur += 1
            else:
                if cur > 0: spells.append(cur); cur = 0
        if cur > 0: spells.append(cur)
        if not spells:
            return 0.0
        return float(np.mean(spells))
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f48_ssat_476_max_5d_cum_loss_capped_21d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cum5 = r.rolling(5, min_periods=2).sum()
    out = (-cum5.rolling(21, min_periods=7).min()).rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_477_bars_to_recover_from_5pct_dd_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=21).max()
    dd_5pct = (rmax - lc > 0.05)
    # bars-since-last-time-NOT-in-dd5pct
    out = _bars_since_true(~dd_5pct)
    return out.diff()


def f48_ssat_478_consec_5d_negative_blocks_streak_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    neg = (r5 < 0).astype(int).where(r5.notna(), 0)
    block = (neg != neg.shift(1)).fillna(False).cumsum()
    st = neg.groupby(block).cumcount().astype(float)
    out = (st * (neg > 0)).where(r5.notna(), np.nan)
    return out.diff()


def f48_ssat_479_cond_hazard_break_63d_low_given_21d_high_30d_prior_d1(close: pd.Series) -> pd.Series:
    rmin63 = close.rolling(63, min_periods=21).min()
    rmax21_30 = close.shift(30).rolling(21, min_periods=7).max()
    ev = ((close <= rmin63) & (close.shift(30) >= 0.95 * rmax21_30)).astype(float)
    out = ev.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_480_hazard_new_252d_low_indicator_504d_d1(close: pd.Series) -> pd.Series:
    rmin252 = close.rolling(252, min_periods=84).min()
    ev = (close <= rmin252).astype(float).where(rmin252.notna(), np.nan)
    out = ev.rolling(504, min_periods=168).mean()
    return out.diff()


def f48_ssat_481_bounce_strength_5d_after_5d_decline_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    prior_decline = -r5.shift(5).where(r5.shift(5) < 0, np.nan)
    rally = r5.where(r5.shift(5) < 0, np.nan)
    out = _safe_div(rally, prior_decline)
    return out.diff()


def f48_ssat_482_rally_after_10pct_decline_pct_recovered_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    # 5d-rally only counted after 10pct prior 21d decline
    prior21 = _safe_log(close).diff(21).shift(5)
    cond_rally = r5.where(prior21 < -0.10, np.nan)
    out = cond_rally.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_483_failed_50pct_retrace_count_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    rmin = lc.rolling(63, min_periods=21).min()
    rmax = lc.rolling(63, min_periods=21).max()
    range_5pct = (rmax - rmin) * 0.5
    # Bars where 21d-bounce didn't exceed 50% retrace from local min
    bounce21 = lc - rmin
    failed = ((lc.shift(21).rolling(21, min_periods=7).max() - rmin) < range_5pct).astype(float).where(range_5pct.notna(), np.nan)
    out = failed.rolling(252, min_periods=84).sum()
    return out.diff()


def f48_ssat_484_lower_high_after_21d_low_rate_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    at_low = (lc <= lc.rolling(21, min_periods=7).min()).astype(float)
    posthigh = lc.shift(21).rolling(21, min_periods=7).max()
    priorhigh = lc.shift(21).rolling(21, min_periods=7).max()
    low_then_lower = at_low * (posthigh < priorhigh).astype(float)
    out = low_then_lower.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_485_rally_amplitude_decay_slope_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    pos = r5.clip(lower=0).rolling(21, min_periods=7).max()
    out = pos.diff(63)
    return out.diff()


def f48_ssat_486_rally_vol_to_decline_vol_ratio_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rally_vol = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    decline_vol = volume.where(r < 0, 0.0).rolling(63, min_periods=21).sum()
    out = _safe_div(rally_vol, decline_vol)
    return out.diff()


def f48_ssat_487_mean_reversion_strength_actual_vs_expected_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    prior_neg = r.shift(1).clip(upper=0)
    expected = -prior_neg * 0.3  # ~30% mean revert assumption
    actual = r.where(prior_neg < 0, np.nan)
    out = _safe_div(actual.rolling(252, min_periods=84).mean(), expected.rolling(252, min_periods=84).mean())
    return out.diff()


def f48_ssat_488_consec_no_rally_5d_streak_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5)
    no_rally = (r5 <= 0).astype(int).where(r5.notna(), 0)
    block = (no_rally != no_rally.shift(1)).fillna(False).cumsum()
    st = no_rally.groupby(block).cumcount().astype(float)
    out = (st * (no_rally > 0)).where(r5.notna(), np.nan)
    return out.diff()


def f48_ssat_489_bounce_5d_after_3sigma_down_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    big_down = (r.shift(5) < -3.0 * sd.shift(5))
    bounce5 = _safe_log(close).diff(5).where(big_down, np.nan)
    out = bounce5.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_490_sustained_decline_4_of_5_indicator_21d_density_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    down = (r < 0).astype(float)
    out = (down.rolling(5, min_periods=3).sum() >= 4).astype(float).where(r.notna(), np.nan).rolling(21, min_periods=7).mean()
    return out.diff()


def f48_ssat_491_rally_vol_zscore_minus_decline_vol_zscore_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv_up = volume.where(r > 0, np.nan).rolling(63, min_periods=21).mean()
    rv_dn = volume.where(r < 0, np.nan).rolling(63, min_periods=21).mean()
    zu = _rolling_zscore(rv_up, 252, min_periods=84)
    zd = _rolling_zscore(rv_dn, 252, min_periods=84)
    out = zu - zd
    return out.diff()


def f48_ssat_492_close_to_21d_high_after_recent_low_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    max21 = lc.rolling(21, min_periods=7).max()
    at_low = (lc.shift(10) <= lc.shift(10).rolling(21, min_periods=7).min()).astype(float)
    recover = (max21 - lc) * at_low
    out = recover.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_493_mean_5d_return_after_neg_day_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r5_after = _safe_log(close).diff(5).shift(5)
    cond = r5_after.where(r < 0, np.nan)
    out = cond.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_494_rally_count_after_3sigma_down_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    capit = (r.shift(5) < -3.0 * sd.shift(5)).astype(float)
    rally5 = (_safe_log(close).diff(5) > 0.05).astype(float)
    out = (capit * rally5).rolling(252, min_periods=84).sum()
    return out.diff()


def f48_ssat_495_rally_5d_magnitude_pct_rank_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(5).clip(lower=0)
    out = _rolling_pct_rank(r5, 252, min_periods=84)
    return out.diff()


def f48_ssat_496_vol_t_minus_1_to_ret_t_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = volume.shift(1).rolling(63, min_periods=21).corr(r)
    return out.diff()


def f48_ssat_497_ret_t_minus_1_to_vol_t_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.shift(1).rolling(63, min_periods=21).corr(volume)
    return out.diff()


def f48_ssat_498_vol_ret_lead_lag_asym_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    c1 = volume.rolling(63, min_periods=21).corr(r.shift(1)).abs()
    c2 = r.rolling(63, min_periods=21).corr(volume.shift(1)).abs()
    out = c1 - c2
    return out.diff()


def f48_ssat_499_signed_vol_to_neg_ret_lag1_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sgn = np.sign(r)
    sv = sgn * volume
    out = sv.shift(1).rolling(63, min_periods=21).corr(r.where(r < 0, 0.0))
    return out.diff()


def f48_ssat_500_abs_ret_leads_vol_lag1_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    out = r.shift(1).rolling(63, min_periods=21).corr(volume)
    return out.diff()


def f48_ssat_501_signed_vol_60d_minus_price_60d_zscore_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sgn = np.sign(r)
    sv60 = (sgn * volume).rolling(60, min_periods=21).sum()
    ret60 = r.rolling(60, min_periods=21).sum()
    sv_z = _rolling_zscore(sv60, 252, min_periods=84)
    ret_z = _rolling_zscore(ret60, 252, min_periods=84)
    out = sv_z - ret_z
    return out.diff()


def f48_ssat_502_abs_ret_volume_info_corr_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    out = _safe_log(close).diff().abs().rolling(21, min_periods=7).corr(_safe_log(volume.replace(0, np.nan)))
    return out.diff()


def f48_ssat_503_signed_imbalance_vs_price_sign_mismatch_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sgn_p = np.sign(r)
    sgn_v = np.sign(r) * volume
    imb = sgn_v.rolling(5, min_periods=2).sum()
    mismatch = (np.sign(imb) != sgn_p).astype(float).where(sgn_p.notna() & imb.notna(), np.nan)
    out = mismatch.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_504_vol_lag1_to_realized_vol_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    rv = _safe_log(close).diff().rolling(21, min_periods=7).std()
    out = volume.shift(1).rolling(63, min_periods=21).corr(rv)
    return out.diff()


def f48_ssat_505_vol_spike_then_5d_decline_rate_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)
    spike = (vz > 2.0).astype(float)
    decline5 = (_safe_log(close).diff(5).shift(5) < -0.05).astype(float)
    out = (spike * decline5).rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_506_ret_lag2_to_vol_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.shift(2).rolling(63, min_periods=21).corr(volume)
    return out.diff()


def f48_ssat_507_cum_signed_vol_to_cum_ret_ratio_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sv = np.sign(r) * volume
    cum_sv = sv.rolling(63, min_periods=21).sum()
    cum_r = r.rolling(63, min_periods=21).sum()
    out = _safe_div(cum_sv, cum_r * volume.rolling(63, min_periods=21).mean())
    return out.diff()


def f48_ssat_508_cum_negative_day_signed_vol_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = (volume.where(r < 0, 0.0) * np.sign(r)).rolling(63, min_periods=21).sum()
    return out.diff()


def f48_ssat_509_cum_positive_day_signed_vol_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    return out.diff()


def f48_ssat_510_selling_pressure_dominance_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    neg_v = volume.where(r < 0, 0.0).rolling(63, min_periods=21).sum()
    pos_v = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    out = _safe_div(neg_v - pos_v, neg_v + pos_v)
    return out.diff()


def f48_ssat_511_round_number_rejection_rate_252d_d1(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(float)
    at_round = ((cents % 100) == 0).astype(float)
    bear_next = (close.shift(1) < close).astype(float)
    rej = at_round * bear_next
    out = rej.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_512_round_number_attraction_within_1pct_252d_d1(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(float)
    nearest_round = (cents / 100).round() * 100
    attract = ((cents - nearest_round).abs() < cents * 0.01).astype(float)
    out = attract.rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_513_hl_minus_oc_fragmentation_index_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = high - low
    oc = (open - close).abs()
    frag = _safe_div(hl - oc, hl)
    out = frag.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_514_closing_auction_extreme_close_change_63d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    intra = (close - open).abs() / open
    out = _rolling_pct_rank(intra, 63, min_periods=21)
    return out.diff()


def f48_ssat_515_squeeze_volume_half_life_post_max_63d_d1(volume: pd.Series) -> pd.Series:
    def _hl(w):
        if w.size < 30 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk >= w.size - 1:
            return np.nan
        peak_v = w[pk]
        if not np.isfinite(peak_v):
            return np.nan
        for j in range(pk + 1, w.size):
            if not np.isnan(w[j]) and w[j] <= 0.5 * peak_v:
                return float(j - pk)
        return float(w.size - pk)
    out = volume.rolling(63, min_periods=21).apply(_hl, raw=True)
    return out.diff()


def f48_ssat_516_squeeze_vol_ratio_peak_to_post21_63d_d1(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 30 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk > w.size - 22:
            return np.nan
        peak_v = w[pk]
        post = w[pk + 1:pk + 22]
        if peak_v <= 0 or np.isnan(post).all():
            return np.nan
        return float(peak_v / np.nanmean(post))
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f48_ssat_517_close_vs_bar_midpoint_norm_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    dev = _safe_div(close - mid, high - low)
    out = dev.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_518_close_in_bottom_10pct_range_freq_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    bot = (pos < 0.10).astype(float).where(pos.notna(), np.nan)
    out = bot.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_519_close_in_top_10pct_range_freq_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    top = (pos > 0.90).astype(float).where(pos.notna(), np.nan)
    out = top.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_520_close_low_minus_high_freq_diff_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    bot = (pos < 0.10).astype(float).where(pos.notna(), np.nan).rolling(63, min_periods=21).mean()
    top = (pos > 0.90).astype(float).where(pos.notna(), np.nan).rolling(63, min_periods=21).mean()
    out = bot - top
    return out.diff()


def f48_ssat_521_atr_ratio_peak_to_post21_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, n=21)
    def _f(w):
        if w.size < 30 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk > w.size - 22:
            return np.nan
        peak = w[pk]; post = np.nanmean(w[pk + 1:pk + 22])
        if peak <= 0 or not np.isfinite(post):
            return np.nan
        return float(peak / post)
    out = atr.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff()


def f48_ssat_522_bar_internal_momentum_slope_21d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body_frac = _safe_div((close - open).abs(), high - low)
    out = body_frac.rolling(21, min_periods=7).mean() - body_frac.rolling(21, min_periods=7).mean().shift(21)
    return out.diff()


def f48_ssat_523_same_sign_close_run_density_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    same = (np.sign(r) == np.sign(r.shift(1))).astype(float).where(r.notna() & r.shift(1).notna(), np.nan)
    out = same.rolling(63, min_periods=21).mean()
    return out.diff()


def f48_ssat_524_large_range_small_body_freq_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open).abs()
    large_rng = (rng > rng.rolling(63, min_periods=21).mean() * 1.5).astype(float)
    small_body = (body < rng * 0.3).astype(float)
    out = (large_rng * small_body).rolling(252, min_periods=84).mean()
    return out.diff()


def f48_ssat_525_consec_5d_overlap_density_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    ov_h = pd.concat([high, high.shift(1)], axis=1).min(axis=1)
    ov_l = pd.concat([low, low.shift(1)], axis=1).max(axis=1)
    ov = (ov_h - ov_l).clip(lower=0)
    ov_pct = _safe_div(ov, high - low)
    out = ov_pct.rolling(252, min_periods=84).mean()
    return out.diff()


# ============================================================
#                         REGISTRY 451_525 (d1)
# ============================================================

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_D1_REGISTRY_451_525 = {
    "f48_ssat_451_interevent_gap_std_3sigma_252d_d1": {"inputs": ["close"], "func": f48_ssat_451_interevent_gap_std_3sigma_252d_d1},
    "f48_ssat_452_hawkes_branching_ratio_3sigma_5d_252d_d1": {"inputs": ["close"], "func": f48_ssat_452_hawkes_branching_ratio_3sigma_5d_252d_d1},
    "f48_ssat_453_hawkes_branching_neg_3sigma_10d_252d_d1": {"inputs": ["close"], "func": f48_ssat_453_hawkes_branching_neg_3sigma_10d_252d_d1},
    "f48_ssat_454_interevent_3sigma_cv_252d_d1": {"inputs": ["close"], "func": f48_ssat_454_interevent_3sigma_cv_252d_d1},
    "f48_ssat_455_cond_hazard_3sigma_given_recent_5d_252d_d1": {"inputs": ["close"], "func": f48_ssat_455_cond_hazard_3sigma_given_recent_5d_252d_d1},
    "f48_ssat_456_bars_since_last_3sigma_event_d1": {"inputs": ["close"], "func": f48_ssat_456_bars_since_last_3sigma_event_d1},
    "f48_ssat_457_bars_since_last_neg_3sigma_event_d1": {"inputs": ["close"], "func": f48_ssat_457_bars_since_last_neg_3sigma_event_d1},
    "f48_ssat_458_max_event_free_gap_3sigma_252d_d1": {"inputs": ["close"], "func": f48_ssat_458_max_event_free_gap_3sigma_252d_d1},
    "f48_ssat_459_fano_factor_3sigma_events_21d_bins_252d_d1": {"inputs": ["close"], "func": f48_ssat_459_fano_factor_3sigma_events_21d_bins_252d_d1},
    "f48_ssat_460_clustered_vs_isolated_3sigma_ratio_252d_d1": {"inputs": ["close"], "func": f48_ssat_460_clustered_vs_isolated_3sigma_ratio_252d_d1},
    "f48_ssat_461_hawkes_self_excite_rate_prior_21d_252d_d1": {"inputs": ["close"], "func": f48_ssat_461_hawkes_self_excite_rate_prior_21d_252d_d1},
    "f48_ssat_462_pos_to_neg_3sigma_event_ratio_252d_d1": {"inputs": ["close"], "func": f48_ssat_462_pos_to_neg_3sigma_event_ratio_252d_d1},
    "f48_ssat_463_event_3sigma_21d_count_minus_63d_rate_d1": {"inputs": ["close"], "func": f48_ssat_463_event_3sigma_21d_count_minus_63d_rate_d1},
    "f48_ssat_464_max_3sigma_5d_count_in_252d_d1": {"inputs": ["close"], "func": f48_ssat_464_max_3sigma_5d_count_in_252d_d1},
    "f48_ssat_465_poisson_deviance_3sigma_252d_d1": {"inputs": ["close"], "func": f48_ssat_465_poisson_deviance_3sigma_252d_d1},
    "f48_ssat_466_hazard_5pct_dd_from_21d_peak_63d_d1": {"inputs": ["close"], "func": f48_ssat_466_hazard_5pct_dd_from_21d_peak_63d_d1},
    "f48_ssat_467_hazard_10pct_dd_from_21d_peak_63d_d1": {"inputs": ["close"], "func": f48_ssat_467_hazard_10pct_dd_from_21d_peak_63d_d1},
    "f48_ssat_468_hazard_20pct_dd_from_63d_peak_252d_d1": {"inputs": ["close"], "func": f48_ssat_468_hazard_20pct_dd_from_63d_peak_252d_d1},
    "f48_ssat_469_fpt_5pct_below_21d_peak_252d_d1": {"inputs": ["close"], "func": f48_ssat_469_fpt_5pct_below_21d_peak_252d_d1},
    "f48_ssat_470_fpt_10pct_below_63d_peak_252d_d1": {"inputs": ["close"], "func": f48_ssat_470_fpt_10pct_below_63d_peak_252d_d1},
    "f48_ssat_471_cond_hazard_new_21d_low_given_5d_up_252d_d1": {"inputs": ["close"], "func": f48_ssat_471_cond_hazard_new_21d_low_given_5d_up_252d_d1},
    "f48_ssat_472_bars_since_21d_peak_vs_252d_avg_d1": {"inputs": ["close"], "func": f48_ssat_472_bars_since_21d_peak_vs_252d_avg_d1},
    "f48_ssat_473_current_streak_above_252d_peak_90pct_d1": {"inputs": ["close"], "func": f48_ssat_473_current_streak_above_252d_peak_90pct_d1},
    "f48_ssat_474_hazard_3sigma_down_no_bounce_5d_252d_d1": {"inputs": ["close"], "func": f48_ssat_474_hazard_3sigma_down_no_bounce_5d_252d_d1},
    "f48_ssat_475_mean_underwater_spell_length_252d_d1": {"inputs": ["close"], "func": f48_ssat_475_mean_underwater_spell_length_252d_d1},
    "f48_ssat_476_max_5d_cum_loss_capped_21d_252d_d1": {"inputs": ["close"], "func": f48_ssat_476_max_5d_cum_loss_capped_21d_252d_d1},
    "f48_ssat_477_bars_to_recover_from_5pct_dd_252d_d1": {"inputs": ["close"], "func": f48_ssat_477_bars_to_recover_from_5pct_dd_252d_d1},
    "f48_ssat_478_consec_5d_negative_blocks_streak_d1": {"inputs": ["close"], "func": f48_ssat_478_consec_5d_negative_blocks_streak_d1},
    "f48_ssat_479_cond_hazard_break_63d_low_given_21d_high_30d_prior_d1": {"inputs": ["close"], "func": f48_ssat_479_cond_hazard_break_63d_low_given_21d_high_30d_prior_d1},
    "f48_ssat_480_hazard_new_252d_low_indicator_504d_d1": {"inputs": ["close"], "func": f48_ssat_480_hazard_new_252d_low_indicator_504d_d1},
    "f48_ssat_481_bounce_strength_5d_after_5d_decline_d1": {"inputs": ["close"], "func": f48_ssat_481_bounce_strength_5d_after_5d_decline_d1},
    "f48_ssat_482_rally_after_10pct_decline_pct_recovered_252d_d1": {"inputs": ["close"], "func": f48_ssat_482_rally_after_10pct_decline_pct_recovered_252d_d1},
    "f48_ssat_483_failed_50pct_retrace_count_252d_d1": {"inputs": ["close"], "func": f48_ssat_483_failed_50pct_retrace_count_252d_d1},
    "f48_ssat_484_lower_high_after_21d_low_rate_252d_d1": {"inputs": ["close"], "func": f48_ssat_484_lower_high_after_21d_low_rate_252d_d1},
    "f48_ssat_485_rally_amplitude_decay_slope_252d_d1": {"inputs": ["close"], "func": f48_ssat_485_rally_amplitude_decay_slope_252d_d1},
    "f48_ssat_486_rally_vol_to_decline_vol_ratio_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_486_rally_vol_to_decline_vol_ratio_63d_d1},
    "f48_ssat_487_mean_reversion_strength_actual_vs_expected_252d_d1": {"inputs": ["close"], "func": f48_ssat_487_mean_reversion_strength_actual_vs_expected_252d_d1},
    "f48_ssat_488_consec_no_rally_5d_streak_d1": {"inputs": ["close"], "func": f48_ssat_488_consec_no_rally_5d_streak_d1},
    "f48_ssat_489_bounce_5d_after_3sigma_down_252d_d1": {"inputs": ["close"], "func": f48_ssat_489_bounce_5d_after_3sigma_down_252d_d1},
    "f48_ssat_490_sustained_decline_4_of_5_indicator_21d_density_d1": {"inputs": ["close"], "func": f48_ssat_490_sustained_decline_4_of_5_indicator_21d_density_d1},
    "f48_ssat_491_rally_vol_zscore_minus_decline_vol_zscore_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_491_rally_vol_zscore_minus_decline_vol_zscore_63d_d1},
    "f48_ssat_492_close_to_21d_high_after_recent_low_252d_d1": {"inputs": ["close"], "func": f48_ssat_492_close_to_21d_high_after_recent_low_252d_d1},
    "f48_ssat_493_mean_5d_return_after_neg_day_252d_d1": {"inputs": ["close"], "func": f48_ssat_493_mean_5d_return_after_neg_day_252d_d1},
    "f48_ssat_494_rally_count_after_3sigma_down_252d_d1": {"inputs": ["close"], "func": f48_ssat_494_rally_count_after_3sigma_down_252d_d1},
    "f48_ssat_495_rally_5d_magnitude_pct_rank_252d_d1": {"inputs": ["close"], "func": f48_ssat_495_rally_5d_magnitude_pct_rank_252d_d1},
    "f48_ssat_496_vol_t_minus_1_to_ret_t_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_496_vol_t_minus_1_to_ret_t_corr_63d_d1},
    "f48_ssat_497_ret_t_minus_1_to_vol_t_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_497_ret_t_minus_1_to_vol_t_corr_63d_d1},
    "f48_ssat_498_vol_ret_lead_lag_asym_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_498_vol_ret_lead_lag_asym_63d_d1},
    "f48_ssat_499_signed_vol_to_neg_ret_lag1_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_499_signed_vol_to_neg_ret_lag1_corr_63d_d1},
    "f48_ssat_500_abs_ret_leads_vol_lag1_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_500_abs_ret_leads_vol_lag1_corr_63d_d1},
    "f48_ssat_501_signed_vol_60d_minus_price_60d_zscore_d1": {"inputs": ["close", "volume"], "func": f48_ssat_501_signed_vol_60d_minus_price_60d_zscore_d1},
    "f48_ssat_502_abs_ret_volume_info_corr_21d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_502_abs_ret_volume_info_corr_21d_d1},
    "f48_ssat_503_signed_imbalance_vs_price_sign_mismatch_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_503_signed_imbalance_vs_price_sign_mismatch_63d_d1},
    "f48_ssat_504_vol_lag1_to_realized_vol_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_504_vol_lag1_to_realized_vol_corr_63d_d1},
    "f48_ssat_505_vol_spike_then_5d_decline_rate_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_505_vol_spike_then_5d_decline_rate_63d_d1},
    "f48_ssat_506_ret_lag2_to_vol_corr_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_506_ret_lag2_to_vol_corr_63d_d1},
    "f48_ssat_507_cum_signed_vol_to_cum_ret_ratio_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_507_cum_signed_vol_to_cum_ret_ratio_63d_d1},
    "f48_ssat_508_cum_negative_day_signed_vol_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_508_cum_negative_day_signed_vol_63d_d1},
    "f48_ssat_509_cum_positive_day_signed_vol_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_509_cum_positive_day_signed_vol_63d_d1},
    "f48_ssat_510_selling_pressure_dominance_63d_d1": {"inputs": ["close", "volume"], "func": f48_ssat_510_selling_pressure_dominance_63d_d1},
    "f48_ssat_511_round_number_rejection_rate_252d_d1": {"inputs": ["close"], "func": f48_ssat_511_round_number_rejection_rate_252d_d1},
    "f48_ssat_512_round_number_attraction_within_1pct_252d_d1": {"inputs": ["close"], "func": f48_ssat_512_round_number_attraction_within_1pct_252d_d1},
    "f48_ssat_513_hl_minus_oc_fragmentation_index_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f48_ssat_513_hl_minus_oc_fragmentation_index_63d_d1},
    "f48_ssat_514_closing_auction_extreme_close_change_63d_d1": {"inputs": ["open", "close"], "func": f48_ssat_514_closing_auction_extreme_close_change_63d_d1},
    "f48_ssat_515_squeeze_volume_half_life_post_max_63d_d1": {"inputs": ["volume"], "func": f48_ssat_515_squeeze_volume_half_life_post_max_63d_d1},
    "f48_ssat_516_squeeze_vol_ratio_peak_to_post21_63d_d1": {"inputs": ["volume"], "func": f48_ssat_516_squeeze_vol_ratio_peak_to_post21_63d_d1},
    "f48_ssat_517_close_vs_bar_midpoint_norm_63d_d1": {"inputs": ["high", "low", "close"], "func": f48_ssat_517_close_vs_bar_midpoint_norm_63d_d1},
    "f48_ssat_518_close_in_bottom_10pct_range_freq_63d_d1": {"inputs": ["high", "low", "close"], "func": f48_ssat_518_close_in_bottom_10pct_range_freq_63d_d1},
    "f48_ssat_519_close_in_top_10pct_range_freq_63d_d1": {"inputs": ["high", "low", "close"], "func": f48_ssat_519_close_in_top_10pct_range_freq_63d_d1},
    "f48_ssat_520_close_low_minus_high_freq_diff_63d_d1": {"inputs": ["high", "low", "close"], "func": f48_ssat_520_close_low_minus_high_freq_diff_63d_d1},
    "f48_ssat_521_atr_ratio_peak_to_post21_63d_d1": {"inputs": ["high", "low", "close"], "func": f48_ssat_521_atr_ratio_peak_to_post21_63d_d1},
    "f48_ssat_522_bar_internal_momentum_slope_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f48_ssat_522_bar_internal_momentum_slope_21d_d1},
    "f48_ssat_523_same_sign_close_run_density_63d_d1": {"inputs": ["close"], "func": f48_ssat_523_same_sign_close_run_density_63d_d1},
    "f48_ssat_524_large_range_small_body_freq_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f48_ssat_524_large_range_small_body_freq_252d_d1},
    "f48_ssat_525_consec_5d_overlap_density_252d_d1": {"inputs": ["high", "low"], "func": f48_ssat_525_consec_5d_overlap_density_252d_d1},
}
