"""04_distribution_top_signature — base features 076-150.

Pipeline 1b-technical. Continues groups G-M from the base 001-075 file:
selling pressure intensity (cont.), climactic vs orderly distribution,
recovery probability proxies, failed-recovery / DCB, time-to-confirmation,
range contraction, multi-anchor distribution composites.

PIT-clean. Self-contained (no cross-family imports).
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
    ret = close.pct_change()
    vol_up = volume > volume.shift(1)
    return ((ret <= -0.002) & vol_up).astype(float)


def _is_pivot_high(high: pd.Series, k: int = 3) -> pd.Series:
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


def _lh_events(high: pd.Series, k: int = 3) -> pd.Series:
    piv = _is_pivot_high(high, k=k)
    centered_high = high.shift(k)
    piv_h = centered_high.where(piv == 1.0)
    prev_piv_h = piv_h.ffill().shift(1)
    lh = ((piv == 1.0) & (piv_h < prev_piv_h)).astype(float)
    return lh


def _ll_events(low: pd.Series, k: int = 3) -> pd.Series:
    piv = _is_pivot_low(low, k=k)
    centered_low = low.shift(k)
    piv_l = centered_low.where(piv == 1.0)
    prev_piv_l = piv_l.ffill().shift(1)
    ll = ((piv == 1.0) & (piv_l < prev_piv_l)).astype(float)
    return ll


# =====================================================================
#  GROUP G CONTINUED — SELLING PRESSURE INTENSITY (076-082)
# =====================================================================

def f04_dtsg_076_selling_pressure_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling pressure = sum(down-bar vol * |return|) / sum(vol * |return|),
    expressed as 21d z-score."""
    ret = close.pct_change()
    weight = volume * ret.abs()
    down_w = weight.where(ret < 0, 0.0)
    sp = _safe_div(down_w.rolling(MDAYS, min_periods=5).sum(),
                   weight.rolling(MDAYS, min_periods=5).sum())
    return _rolling_zscore(sp, YDAYS, min_periods=63)


def f04_dtsg_077_selling_pressure_acceleration_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of selling pressure = diff between current sp and 21d-prior sp."""
    ret = close.pct_change()
    weight = volume * ret.abs()
    down_w = weight.where(ret < 0, 0.0)
    sp = _safe_div(down_w.rolling(MDAYS, min_periods=5).sum(),
                   weight.rolling(MDAYS, min_periods=5).sum())
    return sp - sp.shift(MDAYS)


def f04_dtsg_078_aggregate_down_bar_volume_ratio_21d_to_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate down-bar volume in 21d divided by aggregate down-bar volume in 63d.
    >0.33 means recent down-vol is over-proportionate."""
    ret = close.pct_change()
    dv = volume.where(ret < 0, 0.0)
    return _safe_div(dv.rolling(MDAYS, min_periods=5).sum(),
                     dv.rolling(QDAYS, min_periods=15).sum())


def f04_dtsg_079_heavy_supply_bar_count_lower_third_close_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars with close in lower third of bar range AND vol > 1.5x 50d avg, count in 42d."""
    pos = _safe_div(close - low, high - low)
    vavg = volume.rolling(50, min_periods=10).mean()
    cond = (pos < 1.0 / 3.0) & (volume > 1.5 * vavg)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_080_supply_overhang_persistence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest streak in last 21d where down-bar volume > up-bar volume (bar-by-bar)."""
    ret = close.pct_change()
    dv = volume.where(ret < 0, 0.0)
    uv = volume.where(ret > 0, 0.0)
    flag = (dv > uv).astype(float).values
    n = MDAYS
    out = np.full(len(flag), np.nan)
    for i in range(n - 1, len(flag)):
        seg = flag[i - n + 1 : i + 1]
        best = 0
        cur = 0
        for v in seg:
            if v == 1.0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out[i] = float(best)
    return pd.Series(out, index=close.index)


def f04_dtsg_081_selling_climax_then_supply_test_pattern_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pattern: selling-climax bar (heavy vol + wide range down) followed within
    21 bars by a supply-test (rally on light volume hitting prior pivot). Count in 63d."""
    atr = _atr(high, low, close, 14)
    vavg = volume.rolling(50, min_periods=10).mean()
    wide_down = (high - low > 2.0 * atr) & (close < close.shift(1)) & (volume > 2.0 * vavg)
    weak_rally = (close > close.shift(1)) & (volume < 0.8 * vavg)
    wd = wide_down.fillna(False).values
    wr = weak_rally.fillna(False).values
    n = QDAYS
    out = np.full(len(wd), np.nan)
    for i in range(n - 1, len(wd)):
        cnt = 0.0
        for j in range(i - n + 1, i + 1):
            if not wd[j]:
                continue
            kmax = min(len(wd), j + 22)
            if j + 1 >= kmax:
                continue
            if wr[j + 1 : kmax].any():
                cnt += 1
        out[i] = cnt
    return pd.Series(out, index=close.index)


def f04_dtsg_082_selling_pressure_asymmetry_down_vs_up_vol_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(down-vol - up-vol) / (down-vol + up-vol) over 42d. Range [-1, +1]; positive
    = down-side asymmetry."""
    ret = close.pct_change()
    dv = volume.where(ret < 0, 0.0).rolling(42, min_periods=10).sum()
    uv = volume.where(ret > 0, 0.0).rolling(42, min_periods=10).sum()
    return _safe_div(dv - uv, dv + uv)


# =====================================================================
#  GROUP H — CLIMACTIC VS ORDERLY DISTRIBUTION (083-092)
# =====================================================================

def f04_dtsg_083_climactic_distribution_score_single_day_blowout_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climactic score: max single-day (|return| * vol_z) on down-days in 63d.
    High = one-day blowout."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    score = (ret.abs() * vz).where(ret < 0)
    return score.rolling(QDAYS, min_periods=10).max()


def f04_dtsg_084_orderly_distribution_score_gradual_lh_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Orderly score: lower-high event count divided by max single-day |return|
    in 63d. High = gradual distribution; low = climactic dominance."""
    lh = _lh_events(high)
    lh_cnt = lh.rolling(QDAYS, min_periods=15).sum()
    max_abs_ret = close.pct_change().abs().rolling(QDAYS, min_periods=15).max()
    return _safe_div(lh_cnt, max_abs_ret * 100)


def f04_dtsg_085_climactic_vs_orderly_classifier_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Classifier in [-1, +1]: positive = climactic dominates, negative = orderly.
    Computed as tanh of (climactic_score / orderly_score - 1)."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    climactic = (ret.abs() * vz).where(ret < 0).rolling(QDAYS, min_periods=10).max()
    lh = _lh_events(high)
    orderly = lh.rolling(QDAYS, min_periods=15).sum()
    ratio = _safe_div(climactic, orderly + 1.0)
    return np.tanh(ratio - ratio.rolling(YDAYS, min_periods=63).median())


def f04_dtsg_086_time_spent_in_climactic_phase_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where return is in worst 5% AND vol_z > 1."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    worst5 = ret.rolling(QDAYS, min_periods=15).quantile(0.05)
    cond = (ret <= worst5) & (vz > 1.0)
    return cond.astype(float).rolling(QDAYS, min_periods=15).mean()


def f04_dtsg_087_volatility_during_distribution_42d(close: pd.Series) -> pd.Series:
    """Std-dev of daily log-returns over 42d. Higher = more climactic distribution."""
    lret = _safe_log(close).diff()
    return lret.rolling(42, min_periods=10).std(ddof=0)


def f04_dtsg_088_range_expansion_during_distribution_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg true-range in last 21d vs avg in prior 21d. >1 = expansion."""
    tr = _true_range(high, low, close)
    a = tr.rolling(MDAYS, min_periods=5).mean()
    b = tr.rolling(MDAYS, min_periods=5).mean().shift(MDAYS)
    return _safe_div(a, b)


