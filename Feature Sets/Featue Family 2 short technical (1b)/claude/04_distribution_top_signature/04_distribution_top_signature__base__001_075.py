"""04_distribution_top_signature — base features 001-075.

Pipeline 1b-technical. SEP-only inputs (open, high, low, close, volume).
Focus: POST-PEAK distribution DYNAMICS — Wyckoff phase classification,
distribution-day intensity by stage, recovery probability proxies, failed-
recovery (dead-cat-bounce), time-to-confirmation, breakdown follow-through
deceleration, range contraction within rolling top.

Differentiator from 1a `drts` (38_distribution_rolling_top_signature):
focus on PROCESS DYNAMICS (stage-by-stage, recovery-failure, Wyckoff
phases A-E) rather than instantaneous top-dwell or classical chart
patterns.

PIT-clean: right-anchored rolling, explicit min_periods, no shift(-N).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# ----------------------------- constants -------------------------------
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260

# ----------------------------- helpers ---------------------------------
def _safe_log(s: pd.Series) -> pd.Series:
    s = pd.Series(s, dtype="float64")
    return np.log(s.where(s > 0))


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    num = pd.Series(num, dtype="float64")
    den = pd.Series(den, dtype="float64")
    out = num / den.where(den != 0)
    return out.replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
    if min_periods is None:
        min_periods = max(n // 3, 5)
    m = s.rolling(n, min_periods=min_periods).mean()
    sd = s.rolling(n, min_periods=min_periods).std(ddof=0)
    return _safe_div(s - m, sd)


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    tr = pd.concat(
        [(high - low).rename("hl"),
         (high - pc).abs().rename("hpc"),
         (low - pc).abs().rename("lpc")],
        axis=1,
    ).max(axis=1)
    return tr


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    tr = _true_range(high, low, close)
    return tr.rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan

    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _is_dday(close: pd.Series, volume: pd.Series) -> pd.Series:
    """IBD-style distribution day: close down >=0.2% on volume > prior-day vol."""
    ret = close.pct_change()
    vol_up = volume > volume.shift(1)
    return ((ret <= -0.002) & vol_up).astype(float)


def _is_heavy_dday(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Heavy distribution: close down >1% on vol > 1.5x 50d avg."""
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    return ((ret <= -0.01) & (volume > 1.5 * vavg)).astype(float)


