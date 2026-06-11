"""turnover_and_churn base features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. DISTINCT concepts NOT covered:

- Pocket Pivots (O'Neil) — volume > max-down-vol-10d AND close > 10d-SMA
- Volume Dry Up (VDU) — lowest 5d volume in 21d near 21d high
- Volatility Contraction Pattern (VCP) — successively smaller pullbacks
- Distribution days with O'Neil 25d-decay / 5%-erase rules
- Pre-breakout setups (volume buildup, ATR compression, tight base, cup-with-handle)
- Effective Volume (Pascal Willain) — volume × close-position-in-range
- Trin / Arms Index proxy via close-strength weighted volume
- Volume profile VAH/VAL — high/low volume node distances + value-area width
- Sequential consolidation (NR7+NR7, NR7+inside bar, multiple inside runs)
- Wide-range bar with weak / strong close (engulfing exhaustion)
- Volatility expansion 1→2 ATR events + regime classifier
- Volume cascade after WRB / silent vs clear followthrough
- Composite top/bottom signatures

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


def _streak(condition):
    grp = (~condition).cumsum()
    return condition.astype(int).groupby(grp).cumsum().astype(float)


# ============================================================
# Bucket A — Pocket Pivots (O'Neil) (151-157)
# ============================================================

def f24_tnch_151_pocket_pivot_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """O'Neil pocket pivot: today's volume > max down-day volume in prior 10 bars AND close > open (up day) AND close > 10d-SMA."""
    dn_vol = volume.where(close < close.shift(1), 0.0)
    max_dn_vol_10 = dn_vol.rolling(10, min_periods=10).max()
    up_day = (close > close.shift(1))
    sma10 = close.rolling(10, min_periods=10).mean()
    return ((volume > max_dn_vol_10) & up_day & (close > sma10)).astype(float)


def f24_tnch_152_pocket_pivot_count_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pocket pivot count in trailing 21d."""
    return f24_tnch_151_pocket_pivot_indicator(close, volume).rolling(MDAYS, min_periods=WDAYS).sum()