def f04_dtsg_089_gap_frequency_during_distribution_42d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in last 42d that gapped (|open - prior close| / prior close > 1%)."""
    pc = close.shift(1)
    gap = (open_ - pc).abs() / pc
    big_gap = (gap > 0.01).astype(float)
    return big_gap.rolling(42, min_periods=10).mean()


def f04_dtsg_090_wide_range_day_count_during_distribution_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of wide-range days (TR > 1.5x 42d avg TR) in last 42d."""
    tr = _true_range(high, low, close)
    avg = tr.rolling(42, min_periods=10).mean()
    return (tr > 1.5 * avg).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_091_climactic_then_orderly_transition_event_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Transition event: a climactic-down bar in early-half (first 32d) of 63d
    window followed by predominantly orderly distribution in late-half. Indicator."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    climactic = (ret < -0.02) & (vz > 1.5)
    early = climactic.rolling(32, min_periods=5).sum().shift(31)
    late_lh = _lh_events(high).rolling(31, min_periods=5).sum()
    cond = (early > 0) & (late_lh >= 2) & (vz.rolling(31, min_periods=5).max() < 1.5)
    return cond.astype(float)


def f04_dtsg_092_distribution_type_persistence_classification_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Persistence of distribution style: rolling 63d standard deviation of
    sign(climactic_score - orderly_score). Low = consistent style; high = switching."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    climactic = (ret.abs() * vz).where(ret < 0).fillna(0)
    lh = _lh_events(high)
    diff = climactic.rolling(5, min_periods=1).sum() - lh.rolling(5, min_periods=1).sum()
    sign = np.sign(diff)
    return sign.rolling(QDAYS, min_periods=15).std(ddof=0)


# =====================================================================
#  GROUP I — RECOVERY PROBABILITY PROXIES (093-104)
# =====================================================================

def f04_dtsg_093_recovery_attempt_magnitude_post_first_break_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude of recovery (max close after most recent 63d low) / breakdown amplitude
    (peak-to-low) in 63d. >0.5 = strong recovery."""
    h = high.values
    l = low.values
    c = close.values
    n = QDAYS
    out = np.full(len(c), np.nan)
    for i in range(n - 1, len(c)):
        win_h = h[i - n + 1 : i + 1]
        win_l = l[i - n + 1 : i + 1]
        win_c = c[i - n + 1 : i + 1]
        if np.all(np.isnan(win_l)) or np.all(np.isnan(win_h)):
            continue
        lo_local = int(np.nanargmin(win_l))
        hi_local = int(np.nanargmax(win_h))
        if hi_local >= lo_local:
            continue  # peak after low => not a breakdown
        peak_val = win_h[hi_local]
        lo_val = win_l[lo_local]
        if np.isnan(peak_val) or np.isnan(lo_val) or peak_val == lo_val:
            continue
        rec_max = np.nanmax(win_c[lo_local + 1 :]) if lo_local + 1 < n else np.nan
        if np.isnan(rec_max):
            continue
        out[i] = float((rec_max - lo_val) / (peak_val - lo_val))
    return pd.Series(out, index=close.index)


def f04_dtsg_094_bars_to_first_recovery_attempt_post_break_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from 63d low to first close >= low * 1.05 (5% recovery attempt)."""
    lo = low.values
    cl = close.values
    n = QDAYS
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
        above = np.where(after >= lo_val * 1.05)[0]
        if above.size == 0:
            continue
        out[i] = float(above[0] + 1)
    return pd.Series(out, index=close.index)


def f04_dtsg_095_recovery_attempts_count_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of distinct recovery attempts in 63d. An attempt = sequence rising
    from a local min to a local max with >=3% gain."""
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win = cl[i - n + 1 : i + 1]
        if np.isnan(win).all():
            out[i] = 0.0
            continue
        # find local mins/maxes via sign changes of diff
        d = np.diff(win)
        if d.size < 2:
            out[i] = 0.0
            continue
        s = np.sign(d)
        cnt = 0
        last_min_val = win[0]
        for j in range(1, len(s)):
            if s[j - 1] < 0 and s[j] > 0:
                last_min_val = win[j]
            if s[j - 1] > 0 and s[j] < 0:
                if not np.isnan(last_min_val) and win[j] > last_min_val * 1.03:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_096_recovery_attempts_amplitude_decay_63d(close: pd.Series) -> pd.Series:
    """Slope of recovery-attempt amplitudes in 63d. Negative = each attempt weaker."""
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win = cl[i - n + 1 : i + 1]
        if np.isnan(win).all():
            continue
        d = np.diff(win)
        if d.size < 5:
            continue
        s = np.sign(d)
        amps = []
        last_min_val = win[0]
        for j in range(1, len(s)):
            if s[j - 1] < 0 and s[j] > 0:
                last_min_val = win[j]
            if s[j - 1] > 0 and s[j] < 0:
                if not np.isnan(last_min_val):
                    amps.append(win[j] - last_min_val)
        if len(amps) < 3:
            continue
        x = np.arange(len(amps), dtype=float)
        y = np.array(amps, dtype=float)
        x -= x.mean()
        if (x ** 2).sum() == 0:
            continue
        out[i] = float(((x) * (y - y.mean())).sum() / (x ** 2).sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_097_recovery_attempt_volume_profile_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on up-bars in 63d divided by mean vol on down-bars in 63d. Low =
    weak recovery vol."""
    ret = close.pct_change()
    up_vol_mean = volume.where(ret > 0).rolling(QDAYS, min_periods=10).mean()
    dn_vol_mean = volume.where(ret < 0).rolling(QDAYS, min_periods=10).mean()
    return _safe_div(up_vol_mean, dn_vol_mean)


def f04_dtsg_098_recovery_attempt_success_rate_reaching_prior_high_126d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of pivot-low bars in last 126d whose subsequent close (within next
    21 bars) reached >= 0.95 * prior pivot-high."""
    piv_lo = _is_pivot_low(close, 3).fillna(0.0).values
    cl = close.values
    n = 126
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        attempts = 0
        success = 0
        # only consider pivot bars whose centered index (j - 3) + 21 <= i
        for j in range(i - n + 1, i - 24):
            if piv_lo[j] == 1.0:
                attempts += 1
                pivot_close = cl[j - 3] if j - 3 >= 0 else np.nan
                if np.isnan(pivot_close):
                    continue
                fwd_max = np.nanmax(cl[j + 1 : j + 22])
                # 'prior high' proxy = max close in 63d window ending at j
                a = max(0, j - 63)
                prior_high = np.nanmax(cl[a : j + 1])
                if not np.isnan(prior_high) and fwd_max >= prior_high * 0.95:
                    success += 1
        if attempts == 0:
            continue
        out[i] = float(success / attempts)
    return pd.Series(out, index=close.index)


def f04_dtsg_099_time_to_recovery_failure_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from start of a recovery attempt to its failure (close back below
    starting low). Averaged over 63d."""
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win = cl[i - n + 1 : i + 1]
        if np.isnan(win).all():
            continue
        d = np.diff(win)
        if d.size < 5:
            continue
        s = np.sign(d)
        durations = []
        start_idx = None
        start_val = None
        for j in range(1, len(s)):
            if s[j - 1] < 0 and s[j] > 0:
                start_idx = j
                start_val = win[j]
            elif start_idx is not None and not np.isnan(start_val) and win[j] < start_val:
                durations.append(j - start_idx)
                start_idx = None
        if not durations:
            continue
        out[i] = float(np.mean(durations))
    return pd.Series(out, index=close.index)


