"""04_distribution_top_signature — base features 151-225 (gap-fill).

Pipeline 1b-technical. Extension beyond the original 150 with 75 distinct
hypotheses targeting gaps identified after Wyckoff / climactic / recovery
coverage was already in place. Covers:

  Bucket A (151-160) Volume-profile proxies (POC/VAH/VAL from daily bars)
  Bucket B (161-168) Smart-money / dumb-money proxies
  Bucket C (169-173) IBD-style follow-through-day failure metrics
  Bucket D (174-179) Weinstein Stage-3-to-Stage-4 detection
  Bucket E (180-185) Cumulative-volume-delta (CVD) proxies
  Bucket F (186-190) Hindenburg-Omen single-name internals
  Bucket G (191-200) Wyckoff refinements beyond the 061-075 / 145 set
  Bucket H (201-206) Rounding vs sharp distribution shape
  Bucket I (207-214) Bar-level distribution signatures
  Bucket J (215-218) Anchored-VWAP-from-distribution-peak metrics
  Bucket K (219-222) Phase-transition / time-decay
  Bucket L (223-225) Narrow dtsg-internal composites

Inputs: SEP only — open, high, low, close, volume. PIT-clean: right-anchored
rolling windows, explicit min_periods, no centered windows, no .shift(N).
Self-contained: no cross-family imports. numpy + pandas only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# ----------------------------- constants -------------------------------
YDAYS = 252
HDAYS = 126
QDAYS = 63
MDAYS = 21
WDAYS = 5
WK30 = 150  # 30-week SMA in trading days


# ----------------------------- helpers ---------------------------------
def _safe_log(s: pd.Series) -> pd.Series:
    s = pd.Series(s, dtype="float64")
    return np.log(s.where(s > 0))


def _safe_div(num, den):
    num = pd.Series(num, dtype="float64") if not isinstance(num, pd.Series) else num.astype("float64")
    den = pd.Series(den, dtype="float64") if not isinstance(den, pd.Series) else den.astype("float64")
    out = num / den.where(den != 0)
    return out.replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
    if min_periods is None:
        min_periods = max(n // 3, 5)
    m = s.rolling(n, min_periods=min_periods).mean()
    sd = s.rolling(n, min_periods=min_periods).std(ddof=0)
    return _safe_div(s - m, sd)


def _zsc(s: pd.Series) -> pd.Series:
    return _rolling_zscore(s, YDAYS, min_periods=60)


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    return pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
    if min_periods is None:
        min_periods = max(n // 3, 3)

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
        den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        return float(((x - xm) * (wv - wm)).sum() / den)

    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _typical(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


def _vwap_window(price: pd.Series, volume: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
    if min_periods is None:
        min_periods = max(n // 3, 5)
    pv = (price * volume).rolling(n, min_periods=min_periods).sum()
    v = volume.rolling(n, min_periods=min_periods).sum()
    return _safe_div(pv, v)


def _argmax_window(s: pd.Series, n: int, min_periods: int | None = None) -> pd.Series:
    """Right-anchored rolling argmax position (0..n-1), where n-1 is current bar."""
    if min_periods is None:
        min_periods = max(n // 3, 3)
    return s.rolling(n, min_periods=min_periods).apply(
        lambda w: float(np.nanargmax(w)) if np.isfinite(w).any() else np.nan, raw=True
    )


# ============================================================
#  BUCKET A — Volume-profile proxies (151-160)
# ============================================================

def f04_dtsg_151_vwap_21d_distance(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP_21d) / VWAP_21d. Above-VWAP support proxy near top."""
    tp = _typical(high, low, close)
    vwap = _vwap_window(tp, volume, MDAYS)
    return _safe_div(close - vwap, vwap)


def f04_dtsg_152_vwap_63d_distance(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP_63d) / VWAP_63d. Mid-horizon volume-weighted equilibrium."""
    tp = _typical(high, low, close)
    vwap = _vwap_window(tp, volume, QDAYS)
    return _safe_div(close - vwap, vwap)


def f04_dtsg_153_vwap_252d_distance(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP_252d) / VWAP_252d. Long-horizon vol-weighted fair value."""
    tp = _typical(high, low, close)
    vwap = _vwap_window(tp, volume, YDAYS)
    return _safe_div(close - vwap, vwap)


def _poc_metrics(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, n: int, bins: int = 20):
    """Approximate POC / VAH / VAL by binning typical-price weighted by volume over n bars.
    Returns DataFrame with columns: poc, vah, val (price levels)."""
    tp = _typical(high, low, close).astype("float64")
    vol = volume.astype("float64")
    idx = close.index
    poc = np.full(len(close), np.nan)
    vah = np.full(len(close), np.nan)
    val = np.full(len(close), np.nan)
    tp_arr = tp.values
    vol_arr = vol.values
    min_periods = max(n // 3, 10)
    for i in range(min_periods - 1, len(close)):
        lo = max(0, i - n + 1)
        seg_p = tp_arr[lo:i + 1]
        seg_v = vol_arr[lo:i + 1]
        m = np.isfinite(seg_p) & np.isfinite(seg_v) & (seg_v > 0)
        if m.sum() < min_periods:
            continue
        sp = seg_p[m]
        sv = seg_v[m]
        pmin, pmax = float(sp.min()), float(sp.max())
        if not np.isfinite(pmin) or not np.isfinite(pmax) or pmax <= pmin:
            poc[i] = pmin
            vah[i] = pmax
            val[i] = pmin
            continue
        edges = np.linspace(pmin, pmax, bins + 1)
        hist = np.zeros(bins, dtype="float64")
        # bin index for each typical price
        bin_idx = np.clip(((sp - pmin) / (pmax - pmin) * bins).astype(int), 0, bins - 1)
        for b, v_ in zip(bin_idx, sv):
            hist[b] += v_
        total = hist.sum()
        if total <= 0:
            continue
        # POC = center of max-vol bin
        poc_b = int(np.argmax(hist))
        poc[i] = 0.5 * (edges[poc_b] + edges[poc_b + 1])
        # Value area = expand symmetrically from POC until 70% volume covered
        target = 0.70 * total
        covered = hist[poc_b]
        lo_b = hi_b = poc_b
        while covered < target and (lo_b > 0 or hi_b < bins - 1):
            left_v = hist[lo_b - 1] if lo_b > 0 else -1.0
            right_v = hist[hi_b + 1] if hi_b < bins - 1 else -1.0
            if right_v >= left_v and hi_b < bins - 1:
                hi_b += 1
                covered += hist[hi_b]
            elif lo_b > 0:
                lo_b -= 1
                covered += hist[lo_b]
            else:
                break
        val[i] = edges[lo_b]
        vah[i] = edges[hi_b + 1]
    return pd.DataFrame({"poc": poc, "vah": vah, "val": val}, index=idx)


def f04_dtsg_154_poc_distance_to_close_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - POC_63d) / POC_63d. POC = volume-profile point-of-control proxy."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    return _safe_div(close - pm["poc"], pm["poc"])


def f04_dtsg_155_value_area_high_distance_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VAH_63d) / VAH_63d. Above VAH = above 70%-volume value area top."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    return _safe_div(close - pm["vah"], pm["vah"])


def f04_dtsg_156_value_area_low_distance_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VAL_63d) / VAL_63d. Below VAL = below 70%-volume value area bottom."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    return _safe_div(close - pm["val"], pm["val"])


def f04_dtsg_157_days_inside_value_area_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d where close lies between VAL_63d and VAH_63d."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    inside = ((close >= pm["val"]) & (close <= pm["vah"])).astype(float)
    return inside.rolling(MDAYS, min_periods=5).mean()