def f24_tnch_153_pocket_pivot_count_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pocket pivot count in trailing 63d."""
    return f24_tnch_151_pocket_pivot_indicator(close, volume).rolling(QDAYS, min_periods=MDAYS).sum()


def f24_tnch_154_pocket_pivot_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pocket pivot count in trailing 252d — institutional accumulation footprint."""
    return f24_tnch_151_pocket_pivot_indicator(close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_155_bars_since_last_pocket_pivot(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the most recent pocket pivot event."""
    ev = f24_tnch_151_pocket_pivot_indicator(close, volume).astype(bool)
    return _bars_since(ev)


def f24_tnch_156_pocket_pivot_at_or_above_50d_sma_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pocket pivot on a day where close >= 50d-SMA — premium institutional buy."""
    pp = f24_tnch_151_pocket_pivot_indicator(close, volume).astype(bool)
    sma50 = close.rolling(50, min_periods=20).mean()
    return (pp & (close >= sma50)).astype(float)


def f24_tnch_157_pocket_pivot_with_followthrough_5d_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of pocket pivots in last 252d that were followed by close 5d later being higher (PIT-safe via lag)."""
    pp_lag = f24_tnch_151_pocket_pivot_indicator(close, volume).shift(WDAYS).fillna(0).astype(bool)
    higher_5d_later = (close > close.shift(WDAYS))
    return (pp_lag & higher_5d_later).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket B — Volume Dry Up (VDU) (158-162)
# ============================================================

def f24_tnch_158_vdu_5d_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VDU: today's 5d-avg volume is the lowest in trailing 21d AND close is within 5% of 21d high — coiled spring at highs."""
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    v5_min_21 = v5.rolling(MDAYS, min_periods=WDAYS).min()
    hi21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    near_high = (close >= 0.95 * hi21)
    return ((v5 == v5_min_21) & near_high).astype(float)


def f24_tnch_159_vdu_5d_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of VDU events in trailing 63d."""
    return f24_tnch_158_vdu_5d_indicator(high, low, close, volume).rolling(QDAYS, min_periods=MDAYS).sum()


def f24_tnch_160_vdu_followed_by_pocket_pivot_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of VDU events (in last 252d, 5+ bars old) followed by a pocket pivot within 5 bars."""
    vdu_lag = f24_tnch_158_vdu_5d_indicator(high, low, close, volume).shift(WDAYS).fillna(0).astype(bool)
    pp = f24_tnch_151_pocket_pivot_indicator(close, volume)
    pp_in_5 = pp.rolling(WDAYS, min_periods=1).sum() > 0
    return (vdu_lag & pp_in_5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_161_vdu_to_breakout_velocity_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean bars-to-breakout (close > 21d high) following VDU in last 252d (capped at 21 bars)."""
    vdu = f24_tnch_158_vdu_5d_indicator(high, low, close, volume).astype(bool).to_numpy()
    hi21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    close_arr = close.to_numpy(); hi_arr = hi21.to_numpy()
    n = len(close); times = []
    for i in range(n - MDAYS):
        if not vdu[i]: continue
        # find next 5..21 bars where close > prior 21d high
        for k in range(1, MDAYS + 1):
            if close_arr[i + k] > hi_arr[i + k - 1]:
                times.append(float(k))
                break
    # Now produce a rolling mean over trailing 252d of THESE times — emit at bar i+MDAYS where confirmation done
    out = np.full(n, np.nan)
    for i in range(MDAYS, n):
        start = max(0, i - YDAYS + 1)
        # collect VDU events whose breakout confirmed by bar i
        evs = []
        for k in range(start, i - MDAYS + 1):
            if not vdu[k]: continue
            for kk in range(1, MDAYS + 1):
                if k + kk > i: break
                if close_arr[k + kk] > hi_arr[k + kk - 1]:
                    evs.append(float(kk))
                    break
        if len(evs) > 0:
            out[i] = float(np.mean(evs))
    return pd.Series(out, index=close.index)


def f24_tnch_162_bars_since_last_vdu(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the most recent VDU event."""
    return _bars_since(f24_tnch_158_vdu_5d_indicator(high, low, close, volume).astype(bool))


# ============================================================
# Bucket C — Volatility Contraction Pattern (VCP) (163-169)
# ============================================================

def _vcp_pullback_depths(high: pd.Series, low: pd.Series, n_lookback: int = YDAYS, threshold: float = 0.03):
    """Identify recent pullback depths (peak-to-trough drops > threshold) within trailing window.
    Returns array of (peak_idx, trough_idx, depth_pct) tuples per bar. We compute the LAST 3 pullback depths."""
    n = len(high)
    high_arr = high.to_numpy(); low_arr = low.to_numpy()
    # For each bar i, walk back through trailing n_lookback bars and extract pullbacks
    out_depths = np.full((n, 3), np.nan)  # last 3 pullback depths (most recent at col 2)
    for i in range(n):
        start = max(0, i - n_lookback + 1)
        h_win = high_arr[start:i + 1]; l_win = low_arr[start:i + 1]
        if h_win.size < 10: continue
        # walking peak/trough extraction (simple)
        peaks = []; troughs = []; cur_peak = h_win[0]; cur_trough = l_win[0]; in_drop = False
        for j in range(1, len(h_win)):
            if h_win[j] > cur_peak * (1 + threshold):
                if in_drop:
                    troughs.append(cur_trough); peaks.append(cur_peak); in_drop = False
                cur_peak = h_win[j]; cur_trough = h_win[j]
            elif l_win[j] < cur_trough:
                cur_trough = l_win[j]; in_drop = True
        # close out
        if in_drop:
            troughs.append(cur_trough); peaks.append(cur_peak)
        if len(peaks) >= 1 and len(troughs) >= 1:
            pulls = []
            for p, t in zip(peaks[-3:], troughs[-3:]):
                if p > 0:
                    pulls.append((p - t) / p)
            for k, pv in enumerate(pulls[-3:]):
                out_depths[i, 3 - len(pulls[-3:]) + k] = pv
    return out_depths


def f24_tnch_163_vcp_indicator_3_contractions_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 3 successively smaller pullbacks in trailing 252d — classic VCP setup."""
    d = _vcp_pullback_depths(high, low, n_lookback=YDAYS, threshold=0.03)
    n = len(high); out = np.full(n, 0.0)
    for i in range(n):
        a, b, c = d[i, 0], d[i, 1], d[i, 2]
        if np.isnan(a) or np.isnan(b) or np.isnan(c): continue
        if a > b > c:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f24_tnch_164_vcp_compression_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Compression score: 1 - (c/a) where a is oldest of last 3 pullbacks, c is newest. High = strong contraction."""
    d = _vcp_pullback_depths(high, low, n_lookback=YDAYS, threshold=0.03)
    n = len(high); out = np.full(n, np.nan)
    for i in range(n):
        a, c = d[i, 0], d[i, 2]
        if np.isnan(a) or np.isnan(c) or a <= 0: continue
        out[i] = 1.0 - (c / a)
    return pd.Series(out, index=close.index)


def f24_tnch_165_vcp_pullback_depth_decay_slope_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear slope of the last 3 pullback depths (negative = contracting)."""
    d = _vcp_pullback_depths(high, low, n_lookback=YDAYS, threshold=0.03)
    n = len(high); out = np.full(n, np.nan)
    for i in range(n):
        vals = d[i]
        if np.isnan(vals).any(): continue
        x = np.array([0, 1, 2], dtype=float)
        xm = x.mean(); ym = vals.mean()
        den = ((x - xm) ** 2).sum()
        if den > 0:
            out[i] = float(((x - xm) * (vals - ym)).sum() / den)
    return pd.Series(out, index=close.index)


def f24_tnch_166_final_contraction_atr_ratio_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most recent VCP pullback depth normalized by current 21d ATR / close — final tightness."""
    d = _vcp_pullback_depths(high, low, n_lookback=YDAYS, threshold=0.03)
    atr = _atr(high, low, close, n=MDAYS)
    n = len(high); out = np.full(n, np.nan)
    atr_arr = atr.to_numpy(); close_arr = close.to_numpy()
    for i in range(n):
        c = d[i, 2]
        if np.isnan(c) or np.isnan(atr_arr[i]) or np.isnan(close_arr[i]) or close_arr[i] == 0: continue
        # convert c (pct depth) to abs price then to ATR units
        depth_abs = c * close_arr[i]
        if atr_arr[i] > 0:
            out[i] = float(depth_abs / atr_arr[i])
    return pd.Series(out, index=close.index)


def f24_tnch_167_vcp_base_duration_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the start of the VCP base (oldest of last 3 pullback peaks). Approximated as bars-since 252d-max-high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_max = (high == rmax) & high.notna()
    return _bars_since(is_max)


def f24_tnch_168_vcp_breakout_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VCP detected in last 21d AND today's close > prior 21d high — breakout from VCP base."""
    vcp = f24_tnch_163_vcp_indicator_3_contractions_252(high, low, close)
    vcp_recent = vcp.rolling(MDAYS, min_periods=1).max().fillna(0).astype(bool)
    hi21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (vcp_recent & (close > hi21)).astype(float)


def f24_tnch_169_vcp_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VCP detected AND today's close < prior 21d low (broke contraction floor)."""
    vcp = f24_tnch_163_vcp_indicator_3_contractions_252(high, low, close)
    vcp_recent = vcp.rolling(MDAYS, min_periods=1).max().fillna(0).astype(bool)
    lo21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    return (vcp_recent & (close < lo21)).astype(float)


# ============================================================
# Bucket D — Distribution day O'Neil rules (170-173)
# ============================================================

def _is_distribution_day_oneil(close, volume):
    """O'Neil distribution day: close < prior close AND volume > prior volume (institutional selling)."""
    return (close < close.shift(1)) & (volume > volume.shift(1))


def f24_tnch_170_distribution_day_count_oneil_25d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of O'Neil distribution days in trailing 25 bars (canonical O'Neil window)."""
    return _is_distribution_day_oneil(close, volume).astype(float).rolling(25, min_periods=10).sum()


def f24_tnch_171_distribution_day_count_oneil_active(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of ACTIVE (not yet erased) distribution days: dist day occurred in last 25d AND price hasn't risen 5%+
    from that day's close."""
    dd = _is_distribution_day_oneil(close, volume).to_numpy()
    close_arr = close.to_numpy(); n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        active = 0
        for k in range(max(0, i - 24), i + 1):
            if not dd[k]: continue
            c_dd = close_arr[k]
            if np.isnan(c_dd) or c_dd <= 0: continue
            # check if any subsequent bar's close >= 1.05 * c_dd by bar i
            window = close_arr[k + 1:i + 1]
            if window.size > 0 and np.any(window >= 1.05 * c_dd):
                continue
            active += 1
        out[i] = float(active)
    return pd.Series(out, index=close.index)


def f24_tnch_172_consecutive_distribution_days_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak of consecutive O'Neil distribution days."""
    return _streak(_is_distribution_day_oneil(close, volume).fillna(False))


def f24_tnch_173_distribution_day_cluster_count_oneil_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-day CLUSTERS in last 252d (5+ dist days in any rolling 21d window)."""
    dd_cnt_21 = _is_distribution_day_oneil(close, volume).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    cluster = (dd_cnt_21 >= 5).astype(float)
    return cluster.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket E — Pre-breakout setups (174-178)
# ============================================================

def f24_tnch_174_pre_breakout_volume_buildup_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5d-mean volume on the day BEFORE a breakout (close > 21d high). Lagged value."""
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    vz = _rolling_zscore(v5, YDAYS, min_periods=QDAYS)
    hi21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    breakout = (close > hi21)
    return vz.shift(1).where(breakout, np.nan).ffill()


def f24_tnch_175_atr_compression_before_breakout_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: breakout today (close > 21d high) AND prior 5d ATR < 70% of trailing 63d median ATR."""
    atr5 = _atr(high, low, close, n=WDAYS)
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_median_63 = atr21.rolling(QDAYS, min_periods=MDAYS).median()
    compressed = (atr5.shift(1) < 0.7 * atr_median_63.shift(1))
    hi21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return ((close > hi21) & compressed).astype(float)


def f24_tnch_176_tight_base_indicator_252(close: pd.Series) -> pd.Series:
    """Indicator: 21d (max_close - min_close)/mean_close < 1% — extremely tight base (Minervini-style)."""
    cmax = close.rolling(MDAYS, min_periods=WDAYS).max()
    cmin = close.rolling(MDAYS, min_periods=WDAYS).min()
    cmean = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(cmax - cmin, cmean) < 0.01).astype(float)


def f24_tnch_177_handle_pattern_indicator_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Handle pattern: small pullback (5-15%) over 5-10 bars following a 21-63d cup-shaped base (recovery to within 5% of 252d high)."""
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = close >= 0.95 * rmax252
    pullback = (close.rolling(WDAYS, min_periods=WDAYS).min() <= 0.95 * close.rolling(MDAYS, min_periods=WDAYS).max())
    return (near_high & pullback).astype(float)


def f24_tnch_178_cup_with_handle_indicator_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cup-with-handle: in last 252d, price dropped 12-33% then recovered to within 5% of pre-drop high AND a recent handle is present."""
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    cup_depth = _safe_div(rmax252 - rmin252, rmax252)
    cup_ok = (cup_depth >= 0.12) & (cup_depth <= 0.33)
    recovered = close >= 0.95 * rmax252
    handle = f24_tnch_177_handle_pattern_indicator_252(high, low, close).astype(bool)
    return (cup_ok & recovered & handle).astype(float)


# ============================================================
# Bucket F — Effective Volume (Pascal Willain) (179-182)
# ============================================================

def _effective_volume_bar(high, low, close, volume):
    """Effective volume per bar: volume × close-position-in-range (a proxy for 'smart money'-aligned volume)."""
    pos = _safe_div(close - low, high - low)
    return volume * pos


def f24_tnch_179_effective_volume_session(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Effective volume = volume × close-position-in-range (single bar)."""
    return _effective_volume_bar(high, low, close, volume)


def f24_tnch_180_effective_volume_cumulative_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative effective volume over trailing 63d."""
    return _effective_volume_bar(high, low, close, volume).rolling(QDAYS, min_periods=MDAYS).sum()


def f24_tnch_181_effective_volume_slope_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d linear slope of effective volume — trend in 'smart money'."""
    return _rolling_slope(_effective_volume_bar(high, low, close, volume), QDAYS, min_periods=MDAYS)


def f24_tnch_182_effective_volume_divergence_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Divergence: price new 63d high AND cum-effective-volume below prior 63d max."""
    cev = _effective_volume_bar(high, low, close, volume).rolling(QDAYS, min_periods=MDAYS).sum()
    p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
    p_at_high = close >= p_max
    cev_prev_max = cev.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_at_high & (cev < cev_prev_max)).astype(float)


# ============================================================
# Bucket G — Trin (Arms Index) proxy (183-186)
# ============================================================

def f24_tnch_183_trin_proxy_close_strength_volume_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Single-stock Trin proxy: (sum down-day volume in 21d) / (sum up-day volume in 21d).
    >1 = distribution bias, <1 = accumulation bias."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    dn_vol = volume.where(close < close.shift(1), 0.0)
    up_sum = up_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    dn_sum = dn_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn_sum, up_sum)


def f24_tnch_184_trin_proxy_zscore_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of Trin proxy vs 252d distribution."""
    return _rolling_zscore(f24_tnch_183_trin_proxy_close_strength_volume_21(close, volume), YDAYS, min_periods=QDAYS)


def f24_tnch_185_trin_proxy_extreme_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: Trin proxy z-score > 2.0 — extreme distribution bias (capitulation or top-of-bounce)."""
    return (f24_tnch_184_trin_proxy_zscore_252(close, volume) > 2.0).astype(float)


def f24_tnch_186_arms_box_score_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trin proxy times close-direction sign — directional Arms strength."""
    trin = f24_tnch_183_trin_proxy_close_strength_volume_21(close, volume)
    return trin * np.sign(close - close.shift(MDAYS))


# ============================================================
# Bucket H — Volume profile VAH/VAL proxies (187-193)
# ============================================================

def f24_tnch_187_volume_at_close_concentration_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252d volume occurring on bars whose close was within ±2.5% of current close."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        c = close_arr[i]
        if np.isnan(c) or c == 0: continue
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        tot = win_v[m].sum()
        if tot == 0: continue
        near = win_v[m & (np.abs(win_c - c) <= 0.025 * c)].sum()
        out[i] = float(near / tot)
    return pd.Series(out, index=close.index)


def f24_tnch_188_distance_to_high_volume_node_log_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance from current close to the close of the single highest-volume bar in last 252d (HVN)."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        idx = int(np.argmax(np.where(m, win_v, -np.inf)))
        hvn = win_c[idx]; c = close_arr[i]
        if np.isnan(hvn) or np.isnan(c) or hvn <= 0 or c <= 0: continue
        out[i] = float(np.log(c) - np.log(hvn))
    return pd.Series(out, index=close.index)


def f24_tnch_189_high_volume_node_below_close_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in last 252d where close was below current close AND volume in top 10% of 252d distribution — support stack."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        c = close_arr[i]
        if np.isnan(c): continue
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if m.sum() < 20: continue
        vol_q90 = float(np.quantile(win_v[m], 0.9))
        out[i] = float(((win_v >= vol_q90) & (win_c < c) & m).sum())
    return pd.Series(out, index=close.index)


def f24_tnch_190_high_volume_node_above_close_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HVN ABOVE close — overhead supply count in 252d."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        c = close_arr[i]
        if np.isnan(c): continue
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if m.sum() < 20: continue
        vol_q90 = float(np.quantile(win_v[m], 0.9))
        out[i] = float(((win_v >= vol_q90) & (win_c > c) & m).sum())
    return pd.Series(out, index=close.index)


def f24_tnch_191_volume_profile_skew_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Skewness of volume-weighted close distribution over last 252d — asymmetry of volume vs price."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v) & (win_v > 0)
        if m.sum() < 20: continue
        wc = win_c[m]; wv = win_v[m]
        mu = (wc * wv).sum() / wv.sum()
        var = ((wc - mu) ** 2 * wv).sum() / wv.sum()
        if var <= 0: continue
        m3 = ((wc - mu) ** 3 * wv).sum() / wv.sum()
        out[i] = float(m3 / (var ** 1.5))
    return pd.Series(out, index=close.index)


def f24_tnch_192_volume_profile_value_area_width_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of the 70% volume zone (value area) in log-price units over last 252d."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v) & (win_v > 0) & (win_c > 0)
        if m.sum() < 20: continue
        # sort by close, take cumulative volume, find 15th and 85th percentile prices by volume
        order = np.argsort(win_c[m])
        sorted_c = win_c[m][order]; sorted_v = win_v[m][order]
        cum = np.cumsum(sorted_v); total = cum[-1]
        if total == 0: continue
        cum_pct = cum / total
        lo_idx = np.searchsorted(cum_pct, 0.15); hi_idx = np.searchsorted(cum_pct, 0.85)
        if lo_idx >= len(sorted_c): lo_idx = len(sorted_c) - 1
        if hi_idx >= len(sorted_c): hi_idx = len(sorted_c) - 1
        out[i] = float(np.log(sorted_c[hi_idx]) - np.log(sorted_c[lo_idx]))
    return pd.Series(out, index=close.index)


def f24_tnch_193_price_position_in_value_area_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Position of current close in value area (0=at VAL/low edge, 1=at VAH/high edge, >1=above VAH)."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v) & (win_v > 0) & (win_c > 0)
        if m.sum() < 20: continue
        order = np.argsort(win_c[m])
        sorted_c = win_c[m][order]; sorted_v = win_v[m][order]
        cum = np.cumsum(sorted_v); total = cum[-1]
        if total == 0: continue
        cum_pct = cum / total
        lo_idx = min(np.searchsorted(cum_pct, 0.15), len(sorted_c) - 1)
        hi_idx = min(np.searchsorted(cum_pct, 0.85), len(sorted_c) - 1)
        val_lo = sorted_c[lo_idx]; val_hi = sorted_c[hi_idx]
        c = close_arr[i]
        if val_hi - val_lo == 0 or np.isnan(c): continue
        out[i] = float((c - val_lo) / (val_hi - val_lo))
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket I — Sequential consolidation indicators (194-198)
# ============================================================

def _nr7(high, low):
    """NR7: today's range is the smallest in trailing 7 bars."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    return (rng == rmin7) & rng.notna()


def f24_tnch_194_nr7_nr7_consecutive_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: NR7 today AND NR7 yesterday — double-tight consolidation."""
    nr7 = _nr7(high, low)
    return (nr7 & nr7.shift(1).fillna(False)).astype(float)


def f24_tnch_195_nr7_inside_bar_combo_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NR7 AND inside-bar same bar — strongest single-bar consolidation signal."""
    nr7 = _nr7(high, low)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (nr7 & inside).astype(float)


def f24_tnch_196_sequential_inside_bar_run_max_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of consecutive inside bars in trailing 252d."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).fillna(False)
    return _streak(inside).rolling(YDAYS, min_periods=QDAYS).max()


def f24_tnch_197_consecutive_nr_run_max_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run in 252d where each bar is either NR4 or NR7 (NR4 = smallest range in 4 bars)."""
    rng = high - low
    rmin4 = rng.rolling(4, min_periods=4).min()
    rmin7 = rng.rolling(7, min_periods=7).min()
    is_nr = ((rng == rmin4) | (rng == rmin7)) & rng.notna()
    return _streak(is_nr.fillna(False)).rolling(YDAYS, min_periods=QDAYS).max()


def f24_tnch_198_consolidation_density_index_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Density of consolidation bars (NR7 + inside) in last 63d / 63 — high = trapped/coiled regime."""
    nr7 = _nr7(high, low).astype(float)
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return (nr7 + inside).rolling(QDAYS, min_periods=MDAYS).sum() / float(QDAYS)


# ============================================================
# Bucket J — Wide-range bar with weak / strong close (199-202)
# ============================================================

def f24_tnch_199_wide_range_weak_close_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: range > 2 × ATR21 AND close position in range <= 0.3 — wide-range bearish bar."""
    rng = high - low
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    return (((rng / atr) > 2.0) & (pos <= 0.3)).astype(float)


def f24_tnch_200_count_wide_range_weak_close_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of wide-range-weak-close events in trailing 252d."""
    return f24_tnch_199_wide_range_weak_close_indicator(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_201_wide_range_strong_close_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of wide-range bars (range > 2 × ATR21) with close position >= 0.7 in trailing 252d."""
    rng = high - low
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    return ((((rng / atr) > 2.0) & (pos >= 0.7)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum())


def f24_tnch_202_wrb_close_strength_imbalance_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Strong-close WRB count minus weak-close WRB count in 252d — directional regime."""
    return f24_tnch_201_wide_range_strong_close_count_252(high, low, close) - f24_tnch_200_count_wide_range_weak_close_252(high, low, close)


# ============================================================
# Bucket K — Volatility expansion / regime events (203-207)
# ============================================================

def f24_tnch_203_atr_expansion_1to2_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR21 today >= 2 × ATR21 5 bars ago — vol-doubling event."""
    atr21 = _atr(high, low, close, n=MDAYS)
    return (atr21 >= 2.0 * atr21.shift(WDAYS)).astype(float)


def f24_tnch_204_atr_expansion_event_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR doubling events in 252d."""
    return f24_tnch_203_atr_expansion_1to2_event_indicator(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_205_atr_regime_shift_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's ATR21 is above 252d median AND yesterday's was below — first-cross regime shift."""
    atr21 = _atr(high, low, close, n=MDAYS)
    med252 = atr21.rolling(YDAYS, min_periods=QDAYS).median()
    today_above = atr21 > med252
    yest_below = atr21.shift(1) <= med252.shift(1)
    return (today_above & yest_below).astype(float)


def f24_tnch_206_range_expansion_zscore_with_close_pos_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of range × signed-close-position (positive = range expansion with bullish close, negative = bearish)."""
    rng = high - low
    pos = _safe_div(close - low, high - low) * 2.0 - 1.0  # rescale 0..1 → -1..+1
    signed = rng * pos
    return _rolling_zscore(signed, YDAYS, min_periods=QDAYS)


def f24_tnch_207_volatility_regime_classifier_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Categorical: 0=quiet (ATR < 50%ile of 252d), 1=normal (50-75%ile), 2=expanding (75-90%), 3=extreme (>90%ile)."""
    atr21 = _atr(high, low, close, n=MDAYS)
    n = len(close); arr = atr21.to_numpy(); out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = arr[start:i + 1]; win = win[~np.isnan(win)]
        if win.size < 20 or np.isnan(arr[i]): continue
        rk = float((win <= arr[i]).sum()) / float(win.size)
        if rk < 0.5: out[i] = 0
        elif rk < 0.75: out[i] = 1
        elif rk < 0.9: out[i] = 2
        else: out[i] = 3
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket L — Volume cascade & follow-through (208-213)
# ============================================================

def f24_tnch_208_volume_cascade_after_wrb_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """For most recent WRB (range > 2 × ATR21) in last 63d: mean volume in next 5 bars after the WRB (PIT-safe via lag)."""
    rng = high - low; atr = _atr(high, low, close, n=MDAYS)
    wrb = ((rng / atr) > 2.0).fillna(False)
    bsu = _bars_since(wrb)
    n = len(close); bsu_arr = bsu.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        post = vol_arr[j + 1:j + 1 + WDAYS]
        if post.size > 0 and not np.all(np.isnan(post)):
            out[i] = float(np.nanmean(post))
    return pd.Series(out, index=close.index)


def f24_tnch_209_volume_cascade_decay_ratio_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (post-WRB-5d-volume / WRB-day-volume) ratios in 252d — typical post-event volume decay."""
    rng = high - low; atr = _atr(high, low, close, n=MDAYS)
    wrb_arr = (((rng / atr) > 2.0).fillna(False)).to_numpy()
    vol_arr = volume.to_numpy(); n = len(close)
    out = np.full(n, np.nan)
    for i in range(WDAYS + 1, n):
        ratios = []
        start = max(0, i - YDAYS)
        for k in range(start, i - WDAYS):
            if not wrb_arr[k]: continue
            v_event = vol_arr[k]
            if np.isnan(v_event) or v_event == 0: continue
            post = vol_arr[k + 1:k + 1 + WDAYS]
            if post.size > 0 and not np.all(np.isnan(post)):
                ratios.append(float(np.nanmean(post) / v_event))
        if len(ratios) > 0:
            out[i] = float(np.mean(ratios))
    return pd.Series(out, index=close.index)


def f24_tnch_210_silent_followthrough_indicator_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: close > close 5 bars ago AND 5d-mean volume < 21d-mean volume (price up on declining volume — suspect)."""
    return ((close > close.shift(WDAYS)) & (volume.rolling(WDAYS, min_periods=WDAYS).mean() < volume.rolling(MDAYS, min_periods=WDAYS).mean())).astype(float)


def f24_tnch_211_silent_followthrough_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of silent-followthrough events in 252d."""
    return f24_tnch_210_silent_followthrough_indicator_5d(close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_212_clear_followthrough_indicator_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: close > close 5d ago AND 5d-mean vol > 21d-mean vol (price up on rising volume — confirmed)."""
    return ((close > close.shift(WDAYS)) & (volume.rolling(WDAYS, min_periods=WDAYS).mean() > volume.rolling(MDAYS, min_periods=WDAYS).mean())).astype(float)


def f24_tnch_213_clear_followthrough_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of clear-followthrough events in 252d."""
    return f24_tnch_212_clear_followthrough_indicator_5d(close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Composite scores (214-225)
# ============================================================

def f24_tnch_214_distribution_phase_top_composite_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top composite: O'Neil dist day count (25d) + lack of pocket pivots (252d=0 OR <2) + weak close fraction."""
    dd = f24_tnch_170_distribution_day_count_oneil_25d(close, volume).fillna(0)
    pp = f24_tnch_154_pocket_pivot_count_252(close, volume).fillna(0)
    no_pp = (pp < 2).astype(float)
    return dd + 3.0 * no_pp


def f24_tnch_215_accumulation_phase_bottom_composite_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bottom composite: pocket pivots present + low distribution count + tight base."""
    pp = f24_tnch_154_pocket_pivot_count_252(close, volume).fillna(0)
    dd = f24_tnch_170_distribution_day_count_oneil_25d(close, volume).fillna(0)
    low_dd = (dd <= 1).astype(float)
    tb = f24_tnch_176_tight_base_indicator_252(close).fillna(0)
    return pp + 2.0 * low_dd + 3.0 * tb


def f24_tnch_216_tnch_terminal_top_score_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal-top: dist-cluster + WRB-weak + climax + silent-followthrough."""
    dd_cl = f24_tnch_173_distribution_day_cluster_count_oneil_252(close, volume).fillna(0)
    wrb_weak = f24_tnch_200_count_wide_range_weak_close_252(high, low, close).fillna(0)
    silent = f24_tnch_211_silent_followthrough_count_252(close, volume).fillna(0)
    return dd_cl + wrb_weak + 0.5 * silent


def f24_tnch_217_tnch_capitulation_bottom_score_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation-bottom: volume spike at low + WRB with strong close + clear followthrough."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    rmin252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    at_low = (close <= 1.05 * rmin252).astype(float)
    spike_at_low = ((vz > 2.0) & (at_low.astype(bool))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    wrb_strong = f24_tnch_201_wide_range_strong_close_count_252(high, low, close).fillna(0)
    clear = f24_tnch_213_clear_followthrough_count_252(close, volume).fillna(0)
    return spike_at_low + wrb_strong + 0.5 * clear


def f24_tnch_218_volume_climax_with_doji_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: volume z > 2.0 AND body / range < 0.2 (doji with extreme volume — reversal candle)."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    body = (close - close.shift(1)).abs()
    rng = high - low
    return ((vz > 2.0) & (_safe_div(body, rng) < 0.2)).astype(float)


def f24_tnch_219_volume_climax_with_doji_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-climax-doji events in 252d."""
    return f24_tnch_218_volume_climax_with_doji_indicator(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


def f24_tnch_220_volume_compression_explosion_pattern_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pattern: 5d-mean volume in last 21d was in bottom decile of 252d distribution AND today volume z > 2.0."""
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    v5_min_21 = v5.rolling(MDAYS, min_periods=WDAYS).min()
    def _pct_rank(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    pct = v5_min_21.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank, raw=True)
    compressed = pct <= 0.1
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return (compressed & (vz > 2.0)).astype(float)


def f24_tnch_221_churn_to_breakout_pattern_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pattern: consolidation density > 0.4 in last 21d AND close today > 21d high — churn-then-breakout."""
    nr7 = _nr7(high, low).astype(float)
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    density = (nr7 + inside).rolling(MDAYS, min_periods=WDAYS).sum() / float(MDAYS)
    hi21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return ((density > 0.4) & (close > hi21)).astype(float)


def f24_tnch_222_churn_to_breakdown_pattern_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pattern: consolidation density > 0.4 in 21d AND close today < 21d low — churn-then-breakdown."""
    nr7 = _nr7(high, low).astype(float)
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    density = (nr7 + inside).rolling(MDAYS, min_periods=WDAYS).sum() / float(MDAYS)
    lo21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    return ((density > 0.4) & (close < lo21)).astype(float)


def f24_tnch_223_multi_horizon_churn_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: NR7-density > 0.3 across all of {21d, 63d, 252d} windows simultaneously — sustained tight regime."""
    nr7 = _nr7(high, low).astype(float)
    d21 = nr7.rolling(MDAYS, min_periods=WDAYS).mean()
    d63 = nr7.rolling(QDAYS, min_periods=MDAYS).mean()
    d252 = nr7.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((d21 > 0.3) & (d63 > 0.3) & (d252 > 0.3)).astype(float)


def f24_tnch_224_multi_horizon_expansion_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR21 > 252d median AND ATR63 > 252d median AND ATR252 rising — sustained expansion regime."""
    atr21 = _atr(high, low, close, n=MDAYS); atr63 = _atr(high, low, close, n=QDAYS); atr252 = _atr(high, low, close, n=YDAYS)
    med252 = atr21.rolling(YDAYS, min_periods=QDAYS).median()
    return ((atr21 > med252) & (atr63 > med252) & (atr252 > atr252.shift(MDAYS))).astype(float)


def f24_tnch_225_tnch_regime_top_signature_weighted(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final weighted top signature: 3 × terminal_top + 2 × dist_phase_top + 1 × volume_climax_doji_count + 1 × WRB_weak_close_count."""
    a = f24_tnch_216_tnch_terminal_top_score_252(high, low, close, volume).fillna(0)
    b = f24_tnch_214_distribution_phase_top_composite_252(close, volume).fillna(0)
    c = f24_tnch_219_volume_climax_with_doji_count_252(high, low, close, volume).fillna(0)
    d = f24_tnch_200_count_wide_range_weak_close_252(high, low, close).fillna(0)
    return 3.0 * a + 2.0 * b + c + d


# ============================================================
#                         REGISTRY 151-225
# ============================================================

TURNOVER_AND_CHURN_BASE_REGISTRY_151_225 = {
    "f24_tnch_151_pocket_pivot_indicator": {"inputs": ["close", "volume"], "func": f24_tnch_151_pocket_pivot_indicator},
    "f24_tnch_152_pocket_pivot_count_21": {"inputs": ["close", "volume"], "func": f24_tnch_152_pocket_pivot_count_21},
    "f24_tnch_153_pocket_pivot_count_63": {"inputs": ["close", "volume"], "func": f24_tnch_153_pocket_pivot_count_63},
    "f24_tnch_154_pocket_pivot_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_154_pocket_pivot_count_252},
    "f24_tnch_155_bars_since_last_pocket_pivot": {"inputs": ["close", "volume"], "func": f24_tnch_155_bars_since_last_pocket_pivot},
    "f24_tnch_156_pocket_pivot_at_or_above_50d_sma_indicator": {"inputs": ["close", "volume"], "func": f24_tnch_156_pocket_pivot_at_or_above_50d_sma_indicator},
    "f24_tnch_157_pocket_pivot_with_followthrough_5d_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_157_pocket_pivot_with_followthrough_5d_count_252},
    "f24_tnch_158_vdu_5d_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_158_vdu_5d_indicator},
    "f24_tnch_159_vdu_5d_count_63": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_159_vdu_5d_count_63},
    "f24_tnch_160_vdu_followed_by_pocket_pivot_count_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_160_vdu_followed_by_pocket_pivot_count_252},
    "f24_tnch_161_vdu_to_breakout_velocity_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_161_vdu_to_breakout_velocity_252},
    "f24_tnch_162_bars_since_last_vdu": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_162_bars_since_last_vdu},
    "f24_tnch_163_vcp_indicator_3_contractions_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_163_vcp_indicator_3_contractions_252},
    "f24_tnch_164_vcp_compression_score_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_164_vcp_compression_score_252},
    "f24_tnch_165_vcp_pullback_depth_decay_slope_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_165_vcp_pullback_depth_decay_slope_252},
    "f24_tnch_166_final_contraction_atr_ratio_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_166_final_contraction_atr_ratio_252},
    "f24_tnch_167_vcp_base_duration_days": {"inputs": ["high", "low", "close"], "func": f24_tnch_167_vcp_base_duration_days},
    "f24_tnch_168_vcp_breakout_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_168_vcp_breakout_indicator},
    "f24_tnch_169_vcp_failure_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_169_vcp_failure_indicator},
    "f24_tnch_170_distribution_day_count_oneil_25d": {"inputs": ["close", "volume"], "func": f24_tnch_170_distribution_day_count_oneil_25d},
    "f24_tnch_171_distribution_day_count_oneil_active": {"inputs": ["close", "volume"], "func": f24_tnch_171_distribution_day_count_oneil_active},
    "f24_tnch_172_consecutive_distribution_days_streak": {"inputs": ["close", "volume"], "func": f24_tnch_172_consecutive_distribution_days_streak},
    "f24_tnch_173_distribution_day_cluster_count_oneil_252": {"inputs": ["close", "volume"], "func": f24_tnch_173_distribution_day_cluster_count_oneil_252},
    "f24_tnch_174_pre_breakout_volume_buildup_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_174_pre_breakout_volume_buildup_zscore_5d},
    "f24_tnch_175_atr_compression_before_breakout_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_175_atr_compression_before_breakout_indicator},
    "f24_tnch_176_tight_base_indicator_252": {"inputs": ["close"], "func": f24_tnch_176_tight_base_indicator_252},
    "f24_tnch_177_handle_pattern_indicator_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_177_handle_pattern_indicator_252},
    "f24_tnch_178_cup_with_handle_indicator_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_178_cup_with_handle_indicator_252},
    "f24_tnch_179_effective_volume_session": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_179_effective_volume_session},
    "f24_tnch_180_effective_volume_cumulative_63": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_180_effective_volume_cumulative_63},
    "f24_tnch_181_effective_volume_slope_63": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_181_effective_volume_slope_63},
    "f24_tnch_182_effective_volume_divergence_63": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_182_effective_volume_divergence_63},
    "f24_tnch_183_trin_proxy_close_strength_volume_21": {"inputs": ["close", "volume"], "func": f24_tnch_183_trin_proxy_close_strength_volume_21},
    "f24_tnch_184_trin_proxy_zscore_252": {"inputs": ["close", "volume"], "func": f24_tnch_184_trin_proxy_zscore_252},
    "f24_tnch_185_trin_proxy_extreme_high_indicator": {"inputs": ["close", "volume"], "func": f24_tnch_185_trin_proxy_extreme_high_indicator},
    "f24_tnch_186_arms_box_score_252": {"inputs": ["close", "volume"], "func": f24_tnch_186_arms_box_score_252},
    "f24_tnch_187_volume_at_close_concentration_252": {"inputs": ["close", "volume"], "func": f24_tnch_187_volume_at_close_concentration_252},
    "f24_tnch_188_distance_to_high_volume_node_log_252": {"inputs": ["close", "volume"], "func": f24_tnch_188_distance_to_high_volume_node_log_252},
    "f24_tnch_189_high_volume_node_below_close_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_189_high_volume_node_below_close_count_252},
    "f24_tnch_190_high_volume_node_above_close_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_190_high_volume_node_above_close_count_252},
    "f24_tnch_191_volume_profile_skew_252": {"inputs": ["close", "volume"], "func": f24_tnch_191_volume_profile_skew_252},
    "f24_tnch_192_volume_profile_value_area_width_252": {"inputs": ["close", "volume"], "func": f24_tnch_192_volume_profile_value_area_width_252},
    "f24_tnch_193_price_position_in_value_area_252": {"inputs": ["close", "volume"], "func": f24_tnch_193_price_position_in_value_area_252},
    "f24_tnch_194_nr7_nr7_consecutive_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_194_nr7_nr7_consecutive_indicator},
    "f24_tnch_195_nr7_inside_bar_combo_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_195_nr7_inside_bar_combo_indicator},
    "f24_tnch_196_sequential_inside_bar_run_max_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_196_sequential_inside_bar_run_max_252},
    "f24_tnch_197_consecutive_nr_run_max_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_197_consecutive_nr_run_max_252},
    "f24_tnch_198_consolidation_density_index_63": {"inputs": ["high", "low", "close"], "func": f24_tnch_198_consolidation_density_index_63},
    "f24_tnch_199_wide_range_weak_close_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_199_wide_range_weak_close_indicator},
    "f24_tnch_200_count_wide_range_weak_close_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_200_count_wide_range_weak_close_252},
    "f24_tnch_201_wide_range_strong_close_count_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_201_wide_range_strong_close_count_252},
    "f24_tnch_202_wrb_close_strength_imbalance_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_202_wrb_close_strength_imbalance_252},
    "f24_tnch_203_atr_expansion_1to2_event_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_203_atr_expansion_1to2_event_indicator},
    "f24_tnch_204_atr_expansion_event_count_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_204_atr_expansion_event_count_252},
    "f24_tnch_205_atr_regime_shift_indicator": {"inputs": ["high", "low", "close"], "func": f24_tnch_205_atr_regime_shift_indicator},
    "f24_tnch_206_range_expansion_zscore_with_close_pos_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_206_range_expansion_zscore_with_close_pos_252},
    "f24_tnch_207_volatility_regime_classifier_252": {"inputs": ["high", "low", "close"], "func": f24_tnch_207_volatility_regime_classifier_252},
    "f24_tnch_208_volume_cascade_after_wrb_5d": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_208_volume_cascade_after_wrb_5d},
    "f24_tnch_209_volume_cascade_decay_ratio_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_209_volume_cascade_decay_ratio_252},
    "f24_tnch_210_silent_followthrough_indicator_5d": {"inputs": ["close", "volume"], "func": f24_tnch_210_silent_followthrough_indicator_5d},
    "f24_tnch_211_silent_followthrough_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_211_silent_followthrough_count_252},
    "f24_tnch_212_clear_followthrough_indicator_5d": {"inputs": ["close", "volume"], "func": f24_tnch_212_clear_followthrough_indicator_5d},
    "f24_tnch_213_clear_followthrough_count_252": {"inputs": ["close", "volume"], "func": f24_tnch_213_clear_followthrough_count_252},
    "f24_tnch_214_distribution_phase_top_composite_252": {"inputs": ["close", "volume"], "func": f24_tnch_214_distribution_phase_top_composite_252},
    "f24_tnch_215_accumulation_phase_bottom_composite_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_215_accumulation_phase_bottom_composite_252},
    "f24_tnch_216_tnch_terminal_top_score_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_216_tnch_terminal_top_score_252},
    "f24_tnch_217_tnch_capitulation_bottom_score_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_217_tnch_capitulation_bottom_score_252},
    "f24_tnch_218_volume_climax_with_doji_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_218_volume_climax_with_doji_indicator},
    "f24_tnch_219_volume_climax_with_doji_count_252": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_219_volume_climax_with_doji_count_252},
    "f24_tnch_220_volume_compression_explosion_pattern_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_220_volume_compression_explosion_pattern_indicator},
    "f24_tnch_221_churn_to_breakout_pattern_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_221_churn_to_breakout_pattern_indicator},
    "f24_tnch_222_churn_to_breakdown_pattern_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_222_churn_to_breakdown_pattern_indicator},
    "f24_tnch_223_multi_horizon_churn_consensus": {"inputs": ["high", "low", "close"], "func": f24_tnch_223_multi_horizon_churn_consensus},
    "f24_tnch_224_multi_horizon_expansion_consensus": {"inputs": ["high", "low", "close"], "func": f24_tnch_224_multi_horizon_expansion_consensus},
    "f24_tnch_225_tnch_regime_top_signature_weighted": {"inputs": ["high", "low", "close", "volume"], "func": f24_tnch_225_tnch_regime_top_signature_weighted},
}