def f04_dtsg_100_recovery_to_breakdown_slope_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recovery slope / breakdown slope in 63d. >1 = recovery steeper than breakdown."""
    h = high.values
    l = low.values
    c = close.values
    n = QDAYS
    out = np.full(len(c), np.nan)
    for i in range(n - 1, len(c)):
        win_h = h[i - n + 1 : i + 1]
        win_l = l[i - n + 1 : i + 1]
        win_c = c[i - n + 1 : i + 1]
        if np.all(np.isnan(win_h)) or np.all(np.isnan(win_l)):
            continue
        hi_local = int(np.nanargmax(win_h))
        lo_local = int(np.nanargmin(win_l))
        if hi_local >= lo_local:
            continue
        break_bars = lo_local - hi_local
        break_amp = win_h[hi_local] - win_l[lo_local]
        if break_bars <= 0 or break_amp <= 0:
            continue
        break_slope = break_amp / break_bars
        rec_bars = len(win_c) - 1 - lo_local
        if rec_bars <= 0:
            continue
        rec_amp = np.nanmax(win_c[lo_local + 1 :]) - win_l[lo_local]
        if np.isnan(rec_amp) or rec_amp <= 0:
            continue
        rec_slope = rec_amp / rec_bars
        if break_slope == 0:
            continue
        out[i] = float(rec_slope / break_slope)
    return pd.Series(out, index=close.index)


def f04_dtsg_101_cumulative_recovery_attempt_amplitude_63d(close: pd.Series) -> pd.Series:
    """Sum of all recovery-attempt amplitudes in 63d, normalized by 63d range."""
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win = cl[i - n + 1 : i + 1]
        if np.isnan(win).all():
            continue
        d = np.diff(win)
        if d.size < 2:
            continue
        s = np.sign(d)
        amps = []
        last_min = win[0]
        for j in range(1, len(s)):
            if s[j - 1] < 0 and s[j] > 0:
                last_min = win[j]
            if s[j - 1] > 0 and s[j] < 0:
                if not np.isnan(last_min):
                    amps.append(win[j] - last_min)
        rng = np.nanmax(win) - np.nanmin(win)
        if rng <= 0:
            continue
        out[i] = float(np.nansum(amps) / rng)
    return pd.Series(out, index=close.index)


def f04_dtsg_102_recovery_attempt_cluster_density_63d(close: pd.Series) -> pd.Series:
    """Max count of recovery attempts within any 21d sub-window of 63d."""
    cl = close.values
    n = QDAYS
    sub = 21
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        best = 0
        for start in range(i - n + 1, i - sub + 2):
            win = cl[start : start + sub]
            if np.isnan(win).all():
                continue
            d = np.diff(win)
            if d.size < 2:
                continue
            s = np.sign(d)
            cnt = 0
            last_min = win[0]
            for j in range(1, len(s)):
                if s[j - 1] < 0 and s[j] > 0:
                    last_min = win[j]
                if s[j - 1] > 0 and s[j] < 0:
                    if not np.isnan(last_min) and win[j] > last_min * 1.02:
                        cnt += 1
            if cnt > best:
                best = cnt
        out[i] = float(best)
    return pd.Series(out, index=close.index)


def f04_dtsg_103_recovery_attempt_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Asymmetry: number of recovery attempts in first half (32d) minus number in
    second half (31d) of 63d window."""
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    def _count(arr):
        d = np.diff(arr)
        if d.size < 2:
            return 0
        s = np.sign(d)
        cnt = 0
        last_min = arr[0]
        for j in range(1, len(s)):
            if s[j - 1] < 0 and s[j] > 0:
                last_min = arr[j]
            if s[j - 1] > 0 and s[j] < 0:
                if not np.isnan(last_min) and arr[j] > last_min * 1.02:
                    cnt += 1
        return cnt
    for i in range(n - 1, len(cl)):
        a = cl[i - n + 1 : i - 31 + 1]
        b = cl[i - 31 + 1 : i + 1]
        if a.size < 5 or b.size < 5:
            continue
        out[i] = float(_count(a) - _count(b))
    return pd.Series(out, index=close.index)


def f04_dtsg_104_recovery_then_failure_specific_indicator_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: in last 63d, there exists a recovery >= 5% from prior low AND a
    subsequent lower low below the original low. Returns 0/1."""
    lo = low.values
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        if np.isnan(win_lo).all():
            continue
        lo_local = int(np.nanargmin(win_lo))
        lo_val = win_lo[lo_local]
        if np.isnan(lo_val) or lo_local >= len(win_cl) - 2:
            out[i] = 0.0
            continue
        post_cl = win_cl[lo_local + 1 :]
        if (post_cl >= lo_val * 1.05).any():
            # check whether after the recovery, lo dipped below lo_val
            post_lo = win_lo[lo_local + 1 :]
            if (post_lo < lo_val * 0.99).any():
                out[i] = 1.0
            else:
                out[i] = 0.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=close.index)


# =====================================================================
#  GROUP J — FAILED-RECOVERY / DEAD-CAT-BOUNCE (105-114)
# =====================================================================

def f04_dtsg_105_dead_cat_bounce_event_count_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of DCB events in 252d. A DCB = recovery >=10% from a local low
    followed by a new lower low within 21 bars."""
    lo = low.values
    cl = close.values
    n = YDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0
        for j in range(i - n + 1, i - 21):
            if j < 5:
                continue
            window5 = lo[max(0, j - 5) : j + 1]
            if window5.size < 2 or np.all(np.isnan(window5)):
                continue
            if lo[j] != np.nanmin(window5):
                continue
            fwd_cl = cl[j + 1 : min(len(cl), j + 22)]
            fwd_lo = lo[j + 1 : min(len(lo), j + 22)]
            if fwd_cl.size == 0:
                continue
            peak_idx_rel = np.nanargmax(fwd_cl)
            peak_val = fwd_cl[peak_idx_rel]
            if np.isnan(peak_val) or lo[j] <= 0:
                continue
            if peak_val < lo[j] * 1.10:
                continue
            # check for new lower low after the bounce
            after_peak = fwd_lo[peak_idx_rel + 1 :]
            if after_peak.size == 0:
                continue
            if (after_peak < lo[j]).any():
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_106_bounce_then_lower_low_pattern_count_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Specific pattern: bounce (close up 5d return >+5%) immediately followed by
    a lower-low within next 10 bars. Count in 63d."""
    cl = close.values
    lo = low.values
    n = QDAYS
    bounce = (np.array(pd.Series(cl).pct_change(5).fillna(0)) > 0.05)
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0
        for j in range(i - n + 1, i - 9):
            if not bounce[j]:
                continue
            start_lo = lo[j]
            if np.isnan(start_lo):
                continue
            fwd_lo = lo[j + 1 : min(len(lo), j + 11)]
            if (fwd_lo < start_lo).any():
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_107_bounce_then_failed_retest_pattern_count_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bounce (5d return >+5%) followed by a failed retest of prior peak (high
    pokes above 21d prior peak then closes below) within 10 bars. Count in 63d."""
    cl = close.values
    h = high.values
    rmax21 = pd.Series(h).rolling(MDAYS, min_periods=5).max().shift(5).values
    n = QDAYS
    bounce = (np.array(pd.Series(cl).pct_change(5).fillna(0)) > 0.05)
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0
        for j in range(i - n + 1, i - 9):
            if not bounce[j]:
                continue
            fwd = range(j + 1, min(len(cl), j + 11))
            for k in fwd:
                if np.isnan(rmax21[k]):
                    continue
                if h[k] > rmax21[k] * 1.01 and cl[k] < rmax21[k]:
                    cnt += 1
                    break
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_108_bounce_amplitude_vs_prior_decline_ratio_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """In last 42d, find peak-to-trough decline and subsequent recovery; ratio
    recovery/decline. Typical DCB = 1/3 to 1/2."""
    h = high.values
    l = low.values
    c = close.values
    n = 42
    out = np.full(len(c), np.nan)
    for i in range(n - 1, len(c)):
        win_h = h[i - n + 1 : i + 1]
        win_l = l[i - n + 1 : i + 1]
        win_c = c[i - n + 1 : i + 1]
        if np.all(np.isnan(win_h)) or np.all(np.isnan(win_l)):
            continue
        hi_local = int(np.nanargmax(win_h))
        lo_local = int(np.nanargmin(win_l[hi_local:])) + hi_local if hi_local < len(win_l) else -1
        if lo_local <= hi_local or lo_local >= len(win_c) - 1:
            continue
        peak = win_h[hi_local]
        trough = win_l[lo_local]
        if np.isnan(peak) or np.isnan(trough) or peak <= trough:
            continue
        rec = np.nanmax(win_c[lo_local + 1 :]) - trough
        decl = peak - trough
        if decl <= 0:
            continue
        out[i] = float(rec / decl)
    return pd.Series(out, index=close.index)


