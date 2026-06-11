"""Generator EXTENSION for 50_terminal_distribution_composite (601-675).

Produces 4 new files: base/d1/d2/d3 x (601-675). 75 distinct INDIVIDUAL signals.

The existing 600 features are heavily composite-based ('master v4 scores').
This extension prioritizes ORTHOGONAL INDIVIDUAL signals — each is a single
clean calculation that targets one concept.

Themes:
- Survival hazard for 'stuck' specific patterns
- Post-peak distribution: bounce magnitude / volume conviction
- Behavioral anchoring: round-number, 52w-low magnetism
- Quantile-regression-style return-vs-lag indicators
- Long-horizon memory: 504d/1260d structural breaks
- Asymmetric mean-reversion (failure modes)
- Conditional moment-shifts at the snap-vicinity
- Information-asymmetry signals (volume leads vs follows)
"""
import os

ROOT = r"C:\Users\jyama\Desktop\short_technical_features_1b\50_terminal_distribution_composite"

HEADER_FMT = '''"""terminal_distribution_composite {order} features {lo:03d}-{hi:03d} — Pipeline 1b-technical.

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
# Group A (601-615) — Stuck-specific survival hazards
# ==================================================================

# 601 cumulative-time-stuck-near-52w-low (close within 5% of rolling 252d-low)
add(601, "frac_time_near_252d_low_5pct_252d", "low,close",
    "rmin = low.rolling(252, min_periods=84).min()\nnear = (close <= rmin * 1.05).astype(float).where(rmin.notna(), np.nan)\nout = near.rolling(252, min_periods=84).mean()\n")

# 602 distance-from-peak velocity: rate at which close moves away from rolling-252d-high
add(602, "rate_distance_from_252d_high_63d", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\ndist = _safe_log(rmax) - _safe_log(close)\nout = dist - dist.shift(63)\n")

# 603 stuck-regime indicator: max-DD-from-rolling-peak > 50% AND no recovery (≤ -50% over 252d)
add(603, "stuck_dd50_no_recover_indicator_252d", "high,close",
    "rmax_all = high.expanding(min_periods=63).max()\ndd = _safe_log(rmax_all) - _safe_log(close)\nbig_dd = (dd > 0.69).astype(float)  # log(2) ~= 0.693, i.e. -50% in linear\nout = big_dd.rolling(252, min_periods=84).min()\n")

# 604 days-since-last-peak (rolling 252d-high)
add(604, "bars_since_last_252d_high", "high",
    "rmax = high.rolling(252, min_periods=84).max()\nev = (high >= rmax)\nout = _bars_since_true(ev)\n")

# 605 expected time-to-next-peak: inverse of new-252d-high frequency
add(605, "expected_time_to_next_peak_252d", "high",
    "rmax = high.rolling(252, min_periods=84).max()\nev = (high >= rmax).astype(float).where(rmax.notna(), np.nan)\ncnt = ev.rolling(252, min_periods=84).sum()\nout = 252.0 / cnt.replace(0, np.nan)\n")

# 606 hazard of new-1260d-low in 252d (long-horizon structural break)
add(606, "hazard_new_1260d_low_252d", "low",
    "rmin = low.rolling(1260, min_periods=252).min()\nev = (low <= rmin).astype(float).where(rmin.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).mean()\n")

# 607 stuck-momentum: 252d-return < -50% AND no positive 63d-return in past 252d
add(607, "stuck_momentum_no_pos_63d_in_252d", "close",
    "r252 = _safe_log(close).diff(252)\nr63 = _safe_log(close).diff(63)\nno_pos = (r63.rolling(252, min_periods=84).max() < 0).astype(float)\nbig_decl = (r252 < -0.5).astype(float)\nout = (no_pos * big_decl).where(r252.notna(), np.nan)\n")

# 608 multi-year decline persistence: 504d cum-return < -50% indicator
add(608, "indicator_504d_cum_decline_50pct", "close",
    "r504 = _safe_log(close).diff(504)\nout = (r504 < -0.69).astype(float).where(r504.notna(), np.nan)\n")

# 609 longest-time-without-new-21d-high (resistance dwell)
add(609, "longest_gap_no_new_21d_high_252d", "high",
    "rmax21 = high.rolling(21, min_periods=7).max()\nev = (high >= rmax21).astype(float).where(rmax21.notna(), np.nan)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    best = 0; cur = 0\n    for x in v:\n        if x < 0.5:\n            cur += 1\n            if cur > best:\n                best = cur\n        else:\n            cur = 0\n    return float(best)\nout = ev.rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 610 stuck-trajectory-conditional: average return in next 21d given DD > 30% from 252d high
add(610, "cond_5d_ret_given_dd30_from_252d_high_252d", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\ndd = _safe_log(rmax) - _safe_log(close)\ncond_dd30 = (dd > 0.35).astype(bool)\nret5 = _safe_log(close).diff(5)\nout = ret5.where(cond_dd30, np.nan).rolling(252, min_periods=84).mean()\n")

# 611 hazard rate of >5% gap-down event (sudden decline)
add(611, "hazard_5pct_gap_down_event_252d", "open,close",
    "g = _safe_log(open) - _safe_log(close.shift(1))\nev = (g < -0.05).astype(float).where(g.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).mean()\n")

# 612 conditional max-DD in 21d given currently at 252d-high
add(612, "cond_max_dd_21d_given_at_252d_high_252d", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\nat_high = (high >= 0.95 * rmax).astype(bool)\nfut_min = _safe_log(close.shift(-21)).rolling(21, min_periods=7).min()\ndd_fwd = _safe_log(close) - fut_min\nout = dd_fwd.where(at_high, np.nan).rolling(252, min_periods=84).mean()\n")

# 613 sequential-lower-low count (lower-low after lower-low) in 252d
add(613, "sequential_lower_low_count_252d", "low",
    "ll = (low < low.shift(21)).astype(int).where(low.notna() & low.shift(21).notna(), 0)\nseq = ll * ll.shift(21)\nout = seq.rolling(252, min_periods=84).sum()\n")

# 614 sequential-lower-high count in 252d
add(614, "sequential_lower_high_count_252d", "high",
    "lh = (high < high.shift(21)).astype(int).where(high.notna() & high.shift(21).notna(), 0)\nseq = lh * lh.shift(21)\nout = seq.rolling(252, min_periods=84).sum()\n")

# 615 hazard of breaking new 504d-low (multi-year capitulation)
add(615, "hazard_new_504d_low_252d", "low",
    "rmin = low.rolling(504, min_periods=168).min()\nev = (low <= rmin).astype(float).where(rmin.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).mean()\n")


# ==================================================================
# Group B (616-630) — Post-peak bounce magnitude / conviction
# ==================================================================

# 616 mean 5d-bounce magnitude after 5%-drawdown 252d
add(616, "mean_5d_bounce_after_5pct_dd_252d", "high,close",
    "lc = _safe_log(close); lh = _safe_log(high)\nrmax = lh.rolling(21, min_periods=7).max()\nbig_dd_5d_ago = ((rmax.shift(5) - lc.shift(5)) > 0.05).astype(bool)\nbounce = (lc - lc.shift(5)).where(big_dd_5d_ago, np.nan)\nout = bounce.rolling(252, min_periods=84).mean()\n")

# 617 mean 21d-bounce after 10%-drawdown
add(617, "mean_21d_bounce_after_10pct_dd_252d", "high,close",
    "lc = _safe_log(close); lh = _safe_log(high)\nrmax = lh.rolling(63, min_periods=21).max()\nbig_dd = ((rmax.shift(21) - lc.shift(21)) > 0.10).astype(bool)\nbounce = (lc - lc.shift(21)).where(big_dd, np.nan)\nout = bounce.rolling(252, min_periods=84).mean()\n")

# 618 bounce-volume conviction: avg volume during 5d bounce / avg volume during prior 5d decline
add(618, "bounce_vol_conviction_ratio_252d", "close,volume",
    "r = _safe_log(close).diff()\nup_v = volume.where(r > 0, 0.0).rolling(5, min_periods=2).sum()\ndn_v = volume.where(r < 0, 0.0).shift(5).rolling(5, min_periods=2).sum()\nout = _safe_div(up_v, dn_v).rolling(252, min_periods=84).mean()\n")

# 619 bounce-fizzle indicator: 5d-bounce > 5% AND next-5d-return < 0
add(619, "bounce_fizzle_rate_252d", "close",
    "r5 = _safe_log(close).diff(5)\nfizzle = ((r5 > 0.05).shift(5) & (r5 < 0)).astype(float).where(r5.notna() & r5.shift(5).notna(), np.nan)\nout = fizzle.rolling(252, min_periods=84).mean()\n")

# 620 percentage-of-DD-recovered in next-21d after 10%+ DD
add(620, "pct_dd_recovered_21d_after_dd10_252d", "high,close",
    "lc = _safe_log(close); lh = _safe_log(high)\nrmax = lh.rolling(63, min_periods=21).max()\ndd_21d_ago = (rmax.shift(21) - lc.shift(21)).where(rmax.shift(21).notna(), np.nan)\nrecovery = (lc - lc.shift(21)).where(dd_21d_ago > 0.10, np.nan)\npct_rec = _safe_div(recovery, dd_21d_ago.where(dd_21d_ago > 0.10, np.nan))\nout = pct_rec.rolling(252, min_periods=84).mean()\n")

# 621 mean-DD-magnitude that caused bounce > 0.5*DD (recovery success rate)
add(621, "recovery_success_rate_dd_gt_5pct_252d", "high,close",
    "lc = _safe_log(close); lh = _safe_log(high)\nrmax = lh.rolling(63, min_periods=21).max()\ndd_21d = (rmax.shift(21) - lc.shift(21))\nrecov_21d = (lc - lc.shift(21))\nsuccess = ((dd_21d > 0.05) & (recov_21d > 0.5 * dd_21d)).astype(float).where(dd_21d.notna() & recov_21d.notna(), np.nan)\ntotal_dd = (dd_21d > 0.05).astype(float).where(dd_21d.notna(), np.nan)\nout = _safe_div(success.rolling(252, min_periods=84).sum(), total_dd.rolling(252, min_periods=84).sum())\n")

# 622 mean-volume-during-bounce / 252d-median-volume
add(622, "bounce_vol_vs_252d_median_252d", "close,volume",
    "r = _safe_log(close).diff()\nr5 = _safe_log(close).diff(5)\nin_bounce = (r5 > 0.03).astype(bool)\nbounce_vol = volume.where(in_bounce, np.nan)\nmed_v = volume.rolling(252, min_periods=84).median()\nout = _safe_div(bounce_vol.rolling(252, min_periods=84).mean(), med_v)\n")

# 623 reaction-rally lower-high rate (after 5%+ decline, rally peaks below prior peak)
add(623, "reaction_rally_lower_high_rate_252d", "high,low,close",
    "lh = _safe_log(high); lc = _safe_log(close)\nprior_h = lh.shift(5).rolling(5, min_periods=2).max()\ndecline = (lc - lc.shift(5)) < -0.05\npost_h = lh.rolling(5, min_periods=2).max()\nlower_h = ((post_h < prior_h.shift(-5)) & decline.shift(-5)).astype(float).where(decline.shift(-5).notna(), np.nan)\nout = lower_h.rolling(252, min_periods=84).mean()\n")

# 624 bounce-decay slope: regression slope of 5d-bounce magnitude over 63d window
add(624, "bounce_5d_decay_slope_63d", "close",
    "r5 = _safe_log(close).diff(5)\npos5 = r5.clip(lower=0).rolling(21, min_periods=7).max()\nout = _rolling_slope(pos5, 63, min_periods=21)\n")

# 625 mean-up-day-vol on bounces / mean-down-day-vol on declines (post-bounce conviction)
add(625, "up_day_vol_minus_down_day_vol_pct_rank_252d", "close,volume",
    "r = _safe_log(close).diff()\nup_v = volume.where(r > 0, np.nan).rolling(63, min_periods=21).mean()\ndn_v = volume.where(r < 0, np.nan).rolling(63, min_periods=21).mean()\nratio = _safe_div(up_v, dn_v)\nout = _rolling_pct_rank(ratio, 252, min_periods=84)\n")

# 626 bounce-acceleration: change in bounce-rate over 21d
add(626, "bounce_rate_acceleration_21d_in_252d", "close",
    "r5 = _safe_log(close).diff(5)\nrate = (r5 > 0.05).astype(float).where(r5.notna(), np.nan).rolling(63, min_periods=21).mean()\nout = rate - rate.shift(21)\n")

# 627 close vs 21d-mean post-decline asymmetry
add(627, "close_vs_21d_mean_post_decline_252d", "close",
    "r21 = _safe_log(close).diff(21)\nbig_decl = (r21.shift(1) < -0.1).astype(bool)\nm21 = close.rolling(21, min_periods=7).mean()\ngap = _safe_div(close - m21, m21).where(big_decl, np.nan)\nout = gap.rolling(252, min_periods=84).mean()\n")

# 628 expected vs actual recovery time mismatch (21d/63d bounce vs full DD recovery)
add(628, "actual_vs_expected_recovery_time_ratio_252d", "high,close",
    "lc = _safe_log(close); lh = _safe_log(high)\nrmax21 = lh.rolling(21, min_periods=7).max()\ndd21 = rmax21 - lc\n# actual_recovery_bars: bars-since-last-not-in-dd (proxy for time underwater)\nin_dd = (dd21 > 0.01)\nactual_bars = _bars_since_true(~in_dd)\n# expected ~ 21d on average\nout = _safe_div(actual_bars, 21.0).rolling(252, min_periods=84).mean()\n")

# 629 distribution-of-bounce-magnitudes 75th percentile 252d
add(629, "bounce_75pct_percentile_252d", "close",
    "r5 = _safe_log(close).diff(5).clip(lower=0)\nout = r5.rolling(252, min_periods=84).quantile(0.75)\n")

# 630 bounce-failure index: 1 - frac of bounces that hold (no immediate down day after)
add(630, "bounce_fail_to_hold_rate_63d", "close",
    "r = _safe_log(close).diff()\nbounce = (r > 0.03).astype(bool)\nfollow_dn = (r.shift(-1) < 0).astype(float)\nfail = follow_dn.where(bounce, np.nan)\nout = fail.rolling(63, min_periods=21).mean()\n")


# ==================================================================
# Group C (631-645) — Behavioral anchoring & attention proxies
# ==================================================================

# 631 distance to nearest round-$ multiple
add(631, "nearest_round_dollar_distance_pct", "close",
    "nearest = close.round(0)\nout = (close - nearest).abs() / close\n")

# 632 close-at-round-$ + bear-next-day frequency
add(632, "round_dollar_bear_next_freq_252d", "close",
    "cents = (close * 100.0).round().astype(float)\nat_r = ((cents % 100) == 0).astype(float)\nbear = (close.shift(-1) < close).astype(float)\nout = (at_r * bear).rolling(252, min_periods=84).mean()\n")

# 633 attention-spike: |return| > 3σ AND |volume-z| > 2 — joint signal
add(633, "attention_spike_3sigma_ret_vol2_252d", "close,volume",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nvz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)\nev = ((r.abs() > 3.0 * sd) & (vz > 2.0)).astype(float).where(sd.notna() & vz.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).mean()\n")

# 634 distance-from-IPO-style-anchor (proxy: distance from 2-year-low normalized by 2-year range)
add(634, "ipo_anchor_pct_distance_504d", "high,low,close",
    "rmin = low.rolling(504, min_periods=168).min()\nrmax = high.rolling(504, min_periods=168).max()\nout = _safe_div(close - rmin, rmax - rmin)\n")

# 635 magnetism to 200-day SMA
add(635, "magnetism_to_200d_sma_pct", "close",
    "sma = close.rolling(200, min_periods=84).mean()\nout = _safe_div(close - sma, close)\n")

# 636 number-of-touches at 200-day SMA in 252d
add(636, "touch_count_200d_sma_within_2pct_252d", "close",
    "sma = close.rolling(200, min_periods=84).mean()\ntouch = ((close - sma).abs() < 0.02 * close).astype(float).where(sma.notna(), np.nan)\nout = touch.rolling(252, min_periods=84).sum()\n")

# 637 reluctance-to-cross-200d-sma: bars-since-last-cross of 200d SMA
add(637, "bars_since_last_200d_sma_cross", "close",
    "sma = close.rolling(200, min_periods=84).mean()\nabove = (close > sma).astype(float)\ncross = (above != above.shift(1)).fillna(False) & sma.notna() & sma.shift(1).notna()\nout = _bars_since_true(cross)\n")

# 638 close-magnetism to 50d-SMA pct
add(638, "magnetism_to_50d_sma_pct", "close",
    "sma = close.rolling(50, min_periods=21).mean()\nout = _safe_div(close - sma, close)\n")

# 639 frequency of close within 1% of 21d-mean (anchoring to local mean)
add(639, "anchor_to_21d_mean_within_1pct_freq_252d", "close",
    "sma = close.rolling(21, min_periods=7).mean()\nanc = ((close - sma).abs() < 0.01 * close).astype(float).where(sma.notna(), np.nan)\nout = anc.rolling(252, min_periods=84).mean()\n")

# 640 round-$5-attraction freq (close within 5c of $5 multiple)
add(640, "round_5dollar_within_5c_freq_252d", "close",
    "nearest = (close / 5.0).round() * 5.0\nnear = ((close - nearest).abs() < 0.05).astype(float).where(close.notna(), np.nan)\nout = near.rolling(252, min_periods=84).mean()\n")

# 641 distance from prior-21d-low (loss-aversion anchor)
add(641, "distance_above_21d_low_pct", "low,close",
    "rmin21 = low.rolling(21, min_periods=7).min()\nout = _safe_div(close - rmin21, close)\n")

# 642 attention-decay-rate: change in volume-zscore after attention-spike
add(642, "attention_decay_post_spike_21d_252d", "close,volume",
    "vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), 63, min_periods=21)\nspike = (vz > 2.0).astype(float)\nfut_vz = vz.shift(-21)\ndecay = (vz - fut_vz).where(spike > 0.5, np.nan)\nout = decay.rolling(252, min_periods=84).mean()\n")

# 643 conditional distance-from-52w-high given current vol > median
add(643, "cond_dist_52w_high_given_high_vol_252d", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\ndist = _safe_div(rmax - close, rmax)\nr = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nmed_rv = rv21.rolling(252, min_periods=84).median()\nout = dist.where(rv21 > med_rv, np.nan).rolling(252, min_periods=84).mean()\n")

# 644 magnitude-attention-imbalance: |return| / mean-|return-21d| at attention spikes
add(644, "attention_ret_magnitude_normed_252d", "close",
    "r = _safe_log(close).diff()\nabs_r = r.abs()\nmean_21 = abs_r.rolling(21, min_periods=7).mean()\nout = _safe_div(abs_r, mean_21).rolling(252, min_periods=84).mean()\n")

# 645 anchoring-break event: close < 50d-SMA - 5% (anchor failure)
add(645, "anchor_break_below_50d_sma_5pct_252d", "close",
    "sma = close.rolling(50, min_periods=21).mean()\nev = (close < 0.95 * sma).astype(float).where(sma.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).mean()\n")


# ==================================================================
# Group D (646-660) — Quantile-regression-style return-lag indicators
# ==================================================================

# 646 5% quantile of return given prior-5d-up (asymmetric tail conditional on regime)
add(646, "q05_ret_given_prior_5d_up_252d", "close",
    "r = _safe_log(close).diff()\nr5p = _safe_log(close).diff(5).shift(1)\ncond = r.where(r5p > 0, np.nan)\nout = cond.rolling(252, min_periods=84).quantile(0.05)\n")

# 647 5% quantile of return given prior-5d-down
add(647, "q05_ret_given_prior_5d_down_252d", "close",
    "r = _safe_log(close).diff()\nr5p = _safe_log(close).diff(5).shift(1)\ncond = r.where(r5p < 0, np.nan)\nout = cond.rolling(252, min_periods=84).quantile(0.05)\n")

# 648 1% quantile given high-vol regime
add(648, "q01_ret_given_high_vol_252d", "close",
    "r = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nmed_rv = rv21.rolling(252, min_periods=84).median()\ncond = r.where(rv21 > med_rv, np.nan)\nout = cond.rolling(252, min_periods=84).quantile(0.01)\n")

# 649 95% quantile given low-vol regime (upside tail in calm)
add(649, "q95_ret_given_low_vol_252d", "close",
    "r = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nmed_rv = rv21.rolling(252, min_periods=84).median()\ncond = r.where(rv21 < med_rv, np.nan)\nout = cond.rolling(252, min_periods=84).quantile(0.95)\n")

# 650 1% quantile - 99% quantile spread (tail-asymmetry magnitude)
add(650, "q99_minus_q01_spread_252d", "close",
    "r = _safe_log(close).diff()\nq99 = r.rolling(252, min_periods=84).quantile(0.99)\nq01 = r.rolling(252, min_periods=84).quantile(0.01)\nout = q99 + q01\n")

# 651 lower-tail quantile gap: q1 - q5 (extreme-vs-near-extreme)
add(651, "lower_tail_q1_minus_q5_252d", "close",
    "r = _safe_log(close).diff()\nq1 = r.rolling(252, min_periods=84).quantile(0.01)\nq5 = r.rolling(252, min_periods=84).quantile(0.05)\nout = q1 - q5\n")

# 652 upper-tail quantile gap: q99 - q95
add(652, "upper_tail_q99_minus_q95_252d", "close",
    "r = _safe_log(close).diff()\nq99 = r.rolling(252, min_periods=84).quantile(0.99)\nq95 = r.rolling(252, min_periods=84).quantile(0.95)\nout = q99 - q95\n")

# 653 conditional expectation given exceeding 95% quantile (mean of right tail)
add(653, "cond_mean_above_q95_252d", "close",
    "r = _safe_log(close).diff()\nq95 = r.rolling(252, min_periods=84).quantile(0.95)\ntail = r.where(r >= q95, np.nan)\nout = tail.rolling(252, min_periods=84).mean()\n")

# 654 conditional expectation given below 5% quantile (left tail expected loss)
add(654, "cond_mean_below_q05_252d", "close",
    "r = _safe_log(close).diff()\nq05 = r.rolling(252, min_periods=84).quantile(0.05)\ntail = r.where(r <= q05, np.nan)\nout = tail.rolling(252, min_periods=84).mean()\n")

# 655 median-vs-mean divergence at peak (positive ⇒ left-skewed)
add(655, "mean_minus_median_at_252d_high_252d", "high,close",
    "r = _safe_log(close).diff()\nrmax = high.rolling(252, min_periods=84).max()\nat_high = (high >= 0.95 * rmax)\ncond_r = r.where(at_high, np.nan)\nm = cond_r.rolling(252, min_periods=84).mean()\nmed = cond_r.rolling(252, min_periods=84).median()\nout = m - med\n")

# 656 IQR ratio conditional on past 21d-up trend
add(656, "iqr_cond_on_up_trend_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21).shift(1)\ncond = r.where(ret21 > 0, np.nan)\nq75 = cond.rolling(252, min_periods=84).quantile(0.75)\nq25 = cond.rolling(252, min_periods=84).quantile(0.25)\nout = q75 - q25\n")

# 657 IQR cond on past 21d-down
add(657, "iqr_cond_on_down_trend_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21).shift(1)\ncond = r.where(ret21 < 0, np.nan)\nq75 = cond.rolling(252, min_periods=84).quantile(0.75)\nq25 = cond.rolling(252, min_periods=84).quantile(0.25)\nout = q75 - q25\n")

# 658 IQR-ratio up-vs-down regime (vol-asymmetry via robust scale)
add(658, "iqr_ratio_up_over_down_regime_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21).shift(1)\nup = r.where(ret21 > 0, np.nan)\ndn = r.where(ret21 < 0, np.nan)\niqr_u = up.rolling(252, min_periods=84).quantile(0.75) - up.rolling(252, min_periods=84).quantile(0.25)\niqr_d = dn.rolling(252, min_periods=84).quantile(0.75) - dn.rolling(252, min_periods=84).quantile(0.25)\nout = _safe_div(iqr_u, iqr_d)\n")

# 659 ratio of negative-tail-volume-share (vol on -3σ days / total vol) 252d
add(659, "neg_3sigma_day_vol_share_252d", "close,volume",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r < -3.0 * sd)\nneg_vol = volume.where(ev, 0.0).rolling(252, min_periods=84).sum()\ntot_vol = volume.rolling(252, min_periods=84).sum()\nout = _safe_div(neg_vol, tot_vol)\n")

# 660 ratio of positive-tail-volume-share
add(660, "pos_3sigma_day_vol_share_252d", "close,volume",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r > 3.0 * sd)\npos_vol = volume.where(ev, 0.0).rolling(252, min_periods=84).sum()\ntot_vol = volume.rolling(252, min_periods=84).sum()\nout = _safe_div(pos_vol, tot_vol)\n")


# ==================================================================
# Group E (661-675) — Long-horizon memory & structural breaks
# ==================================================================

# 661 504d return vs 252d return divergence (long vs medium memory)
add(661, "ret_504d_minus_2x_ret_252d", "close",
    "out = _safe_log(close).diff(504) - 2.0 * _safe_log(close).diff(252)\n")

# 662 1260d (5y) cumulative return — long-horizon memory
add(662, "log_ret_1260d", "close",
    "out = _safe_log(close).diff(1260)\n")

# 663 504d slope-of-trend / 252d slope-of-trend (multi-horizon trend dominance)
add(663, "slope_ratio_504d_over_252d", "close",
    "out = _safe_div(_rolling_slope(_safe_log(close), 504, min_periods=168), _rolling_slope(_safe_log(close), 252, min_periods=84))\n")

# 664 1260d-vol vs 252d-vol (long-cycle volatility ratio)
add(664, "rv_1260d_over_252d_ratio", "close",
    "r = _safe_log(close).diff()\nout = _safe_div(r.rolling(1260, min_periods=252).std(), r.rolling(252, min_periods=84).std())\n")

# 665 structural-break-test 504d (mean-1H vs mean-2H proxy)
add(665, "structural_break_mean_test_504d", "close",
    "r = _safe_log(close).diff()\nm1 = r.shift(252).rolling(252, min_periods=84).mean()\nm2 = r.rolling(252, min_periods=84).mean()\nsd = r.rolling(504, min_periods=168).std() / np.sqrt(252.0)\nout = _safe_div((m2 - m1).abs(), sd)\n")

# 666 long-cycle mean-reversion: 1260d-mean - current-close (anchor distance)
add(666, "current_vs_1260d_mean_close_distance_pct", "close",
    "m = close.rolling(1260, min_periods=252).mean()\nout = _safe_div(close - m, m)\n")

# 667 conditional expected return given currently below 200d-SMA (regime-1 mean)
add(667, "cond_5d_ret_given_below_200d_sma_252d", "close",
    "sma200 = close.rolling(200, min_periods=84).mean()\nbelow = (close < sma200).astype(bool)\nret5 = _safe_log(close).diff(5)\nout = ret5.where(below, np.nan).rolling(252, min_periods=84).mean()\n")

# 668 cond expected return given above 200d-SMA
add(668, "cond_5d_ret_given_above_200d_sma_252d", "close",
    "sma200 = close.rolling(200, min_periods=84).mean()\nabove = (close > sma200).astype(bool)\nret5 = _safe_log(close).diff(5)\nout = ret5.where(above, np.nan).rolling(252, min_periods=84).mean()\n")

# 669 long-memory test: |AR(1)| at 504d vs 252d horizon
add(669, "ar1_504d_minus_ar1_252d", "close",
    "r = _safe_log(close).diff()\ndef _ar1(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    m = v.mean(); vc = v - m\n    den = float((vc ** 2).sum())\n    if den == 0:\n        return np.nan\n    return float((vc[1:] * vc[:-1]).sum() / den)\nar504 = r.rolling(504, min_periods=168).apply(_ar1, raw=True)\nar252 = r.rolling(252, min_periods=84).apply(_ar1, raw=True)\nout = ar504.abs() - ar252.abs()\n")

# 670 21d-frequency of new 504d-lows (escalation indicator)
add(670, "new_504d_low_count_in_21d", "low",
    "rmin504 = low.rolling(504, min_periods=168).min()\nev = (low <= rmin504).astype(float).where(rmin504.notna(), np.nan)\nout = ev.rolling(21, min_periods=7).sum()\n")

# 671 21d-frequency of new 1260d-highs (long-cycle blowoff)
add(671, "new_1260d_high_count_in_21d", "high",
    "rmax = high.rolling(1260, min_periods=252).max()\nev = (high >= rmax).astype(float).where(rmax.notna(), np.nan)\nout = ev.rolling(21, min_periods=7).sum()\n")

# 672 conditional kurtosis given currently > 80th percentile in 1260d range
add(672, "cond_kurt_given_top_quintile_1260d_range_252d", "high,low,close",
    "rmin = low.rolling(1260, min_periods=252).min()\nrmax = high.rolling(1260, min_periods=252).max()\npos = _safe_div(close - rmin, rmax - rmin)\ntop = (pos > 0.8).astype(bool)\nr = _safe_log(close).diff().where(top, np.nan)\ndef _kt(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 4) - 3.0)\nout = r.rolling(252, min_periods=84).apply(_kt, raw=True)\n")

# 673 long-horizon-cumulative-return rank in 1260d (extreme winners)
add(673, "ret_252d_pct_rank_in_1260d", "close",
    "r252 = _safe_log(close).diff(252)\nout = _rolling_pct_rank(r252, 1260, min_periods=252)\n")

# 674 long-horizon-cumulative-return rank 504d in 1260d
add(674, "ret_504d_pct_rank_in_1260d", "close",
    "r504 = _safe_log(close).diff(504)\nout = _rolling_pct_rank(r504, 1260, min_periods=252)\n")

# 675 max-drawdown-from-1260d-peak indicator (terminal stuck condition)
add(675, "max_dd_from_1260d_peak_pct", "high,close",
    "rmax = high.rolling(1260, min_periods=252).max()\nout = _safe_div(rmax - close, rmax)\n")


# ==================================================================
# Writer
# ==================================================================

def _build_function_source(idx, suffix, inputs_csv, body, order):
    fname_base = f"f50_tdco_{idx:03d}_{suffix}"
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
    reg_name = f"TERMINAL_DISTRIBUTION_COMPOSITE_{order.upper()}_REGISTRY_{lo:03d}_{hi:03d}"
    src += f"\n# ============================================================\n#                         REGISTRY {lo:03d}_{hi:03d} ({order})\n# ============================================================\n\n{reg_name} = {{\n"
    for idx, suffix, inputs_csv, _ in in_range:
        fname_base = f"f50_tdco_{idx:03d}_{suffix}"
        fname = fname_base if order == "base" else f"{fname_base}_{order}"
        in_list = [i.strip() for i in inputs_csv.split(",")]
        in_repr = "[" + ", ".join([f'"{x}"' for x in in_list]) + "]"
        src += f'    "{fname}": {{"inputs": {in_repr}, "func": {fname}}},\n'
    src += "}\n"
    out_path = os.path.join(ROOT, f"50_terminal_distribution_composite__{order}__{lo:03d}_{hi:03d}.py")
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
    missing = [i for i in range(601, 676) if i not in seen]
    if missing:
        raise SystemExit(f"MISSING indices: {missing}")
    print(f"OK: {len(FEATS)} features, indices 601-675 all present.")
    for order in ("base", "d1", "d2", "d3"):
        p = _write_file(order, 601, 675)
        print(f"wrote {p} ({os.path.getsize(p)} bytes)")
    print("DONE")


if __name__ == "__main__":
    main()
