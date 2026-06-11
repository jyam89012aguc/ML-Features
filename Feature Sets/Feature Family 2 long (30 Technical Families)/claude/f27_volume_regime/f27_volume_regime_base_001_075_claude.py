"""f27_volume_regime base features 001-075.

Domain: VOLUME REGIME CLASSIFICATION & TRANSITIONS — discrete buckets
(quartile/quintile/decile of volume in trailing windows), high/low-volume
state indicators, multi-window regime agreement, regime transition counts,
bars-since-last-regime-change, persistence/streak in current regime,
expansion/contraction ratios, spike detection, dollar-volume regimes,
bounded transforms of regime scores, regime-conditional stats.

Distinct from f21 (raw volume statistics), f22 (volume trend / MA slopes),
f24 (volume-price confirmation). Stays focused on REGIME CLASSIFICATION
and TRANSITIONS of the volume series itself.

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
final return. Window > 21d uses closeadj for any price-component; volume
is always raw (no adjustment needed). Each function spells its formula
inline. No structural duplicates within a window-change of another.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers — kept minimal; each feature spells its computation inline.
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Discrete quantile bucket classifications =============================


def f27vr_f27_volume_regime_q4_bucket_42d_base_v001_signal(volume):
    """Volume quartile (1..4) in trailing 42d window. Short-horizon discrete regime label.
    Separated from v015 (189d pct-rank) by very different windows."""
    r = volume.rolling(42, min_periods=42).rank(pct=True)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    out[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_base_v002_signal(volume):
    """Q4 bucket(252) today - Q4 bucket(252) yesterday. Bucket move (integer diff).
    Discrete value in {-3..+3}, decorrelated from level-based features."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    bucket[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    return (bucket - bucket.shift(1)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_count_decile_jumps_120d_base_v003_signal(volume):
    """Count of |decile_change| >= 2 in trailing 120d. Big-jump regime events.
    Discrete count; decorrelated from level-rank features."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    bucket[m] = np.ceil(r[m].clip(lower=1e-9) * 10.0)
    jump = (bucket - bucket.shift(1)).abs()
    event = (jump >= 2.0).astype(float).where(jump.notna())
    return event.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dispersion_buckets_21d_base_v004_signal(volume):
    """Number of unique quartile buckets visited in trailing 21d (1..4).
    Short-window regime diversity."""
    r = volume.rolling(63, min_periods=63).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    bucket[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    def _nuniq(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(np.unique(x)))
    return bucket.rolling(21, min_periods=21).apply(_nuniq, raw=True).replace([np.inf, -np.inf], np.nan)


# === High/low regime ENTRY EVENTS (binary) — only sparse events ===========


def f27vr_f27_volume_regime_entry_event_top_d_base_v005_signal(volume):
    """1 on the bar when state enters top-decile regime (0->1 over 252d rank), else 0.
    Sparse entry event signal."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.9).astype(float).where(r.notna())
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_exit_event_top_q_base_v006_signal(volume):
    """1 on the bar when state exits top-quartile regime (1->0 over 126d rank).
    Sparse exit event."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    exit_ = ((state <= 0.5) & (state.shift(1) > 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return exit_.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_any_state_flip_q4_base_v007_signal(volume):
    """1 on any quartile-bucket change (252d). Sparse transition indicator."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    bucket[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    return (bucket != bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna()).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_streak_below_med_120d_base_v008_signal(volume):
    """Consecutive bars where volume < median(volume,63), capped 120.
    Streak counter; decorrelated from rank/level features."""
    med = volume.rolling(63, min_periods=63).median()
    state = (volume < med).astype(float).where(med.notna())
    return state.rolling(120, min_periods=120).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Multi-window regime agreement ========================================


def f27vr_f27_volume_regime_multi_top_q_agree_base_v009_signal(volume):
    """Count of windows {21,63,126,252} where volume is in top quartile of that window."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    r126 = volume.rolling(126, min_periods=126).rank(pct=True)
    r252 = volume.rolling(252, min_periods=252).rank(pct=True)
    a = (r21 >= 0.75).astype(float) + (r63 >= 0.75).astype(float) + (r126 >= 0.75).astype(float) + (r252 >= 0.75).astype(float)
    mask = r21.notna() & r63.notna() & r126.notna() & r252.notna()
    return a.where(mask).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_multi_bot_q_agree_base_v010_signal(volume):
    """Count of windows {21,63,126,252} where volume is in bottom quartile of that window."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    r126 = volume.rolling(126, min_periods=126).rank(pct=True)
    r252 = volume.rolling(252, min_periods=252).rank(pct=True)
    a = (r21 <= 0.25).astype(float) + (r63 <= 0.25).astype(float) + (r126 <= 0.25).astype(float) + (r252 <= 0.25).astype(float)
    mask = r21.notna() & r63.notna() & r126.notna() & r252.notna()
    return a.where(mask).replace([np.inf, -np.inf], np.nan)


# === Volume / median ratio (regime-level normalization) ===================