def _is_stealth_dday(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stealth distribution: close down <0.5% but vol > 1.5x 50d avg."""
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    return ((ret < 0) & (ret > -0.005) & (volume > 1.5 * vavg)).astype(float)


def _is_pivot_high(high: pd.Series, k: int = 3) -> pd.Series:
    """Past-only pivot detection: bar at index t-k was the local max over t-2k..t.
    Returned series is aligned to the END of the window (current bar)."""
    n = 2 * k + 1
    w = high.rolling(n, min_periods=n)
    center = high.shift(k)
    is_max = (w.max() == center)
    return is_max.fillna(False).astype(float)


def _is_pivot_low(low: pd.Series, k: int = 3) -> pd.Series:
    n = 2 * k + 1
    w = low.rolling(n, min_periods=n)
    center = low.shift(k)
    is_min = (w.min() == center)
    return is_min.fillna(False).astype(float)


def _is_252d_high(high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=63).max()
    return (high >= rmax * 0.9999).astype(float)


# =====================================================================
#  GROUP A — LOWER-HIGH SEQUENCE FORMATION (001-012)
# =====================================================================

def _lh_events(high: pd.Series, k: int = 3) -> pd.Series:
    """Series of 1.0 at confirmed lower-high pivot events (aligned at t,
    referring to pivot at t-k). A lower-high event = pivot-high whose
    centered value < previous pivot-high centered value."""
    piv = _is_pivot_high(high, k=k)
    centered_high = high.shift(k)
    piv_h = centered_high.where(piv == 1.0)
    prev_piv_h = piv_h.ffill().shift(1)
    lh = ((piv == 1.0) & (piv_h < prev_piv_h)).astype(float)
    return lh


def f04_dtsg_001_lh_count_post_first_252d_high_21d(high: pd.Series) -> pd.Series:
    """Lower-high event count in last 21d, gated to fire only AFTER first
    252d-high has occurred at some point in the prior 252d window."""
    lh = _lh_events(high)
    cnt = lh.rolling(MDAYS, min_periods=5).sum()
    is_high = _is_252d_high(high)
    seen_high = is_high.rolling(YDAYS, min_periods=21).max()
    return cnt.where(seen_high == 1.0, np.nan)


def f04_dtsg_002_lh_count_post_first_252d_high_63d(high: pd.Series) -> pd.Series:
    """Lower-high event count in last 63d, gated on prior 252d-high having occurred."""
    lh = _lh_events(high)
    cnt = lh.rolling(QDAYS, min_periods=15).sum()
    is_high = _is_252d_high(high)
    seen_high = is_high.rolling(YDAYS, min_periods=21).max()
    return cnt.where(seen_high == 1.0, np.nan)


def f04_dtsg_003_lh_count_post_first_252d_high_126d(high: pd.Series) -> pd.Series:
    """Lower-high event count in last 126d, gated on prior 252d-high having occurred."""
    lh = _lh_events(high)
    cnt = lh.rolling(126, min_periods=30).sum()
    is_high = _is_252d_high(high)
    seen_high = is_high.rolling(YDAYS, min_periods=21).max()
    return cnt.where(seen_high == 1.0, np.nan)


def f04_dtsg_004_lh_count_post_first_252d_high_252d(high: pd.Series) -> pd.Series:
    """Lower-high event count in last 252d, gated on prior 252d-high having occurred."""
    lh = _lh_events(high)
    cnt = lh.rolling(YDAYS, min_periods=60).sum()
    is_high = _is_252d_high(high)
    seen_high = is_high.rolling(YDAYS, min_periods=21).max()
    return cnt.where(seen_high == 1.0, np.nan)


def f04_dtsg_005_lh_rank_first_event_post_peak_126d(high: pd.Series) -> pd.Series:
    """Days-since-1st-lower-high event in last 126d (= recency of the 1st LH
    after the most recent 252d high). NaN before any LH after peak."""
    lh = _lh_events(high)
    is_peak = _is_252d_high(high)
    # bars since most recent peak inside 126d window
    n = 126
    h_arr = high.values
    peak_arr = is_peak.values
    lh_arr = lh.values
    out = np.full(len(h_arr), np.nan)
    for i in range(n - 1, len(h_arr)):
        win_peak = peak_arr[i - n + 1 : i + 1]
        win_lh = lh_arr[i - n + 1 : i + 1]
        peak_idx = np.where(win_peak == 1.0)[0]
        if peak_idx.size == 0:
            continue
        last_peak = peak_idx[-1]
        lh_after = np.where(win_lh[last_peak + 1 :] == 1.0)[0]
        if lh_after.size == 0:
            continue
        # days-since 1st LH after peak (from current bar's perspective)
        first_lh_local = last_peak + 1 + lh_after[0]
        out[i] = float(n - 1 - first_lh_local)
    return pd.Series(out, index=high.index)


def f04_dtsg_006_lh_rank_second_event_post_peak_126d(high: pd.Series) -> pd.Series:
    """Days-since-2nd-lower-high event in last 126d after most recent peak."""
    lh = _lh_events(high)
    is_peak = _is_252d_high(high)
    n = 126
    h_arr = high.values
    peak_arr = is_peak.values
    lh_arr = lh.values
    out = np.full(len(h_arr), np.nan)
    for i in range(n - 1, len(h_arr)):
        win_peak = peak_arr[i - n + 1 : i + 1]
        win_lh = lh_arr[i - n + 1 : i + 1]
        peak_idx = np.where(win_peak == 1.0)[0]
        if peak_idx.size == 0:
            continue
        last_peak = peak_idx[-1]
        lh_after = np.where(win_lh[last_peak + 1 :] == 1.0)[0]
        if lh_after.size < 2:
            continue
        snd_local = last_peak + 1 + lh_after[1]
        out[i] = float(n - 1 - snd_local)
    return pd.Series(out, index=high.index)


def f04_dtsg_007_lh_rank_third_event_post_peak_126d(high: pd.Series) -> pd.Series:
    """Days-since-3rd-lower-high event in last 126d after most recent peak."""
    lh = _lh_events(high)
    is_peak = _is_252d_high(high)
    n = 126
    h_arr = high.values
    peak_arr = is_peak.values
    lh_arr = lh.values
    out = np.full(len(h_arr), np.nan)
    for i in range(n - 1, len(h_arr)):
        win_peak = peak_arr[i - n + 1 : i + 1]
        win_lh = lh_arr[i - n + 1 : i + 1]
        peak_idx = np.where(win_peak == 1.0)[0]
        if peak_idx.size == 0:
            continue
        last_peak = peak_idx[-1]
        lh_after = np.where(win_lh[last_peak + 1 :] == 1.0)[0]
        if lh_after.size < 3:
            continue
        thd_local = last_peak + 1 + lh_after[2]
        out[i] = float(n - 1 - thd_local)
    return pd.Series(out, index=high.index)


def f04_dtsg_008_lh_mean_amplitude_vs_peak_126d(high: pd.Series) -> pd.Series:
    """Mean amplitude (drawdown from peak) of confirmed lower-high pivots
    within the last 126d, expressed as a log fraction below the rolling peak."""
    lh = _lh_events(high)
    centered = high.shift(3)
    peak126 = high.rolling(126, min_periods=30).max()
    lh_h = centered.where(lh == 1.0)
    lh_logdist = (_safe_log(lh_h) - _safe_log(peak126))
    return lh_logdist.rolling(126, min_periods=10).mean()


def f04_dtsg_009_lh_volume_profile_zscore_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on lower-high pivot days vs 63d avg vol, expressed as z-score."""
    lh = _lh_events(high)
    vol_lh = volume.where(lh == 1.0)
    avg_lh = vol_lh.rolling(QDAYS, min_periods=5).mean()
    avg_all = volume.rolling(QDAYS, min_periods=10).mean()
    sd_all = volume.rolling(QDAYS, min_periods=10).std(ddof=0)
    return _safe_div(avg_lh - avg_all, sd_all)


def f04_dtsg_010_lh_inter_event_mean_days_126d(high: pd.Series) -> pd.Series:
    """Mean spacing (days) between consecutive lower-high events in last 126d."""
    lh = _lh_events(high).values
    n = 126
    out = np.full(len(lh), np.nan)
    for i in range(n - 1, len(lh)):
        idx = np.where(lh[i - n + 1 : i + 1] == 1.0)[0]
        if idx.size < 2:
            continue
        out[i] = float(np.diff(idx).mean())
    return pd.Series(out, index=high.index)


def f04_dtsg_011_lh_inter_event_cv_126d(high: pd.Series) -> pd.Series:
    """Coefficient of variation of lower-high event spacing in last 126d."""
    lh = _lh_events(high).values
    n = 126
    out = np.full(len(lh), np.nan)
    for i in range(n - 1, len(lh)):
        idx = np.where(lh[i - n + 1 : i + 1] == 1.0)[0]
        if idx.size < 3:
            continue
        d = np.diff(idx).astype(float)
        m = d.mean()
        if m <= 0:
            continue
        out[i] = float(d.std(ddof=0) / m)
    return pd.Series(out, index=high.index)


def f04_dtsg_012_lh_cadence_acceleration_126d(high: pd.Series) -> pd.Series:
    """Lower-high cadence acceleration: difference between mean spacing in
    early-half (first 63d) and late-half (last 63d) of a 126d window. Positive
    = LHs forming faster (distribution tightening)."""
    lh = _lh_events(high).values
    n = 126
    h = n // 2
    out = np.full(len(lh), np.nan)
    for i in range(n - 1, len(lh)):
        a = lh[i - n + 1 : i - h + 1]
        b = lh[i - h + 1 : i + 1]
        ia = np.where(a == 1.0)[0]
        ib = np.where(b == 1.0)[0]
        if ia.size < 2 or ib.size < 2:
            continue
        out[i] = float(np.diff(ia).mean() - np.diff(ib).mean())
    return pd.Series(out, index=high.index)


# =====================================================================
#  GROUP B — DISTRIBUTION-DAY INTENSITY BY STAGE (013-024)
# =====================================================================

def _bars_since_peak(high: pd.Series, lookback: int = 252) -> pd.Series:
    """Bars since the most recent 252d high within a lookback window. NaN if
    no peak in the window."""
    is_peak = _is_252d_high(high).values
    n = lookback
    out = np.full(len(is_peak), np.nan)
    for i in range(n - 1, len(is_peak)):
        idx = np.where(is_peak[i - n + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        out[i] = float(n - 1 - idx[-1])
    return pd.Series(out, index=high.index)


def f04_dtsg_013_dday_pre_peak_count_60d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days in the 60d window ENDING at the most recent
    252d peak (i.e. pre-peak distribution leading INTO the high)."""
    is_peak = _is_252d_high(high).values
    dd = _is_dday(close, volume).values
    out = np.full(len(dd), np.nan)
    n_lookback = 252
    for i in range(n_lookback, len(dd)):
        # find most recent peak within lookback
        idx = np.where(is_peak[i - n_lookback + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n_lookback + 1 + idx[-1]
        a = max(0, peak_pos - 60 + 1)
        b = peak_pos + 1
        out[i] = float(np.nansum(dd[a:b]))
    return pd.Series(out, index=close.index)


def f04_dtsg_014_dday_at_peak_count_10d_window(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days within +/- 5d window around the most recent
    252d peak. Captures churning at the high."""
    is_peak = _is_252d_high(high).values
    dd = _is_dday(close, volume).values
    out = np.full(len(dd), np.nan)
    n_lookback = 252
    for i in range(n_lookback, len(dd)):
        idx = np.where(is_peak[i - n_lookback + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n_lookback + 1 + idx[-1]
        a = max(0, peak_pos - 5)
        b = min(len(dd), peak_pos + 6)
        # only count bars actually <= current i
        b = min(b, i + 1)
        out[i] = float(np.nansum(dd[a:b]))
    return pd.Series(out, index=close.index)


def f04_dtsg_015_dday_post_peak_count_60d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-days in the 60d window AFTER the most recent
    252d peak (capped at current bar)."""
    is_peak = _is_252d_high(high).values
    dd = _is_dday(close, volume).values
    out = np.full(len(dd), np.nan)
    n_lookback = 252
    for i in range(n_lookback, len(dd)):
        idx = np.where(is_peak[i - n_lookback + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n_lookback + 1 + idx[-1]
        a = peak_pos + 1
        b = min(len(dd), peak_pos + 1 + 60, i + 1)
        if a >= b:
            out[i] = 0.0
        else:
            out[i] = float(np.nansum(dd[a:b]))
    return pd.Series(out, index=close.index)


def _dday_stage_intensity(close: pd.Series, volume: pd.Series, high: pd.Series,
                          stage_start: int, stage_end: int) -> pd.Series:
    """Distribution-day intensity = D-day count / total bars in the [stage_start,
    stage_end) window measured in bars-post-peak. Window is anchored at the
    most recent 252d peak; only bars <= current i are counted."""
    is_peak = _is_252d_high(high).values
    dd = _is_dday(close, volume).values
    out = np.full(len(dd), np.nan)
    n_lookback = 252
    for i in range(n_lookback, len(dd)):
        idx = np.where(is_peak[i - n_lookback + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n_lookback + 1 + idx[-1]
        a = peak_pos + 1 + stage_start
        b = min(len(dd), peak_pos + 1 + stage_end, i + 1)
        if a >= b:
            continue
        seg = dd[a:b]
        if seg.size == 0:
            continue
        out[i] = float(np.nansum(seg) / seg.size)
    return pd.Series(out, index=close.index)


def f04_dtsg_016_dday_stage1_intensity_post_peak_21d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stage-1 (0-21d post-peak) distribution-day intensity (count / window length)."""
    return _dday_stage_intensity(close, volume, high, 0, 21)


def f04_dtsg_017_dday_stage2_intensity_post_peak_21_42d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stage-2 (21-42d post-peak) distribution-day intensity."""
    return _dday_stage_intensity(close, volume, high, 21, 42)


def f04_dtsg_018_dday_stage3_intensity_post_peak_42_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stage-3 (42-63d post-peak) distribution-day intensity."""
    return _dday_stage_intensity(close, volume, high, 42, 63)


def f04_dtsg_019_dday_acceleration_stage1_to_stage2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-day acceleration = stage-2 intensity minus stage-1 intensity."""
    s1 = _dday_stage_intensity(close, volume, high, 0, 21)
    s2 = _dday_stage_intensity(close, volume, high, 21, 42)
    return s2 - s1


def f04_dtsg_020_dday_cluster_density_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cluster density: max number of D-days within any 5d sub-window inside the
    most recent 42d window (peak local concentration of selling)."""
    dd = _is_dday(close, volume)
    rolled5 = dd.rolling(5, min_periods=1).sum()
    return rolled5.rolling(42, min_periods=10).max()


def f04_dtsg_021_heavy_dday_count_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Heavy distribution day count (close down >1% on vol > 1.5x 50d avg) in 42d."""
    return _is_heavy_dday(close, volume).rolling(42, min_periods=10).sum()


def f04_dtsg_022_stealth_dday_count_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stealth distribution count (small price loss on heavy volume) in 42d."""
    return _is_stealth_dday(close, volume).rolling(42, min_periods=10).sum()


def f04_dtsg_023_dday_breadth_multi_horizon_alignment(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-horizon alignment: how many of {21d, 42d, 63d} D-day counts are
    elevated (above their own 252d median). Range 0-3."""
    dd = _is_dday(close, volume)
    c21 = dd.rolling(21, min_periods=5).sum()
    c42 = dd.rolling(42, min_periods=10).sum()
    c63 = dd.rolling(63, min_periods=15).sum()
    m21 = c21.rolling(YDAYS, min_periods=63).median()
    m42 = c42.rolling(YDAYS, min_periods=63).median()
    m63 = c63.rolling(YDAYS, min_periods=63).median()
    out = (c21 > m21).astype(float) + (c42 > m42).astype(float) + (c63 > m63).astype(float)
    # Mask warmup
    valid = c63.notna()
    return out.where(valid, np.nan)


def f04_dtsg_024_dday_then_failed_recovery_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of D-days within last 63d that were FOLLOWED in the next 5 bars by
    a failed recovery attempt — defined as: max close in next 5 bars > D-day
    close but does NOT exceed D-day high (i.e. bounce, but not a real recovery)."""
    dd = _is_dday(close, volume).values
    cl = close.values
    n = 63
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0.0
        for j in range(i - n + 1, i + 1):
            if dd[j] != 1.0:
                continue
            kmax = min(len(cl), j + 6)
            if j + 1 >= kmax:
                continue
            fwd = cl[j + 1 : kmax]
            # bounce above close but stays below close of D-day + small buffer
            # use close-only proxy: max close in next 5 < D-day close (failed)
            if fwd.max() < cl[j]:
                cnt += 1
        out[i] = cnt
    return pd.Series(out, index=close.index)


# =====================================================================
#  GROUP C — VOLUME-WEIGHTED DISTRIBUTION MEASURES (025-036)
# =====================================================================

def f04_dtsg_025_vw_close_position_in_bar_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted close-position-in-bar (0 = at low, 1 = at high) over 21d.
    Low value = supply pushing closes down on volume."""
    pos = _safe_div(close - low, high - low)
    num = (pos * volume).rolling(MDAYS, min_periods=5).sum()
    den = volume.rolling(MDAYS, min_periods=5).sum()
    return _safe_div(num, den)


def f04_dtsg_026_dollar_vw_lower_high_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar-volume on lower-high pivot days in last 63d, normalized by
    63d avg dollar-volume. Heavy dollars on rejected highs = distribution."""
    lh = _lh_events(high)
    dv = close * volume
    lh_dv = dv.where(lh == 1.0).rolling(QDAYS, min_periods=10).sum()
    avg_dv = dv.rolling(QDAYS, min_periods=10).mean()
    return _safe_div(lh_dv, avg_dv * QDAYS)


def f04_dtsg_027_dist_to_accum_volume_ratio_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of D-day volume aggregate to accumulation-day volume aggregate in
    42d. Accumulation = close up >=0.2% on rising volume. Above 1 = distribution."""
    ret = close.pct_change()
    vol_up = volume > volume.shift(1)
    dd = (ret <= -0.002) & vol_up
    ad = (ret >= 0.002) & vol_up
    d_vol = volume.where(dd).rolling(42, min_periods=10).sum()
    a_vol = volume.where(ad).rolling(42, min_periods=10).sum()
    return _safe_div(d_vol, a_vol)


def f04_dtsg_028_volume_profile_skew_21d(volume: pd.Series) -> pd.Series:
    """Skewness of the 21d volume distribution. Positive skew = a few heavy
    bars dominate (climactic); negative = uniform high vol."""
    def _skew(w):
        v = w[~np.isnan(w)]
        if v.size < 5 or v.std(ddof=0) == 0:
            return np.nan
        return float(((v - v.mean()) ** 3).mean() / (v.std(ddof=0) ** 3))
    return volume.rolling(MDAYS, min_periods=5).apply(_skew, raw=True)


def f04_dtsg_029_heavy_down_day_volume_aggregate_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate volume on heavy-down (close <= -1%) days in 42d, normalized by
    42d total volume."""
    ret = close.pct_change()
    heavy = ret <= -0.01
    h_vol = volume.where(heavy, 0.0).rolling(42, min_periods=10).sum()
    t_vol = volume.rolling(42, min_periods=10).sum()
    return _safe_div(h_vol, t_vol)


def f04_dtsg_030_light_up_day_volume_aggregate_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate volume on light-up (0 < close <= +0.5%) days in 42d, normalized
    by 42d total. Up-bars without volume support = weak demand."""
    ret = close.pct_change()
    light = (ret > 0) & (ret <= 0.005)
    l_vol = volume.where(light, 0.0).rolling(42, min_periods=10).sum()
    t_vol = volume.rolling(42, min_periods=10).sum()
    return _safe_div(l_vol, t_vol)


def f04_dtsg_031_volume_zscore_on_lh_days_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (over 63d) of volume on confirmed lower-high pivot bars. Avg of
    lh-day z-scores within last 63d."""
    lh = _lh_events(high)
    z = _rolling_zscore(volume, QDAYS)
    lh_z = z.where(lh == 1.0)
    return lh_z.rolling(QDAYS, min_periods=5).mean()


def f04_dtsg_032_volume_divergence_on_retests_42d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume divergence on retests: when current bar is within 1% of the 21d
    rolling max but volume < 0.8x 21d avg, count as divergent retest. Sum/42d."""
    rmax21 = high.rolling(MDAYS, min_periods=5).max()
    near_top = (high >= rmax21 * 0.99)
    vavg = volume.rolling(MDAYS, min_periods=5).mean()
    weak_vol = volume < 0.8 * vavg
    return (near_top & weak_vol).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_033_cumulative_net_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative net volume = sum(down-bar vol) - sum(up-bar vol) over 21d,
    normalized by 21d total volume. Positive = supply dominates."""
    ret = close.pct_change()
    sign = np.where(ret > 0, -1.0, np.where(ret < 0, 1.0, 0.0))
    signed = pd.Series(sign, index=close.index) * volume
    num = signed.rolling(MDAYS, min_periods=5).sum()
    den = volume.rolling(MDAYS, min_periods=5).sum()
    return _safe_div(num, den)


def f04_dtsg_034_up_to_down_volume_ratio_decay_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-to-down volume ratio decay: ratio in early-half minus late-half of
    42d window. Positive = ratio shrinking (demand fading)."""
    ret = close.pct_change()
    uv = volume.where(ret > 0, 0.0)
    dv = volume.where(ret < 0, 0.0)
    early_u = uv.rolling(21, min_periods=5).sum().shift(21)
    early_d = dv.rolling(21, min_periods=5).sum().shift(21)
    late_u = uv.rolling(21, min_periods=5).sum()
    late_d = dv.rolling(21, min_periods=5).sum()
    return _safe_div(early_u, early_d) - _safe_div(late_u, late_d)


def f04_dtsg_035_vw_close_to_mid_distance_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted distance of close from bar midpoint over 21d, normalized
    by bar range. Negative = closes below midpoint (supply)."""
    mid = (high + low) / 2.0
    dist = _safe_div(close - mid, (high - low))
    num = (dist * volume).rolling(MDAYS, min_periods=5).sum()
    den = volume.rolling(MDAYS, min_periods=5).sum()
    return _safe_div(num, den)


def f04_dtsg_036_effort_vs_result_heavy_vol_bars_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Effort-vs-result on heavy-vol bars: mean of (volume_z / |return|) on
    bars with vol > 1.5x 21d avg. High value = big effort, tiny price move
    (absorption)."""
    vavg = volume.rolling(MDAYS, min_periods=5).mean()
    heavy = volume > 1.5 * vavg
    vz = _rolling_zscore(volume, MDAYS)
    ret_abs = close.pct_change().abs().clip(lower=1e-6)
    ratio = (vz / ret_abs).where(heavy)
    return ratio.rolling(MDAYS, min_periods=3).mean()


# =====================================================================
#  GROUP D — NECKLINE BREAK AND RETEST DYNAMICS (037-048)
# =====================================================================

def _neckline_estimate(low: pd.Series, n: int = 63) -> pd.Series:
    """Neckline = 0.25-quantile of lows over the past n bars (rough proxy for
    the support line of a topping pattern)."""
    return low.rolling(n, min_periods=15).quantile(0.25)


def f04_dtsg_037_time_to_first_neckline_test_post_recognition_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the FIRST close-near-neckline (within 2% of neckline) inside
    the last 63d, after the neckline first formed."""
    neck = _neckline_estimate(low, 63)
    near = (close <= neck * 1.02) & (close >= neck * 0.98)
    near_arr = near.fillna(False).values
    n = 63
    out = np.full(len(near_arr), np.nan)
    for i in range(n - 1, len(near_arr)):
        idx = np.where(near_arr[i - n + 1 : i + 1])[0]
        if idx.size == 0:
            continue
        first_local = idx[0]
        out[i] = float(n - 1 - first_local)
    return pd.Series(out, index=close.index)


def f04_dtsg_038_time_to_first_failed_retest_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since first FAILED retest in last 63d. Failed retest = bar where
    high pokes above neckline*1.01 but close < neckline."""
    neck = _neckline_estimate(low, 63)
    failed = (high > neck * 1.01) & (close < neck)
    arr = failed.fillna(False).values
    n = 63
    out = np.full(len(arr), np.nan)
    for i in range(n - 1, len(arr)):
        idx = np.where(arr[i - n + 1 : i + 1])[0]
        if idx.size == 0:
            continue
        out[i] = float(n - 1 - idx[0])
    return pd.Series(out, index=close.index)


def f04_dtsg_039_neckline_retest_count_before_break_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of retest events (close within 2% of neckline) before the FIRST
    confirmed neckline-break (close < neckline * 0.98) in the last 63d."""
    neck = _neckline_estimate(low, 63)
    near = ((close <= neck * 1.02) & (close >= neck * 0.98)).fillna(False).values
    brk = (close < neck * 0.98).fillna(False).values
    n = 63
    out = np.full(len(near), np.nan)
    for i in range(n - 1, len(near)):
        wb = brk[i - n + 1 : i + 1]
        wn = near[i - n + 1 : i + 1]
        idx = np.where(wb)[0]
        if idx.size == 0:
            continue
        first_brk = idx[0]
        out[i] = float(wn[:first_brk].sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_040_first_retest_excursion_above_neckline_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Magnitude (in log units) of the FIRST retest excursion above neckline in
    63d, after a prior break. = log(retest_high / neckline)."""
    neck = _neckline_estimate(low, 63)
    # A simple proxy: max(0, log(high/neck)) when high > neck after a break
    excursion = (_safe_log(high) - _safe_log(neck)).clip(lower=0)
    return excursion.rolling(QDAYS, min_periods=10).mean()


def f04_dtsg_041_heavy_vol_neckline_break_strength_42d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Heavy-volume neckline-break confirmation: on bars closing below
    neckline*0.99, mean of volume / 42d avg. Higher = stronger break."""
    neck = _neckline_estimate(low, 63)
    brk = close < neck * 0.99
    vavg = volume.rolling(42, min_periods=10).mean()
    vol_ratio = _safe_div(volume, vavg).where(brk)
    return vol_ratio.rolling(42, min_periods=5).mean()


def f04_dtsg_042_retest_exhaustion_ratio_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Each retest weaker than previous: ratio of mean retest amplitude in late
    half (last 31d) vs early half (first 31d) of 63d window."""
    neck = _neckline_estimate(low, 63)
    exc = (_safe_log(high) - _safe_log(neck)).clip(lower=0)
    early = exc.rolling(31, min_periods=5).mean().shift(32)
    late = exc.rolling(31, min_periods=5).mean()
    return _safe_div(late, early)


def f04_dtsg_043_slope_declining_retest_amplitude_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of retest amplitude (high - neckline) over 63d. Negative = retests
    progressively weaker."""
    neck = _neckline_estimate(low, 63)
    amp = (high - neck).clip(lower=0)
    return _rolling_slope(amp, QDAYS)


def f04_dtsg_044_pre_break_consolidation_tightness_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range tightness (mean daily range / 21d avg price) in last 21d. Tight
    pre-break consolidation = lower value."""
    rng = high - low
    mid = (high + low) / 2.0
    return _safe_div(rng.rolling(MDAYS, min_periods=5).mean(), mid.rolling(MDAYS, min_periods=5).mean())


def f04_dtsg_045_neckline_break_then_throwback_count_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (break-then-throwback) events in 63d. A throwback = close drops
    below neckline*0.98 and within next 5 bars rises back to within 1% of neckline."""
    neck = _neckline_estimate(low, 63).values
    cl = close.values
    n = 63
    brk = cl < neck * 0.98
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0.0
        for j in range(i - n + 1, i + 1):
            if not brk[j] or np.isnan(neck[j]):
                continue
            kmax = min(len(cl), j + 6)
            if j + 1 >= kmax:
                continue
            fwd = cl[j + 1 : kmax]
            if np.nanmax(fwd) >= neck[j] * 0.99:
                cnt += 1
        out[i] = cnt
    return pd.Series(out, index=close.index)


def f04_dtsg_046_neckline_break_angle_steepness_21d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Steepness of neckline-break: slope of close in 5 bars following the
    most recent break, normalized by close. Computed and averaged in last 21d."""
    neck = _neckline_estimate(low, 63)
    brk = (close < neck * 0.99) & (close.shift(1) >= neck.shift(1) * 0.99)
    slope5 = _rolling_slope(close, 5, min_periods=3)
    return (slope5 / close).where(brk).rolling(MDAYS, min_periods=3).mean()


def f04_dtsg_047_days_since_most_recent_neckline_test_42d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent neckline test (close within 2% of neckline) in
    last 42d."""
    neck = _neckline_estimate(low, 63)
    near = ((close <= neck * 1.02) & (close >= neck * 0.98)).fillna(False).values
    n = 42
    out = np.full(len(near), np.nan)
    for i in range(n - 1, len(near)):
        idx = np.where(near[i - n + 1 : i + 1])[0]
        if idx.size == 0:
            out[i] = float(n)
            continue
        out[i] = float(n - 1 - idx[-1])
    return pd.Series(out, index=close.index)


def f04_dtsg_048_neckline_test_cluster_density_42d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Max number of neckline tests within any 5d sub-window of last 42d."""
    neck = _neckline_estimate(low, 63)
    near = ((close <= neck * 1.02) & (close >= neck * 0.98)).astype(float)
    return near.rolling(5, min_periods=1).sum().rolling(42, min_periods=10).max()


# =====================================================================
#  GROUP E — BREAKDOWN FOLLOW-THROUGH (049-060)
# =====================================================================

def f04_dtsg_049_first_breakdown_leg_magnitude_42d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Magnitude (log fraction) of the first breakdown leg = log(rolling 42d high
    / current 42d low). Bigger = deeper first leg."""
    rmax = high.rolling(42, min_periods=10).max()
    rmin = low.rolling(42, min_periods=10).min()
    return _safe_log(rmax) - _safe_log(rmin)


def f04_dtsg_050_bars_peak_to_5pct_loss_42d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from the most recent 42d peak to the first close <= peak * 0.95.
    NaN if no peak or no 5% breakdown yet."""
    h = high.values
    cl = close.values
    n = 42
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_h = h[i - n + 1 : i + 1]
        win_c = cl[i - n + 1 : i + 1]
        if np.all(np.isnan(win_h)):
            continue
        peak_local = int(np.nanargmax(win_h))
        peak_val = win_h[peak_local]
        if np.isnan(peak_val):
            continue
        after = win_c[peak_local + 1 :]
        if after.size == 0:
            continue
        below = np.where(after <= peak_val * 0.95)[0]
        if below.size == 0:
            continue
        out[i] = float(below[0] + 1)
    return pd.Series(out, index=close.index)


def f04_dtsg_051_breakdown_momentum_acceleration_21d(close: pd.Series) -> pd.Series:
    """Breakdown momentum acceleration = diff between 5d log-return and 21d log-return
    when both are negative. More negative = accelerating downward."""
    ret5 = _safe_log(close) - _safe_log(close.shift(5))
    ret21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    accel = ret5 - (ret21 / 4.2)  # 5d vs scaled 21d rate
    return accel.where((ret5 < 0) | (ret21 < 0))


def f04_dtsg_052_breakdown_volume_profile_orderly_vs_climax_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of MAX 1-day vol to AVG vol on down-bars within 21d. High value =
    climactic breakdown; low = orderly."""
    ret = close.pct_change()
    down_vol = volume.where(ret < 0)
    return _safe_div(down_vol.rolling(MDAYS, min_periods=5).max(),
                     down_vol.rolling(MDAYS, min_periods=5).mean())


def f04_dtsg_053_first_bounce_magnitude_post_breakdown_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """First-bounce magnitude post-breakdown: log(local-high after local-low /
    local-low). Computed over rolling 21d as max-after-low excess."""
    rmin = low.rolling(MDAYS, min_periods=5).min()
    # max high since min over the last 21d window
    # Approximation: 21d max minus the 21d min, in log units.
    rmax = high.rolling(MDAYS, min_periods=5).max()
    return _safe_log(rmax) - _safe_log(rmin)


def f04_dtsg_054_bars_to_first_bounce_post_breakdown_42d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from most recent 42d low to first close > low * 1.03 (3% bounce)."""
    lo = low.values
    cl = close.values
    n = 42
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        if np.all(np.isnan(win_lo)):
            continue
        lo_local = int(np.nanargmin(win_lo))
        lo_val = win_lo[lo_local]
        if np.isnan(lo_val):
            continue
        after = win_cl[lo_local + 1 :]
        if after.size == 0:
            continue
        above = np.where(after >= lo_val * 1.03)[0]
        if above.size == 0:
            continue
        out[i] = float(above[0] + 1)
    return pd.Series(out, index=close.index)


def f04_dtsg_055_first_bounce_volume_profile_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-profile on bounce bars = mean vol on up-bars in 21d / mean vol on
    down-bars in 21d. Low value = weak bounce volume."""
    ret = close.pct_change()
    up_vol = volume.where(ret > 0)
    down_vol = volume.where(ret < 0)
    return _safe_div(up_vol.rolling(MDAYS, min_periods=3).mean(),
                     down_vol.rolling(MDAYS, min_periods=3).mean())


def f04_dtsg_056_breakdown_followthrough_lowry_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lowry-style follow-through proxy (SEP only): cum dn-volume - cum up-volume
    over 21d, divided by 21d total volume. Negative of accumulation."""
    ret = close.pct_change()
    dn = volume.where(ret < 0, 0.0)
    up = volume.where(ret > 0, 0.0)
    num = (dn - up).rolling(MDAYS, min_periods=5).sum()
    den = volume.rolling(MDAYS, min_periods=5).sum()
    return _safe_div(num, den)


def f04_dtsg_057_breakdown_to_prior_cycle_low_ratio_126d(low: pd.Series) -> pd.Series:
    """Current low vs prior 126d cycle-low. log(current_low / prior_cycle_low).
    Negative = breaking the prior major low."""
    prior = low.rolling(126, min_periods=30).min().shift(63)
    return _safe_log(low) - _safe_log(prior)


def f04_dtsg_058_heavy_vol_breakdown_day_count_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days with close down >=2% AND vol > 2x 50d avg, counted in 42d."""
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    cond = (ret <= -0.02) & (volume > 2.0 * vavg)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_059_days_below_sma200_after_breakdown_63d(close: pd.Series) -> pd.Series:
    """Count of days closing below SMA200 in last 63d (only counts after first
    below-SMA cross in 252d window)."""
    sma200 = close.rolling(200, min_periods=63).mean()
    below = (close < sma200).astype(float)
    cnt = below.rolling(QDAYS, min_periods=15).sum()
    # gate: must have been above sma200 at some point in prior 252d to count
    seen_above = (close >= sma200).rolling(YDAYS, min_periods=63).max()
    return cnt.where(seen_above == 1.0, np.nan)


def f04_dtsg_060_close_below_prior_high_state_persistence_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Persistence of state: fraction of last 63d where close < 252d-rolling-high.
    Rises as time below the peak accumulates."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    below = (close < rmax * 0.99).astype(float)
    return below.rolling(QDAYS, min_periods=15).mean()


# =====================================================================
#  GROUP F — WYCKOFF PHASE A-E CLASSIFICATION (061-072)
# =====================================================================

def _wyckoff_phase_state(high: np.ndarray, low: np.ndarray, close: np.ndarray,
                         volume: np.ndarray, vavg: np.ndarray, atr: np.ndarray) -> np.ndarray:
    """State-machine assignment of Wyckoff phase per bar over the entire series.
    Phases: 0=none, 1=A (climax), 2=B (range), 3=C (test), 4=D (SOW), 5=E (markdown).
    Heuristic, monotone within an episode triggered by a 63d-high peak."""
    n = len(close)
    phase = np.zeros(n, dtype=float)
    # rolling 63d high/low
    cur_phase = 0
    peak_idx = -1
    range_hi = np.nan
    range_lo = np.nan
    for i in range(63, n):
        h63 = np.nanmax(high[max(0, i - 63 + 1) : i + 1])
        l63 = np.nanmin(low[max(0, i - 63 + 1) : i + 1])
        # entry to Phase A: high near 63d max AND prior bar saw a heavy-vol
        # wide-range down (selling climax)
        if cur_phase == 0:
            if i >= 1 and not np.isnan(atr[i]) and not np.isnan(vavg[i]):
                wide = (high[i - 1] - low[i - 1]) > 2.0 * atr[i]
                heavy = volume[i - 1] > 2.0 * vavg[i]
                near_top = high[i - 1] >= 0.95 * h63
                down = close[i - 1] < close[max(0, i - 2)]
                if wide and heavy and near_top and down:
                    cur_phase = 1
                    peak_idx = i - 1
                    range_hi = high[i - 1]
                    range_lo = low[i - 1]
        elif cur_phase == 1:
            # Phase A -> B once we see an automatic rally back
            if close[i] > close[peak_idx] * 0.97:
                cur_phase = 2
                range_hi = max(range_hi, high[i])
                range_lo = min(range_lo, low[i])
            elif i - peak_idx > 21:
                cur_phase = 2  # forced
        elif cur_phase == 2:
            range_hi = max(range_hi, high[i])
            range_lo = min(range_lo, low[i])
            # Phase C upthrust: spike above range_hi then close back inside
            if high[i] > range_hi * 1.01 and close[i] < range_hi:
                cur_phase = 3
            # Phase D sign-of-weakness: close < range mid on heavy vol
            elif (close[i] < (range_hi + range_lo) / 2) and (
                not np.isnan(vavg[i]) and volume[i] > 1.5 * vavg[i]
            ):
                cur_phase = 4
            elif i - peak_idx > 126:
                cur_phase = 4  # range fatigue
        elif cur_phase == 3:
            # Phase C -> D once price closes below range mid
            if close[i] < (range_hi + range_lo) / 2:
                cur_phase = 4
        elif cur_phase == 4:
            # Phase D -> E once we close below range_lo
            if close[i] < range_lo * 0.99:
                cur_phase = 5
        # else cur_phase == 5: stays in E (markdown) until next peak
        # Reset to 0 if a new 252d high appears
        if not np.isnan(h63) and high[i] >= 0.999 * np.nanmax(high[max(0, i - 252 + 1) : i + 1]) and cur_phase == 5:
            cur_phase = 0
            peak_idx = -1
            range_hi = np.nan
            range_lo = np.nan
        phase[i] = cur_phase
    return phase


def _wyckoff_phase_series(high: pd.Series, low: pd.Series, close: pd.Series,
                          volume: pd.Series) -> pd.Series:
    """Cached wrapper around state-machine."""
    vavg = volume.rolling(50, min_periods=10).mean().values
    atr = _atr(high, low, close, 14).values
    phase = _wyckoff_phase_state(high.values, low.values, close.values,
                                 volume.values, vavg, atr)
    return pd.Series(phase, index=close.index)


def f04_dtsg_061_wyckoff_phase_a_selling_climax_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Phase-A (selling-climax) bars in 42d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    return (ph == 1).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_062_wyckoff_phase_a_automatic_rally_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Automatic rally proxy: count in 42d of bars that transitioned from phase
    1 -> 2 (i.e. bars where current phase=2 and prior=1)."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    trans = ((ph == 2) & (ph.shift(1) == 1)).astype(float)
    return trans.rolling(42, min_periods=10).sum()


def f04_dtsg_063_wyckoff_phase_a_secondary_test_detect_42d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Secondary test = retest of recent 42d low on lower volume than the test
    that made it. Count in 42d."""
    rmin42 = low.rolling(42, min_periods=10).min()
    near_lo = low <= rmin42 * 1.02
    vavg = volume.rolling(42, min_periods=10).mean()
    weak_vol = volume < 0.7 * vavg
    return (near_lo & weak_vol).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_064_wyckoff_phase_b_trading_range_detect_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Phase-B (trading range) bars in 63d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    return (ph == 2).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_065_wyckoff_phase_b_range_duration_metric_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest current streak of Phase-B bars within last 63d."""
    ph = _wyckoff_phase_series(high, low, close, volume).values
    n = QDAYS
    out = np.full(len(ph), np.nan)
    for i in range(n - 1, len(ph)):
        seg = (ph[i - n + 1 : i + 1] == 2).astype(int)
        # longest run of 1s
        best = 0
        cur = 0
        for v in seg:
            if v == 1:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out[i] = float(best)
    return pd.Series(out, index=close.index)


def f04_dtsg_066_wyckoff_phase_b_supply_test_event_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Supply-test events (rallies inside Phase B that touch upper bound but
    fail to break): bars where phase==2 and high >= 0.97 * 63d max but close < high."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    rmax63 = high.rolling(QDAYS, min_periods=15).max()
    touch_upper = high >= 0.97 * rmax63
    fail = close < high * 0.995
    cond = (ph == 2) & touch_upper & fail
    return cond.astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_067_wyckoff_phase_c_upthrust_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-C upthrust count in 42d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    return (ph == 3).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_068_wyckoff_phase_c_spring_detect_42d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spring = false break BELOW range_lo with reclaim. Proxy: low pierces 63d
    min by >0.5% but close > 63d min. Count in 42d."""
    rmin63 = low.rolling(QDAYS, min_periods=15).min()
    pierce = low < rmin63 * 0.995
    reclaim = close > rmin63
    return (pierce & reclaim).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_069_wyckoff_phase_d_sign_of_weakness_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-D (sign-of-weakness) bar count in 42d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    return (ph == 4).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_070_wyckoff_phase_d_last_point_of_supply_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Last-point-of-supply (LPSY): in Phase D, failed rally with declining
    volume. Proxy: phase==4 & high > 5d max(shift1) & vol < 21d vol avg & close < high."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    rmax5 = high.shift(1).rolling(5, min_periods=2).max()
    vavg = volume.rolling(MDAYS, min_periods=5).mean()
    cond = (ph == 4) & (high > rmax5) & (volume < vavg) & (close < high * 0.99)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_071_wyckoff_phase_e_markdown_entry_detect_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in Phase E (markdown) in 42d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    return (ph == 5).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_072_wyckoff_current_phase_probability_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current Wyckoff phase scaled to a bearishness-probability score:
    phase 0 -> 0, 1 -> 0.4, 2 -> 0.5, 3 -> 0.6, 4 -> 0.8, 5 -> 1.0. Averaged
    over last 63d as the 'probability of being in late-distribution'."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    mapper = {0.0: 0.0, 1.0: 0.4, 2.0: 0.5, 3.0: 0.6, 4.0: 0.8, 5.0: 1.0}
    mapped = ph.map(mapper)
    return mapped.rolling(QDAYS, min_periods=15).mean()


# =====================================================================
#  GROUP G — SELLING PRESSURE INTENSITY (073-075 — group continues in 076 file)
# =====================================================================

def f04_dtsg_073_effort_result_supply_absorption_divergence_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Supply absorption: high effort (vol z>1) but small price result (|ret|<atr/2).
    Counted and normalized by 21d."""
    vz = _rolling_zscore(volume, MDAYS)
    atr = _atr(high, low, close, 14)
    abs_ret = (close - close.shift(1)).abs()
    cond = (vz > 1.0) & (abs_ret < 0.5 * atr)
    return cond.astype(float).rolling(MDAYS, min_periods=5).mean()


def f04_dtsg_074_smart_money_distribution_score_red_day_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Smart-money distribution score: sum of (vol_z) on red days / sum of |vol_z|
    over 21d. High value = volume concentrated on down days."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, MDAYS)
    red_vz = vz.where(ret < 0, 0.0)
    abs_vz = vz.abs()
    return _safe_div(
        red_vz.rolling(MDAYS, min_periods=5).sum(),
        abs_vz.rolling(MDAYS, min_periods=5).sum(),
    )


def f04_dtsg_075_wyckoff_up_down_volume_ratio_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff up/down volume ratio = sum(up-day vol) / sum(down-day vol) over 42d.
    Below 1 = supply dominates."""
    ret = close.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(42, min_periods=10).sum()
    dn = volume.where(ret < 0, 0.0).rolling(42, min_periods=10).sum()
    return _safe_div(up, dn)


# =====================================================================
#  REGISTRY
# =====================================================================

DISTRIBUTION_TOP_SIGNATURE_BASE_REGISTRY_001_075 = {
    "f04_dtsg_001_lh_count_post_first_252d_high_21d": {"inputs": ["high"], "func": f04_dtsg_001_lh_count_post_first_252d_high_21d},
    "f04_dtsg_002_lh_count_post_first_252d_high_63d": {"inputs": ["high"], "func": f04_dtsg_002_lh_count_post_first_252d_high_63d},
    "f04_dtsg_003_lh_count_post_first_252d_high_126d": {"inputs": ["high"], "func": f04_dtsg_003_lh_count_post_first_252d_high_126d},
    "f04_dtsg_004_lh_count_post_first_252d_high_252d": {"inputs": ["high"], "func": f04_dtsg_004_lh_count_post_first_252d_high_252d},
    "f04_dtsg_005_lh_rank_first_event_post_peak_126d": {"inputs": ["high"], "func": f04_dtsg_005_lh_rank_first_event_post_peak_126d},
    "f04_dtsg_006_lh_rank_second_event_post_peak_126d": {"inputs": ["high"], "func": f04_dtsg_006_lh_rank_second_event_post_peak_126d},
    "f04_dtsg_007_lh_rank_third_event_post_peak_126d": {"inputs": ["high"], "func": f04_dtsg_007_lh_rank_third_event_post_peak_126d},
    "f04_dtsg_008_lh_mean_amplitude_vs_peak_126d": {"inputs": ["high"], "func": f04_dtsg_008_lh_mean_amplitude_vs_peak_126d},
    "f04_dtsg_009_lh_volume_profile_zscore_63d": {"inputs": ["high", "volume"], "func": f04_dtsg_009_lh_volume_profile_zscore_63d},
    "f04_dtsg_010_lh_inter_event_mean_days_126d": {"inputs": ["high"], "func": f04_dtsg_010_lh_inter_event_mean_days_126d},
    "f04_dtsg_011_lh_inter_event_cv_126d": {"inputs": ["high"], "func": f04_dtsg_011_lh_inter_event_cv_126d},
    "f04_dtsg_012_lh_cadence_acceleration_126d": {"inputs": ["high"], "func": f04_dtsg_012_lh_cadence_acceleration_126d},
    "f04_dtsg_013_dday_pre_peak_count_60d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_013_dday_pre_peak_count_60d},
    "f04_dtsg_014_dday_at_peak_count_10d_window": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_014_dday_at_peak_count_10d_window},
    "f04_dtsg_015_dday_post_peak_count_60d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_015_dday_post_peak_count_60d},
    "f04_dtsg_016_dday_stage1_intensity_post_peak_21d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_016_dday_stage1_intensity_post_peak_21d},
    "f04_dtsg_017_dday_stage2_intensity_post_peak_21_42d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_017_dday_stage2_intensity_post_peak_21_42d},
    "f04_dtsg_018_dday_stage3_intensity_post_peak_42_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_018_dday_stage3_intensity_post_peak_42_63d},
    "f04_dtsg_019_dday_acceleration_stage1_to_stage2": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_019_dday_acceleration_stage1_to_stage2},
    "f04_dtsg_020_dday_cluster_density_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_020_dday_cluster_density_42d},
    "f04_dtsg_021_heavy_dday_count_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_021_heavy_dday_count_42d},
    "f04_dtsg_022_stealth_dday_count_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_022_stealth_dday_count_42d},
    "f04_dtsg_023_dday_breadth_multi_horizon_alignment": {"inputs": ["close", "volume"], "func": f04_dtsg_023_dday_breadth_multi_horizon_alignment},
    "f04_dtsg_024_dday_then_failed_recovery_count_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_024_dday_then_failed_recovery_count_63d},
    "f04_dtsg_025_vw_close_position_in_bar_21d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_025_vw_close_position_in_bar_21d},
    "f04_dtsg_026_dollar_vw_lower_high_count_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_026_dollar_vw_lower_high_count_63d},
    "f04_dtsg_027_dist_to_accum_volume_ratio_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_027_dist_to_accum_volume_ratio_42d},
    "f04_dtsg_028_volume_profile_skew_21d": {"inputs": ["volume"], "func": f04_dtsg_028_volume_profile_skew_21d},
    "f04_dtsg_029_heavy_down_day_volume_aggregate_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_029_heavy_down_day_volume_aggregate_42d},
    "f04_dtsg_030_light_up_day_volume_aggregate_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_030_light_up_day_volume_aggregate_42d},
    "f04_dtsg_031_volume_zscore_on_lh_days_63d": {"inputs": ["high", "volume"], "func": f04_dtsg_031_volume_zscore_on_lh_days_63d},
    "f04_dtsg_032_volume_divergence_on_retests_42d": {"inputs": ["high", "volume"], "func": f04_dtsg_032_volume_divergence_on_retests_42d},
    "f04_dtsg_033_cumulative_net_volume_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_033_cumulative_net_volume_21d},
    "f04_dtsg_034_up_to_down_volume_ratio_decay_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_034_up_to_down_volume_ratio_decay_42d},
    "f04_dtsg_035_vw_close_to_mid_distance_21d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_035_vw_close_to_mid_distance_21d},
    "f04_dtsg_036_effort_vs_result_heavy_vol_bars_21d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_036_effort_vs_result_heavy_vol_bars_21d},
    "f04_dtsg_037_time_to_first_neckline_test_post_recognition_63d": {"inputs": ["low", "close"], "func": f04_dtsg_037_time_to_first_neckline_test_post_recognition_63d},
    "f04_dtsg_038_time_to_first_failed_retest_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_038_time_to_first_failed_retest_63d},
    "f04_dtsg_039_neckline_retest_count_before_break_63d": {"inputs": ["low", "close"], "func": f04_dtsg_039_neckline_retest_count_before_break_63d},
    "f04_dtsg_040_first_retest_excursion_above_neckline_63d": {"inputs": ["high", "low"], "func": f04_dtsg_040_first_retest_excursion_above_neckline_63d},
    "f04_dtsg_041_heavy_vol_neckline_break_strength_42d": {"inputs": ["low", "close", "volume"], "func": f04_dtsg_041_heavy_vol_neckline_break_strength_42d},
    "f04_dtsg_042_retest_exhaustion_ratio_63d": {"inputs": ["high", "low"], "func": f04_dtsg_042_retest_exhaustion_ratio_63d},
    "f04_dtsg_043_slope_declining_retest_amplitude_63d": {"inputs": ["high", "low"], "func": f04_dtsg_043_slope_declining_retest_amplitude_63d},
    "f04_dtsg_044_pre_break_consolidation_tightness_21d": {"inputs": ["high", "low"], "func": f04_dtsg_044_pre_break_consolidation_tightness_21d},
    "f04_dtsg_045_neckline_break_then_throwback_count_63d": {"inputs": ["low", "close"], "func": f04_dtsg_045_neckline_break_then_throwback_count_63d},
    "f04_dtsg_046_neckline_break_angle_steepness_21d": {"inputs": ["low", "close"], "func": f04_dtsg_046_neckline_break_angle_steepness_21d},
    "f04_dtsg_047_days_since_most_recent_neckline_test_42d": {"inputs": ["low", "close"], "func": f04_dtsg_047_days_since_most_recent_neckline_test_42d},
    "f04_dtsg_048_neckline_test_cluster_density_42d": {"inputs": ["low", "close"], "func": f04_dtsg_048_neckline_test_cluster_density_42d},
    "f04_dtsg_049_first_breakdown_leg_magnitude_42d": {"inputs": ["high", "low"], "func": f04_dtsg_049_first_breakdown_leg_magnitude_42d},
    "f04_dtsg_050_bars_peak_to_5pct_loss_42d": {"inputs": ["high", "close"], "func": f04_dtsg_050_bars_peak_to_5pct_loss_42d},
    "f04_dtsg_051_breakdown_momentum_acceleration_21d": {"inputs": ["close"], "func": f04_dtsg_051_breakdown_momentum_acceleration_21d},
    "f04_dtsg_052_breakdown_volume_profile_orderly_vs_climax_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_052_breakdown_volume_profile_orderly_vs_climax_21d},
    "f04_dtsg_053_first_bounce_magnitude_post_breakdown_21d": {"inputs": ["high", "low"], "func": f04_dtsg_053_first_bounce_magnitude_post_breakdown_21d},
    "f04_dtsg_054_bars_to_first_bounce_post_breakdown_42d": {"inputs": ["low", "close"], "func": f04_dtsg_054_bars_to_first_bounce_post_breakdown_42d},
    "f04_dtsg_055_first_bounce_volume_profile_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_055_first_bounce_volume_profile_21d},
    "f04_dtsg_056_breakdown_followthrough_lowry_index_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_056_breakdown_followthrough_lowry_index_21d},
    "f04_dtsg_057_breakdown_to_prior_cycle_low_ratio_126d": {"inputs": ["low"], "func": f04_dtsg_057_breakdown_to_prior_cycle_low_ratio_126d},
    "f04_dtsg_058_heavy_vol_breakdown_day_count_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_058_heavy_vol_breakdown_day_count_42d},
    "f04_dtsg_059_days_below_sma200_after_breakdown_63d": {"inputs": ["close"], "func": f04_dtsg_059_days_below_sma200_after_breakdown_63d},
    "f04_dtsg_060_close_below_prior_high_state_persistence_63d": {"inputs": ["high", "close"], "func": f04_dtsg_060_close_below_prior_high_state_persistence_63d},
    "f04_dtsg_061_wyckoff_phase_a_selling_climax_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_061_wyckoff_phase_a_selling_climax_detect_42d},
    "f04_dtsg_062_wyckoff_phase_a_automatic_rally_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_062_wyckoff_phase_a_automatic_rally_detect_42d},
    "f04_dtsg_063_wyckoff_phase_a_secondary_test_detect_42d": {"inputs": ["low", "close", "volume"], "func": f04_dtsg_063_wyckoff_phase_a_secondary_test_detect_42d},
    "f04_dtsg_064_wyckoff_phase_b_trading_range_detect_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_064_wyckoff_phase_b_trading_range_detect_63d},
    "f04_dtsg_065_wyckoff_phase_b_range_duration_metric_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_065_wyckoff_phase_b_range_duration_metric_63d},
    "f04_dtsg_066_wyckoff_phase_b_supply_test_event_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_066_wyckoff_phase_b_supply_test_event_count_63d},
    "f04_dtsg_067_wyckoff_phase_c_upthrust_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_067_wyckoff_phase_c_upthrust_detect_42d},
    "f04_dtsg_068_wyckoff_phase_c_spring_detect_42d": {"inputs": ["low", "close", "volume"], "func": f04_dtsg_068_wyckoff_phase_c_spring_detect_42d},
    "f04_dtsg_069_wyckoff_phase_d_sign_of_weakness_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_069_wyckoff_phase_d_sign_of_weakness_detect_42d},
    "f04_dtsg_070_wyckoff_phase_d_last_point_of_supply_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_070_wyckoff_phase_d_last_point_of_supply_detect_42d},
    "f04_dtsg_071_wyckoff_phase_e_markdown_entry_detect_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_071_wyckoff_phase_e_markdown_entry_detect_42d},
    "f04_dtsg_072_wyckoff_current_phase_probability_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_072_wyckoff_current_phase_probability_score_63d},
    "f04_dtsg_073_effort_result_supply_absorption_divergence_21d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_073_effort_result_supply_absorption_divergence_21d},
    "f04_dtsg_074_smart_money_distribution_score_red_day_vol_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_074_smart_money_distribution_score_red_day_vol_21d},
    "f04_dtsg_075_wyckoff_up_down_volume_ratio_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_075_wyckoff_up_down_volume_ratio_42d},
}