def f04_dtsg_109_bounce_completion_then_rollover_indicator_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bounce completed (close rose >=10% from prior 21d low) and is
    now rolling over (current close < high of last 10d * 0.95). Returns 0/1."""
    rmin21 = low.rolling(MDAYS, min_periods=5).min()
    bounce_done = close >= rmin21 * 1.10
    rmax10 = close.rolling(10, min_periods=3).max()
    rollover = close < rmax10 * 0.95
    return (bounce_done & rollover).astype(float)


def f04_dtsg_110_bounce_with_declining_volume_signature_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bounce vol signature: 5d return > +5% AND 5d-avg vol < 21d-avg vol. Count in 42d."""
    ret5 = close.pct_change(5)
    v5 = volume.rolling(5, min_periods=2).mean()
    v21 = volume.rolling(MDAYS, min_periods=5).mean()
    cond = (ret5 > 0.05) & (v5 < v21)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_111_failed_recovery_count_after_first_break_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of recovery attempts (closes rising >=3% from a local low) that
    subsequently failed (close fell back to <= the local low) within 21 bars
    after first 63d-breakdown. Count over 63d window."""
    lo = low.values
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        cnt = 0
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        # iterate looking for local-low -> recovery -> failure
        for j in range(2, len(win_lo) - 2):
            if win_lo[j] != np.nanmin(win_lo[max(0, j - 5) : j + 1]):
                continue
            fwd_cl = win_cl[j + 1 : min(len(win_cl), j + 22)]
            if fwd_cl.size == 0:
                continue
            peak_rel = np.nanargmax(fwd_cl)
            if not np.isfinite(fwd_cl[peak_rel]) or win_lo[j] <= 0:
                continue
            if fwd_cl[peak_rel] < win_lo[j] * 1.03:
                continue
            # check failure after peak
            after = fwd_cl[peak_rel + 1 :]
            if after.size == 0:
                continue
            if (after <= win_lo[j]).any():
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_112_cumulative_failed_recovery_amplitude_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative amplitude (peak-of-attempt minus its starting low) of all
    failed recoveries in 63d, normalized by 63d range."""
    lo = low.values
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        amps = 0.0
        for j in range(2, len(win_lo) - 2):
            if win_lo[j] != np.nanmin(win_lo[max(0, j - 5) : j + 1]):
                continue
            fwd_cl = win_cl[j + 1 : min(len(win_cl), j + 22)]
            if fwd_cl.size == 0:
                continue
            peak_rel = np.nanargmax(fwd_cl)
            if not np.isfinite(fwd_cl[peak_rel]) or win_lo[j] <= 0:
                continue
            after = fwd_cl[peak_rel + 1 :]
            if after.size == 0:
                continue
            if (after <= win_lo[j]).any():
                amps += max(0.0, fwd_cl[peak_rel] - win_lo[j])
        rng = np.nanmax(win_cl) - np.nanmin(win_lo) if win_cl.size and win_lo.size else 0
        if rng <= 0:
            continue
        out[i] = float(amps / rng)
    return pd.Series(out, index=close.index)


def f04_dtsg_113_dcb_time_to_completion_42d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from start of bounce to peak of bounce, averaged across DCB events in 42d.
    A DCB event = bounce >=10% from a local low followed by a lower low."""
    lo = low.values
    cl = close.values
    n = 42
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        durs = []
        for j in range(2, len(win_lo) - 2):
            if win_lo[j] != np.nanmin(win_lo[max(0, j - 5) : j + 1]):
                continue
            fwd_cl = win_cl[j + 1 : min(len(win_cl), j + 22)]
            fwd_lo = win_lo[j + 1 : min(len(win_lo), j + 22)]
            if fwd_cl.size == 0:
                continue
            peak_rel = np.nanargmax(fwd_cl)
            if np.isnan(fwd_cl[peak_rel]) or win_lo[j] <= 0:
                continue
            if fwd_cl[peak_rel] < win_lo[j] * 1.10:
                continue
            after = fwd_lo[peak_rel + 1 :]
            if (after < win_lo[j]).any():
                durs.append(peak_rel + 1)
        if not durs:
            continue
        out[i] = float(np.mean(durs))
    return pd.Series(out, index=close.index)


def f04_dtsg_114_dcb_then_extension_pattern_count_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """DCB-then-extension: after a DCB (bounce + lower-low), the new lower-low
    is followed by another DCB. Count in 63d."""
    lo = low.values
    cl = close.values
    n = QDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        win_lo = lo[i - n + 1 : i + 1]
        win_cl = cl[i - n + 1 : i + 1]
        cnt = 0
        # find DCB events (peaks of bounces that ended in a lower-low)
        dcb_lows = []
        for j in range(2, len(win_lo) - 2):
            if win_lo[j] != np.nanmin(win_lo[max(0, j - 5) : j + 1]):
                continue
            fwd_cl = win_cl[j + 1 : min(len(win_cl), j + 22)]
            fwd_lo = win_lo[j + 1 : min(len(win_lo), j + 22)]
            if fwd_cl.size == 0:
                continue
            peak_rel = np.nanargmax(fwd_cl)
            if np.isnan(fwd_cl[peak_rel]) or win_lo[j] <= 0:
                continue
            if fwd_cl[peak_rel] < win_lo[j] * 1.10:
                continue
            after = fwd_lo[peak_rel + 1 :]
            if not (after < win_lo[j]).any():
                continue
            dcb_lows.append(j)
        # Two DCB events in sequence => extension
        if len(dcb_lows) >= 2:
            cnt = len(dcb_lows) - 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


# =====================================================================
#  GROUP K — TIME-TO-CONFIRMATION (115-122)
# =====================================================================

def f04_dtsg_115_time_first_close_below_prior_high_to_confirmed_breakdown_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from first close < 252d-rolling-high to first close <= 252d-high * 0.90
    (10% confirmed breakdown), measured in last 63d."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    below = close < rmax * 0.999
    confirm = close <= rmax * 0.90
    below_arr = below.fillna(False).values
    confirm_arr = confirm.fillna(False).values
    n = QDAYS
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        ib = np.where(below_arr[i - n + 1 : i + 1])[0]
        ic = np.where(confirm_arr[i - n + 1 : i + 1])[0]
        if ib.size == 0 or ic.size == 0:
            continue
        first_b = ib[0]
        first_c_after = ic[ic >= first_b]
        if first_c_after.size == 0:
            continue
        out[i] = float(first_c_after[0] - first_b)
    return pd.Series(out, index=close.index)


def f04_dtsg_116_time_neckline_break_to_followthrough_42d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from neckline break (close < neck*0.98) to follow-through (close < neck*0.93)
    in 42d window."""
    neck = low.rolling(QDAYS, min_periods=15).quantile(0.25)
    brk = (close < neck * 0.98).fillna(False).values
    follow = (close < neck * 0.93).fillna(False).values
    n = 42
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        ib = np.where(brk[i - n + 1 : i + 1])[0]
        ic = np.where(follow[i - n + 1 : i + 1])[0]
        if ib.size == 0 or ic.size == 0:
            continue
        first_b = ib[0]
        after = ic[ic >= first_b]
        if after.size == 0:
            continue
        out[i] = float(after[0] - first_b)
    return pd.Series(out, index=close.index)


