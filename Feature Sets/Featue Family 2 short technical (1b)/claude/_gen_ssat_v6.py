"""Generator EXTENSION for 48_short_squeeze_aftermath_technical (451-525).

Produces 4 new files: base/d1/d2/d3 x (451-525). 75 distinct, individual signals
targeting concepts NOT already in the 450 existing features.

INDIVIDUAL SIGNAL philosophy: each feature is ONE distinct calculation, NOT a
composite. Goal: orthogonal coverage that increases ML AUC/recall on the
'stuck at peak' label (touch -80% AND no recover above -50% in 5y).

Themes:
- Hawkes self-excitation proxies (event clustering / time-between-events)
- Survival hazard rates at various drawdown levels
- Reaction-rally failure quantification (post-decline bounces)
- Volume-return lead/lag asymmetry (toxic-flow at peak)
- Microstructure price-clustering effects (round-number aversion)
- Squeeze-decay half-life dynamics
- First-passage time statistics (time to N% loss)
- Cross-bar internal coherence (HL vs OC fragmentation)
"""
import os

ROOT = r"C:\Users\jyama\Desktop\short_technical_features_1b\48_short_squeeze_aftermath_technical"

HEADER_FMT = '''"""short_squeeze_aftermath_technical {order} features {lo:03d}-{hi:03d} — Pipeline 1b-technical.

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
'''

FEATS = []


def add(idx, suffix, inputs, body):
    lines = []
    for ln in body.splitlines():
        if ln.strip() == "":
            lines.append("")
        else:
            lines.append("    " + ln)
    FEATS.append((idx, suffix, inputs, "\n".join(lines)))


# ==================================================================
# Group A (451-465) — Hawkes self-excitation / event clustering
# ==================================================================

