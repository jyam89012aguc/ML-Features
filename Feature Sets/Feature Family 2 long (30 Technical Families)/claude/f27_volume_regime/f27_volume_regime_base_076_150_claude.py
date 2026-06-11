"""f27_volume_regime base features 076-150.

Domain: VOLUME REGIME CLASSIFICATION & TRANSITIONS (continued).
Companion to base_001_075. NO structural duplicates with that file
(no two features share the same expression up to a window-size change).

This file adds:
- HIGHER-MOMENT regime indicators (skew/kurt of rank distribution)
- DIFFERENT bucket-set classifications (deciles vs sextiles, etc)
- Regime "trigger" indicators based on volume DERIVATIVES
- Volume-vs-OHLC range regime crossings
- Symmetric / asymmetric regime indicators
- More transition / event count features at distinct windows
- Distinct streak / time-in-regime constructions

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _streak(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def _consec_true(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)


def _maxrun(x):
    if not np.all(np.isfinite(x)):
        return np.nan
    best = 0; cur = 0
    for v in x:
        if v > 0.5:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return float(best)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === Sextile / octile regimes (DIFFERENT bucket-set than file 1) ==========


def f27vr_f27_volume_regime_sextile_bucket_84d_base_v076_signal(volume):
    """Volume sextile (1..6) in trailing 84d. Different bucket scheme + window."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    out[m] = np.ceil(r[m].clip(lower=1e-9) * 6.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_octile_change_count_60d_base_v077_signal(volume):
    """Count of octile-label changes (rank bucket 1..8) in trailing 60d.
    Different bucket count + shorter aggregation window than file-1's quartile/decile change counts."""
    r = volume.rolling(168, min_periods=168).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 8.0)
    flip = (bucket != bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Volume distribution moment features (regime classification) =========




def f27vr_f27_volume_regime_v_kurt_252d_base_v079_signal(volume):
    """252d rolling kurtosis of raw volume. Regime tails at long window.
    Distinct from file 1 v052 (log-kurt, 126d)."""
    return volume.rolling(252, min_periods=252).kurt().replace([np.inf, -np.inf], np.nan)


# === Volume rate-of-change regime =========================================


def f27vr_f27_volume_regime_logv_roc_21d_base_v080_signal(volume):
    """log(volume / SMA(volume, 21)). Short volume excitation level (single-bar)."""
    m = volume.rolling(21, min_periods=21).mean()
    return np.log(volume / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sma_v_ratio_10_252_base_v081_signal(volume):
    """log( SMA(volume,10) / SMA(volume,252) ). Very-short-vs-very-long expansion."""
    s10 = volume.rolling(10, min_periods=10).mean()
    s252 = volume.rolling(252, min_periods=252).mean()
    return np.log(s10 / s252.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Bucket TRANSITION matrix-derived features ============================


def f27vr_f27_volume_regime_up_trans_count_q3_120d_base_v082_signal(volume):
    """Count of UPWARD tertile transitions (b > b.shift(1)) in trailing 120d.
    Directional transition counter; tertile bucket from 84d rank."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 3.0)
    up = (bucket > bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return up.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_down_trans_count_q3_120d_base_v083_signal(volume):
    """Count of DOWNWARD tertile transitions in trailing 120d.
    Counterpart to v082."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 3.0)
    dn = (bucket < bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return dn.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Volume vs OHLC range regime ==========================================


def f27vr_f27_volume_regime_v_per_range_pctrank_84d_base_v084_signal(high, low, volume):
    """Pct rank of (volume / (high-low)) in trailing 84d. Volume-per-range regime level.
    Folder-specific because (high-low) is intraday; we classify volume-efficiency regime."""
    rng = (high - low).replace(0.0, np.nan)
    vpr = volume / rng
    return vpr.rolling(84, min_periods=84).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_v_per_range_high_state_120d_base_v085_signal(high, low, volume):
    """Fraction of last 120 bars where (volume/(high-low)) > median(over 120d).
    Persistence of high-efficiency volume regime."""
    rng = (high - low).replace(0.0, np.nan)
    vpr = volume / rng
    med = vpr.rolling(120, min_periods=120).median()
    state = (vpr > med).astype(float).where(med.notna())
    return state.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Up-volume / down-volume regime =======================================


def f27vr_f27_volume_regime_up_v_frac_42d_base_v086_signal(close, volume):
    """Fraction of last 42 bars where (close > close.shift(1)) AND volume > median(volume,42).
    "Up-on-volume" regime intensity."""
    up = (close > close.shift(1)).astype(float)
    med = volume.rolling(42, min_periods=42).median()
    cond = (up * (volume > med).astype(float)).where(med.notna())
    return cond.rolling(42, min_periods=42).mean().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_down_v_frac_84d_base_v087_signal(closeadj, volume):
    """Fraction of last 84 bars with (close < close.shift) AND volume > median(volume,84).
    "Down-on-volume" regime intensity."""
    dn = (closeadj < closeadj.shift(1)).astype(float)
    med = volume.rolling(84, min_periods=84).median()
    cond = (dn * (volume > med).astype(float)).where(med.notna())
    return cond.rolling(84, min_periods=84).mean().replace([np.inf, -np.inf], np.nan)


# === Regime "shock" indicators (volume > k * past max) ====================


def f27vr_f27_volume_regime_shock_pct_max60_base_v088_signal(volume):
    """1 if volume > 1.5 * max(volume.shift(1), 60). Volume shock vs prior max."""
    mx = volume.shift(1).rolling(60, min_periods=60).max()
    out = (volume > 1.5 * mx).astype(float).where(mx.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dayssince_shock_max60_252d_base_v089_signal(volume):
    """Days since last shock event from v088 (capped 252)."""
    mx = volume.shift(1).rolling(60, min_periods=60).max()
    shock = (volume > 1.5 * mx).astype(float).where(mx.notna())
    return shock.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Quartile-bar density (count of bars at certain bucket) ===============


def f27vr_f27_volume_regime_bars_in_top_q_42d_base_v090_signal(volume):
    """Count of bars in trailing 42d where volume is in top quartile of trailing 252d.
    Discrete count of high-regime bars over 42d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    return state.rolling(42, min_periods=42).sum().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_bars_in_bot_q_42d_base_v091_signal(volume):
    """Count of bars in trailing 42d where volume is in bottom quartile of trailing 252d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r <= 0.25).astype(float).where(r.notna())
    return state.rolling(42, min_periods=42).sum().replace([np.inf, -np.inf], np.nan)


# === Volume regime "asymmetry" — top/bot bar diff =========================


def f27vr_f27_volume_regime_topbot_diff_84d_base_v092_signal(volume):
    """[Bars in top-q] - [Bars in bot-q] over trailing 84d (using 252d rank).
    Net regime-balance."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    s_top = (r >= 0.75).astype(float).where(r.notna())
    s_bot = (r <= 0.25).astype(float).where(r.notna())
    return (s_top.rolling(84, min_periods=84).sum() - s_bot.rolling(84, min_periods=84).sum()).replace([np.inf, -np.inf], np.nan)


# === Volume "regime crossings" — count of crossings of median =============


def f27vr_f27_volume_regime_median_crossings_60d_base_v093_signal(volume):
    """Number of times volume crosses its 30d median, counted in trailing 60d."""
    med = volume.rolling(30, min_periods=30).median()
    s = np.sign(volume - med)
    flip = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Log-volume autocorrelation lag-2 (different lag than file 1 v059) ===


def f27vr_f27_volume_regime_logv_acf2_60d_base_v094_signal(volume):
    """60d autocorr lag-2 of log(volume).  Regime persistence at 2-bar lag."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _ac2(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=2))
    return lv.rolling(60, min_periods=60).apply(_ac2, raw=False).replace([np.inf, -np.inf], np.nan)


# === Bucket-mode (most-frequent regime in window) =========================


def f27vr_f27_volume_regime_mode_bucket_q4_60d_base_v095_signal(volume):
    """Most-frequent quartile bucket (1..4) in trailing 60d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    def _mode(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        return float(vals[np.argmax(counts)])
    return bucket.rolling(60, min_periods=60).apply(_mode, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "consolidation" (low CV) state ================================


def f27vr_f27_volume_regime_calm_state_base_v096_signal(volume):
    """1 if CV(volume,30) < 30-day rolling median of CV(volume,30). Calm-volume state."""
    m = volume.rolling(30, min_periods=30).mean()
    s = volume.rolling(30, min_periods=30).std()
    cv = s / m.replace(0.0, np.nan)
    cv_med = cv.rolling(120, min_periods=120).median()
    out = (cv < cv_med).astype(float).where(cv.notna() & cv_med.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_streak_calm_84d_base_v097_signal(volume):
    """Consecutive bars in calm state (v096 def), capped 84."""
    m = volume.rolling(30, min_periods=30).mean()
    s = volume.rolling(30, min_periods=30).std()
    cv = s / m.replace(0.0, np.nan)
    cv_med = cv.rolling(120, min_periods=120).median()
    state = (cv < cv_med).astype(float).where(cv.notna() & cv_med.notna())
    return state.rolling(84, min_periods=84).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === DV regime persistence (DIFFERENT from file 1 DV streak) ==============


def f27vr_f27_volume_regime_dv_frac_low_42d_base_v098_signal(closeadj, volume):
    """Fraction of last 42 bars where dollar-volume is in bottom quartile of trailing 126d."""
    dv = closeadj * volume
    r = dv.rolling(126, min_periods=126).rank(pct=True)
    state = (r <= 0.25).astype(float).where(r.notna())
    return state.rolling(42, min_periods=42).mean().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dv_count_extreme_z_120d_base_v099_signal(closeadj, volume):
    """Count of bars in trailing 120d where |z(log DV, 60)| > 2. DV extreme density."""
    ldv = np.log((closeadj * volume).replace(0.0, np.nan))
    m = ldv.rolling(60, min_periods=60).mean()
    s = ldv.rolling(60, min_periods=60).std()
    z = (ldv - m) / s.replace(0.0, np.nan)
    ext = (z.abs() > 2.0).astype(float).where(z.notna())
    return ext.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Volume regime "skewness of bucket trajectory" ========================


def f27vr_f27_volume_regime_bucket_skew_84d_base_v100_signal(volume):
    """Skew of decile-bucket trajectory over trailing 84d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    return bucket.rolling(84, min_periods=84).skew().replace([np.inf, -np.inf], np.nan)


# === Volume regime correlation across windows =============================


def f27vr_f27_volume_regime_corr_rank_42_126_60d_base_v101_signal(volume):
    """60d Pearson correlation between rank(volume,42) and rank(volume,126).
    Correlation of two rank-series across windows."""
    r42 = volume.rolling(42, min_periods=42).rank(pct=True)
    r126 = volume.rolling(126, min_periods=126).rank(pct=True)
    return r42.rolling(60, min_periods=60).corr(r126).replace([np.inf, -np.inf], np.nan)


# === Days since volume regime mode change =================================


def f27vr_f27_volume_regime_dayssince_mode_change_84d_base_v102_signal(volume):
    """Days since mode_bucket(q4, 60d) changed (capped 84)."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    def _mode(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        return float(vals[np.argmax(counts)])
    mode = bucket.rolling(60, min_periods=60).apply(_mode, raw=True)
    flip = (mode != mode.shift(1)).astype(float).where(mode.notna() & mode.shift(1).notna())
    return flip.rolling(84, min_periods=84).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "trigger" — short rank vs long rank crossover sign ====


def f27vr_f27_volume_regime_sign_rank21_minus_rank63_base_v103_signal(volume):
    """sign(rank(volume,21) - rank(volume,63)). Discrete short-vs-medium regime tilt."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    return np.sign(r21 - r63).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sign_rank63_minus_rank252_base_v104_signal(volume):
    """sign(rank(volume,63) - rank(volume,252)). Discrete medium-vs-long tilt."""
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    r252 = volume.rolling(252, min_periods=252).rank(pct=True)
    return np.sign(r63 - r252).replace([np.inf, -np.inf], np.nan)


# === Volume regime ROC family (different from log/median) =================


def f27vr_f27_volume_regime_pct_change_30d_base_v105_signal(volume):
    """30d % change of volume: volume / volume.shift(30) - 1. Regime-level rate of change."""
    return (volume / volume.shift(30).replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_pct_change_120d_base_v106_signal(volume):
    """120d % change of volume."""
    return (volume / volume.shift(120).replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Volume "regime-conditional" mean diff ================================


def f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_base_v107_signal(volume):
    """[avg(volume | top-q, 84d) - avg(volume, 84d)] / avg(volume, 84d).
    Excess volume in top-q regime."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    is_top = (r >= 0.75).astype(float).where(r.notna())
    num = (volume * is_top).rolling(84, min_periods=84).sum()
    cnt = is_top.rolling(84, min_periods=84).sum()
    mean_top = num / cnt.replace(0.0, np.nan)
    mean_all = volume.rolling(84, min_periods=84).mean()
    return ((mean_top - mean_all) / mean_all.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume regime "rate of fired events" =================================


def f27vr_f27_volume_regime_spike_freq_252d_base_v108_signal(volume):
    """Number of "volume > 2.5 * SMA(volume,30)" events in trailing 252d."""
    m = volume.rolling(30, min_periods=30).mean()
    spike = (volume > 2.5 * m).astype(float).where(m.notna())
    return spike.rolling(252, min_periods=252).sum().replace([np.inf, -np.inf], np.nan)


# === Bars-since-extreme (use a different threshold than file 1) ==========


def f27vr_f27_volume_regime_dayssince_q90_event_120d_base_v109_signal(volume):
    """Days since rank(volume, 60d) >= 0.90, capped 120.
    Different threshold/window from file 1 dayssince features."""
    r = volume.rolling(60, min_periods=60).rank(pct=True)
    event = (r >= 0.90).astype(float).where(r.notna())
    return event.rolling(120, min_periods=120).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Regime "purity" — fraction of bars in same bucket as most common ====


def f27vr_f27_volume_regime_mode_share_60d_base_v110_signal(volume):
    """Fraction of trailing 60d in the most-common quartile bucket. Regime purity."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    def _mode_share(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        _, counts = np.unique(x, return_counts=True)
        return float(np.max(counts) / len(x))
    return bucket.rolling(60, min_periods=60).apply(_mode_share, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "expansion-from-low" ===================================


def f27vr_f27_volume_regime_lowtomed_lift_base_v111_signal(volume):
    """log(volume / rolling-min-of-volume(30)) / log(rolling-max(30) / rolling-min(30)).
    Position of current volume within recent min-max range."""
    mn = volume.rolling(30, min_periods=30).min()
    mx = volume.rolling(30, min_periods=30).max()
    num = np.log(volume / mn.replace(0.0, np.nan))
    den = np.log(mx / mn.replace(0.0, np.nan))
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Decile transition magnitude average ==================================


def f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_base_v112_signal(volume):
    """Mean |Δ quartile-bucket| (252d-rank) over trailing 84d.
    Average regime move magnitude per bar."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    j = (bucket - bucket.shift(1)).abs()
    return j.rolling(84, min_periods=84).mean().replace([np.inf, -np.inf], np.nan)


# === Volume regime "Hurst-like" range/std =================================


def f27vr_f27_volume_regime_rs_logv_84d_base_v113_signal(volume):
    """R/S range/std of log(volume) over 84d. Persistence diagnostic."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _rs(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        y = x - x.mean()
        z = np.cumsum(y)
        R = z.max() - z.min()
        S = x.std(ddof=0)
        if S == 0.0:
            return np.nan
        return float(R / S)
    return lv.rolling(84, min_periods=84).apply(_rs, raw=True).replace([np.inf, -np.inf], np.nan)


# === Regime "stickiness" with longer window ===============================


def f27vr_f27_volume_regime_run_length_avg_high_120d_base_v114_signal(volume):
    """Average completed-run length of high-q regime in trailing 120d.
    Differs from file 1 v058 (252d, 126d-rank) — here 120d window, 84d-rank."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    cnt_in = state.rolling(120, min_periods=120).sum()
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    n_runs = entry.rolling(120, min_periods=120).sum()
    return (cnt_in / n_runs.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume regime "transition complexity" — entropy of bucket transitions =


def f27vr_f27_volume_regime_max_bucket_jump_84d_base_v115_signal(volume):
    """Max absolute decile-bucket jump in trailing 84d. Largest single-bar regime move.
    Differs structurally from v112 (mean jump): max-aggregator + decile (not quartile)."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    d = (bucket - bucket.shift(1)).abs()
    return d.rolling(84, min_periods=84).max().replace([np.inf, -np.inf], np.nan)


# === Volume regime "agreement" — count of windows in same decile ========


def f27vr_f27_volume_regime_window_same_decile_count_base_v116_signal(volume):
    """Count of windows among {63d, 126d, 252d} where current volume falls in same decile.
    Captures how robust the decile label is across horizons."""
    r1 = volume.rolling(63, min_periods=63).rank(pct=True)
    r2 = volume.rolling(126, min_periods=126).rank(pct=True)
    r3 = volume.rolling(252, min_periods=252).rank(pct=True)
    b1 = np.ceil(r1.where(r1.notna()).clip(lower=1e-9) * 10.0)
    b2 = np.ceil(r2.where(r2.notna()).clip(lower=1e-9) * 10.0)
    b3 = np.ceil(r3.where(r3.notna()).clip(lower=1e-9) * 10.0)
    agg = ((b1 == b2).astype(float) + (b2 == b3).astype(float) + (b1 == b3).astype(float))
    mask = r1.notna() & r2.notna() & r3.notna()
    return agg.where(mask).replace([np.inf, -np.inf], np.nan)


# === Discrete state durations (different streak target than file 1) =====


def f27vr_f27_volume_regime_streak_below_sma60_120d_base_v117_signal(volume):
    """Consecutive bars where volume < SMA(volume,60), capped 120."""
    m = volume.rolling(60, min_periods=60).mean()
    state = (volume < m).astype(float).where(m.notna())
    return state.rolling(120, min_periods=120).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_streak_above_sma120_180d_base_v118_signal(volume):
    """Consecutive bars where volume > SMA(volume,120), capped 180."""
    m = volume.rolling(120, min_periods=120).mean()
    state = (volume > m).astype(float).where(m.notna())
    return state.rolling(180, min_periods=180).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Multi-state count: 3+ horizons in elevated =========================


def f27vr_f27_volume_regime_count_ge_3_horizons_high_base_v119_signal(volume):
    """1 if at least 3 of 4 horizons {21,63,126,252} have rank >= 0.6, else 0.
    Binary multi-horizon confluence."""
    r1 = volume.rolling(21, min_periods=21).rank(pct=True)
    r2 = volume.rolling(63, min_periods=63).rank(pct=True)
    r3 = volume.rolling(126, min_periods=126).rank(pct=True)
    r4 = volume.rolling(252, min_periods=252).rank(pct=True)
    cnt = ((r1 >= 0.6).astype(float) + (r2 >= 0.6).astype(float) + (r3 >= 0.6).astype(float) + (r4 >= 0.6).astype(float))
    out = (cnt >= 3.0).astype(float).where(r1.notna() & r2.notna() & r3.notna() & r4.notna())
    return out.replace([np.inf, -np.inf], np.nan)


# === Volume regime "median deviation" =====================================


def f27vr_f27_volume_regime_v_minus_median_z_42d_base_v120_signal(volume):
    """(volume - median(60)) / IQR(60). Robust z-score (orthogonal to mean-based z)."""
    med = volume.rolling(60, min_periods=60).median()
    q75 = volume.rolling(60, min_periods=60).quantile(0.75)
    q25 = volume.rolling(60, min_periods=60).quantile(0.25)
    iqr = (q75 - q25)
    return ((volume - med) / iqr.replace(0.0, np.nan)).rolling(42, min_periods=42).mean().replace([np.inf, -np.inf], np.nan)


# === Sign(volume - SMA(volume, N)) at distinct N ==========================


def f27vr_f27_volume_regime_sign_v_sma100_base_v121_signal(volume):
    """sign(volume - SMA(volume, 100)). Discrete long-term regime side."""
    m = volume.rolling(100, min_periods=100).mean()
    return np.sign(volume - m).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sign_v_sma15_base_v122_signal(volume):
    """sign(volume - SMA(volume, 15)). Discrete short-term regime side."""
    m = volume.rolling(15, min_periods=15).mean()
    return np.sign(volume - m).replace([np.inf, -np.inf], np.nan)


# === Variance of variance — vol-of-volvol =================================


def f27vr_f27_volume_regime_volvol_of_volvol_120d_base_v123_signal(volume):
    """std of CV(volume,30) over 120d. How much "regime stability" itself moves."""
    m = volume.rolling(30, min_periods=30).mean()
    s = volume.rolling(30, min_periods=30).std()
    cv = s / m.replace(0.0, np.nan)
    return cv.rolling(120, min_periods=120).std().replace([np.inf, -np.inf], np.nan)


# === Volume "drift" in regime: lin reg slope of bucket ==================


def f27vr_f27_volume_regime_regslope_bucket_q4_84d_base_v124_signal(volume):
    """OLS slope of quartile-bucket vs time over 84d (252d rank).
    Trend of regime, normalized."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var = np.sum((t - mean_t) ** 2)
        if var == 0.0:
            return np.nan
        return float(cov / var)
    return bucket.rolling(84, min_periods=84).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime peak-trough features ===================================


def f27vr_f27_volume_regime_v_to_max_dist_index_42d_base_v125_signal(volume):
    """Bars since volume.rolling(42).max() was set, capped 42.
    Time-since-peak-volume; signals "regime cooling" since last peak."""
    def _argmax_age(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return volume.rolling(42, min_periods=42).apply(_argmax_age, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_v_to_min_dist_index_84d_base_v126_signal(volume):
    """Bars since volume.rolling(84).min() was set."""
    def _argmin_age(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(x) - 1 - int(np.argmin(x)))
    return volume.rolling(84, min_periods=84).apply(_argmin_age, raw=True).replace([np.inf, -np.inf], np.nan)


# === Discrete bucket "stickiness" with shift-N comparison ===============


def f27vr_f27_volume_regime_stickiness_decile_30d_base_v127_signal(volume):
    """Fraction of last 30 bars where decile(volume,252d) == decile 5 bars ago.
    Mid-horizon stickiness."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    same = (bucket == bucket.shift(5)).astype(float).where(bucket.notna() & bucket.shift(5).notna())
    return same.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Volume "regime trigger" — diff of differences  ======================


def f27vr_f27_volume_regime_logv_accel_5_5_base_v128_signal(volume):
    """log(volume).diff(5).diff(5). Volume regime acceleration."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.diff(5).diff(5).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sign_logv_accel_10_10_base_v129_signal(volume):
    """sign(log(volume).diff(10).diff(10)). Discrete regime acceleration sign."""
    lv = np.log(volume.replace(0.0, np.nan))
    return np.sign(lv.diff(10).diff(10)).replace([np.inf, -np.inf], np.nan)


# === Volume regime CV difference across windows ==========================


def f27vr_f27_volume_regime_volvol_short_minus_long_base_v130_signal(volume):
    """CV(volume,30) - CV(volume,120). Regime-stability difference (short - long)."""
    m1 = volume.rolling(30, min_periods=30).mean()
    s1 = volume.rolling(30, min_periods=30).std()
    cv1 = s1 / m1.replace(0.0, np.nan)
    m2 = volume.rolling(120, min_periods=120).mean()
    s2 = volume.rolling(120, min_periods=120).std()
    cv2 = s2 / m2.replace(0.0, np.nan)
    return (cv1 - cv2).replace([np.inf, -np.inf], np.nan)


# === DV regime entry/exit events (different from file 1) =================


def f27vr_f27_volume_regime_dv_exit_event_top_q_base_v131_signal(closeadj, volume):
    """1 on bar dollar-volume exits top-quartile regime (over 126d rank)."""
    dv = closeadj * volume
    r = dv.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    exit_ = ((state <= 0.5) & (state.shift(1) > 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return exit_.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dv_dayssince_low_state_base_v132_signal(closeadj, volume):
    """Days since dollar-volume last in bottom decile of 126d, capped 252."""
    dv = closeadj * volume
    r = dv.rolling(126, min_periods=126).rank(pct=True)
    event = (r <= 0.1).astype(float).where(r.notna())
    return event.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "stability" — autocorrelation of bucket sequence ======


def f27vr_f27_volume_regime_bucket_acf1_120d_base_v133_signal(volume):
    """120d autocorr lag-1 of decile-bucket trajectory (252d rank).
    Persistence of discrete regime label."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    def _ac1(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=1))
    return bucket.rolling(120, min_periods=120).apply(_ac1, raw=False).replace([np.inf, -np.inf], np.nan)


# === Volume regime "drawdown" from local max =============================


def f27vr_f27_volume_regime_v_drawdown_from_max252_base_v134_signal(volume):
    """log(volume / max(volume, 252)). Distance below 252d peak, in log."""
    mx = volume.rolling(252, min_periods=252).max()
    return np.log(volume / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "bracketed" — sign-and-mag classification ====================


def f27vr_f27_volume_regime_bracket_z_logv_60d_base_v135_signal(volume):
    """Classification: -2 if z<-2, -1 if -2<=z<-1, 0 if |z|<1, 1 if 1<=z<2, 2 if z>=2.
    Discrete 5-class regime label."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    mz = z.notna()
    zz = z[mz]
    cls = pd.Series(0.0, index=zz.index, dtype=float)
    cls[zz <= -2.0] = -2.0
    cls[(zz > -2.0) & (zz <= -1.0)] = -1.0
    cls[(zz >= 1.0) & (zz < 2.0)] = 1.0
    cls[zz >= 2.0] = 2.0
    out[mz] = cls
    return out.replace([np.inf, -np.inf], np.nan)


# === Volume regime "noise floor" — std / median ==========================


def f27vr_f27_volume_regime_std_over_median_60d_base_v136_signal(volume):
    """std(volume, 60) / median(volume, 60). Robust dispersion measure."""
    s = volume.rolling(60, min_periods=60).std()
    med = volume.rolling(60, min_periods=60).median()
    return (s / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Number of bars in 80-100% bucket within window ======================


def f27vr_f27_volume_regime_count_top20_84d_base_v137_signal(volume):
    """Count of trailing 84d bars with rank(volume, 252) >= 0.80."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.80).astype(float).where(r.notna())
    return state.rolling(84, min_periods=84).sum().replace([np.inf, -np.inf], np.nan)


# === Volume regime "winsorized mean" ratio ==============================


def f27vr_f27_volume_regime_logv_winsor_over_mean_120d_base_v138_signal(volume):
    """log( winsor-mean(volume, 120, 5%) / mean(volume, 120) ). Robust-vs-raw mean ratio.
    Captures how much tails distort the regime mean."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _w(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        lo = np.quantile(x, 0.05); hi = np.quantile(x, 0.95)
        y = np.clip(x, lo, hi)
        return float(np.mean(y))
    win = lv.rolling(120, min_periods=120).apply(_w, raw=True)
    return (win - lv.rolling(120, min_periods=120).mean()).replace([np.inf, -np.inf], np.nan)


# === Volume bucket "frequency tail" =====================================


def f27vr_f27_volume_regime_top_decile_freq_252d_base_v139_signal(volume):
    """Fraction of trailing 252d in top decile (252d rank)."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.9).astype(float).where(r.notna())
    return state.rolling(252, min_periods=252).mean().replace([np.inf, -np.inf], np.nan)


# === Volume regime "alternation rate" — sign flips ======================


def f27vr_f27_volume_regime_signflip_v_sma_42d_base_v140_signal(volume):
    """Number of times sign(volume - SMA(volume,21)) flips in trailing 42d / 42.
    Volume regime alternation frequency."""
    m = volume.rolling(21, min_periods=21).mean()
    s = np.sign(volume - m)
    flip = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return (flip.rolling(42, min_periods=42).sum() / 42.0).replace([np.inf, -np.inf], np.nan)


# === Volume regime "weighted bucket" =====================================


def f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_base_v141_signal(volume):
    """Time-weighted average of quartile bucket (252d rank) over 60d, more weight on recent."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    w = np.arange(1, 61, dtype=float); w /= w.sum()
    def _wm(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(np.dot(x, w))
    return bucket.rolling(60, min_periods=60).apply(_wm, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "min-max sweep range" =================================




# === Bucket variance ratio short vs long =================================


def f27vr_f27_volume_regime_bucket_var_short_over_long_base_v143_signal(volume):
    """var(bucket, 30) / var(bucket, 120). Short-vs-long-window regime variance ratio."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    v1 = bucket.rolling(30, min_periods=30).var()
    v2 = bucket.rolling(120, min_periods=120).var()
    return (v1 / v2.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Stationarity check — bucket frequency std =========================


def f27vr_f27_volume_regime_bucket_freq_std_120d_base_v144_signal(volume):
    """Std of decile-bucket distribution counts over 120d. Lower => more uniform."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    def _freq_std(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        return float(np.std(counts))
    return bucket.rolling(120, min_periods=120).apply(_freq_std, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "fanout" — number of distinct buckets visited ========


def f27vr_f27_volume_regime_distinct_deciles_60d_base_v145_signal(volume):
    """Number of distinct decile buckets visited in trailing 60d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    def _nuniq(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(np.unique(x)))
    return bucket.rolling(60, min_periods=60).apply(_nuniq, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "quiet period" indicator =============================


def f27vr_f27_volume_regime_quiet_60d_streak_base_v146_signal(volume):
    """Consecutive bars where volume in bottom-30% of trailing 60d, capped 60.
    Quiet-volume regime persistence."""
    r = volume.rolling(60, min_periods=60).rank(pct=True)
    state = (r <= 0.3).astype(float).where(r.notna())
    return state.rolling(60, min_periods=60).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume regime SHOCKS =========================================


def f27vr_f27_volume_regime_dv_shock_3x_sma40_base_v147_signal(closeadj, volume):
    """1 if dollar-volume > 3 * SMA(DV, 40). DV shock indicator."""
    dv = closeadj * volume
    m = dv.rolling(40, min_periods=40).mean()
    out = (dv > 3.0 * m).astype(float).where(m.notna())
    return out.replace([np.inf, -np.inf], np.nan)


# === Volume regime "trend in rank" =======================================


def f27vr_f27_volume_regime_rank_regslope_60d_base_v148_signal(volume):
    """OLS slope of rank(volume, 84) vs time over 60d. Trend of percentile placement."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var = np.sum((t - mean_t) ** 2)
        if var == 0.0:
            return np.nan
        return float(cov / var)
    return r.rolling(60, min_periods=60).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime — pct in extreme |z| ===================================


def f27vr_f27_volume_regime_frac_abszgt1_120d_base_v149_signal(volume):
    """Fraction of last 120 bars where |z(logv, 60)| > 1. Density of "off-baseline" days."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    state = (z.abs() > 1.0).astype(float).where(z.notna())
    return state.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Volume regime — count of cross-quartile leaps =====================


def f27vr_f27_volume_regime_big_bucket_leap_count_42d_base_v150_signal(volume):
    """Count of bars in trailing 42d with |Δ tertile-bucket(84d)| == 2. Big regime leap density."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 3.0)
    d = (bucket - bucket.shift(1)).abs()
    leap = (d == 2.0).astype(float).where(d.notna())
    return leap.rolling(42, min_periods=42).sum().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f27_volume_regime_base_076_150_REGISTRY = {
    "f27vr_f27_volume_regime_sextile_bucket_84d_base_v076_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sextile_bucket_84d_base_v076_signal},
    "f27vr_f27_volume_regime_octile_change_count_60d_base_v077_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_octile_change_count_60d_base_v077_signal},
    "f27vr_f27_volume_regime_v_kurt_252d_base_v079_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_kurt_252d_base_v079_signal},
    "f27vr_f27_volume_regime_logv_roc_21d_base_v080_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_roc_21d_base_v080_signal},
    "f27vr_f27_volume_regime_sma_v_ratio_10_252_base_v081_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sma_v_ratio_10_252_base_v081_signal},
    "f27vr_f27_volume_regime_up_trans_count_q3_120d_base_v082_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_up_trans_count_q3_120d_base_v082_signal},
    "f27vr_f27_volume_regime_down_trans_count_q3_120d_base_v083_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_down_trans_count_q3_120d_base_v083_signal},
    "f27vr_f27_volume_regime_v_per_range_pctrank_84d_base_v084_signal": {"inputs": ["high", "low", "volume"], "func": f27vr_f27_volume_regime_v_per_range_pctrank_84d_base_v084_signal},
    "f27vr_f27_volume_regime_v_per_range_high_state_120d_base_v085_signal": {"inputs": ["high", "low", "volume"], "func": f27vr_f27_volume_regime_v_per_range_high_state_120d_base_v085_signal},
    "f27vr_f27_volume_regime_up_v_frac_42d_base_v086_signal": {"inputs": ["close", "volume"], "func": f27vr_f27_volume_regime_up_v_frac_42d_base_v086_signal},
    "f27vr_f27_volume_regime_down_v_frac_84d_base_v087_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_down_v_frac_84d_base_v087_signal},
    "f27vr_f27_volume_regime_shock_pct_max60_base_v088_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_shock_pct_max60_base_v088_signal},
    "f27vr_f27_volume_regime_dayssince_shock_max60_252d_base_v089_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_shock_max60_252d_base_v089_signal},
    "f27vr_f27_volume_regime_bars_in_top_q_42d_base_v090_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bars_in_top_q_42d_base_v090_signal},
    "f27vr_f27_volume_regime_bars_in_bot_q_42d_base_v091_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bars_in_bot_q_42d_base_v091_signal},
    "f27vr_f27_volume_regime_topbot_diff_84d_base_v092_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_topbot_diff_84d_base_v092_signal},
    "f27vr_f27_volume_regime_median_crossings_60d_base_v093_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_median_crossings_60d_base_v093_signal},
    "f27vr_f27_volume_regime_logv_acf2_60d_base_v094_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_acf2_60d_base_v094_signal},
    "f27vr_f27_volume_regime_mode_bucket_q4_60d_base_v095_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mode_bucket_q4_60d_base_v095_signal},
    "f27vr_f27_volume_regime_calm_state_base_v096_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_calm_state_base_v096_signal},
    "f27vr_f27_volume_regime_streak_calm_84d_base_v097_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_calm_84d_base_v097_signal},
    "f27vr_f27_volume_regime_dv_frac_low_42d_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_frac_low_42d_base_v098_signal},
    "f27vr_f27_volume_regime_dv_count_extreme_z_120d_base_v099_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_count_extreme_z_120d_base_v099_signal},
    "f27vr_f27_volume_regime_bucket_skew_84d_base_v100_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_skew_84d_base_v100_signal},
    "f27vr_f27_volume_regime_corr_rank_42_126_60d_base_v101_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_corr_rank_42_126_60d_base_v101_signal},
    "f27vr_f27_volume_regime_dayssince_mode_change_84d_base_v102_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_mode_change_84d_base_v102_signal},
    "f27vr_f27_volume_regime_sign_rank21_minus_rank63_base_v103_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_rank21_minus_rank63_base_v103_signal},
    "f27vr_f27_volume_regime_sign_rank63_minus_rank252_base_v104_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_rank63_minus_rank252_base_v104_signal},
    "f27vr_f27_volume_regime_pct_change_30d_base_v105_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_change_30d_base_v105_signal},
    "f27vr_f27_volume_regime_pct_change_120d_base_v106_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_change_120d_base_v106_signal},
    "f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_base_v107_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_base_v107_signal},
    "f27vr_f27_volume_regime_spike_freq_252d_base_v108_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike_freq_252d_base_v108_signal},
    "f27vr_f27_volume_regime_dayssince_q90_event_120d_base_v109_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_q90_event_120d_base_v109_signal},
    "f27vr_f27_volume_regime_mode_share_60d_base_v110_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mode_share_60d_base_v110_signal},
    "f27vr_f27_volume_regime_lowtomed_lift_base_v111_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_lowtomed_lift_base_v111_signal},
    "f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_base_v112_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_base_v112_signal},
    "f27vr_f27_volume_regime_rs_logv_84d_base_v113_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rs_logv_84d_base_v113_signal},
    "f27vr_f27_volume_regime_run_length_avg_high_120d_base_v114_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_run_length_avg_high_120d_base_v114_signal},
    "f27vr_f27_volume_regime_max_bucket_jump_84d_base_v115_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_max_bucket_jump_84d_base_v115_signal},
    "f27vr_f27_volume_regime_window_same_decile_count_base_v116_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_window_same_decile_count_base_v116_signal},
    "f27vr_f27_volume_regime_streak_below_sma60_120d_base_v117_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_below_sma60_120d_base_v117_signal},
    "f27vr_f27_volume_regime_streak_above_sma120_180d_base_v118_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_above_sma120_180d_base_v118_signal},
    "f27vr_f27_volume_regime_count_ge_3_horizons_high_base_v119_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_ge_3_horizons_high_base_v119_signal},
    "f27vr_f27_volume_regime_v_minus_median_z_42d_base_v120_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_minus_median_z_42d_base_v120_signal},
    "f27vr_f27_volume_regime_sign_v_sma100_base_v121_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_v_sma100_base_v121_signal},
    "f27vr_f27_volume_regime_sign_v_sma15_base_v122_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_v_sma15_base_v122_signal},
    "f27vr_f27_volume_regime_volvol_of_volvol_120d_base_v123_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_of_volvol_120d_base_v123_signal},
    "f27vr_f27_volume_regime_regslope_bucket_q4_84d_base_v124_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_regslope_bucket_q4_84d_base_v124_signal},
    "f27vr_f27_volume_regime_v_to_max_dist_index_42d_base_v125_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_to_max_dist_index_42d_base_v125_signal},
    "f27vr_f27_volume_regime_v_to_min_dist_index_84d_base_v126_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_to_min_dist_index_84d_base_v126_signal},
    "f27vr_f27_volume_regime_stickiness_decile_30d_base_v127_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_stickiness_decile_30d_base_v127_signal},
    "f27vr_f27_volume_regime_logv_accel_5_5_base_v128_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_accel_5_5_base_v128_signal},
    "f27vr_f27_volume_regime_sign_logv_accel_10_10_base_v129_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_logv_accel_10_10_base_v129_signal},
    "f27vr_f27_volume_regime_volvol_short_minus_long_base_v130_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_short_minus_long_base_v130_signal},
    "f27vr_f27_volume_regime_dv_exit_event_top_q_base_v131_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_exit_event_top_q_base_v131_signal},
    "f27vr_f27_volume_regime_dv_dayssince_low_state_base_v132_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_dayssince_low_state_base_v132_signal},
    "f27vr_f27_volume_regime_bucket_acf1_120d_base_v133_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_acf1_120d_base_v133_signal},
    "f27vr_f27_volume_regime_v_drawdown_from_max252_base_v134_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_drawdown_from_max252_base_v134_signal},
    "f27vr_f27_volume_regime_bracket_z_logv_60d_base_v135_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bracket_z_logv_60d_base_v135_signal},
    "f27vr_f27_volume_regime_std_over_median_60d_base_v136_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_std_over_median_60d_base_v136_signal},
    "f27vr_f27_volume_regime_count_top20_84d_base_v137_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_top20_84d_base_v137_signal},
    "f27vr_f27_volume_regime_logv_winsor_over_mean_120d_base_v138_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_winsor_over_mean_120d_base_v138_signal},
    "f27vr_f27_volume_regime_top_decile_freq_252d_base_v139_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_top_decile_freq_252d_base_v139_signal},
    "f27vr_f27_volume_regime_signflip_v_sma_42d_base_v140_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_signflip_v_sma_42d_base_v140_signal},
    "f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_base_v141_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_base_v141_signal},
    "f27vr_f27_volume_regime_bucket_var_short_over_long_base_v143_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_var_short_over_long_base_v143_signal},
    "f27vr_f27_volume_regime_bucket_freq_std_120d_base_v144_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_freq_std_120d_base_v144_signal},
    "f27vr_f27_volume_regime_distinct_deciles_60d_base_v145_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_distinct_deciles_60d_base_v145_signal},
    "f27vr_f27_volume_regime_quiet_60d_streak_base_v146_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_quiet_60d_streak_base_v146_signal},
    "f27vr_f27_volume_regime_dv_shock_3x_sma40_base_v147_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_shock_3x_sma40_base_v147_signal},
    "f27vr_f27_volume_regime_rank_regslope_60d_base_v148_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_regslope_60d_base_v148_signal},
    "f27vr_f27_volume_regime_frac_abszgt1_120d_base_v149_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_abszgt1_120d_base_v149_signal},
    "f27vr_f27_volume_regime_big_bucket_leap_count_42d_base_v150_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_big_bucket_leap_count_42d_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f27_volume_regime_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