def f04_dtsg_117_time_first_retest_failure_to_next_leg_breakdown_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from first failed retest (high>neck*1.01 & close<neck) to subsequent
    close < neck*0.95, in 63d."""
    neck = low.rolling(QDAYS, min_periods=15).quantile(0.25)
    failed = ((high > neck * 1.01) & (close < neck)).fillna(False).values
    leg = (close < neck * 0.95).fillna(False).values
    n = QDAYS
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        ifd = np.where(failed[i - n + 1 : i + 1])[0]
        ileg = np.where(leg[i - n + 1 : i + 1])[0]
        if ifd.size == 0 or ileg.size == 0:
            continue
        after = ileg[ileg >= ifd[0]]
        if after.size == 0:
            continue
        out[i] = float(after[0] - ifd[0])
    return pd.Series(out, index=close.index)


def _wyckoff_phase_state(high: np.ndarray, low: np.ndarray, close: np.ndarray,
                         volume: np.ndarray, vavg: np.ndarray, atr: np.ndarray) -> np.ndarray:
    n = len(close)
    phase = np.zeros(n, dtype=float)
    cur_phase = 0
    peak_idx = -1
    range_hi = np.nan
    range_lo = np.nan
    for i in range(63, n):
        h63 = np.nanmax(high[max(0, i - 63 + 1) : i + 1])
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
            if close[i] > close[peak_idx] * 0.97:
                cur_phase = 2
                range_hi = max(range_hi, high[i])
                range_lo = min(range_lo, low[i])
            elif i - peak_idx > 21:
                cur_phase = 2
        elif cur_phase == 2:
            range_hi = max(range_hi, high[i])
            range_lo = min(range_lo, low[i])
            if high[i] > range_hi * 1.01 and close[i] < range_hi:
                cur_phase = 3
            elif (close[i] < (range_hi + range_lo) / 2) and (
                not np.isnan(vavg[i]) and volume[i] > 1.5 * vavg[i]
            ):
                cur_phase = 4
            elif i - peak_idx > 126:
                cur_phase = 4
        elif cur_phase == 3:
            if close[i] < (range_hi + range_lo) / 2:
                cur_phase = 4
        elif cur_phase == 4:
            if close[i] < range_lo * 0.99:
                cur_phase = 5
        if not np.isnan(h63) and high[i] >= 0.999 * np.nanmax(high[max(0, i - 252 + 1) : i + 1]) and cur_phase == 5:
            cur_phase = 0
            peak_idx = -1
            range_hi = np.nan
            range_lo = np.nan
        phase[i] = cur_phase
    return phase


def _wyckoff_phase_series(high: pd.Series, low: pd.Series, close: pd.Series,
                          volume: pd.Series) -> pd.Series:
    vavg = volume.rolling(50, min_periods=10).mean().values
    atr = _atr(high, low, close, 14).values
    phase = _wyckoff_phase_state(high.values, low.values, close.values,
                                 volume.values, vavg, atr)
    return pd.Series(phase, index=close.index)


def f04_dtsg_118_time_wyckoff_phase_d_to_phase_e_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from first phase==4 to first phase==5 in 63d window."""
    ph = _wyckoff_phase_series(high, low, close, volume).values
    n = QDAYS
    out = np.full(len(ph), np.nan)
    for i in range(n - 1, len(ph)):
        seg = ph[i - n + 1 : i + 1]
        i4 = np.where(seg == 4)[0]
        i5 = np.where(seg == 5)[0]
        if i4.size == 0 or i5.size == 0:
            continue
        after = i5[i5 >= i4[0]]
        if after.size == 0:
            continue
        out[i] = float(after[0] - i4[0])
    return pd.Series(out, index=close.index)