def f27vr_f27_volume_regime_v_over_median_21d_base_v011_signal(volume):
    """log(volume / median(volume, 21)). SHORT-window regime level; very different
    horizon from v015 (189d pct rank) and v001 (42d q4 bucket)."""
    med = volume.rolling(21, min_periods=21).median()
    return np.log(volume / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_q4_bucket_diff_short_long_base_v012_signal(volume):
    """Q4_bucket(63d) - Q4_bucket(252d). Short-vs-long horizon bucket disagreement.
    Integer in {-3..+3}; orthogonal to single-bar level features."""
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    r252 = volume.rolling(252, min_periods=252).rank(pct=True)
    b63 = pd.Series(np.nan, index=volume.index, dtype=float)
    b252 = pd.Series(np.nan, index=volume.index, dtype=float)
    m1 = r63.notna(); m2 = r252.notna()
    b63[m1] = np.ceil(r63[m1].clip(lower=1e-9) * 4.0)
    b252[m2] = np.ceil(r252[m2].clip(lower=1e-9) * 4.0)
    return (b63 - b252).replace([np.inf, -np.inf], np.nan)


# === Volume change-rate (orthogonal to level) =============================


def f27vr_f27_volume_regime_logv_diff_5d_base_v013_signal(volume):
    """log(volume) - log(volume).shift(5). Short-period volume regime delta.
    Orthogonal to single-bar level features (it's a difference)."""
    lv = np.log(volume.replace(0.0, np.nan))
    return (lv - lv.shift(5)).replace([np.inf, -np.inf], np.nan)


# === Cross-bar regime correlation =========================================


def f27vr_f27_volume_regime_lag_v_corr_30d_base_v014_signal(volume):
    """30d Pearson corr between log(volume) and log(volume).shift(1).
    Regime auto-tracking (different from raw acf)."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(30, min_periods=30).corr(lv.shift(1)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_pct_rank_189d_base_v015_signal(volume):
    """Percentile rank of volume in trailing 189d window. KEPT level feature #3."""
    return volume.rolling(189, min_periods=189).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Regime transitions (days-since, counts) ==============================


def f27vr_f27_volume_regime_dayssince_top_q_change_252d_base_v016_signal(volume):
    """Bars since last entry into top-quartile regime (over 252d window)."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    # entry event: state goes 0 -> 1
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dayssince_bot_q_change_252d_base_v017_signal(volume):
    """Bars since last entry into bottom-quartile regime (over 252d window)."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r <= 0.25).astype(float).where(r.notna())
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_change_count_q4_120d_base_v018_signal(volume):
    """Number of quartile-regime changes in trailing 120d (over 63d quartile labels)."""
    r = volume.rolling(63, min_periods=63).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    bucket[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    flip = (bucket != bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return flip.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_change_count_top_state_252d_base_v019_signal(volume):
    """Number of top-decile-state transitions in trailing 252d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.9).astype(float).where(r.notna())
    flip = (state != state.shift(1)).astype(float).where(state.notna() & state.shift(1).notna())
    return flip.rolling(252, min_periods=252).sum().replace([np.inf, -np.inf], np.nan)


# === Regime persistence (fraction in regime) ==============================


def f27vr_f27_volume_regime_frac_top_q_120d_base_v020_signal(volume):
    """Fraction of last 120 bars where volume was in top quartile of trailing 252d."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    return state.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_frac_bot_q_63d_base_v021_signal(volume):
    """Fraction of last 63 bars where volume was in bottom quartile of trailing 126d."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r <= 0.25).astype(float).where(r.notna())
    return state.rolling(63, min_periods=63).mean().replace([np.inf, -np.inf], np.nan)


# === Streaks in regime ====================================================


def f27vr_f27_volume_regime_streak_top_q_120d_base_v022_signal(volume):
    """Consecutive bars where volume is in top quartile of trailing 126d, capped 120."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    return state.rolling(120, min_periods=120).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_streak_bot_d_180d_base_v023_signal(volume):
    """Consecutive bars where volume is in bottom decile of trailing 252d, capped 180."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r <= 0.1).astype(float).where(r.notna())
    return state.rolling(180, min_periods=180).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume expansion / contraction =======================================


def f27vr_f27_volume_regime_expand_10_60_base_v024_signal(volume):
    """log(SMA(volume,10) / SMA(volume,60)). Short-vs-medium volume regime expansion."""
    s10 = volume.rolling(10, min_periods=10).mean()
    s60 = volume.rolling(60, min_periods=60).mean()
    return np.log(s10 / s60.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_expand_21_126_base_v025_signal(volume):
    """log(SMA(volume,21) / SMA(volume,126))."""
    s21 = volume.rolling(21, min_periods=21).mean()
    s126 = volume.rolling(126, min_periods=126).mean()
    return np.log(s21 / s126.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_expand_5_42_base_v026_signal(volume):
    """log(SMA(volume,5) / SMA(volume,42)). Very-short vs medium."""
    s5 = volume.rolling(5, min_periods=5).mean()
    s42 = volume.rolling(42, min_periods=42).mean()
    return np.log(s5 / s42.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume vol-of-vol (regime stability) =================================


def f27vr_f27_volume_regime_volvol_30d_base_v027_signal(volume):
    """std(volume, 30) / mean(volume, 30). Volume coefficient-of-variation; regime stability."""
    m = volume.rolling(30, min_periods=30).mean()
    s = volume.rolling(30, min_periods=30).std()
    return (s / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_volvol_120d_base_v028_signal(volume):
    """std(volume, 120) / mean(volume, 120). Long-window volume CV."""
    m = volume.rolling(120, min_periods=120).mean()
    s = volume.rolling(120, min_periods=120).std()
    return (s / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume spike detection ===============================================


def f27vr_f27_volume_regime_spike2x_sma20_base_v029_signal(volume):
    """1 if volume > 2 * SMA(volume,20). Volume spike indicator."""
    m = volume.rolling(20, min_periods=20).mean()
    out = (volume > 2.0 * m).astype(float).where(m.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_base_v030_signal(volume):
    """Bars since last 2x-SMA20 volume spike, capped 252."""
    m = volume.rolling(20, min_periods=20).mean()
    spike = (volume > 2.0 * m).astype(float).where(m.notna())
    return spike.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_spike_count_3x_sma50_120d_base_v031_signal(volume):
    """Count of bars where volume > 3 * SMA(volume,50) in trailing 120d."""
    m = volume.rolling(50, min_periods=50).mean()
    spike = (volume > 3.0 * m).astype(float).where(m.notna())
    return spike.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Bounded transforms ===================================================


def f27vr_f27_volume_regime_arctan_logv_diff_10d_base_v032_signal(volume):
    """arctan of (log(volume).diff(10) / 10d-std of that diff). Bounded regime velocity.
    Operates on DIFFS not levels, so decorrelated from level cluster."""
    lv = np.log(volume.replace(0.0, np.nan))
    d = lv.diff(10)
    sd = d.rolling(30, min_periods=30).std()
    return np.arctan(d / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_tanh_volvol_change_60d_base_v033_signal(volume):
    """tanh of (volvol_30 - volvol_120). Tanh of CV-change (change in regime stability)."""
    m30 = volume.rolling(30, min_periods=30).mean()
    s30 = volume.rolling(30, min_periods=30).std()
    cv30 = s30 / m30.replace(0.0, np.nan)
    m120 = volume.rolling(120, min_periods=120).mean()
    s120 = volume.rolling(120, min_periods=120).std()
    cv120 = s120 / m120.replace(0.0, np.nan)
    return np.tanh(cv30 - cv120).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sigmoid_rankcross_diff_base_v034_signal(volume):
    """Sigmoid of (rank21 - rank63) * 6. Bounded short-vs-mid disagreement.
    Operates on a difference of ranks, not on level, so decorrelated."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r63 = volume.rolling(63, min_periods=63).rank(pct=True)
    x = (r21 - r63) * 6.0
    return (1.0 / (1.0 + np.exp(-x.clip(-30.0, 30.0)))).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume regime =================================================


def f27vr_f27_volume_regime_dv_q4_bucket_252d_base_v035_signal(closeadj, volume):
    """Dollar-volume quartile (1..4) in trailing 252d window.
    KEPT as the only DV-level feature."""
    dv = closeadj * volume
    r = dv.rolling(252, min_periods=252).rank(pct=True)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    out[m] = np.ceil(r[m].clip(lower=1e-9) * 4.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dv_entry_event_top_d_base_v036_signal(closeadj, volume):
    """1 on bar dollar-volume enters top-decile (252d rank). Sparse DV event."""
    dv = closeadj * volume
    r = dv.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.9).astype(float).where(r.notna())
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_base_v037_signal(closeadj, volume):
    """log( mean(DV,42) / (mean(volume,42)*mean(closeadj,42)) ).  Captures DV-vs-price-vol
    decomposition asymmetry; orthogonal to single-bar level features."""
    dv_mean = (closeadj * volume).rolling(42, min_periods=42).mean()
    v_mean = volume.rolling(42, min_periods=42).mean()
    p_mean = closeadj.rolling(42, min_periods=42).mean()
    return np.log(dv_mean / (v_mean * p_mean).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dv_frac_high_60d_base_v038_signal(closeadj, volume):
    """Fraction of last 60 bars where dollar-volume was top-quartile of trailing 126d."""
    dv = closeadj * volume
    r = dv.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    return state.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Regime entry/exit timing =============================================


def f27vr_f27_volume_regime_dayssince_top_d_entry_252d_base_v039_signal(volume):
    """Bars since last entry into top-decile-volume regime (capped 252)."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.9).astype(float).where(r.notna())
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_base_v040_signal(volume):
    """Bars since last exit from bottom-decile-volume regime (capped 252)."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r <= 0.1).astype(float).where(r.notna())
    # exit event: state goes 1 -> 0
    exit_ = ((state <= 0.5) & (state.shift(1) > 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return exit_.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume-mean-by-regime (conditional) ==================================


def f27vr_f27_volume_regime_high_v_avg_diff_84d_base_v041_signal(volume):
    """Mean(volume | top-q regime, 84d) - Mean(volume | bottom-q regime, 84d), all over 84d.
    Standardized by 84d mean."""
    r = volume.rolling(84, min_periods=84).rank(pct=True)
    is_top = (r >= 0.75).astype(float).where(r.notna())
    is_bot = (r <= 0.25).astype(float).where(r.notna())
    vt = (volume * is_top).rolling(84, min_periods=84).sum()
    ct = is_top.rolling(84, min_periods=84).sum()
    vb = (volume * is_bot).rolling(84, min_periods=84).sum()
    cb = is_bot.rolling(84, min_periods=84).sum()
    mean_top = vt / ct.replace(0.0, np.nan)
    mean_bot = vb / cb.replace(0.0, np.nan)
    m = volume.rolling(84, min_periods=84).mean()
    return ((mean_top - mean_bot) / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Min/max regime score =================================================


def f27vr_f27_volume_regime_rank_consistency_3w_base_v042_signal(volume):
    """1 if rank21 > 0.5 AND rank63 > 0.5 AND rank252 > 0.5, -1 if all < 0.5, else 0.
    Trinary multi-horizon agreement; orthogonal to single rank features."""
    r1 = volume.rolling(21, min_periods=21).rank(pct=True)
    r2 = volume.rolling(63, min_periods=63).rank(pct=True)
    r3 = volume.rolling(252, min_periods=252).rank(pct=True)
    mask = r1.notna() & r2.notna() & r3.notna()
    high = ((r1 > 0.5) & (r2 > 0.5) & (r3 > 0.5)).astype(float)
    low = ((r1 < 0.5) & (r2 < 0.5) & (r3 < 0.5)).astype(float)
    return (high - low).where(mask).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_mean_abs_rank_jump_84d_base_v043_signal(volume):
    """Mean of |Δ pct-rank(252d)| in trailing 84d. Average bar-to-bar rank jitter."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    jump = (r - r.shift(1)).abs()
    return jump.rolling(84, min_periods=84).mean().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_range_rank_over_windows_base_v044_signal(volume):
    """Range (max-min) of pct-rank across {21,63,189} — multi-horizon regime SPREAD.
    A DIFFERENCE, not a level; decorrelated from level cluster."""
    r1 = volume.rolling(21, min_periods=21).rank(pct=True)
    r2 = volume.rolling(63, min_periods=63).rank(pct=True)
    r3 = volume.rolling(189, min_periods=189).rank(pct=True)
    mat = pd.concat([r1, r2, r3], axis=1)
    mask = r1.notna() & r2.notna() & r3.notna()
    return (mat.max(axis=1) - mat.min(axis=1)).where(mask).replace([np.inf, -np.inf], np.nan)


# === Volume regime "second moment" — vol-of-rank ==========================


def f27vr_f27_volume_regime_rank_std_60d_base_v045_signal(volume):
    """Std of pct-rank(volume,252) over trailing 60d. Volatility of regime placement.
    Not a level; measures regime turbulence."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    return r.rolling(60, min_periods=60).std().replace([np.inf, -np.inf], np.nan)


# === Volume Sharpe / consistency ==========================================


def f27vr_f27_volume_regime_vol_sharpe_42d_base_v046_signal(volume):
    """mean(volume, 42) / std(volume, 42). Volume "Sharpe" — regime consistency."""
    m = volume.rolling(42, min_periods=42).mean()
    s = volume.rolling(42, min_periods=42).std()
    return (m / s.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sign of regime expansion =============================================


def f27vr_f27_volume_regime_sign_expand_10_30_base_v047_signal(volume):
    """sign(SMA(volume,10) - SMA(volume,30)). Discrete short-term expansion sign."""
    s10 = volume.rolling(10, min_periods=10).mean()
    s30 = volume.rolling(30, min_periods=30).mean()
    return np.sign(s10 - s30).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_sign_expand_21_63_base_v048_signal(volume):
    """sign(SMA(volume,21) - SMA(volume,63))."""
    s21 = volume.rolling(21, min_periods=21).mean()
    s63 = volume.rolling(63, min_periods=63).mean()
    return np.sign(s21 - s63).replace([np.inf, -np.inf], np.nan)


# === Discrete state signals ===============================================


def f27vr_f27_volume_regime_high_state_z2_base_v049_signal(volume):
    """1 if log(volume) z-score over 60d > 2. Extreme-high binary state."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    out = (z > 2.0).astype(float).where(z.notna())
    return out.replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_low_state_zneg1_base_v050_signal(volume):
    """1 if log(volume) z-score over 60d < -1. Low-volume binary state."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    out = (z < -1.0).astype(float).where(z.notna())
    return out.replace([np.inf, -np.inf], np.nan)


# === Volume regime kurtosis / skew ========================================


def f27vr_f27_volume_regime_logv_skew_84d_base_v051_signal(volume):
    """84d rolling skew of log(volume). Regime asymmetry."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(84, min_periods=84).skew().replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_logv_kurt_126d_base_v052_signal(volume):
    """126d rolling kurtosis of log(volume). Regime tail thickness."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(126, min_periods=126).kurt().replace([np.inf, -np.inf], np.nan)


# === Regime dispersion ====================================================


def f27vr_f27_volume_regime_logv_iqr_84d_base_v053_signal(volume):
    """IQR of log(volume) over 84d, divided by median. Regime spread."""
    lv = np.log(volume.replace(0.0, np.nan))
    q75 = lv.rolling(84, min_periods=84).quantile(0.75)
    q25 = lv.rolling(84, min_periods=84).quantile(0.25)
    med = lv.rolling(84, min_periods=84).median().abs()
    return ((q75 - q25) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Regime transition density ============================================


def f27vr_f27_volume_regime_decile_change_rate_120d_base_v054_signal(volume):
    """Number of decile-label changes (252d rank decile) in trailing 120d, divided by 120."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    flip = (bucket != bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return (flip.rolling(120, min_periods=120).sum() / 120.0).replace([np.inf, -np.inf], np.nan)


# === Markov-like persistence: P(stay in high | currently high) ============


def f27vr_f27_volume_regime_markov_stay_high_252d_base_v055_signal(volume):
    """P(still in top-q at next bar | currently in top-q), estimated over trailing 252d.
    Persistence transition prob."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    is_high = state > 0.5
    next_high = state.shift(-1) > 0.5
    both = (is_high & next_high).astype(float).where(state.notna() & state.shift(-1).notna())
    cnt_high = is_high.astype(float).where(state.notna() & state.shift(-1).notna())
    num = both.rolling(252, min_periods=252).sum()
    den = cnt_high.rolling(252, min_periods=252).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "z" trimmed extreme indicators ================================


def f27vr_f27_volume_regime_count_z_extreme_252d_base_v056_signal(volume):
    """Count of bars where |z(logv,60)| > 1.5 in trailing 252d. Extremes density.
    A count, decorrelated from level features."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    ext = (z.abs() > 1.5).astype(float).where(z.notna())
    return ext.rolling(252, min_periods=252).sum().replace([np.inf, -np.inf], np.nan)


# === MAD-based regime score ===============================================


def f27vr_f27_volume_regime_v_over_mad_60d_base_v057_signal(volume):
    """(volume - median(volume,60)) / MAD(volume,60). Robust regime z-score."""
    med = volume.rolling(60, min_periods=60).median()
    dev = (volume - med).abs()
    mad = dev.rolling(60, min_periods=60).median()
    return ((volume - med) / mad.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Average duration of high-vol regime ==================================


def f27vr_f27_volume_regime_avg_high_run_length_252d_base_v058_signal(volume):
    """Average length of high-volume (top-q) runs ending in trailing 252d.
    Counts runs by summing consecutive '1' periods, divides by transition count."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    # number of bars in high-state
    cnt_in = state.rolling(252, min_periods=252).sum()
    # number of high-state entries (0->1) in trailing 252d
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    n_runs = entry.rolling(252, min_periods=252).sum()
    return (cnt_in / n_runs.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume Hurst-style persistence ratio =================================


def f27vr_f27_volume_regime_logv_persistence_acf1_84d_base_v059_signal(volume):
    """84d autocorr lag-1 of log(volume). Volume regime persistence measure."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _ac1(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=1))
    return lv.rolling(84, min_periods=84).apply(_ac1, raw=False).replace([np.inf, -np.inf], np.nan)


# === Regime composite "low" ===============================================


def f27vr_f27_volume_regime_count_low_state_runs_252d_base_v060_signal(volume):
    """Number of separate low-state ENTRY events (rank<=0.25, 126d) in trailing 252d.
    Counts how many times we entered low-vol regime."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r <= 0.25).astype(float).where(r.notna())
    entry = ((state > 0.5) & (state.shift(1) <= 0.5)).astype(float).where(state.notna() & state.shift(1).notna())
    return entry.rolling(252, min_periods=252).sum().replace([np.inf, -np.inf], np.nan)


# === Volume spike days-since at different threshold =======================


def f27vr_f27_volume_regime_dayssince_z_pos2_252d_base_v061_signal(volume):
    """Bars since last z(log v, 60d) > 2.0 event."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(60, min_periods=60).mean()
    s = lv.rolling(60, min_periods=60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    flag = (z > 2.0).astype(float).where(z.notna())
    return flag.rolling(252, min_periods=252).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Net regime score: top-q frac minus bot-q frac =========================


def f27vr_f27_volume_regime_entropy_quartiles_84d_base_v062_signal(volume):
    """Shannon entropy of quartile-bucket distribution over trailing 84d.
    Different aggregation than v072 (decile entropy 120d) — quartiles, 84d."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    def _ent(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        p = counts / counts.sum()
        p = p[p > 0]
        return float(-np.sum(p * np.log(p)))
    return bucket.rolling(84, min_periods=84).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "stickiness": frac-bar-with-same-quartile-as-yesterday =


def f27vr_f27_volume_regime_stickiness_q4_84d_base_v063_signal(volume):
    """Fraction of last 84 bars where quartile(volume,252) == quartile yesterday."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    same = (bucket == bucket.shift(1)).astype(float).where(bucket.notna() & bucket.shift(1).notna())
    return same.rolling(84, min_periods=84).mean().replace([np.inf, -np.inf], np.nan)


# === Volume tertile signal ================================================


def f27vr_f27_volume_regime_q3_bucket_42d_base_v064_signal(volume):
    """Volume tertile (1..3) in trailing 42d window."""
    r = volume.rolling(42, min_periods=42).rank(pct=True)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    m = r.notna()
    out[m] = np.ceil(r[m].clip(lower=1e-9) * 3.0)
    return out.replace([np.inf, -np.inf], np.nan)


# === DV days in high regime ===============================================


def f27vr_f27_volume_regime_dv_streak_high_q_120d_base_v065_signal(closeadj, volume):
    """Consecutive bars where dollar-volume is in top-quartile of trailing 126d, capped 120."""
    dv = closeadj * volume
    r = dv.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
    return state.rolling(120, min_periods=120).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Regime crossover: when 21d-rank crosses 252d-rank ====================


def f27vr_f27_volume_regime_rank_diff_21_189_base_v066_signal(volume):
    """rank(volume, 21) - rank(volume, 189). Short vs long regime rank differential."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r189 = volume.rolling(189, min_periods=189).rank(pct=True)
    return (r21 - r189).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_dayssince_rankcross_84d_base_v067_signal(volume):
    """Days since rank(volume,21) crossed rank(volume,189) (sign change of difference)."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r189 = volume.rolling(189, min_periods=189).rank(pct=True)
    d = r21 - r189
    s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return flip.rolling(84, min_periods=84).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "stretch" — current relative to short max ====================


def f27vr_f27_volume_regime_v_over_max60_base_v068_signal(volume):
    """log(volume / max(volume, 60)). How close to recent max (regime extremity)."""
    mx = volume.rolling(60, min_periods=60).max()
    return np.log(volume / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f27vr_f27_volume_regime_v_over_min30_base_v069_signal(volume):
    """log(volume / min(volume, 30)). Distance above recent min."""
    mn = volume.rolling(30, min_periods=30).min()
    return np.log(volume / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Quartile mean / std (volatility-of-regime) ===========================


def f27vr_f27_volume_regime_bucket_std_84d_base_v070_signal(volume):
    """Std of (quartile bucket, 252d) over last 84 bars. How variable the bucket is."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 4.0)
    return bucket.rolling(84, min_periods=84).std().replace([np.inf, -np.inf], np.nan)


# === Indicator: simultaneous high in short AND long rank =================


def f27vr_f27_volume_regime_xor_short_long_state_base_v071_signal(volume):
    """1 if (rank21 >= 0.75) XOR (rank252 >= 0.75). Disagreement state (one but not both)."""
    r21 = volume.rolling(21, min_periods=21).rank(pct=True)
    r252 = volume.rolling(252, min_periods=252).rank(pct=True)
    a = (r21 >= 0.75).astype(float)
    b = (r252 >= 0.75).astype(float)
    out = (a + b - 2.0 * a * b).where(r21.notna() & r252.notna())
    return out.replace([np.inf, -np.inf], np.nan)


# === Volume regime entropy ================================================


def f27vr_f27_volume_regime_decile_entropy_120d_base_v072_signal(volume):
    """Shannon entropy of decile distribution in trailing 120d window."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    bucket = pd.Series(np.nan, index=volume.index, dtype=float)
    mb = r.notna()
    bucket[mb] = np.ceil(r[mb].clip(lower=1e-9) * 10.0)
    def _ent(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        p = counts / counts.sum()
        p = p[p > 0]
        return float(-np.sum(p * np.log(p)))
    return bucket.rolling(120, min_periods=120).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "regime velocity" — rate of change of pct rank =================


def f27vr_f27_volume_regime_max_streak_high_q_252d_base_v073_signal(volume):
    """Maximum continuous high-q (rank>=0.75) streak length in trailing 252d.
    Captures longest run; orthogonal to velocity features."""
    r = volume.rolling(126, min_periods=126).rank(pct=True)
    state = (r >= 0.75).astype(float).where(r.notna())
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
    return state.rolling(252, min_periods=252).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume regime "headroom": (1 - rank). Distance to top regime =========


def f27vr_f27_volume_regime_mean_rank_change_signed_84d_base_v074_signal(volume):
    """Mean of (rank252 - rank252.shift(1)) over 84d. Signed mean of rank changes;
    captures regime drift direction; orthogonal to level."""
    r = volume.rolling(252, min_periods=252).rank(pct=True)
    return (r - r.shift(1)).rolling(84, min_periods=84).mean().replace([np.inf, -np.inf], np.nan)


# === Coefficient of regime variation across windows =======================


def f27vr_f27_volume_regime_cv_rank_across_windows_base_v075_signal(volume):
    """std/mean of pct-ranks across windows {21,63,126,252}. Regime divergence across horizons."""
    r1 = volume.rolling(21, min_periods=21).rank(pct=True)
    r2 = volume.rolling(63, min_periods=63).rank(pct=True)
    r3 = volume.rolling(126, min_periods=126).rank(pct=True)
    r4 = volume.rolling(252, min_periods=252).rank(pct=True)
    mat = pd.concat([r1, r2, r3, r4], axis=1)
    mask = r1.notna() & r2.notna() & r3.notna() & r4.notna()
    return (mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).where(mask).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f27_volume_regime_base_001_075_REGISTRY = {
    "f27vr_f27_volume_regime_q4_bucket_42d_base_v001_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_42d_base_v001_signal},
    "f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_base_v002_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_base_v002_signal},
    "f27vr_f27_volume_regime_count_decile_jumps_120d_base_v003_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_decile_jumps_120d_base_v003_signal},
    "f27vr_f27_volume_regime_dispersion_buckets_21d_base_v004_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dispersion_buckets_21d_base_v004_signal},
    "f27vr_f27_volume_regime_entry_event_top_d_base_v005_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_entry_event_top_d_base_v005_signal},
    "f27vr_f27_volume_regime_exit_event_top_q_base_v006_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_exit_event_top_q_base_v006_signal},
    "f27vr_f27_volume_regime_any_state_flip_q4_base_v007_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_any_state_flip_q4_base_v007_signal},
    "f27vr_f27_volume_regime_streak_below_med_120d_base_v008_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_below_med_120d_base_v008_signal},
    "f27vr_f27_volume_regime_multi_top_q_agree_base_v009_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_multi_top_q_agree_base_v009_signal},
    "f27vr_f27_volume_regime_multi_bot_q_agree_base_v010_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_multi_bot_q_agree_base_v010_signal},
    "f27vr_f27_volume_regime_v_over_median_21d_base_v011_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_median_21d_base_v011_signal},
    "f27vr_f27_volume_regime_q4_bucket_diff_short_long_base_v012_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_diff_short_long_base_v012_signal},
    "f27vr_f27_volume_regime_logv_diff_5d_base_v013_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_diff_5d_base_v013_signal},
    "f27vr_f27_volume_regime_lag_v_corr_30d_base_v014_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_lag_v_corr_30d_base_v014_signal},
    "f27vr_f27_volume_regime_pct_rank_189d_base_v015_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_rank_189d_base_v015_signal},
    "f27vr_f27_volume_regime_dayssince_top_q_change_252d_base_v016_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_top_q_change_252d_base_v016_signal},
    "f27vr_f27_volume_regime_dayssince_bot_q_change_252d_base_v017_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_bot_q_change_252d_base_v017_signal},
    "f27vr_f27_volume_regime_change_count_q4_120d_base_v018_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_change_count_q4_120d_base_v018_signal},
    "f27vr_f27_volume_regime_change_count_top_state_252d_base_v019_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_change_count_top_state_252d_base_v019_signal},
    "f27vr_f27_volume_regime_frac_top_q_120d_base_v020_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_top_q_120d_base_v020_signal},
    "f27vr_f27_volume_regime_frac_bot_q_63d_base_v021_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_bot_q_63d_base_v021_signal},
    "f27vr_f27_volume_regime_streak_top_q_120d_base_v022_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_top_q_120d_base_v022_signal},
    "f27vr_f27_volume_regime_streak_bot_d_180d_base_v023_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_bot_d_180d_base_v023_signal},
    "f27vr_f27_volume_regime_expand_10_60_base_v024_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_10_60_base_v024_signal},
    "f27vr_f27_volume_regime_expand_21_126_base_v025_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_21_126_base_v025_signal},
    "f27vr_f27_volume_regime_expand_5_42_base_v026_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_5_42_base_v026_signal},
    "f27vr_f27_volume_regime_volvol_30d_base_v027_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_30d_base_v027_signal},
    "f27vr_f27_volume_regime_volvol_120d_base_v028_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_120d_base_v028_signal},
    "f27vr_f27_volume_regime_spike2x_sma20_base_v029_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike2x_sma20_base_v029_signal},
    "f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_base_v030_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_base_v030_signal},
    "f27vr_f27_volume_regime_spike_count_3x_sma50_120d_base_v031_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike_count_3x_sma50_120d_base_v031_signal},
    "f27vr_f27_volume_regime_arctan_logv_diff_10d_base_v032_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_arctan_logv_diff_10d_base_v032_signal},
    "f27vr_f27_volume_regime_tanh_volvol_change_60d_base_v033_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_tanh_volvol_change_60d_base_v033_signal},
    "f27vr_f27_volume_regime_sigmoid_rankcross_diff_base_v034_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sigmoid_rankcross_diff_base_v034_signal},
    "f27vr_f27_volume_regime_dv_q4_bucket_252d_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_q4_bucket_252d_base_v035_signal},
    "f27vr_f27_volume_regime_dv_entry_event_top_d_base_v036_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_entry_event_top_d_base_v036_signal},
    "f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_base_v037_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_base_v037_signal},
    "f27vr_f27_volume_regime_dv_frac_high_60d_base_v038_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_frac_high_60d_base_v038_signal},
    "f27vr_f27_volume_regime_dayssince_top_d_entry_252d_base_v039_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_top_d_entry_252d_base_v039_signal},
    "f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_base_v040_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_base_v040_signal},
    "f27vr_f27_volume_regime_high_v_avg_diff_84d_base_v041_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_high_v_avg_diff_84d_base_v041_signal},
    "f27vr_f27_volume_regime_rank_consistency_3w_base_v042_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_consistency_3w_base_v042_signal},
    "f27vr_f27_volume_regime_mean_abs_rank_jump_84d_base_v043_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_abs_rank_jump_84d_base_v043_signal},
    "f27vr_f27_volume_regime_range_rank_over_windows_base_v044_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_range_rank_over_windows_base_v044_signal},
    "f27vr_f27_volume_regime_rank_std_60d_base_v045_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_std_60d_base_v045_signal},
    "f27vr_f27_volume_regime_vol_sharpe_42d_base_v046_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_vol_sharpe_42d_base_v046_signal},
    "f27vr_f27_volume_regime_sign_expand_10_30_base_v047_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_expand_10_30_base_v047_signal},
    "f27vr_f27_volume_regime_sign_expand_21_63_base_v048_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_expand_21_63_base_v048_signal},
    "f27vr_f27_volume_regime_high_state_z2_base_v049_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_high_state_z2_base_v049_signal},
    "f27vr_f27_volume_regime_low_state_zneg1_base_v050_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_low_state_zneg1_base_v050_signal},
    "f27vr_f27_volume_regime_logv_skew_84d_base_v051_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_skew_84d_base_v051_signal},
    "f27vr_f27_volume_regime_logv_kurt_126d_base_v052_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_kurt_126d_base_v052_signal},
    "f27vr_f27_volume_regime_logv_iqr_84d_base_v053_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_iqr_84d_base_v053_signal},
    "f27vr_f27_volume_regime_decile_change_rate_120d_base_v054_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_decile_change_rate_120d_base_v054_signal},
    "f27vr_f27_volume_regime_markov_stay_high_252d_base_v055_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_markov_stay_high_252d_base_v055_signal},
    "f27vr_f27_volume_regime_count_z_extreme_252d_base_v056_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_z_extreme_252d_base_v056_signal},
    "f27vr_f27_volume_regime_v_over_mad_60d_base_v057_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_mad_60d_base_v057_signal},
    "f27vr_f27_volume_regime_avg_high_run_length_252d_base_v058_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_avg_high_run_length_252d_base_v058_signal},
    "f27vr_f27_volume_regime_logv_persistence_acf1_84d_base_v059_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_persistence_acf1_84d_base_v059_signal},
    "f27vr_f27_volume_regime_count_low_state_runs_252d_base_v060_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_low_state_runs_252d_base_v060_signal},
    "f27vr_f27_volume_regime_dayssince_z_pos2_252d_base_v061_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_z_pos2_252d_base_v061_signal},
    "f27vr_f27_volume_regime_entropy_quartiles_84d_base_v062_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_entropy_quartiles_84d_base_v062_signal},
    "f27vr_f27_volume_regime_stickiness_q4_84d_base_v063_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_stickiness_q4_84d_base_v063_signal},
    "f27vr_f27_volume_regime_q3_bucket_42d_base_v064_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q3_bucket_42d_base_v064_signal},
    "f27vr_f27_volume_regime_dv_streak_high_q_120d_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_streak_high_q_120d_base_v065_signal},
    "f27vr_f27_volume_regime_rank_diff_21_189_base_v066_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_diff_21_189_base_v066_signal},
    "f27vr_f27_volume_regime_dayssince_rankcross_84d_base_v067_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_rankcross_84d_base_v067_signal},
    "f27vr_f27_volume_regime_v_over_max60_base_v068_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_max60_base_v068_signal},
    "f27vr_f27_volume_regime_v_over_min30_base_v069_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_min30_base_v069_signal},
    "f27vr_f27_volume_regime_bucket_std_84d_base_v070_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_std_84d_base_v070_signal},
    "f27vr_f27_volume_regime_xor_short_long_state_base_v071_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_xor_short_long_state_base_v071_signal},
    "f27vr_f27_volume_regime_decile_entropy_120d_base_v072_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_decile_entropy_120d_base_v072_signal},
    "f27vr_f27_volume_regime_max_streak_high_q_252d_base_v073_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_max_streak_high_q_252d_base_v073_signal},
    "f27vr_f27_volume_regime_mean_rank_change_signed_84d_base_v074_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_rank_change_signed_84d_base_v074_signal},
    "f27vr_f27_volume_regime_cv_rank_across_windows_base_v075_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_cv_rank_across_windows_base_v075_signal},
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
    for name, entry in f27_volume_regime_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