# 451 inter-event gap std (3sigma events) — high std = clustering
add(451, "interevent_gap_std_3sigma_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    idx = np.where(v > 0.5)[0]\n    if idx.size < 3:\n        return np.nan\n    return float(np.std(np.diff(idx), ddof=1))\nout = ev.astype(float).rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 452 Hawkes branching ratio proxy: fraction of 3sigma events within 5d of prior 3sigma event
add(452, "hawkes_branching_ratio_3sigma_5d_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nfollow = ev * ev.shift(-5).rolling(5, min_periods=1).max()\nout = follow.rolling(252, min_periods=84).sum() / ev.rolling(252, min_periods=84).sum().replace(0, np.nan)\n")

# 453 Hawkes branching downside-only (negative 3sigma followed by another within 10d)
add(453, "hawkes_branching_neg_3sigma_10d_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r < -3.0 * sd).astype(float)\nfollow = ev * ev.shift(-10).rolling(10, min_periods=1).max()\nout = follow.rolling(252, min_periods=84).sum() / ev.rolling(252, min_periods=84).sum().replace(0, np.nan)\n")

# 454 inter-3sigma-event coefficient of variation (gap std / gap mean)
add(454, "interevent_3sigma_cv_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    idx = np.where(v > 0.5)[0]\n    if idx.size < 3:\n        return np.nan\n    gaps = np.diff(idx)\n    if np.mean(gaps) == 0:\n        return np.nan\n    return float(np.std(gaps, ddof=1) / np.mean(gaps))\nout = ev.astype(float).rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 455 conditional hazard of next 3sigma event given event in last 5d
add(455, "cond_hazard_3sigma_given_recent_5d_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nhas_recent = ev.shift(1).rolling(5, min_periods=1).max()\ncond_ev = ev.where(has_recent > 0.5, np.nan)\nout = cond_ev.rolling(252, min_periods=84).mean()\n")

# 456 time-since-last-3sigma-event
add(456, "bars_since_last_3sigma_event", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd)\nout = _bars_since_true(ev)\n")

# 457 time-since-last-negative-3sigma event
add(457, "bars_since_last_neg_3sigma_event", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r < -3.0 * sd)\nout = _bars_since_true(ev)\n")

# 458 max consecutive-no-event run (longest event-free gap in 252d)
add(458, "max_event_free_gap_3sigma_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    best = 0; cur = 0\n    for x in v:\n        if x < 0.5:\n            cur += 1\n            if cur > best:\n                best = cur\n        else:\n            cur = 0\n    return float(best)\nout = ev.rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 459 fano factor of 3sigma events 252d (var/mean of bin-counts)
add(459, "fano_factor_3sigma_events_21d_bins_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nbin_ct = ev.rolling(21, min_periods=7).sum()\nm = bin_ct.rolling(252, min_periods=84).mean()\nv = bin_ct.rolling(252, min_periods=84).var()\nout = _safe_div(v, m)\n")

# 460 ratio of clustered events (within 5d of another) to isolated events
add(460, "clustered_vs_isolated_3sigma_ratio_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nclustered = ev * (ev.shift(1).rolling(5, min_periods=1).max() + ev.shift(-5).rolling(5, min_periods=1).max() > 0).astype(float)\nisolated = ev - clustered\nout = clustered.rolling(252, min_periods=84).sum() / isolated.rolling(252, min_periods=84).sum().replace(0, np.nan)\n")

# 461 Hawkes self-excitation rate (count-of-events-in-prior-21d at each event time, averaged)
add(461, "hawkes_self_excite_rate_prior_21d_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nrate = ev.shift(1).rolling(21, min_periods=7).sum()\n# average rate AT event bars\nrate_at_ev = rate.where(ev > 0.5, np.nan)\nout = rate_at_ev.rolling(252, min_periods=84).mean()\n")

# 462 5d-pos to 5d-neg event ratio (directional Hawkes asymmetry)
add(462, "pos_to_neg_3sigma_event_ratio_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\npos_ev = (r > 3.0 * sd).astype(float).rolling(252, min_periods=84).sum()\nneg_ev = (r < -3.0 * sd).astype(float).rolling(252, min_periods=84).sum()\nout = _safe_div(pos_ev, neg_ev)\n")

# 463 acceleration: 21d-event-count minus 63d-event-rate (event regime change)
add(463, "event_3sigma_21d_count_minus_63d_rate", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nout = ev.rolling(21, min_periods=7).sum() - ev.rolling(63, min_periods=21).sum() * 21.0 / 63.0\n")

# 464 max 5d count of 3sigma events in 252d (event-burst extreme)
add(464, "max_3sigma_5d_count_in_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nrolling5 = ev.rolling(5, min_periods=1).sum()\nout = rolling5.rolling(252, min_periods=84).max()\n")

# 465 Poisson-deviance: chi-squared deviation of event count from Poisson expectation
add(465, "poisson_deviance_3sigma_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 3.0 * sd).astype(float)\nbin_ct = ev.rolling(21, min_periods=7).sum()\nm = bin_ct.rolling(252, min_periods=84).mean()\nv = bin_ct.rolling(252, min_periods=84).var()\nout = (v - m).abs() / m.replace(0, np.nan)\n")


# ==================================================================
# Group B (466-480) — Survival hazard & first-passage time
# ==================================================================

# 466 hazard rate of -5% drawdown from rolling-21d peak
add(466, "hazard_5pct_dd_from_21d_peak_63d", "close",
    "lc = _safe_log(close)\npeak21 = lc.rolling(21, min_periods=7).max()\ndd = peak21 - lc\nev = (dd > 0.05).astype(float)\nout = ev.rolling(63, min_periods=21).mean()\n")

# 467 hazard rate of -10% from 21d peak
add(467, "hazard_10pct_dd_from_21d_peak_63d", "close",
    "lc = _safe_log(close)\npeak21 = lc.rolling(21, min_periods=7).max()\ndd = peak21 - lc\nev = (dd > 0.10).astype(float)\nout = ev.rolling(63, min_periods=21).mean()\n")

# 468 hazard rate of -20% from 63d peak
add(468, "hazard_20pct_dd_from_63d_peak_252d", "close",
    "lc = _safe_log(close)\npeak = lc.rolling(63, min_periods=21).max()\ndd = peak - lc\nev = (dd > 0.20).astype(float)\nout = ev.rolling(252, min_periods=84).mean()\n")

# 469 first-passage time below -5% from 21d peak (bars-since-first-touch)
add(469, "fpt_5pct_below_21d_peak_252d", "close",
    "lc = _safe_log(close)\npeak21 = lc.rolling(21, min_periods=7).max()\ndd = peak21 - lc\nev = (dd > 0.05)\nout = _bars_since_true(ev)\n")

# 470 first-passage time below -10% from 63d peak
add(470, "fpt_10pct_below_63d_peak_252d", "close",
    "lc = _safe_log(close)\npeak = lc.rolling(63, min_periods=21).max()\ndd = peak - lc\nev = (dd > 0.10)\nout = _bars_since_true(ev)\n")

# 471 hazard of new low (vs 21d rolling) given prior 5d up-trend
add(471, "cond_hazard_new_21d_low_given_5d_up_252d", "close",
    "lc = _safe_log(close)\nmin21 = lc.rolling(21, min_periods=7).min()\nnew_low = (lc <= min21).astype(float)\nup_prior = (lc.shift(1) - lc.shift(6) > 0).astype(float)\nev = new_low * up_prior\nout = ev.rolling(252, min_periods=84).mean()\n")

# 472 expected time-to-stuck proxy: bars-since-21d-peak vs 252d avg
add(472, "bars_since_21d_peak_vs_252d_avg", "close",
    "def _f_idx(w):\n    if w.size == 0 or np.isnan(w).all():\n        return np.nan\n    return float(w.size - 1 - int(np.nanargmax(w)))\nbars_since = close.rolling(21, min_periods=7).apply(_f_idx, raw=True)\nout = bars_since - bars_since.rolling(252, min_periods=84).mean()\n")

# 473 longest-time-above-peak-90pct streak (resistance dwell)
add(473, "current_streak_above_252d_peak_90pct", "close",
    "rmax = close.rolling(252, min_periods=84).max()\nabove = (close >= 0.9 * rmax).astype(int).where(rmax.notna(), 0)\nblock = (above != above.shift(1)).fillna(False).cumsum()\nst = above.groupby(block).cumcount().astype(float)\nout = (st * (above > 0)).where(rmax.notna(), np.nan)\n")

# 474 hazard rate of -3sigma-then-continuation-down (capitulation-but-not-bounce)
add(474, "hazard_3sigma_down_no_bounce_5d_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r < -3.0 * sd).astype(float)\nno_bounce = (r.shift(-5).rolling(5, min_periods=1).max() < sd * 0.5).astype(float)\nout = (ev * no_bounce).rolling(252, min_periods=84).mean()\n")

# 475 expected duration in drawdown (mean time-underwater spell length)
add(475, "mean_underwater_spell_length_252d", "close",
    "lc = _safe_log(close)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    peak = np.maximum.accumulate(v)\n    under = (peak - v) > 0\n    spells = []; cur = 0\n    for u in under:\n        if u: cur += 1\n        else:\n            if cur > 0: spells.append(cur); cur = 0\n    if cur > 0: spells.append(cur)\n    if not spells:\n        return 0.0\n    return float(np.mean(spells))\nout = lc.rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 476 censored quantile-at-risk: max 5d cumulative loss capped at 21d window
add(476, "max_5d_cum_loss_capped_21d_252d", "close",
    "r = _safe_log(close).diff()\ncum5 = r.rolling(5, min_periods=2).sum()\nout = (-cum5.rolling(21, min_periods=7).min()).rolling(252, min_periods=84).mean()\n")

# 477 first-passage above peak after drawdown (recovery speed)
add(477, "bars_to_recover_from_5pct_dd_252d", "close",
    "lc = _safe_log(close)\nrmax = lc.expanding(min_periods=21).max()\ndd_5pct = (rmax - lc > 0.05)\n# bars-since-last-time-NOT-in-dd5pct\nout = _bars_since_true(~dd_5pct)\n")

# 478 hazard of consecutive negative-5d-blocks
add(478, "consec_5d_negative_blocks_streak", "close",
    "r5 = _safe_log(close).diff(5)\nneg = (r5 < 0).astype(int).where(r5.notna(), 0)\nblock = (neg != neg.shift(1)).fillna(False).cumsum()\nst = neg.groupby(block).cumcount().astype(float)\nout = (st * (neg > 0)).where(r5.notna(), np.nan)\n")

# 479 hazard of breaking 63d-low conditional on 21d-high present 30 bars ago
add(479, "cond_hazard_break_63d_low_given_21d_high_30d_prior", "close",
    "rmin63 = close.rolling(63, min_periods=21).min()\nrmax21_30 = close.shift(30).rolling(21, min_periods=7).max()\nev = ((close <= rmin63) & (close.shift(30) >= 0.95 * rmax21_30)).astype(float)\nout = ev.rolling(252, min_periods=84).mean()\n")

# 480 hazard of new 252d-low (long-cycle break)
add(480, "hazard_new_252d_low_indicator_504d", "close",
    "rmin252 = close.rolling(252, min_periods=84).min()\nev = (close <= rmin252).astype(float).where(rmin252.notna(), np.nan)\nout = ev.rolling(504, min_periods=168).mean()\n")


# ==================================================================
# Group C (481-495) — Reaction-rally failure quantification
# ==================================================================

# 481 5d-rally-magnitude / prior-5d-decline (bounce-strength)
add(481, "bounce_strength_5d_after_5d_decline", "close",
    "r5 = _safe_log(close).diff(5)\nprior_decline = -r5.shift(5).where(r5.shift(5) < 0, np.nan)\nrally = r5.where(r5.shift(5) < 0, np.nan)\nout = _safe_div(rally, prior_decline)\n")

# 482 5d-rally magnitude after 10%+ decline (failed-rally fraction)
add(482, "rally_after_10pct_decline_pct_recovered_252d", "close",
    "r5 = _safe_log(close).diff(5)\n# 5d-rally only counted after 10pct prior 21d decline\nprior21 = _safe_log(close).diff(21).shift(5)\ncond_rally = r5.where(prior21 < -0.10, np.nan)\nout = cond_rally.rolling(252, min_periods=84).mean()\n")

# 483 failed-rally count (bounces that didn't reach 50% retrace within 21d)
add(483, "failed_50pct_retrace_count_252d", "close",
    "lc = _safe_log(close)\nrmin = lc.rolling(63, min_periods=21).min()\nrmax = lc.rolling(63, min_periods=21).max()\nrange_5pct = (rmax - rmin) * 0.5\n# Bars where 21d-bounce didn't exceed 50% retrace from local min\nbounce21 = lc - rmin\nfailed = ((lc.shift(-21).rolling(21, min_periods=7).max() - rmin) < range_5pct).astype(float).where(range_5pct.notna(), np.nan)\nout = failed.rolling(252, min_periods=84).sum()\n")

# 484 lower-high-after-21d-low rate (sequence breakdown)
add(484, "lower_high_after_21d_low_rate_252d", "close",
    "lc = _safe_log(close)\nat_low = (lc <= lc.rolling(21, min_periods=7).min()).astype(float)\nposthigh = lc.shift(-21).rolling(21, min_periods=7).max()\npriorhigh = lc.shift(21).rolling(21, min_periods=7).max()\nlow_then_lower = at_low * (posthigh < priorhigh).astype(float)\nout = low_then_lower.rolling(252, min_periods=84).mean()\n")

# 485 cumulative bounce-magnitude decay slope (rally-amplitude over time)
add(485, "rally_amplitude_decay_slope_252d", "close",
    "r5 = _safe_log(close).diff(5)\npos = r5.clip(lower=0).rolling(21, min_periods=7).max()\nout = pos.diff(63)\n")

# 486 reaction-rally volume / decline-volume (conviction)
add(486, "rally_vol_to_decline_vol_ratio_63d", "close,volume",
    "r = _safe_log(close).diff()\nrally_vol = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()\ndecline_vol = volume.where(r < 0, 0.0).rolling(63, min_periods=21).sum()\nout = _safe_div(rally_vol, decline_vol)\n")

# 487 mean-reversion-strength: actual-bounce / expected-bounce (252d)
add(487, "mean_reversion_strength_actual_vs_expected_252d", "close",
    "r = _safe_log(close).diff()\nprior_neg = r.shift(1).clip(upper=0)\nexpected = -prior_neg * 0.3  # ~30% mean revert assumption\nactual = r.where(prior_neg < 0, np.nan)\nout = _safe_div(actual.rolling(252, min_periods=84).mean(), expected.rolling(252, min_periods=84).mean())\n")

# 488 longest no-rally streak (bars where 5d-return <= 0)
add(488, "consec_no_rally_5d_streak", "close",
    "r5 = _safe_log(close).diff(5)\nno_rally = (r5 <= 0).astype(int).where(r5.notna(), 0)\nblock = (no_rally != no_rally.shift(1)).fillna(False).cumsum()\nst = no_rally.groupby(block).cumcount().astype(float)\nout = (st * (no_rally > 0)).where(r5.notna(), np.nan)\n")

# 489 bounce-velocity 5d after 3sigma-down (terminal-bounce check)
add(489, "bounce_5d_after_3sigma_down_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nbig_down = (r.shift(5) < -3.0 * sd.shift(5))\nbounce5 = _safe_log(close).diff(5).where(big_down, np.nan)\nout = bounce5.rolling(252, min_periods=84).mean()\n")

# 490 sustained-decline indicator (close < 5d-prior on 4-of-5 days)
add(490, "sustained_decline_4_of_5_indicator_21d_density", "close",
    "r = _safe_log(close).diff()\ndown = (r < 0).astype(float)\nout = (down.rolling(5, min_periods=3).sum() >= 4).astype(float).where(r.notna(), np.nan).rolling(21, min_periods=7).mean()\n")

# 491 rally-vol-decline-vol asymmetry zscore 63d
add(491, "rally_vol_zscore_minus_decline_vol_zscore_63d", "close,volume",
    "r = _safe_log(close).diff()\nrv_up = volume.where(r > 0, np.nan).rolling(63, min_periods=21).mean()\nrv_dn = volume.where(r < 0, np.nan).rolling(63, min_periods=21).mean()\nzu = _rolling_zscore(rv_up, 252, min_periods=84)\nzd = _rolling_zscore(rv_dn, 252, min_periods=84)\nout = zu - zd\n")

# 492 close-to-21d-high distance after recent low (recovery extent)
add(492, "close_to_21d_high_after_recent_low_252d", "close",
    "lc = _safe_log(close)\nmax21 = lc.rolling(21, min_periods=7).max()\nat_low = (lc.shift(10) <= lc.shift(10).rolling(21, min_periods=7).min()).astype(float)\nrecover = (max21 - lc) * at_low\nout = recover.rolling(252, min_periods=84).mean()\n")

# 493 21d-mean-return on bounce-attempts (post-down-day average)
add(493, "mean_5d_return_after_neg_day_252d", "close",
    "r = _safe_log(close).diff()\nr5_after = _safe_log(close).diff(5).shift(-5)\ncond = r5_after.where(r < 0, np.nan)\nout = cond.rolling(252, min_periods=84).mean()\n")

# 494 5d-rally count after capitulation (3-sigma) — failed-recovery indicator
add(494, "rally_count_after_3sigma_down_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\ncapit = (r.shift(5) < -3.0 * sd.shift(5)).astype(float)\nrally5 = (_safe_log(close).diff(5) > 0.05).astype(float)\nout = (capit * rally5).rolling(252, min_periods=84).sum()\n")

# 495 reaction-rally magnitude pct-rank in 252d (relative strength of bounces)
add(495, "rally_5d_magnitude_pct_rank_252d", "close",
    "r5 = _safe_log(close).diff(5).clip(lower=0)\nout = _rolling_pct_rank(r5, 252, min_periods=84)\n")


# ==================================================================
# Group D (496-510) — Volume-return lead/lag asymmetry (toxic-flow)
# ==================================================================

# 496 volume-leads-return: corr(volume[t-1], return[t]) 63d (toxic flow proxy)
add(496, "vol_t_minus_1_to_ret_t_corr_63d", "close,volume",
    "r = _safe_log(close).diff()\nout = volume.shift(1).rolling(63, min_periods=21).corr(r)\n")

# 497 return-leads-volume: corr(return[t-1], volume[t]) 63d
add(497, "ret_t_minus_1_to_vol_t_corr_63d", "close,volume",
    "r = _safe_log(close).diff()\nout = r.shift(1).rolling(63, min_periods=21).corr(volume)\n")

# 498 lead-lag asymmetry: |corr(v,r+1)| - |corr(r,v+1)|
add(498, "vol_ret_lead_lag_asym_63d", "close,volume",
    "r = _safe_log(close).diff()\nc1 = volume.rolling(63, min_periods=21).corr(r.shift(-1)).abs()\nc2 = r.rolling(63, min_periods=21).corr(volume.shift(-1)).abs()\nout = c1 - c2\n")

# 499 signed-volume leads negative return (toxicity in decline)
add(499, "signed_vol_to_neg_ret_lag1_corr_63d", "close,volume",
    "r = _safe_log(close).diff()\nsgn = np.sign(r)\nsv = sgn * volume\nout = sv.shift(1).rolling(63, min_periods=21).corr(r.where(r < 0, 0.0))\n")

# 500 absolute-return-leads-volume (informed-trading detection)
add(500, "abs_ret_leads_vol_lag1_corr_63d", "close,volume",
    "r = _safe_log(close).diff().abs()\nout = r.shift(1).rolling(63, min_periods=21).corr(volume)\n")

# 501 cumulative signed-volume divergence from price (60-day signed-flow vs return)
add(501, "signed_vol_60d_minus_price_60d_zscore", "close,volume",
    "r = _safe_log(close).diff()\nsgn = np.sign(r)\nsv60 = (sgn * volume).rolling(60, min_periods=21).sum()\nret60 = r.rolling(60, min_periods=21).sum()\nsv_z = _rolling_zscore(sv60, 252, min_periods=84)\nret_z = _rolling_zscore(ret60, 252, min_periods=84)\nout = sv_z - ret_z\n")

# 502 effective-information-content: correlation of |return| with volume 21d
add(502, "abs_ret_volume_info_corr_21d", "close,volume",
    "out = _safe_log(close).diff().abs().rolling(21, min_periods=7).corr(_safe_log(volume.replace(0, np.nan)))\n")

# 503 informed-trading proxy: deviation between signed-volume-imbalance and price-change direction
add(503, "signed_imbalance_vs_price_sign_mismatch_63d", "close,volume",
    "r = _safe_log(close).diff()\nsgn_p = np.sign(r)\nsgn_v = np.sign(r) * volume\nimb = sgn_v.rolling(5, min_periods=2).sum()\nmismatch = (np.sign(imb) != sgn_p).astype(float).where(sgn_p.notna() & imb.notna(), np.nan)\nout = mismatch.rolling(63, min_periods=21).mean()\n")

# 504 volume-leads-vol (vol-of-vol) — informed-trading on volatility regime
add(504, "vol_lag1_to_realized_vol_corr_63d", "close,volume",
    "rv = _safe_log(close).diff().rolling(21, min_periods=7).std()\nout = volume.shift(1).rolling(63, min_periods=21).corr(rv)\n")

# 505 volume-spike then-decline asymmetry (vol > 2σ at peak then sustained 5d decline)
add(505, "vol_spike_then_5d_decline_rate_63d", "close,volume",
    "vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)\nspike = (vz > 2.0).astype(float)\ndecline5 = (_safe_log(close).diff(5).shift(-5) < -0.05).astype(float)\nout = (spike * decline5).rolling(63, min_periods=21).mean()\n")

# 506 lag-2 return-volume cross-correlation (delayed information)
add(506, "ret_lag2_to_vol_corr_63d", "close,volume",
    "r = _safe_log(close).diff()\nout = r.shift(2).rolling(63, min_periods=21).corr(volume)\n")

# 507 information ratio between cumulative signed-vol and cumulative price-change 63d
add(507, "cum_signed_vol_to_cum_ret_ratio_63d", "close,volume",
    "r = _safe_log(close).diff()\nsv = np.sign(r) * volume\ncum_sv = sv.rolling(63, min_periods=21).sum()\ncum_r = r.rolling(63, min_periods=21).sum()\nout = _safe_div(cum_sv, cum_r * volume.rolling(63, min_periods=21).mean())\n")

# 508 negative-day signed-volume sum (cumulative selling pressure)
add(508, "cum_negative_day_signed_vol_63d", "close,volume",
    "r = _safe_log(close).diff()\nout = (volume.where(r < 0, 0.0) * np.sign(r)).rolling(63, min_periods=21).sum()\n")

# 509 positive-day signed-volume sum
add(509, "cum_positive_day_signed_vol_63d", "close,volume",
    "r = _safe_log(close).diff()\nout = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()\n")

# 510 selling-pressure dominance: (neg-day-vol - pos-day-vol) / total-vol 63d
add(510, "selling_pressure_dominance_63d", "close,volume",
    "r = _safe_log(close).diff()\nneg_v = volume.where(r < 0, 0.0).rolling(63, min_periods=21).sum()\npos_v = volume.where(r > 0, 0.0).rolling(63, min_periods=21).sum()\nout = _safe_div(neg_v - pos_v, neg_v + pos_v)\n")


# ==================================================================
# Group E (511-525) — Microstructure / cross-bar coherence / squeeze decay
# ==================================================================

# 511 round-number rejection rate at peak (close near round $ then fail)
add(511, "round_number_rejection_rate_252d", "close",
    "cents = (close * 100.0).round().astype(float)\nat_round = ((cents % 100) == 0).astype(float)\nbear_next = (close.shift(-1) < close).astype(float)\nrej = at_round * bear_next\nout = rej.rolling(252, min_periods=84).mean()\n")

# 512 round-number attraction (close gravitates to round $ within 1%)
add(512, "round_number_attraction_within_1pct_252d", "close",
    "cents = (close * 100.0).round().astype(float)\nnearest_round = (cents / 100).round() * 100\nattract = ((cents - nearest_round).abs() < cents * 0.01).astype(float)\nout = attract.rolling(252, min_periods=84).mean()\n")

# 513 HL vs OC fragmentation (intra-bar coherence)
add(513, "hl_minus_oc_fragmentation_index_63d", "open,high,low,close",
    "hl = high - low\noc = (open - close).abs()\nfrag = _safe_div(hl - oc, hl)\nout = frag.rolling(63, min_periods=21).mean()\n")

# 514 closing-auction proxy: last-bar move > mean (proxy by close-vs-open ratio extreme)
add(514, "closing_auction_extreme_close_change_63d", "open,close",
    "intra = (close - open).abs() / open\nout = _rolling_pct_rank(intra, 63, min_periods=21)\n")

# 515 squeeze-decay half-life: bars from volume-peak to median-volume
add(515, "squeeze_volume_half_life_post_max_63d", "volume",
    "def _hl(w):\n    if w.size < 30 or np.isnan(w).all():\n        return np.nan\n    pk = int(np.nanargmax(w))\n    if pk >= w.size - 1:\n        return np.nan\n    peak_v = w[pk]\n    if not np.isfinite(peak_v):\n        return np.nan\n    for j in range(pk + 1, w.size):\n        if not np.isnan(w[j]) and w[j] <= 0.5 * peak_v:\n            return float(j - pk)\n    return float(w.size - pk)\nout = volume.rolling(63, min_periods=21).apply(_hl, raw=True)\n")

# 516 squeeze-decay magnitude: vol(peak)/vol(peak+21d)
add(516, "squeeze_vol_ratio_peak_to_post21_63d", "volume",
    "def _f(w):\n    if w.size < 30 or np.isnan(w).all():\n        return np.nan\n    pk = int(np.nanargmax(w))\n    if pk > w.size - 22:\n        return np.nan\n    peak_v = w[pk]\n    post = w[pk + 1:pk + 22]\n    if peak_v <= 0 or np.isnan(post).all():\n        return np.nan\n    return float(peak_v / np.nanmean(post))\nout = volume.rolling(63, min_periods=21).apply(_f, raw=True)\n")

# 517 close-vs-bar-midpoint asymmetry (bar-shape index)
add(517, "close_vs_bar_midpoint_norm_63d", "high,low,close",
    "mid = (high + low) / 2.0\ndev = _safe_div(close - mid, high - low)\nout = dev.rolling(63, min_periods=21).mean()\n")

# 518 close-near-low frequency (clearly bearish bar share)
add(518, "close_in_bottom_10pct_range_freq_63d", "high,low,close",
    "pos = _safe_div(close - low, high - low)\nbot = (pos < 0.10).astype(float).where(pos.notna(), np.nan)\nout = bot.rolling(63, min_periods=21).mean()\n")

# 519 close-near-high frequency
add(519, "close_in_top_10pct_range_freq_63d", "high,low,close",
    "pos = _safe_div(close - low, high - low)\ntop = (pos > 0.90).astype(float).where(pos.notna(), np.nan)\nout = top.rolling(63, min_periods=21).mean()\n")

# 520 close-near-low minus close-near-high asymmetry
add(520, "close_low_minus_high_freq_diff_63d", "high,low,close",
    "pos = _safe_div(close - low, high - low)\nbot = (pos < 0.10).astype(float).where(pos.notna(), np.nan).rolling(63, min_periods=21).mean()\ntop = (pos > 0.90).astype(float).where(pos.notna(), np.nan).rolling(63, min_periods=21).mean()\nout = bot - top\n")

# 521 squeeze-shock decay: ATR(21) ratio at peak vs 21d-post-peak
add(521, "atr_ratio_peak_to_post21_63d", "high,low,close",
    "atr = _atr(high, low, close, n=21)\ndef _f(w):\n    if w.size < 30 or np.isnan(w).all():\n        return np.nan\n    pk = int(np.nanargmax(w))\n    if pk > w.size - 22:\n        return np.nan\n    peak = w[pk]; post = np.nanmean(w[pk + 1:pk + 22])\n    if peak <= 0 or not np.isfinite(post):\n        return np.nan\n    return float(peak / post)\nout = atr.rolling(63, min_periods=21).apply(_f, raw=True)\n")

# 522 bar-internal-momentum: |close - open| / (high - low) trend over 21d
add(522, "bar_internal_momentum_slope_21d", "open,high,low,close",
    "body_frac = _safe_div((close - open).abs(), high - low)\nout = body_frac.rolling(21, min_periods=7).mean() - body_frac.rolling(21, min_periods=7).mean().shift(21)\n")

# 523 trade-direction-consistency: same-sign-close-to-close-runs density
add(523, "same_sign_close_run_density_63d", "close",
    "r = _safe_log(close).diff()\nsame = (np.sign(r) == np.sign(r.shift(1))).astype(float).where(r.notna() & r.shift(1).notna(), np.nan)\nout = same.rolling(63, min_periods=21).mean()\n")

# 524 cross-bar-coherence: range vs body proportion 252d (large-range with small-body = indecision)
add(524, "large_range_small_body_freq_252d", "open,high,low,close",
    "rng = high - low\nbody = (close - open).abs()\nlarge_rng = (rng > rng.rolling(63, min_periods=21).mean() * 1.5).astype(float)\nsmall_body = (body < rng * 0.3).astype(float)\nout = (large_rng * small_body).rolling(252, min_periods=84).mean()\n")

# 525 cross-bar consistency: 5d high-low overlap density (consolidation regime)
add(525, "consec_5d_overlap_density_252d", "high,low",
    "ov_h = pd.concat([high, high.shift(1)], axis=1).min(axis=1)\nov_l = pd.concat([low, low.shift(1)], axis=1).max(axis=1)\nov = (ov_h - ov_l).clip(lower=0)\nov_pct = _safe_div(ov, high - low)\nout = ov_pct.rolling(252, min_periods=84).mean()\n")


# ==================================================================
# Writer
# ==================================================================

def _build_function_source(idx, suffix, inputs_csv, body, order):
    fname_base = f"f48_ssat_{idx:03d}_{suffix}"
    fname = fname_base if order == "base" else f"{fname_base}_{order}"
    in_names = [i.strip() for i in inputs_csv.split(",")]
    arg_sig = ", ".join([f"{n}: pd.Series" for n in in_names])
    if order == "base":
        ret_chain = "out"
    elif order == "d1":
        ret_chain = "out.diff()"
    elif order == "d2":
        ret_chain = "out.diff().diff()"
    elif order == "d3":
        ret_chain = "out.diff().diff().diff()"
    else:
        raise ValueError(order)
    return f"def {fname}({arg_sig}) -> pd.Series:\n{body}\n    return {ret_chain}\n"


def _write_file(order, lo, hi):
    src = HEADER_FMT.format(order=order, lo=lo, hi=hi) + "\n"
    in_range = [f for f in FEATS if lo <= f[0] <= hi]
    in_range.sort(key=lambda x: x[0])
    for idx, suffix, inputs_csv, body in in_range:
        src += "\n" + _build_function_source(idx, suffix, inputs_csv, body, order) + "\n"
    reg_name = f"SHORT_SQUEEZE_AFTERMATH_TECHNICAL_{order.upper()}_REGISTRY_{lo:03d}_{hi:03d}"
    src += f"\n# ============================================================\n#                         REGISTRY {lo:03d}_{hi:03d} ({order})\n# ============================================================\n\n{reg_name} = {{\n"
    for idx, suffix, inputs_csv, _ in in_range:
        fname_base = f"f48_ssat_{idx:03d}_{suffix}"
        fname = fname_base if order == "base" else f"{fname_base}_{order}"
        in_list = [i.strip() for i in inputs_csv.split(",")]
        in_repr = "[" + ", ".join([f'"{x}"' for x in in_list]) + "]"
        src += f'    "{fname}": {{"inputs": {in_repr}, "func": {fname}}},\n'
    src += "}\n"
    out_path = os.path.join(ROOT, f"48_short_squeeze_aftermath_technical__{order}__{lo:03d}_{hi:03d}.py")
    os.makedirs(ROOT, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return out_path


def main():
    seen = set()
    for f in FEATS:
        if f[0] in seen:
            raise SystemExit(f"DUPLICATE index {f[0]}")
        seen.add(f[0])
    missing = [i for i in range(451, 526) if i not in seen]
    if missing:
        raise SystemExit(f"MISSING indices: {missing}")
    print(f"OK: {len(FEATS)} features, indices 451-525 all present.")
    for order in ("base", "d1", "d2", "d3"):
        p = _write_file(order, 451, 525)
        print(f"wrote {p} ({os.path.getsize(p)} bytes)")
    print("DONE")


if __name__ == "__main__":
    main()