def f04_dtsg_119_time_peak_to_first_10pct_breakdown(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars from most recent 252d peak to first close <= peak * 0.90. NaN if no
    such breakdown has occurred yet."""
    is_peak = _is_252d_high(high).fillna(0.0).values
    h = high.values
    cl = close.values
    n = YDAYS
    out = np.full(len(cl), np.nan)
    for i in range(n - 1, len(cl)):
        idx = np.where(is_peak[i - n + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n + 1 + idx[-1]
        peak_val = h[peak_pos]
        if np.isnan(peak_val):
            continue
        after = cl[peak_pos + 1 : i + 1]
        if after.size == 0:
            continue
        below = np.where(after <= peak_val * 0.90)[0]
        if below.size == 0:
            continue
        out[i] = float(below[0] + 1)
    return pd.Series(out, index=close.index)


def f04_dtsg_120_time_peak_to_confirmed_dow_theory_breakdown_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars from most recent 252d peak to first bar where both prior swing-high and
    prior swing-low have been violated (close-only proxy: low < 63d rolling min
    that excluded the most recent 21 days)."""
    is_peak = _is_252d_high(high).fillna(0.0).values
    rmin = low.rolling(QDAYS, min_periods=15).min().shift(MDAYS).values
    lo = low.values
    n = YDAYS
    out = np.full(len(low), np.nan)
    for i in range(n - 1, len(low)):
        idx = np.where(is_peak[i - n + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - n + 1 + idx[-1]
        after = lo[peak_pos + 1 : i + 1]
        prior_min = rmin[peak_pos + 1 : i + 1]
        if after.size == 0:
            continue
        below = np.where(after < prior_min)[0]
        if below.size == 0:
            continue
        out[i] = float(below[0] + 1)
    return pd.Series(out, index=low.index)


def f04_dtsg_121_confirmation_latency_vs_typical_zscore_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (over 252d) of the time_peak_to_first_10pct_breakdown signal."""
    base = f04_dtsg_119_time_peak_to_first_10pct_breakdown(high, close)
    return _rolling_zscore(base, YDAYS, min_periods=63)


def f04_dtsg_122_multi_confirmation_alignment_time_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Time-window in 63d where at least 3 of {close<sma50, close<sma200,
    dday_count_25d>=5, lower-high event present in 21d} are simultaneously true.
    Returns max consecutive bars meeting condition."""
    sma50 = close.rolling(50, min_periods=15).mean()
    sma200 = close.rolling(200, min_periods=60).mean()
    dd = _is_dday(close, volume).rolling(25, min_periods=5).sum()
    lh21 = _lh_events(high).rolling(MDAYS, min_periods=5).sum()
    c1 = (close < sma50).astype(int)
    c2 = (close < sma200).astype(int)
    c3 = (dd >= 5).astype(int)
    c4 = (lh21 >= 1).astype(int)
    total = (c1 + c2 + c3 + c4) >= 3
    arr = total.fillna(False).astype(int).values
    n = QDAYS
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        seg = arr[i - n + 1 : i + 1]
        best = 0
        cur = 0
        for v in seg:
            if v:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        out[i] = float(best)
    return pd.Series(out, index=close.index)


# =====================================================================
#  GROUP L — RANGE CONTRACTION WITHIN ROLLING TOP (123-130)
# =====================================================================

def f04_dtsg_123_range_contraction_rate_within_top_42d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of contraction = slope of daily range over 42d, divided by mean
    range. Negative = contracting."""
    rng = high - low
    slope = _rolling_slope(rng, 42)
    return _safe_div(slope, rng.rolling(42, min_periods=10).mean())


def f04_dtsg_124_range_compression_breakout_direction_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """After compression (current TR < 0.7 * 42d avg TR), direction of next bar's
    return. Indicator: +1 if up, -1 if down."""
    tr = _true_range(high, low, close)
    avg = tr.rolling(42, min_periods=10).mean()
    compressed = tr.shift(1) < 0.7 * avg.shift(1)
    direction = np.sign(close.pct_change())
    return direction.where(compressed)


def f04_dtsg_125_range_contraction_then_expansion_event_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of contraction-then-expansion events in 42d: TR drops to <0.7x avg
    then rises to >1.5x avg within 5 bars."""
    tr = _true_range(high, low, close)
    avg = tr.rolling(42, min_periods=10).mean()
    contracted = (tr < 0.7 * avg).fillna(False).values
    expanded = (tr > 1.5 * avg).fillna(False).values
    n = 42
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        cnt = 0
        for j in range(i - n + 1, i):
            if contracted[j]:
                kmax = min(len(close), j + 6)
                if expanded[j + 1 : kmax].any():
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f04_dtsg_126_range_volatility_during_distribution_42d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Standard deviation of daily range over 42d, normalized by mean range."""
    rng = high - low
    return _safe_div(rng.rolling(42, min_periods=10).std(ddof=0),
                     rng.rolling(42, min_periods=10).mean())


def f04_dtsg_127_bar_range_entropy_during_distribution_42d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of daily range distribution (10 bins) over 42d."""
    rng = (high - low).values
    n = 42
    out = np.full(len(rng), np.nan)
    for i in range(n - 1, len(rng)):
        w = rng[i - n + 1 : i + 1]
        w = w[~np.isnan(w)]
        if w.size < 10 or w.max() == w.min():
            continue
        hist, _ = np.histogram(w, bins=10)
        p = hist[hist > 0] / hist.sum()
        out[i] = float(-(p * np.log(p)).sum())
    return pd.Series(out, index=high.index)


def f04_dtsg_128_atr_shrinkage_rate_within_top_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(current ATR / ATR 42d ago). Negative = ATR shrinking."""
    atr14 = _atr(high, low, close, 14)
    return _safe_log(atr14) - _safe_log(atr14.shift(42))


def f04_dtsg_129_bb_width_contraction_during_distribution_42d(close: pd.Series) -> pd.Series:
    """Bollinger Band width = (upper - lower) / middle, percentile rank in 42d.
    Low percentile = tight bands."""
    m = close.rolling(MDAYS, min_periods=5).mean()
    sd = close.rolling(MDAYS, min_periods=5).std(ddof=0)
    width = _safe_div(4 * sd, m)
    return width.rolling(42, min_periods=10).rank(pct=True)


def f04_dtsg_130_range_vs_volume_divergence_42d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence: range slope < 0 AND volume slope > 0 over 42d. Returns
    volume_slope * (-range_slope) where both signs align; else 0."""
    rng = high - low
    rs = _rolling_slope(rng, 42)
    vs = _rolling_slope(volume, 42)
    cond = (rs < 0) & (vs > 0)
    return (vs * (-rs)).where(cond, 0.0)


# =====================================================================
#  GROUP M — MULTI-ANCHOR DISTRIBUTION COMPOSITES (131-150)
# =====================================================================

def _zsc(s: pd.Series, n: int = YDAYS) -> pd.Series:
    return _rolling_zscore(s, n, min_periods=63)


def f04_dtsg_131_composite_lh_dday_neckline_test_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite z-score: standardized sum of (LH-count, D-day-count, neckline-test-count) over 63d."""
    lh = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    dd = _is_dday(close, volume).rolling(QDAYS, min_periods=15).sum()
    neck = low.rolling(QDAYS, min_periods=15).quantile(0.25)
    near = ((close <= neck * 1.02) & (close >= neck * 0.98)).astype(float).rolling(QDAYS, min_periods=15).sum()
    return _zsc(lh) + _zsc(dd) + _zsc(near)


def f04_dtsg_132_composite_wyckoff_phase_d_plus_lh_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (Phase-D count in 42d) + LH count in 63d, both z-scored."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    pd_count = (ph == 4).astype(float).rolling(42, min_periods=10).sum()
    lh = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    return _zsc(pd_count) + _zsc(lh)


def f04_dtsg_133_composite_failed_recovery_plus_lower_low_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite of failed-recovery count and lower-low count, z-scored."""
    fr = f04_dtsg_111_failed_recovery_count_after_first_break_63d(low, close)
    ll = _ll_events(low).rolling(QDAYS, min_periods=15).sum()
    return _zsc(fr) + _zsc(ll)


def f04_dtsg_134_composite_breakdown_speed_plus_vol_confirmation_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite of inverse-bars-to-5pct-loss (speed) and heavy-vol-breakdown count, z-scored."""
    bars = _bars_peak_to_5pct_loss_42d_local(high, close)
    speed = _safe_div(pd.Series(1.0, index=close.index), bars + 1.0)
    heavy = _heavy_vol_breakdown_count_local(close, volume)
    return _zsc(speed) + _zsc(heavy)


def _bars_peak_to_5pct_loss_42d_local(high: pd.Series, close: pd.Series) -> pd.Series:
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


def _heavy_vol_breakdown_count_local(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    cond = (ret <= -0.02) & (volume > 2.0 * vavg)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_135_composite_dcb_plus_extension_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite of DCB-count and DCB-then-extension count, z-scored."""
    dcb = f04_dtsg_105_dead_cat_bounce_event_count_252d(low, close)
    ext = f04_dtsg_114_dcb_then_extension_pattern_count_63d(low, close)
    return _zsc(dcb) + _zsc(ext)


def f04_dtsg_136_composite_climactic_orderly_transition_score_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite of climactic-score, orderly-score, and transition event, z-scored."""
    ret = close.pct_change()
    vz = _rolling_zscore(volume, QDAYS, min_periods=15)
    climactic = (ret.abs() * vz).where(ret < 0).rolling(QDAYS, min_periods=10).max()
    orderly = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    trans = ((ret < -0.02) & (vz > 1.5)).astype(float).rolling(63, min_periods=15).sum()
    return _zsc(climactic) + _zsc(orderly) + _zsc(trans)


def f04_dtsg_137_composite_selling_pressure_plus_lh_acceleration_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling pressure z-score plus LH cadence acceleration z-score."""
    ret = close.pct_change()
    weight = volume * ret.abs()
    down_w = weight.where(ret < 0, 0.0)
    sp = _safe_div(down_w.rolling(MDAYS, min_periods=5).sum(),
                   weight.rolling(MDAYS, min_periods=5).sum())
    lh_arr = _lh_events(high).values
    out = np.full(len(close), np.nan)
    nh = 126
    h = nh // 2
    for i in range(nh - 1, len(lh_arr)):
        a = lh_arr[i - nh + 1 : i - h + 1]
        b = lh_arr[i - h + 1 : i + 1]
        ia = np.where(a == 1.0)[0]
        ib = np.where(b == 1.0)[0]
        if ia.size < 2 or ib.size < 2:
            continue
        out[i] = float(np.diff(ia).mean() - np.diff(ib).mean())
    accel = pd.Series(out, index=close.index)
    return _zsc(sp) + _zsc(accel)


def f04_dtsg_138_multi_stage_distribution_intensity_sum_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of stage-1, stage-2, stage-3 D-day intensities (all already in [0,1])."""
    is_peak = _is_252d_high(high).values
    dd = _is_dday(close, volume).values
    out = np.full(len(close), np.nan)
    for i in range(YDAYS, len(close)):
        idx = np.where(is_peak[i - YDAYS + 1 : i + 1] == 1.0)[0]
        if idx.size == 0:
            continue
        peak_pos = i - YDAYS + 1 + idx[-1]
        total = 0.0
        cnt = 0
        for (a, b) in [(0, 21), (21, 42), (42, 63)]:
            sa = peak_pos + 1 + a
            sb = min(len(close), peak_pos + 1 + b, i + 1)
            if sa >= sb:
                continue
            seg = dd[sa:sb]
            if seg.size == 0:
                continue
            total += float(np.nansum(seg) / seg.size)
            cnt += 1
        if cnt == 0:
            continue
        out[i] = total
    return pd.Series(out, index=close.index)


def f04_dtsg_139_distribution_process_maturity_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maturity score: weighted sum of (early markers, mid markers, late markers).
    Early = top-dwell; mid = LH+DDay; late = phase-E count. Returns weighted z."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    top_dwell = (high >= rmax * 0.97).astype(float).rolling(QDAYS, min_periods=15).mean()
    lh = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    dd = _is_dday(close, volume).rolling(QDAYS, min_periods=15).sum()
    ph = _wyckoff_phase_series(high, low, close, volume)
    phE = (ph == 5).astype(float).rolling(QDAYS, min_periods=15).sum()
    return _zsc(top_dwell) * 0.2 + _zsc(lh + dd) * 0.4 + _zsc(phE) * 0.4


def f04_dtsg_140_distribution_confirmation_breadth_signals_firing_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count (0-6) of distribution signals firing above their 252d median in 63d window.
    Signals: LH cnt, DDay cnt, Phase-D cnt, neckline-test cnt, heavy-supply cnt, vol-z on red days."""
    lh = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    dd = _is_dday(close, volume).rolling(QDAYS, min_periods=15).sum()
    ph = _wyckoff_phase_series(high, low, close, volume)
    pd_cnt = (ph == 4).astype(float).rolling(QDAYS, min_periods=15).sum()
    neck = low.rolling(QDAYS, min_periods=15).quantile(0.25)
    near = ((close <= neck * 1.02) & (close >= neck * 0.98)).astype(float).rolling(QDAYS, min_periods=15).sum()
    pos = _safe_div(close - low, high - low)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy_sup = ((pos < 1.0/3.0) & (volume > 1.5 * vavg)).astype(float).rolling(QDAYS, min_periods=15).sum()
    ret = close.pct_change()
    vz = _rolling_zscore(volume, MDAYS)
    red_vz_avg = vz.where(ret < 0).rolling(QDAYS, min_periods=10).mean()
    signals = [lh, dd, pd_cnt, near, heavy_sup, red_vz_avg]
    pieces = []
    for k, s in enumerate(signals):
        med = s.rolling(YDAYS, min_periods=63).median()
        pieces.append((s > med).astype(float).rename(k))
    cat = pd.concat(pieces, axis=1)
    return cat.sum(axis=1).where(lh.notna(), np.nan)


def f04_dtsg_141_distribution_price_volume_divergence_composite_42d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite divergence: price slope - volume slope - OBV-style proxy slope, all 42d, z-scored."""
    ps = _rolling_slope(close, 42)
    vs = _rolling_slope(volume, 42)
    ret = close.pct_change()
    obv = (np.sign(ret) * volume).cumsum()
    os = _rolling_slope(obv, 42)
    return _zsc(-ps) + _zsc(vs) + _zsc(-os)


def f04_dtsg_142_distribution_day_cluster_intensity_composite_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of D-day cluster densities at three sub-window sizes (3d, 5d, 10d) within 42d."""
    dd = _is_dday(close, volume)
    c3 = dd.rolling(3, min_periods=1).sum().rolling(42, min_periods=10).max()
    c5 = dd.rolling(5, min_periods=1).sum().rolling(42, min_periods=10).max()
    c10 = dd.rolling(10, min_periods=1).sum().rolling(42, min_periods=10).max()
    return _zsc(c3) + _zsc(c5) + _zsc(c10)


def f04_dtsg_143_recovery_failure_persistence_composite_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: failed-recovery count + cumulative failed-recovery amplitude, z-scored."""
    fr = f04_dtsg_111_failed_recovery_count_after_first_break_63d(low, close)
    ca = f04_dtsg_112_cumulative_failed_recovery_amplitude_63d(low, close)
    return _zsc(fr) + _zsc(ca)


def f04_dtsg_144_distribution_process_velocity_pattern_progression_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of progression through Wyckoff phases: avg phase value change per day over 63d."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    delta = ph - ph.shift(QDAYS)
    return delta / float(QDAYS)


def f04_dtsg_145_wyckoff_phase_transition_imminence_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Imminence score: when current phase==4 (D), how persistent has phase==4 been?
    Returns fraction of last 21 bars in phase 4."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    in_d = (ph == 4).astype(float)
    return in_d.rolling(MDAYS, min_periods=5).mean()


def f04_dtsg_146_distribution_completion_probability_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Logistic-style completion score: weighted blend (clipped 0-1) of normalized
    LH count, D-day count, and current phase / 5."""
    lh = _lh_events(high).rolling(QDAYS, min_periods=15).sum()
    dd = _is_dday(close, volume).rolling(QDAYS, min_periods=15).sum()
    ph = _wyckoff_phase_series(high, low, close, volume)
    lh_n = (lh / lh.rolling(YDAYS, min_periods=63).max()).clip(0, 1)
    dd_n = (dd / dd.rolling(YDAYS, min_periods=63).max()).clip(0, 1)
    ph_n = (ph / 5.0).clip(0, 1)
    return (0.3 * lh_n + 0.3 * dd_n + 0.4 * ph_n).clip(0, 1)


def f04_dtsg_147_cumulative_selling_pressure_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative selling pressure over 63d, expressed as 252d z-score."""
    ret = close.pct_change()
    sp = (volume * (-ret).clip(lower=0)).rolling(QDAYS, min_periods=15).sum()
    return _zsc(sp)


def f04_dtsg_148_multi_horizon_distribution_agreement_21_63_126d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """How many of {21d, 63d, 126d} LH-count rolling z-scores exceed +0.5?
    Range 0-3. Captures multi-horizon agreement that distribution is ongoing."""
    lh = _lh_events(high)
    c21 = lh.rolling(MDAYS, min_periods=5).sum()
    c63 = lh.rolling(QDAYS, min_periods=15).sum()
    c126 = lh.rolling(126, min_periods=30).sum()
    z21 = _rolling_zscore(c21, YDAYS, min_periods=63)
    z63 = _rolling_zscore(c63, YDAYS, min_periods=63)
    z126 = _rolling_zscore(c126, YDAYS, min_periods=63)
    return ((z21 > 0.5).astype(float) + (z63 > 0.5).astype(float) + (z126 > 0.5).astype(float)).where(c126.notna(), np.nan)


def f04_dtsg_149_distribution_fatigue_selling_exhausted_no_rally_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fatigue: low volume (vol_z < -0.5) AND no positive 5d return AND no big down
    move (|5d ret| < 3%). Count in 42d (selling exhausted but no rally either)."""
    ret5 = close.pct_change(5)
    vz = _rolling_zscore(volume, MDAYS)
    cond = (vz < -0.5) & (ret5 < 0.01) & (ret5 > -0.03)
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_150_terminal_distribution_state_composite_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal state composite: ph==5 fraction + cum negative return + below-SMA200 fraction."""
    ph = _wyckoff_phase_series(high, low, close, volume)
    ph5 = (ph == 5).astype(float).rolling(QDAYS, min_periods=15).mean()
    cumneg = (close.pct_change().clip(upper=0)).rolling(QDAYS, min_periods=15).sum()
    sma200 = close.rolling(200, min_periods=60).mean()
    below = (close < sma200).astype(float).rolling(QDAYS, min_periods=15).mean()
    return _zsc(ph5) + _zsc(-cumneg) + _zsc(below)


# =====================================================================
#  REGISTRY
# =====================================================================

DISTRIBUTION_TOP_SIGNATURE_BASE_REGISTRY_076_150 = {
    "f04_dtsg_076_selling_pressure_zscore_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_076_selling_pressure_zscore_21d},
    "f04_dtsg_077_selling_pressure_acceleration_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_077_selling_pressure_acceleration_21d},
    "f04_dtsg_078_aggregate_down_bar_volume_ratio_21d_to_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_078_aggregate_down_bar_volume_ratio_21d_to_63d},
    "f04_dtsg_079_heavy_supply_bar_count_lower_third_close_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_079_heavy_supply_bar_count_lower_third_close_42d},
    "f04_dtsg_080_supply_overhang_persistence_21d": {"inputs": ["close", "volume"], "func": f04_dtsg_080_supply_overhang_persistence_21d},
    "f04_dtsg_081_selling_climax_then_supply_test_pattern_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_081_selling_climax_then_supply_test_pattern_63d},
    "f04_dtsg_082_selling_pressure_asymmetry_down_vs_up_vol_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_082_selling_pressure_asymmetry_down_vs_up_vol_42d},
    "f04_dtsg_083_climactic_distribution_score_single_day_blowout_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_083_climactic_distribution_score_single_day_blowout_63d},
    "f04_dtsg_084_orderly_distribution_score_gradual_lh_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_084_orderly_distribution_score_gradual_lh_63d},
    "f04_dtsg_085_climactic_vs_orderly_classifier_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_085_climactic_vs_orderly_classifier_63d},
    "f04_dtsg_086_time_spent_in_climactic_phase_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_086_time_spent_in_climactic_phase_63d},
    "f04_dtsg_087_volatility_during_distribution_42d": {"inputs": ["close"], "func": f04_dtsg_087_volatility_during_distribution_42d},
    "f04_dtsg_088_range_expansion_during_distribution_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_088_range_expansion_during_distribution_42d},
    "f04_dtsg_089_gap_frequency_during_distribution_42d": {"inputs": ["open", "close"], "func": f04_dtsg_089_gap_frequency_during_distribution_42d},
    "f04_dtsg_090_wide_range_day_count_during_distribution_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_090_wide_range_day_count_during_distribution_42d},
    "f04_dtsg_091_climactic_then_orderly_transition_event_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_091_climactic_then_orderly_transition_event_63d},
    "f04_dtsg_092_distribution_type_persistence_classification_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_092_distribution_type_persistence_classification_63d},
    "f04_dtsg_093_recovery_attempt_magnitude_post_first_break_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_093_recovery_attempt_magnitude_post_first_break_63d},
    "f04_dtsg_094_bars_to_first_recovery_attempt_post_break_63d": {"inputs": ["low", "close"], "func": f04_dtsg_094_bars_to_first_recovery_attempt_post_break_63d},
    "f04_dtsg_095_recovery_attempts_count_63d": {"inputs": ["low", "close"], "func": f04_dtsg_095_recovery_attempts_count_63d},
    "f04_dtsg_096_recovery_attempts_amplitude_decay_63d": {"inputs": ["close"], "func": f04_dtsg_096_recovery_attempts_amplitude_decay_63d},
    "f04_dtsg_097_recovery_attempt_volume_profile_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_097_recovery_attempt_volume_profile_63d},
    "f04_dtsg_098_recovery_attempt_success_rate_reaching_prior_high_126d": {"inputs": ["high", "close"], "func": f04_dtsg_098_recovery_attempt_success_rate_reaching_prior_high_126d},
    "f04_dtsg_099_time_to_recovery_failure_63d": {"inputs": ["low", "close"], "func": f04_dtsg_099_time_to_recovery_failure_63d},
    "f04_dtsg_100_recovery_to_breakdown_slope_ratio_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_100_recovery_to_breakdown_slope_ratio_63d},
    "f04_dtsg_101_cumulative_recovery_attempt_amplitude_63d": {"inputs": ["close"], "func": f04_dtsg_101_cumulative_recovery_attempt_amplitude_63d},
    "f04_dtsg_102_recovery_attempt_cluster_density_63d": {"inputs": ["close"], "func": f04_dtsg_102_recovery_attempt_cluster_density_63d},
    "f04_dtsg_103_recovery_attempt_asymmetry_63d": {"inputs": ["close"], "func": f04_dtsg_103_recovery_attempt_asymmetry_63d},
    "f04_dtsg_104_recovery_then_failure_specific_indicator_63d": {"inputs": ["low", "close"], "func": f04_dtsg_104_recovery_then_failure_specific_indicator_63d},
    "f04_dtsg_105_dead_cat_bounce_event_count_252d": {"inputs": ["low", "close"], "func": f04_dtsg_105_dead_cat_bounce_event_count_252d},
    "f04_dtsg_106_bounce_then_lower_low_pattern_count_63d": {"inputs": ["low", "close"], "func": f04_dtsg_106_bounce_then_lower_low_pattern_count_63d},
    "f04_dtsg_107_bounce_then_failed_retest_pattern_count_63d": {"inputs": ["high", "close"], "func": f04_dtsg_107_bounce_then_failed_retest_pattern_count_63d},
    "f04_dtsg_108_bounce_amplitude_vs_prior_decline_ratio_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_108_bounce_amplitude_vs_prior_decline_ratio_42d},
    "f04_dtsg_109_bounce_completion_then_rollover_indicator_63d": {"inputs": ["low", "close"], "func": f04_dtsg_109_bounce_completion_then_rollover_indicator_63d},
    "f04_dtsg_110_bounce_with_declining_volume_signature_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_110_bounce_with_declining_volume_signature_42d},
    "f04_dtsg_111_failed_recovery_count_after_first_break_63d": {"inputs": ["low", "close"], "func": f04_dtsg_111_failed_recovery_count_after_first_break_63d},
    "f04_dtsg_112_cumulative_failed_recovery_amplitude_63d": {"inputs": ["low", "close"], "func": f04_dtsg_112_cumulative_failed_recovery_amplitude_63d},
    "f04_dtsg_113_dcb_time_to_completion_42d": {"inputs": ["low", "close"], "func": f04_dtsg_113_dcb_time_to_completion_42d},
    "f04_dtsg_114_dcb_then_extension_pattern_count_63d": {"inputs": ["low", "close"], "func": f04_dtsg_114_dcb_then_extension_pattern_count_63d},
    "f04_dtsg_115_time_first_close_below_prior_high_to_confirmed_breakdown_63d": {"inputs": ["high", "close"], "func": f04_dtsg_115_time_first_close_below_prior_high_to_confirmed_breakdown_63d},
    "f04_dtsg_116_time_neckline_break_to_followthrough_42d": {"inputs": ["low", "close"], "func": f04_dtsg_116_time_neckline_break_to_followthrough_42d},
    "f04_dtsg_117_time_first_retest_failure_to_next_leg_breakdown_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_117_time_first_retest_failure_to_next_leg_breakdown_63d},
    "f04_dtsg_118_time_wyckoff_phase_d_to_phase_e_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_118_time_wyckoff_phase_d_to_phase_e_63d},
    "f04_dtsg_119_time_peak_to_first_10pct_breakdown": {"inputs": ["high", "close"], "func": f04_dtsg_119_time_peak_to_first_10pct_breakdown},
    "f04_dtsg_120_time_peak_to_confirmed_dow_theory_breakdown_252d": {"inputs": ["high", "low"], "func": f04_dtsg_120_time_peak_to_confirmed_dow_theory_breakdown_252d},
    "f04_dtsg_121_confirmation_latency_vs_typical_zscore_252d": {"inputs": ["high", "close"], "func": f04_dtsg_121_confirmation_latency_vs_typical_zscore_252d},
    "f04_dtsg_122_multi_confirmation_alignment_time_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_122_multi_confirmation_alignment_time_63d},
    "f04_dtsg_123_range_contraction_rate_within_top_42d": {"inputs": ["high", "low"], "func": f04_dtsg_123_range_contraction_rate_within_top_42d},
    "f04_dtsg_124_range_compression_breakout_direction_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_124_range_compression_breakout_direction_42d},
    "f04_dtsg_125_range_contraction_then_expansion_event_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_125_range_contraction_then_expansion_event_42d},
    "f04_dtsg_126_range_volatility_during_distribution_42d": {"inputs": ["high", "low"], "func": f04_dtsg_126_range_volatility_during_distribution_42d},
    "f04_dtsg_127_bar_range_entropy_during_distribution_42d": {"inputs": ["high", "low"], "func": f04_dtsg_127_bar_range_entropy_during_distribution_42d},
    "f04_dtsg_128_atr_shrinkage_rate_within_top_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_128_atr_shrinkage_rate_within_top_42d},
    "f04_dtsg_129_bb_width_contraction_during_distribution_42d": {"inputs": ["close"], "func": f04_dtsg_129_bb_width_contraction_during_distribution_42d},
    "f04_dtsg_130_range_vs_volume_divergence_42d": {"inputs": ["high", "low", "volume"], "func": f04_dtsg_130_range_vs_volume_divergence_42d},
    "f04_dtsg_131_composite_lh_dday_neckline_test_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_131_composite_lh_dday_neckline_test_63d},
    "f04_dtsg_132_composite_wyckoff_phase_d_plus_lh_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_132_composite_wyckoff_phase_d_plus_lh_count_63d},
    "f04_dtsg_133_composite_failed_recovery_plus_lower_low_63d": {"inputs": ["low", "close"], "func": f04_dtsg_133_composite_failed_recovery_plus_lower_low_63d},
    "f04_dtsg_134_composite_breakdown_speed_plus_vol_confirmation_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_134_composite_breakdown_speed_plus_vol_confirmation_42d},
    "f04_dtsg_135_composite_dcb_plus_extension_63d": {"inputs": ["low", "close"], "func": f04_dtsg_135_composite_dcb_plus_extension_63d},
    "f04_dtsg_136_composite_climactic_orderly_transition_score_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_136_composite_climactic_orderly_transition_score_63d},
    "f04_dtsg_137_composite_selling_pressure_plus_lh_acceleration_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_137_composite_selling_pressure_plus_lh_acceleration_63d},
    "f04_dtsg_138_multi_stage_distribution_intensity_sum_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_138_multi_stage_distribution_intensity_sum_63d},
    "f04_dtsg_139_distribution_process_maturity_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_139_distribution_process_maturity_score_63d},
    "f04_dtsg_140_distribution_confirmation_breadth_signals_firing_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_140_distribution_confirmation_breadth_signals_firing_63d},
    "f04_dtsg_141_distribution_price_volume_divergence_composite_42d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_141_distribution_price_volume_divergence_composite_42d},
    "f04_dtsg_142_distribution_day_cluster_intensity_composite_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_142_distribution_day_cluster_intensity_composite_42d},
    "f04_dtsg_143_recovery_failure_persistence_composite_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_143_recovery_failure_persistence_composite_63d},
    "f04_dtsg_144_distribution_process_velocity_pattern_progression_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_144_distribution_process_velocity_pattern_progression_63d},
    "f04_dtsg_145_wyckoff_phase_transition_imminence_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_145_wyckoff_phase_transition_imminence_score_63d},
    "f04_dtsg_146_distribution_completion_probability_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_146_distribution_completion_probability_63d},
    "f04_dtsg_147_cumulative_selling_pressure_zscore_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_147_cumulative_selling_pressure_zscore_63d},
    "f04_dtsg_148_multi_horizon_distribution_agreement_21_63_126d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_148_multi_horizon_distribution_agreement_21_63_126d},
    "f04_dtsg_149_distribution_fatigue_selling_exhausted_no_rally_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_149_distribution_fatigue_selling_exhausted_no_rally_42d},
    "f04_dtsg_150_terminal_distribution_state_composite_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_150_terminal_distribution_state_composite_63d},
}