def f04_dtsg_158_single_print_bar_count_at_top_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Single-print proxy: bars where volume is in bottom-decile of 63d AND high
    is within 5% of 63d max. Such low-vol gap-bars near the top = weak demand zones."""
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near_top = (_safe_div(high, rmax) >= 0.95)
    vq10 = volume.rolling(QDAYS, min_periods=15).quantile(0.10)
    light = volume <= vq10
    cond = (near_top & light).astype(float)
    return cond.rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_159_vah_val_range_width_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(VAH - VAL) / POC over 63d profile. Wider value area = more distribution spread."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    return _safe_div(pm["vah"] - pm["val"], pm["poc"])


def f04_dtsg_160_vol_weighted_skew_around_poc_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted skewness of typical-price around its mean over 63d.
    Negative skew = heavy tail below = distribution toward downside."""
    tp = _typical(high, low, close)
    n = QDAYS
    min_periods = max(n // 3, 10)
    tp_arr = tp.values.astype("float64")
    v_arr = volume.values.astype("float64")
    out = np.full(len(close), np.nan)
    for i in range(min_periods - 1, len(close)):
        lo = max(0, i - n + 1)
        sp = tp_arr[lo:i + 1]
        sv = v_arr[lo:i + 1]
        m = np.isfinite(sp) & np.isfinite(sv) & (sv > 0)
        if m.sum() < min_periods:
            continue
        sp = sp[m]
        sv = sv[m]
        w = sv / sv.sum()
        mu = (w * sp).sum()
        var = (w * (sp - mu) ** 2).sum()
        if var <= 0:
            continue
        sd = np.sqrt(var)
        skew = (w * ((sp - mu) / sd) ** 3).sum()
        out[i] = float(skew)
    return pd.Series(out, index=close.index)


# ============================================================
#  BUCKET B — Smart-money / dumb-money proxies (161-168)
# ============================================================

def f04_dtsg_161_smart_money_index_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """SMI proxy: cumulative (close - open) minus first-30-min-proxy (= open - prev close).
    Smart money trades the close; dumb money trades the open. 21d sum normalised by close."""
    early = open_ - close.shift(1)        # dumb-money proxy
    late = close - open_                  # smart-money proxy
    smi = (late - early).rolling(MDAYS, min_periods=5).sum()
    return _safe_div(smi, close)


def f04_dtsg_162_smart_money_index_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """SMI proxy cumulative over 63d, normalised by close."""
    early = open_ - close.shift(1)
    late = close - open_
    smi = (late - early).rolling(QDAYS, min_periods=15).sum()
    return _safe_div(smi, close)


def f04_dtsg_163_open_close_vs_open_prev_divergence_42d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean(close-open) - Mean(open-prev_close) over 42d, normalised. Negative when late-day
    selling dominates early-day buying = distribution."""
    intra = (close - open_).rolling(42, min_periods=10).mean()
    overnight = (open_ - close.shift(1)).rolling(42, min_periods=10).mean()
    return _safe_div(intra - overnight, close.rolling(42, min_periods=10).mean())


def f04_dtsg_164_cum_net_buying_pressure_proxy_42d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative (close-open) * volume over 42d, normalised by close * mean(volume).
    Negative = sellers controlled the session in aggregate."""
    pres = ((close - open_) * volume).rolling(42, min_periods=10).sum()
    norm = (close.rolling(42, min_periods=10).mean()
            * volume.rolling(42, min_periods=10).mean()) * 42.0
    return _safe_div(pres, norm)


def f04_dtsg_165_williams_smart_money_composite_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams-style composite: ((close-open)/(high-low)) * volume, summed 21d, normalised."""
    rng = (high - low)
    body_frac = _safe_div(close - open_, rng)
    flow = (body_frac * volume).rolling(MDAYS, min_periods=5).sum()
    vsum = volume.rolling(MDAYS, min_periods=5).sum()
    return _safe_div(flow, vsum)


def f04_dtsg_166_power_hour_proxy_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Late-day strength proxy: (close - mid) / range over 21d. mid = (high+low)/2.
    Positive = late-day buying dominates; falling toward 0 = distribution."""
    mid = (high + low) / 2.0
    rng = (high - low)
    pos = _safe_div(close - mid, rng)
    return pos.rolling(MDAYS, min_periods=5).mean()


def f04_dtsg_167_monday_friday_close_strength_diff_63d(close: pd.Series) -> pd.Series:
    """Mean Friday return minus mean Monday return over 63d (calendar weekday).
    Positive = institutional Friday-mark-up pattern; turning negative is distribution-ish."""
    ret = close.pct_change()
    dow = pd.Series(close.index.dayofweek, index=close.index)
    fri = ret.where(dow == 4)
    mon = ret.where(dow == 0)
    # 63 trading days contain ~12-13 Fridays and Mondays; require >=3 to estimate
    return (fri.rolling(QDAYS, min_periods=3).mean()
            - mon.rolling(QDAYS, min_periods=3).mean())


def f04_dtsg_168_cumulative_gap_breakdown_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative net gap (open / prev_close - 1), separating up vs down gaps over 63d.
    (gap_up_sum + gap_down_sum) — negative = gap-down dominance = distribution."""
    gap = open_ / close.shift(1) - 1.0
    up = gap.where(gap > 0, 0.0).rolling(QDAYS, min_periods=15).sum()
    dn = gap.where(gap < 0, 0.0).rolling(QDAYS, min_periods=15).sum()
    return up + dn


# ============================================================
#  BUCKET C — IBD follow-through-day failure (169-173)
# ============================================================

def f04_dtsg_169_ftd_failure_event_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Follow-through day = close up >=1.25% on volume > prev day. FAILURE = within next 5
    bars, close falls below the FTD-bar's low (proxied as close on FTD day). Count in 63d."""
    ret = close.pct_change()
    ftd = (ret >= 0.0125) & (volume > volume.shift(1))
    ftd_arr = ftd.fillna(False).values
    c_arr = close.values
    n = len(close)
    fail = np.zeros(n, dtype="float64")
    for i in range(n):
        if not ftd_arr[i]:
            continue
        anchor = c_arr[i]
        end = min(n, i + 6)
        if any(c_arr[i + 1:end] < anchor):
            fail[i] = 1.0
    fail_s = pd.Series(fail, index=close.index)
    return fail_s.rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_170_dday_count_after_ftd_attempt_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-day count in the 42d AFTER the most recent FTD attempt.
    DD = close down >= 0.2% on rising volume."""
    ret = close.pct_change()
    ftd = (ret >= 0.0125) & (volume > volume.shift(1))
    dd = ((ret <= -0.002) & (volume > volume.shift(1))).astype(float)
    # bars since last FTD
    ftd_arr = ftd.fillna(False).values
    dd_arr = dd.fillna(0.0).values
    n = len(close)
    out = np.full(n, np.nan)
    last_ftd = -1
    for i in range(n):
        if ftd_arr[i]:
            last_ftd = i
        if last_ftd >= 0:
            lo = max(last_ftd, i - 42 + 1)
            out[i] = float(dd_arr[lo:i + 1].sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_171_ibd_m_pattern_score_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """IBD 'M' = two highs with declining volume. Score = (second_peak/first_peak in [0.97,1.03])
    AND (vol at second_peak < vol at first_peak). Locate two highest peaks in 126d window."""
    n = HDAYS
    c = close.values.astype("float64")
    v = volume.values.astype("float64")
    out = np.full(len(close), np.nan)
    min_periods = max(n // 3, 20)
    for i in range(min_periods - 1, len(close)):
        lo = max(0, i - n + 1)
        seg_c = c[lo:i + 1]
        seg_v = v[lo:i + 1]
        if np.isfinite(seg_c).sum() < min_periods:
            continue
        # two highest by close
        order = np.argsort(-seg_c)
        if len(order) < 2:
            continue
        p1 = order[0]
        # second peak must be at least 5 bars away
        p2 = next((idx for idx in order[1:] if abs(idx - p1) >= 5), None)
        if p2 is None:
            continue
        r1, r2 = seg_c[p1], seg_c[p2]
        vp1, vp2 = seg_v[p1], seg_v[p2]
        if r1 <= 0 or not np.isfinite(vp1) or not np.isfinite(vp2):
            continue
        ratio = r2 / r1
        near = 0.97 <= ratio <= 1.03
        decl = vp2 < vp1 if p2 > p1 else vp1 < vp2  # vol decline at the LATER peak
        out[i] = 1.0 if (near and decl) else 0.0
    return pd.Series(out, index=close.index)


def f04_dtsg_172_high_pivot_count_after_rally_failure_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count pivot-highs (3-bar) AFTER the last FTD-failure event, capped at 63d."""
    ret = close.pct_change()
    ftd = (ret >= 0.0125) & (volume > volume.shift(1))
    ftd_arr = ftd.fillna(False).values
    c = close.values
    n = len(close)
    fail_arr = np.zeros(n, dtype=bool)
    for i in range(n):
        if not ftd_arr[i]:
            continue
        end = min(n, i + 6)
        if any(c[i + 1:end] < c[i]):
            fail_arr[i] = True
    # pivot highs k=2
    piv = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
           & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)).fillna(False).values
    out = np.full(n, np.nan)
    last_fail = -1
    for i in range(n):
        if fail_arr[i]:
            last_fail = i
        if last_fail >= 0:
            lo = max(last_fail, i - QDAYS + 1)
            out[i] = float(piv[lo:i + 1].sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_173_stalling_action_day_count_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stalling day = close up in [0, 0.5%) AND volume > 1.25 * 50d mean (heavy vol, no progress).
    Count in 42d. Classic IBD distribution-day variant."""
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    cond = (ret >= 0.0) & (ret < 0.005) & (volume > 1.25 * vavg)
    return cond.astype(float).rolling(42, min_periods=10).sum()


# ============================================================
#  BUCKET D — Weinstein Stage 4 detection (174-179)
# ============================================================

def f04_dtsg_174_stage4_entry_below_30wk_sma(close: pd.Series) -> pd.Series:
    """Stage 4 entry indicator: close < SMA_150 (30-week) AND prior 21 bars had close above
    that SMA at least half the time (i.e. coming OUT of Stage 3)."""
    sma = close.rolling(WK30, min_periods=60).mean()
    below = (close < sma)
    prior_above = (close > sma).astype(float).rolling(MDAYS, min_periods=5).mean().shift(1)
    return (below & (prior_above >= 0.5)).astype(float)


def f04_dtsg_175_stage4_confirmed_sma_slope_negative(close: pd.Series) -> pd.Series:
    """Stage 4 confirmed: 30-week SMA slope (10-bar) < 0 AND close below it."""
    sma = close.rolling(WK30, min_periods=60).mean()
    sl = _rolling_slope(sma, 10, min_periods=5)
    return ((close < sma) & (sl < 0)).astype(float)


def f04_dtsg_176_stage4_duration_bars(close: pd.Series) -> pd.Series:
    """Bars since most recent Stage 4 confirmation (sma_30wk slope < 0 AND close < sma).
    Caps at 252; NaN if never confirmed in 252d lookback."""
    sma = close.rolling(WK30, min_periods=60).mean()
    sl = _rolling_slope(sma, 10, min_periods=5)
    conf = ((close < sma) & (sl < 0)).fillna(False).values
    out = np.full(len(close), np.nan)
    last = -1
    for i in range(len(close)):
        if conf[i]:
            last = i
            out[i] = 0.0
        elif last >= 0 and (i - last) <= YDAYS:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f04_dtsg_177_stage3_to_stage4_transition_speed(close: pd.Series) -> pd.Series:
    """Speed = 1 / (1 + bars from first close-below-SMA_150 to slope-turning-negative).
    Faster transition = sharper top. Looks back at last 126d."""
    sma = close.rolling(WK30, min_periods=60).mean()
    below = (close < sma).fillna(False).values
    sl = _rolling_slope(sma, 10, min_periods=5).fillna(0.0).values
    neg_sl = sl < 0
    out = np.full(len(close), np.nan)
    for i in range(HDAYS - 1, len(close)):
        lo = i - HDAYS + 1
        # earliest below in window
        seg_below = below[lo:i + 1]
        seg_negsl = neg_sl[lo:i + 1]
        if not seg_below.any() or not seg_negsl.any():
            continue
        first_below = int(np.argmax(seg_below))
        first_neg = int(np.argmax(seg_negsl))
        if first_neg < first_below:
            continue
        out[i] = 1.0 / (1.0 + (first_neg - first_below))
    return pd.Series(out, index=close.index)


def f04_dtsg_178_stage4_lower_low_acceleration_63d(low: pd.Series) -> pd.Series:
    """Stage-4 acceleration: slope of the rolling-21d MIN(low) over the last 63d.
    More negative = lower-lows are coming faster/deeper."""
    rmin = low.rolling(MDAYS, min_periods=5).min()
    return _rolling_slope(rmin, QDAYS, min_periods=20)


def f04_dtsg_179_stage4_magnitude_below_30wk_sma(close: pd.Series) -> pd.Series:
    """How far below 30-week SMA the close currently sits, in %: (close-sma)/sma.
    Negative; more negative = deeper into Stage 4."""
    sma = close.rolling(WK30, min_periods=60).mean()
    return _safe_div(close - sma, sma)


# ============================================================
#  BUCKET E — Cumulative-volume-delta proxies (180-185)
# ============================================================

def _cvd_bar(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Per-bar CVD proxy: +volume on up-close, -volume on down-close, 0 unchanged."""
    ret = close.pct_change()
    sign = pd.Series(np.where(ret > 0, 1.0, np.where(ret < 0, -1.0, 0.0)), index=close.index)
    return sign * volume


def f04_dtsg_180_cvd_21d_sum_normalised(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of per-bar CVD over 21d, normalised by sum of |CVD|."""
    cvd = _cvd_bar(close, volume)
    return _safe_div(cvd.rolling(MDAYS, min_periods=5).sum(),
                     cvd.abs().rolling(MDAYS, min_periods=5).sum())


def f04_dtsg_181_cvd_63d_sum_normalised(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of per-bar CVD over 63d, normalised by sum of |CVD|."""
    cvd = _cvd_bar(close, volume)
    return _safe_div(cvd.rolling(QDAYS, min_periods=15).sum(),
                     cvd.abs().rolling(QDAYS, min_periods=15).sum())


def f04_dtsg_182_cvd_slope_at_top_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of cumulative CVD over last 42d. Negative slope = net selling pressure."""
    cvd = _cvd_bar(close, volume).cumsum()
    return _rolling_slope(cvd, 42, min_periods=10)


def f04_dtsg_183_cvd_price_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence = sign(slope(price,63d)) * (-1) * sign(slope(CVD,63d)).
    +1 when price up but CVD down = bearish divergence at top."""
    cvd_cum = _cvd_bar(close, volume).cumsum()
    sp = _rolling_slope(close, QDAYS, min_periods=15)
    sv = _rolling_slope(cvd_cum, QDAYS, min_periods=15)
    return np.sign(sp) * (-1.0) * np.sign(sv)


def f04_dtsg_184_cvd_regime_reset_event_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CVD regime reset: count bars in 63d where cum-CVD crossed below its 21d mean
    after being above it (negative regime switch)."""
    cvd_cum = _cvd_bar(close, volume).cumsum()
    avg = cvd_cum.rolling(MDAYS, min_periods=5).mean()
    above = (cvd_cum > avg).astype(float)
    prev_above = above.shift(1).fillna(0.0)
    cross = ((prev_above > 0.5) & (above < 0.5)).astype(float)
    return cross.rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_185_cvd_acceleration_into_top_42d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration = slope(CVD_cum, 21d) - slope(CVD_cum, 42d). Negative & growing in
    magnitude = selling accelerating."""
    cvd_cum = _cvd_bar(close, volume).cumsum()
    s1 = _rolling_slope(cvd_cum, MDAYS, min_periods=5)
    s2 = _rolling_slope(cvd_cum, 42, min_periods=10)
    return s1 - s2


# ============================================================
#  BUCKET F — Hindenburg-Omen single-name internals (186-190)
# ============================================================

def f04_dtsg_186_hindenburg_warning_bar_count_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Warning bar = (high == 252d max) AND (vol > 1.5 * 50d avg) AND (close in lower-third of bar).
    Count in 42d (single-name Hindenburg-Omen proxy)."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    new_high = (high >= rmax * 0.9999)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.5 * vavg
    pos = _safe_div(close - low, high - low)
    poor = pos < (1.0 / 3.0)
    cond = new_high & heavy & poor
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_187_mixed_signal_day_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mixed = (high makes new 252d high) AND (close in lower-third of bar).
    The 'price up intraday but rejected at top' tell. Count in 63d."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    new_high = (high >= rmax * 0.9999)
    pos = _safe_div(close - low, high - low)
    cond = new_high & (pos < (1.0 / 3.0))
    return cond.astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_188_high_close_divergence_at_top_21d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high - close) / close over 21d, but only on bars where high is within 5% of 252d max.
    Larger = more daily-high-rejection at the top."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    near_top = (_safe_div(high, rmax) >= 0.95)
    div = _safe_div(high - close, close).where(near_top)
    # min_periods=1 so the metric is reported as long as at least 1 bar in the last 21
    # was near the top; returns NaN only when no near-top bar exists in the window.
    return div.rolling(MDAYS, min_periods=1).mean()


def f04_dtsg_189_heavy_vol_close_at_low_near_high_count_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar with heavy vol (>1.5x 50d avg), close at bar-low (pos<0.2), AND close within 5%
    of 252d high. Top-quality distribution candle. Count in 42d."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    near = (_safe_div(close, rmax) >= 0.95)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.5 * vavg
    pos = _safe_div(close - low, high - low)
    at_low = pos < 0.20
    cond = near & heavy & at_low
    return cond.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_190_hindenburg_aggregate_warning_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of three Hindenburg-style warning signals (rescaled) over 63d:
    warning_bar (186-style) + mixed-signal (187-style) + heavy-vol-poor-close (189-style)."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    new_high = (high >= rmax * 0.9999)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.5 * vavg
    pos = _safe_div(close - low, high - low)
    poor = pos < (1.0 / 3.0)
    at_low = pos < 0.20
    near_top = (_safe_div(high, rmax) >= 0.95)
    s1 = (new_high & heavy & poor).astype(float).rolling(QDAYS, min_periods=15).sum()
    s2 = (new_high & poor).astype(float).rolling(QDAYS, min_periods=15).sum()
    s3 = (near_top & heavy & at_low).astype(float).rolling(QDAYS, min_periods=15).sum()
    return s1 + s2 + s3


# ============================================================
#  BUCKET G — Wyckoff refinements (191-200)
# ============================================================

def f04_dtsg_191_wyckoff_creek_detection_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Creek (Phase B): gentle pullback inside the trading range. Detected as a sequence
    of 5+ bars where each bar's range is < ATR_21 AND close stays within 0.02 * range_mid.
    Count in 42d window."""
    atr = _atr(high, low, close, MDAYS)
    rng = high - low
    narrow = rng < atr
    rng_mid = ((high.rolling(42, min_periods=10).max()
                + low.rolling(42, min_periods=10).min()) / 2.0)
    near_mid = (_safe_div(close - rng_mid, rng_mid).abs() < 0.02)
    cond = (narrow & near_mid).astype(float)
    # rolling 5-bar block where all True
    blk = cond.rolling(5, min_periods=5).sum() >= 5
    return blk.astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_192_wyckoff_jump_across_creek_failure_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Jump-across-creek failure: close exceeds 21d max but within next 5 bars closes back
    below that prior 21d max. Count failures in 63d."""
    rmax21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    jump = (close > rmax21).fillna(False).values
    rmax_arr = rmax21.values
    c = close.values
    n = len(close)
    fail = np.zeros(n, dtype="float64")
    for i in range(n):
        if not jump[i]:
            continue
        thr = rmax_arr[i]
        if not np.isfinite(thr):
            continue
        end = min(n, i + 6)
        if any(c[i + 1:end] < thr):
            fail[i] = 1.0
    return pd.Series(fail, index=close.index).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_193_wyckoff_trading_range_midpoint_persistence_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Persistence: fraction of bars in 63d where close is within 20% (range-relative)
    of the rolling mid-point — proxies a tight Wyckoff trading-range mid."""
    hi = high.rolling(QDAYS, min_periods=15).max()
    lo = low.rolling(QDAYS, min_periods=15).min()
    mid = (hi + lo) / 2.0
    rng = (hi - lo)
    near = (_safe_div(close - mid, rng).abs() < 0.20).astype(float)
    return near.rolling(QDAYS, min_periods=15).mean()


def f04_dtsg_194_wyckoff_buying_climax_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """BCLX magnitude: max ((high-low)/ATR_21 * vol/vol_avg_50) over 63d on bars where
    high is within 2% of 63d max. Bigger = more climactic the buying climax."""
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.rolling(50, min_periods=10).mean()
    intensity = _safe_div(high - low, atr) * _safe_div(volume, vavg)
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near = (_safe_div(high, rmax) >= 0.98)
    masked = intensity.where(near)
    return masked.rolling(QDAYS, min_periods=15).max()


def f04_dtsg_195_wyckoff_automatic_reaction_depth_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR depth = (rolling63d_max_high - rolling-21d-min-low-after-peak) / (peak - 63d_min_low).
    Approximate as (max63 - min(low,21d)) / (max63 - min63)."""
    hi63 = high.rolling(QDAYS, min_periods=15).max()
    lo63 = low.rolling(QDAYS, min_periods=15).min()
    lo21 = low.rolling(MDAYS, min_periods=5).min()
    return _safe_div(hi63 - lo21, hi63 - lo63)


def f04_dtsg_196_wyckoff_secondary_test_success_rate_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ST success rate: ratio of (light-vol up bars near 63d-high) over (all up bars near
    63d-high) over 63d. Higher = more successful supply tests = topping."""
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near_top = _safe_div(high, rmax) >= 0.95
    vavg = volume.rolling(50, min_periods=10).mean()
    up = close > close.shift(1)
    light = volume < 0.8 * vavg
    n_top_up = (near_top & up).astype(float).rolling(QDAYS, min_periods=15).sum()
    n_st = (near_top & up & light).astype(float).rolling(QDAYS, min_periods=15).sum()
    return _safe_div(n_st, n_top_up)


def f04_dtsg_197_wyckoff_sow_sequence_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """SOW (Sign of Weakness) sequence: a wide-range down bar on heavy vol followed within
    5 bars by another lower close. Count sequences in 63d."""
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.rolling(50, min_periods=10).mean()
    wide_down = ((high - low) > 1.5 * atr) & (close < close.shift(1)) & (volume > 1.3 * vavg)
    wd = wide_down.fillna(False).values
    c = close.values
    n = len(close)
    seq = np.zeros(n, dtype="float64")
    for i in range(n):
        if not wd[i]:
            continue
        end = min(n, i + 6)
        if any(c[i + 1:end] < c[i]):
            seq[i] = 1.0
    return pd.Series(seq, index=close.index).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_198_wyckoff_phase_b_to_c_transition_speed_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Transition speed B->C: range-width change. (range_recent21d / range_prior42d). <1
    indicates compression-into-shakeout (typical B->C)."""
    rng = high - low
    r21 = rng.rolling(MDAYS, min_periods=5).mean()
    r42 = rng.rolling(42, min_periods=10).mean()
    return _safe_div(r21, r42)


def f04_dtsg_199_wyckoff_phase_c_to_d_entry_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase C->D entry: an UTAD-style upthrust (high makes new 21d high but close < open
    and vol > 1.3x 50d avg) followed within 10 bars by close < 21d low. Detect last 42d."""
    rmax21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    rmin21 = low.rolling(MDAYS, min_periods=5).min().shift(1)
    vavg = volume.rolling(50, min_periods=10).mean()
    # UTAD-proxy: new 21d high but close failed vs prior close, on heavy volume
    # (open not in signature, so prev-close is used as the failure reference)
    utad = (high > rmax21) & (close < close.shift(1)) & (volume > 1.3 * vavg)
    ut_arr = utad.fillna(False).values
    c = close.values
    lo_arr = rmin21.values
    n = len(close)
    ev = np.zeros(n, dtype="float64")
    for i in range(n):
        if not ut_arr[i]:
            continue
        thr = lo_arr[i]
        if not np.isfinite(thr):
            continue
        end = min(n, i + 11)
        if any(c[i + 1:end] < thr):
            ev[i] = 1.0
    return pd.Series(ev, index=close.index).rolling(42, min_periods=10).sum()


def f04_dtsg_200_wyckoff_dist_vs_accum_classifier_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-vs-accumulation classifier:
       +1 = distribution-like (heavy-vol up-bars closing poorly + supply tests dominate),
       -1 = accumulation-like (heavy-vol down-bars closing strong),
        0 = ambiguous. Computed over 63d as a normalised diff."""
    pos = _safe_div(close - low, high - low)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.3 * vavg
    up = close > close.shift(1)
    dn = close < close.shift(1)
    dist_bar = (heavy & up & (pos < 0.4)).astype(float).rolling(QDAYS, min_periods=15).sum()
    accum_bar = (heavy & dn & (pos > 0.6)).astype(float).rolling(QDAYS, min_periods=15).sum()
    return _safe_div(dist_bar - accum_bar, dist_bar + accum_bar)


# ============================================================
#  BUCKET H — Rounding vs sharp distribution (201-206)
# ============================================================

def f04_dtsg_201_rounding_top_arc_fit_r2_63d(close: pd.Series) -> pd.Series:
    """Fit a downward-opening parabola (deg=2) over 63d log-prices; report R^2.
    High R^2 with negative leading coef = clean rounding top."""
    n = QDAYS
    min_periods = max(n // 3, 20)
    lp = _safe_log(close).values

    def _r2(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]
            w = w[valid]
        try:
            coef = np.polyfit(x, w, 2)
        except Exception:
            return np.nan
        if coef[0] >= 0:
            return 0.0  # not a top arc
        pred = np.polyval(coef, x)
        ss_res = ((w - pred) ** 2).sum()
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        return float(1.0 - ss_res / ss_tot)

    return pd.Series(lp, index=close.index).rolling(n, min_periods=min_periods).apply(_r2, raw=True)


def f04_dtsg_202_sharp_top_kurtosis_42d(close: pd.Series) -> pd.Series:
    """Kurtosis of log returns over 42d — high kurtosis = fat tails = spike-top distribution."""
    lr = _safe_log(close).diff()
    return lr.rolling(42, min_periods=10).kurt()


def f04_dtsg_203_rounding_vs_sharp_classifier_63d(close: pd.Series) -> pd.Series:
    """Rounding-vs-sharp = R2(parabola) - normalised_kurtosis.
    >0 = rounding-top character; <0 = spike-top character."""
    r2 = f04_dtsg_201_rounding_top_arc_fit_r2_63d(close)
    k = f04_dtsg_202_sharp_top_kurtosis_42d(close)
    k_norm = _safe_div(k - k.rolling(YDAYS, min_periods=60).mean(),
                       k.rolling(YDAYS, min_periods=60).std(ddof=0))
    return r2.fillna(0.0) - k_norm.fillna(0.0)


def f04_dtsg_204_time_spent_near_peak_ratio_63d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Dwell vs spike: fraction of 63d close within 3% of 63d max."""
    rmax = close.rolling(QDAYS, min_periods=15).max()
    near = (_safe_div(close, rmax) >= 0.97).astype(float)
    return near.rolling(QDAYS, min_periods=15).mean()


def f04_dtsg_205_distribution_shape_symmetry_63d(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Left-vs-right volume symmetry around the 63d argmax(close).
    abs(left_vol - right_vol) / total_vol; 0 = perfectly symmetric, 1 = highly asymmetric."""
    n = QDAYS
    min_periods = max(n // 3, 15)
    c = close.values
    v = volume.values
    out = np.full(len(close), np.nan)
    for i in range(min_periods - 1, len(close)):
        lo = max(0, i - n + 1)
        seg_c = c[lo:i + 1]
        seg_v = v[lo:i + 1]
        m = np.isfinite(seg_c) & np.isfinite(seg_v)
        if m.sum() < min_periods:
            continue
        peak = int(np.nanargmax(seg_c))
        left_v = float(np.nansum(seg_v[:peak])) if peak > 0 else 0.0
        right_v = float(np.nansum(seg_v[peak + 1:])) if peak < len(seg_v) - 1 else 0.0
        tot = left_v + right_v
        if tot <= 0:
            continue
        out[i] = abs(left_v - right_v) / tot
    return pd.Series(out, index=close.index)


def f04_dtsg_206_distribution_shape_stability_multi_window(close: pd.Series) -> pd.Series:
    """Shape-stability: std of R^2(arc-fit) across windows {42d, 63d, 84d}. Low std = stable
    rounding shape across horizons; high std = ambiguous."""
    def _r2(n):
        min_periods = max(n // 3, 15)
        lp = _safe_log(close).values

        def f(w):
            valid = ~np.isnan(w)
            if valid.sum() < min_periods:
                return np.nan
            x = np.arange(len(w), dtype=float)
            if not valid.all():
                x = x[valid]
                w = w[valid]
            try:
                coef = np.polyfit(x, w, 2)
            except Exception:
                return np.nan
            if coef[0] >= 0:
                return 0.0
            pred = np.polyval(coef, x)
            ss_res = ((w - pred) ** 2).sum()
            ss_tot = ((w - w.mean()) ** 2).sum()
            if ss_tot == 0:
                return np.nan
            return float(1.0 - ss_res / ss_tot)
        return pd.Series(lp, index=close.index).rolling(n, min_periods=min_periods).apply(f, raw=True)

    a = _r2(42); b = _r2(63); c = _r2(84)
    return pd.concat([a, b, c], axis=1).std(axis=1)


# ============================================================
#  BUCKET I — Bar-level distribution signatures (207-214)
# ============================================================

def f04_dtsg_207_inside_bar_after_new_high_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside bar (high<prev_high AND low>prev_low) IMMEDIATELY after a new 252d high.
    Count of (prev was new 252d high AND today inside) over 63d."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    prev_new_high = (high.shift(1) >= rmax.shift(1) * 0.9999)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    cond = prev_new_high & inside
    return cond.fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_208_outside_bar_bearish_at_top_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish outside bar at the top: high>prev_high AND low<prev_low AND close<prev_close
    AND high within 5% of 252d max. Count in 63d."""
    rmax = high.rolling(YDAYS, min_periods=63).max()
    near = (_safe_div(high, rmax) >= 0.95)
    out_bar = ((high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1)))
    return (near & out_bar).fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_209_single_day_reversal_at_distribution_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Single-day reversal: high makes new 21d high but close < open-proxy (= prev close),
    i.e. close < prev_close. Count in 63d (reversal-of-direction at top)."""
    rmax21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    new_high = (high > rmax21)
    reversed_ = (close < close.shift(1))
    cond = new_high & reversed_
    return cond.fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_210_lowry_90pct_down_day_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lowry-style 90% down-day proxy: close in bottom 10% of bar range AND |return|>1% AND
    vol>1.3x 50d avg. Count in 63d."""
    pos = _safe_div(close - low, high - low)
    ret = close.pct_change()
    vavg = volume.rolling(50, min_periods=10).mean()
    cond = (pos < 0.10) & (ret < -0.01) & (volume > 1.3 * vavg)
    return cond.fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_211_bearish_engulfing_heavy_vol_at_top_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish engulfing on heavy vol near top: today's range engulfs yesterday's
    (high>prev_high AND low<prev_low) AND close < prev_close AND vol > 1.3x 50d avg AND
    high within 5% of 63d max. Count in 63d."""
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near = (_safe_div(high, rmax) >= 0.95)
    eng = (high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1))
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.3 * vavg
    cond = near & eng & heavy
    return cond.fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_212_distribution_bar_clustering_index_42d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Clustering index: max number of distribution-bars (heavy vol + close in lower third)
    inside any rolling-7d window within the last 42d. Higher = more concentrated."""
    pos = _safe_div(close - low, high - low)
    vavg = volume.rolling(50, min_periods=10).mean()
    db = ((pos < (1.0 / 3.0)) & (volume > 1.3 * vavg)).astype(float)
    cluster7 = db.rolling(7, min_periods=3).sum()
    return cluster7.rolling(42, min_periods=10).max()


def f04_dtsg_213_bar_range_expansion_top_count_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in 42d where range > 2 * ATR_21 AND high is within 5% of 63d max."""
    atr = _atr(high, low, close, MDAYS)
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near = (_safe_div(high, rmax) >= 0.95)
    expand = (high - low) > 2.0 * atr
    cond = near & expand
    return cond.fillna(False).astype(float).rolling(42, min_periods=10).sum()


def f04_dtsg_214_bar_range_contraction_top_count_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in 42d where range < 0.5 * ATR_21 AND high within 5% of 63d max (coiling at top)."""
    atr = _atr(high, low, close, MDAYS)
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near = (_safe_div(high, rmax) >= 0.95)
    contract = (high - low) < 0.5 * atr
    cond = near & contract
    return cond.fillna(False).astype(float).rolling(42, min_periods=10).sum()


# ============================================================
#  BUCKET J — Anchored-VWAP-from-distribution-peak (215-218)
# ============================================================

def _avwap_from_peak(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, window: int = HDAYS) -> pd.Series:
    """Locate the right-anchored argmax(close) within `window`; compute AVWAP from that
    anchor bar through current bar, returned as a series aligned to current bar."""
    tp = _typical(high, low, close).values.astype("float64")
    v = volume.values.astype("float64")
    c = close.values.astype("float64")
    n = len(close)
    out = np.full(n, np.nan)
    min_periods = max(window // 3, 20)
    for i in range(min_periods - 1, n):
        lo = max(0, i - window + 1)
        seg_c = c[lo:i + 1]
        valid = np.isfinite(seg_c)
        if valid.sum() < min_periods:
            continue
        peak_off = int(np.nanargmax(seg_c))
        anchor = lo + peak_off
        if anchor > i:
            continue
        pv = tp[anchor:i + 1] * v[anchor:i + 1]
        vv = v[anchor:i + 1]
        m = np.isfinite(pv) & np.isfinite(vv) & (vv > 0)
        if m.sum() < 1:
            continue
        out[i] = float(pv[m].sum() / vv[m].sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_215_avwap_from_peak_distance(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - AVWAP_from_peak) / AVWAP_from_peak. Negative = below the volume-weighted
    average price computed from the peak — late stage of distribution."""
    av = _avwap_from_peak(high, low, close, volume, window=HDAYS)
    return _safe_div(close - av, av)


def f04_dtsg_216_avwap_from_peak_time_below_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where close < AVWAP_from_peak."""
    av = _avwap_from_peak(high, low, close, volume, window=HDAYS)
    below = (close < av).astype(float)
    return below.rolling(QDAYS, min_periods=15).mean()


def f04_dtsg_217_avwap_from_peak_rejection_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rejection = bar where close moves from below AVWAP_from_peak to touch >= AVWAP
    intraday (high>=AVWAP) but closes back below. Count in 63d."""
    av = _avwap_from_peak(high, low, close, volume, window=HDAYS)
    touched = (high >= av) & (close < av) & (close.shift(1) < av.shift(1))
    return touched.fillna(False).astype(float).rolling(QDAYS, min_periods=15).sum()


def f04_dtsg_218_avwap_from_peak_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of AVWAP_from_peak over last 63d. Negative & deepening = price-side AVWAP
    is dragged lower bar by bar = distribution maturity."""
    av = _avwap_from_peak(high, low, close, volume, window=HDAYS)
    return _rolling_slope(av, QDAYS, min_periods=15)


# ============================================================
#  BUCKET K — Phase-transition / time-decay (219-222)
# ============================================================

def f04_dtsg_219_time_decay_weighted_distribution_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Time-decay-weighted dday score: dday flag * exp(-(63-i)/21) summed over 63d.
    Recent distribution-days carry more weight."""
    ret = close.pct_change()
    dd = ((ret <= -0.002) & (volume > volume.shift(1))).astype(float)
    n = QDAYS
    weights = np.exp(-np.arange(n - 1, -1, -1) / float(MDAYS))
    weights /= weights.sum()
    dd_arr = dd.fillna(0.0).values
    out = np.full(len(close), np.nan)
    min_periods = max(n // 3, 15)
    for i in range(min_periods - 1, len(close)):
        lo = max(0, i - n + 1)
        seg = dd_arr[lo:i + 1]
        if len(seg) < n:
            ws = np.exp(-np.arange(len(seg) - 1, -1, -1) / float(MDAYS))
            ws /= ws.sum()
            out[i] = float((seg * ws).sum())
        else:
            out[i] = float((seg * weights).sum())
    return pd.Series(out, index=close.index)


def f04_dtsg_220_phase_progression_imminence_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Imminence = (recent 21d SOW-count) - (recent 21d ST-count), both as fractions.
    Larger = more weakness vs more upper-test = phase D-imminent."""
    # SOW proxy
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.rolling(50, min_periods=10).mean()
    sow = ((high - low > 1.5 * atr) & (close < close.shift(1)) & (volume > 1.3 * vavg))
    # ST proxy
    rmax = high.rolling(QDAYS, min_periods=15).max()
    near = _safe_div(high, rmax) >= 0.95
    up = close > close.shift(1)
    light = volume < 0.8 * vavg
    st = near & up & light
    sow_f = sow.astype(float).rolling(MDAYS, min_periods=5).mean()
    st_f = st.astype(float).rolling(MDAYS, min_periods=5).mean()
    return sow_f - st_f


def f04_dtsg_221_distribution_maturity_stage_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maturity stage (early=0, mid=1, late=2). Heuristic:
       early = ATR contraction without SMA200 breach,
       mid   = lower-high count >= 3 with close > SMA200,
       late  = close < SMA200 AND CVD slope < 0."""
    sma200 = close.rolling(200, min_periods=60).mean()
    atr_short = _atr(high, low, close, MDAYS)
    atr_long = _atr(high, low, close, QDAYS)
    contract = atr_short < atr_long
    # lower-high pivot count (k=2) over 63d
    piv_high = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
                & (high.shift(2) > high.shift(1)) & (high.shift(2) > high)).fillna(False)
    centered = high.shift(2).where(piv_high)
    lh = (centered.ffill().diff() < 0).astype(float)
    lh_count = lh.rolling(QDAYS, min_periods=15).sum()
    cvd_cum = _cvd_bar(close, volume).cumsum()
    cvd_sl = _rolling_slope(cvd_cum, 42, min_periods=10)
    early = (contract & (close > sma200))
    mid = (lh_count >= 3) & (close > sma200)
    late = (close < sma200) & (cvd_sl < 0)
    stage = pd.Series(np.where(late, 2.0, np.where(mid, 1.0, np.where(early, 0.0, np.nan))),
                      index=close.index)
    return stage


def f04_dtsg_222_dist_vs_reaccum_probability_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-vs-reaccumulation probability proxy:
       sigmoid( z(dist_signals) - z(reaccum_signals) ), each over 63d.
       dist signals: distbar count, CVD slope negative.
       reaccum signals: heavy-vol-up-bars closing strong, CVD slope positive."""
    pos = _safe_div(close - low, high - low)
    vavg = volume.rolling(50, min_periods=10).mean()
    heavy = volume > 1.3 * vavg
    up = close > close.shift(1)
    dn = close < close.shift(1)
    distbar = (heavy & dn & (pos < (1.0 / 3.0))).astype(float).rolling(QDAYS, min_periods=15).sum()
    accbar = (heavy & up & (pos > (2.0 / 3.0))).astype(float).rolling(QDAYS, min_periods=15).sum()
    cvd_cum = _cvd_bar(close, volume).cumsum()
    cvd_sl = _rolling_slope(cvd_cum, QDAYS, min_periods=15)
    z_dist = _zsc(distbar).fillna(0.0) + _zsc(-cvd_sl).fillna(0.0)
    z_acc = _zsc(accbar).fillna(0.0) + _zsc(cvd_sl).fillna(0.0)
    diff = z_dist - z_acc
    return 1.0 / (1.0 + np.exp(-diff))


# ============================================================
#  BUCKET L — Narrow dtsg-internal composites (223-225)
# ============================================================

def f04_dtsg_223_vp_smartmoney_cvd_joint_score_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Joint score = z(-(close-VAH)/VAH) + z(-SMI_63) + z(-cvd_slope_63).
    Higher = volume-profile, smart-money, and CVD all pointing to distribution."""
    pm = _poc_metrics(high, low, close, volume, QDAYS)
    vah_dist = _safe_div(close - pm["vah"], pm["vah"])
    early = open_ - close.shift(1)
    late = close - open_
    smi = (late - early).rolling(QDAYS, min_periods=15).sum()
    cvd_cum = _cvd_bar(close, volume).cumsum()
    cvd_sl = _rolling_slope(cvd_cum, QDAYS, min_periods=15)
    return (_zsc(-vah_dist).fillna(0.0)
            + _zsc(-smi).fillna(0.0)
            + _zsc(-cvd_sl).fillna(0.0))


def f04_dtsg_224_wyckoff_refinement_aggregate_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate of new Wyckoff refinement signals normalised over 63d:
       creek + jump-failure + SOW-sequence + dist-vs-accum-classifier."""
    creek = f04_dtsg_191_wyckoff_creek_detection_42d(high, low, close)
    jump = f04_dtsg_192_wyckoff_jump_across_creek_failure_63d(high, close)
    sow = f04_dtsg_197_wyckoff_sow_sequence_count_63d(high, low, close, volume)
    cls = f04_dtsg_200_wyckoff_dist_vs_accum_classifier_63d(high, low, close, volume)
    return (_zsc(creek).fillna(0.0)
            + _zsc(jump).fillna(0.0)
            + _zsc(sow).fillna(0.0)
            + _zsc(cls).fillna(0.0))


def f04_dtsg_225_terminal_distribution_process_composite_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal-distribution-process composite — sums (z) of:
       Stage4 confirmation, AVWAP-from-peak distance (negative), CVD slope (negative),
       Hindenburg warning count, time-decay-weighted DD score."""
    sma = close.rolling(WK30, min_periods=60).mean()
    sl = _rolling_slope(sma, 10, min_periods=5)
    s4 = ((close < sma) & (sl < 0)).astype(float)
    av = _avwap_from_peak(high, low, close, volume, window=HDAYS)
    av_dist = _safe_div(close - av, av)
    cvd_cum = _cvd_bar(close, volume).cumsum()
    cvd_sl = _rolling_slope(cvd_cum, QDAYS, min_periods=15)
    hb = f04_dtsg_186_hindenburg_warning_bar_count_42d(high, low, close, volume)
    td = f04_dtsg_219_time_decay_weighted_distribution_score_63d(close, volume)
    return (_zsc(s4).fillna(0.0)
            + _zsc(-av_dist).fillna(0.0)
            + _zsc(-cvd_sl).fillna(0.0)
            + _zsc(hb).fillna(0.0)
            + _zsc(td).fillna(0.0))


# =====================================================================
#  REGISTRY
# =====================================================================

DISTRIBUTION_TOP_SIGNATURE_BASE_REGISTRY_151_225 = {
    "f04_dtsg_151_vwap_21d_distance": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_151_vwap_21d_distance},
    "f04_dtsg_152_vwap_63d_distance": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_152_vwap_63d_distance},
    "f04_dtsg_153_vwap_252d_distance": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_153_vwap_252d_distance},
    "f04_dtsg_154_poc_distance_to_close_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_154_poc_distance_to_close_63d},
    "f04_dtsg_155_value_area_high_distance_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_155_value_area_high_distance_63d},
    "f04_dtsg_156_value_area_low_distance_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_156_value_area_low_distance_63d},
    "f04_dtsg_157_days_inside_value_area_21d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_157_days_inside_value_area_21d},
    "f04_dtsg_158_single_print_bar_count_at_top_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_158_single_print_bar_count_at_top_63d},
    "f04_dtsg_159_vah_val_range_width_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_159_vah_val_range_width_63d},
    "f04_dtsg_160_vol_weighted_skew_around_poc_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_160_vol_weighted_skew_around_poc_63d},
    "f04_dtsg_161_smart_money_index_21d": {"inputs": ["open", "close"], "func": f04_dtsg_161_smart_money_index_21d},
    "f04_dtsg_162_smart_money_index_63d": {"inputs": ["open", "close"], "func": f04_dtsg_162_smart_money_index_63d},
    "f04_dtsg_163_open_close_vs_open_prev_divergence_42d": {"inputs": ["open", "close"], "func": f04_dtsg_163_open_close_vs_open_prev_divergence_42d},
    "f04_dtsg_164_cum_net_buying_pressure_proxy_42d": {"inputs": ["open", "close", "volume"], "func": f04_dtsg_164_cum_net_buying_pressure_proxy_42d},
    "f04_dtsg_165_williams_smart_money_composite_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f04_dtsg_165_williams_smart_money_composite_21d},
    "f04_dtsg_166_power_hour_proxy_21d": {"inputs": ["open", "high", "low", "close"], "func": f04_dtsg_166_power_hour_proxy_21d},
    "f04_dtsg_167_monday_friday_close_strength_diff_63d": {"inputs": ["close"], "func": f04_dtsg_167_monday_friday_close_strength_diff_63d},
    "f04_dtsg_168_cumulative_gap_breakdown_63d": {"inputs": ["open", "close"], "func": f04_dtsg_168_cumulative_gap_breakdown_63d},
    "f04_dtsg_169_ftd_failure_event_count_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_169_ftd_failure_event_count_63d},
    "f04_dtsg_170_dday_count_after_ftd_attempt_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_170_dday_count_after_ftd_attempt_42d},
    "f04_dtsg_171_ibd_m_pattern_score_126d": {"inputs": ["close", "volume"], "func": f04_dtsg_171_ibd_m_pattern_score_126d},
    "f04_dtsg_172_high_pivot_count_after_rally_failure_63d": {"inputs": ["high", "close", "volume"], "func": f04_dtsg_172_high_pivot_count_after_rally_failure_63d},
    "f04_dtsg_173_stalling_action_day_count_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_173_stalling_action_day_count_42d},
    "f04_dtsg_174_stage4_entry_below_30wk_sma": {"inputs": ["close"], "func": f04_dtsg_174_stage4_entry_below_30wk_sma},
    "f04_dtsg_175_stage4_confirmed_sma_slope_negative": {"inputs": ["close"], "func": f04_dtsg_175_stage4_confirmed_sma_slope_negative},
    "f04_dtsg_176_stage4_duration_bars": {"inputs": ["close"], "func": f04_dtsg_176_stage4_duration_bars},
    "f04_dtsg_177_stage3_to_stage4_transition_speed": {"inputs": ["close"], "func": f04_dtsg_177_stage3_to_stage4_transition_speed},
    "f04_dtsg_178_stage4_lower_low_acceleration_63d": {"inputs": ["low"], "func": f04_dtsg_178_stage4_lower_low_acceleration_63d},
    "f04_dtsg_179_stage4_magnitude_below_30wk_sma": {"inputs": ["close"], "func": f04_dtsg_179_stage4_magnitude_below_30wk_sma},
    "f04_dtsg_180_cvd_21d_sum_normalised": {"inputs": ["close", "volume"], "func": f04_dtsg_180_cvd_21d_sum_normalised},
    "f04_dtsg_181_cvd_63d_sum_normalised": {"inputs": ["close", "volume"], "func": f04_dtsg_181_cvd_63d_sum_normalised},
    "f04_dtsg_182_cvd_slope_at_top_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_182_cvd_slope_at_top_42d},
    "f04_dtsg_183_cvd_price_divergence_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_183_cvd_price_divergence_63d},
    "f04_dtsg_184_cvd_regime_reset_event_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_184_cvd_regime_reset_event_63d},
    "f04_dtsg_185_cvd_acceleration_into_top_42d": {"inputs": ["close", "volume"], "func": f04_dtsg_185_cvd_acceleration_into_top_42d},
    "f04_dtsg_186_hindenburg_warning_bar_count_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_186_hindenburg_warning_bar_count_42d},
    "f04_dtsg_187_mixed_signal_day_count_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_187_mixed_signal_day_count_63d},
    "f04_dtsg_188_high_close_divergence_at_top_21d": {"inputs": ["high", "close"], "func": f04_dtsg_188_high_close_divergence_at_top_21d},
    "f04_dtsg_189_heavy_vol_close_at_low_near_high_count_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_189_heavy_vol_close_at_low_near_high_count_42d},
    "f04_dtsg_190_hindenburg_aggregate_warning_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_190_hindenburg_aggregate_warning_score_63d},
    "f04_dtsg_191_wyckoff_creek_detection_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_191_wyckoff_creek_detection_42d},
    "f04_dtsg_192_wyckoff_jump_across_creek_failure_63d": {"inputs": ["high", "close"], "func": f04_dtsg_192_wyckoff_jump_across_creek_failure_63d},
    "f04_dtsg_193_wyckoff_trading_range_midpoint_persistence_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_193_wyckoff_trading_range_midpoint_persistence_63d},
    "f04_dtsg_194_wyckoff_buying_climax_magnitude_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_194_wyckoff_buying_climax_magnitude_63d},
    "f04_dtsg_195_wyckoff_automatic_reaction_depth_ratio_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_195_wyckoff_automatic_reaction_depth_ratio_63d},
    "f04_dtsg_196_wyckoff_secondary_test_success_rate_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_196_wyckoff_secondary_test_success_rate_63d},
    "f04_dtsg_197_wyckoff_sow_sequence_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_197_wyckoff_sow_sequence_count_63d},
    "f04_dtsg_198_wyckoff_phase_b_to_c_transition_speed_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_198_wyckoff_phase_b_to_c_transition_speed_63d},
    "f04_dtsg_199_wyckoff_phase_c_to_d_entry_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_199_wyckoff_phase_c_to_d_entry_42d},
    "f04_dtsg_200_wyckoff_dist_vs_accum_classifier_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_200_wyckoff_dist_vs_accum_classifier_63d},
    "f04_dtsg_201_rounding_top_arc_fit_r2_63d": {"inputs": ["close"], "func": f04_dtsg_201_rounding_top_arc_fit_r2_63d},
    "f04_dtsg_202_sharp_top_kurtosis_42d": {"inputs": ["close"], "func": f04_dtsg_202_sharp_top_kurtosis_42d},
    "f04_dtsg_203_rounding_vs_sharp_classifier_63d": {"inputs": ["close"], "func": f04_dtsg_203_rounding_vs_sharp_classifier_63d},
    "f04_dtsg_204_time_spent_near_peak_ratio_63d": {"inputs": ["high", "close"], "func": f04_dtsg_204_time_spent_near_peak_ratio_63d},
    "f04_dtsg_205_distribution_shape_symmetry_63d": {"inputs": ["volume", "close"], "func": f04_dtsg_205_distribution_shape_symmetry_63d},
    "f04_dtsg_206_distribution_shape_stability_multi_window": {"inputs": ["close"], "func": f04_dtsg_206_distribution_shape_stability_multi_window},
    "f04_dtsg_207_inside_bar_after_new_high_count_63d": {"inputs": ["high", "low"], "func": f04_dtsg_207_inside_bar_after_new_high_count_63d},
    "f04_dtsg_208_outside_bar_bearish_at_top_count_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_208_outside_bar_bearish_at_top_count_63d},
    "f04_dtsg_209_single_day_reversal_at_distribution_count_63d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_209_single_day_reversal_at_distribution_count_63d},
    "f04_dtsg_210_lowry_90pct_down_day_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_210_lowry_90pct_down_day_count_63d},
    "f04_dtsg_211_bearish_engulfing_heavy_vol_at_top_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_211_bearish_engulfing_heavy_vol_at_top_count_63d},
    "f04_dtsg_212_distribution_bar_clustering_index_42d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_212_distribution_bar_clustering_index_42d},
    "f04_dtsg_213_bar_range_expansion_top_count_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_213_bar_range_expansion_top_count_42d},
    "f04_dtsg_214_bar_range_contraction_top_count_42d": {"inputs": ["high", "low", "close"], "func": f04_dtsg_214_bar_range_contraction_top_count_42d},
    "f04_dtsg_215_avwap_from_peak_distance": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_215_avwap_from_peak_distance},
    "f04_dtsg_216_avwap_from_peak_time_below_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_216_avwap_from_peak_time_below_63d},
    "f04_dtsg_217_avwap_from_peak_rejection_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_217_avwap_from_peak_rejection_count_63d},
    "f04_dtsg_218_avwap_from_peak_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_218_avwap_from_peak_slope_63d},
    "f04_dtsg_219_time_decay_weighted_distribution_score_63d": {"inputs": ["close", "volume"], "func": f04_dtsg_219_time_decay_weighted_distribution_score_63d},
    "f04_dtsg_220_phase_progression_imminence_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_220_phase_progression_imminence_63d},
    "f04_dtsg_221_distribution_maturity_stage_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_221_distribution_maturity_stage_63d},
    "f04_dtsg_222_dist_vs_reaccum_probability_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_222_dist_vs_reaccum_probability_63d},
    "f04_dtsg_223_vp_smartmoney_cvd_joint_score_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f04_dtsg_223_vp_smartmoney_cvd_joint_score_63d},
    "f04_dtsg_224_wyckoff_refinement_aggregate_63d": {"inputs": ["high", "low", "close", "volume"], "func": f04_dtsg_224_wyckoff_refinement_aggregate_63d},
    "f04_dtsg_225_terminal_distribution_process_composite_63d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f04_dtsg_225_terminal_distribution_process_composite_63d},
}
